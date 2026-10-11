# GRV-005-10 — Tek kanal 1000 örnek istatistik penceresi v02

## Hedef
GPIO33 / 1T üzerinden 1000 ham ADC callback örneği toplayıp tek satır istatistik üretmek; pencerenin gerçek geçen süresini de ölçmek.

## Donanım ve kapsam
- ESP32-D1, GPIO33 / 1T
- ESPHome ADC, `raw: true`
- `update_interval: 10ms`; bu yalnızca istenen güncelleme aralığıdır, 10 ms kesin örnekleme garantisi değildir.
- CSV yok, PZEM yok, dört kanal yok.
- Cihaz adı `esp32d1` olarak korunmuştur.

## v02 değişikliği
`window_start_ms` ilk kabul edilen callback'te başlatılır. 1000 geçerli callback örneğine ulaşıldığında `millis() - window_start_ms` ile `window_duration_ms` hesaplanır ve tek satır loga eklenir. İşlem unsigned 32-bit farkı kullandığından normal `millis()` taşması boyunca geçen süre hesabı korunur (tek pencere süresi sayaç turundan çok kısa olmalıdır). Sonrasında yeni pencerenin başlangıç zamanı sıfırlanır.

## Üretilen alanlar
- `sample_count`: kabul edilen sonlu, negatif olmayan callback örnekleri; hedef 1000.
- `window_duration_ms`: ilk kabul edilen örnekten 1000. örnek işlendiği ana kadar geçen süre.
- `invalid_count=NOT_TRACKED`: callback tabanlı bu tasarım gerçek ADC sürücü hatalarını saymaz.
- `zero_count`: ham değeri tam sıfır olan geçerli örnek sayısı.
- `adc_mean`: aritmetik ortalama.
- `adc_std`: örnek standart sapması, payda N−1 (Welford çevrimiçi hesabı).
- `adc_rms_raw`: ham kodların RMS değeri.
- `adc_rms_ac=NA_NO_BIAS`: BIAS kanalı bu testte okunmadığından BIAS merkezli RMS hesaplanmaz.

## Beklenen log şekli
`channel=CH0-1T sample_count=1000 window_duration_ms=... invalid_count=NOT_TRACKED zero_count=... adc_mean=... adc_std=... adc_rms_raw=... adc_rms_ac=NA_NO_BIAS`

Bu bir şablondur; gerçek sayısal sonuçlar cihaz logundan alınmalıdır. Önceki GPIO33 logundaki 1853–1872 değerleri yalnızca önceki gözlemdir, yeni pencerenin sonucu olarak kabul edilmez.

## Doğrulama durumu
- Kaydedilen aşama: v02 kod taslağı.
- Derleme: bu sürüm için henüz doğrulanmadı.
- Cihaz yüklemesi / 1000 örnek penceresi: henüz doğrulanmadı.
- v01 ve önceki raporlar korunur.

## Kabul ölçütleri
1. Bu YAML derlemesi başarılı olmalı.
2. Cihazda log `sample_count=1000` göstermeli.
3. `window_duration_ms` sıfırdan büyük olmalı ve gerçek logdan okunmalı.
4. İstatistikler sonlu sayılar olmalı.
5. `invalid_count` ve BIAS merkezli RMS eksikliği açıkça belirtilmeye devam etmeli.
