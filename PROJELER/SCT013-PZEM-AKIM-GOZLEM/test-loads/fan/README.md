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


## 2026-10-31 — FAN-1 Modül 2 ısınma/deneme kaydı kapatıldı

- Son UNIT bildirimi: **0,093 A**. Önceki bildirimler 0,097 A ve 0,096 A olarak tarihsel nottur.
- Uzatılmış log: `esp32d1-logs (40).txt`; 140.312 bayt / 1.887 satır; SHA-256 `8687da052b254f16b88f6eb6d27d41c94ae8166b027f089f0b6186069c58bedf`; 17:13:51.283–17:22:23.079 (+03:00).
- FAN-1 yaklaşık bölümü: 17:14:11.079 sonrası 247 yayın; ortalama **0,146757 A**, medyan **0,147 A**, min–maks **0,064–0,259 A**, SD **0,026064 A**.
- UNIT 0,093 A için yalnız aritmetik ±%4 bandı 0,08928–0,09672 A'dır; 4/247 (%1,6) yayın bu banttadır. Bu oran tek başına nihai kabul/ret değildir.
- UNIT PF göstermediği için olası PF etkisi değerlendirilemedi. PF açıklaması hipotezdir; FAN-1'in aynı kararlı çalışma penceresinde PZEM akım ve PF kaydıyla yeniden incelenmesi gerekir.
- **KAPANIŞ SINIFI:** FAN-1, Modül 2 ısınma/deneme gözlemi olarak kapatıldı; ±%4 akım doğrulaması olarak kapatılmadı. PZEM ile ileri doğrulama açık kalır.
- FAN-2 ve sonraki fan kademeleri için PZEM akım + PF kaydı gerekli kabul edildi.
- Kod snapshot: [FAN-1 kapanış YAML](../../firmware/archive/FAN-1-2026-10-31-esp32d1-sct1.yaml); [uzun ham log](../../logs/module2/2026-10-31-fan1-module2-sct1-long-full.txt); [uzun analiz](../../logs/module2/2026-10-31-fan1-module2-sct1-long-analysis.md).
