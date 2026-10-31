# FAN-2 — Modül 2 / SCT-1 uzun log analizi

**Test durumu:** KAPATILDI — düşük akım gözlem kaydı. ±%4 doğruluk testi değildir.

## 1. Kaynak ve bütünlük

- Kaynak dosya: `esp32d1-logs (42).txt`
- Dosya boyutu: 90.706 bayt
- Kaynak satır sayısı: 1.228
- SHA-256: `e550d447b75b50e2b99581a70de23b8916caba576a8665240f44574e586a3dca`
- Akım yayın aralığı: 17:26:19.113–17:31:41.120 (+03:00), yaklaşık 5 dakika 22 saniye
- SCT akım yayını: 162
- Önceki kısa FAN-2 kaydı (41) ilk 54 yayını içeriyordu. Uzun dosyanın başlangıcı kısa dosyayla byte düzeyinde aynıdır; bu aynı oturumun uzatılmış kaydıdır. Kısa ve uzun kayıt birleştirilerek 216 yayın sayılmaz; uzun dosya 108 yeni yayın ekler.

## 2. Fiziksel düzenek ve firmware

- ESP32D1 / Modül 2
- SCT-1 sarı sinyal: GPIO32 / ADC1_CH4
- Ortak bias turuncu: GPIO35 / ADC1_CH7
- SCT-2 GPIO33 ve SCT-3 GPIO34 bu oturumda kullanılmadı.
- ESPHome 2026.10.1; derleme zamanı 2026-10-31 15:55:25 +0300
- ADC attenuation 12 dB; ADC entity güncellemesi 1 s
- `ct_clamp` örnek penceresi 200 ms; akım ve Raw AC yayın aralığı 2 s
- Logda raporlanan SPS ortalaması 17.076,8; aralık 16.530–17.800 SPS. Bu, ct_clamp logundaki farklı örnek sayısından türetilmiştir; bağımsız donanım örnekleme doğrulaması değildir.
- Kapanış YAML snapshot: [FAN-2 YAML](../../firmware/archive/FAN-2-2026-10-31-esp32d1-sct1.yaml). Snapshot depodaki Modül 2 tek kanal YAML'ının kapanış anındaki kopyasıdır; binary ile kriptografik eşleşme iddiası yoktur.

## 3. UNIT bildirimi ve düşük akım sınıfı

- Kullanıcı bildirimi: UNIT akımı **0,106 A**.
- 0,30 A altı BERO düşük akım araştırma bölgesidir; ±%4 kabul/ret kriteri uygulanmaz.
- 0,30 A sınırı BERO test sınıflandırmasıdır; SCT üretici spesifikasyonu veya garantili alt ölçüm sınırı değildir.
- UNIT mutlak doğru/ground truth kabul edilmez. Bu logda PZEM akım ve PF verisi yoktur.

## 4. Akım istatistikleri

162 SCT akım yayını:

| İstatistik | Değer |
|---|---:|
| Ortalama | 0,168969 A |
| Medyan | 0,1685 A |
| Minimum | 0,108 A |
| Maksimum | 0,257 A |
| Örnek standart sapma | 0,024640 A |
| 0,30 A altındaki yayın | 162 / 162 |

Kısa dosyadaki ilk 54 yayının ortalaması 0,164259 A idi. Uzun dosyanın tamamında ortalama 0,168969 A oldu. İlk 54 yayının uzun dosyada zaten bulunduğu dikkate alınmıştır.

## 5. Analog kanallar

| Kanal | Örnek sayısı | Ortalama | Minimum | Maksimum |
|---|---:|---:|---:|---:|
| Raw AC (ct_clamp penceresi) | 162 | 0,006977 V | 0,00445 V | 0,01059 V |
| Ortak bias GPIO35 | 324 | 1,663426 V | 1,651 V | 1,673 V |
| SCT-1 ADC GPIO32 | 324 | 1,660537 V | 1,642 V | 1,684 V |

Raw AC, ct_clamp 200 ms penceresinden yayınlanan gerilimdir; GPIO32'nin 1 saniyelik ADC entity voltajıyla aynı ölçüm değildir.

## 6. Sistem ve log sağlığı

- Wi-Fi bağlantısı başarılı; cihaz IP 192.168.0.31; başlangıç RSSI −54 dB.
- ADC GPIO32 ve GPIO35 başlatma/konfigürasyon/kalibrasyon durumları OK.
- Üç ESPHome derleyici/optimizasyon uyarısı mevcut.
- Logda [E] hata kaydı, brownout veya yeniden başlatma işareti görülmedi.
- Bu tespit yalnızca paylaşılan log kapsamındadır; uzun süreli donanım güvenilirliği sertifikası değildir.

## 7. Teknik yorum ve karar

FAN-2 uzun logu, Modül 2 / SCT-1 zincirinin yaklaşık 5 dakika 22 saniye boyunca 162 akım yayını ürettiğini gösterir. Ölçümlerin tamamı 0,30 A altındadır. Bu nedenle log düşük akım gözlemidir; ±%4 başarı/başarısızlık sonucu çıkarılmaz.

UNIT'in 0,106 A bildirimi ile SCT ortalaması 0,168969 A arasındaki fark not edilebilir; ancak düşük akım politikasına göre bu fark kabul/ret ölçütü değildir. UNIT ve SCT ölçümlerinin aynı kararlı zaman penceresinde eşzamanlı alındığı logla gösterilmemiştir.

UNIT PF göstermiyor. PF'nin olası etkisi hipotez olarak kalır; bu logla doğrulanamaz. Sonraki değerlendirmede PZEM akım ve PF aynı kararlı pencerede kaydedilmelidir.

## 8. Kapanış ve açık işler

- FAN-2, **Modül 2 düşük akım gözlem oturumu** olarak kapatıldı.
- FAN-2, ±%4 akım doğrulama testi olarak kapatılmadı.
- K=24.22 değiştirilmedi; yazılımsal sıfır eşiği eklenmedi.
- Kısa log ve uzun log ayrı kaynaklar olarak korunur; uzun log kısa kaydı içerdiğinden yayınlar çift sayılmaz.
- 0,30 A altı ayrı deney programı açıktır. 1 tur / 2 tur / 4 tur karşılaştırmaları henüz yapılmış değildir.
- PZEM akım + PF ile eşleşmiş kararlı pencere kaydı sonraki aşamadır.
