# FAN-3-3T-001 — FAN-3 / SCT-1 üç primer tur deneyi

**Durum:** AÇIK — fiziksel ölçüm ve log bekleniyor.

## 1. Amaç

FAN-3 yükünde mevcut SCT013-030 (30A/1V) sensörün düşük akım sinyalini, aynı tek yalıtılmış iletken CT çekirdeğinden **3 tur geçirilerek** gözlemlemek. Amaç Raw AC geriliminin ve ct_clamp göstergesinin tek tur koşuluna göre nasıl değiştiğini incelemektir.

Bu deney, FAN-3'ün önceki tek tur kaydının devamı niteliğinde ayrı bir oturumdur. Önceki log değiştirilmez.

## 2. Sabit tutulacak düzenek

- Kart/modül: ESP32D1 / Modül 2.
- SCT kanalı: SCT-1 sarı sinyal, GPIO32 / ADC1_CH4.
- Ortak bias: turuncu, GPIO35 / ADC1_CH7.
- SCT: mevcut SCT013-030, nominal 30A/1V.
- ESPHome: mevcut cihaz sürümü 2026.10.1.
- ADC: 12 dB attenuation, ADC entity 1 s.
- ct_clamp: 200 ms pencere, 2 s yayın.
- Firmware: `firmware/esp32d1.yaml`; açılış anında blob SHA `e1b110aca2ffa05fa792fd8e4b6248ed986e738c`.
- **Kod değişikliği yok.** K=24.22 korunur; yazılımsal sıfır eşiği eklenmez.
- UNIT FAN-3 değeri: en güncel kullanıcı bildirimi 0,142 A. Depodaki önceki kayıtta 0,141 A bulunur; tarihsel değer silinmez. Bu oturumda kullanılacak UNIT değeri 0,142 A olarak işaretlenmiştir (kullanıcı bildirimi).

## 3. Sarım ve güvenlik

- Enerji tamamen kesildikten sonra CT çekirdeğinden yalnızca fan beslemesinin **aynı tek yalıtılmış iletkeni** üç kez geçirilir.
- Faz ve nötr birlikte CT'den geçirilmez.
- İletken yalıtımı zedelenmez; CT klipsi ve kablo mekanik olarak zorlanmaz.
- Sarım sayısı ve yönü test notunda/fotoğrafta doğrulanır.
- Sarım düzeni değiştirildikten sonra kapalı ve güvenli kurulumla enerji verilir.

## 4. Ölçüm ve hesap yöntemi

Firmware'in yayınladığı akım değeri üç tur nedeniyle yaklaşık üç kat ölçeklenmiş olabilir. Gerçek hat akımını tahmin etmek için analizde ayrıca:

`Üç tur normalizasyonu = firmware akım göstergesi / 3`

hesaplanacaktır.

Bu bölme yalnızca deneysel normalizasyondur; firmware K katsayısını değiştirmez ve kalibrasyon sonucu değildir. Ham firmware akım göstergesi hiçbir zaman normalize edilmiş değerle değiştirilmeden ayrı saklanır.

Raw AC (V) ayrıca incelenir. İdeal doğrusal varsayımda tek turdaki sinyalin yaklaşık üç katı beklenir; gerçek sonuç ölçümle belirlenecektir.

## 5. Önceki tek tur karşılaştırma kaydı

FAN-3 tek tur logu:
- UNIT: 0,142 A (en güncel kullanıcı bildirimi; eski arşivde 0,141 A).
- SCT ortalama: 0,224612 A; medyan: 0,223 A.
- Raw AC ortalama: 0,009273 V.
- 255 akım yayını; 17:35:27.127–17:43:55.115 (+03:00).
- [Önceki tam ham log](../../logs/module2/2026-10-31-fan3-module2-sct1-long-full.txt)
- [Önceki analiz](../../logs/module2/2026-10-31-fan3-module2-sct1-long-analysis.md)
- [Önceki firmware snapshot](../../firmware/archive/FAN-3-2026-10-31-esp32d1-sct1.yaml)

Önceki tek turdaki 0,224612 A ortalama doğrudan gerçek fan akımı kabul edilmez; 0,30 A altı düşük akım alanında ±%4 kabul/ret uygulanmaz.

## 6. Kaydedilecek veriler

- Ham ESPHome logunun tamamı ve kaynak dosyanın SHA-256 değeri.
- Üç tur sarımın fiziksel doğrulaması.
- İlk/son yayın zamanları ve fanın çalışma durumu.
- Firmware akım göstergesi: ortalama, medyan, min/maks, standart sapma ve yayın sayısı.
- Üçe bölünmüş deneysel normalizasyon: aynı istatistikler.
- Raw AC (V), bias ADC (V), SCT ADC (V), raporlanan SPS.
- UNIT/PZEM verileri varsa kaynakları ayrı belirtilerek kaydedilir.
- Kod/YAML değişmediği doğrulanır; kapanışta kullanılan YAML snapshot ayrı arşivlenir.

## 7. Değerlendirme ve kapanış

- 0,30 A altındaki gerçek akım alanı için ±%4 kabul/ret kararı verilmez.
- Öncelik, Raw AC sinyalinin büyümesi ve üç tur normalizasyonunun önceki tek tur gözlemiyle tutarlılığıdır.
- Test, ham log ve analiz raporu GitHub'a kaydedilip doğrulanmadan kapatılmaz.
- Test kapanışında kullanılan son YAML snapshot'ı arşivlenir; log ve analiz bu snapshot'a bağlanır.
- Bu testin açılması, ölçümün yapıldığı veya başarılı olduğu anlamına gelmez.
