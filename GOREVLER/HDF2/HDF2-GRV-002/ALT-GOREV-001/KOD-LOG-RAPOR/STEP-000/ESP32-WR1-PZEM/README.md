# ESP32-WR1-PZEM

Bu klasör ESP32-WR1-PZEM cihazına ait kod, log ve rapor kayıtları için oluşturulmuştur.

## Kayıtlar

- [ESPHome YAML — esphome-web-2a35cc.yaml](./esphome-web-2a35cc.yaml)
- [ESP32-WR1-PZEM logu — 2026-10-16](./ESP32-WR1-PZEM-LOG-2026-10-16.txt)
- [Teknik inceleme ve test raporu — 2026-10-16](./ESP32-WR1-PZEM-TEST-RAPORU-2026-10-16.md)

## Mevcut durum

- Log, ESPHome 2026.9.1 firmware'i çalıştıran cihazla bağlantıyı ve PZEM ölçüm okumalarını gösteriyor.
- ESP32-C3-SSR'den gelen UDP EVENT_ID 18 (OFF), 19 (ON) ve 20 (OFF) olayları alıcıda loglanmış.
- PZEM ölçümleri ile UDP olayları henüz zaman damgalı CSV kaydında birleştirilmiyor.
- Logun gönderilen kopyası son satırda tek başına "S" karakteriyle bitiyor; kaynak metin değiştirilmeden korunmuştur.
