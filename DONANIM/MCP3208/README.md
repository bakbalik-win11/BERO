# MCP3208 — Donanım ve üretici referansı

## Kimlik ve kapsam

MCP3208, Microchip Technology üretimi **12 bit, 8 kanallı, SPI arayüzlü SAR ADC**'dir. MCP3204 ile aynı ailede olsa da kanal sayısı ve paket/pin dizilimi farklıdır. Parça üstündeki işaretlemeyi ve fiziksel paketi kontrol etmeden MCP3204 ile MCP3208'i birbirinin yerine kabul etme.

- MCP3204: 4 tek uçlu analog kanal; 14 pinli paket seçenekleri.
- MCP3208: 8 tek uçlu analog kanal; 16 pinli paket seçenekleri.
- Çözünürlük: 12 bit, ham kod aralığı 0–4095.
- Besleme çalışma aralığı: 2,7–5,5 V.
- Referans: VREF, VDD'yi aşmamalıdır.
- Arayüz: SPI uyumlu seri arayüz; veri sayfasında SPI modları 0,0 ve 1,1 belirtilir.
- Üreticinin veri sayfasında azami dönüşüm hızı 5 V'ta 100 ksps, 2,7 V'ta 50 ksps olarak verilir. Gerçek sistem hızı SPI saatine, komut çerçevesine, yazılım gecikmelerine ve kanal tarama düzenine bağlıdır.

## MCP3208 — 16 pin bağlantı özeti

Aşağıdaki numaralar **MCP3208 entegresinin kendi 16 pinli paketine** aittir; modül/adapter kartındaki konnektör numaralarıyla karıştırılmamalıdır.

| Pin | Sinyal | Açıklama |
|---:|---|---|
| 1–8 | CH0–CH7 | Analog girişler |
| 9 | DGND | Dijital toprak |
| 10 | CS/SHDN | Chip select / shutdown |
| 11 | DIN | SPI veri girişi (ADC'ye) |
| 12 | DOUT | SPI veri çıkışı (ADC'den) |
| 13 | CLK | Seri saat |
| 14 | AGND | Analog toprak |
| 15 | VREF | ADC ölçüm referansı |
| 16 | VDD | Besleme |

Analog sinyalin izin verilen aralığı devrenin GND/VREF düzenine uygun olmalıdır. ESP32 ile birlikte kullanıldığında mantık seviyelerini, ADC beslemesini, referansını ve ortak GND'yi tüm devre üzerinden doğrula; MCP3208'i 5 V ile beslemek, ESP32'nin MISO girişine 5 V çıkış gelebileceği anlamına gelebilir. ESP32 GPIO'larına 5 V uygulama.

## BERO bağlantı başlangıcı

Mevcut ESP32-WROOM-32D / DevKitC test notlarında kullanılan yaygın VSPI eşlemesi:

| ESP32 GPIO | MCP3208 | Yön |
|---|---|---|
| GPIO18 | CLK | ESP32 → ADC |
| GPIO23 | DIN | ESP32 → ADC |
| GPIO19 | DOUT | ADC → ESP32 |
| GPIO5 | CS/SHDN | ESP32 → ADC |

Bu tablo bir **test başlangıcıdır**, doğrulanmış tek bağlantı seçeneği değildir. GPIO5 bir boot strapping pinidir; reset davranışı kontrol edilmelidir. BERO'daki gerçek kablolamayı ölçerek teyit et.

## BERO'da doğrulama sırası

1. Entegrenin üzerindeki işaretlemeyi ve paketin 14/16 pin olduğunu kontrol et.
2. Enerji kapalıyken pin yönünü, GND ve besleme bağlantılarını kontrol et.
3. Enerji verildiğinde VDD–DGND, VREF–AGND ve analog giriş–AGND gerilimlerini ölç.
4. ADC'ye sensör yerine bilinen, güvenli ve sabit bir giriş uygula; ham SPI TX/RX baytlarını kaydet.
5. CS çerçevesini, CLK kenarlarını, komut bitlerini ve 12 bitlik sonuç decode'unu veri sayfasıyla karşılaştır.
6. Ancak ADC okuması doğrulandıktan sonra SCT013 sinyali, RMS ve amper hesabına geç.

## Resmî kaynaklar

- [Microchip MCP3208 ürün sayfası](https://www.microchip.com/en-us/product/MCP3208)
- [Microchip MCP3204 ürün sayfası](https://www.microchip.com/en-us/product/MCP3204)
- [MCP3204/3208 veri sayfası — DS21298](https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf)

**Durum:** Üretici özellikleri dokümante edildi. BERO devresinin fiziksel bağlantısı ve ölçüm doğruluğu ayrıca test edilmelidir.
