# ESP32-DevKitC / ESP32-WROOM-32D — Pin Rehberi

> **Önemli:** Bu rehber, paylaşılan pinout görseliyle uyumlu ESP32-DevKitC V4 + ESP32-WROOM-32D düzenini esas alır. Kartın gerçek revizyonunu ve modül üzerindeki yazıyı kontrol et. DevKitC kart pinleri ile çıplak WROOM modülünün pinleri aynı şey değildir.

## Öncelikle bilinmesi gerekenler

- ESP32 GPIO'ları **3.3 V mantık seviyesindedir**. GPIO'ya 5 V uygulama.
- **GPIO34–GPIO39 yalnızca giriş** olarak kullanılabilir; dahili pull-up/pull-down yoktur.
- **GPIO6–GPIO11** modülün SPI flash belleğiyle bağlantılıdır. Genel GPIO olarak kullanma.
- **GPIO0, GPIO2, GPIO5, GPIO12, GPIO15** açılış yapılandırmasını etkileyen strapping pinleridir. Harici devreler açılış seviyelerini bozabilir. Özellikle GPIO12'nin reset anında HIGH olması bazı flash besleme yapılandırmalarında boot sorununa neden olabilir.
- **ADC2**, Wi-Fi kullanılırken kısıtlanabilir. Wi-Fi ile analog ölçüm gerekiyorsa ADC1 pinleri (GPIO32–GPIO39) genellikle daha uygun başlangıçtır.
- GPIO işlevlerinin çoğu GPIO Matrix üzerinden farklı pinlere atanabilir; aşağıdaki UART/SPI/I²C işlevleri yaygın varsayılanlardır, tek seçenek değildir.
- DevKitC kartını USB, 5V-GND veya 3V3-GND seçeneklerinden **yalnızca biriyle** besle. Beslemeleri aynı anda bağlama.
- GND ortak referanstır. 3V3 pinini bir GPIO gibi kullanma.

## Güç ve kontrol pinleri

### 3V3
- İşlev: Kartın 3.3 V güç rayı.
- Dikkat: Harici 3.3 V ile besleme yapılacaksa DevKitC kılavuzundaki güç seçeneğine uy; USB/5V beslemesiyle aynı anda kullanma.

### 5V / 5V0
- İşlev: USB/VIN tarafındaki 5 V güç hattı.
- Dikkat: GPIO seviyesi değildir. 5 V'u doğrudan GPIO'ya bağlama.

### GND
- İşlev: Toprak / ortak elektriksel referans.
- Dikkat: Harici sensör ve ADC devrelerinin referansı, devre tasarımına göre ortaklanmalıdır.

### EN
- İşlev: Chip enable / reset. LOW tutulursa ESP32 çalışmaz; HIGH olduğunda çalışabilir.
- Kullanım: Reset için kısa süre LOW çekilebilir.
- Dikkat: Normal çalışmada HIGH seviyesinde kalmalıdır; rastgele GPIO olarak kullanma.

## GPIO pinleri — pin pin

### GPIO0
- İşlev: Dijital giriş/çıkış; ADC2_CH1; Touch T1.
- Özel durum: Boot strapping pinidir; BOOT düğmesi bu pini LOW yaparak indirme moduna alabilir.
- Kullanım: Genel GPIO olarak kullanılabilir ama bağlı devrenin reset anında seviyeyi bozmadığını doğrula.

### GPIO1 (U0TXD / TX)
- İşlev: UART0 seri verici; dijital GPIO.
- Varsayılan kullanım: USB-UART üzerinden log ve programlama çıktısı.
- Risk: Harici devre UART mesajlarını bozabilir; seri log kullanıyorsan başka işlev için ayırma.

### GPIO2
- İşlev: Dijital GPIO; ADC2_CH2; Touch T2.
- Özel durum: Boot strapping pinidir; reset sırasındaki seviye boot davranışını etkileyebilir.

### GPIO3 (U0RXD / RX)
- İşlev: UART0 seri alıcı; dijital GPIO.
- Varsayılan kullanım: USB-UART üzerinden programlama/seri iletişim.
- Risk: Harici devre RX hattına veri sürerse yükleme veya seri haberleşme etkilenebilir.

### GPIO4
- İşlev: Dijital GPIO; ADC2_CH0; Touch T0.
- Kullanım: Genel I/O için uygundur; ADC2'nin Wi-Fi kısıtını dikkate al.

### GPIO5
- İşlev: Dijital GPIO; VSPI varsayılan CS/SS işlevi.
- Özel durum: Boot strapping pinidir; harici devre reset seviyesini etkileyebilir.

### GPIO6
- İşlev: SPI flash CLK hattı.
- Durum: **KULLANMA — flash için ayrılmıştır.**

### GPIO7
- İşlev: SPI flash D0 hattı.
- Durum: **KULLANMA — flash için ayrılmıştır.**

### GPIO8
- İşlev: SPI flash D1 hattı.
- Durum: **KULLANMA — flash için ayrılmıştır.**

### GPIO9
- İşlev: SPI flash D2 hattı.
- Durum: **KULLANMA — flash için ayrılmıştır.**

### GPIO10
- İşlev: SPI flash D3 hattı.
- Durum: **KULLANMA — flash için ayrılmıştır.**

### GPIO11
- İşlev: SPI flash CMD hattı.
- Durum: **KULLANMA — flash için ayrılmıştır.**

### GPIO12 (MTDI)
- İşlev: Dijital GPIO; ADC2_CH5; Touch T5; JTAG MTDI.
- Özel durum: Boot strapping pini; reset anındaki seviyesi önemlidir.
- Risk: Reset anında HIGH olması bazı flash besleme yapılandırmalarında boot sorununa neden olabilir.

### GPIO13 (MTCK)
- İşlev: Dijital GPIO; ADC2_CH4; Touch T4; JTAG MTCK.
- Kullanım: Genel I/O; JTAG kullanılıyorsa debug işleviyle paylaşılır.

### GPIO14 (MTMS)
- İşlev: Dijital GPIO; ADC2_CH6; Touch T6; JTAG MTMS; yaygın VSPI SCLK alternatifi.
- Kullanım: Genel I/O veya uygun SPI sinyali.

### GPIO15 (MTDO)
- İşlev: Dijital GPIO; ADC2_CH3; Touch T3; JTAG MTDO.
- Özel durum: Boot strapping pinidir; harici devre reset seviyesini etkileyebilir.

### GPIO16
- İşlev: Dijital GPIO.
- Kullanım: WROOM-32D modüllü DevKitC V4 kartlarında genellikle kullanılabilir.
- Dikkat: WROVER gibi farklı modül varyantlarında GPIO16 dahili işlevler için ayrılmış olabilir.

### GPIO17
- İşlev: Dijital GPIO.
- Kullanım: WROOM-32D modüllü DevKitC V4 kartlarında genellikle kullanılabilir.
- Dikkat: WROVER gibi farklı modül varyantlarında GPIO17 dahili işlevler için ayrılmış olabilir.

### GPIO18
- İşlev: Dijital GPIO; yaygın VSPI SCLK.
- Kullanım: SPI saat sinyali için sık kullanılan seçim.

### GPIO19
- İşlev: Dijital GPIO; yaygın VSPI MISO.
- Kullanım: SPI veri girişi (ESP32'ye doğru).

### GPIO21
- İşlev: Dijital GPIO; yaygın I²C SDA.
- Kullanım: I²C veri hattı için sık kullanılan varsayılan.

### GPIO22
- İşlev: Dijital GPIO; yaygın I²C SCL.
- Kullanım: I²C saat hattı için sık kullanılan varsayılan.

### GPIO23
- İşlev: Dijital GPIO; yaygın VSPI MOSI.
- Kullanım: SPI veri çıkışı (ESP32'den çevre birimine).

### GPIO25
- İşlev: Dijital GPIO; ADC2_CH8; DAC1 çıkışı.
- Kullanım: Dijital I/O veya uygun koşullarda DAC/ADC2.

### GPIO26
- İşlev: Dijital GPIO; ADC2_CH9; DAC2 çıkışı.
- Kullanım: Dijital I/O veya uygun koşullarda DAC/ADC2.

### GPIO27
- İşlev: Dijital GPIO; ADC2_CH7; Touch T7.
- Kullanım: Genel I/O; ADC2/Wi-Fi kısıtını dikkate al.

### GPIO32
- İşlev: Dijital GPIO; ADC1_CH4; Touch T9; 32.768 kHz kristal işlevi.
- Kullanım: ADC1 analog giriş veya genel I/O.

### GPIO33
- İşlev: Dijital GPIO; ADC1_CH5; Touch T8; 32.768 kHz kristal işlevi.
- Kullanım: ADC1 analog giriş veya genel I/O.

### GPIO34
- İşlev: **Yalnızca giriş**; ADC1_CH6.
- Kullanım: Analog/dijital sensör girdisi.
- Dikkat: Çıkış veremez; dahili pull-up/pull-down yoktur.

### GPIO35
- İşlev: **Yalnızca giriş**; ADC1_CH7.
- Kullanım: Analog/dijital sensör girdisi.
- Dikkat: Çıkış veremez; dahili pull-up/pull-down yoktur.

### GPIO36 (VP / SENSOR_VP)
- İşlev: **Yalnızca giriş**; ADC1_CH0.
- Kullanım: Analog ölçüm girdisi.
- Dikkat: Çıkış veremez; dahili pull-up/pull-down yoktur.

### GPIO39 (VN / SENSOR_VN)
- İşlev: **Yalnızca giriş**; ADC1_CH3.
- Kullanım: Analog ölçüm girdisi.
- Dikkat: Çıkış veremez; dahili pull-up/pull-down yoktur.

## DevKitC başlıklarındaki özel adlar

- **VP** = GPIO36 = ADC1_CH0 (yalnızca giriş).
- **VN** = GPIO39 = ADC1_CH3 (yalnızca giriş).
- **TX** = GPIO1 / U0TXD.
- **RX** = GPIO3 / U0RXD.
- **D0 / D1 / D2 / D3 / CMD / CLK** = sırasıyla GPIO7 / GPIO8 / GPIO9 / GPIO10 / GPIO11 / GPIO6; modül flash belleğine bağlı olduklarından kullanma.
- **3V3, 5V, GND, EN** GPIO değildir.

## SPI için yaygın VSPI pinleri

- SCLK: GPIO18
- MISO: GPIO19
- MOSI: GPIO23
- CS/SS: GPIO5 (başlangıç seviyesi nedeniyle harici devreyi kontrol et; başka uygun GPIO seçilebilir)

ESP32 GPIO Matrix nedeniyle SPI sinyalleri başka uygun GPIO'lara da atanabilir. SPI çevre birimi, kart ve kütüphane ayarlarını birlikte doğrula.

## I²C için yaygın varsayılanlar

- SDA: GPIO21
- SCL: GPIO22

I²C pinleri yazılımla değiştirilebilir; gerçek firmware yapılandırmasını kontrol et.

## Kaynaklar

- Espressif — ESP32-DevKitC V4 User Guide: https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html
- Espressif — Pin Layout: https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html#pin-layout
- Espressif — ESP32-WROOM-32D / 32U Datasheet: https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf
