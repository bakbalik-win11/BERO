# T001 — Fiziksel donanım envanteri

- **Durum:** DEVAM EDİYOR — fiziksel stok ve hazır analog kart bilgileri kaydedildi; analog ön uç elektriksel ayrıntıları açık. GPIO/pin numarası firmware ve pin planlama aşamasında belirlenecek; T001’de pin seçimi istenmiyor.
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
- Önceden hazırlanmış 8 kanallı kart: her kanalda ayrı bias ve direnç ağı. Kullanıcının tarifine göre SCT fişi dişi jack'e takılır, sinyal bias devresi üzerinden ESP32 GPIO bacağına gider. İlk aşamada harici ADC entegresi kullanılmayacak; analog okuma ESP32'nin dahili ADC'si üzerinden, ADC destekli GPIO'dan yapılacak. MCP3208 fiziksel olarak mevcut; ileriki aşama için ayrıldı, ilk aşamada kullanılmayacak. Seçilecek kartın GPIO numarası henüz proje kaydında kesinleştirilmedi.
- Kullanıcı kararı: SCT okumaları için 2 × ESP32-WROOM-32D ve 1 × ESP32-WROOM-32E ayrı hızlı örnekleme kanalları olarak kullanılacak. Bu aşamanın çıktısı akım/RMS hesabı değil, sensörün ham/anlık gerilim okumaları ile SSR-zamanlayıcı düğümünden gelen paket bilgisinin birlikte yazdırılmasıdır. 1, 2 ve 4 sarım testleri aynı hat üzerinde ayrı ayrı yapılacak.

## İlerleme ilkesi
İşi en küçük anlamlı birimlere böl ve teker teker ilerle. Sonraki aşamaya ait donanım (MCP3208) envantere yazılır ancak mevcut aşamanın kapsamına taşınmaz. Bir sonraki adımı ancak o anki küçük birimin kabul ölçütü karşılandıktan sonra başlat.
- Bias üretim alt devresi önceki proje kayıtlarında kullanıcı onayıyla tamamlandı sayılıyor. Bu, SCT AC sinyalinin bias noktasına kuplajının da doğrulandığı anlamına gelmez.

## Kalan proje-özel işler
1. Kullanıcının açıkladığı bağlantı yolunu kaydet: SCT013 dişi jack yuvasına bağlanır; sensör dönüş sinyali dişi jack üzerinden 8 kanallı analog arayüze ve oradan ESP32 ADC girişine gider. Elektriksel bias kuplaj topolojisinin (hangi sinyal hattının bias orta noktasına nasıl bağlandığı), kanal direnç/filtre değerlerinin ve güvenli ADC aralığının kanıtla belgelenmesi hâlâ gerekir. Ölçülmeyen değerleri tahmin etme.
2. ADC model/revizyonu ve VREF kaynağı/değeri bilinmiyor olarak açık bırak; ilk aşamada ESP32 dahili ADC planı var, MCP3208 seçilmiş sayılmaz. Dahili ADC’ye harici ADC VREF alanı uygulama.
3. ADC destekli GPIO numarası, pin eşlemesi ve firmware attenuation/ADC yapılandırmasını firmware/pin planlama aşamasına bırak; bunları T001’in eksik işi olarak kullanıcıya sorma.
4. True-RMS referans cihazı ve en az üç kontrollü yük seviyesini [T003](T003-reference-and-error-target.md) altında ele al.
5. SSR için iki AC yükü ve GPIO eşlemesini sonraki güvenli test planında kaydet; tetik mantığını düşük gerilimli testte doğrula. Ürün kimliği İzmo9659 / MP02637; tekil SSR parça kodu doğrulanmış değil.
6. DS3231 breakout pinleri, pull-up gerilimi, yedek pil/şarj devresi ve ilk saat ayarlama yöntemini kablolama öncesi doğrula; hızlı örnekleme zamanlamasını RTC takvim okumalarından bağımsız tut.

## Kabul ölçütü
Fiziksel envanter ve hazır analog kart kaydı mevcut kaynaklara bağlanmalı; SCT'nin dişi jack üzerinden analog karta ve oradan ESP32 ADC'ye giden bağlantı yolu kaydedilmiştir. ADC modeli/revizyonu ve VREF bilgisi, bias orta noktasına elektriksel kuplajın ayrıntısı, kanal direnç/filtre değerleri ve güvenli ADC aralığı bilinen kanıta göre kaydedilmeli; bilinmeyenler açıkça işaretlenmelidir. GPIO numarası, pin eşlemesi ve firmware ADC yapılandırması T001 kabul şartı değildir; firmware/pin planlama aşamasına aittir. Stok sayıları kullanıcı bildirimi olarak sunulur. Envanterin yazılması tek başına elektriksel doğrulama veya deney tamamlandığı anlamına gelmez.

## Güvenlik
Bu görev dokümantasyon ve görsel incelemedir. Şebeke bağlantısını sökme, kabloyu ayırma veya sisteme enerji verme.
