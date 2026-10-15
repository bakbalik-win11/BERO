# GRV-005-02 — ADC özellik tanımları, öneri v01

- Tarih: 2026-10-11
- Durum: Teknik öneri; kullanıcı onayıyla kilitlenecek.
- Amaç: Kanal başına 1000 örnekten üretilecek istatistikleri açık, tekrar üretilebilir ve Python tarafında yorumlanabilir şekilde tanımlamak.
- Kanallar: CH0, CH1, CH2 ve BIAS.
- Önemli sınır: Bu belge karar önerisidir; henüz YAML uygulaması veya donanım doğrulaması değildir.

## 1. Örnek penceresi ve kalite

Her kanal için hedef 1000 ADC kodudur. Ham örnekler yalnızca RAM'de geçici tutulur. Her pencere için:
- `sample_count`: pencerede alınan toplam örnek denemesi.
- `valid_count`: istatistiklere dahil edilen geçerli ADC kodu sayısı.
- `invalid_count`: eksik okuma veya ADC'nin geçerli kod aralığı dışında sonuç verdiği deneme sayısı.
- `zero_count`: ham ADC kodu tam olarak 0 olan geçerli örnek sayısı. Bias çıkarıldıktan sonraki sıfıra yakın değer bu sayaç değildir.
- İstatistikler yalnız geçerli örneklerden hesaplanır; `valid_count < 1000` ise pencere kalite açısından eksik olarak işaretlenir, eldeki istatistikler 1000 örnekle tamamlanmış gibi gösterilmez.

MCP320x 12 bit için geçerli ham kod aralığı 0–4095'tir. Kod uygulamasında okuma API'si hata durumunu ayrı sunuyorsa bu hata da `invalid_count` içine alınır; sırf kod 0 döndü diye otomatik olarak okuma hatası kabul edilmez.

## 2. Temel istatistikler

Her kanalın ham ADC kodları (x_i), geçerli örnek sayısı (N) olsun.

- `adc_mean`: (rac{1}{N}sum x_i). Birim: ADC kodu.
- `adc_std`: popülasyon standart sapması, (sqrt{rac{1}{N}sum (x_i-ar{x})^2}). Birim: ADC kodu. Burada pencere içindeki alınmış örneklerin tamamı tanımlanmak istendiğinden payda (N) kullanılır.
- `adc_median`: ham kodların medyanı. Birim: ADC kodu.
- `adc_p05`, `adc_p25`, `adc_p75`, `adc_p95`: ham kod dağılımının yüzde 5, 25, 75 ve 95 yüzdelikleri. Yüzdelik algoritması/enterpolasyon kuralı kod uygulaması başlamadan veri sözlüğünde sabitlenir. Bu değerler dağılım ve aykırı örnek davranışını izlemek içindir; kendi başlarına filtreleme veya akım tahmini değildir.

## 3. RMS alanlarının ayrılması

Tek bir belirsiz `adc_rms` alanı kullanmak yerine iki ayrı alan önerilir:

- `adc_raw_rms`: (sqrt{rac{1}{N}sum x_i^2}). Birim: ADC kodu. Bias çevresindeki AC sinyalinin RMS'i veya akım değeri olarak yorumlanmaz.
- `adc_ac_rms_counts`: (sqrt{rac{1}{N}sum (x_i-b)^2}). Birim: ADC kodu. (b), aynı ölçüm penceresindeki BIAS kanalının geçerli örnek ortalamasıdır.

`adc_ac_rms_counts` için BIAS kanalının 1000 örneği eksik/kalitesizse sonuç güvenilir kabul edilmez; alan geçersiz/boş olarak işaretlenir. CH kanalları ve BIAS MCP320x üzerinde ardışık okunduğundan örnekler fiziksel olarak eşzamanlı değildir; bu yaklaşım ortak bias kaynağı varsayımına dayanır ve donanım ölçümüyle doğrulanmalıdır.

ADC kodundan volta ve ardından ampere dönüşüm bu özellik tanımından ayrı tutulur. Akım dönüşümü için referans gerilimi, analog devre ölçeği ve sensör kalibrasyonu gerekir. Bu aşamada `adc_ac_rms_counts` akım ölçümü diye sunulmaz.

## 4. BIAS kanalı

BIAS kanalı da kendi `adc_mean`, `adc_std`, `adc_median`, yüzdelik ve kalite sayımlarına sahip olur. `adc_ac_rms_counts` hesabında kullanılan (b), BIAS kanalının aynı pencere içindeki geçerli örnek ortalamasıdır. BIAS kanalının istatistikleri ayrıca korunur; referans kalitesi zayıfsa ona bağlı AC RMS geçersiz işaretlenir.

## 5. Karar olarak kilitlenmeden önce kalan tek noktalar

1. Yüzdelik hesabı için kesin algoritma (ör. doğrusal enterpolasyon kuralı).
2. Eksik pencerede özelliklerin tutulması: öneri, özellikleri hesaplanabiliyorsa saklamak ama `valid_count` ve kalite bayrağıyla eksik olduğunu açıkça belirtmek.
3. ESPHome/ADC bileşeninin hata durumunu nasıl raporladığının kodlamadan önce doğrulanması.

## 6. Sonraki sıra

1. Bu tanımları gözden geçirip kullanıcı onayıyla kilitle.
2. GRV-005-03: PZEM ve ADC pencere zamanlarının aynı monoton saat tabanında eşleştirilmesi ve `time_delta_ms` işaret yönünün tanımlanması.
3. GRV-005-04: birleşik ölçüm döngüsü için CSV satır yapısı ve veri sözlüğü.
4. Ancak bundan sonra uygulama YAML'ı yeni sürüm/dosya olarak oluşturulur; derleme onayı gelmeden KOD klasörüne taşınmaz.

## Geçmişi koruma

GRV-002, GRV-004, ALT09, ALT10 ve GRV-005-01 dosyaları değiştirilmez. Bu belge yeni öneri kaydıdır.
