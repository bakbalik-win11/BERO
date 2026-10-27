# T001 — Fiziksel donanım envanteri

- **Durum:** DEVAM EDİYOR — fiziksel stok ve hazır analog kart bilgileri kaydedildi; görev kabul ölçütleri henüz bütünüyle karşılanmadı.
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
- SAMM Market 5 V, 2 kanallı SSR kartı; DS3231 RTC.
- Masaüstü 5 V / 1,8 A güç kaynağı; lamba test yükü.
- Jack yuvaları ve bağlantı/ölçüm parçaları mevcut.
- Önceden hazırlanmış 8 kanallı kart: her kanalda ayrı bias ve direnç ağı. SCT jack sinyali arayüze bağlanır ve ESP32 ADC girişinden okunur. İstenirse MCP serisi ADC eklenebilir; belirli MCP modelinin seçildiği varsayılmıyor.
- Bias üretim alt devresi önceki proje kayıtlarında kullanıcı onayıyla tamamlandı sayılıyor. Bu, SCT AC sinyalinin bias noktasına kuplajının da doğrulandığı anlamına gelmez.

## Kalan proje-özel işler
1. Gerçekte kullanılacak ADC modelini/revizyonunu ve VREF kaynağını/değerini kaydet.
2. SCT AC sinyalinin bias noktasına kuplaj yöntemini; burden/filtre değerlerini ve güvenli ADC aralığını analog ön uç kaydına taşı. Ölçülmeyen değerleri tahmin etme.
3. True-RMS referans cihazı ve üç kontrollü yük seviyesini T003 görevine bağla.
4. SSR için iki AC yük ve GPIO eşlemesini sonraki güvenli test planında kaydet; tetik mantığını düşük gerilim testinde doğrula.
5. DS3231 breakout pinleri, pull-up gerilimi, yedek pil/şarj devresi ve ilk saat ayarlama yöntemini kablolama öncesi doğrula.

## Kabul ölçütü
Fiziksel envanter, seçilen ADC/VREF ve analog bağlantı bilgileri bilinen kanıta bağlanmalı; bilinmeyenler açıkça işaretlenmelidir. Stok sayıları kullanıcı bildirimi olarak sunulur. Envanterin yazılması tek başına elektriksel doğrulama veya deney tamamlandığı anlamına gelmez.

## Güvenlik
Bu görev dokümantasyon ve görsel incelemedir. Şebeke bağlantısını sökme, kabloyu ayırma veya sisteme enerji verme.
