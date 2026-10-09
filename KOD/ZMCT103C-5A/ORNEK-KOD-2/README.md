# Örnek Kod-2 — ESP32 + MCP3208 SPI ham örnekleme

Amaç, MCP3208 ham kodlarını ve dönüş baytlarını kaydetmektir. Burden/bias hazır olmalı; MCP3208 girişine negatif gerilim uygulanmamalı. ADC girişi AGND–VREF aralığında ve VREF ≤ VDD olmalıdır.

Örnek pinler klasik ESP32 içindir: SCK=GPIO18, MOSI=GPIO23, MISO=GPIO19, CS=GPIO5.

~~~cpp
#include <Arduino.h>
#include <SPI.h>
constexpr int CS_PIN=5, SCK_PIN=18, MISO_PIN=19, MOSI_PIN=23;
constexpr uint8_t CHANNEL=0;
constexpr uint16_t N=1000;
constexpr uint32_t PERIOD_US=1000;
SPISettings settings(500000, MSBFIRST, SPI_MODE0);

uint16_t readMCP3208(uint8_t ch, uint8_t rx[3]) {
  uint8_t tx[3] = {
    (uint8_t)(0x06 | ((ch & 0x04) >> 2)),
    (uint8_t)((ch & 0x03) << 6), 0x00
  };
  digitalWrite(CS_PIN, HIGH);
  delayMicroseconds(1);
  SPI.beginTransaction(settings);
  digitalWrite(CS_PIN, LOW);
  for (int i=0; i<3; ++i) rx[i]=SPI.transfer(tx[i]);
  digitalWrite(CS_PIN, HIGH);
  SPI.endTransaction();
  return ((uint16_t)(rx[1]&0x0F)<<8) | rx[2];
}
void setup() {
  Serial.begin(115200);
  pinMode(CS_PIN,OUTPUT); digitalWrite(CS_PIN,HIGH);
  SPI.begin(SCK_PIN,MISO_PIN,MOSI_PIN,CS_PIN);
  Serial.println("index,time_us,rx0,rx1,rx2,raw");
}
void loop() {
  uint32_t start=micros(), next=start;
  for (uint16_t i=0; i<N; ++i) {
    while ((int32_t)(micros()-next)<0) {}
    uint8_t rx[3]={0,0,0};
    uint16_t raw=readMCP3208(CHANNEL,rx);
    Serial.printf("%u,%lu,0x%02X,0x%02X,0x%02X,%u\n",
      i,(unsigned long)(micros()-start),rx[0],rx[1],rx[2],raw);
    next+=PERIOD_US;
  }
  Serial.println("# WINDOW_END"); delay(1000);
}
~~~

Bu SPI çerçevesi doğrulanmış sürücü değil, test iskeletidir. MCP3208 datasheet'i ve SANEC lojik analizör yakalamasıyla komut bitlerini, CS sınırlarını ve RX hizalamasını doğrula. Sekonderi açık devre bırakma.

**Durum:** Fiziksel BERO donanımında test edilmedi.