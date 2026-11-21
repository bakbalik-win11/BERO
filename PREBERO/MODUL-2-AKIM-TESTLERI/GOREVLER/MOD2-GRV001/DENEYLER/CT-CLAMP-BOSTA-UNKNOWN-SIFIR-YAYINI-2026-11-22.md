# ct_clamp yüksüz durumda unknown / sıfır yayınlama deneyi

**Tarih:** 2026-11-22  
**Görev:** MOD2-GRV001  
**Durum:** AÇILDI – kod incelemesi ve kontrollü doğrulama bekliyor

## Amaç

Biassız A0-A1 ölçüm yolunda akım yokken Home Assistant sensörünün neden `unknown` durumuna geçtiğini belirlemek ve gerçek ADC örneklemesi sürdüğü hâlde akım bulunmadığında `0.000 A` yayınlanmasını sağlayacak en küçük, doğrulanabilir yazılım değişikliğini araştırmak.

Bu deneyin amacı ölçüm yapılmadığı hâlde yapay olarak sıfır üretmek değildir. Sıfır değeri ancak ADS1115 örneklemesi ve RMS ölçüm penceresi gerçekten çalışmışsa yayınlanmalıdır.

## Sabit donanım ve mevcut yapı

- ESP: ESP32D2
- ADC: ADS1115 No.10
- I²C adresi: 0x48
- I²C: GPIO21 SDA, GPIO22 SCL
- ADC beslemesi: 3.3 V
- Ölçüm: A0-A1 diferansiyel
- SCT: SCT013 30A/1V
- Analog düzen: Biassız
- ADS1115: Continuous mode
- PGA: 2.048 V
- Örnekleme hızı: 860 SPS
- ct_clamp penceresi: 200 ms
- Sensör update_interval: 1 s
- Mevcut K: 27.59
- Mevcut alt eşik: 0.005 A

## İncelenecek mevcut YAML davranışı

Kaynak dosya:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/V1.1-TEST-A0A1.yaml`

Mevcut akış:
1. ADS1115 A0-A1 diferansiyel ölçümünü `ads_sct_a0_a1_raw` dahili sensörüne verir.
2. `ct_clamp`, 200 ms pencerede RMS akım hesabı yapar.
3. Sensör 1 saniyede bir güncellenir.
4. Linear kalibrasyon K=27.59 uygular.
5. Lambda filtresi x < 0.005 A ise 0.0 döndürür; aksi hâlde x değerini geçirir.

Bu YAML'de 5 mA altı için açıkça sıfır döndüren filtre zaten vardır. Buna rağmen yüksüz durumda HA'da `unknown` görülmesi, yalnızca alt eşik filtresinin eksikliğiyle açıklanamaz. Önce `ct_clamp` girişine gelen değer, RMS çıktısı, NaN/invalid davranışı ve filtre zincirinin çalışıp çalışmadığı incelenmelidir.

## Araştırma soruları

1. `ct_clamp`, ADS1115 kaynağından her güncelleme aralığında geçerli örnek alıyor mu?
2. Yüksüz durumda kaynak sensör hangi değeri yayınlıyor: sıfır, çok küçük RMS, NaN veya hiç yayın yok mu?
3. `ct_clamp` hesaplaması yüksüz sinyalde NaN/invalid sonuç üretebiliyor mu?
4. `calibrate_linear` ve lambda filtresi NaN değerini nasıl ele alıyor?
5. Home Assistant'taki `unknown`, ESPHome'un NaN/invalid durumundan mı, yoksa hiç yeni durum yayınlanmamasından mı kaynaklanıyor?
6. Ölçüm penceresi tamamlandığında geçerli örnek alınmışsa ve RMS akımı 5 mA altındaysa 0.000 A yayınlamak mümkün mü?
7. ADS1115/I²C örneklemesi kesilirse sıfır basmak yerine `unknown` kalmasını nasıl garanti ederiz?

## Test aşamaları

### Aşama 1 – Mevcut kodu değiştirmeden gözlem

- Mevcut V1.1 A0-A1 YAML korunacak.
- Yüksüz durumda ESPHome DEBUG logu incelenecek.
- ADS1115/I²C hata mesajları, kaynak sensör güncellemeleri ve ct_clamp yayınları ayrıştırılacak.
- Home Assistant geçmişiyle ESPHome log zamanları eşleştirilecek.
- Yük verildiğinde akım ölçümünün yeniden yayınlandığı kontrol edilecek.

### Aşama 2 – Kaynak kod / bileşen davranışı incelemesi

- Kullanılan ESPHome sürümündeki `ct_clamp` uygulamasının örnekleme, RMS hesaplama ve geçersiz değer davranışı incelenecek.
- Filtre zincirinin NaN/invalid değerleri nasıl işlediği doğrulanacak.
- Kaynak kod veya log kanıtı olmadan `ct_clamp` davranışı hakkında kesin neden yazılmayacak.

### Aşama 3 – Ayrı deney YAML'i ile kontrollü doğrulama

Yalnızca Aşama 1 ve 2 sonrasında gerekirse yeni bir sürüm oluşturulacak. Mevcut V1.1 dosyasının üzerine yazılmayacak.

Hedef davranış:
- Ölçüm penceresi başarıyla örneklenmiş ve RMS < 0.005 A ise: 0.000 A yayınla.
- Ölçüm penceresi başarıyla örneklenmiş ve RMS >= 0.005 A ise: kalibre edilmiş akımı yayınla.
- ADS1115/I²C okuması başarısız, örnekleme geçersiz veya ölçüm penceresi tamamlanmamışsa: geçersizliği gizleyip sıfır üretme.

Bu davranışın uygulanabilirliği ESPHome bileşeninin gerçek davranışı ve test sonuçlarıyla doğrulanacaktır.

## Başarı ölçütleri

- Yüksüz durumda ADC örneklemesinin sürdüğü kanıtlanmalı.
- Geçerli yüksüz ölçüm pencereleri Home Assistant'a düzenli 0.000 A yayınlamalı.
- Kontrollü yük verildiğinde akım değeri doğru yönde yükselmeli.
- ADC/I²C bağlantısı kesildiğinde sistem sahte 0.000 A üretmemeli.
- Geçerli sıfır ile ölçüm arızası birbirinden ayırt edilebilmeli.

## Koruma kuralları

- Mevcut çalışan V1.1 YAML değiştirilmeyecek.
- K=27.59 değiştirilmeyecek.
- Bias eklenmeyecek; mevcut biassız A0-A1 düzeni korunacak.
- Bu aşamada eşik veya filtre değeri değiştirilmez.
- Test logu ve gerçek sonuç olmadan deney tamamlandı denmez.

## İlk durum

Deney açıldı. Henüz kök neden belirlenmedi, yeni YAML hazırlanmadı ve yazılım değişikliği uygulanmadı.


## 2026-11-22 – Kullanıcı işletim tercihi ve V1.2 deney YAML'i

Kullanıcı kararı: ESP32 çalışırken sensörün `unknown` üretmesi yerine `0.000 A` yayınlaması tercih edilir. ESP32 kapalı/bağlantısız olduğunda Home Assistant'ın `unknown` veya `unavailable` göstermesi beklenir. Böylece normal yüksüz durum sıfırla, cihaz/iletişim kesintisi ise bilinmeyen durumla izlenebilir; yük varken sıfır görülmesi dikkat gerektiren anomali olur.

### Kod incelemesi bulgusu

ESPHome `ct_clamp` kaynak kodunda örnekleme penceresi sonunda `num_samples_ == 0` ise `NAN` yayınlanır. Örnek varsa RMS hesabı yapılır; RMS kare değeri pozitif değilse 0.0 sonucu yayınlanır. Örnekleme döngüsü ayrıca aynı ardışık ADC değerlerini tekrar saymaz. Bu nedenle mevcut YAML'deki 5 mA altı lambda filtresi, kaynak bileşenin `NAN` yayınlaması durumunda tek başına sıfır üretemez. Kaynak incelemesi: ESPHome ct_clamp_sensor.cpp (2026.11 API dokümantasyonu).

### V1.2 deney yaklaşımı

Yeni, ayrı YAML oluşturuldu:

`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.2/V1.2-TEST-A0A1-UNKNOWN-ZERO.yaml`

- V1.1 ölçüm zinciri, ADS1115 ayarları, 200 ms pencere, 1 s aralık ve K=27.59 korunur.
- ct_clamp sensörü internal yapılır.
- Ayrı template sensör, ct_clamp durumu NaN ise 0.000 A; sayısal ise ölçülen akımı yayınlar.
- ESP32 kapanması veya API bağlantısının kesilmesi hâlinde HA'nın entity'yi unavailable yapması beklenir.
- Bu çözüm ESP32 açıkken ADS1115/I²C kaynaklı NaN'ı da sıfıra dönüştürebilir; bu sürüm arıza teşhis sensörü değildir.

### Sabah test sırası

1. ESP32 açık ve SCT yüksüz: HA'da düzenli 0.000 A görülüyor mu?
2. Kontrollü yük ver: akım değeri yükseliyor mu?
3. Yükü kaldır: değer yeniden 0.000 A oluyor mu?
4. ESP32'yi kapat: HA entity'si unavailable/unknown oluyor mu?
5. ESP32'yi yeniden aç: entity tekrar çevrimiçi olup sıfır/akım yayınlıyor mu?
6. ESPHome DEBUG logu ve HA geçmişi birlikte saklanır.

**Durum:** V1.2 YAML depoya eklendi ve dosya geri okunarak doğrulandı. Derleme, cihaza yükleme ve fiziksel test henüz yapılmadı. Deney açık durumdadır.
