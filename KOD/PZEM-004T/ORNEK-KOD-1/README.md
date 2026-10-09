# Örnek Kod-1 — Arduino-ESP32 ile PZEM-004T V3.0

## Amaç

PZEM-004T V3.0 kütüphanesi üzerinden gerilim, akım, aktif güç, enerji, frekans ve güç faktörünü seri porta yazdırmak.

Kütüphane: https://github.com/mandulaj/PZEM-004T-v30

## Bağlantı örneği

| PZEM | ESP32 |
|---|---|
| TX | UART RX, ör. GPIO16 |
| RX | UART TX, ör. GPIO17 |
| GND | GND |
| VCC/5V | Modül dokümanındaki besleme |

RX/TX çapraz bağlanır. GPIO16/17 örnektir; kullandığın kartta UART pinlerini doğrula. UART lojik seviyelerini ve beslemeyi modül revizyonuna göre kontrol et.

## Arduino-ESP32 örnek kod

~~~cpp
#include <Arduino.h>
#include <PZEM004Tv30.h>

HardwareSerial pzemSerial(2);
PZEM004Tv30 pzem(pzemSerial, 16, 17); // RX, TX

void setup() {
  Serial.begin(115200);
  pzemSerial.begin(9600, SERIAL_8N1, 16, 17);
  delay(500);
  Serial.println("PZEM-004T V3.0 reading");
}

void loop() {
  float voltage = pzem.voltage();
  float current = pzem.current();
  float power = pzem.power();
  float energy = pzem.energy();
  float frequency = pzem.frequency();
  float pf = pzem.pf();

  if (isnan(voltage) || isnan(current) || isnan(power)) {
    Serial.println("PZEM read error: check AC supply, VCC/GND, RX/TX and model/library");
  } else {
    Serial.printf("V=%.1f V, I=%.3f A, P=%.1f W, E=%.3f kWh, F=%.1f Hz, PF=%.2f\n",
                  voltage, current, power, energy, frequency, pf);
  }
  delay(2000);
}
~~~

## Açıklama

- Örnek, kütüphanenin voltage(), current(), power(), energy(), frequency() ve pf() metotlarını kullanır.
- Constructor/API değişebileceği için kullandığın kütüphane sürümünün README örneğiyle karşılaştır.
- PZEM'in AC ölçüm kısmı doğru beslenmiyorsa UART arayüzüne 5 V vermek tek başına yeterli olmayabilir.
- Birden çok modül kullanılıyorsa Modbus adreslerini ve kütüphane desteğini ayrıca ayarla.

**Durum:** Kaynak tabanlı örnek; BERO'da test edilmedi. Şebeke bağlantısı yalnızca uygun korumalı düzenekte yetkin kişi tarafından yapılmalıdır.