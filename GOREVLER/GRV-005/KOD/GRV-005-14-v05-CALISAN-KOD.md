# GRV-005-14 v05 — Çalışan Kod Kaydı

## Hedef
Dört ADC kanalından 1000'er örnek toplamak ve CSV başlığı ile kanal satırlarını ayrı, aralıklı script adımlarında yazdırmak.

## Donanım / yazılım
- ESP: `esp32d1`
- CH0-1T: GPIO33
- CH1-2T: GPIO34
- CH2-3T: GPIO35
- BIAS: GPIO32
- PZEM UART: TX GPIO16 / RX GPIO17, 9600 baud
- ESPHome 2026.9.1; ESP32 rev3.1, 2 core

## Derleme kanıtı
Gerçek cihaz logu firmware'in `2026-10-11 14:49:24 +0300` tarihinde derlendiğini bildiriyor. API bağlantısı ve handshake başarılı. Bu kayıt kullanıcı tarafından sağlanan gerçek cihaz loguna dayanır.

## Değişiklik
v04'te görülen 92 ms uyarısına karşı rapor başlığı ve satırları ayrı script adımlarına ayrıldı; adımlar arasında 20 ms gecikmeler eklendi.

## Gerçek log sonucu
- 4 kanalın her biri 1000 örnek raporladı.
- Başlık iki parçalı: 16 + 25 = 41 alan.
- Dört veri satırının her biri 41 alan.
- Bu log parçasında önceki `interval took a long time (92 ms)` uyarısı görünmüyor.
- Ancak PZEM zaman damgası/delta ve PZEM alanları satırlar arasında tutarsız; bkz. değerlendirme raporu.

## Durum
Kod kullanıcı tarafından derlenmiş ve gerçek cihaz logu alınmış sürüm olarak kaydedildi. CSV alan yapısı iyi; PZEM snapshot tutarlılığı için bir sonraki sürüm gerekli.

## İlgili dosyalar
- `GOREVLER/GRV-005/KOD/GRV-005-14-v05-CALISAN-KOD.yaml`
- `GOREVLER/GRV-005/LOG/GRV-005-14-v05-GERCEK-CIHAZ-LOGU-20261011.txt`
- `GOREVLER/GRV-005/RAPOR/GRV-005-14-v05-LOG-DEGERLENDIRME-20261011.md`
