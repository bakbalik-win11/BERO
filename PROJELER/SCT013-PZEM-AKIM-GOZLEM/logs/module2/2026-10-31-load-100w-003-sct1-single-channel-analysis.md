# LOAD-100W-003 — ESP32D1 SCT-1 tek kanal log analizi

- Tarih: 2026-10-31
- Log aralığı: 15:59:53.051–16:01:39.884 (+03:00)
- Cihaz: esp32d1, ESP32 rev3.1, IP 192.168.0.31
- Firmware derleme zamanı: 2026-10-31 15:55:25 +0300
- Yük/kanal: 100 W akkor ampul, SCT-1 / GPIO32 (sarı); ortak bias GPIO35 (turuncu)
- Yapılandırma: GPIO32 ADC1_CH4, GPIO35 ADC1_CH7, 12 dB attenuation; ct_clamp sample_duration 200 ms, update_interval 2 s.
- Akım yayını: 54 örnek; medyan 0.469 A; min–max 0.426–1.164 A.
- 52/54 yayın 0.426–0.541 A aralığında. İki belirgin yüksek değer: 0.797 A (16:00:13.890) ve 1.164 A (16:01:33.849).
- Raw AC: 54 yayın; 0.01758–0.04805 V; ortalama 0.02030 V.
- Bias: 107 yayın; 1.623–1.678 V; ortalama 1.65672 V.
- Referans cihaz değeri bu logda yok; sapma ve ±%4 değerlendirmesi yapılamaz.
- Özgün kullanıcı logu SHA-256: `c92d51915de6b7ab69fdbc1f00ad4b7554455748958d18525ba2b3320a9d9723`

## Logdan seçilmiş gerçek satırlar

```text
[15:59:53.051][I][app:164]: ESPHome version 2026.10.1 compiled on 2026-10-31 15:55:25 +0300
[15:59:53.140][C][adc:131]:   Pin: GPIO32
[15:59:53.140][C][adc:131]:   Channel:       4
[15:59:53.153][C][adc:131]:   Pin: GPIO35
[15:59:53.237][C][ct_clamp:013]:   Sample Duration: 0.20s
[15:59:53.237][C][ct_clamp:340]:   Update Interval: 2.000s
[15:59:53.739][D][ct_clamp:040]: 'BERO Mod2 SCT1 Akim' - Raw AC Value: 0.021A after 3502 different samples (17510 SPS)
[15:59:53.851][S][sensor]: 'BERO Mod2 SCT1 Akim' >> 0.497 A
[16:00:13.890][S][sensor]: 'BERO Mod2 SCT1 Akim' >> 0.797 A
[16:01:33.849][S][sensor]: 'BERO Mod2 SCT1 Akim' >> 1.164 A
[16:01:39.883][S][sensor]: 'BERO Mod2 SCT1 Akim' >> 0.447 A
```

## Teknik yorum

Log, ESPHome 2026.10.1 cihazının ağa/API'ye bağlandığını, GPIO32 ve GPIO35 ADC kurulumlarının başarılı olduğunu ve tek kanallı ct_clamp akım yayınının çalıştığını gösterir. 54 yayının medyanı 0.469 A'dır. İki yüksek değer (0.797 A ve 1.164 A) dağılımı etkiler; bunlar açıklanmadan bütün kayıtların aritmetik ortalaması kararlı yük sonucu olarak kullanılmamalıdır. 52 yayın 0.426–0.541 A aralığındadır; bu aralık yalnız log içi betimlemedir, referansla doğrulanmış kararlı pencere değildir. Bias ortalaması yaklaşık 1.657 V'tur. Eşzamanlı PENS/U200B+ veya PZEM referansı olmadan katsayı değişikliği ya da ±%4 kabul kararı verilmez.

## Kod kaydı

Testte kullanıcı tarafından belirtilen tek kanal SCT-1 akım okuma firmware'i, aşağıdaki arşiv kopyasıyla sabitlenmiştir:
[`LOAD-100W-003` firmware snapshot](../../firmware/archive/LOAD-100W-003-esp32d1-sct1-single-channel.yaml)

Not: Bu dosya depodaki o anki `firmware/esp32d1.yaml` içeriğinin değişmez arşiv kopyasıdır. Logun derleme zamanı 15:55:25 +0300 olarak kayıtlıdır; log tek başına derlenen YAML'ın kriptografik kaynak eşleşmesini kanıtlamaz.
