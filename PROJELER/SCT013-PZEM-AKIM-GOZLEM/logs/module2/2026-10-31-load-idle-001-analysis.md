# LOAD-IDLE-001 — Modül 2 yüksüz SCT-1 uzun log analizi

- **TEST ID:** LOAD-IDLE-001
- **OTURUM:** İlk kısa logun devamı; yeni test ID değildir.
- **KAYNAK:** `esp32d1-logs (37).txt`
- **BOYUT:** 110.590 bayt; 1.492 satır.
- **SHA-256:** `e4b229b45abce1f85e74f60260c0a7ed279e48c6b8f59d70ccbabaf23c8ee22f`
- **AKIM YAYIN ARALIĞI:** 16:47:55.066–16:54:33.029 (+03:00), yaklaşık 6 dk 38 sn.
- **DONANIM:** ESP32D1 / Modül 2 / SCT-1 GPIO32 ADC1_CH4; ortak bias GPIO35 ADC1_CH7.
- **FIRMWARE:** ESPHome 2026.10.1; ESP32 rev3.1. ADC 12 dB, samples 1, update 1 s. ct_clamp sample_duration 200 ms, update_interval 2 s. Wi-Fi RSSI −54 dB.
- **REFERANS:** Yüksüz senaryo için UNIT referansı aranmadı. Logda PZEM yok.
- **KATSAYI / SIFIR:** K değiştirilmedi; yazılımsal sıfır eşiği eklenmedi.

## Önceki kısa logla ilişki

Önceki `Yapıştırılan metin(20261031-135010).txt` kaydındaki 60 akım yayınının tamamı, bu uzun logun ilk 60 akım yayınıyla zaman ve değer bazında birebir eşleşmektedir. Bu dosya yeni test değil, aynı LOAD-IDLE-001 ölçümünün uzatılmış kaydıdır. Uzun kayıtta toplam 200 yayın vardır; ilk 60 yayın önceki kısa dosyayla mükerrer içeriktir, 140 yeni yayın eklenmiştir.

## Akım sonuçları — toplam 200 yayın

- Ortalama: **0,017130 A**
- Medyan: **0,000 A**
- Min–maks: **0,000–0,144 A**
- Örnek standart sapma: **0,032705 A**
- Tam sıfır: **146/200 (%73,0)**
- Sıfır dışı: **54/200 (%27,0)**

## Devam bölümü — 140 yeni yayın

- Ortalama: **0,019643 A**
- Medyan: **0,000 A**
- Min–maks: **0,000–0,144 A**
- Tam sıfır: **98/140 (%70,0)**
- Sıfır dışı: **42/140 (%30,0)**

Devam bölümündeki sıfır dışı değerler 0,010–0,144 A aralığındadır. En yüksek gözlenen akım 0,144 A'dır (16:51:27.046). Bunlar yüksüz koşulda görülen sıfır dışı çıktılardır; yalnız bu logla gerçek primer akımı, çevresel girişim veya ölçüm zinciri etkisi olarak kesin sınıflandırılamaz.

## Analog ölçümler — toplam log

| Entity | Yayın | Ortalama | Min–maks | Örnek SD |
|---|---:|---:|---:|---:|
| Raw AC | 200 | 0,00070765 V | 0,00000–0,00593 V | 0,001350 V |
| Common Bias GPIO35 | 399 | 1,664461 V | 1,646–1,685 V | 0,003783 V |
| SCT-1 ADC GPIO32 | 399 | 1,662461 V | 1,647–1,673 V | 0,004020 V |

ADC kanalları 1 saniyelik ayrı yayınlardır; satır sırası üzerinden birebir eşzamanlı çift gibi değerlendirilmemelidir.

## Örnekleme ve cihaz durumu

- ct_clamp DEBUG SPS: **17.465–18.465**, ortalama **17.990 SPS** (200 pencere). Bu, ESPHome logunun raporladığı değerdir; bağımsız ADC zaman ölçümü değildir.
- GPIO32 ve GPIO35 ADC başlatma/konfigürasyon/kalibrasyon durumları OK.
- Üç derleyici/optimizasyon uyarısı; sıfır `[E]` hata. Logda brownout veya reboot işareti görülmedi.

## İlk kısa logla karşılaştırma

İlk 60 yayında sıfır oranı %80 idi. Uzun logun tamamında sıfır oranı %73'e indi; yeni 140 yayınlık devam bölümünde sıfır oranı %70 oldu. Ortalama akım toplam kayıtta 0,011267 A'dan 0,017130 A'ya yükseldi. Ölçüm süresi uzadıkça sıfır dışı düşük okumaların daha fazla görüldüğü anlaşılıyor. Bu aşamada bir sıfır eşiği belirlemek için yeterli kanıt yoktur.

## Teknik yorum ve karar

1. Yüksüz durumda sistem sıfır okuma üretiyor; ancak uzun logda 200 yayının 54'ü sıfır dışıdır.
2. Sıfır dışı değerler 0,010–0,144 A aralığına kadar çıkmıştır. En yüksek değer 0,144 A'dır; gerçek yük akımı olarak yorumlanmamalıdır.
3. Bias ve SCT-1 ADC ortalamaları birbirine yakındır ve yaklaşık 1,66 V seviyesindedir.
4. Tek uzun kayıt, yüksüz dağılımı tanımlamaya yardımcı olur; kalıcı yazılım deadband'i veya K katsayısı değişikliğini haklı çıkarmaz.
5. **K=24.22 korunur; yazılımsal sıfır eşiği eklenmez.** Aynı fiziksel koşul ve firmware ile başka bir yüksüz oturum alınıp dağılımın tekrarlanabilirliği karşılaştırılmalıdır.

**SONUÇ:** LOAD-IDLE-001 uzun logu analiz edildi. Toplam 200 akım yayınının %73'ü sıfır, %27'si sıfır dışıdır. İlk 60 yayın önceki kısa logla aynıdır; 140 yeni yayın eklenmiştir. Tam ham log depoya kaydedilmiştir.
