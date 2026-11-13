# BERO Envanteri

## İmal edilmiş donanımlar

### BIAS TRAFOSU — Taşınabilir Güç Kutusu

- **Tür:** Proje kapsamında imal edilmiş fiziksel donanım.
- **Kullanım amacı:** SCT013 akım ölçüm zincirinin trafo bias/güç yapısı.
- **Fiziksel yapı:** Ana sistemden ayrı, bağımsız ve taşınabilir güç kutusu.
- **Güç zinciri:** RN130421 6 V AC / 2.0 VA trafo → KBU610 köprü doğrultucu → 2200 µF / 35 V filtre kondansatörü → L78L33 (TO-92) regülatör.
- **Doğrulanmış çıkış:** Regülatör çıkışı fiziksel olarak **3.30 V** ölçüldü.
- **İlgili görev:** [GRV-003 — Trafo Bias Yapısının Kurulması ve Doğrulanması](../GOREVLER/GRV-003/RAPOR/README.md)
- **Görüntü / fotoğraf:** Kullanıcı tarafından daha sonra eklenecek.

> Not: Bu kayıt, imal edilmiş taşınabilir güç kutusunu envanter varlığı olarak tanımlar. GPIO32/33/34 üzerindeki 1.65 V okumaları, güç kutusunun 3.30 V çıkışından ayrı ölçüm noktalarıdır.


## BERO ölçüm modülleri — güncel durum (13.11.2026)

| Modül | Önceki işlev / donanım | Güncel durum | Not |
|---|---|---|---|
| **Modül 1** | Bağımsız bias trafosu / taşınabilir bias güç kutusu | **KALACAK** | Fiziksel envanter varlığı korunuyor. Modül 2'nin içine entegre edilmiş bias devresiyle aynı kayıt değildir; Modül 1 bağımsız donanım olarak tutulur. |
| **Modül 2** | Üç kanallı biaslı SCT okuma; Modül 1'in bias yapısını da içeren eski kurulum/kod | **İMHA EDİLDİ (kullanıcı bildirimi)** | Eski üç kanallı firmware yeni Modül 4'e taşınmayacak. Kod, YAML, log ve deney kayıtları tarihsel arşiv olarak korunur; fiziksel modülün imha bildirimi kaynaklı durumdur. |
| **Modül 3** | PZEM ve aç/kapa rölesi içeren eski modül | **İMHA EDİLDİ (kullanıcı bildirimi)** | Eski modül/kod düzeni devreden çıkarıldı. PZEM-004T V3 ölçüm cihazı Modül 4 tasarımında yeniden kullanılacak bileşen olarak planlanmıştır; Modül 3'ün eski kontrol/röle yapısı taşınmayacaktır. |
| **Modül 4** | Yeni ESP32 tabanlı ölçüm modülü: ADS1115 + 100 A / 1 V SCT + PZEM-004T V3 | **OLUŞTURULACAK** | Yeni ve bağımsız YAML/firmware hazırlanacak. 30 A / 1 V çalışan kodu ve eski Modül 2/3 kodları üzerine yazılmayacak. Pinler, UART/I²C, PZEM haberleşmesi ve giriş güvenliği test öncesi doğrulanacak. |

**Kod ve arşiv ilkesi:** Modül 2 ve Modül 3'ün eski kodları fiziksel modüllerin imha edilmesi nedeniyle depodan silinmez. Eski YAML, log, deney ve karar kayıtları tarihsel izlenebilirlik için korunur; yeni geliştirme Modül 4 adıyla ayrı dosyalarda yürütülür.

## Ölçüm ve deney ekipmanları

Bu bölüm, BERO geliştirme ve genel elektronik deneylerinde kullanılan mevcut ölçüm, sinyal üretme ve yük oluşturma araçlarını kaydeder. Cihazların varlığı, ölçüm doğruluğunun veya belirli bir deneyde uygunluğunun önceden doğrulandığı anlamına gelmez.

| Ekipman | Model / tanım | Kullanım amacı ve sınırlar | Durum |
|---|---|---|---|
| Dijital multimetre | UNI-T UT33D+ | Temel DC/AC gerilim, direnç ve süreklilik kontrolleri | Mevcut |
| Pens ampermetre | UNI-T UT200B+ | Temassız akım ölçümü ve yük akımını kontrol etme | Mevcut |
| Osiloskop | FNIRSI 2D15P, 2 kanal, 100 MHz | Analog dalga biçimi, genlik, zamanlama ve iki kanal karşılaştırması; ilk kullanım düşük gerilimli deneylerle yapılacak | **Satın alındı; teslimat bekleniyor (13.11.2026)** |
| Sinyal jeneratörü | SANEC; tam model henüz kaydedilmedi | Düşük gerilimli test sinyalleri üretme | Mevcut |
| Akım/gerilim simülatörü | FNIRSI SG-002, 4–20 mA / 0–10 V | Endüstriyel akım ve gerilim girişlerini simüle etme; çıkış sınırları ve bağlantı biçimi cihaz kılavuzundan doğrulanacak | Mevcut |
| USB lojik analizör | SANEC, 24 MHz, 8 kanal | UART, I²C, SPI ve diğer dijital lojik sinyallerin zamanlama/protokol incelemesi; analog dalga biçimi ölçmez | Mevcut |
| AC güç kontrolü / dimmer | SANEC, SCR, 220 V AC, ilan edilen 4000 W, manuel ve dokunmatik kontrol | Uyumlu rezistif yüklerde ayarlanabilir deney yükü oluşturma. Faz kontrolü nedeniyle akım dalga biçimini kesebilir; dimmerli kayıtlar normal sinüs beslemeli temel deney verilerinden ayrı tutulmalı | Mevcut |

## Akım sensörleri

| Sensör | Tanım | Kullanım amacı | Durum |
|---|---|---|---|
| SCT013 | 30 A / 1 V | Mevcut SCT ölçüm zincirinde kullanılan akım trafosu; düşük akım bölgesindeki davranışı inceleniyor | Mevcut |

| SCT013 | 100 A / 1 V | İleride ana hat gibi daha yüksek akım aralığı beklenen noktalarda değerlendirme; 30 A / 1 V ile ayrı ADS1115 karakterizasyonu | **8 adet mevcut (kullanıcı bildirimi; fiziksel model/etiket teyidi bekliyor)** |
| SCT013 | 5 A sınıfı; sipariş edilen ürünün tam model/çıkış etiketi teslimatta doğrulanacak | 30 A / 1 V sensörle düşük akım bölgesinde karşılaştırmalı deney; aynı yük koşulunda duyarlılık ve kararlılık gözlemi | **5 adet sipariş edildi; uluslararası taşımada (13.11.2026)** |

### 5 A SCT sevkiyat kaydı

- **Sipariş miktarı:** 5 adet (kullanıcı bildirimi).
- **Takip ekranı:** 13.11.2026 tarihinde China Post / uluslararası taşıma durumunda.
- **Son görülen olay:** Guangzhou Uluslararası Takas Bürosu'na ulaştı; Türkiye'ye giriş veya Türkiye gümrük işlemi henüz görünmüyor.
- **Teslimat durumu:** Teslim alınmadı; ürün etiketi, tam model, çıkış tipi, fiziksel durum ve adet teslimatta kontrol edilecek.
- **Gizlilik:** Takip numarası kamuya açık envanter dosyasına yazılmadı.

## Deney yükleri ve kullanım notları

- Akkor ampuller: 15 W, 42 W, 57 W, 100 W ve 150 W sınıflarında daha önce deneylerde kullanılmış yükler.
- 100 W + 150 W akkor ampul kombinasyonu ile yaklaşık 250 W toplam nominal yük elde edilebilir. 230 V varsayımıyla yaklaşık akım 1,09 A'dir; gerçek değer PZEM ile kaydedilmelidir.
- Evde bulunan tost makinesi, kettle ve fırın gibi rezistif ısıtıcılar farklı yük bölgeleri oluşturmak için kullanılabilir. Gerçek güç/akım her deneyde PZEM ile kaydedilir.
- SCR dimmer, yük ayarını kolaylaştırmak için düşünülmüştür; sabit güç kaynağı değildir. Dimmer ayar konumu sabit güç anlamına gelmez.
- Dimmer kullanıldığında faz kesme kaynaklı dalga şekli değişimi ve PF etkisi oluşabileceğinden, bu deneyler normal sinüs beslemeli SCT/PZEM karşılaştırmalarıyla aynı veri sınıfına karıştırılmamalıdır.
- Dimmerin üzerinde yazan 4000 W değeri, BERO deneylerinde bu güce çıkılacağı anlamına gelmez. Gerçek sürekli kapasite, soğutma ve koruma koşulları doğrulanmadan etiket değeri çalışma sınırı kabul edilmez.
- Şebeke gerilimiyle yapılan deneylerde uygun muhafaza, sigorta, bağlantı ve elektrik güvenliği sağlanmalıdır. FNIRSI 2D15P osiloskop probunun toprak klipsi doğrudan şebeke fazına veya nötrüne bağlanmayacaktır.

## Ekipman sınıflandırma ilkesi

- **Mevcut:** Kullanıcının elinde bulunduğu bildirilen cihaz.
- **Sipariş edildi / taşımada:** Sipariş verilmiş, ancak fiziksel teslim ve kutu/etiket kontrolü yapılmamış ekipman.
- Modeli veya teknik özelliği henüz kesinleşmeyen cihazlarda tahmin yürütülmez; doğrulama sonrasında kayıt güncellenir.


## Enerji ölçüm cihazları

| Cihaz | Model / tanım | Haberleşme | Durum | Not |
|---|---|---|---|---|
| AC güç/enerji ölçer | **PZEM-014 AC RS485 Modbus Güç Tüketim Ölçer + USB** | RS485 / Modbus RTU; USB arayüzü/adaptörü ürün seti kapsamında | **Mevcut — kullanıcı bildirimi; hiç kullanılmadı** | Fiziksel olarak mevcut olduğu kullanıcı tarafından teyit edildi. Henüz devreye alınmadı veya haberleşme testi yapılmadı. Slave adresi, baud/parity/stop bit, register haritası ve USB'nin işlevi cihaz etiketi/kılavuz ve ilk testle doğrulanacak. |
| AC güç/enerji ölçer | PZEM-004T V3 | UART / TTL seri haberleşme | Modül 4 için planlanan bileşen | PZEM-014 ile aynı cihaz değildir; Modül 4 ESP32 + ADS1115 + 100 A / 1 V SCT tasarımında ayrı bileşen olarak ele alınır. |

## Modbus ve saha haberleşme donanımları

Aşağıdaki adetler kullanıcı tarafından bildirilen fiziksel envanterdir. Tam model/SKU ve cihaz revizyonu, cihaz etiketleri veya üretici dokümanları üzerinden ayrıca doğrulanacaktır.

| Donanım | Model / tanım | Adet | Kapasite / arayüz | Durum ve not |
|---|---|---:|---|---|
| Dijital I/O | Waveshare Modbus RTU IO 8CH | 2 | Her modülde 8 DI + 8 DO; RS485 / Modbus RTU | Mevcut; toplam 16 DI + 16 DO |
| Analog giriş | Waveshare Modbus RTU Analog Input 8CH | 2 | Her modülde 8 kanal; 0–5 V, 1–5 V, 0–20 mA veya 4–20 mA modları | Mevcut; toplam 16 analog giriş |
| Analog çıkış | Waveshare Modbus RTU Analog Output 8CH (B) | 1 | 8 kanal, 0–10 V | Mevcut |
| RS485–Ethernet dönüştürücü | Waveshare 2-CH RS485 TO ETH (B) | 1 | 2 RS485 kanalı, Ethernet | Mevcut; seri sunucu/gateway çalışma modu konfigürasyonla doğrulanacak |
| Ethernet röle | Waveshare Modbus POE ETH Relay 30CH | 1 | 30 röle çıkışı, Ethernet/PoE | Mevcut; röle kontak sınırları ve Modbus çalışma modu ürün revizyonunun kılavuzundan doğrulanacak |
| Dokunmatik HMI | ESP32-S3, 7 inç ekran | 1 | Tam model, çözünürlük ve arayüzler henüz teyit edilmedi | Mevcut; kart üzerindeki RS485/CAN/GPIO bağlantıları SKU üzerinden doğrulanacak |
| Dokunmatik HMI | ESP32-P4, 7 inç ekran | 1 | Tam model, çözünürlük ve arayüzler henüz teyit edilmedi | Mevcut; kablosuz haberleşme ve yardımcı bağlantı mimarisi kart modeline göre doğrulanacak |

### Modbus envanteri kullanım ilkesi

- Waveshare dijital ve analog I/O modülleri saha I/O birimleri olarak değerlendirilecek.
- 2-CH RS485–ETH cihazı, RS485 segmentlerini Ethernet'e taşımak için kullanılabilir; gerçek Modbus TCP gateway işlevi ile şeffaf seri sunucu modu birbirinden ayrılarak test edilecek.
- 30CH PoE röle cihazı Ethernet tabanlı röle düğümüdür; RS485 saha hattı cihazı olarak sayılmayacak.
- ESP32-S3 ve ESP32-P4 7 inç ekranlı kartlar yerel HMI/operatör paneli adayıdır. İki kartın da tam ürün kodu ve teknik revizyonu henüz kaydedilmedi.
- Bu donanımların envanterde bulunması, aynı RS485 hattında birlikte çalıştıklarının veya register haritalarının doğrulandığının kanıtı değildir. Slave adresleri, baud/parity/stop bit ayarları, register adresleri, izolasyon ve hat sonlandırması saha testinde doğrulanacaktır.
- Bu bölümdeki adetler kullanıcı bildirimi esaslıdır; fiziksel etiket/fotoğraf doğrulaması tamamlandıkça model ayrıntıları güncellenecektir.

