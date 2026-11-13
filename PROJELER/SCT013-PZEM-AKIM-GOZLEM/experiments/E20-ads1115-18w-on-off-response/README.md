# E20 — ADS1115 + SCT 18 W fiziksel aç/kapa tepki deneyi

- **Durum:** PLANLANDI — fiziksel çevrim kaydı henüz alınmadı.
- **Tarih:** 2026-11-13 tarihinde E19 18 W sabit yük gözlemi sonrasında açıldı.
- **İlişki:** E19 ADS1115 düşük akım karakterizasyonu; E20 bu ölçüm zincirinin fiziksel yük açma/kapatma tepkisini inceler.
- **Yük:** E19'da kullanılan 18 W nominal yük. PZEM'in ölçtüğü gerçek W/A değerleri esas kayıt olacaktır.
- **Ölçüm zinciri:** Aynı SCT-013 30A/1V + ADS1115 + ESP32D2; PZEM-004T V3.0 karşılaştırma kaynağı.

## Amaç

ADS1115 + SCT zincirinin 18 W yük fiziksel olarak açıldığında akım değişimini algılama, yük kapandığında yüksüz tabana dönme, geçişteki gecikme/sıçrama ve tekrarlanabilirlik davranışını incelemek.

E19'da 18 W sabit yükte ADS1115 ortalaması 0.078715 A, PZEM ortalaması 0.079500 A bulunmuştu (yaklaşık −%0.99). E20 bu sabit alan sonucunu yeniden kalibre etmez; yalnızca ON/OFF geçiş davranışını inceler.

## Fiziksel test düzeni

- Aynı SCT ve aynı ölçülen iletken/tur düzeni korunur.
- Aynı 18 W yük kullanılır; yükün fiziksel açma/kapatması operatör tarafından doğrulanabilen güvenli bir anahtarla yapılır.
- Şebeke kablosu kesme/ekleme veya açık iletkene müdahale yapılmaz. Anahtarlama yalnızca kapalı/izole edilmiş uygun anahtar veya cihazın kendi güvenli açma-kapama kumandasıyla yapılır.
- SSR/UDP olayları ayrıca kaydedilebilir; fakat fiziksel yük durumunun kanıtı sayılmaz. Önceki CSV'de SSR OFF olaylarından sonra PZEM'in yaklaşık 18 W göstermeyi sürdürmesi nedeniyle bu ayrım zorunludur.
- PZEM, her çevrimde fiziksel ON/OFF durumunu doğrulayan karşılaştırma akışı olarak kullanılır. PZEM akım/güç davranışı fiziksel geçişi doğrulamıyorsa o çevrim geçersiz/şüpheli olarak işaretlenir; SCT sonucu zorla ON/OFF etiketi almaz.

## Sabit tutulacak ölçüm ayarları

- ADS1115 I²C 0x48, differential A0_A1.
- Gain 2.048 V, sample rate 860 SPS, continuous mode.
- ct_clamp sample_duration 200 ms; update_interval 2 s.
- accuracy_decimals 2; mevcut 0.05 A filtresi.
- Kullanılan katsayı, firmware/YAML ve fiziksel SCT tur sayısı değiştirilmeyecek; gerçek çalışan yapı test başında kaydedilecek.
- Bu deneyde yeniden kalibrasyon, gain denemesi, filtre değişikliği veya yeni eşik tanımlaması yapılmayacak.

## Önerilen çevrim dizisi

Her durum için yeterli örnek toplayabilmek ve başlangıç/son yüksüz tabanını görmek üzere:

1. **Başlangıç OFF:** 180 saniye. PZEM'in yükün gerçekten kapalı olduğunu gösterdiği ve ADS tabanının kaydedildiği bölüm.
2. **Beş ON/OFF çevrimi:** Her ON 60 saniye, her OFF 60 saniye. Toplam 10 durum aralığı.
3. **Son OFF:** 180 saniye. Yükün kapandığı ve ADS'nin başlangıç yüksüz seviyesine dönüp dönmediği izlenir.

Bu zamanlar protokol önerisidir; kullanıcı fiziksel düzen veya kayıt kapasitesi nedeniyle değiştirmek isterse gerçek süreler test günlüğüne yazılır. ADS'nin 2 saniyelik yayın aralığında 60 saniyelik bir durum yaklaşık 30 güncelleme verir. Geçiş zaman çözünürlüğü bu yayın aralığıyla sınırlıdır; 200 ms örnek penceresi 200 ms yayın aralığı anlamına gelmez.

## Kayıt edilecek akışlar

- ADS1115 + SCT akım entity'si ve varsa Raw AC/ham ct_clamp debug çıktısı.
- PZEM akım, aktif güç ve gerilim.
- Gerçek operatör anahtarlama zamanları: fiziksel ON ve fiziksel OFF anları ayrı ayrı not edilir.
- SSR/UDP BOOT_ID, EVENT_ID, STATE olayları varsa ayrı akış olarak saklanır; fiziksel anahtarlama zamanının yerine geçmez.
- ESP32D2/Modül 3 çevrim içi durumu, yeniden başlama, I²C/ADS uyarıları ve örnek sayısı/SPS.
- Test başında ve sonunda firmware/YAML sürümü, gain, sample rate, sample_duration, update_interval, filtre, katsayı ve SCT tur sayısı.

## Analiz yöntemi

1. Ham CSV değiştirilmeden saklanır; dosya boyutu ve SHA-256 kaydedilir.
2. PZEM akım/güç zaman serisinden gerçek yük ON/OFF geçişleri belirlenir. Operatör anahtarlama notlarıyla karşılaştırılır.
3. Her çevrim için fiziksel geçiş zamanı, ADS'nin ilk belirgin değişim zamanı, ADS'nin ON kararlı banda yerleşme zamanı ve OFF sonrası yüksüz banda dönüş zamanı ayrı raporlanır.
4. ON/OFF kararlı seviyeleri için n, ortalama, medyan, SD, min–maks ve CV hesaplanır. Geçiş örnekleri kararlı pencere istatistiğine katılmaz.
5. Çevrimler arası ON seviyesi, OFF seviyesi ve gecikmelerin tekrarlanabilirliği karşılaştırılır.
6. ADS OFF seviyesi başlangıç OFF tabanına dönmüyorsa veya PZEM OFF'u doğrulamıyorsa sonuç açıkça belirsiz/başarısız çevrim olarak işaretlenir.
7. Eğitim etiketi veya kalibrasyon katsayısı üretilmez. Ham zaman serisi ve olay akışları korunur.

## Önceden belirlenmiş karar ölçütleri

- **Fiziksel çevrim doğrulaması:** PZEM akım ve aktif güç ON'da yük seviyesine yükselmeli, OFF'ta yüksüz tabana dönmelidir. Eşik, mevcut PZEM yüksüz taban kaydı görüldükten sonra raporda tanımlanır; önceden uydurulmaz.
- **Algılama:** ADS akım serisi ON ve OFF dönemlerini ayırt edilebilir biçimde göstermeli.
- **Geri dönüş:** Her OFF sonrasında ADS seviyesi başlangıç OFF dağılımıyla karşılaştırılmalı; tek bir 0.00 A yayını şart koşulmaz.
- **Tekrarlanabilirlik:** Beş çevrim ayrı ayrı raporlanır; yalnız genel ortalama üzerinden başarım kararı verilmez.
- **Zamanlama:** ADS yayın çözünürlüğü 2 saniyedir. Bu nedenle alt-saniye tepki süresi iddia edilmeyecek; gözlenen gecikme bu örnekleme/yayın sınırıyla birlikte raporlanacaktır.
- **±%4:** E20 bir dinamik aç/kapa testi olduğundan geçiş örneklerine ±%4 doğruluk kriteri uygulanmaz. Kararlı ON bölümü E19 18 W sonucu ile betimleyici olarak karşılaştırılabilir; yeni bir kalibrasyon/kabul kararı değildir.

## Başarısız/şüpheli çevrim koşulları

- Operatör anahtarlama yaptı ancak PZEM fiziksel yük değişimini doğrulamadı.
- PZEM veya ADS kayıt akışında çevrimi değerlendirmeye yetecek veri boşluğu oluştu.
- Cihaz yeniden başladı, ayarlar değişti veya ADS/PZEM ölçüm akışı kesildi.
- OFF komutu/UDP olayı var ancak PZEM yükün sürdüğünü gösteriyor.

Bu çevrimler silinmez; ham kayıtta tutulur ve analizde ayrı işaretlenir.

## Güvenlik ve açık ön koşul

ADS1115 A0/A1 giriş ortak-mod seviyesi ve GND–VDD giriş ray sınırlarının fiziksel doğrulaması E19'dan devralınan açık konudur. Bu doğrulama yapılmadan enerjili bağlantı güvenli kabul edilmez. SCT yalnız yalıtılmış tek iletkeni çevreler; faz ve nötr birlikte CT içinden geçirilmez.

## Sonuç

Henüz test yapılmadı. Bu dosya yalnız E20 deney tasarımını ve önceden belirlenmiş analiz/karar kurallarını tanımlar.
