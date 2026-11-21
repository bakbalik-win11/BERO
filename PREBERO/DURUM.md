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

## Modül 2 – güncel çalışma

- **Aktif modül:** Modül 2 – Masaüstü 4 Kanal / Akım Testleri
- **Aktif görev:** MOD2-GRV001 – Akım davranışı ve katsayı çalışmaları
- **Fiziksel ADC:** ADS1115 **No.10**, I²C 0x48.
- **Son deneme durumu:** 2026-11-21 tarihli iki kanallı deneme, kullanıcının bildirdiği bağlantı sorunu nedeniyle geçersiz kabul edildi. Deney baştan kurulacak.
- **Ölçüm kaydı:** A2-A3 çıktısı yaklaşık 0.494 A seviyesinden 1.357 A'ya yükseldi; bu değerler bias/biassız karşılaştırma veya kalibrasyon verisi olarak kullanılmayacak.
- **Kod koruma:** Mevcut çalışan tek kanallı V1.1 YAML değiştirilmeyecek. İki kanallı denemede kullanılan tam YAML kaynak dosyası henüz depoda yok; logdan tahmin edilerek oluşturulmayacak.
- **Sonraki adım:** Bağlantı düzenini baştan doğrulayıp deneyi yeniden kurmak. Yeni denemede kullanılacak gerçek YAML ayrı sürüm olarak kaydedilecek; ardından log ve yorum aynı sürümün altında tutulacak.
- **Ayrıntılı kayıt:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/ADS1115-IKILI-OKUMA-BAGLANTI-HATALI-2026-11-21.md`.

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


## 2026-11-21 – Aktif deney açıldı: ADS1115 biaslı / biassız ham okuma

- **Görev:** MOD2-GRV001.
- **Durum:** Deney açıldı; fiziksel bağlantı ve ölçüm henüz yapılmadı.
- **Düzen:** ADS1115 No. 1; SCT No. 1 A0-A1 biaslı, SCT No. 2 A2-A3 biassız. İki SCT aynı faz iletkenini aynı yönde ölçecek.
- **Tek değişken:** Biaslı kolda SCT dönüş ucu 1,65 V bias orta noktasına ve A1'e bağlı; biassız kolda SCT uçları doğrudan A2-A3 arasında.
- **Koruma:** Mevcut çalışan akım ölçüm kodu değişmeyecek. İlk karşılaştırmada RMS/akım dönüşümü, katsayı, sıfır düzeltmesi ve filtre yok.
- **Güvenlik kapısı:** Biassız A2/A3 girişleri bağlanmadan önce her pinin GND'ye göre mutlak gerilimi ve ADS1115 giriş sınırları doğrulanacak.
- **Başlangıç koşulu:** Kullanıcı yaklaşık iki saat ara verecek. Döndüğünde önce fiziksel bağlantı ve gerilim kontrolleri yapılacak; ardından deney başlatılacak.
- **Teknik ayrıntı:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/GOREV.md` içindeki 2026-11-21 deney açılış kaydı.


## 2026-11-21 – MOD2-GRV001: ADS1115 deneyi yeniden başlatılacak

- Önceki iki kanallı okuma denemesi bağlantı sorunu nedeniyle geçersiz kabul edildi.
- A2-A3 yükselen akım değerleri karşılaştırma veya kalibrasyon verisi olarak kullanılmayacak.
- Bu kurulumdaki fiziksel ADC **ADS1115 No.10** olarak izlenecek.
- Mevcut çalışan tek kanallı V1.1 YAML korunmuştur; üzerine yazılmamıştır.
- İki kanallı denemede kullanılan tam YAML kaynak dosyası mevcut kayıtta bulunmadığından logdan tahmin edilerek üretilmeyecek. Gerçek YAML temin edildiğinde ayrı sürüm olarak kaydedilecek.
- **Sonraki adım:** Bağlantı düzeni baştan kontrol edilerek deney yeniden kurulacak. Yeni deneme kodu gerçek kullanılan YAML üzerinden arşivlenecek.
- Ayrıntılı kayıt: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/ADS1115-IKILI-OKUMA-BAGLANTI-HATALI-2026-11-21.md`.


- Kullanıcının sağladığı iki kanallı deneme YAML'i, değiştirilmeden `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/MOD2-GRV001_V1.1_IKI-KANAL-DENEY.yaml` yoluna arşivlendi.
- Önceden bulunan tek kanallı V1.1 YAML dosyası korunmuştur; üzerine yazılmamıştır.
- İki kanallı YAML henüz yeniden derlenmiş veya test edilmiş değildir. Yeniden başlatmada kullanılacak yapılandırma açıkça seçilecek ve yeni test kaydı ayrı tutulacaktır.


## 2026-11-21 – MOD2-GRV001 bias karşılaştırması: ilk veri kaydedildi

- Kullanıcının teyit ettiği gerçek bağlantı: **A0–A1 bias yok; A2–A3 bias var.**
- ESP32D2 / ADS1115 No.10 iki kanallı logundan 109'ar yayın örneği çıkarılarak CSV'ye kaydedildi.
- HA history CSV'den 183'er SCT kaydı ve 13 PZEM akım kaydı analiz edildi; 13 PZEM örneği iki SCT kanalıyla ±2 saniye içinde eşleştirildi.
- İlk veri setinde A2–A3 biaslı kolun ortalaması daha yüksek ve PZEM'e daha yakındır. Ancak iki ayrı SCT sensörü kullanıldığı için bu fark yalnızca bias etkisine bağlanamaz.
- Değişim katsayıları iki kanalda yaklaşık %1.86; bu kayıt bias'ın gürültüyü azalttığını göstermiyor.
- Yeni kalibrasyon katsayısı çıkarılmadı; mevcut katsayı değiştirilmedi.
- **Sıradaki adım:** Bias bağlantısını A0–A1'e taşıyıp A2–A3'ü biassız bırakmak; SCT'lerin konumunu/yönünü, yükü ve yazılımı sabit tutarak çapraz deney yapmak.
- Veriler ve teknik yorum: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/LOG/` ve `V1.1/RAPOR/V1.1-BIAS-KARSILASTIRMA-2026-11-21.md`.
- Bu kayıt ilk karşılaştırma aşamasının arşivlendiğini gösterir; çapraz deney ve görev tamamlanmış değildir.


## 2026-11-21 – Aktif deney: bias kanal çapraz deneyi

- **Görev:** MOD2-GRV001.
- **Durum:** Yeni deney açıldı; ölçüm bekleniyor.
- **Fiziksel ADC:** ADS1115 No.10, I²C 0x48; ESP32D2.
- **Yeni bağlantı:** A0–A1 biaslı; A2–A3 biassız. İlk deneyde bunun tersi uygulanmıştı.
- **Kod:** Mevcut iki kanallı YAML aynen kullanılacak; kod değişikliği yapılmadı. Tek kanallı V1.1 korunuyor.
- **Deney kaydı:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/BIAS-KANAL-CAPRAZ-DENEY-2026-11-21.md`.
- Fiziksel bağlantı/gerilim kontrolleri ve yeni log/CSV henüz yok; deney sonucu çıkarılmadı.
