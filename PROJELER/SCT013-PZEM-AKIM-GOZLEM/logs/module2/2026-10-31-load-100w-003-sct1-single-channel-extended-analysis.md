# LOAD-100W-003 — SCT-1 tek kanal uzun log analizi

- **Tarih:** 2026-10-31
- **Log aralığı:** 15:59:53.051–16:05:11.858 (+03:00), yaklaşık 5 dakika 19 saniye
- **Cihaz:** ESP32D1 / Modül 2, IP 192.168.0.31
- **Yük/kanal:** 100 W akkor ampul; SCT-1 sarı/GPIO32/ADC1_CH4; ortak bias turuncu/GPIO35/ADC1_CH7
- **Firmware:** ESPHome 2026.10.1; logda derleme 15:55:25 +03:00; ct_clamp 200 ms örnek penceresi, 2 s yayın; ADC voltaj güncellemesi 1 s; 12 dB attenuation.
- **Kod kaynağı:** [LOAD-100W-003 tek kanal firmware snapshot](../../firmware/archive/LOAD-100W-003-esp32d1-sct1-single-channel.yaml). Log konfigürasyonu snapshot ile uyumludur; log tek başına derlenen binary ile YAML'ın kriptografik eşleşmesini kanıtlamaz.
- **Tam ham log:** [2026-10-31-load-100w-003-sct1-single-channel-full.txt](2026-10-31-load-100w-003-sct1-single-channel-full.txt)
- **Özgün dosya:** esp32d1-logs (31).txt; 1.219 satır; 90.076 bayt.
- **SHA-256:** `30fc5d5ccccf629423924ea17fe1706bdb4f8dfab1185f64f523596661663ed4`

## Akım sonuçları

- 160 akım yayını; aralık **0,422–1,164 A**.
- Medyan **0,460 A**; aritmetik ortalama **0,4841 A**.
- 150/160 yayın 0,422–0,541 A aralığında; 10 yayın 0,55 A üzerindedir.
- 0,55 A üzerindeki 10 yüksek yayın:
  - 16:00:13.890 — 0,797 A
  - 16:01:33.849 — 1,164 A
  - 16:02:25.866 — 0,652 A
  - 16:02:31.857 — 0,742 A
  - 16:02:33.861 — 0,824 A
  - 16:02:37.851 — 0,638 A
  - 16:02:43.850 — 0,593 A
  - 16:02:47.858 — 1,146 A
  - 16:03:35.852 — 0,868 A
  - 16:05:01.979 — 0,600 A
- Bu yüksek değerlerin sebebi logdan tek başına belirlenemez; gerçek yük/bağlantı değişimi, ölçüm davranışı veya parazit olasılıkları ayrıştırılmalıdır. Bu nedenle yalnız ortalama değer kalibrasyon sonucu olarak alınmamalıdır.

## Analog izleme

- Raw AC: 160 yayın; **0,01743–0,04805 V**, ortalama **0,01999 V**.
- Bias: 321 yayın; **1,623–1,678 V**, ortalama **1,65540 V**.
- SCT-1 ADC voltajı: 320 yayın; **1,567–1,690 V**, ortalama **1,65253 V**.
- ct_clamp DEBUG satırlarında 200 ms pencerede yaklaşık 17.400–18.000 SPS aralığında örnek sayımları raporlanıyor.

## 0,427 A geçici beklenen değerle karşılaştırma

0,427 A, kullanıcının UNIT cihazında gördüğünü bildirdiği değerdir. Bu logda UNIT veya PZEM ölçüm satırı bulunmuyor; dolayısıyla 0,427 A **PZEM ile doğrulanmış referans değildir**.

- Uzun log medyanı 0,460 A: 0,427 A'ya göre yaklaşık **+%7,7**.
- 0,55 A üzerindeki 10 yayın dışarıda bırakıldığında 150 yayının ortalaması 0,46288 A; 0,427 A'ya göre yaklaşık **+%8,4**. Bu dışlama yalnız betimleyici istatistiktir; yüksek değerlerin nedenini kanıtlamaz.
- 0,427 A'nın ±%4 aralığı 0,40992–0,44408 A'dır. Bu aralıkta **17/160** yayın vardır.
- Bu nedenle mevcut uzun kayıt, 0,427 A beklentisiyle henüz ±%4 uyum göstermiyor. Ancak referansın UNIT ölçümü olduğu ve eşzamanlı PZEM kararlı değeri bulunmadığı açıkça korunmalıdır.

## Karar

1. K katsayısı değiştirilmedi.
2. 0,427 A, UNIT kullanıcı bildirimi kaynaklı geçici beklenen değer olarak tutuldu; PZEM teyidi bekleniyor.
3. Uzun log, önceki kısa 003 logundan daha kapsamlı kayıt olarak esas alınacak; kısa log tarihsel olarak silinmeyecek.
4. Sonraki testte aynı yük koşulunda UNIT ve PZEM değerleri, ESP32D1 loguyla aynı zaman aralığında kaydedilmeli; yüksek akım sıçramaları ayrıca gözlenmeli.
