# DS3231 — Donanım Referansı

Bu klasör, Proje BERO'da ESP32-C3-SSR ile kullanılan DS3231 gerçek zaman saati (RTC) için referans kodu, test logu ve üretici veri sayfası bağlantısını içerir.

## Klasör içeriği

- `datasheets/`: Üreticinin resmî DS3231 veri sayfası.
- `examples/ds3231_ntp_reference.yaml`: Kullanıcının daha önce çalıştığını bildirdiği ESPHome örnek yapılandırması.
- `logs/2026-10-16_DS3231_NTP_RTC_Read_Success.md`: 16 Ekim 2026 tarihli RTC/NTP test kaydı.

## Donanım bilgileri

- MCU: ESP32-C3
- I²C SDA: GPIO0
- I²C SCL: GPIO1
- I²C frekansı: 50 kHz
- DS3231 I²C adresi: `0x68`
- Saat dilimi: Europe/Istanbul
- Bu örnek YAML'da SSR pini tanımlı değildir; proje donanım notlarında SSR kontrolü GPIO6 olarak belirtilmiştir.

## Test durumu

16 Ekim 2026 tarihli logda DS3231'in saat okuması ve RTC'den sistem saatine eşitleme mesajları görülür. Bu kayıt, pil yedeğiyle elektrik kesintisi testi yapıldığını veya SSR çıkışının fiziksel olarak doğrulandığını tek başına kanıtlamaz.

Not: ESPHome logları kalıcı bir data logger dosyası değildir.