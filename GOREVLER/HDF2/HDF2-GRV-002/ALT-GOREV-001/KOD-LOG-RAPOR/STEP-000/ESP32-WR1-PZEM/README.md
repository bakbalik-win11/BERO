# ESP32-WR1-PZEM

Bu klasör ESP32-WR1-PZEM cihazına ait kod, log ve rapor kayıtları için oluşturulmuştur.

## Kayıtlar

- [ESPHome YAML — esphome-web-2a35cc.yaml](./esphome-web-2a35cc.yaml)
- [ESP32-WR1-PZEM logu — 2026-10-16](./ESP32-WR1-PZEM-LOG-2026-10-16.txt)
- Test raporları

## Mevcut durum

- YAML dosyası kullanıcı tarafından sağlanan haliyle kaydedildi.
- Bu logda ESPHome 2026.9.1 cihazla bağlantı kuruyor; PZEM ölçümleri okunuyor.
- UDP alıcısı, ESP32-C3-SSR cihazından gelen olayları alıyor ve logluyor.
- UDP olayları henüz CSV'ye kaydedilmiyor.
- Kaydedilen log dosyasının sonu, kullanıcı tarafından sağlanan metinde tek başına "S" karakteriyle bitiyor; kaynak bu haliyle korunmuştur.
