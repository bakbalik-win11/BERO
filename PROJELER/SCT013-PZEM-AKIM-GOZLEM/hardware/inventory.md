# Fiziksel donanım envanteri

**Durum: KISMEN HAZIR.** Teknik referanslar [hardware/references/](references/README.md) altına kopyalandı. Bu envanter, önceki BERO bilgilerini tekrar yazmak yerine bu projede seçilen donanımı ve kalan proje-özel kararları kaydeder.

## Stok ve seçimler

| Kalem | Kaydedilen bilgi | Kaynak / durum |
|---|---|---|
| Öncelikli akım sensörü | **SCT013-030 — 30 A / 1 V** | Kullanıcı kararı; bu projede ilk tercih. |
| SCT013-030 stok | **7 adet** | Kullanıcı bildirimi; bağımsız sayım yapılmadı. Paylaşılan fotoğrafta SCT013 30 A / 1 V etiketi görülüyordu; fotoğraf bu sohbette, henüz depoda değil. |
| SCT013-100A-1V stok | **10 adet** | Kullanıcı bildirimi; alternatif stok. |
| 100 nF / 50 V seramik kondansatör | **10 adet bildirilmiş stok; 1 adet bias bölücüsünde kullanılıyor** | Kullanıcı bildirimi. Breadboarddaki kondansatör üzerindeki işaret 104 olarak düzeltildi; 104 = 100 nF. Kalan stok fiziksel olarak sayılmadı. |
| ESP32-WROOM-32D geliştirme kartı | **2 adet** | Kullanıcı bildirimi ve fotoğraflar; teknik referans [burada](../../../DONANIM/ESP32-WROOM-32D/README.md). Bağımsız sayım yapılmadı. |
| ESP32-WROOM-32E geliştirme kartı | **1 adet** | Kullanıcı bildirimi ve fotoğraf; bağımsız sayım yapılmadı. |
| ESP-WROOM-32 tabanlı NodeMCU ESP32 Bluetooth geliştirme kartı | **1 adet** | Kullanıcı bildirimi ve görsel. Tam kart üreticisi/PCB revizyonu okunmuyor; önceki WROOM-32S satırı bununla değiştirildi. |
| SSR kartı | **1 adet SAMM Market 5 V 2 kanallı kart** | Kullanıcı satın alma bağlantısını verdi. Tedarikçi kodu İzmo9659, SKU MP02637; ürün sayfasında OMRON/fototriyak/zero-cross belirtilmiş. |
| DS3231 RTC | **Projede kullanılacak** | Kullanıcı kararı; teknik referans mevcut BERO kaydından kopyalandı. Bu projedeki fiziksel modül revizyonu/adedi ayrıca doğrulanmadı. |

Stok adetleri kullanıcı tarafından bildirilmiştir; bağımsız fiziksel sayım gibi sunulmaz.

## Donanım konfigürasyonu

| Öğe | Mevcut BERO referansı | Bu proje için durum | Kalan adım |
|---|---|---|---|
| SCT | [SCT013-30A-1V](references/SCT013-30A-1V.md); [SCT013-100A-1V](references/SCT013-100A-1V.md) | SCT013-030 (30 A / 1 V) öncelikli; 100 A / 1 V alternatif stok. | Genel model bilgisi hazır; fiziksel fotoğrafı depoya arşivlemek isteğe bağlı kanıt düzenlemesi. |
| PZEM ve CT | [Ana BERO kaydı](../../../DONANIM/PZEM-004T/README.md); [proje içi referans kopyası](references/PZEM-004T-V3.0.md) | PZEM-004T V3.0; kullanıcı CT modelini **PZCT-02 (0–100 A)** olarak belirtti. Fotoğrafta bu CT'nin PZEM'e bağlı olduğu gösterildi. Bu, 100 A harici CT düzenidir. | Donanım kimliği ve CT modeli belirlendi. MCU bağlantısı yapılırken UART lojik seviyesi/izolasyon gereksinimleri kontrol edilecek. Fotoğrafı ayrıca depoya kopyalamak gerekmiyor. |
| ESP32 / MCU | [ESP32-WROOM-32D teknik kaydı](../../../DONANIM/ESP32-WROOM-32D/README.md) | **İlk aşama için 4 kart:** 2× WROOM-32D, 1× WROOM-32E, 1× genel ESP-WROOM-32 NodeMCU ESP32 Bluetooth. Kullanıcı kararı; bağımsız sayım yapılmadı. | Kartların görev/firmware rolünü belirle. Genel NodeMCU kartının tam PCB revizyonu ve pin etiketleri kablolama öncesi doğrulansın. |
| ADC | [MCP3208 BERO kaydı](../../../DONANIM/MCP3208/README.md) | BERO'da ADC referansı var; bu projede fiziksel ADC ve VREF'in kullanımı henüz doğrulanmadı. | Gerçek ADC modelini/revizyonunu ve VREF kaynağını kaydet. |
| DS3231 RTC | [Proje içi teknik kopya](references/DS3231.md); [resmî veri sayfası bağlantısı](references/DS3231-datasheet.md) | Takvim/saat bilgisi ve olay/ölçüm kayıtlarına mutlak zaman damgası sağlamak için kullanılacak. | Modül revizyonu, besleme, I²C SDA/SCL pinleri, pull-up seviyesi, yedek pil/şarj devresi ve ilk saat ayarlama yöntemi doğrulanmalı. Hassas 200 ms pencereler ESP32 zamanlayıcısıyla yürütülmeli. |
| Bias üretim alt devresi | Aşağıdaki “Bias trafosu” bölümü | **TAMAMLANDI — kullanıcı onayı.** | Yeni parça bilgisi beklenmiyor; SCT sinyalinin bias noktasına kuplajı analog ön uç entegrasyonunda ele alınacak. |
| SSR | [SSR donanım referansı](references/SSR.md); [ürün/model eşleştirme notu](references/SSR-datasheet-candidate.md) | SAMM Market 5 V 2 kanal, tedarikçi kodu İzmo9659 / SKU MP02637. Ürün sayfası OMRON, fototriyak, zero-cross; her kanal için 75–264 VAC, 0,1–2 A; kart beslemesi 5 V / tüm kanallar açıkken 160 mA bildiriyor. | Hangi iki AC yükün anahtarlanacağı, gerçek giriş tetik mantığı, giriş akımı, kanal eşzamanlı termal sınırları ve kart üzerindeki SSR entegresinin tam model kodu doğrulanmalı. |
| Referans cihaz | True-RMS ampermetre | Bu projeye ait model/kalibrasyon durumu kayıtlı değil. | T003 kapsamında belirle. |
| Yükler | Rezistif / diğer kontrollü yükler | Üç akım seviyesine karşılık gelen yük kimlikleri kayıtlı değil. | T003 kapsamında belirle. |

## Bias trafosu — tamamlandı

**Durum: TAMAMLANDI (kullanıcı onayı, 2026-10-27).** Temiz yaklaşık 1,65 V bias üretimi için gereken alt devre kullanıcı tarafından tamamlanmış sayıldı.

- **Korunaklı kutu içi:** RN130421, 6 V AC / 2,0 VA PCB tipi trafo → KBU6M, 6 A / 1000 V köprü doğrultucu → 2200 µF / 35 V elektrolitik filtre kondansatörü → L78L33, TO-92 regülatör.
- **Ayrı breadboard:** 2 × 10 kΩ bias bölücü; orta noktada yaklaşık 1,65 V. Orta noktadan GND'ye bir adet 104 kodlu seramik kondansatör (100 nF) bağlı.
- **Stok bilgisi:** 100 nF / 50 V seramikten toplam 10 adet olduğu bildirildi; bunlardan 1 tanesi bias breadboardunda kullanılıyor. Kalan stok ayrıca sayılmadı.
- Bu tamamlanma, kullanıcının kurulumun hazır olduğuna dair onayıdır. Bu oturumda bağımsız voltmetre ölçüm raporu veya osiloskop kaydı eklenmedi.

## SSR kaynak notu

Kaynak [DONANIM/SSR/README.md](../../../DONANIM/SSR/README.md) önceki ESP32-C3 / GPIO6 test düzeneğini anlatıyordu. Kullanıcının satın alma bağlantısı kartı 5 V, 2 kanallı SAMM Market ürünü (İzmo9659 / MP02637) olarak kesinleştirdi. Omron G3MB veri sayfası, fiziksel SSR entegrenin tam kodu okunmadığı için yalnız karşılaştırma kaynağıdır. Ürün sayfasındaki LOW/HIGH eşikleri ile “low-level trigger” notu arasında tutarsızlık olduğundan kontrol mantığı, enerjisiz/ düşük gerilimli masa testinde doğrulanmalıdır. İki kanalın yükleri ve GPIO eşlemesi daha sonra seçilecektir.

## Kalan proje-özel bilgiler

1. Kullanılacak ESP32 modülü ve geliştirme kartı/revizyonu; kullanılacak ADC modeli ve VREF kaynağı.
2. SCT'nin AC sinyalinin tamamlanmış yaklaşık 1,65 V bias noktasına kuplaj yöntemi; analog ön uç burden/filtre ve güvenli ADC giriş aralığı.
3. True-RMS referans cihazı ve en az üç kontrollü yük seviyesi.

## Kayıt kuralları
- Önceki BERO teknik belgelerindeki ürün bilgilerini tekrar yazmak yerine ilgili referansa bağlan.
- Önceki test notları yalnız kendi kayıt kapsamları için kanıttır; yeni deney veya kalibrasyon sonucu gibi sunulmaz.
- Kullanıcı tarafından bildirilen stokları “kullanıcı bildirimi” olarak etiketle.
- Bu projede ölçülmemiş değerleri ölçülmüş gibi yazma.
