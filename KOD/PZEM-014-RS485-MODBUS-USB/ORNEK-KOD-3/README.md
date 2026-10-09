# Örnek Kod-3 — Home Assistant ve entegrasyon notları

PZEM-014'ün RS485/Modbus RTU arayüzü, USB–RS485 dönüştürücü ile bilgisayardan veya RS485 transceiver ile ESP32/HA tarafından okunabilir.

## Entegrasyon yolları
1. USB–RS485 + host yazılımı: seri portu okuyan Python/Modbus uygulaması üzerinden Home Assistant'a aktarım.
2. ESP32 + RS485: ESPHome Modbus bileşenleriyle ham register okuma ve template sensörler; register adresleri ve ölçekler kesin cihaz kılavuzundan alınmalı.
3. Hazır PZEM bileşeni: PZEM adını taşıması PZEM-014 RS485 varyantını desteklediğini garanti etmez.

## Kaynaklar
- https://esphome.io/components/modbus_controller/
- https://esphome.io/components/uart/
- https://m.media-amazon.com/images/I/81wHLsuaIOL.pdf

Cihazın register adresleri ve ölçekleri doğrulanmadan sensör tanımlamak hatalı sonuç üretebilir.