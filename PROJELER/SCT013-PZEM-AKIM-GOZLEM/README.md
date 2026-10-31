# SCT013 – PZEM Akım Gözlem

## Projenin amacı

BERO'nun bu alt projesi, SCT013 akım sensöründen elde edilen ölçüm çıktısını çalışan bir kod yolu üzerinden izlemek ve PZEM-004T V3.0 referans akışıyla karşılaştırarak zaman içinde geliştirmektir.

Proje iki ana fazdan oluşur:

- **Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak: TAMAMLANDI.** Dış kaynaklı ESPHome ct_clamp koduyla hedef sağlandı.
- **Faz 2 — Pratik yeniden kurulum ve sistem geliştirme: AKTİF.** Kayıtlı kod ve çalışan örneklerden yararlanarak modüller ve ESP düğümleri tek tek devreye alınacak; ardından PZEM referanslı veri aktarımı, kararlı alan eşleştirme ve model iyileştirmesi yapılacak.

Bu proje enerji analizörü, güç kalitesi analizörü veya harmonik analiz sistemi değildir.

## Faz 1 — kapanış sonucu

Dış kaynaklı çalışan kodla yapılan karşılaştırmalar:

| Yük koşulu | Referans | Kod sonucu | Sapma |
|---|---:|---:|---:|
| 100 W akkor | 0,446–0,447 A | 0,4471 A | yaklaşık %0 |
| 150 W akkor | 0,616 A | 0,615 A | −%0,2 |
| Kettle düşük/kararlı | 0,637 A | 0,656 A | +%3,0 |
| Kettle kaynama | 6,39 A | 6,15 A | −%3,8 |

Dört karşılaştırmanın tamamı ±%4 sınırındadır. Faz 1 hedefi sağlandığı için bu fazın yapılmamış deney ve işleri de kapatılmıştır. Eski deney kayıtları silinmez; [Faz 1 deney arşivinde](experiments/README.md) tutulur. Kapatılan bir planın fiziksel olarak yapılmış olduğu iddia edilmez. Karar: [ADR-009](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md).

## Faz 2 — güncel çalışma

Faz 2, yeni bir pratik başlangıçtır: önce çalışan kod/örnek bulunur, kayıtlı YAML ve donanım bilgileri başlangıç referansı olarak kullanılır, modüller ve ESP düğümleri tek tek devreye alınır. Her modül için derleme, bağlantı ve gerçek donanım çıktısı ayrı doğrulanır. Başarılı kod, gerçek log/çıktı ve yorum depoda saklanır.

İlk aktif iş **T009 — modülleri ve ESP düğümlerini pratik olarak yeniden devreye alma**. Manyetik teori veya ESP32 ADC iç mimarisi, somut bir sorun veya uygulama kararı gerektirmediği sürece çalışma odağı yapılmaz. Önceki araştırmalar tarihsel teknik referans olarak korunur.

Modüller çalışır ve gerçek Home Assistant entity akışları oluşur hâle geldikten sonra:
1. T007 — HA → PC veri aktarımı.
2. T008 — PZEM ve SCT kararlı alanlarını ayrı bulma, örtüşen alanları eşleştirme ve PZEM ile etiketleme.
3. T006 — mevcut K=24.22 katsayısını değerlendirme; yalnız veri gerekçelendirirse iyileştirme.

Faz 2 kapsamı: [ADR-014](docs/decisions/ADR-014-phase2-practical-restart.md). İlk görev: [T009](tasks/T009-practical-system-bringup.md).

## Çalışan ölçüm baseline'ı

- ESP32D2 / E00F.
- ESPHome ct_clamp.
- SCT giriş GPIO33.
- sample_duration: 200ms.
- update_interval: 2s.
- Mevcut katsayı K=24.22.

Bu ayarlar ilk PZEM/SCT veri karşılaştırmasında başlangıç baseline'ıdır. Gerekçe ve eşleşmiş veri olmadan firmware veya ct_clamp değiştirilmez. [Firmware kaydı](firmware/esp32d2.yaml).

## Donanım referansları

- Öncelikli SCT: [SCT013-030 — 30 A / 1 V](hardware/references/SCT013-30A-1V.md).
- Diğer SCT/CT stokları: [donanım envanteri](hardware/inventory.md).
- PZEM-004T V3.0: [proje referansı](hardware/references/PZEM-004T-V3.0.md); PZEM'e bağlı CT modeli PZCT-02 (0–100 A) olarak kaydedilmiştir.
- Bias alt devresi: breadboard üzerinde 2 × 10 kΩ ve 104/100 nF kondansatör; [analog ön uç kaydı](hardware/frontend.md).
- ESP32D2, ESP32-WROOM ve diğer kartlar: [donanım envanteri](hardware/inventory.md).
- SSR ve DS3231, olay/zamanlama altyapısının donanım referanslarıdır.

## Öncelikli okuma sırası

1. [AGENTS.md](AGENTS.md) — çalışma protokolü.
2. [STATUS.md](STATUS.md) — güncel aktif görev.
3. [ROADMAP.md](ROADMAP.md) — yalnız iki ana faz.
4. [PROGRESS_TREE.md](PROGRESS_TREE.md) — genel görünüm.
5. [tasks/README.md](tasks/README.md) — Faz 2 görev sırası.
6. [T009](tasks/T009-practical-system-bringup.md) — ilk aktif iş.
7. [T007](tasks/T007-python-architecture.md) — sonraki veri aktarımı adımı.
7. [Python veri hattı mimarisi](docs/architecture/python-program-architecture.md).
8. [Deney arşivi](experiments/README.md) — Faz 1 tarihçesi.
9. [Karar kayıtları](docs/decisions/).

## Kapsam dışı

- Enerji analizörü veya güç kalitesi ölçümü.
- SCT'den PF/faz açısı hesabı.
- FFT, THD ve harmonik analiz.
- Sürekli ham ADC/50 Hz dalga kaydı ve örnek başına timestamp.
- Faz 1'de hedefe ulaşmak için artık gerekmeyen deneylerin yeniden açılması.
