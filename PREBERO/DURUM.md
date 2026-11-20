# PREBERO – Durum ve çalışma akışı

Bu dosya PREBERO'nun güncel iş akışını gösteren tek takip yeridir. Aktif modül ve görev, mevcut çalışma aşaması, ilerleme, bekleyen işler ve sıradaki adım burada tutulur. Kalıcı ilkeler README.md dosyasındadır; görev teknik ayrıntıları ilgili görev klasöründedir.

## Genel durum

| Modül | Hedef | Durum |
|---|---|---|
| Modül 1 – Şebeke Karakterini Koruyan Bias | Şebeke ile ilişkili AC sinyalin karakterini korumayı hedefleyen bias yapısını geliştirmek ve ESP kaynaklı bias yaklaşımından ayrı değerlendirmek | Yardımcı modül |
| Modül 2 – Akım Testleri | Akım davranışını anlamak, testleri sürdürmek ve ölçüm katsayılarını belirlemek | **Aktif** |
| Modül 3 – Çamaşır Makinesi | Program aşamalarını gözlemleyip tahmin etmek ve bildirim üretmek | Bekliyor |
| Modül 4 – Bulaşık Makinesi | Program aşamalarını gözlemleyip tahmin etmek ve bildirim üretmek | Bekliyor |
| Modül 5 – Ana Pano | Evde gün boyunca gerçekleşen elektriksel faaliyetleri gözlemlemek | Bekliyor |

## Şu anki çalışma

- **Aktif modül:** Modül 2 – Masaüstü 4 Kanal / Akım Testleri
- **Aktif görev:** MOD2-GRV001 – Akım davranışı ve katsayı çalışmaları
- **Çalışma odağı:** Sinyali gözlemlemek, testleri sürdürmek, bias ihtiyacını değerlendirmek ve katsayıları deney sonuçlarına göre belirlemek.

## İlerleme kuralı

Bir görev tamamlandığında sonucu kendi görev klasörüne kaydedilir. Ardından aynı modülün altında bir sonraki görev açılır ve bu dosyadaki durum güncellenir. Modüller arası geçiş, ilgili modülün hedefi ve hazır olma durumuna göre yapılır.


## Modül 1 için kaydedilen karar

- Modül adı: **Şebeke Karakterini Koruyan Bias**.
- 1,65 V seviyesinin elde edilme yöntemi, bias devresinin tanımı değil; ayrı bir ara süreçtir.
- Bias yapısının kendisi, gerçek direnç ve kondansatör değerleri ile bağlantı biçimi belirlenerek yeniden kurulabilir bir standart olarak tarif edilecektir.
- ESP beslemesinden oluşturulan bias, şebeke karakterini taşımayan ayrı bir karşılaştırma yaklaşımıdır.
- Bu karar, devrenin elektriksel davranışının veya izolasyonunun doğrulandığı anlamına gelmez.
