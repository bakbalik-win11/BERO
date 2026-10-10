# ALT09 Log 22 — İlk Grafik İncelemesi

Tarih: 2026-10-10  
Kaynak: `esp32d1-logs (22).txt` (bu sohbet içinde yüklenen dosya)

## Durum
- Ayrıştırılan `ALT09_RAW` örneği: 4.943
- Görünen cihaz log aralığı: 22:08:46.595–22:10:22.201
- Batch aralığı: 148–167
- ALT09 YAML: **değişmedi**
- Ham satırlar: **değiştirilmedi**
- Bu rapor ve CSV özet GitHub'a kaydediliyor; grafik PNG'leri bu commit'e dahil değil.

## Yük işaretleri
- 22:09 — 150 W açıldı (kullanıcı bildirimi)
- 22:10 — yük kapatıldı (kullanıcı bildirimi)

Kullanıcı saatleriyle cihaz log saatleri saniye düzeyinde senkronize edilmedi; işaretler yaklaşık karşılaştırma içindir.

## Pencere karşılaştırması

Standart sapma ADC sayımı cinsindendir, amper değildir.

| Pencere | Örnek | BIAS std | K1 std | K2 std | K3 std |
|---|---:|---:|---:|---:|---:|
| 22:09 öncesi | 629 | 13.74 | 12.64 | 8.83 | 8.64 |
| 22:09–22:10 (yük açık işaretli) | 3072 | 29.25 | 58.22 | 85.54 | 8.91 |
| 22:10 sonrası | 1242 | 16.83 | 32.43 | 42.83 | 9.73 |

## İlk yorum
- 22:09–22:10 penceresinde K1 ve özellikle K2 değişkenliği, 22:09 öncesine göre belirgin artıyor.
- 22:10 sonrasında K1/K2 değişkenliği azalıyor, fakat önceki pencereye tamamen dönmüyor.
- BIAS değişkenliği de yük işareti civarında arttığı için değişimin tamamını doğrudan akım sinyali olarak yorumlayamayız.
- K3 standart sapması pencereler arasında görece sabit kalıyor.
- Bu, yükle ilişkili bir değişim olabileceğini gösterir; akım RMS değerini veya amper kalibrasyonunu doğrulamaz.

## Sonraki adım
1. Ham veriyi değiştirmeden tekil sıçramaları işaretle.
2. Ardışık örnek farklarını ve kanallar arası birlikte sapmaları incele.
3. ALT09 YAML'a dokunmadan önce örnekleme zamanlamasını ve analog giriş zincirini doğrula.
