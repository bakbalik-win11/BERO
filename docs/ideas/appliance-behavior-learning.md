# BERO — PREBERO Saha Deney Ortamı ve Cihaz Davranışını Öğrenme Fikri

**Durum:** Fikir / saha veri toplama ortamı. Henüz doğrulanmış deney sonuçları, kesin tasarım veya ürün kararı değildir.

## PREBERO kavramı

PREBERO, gerçek BERO sistemine geçmeden önce modüllerin gerçek ev ortamında yerleştirilip çalıştırılacağı, uzun süreli saha verisi ve deneyim kazanılacağı ilk ortamdır. Masaüstü testlerinden gerçek kullanım koşullarına geçişi temsil eder: cihazlar kendi ortamlarında çalışırken sensör verileri toplanır, sistemin sürekliliği ve davranışı gözlenir.

PREBERO'nun ilk saha çalışmasında üç modül bulunur. Üçü de verilerini Wi-Fi üzerinden Home Assistant'a aktarır. Bu, deney ve gözlem aşamasında kurulumu kolaylaştıran iletişim tercihidir. Gerçek BERO mimarisinde modüller arası haberleşme RS485 olarak planlanmaktadır.

## PREBERO modülleri

### Modül 4 — Çamaşır makinesi

Çamaşır makinesine sabitlenecek veri toplama modülü. Sensör yaklaşımı:
- SCT ile akım davranışı
- Mikrofon ile ses gözlemi
- Titreşim sensörü ile mekanik davranış gözlemi

PZEM kullanılmayacaktır. Bu modülün hedefi elektrik ölçümünü referansla karşılaştırmak değil, çamaşır makinesinin gerçek çalışma döngülerinde akım, ses ve titreşim örüntülerini uzun süreli gözlemlemektir.

### Modül 5 — Bulaşık makinesi

Modül 4 ile aynı sensör yaklaşımına sahip ikiz modül:
- SCT ile akım davranışı
- Mikrofon ile ses gözlemi
- Titreşim sensörü ile mekanik davranış gözlemi

PZEM kullanılmayacaktır. Bulaşık makinesinin kendi çalışma döngüleri ve davranış örüntüleri gerçek ortamda uzun süre gözlenecektir.

Modül 4 ve 5'ten alınan daha zengin (akım + ses + titreşim) veriler, cihaz davranışının incelenmesi ve öğrenme çalışmaları için kullanılacaktır.

### Modül 6 — Evin tek faz ana girişi

Ana panoda, tek fazlı evin toplam yükünü gözlemlemek üzere düşünülen modül:
- SCT akım sensörü
- ADS1115 analog-dijital dönüştürücü
- ESP32 mini
- PZEM ölçüm modülü

SCT tarafında BERO deneylerinde kullanılan 1,65 V orta nokta bias yaklaşımı ESP'nin 3,3 V hattından oluşturulabilir; mevcut bias devresi temel alınacaktır. Bu henüz saha testinde doğrulanmış bağlantı veya tasarım kararı değildir.

Modül 6'nın amaçları:
- Evin ana giriş toplam akımını gözlemlemek
- PZEM ile SCT ölçümlerini aynı ortamda karşılaştırmak
- PZEM üzerinden gerilim, güç ve enerji gibi ölçümleri izlemek
- SCT/ADS1115 tarafının yük değişimlerine ve akım davranışına verdiği yanıtı karşılaştırma verisi olarak toplamak

Modül 6, ana giriş yükünü gözlemleyen saha modülü olarak BERO ana ev panosu uygulamasına yönelik bir çalışma alanıdır.

## PREBERO haberleşmesi

- Modül 4, Modül 5 ve Modül 6: Wi-Fi üzerinden Home Assistant'a veri aktarımı.
- PREBERO'da Wi-Fi, saha deneylerini kurmak, izlemek ve geliştirmek için kullanılır.
- Gerçek BERO'da modüller arası haberleşme RS485 olarak planlanmaktadır.

## Araştırma hedefi

Modül 4 ve 5'te ses, titreşim ve akım verilerinden cihaz davranış örüntülerini öğrenmek; daha sonra yalnızca SCT/akım verisinin bu davranışları tanıma veya durum tahmini için ne ölçüde yeterli olabileceğini araştırmak.

## Araştırma ve veri çalışma yönü

1. Modül 4 ve 5'i cihazlara sabitleyerek gerçek çalışma koşullarında uzun süreli veri toplamak.
2. Modül 6 ile evin ana giriş toplam yükünü ve SCT/PZEM karşılaştırmasını gözlemek.
3. Verileri incelemek, düzenlemek ve analiz etmek için harici PC/Python kullanmak.
4. Cihaz çalışma davranışlarını ve olası aşamalarını veriler üzerinden incelemek.
5. Öğrenme ve tahmin yöntemlerini toplanan verilerle denemek.
6. Akım verisinin tek başına davranış tanıma veya durum tahminine ne kadar katkı sağlayabileceğini araştırmak.
7. Sonuçları doğrulamadan öğrenilmiş davranışların Modül 6 veya gerçek BERO'ya aktarılabilir olduğunu varsaymamak.

## Sınırlar ve açık noktalar

- PREBERO bir saha deney ortamıdır; henüz doğrulanmış sonuç veya ürün değildir.
- Modül 4 ve 5'te PZEM yoktur; SCT, ses ve titreşim davranış gözlemi içindir.
- Modül 6'da PZEM, SCT ölçümünü karşılaştırmak ve ana giriş yükünü izlemek için bulunur.
- Wi-Fi/HA PREBERO'nun deney iletişim yoludur; gerçek BERO iletişim yapısı RS485 olarak planlanmaktadır.
- Bu fikir arıza teşhisi veya güvenilir arıza tahmini iddiası içermez.
- Modüllerin sensör bağlantıları, örnekleme hızları, dosya/veri biçimleri, model türü ve alarm mantığı henüz kesinleşmemiştir.
- Elektrik panosuna montaj ve şebeke bağlantıları, güvenli izolasyon ve uygun koruma koşulları gerektirir.

Bu belge PREBERO'nun kavramını ve saha deneyi yönünü kaydetmek için hazırlanmıştır; uygulama ayrıntıları ve sonuçlar testlerle ayrıca belgelenecektir.


## Fikir — Merkezi canlı akım ekranı

PREBERO/BERO modüllerinin Home Assistant'a gönderdiği akım değerlerini, ayrı bir ekranlı ESP üzerinden tek noktada göstermek fikri.

- Ölçüm yapan üç ESP kendi ölçümünü yapmaya ve Home Assistant'a veri göndermeye devam eder.
- Ekranlı ESP ölçüm görevi üstlenmez; merkezi gösterim terminali olarak Home Assistant'taki değerleri alıp yayınlar.
- İlk hedef, üç modülün akım değerlerini tek ekranda canlı ve kolay okunur biçimde göstermektir.
- Bu ekran için ESP32-S3 ve 4,3 inç veya 7 inç ekran seçenekleri düşünülmektedir.
- Ekran ve arayüz çalışması acil bir uygulama değil; hobi kapsamında yavaş yavaş ele alınabilecek ayrı bir çalışma.
- İleride ekran düzeni, bağlantı durumu, toplam yük veya grafik gibi ek bilgiler değerlendirilebilir; bunlar şimdilik kesin kapsam değildir.

Fikir aşamasındadır. Ekran modeli, arayüz, veri alışverişi ve uygulama ayrıntıları henüz seçilmemiştir.


## Fikir — PREBERO masaüstü haberleşme ve ekran laboratuvarı

**Durum:** Olgunlaşmış deney fikri. Mimari yaklaşım belirginleşmiştir; donanım bağlantıları, yazılım ve deney sonuçları henüz doğrulanmamıştır.

PREBERO saha modülleri evde kendi görevlerini yürütürken, masa üzerinde ihtiyaç oldukça kurulup kaldırılabilecek bağımsız bir deney düzeneği hazırlanması düşünülmektedir. Düzenek sürekli çalışmak zorunda değildir. Deney konusu önceden belirlenir, bağlantılar kurulur, kod ve haberleşme sınanır; başarılı kod, örnek log ve sonuç yorumu depoda saklanır.

### Deney düzeneğinin ana bileşenleri

- Raspberry Pi 4 (8 GB): Home Assistant çalışma ortamı.
- Raspberry Pi'ye USB üzerinden bağlanan RS485 adaptörü.
- ESP32-S3, 4,3 inç ekranlı kart: ekran arayüzü ve iki bağımsız RS485 hattının yönetimi.
- Mikro ESP: basit sensörler, düğmeler ve dijital giriş/çıkış deneyleri.
- Bir veya daha fazla Modbus sensör / dijital giriş-çıkış modülü.
- ESP32-S3 kartının mevcut RS485 A/B bağlantısı: birinci hat.
- ESP32-S3 üzerindeki boş UART'a eklenecek ikinci RS485 transceiver: ikinci hat.

### İki bağımsız RS485 hattı ve roller

**Hat A — Ekran Master**
- ESP32-S3 ekran bu hatta Modbus Master olarak çalışır.
- Mikro ESP ve Modbus sensör / giriş-çıkış cihazları Slave olarak bağlanır.
- Ekran cihazları sorgular, register verilerini okur ve uygun komutları yazar.

**Hat B — Ekran Slave**
- Raspberry Pi 4 üzerindeki Home Assistant, USB-RS485 adaptörü üzerinden bu hattın Master'ı olur.
- ESP32-S3 ekran bu hatta Modbus Slave olarak çalışır.
- Ekran, kendi topladığı veya arayüzünde tuttuğu uygun verileri register haritası üzerinden HA'ya sunabilir; HA'dan gelen yazma komutlarını da deney kapsamında işleyebilir.

İki rol aynı RS485 hattında paylaşılmayacaktır. Ekran kartı iki ayrı fiziksel RS485 bağlantısı ve iki ayrı UART üzerinden bir hatta Master, diğer hatta Slave olarak görev yapacaktır. Böylece aynı hatta iki Master'ın çakışması önlenir.

### Deney senaryoları

1. Mikro ESP'den sıcaklık gibi basit sensör verisi okumak ve ekranda göstermek.
2. Modbus sensör register'larını ekranda göstermek.
3. Ekran dokunmatiğindeki bir düğmeyle Hat A üzerinden dijital Modbus çıkışını veya röleyi tetiklemek.
4. HA'nın Hat B üzerinden ekranın Slave register'larını okuması.
5. HA'dan ekrana register yazılması ve ekran arayüzünde karşılığının gösterilmesi.
6. Ekranın Hat A'dan topladığı veriyi Hat B üzerinden HA'ya sunması.
7. Birden fazla Modbus cihazında adresleme, sorgulama sırası, zaman aşımı ve haberleşme hatası davranışlarını denemek.
8. Ekran arayüzünde akan oklar, birden fazla değerin toplamı, grafikler, sayfa geçişleri, dokunmatik kontroller, parlaklık ve backlight yönetimini öğrenmek.

### Öğrenme amacı

Bu laboratuvarın temel amacı yalnızca akım değerlerini ekranda göstermek değildir. ESP32-S3 üzerinde ekran tasarımı ve kullanıcı etkileşimi geliştirmek; Modbus Master/Slave rollerini, iki bağımsız RS485 hattını, mikro ESP ile sensör haberleşmesini ve Home Assistant entegrasyonunu deneyerek öğrenmektir.

Ekran tasarımı ayrı bir deneyim alanı olarak ele alınacaktır. LVGL veya uygun başka bir ekran kütüphanesi, kartın gerçek donanımına ve mevcut örnek koduna bakılarak değerlendirilebilir.

### Açık teknik doğrulamalar

- ESP32-S3 ekran kartının tam modeli, mevcut RS485 devresinin UART bağlantısı ve pinleri belirlenecek.
- İkinci RS485 transceiver'ın lojik gerilim uyumluluğu doğrulanacak; ESP32-S3 GPIO'larına uygun 3,3 V lojik seviyeli bir çözüm seçilecek.
- İki UART'ın aynı anda çalışması, DE/RE yön kontrolü, baud/parite ayarları ve Modbus zamanlamaları test edilecek.
- Hat sonlandırma, bias dirençleri, ortak referans/topraklama ve kablo düzeni gerçek modüllere göre belirlenecek.
- HA tarafında Modbus entegrasyonunun register okuma/yazma biçimi ve ekranın Slave register haritası ayrıca tasarlanacak.
- Bu bölüm bir deney fikridir; bağlantı şeması, kod, cihaz modeli veya başarılı çalışma sonucu henüz kesinleşmiş değildir.
