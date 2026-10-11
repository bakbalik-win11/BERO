# GRV-005-14 v04 — Çalışan Kod Kaydı

## Hedef
Dört ADC kanalından 1000'er örnek toplamak, CSV başlığını iki log parçası olarak yazdırmak ve raporlamayı ADC `on_value` akışından ayırmak.

## Donanım / yazılım
- ESP: `esp32d1`
- ADC: GPIO33 (CH0-1T), GPIO34 (CH1-2T), GPIO35 (CH2-3T), GPIO32 (BIAS)
- PZEM UART: TX GPIO16 / RX GPIO17, 9600 baud
- ESPHome: 2026.9.1
- Cihaz: ESP32 rev3.1, 2 çekirdek

## Derleme ve cihaz kaydı
Gerçek cihaz logu firmware derleme zamanını `2026-10-11 14:40:42 +0300` olarak bildiriyor. Cihaz `192.168.0.8` üzerinden API ile bağlanmış; handshake başarılı. Bu kayıt kullanıcı tarafından sağlanan gerçek cihaz loguna dayanır.

## v04 değişiklikleri
1. Dört kanalın 1000 örneğe ulaşması `interval: 50ms` kontrolü ile izlenir.
2. Uzun CSV başlığı `CSV_HEADER_PART_1` ve `CSV_HEADER_PART_2` olarak yazdırılır.
3. Cihaz adı `esp32d1` korunmuştur.
4. Önceki v03 ve aday dosyaları değiştirilmemiştir.

## Gerçek cihaz logu sonucu
- CH0-1T: 1000 örnek
- CH1-2T: 1000 örnek
- CH2-3T: 1000 örnek
- BIAS: 1000 örnek
- Başlık: 16 + 25 = 41 alan
- Dört veri satırı: her biri 41 alan
- Ölçüm penceresi: 251–10309 ms, süre 10058 ms, merkez 5280 ms
- PZEM güncelleme zamanı: 9425 ms; merkezden fark: 4145 ms
- CSV satırları yazdırıldıktan sonra `interval took a long time (92 ms), max is 50 ms` uyarısı görüldü.

## Sınırlamalar
- `pzem_update_millis`, PZEM akım sensörünün `on_value` anında kaydedilir; gerçek Modbus paket zaman damgası değildir.
- PZEM gerilim, frekans ve enerji alanları bu YAML'da doldurulmadığından boş kalır.
- ADC `update_interval: 10ms` ayarı gerçek örneklerin kesin 10 ms aralıklarla alındığını kanıtlamaz.
- Derleme uyarıları: `minimum_chip_revision: "3.1"` ve `sram1_as_iram: true` seçenekleri öneriliyor; bunlar bu testte derleme başarısızlığı değildir.

## Dosyalar
- Çalışan kod: `GOREVLER/GRV-005/KOD/GRV-005-14-v04-CALISAN-KOD.yaml`
- Ham log: `GOREVLER/GRV-005/LOG/GRV-005-14-v04-GERCEK-CIHAZ-LOGU-20261011.txt`
- Değerlendirme: `GOREVLER/GRV-005/RAPOR/GRV-005-14-v04-LOG-DEGERLENDIRME-20261011.md`
