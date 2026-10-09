# Örnek Kod-1 — ESP32 dahili ADC ile raw örnekleme

## Amaç

SCT013 çıkışından gelen biaslı dalga biçimini ESP32'nin dahili ADC'siyle okuyup ham örnekleri Serial Monitor'a yazdırmak. Bu örnek önce **raw veriyi ve örnekleme zamanını** incelemek içindir; amper kalibrasyonu yapmaz.

> BERO'da kullanılan MCP3208 harici ADC ile aynı yöntem değildir. Bu kod yalnızca ESP32'nin dahili ADC'sine bağlı uygun analog ön uç varsa kullanılabilir.

## Bağlantı ön koşulu

SCT013-030 ve SCT013-100 gerilim çıkışlıdır. ADC'ye negatif gerilim veya ADC aralığının üstünde gerilim uygulanamaz. Uygun bias, giriş koruması ve ölçekleme devresi gerekir. Sensörü çıplak olarak doğrudan GPIO'ya bağlamak güvenli bir varsayım değildir.

## Arduino-ESP32 örnek kodu

```cpp
#include <Arduino.h>
#include <math.h>

constexpr int ADC_PIN = 34;          // ESP32 klasik WROOM DevKitC: ADC1 input-only
constexpr uint16_t SAMPLE_COUNT = 1000;
constexpr uint32_t SAMPLE_PERIOD_US = 1000; // hedef: 1 kS/s, gerçek zamanlamayı ölç

uint16_t rawSamples[SAMPLE_COUNT];
uint32_t timeUs[SAMPLE_COUNT];

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);          // tipik Arduino-ESP32 raw aralığı: 0..4095
  delay(500);
  Serial.println("index,time_us,raw");
}

void loop() {
  // Bu hedef zamanlama busy-wait kullanır; gerçek aralık jitter içerebilir.
  uint32_t start = micros();
  uint32_t next = start;

  for (uint16_t i = 0; i < SAMPLE_COUNT; i++) {
    while ((int32_t)(micros() - next) < 0) {
      // hedef örnek zamanına kadar bekle
    }
    timeUs[i] = micros() - start;
    rawSamples[i] = analogRead(ADC_PIN);
    next += SAMPLE_PERIOD_US;
  }

  for (uint16_t i = 0; i < SAMPLE_COUNT; i++) {
    Serial.printf("%u,%lu,%u\n",
                  i,
                  (unsigned long)timeUs[i],
                  rawSamples[i]);
  }

  Serial.println("# WINDOW_END");
  delay(1000);
}
```

## Kodun açıklaması

- `ADC_PIN=34`: klasik ESP32-WROOM-32D/DevKitC içindir; ESP32-C3 veya başka kartta pin eşlemesi farklı olabilir.
- `SAMPLE_COUNT=1000`: bir pencerede 1000 raw okuma.
- `SAMPLE_PERIOD_US=1000`: 1 ms hedef aralık, yani hedef yaklaşık 1000 örnek/saniye. Gerçek zaman damgalarıyla hedefin tutup tutmadığı kontrol edilir.
- `rawSamples[]`: ADC'nin sayısal ham sayımlarını saklar. Bunlar volt veya amper değildir.
- `timeUs[]`: pencerenin başından itibaren mikro saniye cinsinden zaman.
- Önce bütün örnekler alınır, sonra yazdırılır; Serial çıktısı örnekleme anlarını gereksiz yere yavaşlatmaz.

## Beklenen çıktı

CSV benzeri satırlar: `index,time_us,raw`. Biaslı bir sinyalde raw değerlerin sıfır çevresinde değil, orta bir değer çevresinde salınması normaldir. Giriş sabitse raw değerler de sabit çevrede kalmalıdır. Sadece sabit sayı veya 0 görülürse sensör kalibrasyonuna geçmeden pin, bias, ADC ayarı ve bağlantıyı kontrol et.

## Sınırlamalar

Bu kod gerçek zamanlı üretim örnekleyicisi değildir; Arduino-ESP32 `analogRead()` süresi ve görev kesintileri zaman aralığını etkileyebilir. Kesin örnekleme için donanım timer/ADC continuous mode gibi yöntemler değerlendirilmelidir. ESP32 ADC doğrusal değildir; voltaj dönüşümü için kartın kalibre edilmiş ADC dönüşüm API'si ve gerçek ölçüm gerekir. Bu kodda RMS veya amper hesabı kasıtlı olarak yoktur.
