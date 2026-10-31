# ADR-016 — Modül 2 üç SCT kanalında ct_clamp akım okuması

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ — ilk yazılım yaklaşımı; derleme ve saha kalibrasyonu bekliyor
- **İlgili görev:** T010
- **İlgili firmware:** [esp32d1.yaml](../../firmware/esp32d1.yaml)

## Karar

Modül 2'nin üç SCT girişinde ESPHome `ct_clamp` bileşeni kullanılacak. Her kanalın ADC kaynağı korunacak; akım sensörleri 200 ms örnekleme penceresiyle AC etkin değerini hesaplayacak. GPIO35 ortak bias izleme sensörü olarak kalacak.

## Kanal eşlemesi

| Kanal | Kablo | GPIO | ADC kaynak ID | Akım sensörü ID |
|---|---|---:|---|---|
| SCT-1 | Sarı | GPIO32 | sct_1_adc_voltage | sct_1_current |
| SCT-2 | Yeşil | GPIO33 | sct_2_adc_voltage | sct_2_current |
| SCT-3 | Mavi | GPIO34 | sct_3_adc_voltage | sct_3_current |
| Ortak bias | Turuncu | GPIO35 | common_bias_adc_voltage | — |

## İlk nominal dönüşüm

Kullanıcı envanterinde SCT-013-030, 30 A / 1 V olarak tanımlanmıştır. Üretici veri sayfasındaki nominal değer 30 A girişte 1 V çıkıştır. Bu nedenle ilk yazılım katsayısı 30 A/V seçildi:

- 0.0 V RMS → 0.0 A
- 1.0 V RMS → 30.0 A

Bu, üretici nominal oranından türetilmiş **HESAP** niteliğinde başlangıç dönüşümüdür; modülün saha kalibrasyonu veya doğrulanmış doğruluk iddiası değildir. ADC, bias ve gerçek SCT kanal farklılıkları nedeniyle her kanal daha sonra bilinen yük ve U200B+/PZEM karşılaştırmasıyla ayrı kalibre edilebilir.

## Örnekleme ve yayın

- Her kanal için ct_clamp örnekleme penceresi: 200 ms (50 Hz'de 10 periyot).
- Yayın aralıkları: SCT-1 5 s, SCT-2 5.5 s, SCT-3 6 s. Ayrı aralıklar başlangıçların sürekli aynı anda çakışmasını azaltmak içindir; gerçek çalışma loguyla gözlenecek.
- ADC gerilim entity'leri 1 s aralıkla korunur.
- GPIO35 bias gerilimi 1 s aralıkla korunur.

## Kabul sınırları

- YAML cihaz kimliği `esp32d1` korunur.
- Üç akım entity'si A biriminde Home Assistant'a açılmalıdır.
- Derleme başarılı olmalıdır.
- Yüksüz, 100 W yükte ve yük kapatıldıktan sonra her kanal için akım davranışı logla incelenmelidir.
- İlk katsayı U200B+ veya PZEM referansıyla karşılaştırılmalı; gerçek kanal kalibrasyonu yapılmadan ±%4 veya başka doğruluk iddiası verilmemelidir.
- Bu firmware güç, enerji, PF, harmonik, FFT veya THD hesaplamaz.

## Kaynaklar

- ESPHome CT Clamp bileşeni: https://beta.esphome.io/components/sensor/ct_clamp/
- ESPHome CT Clamp uygulaması: https://api-docs-beta.esphome.io/ct__clamp__sensor_8cpp_source
- SCT-013-030 veri sayfası: https://www.mouser.com/datasheet/2/744/101990028_SCT_013_030_Datasheet-2487857.pdf
