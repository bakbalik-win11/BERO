# PROJE BERO — ESP32-C3-SSR Donanım Test Kaydı

- **Kayıt tarihi:** 2026-10-16
- **Cihaz:** `esphome-web-0424f4`
- **Friendly name:** `ESP32-C3-SSR`
- **ESPHome:** 2026.9.1
- **Derleme zamanı:** 2026-10-16 12:54:16 +0300
- **Log penceresi:** 13:00:53–13:02:23 (+0300)
- **IP:** `192.168.0.111`
- **Amaç:** ESP32-C3, I²C üzerindeki DS3231 RTC ve SNTP zaman kaynağının gözlemlenmesi.

## Donanım ve yapılandırma

| Öğe | Logda görülen değer |
|---|---|
| MCU | ESP32-C3 rev0.4, tek çekirdek |
| I²C SDA | GPIO0 |
| I²C SCL | GPIO1 |
| I²C frekansı | 50,000 Hz |
| I²C taraması | `0x57` ve `0x68` bulundu |
| DS3231 adresi | `0x68` |
| SNTP sunucuları | `time.google.com`, `time.cloudflare.com`, `0.pool.ntp.org` |
| Saat dilimi | UTC+3 / Europe/Istanbul yapılandırması |
| Wi-Fi | Bağlı |
| ESPHome API | İlk bağlantı başarılı; log sırasında bir kesinti ve yeniden bağlantı var |

## Sonuçlar — yalnızca logun doğruladıkları

1. ESPHome API bağlantısı başlangıçta başarılı oldu.
2. I²C veri yolu kurtarma işlemi başarılı olarak raporlandı.
3. I²C taramasında `0x57` ve `0x68` adresleri bulundu.
4. DS3231 sürücüsü sistem saatini RTC'den eşitledi:
   - `13:00:55` civarında: `RTC synchronized system clock to 2026-10-16 10:00:54 UTC`
   - Bu mesaj sonraki aralıklarla tekrarlandı.
5. `BERO DS3231 RTC Saat` metin sensörü geçerli ve ilerleyen zamanlar verdi; örnekler:
   - `2026-10-16 13:00:56`
   - `2026-10-16 13:01:06`
   - `2026-10-16 13:01:36`
   - Yeniden bağlantıdan sonra `2026-10-16 13:02:18` ve `13:02:23`
6. `BERO NTP Saat` de geçerli ve ilerleyen zamanlar verdi.
7. Logda bir `unexpected disconnect from ESPHome API` uyarısı görüldü; cihaz daha sonra yeniden bağlandı.

## Teknik değerlendirme ve sınırlar

- Bu log, **RTC okumasının ve RTC'den sistem saatine eşitlemenin o oturumda çalıştığına dair olumlu kanıttır**.
- Bu kesitte `NTP_TIME` değerlerinin geçerli olduğu görülür; ancak `BERO_NTP_SYNC_OK` mesajı bu log parçasında yer almadığından, burada NTP eşitleme olayının tam zamanını ayrıca doğrulayamıyoruz.
- I²C taramasında `0x68` görülmesi tek başına tüm RTC işlemlerinin başarılı olduğunu kanıtlamaz; bu kayıtta ayrıca RTC okuma ve eşitleme logları da vardır.
- Bu log, ana güç kesildikten sonra pil yedeğiyle zamanın korunduğunu **tek başına kanıtlamaz**.
- Bu log, SSR'nin fiziksel çıkışını veya bağlı yükün açılıp kapandığını doğrulamaz.
- Bu YAML/log, kalıcı depolamaya dosya yazan bağımsız bir data logger'ın varlığını kanıtlamaz; burada gözlenen şey ESPHome logları ve zaman sensörleridir.
- Daha sonraki bir oturumda görülen DS3231 yazma hataları bu kayıtla karıştırılmamalıdır. Bu kayıt ayrı bir başarılı RTC okuma/eşitleme örneği olarak saklanmalıdır.

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

## Önerilen dosya konumu

```text
ESP32-C3-SSR/
└── logs/
    └── 2026-10-16_DS3231_NTP_RTC_Read_Success.md
```

**Kayıt durumu:** Bu belge, kullanıcının sohbette paylaştığı logdan oluşturulmuş bir test kaydıdır. Proje deposuna veya fiziksel donanım klasörüne otomatik olarak eklenmiş değildir.