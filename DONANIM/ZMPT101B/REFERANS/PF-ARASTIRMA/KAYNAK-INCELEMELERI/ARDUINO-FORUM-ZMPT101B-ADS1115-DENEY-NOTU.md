# Arduino Forum Deney Notu — ZMPT101B + ADS1115

- Tarih: 2026-11-22
- Kaynak: [Arduino Forum — Using ZMPT101B with ADS1115](https://forum.arduino.cc/t/using-zmpt101b-with-ads1115/1434976)
- Konu başlangıcı: 12.03.2026
- Son ilgili mesajlar: 20.08.2026
- Belge türü: Kullanıcı deneyimi ve teknik forum tartışması; üretici veri sayfası veya kontrollü laboratuvar raporu değildir.

## 1. Tartışmanın konusu

Konu sahibi ESP32 ve ADS1115 kullanırken, Arduino GPIO pini bekleyen ZMPT101B kütüphanesini harici ADC ile kullanmaya çalışıyor. Örnek olarak `ZMPT101B voltageSensor(ads_1.readADC_SingleEnded(2), 60.0)` çağrısının beklenen biçimde çalışmadığını gösteriyor.

Forumda paylaşılan kütüphane kaynak kodunda:
- Kurucu fonksiyon analog pin numarası alıyor.
- `pinMode(pin, INPUT)` çağrılıyor.
- Sıfır noktası ve RMS ölçümü boyunca `analogRead(pin)` kullanılıyor.

Bu nedenle ADS1115 okumasını Arduino pin numarası gibi vermek doğrudan uyumlu değildir. Forum önerisi, harici ADC okumasını doğrudan uygulama içinde yapmak veya harici ADC okuma fonksiyonunu destekleyen ayrı/genel bir kütüphane arayüzü kullanmaktır.

## 2. Forum katılımcılarının paylaştığı gözlemler

- Konu sahibi 60 saniyelik kendi testinde ADS okuma sayısını 1.213 okuma/s, ESP32 GPIO ADC okuma sayısını 24.196 okuma/s olarak bildirmiştir. Bu, forum kullanıcısının kendi yazılım/test düzenindeki ölçümüdür; ADS1115'in veri sayfası örnekleme hızı olarak alınmamalıdır.
- Başka bir katılımcı ADS1115 veri sayfasındaki azami 860 SPS değerini hatırlatmış ve çoklu kanal kullanımında kanal başına hızın düşeceğine dikkat çekmiştir.
- 18.08.2026 tarihli mesajda bir katılımcı, ZMPT101B modülünün analog koşullandırma yaptığı; ADS1115'ten ham örnekleri doğrudan okuyup ortalamayı çıkararak RMS hesabı yapılabileceği yaklaşımını önermiştir. Aynı mesaj, ADS1115'in örnekleme hızını yetersiz bulduğunu ve kendi uygulamasında STM32 ADC kullandığını belirtir.
- Aynı mesaj, ZMPT101B transformatörünün ölçülen gerilim dalgasına birkaç derecelik faz kayması ekleyebileceği uyarısını yapar. Bu ifade forum katılımcısının genel deney/yorumudur; bizim satın aldığımız kartın ölçülmüş faz değeri değildir.
- 20.08.2026 tarihli son mesajlardan biri, ADS1115 ile yarım periyot başına sekizden az örnek elde edildiği yönünde uyarı yapar. Bu yorum, tek kanal kullanımına ilişkin forum tartışmasıdır; gerçek kart ve yazılım düzenimizde ayrıca ölçülmelidir.

## 3. BERO için çıkarımlar

1. Eski ZMPT101B Arduino kütüphanesinin analog GPIO pini bekleyen arayüzü ADS1115 kanal okumasına doğrudan uymaz.
2. BERO deneyinde hazır kütüphaneyi zorlamak yerine ADS1115 ham kodlarını okuyup DC ortalamayı çıkaran, RMS hesabını yapan ve ham örnekleri kaydeden bağımsız bir ölçüm yolu tercih edilebilir.
3. ADS1115'in nominal azami dönüşüm hızı 860 SPS'dir. İki kanalın dönüşümleri sırayla yapılır; ADC eşzamanlı iki kanal örneklemez. Kanal başına efektif örnekleme hızı ve kanal arası zaman farkı gerçek sistemde ölçülmelidir.
4. 50 Hz sinyalde örnekleme sayısının sınırlı olması dalga şekli temsili, RMS kararlılığı ve özellikle gerilim-akım örneklerinin hizalanması açısından deneysel risk oluşturur.
5. ZMPT101B'nin faz gecikmesi, hazır kartın LM358/filtre katı ve gerçek PCB revizyonuyla birlikte ölçülmelidir. Forumdaki “birkaç derece” ifadesi sabit kalibrasyon katsayısı olarak kullanılmayacaktır.
6. PZEM ile gerilim ve akım RMS karşılaştırması genlik kalibrasyonuna yardımcı olabilir; faz gecikmesini tek başına kalibre etmez.
7. FNIRSI 2D15P ile düşük gerilimli/izole test sinyallerinde dalga biçimi, sıfır geçişi ve iki kanal zaman farkı incelenebilir. Şebeke ölçüm bağlantısı için uygun izolasyon/prob güvenliği ayrıca doğrulanmalıdır.

## 4. Önerilen deney sırası

- [ ] ZMPT101B kartı teslim alındığında PCB revizyonu, op-amp işareti, pin sırası ve besleme aralığı fotoğrafla kaydedilecek.
- [ ] Önce güvenli, düşük gerilimli ve izole bir AC kaynakla OUT sinyalinin DC ofseti, genliği ve kırpılması gözlenecek.
- [ ] ADS1115 tek kanal okuma hızı zaman damgalı testle ölçülecek.
- [ ] İki kanal sırayla okunduğunda efektif kanal hızları ve A0/A1 ile A2 arasındaki dönüşüm zaman farkı ölçülecek.
- [ ] Ham örnekler kaydedilip ortalama çıkarma ve RMS hesabı çevrimdışı doğrulanacak.
- [ ] SCT013 ile ortak zaman tabanında örnekleme ve faz karşılaştırması ayrıca değerlendirilecek.
- [ ] PZEM karşılaştırması RMS genlik kontrolü için kullanılacak; PZEM faz referansı gibi kabul edilmeyecek.

## 5. Kaynak sınırları ve doğrulama

Bu forum konusu bir üretici teknik belgesi değildir. Katılımcıların örnek kodu, test hızları ve faz kayması yorumları kendi sistemlerine aittir. Bunlar BERO kartının doğrulanmış performans verileri olarak kopyalanmayacaktır.

ADS1115'in 860 SPS sınırı ve kanal çalışma biçimi için üretici veri sayfası esas alınmalıdır. Forumda bildirilen 1.213 okuma/s değerinin ADC'nin gerçek dönüşüm hızı olduğu varsayılmayacaktır.

## Durum

- Forum bağlantısı ve BERO'ya ilişkin teknik notlar kaydedildi.
- ZMPT101B kartı henüz fiziksel olarak test edilmedi.
- ADS1115 ile ZMPT101B + SCT013 PF ölçümü uygulanmış veya doğrulanmış değildir.
