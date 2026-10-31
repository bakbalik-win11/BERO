# FAN-1 — Modül 2 / SCT-1 uzun log analizi

- Kaynak: `esp32d1-logs (39).txt`
- Özgün dosya SHA-256: `ccc520db070555741d45f3fa67b5866011bec0dadc092c839eb52ff5502eba8e`
- Depodaki tam ham log: [2026-10-31-fan1-module2-sct1-extended-full.txt](../../logs/module2/2026-10-31-fan1-module2-sct1-extended-full.txt)
- Cihaz: ESP32D1 / Modül 2; ESPHome 2026.10.1; SCT-1 GPIO32 / ADC1_CH4; ortak bias GPIO35 / ADC1_CH7.
- Yapılandırma: ADC 12 dB, 1 s güncelleme; ct_clamp 200 ms pencere, 2 s yayın.
- Akım yayını: 97 kayıt; 17:13:53.070–17:17:05.067 (+03:00).
- Dağılım (tüm kayıt): ortalama 0,14114 A; medyan 0,147 A; min–maks 0,000–0,259 A.
- İlk açılışta 0,000 / 0,081 / 0,049 / 0,000 / 0,057 A gibi kısa geçiş değerleri görülüyor. Kullanıcı ilk açılışın çok kısa süre yüksüz olduğunu bildirdi; bu bölüm kararlı FAN-1 ölçümüyle birleştirilmemelidir.
- 17:14:11.079 sonrası 88 yayın: ortalama 0,15295 A; medyan 0,149 A; min–maks 0,105–0,259 A. Bu aralık yalnız log zamanına göre ayrılmıştır; fanın gerçek kararlı devreye giriş anı logda işaretli değildir.
- UNIT FAN-1 bildirimi: ilk 0,097 A, son güncelleme 0,096 A. ±%4 bandı 0,09216–0,09984 A. Logdaki son bölümün tüm değerleri bu bandın üzerindedir; ancak hız/kademe ve gerçek kararlı pencere sınırı teyit edilmeden kesin sapma/başarısızlık kararı verilmez.
- PZEM yok; UNIT bilgisi kullanıcı bildirimidir. UNIT'in PF gösteremediği not edildi; daha sonra PZEM ile yeniden değerlendirilecek.
- Üç derleyici uyarısı var; görünen kayıtta ADC init/config/calibration OK. Ham logda PZEM/UNIT telemetrisi yok.
- Karar: K=24.22 korunur; yazılımsal sıfır eşiği eklenmez. Başlangıç yüksüz/geçiş bölümü ve fanın kararlı çalışma bölümü ayrı ele alınır. Sonraki kayıtta fan anahtarlama zamanı ayrıca not edilmelidir.

Bu analiz, fanın elektriksel akımını mutlak doğrulamaz; UNIT ilk karşılaştırma verisidir. PZEM ile daha sonra aynı hız kademelerinde yeniden kıyas yapılacaktır.
