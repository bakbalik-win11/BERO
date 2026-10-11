# GRV-005-01 — İlk PZEM zaman damgası log incelemesi

- Tarih: 2026-10-11
- Kaynak: Kullanıcının sağladığı ESPHome logu (ESP32D1, ESPHome 2026.9.1).
- YAML sürümü: GRV-005-01 PZEM timestamp diagnostic v01.
- Derleme: Kullanıcı tarafından başarılı bildirildi.
- Cihaza yükleme: Logda cihazın çalıştığı ve API bağlantısının kurulduğu görülüyor.
- Donanım doğrulama seviyesi: İlk zamanlama davranışı gözlendi; Modbus sorgu/yanıtı bağımsız olarak sayılmadı.

## Gözlemler

1. Cihaz ESPHome 2026.9.1 ile açılıyor; ESP32 rev3.1, Wi-Fi bağlı ve ESPHome API bağlantısı başarılı.
2. UART: TX GPIO16, RX GPIO17, 9600 baud, 8N1. PZEMAC adresi 0x01.
3. PZEM sensör alanları yaklaşık her 5 saniyede bir yayımlanıyor. Örnek akım güncellemeleri:
   - 09:26:42.094 — 0.028 A
   - 09:26:47.107 — 0.028 A
   - 09:26:52.093 — 0.028 A
   - 09:26:57.092 — 0.028 A
   - 09:27:02.083 — 0.028 A
   - 09:27:07.097 — 0.028 A
   - 09:27:12.091 — 0.028 A
   - 09:27:17.081 — 0.028 A
   - Kayıt devamında da yaklaşık 5 saniyelik ritim sürüyor.
4. Akım sayısal olarak 0.028 A sabit kalırken `pzem_update_millis` düzenli yenileniyor. Örnekler:
   - 6436 → 11449 → 16448 → 21446 → 26439 → 31452 → 36445 → 41438 → 46446 → 51439 ms.
5. Her PZEM güncellemesinden yaklaşık 0.8 saniye sonra `age_ms` yaklaşık 800–820 ms seviyesine düşüyor; sonraki saniyelik tanı kayıtlarında artarak bir sonraki güncellemeden önce yaklaşık 4.8 saniyeye ulaşıyor.
6. SNTP başlangıçta eşitlenmemiş. Logda 09:27:09.786'da saat eşitlendiği görülüyor; daha sonra epoch_s alanı görünür hale geliyor. Bu başlangıçtaki `CLOCK_NOT_SYNCED` kayıtlarını açıklıyor.
7. PZEM gerilimi yaklaşık 229–231 V, akım 0.028 A, güç yaklaşık 1.5–1.8 W görünüyor. Bu kayıt gerçek 0 A testi değildir.

## Sonuç

**İlk zaman damgası hipotezi için olumlu kanıt:** Sabit 0.028 A değerinde PZEM sensör güncellemeleri sürerken `on_value` içindeki `millis()` işareti yaklaşık 5 saniyede bir yenileniyor. Dolayısıyla bu ESPHome/PZEM yapılandırmasında `on_value` yalnızca akım sayısal olarak değiştiğinde tetikleniyor gibi görünmüyor.

Bu sonuç şu iddiayı henüz kanıtlamaz: “Her başarılı Modbus yanıtı, tam olarak bir `on_value` üretir.” Logda Modbus başarılı yanıtları bağımsız bir sayaçla kaydedilmediği için sorgu, yanıt ve sensör yayını bire bir eşleştirilmiş değildir.

## Açık kalan doğrulamalar

1. Gerçek 0 A koşulunda PZEM güncellemesi ve `on_value` devam ediyor mu?
2. Sabit akımda daha uzun gözlemde her sensör güncellemesiyle zaman damgası yenileniyor mu?
3. Modbus sorgusu/başarılı yanıt sayısı bağımsız olarak nasıl gözlenecek ve `on_value` sayısıyla karşılaştırılacak?
4. SNTP zamanı eşitlendikten sonra epoch alanı ile monoton `millis()` tabanlı zaman işareti nasıl ilişkilendirilecek? `millis()` monoton çalışma süresi işaretidir; tek başına duvar saati timestamp'i değildir.

## Sonraki adım

Önce gerçek 0 A testi yapılacak. Ardından gerekiyorsa Modbus katmanındaki başarılı yanıtı bağımsız gözlemleyecek tanılama eklenerek sorgu/yanıt ile `on_value` ilişkisi doğrulanacak. Bu kabulden önce `on_value` zamanı kesin Modbus yanıt zamanı sayılmayacak.

## Veri sınırı

Bu logda ADC örneklemesi, `window_start/window_end/window_center`, `time_delta_ms`, `adc_rms`, `zero_count`, `invalid_count` veya CSV kaydı yoktur. Bu alanların çalıştığı sonucuna varılamaz.
