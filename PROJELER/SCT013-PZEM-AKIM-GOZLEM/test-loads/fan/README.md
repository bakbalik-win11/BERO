# FAN-1 — Modül 2 / SCT-1 test kaydı

- Test: Fan kademe 1 (FAN-1), Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35.
- UNIT: İlk bildirim 0,097 A; son bildirim 0,096 A. Geçici UNIT değeri 0,096 A; ±%4 aralığı 0,09216–0,09984 A.
- Not: UNIT ölçümü kesin referans değildir; fan PF bilgisi UNIT'te görünmüyor. PZEM daha sonra eklenecek.
- Uzun ham log: [FAN-1 tam log](../../logs/module2/2026-10-31-fan1-module2-sct1-extended-full.txt).
- Analiz: [FAN-1 log analizi](../../logs/module2/2026-10-31-fan1-module2-sct1-analysis.md).
- Log zamanı: 17:13:53.070–17:17:05.067 (+03:00), 97 akım yayını.
- Kullanıcı notu: İlk açılışta çok kısa yüksüz bölüm var. Bu bölüm kararlı FAN-1 ölçümünden ayrı tutulmalıdır.
- Kararlı kademe sınırı logda olay işaretiyle kaydedilmediğinden geçiş/kararlı ayrımı yaklaşık kalır.
- K=24.22 korunur; yazılımsal sıfır eşiği eklenmez.
