# ESP32 Kaynaklı Bias ve Ortak GND Deneyi

**Tarih:** 2026-11-21  
**Durum:** AÇILDI – fiziksel uygulama ve ölçüm bekleniyor  
**Görev:** MOD2-GRV001  
**Donanım:** ESP32D2 + ADS1115 No.10 (I²C 0x48) + SCT013 ölçüm kanalı  
**Deney türü:** Bias besleme kaynağı / referans bağlantısı karşılaştırması

## 1. Amaç

Önceki bias deneylerinde bias gerilimi harici Bias Modül 1'den sağlanmıştı. Bu yeni deneyde bias ESP32 kartının 3.3 V beslemesinden üretilecek ve **ESP32 GND ile ADS1115/bias devresi GND ortaklanacaktır**.

Amaç, ESP32 kaynaklı bias ve ortak toprak referansı ile ölçümün davranışını gözlemlemek; önceki Modül 1 bias sonuçlarıyla karşılaştırılabilir veri toplamaktır.

## 2. Bu deneyde açıkça değiştirilen koşullar

- **Bias kaynağı:** Harici Bias Modül 1 yerine ESP32 kartının 3.3 V hattı.
- **Toprak referansı:** ESP32 GND, ADS1115 GND ve bias bölücü devresinin GND noktası ortak olacak.
- **Bias orta noktası:** ESP32 3.3 V ve GND arasında kurulacak bias ağı üzerinden üretilecek. Direnç değerleri ve tam bağlantı, enerji verilmeden önce fiziksel devre teyidiyle ayrıca kaydedilecek.

Bu deneyin temel farkı yalnızca bias kaynağının ESP32 olması değil; **GND'nin de ortak referans olarak bağlanmasıdır**. Önceki Modül 1 deneyleriyle karşılaştırırken bu iki değişken birlikte dikkate alınmalıdır.

## 3. Korunacak koşullar

- ESP32D2 ve ADS1115 No.10 kullanılacak.
- Mevcut SCT sensörleri, iletken, yön ve fiziksel konum mümkün olduğunca korunacak.
- K=27.59 değiştirilmeyecek.
- Çalışan YAML/firmware değiştirilmeyecek.
- Mevcut Modül 1 bias deneyi kayıtları değiştirilmeden korunacak.
- PZEM karşılaştırma referansıdır; ground truth değildir.

## 4. Enerji vermeden önce bağlantı ve güvenlik kontrolleri

1. Tüm bağlantılar enerji kesikken yapılacak.
2. ESP32 GND, ADS1115 GND ve bias devresi GND sürekliliği kontrol edilecek.
3. Bias orta noktası ölçülerek DC seviyesi kaydedilecek.
4. ADS1115 A girişlerinin her birinin GND'ye göre mutlak gerilimi kontrol edilecek.
5. ADS1115 girişleri, kartın besleme sınırlarının dışına çıkarılmayacak. Diferansiyel ölçüm seçimi mutlak giriş gerilimi sınırlarını kaldırmaz.
6. SCT013 sekonder devresi ve ADC giriş bağlantıları doğrulanmadan ölçüme başlanmayacak.
7. Direnç değerleri, bağlantı fotoğrafı ve ölçülen bias gerilimi deney kaydına eklenecek.

**Önemli:** ESP32 3.3 V hattı, bias bölücüsü ve ADS1115 giriş bağlantısı için kesin direnç değerleri bu kayıt açılırken henüz teyit edilmedi. Bu nedenle burada direnç değeri veya kesin pin bağlantısı varsayılmamıştır.

## 5. Değerlendirme

- Boşta davranış: taban, medyan, standart sapma, maksimum ve eşik üstü spike sayısı.
- Yük altında davranış: ortalama, medyan, standart sapma ve CV.
- PZEM ile aynı zaman aralığında akım karşılaştırması; mümkünse ±2 saniye eşleştirme.
- Biaslı ölçümün PZEM'e yakınlığı ve boşta spike davranışı ayrı ayrı değerlendirilecek.
- Önceki Modül 1 bias kayıtlarıyla karşılaştırma yapılırken ortak GND farkı açıkça belirtilecek.
- PZEM'in yetersiz örnek verdiği alanlarda MAPE hesaplanmayacak.

## 6. Açılış kararı

Kullanıcı, yeni deneyde biasın ESP32 kartından sağlanacağını ve GND'nin ortaklanacağını açıkça belirtti. Deney bu bağlantı koşullarıyla açıldı.

**Henüz yapılmadı:** Fiziksel bağlantı, direnç değerlerinin teyidi, bias DC ölçümü, ESPHome/HA veri kaydı ve sonuç analizi.

**Durum:** Deney açık; tamamlandı olarak işaretlenmedi.
