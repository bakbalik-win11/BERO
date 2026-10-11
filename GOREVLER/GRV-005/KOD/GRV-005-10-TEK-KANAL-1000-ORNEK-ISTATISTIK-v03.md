# GRV-005-10 v03 — 1000 örnek tek kanal istatistik penceresi

## Hedef ve donanım
- Hedef: GPIO33 / 1T üzerinden 1000 ham ADC callback örneğinden tek satır istatistik üretmek.
- Donanım: ESP32-D1 / ESP32, GPIO33.
- ESPHome adı korunur: `esp32d1`.
- Kapsam: tek kanal; CSV yok, PZEM yok, dört kanal yok.

## v03
Bu dosya, pencere süresini açıkça `window_duration_ms` alanıyla loglayan yükleme adayıdır. `update_interval: 10ms` hedeflenen güncelleme aralığıdır; kesin 10 ms ADC örnekleme garantisi değildir. Süre, ilk kabul edilen callback'te başlatılan `millis()` değeri ile 1000. kabul edilen callback anındaki farktan hesaplanır.

## Log alanları
- `sample_count`: 1000 kabul edilen callback örneği hedefi.
- `window_duration_ms`: ilk kabul edilen örnekten pencerenin tamamlandığı ana kadar geçen süre.
- `invalid_count=NOT_TRACKED`: ESPHome callback yapısından gerçek ADC sürücü hata sayısı çıkarılmıyor.
- `zero_count`: ham değeri tam sıfır olan geçerli örnekler.
- `adc_mean`: ortalama.
- `adc_std`: örnek standart sapması (N−1).
- `adc_rms_raw`: ham kod RMS.
- `adc_rms_ac=NA_NO_BIAS`: BIAS örneklenmediğinden BIAS merkezli AC RMS bu aşamada hesaplanmaz.

## Beklenen log biçimi
`channel=CH0-1T sample_count=1000 window_duration_ms=... invalid_count=NOT_TRACKED zero_count=... adc_mean=... adc_std=... adc_rms_raw=... adc_rms_ac=NA_NO_BIAS`

## Durum
- Bu v03 dosyası depoya yeni ve ayrı dosya olarak eklendi.
- Derleme: v03 için henüz doğrulanmadı.
- Cihaza yükleme: kullanıcı yapacak; henüz doğrulanmadı.
- Cihaz sonucu: `window_duration_ms` alanının logda görülmesi bekleniyor.
- v01/v02 dosyaları ve eski raporlar korunur.
