# GRV-005-05 — ESP32 özellik üretimi ve tek satır doğrulaması

- Tarih: 2026-10-11
- Durum: Kapsam ve ilk doğrulama adımları tanımlandı; firmware kodu henüz yazılmadı.
- Ön koşul: [GRV-005-04 CSV şeması v03](GRV-005-04-CSV-SCHEMASI-v03-20261011.md).
- Cihaz: `esp32d1`; cihaz adı değiştirilmez.
- Geçmişi koruma: ALT09, ALT10, GRV-002 ve önceki GRV-005 rapor/kod sürümleri değiştirilmez.

## 1. Amaç

1000 örneklik ADC penceresi için özelliklerin sözleşmeye uygun hesaplandığını ve beklenen sınırlar içinde olduğunu, CSV üretimine geçmeden önce doğrulamak. İlk aşama tam veri toplama/kalıcı CSV kaydı değil; kontrollü hesaplama ve tek satırlık çıktı doğrulamasıdır.

## 2. İlk aşamanın dar kapsamı

1. Her hedef kanal için 1000 örnekleme denemesi yürütmek.
2. Geçerli örneklerden aşağıdaki temel özellikleri hesaplamak:
   - `sample_count`
   - `invalid_count`
   - `zero_count`
   - `adc_mean`
   - `adc_std`
   - `adc_rms_raw`
   - `adc_rms_ac`
3. Test/diagnostic çıktısında tek kanal için tek özet satırı üretmek; bu aşamada CSV dosyası üretimini başlatmamak.
4. Çıktıyı CSV yazımına geçmeden önce sözleşme ve matematiksel kontrollerden geçirmek.

Bu ilk liste temel doğrulama kapsamıdır. GRV-005-04'teki median, percentiles, min/max/range ve zaman/PZEM alanları, ilk istatistik hesaplaması güvenilir olduktan sonra aynı görev içinde aşamalı eklenebilir; doğrulanmamış alanlar başarılıymış gibi raporlanmaz.

## 3. Kimlik üretimi

Önerilen kimlik yapısı:

`measurement_id = session_id + epoch_s + sequence_no`

- `session_id` her cihaz açılış/ölçüm oturumu için benzersiz bileşendir.
- `epoch_s` geçerli SNTP varsa pencere merkezine ait epoch saniyesidir.
- `sequence_no` aynı saniyedeki kayıtları ayırır.
- SNTP yoksa kimlik yine üretilebilmelidir; bu durumda oturum bileşeni ve monotonik/sıralı bileşen çakışmayı önlemelidir.
- Yalnızca yeniden başlayan bir sayaç veya yalnızca epoch saniyesi yeterli kabul edilmez.
- ESP32 üzerinde gerçekten çakışmasız üretim yöntemi kodlamadan önce seçilecek ve test edilecektir; bu belge belirli bir rastgelelik/kalıcılık API'sinin kullanılacağını varsaymaz.

## 4. ADC hata ve sıfır modeli

- `zero_count`: başarıyla alınmış, geçerli ham ADC kodu tam 0 olan örnekler.
- `invalid_count`: yalnızca ADC okuma API'si başarısız/sonuçsuz okumayı gerçekten bildirebiliyorsa artırılır.
- Sürücü hata durumunu bildirmiyorsa firmware başarısız okuma tespit ettiğini iddia etmez. `zero_count` ile `invalid_count` birbirinin yerine kullanılamaz.
- İstenen 1000 deneme için `sample_count + invalid_count = 1000` eşitliği, yalnızca tüm denemelerin durumunun API tarafından güvenilir biçimde sınıflandırılabildiği durumda doğrulanabilir.
- Gerçek 0 A testi bu prototip için beklenmez; sistemin kendi tüketimi nedeniyle 0.028 A mevcut pratik taban gözlemidir, fiziksel sıfır değildir.

## 5. Matematiksel kontroller

- `sample_count` 0 ise örnek tabanlı istatistikler boş/hesaplanamaz kalır; sahte sıfır üretilmez.
- `adc_std` örnek standart sapmasıdır (N−1); N<2 ise boş.
- `adc_rms_raw = sqrt(sum(x²)/N)` ve ham ADC kodu birimindedir.
- `adc_rms_ac = sqrt(sum((x - bias_mean)²)/N)`; BIAS geçerli değilse boş. Bu değer ADC count birimindedir, amper değildir.
- `zero_count <= sample_count` olmalıdır.
- Min/max, ortalama ve RMS gibi değerler ham örneklerle bağımsız hesaplama/örnek veri üzerinden karşılaştırılmalıdır.

## 6. Doğrulama sırası

1. Önce ADC API'sinin hata bildirimi ve mevcut ESPHome/Arduino uygulamasındaki gerçek okuma türü incelenir.
2. İstatistik hesaplamaları ayrı bir fonksiyon/katmanda tutulur; CSV yazımıyla iç içe geçirilmez.
3. Kontrollü örnek dizileriyle beklenen ortalama, örnek standart sapması, ham RMS, bias çıkarılmış RMS ve sıfır sayısı kontrol edilir.
4. Tek satırlık diagnostic çıktı incelenir.
5. Ancak temel hesaplamalar ve veri sözleşmesi kontrolleri geçerse tam alan seti ve CSV yazımı için bir sonraki uygulama adımına geçilir.

## 7. Kod ve doğrulama disiplini

- İlk firmware dosyası yeni ve sürümlü dosya olarak hazırlanır; mevcut YAML dosyalarının üzerine yazılmaz.
- Kullanıcının başarılı derleme onayı olmadan kod `KOD/` klasörüne doğrulanmış kod olarak taşınmaz.
- Derleme, cihaza yükleme ve gerçek ölçüm sonuçları ayrı doğrulama seviyeleri olarak raporlanır.
- Bir testin sonucu logda görünmüyorsa tamamlandı sayılmaz.

## 8. Veri bilimi kapsam sınırı

Lineer/polinom regresyon, Random Forest ve XGBoost ile akım/güç tahmini bu alt görevin ilk firmware doğrulama hedefi değildir. Önce ölçüm özelliklerinin doğru ve izlenebilir biçimde üretilmesi gerekir. Sonraki model deneylerinde hedef değişkenin kendisi (`pzem_current` gibi) giriş özelliklerine sızdırılmaz.

## 9. Kapanış ölçütü

GRV-005-05'in ilk aşaması ancak temel istatistiklerin kontrollü testlerle doğrulanması, tek satır çıktının şemayla uyumunun incelenmesi ve kullanıcı tarafından derleme/test seviyesinin teyit edilmesi sonrasında tamamlanmış sayılır. Bu kayıt plan/kapsam belgesidir; kodun yazıldığı veya testlerin geçtiği anlamına gelmez.
