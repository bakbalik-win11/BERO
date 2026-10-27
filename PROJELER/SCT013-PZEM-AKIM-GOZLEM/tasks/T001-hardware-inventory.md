# T001 — Fiziksel donanım envanteri

- **Durum:** DEVAM EDİYOR — fiziksel stok ve breadboard üzerinde hazırlanmış bias alt devresinin kullanıcı tarafından bildirilen yapısı kaydedildi. Bu aşamada 8 kanallı analog kart söz konusu değil. GPIO/pin numarası firmware ve pin planlama aşamasında belirlenecek; T001’de pin seçimi istenmiyor.
- **Faz:** 0.1
- **Bağımlılık:** Yok
- **Hedef:** Önceki BERO kayıtlarını yeniden toplatmadan kullanmak; seçilmiş donanımı, kullanıcı tarafından bildirilen stokları ve kalan proje-özel bilgileri kaydetmek.

## Önceden mevcut referanslar
- [SCT013-100A-1V](../hardware/references/SCT013-100A-1V.md)
- [SCT013-30A-1V](../hardware/references/SCT013-30A-1V.md)
- [PZEM-004T V3.0](../hardware/references/PZEM-004T-V3.0.md)
- [SSR donanım referansı](../hardware/references/SSR.md)
- [DS3231 RTC referansı](../hardware/references/DS3231.md)
- [Referans indeksi](../hardware/references/README.md)
- [T001 kullanıcı envanteri](../docs/inventory/T001-fiziksel-donanim-envanteri.md)

Önceden var olan genel teknik özellikleri tekrar yazma; mevcut kaynaklardan yararlan.

## Kaydedilen bilgiler
- SCT013 30 A / 1 V: 7 adet; jack çıkışlı.
- SCT013 100 A / 1 V: 10 adet; jack çıkışlı.
- PZEM-004T V3.0.
- ESP32-C3 SuperMini SSR kontrol düğümü ve ayrı ESP32 PZEM ölçüm düğümü.
- BERO envanter kayıtlarında bulunan ESP32 kart/modül stoku: 2 × ESP32-WROOM-32D, 1 × ESP32-WROOM-32E ve 1 × genel ESP-WROOM-32 tabanlı NodeMCU ESP32 kartı. Bu stok kaydı, SCT analog örneklemesi için hangi fiziksel kartın seçildiğini veya kart revizyonunu tek başına belirlemiyor.
- SAMM Market 5 V, 2 kanallı SSR kartı; DS3231 RTC.
- Masaüstü 5 V / 1,8 A güç kaynağı; lamba test yükü.
- Jack yuvaları ve bağlantı/ölçüm parçaları mevcut.
- Breadboard üzerinde hazırlanmış bias alt devresi: 2 adet 10 kΩ, 1/4 W metal film dirençle orta nokta oluşturulur; sensör bu bias orta noktasına bağlanır. Orta nokta ile GND arasına “104” kodlu kondansatör (100 nF) bağlanır. Bu aşamada 8 kanallı analog kart söz konusu değil. Bu aşamada ayrı/harici ADC kullanılmayacak; MCP3208 sonraki aşamaya ayrılmıştır. GPIO numarası bu aşamada istenmiyor.
- Kullanıcı kararı: SCT okumaları için 2 × ESP32-WROOM-32D ve 1 × ESP32-WROOM-32E ayrı hızlı örnekleme kanalları olarak kullanılacak. Bu aşamanın çıktısı akım/RMS hesabı değil, sensörün ham/anlık gerilim okumaları ile SSR-zamanlayıcı düğümünden gelen paket bilgisinin birlikte yazdırılmasıdır. 1, 2 ve 4 sarım testleri aynı hat üzerinde ayrı ayrı yapılacak.

## İlerleme ilkesi
İşi en küçük anlamlı birimlere böl ve teker teker ilerle. Sonraki aşamaya ait donanım (MCP3208) envantere yazılır ancak mevcut aşamanın kapsamına taşınmaz. Bir sonraki adımı ancak o anki küçük birimin kabul ölçütü karşılandıktan sonra başlat.
- Bias üretim alt devresi önceki proje kayıtlarında kullanıcı onayıyla tamamlandı sayılıyor. Bu, SCT AC sinyalinin bias noktasına kuplajının da doğrulandığı anlamına gelmez.

## Kalan proje-özel işler
1. Breadboard üzerindeki bias alt devresi kullanıcı tarafından tarif edildi: 2 adet 10 kΩ, 1/4 W metal film dirençle orta nokta; sensör bu bias orta noktasına bağlanıyor; orta nokta ile GND arasında “104” kodlu kondansatör (100 nF) var. Şimdilik 8 kanallı analog kart/kanal tasarımı bu görevin parçası değil. Bu tarifin ötesinde başka direnç/filtre elemanları olduğu varsayılmayacak.
2. Bu aşamada ayrı/harici ADC kullanılmayacak; MCP3208 sonraki aşamaya ayrılmıştır. Harici ADC modeli/revizyonu veya VREF seçimi T001 kapsamına alınmayacak. GPIO/pin numarası da bu aşamada istenmiyor.
3. True-RMS referans cihazı ve en az üç kontrollü yük seviyesini [T003](T003-reference-and-error-target.md) altında ele al.
4. SSR için iki AC yükü ve GPIO eşlemesini sonraki güvenli test planında kaydet; tetik mantığını düşük gerilimli testte doğrula. Ürün kimliği İzmo9659 / MP02637; tekil SSR parça kodu doğrulanmış değil.
5. DS3231 breakout pinleri, pull-up gerilimi, yedek pil/şarj devresi ve ilk saat ayarlama yöntemini kablolama öncesi doğrula; hızlı örnekleme zamanlamasını RTC takvim okumalarından bağımsız tut.

## Kabul ölçütü
Fiziksel envanter ve breadboard bias alt devresinin kullanıcı tarafından tarif edilen yapısı kaydedilmelidir: 2 adet 10 kΩ, 1/4 W metal film dirençle orta nokta ve orta nokta-GND arasında 104 (100 nF) kondansatör; sensör bu bias noktasına bağlanır. Şimdilik 8 kanallı analog kart/kanal tasarımı kapsamda değildir. Henüz bildirilmemiş ayrıntılar varmış gibi yeni eleman veya değer istenmemelidir. GPIO numarası, pin eşlemesi ve firmware ADC yapılandırması T001 kabul şartı değildir; firmware/pin planlama aşamasına aittir. Stok sayıları kullanıcı bildirimi olarak sunulur. Envanterin yazılması tek başına elektriksel doğrulama veya deney tamamlandığı anlamına gelmez.

## Güvenlik
Bu görev dokümantasyon ve görsel incelemedir. Şebeke bağlantısını sökme, kabloyu ayırma veya sisteme enerji verme.
