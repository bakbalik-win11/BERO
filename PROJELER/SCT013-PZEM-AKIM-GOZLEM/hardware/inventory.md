# Fiziksel donanım envanteri

**Durum: KISMEN HAZIR.** Kullanıcı tarafından bildirilen fiziksel stok, ESP32 kart/modül çeşitleri, güç kaynağı, test yükü ve önceden hazırlanmış 8 kanallı bias/direnç kartı kaydedildi. T001'in kabulü için SCT analog örneklemesinde kullanılacak fiziksel kartın fotoğraf/etiketle eşleştirilmesi ve analog giriş ayrıntılarının doğrulanması gerekiyor.

## Stok ve seçimler

| Kalem | Kaydedilen bilgi | Kaynak / durum |
|---|---|---|
| SCT013-030 stok | 7 adet, 30 A / 1 V, jack çıkışlı | Kullanıcı bildirimi |
| SCT013-100A-1V stok | 10 adet, 100 A / 1 V, jack çıkışlı | Kullanıcı bildirimi |
| Jack yuvaları | Mevcut | Kullanıcı bildirimi |
| ESP32-C3 SuperMini | 1 adet | Kullanıcının bu turda paylaştığı fotoğraf kartı ESP32-C3 SuperMini olarak tanımlıyor; kullanıcı SSR kontrolü ve zamanlama kodunun bu karta ait olduğunu belirtti |
| ESP32-WROOM-32D tabanlı kart/modül | 2 adet | Kullanıcı fotoğrafında ESP32-WROOM-32D metal kalkanlı kart görsel olarak eşleştirildi; kullanıcı bu iki kartı SCT013 ölçümünde kullanacağını belirtti |
| ESP32-WROOM-32E tabanlı kart/modül | 1 adet | Kullanıcı bu kartı da SCT013 ölçümünde kullanacağını belirtti |
| Genel ESP-WROOM-32 tabanlı NodeMCU ESP32 kartı | 1 adet | BERO envanter kaydı; kart üreticisi/revizyonu ve fotoğrafla eşleşmesi proje kaydında net değil |
| ESP32 ölçüm düğümü | 1 adet | Önceki PZEM ölçüm düğümünde kullanıldı; fiziksel kart modeli yukarıdaki stoktan kesin eşleştirilmedi |
| PZEM-004T | V3.0 | Kullanıcı bildirimi; ayrıntı için [mevcut BERO kaydı](../../../DONANIM/PZEM-004T/README.md) |
| SSR kartı | SAMM Market 5 V, 2 kanal | Tedarikçi kodu İzmo9659, SKU MP02637; kart üzerindeki SSR'nin tam kodu ayrıca doğrulanmalı |
| RTC | DS3231 | Mevcut BERO referansı kullanılıyor; fiziksel breakout ayrıntıları ayrıca doğrulanmalı |
| Güç kaynağı | Masaüstü 5 V / 1,8 A | Kullanıcı bildirimi |
| Test yükü | Lamba | Kullanıcı bildirimi |
| Bağlantı ve ölçüm parçaları | Tam takım mevcut | Kullanıcı bildirimi |

**Toplam SCT013: 17 adet.** Bu adetler kullanıcı bildirimi olup bağımsız fiziksel sayım değildir.

## Hazır analog arayüz kartı

Kullanıcı daha önce **8 kanallı, her kanalında ayrı bias ve direnç ağı bulunan bir kart** hazırlamıştır. Jack yuvaları da mevcuttur. Kullanıcının tarif ettiği bağlantı:

**SCT013 → jack yuvası → ayrı bias/direnç ağı olan 8 kanallı kart → ESP32'nin dahili ADC girişi**

İlk aşamada MCP3208 kullanılmayacak; fiziksel olarak mevcut olan MCP3208 ileriki aşama için ayrılmıştır.

## SCT ölçüm kartı ve test düzeni

Kullanıcı kararı ve hedef mimari:

- **Zamanlayıcı/olay üreticisi:** ESP32-C3 SuperMini, SSR yükünü açıp kapatır ve her geçiş için olay/paket bilgisi üretir. Mevcut ADR-006 tasarım kaydında 40 s ON / 20 s OFF, UDP broadcast port 4210 ve `BERO_EVT,BOOT_ID=XXXXXXXX,EVENT_ID=N,STATE=ON|OFF` biçimi tanımlıdır.
- **Üç hızlı örnekleme düğümü:** 2 × ESP32-WROOM-32D + 1 × ESP32-WROOM-32E. Her biri SCT013 sensöründen ham/anlık gerilim örneklerini hızlı biçimde alır; bu aşamada akım veya RMS hesabı yapmaz.
- **Çıktı hedefi:** Her örnekleme düğümü sensör gerilim örneklerini zamanlayıcıdan gelen olay/paket bilgisiyle birlikte yazdırır; böylece örnekler SSR'nin ON/OFF olayına bağlanabilir. Paket alımı/teslimi ve örnekleme zamanlaması testle doğrulanmalıdır.
- **Sarım testleri:** Aynı hatta iletkenin SCT içinden 1, 2 ve 4 sarım geçirilmesi ayrı ayrı denenir.

Bu, hedef mimari ve test planıdır; henüz ölçüm sonucu veya GPIO eşlemesi değildir.

## Önceden hazırlanmış bias üretim alt devresi

**Durum: TAMAMLANDI — kullanıcı onayı.** Mevcut BERO kaydına göre kutu içinde RN130421 6 V AC / 2,0 VA trafo, KBU6M köprü doğrultucu, 2200 µF / 35 V filtre kondansatörü ve L78L33 regülatör; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) kondansatör bulunuyor. Bu, bias üretim alt devresinin hazır olduğu bilgisidir; SCT AC sinyalinin bias noktasına kuplajı ayrıca tanımlanmalıdır. Bağımsız ölçüm raporu bu kayda eklenmemiştir.

## Donanım konfigürasyonu ve açık teknik maddeler

| Öğe | Mevcut durum | Kalan adım |
|---|---|---|
| SCT | 30 A / 1 V öncelikli; 100 A / 1 V alternatif stok | Kullanılacak kanal/sensör eşlemesini belirle |
| MCU | SCT ölçümü için 2 × ESP32-WROOM-32D ve 1 × ESP32-WROOM-32E; SSR kontrolü/zamanlama için ayrı ESP32-C3 SuperMini | ADC destekli GPIO ve pin eşlemesi firmware/pin planlama aşamasında, seçilen fiziksel kart ve teknik belgeyle doğrulanacak; T001’de pin numarası şartı değil |
| Dahili ADC | İlk aşamada ESP32 dahili ADC'si kullanılacak; harici ADC modeli seçilmiş sayılmıyor | Firmware aşamasında, seçilen kart/pin için ADC destekli GPIO, giriş aralığı ve attenuation/ADC yapılandırmasını teknik belgeyle doğrula |
| Harici ADC | MCP3208 mevcut, ileriki aşamaya ayrıldı | İlk aşamada kullanılmayacak |
| Analog ön uç | 8 kanal, her kanalda ayrı bias ve direnç ağı; SCT sinyali ESP32 ADC'ye aktarılacak | SCT AC sinyalinin bias noktasına kuplajı, direnç/filtre değerleri ve güvenli ADC aralığı belgelenmeli |
| PZEM ve CT | PZEM-004T için [mevcut BERO donanım kaydı](../../../DONANIM/PZEM-004T/README.md) esas alınır; bağlı CT modeli kullanıcı beyanıyla PZCT-02 (0–100 A) | Bu projede yeniden donanım belgesi açma veya CT modelini tekrar sorma; entegrasyon sırasında UART lojik seviyesi ve izolasyon gereksinimlerini kontrol et |
| DS3231 | RTC referansı mevcut | Breakout revizyonu, SDA/SCL pinleri, pull-up seviyesi, yedek pil/şarj devresi ve ilk saat ayarlama yöntemi doğrulanmalı |
| SSR | SAMM Market 5 V, 2 kanal, İzmo9659 / MP02637 | İki AC yük, GPIO eşlemesi, tetik mantığı ve termal sınırlar güvenli biçimde doğrulanmalı |
| Referans cihaz | Model kaydı henüz yok | T003 kapsamında True-RMS referans cihazının marka/modeli ve kalibrasyon/izlenebilirlik durumu kaydedilmeli |
| Yükler | Lamba mevcut; üç kontrollü yük seviyesi henüz tanımlı değil | T003 kapsamında lamba dâhil en az üç kontrollü akım seviyesi için yük senaryoları, etiket gücü ve güvenli kullanım koşulları belirlenmeli |

## Kayıt kuralları
- Önceki BERO teknik belgelerindeki ürün bilgilerini tekrar yazmak yerine ilgili referansa bağlan.
- Önceki test notları yalnız kendi kayıt kapsamları için kanıttır; yeni deney veya kalibrasyon sonucu gibi sunulmaz.
- Kullanıcı tarafından bildirilen stokları kullanıcı bildirimi olarak etiketle.
- Bu projede ölçülmemiş değerleri ölçülmüş gibi yazma.
- Fotoğraf dosyasına erişilemiyorsa fotoğraftan model/revizyon doğrulanmış gibi işaretleme.
