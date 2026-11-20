# ADR-032 — Çamaşır ve bulaşık makineleri için ikiz sensör modülleri

- **Tarih:** 2026-11-20
- **Durum:** KABUL EDİLDİ — donanım mimarisi ve iş sırası kararı; fiziksel doğrulama bekliyor
- **Karar sahibi:** Kullanıcı

## Bağlam ve amaç

Çamaşır makinesi (Modül 5) ve bulaşık makinesi (Modül 6) için taşınabilir gözlem modülleri üretilecek. İki modül aynı elektronik donanım tasarımını ve ortak firmware temelini kullanacak; cihaz adı, modül kimliği ve veri kayıt etiketleri farklı olacak.

Makine davranışını incelemede ses ve titreşim birincil kanallardır. Akım, bu kanalları yorumlamaya yardımcı ikincil/bağlamsal kanaldır. Bulaşık makinesinde özellikle su alma ve su boşaltma evrelerinin ses/titreşim kayıtlarında gözlenmesi hedeflenir; bunlar henüz doğrulanmış sınıflar değildir.

## İkiz modüllerin ortak donanım listesi

Her modülde birer adet:
- ESP32-D kartı — tam kart/revizyon ve pin etiketleri fiziksel kontrolde teyit edilecek.
- ESP32-D için vidalı terminal shield.
- MAX4466 mikrofon yükselteç modülü — ses kanalı.
- MPU6050 ivmeölçer/jiroskop modülü — titreşim/hareket kanalı.
- SCT013 30 A / 1 V akım trafosu — yardımcı akım kanalı.
- ADS1115 harici ADC — SCT013 analog sinyalini okumak için.

İki modülün toplam planlanan miktarı: 2 ESP32-D, 2 vidalı shield, 2 MAX4466, 2 MPU6050, 2 SCT013 30 A / 1 V ve 2 ADS1115.

## Bağlantı mimarisi kararı

- MAX4466 analog çıkışı ESP32'nin ADC girişinden okunacak; ses örnekleme hızı, çözünürlük, analog giriş aralığı ve kayıt yöntemi henüz belirlenmedi.
- MPU6050, ESP32'nin birinci I²C hattında kullanılacak.
- ADS1115, ESP32'nin ikinci ve fiziksel olarak ayrı I²C hattında kullanılacak.
- **I²C mimarisi kesin kullanıcı kararıdır:** iki sensör aynı hattı paylaşmayacak; MPU6050 ve ADS1115 fiziksel bağlantı kolaylığı nedeniyle ayrı I²C bus'larında tutulacak.
- SCT013, ADS1115 analog girişine bağlanacak.
- İki I²C hattı için GPIO/SDA/SCL numaraları, kartın tam modeli ve shield pinleri fiziksel olarak incelendikten sonra belirlenecek. Ayrı I²C hattı tercihi kullanıcı kararıdır; ilgili ESP32 kartı ve framework üzerinde gerçek bağlantı/derleme ile doğrulanmalıdır.
- Besleme gerilimleri, ortak referans/toprak düzeni, MAX4466 analog bias/ölçekleme, SCT sekonderi ve ADS1115 giriş aralığı/koruması montaj öncesinde kontrol edilecek. Bu ADR pin şeması veya elektriksel güvenlik onayı değildir.

## İmalat sırası ve güç beslemesi

1. **Önce Modül 5 — Çamaşır makinesi** oluşturulacak. Kullanıcı bildirimi: kurulum noktasındaki prizde 5 V besleme mevcut.
2. **Modül 6 — Bulaşık makinesi** aynı donanım tasarımının ikinci kopyası olacak; ancak güç beslemesi çözülene kadar imalatı ertelenecek.
3. Bulaşık makinesi kendi mevcut elektrik hattından beslenecek; makineyi üçlü priz üzerinden besleme planı yoktur. Burada çözülecek konu yalnızca gözlem modülünün 5 V DC beslemesidir. Kullanıcı, modül için sıva üstü 5 V çıkışlı priz veya makine beslemesinden bağımsız ayrı bir hattan adaptör seçeneğini değerlendirecek; kesin çözüm henüz belirlenmedi.
4. İki modülün elektriksel tasarımı aynı kalır; kurulum ve besleme altyapısı cihaz konumuna göre farklı olabilir.

## Kapsam dışı / henüz kararlaştırılmayanlar

- GPIO pin eşlemesi, I²C hızları ve adres doğrulaması.
- MAX4466 ses örnekleme hızı, kayıt süresi ve veri biçimi.
- MPU6050 örnekleme hızı, aralıkları ve filtre ayarları.
- ADS1115 gain/data rate, SCT ön uç/bias/koruma ve kalibrasyon katsayısı.
- ESPHome mu, başka firmware yaklaşımı mı kullanılacağı; kod ve Home Assistant entegrasyonu.
- Muhafaza, sensör yerleşimi, kablo uzunlukları ve montaj yöntemi.
- Bulaşık makinesi gözlem modülünün 5 V besleme yönteminin seçimi.

## Kanıt ve durum

- Sensör modelleri, ESP32-D ve vidalı shield adedi, iki ayrı I²C hattının fiziksel bağlantı kolaylığı nedeniyle kesinleştirilmesi, Modül 5'ün önce yapılması ve Modül 6'in güç çözümüne kadar bekletilmesi **KULLANICI KARARI / KULLANICI BİLDİRİMİ** olarak kaydedilmiştir.
- Bu kayıt donanımın satın alındığı, bağlandığı, firmware'in yazıldığı/derlendiği veya ölçüm yapıldığı anlamına gelmez.
- Her iki modül de fiziksel montaj, elektriksel kontrol, firmware doğrulaması ve gerçek sensör logları tamamlanana kadar **PLANLANDI** durumundadır.

## İlgili dosyalar

- [Modül 5 — Çamaşır makinesi](../../devices/washing-machine/README.md)
- [Modül 6 — Bulaşık makinesi](../../devices/dishwasher/README.md)
