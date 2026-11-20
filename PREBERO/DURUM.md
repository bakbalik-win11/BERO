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
- **Çalışma odağı:** ESP32-D geliştirme kartı + ESP32 shield, SCT013 30A/1V akım sensörü ve ADS1115 ara entegresiyle masaüstü deney düzeneğinin imalatı; ardından sinyal/akım davranışını gözlemlemek ve test kayıtlarını MOD2-GRV001 altında tutmak. Paylaşılan ESP32/shield görseli temsildir; kesin kart modeli ve pinout değildir. Modül 1, gerektiğinde bu deney düzenine bias gerilimi sağlayan mevcut donanımdır.

## Modül 2 – sıradaki deney

- Mevcut sadeleştirilmiş akım okuma koduyla önceki ADS1115 modülünde okuma yapılmıştır; kullanıcı bu sürümü **Kod 0** olarak ayırmıştır.
- Yeni katsayı çalışması ADS1115 **No. 1** üzerinde yapılacaktır; önceki modülün katsayısı aktarılmayacaktır.
- Katsayı çalışmasından önce bias ve sıfır düzeltmesi gerekliliği deneyi yapılacaktır. Tek ADS1115 No. 1 ve aynı faz iletkenini ölçen iki ayrı SCT013 kullanılacaktır.
- **SCT013 No. 1 → A0–A1:** biaslı ölçüm kolu.
- **SCT013 No. 2 → A2–A3:** biassız ölçüm kolu.
- İki SCT aynı tek faz iletkenini ölçecek; sensörlerin çıkışları birbirinden ayrı kalacaktır. Böylece aynı akım koşulunda biaslı ve biassız ölçüm karşılaştırılacaktır.
- Önce bias hattı SCT bağlı değilken multimetre ve osiloskopla incelenecek; ardından iki SCT yüksüz durumda kontrol edilecektir.
- İlk karşılaştırmalarda sıfır düzeltmesi ve kalibrasyon katsayısı uygulanmadan ham davranış incelenecek. Yüksüz taban değerinin sıfırlanmasının gerekip gerekmediği ve katsayı ihtiyacı ayrıca değerlendirilecektir.
- Deney henüz yapılmadı; bu kayıt deney düzenini ve planını tanımlar, ölçüm sonucu veya bias/sıfırlama/katsayı kararı içermez.
- Teknik deney planı: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/GOREV.md`.

## İlerleme kuralı

Bir görev tamamlandığında sonucu kendi görev klasörüne kaydedilir. Ardından aynı modülün altında bir sonraki görev açılır ve bu dosyadaki durum güncellenir. Modüller arası geçiş, ilgili modülün hedefi ve hazır olma durumuna göre yapılır.


## Modül 1 için kaydedilen karar

- Modül 1, PREBERO/README.md içinde tanımlanmış genel bias orta nokta yapısının fiziksel olarak uygulanmış örneğidir; şebeke karakterinde gerilimi bias girişine aktarmak için kullanılır. Bias standardının kaynağı README.md'dir.
- Modül 1 mevcut, eski fiziksel yapıdır; imalatı tamamlanmıştır. Kapalı kutu içindedir ve bağlantıları soketlidir.
- Modül 1'in önceki imalat multimetre ölçümleri kendi imalat kaydında korunur.
- Masaüstü ESP ile yürütülen sinyal/akım deneyleri Modül 2 kapsamındadır. Modül 1 bu deneylerde bias gerilimi sağlayan donanım olarak kullanılabilir.
- Modül 1 için yeni imalat veya yeniden kurulum görevi açık değildir.
