# GRV-005-12 — Çok Kanallı ADC Pencere Cihaz Sonucu
**Tarih:** 2026-10-11  
**Durum:** PASS — bu testin tanımlı kapsamı içinde  
**Kod sürümü:** GRV-005-12 v01 aday YAML (kullanıcının derleme ve cihaz logu bildirimine göre)  

## 1. Hedef
ESP32-D1 üzerinde GPIO33 (CH0-1T), GPIO34 (CH1-2T), GPIO35 (CH2-3T) ve GPIO32 (BIAS) girişlerinden ayrı ayrı 1000 geçerli ham ADC örneği toplamak; üç CH kanalı için BIAS merkezli RMS üretmek ve sonuçları loglamaktır.

## 2. Derleme ve cihaz bilgisi
- ESPHome: 2026.9.1
- Derleme zamanı: 2026-10-11 11:07:56 +0300
- Cihaz: ESP32 rev3.1, 2 çekirdek
- OTA/API bağlantısı başarılı; cihazdan log alındı.
- Derleme uyarıları:
  - ESP32 rev >= 3.0 için `minimum_chip_revision: "3.1"` ayarı önerildi.
  - Bootloader SRAM1'i IRAM olarak destekliyor; `sram1_as_iram: true` önerildi.
  - Bu uyarılar ölçüm sonuçlarının loglanmasını engellemedi.

## 3. Ham cihaz logu
```text
INFO ESPHome 2026.9.1
INFO Loaded validated config cache for esp32d1.yaml, skipping validation.
INFO Starting log output from 192.168.0.8 using esphome API
INFO Successfully resolved esp32d1 @ 192.168.0.8 in 0.000s
INFO Successfully connected to esp32d1 @ 192.168.0.8 in 4.238s
INFO Successful handshake with esp32d1 @ 192.168.0.8 in 0.056s
[11:11:47.944][I][app:151]: ESPHome version 2026.9.1 compiled on 2026-10-11 11:07:56 +0300
[11:11:47.944][I][app:158]: ESP32 Chip: ESP32 rev3.1, 2 core(s)
[11:11:47.945][W][app:171]: Chip rev >= 3.0 detected. Set minimum_chip_revision: "3.1" under esp32 > framework > advanced to reduce binary size
[11:11:47.945][W][app:198]: Bootloader supports SRAM1 as IRAM (+40KB). Set sram1_as_iram: true under esp32 > framework > advanced
[11:11:53.185][I][grv005_window:207]: channel=CH0-1T sample_count=1000 window_duration_ms=10639 invalid_count=NOT_TRACKED zero_count=0 adc_mean=1863.700000 adc_std=7.675475 adc_rms_raw=1863.715789 bias_mean=1865.132000 ac_mean_square=60.904624000 adc_rms_ac=7.804141
[11:11:53.212][I][grv005_window:216]: channel=CH1-2T sample_count=1000 window_duration_ms=10639 invalid_count=NOT_TRACKED zero_count=0 adc_mean=1861.247000 adc_std=7.016639 adc_rms_raw=1861.260213 bias_mean=1865.132000 ac_mean_square=64.277216000 adc_rms_ac=8.017307
[11:11:53.213][I][grv005_window:225]: channel=CH2-3T sample_count=1000 window_duration_ms=10639 invalid_count=NOT_TRACKED zero_count=0 adc_mean=1855.859000 adc_std=8.836810 adc_rms_raw=1855.880017 bias_mean=1865.132000 ac_mean_square=163.999648000 adc_rms_ac=12.806235
[11:11:53.213][I][grv005_window:234]: channel=BIAS sample_count=1000 window_duration_ms=10639 invalid_count=NOT_TRACKED zero_count=0 bias_mean=1865.132000 bias_std=6.258574
```

## 4. Sonuç özeti

| Alan | CH0-1T | CH1-2T | CH2-3T | BIAS |
|---|---:|---:|---:|---:|
| sample_count | 1000 | 1000 | 1000 | 1000 |
| window_duration_ms | 10639 | 10639 | 10639 | 10639 |
| invalid_count | NOT_TRACKED | NOT_TRACKED | NOT_TRACKED | NOT_TRACKED |
| zero_count | 0 | 0 | 0 | 0 |
| adc_mean | 1863.700000 | 1861.247000 | 1855.859000 | — |
| adc_std | 7.675475 | 7.016639 | 8.836810 | 6.258574 |
| adc_rms_raw | 1863.715789 | 1861.260213 | 1855.880017 | — |
| bias_mean | 1865.132000 | 1865.132000 | 1865.132000 | 1865.132000 |
| ac_mean_square | 60.904624000 | 64.277216000 | 163.999648000 | — |
| adc_rms_ac | 7.804141 | 8.017307 | 12.806235 | — |

## 5. Değerlendirme
- Dört kanalın her birinde `sample_count=1000` görüldü.
- Üç CH kanalında BIAS merkezli RMS üretildi; `ac_mean_square` değerleri loglandı ve üçü de pozitif.
- Ortak loglanan pencere süresi 10639 ms.
- Bu nedenle GRV-005-12, **çok kanallı örnek toplama ve BIAS merkezli RMS üretimi** kapsamı için PASS olarak kaydedildi.
- `invalid_count=NOT_TRACKED`: ADC sürücüsünün gerçek hata sayımı elde edilmedi; bu alan gerçek hata sayısı değildir.
- Kanallar donanım seviyesinde eşzamanlı örneklenmiş sayılmaz. Aynı pencere etiketi, örnek çiftlerinin zaman eşleşmesini kanıtlamaz.
- PZEM hizalaması ve CSV üretimi bu görevde uygulanmadı.
- Bu log, cihazın dört kanal için 1000 örnek biriktirdiğini ve özetleri yazdığını gösterir; gerçek elektrik akımı kalibrasyonunu veya sensör doğruluğunu tek başına kanıtlamaz.

## 6. Sonraki görevler
1. GRV-005-13 — PZEM hizalama
2. GRV-005-14 — CSV üretimi
3. GRV-005-15 — Python kalite kontrolü

## 7. Geçmişi koruma
Bu rapor, GRV-005-12 için yeni ve tarihli bir cihaz sonucu kaydıdır. GRV-005-01…11 raporları, önceki YAML sürümleri ve deney geçmişi değiştirilmemiştir.
