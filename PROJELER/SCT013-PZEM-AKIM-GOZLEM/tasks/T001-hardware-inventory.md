# T001 — Fiziksel donanım envanteri

- **Durum:** TAMAMLANDI — envanter belgeleme kapsamı tamamlandı; donanım listesi ve breadboard bias alt devresi kullanıcı beyanına dayanarak kaydedildi. Bu durum tüm fiziksel bağlantıların bağımsız olarak doğrulandığı anlamına gelmez. GPIO/pin numarası ve firmware ADC yapılandırması bu görevin kapsamında değil.
- **Faz:** 0.1
- **Bağımlılık:** Yok
- **Hedef:** Önceki BERO kayıtlarını yeniden toplatmadan kullanmak; seçilmiş donanımı, mevcut stokları ve kalan proje-özel bilgileri kaydetmek.

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
- Kart envanteri: 1 × ESP32-C3 SuperMini (SSR kontrolü/zamanlama), 1 × ESP32-WROOM-32E ve 2 × ESP32-WROOM-32D (SCT ham örnekleme düğümleri). Kullanıcı 1 adet ESP32-WROOM-32E kart fotoğrafını da sağladı. Kullanıcı ESP32-WROOM-32D, ESP32-C3 Super Mini arka yüzü, ESP32-WROOM-32E ve ESP32-WROOM-32 tabanlı geliştirme kartlarının fotoğraflarını sağladı. Görsel referanslar kayda alındı; tekrar istenmeyecek.
- SCT013 30 A / 1 V: 7 adet; jack çıkışlı.
- SCT013 100 A / 1 V: 10 adet; jack çıkışlı.
- PZEM-004T V3.0.
- ESP32-C3 SuperMini SSR kontrol düğümü ve ayrı ESP32 PZEM ölçüm düğümü.
- BERO envanter kayıtlarında bulunan ESP32 kart/modül stoku: 2 × ESP32-WROOM-32D, 1 × ESP32-WROOM-32E ve 1 × genel ESP-WROOM-32 tabanlı NodeMCU ESP32 kartı. Kullanıcı tarafından sağlanan fotoğrafta ESP32-WROOM-32D metal kalkanlı geliştirme kartı görülüyor; ayrıca ESP32-C3 Super Mini kartının arka yüz fotoğrafı da sağlandı. Görseller envanter notlarına işlendi. Kart dağılımında kullanıcının verdiği bilgiler esas alınır; fotoğraflar tekrar istenmeyecek.
- SAMM Market 5 V, 2 kanallı SSR kartı; DS3231 RTC.
- Masaüstü 5 V / 1,8 A güç kaynağı; lamba test yükü.
- Jack yuvaları ve bağlantı/ölçüm parçaları mevcut.
- Breadboard üzerinde hazırlanmış bias alt devresi: 2 adet 10 kΩ, 1/4 W metal film dirençle orta nokta oluşturulur; sensör bu bias orta noktasına bağlanır. Orta nokta ile GND arasına “104” kodlu kondansatör (100 nF) bağlanır. Bu aşamada ayrı/harici ADC kullanılmayacak; MCP3208 sonraki aşamaya ayrılmıştır. GPIO numarası bu aşamada istenmiyor.
- Kullanıcı kararı: SCT okumaları için 2 × ESP32-WROOM-32D ve 1 × ESP32-WROOM-32E ayrı hızlı örnekleme kanalları olarak kullanılacak. Bu aşamanın çıktısı akım/RMS hesabı değil, sensörün ham/anlık gerilim okumaları ile SSR-zamanlayıcı düğümünden gelen paket bilgisinin birlikte yazdırılmasıdır. 1, 2 ve 4 sarım testleri aynı hat üzerinde ayrı ayrı yapılacak.

## İlerleme ilkesi
İşi en küçük anlamlı birimlere böl ve teker teker ilerle. Sonraki aşamaya ait donanım (MCP3208) envantere yazılır ancak mevcut aşamanın kapsamına taşınmaz. Bir sonraki adımı ancak o anki küçük birimin kabul ölçütü karşılandıktan sonra başlat.
- Bias üretim alt devresi kullanıcı tarafından hazırlanmış ve tamamlanmış olarak kaydedilmiştir. Bu, SCT AC sinyalinin bias noktasına kuplajının ayrıca test edildiği anlamına gelmez.
- DS3231 için kullanıcı RTC kodunun çalıştığını ve güç kesilip yeniden verildiğinde saat tutma testinin yapıldığını bildirdi. İki modülde de 2032 tipi pil bulunuyor. Bu kayıt esas alınır; test tekrar istenmeyecek.

## Kapsam dışı / sonraki aşamalar
- Harici ADC (MCP3208) ve VREF seçimi sonraki aşamaya ayrılmıştır.
- GPIO/pin eşlemesi ve firmware ADC yapılandırması firmware/pin planlama aşamasında ele alınacaktır.
- Bias alt devresinin mevcut yapısı kaydedilmiştir; SCT sinyalinin elektriksel kuplaj doğrulaması bu envanter görevinin kabul şartı değildir.

## Kabul ölçütü
Fiziksel envanter ve breadboard bias alt devresinin yapısı kaydedilmelidir: 2 adet 10 kΩ, 1/4 W metal film dirençle orta nokta ve orta nokta-GND arasında 104 (100 nF) kondansatör; sensör bu bias noktasına bağlanır. Bildirilen stoklar ve kurulum bilgileri envanter kaydı için esas alınır; kullanıcıdan tekrar tekrar aynı ayrıntıları vermesi istenmez. GPIO numarası, pin eşlemesi ve firmware ADC yapılandırması T001 kabul şartı değildir; firmware/pin planlama aşamasına aittir. Envanter kaydı, SCT sinyal kuplajının veya deney sonuçlarının ayrıca test edildiği anlamına gelmez.

## Güvenlik
Bu görev dokümantasyon ve görsel incelemedir. Şebeke bağlantısını sökme, kabloyu ayırma veya sisteme enerji verme.
