# MOD2-GRV001 – Bias sabit kanal 42 W testi

**Tarih:** 2026-11-21  
**Durum:** AÇILDI – 42 W yükte ölçüm bekleniyor.  
**Amaç:** Üç çapraz deneyde bias lehine oluşan bulgudan sonra, bias bağlantısını ve kanal eşlemesini hiç değiştirmeden yaklaşık 42 W yükte davranışı incelemek. Özellikle düşük akım bölgesinde biaslı ve biassız kanalın ölçüm farkını, PZEM karşılaştırmasını ve kararlılığını gözlemek.

## 1. Sabit fiziksel bağlantı

| ADS1115 kanalı | Bağlantı |
|---|---|
| A0–A1 | **Bias yok** |
| A2–A3 | **Bias var** |

- Üçüncü çapraz deneyde kullanılan kanal eşlemesi korunacak.
- Sensörler, kablolar ve bias bağlantısı bu test için yer değiştirmeyecek.
- Bias besleme kaynağı Modül 1 olarak kalacak. ESP32 kartından bias beslemesi bu testin konusu değildir.

## 2. Test yükü

- Hedef yük: yaklaşık **42 W**.
- Gerçek aktif güç ve akım PZEM'den ayrıca kaydedilecek.
- 42 W değeri nominal/hedef yük olarak kabul edilecek; gerçek yükün tam 42 W olduğu varsayılmayacak.
- Yük kararlı hale geldikten sonra HA kaydı alınacak. Başlangıç/geçiş anları analiz penceresine karıştırılmayacak.

## 3. Değişmeden kalacak sistem

- ESP32D2.
- ADS1115 fiziksel modül No.10, I²C 0x48.
- Aynı iki SCT013 30A/1V sensörü; aynı faz iletkeni, yön ve konum.
- Mevcut iki kanallı YAML aynen kullanılacak.
- K=27.59 ve diğer firmware/ölçüm ayarları değiştirilmeyecek.
- Tek kanallı çalışan V1.1 YAML korunacak.

## 4. Değerlendirme

Her kanal için örnek sayısı, ortalama, standart sapma, minimum, maksimum ve CV hesaplanacak. PZEM akımı ve gücü karşılaştırma referansı olarak kaydedilecek; PZEM ground truth değildir.

PZEM/SCT örnekleri ±2 saniye içinde eşleştirilerek biaslı ve biassız kolların ortalama farkı, signed error ve MAPE değerleri karşılaştırılacak.

Önceki deneylerde SCT'nin düşük akım bölgesinde (yaklaşık 0.3–0.5 A altı) güvenilirliğinin zayıflayabildiği gözlenmişti. 42 W testi bu nedenle özellikle önemlidir. Ancak biasın bu bölgede ölçümü iyileştireceği peşinen kabul edilmeyecek; veriyle değerlendirilecek.

## 5. Karar sınırları

- Biaslı A2–A3 kolunun PZEM referansına daha yakın olması, 42 W çalışma noktasında bias lehine bulgu sayılacaktır.
- Daha yüksek akım okuması tek başına pozitif doğruluk kanıtı değildir.
- Standart sapma ve CV ayrıca incelenmeden gürültü azalması sonucu çıkarılmayacaktır.
- Tek bir 42 W noktası tüm düşük akım aralığını veya tek K katsayısının yeterliliğini kanıtlamaz.
- Bu testte kanal veya bias kaynağı değiştirilirse deney koşulları bozulur; değişiklik ayrı deney olarak kaydedilmelidir.

## 6. Arşivlenecek çıktılar

- Kaynak Home Assistant CSV.
- ESPHome logu (mevcutsa).
- PZEM/SCT zaman eşleştirme CSV.
- İstatistik ve karşılaştırma raporu.
- Fiziksel bağlantı ve yük fotoğrafı/teyidi.

**Mevcut durum:** Deney planı açıldı. 42 W ölçümü henüz alınmadı; sonuç veya doğrulama iddiası yoktur.


## Kapanış kaydı (2026-11-21)

**Durum: KAPATILDI – uygulanmadı / iptal edildi.**

Üç çapraz deneyin ortak sonucu kullanıcı tarafından biasın yaklaşık 0.47 A çalışma noktasında faydalı olduğuna dair yeterli bulgu olarak değerlendirildi. Bu nedenle planlanan 42 W sabit kanal deneyi bu aşamada yapılmayacak. Bu dosya deney sonucu içermez; yalnızca açılmış ancak uygulanmadan kapatılmış planın iz kaydıdır.

Yeni bir düşük akım testi ileride gerekli görülürse ayrı bir deney olarak, yeni karar ve koşullarla açılacaktır.
