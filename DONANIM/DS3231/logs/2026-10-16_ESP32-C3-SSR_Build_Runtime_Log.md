# Logs — ESP32-C3-SSR / DS3231 + SSR Birleşik Kod
**Tarih:** 2026-10-16  
**ESPHome:** 2026.9.1  
**Cihaz:** ESP32-C3 rev0.4, tek çekirdek  
**Derleme zamanı:** 2026-10-16 13:36:45 +0300  
**Log bağlantı zamanı:** 13:41:00 (+03:00)  
**Cihaz IP:** 192.168.0.111  
**Wi-Fi:** AKFISH — bağlı  
**Firmware OTA:** ESPHome API üzerinden log bağlantısı başarılı

## Ara kod
Birleşik DS3231 + NTP + SSR 40 s ON / 20 s OFF YAML:
[ds3231_ssr_40on_20off.yaml](../examples/ds3231_ssr_40on_20off.yaml)

Bu kayıt, kullanıcının 2026-10-16 tarihinde gönderdiği derleme/çalışma loguna ve o sırada depoda bulunan YAML dosyasına dayanır. Log, kodun derlenip cihaza yüklendiğini ve API üzerinden erişildiğini destekler; fiziksel SSR anahtarlamasının doğrulandığını göstermez.

## Doğrulananlar
- ESPHome 2026.9.1 firmware derlenmiş: `2026-10-16 13:36:45 +0300`.
- API bağlantısı ve handshake başarılı.
- ESP32-C3 rev0.4 olarak tanımlanmış.
- I²C: SDA GPIO0, SCL GPIO1, 50 kHz; bus recovery başarılı.
- I²C taramasında `0x57` ve `0x68` bulunmuş.
- SSR switch yapılandırması GPIO6, `restore_mode: ALWAYS_OFF`.
- Wi-Fi bağlı, IP `192.168.0.111`.
- NTP saati geçerli; `2026-10-16 13:41:00` raporlanmış.
- DS3231 RTC metin sensörü `13:41:00`, `13:41:05`, `13:41:10` değerlerini raporlamış.
- NTP metin sensörü `13:41:01`, `13:41:06`, `13:41:11` değerlerini raporlamış.

## Hata / dikkat noktası
Başlangıçta DS3231 sürücüsü şu hatayı vermiş:
`Communication with DS3231 failed!`
`ds3231.time is marked FAILED: unspecified`

Buna rağmen sonraki RTC metin sensörü geçerli ve ilerleyen saat değerleri raporlamış. Bu çelişkili gözlem ayrı olarak araştırılmalı; yalnızca I²C taramasında `0x68` bulunması DS3231 register haberleşmesinin bütünüyle sağlıklı olduğunu kanıtlamaz.

## Henüz kanıtlanmayanlar
- DS3231'e NTP saati yazma işleminin gerçekten başarılı olduğu (logda yalnızca komutun çağrılması/başlatılması görülürse yeterli kanıt sayılmaz).
- Wi-Fi kapalıyken RTC'nin bağımsız zaman tutması.
- GPIO6'nın elektriksel seviyesinin ölçülmesi.
- SSR giriş LED'inin yanıp sönmesi.
- SSR yük çıkışının ve bağlı yükün 40 s ON / 20 s OFF çevriminde fiziksel olarak anahtarlanması.

## Sonraki adım
Önce RTC haberleşme hatası ile geçerli görünen RTC sensör değerleri arasındaki farkı incele. Ardından loglarda `COMMAND_ON/OFF`, GPIO geri okuma ve fiziksel çıkış ölçümünü ayrı kanıt seviyeleri olarak kaydet. Fiziksel test yapılmadan SSR testi PASS olarak işaretlenmeyecek.
