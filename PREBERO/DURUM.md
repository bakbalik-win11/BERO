# PREBERO – Durum ve çalışma akışı

> **Güncellik notu (2026-11-22):** Bu dosyanın aşağıdaki eski tarihli kayıtları deney geçmişidir. Birbiriyle çelişen eski “sıradaki adım” ve “aktif bağlantı” ifadeleri yerine, bu bölümdeki güncel durum esas alınır.

## Yetkili güncel durum – 2026-11-22

- **Modül 2 / MOD2-GRV001:** KAPANDI. Masaüstü prototipin geliştirme, geniş yük aralığı ve kombinasyon testleri tamamlandı; V1.6 tek fonksiyon kalibrasyon modeli referans olarak kabul edildi. Prototip, Modül 3 ve Modül 4'teki gerçek cihaz çalışmalarına teknik zemin oluşturdu.
- **Mevcut referans ölçüm yolu:** ESP32D2 + ADS1115 No.10 (I²C 0x48) + SCT013 30A/1V, A0–A1 diferansiyel; GPIO21 SDA, GPIO22 SCL; 3.3 V besleme ve ortak GND.
- **Referans kalibrasyon modeli:** K(x)=26.89+5.39·exp(-x/0.882); YAML'da K=27.59 baz ölçeği kullanılır ve Home Assistant yayın eşiği 30 mA'dir. V1.6 YAML ve doğrulama raporu kendi sürüm klasöründedir.
- **Sıfır yayınlama:** V1.2 yüksüz → yük → yeniden yüksüz geçişi logla doğrulandı (0.000 A → yaklaşık 0.600–0.604 A → 0.000 A). Bu, kalibrasyon doğruluğu kanıtı değildir.
- **20 mA filtre:** V1.3 derlendi/çalıştırıldı; kullanıcı gece boyu gözlemleyip yeterli buldu ve işi kapattı. Sayısal gece CSV/logu yok; performans metriği iddia edilmiyor. Rapor: `V1.3/RAPOR/V1.3-20MA-FILTRE-DERLEME-VE-GECE-GOZLEMI-2026-11-22.md`.
- **Bias deneyleri:** Önceki biaslı/biassız testler tarihsel veri olarak korunuyor. Yaklaşık 0.47 A ve bazı yüklerde biaslı kolun PZEM'e daha yakın olduğu görüldü; yüksüz spike ve kararlılık sorunları da kaydedildi. Yeni tasarımda bias tercih edilmeyecek.
- **Kalibrasyon kararı:** Önceki 1.5 A altı/üstü iki katsayılı ve parçalı geçiş planı V1.6 tam aralık tek fonksiyon modeliyle kapatıldı. Eski plan tarihsel kayıt olarak korunur; aktif gereksinim değildir. PZEM yalnızca karşılaştırma referansıdır.
- **Modül 3 / MOD3-AKM001:** 2026-11-22 tarihinde kapatıldı. Amaç, Modül 2'den devralınan V1.6 akım kodunu gerçek çamaşır makinesinde uzun pamuklu program boyunca test etmekti. Yaklaşık 78 dakikalık kayıt alındı; V1.6 değiştirilmedi. Isıtma bloğında PZEM'e yakın takip, sonraki düşük akım bölümlerinde pozitif fark gözlendi. Farkın PF kaynaklı olduğu kanıtlanmadı. Ayrıntı: `PREBERO/MODUL-3-CAMASIR-MAKINESI/GOREVLER/MOD3-AKM001/RAPOR/MOD3-AKM001-V1.6-UZUN-PAMUKLU-SAHA-TESTI-2026-11-22.md`.
- **Modül 3/4 imalat öncesi tasarım kapısı:** SCT013 akım + MAX4466 ses + MPU6050 titreşim için ortak zaman pencereli veri toplama mimarisi taslak olarak kaydedildi. Sensörler kendi örnekleme hızlarında çalışacak, özellik özetleri ortak 1 saniyelik slotta birleştirilecek. Örnekleme hızları, ADC/pin planı, zamanlama, veri şeması ve kaynak yükü netleşmeden Modül 3 veya 4 imalatına başlanmayacak. ZMPT101B/PF bu taslağın zorunlu parçası değildir. Ayrıntı: `PREBERO/ORTAK-MIMARI/MODUL-3-4-ORTAK-ZAMAN-PENCERELI-VERI-TOPLAMA-MIMARISI.md`.
- **Mevcut proje önceliği:** Modül 3 (çamaşır makinesi) ve Modül 4 (bulaşık makinesi) donanımlarını imal etmek, kaba yazılım taslaklarını geliştirmek ve gerçek cihazlardan veri toplamaya başlamak. Akım ölçüm altyapısı Modül 2'den hazır temel olarak devralınır; ses ve titreşim kanalları eklenecektir.
- **İleriye dönük fikir – aktif hedef değil:** İleride Modül 2'nin masaüstü akım ölçüm yaklaşımı, ana panoda PZEM ile birlikte kullanılabilir. Bu fikir şimdiki çalışma kapsamına alınmamıştır; Modül 3 ve 4'ün imalatı ve veri toplama hedeflerini etkilemez.
- **Modül 2 açık işi:** MOD2-GRV001 kapalıdır; ek masaüstü yük testi veya uzun süreli gözlem yapılmayacaktır. PF araştırması ayrı ve isteğe bağlıdır.
- **Modül 2'nin modül 3–4'e devrettiği akım altyapısı:** Masaüstü prototipte SCT013 + ADS1115 + ESP32D2 ölçüm yolu geliştirildi; katsayı çalışması iyileştirilip V1.6 tek fonksiyon modeli referans olarak belirlendi. Farklı ev yükleri ve kombinasyonlarıyla geniş aralıkta denendi. Bu çalışma MOD2-GRV001'in kapanış çıktısıdır; gerçek cihaz uygulaması Modül 3 ve 4'te yapılacaktır. PZEM karşılaştırma referansıdır, ground truth değildir.

## Deney geçmişi – kısa durum dizini

Her madde deneyin sonucunu bir-iki cümlede özetler; ayrıntılı veri ve yorum ilgili rapor/CSV/YAML yolundadır.

- **2026-11-21 – Osiloskop yük kademeleri:** Biaslı SCT sinyalinde yüksüz, 42, 57, 100 ve 150 W kademelerinde ölçüm alındı; Vrms yükle arttı. Bu çalışma ADS1115 akım ölçümünü veya kalibrasyonu doğrulamadı. Ayrıntı: `TESTLER/OSILOSKOP-YUK-KADEMELERI-BIAS-2026-11-21.md`.
- **2026-11-21 – İlk iki kanallı ADS1115 denemesi:** Bağlantı sorunu nedeniyle geçersiz sayıldı; yükselen A2–A3 değerleri veri/katsayı hesabında kullanılmadı. Ayrıntı: `DENEYLER/ADS1115-IKILI-OKUMA-BAGLANTI-HATALI-2026-11-21.md`.
- **2026-11-21 – Bias kanal karşılaştırmaları:** A0–A1/A2–A3 bias eşlemesi çaprazlandı; üç 100 W tekrarında biaslı kolun ortalaması daha yüksek ve PZEM'e göre MAPE'si daha düşük çıktı. Bu sonuç yaklaşık 0.47 A çalışma noktasıyla sınırlı; biasın gürültüyü azalttığı gösterilmedi.
- **2026-11-21 – Boşta bias spike gözlemi:** Biaslı kanalda yüksüz pozitif spike'lar ve 15 W deneyinde tekil yüksek spike kaydedildi. Ham uzun süreli nicel analiz bulunmadığından spike davranışının genel istatistiği çıkarılmadı.
- **2026-11-21 – Kettle / ESP32 kaynaklı bias denemeleri:** Farklı bias besleme ve kettle çalışma koşulları incelendi; ölçüm yakınlığı ile yüksüz kararlılık aynı yönde sonuç vermedi. Ayrıntılar ilgili tarihli deney raporlarında korunur.
- **2026-11-22 – 150 W A0–A1 tek kanal:** HA kaydı analiz edildi; ortalama 0.583896 A, CV %0.9343 ve PZEM akımıyla 40 eşleşmede MAPE %9.54 bulundu. Ayrı oturum olduğundan önceki çift kanal sonuçlarıyla farkın nedeni kesinleştirilmedi.
- **2026-11-22 – 150 W A2–A3 tek kanal:** Ortalama 0.589707 A, CV %1.1146 ve PZEM akımıyla 52 eşleşmede MAPE %8.510 bulundu. A0–A1 ile fark kanal üstünlüğü veya kök neden kanıtı değildir.
- **2026-11-22 – İki sabit katsayıyı ardışık çarpma önerisi:** K1×K2=K ise sonuç tek katsayıyla matematiksel olarak aynıdır; biasın yerine geçmez. Değerlendirme fiziksel deney yapılmadan kapatıldı.
- **2026-11-22 – V1.2 UNKNOWN→ZERO:** ESPHome logunda çevrimiçi sıfır yayını; kontrollü yükte 0.604/0.602/0.600 A ve yük kalkınca 0.000 A görüldü. İşlevsel geçiş doğrulandı; mutlak doğruluk doğrulanmadı.
- **2026-11-22 – V1.3 20 mA filtresi:** Kullanıcı derleme ve gece gözlemini doğruladı, filtreyi yeterli bularak kapattı. Sayısal gece verisi olmadığı için eşik çevresi/uzun dönem istatistiği yoktur.
- **2026-11-22 – İki bölgeli kalibrasyon kararı:** Ampuller (≤150 W) düşük bölge; ütü, tost makinesi ve kettle kaynatma modu yüksek bölge için seçildi. Veri toplama ve katsayı hesabı henüz yapılmadı.

---

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

## 2026-11-21 – Kettle testleri ve bias kararı

Kettle 1 (sıcaklık koruma modu) ve Kettle 2 (kaynatma modu) ayrı sabit çalışma koşulları olarak değerlendirildi. Kullanıcının kararıyla ek kettle testine devam edilmeyecek.

**Karar:** Mevcut deney dizisi kapsamında ADS1115 ölçüm yolunda bias gerekli kabul edildi. Kettle karşılaştırmalarında biaslı A2–A3 kanalının PZEM akım ortalamasına daha yakın sonuç verdiği değerlendirildi. Bu karar, biasın tüm çalışma koşullarında gürültüyü azalttığı anlamına gelmez.

**Sınırlar ve açık bulgular:**
- Boşta alınan CSV'de biaslı kanalda 0.030 A üzeri 128 örnek ve 0.10114 A maksimum görülmüştür; biassız kanalda 0.030 A üzeri örnek görülmemiştir.
- 15 W deneyinde biaslı kanalda 0.516451 A tekil spike kaydedilmiştir.
- Kettle sonuçlarında ölçüm yakınlığı bias lehine değerlendirilmiş olsa da değişkenlik/kararlılık her deneyde aynı yönde değildir.
- PZEM karşılaştırma referansıdır, ground truth değildir.
- 0.020 A altını sıfırlama yalnızca ileride tartışılacak aday eşiktir; uygulanmadı.
- K=27.59 ve çalışan YAML değiştirilmedi.
- Bu karar mevcut deneylerin kapsamındadır; tüm akım aralığı için mutlak doğruluk veya nihai devre tasarımı iddiası değildir.

**Kullanıcı kararı:** Daha fazla kettle testi gerekmiyor; bias kullanılmalı.

## 2026-11-21 – ESP32 kaynaklı bias + ortak GND deneyi AÇILDI

Yeni deneyde bias ESP32 kartının 3.3 V hattından sağlanacak; ESP32 GND, ADS1115 GND ve bias devresi GND ortaklanacak. Önceki Modül 1 bias deneylerinde bu ortak GND koşulu kullanılmamıştı; dolayısıyla bu yeni deneyde besleme kaynağı ve toprak referansı farkı birlikte değerlendirilecek.

Fiziksel bağlantı, direnç değerleri ve bias DC seviyesi henüz teyit edilmedi. Enerji verilmeden önce bağlantı ve ADS1115 mutlak giriş gerilimleri kontrol edilecek. K=27.59 ve çalışan YAML korunacak. Deney açık; henüz ölçüm sonucu yoktur.

Deney kaydı: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/ESP32-KAYNAKLI-BIAS-ORTAK-GND-2026-11-21.md`.

## 2026-11-21 – ESP32 kaynaklı bias / ortak GND: Kettle 2 kapatıldı

- ESP32 3.3 V kaynaklı yaklaşık 1.66 V bias ve ortak GND düzeniyle Kettle 2 (kaynatma modu) ölçümü analiz edildi.
- Analiz raporu: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/RAPOR/V1.1-ESP32-BIAS-KETTLE2-2026-11-21.md`.
- Sayısal özet CSV: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/LOG/V1.1-ESP32-BIAS-KETTLE2-OZET-2026-11-21.csv`.
- Kettle 2 analizinde A2–A3 ortalaması 6.83096 A, PZEM ortalaması 6.80079 A; ±2 saniye eşleştirmeli MAPE A2–A3 için %2.550, diğer SCT serisi için %2.801.
- Her iki SCT kanalında da belirgin dalgalanma gözlendi; dalgalanmanın kaynağı belirlenmedi. Biasın gürültüyü azalttığı iddia edilmez.
- **Karar:** ESP32 bias + ortak GND Kettle 2 deneyi kapatıldı. Basitleştirme kararını tamamlamak için aynı düzenle 100 W ve 15 W deneyleri sıradadır.
- K=27.59 ve firmware/YAML değiştirilmedi. PZEM karşılaştırma referansıdır, ground truth değildir.
- Ham kaynak `history (17)(1).csv` 430 satırdır; GitHub'a birebir ham kopyası yüklenmedi, sayısal özet CSV kaydedildi.


## 2026-11-21 – ESP32 bias / trafolu bias Kettle 2 karşılaştırması ve 100 W birlikte değerlendirme

- Kullanıcının sağladığı `history (16).csv` (trafolu 1,65 V bias) ve `history (17).csv` (ESP32 1,66 V bias) karşılaştırması ayrı rapor olarak kaydedildi.
- Kettle 2 A2–A3 PZEM sapması trafolu bias ile -%0,18 (-12,6 mA), ESP32 bias ile +%0,31 (+21,0 mA). Her iki sonuç da PZEM'e yakındır; ESP32 bias geçişinde ortalama doğruluk açısından olumsuz etki görülmemiştir.
- A2–A3 standart sapması 0,1323 A'dan 0,1906 A'ya yükselmiştir; anlık dalgalanma artmıştır. Kanal farkı 61,9 mA'dan 117,3 mA'ya çıkarken farkın standart sapması 142,3 mA'dan 88,9 mA'ya düşmüştür. Bu, kanal davranışının değiştiğini gösterir; gürültü iyileşmesi olarak genellenmez.
- Boşta pik aralıkları iki bias kaynağında benzerdir (0,014–0,101 A ve 0,014–0,110 A); bias kaynağını değiştirmek pikleri ortadan kaldırmamıştır.
- 100 W sınıfı ESP32 bias deneyinde A2–A3 MAPE %5,184, diğer SCT kolu %9,597 olmuştur. ESP32 biaslı kol daha yakın olsa da bu deneyde aynı yükte trafolu bias A/B karşılaştırması yoktur.
- **Genel değerlendirme:** Kettle 2 ve 100 W sonuçları ESP32 biasın bu iki çalışma noktasında kullanılabilir olduğunu ve ölçüm ortalamasında belirgin olumsuz etki göstermediğini destekler. Dalgalanma ve boşta pik sorunu çözülmüş değildir.
- Ayrıntılı rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/RAPOR/V1.1-ESP32-BIAS-KETTLE2-TRAFOLU-KARSILASTIRMA-VE-100W-DEGERLENDIRME-2026-11-21.md`.
- Kaynak sınırı: Kettle 2 history (16)/(17) karşılaştırma metrikleri kullanıcı tarafından sağlandı; CSV'ler bu kayıt sırasında yeniden işlenmedi. 100 W istatistikleri mevcut 100 W raporundan alındı.
- K=27.59 ve çalışan YAML/firmware korunmuştur.


## 2026-11-21 – ESP32 bias 15 W deneyi

- Kaynak: kullanıcı yüklemesi `history (19)(1).csv`, 604 satır.
- Kararlı SCT özeti için ilk 3 saniye çıkarıldı. Diğer SCT kanalı: ortalama 0.058321 A, medyan 0.058056 A, CV %3.611. A2–A3 ESP32 bias: ortalama 0.060924 A, medyan 0.060054 A, CV %6.276.
- PZEM akımında yalnızca 3 örnek vardır; ortalama 0.064333 A. ±2 saniye eşleştirmeli MAPE diğer SCT kanalı %8.900, A2–A3 %8.157. Örnek sayısı kesin doğruluk kararı için yetersizdir.
- A2–A3 maksimumu 0.080796 A; önceki 15 W oturumundaki 0.516451 A tekil spike tekrarlanmamıştır. Buna rağmen A2–A3 değişkenliği daha yüksektir.
- Önceki 15 W A2–A3 medyanı 0.060014 A, yeni ESP32 bias medyanı 0.060054 A; ölçüm seviyesi birbirine çok yakındır.
- Ortalama bazlı kaba katsayı yaklaşık 29.13 çıkar; PZEM akım örneği yalnızca üç olduğu için yeni katsayı kabul edilmemiştir.
- **Karar:** K=27.59 ve çalışan YAML/firmware korunur. Yeni katsayı uygulanmaz. ESP32 bias düşük akımda benzer medyan ölçüm seviyesini vermiş, ancak kararlılık iyileşmesi göstermemiştir.
- Rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/RAPOR/V1.1-ESP32-BIAS-15W-2026-11-21.md`.
- Sayısal özet: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/LOG/V1.1-ESP32-BIAS-15W-OZET-2026-11-21.csv`.
- Ham kaynak CSV bu commit kapsamında GitHub'a yüklenmedi; konuşmadaki kullanıcı dosyası kaynak olarak korunur.


## 2026-11-22 – İki aşamalı katsayı çarpımı önerisi kapatıldı

Kullanıcının mevcut katsayıyı iki sabit katsayıya ayırıp çarpma önerisi matematiksel olarak değerlendirildi. K1 × K2 = K olduğunda iki aşamalı çarpım mevcut tek katsayıyla aynıdır; tek başına biasın yerine geçmez ve ölçüm davranışını değiştirmez. Ayrı fiziksel/kalibrasyon anlamları tanımlanmadan iki katsayılı uygulama yapılmayacak.

- **Durum:** Önerinin matematiksel değerlendirmesi kapatıldı; fiziksel deney yapılmadı.
- **Korunanlar:** K=27.59, çalışan YAML/firmware ve mevcut bias bağlantısı değişmedi.
- **Kapsam:** Bu kapanış MOD2-GRV001 görevinin tamamlandığı anlamına gelmez.
- **Rapor:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/KATSAYI-IKI-ASAMALI-CARPIM-DEGERLENDIRMESI-2026-11-22.md`.


## 2026-11-22 – MOD2-GRV001: iki bölgeli kalibrasyon / bias tasarım kararı

Kullanıcı kararı: 1,5 A altı ve üstü için ayrı katsayılar çalışılacak. Yeni tasarımda bias devresi tercih edilmeyecek; daha sade analog ölçüm yolu izlenecek.

- **Durum:** Tasarım kararı kaydedildi; ölçüm ve katsayı kalibrasyonu henüz yapılmadı.
- **Korunanlar:** K=27.59, çalışan YAML ve firmware değişmedi.
- **Sıradaki iş:** Bias kullanılmayan bağlantıyı güvenli şekilde doğrulamak; 1,5 A altı ve üstünde birden fazla ölçüm noktası toplamak; sınır çevresini ayrıca test etmek.
- **Açık noktalar:** Tam 1,5 A sınırında katsayı seçimi ve bölge geçiş yöntemi.
- **Rapor:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/IKI-BOLGELI-KALIBRASYON-VE-BIAS-KARARI-2026-11-22.md`.


**Bir sonraki oturum:** Önce katsayıları bulma yöntemi planlanacak; test yükleri/noktaları, ölçüm ve eşleştirme süresi, tekrar sayısı, katsayı hesabı ve 1,5 A geçişi netleştirilecek. Bu planlama tamamlanmadan fiziksel bağlantı değişikliği veya ölçüm başlatılmayacak.


## 2026-11-22 – 42 W biassız ADS1115 No.10 deneyi

- Kaynak: kullanıcı CSV'si `42w ads-10.csv`, 501 satır.
- Kullanıcı teyidi: bias yok; 0,02 A filtreli son YAML kullanıldı (dosya adı/sürümü henüz kayda alınmadı).
- SCT (n=320) ortalama 0.153884 A, std. sapma 0.002587 A, CV %1.68.
- PZEM akım (n=14) ortalama 0.187714 A; PZEM güç (n=49) ortalama 42.4245 W.
- ±2 saniye zaman eşleştirmesi: 14 çift; eşleşmiş SCT ortalaması 0.154787 A; ön katsayı K≈33.46; eşleşmiş çift MAPE %17.55.
- PZEM güç kayıtları 42.0–42.9 W aralığında kalmıştır. SSR/BERO dijital OFF/ON kayıtları fiziksel yükün kesildiğini göstermediğinden veri dışlama nedeni yapılmadı.
- **Karar:** K=27.59 korunur; YAML değiştirilmez. K≈33.46 yalnızca ön sonuçtur; düşük bölge ortak katsayısı için diğer yüklerle birlikte değerlendirilecek.
- Ayrıntılı rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/42W-ADS1115-NO10-2026-11-22.md`.


## 2026-11-22 – 57 W dosyası: ADS1115 No.10 ön analizi

- Kaynak: kullanıcı CSV'si `57w ads-10.csv`, 378 satır.
- SCT n=246, ortalama 0.219276 A, std. sapma 0.001670 A, CV %0.762.
- PZEM akım n=17, ortalama 0.264588 A; PZEM güç n=40, ortalama 60.4575 W (59.9–60.9 W).
- ±2 saniye eşleştirme: 17 çift; eşleşmiş SCT ortalaması 0.218940 A; MAPE %17.25; ön katsayı K≈33.34.
- 42 W dosyasındaki ön katsayı K≈33.46; fark yaklaşık 0.12 (%0.36). Aynı bias/YAML/kanal koşulları teyit edilirse düşük akım bölgesi tutarlılığı lehine bulgudur.
- 57 W CSV'si bias, kanal ve YAML bilgisini doğrudan içermez. 42 W oturumundaki bias yok / 0,02 A filtreli YAML teyidinin devam ettiği varsayılmıştır; 57 W için ayrıca doğrulanmalıdır.
- **Karar:** K=27.59 ve YAML korunur. K≈33.34 ön sonuçtur; ortak katsayı henüz belirlenmez.
- Ayrıntılı rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/57W-ADS1115-NO10-2026-11-22.md`.


## 2026-11-22 – 100 W dosyası: ADS1115 No.10 ön analizi

- Kaynak: kullanıcı CSV'si `100w ads-10.csv`, 445 satır.
- SCT n=289, ortalama 0.418344 A, std. sapma 0.003318 A, CV %0.793.
- PZEM akım n=15, ortalama 0.469667 A; PZEM güç n=50, ortalama 107.472 W (106.7–108.3 W).
- ±2 saniye eşleştirme: 15 çift; eşleşmiş SCT ortalaması 0.419415 A; MAPE %10.70; ön katsayı K≈30.90.
- 42 W ve 57 W ön katsayıları sırasıyla ≈33.46 ve ≈33.34 iken 100 W ön katsayısı ≈30.90'dır. Tek ortak düşük bölge katsayısı henüz desteklenmiyor.
- 100 W CSV'si bias, kanal ve YAML dosya/sürümünü doğrudan tanımlamaz; bunlar ayrıca teyit edilmelidir. PZEM güç ortalaması nominal 100 W etiketinden yüksek, 107.47 W'tır.
- **Karar:** K=27.59 korunur; YAML değiştirilmez. K≈30.90 ön sonuçtur; ortak katsayı belirlenmez.
- Ayrıntılı rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/100W-ADS1115-NO10-2026-11-22.md`.


## 2026-11-22 – Son birleşik CSV analizi

- Kullanıcının sağladığı `150-42-57-100.csv` içindeki kararlı pencereler yeniden değerlendirildi: 42 W K≈33.58, 57 W K≈33.30, 100 W K≈30.65, 150 W K≈30.00.
- 100 W penceresinde A0–A1 ilk yaklaşık 230 saniyede ~0.4309 A, devamında ~0.4183 A seviyesinde; PZEM her iki bölümde ~0.470 A. Tek pencere K≈30.65 bu iki alt seviyeyi birleştiriyor.
- Bu sonuçlar yük bazlı ön katsayılardır. Bias ve YAML sürümü birleşik CSV'den teyit edilemedi. Tek ortak düşük bölge katsayısı seçilmedi; K=27.59 ve mevcut YAML korunuyor.
- Ayrıntı: `MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/150-42-57-100-BIRLESIK-KADEME-ANALIZI-2026-11-22.md`.


## 2026-11-22 – İleride PF etkisi araştırması planlandı

- Kullanıcı, mevcut akım kalibrasyonundan ayrı olarak trimpotlu faz kaydırma düzeneğiyle ileride PF etkisini araştırma fikrini onayladı.
- Mevcut kalibrasyonun kabul hedefi ±%4 hata zarfıdır; PF düzeltmesi mevcut fonksiyona eklenmeyecek.
- Trimpot devresinin gerçek topolojisi, faz kaydırma aralığı ve PF üzerindeki etkisi henüz doğrulanmadı; fiziksel deney yapılmadı.
- PF çalışması ayrı deney olarak, devre şeması ve güvenli ölçüm bağlantısı incelendikten sonra açılacak.
- Ayrıntı: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/ILERIDE-PF-ETKISI-TRIMPOT-DENEY-PLANI.md`.

 
## 2026-11-22 – İki bölgeli/parçalı kalibrasyon yaklaşımı kapatıldı; V1.6 tek fonksiyon referans alındı

Önceki tasarım planında 1,5 A altı ve üstü için ayrı katsayılar ve arada bölge geçişi öngörülmüştü. Bu yaklaşım, V1.6 tam aralık testleri sonrasında **uygulama adayı olmaktan çıkarıldı ve kapatıldı**.

Yerine, aynı ölçüm zincirinde 0,065–17,52 A aralığındaki karma yük verileriyle geliştirilen tek fonksiyon kabul edildi:

`K(x) = 26.89 + 5.39 × exp(-x / 0.882)`

V1.6 YAML bu fonksiyonu parçalı bölge seçimi olmadan uygular; 30 mA ve altını Home Assistant'ta 0.000 A yayımlar. V1.6 doğrulama raporu, seçilmiş kademe sonuçları, 23 kademelik genel grafik ve 1:1 karşılaştırma grafiği için esas kayıttır:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.6/RAPOR/V1.6-TAM-ARALIK-TEK-FONKSIYON-DOGRULAMA-2026-11-22.md`.

**Kapanış kararı ve sınırlar**
- İki bölgeli katsayı yöntemi, V1.6 tek fonksiyon modeliyle ikame edildiği için kapatıldı; eski plan ve deney kayıtları silinmedi.
- 1,5 A bölge sınırı ve parçalı geçiş mantığı artık aktif tasarım gereksinimi değildir.
- V1.6, ADS1115 No.10 + SCT013 30A/1V + ESP32D2 + A0–A1 ölçüm zinciri için referans kalibrasyon modeli olarak korunur.
- Yaklaşık 15 W noktası SCT013'ün pratik alt ölçüm sınırına yakın kabul edilir; bu nokta için eğri yeniden şekillendirilmeyecektir.
- Yaklaşık 60 W noktasındaki -%4,89 sapmanın nedeni kanıtlanmış değildir; yük/çalışma koşulu kontrol edilerek ayrıca tekrar edilebilir. Bu istisna formülün yeniden açılması için tek başına gerekçe değildir.
- PF=0,76 olan 20,4 W noktası ayrı PF araştırma konusudur; V1.6'ya PF düzeltmesi eklenmez.
- PZEM karşılaştırma referansıdır, ground truth değildir.
- Bu kapanış MOD2-GRV001 görevinin tamamlandığı anlamına gelmez. Modülün diğer donanım, bağlantı, güvenilirlik ve gerçek yük gözlemleri ayrı iş olarak sürebilir.


## 2026-11-22 – 60 W sapma tekrar testi iptal edildi

Kullanıcı kararıyla V1.6 doğrulama raporunda belirtilen yaklaşık 60 W / -%4,89 sapma için tekrar test yapılması hedefi iptal edildi. Bu sapmanın nedeni araştırılmayacak ve konu MOD2-GRV001'in açık iş listesinde tutulmayacaktır. Mevcut V1.6 kalibrasyon modeli değiştirilmez; tarihsel doğrulama raporundaki ölçüm ve o tarihteki değerlendirme silinmez. Diğer yük karakterlerinde ve uzun süreli kullanımda V1.6 davranışının gözlemlenmesi ayrı açık doğrulama konuları olarak kalır.


## 2026-11-22 – MOD2-GRV001 kapatıldı; Modül 3 ve 4 için zemin oluşturuldu

Kullanıcı kararıyla masaüstü prototip görevi tamamlandı ve kapatıldı. Prototip üzerinde SCT013 + ADS1115 + ESP32D2 ölçüm zinciri geliştirildi; geniş akım aralığında farklı ev yükleri ve yük kombinasyonları denendi; V1.6 tek fonksiyon kalibrasyon modeli referans olarak kabul edildi. 60 W sapma tekrar testi ve uzun süreli masaüstü gerçek kullanım gözlemi iptal edildi. Yeni yük kombinasyonu testi açılmayacak. Masaüstü prototipin görevi, Modül 3 (çamaşır makinesi) ve Modül 4 (bulaşık makinesi) gerçek cihaz izleme çalışmalarına teknik zemin hazırlamaktı; bu hazırlık görevi yerine getirdi. Çamaşır makinesi ve bulaşık makinesi üzerindeki uygulama/testler kendi modüllerinde yürütülecek; MOD2-GRV001'in açık işi olarak sayılmayacaktır.


## Modül 2'den Modül 3 ve 4'e teknik devir

Modül 2'nin masaüstü prototip çalışmasının hedefi, akım ölçüm yolunu geliştirmek ve katsayıyı iyileştirerek kullanılabilir bir referans modele ulaştırmaktı. Bu hedef yerine getirildi: SCT013 + ADS1115 + ESP32D2 ölçüm zinciri farklı ev yükleri ve kombinasyonlarıyla geniş aralıkta denendi; V1.6 tek fonksiyon kalibrasyon modeli referans kabul edildi. Böylece Modül 3 (çamaşır makinesi) ve Modül 4 (bulaşık makinesi) için akım ölçüm tarafının teknik zemini hazırlandı.

Modül 3 ve 4'te mevcut kaba yazılım taslakları geliştirilecek; akım verisine ek olarak ses ve titreşim gözlemleri sisteme dahil edilecek. Bu sensörlerin entegrasyonu ve gerçek cihaz üzerindeki davranışları henüz tamamlanmış/doğrulanmış kabul edilmez; kendi modül görevlerinde ele alınır. Akım ölçüm altyapısının hazırlanması Modül 2'nin tamamlanmış çıktısıdır.


## 2026-11-22 – Öncelik netleştirmesi: Modül 3 ve 4 imalatı ve veri toplama

Kullanıcı kararıyla mevcut ana hedef, Modül 3 çamaşır makinesi ve Modül 4 bulaşık makinesi donanımlarını imal etmek, mevcut kaba yazılım taslaklarını geliştirmek ve gerçek cihazlardan veri toplamaktır. Akım ölçüm tarafı Modül 2 tarafından hazırlanmış ve bu iki modüle temel olarak devredilmiştir. Modül 3 ve 4'te akım verisine ses ve titreşim gözlemleri eklenecektir.

Ana panoda PZEM ile birlikte akım ölçümü yapılması, Modül 2 yaklaşımının ileride değerlendirilebilecek olası kullanım alanıdır. Bu yalnızca gelecek fikridir; mevcut hedef, açık görev veya sıradaki iş değildir. Şimdiki çalışma odağı Modül 3 ve 4'ün imalatı ve veri toplamasıdır.
