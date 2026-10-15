# GRV-005-05 — Matematik self-test cihaz sonucu

- Tarih: 2026-10-11
- Test: GRV-005-05 kontrollü matematik self-test
- Cihaz: `esp32d1`
- ESPHome: 2026.9.1
- Sonuç: **PASS — paylaşılan cihaz logunda gözlendi**
- Kaynak: Kullanıcının paylaştığı ESP32D1OTA logu; test zamanı yaklaşık 10:26:58.
- Kapsam: Sabit test vektörü `x = {1, 2, 3, 4}`, `bias_mean = 2.5`. ADC ve PZEM gerçek okumaları yapılmadı.

## Gözlenen çıktı

| Alan | Log değeri | Beklenen |
|---|---:|---:|
| sample_count | 4 | 4 |
| zero_count | 0 | 0 |
| adc_mean | 2.500000 | 2.500000 |
| adc_std | 1.290994 | 1.29099445 |
| adc_rms_raw | 2.738613 | 2.73861279 |
| adc_rms_ac | 1.118034 | 1.11803399 |
| RESULT | PASS | PASS |

Log ayrıca `invalid_count=NOT_TESTED` değerini, beklenen değer satırlarını ve `MATH SELF TEST START/END` kayıtlarını içeriyor.

## Yorum ve doğrulama sınırı

- Derleme hatası olarak görülen `isfinite` isim alanı problemi düzeltilmiş sürümde aşılmış görünüyor; cihaz logunda self-test çalışmış ve PASS vermiştir.
- Bu sonuç yalnızca sabit test vektörünün ortalama, örnek standart sapması, ham RMS ve bias çıkarılmış RMS hesaplarını doğrular.
- Gerçek ADC okuma başarısızlığı/invalid_count davranışı test edilmedi.
- Gerçek SCT-013 akım ölçümü, PZEM zaman hizalaması, CSV üretimi ve cihazın gerçek ölçüm döngüsü bu testin kapsamı dışındadır.
- Paylaşılan log, düğme üzerinden tetiklenen testin başlangıç ve bitişini göstermektedir.

## Sonraki adım

Matematik self-test doğrulaması tamamlandı. Sonraki adım, GRV-005-04 CSV sözleşmesindeki açık kararları gözden geçirip kilitlemek; ardından gerçek ADC veri penceresi uygulamasını ayrı, sürümlenmiş bir görev olarak planlamaktır. Cihaza yeni firmware yükleme işlemleri ayrıca açıkça onaylanmalıdır.

## Geçmişi koruma

Bu kayıt yeni ve eklemeli bir sonuç kaydıdır. Önceki raporlar, GRV-002/004, ALT09 ve ALT10 kayıtları değiştirilmemiştir.
