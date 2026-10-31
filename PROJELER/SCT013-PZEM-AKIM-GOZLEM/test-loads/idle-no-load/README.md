# LOAD-IDLE — Modül 2 yüksüz / boşta ölçüm kayıtları

Bu klasör, Modül 2'nin primer akım olmayan koşuldaki ölçüm davranışını ayrı bir test senaryosu olarak izler. “Boşta” olması testin yapılmadığı anlamına gelmez; yüksüz taban davranışını ölçmek bu kaydın amacıdır.

## Test düzeni
- ESP32D1 / Modül 2.
- SCT-1 sarı sinyal: GPIO32 / ADC1_CH4.
- Ortak bias turuncu: GPIO35 / ADC1_CH7.
- ESPHome ct_clamp: 200 ms örnekleme penceresi, 2 s yayın aralığı.
- ADC voltaj güncellemesi: 1 s, 12 dB attenuation.
- Yüksüz senaryo için UNIT referansı aranmaz.
- PZEM daha sonraki aşamada ayrıca kullanılabilir; bu logda PZEM verisi yoktur.
- Yazılımsal sıfır eşiği eklenmez; K katsayısı kanıt olmadan değiştirilmez.

## Test kayıtları

| Test ID | Tarih | Durum | Log / analiz |
|---|---|---|---|
| LOAD-IDLE-001 | 2026-10-31 | İlk kısa log + 6 dk 38 sn uzun log analiz edildi | [Uzun log teknik analizi](../../logs/module2/2026-10-31-load-idle-001-analysis.md) · [Tam ham uzun log](../../logs/module2/2026-10-31-load-idle-001-module2-sct1-no-load-full.txt) |

## LOAD-IDLE-001 — İlk log sonucu
- 60 akım yayını; ortalama 0,011267 A; medyan 0,000 A; aralık 0,000–0,104 A.
- 48/60 (%80,0) yayın 0,000 A; 12/60 (%20,0) yayın 0,014–0,104 A aralığında.
- Raw AC ortalaması 0,0004657 V.
- Bias GPIO35 ortalaması 1,663881 V; SCT-1 GPIO32 ADC ortalaması 1,662508 V.
- Akım yayını aralığı yaklaşık 1 dk 58 sn.
- PZEM/UNIT karşılaştırması yapılmadı; yüksüz senaryoda UNIT referansı aranmadı.
- K değişmedi; yazılımsal sıfır eşiği eklenmedi.
- Kaynak dosya SHA-256: 9ac3ece0770a85219e7ad6664f15f1ccc9db9b561d04f6195ef034d4e718e455.

## Sonraki adım
Aynı donanım ve firmware koşulunda daha uzun yüksüz log alınırsa aynı senaryonun devamı olarak kaydedilir; ayrı oturum olduğu belirtilir. 100 W/150 W yük sonuçlarıyla karıştırılmaz.


## LOAD-IDLE-001 — Uzun log güncellemesi

- Kaynak: `esp32d1-logs (37).txt`; 110.590 bayt / 1.492 satır; SHA-256 `e4b229b45abce1f85e74f60260c0a7ed279e48c6b8f59d70ccbabaf23c8ee22f`.
- Akım yayını aralığı 16:47:55.066–16:54:33.029 (+03:00); 200 yayın.
- İlk kısa logdaki 60 yayın uzun logun ilk 60 yayınıyla birebir aynı; uzun log 140 yeni yayın ekliyor.
- Toplam: ortalama 0,017130 A; medyan 0,000 A; min–maks 0,000–0,144 A; 146/200 (%73) sıfır.
- Yeni 140 yayın: ortalama 0,019643 A; medyan 0,000 A; 98/140 (%70) sıfır.
- Raw AC ortalama 0,00070765 V; bias GPIO35 ortalama 1,664461 V; SCT-1 GPIO32 ADC ortalama 1,662461 V.
- ct_clamp SPS ortalaması 17.990; aralık 17.465–18.465 SPS.
- PZEM/UNIT yok; yüksüz testte UNIT referansı aranmadı. K değiştirilmedi; yazılımsal sıfır eşiği eklenmedi.
- [Teknik analiz](../../logs/module2/2026-10-31-load-idle-001-analysis.md) · [Tam ham log](../../logs/module2/2026-10-31-load-idle-001-module2-sct1-no-load-full.txt).
