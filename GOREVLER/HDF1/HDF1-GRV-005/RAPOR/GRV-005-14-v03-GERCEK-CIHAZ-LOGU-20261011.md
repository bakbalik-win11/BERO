# PROJE BERO — GRV-005-14 v03 Gerçek Cihaz Logu
**Tarih:** 2026-10-11  
**Cihaz:** ESP32D1OTA / `esp32d1`  
**IP:** `192.168.0.8`  
**ESPHome:** 2026.9.1  
**Derleme zamanı:** 2026-10-11 14:33:01 +0300  
**Log zamanı:** 14:34:37–14:34:54 +0300  
**Kaynak:** Kullanıcının 2026-10-11 tarihinde sohbete yapıştırdığı gerçek ESPHome logu.

## 1. Sonuç özeti

- ESPHome API bağlantısı ve handshake başarılı.
- Çalışan cihaz, ESPHome 2026.9.1 ile 2026-10-11 14:33:01 +0300 tarihinde derlenmiş firmware bildiriyor.
- PZEM akım, güç ve güç faktörü okumaları geliyor.
- CH0-1T, CH1-2T, CH2-3T ve BIAS satırlarının her biri 1000 örnek olarak loglanmış.
- Dört CSV veri satırı görünür durumda.
- ADC bileşeni için bir kez 92 ms işlem süresi uyarısı var (azami 50 ms).
- Log başlığı satırı ekranda `pz` bölümünde kesilmiş görünüyor. Bu, gösterilen log çıktısının tamamının görünmediği anlamına gelebilir; başlığın cihazdan gerçekten eksik yazıldığı bu tek görüntüden kesinleştirilemez.

## 2. Bağlantı ve firmware kanıtı

```text
INFO ESPHome 2026.9.1
INFO Loaded validated config cache for esp32d1.yaml, skipping validation.
INFO Starting log output from 192.168.0.8 using esphome API
INFO Successfully resolved esp32d1 @ 192.168.0.8 in 0.000s
INFO Successfully connected to esp32d1 @ 192.168.0.8 in 4.185s
INFO Successful handshake with esp32d1 @ 192.168.0.8 in 0.015s
[14:34:37.976][I][app:151]: ESPHome version 2026.9.1 compiled on 2026-10-11 14:33:01 +0300
[14:34:37.977][I][app:158]: ESP32 Chip: ESP32 rev3.1, 2 core(s)
[14:34:37.977][W][app:171]: Chip rev >= 3.0 detected. Set minimum_chip_revision: "3.1" under esp32 > framework > advanced to reduce binary size
[14:34:37.977][W][app:198]: Bootloader supports SRAM1 as IRAM (+40KB). Set sram1_as_iram: true under esp32 > framework > advanced
```

## 3. PZEM ölçümleri

Log aralığında tekrarlanan ölçümler:
- Akım: yaklaşık 0.028–0.029 A
- Güç: yaklaşık 1.60–1.80 W
- Güç faktörü: yaklaşık 0.24–0.28

Bu değerler yalnızca logda görülen PZEM okumalarıdır; bağımsız referans ölçümle doğrulanmış değildir.

## 4. Gerçek cihazın CSV satırları

Aşağıdaki dört satır, kullanıcı tarafından sağlanan logdan olduğu gibi alınmıştır.

```text
measurement_id,experiment_id,firmware_version,device_name,channel_id,load_label,notes,window_start_millis,window_end_millis,window_center_millis,window_duration_ms,pzem_update_millis,time_delta_ms,window_center_epoch_s,pzem_timestamp,sample_count,invalid_count,zero_count,adc_mean,adc_std,adc_min,adc_max,adc_range,adc_median,adc_p05,adc_p25,adc_p75,adc_p95,adc_p95_minus_p05,adc_rms_raw,adc_rms_ac,bias_mean,bias_std,bias_min,bias_max,pzem_voltage,pzem_current,pzem_power,pzem_pf,pz
esp32d1_245_001,,,esp32d1,CH0-1T,,,245,10259,5252,10014,9666,4414,,,1000,NOT_TRACKED,0,1862.888000,33.777898,1584,2160,576,,,,,,,1863.193899,33.779911,1864.018000,13.489538,1739,1988,,0.028,1.700,0.2600,,
esp32d1_245_001,,,esp32d1,CH1-2T,,,245,10259,5252,10014,9666,4414,,,1000,NOT_TRACKED,0,1861.430000,26.377545,1623,2082,459,,,,,,,1861.616696,26.491071,1864.018000,13.489538,1739,1988,,0.028,1.700,0.2600,,
esp32d1_245_001,,,esp32d1,CH2-3T,,,245,10259,5252,10014,9666,4414,,,1000,NOT_TRACKED,0,1855.450000,12.092052,1740,1960,220,,,,,,,1855.489362,14.814929,1864.018000,13.489538,1739,1988,,0.028,1.700,0.2600,,
esp32d1_245_001,,,esp32d1,BIAS,,,245,10259,5252,10014,9666,4414,,,1000,NOT_TRACKED,0,1864.018000,13.489538,1739,1988,249,,,,,,,,,1864.018000,13.489538,1739,1988,,0.028,1.700,0.2600,,
```

## 5. Önemli zamanlama notu

- Pencere başlangıcı: 245 ms
- Pencere bitişi: 10259 ms
- Pencere merkezi: 5252 ms
- Pencere süresi: 10014 ms
- Loglanan `pzem_update_millis`: 9666 ms
- Loglanan `time_delta_ms`: 4414 ms

Bu alanlar arasındaki fark, PZEM örneğinin pencere merkezine göre belirgin biçimde geç olduğunu gösteriyor. Ancak mevcut kodda `pzem_update_millis`, PZEM akım sensörünün `on_value` anında alınır; gerçek Modbus paketinin başlama/bitme zamanı olarak yorumlanmamalıdır. Bu nedenle `time_delta_ms` şimdilik yardımcı bir yaklaşık zaman farkıdır.

## 6. ADC gecikme uyarısı

Log:
```text
[14:34:42.809][W][component:419]: adc.sensor took a long time for an operation (92 ms), max is 50 ms
```

Bu uyarı, en az bir ADC sensör işleminin 50 ms sınırını aştığını bildirir. Örnekleme `update_interval: 10ms` olarak ayarlanmışken 92 ms işlem süresi uyarısı, gerçek örnekleme aralıklarının bu ayarla bire bir örtüştüğünün varsayılamayacağı anlamına gelir. Dört kanalda 1000 örnek tamamlanmış olsa da, örneklerin eşzamanlı veya düzenli aralıklı olduğu bu logla kanıtlanmaz.

## 7. QC durumu

- Gerçek cihazdan dört kanal satırı alındı: **PASS**
- Her satırda örnek sayısı 1000 olarak görünüyor: **PASS**
- CSV alan sayısı: başlık logda kesik göründüğünden ve bu raporda otomatik ayrıştırma yapılmadığından **kesin PASS verilmedi**
- Gerçek v03 CSV'nin GRV-005-15 QC v02 ile doğrulanması: **BEKLEMEDE**
- ADC zamanlama davranışı: **inceleme gerekiyor**
- PZEM zaman hizalaması: **logdaki zaman farkı kaydedildi; zaman damgası semantiği sınırlı**

## 8. Sonraki adım

Bu dört satırı gerçek cihaz verisi olarak GRV-005-15 Python QC v02'ye ver; her satırın alan sayısını ve başlıkla alan eşleşmesini otomatik doğrula. Ardından ADC 92 ms uyarısını ayrı bir zamanlama incelemesi olarak ele al. Bu rapor eski kod veya deney kayıtlarının üzerine yazmaz.
