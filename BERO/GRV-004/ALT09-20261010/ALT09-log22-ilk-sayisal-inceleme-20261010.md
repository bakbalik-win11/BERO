# ALT09 — Log 22 İlk Sayısal İnceleme
Tarih: 2026-10-10
Kaynak dosya: `esp32d1-logs (22).txt` (sohbette yüklenen dosya; ham dosyanın GitHub'a yüklenmesi ayrıca yapılmadı).

## Kod durumu
- ALT09 YAML değiştirilmedi.
- Ham veriler değiştirilmedi.
- Bu belge yalnızca mevcut logdan hesaplanan özet istatistikleri içerir.

## Dosya kapsamı
- Ayrıştırılan ALT09_RAW satırı: 4.943.
- Görünen batch aralığı: 148–167.
- Batch 148 dosyanın başında kısmi (117 örnek); batch 149–167 için 256 örnek/batch.
- 19 batch özeti mevcut (batch 148 özeti görünür dosya bölümünde yok).
- Görünen cihaz log saatleri: 22:08:46–22:10:22.
- Bu dosya 22:04'teki 8,5 W LED başlangıcını ve 22:07'deki 100 W akkor ampul başlangıcını içermiyor. Dolayısıyla bu iki yükün etkisi bu dosyadan ayrı ayrı karşılaştırılamaz.

## Deney işaretleri (kullanıcı bildirimi)
- 22:04 — 8,5 W LED açıldı.
- 22:06 — LED kapatıldı.
- 22:07 — 100 W akkor ampul açıldı.
- 22:08 — 100 W akkor ampul kapatıldı.
- 22:09 — 150 W yük açıldı.
- 22:10 — 150 W yük kapatıldı.
Saat işaretleri kullanıcı tarafından verildi; cihaz log saatleriyle saniye düzeyinde senkron doğrulaması yapılmadı.

## Örnekleme zamanlaması
Batch 149–167 için 19 özetin her biri 256 örnek bildiriyor.
- Ortalama mean_gap_us: 1004,66 µs.
- En küçük bildirilen aralık: 1001 µs.
- Batch'ler arasındaki en büyük max_gap_us: 1793 µs.
- mean_gap_us aralığı: 1003,0–1006,4 µs.
Bu, örnekleme hedefinin yaklaşık 1 kHz olduğunu; ancak aralıkların tamamen sabit olmadığını gösterir. `time_us` damgası dört ADC okumasından önce alındığından, dört kanal aynı anda örneklenmiş sayılmaz.

## Ham ADC dağılımı — karşılaştırma pencereleri
Pencereler, kullanıcı saat işaretlerine göre yaklaşık ayrılmıştır; kesin senkron ölçümü değildir.

| Pencere | Örnek sayısı | BIAS std | K1 std | K2 std | K3 std |
|---|---:|---:|---:|---:|---:|
| 22:08:46–22:09:02 (batch 148–151) | 885 | 12,54 | 14,98 | 9,65 | 9,25 |
| 22:09:05–22:09:57 (batch 152–162; 150 W dönemiyle uyumlu) | 2.816 | 30,43 | 60,82 | 89,46 | 8,90 |
| 22:10:00–22:10:22 (batch 163–167; kapatma çevresi/sonrası) | 1.242 | 24,37 | 37,41 | 58,21 | 9,39 |

Not: Batch 163 22:10:00'da başlar ve kullanıcı 22:10'da yükü kapattığını bildirmiştir; dolayısıyla batch 163 geçişin iki tarafını içerebilir. Batch 164–167 yalnızca kapatma sonrası bölüme daha yakın olmakla birlikte, tekil sıçramalar sürer.

## İlk yorum
- 150 W açma işareti civarında (batch 152–162), K1 ve özellikle K2 dağılımı önceki pencereye göre belirgin büyüyor; K3 dağılımı benzer kalıyor.
- Kapatma sonrasında dağılım genel olarak azalıyor, ancak bazı tekil ADC sıçramaları devam ediyor.
- Bu örüntü yükle ilişkili sinyal olasılığını destekler; tek başına akım ölçümünü doğrulamaz. BIAS ve kanal davranışı, analog devre, ADC girişleri ve örnekleme düzeni birlikte incelenmelidir.
- ALT09 ham örnekleri yaklaşık 1 ms aralıklı olduğundan 50 Hz dalga şeklini örnekleme bakımından temsil edebilir; fakat dört kanalın ardışık okunması ve gerçek aralık değişkenliği nedeniyle RMS doğruluğu ayrıca doğrulanmalıdır. Bu logdan kalibre edilmiş amper değeri çıkarılmamalıdır.

## Sonraki adım
1. Bu ham logu Python ile zaman ekseninde BIAS/K1/K2/K3 olarak çiz.
2. 22:09 ve 22:10 geçişlerini grafikte işaretle.
3. Tekil sıçramaları ve kanallar arası birlikte değişimi incele.
4. Önceki ALT09 raporuna dokunmadan bu incelemeyi ayrı alt rapor olarak tut.
5. YAML'ı değiştirme.
