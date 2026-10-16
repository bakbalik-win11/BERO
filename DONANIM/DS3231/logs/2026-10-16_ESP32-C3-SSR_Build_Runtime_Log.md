# Logs — ESP32-C3-SSR / DS3231 + SSR Birleşik Kod
**Tarih:** 2026-10-16  
**ESPHome:** 2026.9.1  
**Cihaz:** ESP32-C3 rev0.4, tek çekirdek  
**Derleme zamanı:** 2026-10-16 13:36:45 +0300  
**Log bağlantı zamanı:** 13:41 (+03:00)  
**Cihaz IP:** 192.168.0.111

## İlk derleme ve çalışma gözlemi
- Firmware derlenmiş ve ESPHome API bağlantısı başarılı.
- I²C: SDA GPIO0, SCL GPIO1, 50 kHz; bus recovery başarılı.
- Tarama `0x57` ve `0x68` adreslerini bulmuş.
- SSR switch GPIO6, `restore_mode: ALWAYS_OFF`.
- Wi-Fi bağlı; NTP zamanı geçerli.
- RTC metin sensörü 13:41:00, 13:41:05 ve 13:41:10 değerlerini; NTP sensörü 13:41:01, 13:41:06 ve 13:41:11 değerlerini raporlamış.

## Önemli DS3231 uyarısı
Başlangıçta `Communication with DS3231 failed!` ve `ds3231.time is marked FAILED: unspecified` logları görülmüş. Sonraki RTC metin sensörü geçerli zaman raporlamış. Bu çelişki henüz çözülmedi. I²C taramasında `0x68` bulunması tek başına register haberleşmesinin sağlıklı olduğunu kanıtlamaz.

## Copilot incelemesi sonrası kod değişikliği
Birleşik YAML dosyası güncellendi:
[ds3231_ssr_40on_20off.yaml](../examples/ds3231_ssr_40on_20off.yaml)

Yeni olay logları:
- `COMMAND_ON` / `COMMAND_OFF`: yazılım komutunu belirtir.
- `GPIO_ON_CONFIRMED` / `GPIO_OFF_CONFIRMED`: GPIO6 pad seviyesinin okunup beklenen lojik seviyeye eşleştiğini belirtir.
- `GPIO_ON_READBACK_MISMATCH` / `GPIO_OFF_READBACK_MISMATCH`: okunan seviyenin beklenen seviyeden farklı olduğunu belirtir.
- Olay zaman damgasında öncelik RTC, sonra NTP; ikisi de geçersizse `SOURCE=NONE`.

**Not:** GPIO pad geri okuması, SSR giriş LED'inin veya yük çıkışının fiziksel çalıştığını kanıtlamaz. Bunun için bağımsız fiziksel gözlem/ölçüm gerekir.

## Test durumu
- İlk firmware derlemesi ve API bağlantısı: PASS.
- Yeni zaman damgalı olay/GPIO geri okuma revizyonu: depoya kaydedildi; henüz yeniden derlenip doğrulanmadı.
- DS3231 yazma işleminin gerçekten başarılı olması: doğrulanmadı.
- Wi-Fi kapalı RTC testi: doğrulanmadı.
- SSR LED/yük tarafı fiziksel çevrim testi: bekliyor.
