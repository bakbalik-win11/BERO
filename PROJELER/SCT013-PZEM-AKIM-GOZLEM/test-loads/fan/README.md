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


## 2026-10-31 — FAN-1 düşük akım sınıflandırması düzeltmesi

- **KURAL DÜZELTMESİ:** 0,30 A altındaki çalışma bölgesinde ±%4 kabul/ret kriteri uygulanmaz. Bu sınır, BERO'nun mevcut deney değerlendirme kuralıdır; sensör üreticisinin doğruluk spesifikasyonu değildir.
- FAN-1 UNIT son bildirimi 0,093 A olduğundan düşük akım araştırma bölgesindedir. Önceki kayıtlardaki ±%4 bandı (0,08928–0,09672 A) ve 4/247 sayımı yalnız tarihsel aritmetik bilgi olarak korunur; FAN-1 için kabul/ret veya başarısızlık ölçütü değildir.
- 247 yayın ortalaması 0,146757 A, medyanı 0,147 A ve aralığı 0,064–0,259 A olarak korunur. Bu SCT gözlemleri UNIT ile ±%4 uyumu şeklinde yorumlanmaz.
- FAN-1, Modül 2 ısınma/deneme gözlemi olarak kapalıdır. Düşük akım deney programı kapsamında ileride PZEM akım + PF ile, tek tur/2 tur/4 tur düzenekleri kontrollü karşılaştırılabilir.
- FAN-1'in mevcut logu sonradan değiştirilmez; yeni sarım koşulları ayrı deney oturumları ve ayrı loglarla kaydedilir.


## 2026-10-31 — FAN-2 uzun logu ve test kapanışı

- **DURUM:** FAN-2, Modül 2 düşük akım gözlem oturumu olarak kapatıldı; ±%4 akım doğrulama testi değildir.
- **UNIT:** Kullanıcı bildirimi 0,106 A. 0,30 A altı BERO düşük akım bölgesinde ±%4 kabul/ret uygulanmaz.
- **UZUN LOG:** `esp32d1-logs (42).txt`; kaynak boyutu 90.706 bayt; kaynak SHA-256 `e550d447b75b50e2b99581a70de23b8916caba576a8665240f44574e586a3dca`; 17:26:19.113–17:31:41.120 (+03:00); 162 akım yayını.
- **AKIM:** Ortalama 0,168969 A; medyan 0,1685 A; min–maks 0,108–0,257 A; örnek SD 0,024640 A. 162/162 yayın 0,30 A altındadır.
- **ANALOG:** Raw AC ortalama 0,00697685 V; bias GPIO35 ortalama 1,663426 V; SCT-1 ADC GPIO32 ortalama 1,660537 V.
- **KOD:** [FAN-2 kapanış YAML snapshot](../../firmware/archive/FAN-2-2026-10-31-esp32d1-sct1.yaml). ESPHome 2026.10.1; GPIO32 SCT-1, GPIO35 bias; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s; K=24.22; yazılımsal sıfır eşiği yok. Binary eşleşmesi iddia edilmez.
- **PF/REFERANS:** Logda PZEM akım ve PF yok; UNIT PF göstermiyor. PF etkisi hipotez olarak kalır.
- **KAPANIŞ:** Yalnız düşük akım gözlemi kapatıldı. PZEM akım + PF ile eşleşmiş kararlı pencere doğrulaması ve ayrı düşük akım 1T/2T/4T deneyleri açık iş olarak kalır.
- **DOSYALAR:** [Tam ham log](../../logs/module2/2026-10-31-fan2-module2-sct1-long-full.txt); [teknik analiz](../../logs/module2/2026-10-31-fan2-module2-sct1-long-analysis.md).


## 2026-10-31 — FAN-3 uzun SCT-1 logu ve gözlem kapanışı

- **KAPANIŞ SINIFI:** FAN-3, Modül 2 düşük akım gözlem oturumu olarak kapatıldı; ±%4 akım doğrulaması veya PF doğrulaması değildir.
- **UNIT:** Kullanıcı bildirimi **0,141 A**; 0,30 A altı BERO düşük akım bölgesinde ±%4 kabul/ret uygulanmaz.
- **UZUN HAM LOG:** `esp32d1-logs (43).txt`; 139.575 bayt / 1.877 satır; kaynak SHA-256 `a4345c7af2b5dcc608b264e1dceed50dbe8ee5e40c5137d1eeff2583f9a53a9f`.
- **ZAMAN/ÖRNEK:** 17:35:27.127–17:43:55.115 (+03:00); 255 SCT akım yayını.
- **AKIM:** Ortalama **0,224612 A**; medyan **0,223 A**; min–maks **0,189–0,311 A**; örnek SD **0,018657 A**. 253/255 yayın 0,30 A altındadır; yalnız iki tekil yayın 0,30 A'yı aşmıştır.
- **ANALOG:** Raw AC ortalama **0,009273 V**; bias GPIO35 ortalama **1,663387 V**; SCT-1 ADC GPIO32 ortalama **1,661008 V**.
- **KOD:** [FAN-3 kapanış YAML snapshot](../../firmware/archive/FAN-3-2026-10-31-esp32d1-sct1.yaml). ESPHome 2026.10.1; GPIO32 SCT-1, GPIO35 bias; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s; K=24.22; yazılımsal sıfır eşiği yok. Binary eşleşmesi iddia edilmez.
- **PF/REFERANS:** Logda PZEM akım ve PF yok; UNIT PF göstermiyor. PF etkisi bu testte doğrulanamadı.
- **GEÇİŞLER:** Açılma/kapanma olay işareti yok. Gerçek geçiş zamanı ve SCT-PZEM tepki farkı bu logdan çıkarılamaz.
- **RAPOR:** [FAN-3 teknik analiz](../../logs/module2/2026-10-31-fan3-module2-sct1-long-analysis.md); [tam ham log](../../logs/module2/2026-10-31-fan3-module2-sct1-long-full.txt).
- **SONRAKİ:** PZEM akım + PF ile eşleşmiş kararlı pencere; ayrıca fan açma/kapatma anı olay işaretli geçiş deneyi.


## 2026-10-31 — FAN-3-3T-001 üç primer tur deneyi açıldı

- **DURUM:** AÇIK; fiziksel ölçüm/log bekleniyor. Bu kayıt, önceki FAN-3 tek tur oturumundan ayrı bir deneydir.
- **AMAÇ:** Mevcut SCT013-030 (30A/1V) ile FAN-3 akımını, aynı tek yalıtılmış iletken CT çekirdeğinden üç kez geçirilerek gözlemlemek.
- **DÜZENEK:** ESP32D1 Modül 2 / SCT-1 sarı GPIO32 / ortak bias GPIO35. Firmware `firmware/esp32d1.yaml`; açılış anındaki blob SHA `e1b110aca2ffa05fa792fd8e4b6248ed986e738c`.
- **KOD:** Kod değişmeyecek; K=24.22 ve yazılımsal sıfır eşiği olmaması korunacak. Firmware akım göstergesi ayrıca saklanacak; deneysel normalize değer gösterge/3 olarak hesaplanacak. Bu bölme firmware'e uygulanmayacak.
- **UNIT:** En güncel kullanıcı bildirimi 0,142 A; önceki arşivdeki 0,141 A tarihsel olarak korunur.
- **ÖNCEKİ TEK TUR:** Raw AC ortalaması 0,009273 V; SCT akım ortalaması 0,224612 A. [Önceki log](../../logs/module2/2026-10-31-fan3-module2-sct1-long-full.txt).
- **KURAL:** 0,30 A altındaki düşük akım bölgesinde ±%4 kabul/ret yok. Amaç sinyal büyümesi ve tekrarlanabilir gözlemdir.
- **GÜVENLİK:** Enerji kesikken yalnız aynı tek yalıtılmış iletken üç tur geçirilir; faz ve nötr birlikte geçirilmez.
- **TEST PLANI:** [FAN-3-3T-001 ayrıntılı kayıt](fan3-3turn/README.md).


## 2026-10-31 — FAN-1-RETEST-001 yeniden gözlem oturumu açıldı

- **DURUM:** AÇIK; yeni fiziksel ölçüm ve log bekleniyor. Önceki FAN-1 oturumunun yerine geçmez.
- **AMAÇ:** FAN-1'i Modül 2 / ESP32D1 / SCT-1 üzerinde yeniden gözlemlemek; düşük akım eğitim/veri sınıfına ayrı oturum verisi toplamak.
- **DÜZENEK:** SCT-1 sarı GPIO32 / ADC1_CH4; ortak bias turuncu GPIO35 / ADC1_CH7; mevcut SCT013-030; `firmware/esp32d1.yaml`; K=24.22; yazılımsal sıfır eşiği yok.
- **REFERANS:** Son UNIT bildirimi 0,093 A; eski 0,097 A ve 0,096 A bildirimleri tarihsel kalır. 0,30 A altı için ±%4 kabul/ret yok.
- **PROTOKOL:** Fan kapalı başlangıç tabanı → FAN-1 açılış olayı → kararlı pencere → FAN-1 kapanış olayı → fan kapalı son taban. Geçiş ve kararlı veriler ayrı tutulur; varsa PZEM akım/PF ve UNIT aynı pencereye bağlanır.
- **KAPANIŞ:** Ham log/SHA-256, analiz ve kapanış YAML snapshot GitHub'a kaydedilip yeniden okunarak doğrulanmadan kapatılmaz.
- **AYRINTI:** [FAN-1-RETEST-001 test planı](fan1-retest/README.md).
