# BERO Envanteri

## İmal edilmiş donanımlar

### BIAS TRAFOSU — Taşınabilir Güç Kutusu

- **Tür:** Proje kapsamında imal edilmiş fiziksel donanım.
- **Kullanım amacı:** SCT013 akım ölçüm zincirinin trafo bias/güç yapısı.
- **Fiziksel yapı:** Ana sistemden ayrı, bağımsız ve taşınabilir güç kutusu.
- **Güç zinciri:** RN130421 6 V AC / 2.0 VA trafo → KBU610 köprü doğrultucu → 2200 µF / 35 V filtre kondansatörü → L78L33 (TO-92) regülatör.
- **Doğrulanmış çıkış:** Regülatör çıkışı fiziksel olarak **3.30 V** ölçüldü.
- **İlgili görev:** [GRV-003 — Trafo Bias Yapısının Kurulması ve Doğrulanması](../GOREVLER/GRV-003/RAPOR/README.md)
- **Görüntü / fotoğraf:** Kullanıcı tarafından daha sonra eklenecek.

> Not: Bu kayıt, imal edilmiş taşınabilir güç kutusunu envanter varlığı olarak tanımlar. GPIO32/33/34 üzerindeki 1.65 V okumaları, güç kutusunun 3.30 V çıkışından ayrı ölçüm noktalarıdır.

## Ölçüm ve deney ekipmanları

Bu bölüm, BERO geliştirme ve genel elektronik deneylerinde kullanılan mevcut ölçüm, sinyal üretme ve yük oluşturma araçlarını kaydeder. Cihazların varlığı, ölçüm doğruluğunun veya belirli bir deneyde uygunluğunun önceden doğrulandığı anlamına gelmez.

| Ekipman | Model / tanım | Kullanım amacı ve sınırlar | Durum |
|---|---|---|---|
| Dijital multimetre | UNI-T UT33D+ | Temel DC/AC gerilim, direnç ve süreklilik kontrolleri | Mevcut |
| Pens ampermetre | UNI-T UT200B+ | Temassız akım ölçümü ve yük akımını kontrol etme | Mevcut |
| Osiloskop | FNIRSI 2D15P, 2 kanal, 100 MHz | Analog dalga biçimi, genlik, zamanlama ve iki kanal karşılaştırması; ilk kullanım düşük gerilimli deneylerle yapılacak | **Satın alındı; teslimat bekleniyor (13.11.2026)** |
| Sinyal jeneratörü | SANEC; tam model henüz kaydedilmedi | Düşük gerilimli test sinyalleri üretme | Mevcut |
| Akım/gerilim simülatörü | FNIRSI SG-002, 4–20 mA / 0–10 V | Endüstriyel akım ve gerilim girişlerini simüle etme; çıkış sınırları ve bağlantı biçimi cihaz kılavuzundan doğrulanacak | Mevcut |
| USB lojik analizör | SANEC, 24 MHz, 8 kanal | UART, I²C, SPI ve diğer dijital lojik sinyallerin zamanlama/protokol incelemesi; analog dalga biçimi ölçmez | Mevcut |
| AC güç kontrolü / dimmer | SANEC, SCR, 220 V AC, ilan edilen 4000 W, manuel ve dokunmatik kontrol | Uyumlu rezistif yüklerde ayarlanabilir deney yükü oluşturma. Faz kontrolü nedeniyle akım dalga biçimini kesebilir; dimmerli kayıtlar normal sinüs beslemeli temel deney verilerinden ayrı tutulmalı | Mevcut |

## Akım sensörleri

| Sensör | Tanım | Kullanım amacı | Durum |
|---|---|---|---|
| SCT013 | 30 A / 1 V | Mevcut SCT ölçüm zincirinde kullanılan akım trafosu; düşük akım bölgesindeki davranışı inceleniyor | Mevcut |

| SCT013 | 100 A / 1 V | İleride ana hat gibi daha yüksek akım aralığı beklenen noktalarda değerlendirme; 30 A / 1 V ile ayrı ADS1115 karakterizasyonu | **8 adet mevcut (kullanıcı bildirimi; fiziksel model/etiket teyidi bekliyor)** |
| SCT013 | 5 A sınıfı; sipariş edilen ürünün tam model/çıkış etiketi teslimatta doğrulanacak | 30 A / 1 V sensörle düşük akım bölgesinde karşılaştırmalı deney; aynı yük koşulunda duyarlılık ve kararlılık gözlemi | **5 adet sipariş edildi; uluslararası taşımada (13.11.2026)** |

### 5 A SCT sevkiyat kaydı

- **Sipariş miktarı:** 5 adet (kullanıcı bildirimi).
- **Takip ekranı:** 13.11.2026 tarihinde China Post / uluslararası taşıma durumunda.
- **Son görülen olay:** Guangzhou Uluslararası Takas Bürosu'na ulaştı; Türkiye'ye giriş veya Türkiye gümrük işlemi henüz görünmüyor.
- **Teslimat durumu:** Teslim alınmadı; ürün etiketi, tam model, çıkış tipi, fiziksel durum ve adet teslimatta kontrol edilecek.
- **Gizlilik:** Takip numarası kamuya açık envanter dosyasına yazılmadı.

## Deney yükleri ve kullanım notları

- Akkor ampuller: 15 W, 42 W, 57 W, 100 W ve 150 W sınıflarında daha önce deneylerde kullanılmış yükler.
- 100 W + 150 W akkor ampul kombinasyonu ile yaklaşık 250 W toplam nominal yük elde edilebilir. 230 V varsayımıyla yaklaşık akım 1,09 A'dir; gerçek değer PZEM ile kaydedilmelidir.
- Evde bulunan tost makinesi, kettle ve fırın gibi rezistif ısıtıcılar farklı yük bölgeleri oluşturmak için kullanılabilir. Gerçek güç/akım her deneyde PZEM ile kaydedilir.
- SCR dimmer, yük ayarını kolaylaştırmak için düşünülmüştür; sabit güç kaynağı değildir. Dimmer ayar konumu sabit güç anlamına gelmez.
- Dimmer kullanıldığında faz kesme kaynaklı dalga şekli değişimi ve PF etkisi oluşabileceğinden, bu deneyler normal sinüs beslemeli SCT/PZEM karşılaştırmalarıyla aynı veri sınıfına karıştırılmamalıdır.
- Dimmerin üzerinde yazan 4000 W değeri, BERO deneylerinde bu güce çıkılacağı anlamına gelmez. Gerçek sürekli kapasite, soğutma ve koruma koşulları doğrulanmadan etiket değeri çalışma sınırı kabul edilmez.
- Şebeke gerilimiyle yapılan deneylerde uygun muhafaza, sigorta, bağlantı ve elektrik güvenliği sağlanmalıdır. FNIRSI 2D15P osiloskop probunun toprak klipsi doğrudan şebeke fazına veya nötrüne bağlanmayacaktır.

## Ekipman sınıflandırma ilkesi

- **Mevcut:** Kullanıcının elinde bulunduğu bildirilen cihaz.
- **Sipariş edildi / taşımada:** Sipariş verilmiş, ancak fiziksel teslim ve kutu/etiket kontrolü yapılmamış ekipman.
- Modeli veya teknik özelliği henüz kesinleşmeyen cihazlarda tahmin yürütülmez; doğrulama sonrasında kayıt güncellenir.
