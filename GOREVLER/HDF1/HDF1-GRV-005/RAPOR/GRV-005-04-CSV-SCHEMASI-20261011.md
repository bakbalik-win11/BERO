# GRV-005-04 — CSV şeması ve veri sözlüğü

- Tarih: 2026-10-11
- Durum: Şema önerisi ve alan sözlüğü oluşturuldu; kilitleme öncesi gözden geçirme.
- Amaç: ADC istatistiklerini, zaman ilişkisini, PZEM referansını ve deney bağlamını tek, tutarlı CSV sözleşmesinde toplamak.
- Satır mantığı: **Bir satır = bir kanalın bir ölçüm penceresi + o pencereye ilişkilendirilen PZEM referansı.**
- Kod durumu: CSV/firmware uygulaması henüz başlamadı.

## 1. Satır ve kimlik mantığı

Bir ölçüm döngüsünde CH0, CH1, CH2 ve BIAS için dört ayrı kanal penceresi oluşur; her kanal için ayrı CSV satırı yazılır. Bu dört satır aynı `measurement_id` değerini paylaşır; `channel_id` alanları farklıdır. `measurement_id` ölçüm döngüsünü tanımlar, tek bir kanal satırını değil.

Her satır, o ADC pencere merkezine zaman bakımından en yakın PZEM güncellemesini referans alır. PZEM alanları ve zaman farkı bu eşleşmeye aittir. Henüz kabul eşiği belirlenmediğinden yakınlık hakkında GOOD/POOR sınıfı üretilmez; `time_delta_ms` işaretli ham değer olarak tutulur. `pzem_update_millis` ESPHome `on_value` güncelleme işaretidir; bağımsız Modbus yanıt zamanı olduğu kanıtlanmış değildir.

## 2. CSV alan sırası

Önerilen başlık sırası:

1. Kimlik ve deney: `measurement_id, experiment_id, firmware_version, device_name, channel_id, load_label, notes`
2. Zaman: `window_start_millis, window_end_millis, window_center_millis, window_duration_ms, pzem_update_millis, time_delta_ms, window_center_epoch_s, pzem_timestamp`
3. Örnek kalitesi: `sample_count, invalid_count, zero_count`
4. ADC istatistikleri: `adc_mean, adc_std, adc_min, adc_max, adc_range, adc_median, adc_p05, adc_p25, adc_p75, adc_p95, adc_p95_minus_p05, adc_rms_raw, adc_rms_ac`
5. BIAS istatistikleri: `bias_mean, bias_std, bias_min, bias_max`
6. PZEM referansı: `pzem_voltage, pzem_current, pzem_power, pzem_pf, pzem_frequency, pzem_energy`

## 3. Veri sözlüğü

CSV sayısal değerlerinde ondalık ayırıcı nokta kullanılacak; alanlar virgülle ayrılacak. Zaman ve kalite alanlarında birim/sayı türü aşağıdaki tabloda belirtilmiştir. Bilinmeyen veya geçersiz değerler için sahte sıfır yazılmayacak; CSV uygulamasında boş alan kullanılacak. Metin alanlarında virgül, çift tırnak veya satır sonu varsa standart CSV quoting uygulanmalı.

| Alan | Veri tipi | Birim/biçim | Açıklama |
|---|---|---|---|
| `measurement_id` | string | ID | Aynı ölçüm döngüsündeki kanal satırlarında ortak, benzersiz kimlik. |
| `experiment_id` | string | etiket | Deney adı/kodu; ör. `TEST_LED_8W`. |
| `firmware_version` | string | sürüm etiketi | Çalışan firmware/yapılandırma sürümü; ör. `GRV005_V01`. |
| `device_name` | string | ad | ESPHome cihaz adı; bu projede `esp32d1`. |
| `channel_id` | string | `K1/K2/K3/BIAS` | Satırın ADC kanalı. Proje kodlamasında CH0/CH1/CH2 eşlemesiyle tutarlı olacak. |
| `load_label` | string | etiket | Deney yükü; ör. `LED_8W`, `FAN`, `VACUUM`, `PC_POWER`. Bilinmiyorsa boş. |
| `notes` | string | serbest metin | Durum notu; ör. `normal`, `startup`, `unstable_test`. |
| `window_start_millis` | uint32/uygun tamsayı | ms | ADC penceresinin ilk örnekleme denemesinin başlangıç monotonik işareti. |
| `window_end_millis` | uint32/uygun tamsayı | ms | Son örnekleme denemesinin bitiş monotonik işareti. |
| `window_center_millis` | uint32/uygun tamsayı | ms | Pencere başlangıcı ile bitişinin orta noktası; millis taşması güvenli hesaplanmalı. |
| `window_duration_ms` | uint32/uygun tamsayı | ms | Pencerenin geçen süresi. |
| `pzem_update_millis` | uint32/uygun tamsayı | ms | İlişkilendirilen PZEM `on_value` güncellemesinin monotonik işareti. |
| `time_delta_ms` | signed integer | ms | `pzem_update_millis - window_center_millis`; işaret korunur. Pozitif: PZEM işareti pencere merkezinden sonra. |
| `window_center_epoch_s` | integer | Unix epoch s | Pencere merkezinin duvar saati zamanı; SNTP geçersizse boş. |
| `pzem_timestamp` | integer | Unix epoch s | PZEM güncelleme işaretinin duvar saati zamanı; SNTP geçersizse boş. |
| `sample_count` | integer | örnek | Başarılı, geçerli ADC örneklerinin sayısı; hedef 1000. |
| `invalid_count` | integer | örnek | 1000 hedefli pencerede örnek üretilemeyen/okuma hatası görülen deneme sayısı. Yalnızca yazılım gerçekten hatayı algılayabiliyorsa artırılır. |
| `zero_count` | integer | örnek | Geçerli ham ADC kodu tam 0 olan örnek sayısı. |
| `adc_mean` | float | ADC count | Geçerli ham ADC kodlarının aritmetik ortalaması. |
| `adc_std` | float | ADC count | Örnek standart sapması; payda N−1. N<2 ise boş. |
| `adc_min` | integer | ADC count | Geçerli ham kodların minimumu. |
| `adc_max` | integer | ADC count | Geçerli ham kodların maksimumu. |
| `adc_range` | integer | ADC count | `adc_max - adc_min`. |
| `adc_median` | float | ADC count | Geçerli ham kodların medyanı. |
| `adc_p05` | float | ADC count | Doğrusal enterpolasyonla hesaplanan 5. yüzdelik. |
| `adc_p25` | float | ADC count | Doğrusal enterpolasyonla hesaplanan 25. yüzdelik. |
| `adc_p75` | float | ADC count | Doğrusal enterpolasyonla hesaplanan 75. yüzdelik. |
| `adc_p95` | float | ADC count | Doğrusal enterpolasyonla hesaplanan 95. yüzdelik. |
| `adc_p95_minus_p05` | float | ADC count | `adc_p95 - adc_p05`; klasik IQR değildir. |
| `adc_rms_raw` | float | ADC count | Ham ADC kodlarının sıfıra göre RMS'i; AC akım RMS'i değildir. |
| `adc_rms_ac` | float | ADC count | CH kanalında aynı ölçüm döngüsünün `bias_mean` değeri çıkarıldıktan sonraki RMS. BIAS geçersizse boş. |
| `bias_mean` | float | ADC count | BIAS kanalının geçerli örneklerinin ortalaması. BIAS satırında kendi kanal ortalaması; CH satırlarında aynı döngünün BIAS ortalaması. |
| `bias_std` | float | ADC count | BIAS kanalının örnek standart sapması (N−1). |
| `bias_min` | integer | ADC count | BIAS kanalının minimum ham kodu. |
| `bias_max` | integer | ADC count | BIAS kanalının maksimum ham kodu. |
| `pzem_voltage` | float | V | İlişkilendirilen PZEM gerilim değeri. |
| `pzem_current` | float | A | İlişkilendirilen PZEM akım değeri; hedef değişken olarak kullanılacaksa model girişlerinden çıkarılmalı. |
| `pzem_power` | float | W | İlişkilendirilen PZEM aktif güç değeri. |
| `pzem_pf` | float | boyutsuz | PZEM güç faktörü. |
| `pzem_frequency` | float | Hz | PZEM frekans değeri. |
| `pzem_energy` | float | kWh | PZEM enerji değeri; kullanılan ESPHome bileşeninin birimi doğrulanarak dışa aktarılmalı. |

## 4. BIAS istatistikleri ve kanal satırları

Her ölçüm döngüsünde BIAS kanalının kendi satırı bulunur. Ayrıca `bias_mean`, `bias_std`, `bias_min`, `bias_max` alanları CH0/CH1/CH2 satırlarına aynı döngünün bias özetini iliştirmek için tekrarlanır. Bu tekrar, her kanal satırının tek başına yorumlanabilmesini sağlar. BIAS satırında bu alanlar BIAS kanalının kendi istatistiklerini ifade eder.

CH/BIAS örnekleri ardışık okunduğundan fiziksel olarak eşzamanlı değildir. Bu ilişkilendirme, aynı ölçüm döngüsünün BIAS penceresini referans alır; bu sınır veri sözlüğünde korunur.

## 5. PZEM alanları ve model sızıntısı

PZEM alanları her satırda bulunur. Modelleme aşamasında hedef `pzem_current` ise `pzem_current` model girdilerinden çıkarılmalıdır; aynı şekilde hedefle doğrudan türetilmiş veya hedefi açığa çıkaran alanların özellik setine sızması önlenmelidir. CSV'de alanın bulunması, tüm alanların modele girdi yapılacağı anlamına gelmez.

## 6. Eksik/kalitesiz kayıtlar

- Pencere atılmaz. Örneğin `sample_count=997`, `invalid_count=3` satırı kaydedilir.
- İstatistikler yalnız geçerli örneklerden hesaplanır.
- Matematiksel olarak hesaplanamayan alanlar boş bırakılır, sıfırla doldurulmaz.
- SNTP senkronizasyonu yoksa epoch alanları boş kalabilir; monotonik alanlar yine kaydedilir.
- Henüz `abs_time_delta_ms` veya `alignment_quality` alanı üretilmez. Python gerek duyarsa bunları sonradan türetebilir.

## 7. Açık uygulama notları

1. `channel_id` değerlerinin K1/K2/K3/BIAS mı yoksa CH0/CH1/CH2/BIAS mı olacağı mevcut kablo/etiket eşlemesiyle uygulama öncesinde tekleştirilmeli; iki adlandırma karışık kullanılmamalı.
2. `firmware_version` alanı derleme/konfigürasyon kimliğiyle nasıl üretilecekse uygulama öncesinde belirlenmeli; örnek etiket doğrulanmış sürüm gibi kullanılmamalı.
3. `pzem_energy` birimi ve PZEM sensör güncellemesindeki alanların tazeliği gerçek ESPHome bileşeniyle doğrulanmalı.
4. `pzem_timestamp` ve `window_center_epoch_s` saniye çözünürlüğündedir; yüksek hassasiyetli eşleşme `time_delta_ms` ile monotonik alanda yapılır.
5. `measurement_id` üretimi cihaz yeniden başladığında çakışmayacak biçimde tasarlanmalı; basit yeniden başlayan sayaç tek başına yeterli değildir.

## 8. Sonraki adım

Bu şema ve veri sözlüğü kullanıcı tarafından gözden geçirilip kilitlendikten sonra GRV-005-05 altında uygulama tasarımı/kodlama planlanabilir. Kod ayrı yeni sürüm olarak hazırlanır; kullanıcı başarılı derlemeyi doğrulamadan KOD klasörüne taşınmaz.

## Geçmişi koruma

GRV-005-01/02/03 kararları, önceki öneriler, GRV-002, GRV-004, ALT09 ve ALT10 değiştirilmez. Bu belge yeni şema kaydıdır.
