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
