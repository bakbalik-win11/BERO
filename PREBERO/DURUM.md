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

- Mevcut çalışan akım ölçüm kodu korunacaktır; bu kod değiştirilmeyecek.
- Güncel deney hedefi, **ADS1115 No. 1 ile biaslı/biassız ham okuma davranışını karşılaştırmaktır**. SCT doğruluğu, dalga biçimi ve akım katsayısı bu deneyin hedefi değildir.
- Planlanan kanal düzeni: **SCT013 No. 1 → A0–A1 (biaslı)**; **SCT013 No. 2 → A2–A3 (biassız)**.
- İki SCT aynı faz iletkenini aynı yönde ölçecek; çıkışları birbirinden ayrı kalacaktır.
- İlk karşılaştırmada RMS/akım dönüşümü, kalibrasyon katsayısı, sıfır düzeltmesi ve filtre uygulanmayacaktır.
- Osiloskopla SCT sinyalini karşılaştırma çalışması durdurulmuştur. Osiloskop bu deneyin devamı için gerekmeyecektir.
- Biassız kolun bağlantısı, A2 ve A3 pinlerinin GND'ye göre mutlak gerilimleri ve ADS1115 giriş sınırları doğrulanmadan yapılmayacaktır. Diferansiyel ölçüm mutlak giriş sınırlarını ortadan kaldırmaz.
- Deney henüz yapılmamıştır. Kullanıcı hazır olduğunda önce bağlantı topolojisi doğrulanacak, ardından ayrı deney YAML'i hazırlanacaktır.
- Teknik kayıt: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/GOREV.md`.

## İlerleme kuralı

Bir görev tamamlandığında sonucu kendi görev klasörüne kaydedilir. Ardından aynı modülün altında bir sonraki görev açılır ve bu dosyadaki durum güncellenir. Modüller arası geçiş, ilgili modülün hedefi ve hazır olma durumuna göre yapılır.


## Modül 1 için kaydedilen karar

- Modül 1, PREBERO/README.md içinde tanımlanmış genel bias orta nokta yapısının fiziksel olarak uygulanmış örneğidir; şebeke karakterinde gerilimi bias girişine aktarmak için kullanılır. Bias standardının kaynağı README.md'dir.
- Modül 1 mevcut, eski fiziksel yapıdır; imalatı tamamlanmıştır. Kapalı kutu içindedir ve bağlantıları soketlidir.
- Modül 1'in önceki imalat multimetre ölçümleri kendi imalat kaydında korunur.
- Masaüstü ESP ile yürütülen sinyal/akım deneyleri Modül 2 kapsamındadır. Modül 1 bu deneylerde bias gerilimi sağlayan donanım olarak kullanılabilir.
- Modül 1 için yeni imalat veya yeniden kurulum görevi açık değildir.


## 2026-11-21 – Güncel ilerleme: ADS1115 ham okuma sırada

- Bias bağlı osiloskop yük kademeleri tamamlandı: 42 W, 57 W, 100 W ve 150 W; her yükte altı Single Vrms ölçümü alındı. Yüksüz altı ölçüm ayrı kayıt olarak korunuyor.
- Vrms ortalamaları: 42 W = 6.5417 mV; 57 W = 9.2983 mV; 100 W = 16.5700 mV; 150 W = 22.8383 mV.
- 100 W ve 150 W için Vrms, Avg, Vp-p, Vmax ve Vmin alanları altı Single boyunca raporlandı. 42 W ve 57 W için yalnızca Vrms serisi yapılandırılmıştır.
- Ayrıntılı rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/TESTLER/OSILOSKOP-YUK-KADEMELERI-BIAS-2026-11-21.md`.
- **Sıradaki adım:** ADS1115 No. 1 ile A0-A1 ham diferansiyel gerilim okuması. Aynı SCT, bias ve yük koşulları korunarak ADS1115 verisi osiloskopla karşılaştırılacak. İlk testte RMS/akım dönüşümü, katsayı, sıfır düzeltmesi ve filtre uygulanmayacak.
- ADS1115 ham okuma ve karşılaştırma henüz yapılmadı; osiloskop sonuçları ADS1115 performansını doğrulamaz.


## 2026-11-21 – Kullanıcı kararı: osiloskop karşılaştırması durduruldu

Mevcut çalışan akım ölçüm kodu korunacak. Yeni çalışma, kullanıcı hazır olduğunda ADS1115 No. 1 üzerinde A0–A1 biaslı ve A2–A3 biassız kolların ham okuma davranışını karşılaştırmak olacak. Osiloskop kullanılmayacak. Deney henüz başlamadı; biassız giriş bağlantısı mutlak pin gerilimleri ve ADS1115 sınırları doğrulanmadan yapılmayacak. Ayrıntı MOD2-GRV001 görev kaydına işlendi.
