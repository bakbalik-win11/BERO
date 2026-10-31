# FAN-3 — Modül 2 / SCT-1 uzun log analizi

## Test kimliği ve kaynak

- Test: FAN-3 (fan kademe 3), 2026-10-31.
- UNIT: **0,141 A** — kullanıcı bildirimi.
- Kaynak: `esp32d1-logs (43).txt`; 139.575 bayt / 1.877 satır.
- Kaynak SHA-256: `a4345c7af2b5dcc608b264e1dceed50dbe8ee5e40c5137d1eeff2583f9a53a9f`.
- Akım yayın aralığı: **17:35:27.127–17:43:55.115 (+03:00)**; 255 yayın; yaklaşık 8 dk 28 sn.
- ESPHome 2026.10.1; cihaz derleme zamanı 2026-10-31 15:55:25 +0300.

## Donanım ve firmware

- ESP32D1 / Modül 2.
- SCT-1 sarı sinyal GPIO32 / ADC1_CH4.
- Ortak bias turuncu GPIO35 / ADC1_CH7.
- SCT-2 GPIO33 ve SCT-3 GPIO34 kullanılmıyor.
- ADC attenuation 12 dB; ADC entity güncellemesi 1 s.
- `ct_clamp` sample_duration 200 ms; update_interval 2 s.
- K=24.22; yazılımsal sıfır eşiği yok.
- 255 ct_clamp penceresinde raporlanan SPS ortalaması **17.156,9**; min–maks **16.690–17.785 SPS**.
- Kapanış YAML snapshot ayrıca arşivlendi. Log yapılandırmasıyla uyumludur; derlenmiş binary'nin birebir eşleştiği iddia edilmez.

## SCT gözlem istatistikleri

| Alan | Sonuç |
|---|---:|
| Akım yayın sayısı | 255 |
| Akım ortalaması | 0,224612 A |
| Akım medyanı | 0,223 A |
| Akım min–maks | 0,189–0,311 A |
| Akım örnek standart sapması | 0,018657 A |
| Raw AC yayın sayısı | 255 |
| Raw AC ortalaması | 0,009273 V |
| Raw AC min–maks | 0,00782–0,01283 V |
| Bias yayın sayısı | 509 |
| Bias ortalaması | 1,663387 V |
| Bias min–maks | 1,644–1,675 V |
| SCT ADC yayın sayısı | 509 |
| SCT ADC ortalaması | 1,661008 V |
| SCT ADC min–maks | 1,644–1,680 V |

Akım yayınlarının 253/255'i 0,30 A altındadır. Yalnız iki yayın 0,30 A veya üzerindedir: 17:40:25.231'de 0,305 A ve 17:42:29.117'de 0,311 A. Bu iki tekil yayın kararlı yüksek akım bölgesi oluşturmaz.

## UNIT ve düşük akım sınıflandırması

- UNIT 0,141 A kullanıcı bildirimidir; PZEM değeri değildir.
- UNIT değeri 0,30 A sınırının altında olduğundan BERO kuralı gereği ±%4 kabul/ret değerlendirmesi yapılmaz.
- SCT ortalaması ile UNIT değeri arasındaki fark betimleyici gözlemdir; UNIT mutlak doğru kabul edilmez ve bu oturumdan kalibrasyon katsayısı türetilmez.
- Logda PZEM akım, aktif güç, gerilim veya PF verisi yoktur. PF etkisi bu logla sınanamaz.

## Açılma/kapanma geçişi

- Fanın açıldığı veya kapandığı ana ait açık olay işareti / kullanıcı zaman notu bulunmuyor.
- İlk akım yayını 17:35:27.127'de 0,241 A; son yayın 17:43:55.115'te 0,206 A. Kayıt boyunca akım 0,189–0,311 A aralığında.
- Bu nedenle fanın gerçek açılma/kapanma anları, geçiş süresi veya SCT-PZEM tepki farkı bu logdan hesaplanamaz.
- Ölçüm zincirinde ct_clamp penceresi 200 ms, yayın aralığı 2 s. Bu log ham sensörün fiziksel tepki süresini tek başına ölçmez; ESPHome ölçüm/yayın zincirinin gözlemidir.
- Gelecek geçiş deneyinde fan anahtarlama anı ayrı olay işaretiyle kaydedilmeli; PZEM akım/PF ve SCT verileri aynı zaman çizelgesinde tutulmalıdır.

## Cihaz durumu

- Üç derleyici/optimizasyon uyarısı mevcut.
- `[E]` seviyesinde hata, brownout veya reboot kaydı görülmedi.
- Log başlangıcında Wi-Fi bağlı; RSSI −54 dB.

## Sonuç ve kapanış sınıfı

**FAN-3, Modül 2 / SCT-1 düşük akım gözlem oturumu olarak kapatıldı.** Bu, ±%4 akım doğrulaması veya PF doğrulaması değildir.

Ham log ve analiz korunmuştur. K=24.22 değiştirilmemiş, yazılımsal sıfır eşiği eklenmemiştir. PZEM akım + PF ile eşleşmiş kararlı pencere ve olay işaretli açılma/kapanma geçiş deneyi sonraki araştırma işidir.

## Kanıtlar

- Ham log: [FAN-3 tam ham log](2026-10-31-fan3-module2-sct1-long-full.txt).
- Kapanış firmware snapshot: [FAN-3 ESP32D1 SCT-1 YAML](../../firmware/archive/FAN-3-2026-10-31-esp32d1-sct1.yaml).
- Kaynak firmware: [esp32d1.yaml](../../firmware/esp32d1.yaml).
- Fan test kayıtları: [fan/README.md](../../test-loads/fan/README.md).
