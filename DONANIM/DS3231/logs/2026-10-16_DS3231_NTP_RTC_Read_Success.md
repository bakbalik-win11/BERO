# PROJE BERO — ESP32-C3-SSR Donanım Test Kaydı

- Tarih: 2026-10-16
- Cihaz: `esphome-web-0424f4` / `ESP32-C3-SSR`
- ESPHome: 2026.9.1
- Derleme zamanı: 2026-10-16 12:54:16 +0300
- Log penceresi: 13:00:53–13:02:23 (+0300)
- IP: `192.168.0.111`

## Yapılandırma

| Öğe | Logda görülen değer |
|---|---|
| MCU | ESP32-C3 rev0.4, tek çekirdek |
| I²C SDA | GPIO0 |
| I²C SCL | GPIO1 |
| I²C frekansı | 50,000 Hz |
| I²C taraması | `0x57` ve `0x68` bulundu |
| DS3231 adresi | `0x68` |
| SNTP sunucuları | `time.google.com`, `time.cloudflare.com`, `0.pool.ntp.org` |
| Saat dilimi | UTC+3 / Europe/Istanbul |
| Wi-Fi | Bağlı |
| ESPHome API | Başlangıçta başarılı; log sırasında kesinti ve yeniden bağlantı |

## Logun doğruladıkları

1. I²C veri yolu kurtarma işlemi başarılı olarak raporlandı.
2. I²C taramasında `0x57` ve `0x68` adresleri bulundu.
3. DS3231 sürücüsü sistem saatini RTC'den eşitledi.
4. `BERO DS3231 RTC Saat` sensörü geçerli ve ilerleyen zamanlar verdi: 13:00:56, 13:01:06, 13:01:36, 13:02:18 ve 13:02:23.
5. `BERO NTP Saat` de geçerli ve ilerleyen zamanlar verdi.
6. Bir `unexpected disconnect from ESPHome API` uyarısından sonra API yeniden bağlandı.

## Önemli log parçaları

```text
[13:00:53.872][C][i2c:103]:   Recovery: bus successfully recovered
[13:00:53.885][C][i2c:119]: Found device at address 0x57
[13:00:53.885][C][i2c:119]: Found device at address 0x68
[13:00:53.959][C][ds3231:051]: DS3231:
[13:00:53.959][C][ds3231:052]:   Address: 0x68
[13:00:55.139][D][ds3231:197]: RTC synchronized system clock to 2026-10-16 10:00:54 UTC
[13:00:56.209][I][rtc_test:119]: RTC_TIME: 2026-10-16 13:00:56
[13:01:05.165][D][ds3231:197]: RTC synchronized system clock to 2026-10-16 10:01:04 UTC
[13:01:06.242][I][rtc_test:119]: RTC_TIME: 2026-10-16 13:01:06
INFO Processing unexpected disconnect from ESPHome API for esphome-web-0424f4 @ 192.168.0.111
WARNING Disconnected from API
INFO Successfully connected to esphome-web-0424f4 @ 192.168.0.111
[13:02:15.843][D][ds3231:197]: RTC synchronized system clock to 2026-10-16 10:02:15 UTC
[13:02:18.739][I][rtc_test:119]: RTC_TIME: 2026-10-16 13:02:18
[13:02:23.647][I][rtc_test:119]: RTC_TIME: 2026-10-16 13:02:23
[13:02:23.752][I][ntp_test:102]: NTP_TIME: 2026-10-16 13:02:23
```

## Teknik sınırlar

- Bu log, RTC okumasının ve RTC'den sistem saatine eşitlemenin o oturumda çalıştığına dair olumlu kanıttır.
- Log, ana güç kesildikten sonra pil yedeğiyle zamanın korunduğunu tek başına kanıtlamaz.
- Log, SSR'nin fiziksel çıkışını veya bağlı yükün açılıp kapandığını doğrulamaz.
- Bu, ESPHome çalışma logudur; kalıcı depolamaya yazan bağımsız data logger dosyası değildir.
- Daha sonraki oturumda görülen DS3231 yazma hataları bu başarılı okuma/eşitleme kaydıyla karıştırılmamalıdır.
