# Fiziksel donanım envanteri

**Durum: KISMEN HAZIR.** SCT013-100A-1V, SCT013-30A-1V ve PZEM-004T V3.0 için önceki BERO teknik Markdown belgeleri [proje referans klasörüne](references/README.md) kopyalandı. Genel ürün özellikleri yeniden yazılmayacak; bu envanter bu projeye ait seçimi ve gerçek devre ayrıntılarını izler.

| Öğe | Mevcut BERO referansı | Bu proje için kayıtlı durum | Kalan adım |
|---|---|---|---|
| SCT seçimi | [SCT013-100A-1V](references/SCT013-100A-1V.md) ve [SCT013-30A-1V](references/SCT013-30A-1V.md) | İki varyantın teknik kayıtları ve geçmiş notları mevcut; hangisinin bu projede kullanılacağı yazılmadı. | Önceki kayıtlar bu projedeki aynı fiziksel parçayı belirliyorsa o kanıtı bağla; aksi halde hangi varyantın kullanılacağını belirle. |
| PZEM | [PZEM-004T V3.0](references/PZEM-004T-V3.0.md) | Aile belgesi ve geçmiş ESP32D1/ESPHome başarılı haberleşme notu mevcut; bu projedeki 10 A/100 A fiziksel varyantı kesin değil. | Kullanılan modül varyantını ve CT gerekip gerekmediğini/CT modelini mevcut kayıtlarla doğrula. |
| MCU | [ESP32-WROOM-32D BERO kaydı](../../../DONANIM/ESP32-WROOM-32D/README.md) | Aday donanım kaydı var; bu projedeki fiziksel kart/revizyon kaydı yok. | Önceki çalışma kanıtını bağla veya kart kimliğini kaydet. |
| ADC | [MCP3208 BERO kaydı](../../../DONANIM/MCP3208/README.md) | Aday donanım kaydı var; bu projedeki gerçek ADC ve VREF doğrulanmadı. | Fiziksel ADC modelini/revizyonunu ve VREF kaynağını kaydet. |
| Analog ön uç | SCT referanslarındaki tarihsel bias/VREF notları | Yaklaşık 1,67 V bias ve 3,12 V VREF geçmiş notlarda geçiyor; bu projenin güncel ölçümü olarak kabul edilmez. | Gerçek devre kaydı ve gerekiyorsa güvenli düşük gerilim tarafı ölçümüyle doğrula. |
| Referans cihaz | True-RMS ampermetre | Bu proje için model/kalibrasyon durumu kayıtlı değil. | Mevcut geçmiş kaydı bul veya T003 kapsamında tanımla. |
| Yükler | Rezistif / diğer kontrollü yükler | Üç akım seviyesine karşılık gelen mevcut yük kimlikleri kayıtlı değil. | Mevcut kayıt varsa bağla; yoksa T003 kapsamında belirle. |

## Kayıt kuralları
- Önceki BERO teknik belgelerindeki ürün bilgilerini yeniden yazma; ilgili referans dosyasına bağlantı ver.
- Önceki test notları yalnızca kendi kayıt kapsamı içinde kanıttır. Başarılı UART haberleşmesi ölçüm doğruluğu veya kalibrasyon kanıtı değildir.
- Kaynak belgelerdeki eski VREF/bias gibi değerleri bu düzeneğe fiziksel olarak doğrulanmış gibi taşıma.
- Her proje-özel doğrulamada tarih ve kanıt yolu ekle. Boşluğu varsayımla doldurma.
