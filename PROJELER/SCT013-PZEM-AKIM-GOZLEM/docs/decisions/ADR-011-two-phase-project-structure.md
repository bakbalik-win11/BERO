> **Sonraki kapsam güncellemesi:** Bu ADR'de Faz 2 ilk olarak PZEM referanslı öğrenme olarak tanımlanmıştı. 2026-10-31 tarihli [ADR-014](ADR-014-phase2-practical-restart.md), bu tanımı genişleterek Faz 2'nin ana kapsamını pratik sistemin yeniden kurulması ve geliştirilmesi olarak güncelledi. T007 → T008 → T006 sırası, sistem düğümleri çalıştıktan sonraki veri/öğrenme alt aşaması olarak korunur.

# ADR-011 — Projeyi iki ana faza ayırma ve Faz 2'yi başlatma

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ
- **Karar:** Faz 1 kapatıldı; Faz 2 aktif çalışma yönüdür.

## Bağlam

Önceki yol haritası hazırlık, analog ön uç, ham edinim, PZEM edinimi, zaman ilişkisi, kayıt şeması, deneyler ve analiz gibi çok sayıda faza bölünmüştü. Bu yapı eski deneyleri hâlâ yapılması gereken işler gibi gösteriyor ve güncel hedefi belirsizleştiriyordu.

## Karar

Proje bundan sonra yalnızca iki ana faz olarak yürütülür.

### Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak

**TAMAMLANDI.** Dış kaynaklı ESPHome ct_clamp kodu kullanılarak ±%4 hedefi sağlandı. 100 W akkor, 150 W akkor, kettle düşük/kararlı ve kettle kaynama karşılaştırmalarının tamamı ±%4 sınırındadır.

Faz 1 kapsamındaki eski deneyler ve ara işler tarihsel Faz 1 arşivine alınır. Ana hedefe ulaşıldığı için yapılmamış kalan deney ve işler de **KAPATILDI — HEDEFE ULAŞILDI** olarak işaretlenir. Kapatılmaları fiziksel olarak yapılmış oldukları anlamına gelmez. Gerçek log ve sonuç dosyaları korunur.

### Faz 2 — Bulunan kodu PZEM ile eğitmek

**AKTİF.** Mevcut çalışan SCT kodu PZEM-004T V3.0 referans akışıyla eşleştirilir. Önce HA verisi PC'ye aktarılır; ardından PZEM ve SCT kararlı alanları ayrı bulunur, örtüşen alanlar eşleştirilir, PZEM akımıyla SCT pencereleri etiketlenir ve K=24.22 değerlendirilir. Verinin gerekçelendirdiği iyileştirmeler yeni calibration_id ile sürümlenir.

## Faz 2 iş sırası

1. T007 — Home Assistant geçmişini PC'ye aktarma ve Python veri giriş hattı.
2. T008 — PZEM/SCT kararlı alan tespiti, eşleştirme ve etiketleme.
3. T006 — K=24.22 ve model değerlendirmesi.
4. Yeni deneyler yalnız gerçek veri yeni bir soruyu ortaya çıkardığında, yeni numaralarla tasarlanır. Şu anda yeni Faz 2 deneyi planlanmamıştır.

## Korunan baseline ve ct_clamp kararı

E00F ESP32D2 yapılandırması, cihaz kimliği, pinler, 200 ms pencere, 2 s yayın aralığı ve K=24.22 ilk karşılaştırma baseline'ı olarak korunur. Önce PZEM ile eşleştirilmiş veri toplanır. ct_clamp kaynak kodu ancak bu veride tekrarlanabilir sorun görülürse hedefli incelenir; önceden değiştirilmez.

## Sonuç

- Proje iki ana faza indirildi.
- Faz 1 kapatıldı; Faz 2 aktif oldu.
- Eski deneyler tarihsel arşivdir; Faz 2 ön koşulu değildir.
- İlk aktif iş T007'dir.
