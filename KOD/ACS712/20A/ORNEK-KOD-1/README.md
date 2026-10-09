# Örnek Kod-1 — ESP32 dahili ADC ile raw örnekleme (20A)

**Ön koşul:** ACS712 5 V beslenir. OUT'u ESP32 ADC aralığına güvenli şekilde ölçekleyen ön uç hazır olmalı. GPIO34 klasik ESP32-WROOM ADC1 içindir.

~~~cpp
#include <Arduino.h>
constexpr int ADC_PIN = 34;
constexpr uint16_t N = 1000;
constexpr uint32_t PERIOD_US = 1000;
uint16_t raw[N];
uint32_t timeUs[N];

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
  Serial.println("index,time_us,raw");
}
void loop() {
  uint32_t start=micros(), next=start;
  for (uint16_t i=0;i<N;i++) {
    while ((int32_t)(micros()-next)<0) {}
    timeUs[i]=micros()-start;
    raw[i]=analogRead(ADC_PIN);
    next+=PERIOD_US;
  }
  for (uint16_t i=0;i<N;i++)
    Serial.printf("%u,%lu,%u\n",i,(unsigned long)timeUs[i],raw[i]);
  Serial.println("# WINDOW_END");
  delay(1000);
}
~~~

Bu kod **amper hesaplamaz**. 1000 örnek bir pencere boyudur; hedef 1 ms örnek aralığı gerçekte jitter içerebilir. Önce 0 A ofsetini, sonra bilinen DC/AC akımda raw dağılımını ve zaman damgalarını kontrol et.

**Durum:** Test iskeleti, BERO donanımında doğrulanmadı.
