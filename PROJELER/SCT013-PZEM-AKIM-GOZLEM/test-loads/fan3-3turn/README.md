# FAN-3-3T-001 — FAN-3 / SCT-1 üç primer tur deneyi

**Durum:** KAPATILDI — düşük akım üç-tur gözlem oturumu; ±%4/PZEM doğrulaması değildir.

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


## 2026-10-31 — FAN-3-3T-001 üç primer tur gözlemi kapatıldı

- **DURUM:** Düşük akım üç-tur gözlem oturumu kapatıldı. ±%4 doğrulaması, PZEM doğrulaması veya kalibrasyon değildir.
- **KAYNAK:** `esp32d1-logs (47).txt`; 129.554 bayt / 1.744 satır; kaynak SHA-256 `fb48997412ced2a9f769b3084bec9f63dab8ef7174efea23062ce4e63dbc735c`.
- **MÜKERRERLİK:** `esp32d1-logs (46).txt` (SHA-256 `27567257b0cdf05766899da3f5d8db59410069e236a92037e5c72321df0f659e`) bu logun birebir başlangıç önekidir; ayrı veri sayılmadı.
- **ZAMAN/ÖRNEK:** 18:30:59.057–18:38:49.014 (+03:00); 236 akım ve 236 Raw AC yayını.
- **AKIM:** Tüm yayınlarda ortalama 0,416089 A, medyan 0,413 A, min–maks 0,392–0,932 A. 18:31:57.032'deki tekil 0,932 A sıçrama (Raw AC 0,03849 V) korunarak işaretlendi. Sıçrama hariç 235 yayında ortalama 0,413894 A; medyan 0,413 A; min–maks 0,392–0,454 A.
- **NORMALİZASYON:** Sıçrama hariç firmware göstergesi/3 ortalaması 0,137965 A; medyanı 0,137667 A; min–maks 0,130667–0,151333 A. UNIT 0,142 A kullanıcı bildirimine göre ortalama fark −%2,84; yalnız betimleyici aritmetik, kabul/ret değildir.
- **ANALOG:** Sıçrama hariç Raw AC ortalama 0,017089 V; bias GPIO35 ortalama 1,662684 V; SCT ADC GPIO32 ortalama 1,657652 V. SPS ortalama 17.321,6 (16.890–18.430).
- **TEK TUR KIYASI:** Önceki FAN-3 tek tur ortalaması 0,224612 A ve Raw AC 0,009273 V. Bu oturumda sıçrama hariç akım ve Raw AC artış oranları yaklaşık 1,843x; ideal 3x doğrusal artış görülmedi. /3 sonucu kalibrasyon veya doğrusal davranış kanıtı değildir.
- **REFERANS/PF:** Logda PZEM akım/PF yoktur. UNIT 0,142 A kullanıcı bildirimidir. 0,30 A altı düşük akım sınıfında ±%4 kabul/ret uygulanmaz.
- **KOD:** K=24.22 ve yazılımsal sıfır eşiği olmaması korundu; firmware değiştirilmedi. [Kapanış YAML snapshot](../../firmware/archive/FAN-3-3T-001-2026-10-31-esp32d1-sct1.yaml). Binary eşleşmesi iddia edilmez.
- **RAPOR:** [Teknik analiz](../../logs/module2/2026-10-31-fan3-3t-001-module2-sct1-analysis.md). Ham logun GitHub'a tam metin arşivi bu işlemde tamamlanamadı; kaynak dosya bu sohbet yüklemesinde mevcut ve SHA-256 kaydı korunmuştur.
- **AÇIK ARAŞTIRMA:** Ayrı düşük akım ESP/model veri sınıfı, daha uzun/tekrarlı loglar, PZEM akım+PF eşleşmesi ve farklı tur sayılarının kontrollü karşılaştırması.


## 2026-10-31 — FAN-3-3T-001 üç primer tur gözlemi kapatıldı

- **DURUM:** Düşük akım üç-tur gözlem oturumu kapatıldı; ±%4 doğrulaması, PZEM doğrulaması veya kalibrasyon değildir.
- **KAYNAK:** `esp32d1-logs (47).txt`; 129.554 bayt / 1.744 satır; SHA-256 `fb48997412ced2a9f769b3084bec9f63dab8ef7174efea23062ce4e63dbc735c`.
- **MÜKERRERLİK:** Dosya 46 (SHA-256 `27567257b0cdf05766899da3f5d8db59410069e236a92037e5c72321df0f659e`) bu uzun logun birebir başlangıç önekidir; ayrı veri sayılmadı.
- **ZAMAN/ÖRNEK:** 18:30:59.057–18:38:49.014 (+03:00); 236 akım ve 236 Raw AC yayını.
- **AKIM:** Tüm yayın ortalaması 0,416089 A; medyan 0,413 A; min–maks 0,392–0,932 A. Tekil 0,932 A sıçrama (18:31:57.032; Raw AC 0,03849 V) korundu ve işaretlendi. Sıçrama hariç 235 yayında ortalama 0,413894 A; medyan 0,413 A; min–maks 0,392–0,454 A.
- **NORMALİZASYON:** Sıçrama hariç gösterge/3 ortalaması 0,137965 A; medyan 0,137667 A. UNIT 0,142 A kullanıcı bildirimine göre ortalama fark −%2,84; betimleyici hesap, kabul/ret değildir.
- **ANALOG:** Sıçrama hariç Raw AC ortalama 0,017089 V; bias GPIO35 ortalama 1,662684 V; SCT ADC GPIO32 ortalama 1,657652 V; SPS ortalama 17.321,6.
- **TEK TUR KIYASI:** Önceki FAN-3 tek tur akım 0,224612 A, Raw AC 0,009273 V. Yeni/önceki oran yaklaşık 1,843x; ideal 3x doğrusal artış görülmedi.
- **REFERANS:** Logda PZEM akım/PF yok. 0,30 A altı düşük akım alanında ±%4 kabul/ret yok.
- **KOD:** K=24.22 korundu; sıfır eşiği eklenmedi; firmware değiştirilmedi. [Kapanış YAML snapshot](../../firmware/archive/FAN-3-3T-001-2026-10-31-esp32d1-sct1.yaml). Binary eşleşmesi iddia edilmez.
- **RAPOR:** [Teknik analiz](../../logs/module2/2026-10-31-fan3-3t-001-module2-sct1-analysis.md); [tam ham log](../../logs/module2/2026-10-31-fan3-3t-001-module2-sct1-full.txt).
- **AÇIK ARAŞTIRMA:** Ayrı düşük akım ESP/model veri sınıfı, daha uzun/tekrarlı loglar ve PZEM akım+PF ile eşleşmiş kararlı pencereler.
