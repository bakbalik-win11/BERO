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
| Pasif bileşen | 100 nF / 50 V seramik kondansatör, 10 adet bildirildi | Stok kaydı kullanıcı bildirimi; bias alt devresinde kaç adet kullanıldığı belli değil. | Devredeki kondansatör sayısını, yerini ve rolünü şema/fotoğrafla belirt. |
| Bias trafo | RN130421, 6 V AC / 2,0 VA PCB tipi trafo | Kullanıcı tarafından bu alt devrenin trafo kaynağı olarak bildirildi; “bias trafosu” adı kullanıcı terminolojisidir. | Primer/sekonder bağlantısı, sekonderden sonraki doğrultma ve bu trafoyu gerçekten kullanan devre fotoğrafı/şeması kaydedilmeli. |
| Bias regülatörü | L78L33, TO-92 | Kullanıcı tarafından bias alt devresinde bildirildi; nominal 3,3 V regülatör olarak tanımlanıyor. | Parça üzerindeki işaret, pin yönü ve gerçek devredeki giriş/çıkış bağlantısı teyit edilmeli. |
| Bias bölücü | 2 × 10 kΩ, orta nokta ≈ 1,65 V hedefi | Kullanıcı beyanı; iki eşit direnç 3,3 V rayından beslendiğinde nominal orta nokta 1,65 V olur. | Üst/alt uçların hangi ray/toprağa bağlı olduğunu, bias düğümünün nerelere gittiğini ve ölçülen gerçek DC değerini kaydet. |
| Referans cihaz | True-RMS ampermetre | Bu proje için model/kalibrasyon durumu kayıtlı değil. | Mevcut geçmiş kaydı bul veya T003 kapsamında tanımla. |
| Yükler | Rezistif / diğer kontrollü yükler | Üç akım seviyesine karşılık gelen mevcut yük kimlikleri kayıtlı değil. | Mevcut kayıt varsa bağla; yoksa T003 kapsamında belirle. |

## Bias trafosu — mevcut tarif

**Kaynak:** Kullanıcı açıklaması, 2026-10-27. Bu, devreyi nasıl kurma niyetini kaydeder; tam şema veya ölçüm kanıtı değildir.

- Trafo: RN130421, 6 V AC / 2,0 VA, PCB tipi.
- Regülatör: L78L33, TO-92.
- Bias bölücü: 2 adet 10 kΩ; kullanıcı orta noktadan temiz yaklaşık 1,65 V aldığını bildiriyor.
- “Bias trafosu”: kullanıcının bu alt devre için kullandığı ad.
- Kondansatör stoku: 100 nF / 50 V seramikten 10 adet kullanıcı tarafından bildirildi. Bu alt devrede bunlardan kaç adet olduğu ve nerelere bağlandığı henüz belirtilmedi.

### Eksik devre bilgileri

1. 6 V AC sekonderden L78L33 girişine kadar doğrultucu/diyot düzeni ve DC filtreleme nasıl yapılıyor?
2. Kondansatörlerin tam değerleri, adetleri ve konumları nedir (trafo sekonderi, regülatör girişi/çıkışı, bias düğümü vb.)?
3. İki 10 kΩ direncin üst ucu, alt ucu ve orta noktası devrede nereye bağlanıyor?
4. SCT analog sinyali 1,65 V bias noktasına hangi bağlantı/kuplaj elemanıyla ekleniyor?
5. Tasarım amacı “sadece izole ve temiz DC bias üretmek” mi, yoksa bias düğümünde şebeke gerilimindeki değişimi temsil eden AC bileşen de mi amaçlanıyor?

**Teknik not:** RN130421 ürün kaydı 230 V giriş / 6 V AC, 2 VA olarak listeleniyor; L78L33 ise 3,3 V pozitif regülatördür. Bu regülatör normal regülasyon aralığında giriş değişimlerini bastırmayı hedefler. Dolayısıyla trafo + doğrultma/filtre + L78L33 + eşit 10 kΩ bölücü tek başına, 1,65 V biasın şebeke dalgalanmasını aynı dalga biçimiyle izlediğini kanıtlamaz. Bu, şema ve ölçümle netleştirilmesi gereken tasarım niyetidir. Kaynak: [RN130421 ürün bilgisi](https://www.ozdisan.com/p/General-Type-Transformers-471/el-kom-rn130421-516747), [ST L78L veri sayfası](https://docs.rs-online.com/5d09/0900766b8135fb6a.pdf).

## Kayıt kuralları
- Önceki BERO teknik belgelerindeki ürün bilgilerini yeniden yazma; ilgili referans dosyasına bağlantı ver.
- Önceki test notları yalnızca kendi kayıt kapsamı içinde kanıttır. Başarılı UART haberleşmesi ölçüm doğruluğu veya kalibrasyon kanıtı değildir.
- Kaynak belgelerdeki eski VREF/bias gibi değerleri bu düzeneğe fiziksel olarak doğrulanmış gibi taşıma.
- Kullanıcı tarafından bildirilen stok miktarlarını “kullanıcı bildirimi” olarak etiketle; fiziksel sayım yapılmış gibi gösterme.
- Her proje-özel doğrulamada tarih ve kanıt yolu ekle. Boşluğu varsayımla doldurma.
