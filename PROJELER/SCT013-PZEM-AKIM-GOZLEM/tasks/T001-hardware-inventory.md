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
- Üretici veri sayfaları: [ESP32-WROOM-32D/32U](https://documentation.espressif.com/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.html), [ESP32-WROOM-32E/32UE](https://documentation.espressif.com/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.html), [ESP32-WROOM-32](https://documentation.espressif.com/esp32-wroom-32_datasheet_en.html), [ESP32-C3-MINI-1/1U modül veri sayfası](https://documentation.espressif.com/esp32-c3-mini-1_mini-1u_datasheet_en.html). Kartın geliştirme kartı şeması/pinout'u ayrıca doğrulanmadan yalnızca modül veri sayfasına göre pin ataması yapılmayacak.
- [T001 kullanıcı envanteri](../docs/inventory/T001-fiziksel-donanim-envanteri.md)

Önceden var olan genel teknik özellikleri tekrar yazma; mevcut kaynaklardan yararlan.

## Kaydedilen bilgiler
- Kullanıcı tarafından belirtilen kart envanteri: 1 × ESP32-C3 SuperMini (SSR kontrolü/zamanlama), 1 × ESP32-WROOM-32E ve 2 × ESP32-WROOM-32D (SCT ham örnekleme düğümleri). Kullanıcı 1 adet ESP32-WROOM-32E kart fotoğrafını da sağladı. Bu kart dağılımında kullanıcı beyanı esastır. Kullanıcı ESP32-WROOM-32D, ESP32-C3 Super Mini arka yüzü, ESP32-WROOM-32E ve ESP32-WROOM-32 tabanlı geliştirme kartlarının fotoğraflarını sağladı. Görsel referanslar kayda alındı; tekrar istenmeyecek.
- SCT013 30 A / 1 V: 7 adet; jack çıkışlı.
- SCT013 100 A / 1 V: 10 adet; jack çıkışlı.
- PZEM-004T V3.0.
- ESP32-C3 SuperMini SSR kontrol düğümü ve ayrı ESP32 PZEM ölçüm düğümü.
- BERO envanter kayıtlarında bulunan ESP32 kart/modül stoku: 2 × ESP32-WROOM-32D, 1 × ESP32-WROOM-32E ve 1 × genel ESP-WROOM-32 tabanlı NodeMCU ESP32 kartı. Kullanıcı tarafından sağlanan fotoğrafta ESP32-WROOM-32D metal kalkanlı geliştirme kartı görülüyor; ayrıca ESP32-C3 Super Mini kartının arka yüz fotoğrafı da sağlandı. Görseller envanter notlarına işlendi. Kart dağılımında kullanıcı beyanı esastır; fotoğraflar tekrar istenmeyecek.
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
5. DS3231 breakout pinleri, pull-up gerilimi, yedek pil/şarj devresi ve ilk saat ayarlama yöntemini kablolama öncesi doğrula; hızlı örnekleme zamanlamasını RTC takvim okumalarından bağımsız tut.

## Kabul ölçütü
Fiziksel envanter ve breadboard bias alt devresinin kullanıcı tarafından tarif edilen yapısı kaydedilmelidir: 2 adet 10 kΩ, 1/4 W metal film dirençle orta nokta ve orta nokta-GND arasında 104 (100 nF) kondansatör; sensör bu bias noktasına bağlanır. Şimdilik 8 kanallı analog kart/kanal tasarımı kapsamda değildir. Henüz bildirilmemiş ayrıntılar varmış gibi yeni eleman veya değer istenmemelidir. GPIO numarası, pin eşlemesi ve firmware ADC yapılandırması T001 kabul şartı değildir; firmware/pin planlama aşamasına aittir. Stok sayıları kullanıcı bildirimi olarak sunulur. Envanterin yazılması tek başına elektriksel doğrulama veya deney tamamlandığı anlamına gelmez.

## Güvenlik
Bu görev dokümantasyon ve görsel incelemedir. Şebeke bağlantısını sökme, kabloyu ayırma veya sisteme enerji verme.
