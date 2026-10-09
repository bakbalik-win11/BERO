# KOD-1 — ESPHome `mcp3204` bileşeni (MCP3204 veya MCP3208)

## Bu yaklaşım nedir?

Bu örnek ESPHome'un yerleşik `mcp3204` bileşenini kullanır. Bileşen adının `mcp3204` olması yanıltıcı olabilir: ESPHome dokümantasyonu aynı bileşenin MCP3204 (4 kanal) ve MCP3208 (8 kanal) ile kullanılabildiğini açıkça belirtir. MCP3208 kullanıldığında kanal numarası 0–7 olabilir; MCP3204'te 0–3 ile sınırlıdır.

**Kaynak:** https://esphome.io/components/sensor/mcp3204/

## ESP32-WROOM-32D / DevKitC bağlantı varsayımı

| ESP32 | ADC |
|---|---|
| GPIO18 | CLK |
| GPIO23 | DIN / MOSI |
| GPIO19 | DOUT / MISO |
| GPIO5 | CS/SHDN |
| GND | DGND ve AGND (devre tasarımına göre ortak referans) |

Bu, BERO'da daha önce kullanılan SPI pin eşlemesidir; gerçek kablo bağlantısını ölçerek doğrula. GPIO5 boot strapping pini olduğundan açılış davranışına dikkat et.

## Örnek ESPHome YAML

Aşağıdaki örnek CH0 ve CH7'yi okur; **CH7 satırı yalnızca MCP3208 fiziksel entegresi kullanılıyorsa geçerlidir.** Wi-Fi bilgilerini kendi secrets dosyana göre ayarla. Önce yalnızca CH0 ile başlamak istersen CH7 sensör bloğunu kaldır.

```yaml
esphome:
  name: bero-mcp3208-test
  friendly_name: BERO MCP3208 Test

esp32:
  board: esp32dev
  framework:
    type: arduino

logger:

api:

ota:
  - platform: esphome

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

spi:
  clk_pin: GPIO18
  mosi_pin: GPIO23
  miso_pin: GPIO19

mcp3204:
  id: adc_bus
  cs_pin: GPIO5
  reference_voltage: 3.3V

sensor:
  - platform: mcp3204
    mcp3204_id: adc_bus
    id: adc_ch0
    name: "MCP ADC CH0 Voltage"
    number: 0
    update_interval: 1s

  - platform: mcp3204
    mcp3204_id: adc_bus
    id: adc_ch7
    name: "MCP ADC CH7 Voltage"
    number: 7
    update_interval: 1s
```

## Nasıl çalışır?

- ESPHome, SPI haberleşmesini ve ADC değerinden gerilim hesaplamasını bileşen içinde yapar.
- `reference_voltage`, ADC'nin gerçek VREF gerilimiyle eşleşmelidir; örnekteki 3.3 V varsayımdır, ölçülmeden gerçek kabul edilmemeli.
- `number: 0` CH0'ı seçer; MCP3208'de `number: 7` CH7'yi seçer.
- `update_interval: 1s` yaklaşık saniyede bir güncelleme ister; bu yüksek hızlı RMS örneklemesi için tasarlanmış bir örnek değildir.

## Artıları / eksileri

**Artıları**
- Home Assistant'a gerilim sensörleri hızlıca eklenir.
- SPI protokolünü kendin yazman gerekmez.
- BERO'nun önceki `mcp3204` bileşen adı ve 8 kanal hedefiyle doğrudan bağlantılıdır.

**Eksileri**
- Bileşenin içindeki ham SPI TX/RX baytlarını ve CS/CLK zamanlamasını doğrudan incelemek daha zordur.
- Yanlış `reference_voltage` gerilim raporunu ölçek olarak bozar.
- Yüksek hızlı RMS ölçümü için tek başına uygun olduğu varsayılmamalıdır.

## Test durumu

Bu YAML çevrim içi ESPHome dokümantasyonundaki şema temel alınarak hazırlanmış bir başlangıç örneğidir; BERO donanımında derlenip test edilmiş değildir. Önce gerçek ADC modeli, VDD, VREF, GND ve CH0 sabit giriş ölçümünü doğrula. MCP3204 takılıysa CH7 sensörünü kaldır ve sadece CH0–CH3 kullan.
