# SCT013 – PZEM Akım Gözlem

## Projenin amacı

BERO'nun bu alt projesi, SCT013 akım sensöründen elde edilen ölçüm çıktısını çalışan bir kod yolu üzerinden izlemek ve PZEM-004T V3.0 referans akışıyla karşılaştırarak zaman içinde geliştirmektir.

Proje iki ana fazdan oluşur:

- **Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak: TAMAMLANDI.** Dış kaynaklı ESPHome ct_clamp koduyla hedef sağlandı.
- **Faz 2 — Bulunan kodu PZEM ile eğitmek: AKTİF.** Home Assistant verisi PC'ye alınacak; Python ile kararlı alan eşleştirme, etiketleme ve katsayı/model iyileştirme yapılacak.

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

İlk iş **T007 — Home Assistant verisini PC'ye aktarma**. Gerçek PZEM ve SCT entity geçmişleri PC'ye alınacak, kaynak timestamp ve birimler korunacak, Python ile tekrar işlenebilir bir veri girişi oluşturulacak.

Sonraki sıra:
1. T007 — HA → PC aktarımı.
2. T008 — PZEM ve SCT kararlı alanlarını ayrı bulma, örtüşen alanları eşleştirme ve PZEM ile etiketleme.
3. T006 — mevcut K=24.22 katsayısını değerlendirme; yalnız veri gerekçelendirirse iyileştirme.
4. Yeni yük/koşullar geldikçe öğrenme döngüsünü tekrarlama.

Yeni Faz 2 deneyleri şimdiden planlanmayacak. Gerçek verinin cevaplanması gereken somut bir soru ortaya çıkarması hâlinde yeni deney numarasıyla planlanacak.

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
6. [T007](tasks/T007-python-architecture.md) — ilk iş.
7. [Python veri hattı mimarisi](docs/architecture/python-program-architecture.md).
8. [Deney arşivi](experiments/README.md) — Faz 1 tarihçesi.
9. [Karar kayıtları](docs/decisions/).

## Kapsam dışı

- Enerji analizörü veya güç kalitesi ölçümü.
- SCT'den PF/faz açısı hesabı.
- FFT, THD ve harmonik analiz.
- Sürekli ham ADC/50 Hz dalga kaydı ve örnek başına timestamp.
- Faz 1'de hedefe ulaşmak için artık gerekmeyen deneylerin yeniden açılması.
