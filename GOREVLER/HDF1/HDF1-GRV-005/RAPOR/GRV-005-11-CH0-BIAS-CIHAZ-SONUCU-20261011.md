# GRV-005-11 — CH0 + BIAS 1000 Örnek Pencere Cihaz Sonucu
**Tarih:** 2026-10-11  
**Durum:** Cihaz logu alındı  
**Görev:** GPIO33 (CH0-1T) ve GPIO32 (BIAS) için ayrı ayrı 1000 ham ADC örneği toplayıp BIAS merkezli RMS üretimini doğrulamak.

## Derleme / cihaz bilgisi
- ESPHome: 2026.9.1
- Derleme zamanı: 2026-10-11 10:58:46 +0300
- Cihaz: ESP32 rev3.1, 2 core
- Log bağlantısı: ESP32D1OTA üzerinden başarıyla bağlandı.
- Derleme uyarıları:
  - Chip rev >= 3.0 için `minimum_chip_revision: "3.1"` ayarı önerildi.
  - Bootloader SRAM1'i IRAM olarak destekliyor; `sram1_as_iram: true` önerildi.
  - Bu uyarılar ölçüm satırının alınmasını engellemedi.

## Ham cihaz logu
```text
[11:02:37.300][I][app:151]: ESPHome version 2026.9.1 compiled on 2026-10-11 10:58:46 +0300
[11:02:37.300][I][app:158]: ESP32 Chip: ESP32 rev3.1, 2 core(s)
[11:02:37.300][W][app:171]: Chip rev >= 3.0 detected. Set minimum_chip_revision: "3.1" under esp32 > framework > advanced to reduce binary size
[11:02:37.301][W][app:198]: Bootloader supports SRAM1 as IRAM (+40KB). Set sram1_as_iram: true under esp32 > framework > advanced
[11:02:42.169][I][grv005_window:203]: channel=CH0-1T bias_channel=BIAS sample_count=1000 bias_sample_count=1000 window_duration_ms=10035 invalid_count=NOT_TRACKED zero_count=0 bias_zero_count=0 adc_mean=1863.449000 adc_std=8.373979 adc_rms_raw=1863.467797 bias_mean=1864.680000 adc_rms_ac=8.459832
```

## Sonuçların özeti
| Alan | Cihaz sonucu |
|---|---:|
| `sample_count` | 1000 |
| `bias_sample_count` | 1000 |
| `window_duration_ms` | 10035 |
| `invalid_count` | NOT_TRACKED |
| `zero_count` | 0 |
| `bias_zero_count` | 0 |
| `adc_mean` | 1863.449000 |
| `adc_std` | 8.373979 |
| `adc_rms_raw` | 1863.467797 |
| `bias_mean` | 1864.680000 |
| `adc_rms_ac` | 8.459832 |

## Değerlendirme
- CH0 ve BIAS sayaçları 1000 örneğe ulaştı.
- Ölçüm penceresi 10035 ms olarak loglandı.
- `adc_rms_ac` geçerli, sonlu ve sıfırdan farklı bir değer olarak üretildi.
- Bu cihaz sonucu, GRV-005-11'in mevcut kapsamı için **PASS**: ayrı örnek kümelerinden alınan BIAS ortalamasına göre merkezlenmiş RMS üretimi doğrulandı.
- **Eşzamanlı örnekleme veya CH0/BIAS örneklerinin zaman eşleşmesi doğrulanmadı.** `sample_count` ve `bias_sample_count` eşit olsa da örnek çiftleri olarak eşleştirilmiş değiller.
- `invalid_count=NOT_TRACKED`: bu alan gerçek sürücü hata sayımı olarak yorumlanmamalı.
- Bu sürüm `ac_mean_square` değerini loglamıyor. Bu sonuçta `adc_rms_ac=8.459832` olduğu için sıfıra bastırma şüphesi görünmüyor; ara değer ayrıca ölçülmüş değil.

## Sonraki adım
GRV-005-11 cihaz sonucu kaydedildi. Sonraki görevler ayrı kayıtlarla ele alınacak:
1. GRV-005-12 — Çok kanallı pencere
2. GRV-005-13 — PZEM hizalama
3. GRV-005-14 — CSV üretimi
4. GRV-005-15 — Python kalite kontrolü

## Kayıt ilkesi
Bu rapor yeni ve tarihli bir deney kaydıdır. Önceki GRV-005 raporları, YAML sürümleri ve cihaz deneyimleri değiştirilmemiştir.
