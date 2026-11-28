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
| **Modül 2** | Üç kanallı biaslı SCT okuma; Modül 1'in bias yapısını da içeren eski fiziksel kurulum | **ESKİ DÜZENEK İMHA EDİLDİ; masaüstü test düzeneği ayrı ve mevcut** | Eski üç kanallı firmware yeni Modül 4'e taşınmayacak. Güncel masaüstü ESP32-D + ADS1115 + SCT013 düzeneği, eski fiziksel Modül 2 ile aynı cihaz değildir; aşağıda ayrı test varlığı olarak kayıtlıdır. Kod, YAML, log ve deney kayıtları tarihsel arşiv olarak korunur. |
| **Eski elektronik Modül 3 düzeni** | PZEM ve aç/kapa rölesi içeren eski donanım düzeni | **ESKİ RÖLELİ DÜZENEK DEVREDEN ÇIKTI; PZEM yayıncı WROOM ESP YAŞIYOR** | Kullanıcının 2026-11-28 tarihli teyidine göre PZEM ölçümlerini yayınlayan ESP32-WROOM fiziksel olarak mevcut ve bağımsız referans/test cihazı olarak tutulacak; eski `BERO Modul 3 WROOM` adı firmware geçmişi olarak korunur. Bu eski elektronik ad, güncel PREBERO Modül 3 (çamaşır makinesi) ile aynı kimlik değildir. Ayrıntı aşağıdaki cihaz kaydında. |
| **Modül 4** | Yeni ESP32 tabanlı ölçüm modülü: ADS1115 + 100 A / 1 V SCT + PZEM-004T V3 | **OLUŞTURULACAK** | Yeni ve bağımsız YAML/firmware hazırlanacak. 30 A / 1 V çalışan kodu ve eski Modül 2/3 kodları üzerine yazılmayacak. Pinler, UART/I²C, PZEM haberleşmesi ve giriş güvenliği test öncesi doğrulanacak. |

**Kod ve arşiv ilkesi:** Devreden çıkan eski Modül 2 ve Modül 3 düzenlerinin kodları depodan silinmez. Eski YAML, log, deney ve karar kayıtları tarihsel izlenebilirlik için korunur; yeni geliştirme Modül 4 adıyla ayrı dosyalarda yürütülür. PZEM yayıncısı WROOM ESP'nin fiziksel varlığı ayrıca korunur ve deney referansı olarak envanterde izlenir.

### Aktif masaüstü test varlıkları

Bu test varlıkları PREBERO çalışma modüllerinin kimliğiyle karıştırılmaz. Eski fiziksel bir modülün devreden çıkması, başka bir deneyde kullanılan geliştirme kartının da imha edildiği anlamına gelmez.

| Geçici işlev etiketi | Fiziksel düzen / işlev | Durum ve kayıt |
|---|---|---|
| **MOD2-BENCH-01** | ESP32-D2 + ADS1115 No.10 + SCT013 30 A / 1 V masaüstü akım ölçüm düzeneği | **Mevcut; Modül 2 deneylerinde kullanılıyor.** MOD2-GRV001 V1.6 EXP/K(x) bu düzende edinilmiş ve korunmuş akım referansıdır. ZMPT101B, MOD2-GRV002 için ayrıca eklenecek aday sensördür; bağlantı/güvenlik ve kart revizyonu henüz doğrulanmadı. Bu masaüstü düzeneği eski imha edilmiş üç kanallı Modül 2 değildir. |
| **PZEM-REF-WROOM-01** (geçici işlev etiketi) | ESP32-WROOM + PZEM-004T V3.0; yalnızca PZEM ölçümlerini Home Assistant'a 5 saniyede bir yayınlar | **Fiziksel ESP mevcut; kullanıcı 2026-11-28'de teyit etti.** UART: TX GPIO19, RX GPIO18, 9600 baud, 8N1. Arşiv yapılandırmasındaki ESPHome adı `bero-modul3-wroom`, görünen ad `BERO Modul 3 WROOM`; bunlar tarihsel yazılım adlarıdır, güncel modül numarası değildir. Fiziksel kart modeli/revizyonu ve MAC/seri eşlemesi yapılınca kalıcı ESP envanter kimliği atanacak; yüklenmiş yapılandırma da ayrıca kontrol edilecek. Bu cihaz MOD2 deneyleri için PZEM referansı sağlar; Modül 5 veya aktif BERO modülü değildir. |

## Ölçüm ve deney ekipmanları

Bu bölüm, BERO geliştirme ve genel elektronik deneylerinde kullanılan mevcut ölçüm, sinyal üretme ve yük oluşturma araçlarını kaydeder. Cihazların varlığı, ölçüm doğruluğunun veya belirli bir deneyde uygunluğunun önceden doğrulandığı anlamına gelmez.

| Ekipman | Model / tanım | Kullanım amacı ve sınırlar | Durum |
|---|---|---|---|
| Dijital multimetre | UNI-T UT33D+ | Temel DC/AC gerilim, direnç ve süreklilik kontrolleri | Mevcut |
| Bağımsız analog referans multimetre | UNI-T UT61E+ | Planlanan tezgâh DMM'si: düşük AC mV, DC mV/V, AC/DC akım ve direnç ölçümleri; sensörün ham çıkışını ADC'den bağımsız karakterize etme. Üretici spesifikasyonlu ölçü aletidir, kalibrasyon standardı değildir. | **Satın alma kararı verildi; henüz mevcut değil / teslim beklenmiyor** |
| Pens ampermetre | UNI-T UT200B+ | Temassız akım ölçümü ve yük akımını kontrol etme | Mevcut |
| Osiloskop / DMM / DDS | FNIRSI 2D15P, 2 kanal, 100 MHz; dahili True RMS multimetre ve 1 kanallı DDS jeneratör | Analog dalga biçimi, genlik, zamanlama ve iki kanal karşılaştırması; DMM ile temel AC/DC ölçümler; DDS ile 0,1–3,0 Vpp dalga üretimi. Düşük mV AC için pasif zayıflatıcıyla yardımcı test kaynağı olabilir; kalibrasyon standardı değildir. **Mevcut / teslim alındı (22.11.2026 teyidi).** | Mevcut |
| Sinyal jeneratörü | SANEC; tam model henüz kaydedilmedi | Düşük gerilimli test sinyalleri üretme | Mevcut |
| Akım/gerilim simülatörü | FNIRSI SG-002, ayarlanabilir DC gerilim / DC akım simülatörü | 0–10 V sınıfı DC gerilim ve 4–20 mA dahil DC akım döngülerini simüle etme; fiziksel cihazın menü aralıkları ve terminal şeması kılavuzla teyit edilecek. Kılavuzdaki “50HZ” ifadesi ekran gösterim modudur; AC sinüs çıkışı değildir. Kalibrasyon standardı değildir; gerçek çıkış ayrıca ölçülmelidir. | Mevcut |
| USB lojik analizör | SANEC, 24 MHz, 8 kanal | UART, I²C, SPI ve diğer dijital lojik sinyallerin zamanlama/protokol incelemesi; analog dalga biçimi ölçmez | Mevcut |
| AC güç kontrolü / dimmer | SANEC, SCR, 220 V AC, ilan edilen 4000 W, manuel ve dokunmatik kontrol | Uyumlu rezistif yüklerde ayarlanabilir deney yükü oluşturma. Faz kontrolü nedeniyle akım dalga biçimini kesebilir; dimmerli kayıtlar normal sinüs beslemeli temel deney verilerinden ayrı tutulmalı | Mevcut |

## Akım sensörleri

| Sensör | Tanım | Kullanım amacı | Durum |
|---|---|---|---|
| SCT013 | 30 A / 1 V | Mevcut SCT ölçüm zincirinde kullanılan akım trafosu; düşük akım bölgesindeki davranışı inceleniyor | Mevcut |

| SCT013 | 100 A / 1 V | İleride ana hat gibi daha yüksek akım aralığı beklenen noktalarda değerlendirme; 30 A / 1 V ile ayrı ADS1115 karakterizasyonu | **8 adet mevcut (kullanıcı bildirimi; fiziksel model/etiket teyidi bekliyor)** |
| SCT013 | 5 A sınıfı; sipariş edilen ürünün tam model/çıkış etiketi fiziksel teslim olmadığı için doğrulanamadı | 30 A / 1 V sensörle düşük akım bölgesinde karşılaştırmalı deney için planlanmıştı | **Teslim alınmayacak (kullanıcı bildirimi, 27.11.2026; gümrükte takıldı)** |

### 5 A SCT sevkiyat kaydı

- **Sipariş miktarı:** 5 adet (kullanıcı bildirimi).
- **Önceki takip kaydı:** 13.11.2026 tarihinde China Post / uluslararası taşıma durumundaydı; Guangzhou Uluslararası Takas Bürosu'na ulaştığı kaydedilmişti.
- **Güncel teslimat durumu:** Kullanıcı bildirimi (27.11.2026): gönderi gümrükte takıldı ve teslim gelmeyecek. Bu sipariş mevcut fiziksel stok olarak sayılmaz.
- **Ürün bilgisi:** Teslimat gerçekleşmeyeceği için tam model, çıkış tipi, fiziksel durum ve ürün etiketi doğrulanamadı. Sipariş iptali veya ücret iadesi hakkında kayıt bulunmuyor.
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
| AC güç/enerji ölçer | **PZEM-014 AC RS485 Modbus Güç Tüketim Ölçer + USB** | RS485 / Modbus RTU; USB arayüzü/adaptörü ürün seti kapsamında; **10 A sınıfı (kullanıcı bildirimi, etiketle teyit edilecek)** | **Mevcut — kullanıcı bildirimi; henüz kullanılmadı** | BERO'da doğrudan kontrol/aktüatör işlevi yok; bağımsız veri kaynağıdır. Kullanıcının değerlendirdiği olası görevler (henüz kesin karar yok): (1) yalnızca havalandırma hattının ana gözetmeni olmak veya (2) klima gibi yüksek akımlı yükleri ayrı tutarak genel ev akımının kalan bölümünü izlemek. 10 A sınıfının bilinçli tercih edilmiş olabileceği kullanıcı tarafından belirtildi; cihaz etiketi/ölçüm sınırları ve gerçek tesisat akımları doğrulanmadan bağlantı/topoloji kararı verilmeyecek. Bu görevler aday kullanım senaryolarıdır. Modül 4'ün PZEM-004T V3 akışından ayrı tutulacak. 10 A sınırı, havalandırma toplam akımı ve motor kalkış akımıyla birlikte cihaz etiketi/kılavuzundan doğrulanmadan bağlantı yapılmayacak. Koruma veya kontrol elemanı yerine geçmez. Haberleşme, register haritası, örnekleme/güncelleme hızı ve ölçüm davranışı henüz test edilmedi; slave adresi, baud/parity/stop bit ve USB arayüzünün işlevi ilk bağlantıda doğrulanacak. |
| AC güç/enerji ölçer | PZEM-004T V3 | UART / TTL seri haberleşme | En az bir PZEM-004T V3, PZEM-REF-WROOM-01 yayın düzeneğinde mevcut (kullanıcı bildirimi); Modül 4'te yeniden kullanım veya ayrı ünite kararı açık | PZEM-014 ile aynı cihaz değildir. Modül 4 ESP32 + ADS1115 + 100 A / 1 V SCT tasarımında PZEM'in hangi fiziksel ünitesinin kullanılacağı ayrıca kaydedilecek. |

## Modbus ve saha haberleşme donanımları

Aşağıdaki adetler kullanıcı tarafından bildirilen fiziksel envanterdir. Tam model/SKU ve cihaz revizyonu, cihaz etiketleri veya üretici dokümanları üzerinden ayrıca doğrulanacaktır.

| Donanım | Model / tanım | Adet | Kapasite / arayüz | Durum ve not |
|---|---|---:|---|---|
| Dijital I/O | Waveshare Modbus RTU IO 8CH | 2 | Her modülde 8 DI + 8 DO; RS485 / Modbus RTU | Mevcut; toplam 16 DI + 16 DO. Kullanıcı kullanım alanları: kapı zili, kapı/pencere/cam kontakları, akım gerektirmeyen butonlar ve diğer kuru kontak/dijital durum bildirimleri. Giriş elektriksel tipi, izolasyon, ortak uç ve kontak bağlantı sınırları ürün revizyonunun kılavuzundan doğrulanacak. Kullanıcı bildirimi: modülün kendi içinde koşul/olay oluştuğunda dijital çıkış tetikleme özelliği de bulunuyor; bu yerel mantık özelliğinin tam koşul türleri, zamanlama seçenekleri ve çalışma sınırları ürün revizyonunun kılavuzundan doğrulanacak. Uygun arayüz ve yük sınırları doğrulanmadan çıkışlar doğrudan saha yüküne bağlanmayacak. |
| Analog giriş | Waveshare Modbus RTU Analog Input 8CH | 2 | Her modülde 8 kanal; 0–5 V, 1–5 V, 0–20 mA veya 4–20 mA modları | Mevcut; toplam 16 analog giriş. Kullanıcının değerlendirdiği olası görevler: evin farklı noktalarındaki sıcaklıkları; havalandırma sistemindeki çeşitli analog sensörleri; mutfak gibi alanlarda Aqara bağımsız alarm cihazlarına ek olarak analog çıkışlı çevresel izleme sensörlerini (ör. duman yoğunluğu vericisi) okumak. Bu ek analog kanal güvenlik alarmının yerine geçmeyecek. Uygun sensör çıkışı/ölçeklendirme şart; çıplak NTC/PT100 gibi elemanlar doğrudan uyumlu kabul edilmeyecek. Üretici verisinde 12-bit çözünürlük, ≤%3 örnekleme doğruluğu ve 25 Hz veri güncelleme hızı belirtiliyor; gerçek sistem performansı sensör, kanal taraması ve Modbus sorgulamasıyla birlikte test edilecek. Hız yeterliliği uygulama bazında henüz doğrulanmadı. |
| Analog çıkış | Waveshare Modbus RTU Analog Output 8CH (B) | 1 | 8 kanal, 0–10 V | Mevcut; kullanıcı bildirimi: havalandırma motorlarının akıma bağlı hız referansını üretmek/yönetmek için değerlendirilecek. Motoru doğrudan sürmez; uygun sürücü veya 0–10 V girişli fan kontrolcüsüne referans sinyali vermesi hedefleniyor. Uygulama ve kontrol mantığı henüz doğrulanmadı. |
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



## Analog sinyal ve ses modülleri — 18.11.2026

| Donanım | Model / tanım | Adet | Kullanım amacı | Durum / kayıt sınırı |
|---|---|---:|---|---|
| Harici ADC modülü | ADS1115 tabanlı breakout | **10** | SCT013 analog sinyal okuma, ADC karakterizasyonu ve BERO ölçüm modülleri | Mevcut; kullanıcı bildirimi. Kart üreticisi/SKU/PCB revizyonu henüz doğrulanmadı. Her kart ayrı ADS1115-01…10 kimliğiyle test edilecek. [Donanım belgesi](../DONANIM/ADS1115/README.md) |
| Mikrofon yükselteç modülü | MAX4466 tabanlı | **Adet teyit edilecek** | Analog ses sinyali alma; PREBERO/BERO ses tabanlı deneyler | Mevcut; kullanıcı teslim aldığını bildirdi. Kesin adet, kart revizyonu, kapsül ve SKU fiziksel kontrolde kaydedilecek. [Donanım belgesi](../DONANIM/MAX4466/README.md) |

### Envanter kayıt ilkesi

- ADS1115 için 10 adet, kullanıcı bildirimi esaslı stok miktarıdır; on kartın aynı revizyon veya aynı performansta olduğu anlamına gelmez.
- Önceki farklı marka ADS1115 kartı yeni 10'lu gruptan ayrı tutulur.
- MAX4466 kaydı entegreyi değil, MAX4466 entegresi kullandığı belirtilen mikrofon breakout modülünü ifade eder. Kesin kart özellikleri fiziksel incelemeden sonra tamamlanacaktır.
- Üretici veri sayfası entegre özelliklerini açıklar; breakout kartındaki mikrofon kapsülü, potansiyometre, bağlantı sırası ve yardımcı devreleri tek başına doğrulamaz.


## I²C çoklayıcı modülleri — 18.11.2026

| Donanım | Model / tanım | Adet | Kullanım amacı | Durum / kayıt sınırı |
|---|---|---:|---|---|
| I²C multiplexer | TCA9548A, 8 kanallı I²C switch breakout | **2** | Aynı I²C hattında aynı adrese sahip ADS1115 gibi cihazları ayrı kanallardan seçerek kullanma | **2 adet sipariş edildi; teslimat bekleniyor.** Kart üreticisi, PCB revizyonu, pin sırası ve pull-up yapısı teslimatta doğrulanacak. [Donanım belgesi](../DONANIM/TCA9548A/README.md) |

- İki TCA9548A kartının her biri sekiz kanal sunar; toplam kanal sayısı teorik olarak 16'dır. Gerçek sistem topolojisi ve aynı hatta birlikte kullanım henüz test edilmemiştir.
- TCA9548A, I²C kanal anahtarıdır; I²C master veya ADC değildir.

## Fiziksel ESP cihaz envanteri

ESP kartları modüllerden ve görevlerden bağımsız fiziksel varlıklardır. Her fiziksel karta kart modeli ve mümkünse MAC/seri gibi ayırt edici bilgi doğrulandıktan sonra kalıcı ve benzersiz envanter kimliği atanır. Eşleme yapılana kadar işlevi anlatan geçici bir etiket kullanılabilir. Aynı kart farklı modüllerde veya görevlerde kullanılsa da kalıcı kimlik değişmez.

| Envanter kimliği | Kart modeli | Fiziksel ayırt edici bilgi | Sabit ESPHome / HA cihaz adı | Mevcut atama | Durum |
|---|---|---|---|---|---|
| Kalıcı ESP ID bekliyor; geçici işlev etiketi **PZEM-REF-WROOM-01** | ESP32-WROOM ailesi; geliştirme kartının tam modeli/revizyonu bekliyor | Kullanıcı mevcut PZEM yayıncısı olarak teyit etti; MAC/seri etiketi görülünce eşleştirilecek | `bero-modul3-wroom` (eski yapılandırma adı; cihaza yüklü sürüm ayrıca doğrulanacak) | PZEM karşılaştırma yayımlayıcısı; MOD2 masaüstü deneylerinde referans | Fiziksel kart mevcut; kalıcı kimlik ve kurulu firmware teyidi bekliyor |

**Kayıt kuralı:** Kalıcı kimlik fiziksel kart tek tek doğrulanınca atanır. Kart modeli ve MAC/seri bilgisi teyit edilene kadar işlev etiketi kullanılır; bu geçici etiket kalıcı fiziksel ID gibi sunulmaz. Modül ve görev kimliği ESP'nin fiziksel envanter kimliği değildir.
