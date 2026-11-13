# E19 — Deney protokolü

## Soru

SCT-013 30A/1V ile ADS1115 kullanımı, BERO'nun mevcut bias + ESP32 ADC yoluna kıyasla özellikle 0,5 A altındaki ölçüm davranışını iyileştiriyor mu? Kart ve giriş bağlantısı uygunsa harici bias bölücü olmadan çalışabiliyor mu?

## Sabitler

- SCT modeli: SCT-013 30A/1V.
- Referans: PZEM-004T V3.0.
- Mevcut yol: aynı SCT modeli + mevcut bias + ESP32 ADC.
- ADS1115: kart teslim alındıktan sonra kart üzerindeki gerçek bileşenler ve besleme/pull-up düzeni doğrulanacak.
- İlk koşulda iletken tur sayısı mevcut düzenle aynı tutulacak.
- İlk karşılaştırmada K veya kalibrasyon katsayısı uydurulmayacak; önce ham ADC ve voltaj davranışı kaydedilecek.

## Aşama 0 — Teslimat ve kart incelemesi

1. Kartın iki yüzünün net fotoğrafını çek.
2. ADS1115 entegresini, direnç/kondansatörleri, A0–A3, ADDR, SDA, SCL, GND ve VDD pinlerini belirle.
3. Kartın 3,3 V beslemeyle çalışmasını ve I²C pull-up seviyesini doğrula.
4. SCT girişine bağlı olabilecek burden, seri direnç, bias, koruma veya filtre elemanlarını belirle.
5. Kart üzerinde şema/üretici dokümanı yoksa bağlantı sürekliliği ve bileşen izlerini incele; belirsizliği not et.
6. AIN pinlerinin GND–VDD aralığında kalmasını sağlayacak common-mode yol doğrulanmadan CT'yi bağlama.

## Aşama 1 — Yüksüz taban

- Fiziksel olarak ölçülen iletkende akım olmadığı bilinen koşul kaydedilir.
- ADS1115 ham diferansiyel/tek uçlu sayımları, örnek sayısı, ortalama, RMS ve dağılımı ayrı ayrı kaydedilir.
- İlk denemede bias'sız bağlantı yalnızca AIN ortak-mod ve giriş sınırları güvenli biçimde doğrulanmışsa yapılır.
- Güvenli doğrudan bağlantı mümkün değilse deneme durdurulur; gereken en küçük referans/bias ağı ayrıca tasarlanır. Bu sonuç bias'sız hedefin başarısız/kanıtsız kaldığı şeklinde kaydedilir.

## Aşama 2 — Kontrollü yük karşılaştırması

Hedef yük basamakları, gerçek PZEM değerine göre seçilir. Önerilen kapsama:
- yaklaşık 0,1–0,2 A (PZEM'in güvenilir çözünürlüğü ve yük imkânı elverirse),
- 0,24 A çevresi,
- 0,30 A çevresi,
- 0,40–0,41 A çevresi,
- 0,50 A çevresi,
- geçiş davranışını görmek için 0,5 A üzerindeki en az bir kontrol noktası.

Her koşulda:
1. PZEM akım/güç/gerilim ve güncelleme zamanları kaydedilir.
2. ADS1115 ham sayım ve dönüştürülmüş voltaj kaydı alınır.
3. Mevcut ESP32 ADC yolunun verisi aynı yük koşulunda alınır.
4. Yük kararlılığı ve ölçüm penceresi kaydedilir.
5. Aynı koşul tekrarlanır; tek oturumdan genelleme yapılmaz.

## Aşama 3 — Okuma modu ve ayar karşılaştırması

- Single-ended ve differential bağlantılar ayrı deney koşullarıdır; aynı anda veya güvenlik doğrulanmadan değiştirilmez.
- PGA, girişte görülen tepe gerilimi ve clipping payı incelendikten sonra seçilir. GAIN_SIXTEEN varsayılan/evrensel ayar değildir.
- ADS1115 veri hızı seçenekleri ve örnekleme pencereleri gerçek dönüşüm sayısıyla doğrulanır.
- 20 ms pencerede maksimum dönüşüm hızı 860 SPS olsa bile teorik üst sınır yaklaşık 17 örnektir; gerçek örnek sayısı logdan doğrulanır.
- 200 ms ve 1 s gibi daha uzun pencerelerle RMS/kararlılık karşılaştırılır.
- Ortalama DC bileşeni çıkarılmış RMS ile ham RMS ayrı raporlanır.

## Analiz ölçütleri

Her koşul için:
- geçerli örnek sayısı ve gerçek ölçüm süresi,
- ADC ham min/maks ve clipping/dropout,
- ortalama ve ortalama çıkarılmış RMS,
- standart sapma, CV ve P5/P50/P95,
- tekrarlar arası fark,
- PZEM'e göre akım sapması,
- mevcut ESP32 ADC yoluna göre kararlılık farkı.

PZEM güncelleme hızı daha düşükse SCT/ADS örnekleriyle noktasal zaman eşleştirmesi yapılmaz; yalnız geçerli zaman aralıkları ve kararlı alanlar karşılaştırılır.

## Karar

ADS1115 düşük akım alternatifi olarak ancak şu bulgular birlikte değerlendirilerek kabul edilebilir:
- elektriksel giriş güvenliği doğrulanmış,
- aynı koşullarda tekrarlanabilir,
- mevcut yola göre daha iyi veya anlamlı derecede faydalı kararlılık göstermiş,
- PZEM referansına göre sapması hedeflenen aralıkta,
- bias'sız çalışma iddiası varsa bu durum kart bağlantısı ve ölçümle kanıtlanmış.

±%4 hedefi bir deney kabul ölçütüdür; sonuçlar görülmeden başarı ilan edilmez.


## ESPHome ct_clamp + ADS1115 uygulama notu

ESPHome resmi bileşen yapısı doğrulandı: ADS1115 ayrı bir `platform: ads1115` gerilim kaynağı olarak tanımlanır; ct_clamp bu kaynağı `sensor:` alanıyla tüketir. ADS1115 hub için `continuous_mode: true` ct_clamp kullanımı sırasında önerilir. Paylaşılan taslaktaki `sensor_id`, `ads1115_id`, `multiplexer` ve `gain` alanlarının tek ct_clamp bloğunda verilmesi doğru değildir.

İlk yazılım denemesinde aday ayarlar: ADS1115 differential A0_A1, gain 0.256 V, sample_rate 860 SPS; ct_clamp sample_duration 200 ms ve update_interval 2 s. Bu ayarlar donanım giriş sınırları ve tepe gerilim ölçülmeden kesinleştirilmiş değildir. Gain 0.256 V aralık seçimidir; harici/16x analog yükselteç değildir.

Önemli zaman ayrımı: 2 s update_interval, 2 saniye boyunca kesintisiz örnekleme anlamına gelmez. ct_clamp her güncellemede sample_duration boyunca örnek toplar; 200 ms pencere + 2 s çevrimde arada örneklenmeyen zaman kalır. Gerçek örnek sayısı ve SPS, ct_clamp debug logundan kaydedilecektir.

ESPHome 2026.10.2 kaynak kodu incelemesine göre ct_clamp, örnekleme penceresinde yüksek frekanslı loop ister; ADS1115 continuous mode ile her sample çağrısında dönüşüm register'ından okuma yapar. ct_clamp aynı ADC değerinin tekrarını atlar, farklı örneklerin toplamını ve kare toplamını biriktirir, pencere sonunda DC ortalamasını çıkarıp RMS hesaplar. Dolayısıyla işlemci yükü optimize edilmiş olsa da sıfır değildir.

Kalibrasyon filtresi için 0.1 → 0.4 yalnız örnek çifttir; 5 tur kullanımıyla otomatik doğru kalibrasyon anlamına gelmez. Gerçek ham ct_clamp sonucu, bilinen yük ve PZEM referansı ile kalibrasyon noktaları çıkarılacaktır.

## Ek deney hedefi — yaklaşık 2 A bölgesi

ADS1115 alternatifi 0,5 A altındaki hedef bölgede işe yararsa, yaklaşık 2 A civarında da kullanılabilirliği ayrıca test edilecek. Bu, 0,5 A altı deneyinin yerine geçmeyen ikincil bir doğrulama hedefidir.

2 A çevresinde en az bir kararlı yük noktası ve mümkünse bu noktanın alt/üst komşu noktaları kaydedilecek. ADS1115 gain seçimi, SCT çıkış tepe değeri ve clipping payı dikkate alınacak. Katsayı; ham ölçüm, gerçek bağlantı/tur sayısı ve aynı kararlı koşuldaki PZEM referansı üzerinden hesaplanacak. Tek katsayının hem düşük akım hem 2 A civarında yeterli olduğu varsayılmayacak; aralıklar arası sapma ayrıca raporlanacak.

Kabul için elektriksel giriş güvenliği, clipping olmaması, tekrar edilebilirlik ve PZEM'e göre sapma birlikte incelenecek. Katsayı ve 2 A uygunluğu deney öncesinde belirlenmiş değildir.

## Aday mimari — aynı ESP üzerinde çift ölçüm yolu

E19 başarılı olursa sonraki adımda aynı ESP32 üzerinde iki yolun birlikte çalışması değerlendirilecek:

1. Mevcut dahili ADC + bias yolu.
2. I²C üzerinden ADS1115 ölçüm yolu.

İki yol aynı SCT kanalını izleyebiliyorsa, ilk doğrulama aşamasında ikisi de paralel ölçüm yapıp ayrı değer/log üretebilir. Yazılım, yaklaşık 1 A altındaki bölgede ADS1115 değerini; bu eşik üstünde mevcut ESP32 ADC değerini seçebilir. Bu, fiziksel bağlantıyı değiştirmek değil, hangi ölçüm sonucunun kullanılacağını yazılımla seçmek şeklinde tasarlanacak.

### Geçiş mantığı için açık konular

- 1 A yalnızca başlangıç önerisidir; PZEM referanslı kararlı yük testleriyle doğrulanacak.
- Eşik çevresinde iki yol arasında sık gidip gelmeyi önlemek için histerezis gerekir. Alt/üst geçiş eşikleri deney verisinden seçilecek; henüz sayısal histerezis değeri yoktur.
- Her iki yolun timestamp, örnekleme penceresi ve gecikmesi karşılaştırılmalı; geçiş anında eski/yeni değerler arasında süreksizlik olup olmadığı kaydedilmelidir.
- ADS1115 yaklaşık 2 A civarında da sınanacak; gain ve giriş headroom'u clipping olmayacak şekilde seçilecek.

### Analog bağlantı güvenlik kapısı

Aynı SCT çıkışını iki ADC ön ucuna paralel bağlamak otomatik olarak güvenli/doğru kabul edilmez. ESP32 tarafındaki bias ağı ve ADS1115 tarafındaki giriş/common-mode ağı birlikte analiz edilmeden bağlantı yapılmayacak. Gerekirse tampon, uygun ayırma veya analog anahtarlama kullanılacak. Bu inceleme tamamlanana kadar şema/YAML kesinleştirilmeyecek.

## 2026-11-13 — Aşama 2 protokolü: 100 W ortak alan / katsayı

### Soru
ADS1115 + ct_clamp zinciri, mevcut ESP32D1 SCT/ADC zinciriyle ikisinin de kararlı değer ürettiği 100 W yük alanında PZEM referansına göre nasıl davranıyor? ADS1115 için uygun katsayı nedir?

### Sabit koşul
- Yük: 100 W akkor ampul, sürekli açık.
- Referans: PZEM-004T V3.0.
- Sistem A: ESP32D1 mevcut SCT/ADC/ct_clamp firmware'i; K=24.22 korunur.
- Sistem B: ESP32D2 + ADS1115 A0_A1 + ct_clamp; depodaki YAML.
- ADS1115 ayar adayı: gain 2.048, sample_rate 860, continuous_mode true, sample_duration 200 ms, update_interval 2 s.
- İlk testte kablo tur sayısı, sensör konumu ve diğer ayarlar değiştirilmez.

### Uygulama sırası
1. ADS1115 girişlerinin besleme raylarına göre güvenli common-mode aralığında olduğu doğrulanır. Diferansiyel çıktı tek başına bu güvenliği kanıtlamaz.
2. 100 W akkor sürekli yakılır; açılış/geçiş dönemi kararlı alan hesabına alınmaz.
3. ESP32D1, ESP32D2 ve PZEM zaman damgalı kayıtları aynı oturumda alınır. İki CT kullanılıyorsa aynı tek yalıtılmış iletken üzerindeki sensör konumu ve tur sayısı kaydedilir. Tek CT ile ardışık ölçüm yapılırsa bağlantı değişimi enerjisiz yapılır ve her koşulda PZEM kararlılığı yeniden kontrol edilir.
4. Her akışın kararlılığı ayrı değerlendirilir; yalnız ortak kararlı zaman aralığı katsayı karşılaştırmasına alınır.
5. Ham ct_clamp ve kalibrasyon sonrası değerler ayrı tutulur. Katsayı, birimler doğrulandıktan sonra PZEM kararlı ortalamasına göre hesaplanır.
6. En az bir tekrar alınır; tek oturumdan genel katsayı kararı çıkarılmaz.

### Kayıt alanları
- Oturum tarihi/saat ve timezone.
- SCT modeli, tur sayısı, fiziksel konum ve kanal.
- ESPHome sürümü, YAML dosya yolu ve commit.
- ADS1115 gain, SPS, gerçek ct_clamp farklı örnek sayısı ve loglanan SPS.
- PZEM V/A/W ve zaman damgaları.
- ESP32D1 ve ESP32D2 ham/kalibreli değerleri.
- Kararlı alan başlangıç/bitişleri, n, ortalama, SD, CV, min/maks.
- PZEM'e göre fark ve tekrarlar arası fark.

### Sonuç kapısı
- Derleme başarılı olması donanımda çalıştığını kanıtlamaz.
- I2C bağlantısı RMS akım ölçümünü kanıtlamaz.
- Tek 100 W noktası yalnız başlangıç katsayısını belirler; farklı akım aralığına genelleme yapmaz.
- ±%4 hedefi yalnız ölçüm ve tekrarlar sonrası değerlendirilecek.

## 2026-11-13 — Kullanıcı kararı: çalışma sınırı testi kalibrasyondan önce gelir

Bu bölüm, protokoldeki önceki katsayı belirleme odaklı aşama tariflerini mevcut deney için sınırlar ve günceller.

### Birincil soru
ADS1115 + SCT + ESP32D2 ölçüm zinciri, **mevcut ayarlar ve mevcut kalibre edilmemiş/kaba katsayı değiştirilmeden**, düşük akımda hangi seviyeye kadar kararlı ve kullanılabilir veri üretebiliyor?

### Deney boyunca sabitlenecekler
- ADS1115 gain ve sample_rate.
- continuous_mode ve A0_A1 diferansiyel giriş seçimi.
- ct_clamp sample_duration ve update_interval.
- accuracy_decimals, filtre/eşik ve çalışan katsayı.
- SCT tur sayısı, fiziksel konum ve kablolama.

Bir değişkeni değiştirmek gerekirse o seri mevcut basamak karşılaştırmasından ayrılır ve yeni koşul olarak etiketlenir. Katsayıyı PZEM'e göre ayarlamak bu aşamada yapılmaz.

### Basamak yöntemi
1. Mevcut 57 W sabit yük gözlemini başlangıç düşük-akım noktası olarak kaydet.
2. Her yeni yük seviyesinde PZEM ve ADS/SCT kayıtlarının aynı zaman aralığını al.
3. Geçici/ısınma davranışını kararlı bölümden ayır; kararlılık yalnız geçen süreye göre varsayılmaz.
4. Her akış için n, ortalama, SD, CV, min–maks, sıçrama/boşluk ve mümkünse kararlı zaman aralığını kaydet.
5. PZEM'e göre mutlak fark ve yüzde farkı yalnız betimleyici karşılaştırma olarak hesapla; katsayıyı değiştirmek için kullanma.
6. Yükü kademeli azalt. Kararlı ve kararsız basamakları ayır; mevcut konfigürasyon için gözlenen alt çalışma sınırını raporla.
7. Alt sınır gözlemi tamamlandıktan sonra katsayı belirleme ayrı deney/iş aşaması olarak planlanır.

### 57 W ön gözlemi
- PZEM: 0,265 A (**KULLANICI BİLDİRİMİ**).
- ADS1115 + SCT: 0,270 A (**KULLANICI BİLDİRİMİ**); mevcut kaba/başlangıç katsayısı kullanılmış, kalibrasyon yapılmamış.
- Fark: +0,005 A; PZEM'e göre yaklaşık +%1,89 (**HESAP**).
- Bu kısa bildirim kararlılık izlenimini içerir; ham CSV/zaman serisi istatistikleri olmadan tam kararlı pencere doğrulaması değildir.

### Sonuç sınırı
Bu deney kalibrasyon doğruluğu, ±%4 genel kabulü veya PZEM'in mutlak doğruluğunu kanıtlamaz. Yalnız mevcut yapılandırmanın düşük akım çalışma davranışını ve gözlenen sınırını belirler.

## 2026-11-13 — Genel deney sırası: 100 W kaba kalibrasyon → düşük akımda karakterizasyon

Kullanıcının netleştirdiği yöntem, yalnız ADS1115'e özgü değil, karşılaştırılan her ölçüm yapısı için geçerlidir:

1. Her ölçüm yapısı yaklaşık 100 W sabit yükte PZEM referansına karşı kaba kalibre edilir.
2. Bu başlangıç ayarı/katsayısı o yapının düşük akım karakterizasyonu boyunca sabit tutulur.
3. Yük kademeli olarak azaltılır; her basamakta aynı zaman aralığındaki PZEM ve sensör serileri karşılaştırılır.
4. Amaç düşük akımda tekrar kalibrasyon yapmak değil; kararlılık, dağılım, sıçrama/okuma kaybı, tekrarlanabilirlik ve kullanılabilir alt sınırı tanımaktır.
5. Gerekirse yeni katsayı/kalibrasyon çalışması, düşük akım karakterizasyonundan sonra ayrı bir aşama olarak yürütülür.

100 W'taki kaba kalibrasyon, bağımsız doğruluk doğrulaması veya tüm akım aralığı için katsayı geçerliliği anlamına gelmez.


## 2026-11-13 — 57 W oturumu kapandı (18:40) ve CSV ön analizi

- Kullanıcı bildirimi: 57 W nominal akkor yük oturumu **18:40 (+03:00)** itibarıyla kapatıldı.
- Kaynak CSV: `history (57).csv`; SHA-256: `5945b3731a86408db84426f140c6b71869dd5e43b885514aa060e8d9a892a78b`; 5.441 satır, 3 sütun. CSV zamanları UTC'den Europe/Istanbul'a çevrilerek incelendi.
- İncelenen oturum aralığı: 18:32:00–18:40:00 (+03:00). Kullanıcı yükü 57 W nominal olarak tanımladı; CSV'deki PZEM aktif güç bu aralıkta yaklaşık 60,1–61,0 W (18:32–18:40 ortalama 60,58 W) gösteriyor. Nominal lamba etiketi ile PZEM'in ölçtüğü aktif güç birbirinden ayrıdır.
- 18:35:00–18:40:00 ortak gözlem kesiti: ADS1115 + SCT n=150, ortalama 0,266212 A, örnek SD=0,000985 A, min–maks 0,263838–0,269036 A. PZEM akım n=18, ortalama 0,264500 A, örnek SD=0,000514 A, min–maks 0,264–0,265 A. Ortalama fark +0,001712 A; PZEM'e göre yaklaşık +%0,647 (**HESAP**).
- 18:32:00–18:40:00 tam kesitinde ADS1115 n=239, ortalama 0,266547 A, SD=0,001108 A; PZEM n=23, ortalama 0,264783 A, SD=0,000795 A. Ortalama fark +0,001764 A; yaklaşık +%0,666 (**HESAP**).
- Aynı 18:35–18:40 aralığında eski ESP32D1 dahili ADC CH1-1T serisi n=300, ortalama 0,305881 A, SD=0,021954 A, min–maks 0,277557–0,439324 A. Bu seri ADS1115'ten belirgin biçimde daha geniş dağılım gösteriyor; farklı ölçüm mimarileri ayrı tutulur.
- CSV'nin son ADS1115 örneği 18:39:59.927, son PZEM akım örneği 18:39:57.857; kullanıcının 18:40'ta kapatma bildirimiyle uyumlu kayıt sonu.
- **Yorum sınırı:** 18:35–18:40 ADS1115 serisi bu oturumda dar dağılımlı/kararlı gözüküyor ve PZEM ortalamasına yakın. Bu, 100 W'ta yapılan kaba referans ayarından sonra düşük akımda çalışma davranışına ilişkin gözlemdir; bağımsız kalibrasyon, ±%4 genel doğrulaması veya alt çalışma sınırının kesin belirlenmesi değildir. Daha düşük basamaklar ve tekrarlar gerekir.
- Bu aşamanın yöntemi: her ölçüm yapısı PZEM'e karşı yaklaşık 100 W noktasında kaba kalibre edilir; ardından katsayı değiştirilmeden daha düşük akım basamaklarında davranışı tanınır. Düşük akım aşamasında amaç yeniden kalibrasyon değil, kararlılık ve kullanılabilir alt sınırı bulmaktır. Kullanıcı bu yöntemi her ölçüm yapısı için geçerli olarak netleştirdi.
- Güvenlik ön koşulu (ADS1115 A0/A1 ortak-mod/bias ve giriş ray sınırlarının fiziksel doğrulaması) ayrıca açık kalır.
