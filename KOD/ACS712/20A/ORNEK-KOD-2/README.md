# Örnek Kod-2 — ESP32 + MCP3208 SPI raw (20A)

**Ön koşul:** ACS712 OUT, ADC AGND–VREF aralığına uygun bölücü/koruma üzerinden bağlanmalı; VREF ≤ VDD. MCP3208 girişine 5 V OUT doğrudan bağlama.

~~~cpp
#include <Arduino.h>
#include <SPI.h>
constexpr int CS=5,SCK=18,MISO_PIN=19,MOSI_PIN=23;
constexpr uint8_t CH=0;
constexpr uint16_t N=1000;
constexpr uint32_t PERIOD_US=1000;
SPISettings cfg(500000,MSBFIRST,SPI_MODE0);

uint16_t readADC(uint8_t ch,uint8_t rx[3]) {
  uint8_t tx[3]={(uint8_t)(0x06|((ch&4)>>2)),
                 (uint8_t)((ch&3)<<6),0};
  digitalWrite(CS,HIGH);
  delayMicroseconds(1);
  SPI.beginTransaction(cfg);
  digitalWrite(CS,LOW);
  for(int i=0;i<3;i++) rx[i]=SPI.transfer(tx[i]);
  digitalWrite(CS,HIGH);
  SPI.endTransaction();
  return ((uint16_t)(rx[1]&0x0F)<<8)|rx[2];
}
void setup(){
  Serial.begin(115200);
  pinMode(CS,OUTPUT);digitalWrite(CS,HIGH);
  SPI.begin(SCK,MISO_PIN,MOSI_PIN,CS);
  Serial.println("index,time_us,rx0,rx1,rx2,raw");
}
void loop(){
  uint32_t start=micros(),next=start;
  uint8_t rx[3];
  for(uint16_t i=0;i<N;i++){
    while((int32_t)(micros()-next)<0){}
    uint32_t t=micros()-start;
    uint16_t raw=readADC(CH,rx);
    Serial.printf("%u,%lu,0x%02X,0x%02X,0x%02X,%u\n",
      i,(unsigned long)t,rx[0],rx[1],rx[2],raw);
    next+=PERIOD_US;
  }
  Serial.println("# WINDOW_END");delay(1000);
}
~~~

**Önemli:** MCP3208 3-bayt çerçevesi bir **test adayıdır**; geçmiş BERO SPI anomalileri nedeniyle doğrulanmış sürücü kabul edilmez. SANEC lojik analizörle CS/CLK/DIN/DOUT ve ham TX/RX baytlarını doğrula. ADC kodu amper değildir; VREF, analog ölçekleme ve 100 mV/A hassasiyeti hesaplamaya ayrıca uygulanır. Örnekleme süresi ve aralıklarını kontrol et.
