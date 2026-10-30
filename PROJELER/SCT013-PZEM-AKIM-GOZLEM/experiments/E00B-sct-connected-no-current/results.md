# E00B sonuç kaydı

## 2026-10-30 — Deney açılışı

### HEDEF
SCT013-030 bağlandıktan sonra, izlenen iletkende akım yokken SCT analog düğümünün bias ve ADC dalgalanmasını E00A SCT'siz bias-only tabanıyla karşılaştırmak.

### LOG
- Deney kimliği: E00B.
- Bias kanalları: GPIO34 RAW (ADC1_CH6), GPIO35 ADC voltajı (ADC1_CH7).
- SCT kanalları önerisi: GPIO32 RAW (ADC1_CH4), GPIO33 ADC voltajı (ADC1_CH5).
- Kart adayı: ESP32-WROOM-32D; gerçek geliştirme kartı pinout'u doğrulanmadı.
- Öncelikli sensör: SCT013-030 (30 A / 1 V).
- Fiziksel bağlantı, firmware, derleme ve cihaz logu henüz yok.

### SONUÇ
Deney açıldı ve pin planı önerildi. GPIO32/33 fiziksel pinout doğrulaması beklediğinden bağlantı yapılmamalıdır. Henüz ölçüm sonucu yoktur. İlk ölçüm koşulu SCT bağlı, primer akım sıfır ve yük kapalı/enerjisiz durumudur.
