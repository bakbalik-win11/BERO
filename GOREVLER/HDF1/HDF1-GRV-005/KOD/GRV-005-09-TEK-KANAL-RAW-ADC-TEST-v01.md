# GRV-005-09 — Tek kanal raw ADC testi v01

- Tarih: 2026-10-11
- Kod dosyası: `GRV-005-09-TEK-KANAL-RAW-ADC-TEST-v01.yaml`
- Cihaz adı: `esp32d1` (değiştirilmedi)
- Framework: ESP-IDF
- Kanal: GPIO33 / 1T
- Derleme durumu: **Kullanıcı tarafından başarılı olduğu bildirildi.**
- Cihaza yükleme: Bu kayda göre doğrulanmadı.
- Gerçek ADC logu: Bu kayda göre henüz doğrulanmadı.

## Hedef

ESPHome ADC bileşenindeki `raw: true` seçeneğiyle tek kanalda ham ADC kodu elde edilebilecek en küçük tanılama yapılandırmasını saklamak.

## Yapılandırma özeti

- ESP32 klasik varyantı ve ESP-IDF.
- GPIO33 ADC sensörü.
- `raw: true`, `attenuation: 12db`, `update_interval: 1s`.
- `on_value` log satırı `GPIO33 raw ADC value` etiketiyle değeri yazdırır.
- Bu kodda `invalid_count`, 1000 örnek penceresi, istatistik, PZEM eşleştirmesi veya CSV üretimi yoktur.

## Sonuç ve sınırlar

Kullanıcının derleme bildirimi, bu yapılandırmanın derlendiğini kayda geçirir. Bu, kodun cihaza yüklendiği veya gerçek GPIO33 ADC değerlerinin ham kod olarak doğrulandığı anlamına gelmez. Cihaz testi ayrı bir aşamadır.

## Sonraki adım

Cihaza yükleme yapılacaksa önce bunun mevcut `esp32d1` yapılandırmasının yerini alacağı açıkça kararlaştırılmalıdır. Kullanıcı onayı olmadan yükleme ya da canlı yapılandırma değişikliği yapılmamalıdır. Cihaz logunda görülen değerler ve test koşulu daha sonra ek bir sonuç raporuna kaydedilir.

## Geçmişi koruma

Bu v01 dosyası yeni ve ayrı bir görev kaydıdır. ALT09, ALT10, GRV-004 snapshot'ları ve mevcut çalışan yapılandırmaların üzerine yazmaz.
