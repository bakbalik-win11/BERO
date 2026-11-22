# BERO Faz 1 – Claude yakalama/analiz kodu ve Gemini sentezi incelemesi

- Tarih: 2026-11-22
- Kapsam: ADS1115 şebekesiz zamanlama ve iki kanal eşleştirme deneyi
- İncelenen kaynaklar: Claude tarafından üretilen bero_phase1_capture.ino ve bero_phase1_analysis.py; Gemini'nin uygulama sırası ve teknik sentezi
- Durum: Kod incelemesi / donanımda doğrulanmadı / mevcut haliyle yüklemeye hazır kabul edilmedi
- Araştırma dalı: ZMPT101B ve True PF araştırması; MOD2-GRV001 V1.6 ölçüm yolunu değiştirmez

## 1. Genel karar

Claude'un iki aşamalı yaklaşımı doğru yönde:
1. Önce ADS1115'in kanal dönüşüm zamanlamasını, RDY davranışını ve örnek aralıklarını şebekesiz ölçmek.
2. Aynı düşük gerilimli sinyali iki diferansiyel kanala vererek kanal başına zaman farkını ve zaman damgası sonrası artık faz/gecikmeyi incelemek.

RAM'de yakalayıp seri aktarımı ölçüm bittikten sonra yapmak da yakalama sırasında seri yazdırmanın oluşturacağı değişken yükü azaltır.

Bununla birlikte iki kaynak dosya henüz ESP32D2 üzerinde derlenmiş, yüklenmiş veya ADS1115 ile denenmiş değildir. Kodlar mevcut halleriyle başarılı/kararlı firmware olarak sınıflandırılamaz. Aşağıdaki düzeltme ve kontrollerden sonra Faz 1 aday sürümü olarak denenmelidir.

## 2. Gerçekleştirilen yazılım kontrolü

Python dosyası Python AST/sözdizimi kontrolünden geçti. scipy, numpy ve matplotlib ile --simulate çalıştırıldı.

Bu sentetik koşuda:
- Kanal başına sentetik hız yaklaşık 347,3 SPS çıktı.
- Simülasyona verilen 20,00 µs kanal artık kayması 20,07 µs olarak bulundu.
- Bloklar arası standart sapma yaklaşık 0,22 µs çıktı.
- Naif indeks eşleştirme M0 için ortalama 1-PF sapması yaklaşık 0,10054.
- M1 lineer enterpolasyon + basit ortalama için yaklaşık 0,00002.
- M2 lineer enterpolasyon + birleşik zaman ızgarasında trapez integrasyonu için yaklaşık 0,00562.
- M3 kübik spline + sık zaman ızgarasında trapez integrasyonu için yaklaşık 0,00002.

Bunların tamamı kod içindeki sentetik modelin çıktısıdır; gerçek ADS1115 ölçümü, gerçek örnekleme hızı veya BERO donanım başarısı değildir.

## 3. Önemli analiz bulguları ve düzeltmeler

### 3.1 Kanal örnekleme süresi ile kanal arası fark ayrılmalı

İki kanallı ideal dönüşümlü 860 SPS taramada tek dönüşüm yaklaşık 1,163 ms sürer. Her kanalın kendi tekrar süresi idealde yaklaşık 2,326 ms olur. A ve B dönüşümleri arasındaki ardışık zaman farkı ise nominal olarak yaklaşık 1,163 ms'dir.

Gerçek ESP32 + I²C + sürücü çevrimi bu ideal aralıklardan farklı olabilir. Rapor şu üç değeri ayrı vermelidir:
- Aynı kanalın tekrar aralığı
- Ardışık farklı kanalların dönüşüm hazır zamanları arasındaki aralık
- Sinüs uyumuyla bulunan zaman damgası düzeltmesinden sonraki artık kanal gecikmesi

Bunlardan hiçbiri ölçülmeden sabit kabul edilmeyecektir.

### 3.2 125 Hz frekans taraması mevcut analizde güvenilir değil

Aynı sentetik model 50, 75, 100 ve 125 Hz'de çalıştırıldığında:
- 50 Hz: tahmini frekans 49,994 Hz; artık gecikme 20,07 µs civarı.
- 75 Hz: tahmini frekans 74,847 Hz; artık gecikme 20,04 µs civarı.
- 100 Hz: tahmini frekans 100,151 Hz; artık gecikme 20,03 µs civarı.
- 125 Hz: tahmini frekans 122,897 Hz; artık gecikme 12,68 µs ve blok std yaklaşık 32,85 µs.

Son satır, simülasyonda gerçek 20 µs kaymayı güvenilir biçimde geri bulamadığını gösteriyor. Bu nedenle 125 Hz ölçümü mevcut örnekleme hızında kalibrasyon/başarı kriteri olarak kullanılmayacaktır. İstenirse yalnızca sınır davranışını görmek için stress testi olarak kaydedilebilir. Önce donanımdan gerçek SPS ölçülmeli; frekans taramasının üst sınırı buna göre belirlenmelidir.

Python betiğindeki H_max hesabı MAINS_F=50 değerini sabit kullanıyor. 75/100/125 Hz testlerinin raporunda bu alan şebeke harmonik kapasitesi gibi yorumlanmamalıdır. Test frekansı ve şebeke harmonik hesabı ayrı parametreler olmalıdır.

### 3.3 M2 sonucu trapez kuralının genel olarak yanlış olduğunu göstermez

M2, her iki kanalı ayrı ayrı lineer enterpole edip zaman noktalarının birleşiminde çarpım alıyor ve bu çarpımın trapez integralini hesaplıyor. İki lineer fonksiyonun çarpımı her aralıkta genellikle ikinci dereceden olur; trapez kuralı bu çarpımı tam entegre etmez. Sentetik testte görülen 0,00562 sapma bu uygulama biçiminin sayısal hatası olabilir.

Sonuç olarak:
- Trapez integrasyonu genel olarak reddedilmemeli.
- Birleşik ızgaradaki ürünün entegrasyonu daha yüksek dereceli integrasyonla veya yeterince sık ortak zaman ızgarasında değerlendirilmelidir.
- M1'in basit ortalaması zaman aralıkları düzensizse zaman ağırlıklı ortalama değildir.
- M3 kübik spline, temiz sinüs sentetiğinde iyi sonuç verebilir; ancak gürültülü veya keskin kenarlı harmonikli akım dalgasında taşma/overshoot oluşturabilir.
- Tek bir temiz sinüs sentetiği hangi yöntemin BERO için en iyi olduğunu kanıtlamaz.

### 3.4 Jitter tanımı karışmamalı

Python betiğindeki dt_std_us kanal başına ardışık dönüşüm zaman aralıklarının standart sapmasıdır. Bu örnekleme aralığı jitter'ıdır.

delta_std_us ise 1 saniyelik bloklarda sinüs uyumuyla bulunan artık kanal gecikmesinin bloktan bloğa değişimidir. Bu, doğrudan örnekleme jitter'ı değildir; artık gecikme kararlılığının göstergesidir.

Hata bütçesi çıktısındaki “jitter +-1s” etiketi bu nedenle yanıltıcıdır. “1 saniyelik bloklar arası artık gecikme std” olarak adlandırılmalıdır.

### 3.5 G/H sıra takası

g ve h yakalamaları yararlı bir deneydir. İki kanalı farklı sırada dönüştürerek MUX geçmişi/yerleşme etkisinin kanala bağımlı olup olmadığı araştırılır.

Karşılaştırma için:
- Aynı örnekleme hızı, PGA, I²C, kablo, kaynak ve frekans korunmalı.
- İlk kanal bilgisi meta veride bulunmalı.
- Kanal 0→1 ve 1→0 damga aralıkları ayrı raporlanmalı.
- Artık gecikmenin g/h değişiminde ne kadar oynadığı hesaplanmalı.
- Tek başına ortalama iki yönlü kanal aralığı kullanılarak sıra asimetrisi gizlenmemeli.

## 4. Arduino yakalama kodu incelemesi

### Doğru/yararlı noktalar

- ADS1115 MUX seçimi A0-A1 ve A2-A3 için doğru bit alanlarına karşılık gelir.
- PGA ±2,048 V ve DR=860 SPS ayarı yazmaç alanlarıyla uyumludur.
- ALERT/RDY dönüşüm hazır modu için Hi_thresh MSB=1, Lo_thresh MSB=0 ve COMP_QUE != 11 koşulları sağlanmıştır.
- ALERT/RDY açık drençli çıkış olduğu için 3,3 V'a harici pull-up kullanılması uygundur.
- 8000 adet 12 baytlık kayıt 96.000 bayt RAM gerektirir; tahmin doğrudur.
- Yakalama sırasında seri çıktı vermeyip sonradan dökme yaklaşımı uygundur.
- t_rdy, dönüşüm verisinin hazır olduğu olayın zaman damgasıdır; analog dalganın tek bir anındaki örnek zamanı olarak yorumlanmamalıdır.

### Yükleme öncesi düzeltilmesi/kontrol edilmesi gerekenler

1. g_run, g_done ve g_first değişkenleri farklı çekirdekler arasında volatile ile paylaşılmış. volatile tek başına görevler arası senkronizasyon/atomiklik garantisi değildir. FreeRTOS task notification, event group veya uygun kritik bölüm/atomik değişken yapısı kullanılmalıdır.
2. xTaskCreatePinnedToCore dönüş değeri kontrol edilmeli. Görev oluşturulamazsa g_acq null kalır ve ISR içinde geçersiz task handle kullanılabilir.
3. ADS1115 threshold register yazımları başarısız olursa kod yalnızca mesaj verir, yine de “Hazır” moduna geçer. Başarısız init durumunda yakalama komutu engellenmelidir.
4. ALERT/RDY hattının tek-atış modunda ilk ve sonraki dönüşümlerde nasıl davrandığı osiloskopla doğrulanmalıdır. Her yeni dönüşüm için gerekli kenarın tekrar oluştuğu görülmeden 8000 kayıt yakalama başlatılmamalıdır.
5. attachInterrupt çağrısının acquisition task içinden yapılması, ISR'nin kesin olarak o task'in çekirdeğinde çalıştığı varsayımı için tek başına kanıt değildir. Çekirdek/ISR yerleşimi kullanılan Arduino-ESP32 sürümünde doğrulanmalıdır; yorum satırı kesin garanti gibi yazılmamalıdır.
6. Her I²C işlem sonucu ve RDY zaman aşımı loglanmalı; hata kayıtları toplam sayım ve yüzde ile raporlanmalıdır.
7. Toplam yakalama süresi için de üst sınır olmalı; ana loop g_done beklerken süresiz kilitlenmemelidir.
8. Kod Arduino-ESP32 2.x/3.x uyumlu diye etiketlenmiş olsa da gerçek derleme yapılmadı. Kullanılacak kart seçimi ve core sürümüyle derleme zorunludur.

## 5. FNIRSI 2D15P sinyal jeneratörü ve DC bias

FNIRSI 2D15P üretici ürün sayfası 10 MHz jeneratörü ve 0,1–3,0 Vpp genlik aralığını bildiriyor. Kullanım kılavuzunda dalga biçimi, frekans ve genlik ayarları açıklanıyor; sinüs üzerine bağımsız DC offset ayarı belgelenmiş görünmüyor.

Bu nedenle Claude/Gemini bağlantı şemasındaki “1,6 Vpp +0,9 V DC offset” doğrudan cihazdan ayarlanabilir kabul edilmeyecektir. Önce 2D15P menüsünde ayrı offset kontrolü olup olmadığı kullanıcı tarafından teyit edilmeli veya çıkış osiloskopla ölçülmelidir.

ADS1115 analog pinleri, VDD=3,3 V iken GND'nin altına veya VDD'nin üstüne sürülmemelidir. Sıfır merkezli çift kutuplu sinüs doğrudan A0/A2'ye bağlanmayacaktır.

Offset üretilemiyorsa, jeneratör sinyalini uygun AC kuplaj kondansatörüyle ayrı ve kararlı 1,65 V bias düğümüne bindiren düşük gerilimli test ağı tasarlanabilir. Bu bağlantı şeması ayrıca netleştirilmeden kablolama yapılmamalıdır. Sinyal seviyesi önce multimetre/osiloskopla ölçülmelidir.

## 6. Python betiği ve macOS çalışma koşulları

- Python dosyası sözdizimi kontrolünden geçti.
- --simulate sentetik testte çalıştı.
- Gerçek cihaz yakalaması yapılmadı.
- Gerekli Python paketleri: numpy, scipy, matplotlib; seri porttan yakalama için ayrıca pyserial.
- Örneklerdeki COM5 Windows portudur. Kullanıcının Mac'inde gerçek port /dev/cu.* biçiminde bulunabilir; port adı önceden tespit edilmelidir.
- capture_serial port açıldığında ESP32'nin otomatik resetlenmesi olasılığını ele almıyor. RX tamponunu hemen temizleyip komutu hemen gönderdiği için komut boot sırasında kaybolabilir. “Hazır” mesajı için el sıkışma veya kontrollü bekleme eklenmelidir.
- Betik yetersiz/boş kanal, sıfır genlik, yetersiz sıfır geçişi ve yetersiz 1 saniyelik blok durumlarına karşı daha açık hata kontrolleriyle güçlendirilmelidir.
- Karar kapısı eşikleri kodda tasarım hedefi olarak tanımlanmış; ölçülmüş donanım kabul kriteri değildir. PASS/WARN/FAIL tek başına mimari karar vermemelidir.

## 7. Gemini'nin son sentezinden alınan ve ertelenen öneriler

Alınan yararlı öneriler:
- 96 kB RAM tamponuyla önce yakalama, sonra seri döküm.
- g/h dönüş sırası takası.
- t_rdy zaman damgası sonrası artık gecikmenin ayrıca sinüs uyumuyla incelenmesi.
- Dirençli yük PF≈1 kontrolünün faz doğrulaması için tek başına yeterli olmadığı.
- P, S, PF, DC ofset, crest factor, örnekleme aralığı, clipping ve kayıp örneklerin pencere bazında saklanması.

Şimdilik kabul edilmeyen/ertelenenler:
- 125 Hz'nin mevcut örnekleme hızıyla doğruluk kalibrasyonu olarak kullanılması.
- 10 µF kondansatörün 230 V şebekede doğrudan bağlanması ve R||C şebeke deneyi.
- Kettle çalışırken osiloskop ground uçlarını iki sensör çıkışına bağlamaya dayalı doğrudan şebeke testi.
- Sıradan multimetreyle GND-PE kontrolünün izolasyon güvenliğini kanıtladığı varsayımı.
- 0,15–0,25 A veya 1 VA gibi başka modellerden gelen sabit PF geçerlilik eşikleri.

Önemli güvenlik kararı: FNIRSI 2D15P bataryalı olsa da toprak/kanal izolasyonu varsayılmayacaktır. Bir multimetreyle güç verilmiş devrede GND-PE geriliminin yaklaşık sıfır çıkması izolasyon güvenliği kanıtı değildir. Şebeke üzerinde doğrudan ölçüm yapılmayacaktır. Ototransformatör galvanik izolasyon sağlamaz. Faz 1 ve ilk analog karakterizasyon testleri güvenli düşük gerilimli kaynakla yapılacaktır.

## 8. Güncel ilk deney sırası

1. 2D15P jeneratöründe gerçek DC offset kontrolünün bulunup bulunmadığını doğrula. Çıkış seviyesini cihazın kendisiyle veya uygun ölçümle kontrol et.
2. Offset yoksa 1,65 V biaslı AC kuplaj test ağı tasarımını netleştir; doğrudan sıfır merkezli sinüs bağlama.
3. Arduino kodundaki görev senkronizasyonu, init hata yönetimi, global timeout ve RDY kontrolünü düzelt.
4. Python betiğine macOS seri port el sıkışması, veri doğrulama ve rapor etiket düzeltmelerini ekle.
5. Kullanıcının gerçek ESP32 kartı ve Arduino-ESP32 sürümüyle derle.
6. Önce iki kanala aynı DC seviyeyi uygula; dönüşüm ve RDY zamanlamasını kaydet.
7. Sonra iki kanala aynı güvenli 50 Hz sinyali uygula; g ve h kayıtları al.
8. 75/100 Hz taramalarını yalnızca analiz kararlılığını sınayan ek test olarak değerlendir. 125 Hz, mevcut simülasyon sonucu nedeniyle doğruluk kalibrasyonuna dahil edilmez.
9. Ham CSV, JSON özet, grafik ve yorum saklanır. Gerçek donanım sonucu olmadan PASS/FAIL kararı verilmez.

## 9. Açık durum

- Python AST/sözdizimi kontrolü: geçti.
- Python sentetik simülasyon: çalıştı.
- Python sentetik sonuçları: yalnızca kod testidir.
- Arduino derlemesi: yapılmadı.
- ESP32'ye yükleme: yapılmadı.
- ADS1115 ile gerçek kayıt: yapılmadı.
- FNIRSI 2D15P jeneratörünün DC offset yeteneği: teyit bekliyor.
- Şebekesiz Faz 1 donanım testi: bekliyor.
- Faz 2 sensör ve PF testi: bekliyor.

## 10. Kaynaklar

- Texas Instruments ADS1115 ürün sayfası ve veri sayfası: https://www.ti.com/product/ADS1115
- ADS111x veri sayfası PDF: https://www.ti.com/lit/ds/symlink/ads1115.pdf
- FNIRSI 2D15P üretici ürün sayfası: https://www.fnirsi.com/products/2d15p
- Arduino-ESP32 I²C API: https://docs.espressif.com/projects/arduino-esp32/en/latest/api/i2c.html
- Arduino-ESP32 GPIO API: https://docs.espressif.com/projects/arduino-esp32/en/latest/api/gpio.html
