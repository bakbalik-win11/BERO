# Örnek Kod-1 — ESP32 dahili ADC ile ham örnekleme

Bu örnek biaslanmış analog ön uç çıkışını klasik ESP32-WROOM ADC1 üzerinden raw kod ve zaman damgasıyla kaydeder; akım hesabı yapmaz.

**Güvenli bağlantı:** ZMCT103C sekonderi negatif AC gerilim üretebilir. Uygun burden ve bias olmadan doğrudan GPIO'ya bağlama. GPIO34 örneği klasik ESP32 içindir.

## Arduino-ESP32

~~~cpp
#include <Arduino.h>
constexpr int ADC_PIN = 34;
constexpr uint16_t N = 1000;
constexpr uint32_t PERIOD_US = 1000; // hedef 1 kS/s

uint16_t raw[N];
uint32_t t_us[N];

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
  delay(300);
  Serial.println("index,time_us,raw");
}
void loop() {
  uint32_t start = micros(), next = start;
  for (uint16_t i = 0; i < N; ++i) {
    while ((int32_t)(micros() - next) < 0) {}
    t_us[i] = micros() - start;
    raw[i] = analogRead(ADC_PIN);
    next += PERIOD_US;
  }
  for (uint16_t i = 0; i < N; ++i)
    Serial.printf("%u,%lu,%u\n", i, (unsigned long)t_us[i], raw[i]);
  Serial.println("# WINDOW_END");
  delay(1000);
}
~~~

Raw kod volt/amper değildir. PERIOD_US=1000 hedef yaklaşık 1 kS/s verir; gerçek aralıkları time_us sütunundan denetle. Önce akım yokken ofset/gürültüyü, sonra düşük ve bilinen AC akımda dalga biçimini kaydet.

**Durum:** Örnek iskelet; gerçek BERO kartında test edilmedi.