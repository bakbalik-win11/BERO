# TCA9548A — I²C çoklayıcı / kanal anahtarı donanım kaydı

## Kimlik ve envanter

- **Bileşen:** TCA9548A tabanlı I²C multiplexer / switch breakout kartı.
- **Adet:** 2 adet.
- **Stok durumu:** Sipariş edildi; teslimat bekleniyor (kullanıcı bildirimi).
- **Üretici entegresi:** Texas Instruments TCA9548A.
- **Breakout kartı üreticisi / satıcı / SKU / PCB revizyonu:** Teslimatta kart üzerindeki işaret ve ürün bilgisiyle doğrulanacak.
- **Kullanım amacı:** Aynı I²C veri yolunda aynı adrese sahip birden fazla cihazı ayrı kanallara ayırarak erişilebilir kılmak. BERO'da özellikle birden fazla ADS1115 modülünü aynı ESP32 I²C hattında kullanma olasılığını değerlendirmek.

## Üretici entegresi — TCA9548A

TCA9548A, Texas Instruments üretimi, I²C/SMBus uyumlu, 8 kanallı, çift yönlü I²C anahtarıdır. Ana taraftaki SDA/SCL hattını seçilen aşağı-akış kanallarından bir veya birkaçına bağlar.

| Özellik | Üretici verisi |
|---|---|
| Kanal sayısı | 8 çift yönlü kanal |
| I²C saat frekansı | 100 kHz ve 400 kHz modları; azami 400 kHz |
| Besleme aralığı | 1,65–5,5 V |
| I²C adres seçimi | A0, A1, A2 pinleri; en fazla 8 TCA9548A aynı ana veri yolunda |
| Kanal seçimi | I²C üzerinden 8 bit kontrol yazmacı; her bit bir kanalı kontrol eder |
| RESET | Aktif düşük reset girişi |
| Açılış durumu | Tüm kanallar seçilmemiş başlar |
| Seviye dönüştürme | Uygun besleme ve pull-up düzeniyle farklı gerilim alanları arasında geçişi destekler |
| Çalışma sıcaklığı | −40 °C … +85 °C |

**Çalışma prensibi:** TCA9548A, sekiz bağımsız I²C master üretmez; tek bir ana I²C hattını sekiz seçilebilir aşağı-akış dalına ayırır. Kanal seçimi kontrol yazmacıyla yapılır. Birden fazla kanal aynı anda açılabilir; aynı adrese sahip cihazlar aynı anda açık kanallarda bulunursa adres çakışması devam edebilir. Aynı adresli cihazları ayrı ayrı okumak için ilgili kanalı tek başına seçmek uygundur.

## BERO kullanım gerekçesi — ADS1115

ADS1115'in I²C adresi ADDR bağlantısına göre belirlenir. Aynı adrese ayarlanmış birden fazla ADS1115 doğrudan aynı I²C hattına bağlandığında adres çakışması oluşur. TCA9548A ile her ADS1115 ayrı bir aşağı-akış kanalına bağlanabilir; yazılım önce ilgili kanalı seçer, ardından ADS1115 ile haberleşir.

Örnek topoloji (henüz kurulmuş/denenmiş bağlantı değildir):

- ESP32 SDA/SCL → TCA9548A ana SDA/SCL.
- TCA9548A kanal 0 SDA/SCL → ADS1115-01.
- TCA9548A kanal 1 SDA/SCL → ADS1115-02.
- Diğer ADS1115 modülleri gerekirse ayrı kanallara dağıtılır.
- Her ADS1115'in beslemesi ve GND ortak referansı, kartların gerçek devre yapısına göre tasarlanır ve ölçülerek doğrulanır.

İki adet TCA9548A kartı toplamda 16 kanal anlamına gelebilir; ancak bu, iki kartın aynı hatta bağlanmasının veya 16 ADS1115'in tek seferde sorunsuz çalışmasının otomatik garantisi değildir. TCA9548A adres pinleri, pull-up dirençleri, toplam hat kapasitansı, kablo uzunluğu, besleme ve kanal seçimi yazılımı doğrulanmalıdır.

## Bağlantı doğrulama ve dikkat noktaları

- Breakout kartının VCC, GND, SDA, SCL, A0–A2 ve RESET pin sırası kart üzerindeki baskı/şema ile teyit edilmelidir; farklı üreticilerin kart pin dizilimi varsayılmamalıdır.
- TI entegresi 1,65–5,5 V besleme aralığını destekler. Bu bilgi breakout kartındaki pull-up dirençlerinin hangi gerilime bağlı olduğunu tek başına göstermez.
- ESP32 GPIO'ları 5 V toleranslı değildir. SDA/SCL pull-up gerilimi ESP32 lojik seviyesine uygun olmalıdır.
- TCA9548A seviye geçişi sağlayabilir; ancak kart üzerindeki pull-up ve besleme topolojisi incelenmeden 5 V I²C hattı güvenli kabul edilmemelidir.
- I²C hattı 400 kHz ile sınırlandırılmıştır; kablo ve toplam kapasitans arttıkça daha düşük hız gerekebilir.
- Kanal değiştirme, seçili kanalın sensör adres taraması ve kanal kapatma davranışı firmware ile test edilmelidir.
- RESET pininin nasıl sürüleceği (GPIO veya uygun sabit lojik seviyesi) kart ve sistem tasarımında belirlenecektir.

## BERO doğrulama planı

1. İki kartın teslim alınması, adet ve PCB üzeri entegre işaretinin kontrolü.
2. Kart pin sırası, A0/A1/A2 ve RESET bağlantılarının fotoğraf/şema ile kaydı.
3. Besleme ve SDA/SCL pull-up gerilimlerinin multimetreyle ölçülmesi.
4. ESP32 ile TCA9548A ana I²C haberleşmesinin doğrulanması.
5. Tek bir ADS1115'i bir kanala bağlayıp kanal seçimi ve I²C taraması yapılması.
6. Aynı I²C adresindeki ikinci ADS1115'i başka kanala bağlayıp her iki kanalın ayrı ayrı okunması.
7. Kanal izolasyonu, birden fazla kanal açıkken davranış ve I²C hata/kilitlenme durumlarının loglanması.
8. Ancak bu testlerden sonra çoklu ADS1115 bağlantısı BERO donanım mimarisine alınır.

## Üretici kaynağı

- [Texas Instruments — TCA9548A ürün sayfası ve veri sayfası (Rev. H)](https://www.ti.com/product/TCA9548A)
- [Texas Instruments — TCA9548A datasheet PDF, SCPS207H](https://www.ti.com/lit/ds/symlink/tca9548a.pdf)

**Kayıt sınırı:** Yukarıdaki teknik özellikler TI TCA9548A entegresine aittir. Sipariş edilen iki breakout kartının fiziksel pin dizilimi, pull-up dirençleri, adres jumper'ları ve gerçek kart revizyonu teslimatta doğrulanacaktır. Bu kayıt, modülün BERO'da çalıştığını veya çoklu ADS1115 bağlantısının test edildiğini göstermez.
