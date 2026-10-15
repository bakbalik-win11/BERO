# GRV-005-14 v01 — Derleme ve Cihaz Sonucu

- Tarih: 2026-10-11
- Cihaz: esp32d1 (ESP32 rev3.1, 2 çekirdek)
- ESPHome: 2026.9.1
- Derleme zamanı: 2026-10-11 11:28:24 +0300
- Cihaz logu: [GRV-005-14-CIHAZ-LOGU-20261011.md](GRV-005-14-CIHAZ-LOGU-20261011.md)

## Hedef

Kilitli CSV v03 başlığını ve kanal başına ölçüm satırlarını ESPHome loguna yazmak; dört satırın cihaz üzerinde üretildiğini doğrulamak.

## Sonuç

**Kısmi PASS — derleme/çalışma ve satır üretimi doğrulandı; CSV v03 alan hizası henüz PASS değil.**

OTA/API bağlantısı başarılı olmuş, cihaz başlatılmış ve CSV başlığı ile CH0-1T, CH1-2T, CH2-3T ve BIAS satırları üretilmiştir.

## Ölçüm özeti

| Alan | CH0-1T | CH1-2T | CH2-3T |
|---|---:|---:|---:|
| sample_count | 1000 | 1000 | 1000 |
| window_duration_ms | 10029 | 10029 | 10029 |
| adc_mean | 1864.222000 | 1861.468000 | 1856.022000 |
| adc_std | 18.428574 | 14.192124 | 11.222186 |
| adc_min | 1613 | 1612 | 1738 |
| adc_max | 2174 | 1972 | 1950 |
| adc_range | 561 | 360 | 212 |
| adc_rms_raw | 1864.312994 | 1861.522047 | 1856.055892 |
| adc_rms_ac | 18.463502 | 14.746385 | 14.683531 |

BIAS satırında bias_mean=1865.498000 ve bias_std=12.662398 değerleri görülüyor; ancak satırın alan hizası kaydığı için satırın tüm sütunları güvenilir biçimde eşleştirilemiyor.

PZEM örnekleri: 0.028 A, 1.50–1.70 W ve PF 0.23–0.27. pzem_update_millis=9624, time_delta_ms=4346. Zaman işareti PZEM sensör callback'ine bağlı yazılım işaretidir; gerçek Modbus yanıt zamanı değildir.

## Düzeltme noktaları

1. **BIAS satırının CSV alan hizası düzeltilmeli.** Mevcut satır CSV v03 uyumlu kabul edilmemeli.
2. CH0/CH1/CH2 satırlarında window_start_millis değeri ' 264' olarak başında boşlukla yazılıyor; boşluk kaldırılmalı.
3. Paylaşılan log kopyasında CSV başlığı pz alanında kesilmiş; tam başlığın çıktısı ayrıca doğrulanmalı.
4. ADC işlemi için 80 ms süre uyarısı oluştu (üst sınır 50 ms). Bu tek başına ölçüm hatası kanıtı değildir; kararlılık değerlendirmesinde izlenmeli.
5. ESP32 rev3.1 için minimum_chip_revision ve sram1_as_iram öneri uyarıları oluştu; bunlar derlemeyi veya cihazın başlatılmasını engellemedi.

## Karar listesi

- [x] Firmware derlendi ve cihaz OTA/API üzerinden erişilebilir oldu.
- [x] CSV başlığı ve dört kanal satırı logda üretildi.
- [ ] CSV v03 satırlarının tümü 42 sütun ve doğru alan eşleşmesi açısından doğrulandı.
- [ ] BIAS satırı düzeltildi ve yeniden test edildi.
- [ ] ADC 80 ms uyarısının etkisi sonraki kararlılık testinde değerlendirildi.

Bu rapor yalnızca paylaşılan logun kanıtladığı sonuçları kaydeder; tüm CSV satırları için tam şema uyumu iddia etmez.