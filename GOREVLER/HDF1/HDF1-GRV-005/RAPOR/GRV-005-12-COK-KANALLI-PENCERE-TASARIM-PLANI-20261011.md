# GRV-005-12 — Çok Kanallı ADC Pencere Tasarım Planı
**Tarih:** 2026-10-11  
**Durum:** Tasarım kapsamı tanımlandı; firmware kodu henüz derlenmedi veya cihazda doğrulanmadı.  
**Ön koşul:** GRV-005-11 cihaz sonucu PASS olarak kaydedildi.

## 1. Hedef
ESP32-D1 üzerinde aşağıdaki ADC girişlerinden ayrı ayrı 1000 geçerli ham ADC callback örneği toplamak ve aynı ölçüm çevrimi için kanal istatistiklerini üretmek:
- `CH0-1T`: GPIO33
- `CH1-2T`: GPIO34
- `CH2-3T`: GPIO35
- `BIAS`: GPIO32

Bu aşamanın hedefi çok kanallı pencere toplama ve kanal başına istatistik üretimidir. PZEM hizalaması, CSV yazımı ve Python kalite kontrolü bu görevin kapsamı dışındadır.

## 2. Her kanal için üretilecek alanlar
CH kanallarının her biri için:
- `sample_count`
- `zero_count`
- `adc_mean`
- `adc_std` (örnek standart sapması, N−1)
- `adc_rms_raw`
- `bias_mean`
- `adc_rms_ac`

BIAS için:
- `bias_sample_count`
- `bias_zero_count`
- `bias_mean`
- BIAS kanalının kendi istatistikleri, uygulama logunda ayrıca açıkça belirtilecek.

Ortak alanlar:
- `window_duration_ms`
- `invalid_count=NOT_TRACKED` (ADC API'si gerçek hata sayısını vermediği sürece)
- kanal kimlikleri: `CH0-1T`, `CH1-2T`, `CH2-3T`, `BIAS`.

## 3. Kabul ölçütleri
1. Dört kanalın her biri için sayaç hedefi 1000'e ulaşır.
2. Tamamlanan ölçüm çevriminde CH0-1T, CH1-2T ve CH2-3T için birer log satırı; BIAS için bir özet satırı üretilir.
3. Her CH satırında `bias_mean` ve `adc_rms_ac` bulunur.
4. `window_duration_ms` ölçülüp loglanır.
5. Geçerli ham ADC değeri 0 olduğunda örnek geçerli sayılır ve `zero_count` artırılır.
6. Geçersiz callback değerleri örnek sayacına eklenmez; fakat sürücü hata sayısı bilinmiyorsa `invalid_count` tahmin edilmez ve `NOT_TRACKED` kalır.
7. Önceki görevlerin YAML ve raporları değiştirilmez.

## 4. Zamanlama ve eşzamanlılık sınırı
Dört ADC sensörünün ESPHome callback'leri aynı anda örnekleme garantisi vermez. Her kanalın 1000 örneği ayrı birikim kümesidir; aynı sıra numaralı örnekler eşleştirilmiş çiftler olarak yorumlanamaz. Pencere süresi, ilk geçerli callback ile tüm kanal sayaçlarının hedefe ulaşıp son özetin yazıldığı an arasındaki `millis()` farkıdır. Bu değer, her kanalın tam olarak aynı 1000 örnek boyunca ölçüldüğünü veya örnek çiftlerinin eşzamanlı olduğunu kanıtlamaz.

## 5. Matematik
CH kanalı için:
- `adc_mean = sum(CH) / N`
- `adc_rms_raw = sqrt(sum(CH²) / N)`
- `adc_std`: Welford birikimiyle örnek standart sapması (N−1)
- `adc_rms_ac = sqrt(mean(CH²) - 2 × bias_mean × mean(CH) + bias_mean²)`

Uygulama ara kare değerini negatiften sıfıra sınırlarsa, bu davranış raporda açıkça belirtilecek. İleride sıfırdan beklenmedik sonuç çıkarsa `ac_mean_square` ayrıca loglanabilir.

## 6. Kapsam dışı
- PZEM güncelleme zamanı ve zaman farkı
- CSV üretimi ve tam GRV-005-04 şemasının uygulanması
- Python kalite kontrolü
- Donanım seviyesinde eşzamanlı ADC örneklemesi
- ADC API'si tarafından sağlanmayan hata sayısının tahmini

## 7. Sürüm ve kayıt ilkesi
Kod, derleme ve cihaz testinden önce aday sürüm olarak kalır. Kullanıcı başarılı derlemeyi doğruladıktan sonra sonuç ayrı tarihli rapor olarak eklenir. GRV-005-01…11 kayıtları ve eski YAML sürümleri korunur; üzerine yazılmaz.
