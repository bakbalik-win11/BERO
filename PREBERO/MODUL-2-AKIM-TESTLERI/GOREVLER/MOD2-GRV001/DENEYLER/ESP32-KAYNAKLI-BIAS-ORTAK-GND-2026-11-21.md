# ESP32 Kaynaklı Bias ve Ortak GND Deneyi

**Tarih:** 2026-11-21  
**Durum:** KAPATILDI – Kettle 2 ölçümü analiz edildi  
**Görev:** MOD2-GRV001  
**Donanım:** ESP32D2 + ADS1115 No.10 (I²C 0x48) + SCT013 ölçüm kanalı  
**Deney türü:** ESP32 kaynaklı bias / ortak GND

## 1. Amaç

Önceki bias deneylerinde bias gerilimi harici Bias Modül 1'den sağlanmıştı. Bu deneyde bias ESP32 kartının 3.3 V beslemesinden üretildi ve ESP32 GND ile ADS1115/bias devresi GND ortaklandı.

Amaç, doğru ve yeterli ölçüm davranışı elde edilebiliyorsa harici bias yapısını kaldırarak devreyi basitleştirmektir.

## 2. Deney koşulları

- Bias kaynağı: ESP32 kartının 3.3 V hattı.
- Bias orta noktası: kullanıcı ölçümü/bildirimi 1.66 V.
- Toprak referansı: ESP32 GND, ADS1115 GND ve bias devresi GND ortak.
- ESP32D2 ve ADS1115 No.10 (I²C 0x48).
- K=27.59 korunmuştur.
- Çalışan YAML/firmware değiştirilmemiştir.
- PZEM karşılaştırma referansıdır; ground truth değildir.

## 3. Güvenlik ve bağlantı kaydı

Deney öncesinde bağlantılar enerji kesikken yapılmalı; ortak GND sürekliliği, bias orta noktası ve ADS1115 A girişlerinin GND'ye göre mutlak gerilimleri kontrol edilmelidir. ADS1115 girişleri besleme raylarının mutlak sınırları içinde kalmalıdır. Diferansiyel ölçüm seçimi bu sınırları kaldırmaz.

**Kayıt sınırı:** Bu deney kaydında direnç değerleri ve her ADC pininin ayrı ayrı GND'ye göre ölçülmüş gerilimleri sayısal olarak verilmemiştir. 1.66 V bias bilgisi kullanıcı tarafından bildirilmiştir.

## 4. Kettle 2 – kaynatma modu sonucu

Kaynak: kullanıcı yüklemesi `history (17)(1).csv` (430 satır). İlk açılış/geçiş örnekleri dışarıda bırakılarak 23:03:15–23:05:21.486 Türkiye saati aralığı analiz edildi.

| Seri | n | Ortalama (A) | Std. sapma (A) | Min (A) | Maks (A) | CV |
|---|---:|---:|---:|---:|---:|---:|
| ESP32 akım sensörü | 127 | 6.71357 | 0.19456 | 6.36434 | 7.04518 | %2.898 |
| ESP32 A2–A3 | 127 | 6.83096 | 0.18910 | 6.41020 | 7.12883 | %2.768 |
| PZEM akım | 24 | 6.80079 | 0.01178 | 6.78700 | 6.82400 | %0.173 |

PZEM'in 24 örneği için ±2 saniye içindeki en yakın SCT örnekleri eşleştirildi:

| Seri | Eşleşme | MAPE |
|---|---:|---:|
| ESP32 akım sensörü | 24/24 | %2.801 |
| ESP32 A2–A3 | 24/24 | %2.550 |

### Gözlem

- Her iki SCT serisinde de yaklaşık 6.4–7.1 A aralığında belirgin dalgalanma görülmüştür.
- PZEM serisi aynı aralıkta çok daha az değişmiştir.
- A2–A3 ortalaması PZEM ortalamasına yakındır ve eşleştirmeli MAPE değeri diğer SCT serisinden düşüktür.
- İki SCT kanalındaki ortak dalgalanmanın kaynağı bu deneyle belirlenememiştir. RMS akım trendi, 50 Hz dalga şeklinin kendisi değildir.
- PZEM ground truth değildir; daha düşük örnekleme hızı hızlı değişimleri aynı ayrıntıda göstermez.

## 5. Deney kararı

Kullanıcı kararıyla ESP32 kaynaklı bias + ortak GND deneyi KAPATILDI. Kettle 2 verisi, ESP32 bias yapısının bu çalışma koşulunda işe yaradığını ve A2–A3 sonucunun PZEM karşılaştırmasına yakın olduğunu desteklemektedir.

Bu tek deney, tüm yüklerde doğruluk veya gürültü iyileşmesi kanıtı değildir. K=27.59 ve firmware/YAML değiştirilmemiştir.

## 6. Sonraki deneyler

Aynı ESP32 kaynaklı bias ve ortak GND düzeni korunarak:
1. 100 W yükte karşılaştırma.
2. 15 W yükte karşılaştırma.

Bu iki deney tamamlanmadan ESP32 bias yapısı tüm yükler için nihai ilan edilmeyecektir.

## 7. Veri ve rapor konumları

- Analiz raporu: `../V1.1/RAPOR/V1.1-ESP32-BIAS-KETTLE2-2026-11-21.md`
- Sayısal özet CSV: `../V1.1/LOG/V1.1-ESP32-BIAS-KETTLE2-OZET-2026-11-21.csv`
- Kaynak HA dışa aktarımı: `history (17)(1).csv`, 430 satır. Ham dosyanın GitHub'a birebir kopyası bu kayıtla birlikte yüklenmemiştir; kaynak dosya konuşmadaki yüklemedir.


## 2026-11-21 – 100 W sınıfı yük deneyi

- **Durum:** Veri analizi tamamlandı; 100 W sınıfı oturum kapatıldı.
- **Kaynak:** Kullanıcı yüklemesi `history (18)(1).csv` (431 satır). Ham CSV'nin birebir GitHub kopyası yüklenmedi.
- **Analiz:** SCT kararlı penceresi 23:13:20–23:15:47 Türkiye saati; iki SCT kolunda 148'er örnek. PZEM'de ilk 0 A geçiş örneği hariç 9 akım örneği kullanıldı.
- **Diğer ESP32 akım kolu:** Ortalama 0.425253 A; CV %2.086; PZEM eşleştirmeli MAPE %9.597.
- **A2–A3 ESP32 biaslı kol:** Ortalama 0.441694 A; CV %2.066; PZEM eşleştirmeli MAPE %5.184.
- **PZEM:** Ortalama 0.469889 A; güç kayıtları yaklaşık 106.8–108.8 W.
- **Yorum:** ESP32 biaslı A2–A3 kolu diğer SCT kolundan daha yüksek ve PZEM'e daha yakın sonuç verdi. Ancak MAPE %5.184 ve PZEM örnek sayısı 9 olduğundan sonuç tek başına harici biası kaldırmak için yeterli doğruluk kanıtı değildir. Biasın gürültüyü azalttığı gösterilmedi.
- **Kod:** K=27.59 ve çalışan YAML/firmware değiştirilmedi.
- **Rapor:** `../V1.1/RAPOR/V1.1-ESP32-BIAS-100W-2026-11-21.md`
- **Sayısal özet:** `../V1.1/LOG/V1.1-ESP32-BIAS-100W-OZET-2026-11-21.csv`
- **Sıradaki adım:** Aynı ESP32 bias + ortak GND düzeniyle 15 W deneyi.
