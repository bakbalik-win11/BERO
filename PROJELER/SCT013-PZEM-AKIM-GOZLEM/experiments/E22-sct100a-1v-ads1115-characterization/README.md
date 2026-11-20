# E22 — SCT 100 A / 1 V + ADS1115 karakterizasyonu

## Durum

**PLANLANDI.** Bu belge deney planıdır; firmware hazırlanmış, derlenmiş, OTA edilmiş veya fiziksel deney yapılmış değildir.

## Amaç ve test düzeneği kimliği

Eldeki 100 A / 1 V akım trafosunun ADS1115 tabanlı ölçüm zinciriyle hangi akım aralığında kullanılabilir olduğunu incelemek. Bu deney, çamaşır/bulaşık cihaz modüllerinden bağımsız bir **100 A / 1 V SCT karakterizasyon düzeneğidir**. Deney için ayrı firmware snapshot'ı ve ayrı kalibrasyon/sonuç kaydı tutulur; cihaz modül numarası kullanılmaz. 30 A / 1 V sensörün mevcut kodu ve katsayısı korunur; 100 A / 1 V için ayrı firmware snapshot'ı ve ayrı kalibrasyon/sonuç kaydı tutulur.

### Tarihsel Modül 1–3 durumu

- **Modül 1:** bağımsız bias trafosu/güç kutusu — KALACAK.
- **Modül 2:** üç kanallı biaslı SCT okuma; Modül 1'in bias yapısını da içeren eski modül — kullanıcı bildirimiyle İMHA EDİLDİ.
- **Modül 3:** PZEM + aç/kapa rölesi içeren eski modül — kullanıcı bildirimiyle İMHA EDİLDİ. Eski röle/kontrol yapısı bu karakterizasyon düzeneğine taşınmayacak.

Modül 2/3 firmware ve dokümanları depodan silinmez; tarihsel arşiv olarak korunur. Modül 3'ün eski modül olarak imha edilmesi tarihsel kayıttır. PZEM-004T V3'ün bu karakterizasyon düzeneğinde kullanılması düşünülürse fiziksel durumu ve yeniden bağlantısı test öncesinde teyit edilecektir.

## Kullanıcı kararı ve stok bilgisi

- Kullanıcı bildirimi: **8 adet 100 A / 1 V SCT** mevcut.
- Kullanıcı değerlendirmesi: 30 A / 1 V sensör mevcut kullanım noktalarının çoğu için yeterli; 100 A / 1 V sensörler ileride ana hat gibi daha yüksek akım aralığı beklenen noktalarda değerlendirilebilir.
- Stok adedi ve sensörün tam model/etiketi fiziksel kontrolle teyit edilecek.

## Teknik beklenti

100 A / 1 V sensörün nominal duyarlılığı 30 A / 1 V sensöre göre daha düşüktür. İdeal nominal oranlar üzerinden:

- 30 A / 1 V: 1 V / 30 A ≈ 33,3 mV/A
- 100 A / 1 V: 1 V / 100 A = 10 mV/A

Bu nedenle 100 A / 1 V sensörün düşük akım ölçümünü iyileştirdiği varsayılmayacak. Deneyin ana gerekçesi daha yüksek akım aralığında kullanım ve ADC girişinde yeterli ölçüm payı (headroom) olup olmadığını görmektir. Gerçek sensör davranışı üretici etiketi/datasheet ve ölçümle teyit edilecek.

## Ayrı kod ilkesi

Planlanan dosya:

`firmware/characterization-ads1115-sct100a-1v-pzem.yaml`

Bu adlandırma taslak yoludur; ESP32 kart modeli ve cihaz adı donanım kontrolünde kesinleştirilecektir.

- Bu dosya karakterizasyon düzeneği için sıfırdan/ayrı bir firmware kimliğiyle hazırlanacak; eski Modül 2 veya Modül 3 kodu doğrudan kopyalanmayacak. Mevcut ADS1115 ölçüm ayarları yalnız teknik referans olarak incelenecek.
- 30 A / 1 V canlı YAML'ı değiştirilmeyecek.
- Sensör modeli ve katsayı açıkça 100 A / 1 V olarak adlandırılacak.
- 30 A / 1 V kalibrasyon katsayısı kopyalanmayacak.
- PZEM-004T V3'ün aynı ESP32 tarafından okunması planlanır. PZEM UART pinleri/baud ve ADS1115 I²C pinleri kart üzerinde doğrulanmadan YAML sabitlenmeyecek.
- Test öncesi YAML'da ADS1115 gain, sample rate, ct_clamp penceresi, update interval, analog giriş bağlantısı, PZEM seri haberleşmesi ve güvenlik sınırları yeniden kontrol edilecek.
- Kod, derleme çıktısı, OTA logu, gerçek ölçüm logu ve sonuç yorumu aynı deney klasörü/ilgili log klasöründe birbirine bağlanacak.

## Karakterizasyon düzeneğinin ilk test sınırı

- İlk sürüm tek ESP32 üzerinde ADS1115 ve PZEM-004T V3 okumayı hedefler.
- Harici bias trafosu karakterizasyon düzeneğine otomatik olarak dahil edilmeyecek; Modül 1 bağımsız ve korunmuş donanım olarak kalır. ADS1115 girişinin gerekli ortak-mod/bias düzeni devre tasarımı ve ölçümle ayrıca doğrulanır.
- Eski Modül 2'nin üç kanal okuma düzeni ve Modül 3'ün aç/kapa röle/UDP olay mantığı bu karakterizasyon düzeneğinin kapsamına taşınmaz.
- İlk testte kanal sayısı, pinler ve yayın aralığı ancak fiziksel kart/bağlantı doğrulamasından sonra kesinleştirilir.

## Deney tasarımı

1. Sensörün gövde etiketi, tam modeli, 100 A / 1 V oranı ve kablo/konnektör yapısı fotoğrafla kaydedilir.
2. ADS1115 girişinin sensör çıkış gerilimi, ortak-mod seviyesi ve giriş koruması testten önce doğrulanır.
3. Ayrı 100 A / 1 V YAML hazırlanır; derleme sonucu kaydedilir.
4. Önce yüksüz taban davranışı kaydedilir.
5. Güvenli ve kontrol edilebilir kararlı yük basamaklarında karakterizasyon düzeneğinin ADS1115/SCT çıktısı ve aynı modülden okunan PZEM akımı birlikte kaydedilir.
6. Aynı koşullar mümkünse 30 A / 1 V sensörle ayrı oturumda tekrarlanır.
7. Her basamak için ortalama, standart sapma, min–maks, sıçrama/okuma kaybı ve PZEM'e göre fark raporlanır.
8. Kalibrasyon katsayısı yalnız yeterli veri elde edildikten sonra ayrı değerlendirilir; karakterizasyon sırasında ayarlar ve katsayı değiştirilmez.

Akım basamakları, eldeki güvenli yükler ve bağlantı düzeni görüldükten sonra kesinleştirilecektir. 100 A seviyesine çıkılması hedeflenmemektedir; sensörün nominal kapasitesi test akımı hedefi değildir.

## Güvenlik ve test kapıları

- SCT sekonderi, primer iletkenden akım geçerken açık devre bırakılmaz.
- Şebeke hattında deney, uygun muhafaza, koruma ve güvenli ölçüm düzeni olmadan yapılmaz.
- ADS1115 A0/A1 girişlerinin ortak-mod ve GND–VDD sınırları fiziksel olarak doğrulanmadan enerjili ölçüm yapılmaz.
- ADS1115 PGA full-scale ayarı, giriş pinlerinin mutlak gerilim sınırlarını yükseltmez.
- Sensör çıkışının ADS1115'e doğrudan bağlanmasının uygunluğu varsayılmaz; gerçek bağlantı ve dalga seviyesi kontrol edilir.

## Başarı ölçütleri

- 100 A / 1 V sensör için bağımsız, tekrar kurulabilir YAML snapshot'ı.
- Derleme ve OTA çıktılarının kaydı.
- PZEM karşılaştırmasıyla çalışma aralığı ve kararlılık hakkında ölçüme dayalı sonuç.
- 30 A / 1 V ile farkların açıkça gösterilmesi.
- Kalibrasyon yapılmışsa katsayının dayandığı veri ve hesap yönteminin saklanması.

Bu deney, 100 A / 1 V sensörün tüm ana hatlarda kullanılacağına dair karar değildir. Kullanım yeri, deney sonucu ve gerçek hat akımı gereksinimine göre daha sonra seçilecektir.
