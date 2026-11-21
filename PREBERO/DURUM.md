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
- **Önceki geçersiz deneme:** 2026-11-21 tarihli ilk iki kanallı denemede bağlantı sorunu nedeniyle A2-A3'ün 0.494 A'dan 1.357 A'ya yükseldiği log geçersiz kabul edildi; bu değerler bias karşılaştırması veya kalibrasyon verisi değildir.
- **Sonraki geçerli çalışmalar:** Aynı iki kanallı YAML ve K=27.59 ile iki bias/biassız karşılaştırma yapıldı. İlk deneyde A0-A1 biassız / A2-A3 biaslı; ikinci çapraz deneyde A0-A1 biaslı / A2-A3 biassızdı. Her iki deneyde de yüksek ortalama biaslı kola geçti.
- **Kod koruma:** Mevcut tek kanallı V1.1 ve kullanılan iki kanallı YAML değiştirilmeyecek; üçüncü tekrar aynı iki kanallı YAML ile yapılacak.
- **Kaynak veri:** İkinci deneyin 27 satırlık PZEM/SCT eşleştirme CSV'si ve raporu depoda bulunur. Kullanıcının sağladığı 900 satırlık `history (9).csv` ham kaynak dosyasının birebir kopyası GitHub'a yüklenmemiştir.
- **Güncel sonraki adım:** Üçüncü çapraz tekrar: A0-A1 biassız, A2-A3 biaslı; bias beslemesi Modül 1'de kalacak. Aynı SCT'ler, konum/yön, yük, ESP32D2, ADS1115 No.10, YAML ve K=27.59 korunacak.
- **Ayrıntılı kayıt:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/BIAS-KANAL-TEKRAR-CAPRAZ-DENEY-2026-11-21.md`.

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

## 2026-11-21 – Bias kanal çapraz deneyi: PZEM verisi alındı

- **Durum:** Çapraz deneyin PZEM içeren HA CSV analizi tamamlandı.
- **Fiziksel ADC:** ADS1115 No.10, I²C 0x48; ESP32D2.
- **Bağlantı:** A0–A1 biaslı, A2–A3 biassız.
- **Bias beslemesi:** Modül 1.
- **Kod:** Mevcut iki kanallı V1.1 YAML değişmedi; K=27.59 korundu.
- **Sonuç özeti:** A0–A1 biaslı 0.470006 A; A2–A3 biassız 0.457269 A; PZEM 0.469667 A. ±2 saniye eşleştirilmiş MAPE biaslı kanalda %1.275, biassız kanalda %3.168.
- İlk deneyde bias A2–A3'teyken yüksek ortalama A2–A3'teydi; çapraz deneyde bias A0–A1'e taşınınca yüksek ortalama A0–A1'e geçti. Biasın ölçüm sonucunu etkilediği hipotezi destekleniyor.
- Bu veri tek bir çalışma bölgesini (~0.47 A / 108 W) kapsar; akım arttıkça davranış ve tek katsayının yeterliliği henüz belirlenmedi. Gürültü azalması da iki deneyle kesinleşmedi.
- **Sıradaki adım:** Aynı düzen ve kodla biası ESP kartından besleyerek denemek; ardından düşük/orta/yüksek akım seviyelerini karşılaştırmak.
- **Rapor:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/RAPOR/V1.1-BIAS-KANAL-CAPRAZ-2026-11-21.md`.
- **Görev durumu:** MOD2-GRV001 açık; tamamlanmadı.



## 2026-11-21 – 100 W bias katkısı üçüncü çapraz tekrar

- **Görev:** MOD2-GRV001.
- **Durum:** Üçüncü çapraz deneyin HA verisi analiz edildi; üçlü 100 W bias test serisi kapatıldı.
- **Amaç:** İlk iki deneyde ölçüm ortalaması farkının bias bağlantısını takip ettiği bulgusunu üçüncü bir tersleme ile tekrar etmek.
- **Bağlantı:** A0–A1 biassız; A2–A3 biaslı (ilk deneydeki eşleme).
- **Sabitler:** ADS1115 No.10, ESP32D2, aynı iki SCT, aynı faz/yön/konum, mevcut iki kanallı YAML ve K=27.59. Kod değişmeyecek.
- **Bias kaynağı:** Modül 1 olarak kalacak. ESP32 kartından bias beslemesi ayrı bir sonraki deneydir; bu deneyle karıştırılmayacak.
- **Değerlendirme:** Biaslı kolun ölçüm ortalaması, PZEM'e göre fark/MAPE, standart sapma ve CV birlikte incelenecek. PZEM ground truth değildir.
- **Deney planı:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/BIAS-KANAL-TEKRAR-CAPRAZ-DENEY-2026-11-21.md`.
- **Sonuç:** Üçüncü tekrarın verisi analiz edildi. Üç testin tamamında biaslı kanal başarılı bulundu; bu çalışma noktası için bias katkısı tespit edildi.


## 2026-11-21 – Bias katkısı üçüncü çapraz tekrar: HA verisi analiz edildi

- **Durum:** Üçüncü deneyin HA CSV verisi alındı, ham hali ve PZEM eşleştirmesi depoya kaydedildi; rapor hazırlandı.
- **Veri:** 199 A0–A1, 199 A2–A3, 15 PZEM akım örneği; Türkiye saatiyle 21:51:00–21:54:17.
- **Bağlantı eşlemesi:** A0–A1 biassız, A2–A3 biaslı. Kullanıcı üç testte de biaslı kanalın başarılı olduğunu teyit ederek seriyi kapattı.
- **Ortalama akımlar:** A0–A1 0.459638 A; A2–A3 0.472490 A; PZEM 0.469267 A.
- **PZEM ±2 s MAPE:** A0–A1 %2.508; A2–A3 %1.819.
- **CV:** A0–A1 %1.871; A2–A3 %2.138. Biaslı kolun değişkenliği bu deneyde daha yüksek; biasın gürültüyü azalttığı sonucuna varılamaz.
- **Üç deneyin özeti:** Her üçünde de planlanan biaslı kolun ortalaması daha yüksek çıktı. Kanal çaprazlamalarıyla birlikte bu örüntü biasın yaklaşık 0.47 A bölgesindeki ölçüm ortalamasına pozitif katkı yaptığı hipotezini güçlendiriyor. Üçüncü deney de biaslı kanal lehine sonuçlandı; kullanıcı üçlü test serisini kapattı. PZEM ground truth değildir; mutlak doğruluk iddiası yoktur.
- **Kalibrasyon:** K=27.59 değişmedi; yeni katsayı üretilmedi.
- **Kaynak sınırı:** Ayrı ESPHome logu bu veri paketinde yoktur; analiz HA CSV'ye dayanır.
- **Dosyalar:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/LOG/V1.1-BIAS-KANAL-TEKRAR-HA-KAYNAK-2026-11-21.csv`, `.../V1.1-BIAS-KANAL-TEKRAR-PZEM-ESLESTIRME-2026-11-21.csv`, `.../V1.1/RAPOR/V1.1-BIAS-KANAL-TEKRAR-2026-11-21.md`.
- **Görev:** MOD2-GRV001 açık; tamamlanmadı.


## 2026-11-21 – 100 W bias kanal çapraz testi: üç tekrar sonunda kapanış

- **Durum:** 100 W nominal yük / yaklaşık 0.47 A çalışma noktasındaki üç çapraz test tamamlandı ve kapatıldı.
- **Tespit:** Üç testin tamamında biaslı kanal, biassız kanala göre daha başarılı sonuç verdi; biaslı kolun ortalaması daha yüksek ve PZEM karşılaştırmasına göre MAPE değeri daha düşüktür.
- **Biaslı / biassiz MAPE:** 1. test %1.016 / %3.262; 2. test %1.275 / %3.168; 3. test %1.819 / %2.508.
- **Kanal çaprazlaması:** 1. ve 3. testte bias A2–A3; 2. testte bias A0–A1 kanalındaydı. İlk iki çaprazlamada yüksek ortalamanın biasla birlikte kanal değiştirmesi bias katkısını destekler.
- **Karar:** Yaklaşık 0.47 A çalışma noktasında biasın ölçüm sonucuna olumlu katkısı tespit olarak kaydedildi.
- **Sınırlar:** PZEM karşılaştırma referansıdır, ground truth değildir. Biasın gürültüyü azalttığı gösterilmedi; tüm akım aralığına genelleme yapılmaz. K=27.59 korunmuştur.
- **Görev:** Bu 100 W bias çapraz test serisi kapatıldı; MOD2-GRV001'in tamamı açık kalır.
- **Rapor:** PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/RAPOR/V1.1-BIAS-KANAL-TEKRAR-2026-11-21.md.


## 2026-11-21 – Ek tespit: Biaslı kanalın boşta spike davranışı

- Kullanıcının Home Assistant grafiğinde yük altında (~0.46–0.48 A) A0–A1 ve A2–A3 okumaları PZEM'e yakın seyretmektedir.
- Yük kesildiğinde PZEM sıfıra iner; A0–A1 biassız kanal sıfıra yakın ve daha sakin görünürken A2–A3 biaslı kanalda pozitif spike'lar görülür.
- Yük yeniden geldiğinde (~0.19 A) iki ADS1115 kanalı yaklaşık 0.189–0.190 A, PZEM yaklaşık 0.188 A gösterir.
- **Tespit:** Bias yük altında PZEM karşılaştırmasına olumlu katkı sağlayabilir; ancak sistem boşta biaslı kanalda daha fazla spike gözlenmiştir.
- **Kanıt sınırı:** Bu, ekran görüntüsünden yapılan nitel gözlemdir. Ham CSV ve nicel spike istatistiği yoktur; spike oranı/genliği henüz ölçülmüş değildir.
- **Takip:** Boşta uzun süreli kayıtla iki kanalın spike sayısı, tepe genliği, standart sapması ve eşik üstü olay sıklığı ayrı karşılaştırılmalıdır.
- Günlük ayrıntı: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/RAPOR/GUN-KAPANIS-2026-11-21.md`.

## 2026-11-21 – 15 W biaslı / biassız ADS1115 karşılaştırması

- Tek nominal 15 W ampul ile yapılan oturum kapatıldı.
- A0–A1 biassız medyan 0.058814 A; A2–A3 biaslı medyan 0.060014 A.
- PZEM akımı yalnızca tek örnek (0.065 A); biaslı kanalın medyanı bu örneğe daha yakındır. PZEM güç ortalaması 14.839 W.
- Biaslı A2–A3 kanalında 0.516451 A tekil spike ve yüksek standart sapma (0.030700 A) görüldü. Spike kararlılık açısından olumsuz bulgudur.
- **Tespit:** Biaslı kanalın ölçüm seviyesi PZEM'e daha yakın görünmektedir; buna karşılık spike davranışı vardır. Gürültü/kararlılık iyileşmesi iddia edilmez.
- Sonuç tek deneyle sınırlıdır. PZEM ground truth değildir; K=27.59 ve YAML değişmedi.
- Ayrıntı: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/RAPOR/V1.1-15W-BIAS-KANAL-TESTI-2026-11-21.md`.