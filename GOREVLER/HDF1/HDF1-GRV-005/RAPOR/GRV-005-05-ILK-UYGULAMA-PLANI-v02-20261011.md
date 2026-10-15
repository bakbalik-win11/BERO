# GRV-005-05 — İlk uygulama planı v02: istatistik doğrulama önceliği

- Tarih: 2026-10-11
- Durum: Doğrulama öncelikleri Copilot değerlendirmesiyle genişletildi; firmware kodu henüz yazılmadı.
- Önceki plan: [v01 ilk uygulama planı](GRV-005-05-ILK-UYGULAMA-PLANI-20261011.md) tarihsel kayıt olarak korunur.
- Ön koşul: [GRV-005-04 CSV veri sözleşmesi v03](GRV-005-04-CSV-SCHEMASI-v03-20261011.md).
- Cihaz: `esp32d1`; cihaz adı değiştirilmeyecek.

## 1. İlk başarı ölçütü

İlk firmware sürümünün amacı henüz doğru akım ölçmek veya akım kalibrasyonunu tamamlamak değildir. İlk amaç, **1000 ADC örneğinden tanımlandığı şekilde doğru istatistikler üretildiğini kanıtlamaktır.**

Başarılı derleme tek başına başarı sayılmaz. İstatistikler kontrollü örneklerle bağımsız olarak hesaplanmalı ve firmware çıktısıyla karşılaştırılmalıdır.

## 2. İlk çıktıda kontrol edilecek alanlar

Her kanal için ilk tanılama çıktısında en az şu alanlar incelenir:

- `sample_count`
- `invalid_count`
- `zero_count`
- `adc_mean`
- `adc_std`
- `adc_rms_raw`
- `adc_rms_ac`

Beklenen değerler ölçüm öncesinde otomatik olarak varsayılmaz. Örneğin `sample_count=1000` hedef örnek sayısıdır; `invalid_count=0` ve `zero_count=0` ise ancak gerçek ölçüm çıktısında görülürse raporlanır. ADC API'si hata durumunu bildirmiyorsa `invalid_count` için yapay bir sıfır veya hata iddiası üretilmez.

## 3. Önce kontrollü matematik, sonra yük testi

### A. Kontrollü örneklerle doğrulama

1. İstatistik fonksiyonları CSV ve donanım okuma katmanından bağımsız test edilebilir şekilde tutulur.
2. Önceden bilinen kısa örnek dizileri üzerinde ortalama, N−1 paydalı örnek standart sapması, ham RMS ve bias çıkarılmış RMS bağımsız hesaplanır.
3. Firmware hesaplamaları beklenen sonuçlarla karşılaştırılır; yuvarlama farkları açıkça belirtilir.
4. `zero_count` yalnızca geçerli ham kodu 0 olan örneklerden hesaplanır.

### B. Gerçek ADC ile tekrarlı ölçüm

Kontrollü matematik testi geçtikten sonra sabit bir yük altında ardışık ölçümler alınır. İlk fiziksel testin amacı amper cinsinden doğruluk iddiası değil; istatistiklerin tekrarlanabilirliğini gözlemlemektir.

Aynı yükte şu alanların kayıtları karşılaştırılır:

- `adc_std`
- `adc_rms_ac`
- ayrıca yorum için `sample_count`, `zero_count`, `invalid_count` ve `bias_mean`

Değerlerin ne kadar değişmesine izin verileceğine dair sayısal tolerans, veri görülmeden uydurulmaz. İlk kayıtlar değişkenliği anlamak ve sonraki kabul ölçütünü gerekçelendirmek için kullanılır.

## 4. Üçlü çapraz gözlem: ADC std, ADC AC RMS, PZEM current

Aynı yük ve zaman pencerelerinde aşağıdaki seriler yan yana incelenir:

- `adc_std`
- `adc_rms_ac`
- `pzem_current`

Bu aşamada model kurulmaz ve bu üç değerin matematiksel olarak eşit olması beklenmez. `adc_std`, kanal örneklerinin kendi ortalaması çevresindeki dağılımını ölçer; `adc_rms_ac` ise sözleşme gereği ayrı BIAS kanalının `bias_mean` değerine göre hesaplanır. Bu nedenle aralarında genel durumda bire bir eşitlik zorunlu değildir.

Farklı yük seviyelerinde `pzem_current` yükselirken `adc_rms_ac` değerinin düzenli artıp artmadığı gözlemlenebilir. Böyle bir eğilim yararlı bir işaret olur; tek başına kalibrasyonu, doğruluğu veya nedenselliği kanıtlamaz. PZEM güncelleme işareti de gerçek Modbus yanıt zamanıyla bire bir eşleştiği kanıtlanmış bir zaman damgası değildir.

Gerçek 0 A noktası bu prototipte beklenmez; cihaz kendi tüketimini ölçtüğü için mevcut yaklaşık 0.028 A taban değeri fiziksel sıfır kabul edilmeyecektir.

## 5. Ölçüm ve modelleme aşamalarının ayrımı

1. **Aşama 1:** İstatistiklerin matematiksel doğruluğu kontrollü örneklerle doğrulanır.
2. **Aşama 2:** Sabit yük altında istatistiklerin tekrarlanabilirliği incelenir.
3. **Aşama 3:** Farklı yüklerde `adc_rms_ac` ve PZEM referans akımının birlikte değişimi gözlenir.
4. **Daha sonraki çalışma:** Yeterli ve doğrulanmış veri toplandıktan sonra lineer/polinom regresyon, Random Forest veya XGBoost karşılaştırılabilir. Model seçimi firmware özellik üretiminin doğruluğundan ayrı tutulur; hedef `pzem_current` giriş özelliklerine sızdırılmaz.

## 6. Kimlik, hata modeli ve kayıt disiplini

- Kimlik biçimi: `session_id + epoch_s + sequence_no`; SNTP yokken veya yeniden başlatmada da çakışmayı önleyen yöntem uygulamada doğrulanmalıdır.
- `zero_count` ve `invalid_count` farklı anlamlara sahiptir; geçerli sıfır okumaları hata sayılmaz.
- Ham örnekler kalıcı CSV'ye dökülmeden RAM içinde istatistik için kullanılabilir; ilk adım tek satırlık diagnostic çıktıdır.
- İlk testte her alanın üretilmiş olması değil, üretilen alanların sözleşmeye uygun olması ve hesapların doğrulanması esastır.
- Mevcut ALT09/ALT10 ve diğer görev dosyaları değiştirilmez. Yeni firmware ayrı sürüm olarak hazırlanır; kullanıcı başarılı derlemeyi doğrulamadan doğrulanmış `KOD/` alanına taşınmaz.

## 7. İlk aşamanın tamamlanma ölçütü

İlk istatistik doğrulama aşaması ancak:
- kontrollü diziler için bağımsız beklenen sonuçlar ile firmware hesapları uyuştuğunda,
- tek satırlık tanılama çıktısı alan anlamları ve boş/geçersiz değer kurallarına uyduğunda,
- aynı yük altındaki tekrarlı ölçümlerin logları incelendiğinde,
- derleme, yükleme ve ölçüm kanıtları ayrı ayrı kaydedildiğinde

tamamlandı sayılır. Yalnızca derlenmiş olması veya ADC RMS'in akımla artıyor görünmesi yeterli değildir.

Bu belge plan ve doğrulama ölçütüdür; kodun yazıldığı, derlendiği veya testlerin geçtiği anlamına gelmez.
