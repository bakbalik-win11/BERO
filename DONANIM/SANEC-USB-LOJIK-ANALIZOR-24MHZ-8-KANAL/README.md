# SANEC USB Lojik Analizör — 24 MHz / 8 Kanal

## Amaç

Bu belge, BERO'da kullanılan/planlanan **SANEC USB Lojik Analizör - 24 MHz 8 Kanal** için donanım özetini, yazılım seçeneklerini ve MCP3208 SPI hata ayıklama bağlantı planını toplar.

> **Model doğrulama notu:** İnternetteki ürün sayfalarında aynı sınıfta 24 MHz / 8 kanal USB analizörler çoğunlukla Saleae uyumlu Cypress FX2/FX2LP tabanlı klonlar olarak listeleniyor. SANEC marka/ürün revizyonunun iç devresi ve USB VID/PID'si elimizdeki cihaz üzerinden doğrulanmadı. Aşağıdaki FX2/fx2lafw bilgileri bu ürün sınıfı için güçlü bir eşleşmedir, ancak cihazın üzerindeki çip işaretlemesi veya USB kimliği görülmeden kesin SANEC donanım revizyonu olarak kabul edilmemelidir.

## Temel özellikler

| Özellik | Bilgi | Durum |
|---|---|---|
| Dijital kanal sayısı | 8 (CH0–CH7 / D0–D7) | Ürün sınıfı için listelenmiş |
| Azami örnekleme hızı | 24 MS/s | Ürün adı/sınıfı bilgisi |
| Örnekleme periyodu | 1 / 24 MHz ≈ 41,7 ns | Hesaplanan |
| Arayüz | USB; genellikle USB 2.0 uyumlu | Klon ailesi için tipik |
| Muhtemel donanım ailesi | Cypress CY7C68013 / CY7C68013A (FX2/FX2LP) | SANEC cihazında doğrulanmadı |
| Yazılım | sigrok / PulseView ve fx2lafw; bazı klonlar Saleae Logic eski sürümleriyle çalışabilir | Cihaz kimliğine bağlı |
| Sinyal türü | Dijital lojik seviyeleri; analog osiloskop değildir | Genel işlev |

**24 MHz örnekleme hızı, 24 MHz analog bant genişliği anlamına gelmez.** Dijital kenarlar örnekleme anlarında gözlenir; çok kısa darbeler kaçabilir. Kullanılabilir örnekleme hızı ve uzun kayıt kapasitesi yazılım, USB aktarımı, tampon bellek ve cihaz revizyonuna bağlıdır.

## Üretici/satıcı bilgisi ile genel FX2 klon bilgisini ayırma

- TLS Robotik'in benzer adlı 24 MHz / 8 kanal ürün sayfası, 8 dijital giriş, 24 MHz'e kadar örnekleme ve 3,3 V/5 V tabanlı lojik sistemlerde kullanım bilgisini listeler: https://www.tlsrobotik.com/urun/usb-lojik-analizor-24-mhz-8-kanal-mcu-arm-fpga-dsp-hata-ayiklama-araci/
- sigrok'un “Noname Saleae Logic clone” kaydı, 8 kanal / 24 MHz sınıfında Cypress CY7C68013A, 74LVC245A tampon ve fx2lafw desteği örneği verir: https://sigrok.org/wiki/Noname_Saleae_Logic_clone
- Farklı markaların benzer görünmesi, aynı PCB'yi, eşik seviyesini veya giriş korumasını kullandıklarını kanıtlamaz. Cihaz üzerindeki yazılar, kanal kablo renkleri ve USB kimliği kontrol edilmelidir.

## Yazılım — önerilen başlangıç: PulseView

PulseView, sigrok araç takımının grafik arayüzüdür; dijital dalga biçimlerini kaydetme ve SPI/I²C/UART gibi protokolleri çözümleme amacıyla kullanılır.

- İndirme sayfası (Windows/macOS/Linux): https://sigrok.org/wiki/Downloads
- PulseView kullanım kılavuzu: https://sigrok.org/doc/pulseview/unstable/manual.html
- fx2lafw destekli cihazlar: https://sigrok.org/wiki/Fx2lafw
- USB analizör kurulum örneği: https://learn.sparkfun.com/tutorials/using-the-usb-logic-analyzer-with-sigrok-pulseview/all

### İlk bağlantı adımları

1. PulseView'u işletim sistemine uygun resmî sigrok indirme sayfasından kur.
2. Analizörü USB'ye bağla.
3. Otomatik algılanmazsa yeni cihaz oturumunda sürücü olarak **fx2lafw (generic driver for FX2 based LAs)**, arayüz olarak **USB** seçip cihaz taraması yap.
4. Listede uygun bir **Logic with 8 channels** cihazı görünürse seç. Görünmüyorsa rastgele farklı cihaz/firmware seçme; önce USB VID/PID ve işletim sistemi sürücüsünü kontrol et.
5. D0–D7 kanallarını etkinleştir, örnekleme hızını ve kayıt uzunluğunu ayarla, Run ile yakalama başlat.
6. SPI çözümleyici ekle; CS, CLK, MOSI/DIN ve MISO/DOUT kanallarını doğru eşle.

**Saleae yazılımı hakkında:** Klon uyumluluğu sürüm ve cihaz kimliğine göre değişebilir. Ürün satıcısının “Saleae uyumlu” demesi tüm Logic sürümlerinin çalışacağını garanti etmez. Bu cihaz sınıfında PulseView + fx2lafw açık kaynak bir başlangıç seçeneğidir.

## BERO MCP3208 SPI yakalama planı

Önceki BERO bağlantı notlarında kullanılan ESP32-WROOM-32D / DevKitC eşlemesi:

| Analizör girişi | Bağlanacak sinyal | ESP32/MCP3208 bağlantısı |
|---|---|---|
| GND | Ortak GND | ESP32 GND ve ADC dijital/analog GND referansı |
| CH0 / D0 | CS | ESP32 GPIO5 → MCP3208 CS/SHDN |
| CH1 / D1 | CLK / SCLK | ESP32 GPIO18 → MCP3208 CLK |
| CH2 / D2 | DIN / MOSI | ESP32 GPIO23 → MCP3208 DIN |
| CH3 / D3 | DOUT / MISO | MCP3208 DOUT → ESP32 GPIO19 |
| CH4–CH7 | İsteğe bağlı | Başka sinyaller veya yedek kanallar |

Bu kanal ataması yalnızca önerilen kayıt düzenidir. Gerçek kablolamayı enerjiyi kapatıp kontrol et. PulseView'da SPI çözümleyicide CS aktif-düşük, saat modu ve bit sırası kullanılan firmware ile uyumlu olmalıdır. MCP3208, SPI modları 0,0 ve 1,1'i destekler; BERO testinde kullanılan modu ayrıca kaydet.

### İlk yakalama için öneri

- Önce düşük karmaşıklıkta sabit bir ADC girişiyle tek bir CH0 okuması yakala.
- Başlangıç örnekleme hızını 24 MS/s seçebilirsin. 1 MHz SPI için bu, bir saat periyodunda teorik olarak yaklaşık 24 örnek sağlar; USB aktarımı ve cihaz revizyonuna göre kullanılabilir ayarlar değişebilir.
- CS'nin her çerçeve öncesinde HIGH, ardından LOW olduğunu; üç baytlık aktarım boyunca CS'nin doğru durumda kaldığını kontrol et.
- CLK, MOSI/DIN ve MISO/DOUT dalga biçimlerini aynı zaman çizelgesinde görüntüle.
- SPI decoder sonucunu ham dalga biçiminden bağımsız doğru kabul etme. İlk aşamada MOSI/MISO baytlarını manuel olarak da karşılaştır.
- MCP3208'in single-ended CH0 için beklenen komut dizisi destek yazışmasında TX = `0x06 0x00 0x00` olarak verilmiştir. RX çözümlemesi `((rx[1] & 0x0F) << 8) | rx[2]` şeklindedir; `rx[1]` içindeki zero bitinin 0 olduğunu kontrol et.
- Hatalı/kararsız okuma varsa yakalama dosyasını proje kaydına ekle ve örnekleme hızı, SPI modu, kanal eşlemesi, TX/RX ve beklenen/gerçek değerleri not et.

## Elektriksel güvenlik ve sınırlar

- Bu cihaz **dijital lojik analizörüdür**; analog gerilim dalga biçimini ölçen osiloskop yerine geçmez.
- 24 MHz / 8 kanal klonlarda giriş eşik gerilimi ve mutlak maksimum değer ürün revizyonuna göre değişebilir. Genel FX2 klon kayıtlarında yaklaşık -0,5…5,25 V mutlak aralık ve sabit dijital eşik değerleri listelenir; bu değerler SANEC cihazı için doğrulanmış spesifikasyon değildir.
- ESP32/MCP3208 devresinde dijital sinyallerin 3,3 V seviyesinde kalması beklenir. Analizörün 5 V toleranslı olduğu varsayımıyla hedef devreye 5 V uygulama.
- Analizörün GND'sini hedef devrenin GND'sine bağlamak elektriksel referansları birleştirir. İzolasyon gerektiği durumlarda bu bağlantıyı gelişigüzel yapma.
- **Şebeke gerilimine veya doğrudan 230 V AC devrelere bağlama.** Bu analizör düşük gerilimli dijital sinyaller için kullanılmalıdır; güvenli izolasyon ve uygun ölçüm ekipmanı olmadan şebeke devrelerini inceleme.
- Probları bağlamadan önce devrenin enerjisini kapat; GND ve sinyal uçlarını doğrula.

## Sorun giderme

### PulseView cihazı görmüyor
- USB kablosunun veri taşıdığını ve doğrudan USB portunu dene.
- İşletim sisteminin USB aygıt listesinde cihazın görünüp görünmediğini kontrol et.
- PulseView'da fx2lafw sürücüsüyle USB taraması yap.
- USB VID/PID ve varsa cihaz üzerindeki ana çip işaretlemesini kaydet; farklı donanım ailesine ait firmware'i zorla yükleme.

### Sinyal çizgileri sabit veya anlamsız görünüyor
- Analizör GND'sinin hedef devre GND'sine doğru bağlandığını doğrula.
- Kanal numaralarını ve test kancalarının renklerini kontrol et.
- CS/CLK/DIN/DOUT sinyallerinin gerçekten hareket ettiğini multimetre yerine mantık yakalamasından değerlendir.
- Örnekleme hızını yükselt ve kısa bir SPI çerçevesini yakala; yine de örnekleme hızı dijital kenarların yakalanmasına uygun olmalıdır.

### SPI decoder yanlış bayt gösteriyor
- SPI modu (CPOL/CPHA), bit sırası (MSB-first/LSB-first), CS aktif seviyesi ve kanal eşlemesini kontrol et.
- Decoder'ın gösterdiği baytları ham dalga biçimiyle karşılaştır.
- Her çerçevenin CS HIGH → LOW geçişiyle başladığını ve CS'nin işlem boyunca doğru kaldığını kontrol et.

## Kaynaklar

1. TLS Robotik — benzer 24 MHz / 8 kanal ürün açıklaması: https://www.tlsrobotik.com/urun/usb-lojik-analizor-24-mhz-8-kanal-mcu-arm-fpga-dsp-hata-ayiklama-araci/
2. sigrok — Noname Saleae Logic clone: https://sigrok.org/wiki/Noname_Saleae_Logic_clone
3. sigrok — fx2lafw: https://sigrok.org/wiki/Fx2lafw
4. sigrok — PulseView indirmeleri: https://sigrok.org/wiki/Downloads
5. PulseView kullanıcı kılavuzu: https://sigrok.org/doc/pulseview/unstable/manual.html
6. SparkFun — USB Logic Analyzer + PulseView kurulum rehberi: https://learn.sparkfun.com/tutorials/using-the-usb-logic-analyzer-with-sigrok-pulseview/all
7. Microchip MCP3208 veri sayfası (SPI çerçevesi için): https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf

**Durum:** Dokümantasyon ve bağlantı planı hazırlandı. SANEC cihazının kendi USB kimliği, PCB revizyonu, giriş eşiği ve gerçek PulseView uyumluluğu fiziksel cihazla henüz doğrulanmadı.
