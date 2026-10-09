# Örnek Kod-3 — ESPHome ADC izleme (20A)

~~~yaml
sensor:
  - platform: adc
    pin: GPIO34
    id: acs712_20a_adc
    name: "ACS712 20A ADC Voltage"
    attenuation: 12db
    update_interval: 1s
~~~

Bu yalnızca ADC pinindeki **ölçeklenmiş gerilimi** izler; amper veya AC RMS üretmez. 5 V beslenen ACS712'nin OUT'u 3,3 V ADC'ye doğrudan bağlanmamalı. GPIO34 klasik ESP32 içindir. ESPHome sürümüne göre ADC attenuation ve volt kalibrasyonu kontrol edilmeli.

50 Hz AC için saniyede tek okuma RMS hesabı değildir. Yeterli hızlı, düzenli ham örnekleme ve ayrı RMS hesabı gerekir.

Kaynak: https://esphome.io/components/sensor/adc/

**Durum:** Şematik YAML; BERO'da doğrulanmadı.
