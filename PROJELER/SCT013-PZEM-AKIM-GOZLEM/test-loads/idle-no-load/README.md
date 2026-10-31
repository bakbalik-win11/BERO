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
| LOAD-IDLE-001 | 2026-10-31 | İlk log analiz edildi | [İlk log teknik analizi](../../logs/module2/2026-10-31-load-idle-001-analysis.md) |

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
