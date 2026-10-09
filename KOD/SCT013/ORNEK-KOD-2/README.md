# Örnek Kod-2 — ESP32 + MCP3208 SPI ham örnekleme

## Amaç

Sensör hesabına geçmeden MCP3208'den seçilen kanalı okuyup ham ADC kodlarını ve örnek zamanını kaydetmek. Önce ADC'nin kendisini sabit ve bilinen girişlerle doğrulamak için kullanılır.

> **Bu örnek SPI işlem çerçevesini açıklayan bir iskelettir.** BERO'da kullanılan gerçek ESPHome/custom SPI yapılandırması ve önceki TX/RX gözlemleriyle eşleştirilmeden çalışır/doğru kabul edilmemelidir. Özellikle ESP-IDF/Arduino SPI API'lerinin transfer sırası ve MCP3208 komut biçimi kullanılan kütüphaneye göre doğrulanmalıdır.

## MCP3208 protokol özeti

MCP3208 12 bit, 8 kanallı SPI ADC'dir. Dönüşüm komutunda start biti, single-ended/differential seçimi, kanal seçimi ve saat darbeleri gerekir. Sonuç 12 bittir (0–4095). CS çerçeveyi sınırlar; CS'nin zamanlaması ve bitlerin doğru hizalanması kritik önemdedir.

## Arduino SPI örneği

```cpp
#include <Arduino.h>
#include <SPI.h>

constexpr int PIN_CS = 5;
constexpr int PIN_SCK = 18;
constexpr int PIN_MISO = 19;
constexpr int PIN_MOSI = 23;
constexpr uint8_t ADC_CHANNEL = 0;
constexpr uint16_t SAMPLE_COUNT = 1000;
constexpr uint32_t SAMPLE_PERIOD_US = 1000;

SPISettings adcSettings(500000, MSBFIRST, SPI_MODE0);

uint16_t readMCP3208(uint8_t channel) {
  // MCP3208 single-ended command frame.
  // Keep this byte framing as a test candidate and verify against
  // Microchip datasheet / a known-good driver before relying on values.
  uint8_t tx[3] = {
    (uint8_t)(0x06 | ((channel & 0x04) >> 2)),
    (uint8_t)((channel & 0x03) << 6),
    0x00
  };
  uint8_t rx[3] = {0, 0, 0};

  digitalWrite(PIN_CS, LOW);
  SPI.beginTransaction(adcSettings);
  for (int i = 0; i < 3; i++) {
    rx[i] = SPI.transfer(tx[i]);
  }
  SPI.endTransaction();
  digitalWrite(PIN_CS, HIGH);

  // Common 3-byte decode for 12-bit result. Confirm with datasheet
  // and compare raw RX bytes during initial bring-up.
  return ((uint16_t)(rx[1] & 0x0F) << 8) | rx[2];
}

void setup() {
  Serial.begin(115200);
  pinMode(PIN_CS, OUTPUT);
  digitalWrite(PIN_CS, HIGH);
  SPI.begin(PIN_SCK, PIN_MISO, PIN_MOSI, PIN_CS);
  Serial.println("index,time_us,channel,raw");
}

void loop() {
  uint32_t start = micros();
  uint32_t next = start;

  for (uint16_t i = 0; i < SAMPLE_COUNT; i++) {
    while ((int32_t)(micros() - next) < 0) {}
    uint32_t t = micros() - start;
    uint16_t raw = readMCP3208(ADC_CHANNEL);
    Serial.printf("%u,%lu,%u,%u\n",
                  i, (unsigned long)t, ADC_CHANNEL, raw);
    next += SAMPLE_PERIOD_US;
  }

  Serial.println("# WINDOW_END");
  delay(1000);
}
```

## Açıklama ve dikkat

- GPIO18/19/23 ve CS GPIO5, klasik ESP32-WROOM DevKitC için yaygın VSPI pinleridir; BERO'nun gerçek kablolamasıyla karşılaştır.
- MCP3208 VDD ve VREF bağlantıları veri sayfasına göre yapılmalı; VREF hiçbir zaman VDD'yi aşmamalı. Giriş gerilimi analog GND ve VREF aralığında tutulmalıdır.
- Örnekte `SPI_MODE0`, 500 kHz ve MSB-first test başlangıcıdır; osiloskop/logic analyzer ve datasheet ile doğrulanmalıdır.
- `raw` 0–4095 aralığında 12 bit sayıdır; volt değildir.
- Bu örnek, protokolü doğrulamak için raw RX baytlarını da yazdıracak şekilde genişletilmelidir. Başlangıçta RX baytlarını saklamadan yalnızca decode sonucuna güvenme.
- BERO geçmişinde benzer RX örüntüleri ADC sökülüyken de görüldüğü için önce sabit ADC giriş testi ve SPI dalga biçimi doğrulanmalı.

## Kaynak

- Microchip MCP3208 resmi ürün sayfası: https://www.microchip.com/en-us/product/mcp3208

**Durum:** Test adayı; BERO donanımında doğrulanmadı. Bu dosyayı mevcut ESPHome üretim YAML'si olarak kullanma.
