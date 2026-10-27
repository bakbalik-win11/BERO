# Fiziksel donanım envanteri

**Durum: KISMEN HAZIR.** SCT ve PZEM teknik referansları [proje referans klasöründe](references/README.md) bulunur. Bu envanter genel ürün özelliklerini tekrar yazmak yerine proje seçimini, kullanıcı tarafından bildirilen stokları ve bu düzeneğe ait eksik bilgileri izler.

## Proje önceliği ve stok bildirimi

| Kalem | Kaydedilen bilgi | Bilgi kaynağı / durum |
|---|---|---|
| Öncelikli akım sensörü | **SCT013-030 — 30 A / 1 V** | Kullanıcı kararı, 2026-10-27. Bu projede önce bu model kullanılacak. |
| SCT013-030 stok adedi | **7 adet** | Kullanıcı bildirimi, 2026-10-27; bağımsız sayım yapılmadı. Bu oturumda sunulan görselde SCT013 / 30 A / 1 V etiketi okunuyor; görsel henüz depodaki `hardware/photos/` klasörüne dosya olarak eklenmedi. |
| SCT013-100A-1V stok adedi | **10 adet** | Kullanıcı bildirimi, 2026-10-27; bağımsız sayım yapılmadı. Alternatif stok olarak kaydedildi, öncelikli seçim değil. |
| 100 nF / 50 V seramik kondansatör | **10 adet** | Kullanıcı bildirimi, 2026-10-27; bağımsız sayım yapılmadı. Belirli bir devre konumuna atanmadı; filtre/bypass kullanımı ancak gerçek devre tasarımıyla kararlaştırılacak. |

**Not:** Stok adetleri kullanıcı tarafından bildirilen miktarlardır; depoda fiziksel sayım yapılmış gibi sunulmaz. SCT modeli seçimi, gerçek ünitenin kalıcı fotoğraf kanıtı ve kalibrasyon sonucu birbirinden ayrı kayıtlardır.

## Donanım konfigürasyonu

| Öğe | Mevcut BERO referansı | Bu proje için kayıtlı durum | Kalan adım |
|---|---|---|---|
| SCT seçimi | [SCT013-030](references/SCT013-30A-1V.md); [SCT013-100A-1V](references/SCT013-100A-1V.md) | Öncelik SCT013-030, 30 A / 1 V. SCT013-100A-1V alternatif stokta. | Kullanılan fiziksel ünitenin etiketi için kalıcı kanıt yolu ekle; genel teknik özellikleri tekrar araştırma. |
| PZEM | [PZEM-004T V3.0](references/PZEM-004T-V3.0.md) | Aile belgesi ve geçmiş ESP32D1/ESPHome başarılı haberleşme notu mevcut; bu projedeki 10 A/100 A fiziksel varyantı kesin değil. | Kullanılan modül varyantını ve CT gerekip gerekmediğini/CT modelini mevcut kayıtlarla doğrula. |
| MCU | [ESP32-WROOM-32D BERO kaydı](../../../DONANIM/ESP32-WROOM-32D/README.md) | Aday donanım kaydı var; bu projedeki fiziksel kart/revizyon kaydı yok. | Önceki çalışma kanıtını bağla veya kart kimliğini kaydet. |
| ADC | [MCP3208 BERO kaydı](../../../DONANIM/MCP3208/README.md) | Aday donanım kaydı var; bu projedeki gerçek ADC ve VREF doğrulanmadı. | Fiziksel ADC modelini/revizyonunu ve VREF kaynağını kaydet. |
| Analog ön uç | SCT referanslarındaki tarihsel bias/VREF notları | Yaklaşık 1,67 V bias ve 3,12 V VREF geçmiş notlarda geçiyor; bu projenin güncel ölçümü olarak kabul edilmez. | Gerçek devre kaydı ve gerekiyorsa güvenli düşük gerilim tarafı ölçümüyle doğrula. |
| Pasif bileşen | 100 nF / 50 V seramik kondansatör, 10 adet bildirildi | Stok kaydı kullanıcı bildirimi. | Gerçek şemada bağlantı yeri ve kullanım amacı belirlenmeden tasarım kararı sayılmaz. |
| Referans cihaz | True-RMS ampermetre | Bu proje için model/kalibrasyon durumu kayıtlı değil. | Mevcut geçmiş kaydı bul veya T003 kapsamında tanımla. |
| Yükler | Rezistif / diğer kontrollü yükler | Üç akım seviyesine karşılık gelen mevcut yük kimlikleri kayıtlı değil. | Mevcut kayıt varsa bağla; yoksa T003 kapsamında belirle. |

## Kayıt kuralları
- Önceki BERO teknik belgelerindeki ürün bilgilerini yeniden yazma; ilgili referans dosyasına bağlantı ver.
- Önceki test notları yalnızca kendi kayıt kapsamı içinde kanıttır. Başarılı UART haberleşmesi ölçüm doğruluğu veya kalibrasyon kanıtı değildir.
- Kaynak belgelerdeki eski VREF/bias gibi değerleri bu düzeneğe fiziksel olarak doğrulanmış gibi taşıma.
- Kullanıcı tarafından bildirilen stok miktarlarını “kullanıcı bildirimi” olarak etiketle; fiziksel sayım yapılmış gibi gösterme.
- Her proje-özel doğrulamada tarih ve kanıt yolu ekle. Boşluğu varsayımla doldurma.
