# Örnek Kod-1 — ESP32 dahili ADC ile ham örnekleme

## Amaç

ACS758 çıkışını klasik ESP32-WROOM ADC1 piniyle örnekleyip zaman damgası ve raw kodu CSV olarak kaydetmek. Bu ilk test amper hesabı yapmaz.

## Güvenli bağlantı ön koşulu

ACS758 modülünü 5 V ile besliyorsan VIOUT 3,3 V'u aşabilir. GPIO34'e doğrudan bağlamadan önce tüm ölçüm aralığında VIOUT sınırlarını hesapla/ölç ve uygun giriş ölçeklemesi uygula. GPIO34 örneği klasik ESP32 içindir; diğer ESP32 varyantlarında pin farklı olabilir.

## Arduino-ESP32 örneği

```cpp
#include <Arduino.h>

constexpr int ADC_PIN = 34; // Klasik ESP32-WROOM ADC1; kartına göre doğrula
constexpr uint16_t N = 1000;
constexpr uint32_t PERIOD_US = 1000; // hedef 1 kS/s, garanti edilmiş hız değildir

uint16_t raw[N];
uint32_t t_us[N];

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
  delay(300);
  Serial.println("index,time_us,raw");
}

void loop() {
  const uint32_t start = micros();
  uint32_t next = start;

  for (uint16_t i = 0; i < N; ++i) {
    while ((int32_t)(micros() - next) < 0) {}
    t_us[i] = micros() - start;
    raw[i] = analogRead(ADC_PIN);
    next += PERIOD_US;
  }

  for (uint16_t i = 0; i < N; ++i) {
    Serial.printf("%u,%lu,%u\n", i, (unsigned long)t_us[i], raw[i]);
  }
  Serial.println("# WINDOW_END");
  delay(1000);
}
```

## Açıklama

- Raw kod volt veya amper değildir.
- 1000 örnek pencere başına 1000 ölçümdür; 1 ms hedef aralıkla yaklaşık 1 saniyelik pencere olur.
- Gerçek örnek aralığını `time_us` sütunundan kontrol et; Arduino görevleri ve ADC okuma süresi jitter oluşturabilir.
- Önce sıfır akımda ofset dağılımını kaydet. Ardından bilinen, düşük DC akımla işaret yönünü ve duyarlılığı kontrol et.

**Durum:** Örnek kod; BERO ESP32 kartında doğrulanmadı.
