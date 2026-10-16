# STEP-002 — Tek ESP'den ham sinyal yakalama

**Durum:** BEKLİYOR

- ESP32-WROOM'a doğrulanmış aday firmware'i yükle.
- TEST-001: SCT ve BIAS bağlı, yük kapalı, 100 frame yakala.
- Frame ID, marker'lar, örnek sayısı/sırası ve DMA/USB overflow göstergelerini kaydet.
- Ham kaydı değiştirmeden `LOG/` altında sakla.

Başarı, yalnızca gerçek cihaz kaydı ve loglarla değerlendirilecektir.
