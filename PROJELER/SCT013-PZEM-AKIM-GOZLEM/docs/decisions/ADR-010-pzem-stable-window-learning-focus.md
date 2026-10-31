# ADR-010 — PZEM referanslı kararlı alan etiketleme ve sürekli öğrenme

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ
- **Karar sahibi:** Kullanıcı
- **İlişkili karar:** ADR-009

## Bağlam
Kullanıcı, yeni/harici kodla ±%4 saha hedefinin sağlandığını bildirdi. Bu nedenle ham 50 Hz dalga aktarımı, örnek başına timestamp ve DMA/ADC Continuous geliştirme işleri ADR-009 ile kapatıldı. BERO'nun bundan sonraki amacı çalışan SCT ölçüm yolunu PZEM referans akışıyla karşılaştırmak ve veriye dayalı olarak sürekli iyileştirmektir.

## Karar
1. Kullanıcının paylaştığı E00F ESP32D2 YAML çalışan baseline kabul edilir. Firmware, pinler, ct_clamp 200 ms penceresi, 2 s yayın aralığı, 24.22 katsayısı ve yazılımsal sıfırlama eşiği bulunmaması gerekçesiz değiştirilmez.
2. Ana döngü: aynı yük koşulunda PZEM/SCT kaydı → iki akışta ayrı kararlılık tespiti → örtüşen kararlı alanların eşleştirilmesi → geçerli PZEM değerleriyle etiketleme → mevcut katsayının değerlendirilmesi → veri desteklerse yeni calibration_id ile iyileştirme → yeni yük/koşullarla tekrar.
3. PZEM proje referansıdır; mutlak ve kusursuz ground truth değildir. PZEM sentinel, NaN, timeout ve parse hataları etiketlemeden çıkarılır; dışlama sayıları raporlanır.
4. Kararlılık pencereleri PZEM ve SCT için ayrı belirlenir. Sabit 3 saniyelik gecikme veya sabit maske önceden kabul edilmez. Pencere ölçütleri gerçek veride test edilir.
5. Geçiş/yerleşme dinamikleri ayrı analiz edilir; kararlı alan etiketleriyle karıştırılmaz.
6. 24.22 ilk karşılaştırmada korunur. Katsayı/model yalnız eşleşmiş veride sistematik ve tekrarlanabilir sapma gösterilirse güncellenir. Her sürüm yeni calibration_id ile eklenir; eski sürümler korunur.
7. ±%4 saha sonucu kullanıcı raporudur ve harici kodla ilişkilidir. Harici kodun depoda bulunması, bağımsız derlenmesi veya BERO Python hattının aynı sonucu yeniden üretmesi doğrulanmış değildir.

## ct_clamp incelemesi
ESPHome ct_clamp bileşeni şimdilik değiştirilmez veya yeniden yazılmaz. Önce mevcut çıktılar PZEM referansıyla eşleştirilmiş kararlı alanlarda değerlendirilir. Tekrarlanabilir sapma, kararsızlık veya açıklanamayan anomali bulunursa hedefli kaynak kod incelemesi açılır. Önceden alternatif RMS algoritması, dedup düzeltmesi veya firmware değişikliği yapılmaz. Eski teknik inceleme notları kaynak kod gözlemi/hipotez olarak kalır; ölçüm kanıtı sayılmaz.

## Kapatılan / park edilen işler
- Ham 50 Hz dalga aktarımı, örnek başına timestamp, DMA/ADC Continuous: ADR-009 kapsamında KAPATILDI.
- Eski T005/E00A/E01 yüksüz ham ADC ve gürültü tabanı planı: PZEM etiketleme işinin zorunlu ön koşulu olmaktan çıkarıldı; PARK EDİLDİ.
- ct_clamp algoritmasını değiştirme/yeniden yazma: şimdilik yapılmayacak.
- Eski E03–E08 deneyleri otomatik tamamlanmış sayılmaz; yalnız ana hedefe doğrudan veri sağlayan yük koşulları gerekirse yeniden kullanılır.

## Sonraki görev ve kabul sırası
T008, aynı yük olayında PZEM ve E00F SCT verilerini toplama, geçersiz okumaları ayıklama, ayrı kararlılık ölçütleri geliştirme ve ortak alanları etiketleme görevidir. T006 katsayı/model değerlendirmesi T008 çıktısına bağlıdır. Ana yol haritası ROADMAP.md, görev ayrıntısı tasks/T008-pzem-sct-stable-window-labeling.md içindedir.

## HEDEF / LOG / SONUÇ
- **HEDEF:** BERO'yu kapatılmış yüksek hızlı edinim ara işlerinden çıkarıp PZEM referanslı, kararlı alan temelli ve sürekli öğrenen ölçüm geliştirme döngüsüne yöneltmek.
- **LOG:** Kullanıcının talebi ve bu oturumda paylaştığı E00F çalışan YAML'ı temel alındı. Yeni fiziksel PZEM/SCT karşılaştırma ölçümü yapılmadı.
- **SONUÇ:** Yol haritası ve görev sırası bu karara göre düzenlenir. Bu ADR ölçüm/etiketleme/model tamamlandı anlamına gelmez.
