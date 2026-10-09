# Örnek Kod-3 — ESPHome ile temel ADC izleme

## Amaç

VIOUT geriliminin Home Assistant'ta izlenmesi. Bu örnek yalnızca analog voltajı gösterir; doğrudan amper sensörü değildir ve RMS hesaplamaz.

## Ön koşul

Aşağıdaki GPIO34 örneği klasik ESP32 içindir. Sensör çıkışı ADC girişinin güvenli aralığına ölçeklenmiş olmalıdır. ESPHome ADC kalibrasyonu, attenuation ve gerçek pin eşlemesini kullanılan ESPHome/ESP32 sürümüne göre doğrula.

```yaml
sensor:
  - platform: adc
    pin: GPIO34
    id: acs758_voltage
    name: "ACS758 VIOUT"
    attenuation: 12db
    update_interval: 1s
    filters:
      - multiply: 1.0
```

## Açıklama ve sınırlar

- Bu YAML, kart/ESPHome sürümüne göre uyarlanacak bir başlangıç örneğidir; yüklenmeye hazır BERO yapılandırması olarak doğrulanmamıştır.
- ESP32 ADC kalibrasyonu ve giriş doğrusalığı gerçek gerilim kaynağıyla kontrol edilmelidir.
- 50 Hz AC akım ölçümünde 1 saniyelik seyrek ADC güncellemesi dalga biçimi RMS'i için yeterli örnekleme değildir. Bunun için yüksek hızlı ham örnekleme ve ayrı RMS algoritması gerekir.
- DC ölçüm için sıfır akım ofsetini ölçüp amper dönüşümünü ayrı katmanda yap.

Kaynak: https://esphome.io/components/sensor/adc/
