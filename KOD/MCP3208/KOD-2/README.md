# KOD-2 — ESP32 Arduino SPI ile ham MCP320x okuma

## Bu yaklaşım nedir?

Bu örnek Arduino `SPI.h` ile SPI komutunu ve yanıt baytlarını açıkça gönderip alır. Amaç Home Assistant entegrasyonu değil; ilk donanım testinde **kanal, ham ADC kodu ve RX baytlarını** görünür kılmaktır.

Kodun kanal seçimi MCP3208 için CH0–CH7'yi destekler. Fiziksel MCP3204 kullanılıyorsa yalnızca CH0–CH3 seçilmelidir. Kaynaklarda benzer üç baytlı SPI okuma yaklaşımı görülür; BERO için yine de veri sayfasıyla ve mantık analizörü/oscilloscope ile doğrulama gerekir.

Kaynaklar:
- https://github.com/labfruits/mcp320x/
- https://github.com/MajenkoLibraries/MCP3208
- https://docs.espressif.com/projects/arduino-esp32/en/latest/api/spi.html
- https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf

## ESP32-WROOM-32D bağlantısı

| ESP32 | ADC |
|---|---|
| GPIO18 | CLK |
| GPIO23 | DIN / MOSI |
| GPIO19 | DOUT / MISO |
| GPIO5 | CS/SHDN |

VDD, VREF, AGND ve DGND bağlantılarını üretici veri sayfasına göre yap. ESP32 GPIO'larına 5 V uygulama. MCP3208'i 5 V ile besliyorsan DOUT seviyesinin ESP32 için güvenli olduğunu ayrıca çöz; kolay başlangıç olarak tüm dijital mantığı 3,3 V uyumlu tut.

## Arduino kodu

```cpp
#include <Arduino.h>
#include <SPI.h>

constexpr int PIN_CS   = 5;
constexpr int PIN_SCK  = 18;
constexpr int PIN_MISO = 19;
constexpr int PIN_MOSI = 23;

// MCP3208 için 8 kanal; fiziksel MCP3204 ise 4 yap.
constexpr uint8_t ADC_CHANNELS = 8;

constexpr float VREF_VOLTS = 3.300f; // Gerçek VREF ölçümünle değiştir.
constexpr uint32_t SPI_HZ = 500000;

SPISettings adcSPI(SPI_HZ, MSBFIRST, SPI_MODE0);

uint16_t readMCP320x(uint8_t channel, uint8_t &rx0,
                     uint8_t &rx1, uint8_t &rx2) {
  if (channel >= ADC_CHANNELS) {
    rx0 = rx1 = rx2 = 0;
    return 0;
  }

  // MCP3204/3208: start + single-ended + channel select.
  // 3-byte frame is a test implementation; validate against datasheet.
  const uint8_t tx0 = 0x06 | ((channel & 0x04) >> 2);
  const uint8_t tx1 = (channel & 0x03) << 6;

  SPI.beginTransaction(adcSPI);
  digitalWrite(PIN_CS, LOW);

  rx0 = SPI.transfer(tx0);
  rx1 = SPI.transfer(tx1);
  rx2 = SPI.transfer(0x00);

  digitalWrite(PIN_CS, HIGH);
  SPI.endTransaction();

  // 12-bit result is assembled from the low nibble of rx1 and rx2.
  return (static_cast<uint16_t>(rx1 & 0x0F) << 8) | rx2;
}

void setup() {
  Serial.begin(115200);

  pinMode(PIN_CS, OUTPUT);
  digitalWrite(PIN_CS, HIGH);

  SPI.begin(PIN_SCK, PIN_MISO, PIN_MOSI, PIN_CS);

  Serial.println("time_us,channel,rx0,rx1,rx2,raw,voltage_V");
}

void loop() {
  for (uint8_t ch = 0; ch < ADC_CHANNELS; ++ch) {
    uint8_t rx0, rx1, rx2;
    const uint32_t t = micros();
    const uint16_t raw = readMCP320x(ch, rx0, rx1, rx2);
    const float voltage = (static_cast<float>(raw) * VREF_VOLTS) / 4095.0f;

    Serial.printf("%lu,%u,0x%02X,0x%02X,0x%02X,%u,%.6f\n",
                  static_cast<unsigned long>(t), ch,
                  rx0, rx1, rx2, raw, voltage);
    delay(100);
  }
}
```

## Nasıl çalışır?

1. CS LOW yapılarak ADC seçilir.
2. İlk bayt start/single-ended ve kanalın üst bitini taşır.
3. İkinci bayt kalan kanal bitlerini taşır; üçüncü bayt saat darbeleri sırasında dönüşümün kalan bitlerini alır.
4. Ham sonuç 12 bit olduğundan 0–4095 aralığındadır. Volt hesabı `raw × VREF / 4095` ile yaklaşık hesaplanır.
5. `rx0`, `rx1`, `rx2` sütunları ham SPI yanıtını saklar; ilk testte yalnızca hesaplanmış voltaja bakmak yerine bunları da karşılaştır.

## Artıları / eksileri

**Artıları**
- Ham RX baytları, kanal numarası ve zaman damgası görünür.
- ESPHome bileşeninden bağımsız olarak SPI çerçevesi incelenebilir.
- Sabit giriş testi ve kanal kanal doğrulama için daha elverişlidir.

**Eksileri**
- SPI çerçevesi ve decode sorumluluğu sende kalır.
- VREF değeri elle ayarlanır.
- Örnekteki `delay(100)` ve seri yazdırma yüksek hızlı örnekleme için değildir; RMS/akım ölçüm kodu değildir.

## İlk test planı

1. Sensör bağlamadan önce CH0'a güvenli, sabit bir DC giriş uygula.
2. VDD, VREF ve giriş gerilimini multimetreyle ölç.
3. Seri çıktıda RX baytlarını, raw değerini ve gerilimi kaydet.
4. Girişi birkaç bilinen seviyeye değiştir; raw değerin tutarlı değiştiğini kontrol et.
5. Ardından CH0–CH7'yi tek tek doğrula. MCP3204 kullanılıyorsa `ADC_CHANNELS = 4` yap.
6. Değerler sabit girişle doğrulanmadan SCT013, RMS veya amper hesabına geçme.

**Durum:** İnternet kaynakları ve üretici veri sayfası temel alınarak hazırlanmış test adayıdır; BERO kartında derlenmiş veya fiziksel olarak doğrulanmış değildir.
