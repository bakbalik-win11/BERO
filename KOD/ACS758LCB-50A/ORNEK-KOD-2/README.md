# Örnek Kod-2 — ESP32 + MCP3208 SPI ham örnekleme

## Amaç

Sensör hesaplamasına geçmeden MCP3208'den ham kodları kaydetmek. SPI çerçevesi ve bit hizalaması ilk olarak lojik analizörle doğrulanmalıdır.

## Güvenli giriş aralığı

MCP3208 giriş gerilimi analog GND ile VREF aralığında tutulmalı ve VREF ≤ VDD olmalıdır. ACS758 5 V ile besleniyorsa VIOUT ADC aralığını aşabilir; ADC'ye bağlamadan önce ölçeklemeyi doğrula. Gerekirse bölücü/tampon tasarla.

## Arduino SPI test iskeleti

```cpp
#include <Arduino.h>
#include <SPI.h>

constexpr int PIN_CS = 5;
constexpr int PIN_SCK = 18;
constexpr int PIN_MISO = 19;
constexpr int PIN_MOSI = 23;
constexpr uint8_t CHANNEL = 0;
constexpr uint16_t N = 1000;
constexpr uint32_t PERIOD_US = 1000;

SPISettings settings(500000, MSBFIRST, SPI_MODE0);

uint16_t readMCP3208(uint8_t ch, uint8_t *rxOut) {
  uint8_t tx[3] = {
    (uint8_t)(0x06 | ((ch & 0x04) >> 2)),
    (uint8_t)((ch & 0x03) << 6),
    0x00
  };
  digitalWrite(PIN_CS, HIGH);
  delayMicroseconds(1);
  SPI.beginTransaction(settings);
  digitalWrite(PIN_CS, LOW);
  for (int i = 0; i < 3; ++i) rxOut[i] = SPI.transfer(tx[i]);
  digitalWrite(PIN_CS, HIGH);
  SPI.endTransaction();
  return ((uint16_t)(rxOut[1] & 0x0F) << 8) | rxOut[2];
}

void setup() {
  Serial.begin(115200);
  pinMode(PIN_CS, OUTPUT);
  digitalWrite(PIN_CS, HIGH);
  SPI.begin(PIN_SCK, PIN_MISO, PIN_MOSI, PIN_CS);
  Serial.println("index,time_us,tx0,tx1,tx2,rx0,rx1,rx2,raw");
}

void loop() {
  const uint32_t start = micros();
  uint32_t next = start;
  for (uint16_t i = 0; i < N; ++i) {
    while ((int32_t)(micros() - next) < 0) {}
    uint8_t rx[3] = {0, 0, 0};
    uint16_t raw = readMCP3208(CHANNEL, rx);
    Serial.printf("%u,%lu,0x06,0x00,0x00,0x%02X,0x%02X,0x%02X,%u\n",
                  i, (unsigned long)(micros() - start),
                  rx[0], rx[1], rx[2], raw);
    next += PERIOD_US;
  }
  Serial.println("# WINDOW_END");
  delay(1000);
}
```

## Dikkat

- Bu, SPI çerçevesini test etmek için başlangıç iskeletidir; çalışır/doğru olduğu iddia edilmez. TX baytları sabit kanal 0 komutu olarak yazdırılır; CHANNEL değiştirilecekse TX logunu da dinamik hale getir.
- CS, saat modu, bit sırası ve RX zero-bit hizalamasını SANEC lojik analizörle kontrol et.
- Kablolama örneği: GPIO18=SCLK, GPIO23=MOSI/DIN, GPIO19=MISO/DOUT, GPIO5=CS. Gerçek devreyle karşılaştır.
- Testte ham TX/RX baytlarını ve beklenen sabit giriş sonucunu kaydet.

**Durum:** Test iskeleti; BERO donanımında doğrulanmadı.
