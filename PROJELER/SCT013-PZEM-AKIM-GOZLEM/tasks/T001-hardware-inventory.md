# T001 — Fiziksel donanım envanteri

- **Durum:** DEVAM EDİYOR — fiziksel stok ve kart modellerine ilişkin mevcut kayıtlar işlendi; analog giriş için seçilecek kart/pin ve elektriksel kabul maddeleri açık.
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
0. Hızlı örnekleme çıktısının kapsamını sabitle: sensör ham/anlık gerilim örnekleri ve zamanlayıcı paket bilgisi yazdırılacak; bu aşamada akım/RMS hesabı yapılmayacak.
1. SCT analog örneklemesi için stoktaki ESP32 kartlarından hangisinin seçildiğini ve fiziksel kart revizyonunu, mevcut fotoğraf/etiket kanıtıyla eşleştir.
2. Seçilen kartın dahili ADC kanalını/GPIO numarasını ve bu girişin izin verilen aralığını üretici pin/teknik belgesiyle doğrula.
3. ADC giriş referans/attenuation yapılandırmasını kaydet; ESP32 dahili ADC kullanılırken harici ADC'ye ait VREF alanı uygulanmaz.
4. SCT AC sinyalinin bias noktasına kuplaj yöntemini; kanal direnç/filtre değerlerini ve güvenli ADC aralığını analog ön uç kaydına taşı. Ölçülmeyen değerleri tahmin etme.
5. True-RMS referans cihazı ve üç kontrollü yük seviyesini T003 görevine bağla.
6. SSR için iki AC yük ve GPIO eşlemesini sonraki güvenli test planında kaydet; tetik mantığını düşük gerilim testinde doğrula.
7. DS3231 breakout pinleri, pull-up gerilimi, yedek pil/şarj devresi ve ilk saat ayarlama yöntemini kablolama öncesi doğrula.

## Kabul ölçütü
Fiziksel envanter, seçilen kart/ADC pini ve analog bağlantı bilgileri bilinen kanıta bağlanmalı; bilinmeyenler açıkça işaretlenmelidir. Stok sayıları kullanıcı bildirimi olarak sunulur. Envanterin yazılması tek başına elektriksel doğrulama veya deney tamamlandığı anlamına gelmez.

## Güvenlik
Bu görev dokümantasyon ve görsel incelemedir. Şebeke bağlantısını sökme, kabloyu ayırma veya sisteme enerji verme.
