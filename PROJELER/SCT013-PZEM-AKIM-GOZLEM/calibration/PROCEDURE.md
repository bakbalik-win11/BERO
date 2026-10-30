# SCT akım katsayısı/model değerlendirme prosedürü

**Durum: HAZIR, UYGULANMADI.** Bu belge bir çalışma planıdır; fiziksel kalibrasyon veya ölçüm sonucu içermez.

## Amaç ve sınırlar
- PZEM-004T V3, model eğitimi/değerlendirmesi için proje referans akışıdır; kusursuz ground truth veya bağımsız kalibrasyon standardı sayılmaz.
- Proje kapsamında True-RMS referans cihazı zorunlu değildir.
- Kullanıcının belirlediği hedef: geçerli, sıfırdan farklı PZEM akımına göre model tahmini en fazla ±%4 bağıl sapmada ise `OK`. Bu, PZEM'e uyum hedefidir; mutlak ölçüm doğruluğu garantisi değildir.
- Laboratuvar düzeyinde izlenebilirlik, ADC VREF karakterizasyonu veya üç seviyeli harici referans ölçümü varsayılan zorunluluk değildir.

## Ön koşullar
- İlgili güvenlik kontrolü ve gerçek donanım bağlantısı gözden geçirilmiş olmalı.
- Kullanılan SCT varyantı, ESP32 kartı/GPIO'su ve analog bağlantı kaydedilmiş olmalı.
- E00A ile E00/E01 temel okuma adımları tamamlanmış veya kalibrasyonun hangi kayıtları kullandığı açıkça belirtilmiş olmalı.
- PZEM okumalarının geçerlilik durumu ve yük/olay bağlamı kayıtlı olmalı.

## Adımlar
1. Tarih, SCT/PZEM kimlikleri, ESP32/firmware sürümü, yük koşulu ve veri yollarını kaydet.
2. Kalibrasyon/eğitim için seçilen kararlı alanları, bu alanların nasıl belirlendiğini ve dışlanan geçiş/geçersiz okumaları kaydet.
3. Aynı alanlara ait SCT özetleriyle geçerli PZEM akım okumalarını ilişkilendir; PZEM'in okuma zamanlamasına dair bilinmeyenleri kesinmiş gibi varsayma.
4. Sensör başına katsayı veya `f(x)` modeli çıkar; kullanılan kayıtları ve yöntemi belirt.
5. İlk uyum değerlendirmesinde modeli eğitildiği aynı etiketli kararlı alan verisine yeniden uygula. `abs(prediction - pzem_current) / abs(pzem_current) <= 0.04` ise `OK`, değilse `OUT_OF_RANGE`; sıfır veya geçersiz PZEM referansını bu yüzde kuralıyla sınıflandırma. Sonucu **eğitim verisi içi uyum** olarak adlandır; bağımsız genelleme başarımı olarak sunma.
6. Aynı SSR deneyinin geçişler dahil ham SCT zaman akışına eğitilmiş modeli uygula; SCT tahmini ile PZEM akışını ortak zaman ekseninde görselleştir. Tepki ve gecikme incelemesini ayrı raporla. Bu dinamik gözlem grafiği tek başına ±%4 doğruluk testi değildir.
7. PZEM istek/yanıt zamanlarını, SSR olay zamanını ve SCT örnek/pencere zamanlarını ayrı sakla. PZEM yanıt süresini fiziksel ölçüm güncelleme gecikmesiyle eşitleme. Zaman kaydırma/dengelemeyi ancak ölçümle desteklenen açık bir yöntem olarak uygula.
6. Kullanılan veriyi, hesaplama sürümünü, sınırlamaları ve yeni `calibration_id` bilgisini `calibrations.csv` içine ekle; eski girdilerin üzerine yazma.

## Kabul ve raporlama
İlk kabul raporu, aynı etiketli kararlı alan verisindeki eğitim verisi içi uyumu gösterir; bağımsız genelleme iddiası değildir. Tam ham aç-kapa grafiği ve gecikme/tepki analizi ayrı bir dinamik gözlem çıktısıdır. İki raporun kapsamı birbirine karıştırılmaz. Kabul sonucu yalnız kayıtlı veriler ve açık değerlendirme kuralı ile verilir. PZEM'e göre ±%4 uyum, bağımsız mutlak doğruluğu kanıtlamaz. Clipping veya belirgin veri sorunu görülürse bunu ayrıca raporla; yapılmamış kontrolleri yapılmış gibi yazma.

## HEDEF / LOG / SONUÇ
- **HEDEF:** PZEM referans akışına uyumu ölçmek ve yeniden üretilebilir model kaydı oluşturmak.
- **LOG:** Kullanılan ham/özet veri yolları, seçilen alanlar, gerçek donanım/yazılım koşulları, dışlanan okumalar ve hesaplama yöntemi yazılır. Veri yoksa açıkça belirtilir.
- **SONUÇ:** Ölçüm/eğitim yapılmadan sonuç üretilmez; sonraki adım ve sınırlamalar kaydedilir.
