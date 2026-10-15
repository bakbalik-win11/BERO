# PROJE BERO — GRV-005-14 v06 gerçek cihaz logu değerlendirmesi

**Tarih:** 2026-10-11  
**Firmware:** ESPHome 2026.9.1, derleme zamanı 14:59:19 +0300  
**Cihaz:** `esp32d1`, ESP32 rev3.1, 2 çekirdek  
**Kaynak:** `GOREVLER/GRV-005/LOG/GRV-005-14-v06-GERCEK-CIHAZ-LOGU-20261011.txt`

## Sonuç

- **Derleme/bağlantı:** Kullanıcı bildirimi ve logda başarılı bağlantı/handshake görülüyor.
- **CSV başlığı:** İki bölüm halinde basılmış.
- **Kanal sayısı:** CH0-1T, CH1-2T, CH2-3T ve BIAS için dört satır mevcut.
- **Örnek sayısı:** Her satırda 1000.
- **PZEM snapshot tutarlılığı:** Dört satırda `pzem_update_millis=9532`, `time_delta_ms=4158`, akım `0.028 A`, güç `1.700 W`, PF `0.2600`. Önceki v05 logunda görülen satırlar arası değişim bu logda görünmüyor.
- **Zaman hesabı:** `9532 - 5374 = 4158`; delta hesabı doğru.
- **Örnekleme penceresi:** başlangıç 235, bitiş 10513, süre 10278, merkez 5374. `10513 - 235 = 10278` ve `235 + 10278/2 = 5374` hesapları doğru.
- **92 ms interval uyarısı:** Bu log kesitinde görünmüyor; tek log bunun hiçbir koşulda oluşmayacağını kanıtlamaz.
- **ESPHome önerileri:** `minimum_chip_revision: "3.1"` ve `sram1_as_iram: true` optimizasyon önerileridir; bu logda derleme/bağlantı hatası değiller.

## Dikkat

`pzem_update_millis`, mevcut kodda PZEM akım sensörünün `on_value` callback anında alınır; gerçek Modbus yanıtının tel üzerindeki zaman damgası değildir. `window_center_epoch_s` ve `pzem_timestamp` alanları bu kodda boş kalmaktadır. Median ve yüzdelik alanlar da henüz hesaplanmıyor; boş alanlar bilinçli olarak korunmuştur.

## Karar

v06, kullanıcı tarafından derlendiği bildirilen ve gerçek cihazda dört satırlı CSV çıktısı üreten sürüm olarak kaydedildi. Önceki v05 ve daha eski deneyler değiştirilmedi.