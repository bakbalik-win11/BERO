# Fiziksel donanım envanteri

**Durum: KISMEN HAZIR.** SCT ve PZEM teknik referansları [proje referans klasöründe](references/README.md) bulunur. Bu envanter genel ürün özelliklerini tekrar yazmak yerine proje seçimini, kullanıcı tarafından bildirilen stokları ve bu düzeneğe ait eksik bilgileri izler.

## Proje önceliği ve stok bildirimi

| Kalem | Kaydedilen bilgi | Bilgi kaynağı / durum |
|---|---|---|
| Öncelikli akım sensörü | **SCT013-030 — 30 A / 1 V** | Kullanıcı kararı, 2026-10-27. Bu projede önce bu model kullanılacak. |
| SCT013-030 stok adedi | **7 adet** | Kullanıcı bildirimi, 2026-10-27; bağımsız sayım yapılmadı. Bu oturumda sunulan görselde SCT013 / 30 A / 1 V etiketi okunuyor; görsel henüz depodaki `hardware/photos/` klasörüne dosya olarak eklenmedi. |
| SCT013-100A-1V stok adedi | **10 adet** | Kullanıcı bildirimi, 2026-10-27; bağımsız sayım yapılmadı. Alternatif stok olarak kaydedildi, öncelikli seçim değil. |
| 100 nF / 50 V seramik kondansatör | **10 adet bildirildi; 1 adet kullanılıyor** | Kullanıcı bildirimi, 2026-10-27. Kullanılan parçada **104** işareti olduğu düzeltildi; bu kod 100 nF değerine karşılık gelir. Bir adet bias orta noktasından GND'ye bağlı. Stokun kullanım sonrası kalan adedi ayrıca sayılmadı. |

**Not:** Stok adetleri kullanıcı tarafından bildirilen miktarlardır; depoda fiziksel sayım yapılmış gibi sunulmaz. SCT modeli seçimi, gerçek ünitenin kalıcı fotoğraf kanıtı ve kalibrasyon sonucu birbirinden ayrı kayıtlardır.

## Donanım konfigürasyonu

| Öğe | Mevcut BERO referansı | Bu proje için kayıtlı durum | Kalan adım |
|---|---|---|---|
| SCT seçimi | [SCT013-030](references/SCT013-30A-1V.md); [SCT013-100A-1V](references/SCT013-100A-1V.md) | Öncelik SCT013-030, 30 A / 1 V. SCT013-100A-1V alternatif stokta. | Kullanılan fiziksel ünitenin etiketi için kalıcı kanıt yolu ekle; genel teknik özellikleri tekrar araştırma. |
| PZEM | [PZEM-004T V3.0](references/PZEM-004T-V3.0.md) | Aile belgesi ve geçmiş ESP32D1/ESPHome başarılı haberleşme notu mevcut; bu projedeki 10 A/100 A fiziksel varyantı kesin değil. | Kullanılan modül varyantını ve CT gerekip gerekmediğini/CT modelini mevcut kayıtlarla doğrula. |
| MCU | [ESP32-WROOM-32D BERO kaydı](../../../DONANIM/ESP32-WROOM-32D/README.md) | Aday donanım kaydı var; bu projedeki fiziksel kart/revizyon kaydı yok. | Önceki çalışma kanıtını bağla veya kart kimliğini kaydet. |
| ADC | [MCP3208 BERO kaydı](../../../DONANIM/MCP3208/README.md) | Aday donanım kaydı var; bu projedeki gerçek ADC ve VREF doğrulanmadı. | Fiziksel ADC modelini/revizyonunu ve VREF kaynağını kaydet. |
| Analog ön uç | SCT referanslarındaki tarihsel bias/VREF notları | Yaklaşık 1,67 V bias ve 3,12 V VREF geçmiş notlarda geçiyor; bu projenin güncel ölçümü olarak kabul edilmez. | Gerçek devre kaydı ve gerekiyorsa güvenli düşük gerilim tarafı ölçümüyle doğrula. |
| Pasif bileşen | 100 nF / 50 V seramik kondansatör; işaret kodu 104 | Stokta 10 adet bildirildi; 1 adet 104 kodlu kondansatörün bias orta noktasından GND'ye bağlı olduğu kullanıcı tarafından açıklandı. | Kullanım yeri kaydedildi. Stokun kalan adedi ve varsa diğer kondansatörlerin kullanımı ayrıca teyit edilebilir. |
| Köprü sonrası filtre kondansatörü | 2200 µF / 35 V elektrolitik | Kullanıcı bildirimi: KBU6M köprü doğrultucudan sonra, L78L33 regülatörden önce bias trafosu kutusunda. | Bağlantı/polarite fotoğraf veya şemayla henüz arşivlenmedi. |
| Bias trafo | RN130421, 6 V AC / 2,0 VA PCB tipi trafo | Kullanıcı beyanına göre KBU6M ve L78L33 ile birlikte korunaklı kutuda; bu alt devre “bias trafosu” olarak adlandırılıyor. | Primer/sekonder bağlantısı ve kutunun iç bağlantılarını gösteren şema/fotoğraf kaydedilmeli. |
| Köprü doğrultucu | KBU6M, 6 A / 1000 V tek faz köprü doğrultucu | Kullanıcı tarafından RN130421 sekonderi ile L78L33 arasında kullanıldığı bildirildi. Teknik aile bilgisi: [Vishay KBU6A–KBU6M veri sayfası](https://www.vishay.com/doc/?98732=). Fiziksel işaret fotoğrafı henüz arşivlenmedi. | Gerçek parça işaretini ve AC/+/- pin bağlantılarını şema/fotoğrafla kaydet. |
| Bias bölücü | 2 × 10 kΩ; yaklaşık 1,65 V orta nokta | Kullanıcı beyanına göre ayrı breadboard üzerinde; bias trafosu kutusunun içinde değil. | Breadboarddaki besleme/GND bağlantıları ve SCT sinyalinin bu noktaya kuplajı kaydedilmeli. |
| Bias regülatörü | L78L33, TO-92 | Kullanıcı tarafından bias alt devresinde bildirildi; nominal 3,3 V regülatör olarak tanımlanıyor. | Parça üzerindeki işaret, pin yönü ve gerçek devredeki giriş/çıkış bağlantısı teyit edilmeli. |
| Bias bölücü | 2 × 10 kΩ, orta nokta ≈ 1,65 V hedefi | Kullanıcı beyanı; iki eşit direnç 3,3 V rayından beslendiğinde nominal orta nokta 1,65 V olur. | Üst/alt uçların hangi ray/toprağa bağlı olduğunu, bias düğümünün nerelere gittiğini ve ölçülen gerçek DC değerini kaydet. |
| Referans cihaz | True-RMS ampermetre | Bu proje için model/kalibrasyon durumu kayıtlı değil. | Mevcut geçmiş kaydı bul veya T003 kapsamında tanımla. |
| Yükler | Rezistif / diğer kontrollü yükler | Üç akım seviyesine karşılık gelen mevcut yük kimlikleri kayıtlı değil. | Mevcut kayıt varsa bağla; yoksa T003 kapsamında belirle. |

## Bias trafosu — mevcut tarif

**Kaynak:** Kullanıcı açıklaması, 2026-10-27. Aşağıdaki bilgiler mevcut devre düzeninin kullanıcı tarafından tarifidir; tam şema veya ölçüm kaydı değildir.

- **Korunaklı kutu içi:** RN130421, 6 V AC / 2,0 VA PCB tipi trafo; KBU6M, 6 A / 1000 V köprü doğrultucu; köprü sonrasında 2200 µF / 35 V elektrolitik filtre kondansatörü; L78L33, TO-92 regülatör.
- **Ayrı breadboard:** 2 × 10 kΩ bias bölücü; orta noktada yaklaşık 1,65 V. Orta noktadan GND'ye bir adet **104 kodlu seramik kondansatör (100 nF)** bağlı olduğu kullanıcı tarafından bildirildi.
- **Kondansatör stoku:** 100 nF / 50 V seramikten 10 adet bildirildi. Bu devrede bir adet kullanıldığı belirtiliyor; kullanım sonrası kalan stok ayrıca sayılmadı.
- “Bias trafosu” bu alt devre için kullanıcının tercih ettiği addır.

### Henüz kaydedilmemiş bağlantı ayrıntıları

1. L78L33 giriş/çıkışında 2200 µF / 35 V kondansatöre ek olarak başka bypass kondansatörleri var mı? Varsa değerleri ve bağlantıları nedir?
2. Kutudaki L78L33 regülatörün 3,3 V çıkışı ayrı breadboarddaki 2 × 10 kΩ bölücüye nasıl taşınıyor; ortak GND bağlantısı nereden sağlanıyor?
3. SCT'nin AC sinyali 1,65 V bias noktasına hangi kuplaj/bağlantı elemanı üzerinden ekleniyor?
4. 1,65 V değeri nominal hesap mı, multimetreyle ölçülmüş değer mi? Henüz ölçüm kanıtı paylaşılmadı.

**Teknik not:** RN130421 ürün kaydı 230 V giriş / 6 V AC, 2 VA olarak listeleniyor; KBU6M tek faz köprü doğrultucu, L78L33 ise 3,3 V pozitif regülatördür. L78L33 normal regülasyon aralığında giriş değişimlerini bastırmayı amaçlar. Bu nedenle bu bileşenler tek başına 1,65 V biasın şebeke dalgalanmasını aynı dalga biçimiyle izlediğini kanıtlamaz. Bu tasarım niyeti, bağlantı şeması ve iki sinyalin ölçümüyle netleştirilmelidir. Kaynaklar: [RN130421 ürün bilgisi](https://www.ozdisan.com/p/General-Type-Transformers-471/el-kom-rn130421-516747), [ST L78L veri sayfası](https://docs.rs-online.com/5d09/0900766b8135fb6a.pdf), [Vishay KBU6A–KBU6M veri sayfası](https://www.vishay.com/doc/?98732=).

## Kayıt kuralları
- Önceki BERO teknik belgelerindeki ürün bilgilerini yeniden yazma; ilgili referans dosyasına bağlantı ver.
- Önceki test notları yalnızca kendi kayıt kapsamı içinde kanıttır. Başarılı UART haberleşmesi ölçüm doğruluğu veya kalibrasyon kanıtı değildir.
- Kaynak belgelerdeki eski VREF/bias gibi değerleri bu düzeneğe fiziksel olarak doğrulanmış gibi taşıma.
- Kullanıcı tarafından bildirilen stok miktarlarını “kullanıcı bildirimi” olarak etiketle; fiziksel sayım yapılmış gibi gösterme.
- Her proje-özel doğrulamada tarih ve kanıt yolu ekle. Boşluğu varsayımla doldurma.
