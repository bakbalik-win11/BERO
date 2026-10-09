# Örnek Kod-3 — ESPHome ADC izleme iskeleti

Bu örnek analog ön uçtan çıkan biaslı gerilimi Home Assistant'ta izler. Tek başına akım veya RMS hesabı yapmaz.

~~~yaml
sensor:
  - platform: adc
    pin: GPIO34
    id: zmct103c_voltage
    name: "ZMCT103C Analog Output"
    attenuation: 12db
    update_interval: 1s
~~~

GPIO34 klasik ESP32 içindir. CT sekonderinde uygun burden bulunmalı; negatif AC yarım dalgayı ADC'ye doğrudan uygulama. Bir saniyelik güncelleme AC dalga biçimi RMS hesabı için yeterli değildir; hızlı ham örnekleme gerekir. YAML, kullanılan ESPHome sürümünde doğrulanmadan yüklenmeye hazır kabul edilmemelidir.

Kaynak: https://esphome.io/components/sensor/adc/