# Örnek Kod-3 — ESPHome ct_clamp yaklaşımı

## Amaç

ESPHome'un mevcut `ct_clamp` bileşeniyle ADC kaynak sensöründen akım hesabı yapmak. Bu, elle raw örnek döngüsü yazmaktan farklı, daha yüksek seviyeli bir yaklaşımdır.

## Örnek YAML parçası

```yaml
sensor:
  - platform: adc
    pin: GPIO34
    id: sct_voltage
    attenuation: 12db
    update_interval: 1ms

  - platform: ct_clamp
    sensor: sct_voltage
    name: "SCT013 Current"
    id: sct_current
    sample_duration: 200ms
    update_interval: 1s
    filters:
      - calibrate_linear:
          - 0.0 -> 0.0
          - 0.5 -> 15.0
```

## Açıklama

- `adc` kaynak sensörü analog girişten gerilim ölçümü sağlar.
- `ct_clamp`, kaynak sensör örneklerinden AC akımın etkin değerini hesaplamaya yardımcı olur.
- `sample_duration: 200ms`, 50 Hz şebekede yaklaşık 10 periyotluk bir pencereye karşılık gelir.
- `calibrate_linear` içindeki `0.5 -> 15.0` yalnızca örnek kalibrasyon noktasıdır: gerçek donanımda referans akımla ölçülmeden kullanma.
- GPIO34 yalnızca klasik ESP32 içindir; ADC pinleri ve attenuasyon kart/ESPHome sürümüne göre doğrulanmalıdır.

## Kritik sınırlama

Bu örnek YAML **şematik bir örnektir, doğrudan yüklenmeye hazır BERO yapılandırması değildir**. ESPHome sürümüne göre ADC güncelleme aralığı, örnekleme davranışı ve `ct_clamp` kaynağı gereksinimleri kontrol edilmelidir. ESPHome dokümantasyonunda `ct_clamp` için varsayılan `sample_duration` 200 ms olarak belirtilir; güncelleme aralığı örnekleme süresinden uzun olmalıdır.

## Kaynak

- ESPHome CT Clamp resmi dokümanı: https://esphome.io/components/sensor/ct_clamp/
