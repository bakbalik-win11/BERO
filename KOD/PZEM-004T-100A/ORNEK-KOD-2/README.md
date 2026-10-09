# Örnek Kod-2 — ESPHome PZEMAC

ESPHome, desteklenen PZEM-004T varyantlarını UART üzerinden `pzemac` sensör platformuyla okuyabilir. Uygun sürüm ve modül revizyonunu resmi bileşen sayfasından doğrula.

Kaynak: https://esphome.io/components/sensor/pzemac/

## YAML başlangıç örneği

~~~yaml
uart:
  id: pzem_uart
  tx_pin: GPIO17
  rx_pin: GPIO16
  baud_rate: 9600
  parity: NONE
  stop_bits: 1

sensor:
  - platform: pzemac
    uart_id: pzem_uart
    voltage:
      name: "PZEM Voltage"
    current:
      name: "PZEM Current"
    power:
      name: "PZEM Active Power"
    energy:
      name: "PZEM Energy"
    frequency:
      name: "PZEM Frequency"
    power_factor:
      name: "PZEM Power Factor"
    update_interval: 5s
~~~

## Dikkat

- Pinler örnektir; BERO'nun gerçek UART planıyla karşılaştır.
- ESPHome sürümünün PZEM sürümünü desteklediğini kontrol et.
- PZEM TTL beslemesi, UART lojik seviyeleri ve ortak GND doğru olmalı.
- Şebeke ölçüm bağlantısını yalnızca enerjisiz ve güvenli koşullarda, uygun yetkinlikle yap.
- YAML, BERO cihazında derlenmiş veya yüklenmiş değildir.

**Durum:** Başlangıç yapılandırması; fiziksel test yok.