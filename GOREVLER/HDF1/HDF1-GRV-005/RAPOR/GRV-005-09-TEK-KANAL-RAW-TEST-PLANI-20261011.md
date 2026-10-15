# GRV-005-09 — Tek kanal raw ADC tanılama testi

- Tarih: 2026-10-11
- Durum: Derleme öncesi taslak; kod KOD klasörüne taşınmadı.
- Amaç: ESPHome ADC bileşeninde `raw: true` ile tek bir klasik ESP32 ADC kanalından ham kod çıktığını doğrulamak.
- Kanal: GPIO33 (1T)
- Framework: ESP-IDF; bu seçim GRV-004 YAML snapshot'ıyla uyumludur. Test öncesi aktif YAML/framework sürümü kullanıcı tarafından doğrulanmalıdır.
- Cihaz adı: `esp32d1` olarak korunmuştur. Bu dosya yalnızca derleme testine yöneliktir; cihaza yüklenmemelidir.

## Tasarım sınırları

- Tek ADC sensörü, GPIO33.
- `raw: true`, `attenuation: 12db`.
- `update_interval: 1s`; ilk testte hızlı örnekleme hedeflenmez.
- Her sensör güncellemesi loga bir ham değer olarak yazılır.
- ADC sürücü hata kodu gözlenmediği için `invalid_count` üretilmez.
- PZEM, dört kanal, 1000 örnek penceresi, istatistikler ve CSV bu testte yoktur.
- Aynı `esp32d1` cihazına OTA yükleme yapılmamalıdır. Önce yalnızca derleme doğrulanır; yükleme ancak açıkça planlanan ayrı bir adımda yapılabilir.

## Başarı ölçütü

1. ESPHome yapılandırması doğrulaması ve derleme hatasız tamamlanır.
2. Derleme çıktısı ESP32 klasik varyantı ve ESP-IDF framework'ü ile tutarlıdır.
3. Daha sonraki cihaz testinde GPIO33 sensör logundaki değerler ham ADC kodu olarak gözlemlenir; bu cihaz testi henüz yapılmış sayılmaz.

## Kaynak

ESPHome ADC resmi belgesi: https://esphome.io/components/sensor/adc/

## Durum

Bu rapor bir tasarım kaydıdır. YAML henüz derlenmedi, cihaza yüklenmedi veya gerçek ADC verisiyle doğrulanmadı. Kullanıcı derleme sonucunu paylaşmadan kod KOD klasörüne taşınmayacaktır.
