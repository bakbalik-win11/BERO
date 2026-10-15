# ESP32D1 — ESPHome bağlantı ve sensör logu

Kaynak: kullanıcı tarafından 10.10.2026 tarihinde sağlanan `esp32d1-logs (2).txt`. İkinci yüklenen `esp32d1-logs (2)(1).txt` aynı içeriktedir.

## Bağlantı / derleme

```text
INFO ESPHome 2026.9.1
INFO Loaded validated config cache for esp32d1.yaml, skipping validation.
INFO Starting log output from 192.168.0.8 using esphome API
INFO Successfully resolved esp32d1 @ 192.168.0.8 in 0.001s
INFO Successfully connected to esp32d1 @ 192.168.0.8 in 4.124s
INFO Successful handshake with esp32d1 @ 192.168.0.8 in 0.012s
[16:03:27.135][I][app:151]: ESPHome version 2026.9.1 compiled on 2026-10-10 15:56:15 +0300
[16:03:27.135][I][app:158]: ESP32 Chip: ESP32 rev3.1, 2 core(s)
```

## PZEM ve UART yapılandırması

```text
TX Pin: GPIO16
RX Pin: GPIO17
Baud Rate: 9600 baud
Data Bits: 8
Parity: NONE
Stop bits: 1
PZEMAC Address: 0x01
```

## ADC yapılandırması

```text
CH1 GPIO32 — ADC1 channel 4 — attenuation 12 dB — Samples: 1 — Update Interval: 1.000s — Handle Init: OK — Config: OK — Calibration: OK — Overall Init: OK
CH2 GPIO33 — ADC1 channel 5 — attenuation 12 dB — Samples: 1 — Update Interval: 1.000s — Handle Init: OK — Config: OK — Calibration: OK — Overall Init: OK
CH3 GPIO34 — ADC1 channel 6 — attenuation 12 dB — Samples: 1 — Update Interval: 1.000s — Handle Init: OK — Config: OK — Calibration: OK — Overall Init: OK
```

## Ölçüm örnekleri (orijinal logdaki satırlardan)

```text
[16:03:28.027] CH3 1.657 V
[16:03:28.027] CH1 1.669 V
[16:03:28.307] CH2 1.665 V
[16:03:50.027] CH3 1.643 V
[16:04:02.303] CH2 1.643 V
[16:04:06.307] CH2 1.638 V
[16:04:12.494] PZEM Gerilim 233.7 V
[16:04:12.494] PZEM Akım 0.029 A
[16:04:12.495] PZEM Güç 1.80 W
[16:04:12.496] PZEM Frekans 50.0 Hz
[16:04:13.034] CH3 1.668 V
[16:04:13.035] CH1 1.658 V
[16:04:13.313] CH2 1.669 V
```

Bu kayıt, orijinal 347 satırlık logun tamamının ham kopyası değil; temel bağlantı/yapılandırma satırları ve örnek ölçümler özetlenmiştir. Tam orijinal log kullanıcı yüklemesi olarak sohbet eklerinde durmaktadır.
