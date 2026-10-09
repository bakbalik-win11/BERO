# Microchip Support — MCP3204/MCP3208 yazışmaları

Bu belge, kullanıcının paylaştığı Microchip teknik destek yazışmalarını kaynak metin olarak saklar. Aktarımda teknik ayrıntılar ve tarih/saat bilgileri korunmuştur. Destek yanıtındaki ifadeler, BERO donanımında ölçümle doğrulanmış sonuçlar anlamına gelmez.

## 1. Emanuel B. — 10/08/2026, 16:16

Merhaba Burak,

Onayladığınız için teşekkürler. Geçen sefer değinmediğim birkaç nokta daha var.

Asıl soru, merkez değil, yayılımdır. VREF = 3,12 V'de bir LSB 762 µV'dir, bu nedenle 2040–2051 yaklaşık 8,4 mV tepe-tepe değerine karşılık gelir. Cihaz bunu üretemez: ofset maksimum ±3 LSB, kazanç maksimum ±5 LSB, INL maksimum ±2 LSB'dir (s.2) ve bunlar okumayı kaydırmak yerine, okumanın rastgele hareket etmesine neden olmaz. Tipik SINAD 72 dB (s.2) ile statik bir girişte on bir değil, iki veya üç sayım hareketi beklersiniz. Bu nedenle, şartlandırılmış girişi bias noktasına kısa devre yapın ve yayılımı yeniden ölçün — eğer 8,4 mV devam ederse, sorun ADC'de değil, bias ağınızda veya referansınızdadır.

3,12 V'un nasıl üretildiğini kontrol edin. Bu standart bir referans çıkışı değil, bu da 3,3 V'luk bir bölücü veya ölçülmüş bir LDO'yu düşündürüyor. Yasal bir değer, ancak VREF tipik olarak 100 µA / maksimum 150 µA çekiyor (s.2) ve "referans cihazının çalışmasındaki herhangi bir kararsızlık, A/D dönüştürücünün çalışmasını doğrudan etkileyecektir" (s.17). Dirençli bir bölücü bu yüke dayanamaz ve VREF gürültüsü kodu doğrudan ölçeklendirir. Şekil 6-3 (s.23), amaçlanan düzenlemeyi gösteriyor: tamponlanmış bir referans artı girişi süren bir op amp.

Ham baytlarınızda kontrol etmeniz gereken iki hizalama hatası modu var ve bunların hiçbiri bit kayması gibi görünmüyor:

- CS hala düşükken ek saatler, sonucu önce LSB (Şekil 5-2) olarak yeniden üretir, ardından süresiz olarak sıfırlar (s.19) — bu nedenle çok uzun bir işlem, kaydırılmış değil, aynalanmış veri verir.
- Eğer parça CS zaten düşükken çalışmaya başlarsa, "iletişimi başlatmak için yükseltilip tekrar düşürülmelidir" (s. 19). ESP32 GPIO önyükleme durumuna bağlı olarak, bu sıfırlamadan sonraki ilk işlemi geçersiz kılabilir.

Atomik transferler konusunda gerekenden daha katı davrandım. Parça "tüm zamanlama özelliklerine uyulduğu sürece sabit bir saat hızı veya görev döngüsü gerektirmez" (s. 22). Çerçeve ortasında uzatılmış bir saat sorun değil; tek kısıtlama, 85 °C'lik en kötü durum olan toplam 1,2 ms'dir (s. 22).

1 kSPS'de arayüzden daha önemli iki şey var. Sınırınız 500 Hz'dir - sadece 50 Hz'nin 10. harmonik frekansı - bu nedenle gerçek CT harmonikleri ve anahtarlama gürültüsü bandınıza karışır ve daha sonra giderilemez; veri sayfası bir anti-aliasing filtresi önerir (sayfa 22, bkz. AN699). Ayrı olarak, ve bu veri sayfasından ziyade mantık yürütmedir: 173 ms'lik sapma dönüştürücü için zararsızdır ancak ölçüm için zararlıdır, çünkü RMS ve güç entegrasyonu tekdüze aralık varsayar ve geç bir örnek hala 1 ms olarak ağırlıklandırılır. ADC'yi bir donanım zamanlayıcısından sürün veya her örneğe zaman damgası ekleyin ve ağırlıklandırın. Bu, kesme tabanlı SPI'ye kıyasla doğruluğunuzu çok daha fazla etkiler.

Ölçülen kanal voltajı ve çözümlenen kod uyuşmuyorsa, ham TX/RX baytlarını ve bu dönüşüm için CS, CLK, DIN ve DOUT sinyallerinin yakalanmasını gönderin. Uyuşuyorsa, referans ve CT bias ağının nasıl oluşturulduğunu gönderin.

Saygılarımla,

Teknik Destek

## 2. Burak Akbalık — 10/06/2026, 16:24

MERHABA,

Detaylı ve yardımcı cevabınız için çok teşekkür ederim.

MCP3208 SPI çerçeve formatı, zamanlama gereksinimleri ve yaklaşık 2048 ADC kodunun yorumlanmasına ilişkin açıklamalarınız, araştırmamız için çok faydalı oldu.

Önerilen kontrolleri, özellikle de şunları yapacağız:

- Ham SPI işlemini doğrulama ve kod çözme,
- sıfır bitini kontrol etmek,
- ADC giriş voltajını bir DMM ile ölçmek,
- 1 MHz SPI'yı muhafazakar test koşulu olarak kullanarak,
- ADC işlem zamanlamasını ESP32 ana bilgisayar/görev zamanlamasından ayırmak.

Ayrıca, her 3 baytlık SPI işleminin atomik kaldığını ve örneklemenin sonundan son veri bitine kadar geçen sürenin belirtilen sınır içinde kaldığını da doğrulayacağız.

DMM ölçümleri ve ADC sonuçları uyuşmuyorsa, daha detaylı inceleme için CS, CLK, DIN ve DOUT'un mantık analizörü yakalama verilerini ve ham RX baytlarını sağlayacağız.

Teknik rehberliğiniz ve desteğiniz için tekrar teşekkür ederim.

Saygılarımla,

Burak Akbalık
Türkiye

## 3. Emanuel B. — 10/06/2026, 16:17

Merhaba Burak,

Detaylı açıklama için teşekkür ederim.

Planladığınız yaklaşım (1 MHz saat frekansı, doğrulanmış SPI modu, ham bayt incelemesi, ADC zamanlamasının Wi-Fi görevlerinden ayrılması) uygundur.

Aşağıdaki noktalar sonuçları yorumlamanıza yardımcı olacaktır.

### 3.1 SPI modu ve çerçeve formatı

- MCP3208, SPI modları 0,0 ve 1,1'i destekler (DS21298E, s.1).
- MCU, düşen kenarda veri çıkışı yapmalı ve yükselen kenarda veri girişi yapmalıdır. Her iki modda da ADC, düşen kenarlarda veri çıkışı yapar (s.21).
- Veri sayfasında önerilen 3 baytlık işlem Şekil 6-1 / 6-2'de (s.21–22) gösterilmiştir:
  - TX baytı 1: beş önde sıfır, ardından Start, SGL/DIFF ve D2.
  - TX baytı 2: D1 ve D0, ardından önemsiz bitler.
  - TX baytı 3: önemsiz bitler.
  - RX baytı 2: üç bilinmeyen bit, sıfır biti ve en yüksek dereceli dört bit. RX baytı 3, B7–B0'ı içerir.
- Tek uçlu CH0 için (Tablo 5-2, s.19: SGL=1, D2=D1=D0=0), TX = `0x06, 0x00, 0x00` olur.
- Sonuç `((rx[1] & 0x0F) << 8) | rx[2]` olarak çözülür.
- Faydalı kontrol: rx[1]'in 4. biti sıfır bitidir ve her zaman 0 değerini göstermelidir (s.19).

### 3.2 VDD yaklaşık 3,3 V iken zamanlama

- Belirtilen maksimum fCLK değerleri VDD = 5 V'de 2,0 MHz ve VDD = 2,7 V'de 1,0 MHz'dir. 3,3 V değeri verilmediğinden, 1 MHz muhafazakâr bir seçimdir.
- tHI ve tLO'nun her birinin minimum süresi 250 ns'dir.
- tSUCS (CS düşüşünden ilk CLK yükselişine kadar geçen süre) minimum 100 ns'dir.
- DIN kurulum (tSU) ve tutma (tHD) süreleri her biri minimum 50 ns'dir.
- tDO (CLK'nin DOUT'a düşmesi geçerli) maksimum 200 ns'dir.
- tCSH (dönüşümler arasında CS yüksekliği) minimum 500 ns'dir. CS, dönüşümler arasında yüksek seviyeye çekilmelidir (s.15).
- Microchip KB makalesi: https://support.microchip.com/s/article/Sampling-rate-and-SPI-Clock-frequency-of-MCP3204-MCP3208

### 3.3 Bir bit hatası yaklaşık 2048 değerini üretebilir mi?

- Yanlış hizalanmış bir çerçeve, orta ölçek etrafında sıkı bir küme yerine belirgin kodlar üretme eğilimindedir.
- Bir bitlik kaydırma, kodu yaklaşık olarak yarıya indirir veya iki katına çıkarır.
- Bilinmeyen bitlerin maskelenmemesi 4095'in üzerinde değerler verebilir.
- 2040–2051 aralığı (0x7F8–0x803), VREF/2'ye yakın gerçek bir analog gerilime daha çok benzer. Tek uçlu modda giriş aralığı VSS ile VREF arasındadır; CT sinyali DC biaslı olmalıdır.
- VREF = 3,12 V olduğunda 2048 kodu VIN ≈ 1,56 V'ye karşılık gelir.
- CHx pinindeki DC voltajını DMM ile ölçüp Kod = 4096 × VIN / VREF bağıntısıyla karşılaştırın.
- Kaynak empedansı, ADC'nin yaklaşık 20 pF örnekleme kapasitörünü şarj eden dahili 1 kΩ anahtara eklenir; bu, ofset, kazanç ve INL hatalarını artırabilir. Kaynak düşük empedanslı değilse tamponlama önerilir.

### 3.4 173 ms örnek aralığı

- MCP3208'de BUSY sinyali yoktur; ana bilgisayayı geciktiremez.
- Örnekleme 1,5 saat döngüsü, dönüşüm 12 saat döngüsü alır (s.2).
- 1 MHz'de 24 saatlik bir çerçeve yaklaşık 24 µs sürer; 1 kSPS, her 1 ms'lik periyodun küçük bir bölümünü kullanır.
- 173 ms'lik boşluk ana bilgisayar tarafında oluşur.
- Görev anahtarı CS düşükken çerçeve ortasında saati duraklatırsa örnekleme kapasitöründen şarj boşalabilir. Örneklemenin sonundan son veri bitine kadar geçen süre en kötü durumda 1,2 ms'yi geçmemelidir (s.22). Her 3 baytlık aktarımı atomik tutmak ve mümkünse CS'nin çevre birimi tarafından kontrol edildiği tek bir donanım SPI işlemi olarak gerçekleştirmek önerilir.
- Veri sayfası, kesme tabanlı ve yoklama tabanlı ESP32 SPI arasındaki seçimi ele almaz; bu, ESP32/ESP-IDF davranışıdır.

### 3.5 Donanım

- Cihaza yakın 1 µF bypass kondansatörü (s.23).
- AGND ve DGND'yi analog topraklama düzlemine bağlama (s.24).
- CLK izini analog izlerden uzak tutma (s.23).

DMM ölçümü okuma ile uyuşmuyorsa CS, CLK, DIN ve DOUT mantık analizörü yakalamasını ve ham RX baytlarını Microchip desteğine gönderin.

---

## Kaynak bağlantıları

- MCP3204/3208 veri sayfası DS21298E: https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf
- Microchip KB — örnekleme hızı ve SPI saat frekansı: https://support.microchip.com/s/article/Sampling-rate-and-SPI-Clock-frequency-of-MCP3204-MCP3208

**Kaynak notu:** Bu dosyadaki destek yazışmaları kullanıcı tarafından paylaşılan metinden aktarılmıştır. Alıntılanan sayfa ve tablo numaraları, yazışmadaki atıflardır; gerektiğinde güncel veri sayfasından ayrıca teyit edilmelidir.
