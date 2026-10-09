# Örnek Kod-2 — ESPHome / Home Assistant entegrasyon yaklaşımı

PZEM-004T V3.0 TTL sürümü ESP32 UART üzerinden Modbus-RTU benzeri seri protokol kullanır. Bu, RS-485 A/B arayüzü olduğu anlamına gelmez. ESPHome'da doğrudan entegrasyon desteği kullanılan sürüme göre doğrulanmalıdır.

## Önerilen BERO yolu

1. Önce Arduino-ESP32 kütüphanesiyle UART haberleşmesini test et.
2. Geçerli gerilim/akım/güç değerlerini ve hata durumunu doğrula.
3. Home Assistant entegrasyonu için seçilen ESPHome sürümünün PZEM-004T V3.0 desteğini resmi dokümantasyondan kontrol et.
4. Yerel bileşen yoksa test edilmiş sürücü veya ayrı ESP32 köprüsü kullan; doğrulanmamış YAML'ı üretim yapılandırması gibi sunma.

## UART iskeleti

Aşağıdaki parça tek başına PZEM'i okumaz; uyumlu ve doğrulanmış bir PZEM bileşeni eklenmeden sensör değeri üretmez.

~~~yaml
uart:
  id: pzem_uart
  tx_pin: GPIO17
  rx_pin: GPIO16
  baud_rate: 9600
  data_bits: 8
  parity: NONE
  stop_bits: 1
~~~

Kaynaklar:
- https://esphome.io/components/uart/
- https://github.com/mandulaj/PZEM-004T-v30

**Durum:** UART iskeleti; doğrudan yüklenebilir tam entegrasyon değildir.