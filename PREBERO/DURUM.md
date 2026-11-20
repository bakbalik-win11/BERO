# PREBERO – Durum ve çalışma akışı

Bu dosya PREBERO'nun güncel iş akışını gösteren tek takip yeridir. Aktif modül ve görev, mevcut çalışma aşaması, ilerleme, bekleyen işler ve sıradaki adım burada tutulur. Kalıcı ilkeler README.md dosyasındadır; görev teknik ayrıntıları ilgili görev klasöründedir.

## Genel durum

| Modül | Hedef | Durum |
|---|---|---|
| Modül 1 – Bias Gerilim Aktarımı | Şebeke karakterinde gerilimi mevcut bias girişine aktarmak | **Fiziksel imalat tamamlandı; mevcut donanım** |
| Modül 2 – Masaüstü ESP / Akım Testleri | Masaüstü ESP düzeninde sinyal ve akım davranışını incelemek, deney verilerini ve katsayı çalışmalarını yürütmek | **Aktif** |
| Modül 3 – Çamaşır Makinesi | Program aşamalarını gözlemleyip tahmin etmek ve bildirim üretmek | Bekliyor |
| Modül 4 – Bulaşık Makinesi | Program aşamalarını gözlemleyip tahmin etmek ve bildirim üretmek | Bekliyor |
| Modül 5 – Ana Pano | Evde gün boyunca gerçekleşen elektriksel faaliyetleri gözlemlemek | Bekliyor |

## Şu anki çalışma

- **Aktif modül:** Modül 2 – Masaüstü 4 Kanal / Akım Testleri
- **Aktif görev:** MOD2-GRV001 – Akım davranışı ve katsayı çalışmaları
- **Çalışma odağı:** ESP32-D geliştirme kartı ve ESP32 shield ile masaüstü deney düzeneğinin imalatı; ardından sinyal/akım davranışını gözlemlemek ve test kayıtlarını MOD2-GRV001 altında tutmak. Paylaşılan görsel temsildir; kesin kart modeli ve pinout değildir. Modül 1, gerektiğinde bu deney düzenine bias gerilimi sağlayan mevcut donanımdır.

## İlerleme kuralı

Bir görev tamamlandığında sonucu kendi görev klasörüne kaydedilir. Ardından aynı modülün altında bir sonraki görev açılır ve bu dosyadaki durum güncellenir. Modüller arası geçiş, ilgili modülün hedefi ve hazır olma durumuna göre yapılır.


## Modül 1 için kaydedilen karar

- Modül 1, PREBERO/README.md içinde tanımlanmış genel bias orta nokta yapısının fiziksel olarak uygulanmış örneğidir; şebeke karakterinde gerilimi bias girişine aktarmak için kullanılır. Bias standardının kaynağı README.md'dir.
- Modül 1 mevcut, eski fiziksel yapıdır; imalatı tamamlanmıştır. Kapalı kutu içindedir ve bağlantıları soketlidir.
- Modül 1'in önceki imalat multimetre ölçümleri kendi imalat kaydında korunur.
- Masaüstü ESP ile yürütülen sinyal/akım deneyleri Modül 2 kapsamındadır. Modül 1 bu deneylerde bias gerilimi sağlayan donanım olarak kullanılabilir.
- Modül 1 için yeni imalat veya yeniden kurulum görevi açık değildir.
