# GRV-004 — BIAS + 1T/2T/3T ADC adlandırma seviyesi

- **Tarih:** 2026-10-10
- **Cihaz:** `esp32d1` / ESP32D1
- **Durum:** Kullanıcı tarafından başarılı olarak bildirildi.
- **BIAS fiziksel referansı:** GPIO32 üzerinde multimetreyle 1,65 V.
- **Bağlantı kontrolü:** Kullanıcı tarafından OK olarak doğrulandı.
- **BIAS sensör adı:** `BIAS Ham Voltaj` — GPIO32.
- **1T sensör adı:** `1T Ham Voltaj` — GPIO33.
- **2T sensör adı:** `2T Ham Voltaj` — GPIO34.
- **3T sensör adı:** `3T Ham Voltaj` — GPIO35.
- **PZEM:** Önceki UART/Modbus ayarları korundu (TX GPIO16, RX GPIO17, 9600 baud).
- **ADC ayarları:** 12 dB attenuation, 1 saniye güncelleme, 3 ondalık basamak.
- **Kod:** [Tam YAML](../KOD/esp32d1-bias-1t-2t-3t.yaml)

## Sonuç ve sınırlar

Kullanıcı, kodun başarılı olduğunu ve fiziksel bağlantı kontrollerinin OK olduğunu bildirdi. GPIO32'de fiziksel bias ölçümü 1,65 V olarak kaydedildi.

Bu raporda ESPHome'un canlı BIAS ADC değeri ayrıca verilmediği için ADC ile multimetre arasındaki fark hesaplanmamıştır. 1000 örnek × 3 kanal hızlı kararlılık testi de bu kayıtta yapılmış sayılmaz.

## Koruma kuralı

Bu seviye, önceki `esp32d1-pzem-sct-3kanal.yaml` dosyasının üzerine yazmadan ayrı dosya olarak kaydedildi.
