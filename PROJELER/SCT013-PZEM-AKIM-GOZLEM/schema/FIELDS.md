# Veri alanları sözlüğü

## Kapsam ve uygulama durumu

Bu belge, ileride üretilecek PZEM okuma kayıtları ve SCT pencere kayıtları için hedef alan sözlüğüdür; tek başına uygulanan JSON Schema, Python modeli veya çalışan doğrulama kodu değildir. Bu alanların tamamı henüz firmware ya da Python çıktısında uygulanmış değildir. E00A'nın ilk aşaması ham ADC örnekleri ve bunların tanımlayıcı istatistiklerini toplar; bu deneyden `sct_current_rms_A` veya `calibration_id` üretilmiş olduğu varsayılmayacaktır. Zorunlu alanlar, ilgili kayıt türü gerçek uygulamaya alındığında geçerlidir; deney sonuçları bu hedef şemayla ilişkilendirilirken mevcut olmayan alanlar uydurulmaz.


## SCT pencere kaydı
| Alan | Durum | Açıklama |
|---|---|---|
| timestamp_start_ms / timestamp_end_ms | Zorunlu | Aynı monotonik saat alanında pencere sınırları |
| sample_rate_actual_hz | Zorunlu | Gerçek gözlenen örnekleme hızı |
| sample_count | Zorunlu | Örneklere giren örnek sayısı |
| sct_current_rms_A | Zorunlu, geçerliyse | Ofset giderilmiş/kalibre edilmiş AC RMS |
| adc_mean_raw, adc_min_raw, adc_max_raw | Önerilen | Bias, dinamik aralık ve clipping teşhisi |
| clipped_sample_count | Zorunlu | ADC sınırına çarpan örnek sayısı |
| calibration_id | Zorunlu | Kullanılan kalibrasyon revizyonu |
| record_status | Zorunlu | ok, calibration_missing, clipped, acquisition_error, invalid |
| event_tag | Önerilen | steady, transition_or_settling, unknown |

## PZEM okuması
| Alan | Durum | Açıklama |
|---|---|---|
| requested_at_ms / response_received_at_ms | Zorunlu | İstek ve yanıt zamanı |
| read_duration_ms | Yanıt varsa zorunlu | İstek/yanıt süresi |
| read_status | Zorunlu | ok, timeout, transport_error, parse_error, invalid_measurement |
| V/I/P/E/frequency/PF alanları | Başarılı okumada | PZEM'in bildirdiği sayısal değerler |
| anomaly_flags / raw_error | Önerilen | Hata ve şüpheli durum ayrıntısı |
| synthetic_example | Şema örneklerinde kullanılan işaret; JSON Schema'da zorunlu | Örnek/sentetik kayıtları gerçek ölçüm verisinden ayırır |

PZEM'in iç ölçüm zamanı bilinmiyorsa yanıt zamanını o zamanın tam karşılığı gibi sunma. `synthetic_example` alanı şemada zorunludur; gerçek veri kaydı uygulandığında değeri açıkça `false`, sentetik örneklerde `true` olmalıdır.
