# E11 — Üç SCT sıralı ölçüm / uzatılmış log analizi

- **Tarih:** 2026-11-01
- **Durum:** LOG ANALİZİ TAMAMLANDI; T010 kabulü açık
- **Deney:** E11 — SCT1 GPIO32 → SCT2 GPIO33 → SCT3 GPIO34 → ortak bias GPIO35
- **Firmware snapshot:** [esp32d1-sequential-sct.yaml](../../experiments/E11-sequential-three-sct/esp32d1-sequential-sct.yaml), ESPHome 2026.10.1
- **Ölçüm ayarı:** ct_clamp 200 ms; script adımı 250 ms; nominal 50 ms geçiş payı; çevrim tetikleme 2 s; K=24.22

## 1. Kaynak ve birleştirme

- Önceki kaynak: `esp32d1-logs (64).txt`, 2.795 satır, SHA-256 `97a36071b8319625df5e717b358c8ec69fea609be928ba71e6e3a5153c081484`.
- Yeni kaynak: `esp32d1-logs (66).txt`, 5.000 satır / 378.656 bayt, SHA-256 `b1bad3f1a8ef010d4ff5e717b358c8ec69fea609be928ba71e6e3a5153c081484`.
- Log 66'nın ilk 1.678 satırı, Log 64'ün son 1.678 satırıyla satır satır birebir aynıdır. Birleştirme sırasında bu örtüşme ikinci kez sayılmadı.
- Tekilleştirilmiş birleşik zaman çizgisi: 6.117 satır; 11:57:10.927–12:10:25.270.
- 398 SCT1 START ve 397 ALL CHANNELS COMPLETE kaydı vardır. Son çevrim dosya bittiği için SCT2 debug satırından sonra yarım kalır.
- İlk açılış çevrimi ve son yarım çevrim kararlı istatistiklere alınmadı. Karşılaştırmalı kararlı örnek sayısı: **396 çevrim / kanal**; bias için 396 okuma.

Tam yeni kaynak: [Log 66 — tam log (önceki dosyayla örtüşme içerir)](2026-11-01-e11-three-sct-sequential-log66-full-overlap.txt).

## 2. Kararlı kanal istatistikleri

İlk açılış çevrimi ve son yarım çevrim dışarıda bırakıldı. Değerler logdan hesaplandı; PZEM veya UNIT referansıyla karşılaştırma değildir.

| Kanal | Akım ort. (A) | Medyan (A) | SD (A) | CV | Min–maks (A) | Raw AC ort. (V) |
|---|---:|---:|---:|---:|---:|---:|
| SCT1 / GPIO32 | 0.423884 | 0.423 | 0.011217 | 2.646% | 0.398–0.497 | 0.017502 |
| SCT2 / GPIO33 | 0.424328 | 0.423 | 0.011925 | 2.810% | 0.402–0.499 | 0.017520 |
| SCT3 / GPIO34 | 0.425828 | 0.426 | 0.009431 | 2.215% | 0.405–0.478 | 0.017581 |

- Kanal ortalamaları birbirine yakındır: SCT2, SCT1'den +0.105%; SCT3, SCT1'den +0.459%; SCT3, SCT2'den +0.353%.
- Bu farklar sıralı ölçüm pencerelerinin aynı anda alınmadığı gerçeğiyle birlikte yorumlanmalıdır; sensör doğruluğu veya kalibrasyon kanıtı değildir.
- Dağılım bakımından SCT3 en düşük CV'ye (%2.215), SCT2 en yüksek CV'ye (%2.810) sahiptir.
- İlk 175 kararlı çevrimin ortalamaları önceki kısa analizle aynıdır. Sonraki 221 çevrimde ortalama SCT1 0.425846 A, SCT2 0.425516 A, SCT3 0.425014 A oldu. İlk 175 çevrime göre sırasıyla +1.054%, +0.635% ve −0.432% değişim vardır. Yük/besleme metadata'sı logda tanımlanmadığından değişimin nedeni atanamaz.

## 3. Kabul edilen farklı örnek sayısı

| Kanal | Ortalama farklı örnek / 200 ms | Ortalama SPS | Min–maks örnek |
|---|---:|---:|---:|
| SCT1 | 3401.9 | 17009 | 3299–3500 |
| SCT2 | 3235.5 | 16178 | 3131–3334 |
| SCT3 | 3414.9 | 17075 | 3330–3499 |

SCT2'nin kabul edilen farklı örnek sayısı SCT1'den yaklaşık %5.13, SCT3'ten %5.54 düşüktür. Bu fark önceki kısa logda da görülmüştür; uzun logda tekrarlandığı için takip edilmelidir. Tek başına ADC hatası veya ölçüm doğruluğu kanıtı değildir. ct_clamp debug satırındaki sayı, bileşenin kabul ettiği farklı örnek sayısıdır; ham ADC çağrılarının toplamı olarak yorumlanmamalıdır.

## 4. Ortak bias

- n = 396
- Ortalama: 1.660866 V
- Medyan: 1.661 V
- SD: 0.008008 V
- Min–maks: 1.636–1.687 V
- CV: 0.482%

Bu log aralığında ortak bias seviyesi dar bir dağılım göstermiştir.

## 5. Sıralama zamanlaması ve kanıt sınırı

200–300 ms, 250 ms nominal script adımı çevresinde kullanılan tanısal aralıktır; bağımsız bir kabul standardı değildir.

| Geçiş işareti | Ortalama (ms) | Medyan (ms) | Min–maks (ms) | 200–300 ms içinde |
|---|---:|---:|---:|---:|
| SCT1 START → SCT1 COMPLETE / SCT2 START | 250.6 | 251 | 16–376 | 376/396 |
| SCT1 COMPLETE / SCT2 START → SCT2 COMPLETE / SCT3 START | 253.2 | 253 | 145–454 | 374/396 |
| SCT2 COMPLETE / SCT3 START → SCT3 COMPLETE / BIAS READ | 254.1 | 253 | 164–392 | 374/396 |

- 396 çevrimin 354'ünde üç geçişin tamamı 200–300 ms aralığındadır.
- 42/396 çevrimde en az bir geçiş bu aralığın dışındadır.
- SCT1 START → ALL CHANNELS COMPLETE: ortalama 769.7 ms, medyan 767 ms, aralık 650–1094 ms.
- SCT1 START çevrim aralığı: ortalama 1999.8 ms, medyan 2000 ms, aralık 1748–2249 ms.

**Önemli uygulama ayrıntısı:** YAML'da START logu `component.update` çağrısından hemen önce yazılır. COMPLETE/sonraki START işaretleri, `on_raw_value` tamamlanma callback'inden değil, sabit 250 ms `delay` sonrasından üretilir. Bu nedenle bu işaretler gerçek ADC pencere başlangıç/bitişini tek başına kanıtlamaz; script ilerlemesini gösterir.

ct_clamp debug tamamlanma satırlarının ilgili START işaretine uzaklığı medyan olarak SCT1 203 ms (16–376), SCT2 204 ms (131–453), SCT3 205 ms (12–345) bulundu. Özellikle 16 ms ve 12 ms gibi değerler, 200 ms pencere ve yaklaşık 3.400 kabul edilmiş örnek bilgisiyle aynı çevrim içinde tutarlı görünmemektedir. Bu uyuşmazlık gerçek pencere sınırlarının logdan kesin çıkarılmasını engeller.

### Öne çıkan anomaliler

1. **12:01:07.174:** SCT1 START'tan SCT1 debug/COMPLETE işaretine 16 ms; sonraki geçişler 454 ms ve 392 ms. Debug satırlarında SCT1 3450 örnek / 17250 SPS, SCT2 3260 / 16300 SPS, SCT3 3480 / 17400 SPS görülür. 16 ms işaret aralığı, 200 ms örnekleme penceresiyle bağdaşmaz.
2. **12:06:06.849:** Üç script geçiş aralığı 309 / 393 / 392 ms; toplam çevrim 1094 ms sürer.
3. **Wi-Fi roaming:** 12:01:04.985'te (−52 dBm, attempt 1/3) ve 12:06:04.908'te (−59 dBm, attempt 2/3) roaming scan loglanmıştır. İki olayın çevresinde zamanlama sapmaları görülür. Bu olası bir scheduler/Wi-Fi etkisi olarak izlenebilir; iki gözlem nedensellik kanıtlamaz.

**Karar:** 50 ms geçiş payı azaltılmayacak. Gerçek pencere çakışmasızlığı bu logla kesin kabul edilmeyecek. Sonraki ölçümde çevrim kimliğiyle birlikte `component.update` çağrısı öncesi START ve `on_raw_value` içinde WINDOW_DONE işaretleri ayrı kaydedilmelidir.

## 6. Hata ve referans kontrolü

- Ölçüm bölümünde ERROR, NaN veya timeout satırı bulunmadı.
- Derleme/açılış bölümünde üç ESP32 optimizasyon uyarısı vardır; ölçüm hatası değildir.
- Logda PZEM, UNIT veya SSR olay kaydı yoktur.
- Fiziksel test yükü ve besleme koşulu log metadata'sında açıkça tanımlanmamıştır.
- Bu nedenle PZEM eşleştirmesi, kalibrasyon, ±4% kabulü veya K değişikliği sonucu çıkarılmaz.
- K=24.22 ve YAML değiştirilmedi. E10 (200 → 500 → 1000 → 200 ms) henüz uygulanmadı.

## 7. Sonuç ve sonraki adım

Üç kanal 396 kararlı çevrim boyunca veri üretmiş; kanal ortalamaları birbirine yakın kalmıştır. SCT2'nin yaklaşık %5 düşük kabul edilmiş örnek sayısı uzun logla tekrar doğrulanmıştır. SCT3 en düşük dağılıma sahiptir. Ancak script zaman işaretleri ve ct_clamp debug satırları bazı çevrimlerde uyuşmadığından pencere çakışmasızlığı kanıtlanmamıştır.

Önerilen sonraki adım: firmware/K/50 ms payı değiştirmeden, gerçek pencere başlangıç ve bitişini callback tabanlı işaretlerle, cycle_id ekleyerek yeniden loglamak. Roaming scan olayları ayrıca zaman damgasıyla izlenmelidir. T010 AKTİF kalır.

## Kaynak sınıflandırması

- **Measured/log:** Zaman damgaları, sensor yayınları, debug örnek sayıları, bias ve Wi-Fi roaming satırları.
- **Repository source:** E11 YAML'ın 200 ms sample_duration, 250 ms delay, START/COMPLETE log sırası ve K=24.22 ayarları.
- **User-provided:** Log dosyalarının paylaşılması.
- **Hypothesis:** Wi-Fi roaming'in scheduler gecikmelerine katkı yapmış olabileceği; ek deney olmadan doğrulanmış neden değildir.


## 2026-11-01 — E11 Log 66 / 100 W UNIT karşılaştırması (kullanıcı yük teyidi)

- **YÜK KİMLİĞİ:** İlk log incelemesinde fiziksel yük etiketi log içinde bulunmuyordu. Kullanıcı, sonraki mesajında bu uzun logun 100 W akkor ampul deneyi olduğunu teyit etti. Bu bilgi kullanıcı bildirimi olarak sınıflandırılır; log satırlarının içinde bağımsız yük etiketi değildir.
- **REFERANS:** 100 W akkor için tarihsel UNIT değeri 0,427 A. Bu değer logla eşzamanlı UNIT ölçümü değildir; mevcut test-load kaydındaki geçici çalışma referansıdır.
- **KARARLI VERİ:** Log 64/66 birleştirilmiş zaman çizgisinde 396 kararlı çevrim/kanal analiz edildi. SCT1 ortalama 0,423884 A; SCT2 0,424328 A; SCT3 0,425828 A.
- **UNIT KIYASI:** UNIT 0,427 A'ya göre SCT1 −%0,730; SCT2 −%0,626; SCT3 −%0,274. Üç kanal ortalaması da 0,40992–0,44408 A kabul bandındadır.
- **SONUÇ:** Kullanıcının yük teyidi esas alındığında yeni E11 sıralı üç-SCT kodu, bu 100 W oturumunda üç kanal ortalaması bakımından tarihsel UNIT referansına göre ±%4 hedefini sağlamıştır. Bu, aynı oturumda alınmış UNIT ölçümü değildir; bu nedenle sonuç “tarihsel UNIT referansına göre karşılaştırmalı başarı” olarak kaydedilir, eşzamanlı doğrulama veya genel kalibrasyon garantisi olarak sunulmaz.
- **DİĞER BULGULAR:** SCT2'nin kabul edilmiş örnek sayısı SCT1/SCT3'ten yaklaşık %5 düşük; 42/396 çevrimde en az bir script geçiş işareti 200–300 ms tanısal aralığın dışındadır. Gerçek ADC pencere sınırları callback ile doğrulanmadığından 50 ms geçiş payı azaltılmaz.
- **KOD/KATSAYI:** K=24.22 değişmedi. Bu sonuçtan katsayı düzeltmesi çıkarılmadı. PZEM bu kıyasın referansı değildir.
