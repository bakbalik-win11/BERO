# ADR-020 — E00F ct_clamp kodunun Modül 2 SCT-1 pinlerine uyarlanması

- **Tarih:** 2026-10-31
- **Durum:** KOD DEPOYA KAYDEDİLDİ; derleme/OTA/fiziksel test bekliyor
- **Firmware:** [esp32d1.yaml](../../firmware/esp32d1.yaml)

## Pin uyarlaması

E00F kodundaki dört ADC pininin işlevi Modül 2'ye bire bir taşınamaz. E00F'de GPIO32/33 aynı SCT düğümüne, GPIO34/35 aynı bias düğümüne bağlanmıştı. Modül 2'de GPIO32/33/34 birbirinden bağımsız SCT soketleridir; GPIO35 ortak bias ölçümüdür.

Bu nedenle tek SCT-1 testi için:
- SCT-1 sinyali: GPIO32 / ADC1_CH4
- Ortak bias: GPIO35 / ADC1_CH7
- GPIO33 ve GPIO34: diğer fiziksel SCT soketleri; bu firmware'de kullanılmaz
- E00F RAW count çift girişleri bu pin düzeninde yoktur; paralel analog bağlantı olmadan eklenemez.

## Korunan E00F ölçüm yolu

- ADC attenuation 12 dB
- `ct_clamp` penceresi 200 ms
- `ct_clamp` yayın aralığı 2 s
- `on_raw_value` ile pencere RMS gerilimini ayrı Raw AC template entity'sine yayınlama
- Akım dönüşüm katsayısı 24.22
- Yazılımsal sıfırlama eşiği yok

Katsayı E00F kodundan aynen taşınmıştır; Modül 2'de doğrulanmış kalibrasyon olarak kabul edilmez.

## Beklenen doğrulama

ESPHome derlemesi, cihaz adı `esp32d1` ile OTA, SCT-1 bağlı test ve gece kaydı beklenmektedir. Bu ADR kod uyarlama kararını kaydeder; çalışma başarısı iddiası değildir.
