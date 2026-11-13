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
