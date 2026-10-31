# FAN-1 — Modül 2 / SCT-1 uzun log istatistikleri ve test kapanış notu

## Kaynak ve düzenek
- Kaynak: `esp32d1-logs (40).txt`; 140.312 bayt / 1.887 satır; SHA-256 `8687da052b254f16b88f6eb6d27d41c94ae8166b027f089f0b6186069c58bedf`.
- Zaman: 17:13:51.283–17:22:23.079 (+03:00).
- Donanım: ESP32D1 / Modül 2; SCT-1 sarı GPIO32 / ADC1_CH4; ortak bias turuncu GPIO35 / ADC1_CH7.
- Firmware: ESPHome 2026.10.1; ADC 12 dB, 1 s; ct_clamp 200 ms, yayın 2 s.
- Kod snapshot: [FAN-1 kapanış firmware'i](../../firmware/archive/FAN-1-2026-10-31-esp32d1-sct1.yaml). Kaynak yapılandırma: [aktif esp32d1.yaml](../../firmware/esp32d1.yaml).
- Tam ham log: [FAN-1 uzun ham log](2026-10-31-fan1-module2-sct1-long-full.txt).

## İstatistik
Kullanıcının FAN-1 için en son bildirdiği UNIT değeri 0,093 A'dır. Önceki 0,097 A ve 0,096 A bildirimleri tarihsel not olarak korunur.
- FAN-1 kabul edilen bölüm: 17:14:11.079 sonrası; 247 akım yayını. Bu sınır log içindeki kullanıcı tarafından teyit edilmiş bir olay işareti değil, oturum bağlamına göre seçilmiş yaklaşık kesittir.
- Ortalama: **0,146757 A**
- Medyan: **0,147 A**
- Min–maks: **0,064–0,259 A**
- Standart sapma: **0,026064 A**
- UNIT 0,093 A için aritmetik ±%4 bandı: **0,08928–0,09672 A**
- Bu banda düşen yayın: **4/247 (%1,6)**; 240 yayın bandın üzerinde, 3 yayın altında.
- Medyanın UNIT bildirimine göre farkı yaklaşık **+%58,1**; ortalamanın farkı yaklaşık **+%57,8**.

## Teknik yorum ve karar
Bu istatistikler Modül 2'nin fan yükündeki ısınma/deneme gözlemidir; tek başına kalibre akım doğrulaması veya başarılı/başarısız ölçüm kabulü değildir. UNIT PF göstermediği için PF etkisi mevcut verilerle incelenememiştir. Farkın nedeni PF olabilir, ancak bu yalnızca hipotezdir; PZEM'in aynı FAN-1 çalışma penceresinde akım ve PF verisi olmadan doğrulanamaz.

**Karar:** FAN-1'in Modül 2 ısınma/deneme kaydı kapatıldı; ±%4 akım doğrulama testi olarak kabul edilmedi. FAN-1 için nihai teknik değerlendirme PZEM verisiyle daha sonra yeniden yapılacaktır. FAN-2'ye geçilebilir. FAN-2 ve sonraki fan kademelerinde PZEM akım ve PF kayıtları gerekli test girdisidir.

## Log tanılama notları
- Logda Wi-Fi bağlantısı ve ADC başlatma/konfigürasyon/kalibrasyon başarılı görünüyor.
- Üç derleyici optimizasyon uyarısı var; görünen logda hata, brownout veya reboot belirtisi yok.
- Fanın kesin açılma ve son kapatma anı olay işaretiyle kaydedilmedi; kararlı bölüm sınırı yaklaşık kabul edilmelidir.
- K=24.22 değiştirilmedi; yazılımsal sıfır eşiği eklenmedi.
