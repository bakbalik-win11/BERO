# Fiziksel donanım envanteri

**Durum: KISMEN HAZIR.** Kullanıcı tarafından bildirilen fiziksel stok, ESP32 kart/modül çeşitleri, güç kaynağı, test yükü ve önceden hazırlanmış 8 kanallı bias/direnç kartı kaydedildi. T001'in kabulü için SCT analog örneklemesinde kullanılacak fiziksel kartın fotoğraf/etiketle eşleştirilmesi ve analog giriş ayrıntılarının doğrulanması gerekiyor.

## Stok ve seçimler

| Kalem | Kaydedilen bilgi | Kaynak / durum |
|---|---|---|
| SCT013-030 stok | 7 adet, 30 A / 1 V, jack çıkışlı | Kullanıcı bildirimi |
| SCT013-100A-1V stok | 10 adet, 100 A / 1 V, jack çıkışlı | Kullanıcı bildirimi |
| Jack yuvaları | Mevcut | Kullanıcı bildirimi |
| ESP32-C3 SuperMini | 1 adet | Önceki SSR kontrol düğümünde kullanıldı; kullanıcı tüm parçaların elinde olduğunu bildirdi |
| ESP32-WROOM-32D tabanlı kart/modül | 2 adet | BERO envanter kaydı; bu projede SCT ADC için seçilen kart olduğu henüz belirtilmedi |
| ESP32-WROOM-32E tabanlı kart/modül | 1 adet | BERO envanter kaydı; bu projede SCT ADC için seçilen kart olduğu henüz belirtilmedi |
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

## Önceden hazırlanmış bias üretim alt devresi

**Durum: TAMAMLANDI — kullanıcı onayı.** Mevcut BERO kaydına göre kutu içinde RN130421 6 V AC / 2,0 VA trafo, KBU6M köprü doğrultucu, 2200 µF / 35 V filtre kondansatörü ve L78L33 regülatör; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) kondansatör bulunuyor. Bu, bias üretim alt devresinin hazır olduğu bilgisidir; SCT AC sinyalinin bias noktasına kuplajı ayrıca tanımlanmalıdır. Bağımsız ölçüm raporu bu kayda eklenmemiştir.

## Donanım konfigürasyonu ve açık teknik maddeler

| Öğe | Mevcut durum | Kalan adım |
|---|---|---|
| SCT | 30 A / 1 V öncelikli; 100 A / 1 V alternatif stok | Kullanılacak kanal/sensör eşlemesini belirle |
| MCU | 2 × WROOM-32D, 1 × WROOM-32E, 1 × genel NodeMCU ESP32; ayrıca ESP32-C3 SuperMini SSR düğümü | SCT ADC için kullanılacak fiziksel kartı fotoğraf/etiket ve PCB revizyonuyla eşleştir |
| Dahili ADC | İlk aşamada ESP32 dahili ADC'si kullanılacak | Seçilen kartın ADC destekli GPIO'sunu ve giriş aralığını doğrula; attenuation/ADC yapılandırmasını kaydet |
| Harici ADC | MCP3208 mevcut, ileriki aşamaya ayrıldı | İlk aşamada kullanılmayacak |
| Analog ön uç | 8 kanal, her kanalda ayrı bias ve direnç ağı; SCT sinyali ESP32 ADC'ye aktarılacak | SCT AC sinyalinin bias noktasına kuplajı, direnç/filtre değerleri ve güvenli ADC aralığı belgelenmeli |
| PZEM ve CT | PZEM-004T V3.0; CT modeli kullanıcı tarafından PZCT-02 (0–100 A) olarak belirtildi | MCU bağlantısında UART lojik seviyesi ve izolasyon gereksinimlerini kontrol et |
| DS3231 | RTC referansı mevcut | Breakout revizyonu, SDA/SCL pinleri, pull-up seviyesi, yedek pil/şarj devresi ve ilk saat ayarlama yöntemi doğrulanmalı |
| SSR | SAMM Market 5 V, 2 kanal, İzmo9659 / MP02637 | İki AC yük, GPIO eşlemesi, tetik mantığı ve termal sınırlar güvenli biçimde doğrulanmalı |
| Referans cihaz | Model kaydı yok | T003 kapsamında True-RMS ampermetre ve izlenebilirlik durumu kaydedilmeli |
| Yükler | Lamba mevcut; diğer kontrollü yük seviyeleri tanımlı değil | T003 kapsamında en az üç kontrollü yük seviyesi belirlenmeli |

## Kayıt kuralları
- Önceki BERO teknik belgelerindeki ürün bilgilerini tekrar yazmak yerine ilgili referansa bağlan.
- Önceki test notları yalnız kendi kayıt kapsamları için kanıttır; yeni deney veya kalibrasyon sonucu gibi sunulmaz.
- Kullanıcı tarafından bildirilen stokları kullanıcı bildirimi olarak etiketle.
- Bu projede ölçülmemiş değerleri ölçülmüş gibi yazma.
- Fotoğraf dosyasına erişilemiyorsa fotoğraftan model/revizyon doğrulanmış gibi işaretleme.
