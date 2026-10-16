# Proje BERO — Ara Kod Kaydı

Bu klasör, DS3231 + NTP + SSR birleşik test kodunun ara sürüm kaydını tutar.

## Mevcut derlenen sürüm
- [Birleşik YAML](../examples/ds3231_ssr_40on_20off.yaml)
- [2026-10-16 derleme ve çalışma logu](../logs/2026-10-16_ESP32-C3-SSR_Build_Runtime_Log.md)

## Durum
- Derleme/firmware: ESPHome 2026.9.1, 2026-10-16 13:36:45 +0300.
- API bağlantısı başarılı; cihaz IP: 192.168.0.111.
- I²C taramasında 0x57 ve DS3231 adresi 0x68 görüldü.
- Başlangıçta DS3231 iletişim hatası kaydedildi; sonraki RTC metin sensörü geçerli saat gösterdi. Bu çelişki açık inceleme maddesidir.
- SSR GPIO6 yazılım yapılandırması mevcut.
- Fiziksel SSR/yük anahtarlaması henüz doğrulanmadı.

Bu ara sürüm, fiziksel test PASS olarak değerlendirilmemiştir.
