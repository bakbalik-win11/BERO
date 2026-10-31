# LOAD-100W-004 — ESP32D1 masaüstü güç kaynağıyla SCT-1 uzun tekrar analizi

**Tarih:** 2026-10-31  
**Yük:** 100 W akkor ampul  
**Düzenek:** ESP32D1 / Modül 2 / SCT-1 sarı GPIO32 (ADC1_CH4); ortak bias turuncu GPIO35 (ADC1_CH7)  
**Besleme:** Kullanıcı bildirimi: PC USB yerine masaüstü harici güç kaynağı  
**Firmware:** ESPHome 2026.10.1; derleme zamanı 15:55:25 +03:00; ct_clamp sample_duration 200 ms; akım update 2 s; ADC update 1 s; 12 dB  
**Özgün log:** 1.602 satır, 118.860 bayt; SHA-256 `de3f2289700f657cfcf1fd8bff816bbd8a8bc05bb2296f349462709cbb42d859`

## Kapsam ve zaman aralığı

- Cihaz log başlangıcı: 16:06:43.782
- İlk / son akım yayını: 16:06:45.189 – 16:13:53.226 (+03:00)
- Son bias / SCT ADC yayını: 16:13:53.515 / 16:13:53.652
- Akım yayını sayısı: 215
- Yaklaşık ölçüm süresi: 7 dakika 8 saniye (ilk ve son akım yayını arasındaki süre)

## Akım sonuçları

| Ölçüt | Sonuç |
|---|---:|
| Yayın sayısı | 215 |
| Ortalama | 0,425 A |
| Medyan | 0,423 A |
| Örnek standart sapma | 0,01149 A |
| Minimum – maksimum | 0,401 – 0,480 A |
| 0,55 A üzeri yayın | 0 |
| 0,427 A ±%4 bandında | 192/215 (%89,3) |

Geçici UNIT beklentisi 0,427 A için ±%4 aralığı 0,40992–0,44408 A'dır. Ölçümlerin %89,3'ü bu aralıktadır. Medyan 0,423 A, geçici beklentinin yaklaşık %0,94 altındadır; ortalama 0,425 A yaklaşık %0,47 altındadır.

**Referans ayrımı:** 0,427 A, kullanıcı bildirimiyle kaydedilmiş geçici UNIT beklentisidir. Bu logda eşzamanlı UNIT veya PZEM ölçümü yoktur. Dolayısıyla bu kıyas PZEM doğrulaması veya kesin ±%4 kabul sonucu değildir.

## Analog ve örnekleme telemetrisi

| Kanal / metrik | Örnek sayısı | Minimum | Maksimum | Ortalama |
|---|---:|---:|---:|---:|
| Raw AC | 215 | 0,01656 V | 0,01982 V | 0,01755 V |
| Common Bias GPIO35 | 430 | 1,653 V | 1,681 V | 1,66367 V |
| SCT-1 ADC GPIO32 | 430 | 1,631 V | 1,692 V | 1,66144 V |
| ct_clamp raporlanan SPS | 215 pencere | 17.225 | 18.000 | 17.659 |

ct_clamp logunda 200 ms pencere başına yaklaşık 3.445–3.600 farklı örnek raporlanmıştır. Bu sayıların kütüphane tarafından raporlanan pencere telemetrisi olduğu, bağımsız osiloskop/ADC ham örnek doğrulaması olmadığı not edilmelidir.

## Önceki kısa LOAD-100W-004 kesitiyle ilişki

Önceki kısa log aynı testin ilk yaklaşık 84 saniyesini ve 43 akım yayınını içeriyordu. Bu uzun kayıt ilk bölümle aynı zaman damgasından başlıyor ve 215 akım yayınına uzanıyor; bu nedenle yeni bağımsız test ID'si açılmadı. LOAD-100W-004 kaydının uzun sürümü olarak arşivlendi.

Kısa kesitte ortalama 0,42274 A, medyan 0,423 A ve 39/43 (%90,7) yayın geçici UNIT ±%4 bandındaydı. Uzun kesitte medyan 0,423 A olarak kaldı; ortalama 0,425 A, band içi oranı 192/215 (%89,3) oldu. Bu, daha uzun süre boyunca benzer merkez değerin korunduğuna işaret eder.

Önceki LOAD-100W-003 uzun logunda medyan 0,460 A, ortalama 0,4841 A, maksimum 1,164 A ve 10 adet 0,55 A üzeri yayın vardı. Yeni uzun LOAD-100W-004 kaydında 0,55 A üzeri yayın yoktur. Bu iki koşu arasındaki belirgin fark, harici besleme hipotezini destekler; ancak yük/ortam/zaman koşulları birebir kontrollü eşleştirilmediğinden güç kaynağının tek başına nedensel etkisi kanıtlanmış değildir.

## Güç kaynağı ve ESP32D1 yorumu

Log, cihazın ESP32 rev3.1, iki çekirdekli olduğunu ve Wi-Fi bağlantısının açık kaldığını gösterir. Wi-Fi RSSI yaklaşık -50 dB'dir. Brownout veya yeniden başlama hatası görünmemektedir. Derleme optimizasyonlarıyla ilgili üç bilgilendirme uyarısı vardır; bunlar bu ölçüm sırasında hata veya brownout kanıtı değildir.

Bias değerinin bu koşuda 1,653–1,681 V aralığında kalması ve akım yayınlarının belirgin sıçrama göstermemesi olumlu gözlemlerdir. Bununla birlikte log ESP32'nin 5 V girişini veya 3,3 V regülatör rayını ölçmüyor. Dolayısıyla güç kaynağı çıkışının yük altındaki gerilim/ripple kalitesi bu logdan ölçülmüş sayılamaz.

## Teknik değerlendirme ve karar

1. Bu log, tek aktif SCT-1 ct_clamp kanalının harici masaüstü besleme koşulunda 7 dakikadan uzun süre kararlı akım yayını ürettiğini gösterir.
2. Üç kanallı kodun önceki testindeki yüksek sıçramalar ile bu tek kanallı koşu arasındaki fark, üç kanalı aynı ESP üzerinde eşzamanlı okutmanın ek yük/zamanlama etkisi olabileceği hipotezini güçlendirir. Tek başına kanıtlamaz.
3. **Geçici mimari çalışma kararı:** Bir ESP düğümünde bir aktif SCT akım okuma kanalı. Üç SCT için üç ayrı ESP düğümü yaklaşımı, kontrollü karşılaştırma tamamlanana kadar tercih edilen test mimarisi olarak ele alınacaktır. Bu kararın gerekçesi ölçüm kararlılığı ve görev izolasyonudur; üç kanalın aynı ESP'de kesinlikle çalışamayacağı iddiası değildir.
4. Harici, regüle ve yeterli akım kapasiteli 5 V besleme kullanılmaya devam edilmeli. USB ve harici 5 V aynı anda bağlanmamalı; kartın güç giriş topolojisine göre tek besleme yolu kullanılmalı. ESP GND, bias devresi GND'si ve SCT ölçüm devresinin referans GND'si ortak olmalıdır. ESP32 ADC girişlerine 5 V uygulanmamalıdır.
5. Güç kaynağı etkisini ayırmak için aynı ESP, aynı tek kanal kodu, aynı ampul, aynı SCT ve aynı kablo düzeniyle PC USB / harici 5 V koşuları sırayla tekrarlanmalı; her koşuda en az 5–10 dakika log ve mümkünse 5 V ile 3,3 V ray ölçümü alınmalıdır.
6. K katsayısı değiştirilmedi. 0,427 A geçici UNIT beklentisi PZEM ile aynı kararlı pencerede doğrulanana kadar kesin referans değildir.

## Kanıt sınıflandırması

- **LOG:** 1.602 satırlık ESPHome logu; hash yukarıda.
- **KULLANICI BİLDİRİMİ:** Beslemenin PC USB'den masaüstü harici güç kaynağına alındığı bilgisi.
- **HESAPLAMA:** Akım, bias, ADC ve SPS istatistikleri log satırlarından çıkarıldı.
- **HİPOTEZ:** Harici besleme ve tek kanalın kararlılığa katkısı; kontrollü A/B testiyle ayrıştırılmalı.
- **EKSİK KANIT:** Eşzamanlı UNIT/PZEM ölçümü, 5 V giriş ölçümü, 3,3 V ray ölçümü ve aynı koşulda kontrollü USB A/B tekrarı.
