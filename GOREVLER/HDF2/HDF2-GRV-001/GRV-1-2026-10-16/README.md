# Hedef 2 / GRV-1 — Kod ve log açıklaması (16.10.2026)

Bu klasör, bugünkü sohbetin Hedef 2 / GRV-1 isteği için düzenlenmiştir. Ana kaynak ESP32-C3-SSR kodu ve onun RTC/NTP/UDP çalışma loglarıdır. Hedef 2'nin PZEM UDP alıcı kodu ve alıcı logu da karşılaştırma için ayrıca kopyalanmıştır.

## Dosyalar
- `KOD/ESP32-C3-SSR_RTC_NTP_UDP.yaml`: SSR zaman çevrimi, DS3231/NTP, BOOT_ID/EVENT_ID ve UDP broadcast.
- `KOD/ESP32-WR1-PZEM_UDP.yaml`: PZEM-004T ölçümü ve UDP port 4210 alıcısı.
- `LOG/ESP32-C3-SSR_20261016_1358.txt`: DS3231 iletişim hatası görülen oturum.
- `LOG/ESP32-C3-SSR_20261016_1450.txt`: RTC yazma hatası ve SSR UDP olayları görülen oturum.
- `LOG/2026-10-16_DS3231_NTP_RTC_Read_Success.md`: 13:00–13:02 başarılı RTC okuma/eşitleme kaydı.
- `RAPOR/2026-10-16_HDF2_GRV1_KOD_LOG_RAPORU.md`: adım adım günlük rapor.

## Not
Ham loglar kanıt olarak korunur. Başarılı erken RTC oturumu ile daha sonraki DS3231 hataları birbirine karıştırılmaz. Kullanıcının SSR'nin fiziksel ON/OFF davranışını gözle doğruladığı bilgisi tamamlanmış test olarak kabul edilir.
