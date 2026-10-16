# Proje BERO — Ara Kod Kaydı

## Güncel ara sürüm
- [Birleşik DS3231 + NTP + SSR YAML](../examples/ds3231_ssr_40on_20off.yaml)
- [2026-10-16 derleme ve çalışma logu](../logs/2026-10-16_ESP32-C3-SSR_Build_Runtime_Log.md)

## Değişiklik
Copilot incelemesi dikkate alınarak olay kayıtları geliştirildi:
- Komutlar `COMMAND_ON` / `COMMAND_OFF` olarak ayrı loglanır.
- GPIO6 pad seviyesi okunarak `GPIO_ON_CONFIRMED` / `GPIO_OFF_CONFIRMED` veya mismatch olayı loglanır.
- Olay zaman damgası için RTC önceliklidir; RTC geçersizse NTP, ikisi de geçersizse `SOURCE=NONE` kaydedilir.

## Durum
- Önceki sürüm ESPHome 2026.9.1 ile derlenmiş ve cihaz API üzerinden erişilebilir olmuştu.
- Bu yeni kod revizyonu GitHub'a kaydedildi; yeni sürüm için yeniden derleme sonucu henüz yok.
- DS3231 başlangıç iletişim hatası ile sonraki geçerli görünen RTC metin sensörü değerleri arasındaki çelişki açık iş.
- GPIO geri okuması fiziksel SSR/yük çıkışının doğrulanması değildir.
- Fiziksel SSR testi henüz PASS değildir.
