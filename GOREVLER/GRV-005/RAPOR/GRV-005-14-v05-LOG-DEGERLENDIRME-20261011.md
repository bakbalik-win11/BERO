# GRV-005-14 v05 — Gerçek Cihaz Logu Değerlendirmesi

Tarih: 2026-10-11
ESPHome: 2026.9.1
Firmware compile time: 2026-10-11 14:49:24 +0300
Cihaz: esp32d1, ESP32 rev3.1, 2 core
Ham log: GOREVLER/GRV-005/LOG/GRV-005-14-v05-GERCEK-CIHAZ-LOGU-20261011.txt

## Sonuç
- API bağlantısı ve handshake: PASS.
- Başlık: 16 + 25 = 41 alan.
- Dört kanal satırı: her biri 41 alan.
- CH0-1T, CH1-2T, CH2-3T, BIAS: 1000 örnek; zero_count=0.
- Önceki 92 ms interval uyarısı bu logda görünmüyor. Bu iyi işaret, fakat tek çalıştırma kesin garanti değildir.
- PZEM zaman/delta tutarlılığı: FAIL.
- PZEM snapshot tutarlılığı: FAIL.

## Pencere zamanı
Başlangıç 242 ms, bitiş 10435 ms, süre 10193 ms ve merkez 5338 ms. Süre ve merkez aritmetiği doğru.

## Bulgu: PZEM zamanı ve delta uyuşmuyor
| Kanal | pzem_update_millis | time_delta_ms | pzem zamanı − merkez |
|---|---:|---:|---:|
| CH0-1T | 9508 | 4170 | 4170 |
| CH1-2T | 10510 | 4170 | 5172 |
| CH2-3T | 10510 | 4170 | 5172 |
| BIAS | 10510 | 4170 | 5172 |

CH0 tutarlı; diğer satırlarda 10510 − 5338 = 5172 olması gerekirken delta 4170 kalmış.

En olası neden: v05 rapor başında delta'yı hesaplayıp sabitliyor; fakat satırlar yazılırken pzem_update_millis globalini her seferinde yeniden okuyor. Bu sırada PZEM güncellemesi değişebildiğinden zaman ve delta ayrışıyor.

PZEM akım/güç/PF değerleri de satırlar arasında değişiyor: CH0 0.029 A / 1.700 W / 0.2500; sonraki satırlar 0.028 A / 1.600 W / 0.2500. Aynı measurement_id altında tek bir PZEM snapshot'ı isteniyorsa bu yanlış.

## ADC istatistikleri
| Kanal | Ortalama | Std. sapma | Min | Max | Aralık | Ham RMS | BIAS merkezli RMS |
|---|---:|---:|---:|---:|---:|---:|---:|
| CH0-1T | 1862.606 | 11.986 | 1564 | 1900 | 336 | 1862.645 | 12.187 |
| CH1-2T | 1861.077 | 5.442 | 1839 | 1874 | 35 | 1861.085 | 6.617 |
| CH2-3T | 1855.803 | 8.046 | 1791 | 1926 | 135 | 1855.820 | 12.102 |
| BIAS | 1864.846 | 4.626 | 1850 | 1878 | 28 | — | — |

CH0 minimumu 1564, maksimumu 1900; bu geniş aralık ham örnekler olmadığı için tek başına hata kanıtı sayılmaz. BIAS merkezli RMS eşzamanlı örnek çiftlerinden hesaplanmıyor.

## Sonraki düzeltme
v06 adayında raporun başında PZEM zaman damgası, akım, güç ve PF tek seferlik snapshot olarak kopyalanmalı. Delta bu snapshot zamanından hesaplanmalı; dört satır da aynı değerleri kullanmalı. v05 çalışan sürüm olarak korunmalı.

## Nihai karar
CSV hizası PASS. 92 ms uyarısı bu logda gözlenmedi. PZEM snapshot/delta tutarlılığı FAIL; ayrı v06 adayı gerektiriyor.
