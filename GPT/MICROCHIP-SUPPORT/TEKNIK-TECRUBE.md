# MCP3204/MCP3208 — BERO teknik tecrübe ve devam notları

Bu dosya, BERO'daki geçmiş denemelerden gelen gözlemleri ve asistanın çalışma sırasında çıkardığı teknik sonuçları ayrı tutar. Destek yazışmasının asıl içeriği için [DESTEK-YAZISMALARI.md](DESTEK-YAZISMALARI.md) dosyasına bak.

## 1. Üretici destek yanıtından alınan temel dersler

1. **Kodun ortalaması ile kodların yayılımı farklı sorunlardır.** VREF = 3,12 V iken 1 LSB yaklaşık 762 µV'dir. 2040–2051 aralığı 11 kodluk, yaklaşık 8,4 mV tepe-tepe yayılıma karşılık gelir. Microchip destek yanıtına göre statik girişte bu yayılımın kaynağı yalnızca ADC'nin ofset/kazanç/INL sınırları olarak varsayılmamalıdır.
2. **Önce sabit giriş testi:** Şartlandırılmış ADC girişini bias noktasına kısa devre edip kod yayılımını yeniden ölç. Yayılım devam ederse bias ağı ve VREF kaynağını incele.
3. **VREF kaynağı kritik:** 3,12 V'un nasıl üretildiğini ve yük altında kararlı olup olmadığını ölç. Direnç bölücüsünün VREF yük akımı ve gürültüsü bakımından uygun olduğu varsayılmamalı. Destek yanıtı tamponlanmış referans ve giriş için op-amp tamponlamasına dikkat çekiyor.
4. **SPI'da sadece “bit kayması” arama:** CS düşükken fazla saat darbeleri sonucun LSB-first tekrarına ve ardından sıfırlara yol açabilir. Başlangıçta CS zaten düşükse ilk işlem bozulabilir; haberleşme öncesinde CS'yi HIGH sonra LOW yaparak yeni çerçeve başlat.
5. **Zamanlama:** MCP3208 sabit saat frekansı/duty cycle gerektirmez; zamanlama sınırları korunmalı. Destek yazışmasında örneklemenin sonundan son veri bitine kadar toplam sürenin en kötü durumda 1,2 ms'yi aşmaması gerektiği belirtiliyor. SPI çerçevesini CS LOW boyunca atomik tutmak iyi bir test yaklaşımıdır.
6. **1 kSPS, 50 Hz akım dalgası için sınırlıdır:** Nyquist sınırı 500 Hz olur. Şebeke harmonikleri ve anahtarlama gürültüsü aliasing yapabilir; uygun analog anti-alias filtresi düşünülmeli. Bu nokta veri sayfasındaki örnekleme/filtre uyarısıyla birlikte ele alınmalı.
7. **173 ms aralık gerçek örnekleme düzenini bozar:** ADC'nin kendisi bu boşluğu oluşturmaz; ana bilgisayar/görev zamanlaması kaynaklıdır. RMS/power hesabında her örneği 1 ms aralıklı varsayma. Zaman damgası al ve örnek aralığını hesaba kat; mümkünse donanım zamanlayıcısı kullan.

## 2. BERO'da önceden kaydedilmiş gözlemler

- ESP32/ESPHome MCP3204/MCP3208 denemelerinde CH0 için tekrarlayan 0.000 V veya yaklaşık 2048 çevresinde okumalar görülmüştü.
- Benzer RX örüntülerinin ADC fiziksel olarak çıkarılmışken de gözlendiği kaydedilmişti. Bu, ADC'nin tek şüpheli olmadığını gösterir; ancak tek başına SPI sürücüsünün hatalı olduğunu kanıtlamaz.
- Daha önce kaydedilmiş bağlantı eşlemesi: ESP32 GPIO18=SCLK, GPIO23=MOSI/DIN, GPIO19=MISO/DOUT, GPIO5=CS. Gerçek bağlantıyı her testte doğrula.
- Önceki test ayarlarında MODE0, 500 kHz, MSB-first, üç bayt transfer ve `((rx[1] & 0x0F) << 8) | rx[2]` decode ifadesi yer aldı. Bunlar tarihsel test notlarıdır, doğrulanmış nihai sürücü değildir.
- VREF=3,12 V ve yaklaşık 1,56 V giriş biası olduğunda beklenen kod yaklaşık 2048'dir. Bu nedenle 2048 civarında okuma tek başına hata değildir; kodun yayılımı ve DMM ile ölçülen giriş gerilimi karşılaştırılmalıdır.
- Önceki ESPHome konfigürasyonunda bileşen adı `mcp3204` olmasına rağmen sekiz kanal (CH0–CH7) okuma hedefi vardı. MCP3204 fiziksel olarak 4, MCP3208 ise 8 tek uçlu kanal sağlar. Yazılım bileşen adıyla fiziksel entegreyi birbirine karıştırma.

## 3. Sonraki test sırası

1. Çip üzerindeki tam işaretlemeyi, paket/pin sayısını ve kanal sayısını doğrula.
2. CS açılışta HIGH olduğundan emin ol; her transfer öncesi CS HIGH→LOW geçişini doğrula.
3. ADC'yi sabit bir DC girişle test et. Aynı anda CHx pinindeki gerilimi DMM ile ölç.
4. VDD, VREF, AGND/DGND ve bias ağını ölç; VREF'in nasıl üretildiğini ve yük altındaki kararlılığını kaydet.
5. Her işlem için ham TX/RX baytlarını sakla; özellikle `rx[1]` içindeki zero bitinin 0 olduğunu kontrol et.
6. Mantık analizöründe CS, CLK, DIN ve DOUT'u yakala; üç baytlık çerçevenin başını/sonunu ve CLK kenarlarını veri sayfasıyla karşılaştır.
7. Sabit giriş kararlı okununca kanalları tek tek doğrula. Sonra CT sensörünü ekle.
8. RMS hesabından önce gerçek örnek zamanlarını kaydet; 1 kSPS varsayımıyla düzensiz örnekleri eşit aralıklı kabul etme.
9. 50 Hz CT ölçümünde analog anti-alias filtresini ve beklenen harmonik bant genişliğini tasarımın parçası yap.

## 4. Veri kaydı şablonu

Her test için kaydet:

- Tarih / firmware ve bileşen sürümü:
- Fiziksel ADC parça işaretlemesi:
- VDD / VREF / bias / CHx DMM ölçümü:
- SPI modu / frekansı:
- TX[0..2] ve RX[0..2]:
- Decode edilen raw kod / hesaplanan gerilim:
- CS/CLK/DIN/DOUT yakalama dosyası:
- Örnek zaman damgaları:
- Beklenen sonuç / gözlenen sonuç:
- Sonuç: doğrulandı / hipotez / çözülemedi:

## 5. Kaynaklar

- Microchip MCP3208: https://www.microchip.com/en-us/product/MCP3208
- Microchip MCP3204: https://www.microchip.com/en-us/product/MCP3204
- MCP3204/3208 DS21298E: https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf
- Microchip sampling-rate/SPI-clock KB: https://support.microchip.com/s/article/Sampling-rate-and-SPI-Clock-frequency-of-MCP3204-MCP3208
- Microchip AN699 (anti-aliasing filter context): https://ww1.microchip.com/downloads/en/Appnotes/00699b.pdf

**Durum:** Bu, çalışma notudur. Burada yazanlar gerçek donanım testi yerine geçmez; destek yanıtından aktarılan tavsiyeler ve BERO'da gözlenenler test sırasında yeniden doğrulanmalıdır.
