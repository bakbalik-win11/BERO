# LOAD-100W-004 — ESP32D1 masaüstü güç kaynağı sonrası SCT-1 analizi

- **Tarih:** 2026-10-31
- **Log aralığı:** 16:06:43.782–16:08:09.198 (+03:00); akım yayınları 16:06:45.189–16:08:09.198, yaklaşık 84 saniye.
- **Kaynak değişikliği:** Kullanıcı bildirimi: ESP32D1'in beslemesi PC USB bağlantısından masaüstü harici güç kaynağına taşındı. Gerilim/akım ölçümü veya osiloskop kanıtı bu logda yok; kaynak değişikliği kullanıcı beyanıdır.
- **Düzenek:** ESP32D1 / Modül 2 / SCT-1 sarı GPIO32 ADC1_CH4; ortak bias turuncu GPIO35 ADC1_CH7.
- **Firmware:** ESPHome 2026.10.1; cihazın bildirdiği derleme zamanı 2026-10-31 15:55:25 +0300. ct_clamp sample_duration 200 ms; update_interval 2 s. GPIO32 ve GPIO35 ADC update_interval 1 s; 12 dB attenuation. Önceki LOAD-100W-003 loguyla aynı derleme zamanı/konfigürasyon bilgisi görülüyor.
- **Ham log:** [Tam 397 satır](2026-10-31-load-100w-004-sct1-desktop-power.txt).
- **Özgün dosya:** esp32d1-logs (32).txt; 28.161 bayt.
- **SHA-256:** `0cba41fa5f66894f17ba2cda45773cae6a77c82eab1aa4e4c8bda81e019d4ac3`

## Akım sonuçları

- 43 akım yayını.
- Ortalama: **0,42274 A**.
- Medyan: **0,423 A**.
- Standart sapma (örnek): **0,00852 A**.
- Minimum–maksimum: **0,407–0,440 A**.
- 0,427 A geçici beklenen değerin ±%4 bandı 0,40992–0,44408 A'dır; **39/43 (%90,7)** yayın bu aralıktadır.
- Ortalama 0,427 A'ya göre **−%1,0**; medyan yaklaşık **−%0,94**.

## Analog izleme

- Raw AC: 43 yayın; 0,01679–0,01815 V; ortalama **0,01745 V**.
- Bias: 86 yayın; 1,656–1,675 V; ortalama **1,66342 V**.
- SCT-1 ADC voltajı: 86 yayın; 1,631–1,690 V; ortalama **1,65952 V**.
- ct_clamp DEBUG satırlarında 200 ms pencerede yaklaşık 3.445–3.577 örnek, yaklaşık 17.225–17.885 SPS raporlanıyor.

## LOAD-100W-003 uzun loguyla karşılaştırma

| Ölçüt | LOAD-100W-003 (PC beslemesi öncesi) | LOAD-100W-004 (masaüstü kaynak sonrası) |
|---|---:|---:|
| Akım yayını | 160 | 43 |
| Medyan | 0,460 A | 0,423 A |
| Ortalama | 0,4841 A | 0,42274 A |
| Min–maks | 0,422–1,164 A | 0,407–0,440 A |
| 0,55 A üzeri yayın | 10 | 0 |
| 0,427 A ±%4 bandında | 17/160 (%10,6) | 39/43 (%90,7) |

Yeni testin medyanı önceki uzun kayda göre yaklaşık **%8,0 daha düşük** ve 0,427 A geçici beklentiye çok daha yakındır. Yayın aralığı da belirgin biçimde daralmıştır. Bu, kullanıcının güç kaynağını değiştirmesinden sonra gözlenen güçlü bir iyileşme işaretidir. Ancak iki test farklı zamanlarda yapıldığı için tek başına besleme kaynağının nedensel etkisini kanıtlamaz; ampul/şebeke koşulları ve bağlantıların aynı kaldığı da ayrıca doğrulanmalıdır. Yeni kayıt yalnızca yaklaşık 84 saniye ve 43 akım yayını içerir; daha uzun tekrar gerekir.

## Referans ve karar

- **0,427 A:** UNIT cihazı için kullanıcı bildirimi kaynaklı geçici beklenen değerdir; PZEM'in eşzamanlı kararlı okuması bu logda bulunmuyor.
- Bu nedenle 39/43 örneğin ±%4 bandında olması, PZEM'e göre ±%4 kabulü olarak raporlanamaz.
- K katsayısı değiştirilmedi. Firmware/konfigürasyonun değişmediği cihaz logundaki derleme zamanı ve sensör ayarlarıyla destekleniyor; fiziksel güç kaynağı değişikliği kullanıcı beyanıdır.
- **Öneri:** Aynı masaüstü güç kaynağıyla 5–10 dakikalık yeni kayıt al; yük, SCT konumu ve kablo düzenini değiştirme. Aynı aralıkta UNIT ve PZEM değerlerini de kaydet. Böylece iyileşmenin tekrarlanabilirliği ve referans sapması ayrı ayrı doğrulanabilir.
