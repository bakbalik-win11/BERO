> **Kapsam notu:** Bu ADR'deki PZEM referanslı kararlı alan öğrenme döngüsü geçerlidir; ancak ADR-014 ile Faz 2'nin tamamı değil, modüller ve ESP düğümleri pratik olarak devreye alındıktan sonraki alt aşaması olarak konumlandırılmıştır.

# ADR-010 — PZEM referanslı kararlı alan etiketleme ve sürekli öğrenme

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ
- **İlişkili kararlar:** ADR-009, ADR-011

## Bağlam

ADR-009 ile Faz 1 hedefi dış kaynaklı çalışan kodla ±%4 sapma olarak sağlandı ve Faz 1 kapatıldı. Bundan sonraki çalışma, bulunan kodun PZEM referans akışıyla eğitilmesi ve zaman içinde iyileştirilmesidir.

## Karar

1. Kullanıcının paylaştığı E00F ESP32D2 YAML çalışan baseline olarak korunur.
2. Ana döngü: HA geçmişini PC'ye aktarma → PZEM ve SCT akışlarında ayrı kararlılık tespiti → örtüşen kararlı alanları eşleştirme → geçerli PZEM değerleriyle etiketleme → K=24.22 katsayısını değerlendirme → veri gerekçelendirirse yeni calibration_id ile iyileştirme → yeni koşullarda tekrar.
3. PZEM proje referansıdır; mutlak ve kusursuz ground truth değildir. -1.0, NaN, timeout ve parse hataları etiketlemeden çıkarılır; dışlama sayıları raporlanır.
4. Kararlılık pencereleri PZEM ve SCT için ayrı belirlenir. Sabit gecikme veya maske önceden kabul edilmez.
5. Geçiş/yerleşme dinamikleri kararlı alan etiketlerinden ayrı tutulur.
6. İlk karşılaştırmada K=24.22 korunur. Katsayı/model yalnız eşleşmiş veride sistematik ve tekrarlanabilir sapma gösterilirse güncellenir.
7. Yeni deneyler önceden doldurulmuş bir liste olarak açılmaz; Faz 2 verisinin ortaya çıkardığı somut sorulara göre yeni numaralarla tasarlanır.

## ct_clamp inceleme kararı

ESPHome ct_clamp bileşeni şimdilik değiştirilmez veya yeniden yazılmaz. Önce mevcut çıktılar PZEM referansıyla eşleştirilmiş kararlı alanlarda değerlendirilir. Tekrarlanabilir sapma veya açıklanamayan anomali bulunursa hedefli kaynak kod incelemesi açılır.

## Görev sırası

1. T007 — HA → PC veri aktarımı.
2. T008 — kararlı alan eşleştirme ve etiketleme.
3. T006 — katsayı/model değerlendirmesi.

