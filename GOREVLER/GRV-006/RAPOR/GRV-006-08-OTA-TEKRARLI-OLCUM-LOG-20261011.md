# PROJE BERO — GRV-006-08
## ESP32D1 OTA tekrarlı ölçüm log özeti

- Tarih: 2026-10-11
- ESPHome: 2026.9.1
- Cihaz: esp32d1, ESP32 rev3.1
- Derleme: 2026-10-11 19:38:15 +0300
- API bağlantısı: başarılı, 192.168.0.9

### Logdan alınan kanıt

1. 19:40:10.746 — CSV_HEADER_PART_1
2. 19:40:10.766 — CSV_HEADER_PART_2
3. 19:40:10.790 — CH0-1T satırı; sample_count=1000
4. 19:40:10.807 — CH1-2T satırı; sample_count=1000
5. 19:40:10.837 — CH2-3T satırı; sample_count=1000
6. 19:40:10.874 — BIAS satırı; sample_count=1000
7. 19:40:10.972 — NEXT_MEASUREMENT_READY
8. 19:40:21.000 — CSV_HEADER_PART_1 tekrarlandı
9. 19:40:21.012 — CSV_HEADER_PART_2 tekrarlandı
10. 19:40:21.030 — CH0-1T satırı; sample_count=1000
11. 19:40:21.055 — CH1-2T satırı; sample_count=1000
12. 19:40:21.078 — CH2-3T satırı; sample_count=1000
13. 19:40:21.105 — BIAS satırı; sample_count=1000
14. 19:40:21.227 — NEXT_MEASUREMENT_READY tekrarlandı

### Sonuç

**PASS — tekrarlı rapor üretimi gözlendi.** İki ardışık ölçüm grubunda başlıklar ve dört kanal satırı üretildi. PZEM akışının devam ettiği de logda görülüyor.

### Açık konular

- invalid_count = NOT_TRACKED.
- ADC RMS değerleri ham ADC sayımlarıdır; amper kalibrasyonu ve fiziksel akım doğruluğu bu logla kanıtlanmaz.
- window_duration_ms yaklaşık 10060 ms görünüyor; örnekleme zamanlaması ayrıca incelenecek.
- Bu dosya, kullanıcı tarafından paylaşılan OTA logunun kanıt özetidir; ham logun birebir kopyası değildir.
