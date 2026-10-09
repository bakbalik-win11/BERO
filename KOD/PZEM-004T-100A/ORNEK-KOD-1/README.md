# Örnek Kod-1 — Arduino / ESP32 ve PZEM-004T V3.0

## Kütüphane

- [mandulaj/PZEM-004T-v30 GitHub](https://github.com/mandulaj/PZEM-004T-v30)

Kütüphane PZEM-004T V3.0 içindir. Eski PZEM-004T sürümleriyle protokol uyumluluğunu varsayma.

## ESP32 Arduino örneği

Aşağıdaki örnek, kütüphane API'siyle seri porttan temel ölçümleri okumak için başlangıç taslağıdır. ESP32 pinleri ve PZEM sürümü fiziksel devrede doğrulanmalıdır.

~~~cpp
#include <Arduino.h>
#include <PZEM004Tv30.h>

// Örnek UART2 pinleri; gerçek BERO pin planına göre değiştir.
HardwareSerial pzemSerial(2);
PZEM004Tv30 pzem(pzemSerial, 16, 17); // RX=GPIO16, TX=GPIO17

void setup() {
  Serial.begin(115200);
  pzemSerial.begin(9600, SERIAL_8N1, 16, 17);
  delay(500);
  Serial.println("PZEM-004T V3.0 readout");
}

void loop() {
  float voltage = pzem.voltage();
  float current = pzem.current();
  float power = pzem.power();
  float energy = pzem.energy();
  float frequency = pzem.frequency();
  float pf = pzem.pf();

  if (isnan(voltage) || isnan(current) || isnan(power)) {
    Serial.println("PZEM read failed: check version, 5V/GND, TX/RX and AC input");
  } else {
    Serial.printf("V=%.1f V, I=%.3f A, P=%.1f W, E=%.3f kWh, f=%.1f Hz, PF=%.2f\n",
      voltage, current, power, energy, frequency, pf);
  }
  delay(2000);
}
~~~

## Bağlantı notları

- PZEM TX → ESP32 RX (örnekte GPIO16).
- PZEM RX → ESP32 TX (örnekte GPIO17).
- GND ortak, PZEM TTL tarafına kılavuza uygun 5 V besleme gerekir.
- ESP32 GPIO'sunu 5 V ile sürme; PZEM TX lojik seviyesini ölç ve gerekiyorsa seviye dönüştür.
- Kütüphane örnekleri/kurucusu sürüme göre farklılaşabileceğinden derleme öncesi kurulu kütüphanenin README/API'sini kontrol et.

**Durum:** Kod taslağıdır; gerçek BERO donanımında derlenmedi ve test edilmedi.