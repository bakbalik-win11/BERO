# Hesaplama-3 — OpenEnergyMonitor EmonLib yaklaşımı

## Örnek kullanım

OpenEnergyMonitor'ın EmonLib örneği, akım-only ölçüm için `current(pin, calibration)` ve `calcIrms(numberOfSamples)` çağrılarını kullanır. Kütüphane offset/bias takibini ve kalibrasyon katsayısını kendi algoritması içinde uygular.

```cpp
#include "EmonLib.h"
EnergyMonitor emon1;

void setup() {
  Serial.begin(115200);
  emon1.current(A0, 30.0); // Yalnızca kavramsal başlangıç; donanım kalibrasyonuna göre değiştir
}

void loop() {
  double Irms = emon1.calcIrms(1000);
  Serial.println(Irms, 3);
  delay(500);
}
```

## Kalibrasyon sabiti neden 30.0 örneği?

OpenEnergyMonitor kalibrasyon teorisi, SCT013-030 için 30 A / 1 V oranını örnek verir. Ancak EmonLib kalibrasyon sabitinin ADC referansı, analog giriş ölçeği ve sensör/ön uç bağlantısıyla birlikte belirlenmesi gerekir. Yukarıdaki `30.0` doğrudan tüm ESP32 devreleri için doğru değildir; özellikle dahili ADC ve MCP3208'in sayım/volt ölçekleri farklıdır.

## 1000 örnek

`calcIrms(1000)`, kütüphaneden 1000 örnekle RMS hesabı istemektir; 1000 örnek/saniye demek değildir. Süre, ADC okuma hızı ve yazılım gecikmesine bağlıdır. Bu çağrının gerçek süresini ölç.

## Farklar

- EmonLib: offset kaldırma ve kalibrasyon işlemlerini kütüphane içinde yapar.
- Hesaplama-1: raw veriden RMS işlemini açıkça gösterir; birim önce ADC count'tur.
- Hesaplama-2: sensör çıkışındaki volt RMS'ten amper hesaplar.
- MCP3208: EmonLib'in analog pin varsayımını otomatik olarak karşılamaz; harici SPI ADC için uygun okuma katmanı ve zamanlama gerekir.

## Kaynaklar

- EmonLib: https://github.com/openenergymonitor/EmonLib
- EmonLib akım-only örneği: https://docs.openenergymonitor.org/electricity-monitoring/ct-sensors/how-to-build-an-arduino-energy-monitor-measuring-current-only.html
- Kalibrasyon teorisi: https://docs.openenergymonitor.org/electricity-monitoring/ctac/emonlib-calibration-theory.html

**Durum:** Kavramsal örnek. ESP32 kartında, ADC donanımında ve gerçek sensörde test edilmeden üretim kodu sayılmaz.
