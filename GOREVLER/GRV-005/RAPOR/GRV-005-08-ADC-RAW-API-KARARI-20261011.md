# GRV-005-08 — ADC ham veri API'si: ön karar

- Tarih: 2026-10-11
- Durum: Kaynak incelemesi tamamlandı; kod seçimi ve derleme testi bekliyor.
- Kapsam: ESPHome ADC platformunun ham değer modu ile ESP-IDF oneshot API'sinin farkı.
- Mevcut firmware değiştirilmedi; yeni YAML yazılmadı veya yüklenmedi.

## 1. Kaynak bulguları

ESPHome ADC bileşeninin resmi belgelerinde ESP32 için `raw: true` seçeneği açıklanır. Klasik ESP32'de ham ADC kodları 0–4095 aralığındadır. Bu seçenek, kalibre edilmiş voltaj yerine ham ADC kodlarını kullanmayı incelemek için ilk düşük karmaşıklıklı adaydır.

Espressif ESP-IDF ADC oneshot sürücüsünde `adc_oneshot_read(handle, channel, &out_raw)` ham dönüşüm sonucunu ve `esp_err_t` durum kodunu verir. Başarı `ESP_OK`; belgelenen hatalar arasında geçersiz argüman ve zaman aşımı bulunur. Böylece sürücü düzeyinde okuma hatası ile geçerli ham sıfır kodunu kavramsal olarak ayırmak mümkündür.

Kaynaklar:
- ESPHome ADC belgesi: https://esphome.io/components/sensor/adc/
- ESP-IDF oneshot ADC belgesi: https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32/api-reference/peripherals/adc_oneshot.html

## 2. İki yolun karşılaştırması

### Yol A — ESPHome ADC sensörü, `raw: true`
- Artı: Mevcut ESPHome ADC sensörüne yakın; uygulama değişikliği daha küçük.
- Artı: Ham ADC kodlarını toplama gereksinimine uygun aday.
- Sınır: Sensörün `on_value` callback'i tek başına her alt düzey ADC denemesinin hata durumunu gösterdiğini kanıtlamaz.
- Sonuç: Ham kod toplama için ilk prototip adayı; `invalid_count` donanım okuma hatası sayacı olarak varsayılamaz.

### Yol B — Doğrudan ESP-IDF `adc_oneshot_read()`
- Artı: Ham kod ve sürücü durum kodu aynı çağrıdan elde edilir.
- Sınır: ESPHome bileşeninin ADC sürücüsünü zaten yönetip yönetmediği ve ikinci bir handle/driver kullanmanın çatışma riski incelenmelidir. Aynı ADC birimini iki ayrı katmanın bağımsız sahiplenmesi kabul edilmez.
- Sınır: Mevcut aktif firmware framework'ü ve sürümü kesinleştirilmeden bu yol için kod yazılmamalıdır.
- Sonuç: Hata sayımı gerçekten gerekliyse olası yol; doğrudan API kullanımı ancak sürücü sahipliği ve entegrasyon modeli doğrulandıktan sonra.

## 3. Kritik yapılandırma belirsizliği

Kaydedilmiş GRV-004 kullanıcı YAML snapshot'ında `framework: type: esp-idf` bulunuyor. Önceki çalışma notlarında ALT10 için Arduino framework ifadesi de geçiyor. Bu belgeler aynı yapılandırmanın aktif ve güncel olduğunu kanıtlamıyor. Bu nedenle yeni kod yazmadan önce derleme için kullanılacak gerçek YAML/framework sürümü esas alınmalıdır. Cihaz adı `esp32d1` kullanıcı talebi olmadan değiştirilmeyecek.

## 4. Önerilen sonraki adım

1. Aktif YAML'ın framework ve ESPHome sürümünü doğrula.
2. Önce Yol A ile ayrı tanılama YAML'ında `raw: true` değerlerinin gerçekten ham kod olup olmadığını küçük bir tek-kanal testinde doğrula.
3. Bu testin derleme sonucu ve cihaz logu ayrı ayrı kaydedilsin.
4. `invalid_count` gereksinimi için Yol A'nın yeterli olmadığı doğrulanırsa, ADC sürücü sahipliğini ve ESPHome entegrasyonunu inceleyerek Yol B'yi tasarla.
5. Derleme onayı olmadan kodu KOD klasörüne taşıma; mevcut çalışan YAML'ı değiştirme.

## 5. Henüz iddia edilemeyenler

- Bu rapor bir YAML'ın derlendiğini veya cihaza yüklendiğini söylemez.
- `raw: true` davranışı mevcut cihazda henüz test edilmedi.
- `invalid_count` uygulaması karara bağlanmadı.
- Gerçek örnekleme aralığı, dört kanalın zaman ilişkisi, 1000 deneme garantisi, PZEM hizalaması ve CSV üretimi doğrulanmadı.
