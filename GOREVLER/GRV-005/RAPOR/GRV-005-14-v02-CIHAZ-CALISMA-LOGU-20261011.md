# PROJE BERO — GRV-005-14 v02 Çalışma Logu İncelemesi

- Tarih: 2026-10-11
- Cihaz adı: `esp32d1`
- Bağlantı: ESPHome API üzerinden `192.168.0.8`
- ESPHome sürümü: `2026.9.1`
- Derleme zamanı cihaz logunda: `2026-10-11 14:21:41 +0300`
- Kaynak: Kullanıcının paylaştığı gerçek ESP32D1OTA çalışma logu.

## Logun doğruladıkları

1. ESPHome API bağlantısı başarılı; cihazla handshake tamamlanmış.
2. Cihaz, ESPHome `2026.9.1` ile derlenmiş firmware'i çalıştırıyor.
3. CSV başlığı loga yazdırılmış; ardından aynı `measurement_id=esp32d1_247_001` ile CH0-1T, CH1-2T, CH2-3T ve BIAS satırları üretilmiş.
4. Üç ADC kanalının her birinde `sample_count=1000`; BIAS satırında da `sample_count=1000` görünüyor.
5. PZEM sensörleri çalışıyor ve logda yaklaşık `0.028–0.029 A`, `1.60–1.70 W`, `PF=0.25–0.26` değerleri görülüyor.
6. Dört satır aynı ölçüm penceresi kimliğini taşıyor; bu, tek pencerelik rapor üretiminin çalıştığına dair kanıttır.

## Logda görülen teknik notlar

- `invalid_count` alanı sayısal bir değer yerine `NOT_TRACKED` olarak yazılmış. CSV şeması ve Python QC bunu açıkça desteklemiyorsa bu alan sonraki QC adımında ele alınmalı.
- `window_center_epoch_s` ve `pzem_timestamp` alanları boş görünüyor. Bu log, gerçek PZEM yanıt zaman damgasının elde edildiğini kanıtlamıyor.
- Başlık satırı logda `pzem_pf,pz` kısmında kesilmiş görünüyor. Bu, log satırı sınırı/kesilmesi olabilir; tam CSV başlığının cihaza yazılan gerçek biçimi ayrıca kontrol edilmeli.
- ESPHome, ESP32 revizyonu için `minimum_chip_revision: "3.1"` ve `sram1_as_iram: true` ayarlarını öneriyor. Bunlar uyarı; bu logda derleme/bağlantı hatası değiller.
- `adc.sensor took a long time ... (83 ms), max is 50 ms` uyarısı var. Ölçüm raporu üretildi, ancak bu gecikme not edilmeli; zamanlama davranışı ayrıca değerlendirilmeli.

## Sonuç ve sınırlar

**Çalışma logu: cihaz bağlantısı, PZEM telemetrisi ve dört adet 1000 örnekli rapor satırının üretilmesi açısından olumlu kanıt sunuyor.**

Bu log tek başına şu iddiaları doğrulamaz:
- CSV'nin baştan sona 41 sütunla eksiksiz ve doğru hizalı olduğunu,
- tüm boş alanların ve veri türlerinin Python QC'den geçtiğini,
- PZEM zaman eşlemesinin gerçek yanıt zamanına dayandığını,
- sürekli/tekrarlı ölçüm döngüsünün çalıştığını.

## Kaynak kodu kayıt durumu

Bu rapor gerçek çalışma loguna dayalı yeni ve ayrı bir kayıttır; eski statik inceleme raporları korunur. Depoda derlenen YAML'ın birebir kaynağı doğrulanmadan yerel statik aday dosya, derlenmiş kaynak kod diye `KOD` klasörüne kopyalanmamalıdır. Derlenen dosyanın gerçek içeriği eşleştirildiğinde kaynak kod ayrı sürüm olarak kaydedilmelidir.
