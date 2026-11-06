# E15 — Sonuç defteri

**Durum:** TEST BEKLİYOR  
**Deney firmware'i:** [bero-modul2-e15-single-sct-interval.yaml](../../firmware/experiments/bero-modul2-e15-single-sct-interval.yaml)

## Ortak koşullar

- SCT: CH1-1T / GPIO32 / sarı
- Fiziksel SCT kimliği/seri tanımı: 
- Fiziksel yük ve bağlantı noktası: 
- `sample_duration`: 100 ms
- K: 24.22
- ESPHome sürümü: 
- YAML commit / içerik SHA: 
- Ortak koşul sapması veya test arası müdahale: 

## İlk cihaz çalışma kontrolü — 2026-11-06

**Durum:** Kısa cihaz ön kontrolü LOG İLE DESTEKLENDİ; 10 dakikalık A turu henüz tamamlanmadı.

- ESPHome 2026.10.2; API bağlantısı/handshake başarılı.
- GPIO32 / ADC1_CH4 başlatma, konfigürasyon ve kalibrasyon OK.
- ct_clamp sample_duration=100ms; update_interval=never.
- 28.492 saniyede 58 CH1 akım yayını; medyan yayın aralığı 0.500s (min 0.427s, max 0.577s).
- UDP EVENT_ID=314 / STATE=OFF paketi alındı ve HA text_sensor alanlarına yayınlandı.
- UDP OFF işareti fiziksel yükün kapandığını kanıtlamaz.
- Bu kısa log sıçrama karşılaştırması veya 10 dakikalık A turu sonucu değildir.

Kaynaklar: [ham cihaz logu](../../logs/module2/2026-11-06-e15-a-500ms-initial-device-log.txt), [log analizi](../../logs/module2/2026-11-06-e15-a-500ms-initial-device-log-analysis.md).

## Tur A — 500 ms / 2 Hz

- Başlangıç / bitiş (yerel saat +03:00):
- HA CSV / kaynak dosya:
- Kaynak SHA-256:
- Kayıt süresi:
- Toplam CH1 kayıt:
- Medyan / P05 / P95 yayın aralığı:
- Eksik veya uzun aralıklar:
- Akım ortalama / medyan / SD:
- Ardışık mutlak fark medyan / P95 / P99 / maksimum:
- Ortak sıçrama eşiği:
- Sıçrama adedi:
- Sıçrama / dakika:
- Sıçrama / 1.000 yayın:
- Geçiş veya veri dışlama kuralı:
- Yorum / kanıt sınırı:

## Tur B — 1 s / 1 Hz

- Başlangıç / bitiş (yerel saat +03:00):
- HA CSV / kaynak dosya:
- Kaynak SHA-256:
- Kayıt süresi:
- Toplam CH1 kayıt:
- Medyan / P05 / P95 yayın aralığı:
- Eksik veya uzun aralıklar:
- Akım ortalama / medyan / SD:
- Ardışık mutlak fark medyan / P95 / P99 / maksimum:
- Ortak sıçrama eşiği:
- Sıçrama adedi:
- Sıçrama / dakika:
- Sıçrama / 1.000 yayın:
- Geçiş veya veri dışlama kuralı:
- Yorum / kanıt sınırı:

## Tur C — 2 s / 0,5 Hz

- Başlangıç / bitiş (yerel saat +03:00):
- HA CSV / kaynak dosya:
- Kaynak SHA-256:
- Kayıt süresi:
- Toplam CH1 kayıt:
- Medyan / P05 / P95 yayın aralığı:
- Eksik veya uzun aralıklar:
- Akım ortalama / medyan / SD:
- Ardışık mutlak fark medyan / P95 / P99 / maksimum:
- Ortak sıçrama eşiği:
- Sıçrama adedi:
- Sıçrama / dakika:
- Sıçrama / 1.000 yayın:
- Geçiş veya veri dışlama kuralı:
- Yorum / kanıt sınırı:

## Üç tur karşılaştırması

| Ölçüt | A: 500 ms | B: 1 s | C: 2 s |
|---|---:|---:|---:|
| Gerçek medyan yayın aralığı | — | — | — |
| Kayıt adedi | — | — | — |
| Ardışık mutlak fark P95 | — | — | — |
| Ardışık mutlak fark P99 | — | — | — |
| Sıçrama / dakika | — | — | — |
| Sıçrama / 1.000 yayın | — | — | — |
| Akım SD | — | — | — |

## Sonuç

Henüz sonuç yok. Herhangi bir yayın aralığının daha kararlı olduğu veya fiziksel sıçramaları azalttığı iddia edilmemiştir. Daha seyrek örneklemenin kısa olayları kaçırabileceği karşılaştırma yorumunda korunacaktır.
