# GRV-005-02 — ADC özellik tanımları, birleştirilmiş öneri v02

- Tarih: 2026-10-11
- Durum: Copilot değerlendirmesiyle birleştirilmiş teknik öneri; henüz nihai kilit değil.
- Amaç: İstatistiksel özellikleri fiziksel anlamlardan ayırarak ham ADC pencerelerinden tekrar üretilebilir veri üretmek.
- Kanallar: CH0, CH1, CH2 ve BIAS.
- Örnek hedefi: Kanal başına 1000 okuma denemesi.
- Koruma: Önceki v01 önerisi ve önceki görev/deney kayıtları silinmez veya üzerine yazılmaz.

## 1. Temel ilke

Ölçüm istatistiği ile fiziksel anlam ayrı tutulur. ADC kodundan hesaplanan özellikler kendiliğinden amper veya gerçek AC akım RMS'i değildir. Akıma dönüşüm, analog ön uç ölçeği ve kalibrasyon doğrulamasından sonra ayrı katmanda yapılır.

## 2. Kanal başına özellik seti

Her CH0, CH1, CH2 ve BIAS penceresi için aşağıdaki alanlar önerilir:

- `sample_count`: Başarıyla alınmış ve istatistiklere dahil edilebilen geçerli ADC örneği sayısı. Hedef 1000; örneğin 996, eksik pencere demektir.
- `invalid_count`: 1000 hedeflik pencere içindeki başarısız/eksik ADC okumalarının sayısı. SPI/okuma API'si hata, timeout veya kanal okunamaması gibi durumlar bu alana girer; yalnızca kodun 0 olması okuma hatası sayılmaz.
- `zero_count`: Geçerli ham ADC kodu tam olarak 0 olan örnek sayısı. Bias çıkarılmış değerin sıfıra yakınlığı bu sayaç değildir.
- `adc_mean`: Geçerli ham kodların aritmetik ortalaması; birim ADC kodu.
- `adc_std`: Örnek standart sapması; payda (N-1). Birim ADC kodu. (N<2) ise tanımsız/boş.
- `adc_median`: Geçerli ham kodların medyanı.
- `adc_min`, `adc_max`: Geçerli ham kodların en küçük ve en büyük değeri.
- `adc_range`: `adc_max - adc_min`.
- `adc_p05`, `adc_p95`: Ham kod dağılımının yüzde 5 ve yüzde 95 yüzdelikleri. Hesap algoritması/enterpolasyon kuralı uygulama öncesi sabitlenecek.
- `adc_iqr`: Copilot önerisindeki adlandırma korunarak burada (p95-p05) anlamında kullanılmak isteniyor. **Dikkat:** İstatistikte IQR çoğunlukla (p75-p25) anlamına gelir; bu nedenle adlandırma çakışmasını önlemek için önerilen alan adı `adc_p95_p05_span) veya `adc_p95_minus_p05) olmalıdır. Nihai şemada gerçek IQR istenirse ayrıca p25/p75 gerekir.
- `adc_rms_raw`: Ham kodların sıfıra göre RMS'i, (sqrt{rac{1}{N}sum x_i^2}). Birim ADC kodu; AC akım RMS'i değildir.
- `adc_rms_ac`: Bias çıkarılmış kodların RMS'i, (sqrt{rac{1}{N}sum (x_i-bias_mean)^2}). Birim ADC kodu; doğrudan amper değildir.

## 3. BIAS ve AC RMS tanımı

- `bias_mean`, BIAS kanalının kendi 1000 örnek hedefli penceresindeki geçerli örneklerin aritmetik ortalamasıdır.
- `bias_mean` RMS değildir, akım değildir, AC genliği değildir; bias kanalının o pencere boyunca gözlenen ADC merkez/offset değeridir.
- CH kanalındaki `adc_rms_ac), bu öneri sürümünde BIAS kanalının aynı ölçüm döngüsündeki `bias_mean` değeri çıkarılarak hesaplanır.
- BIAS penceresi kullanılamaz veya yetersiz kalırsa `adc_rms_ac` geçersiz/boş işaretlenir; sahte sıfır yazılmaz.
- CH ve BIAS örnekleri ADC üzerinden ardışık okunduğu için fiziksel olarak eşzamanlı değildir. Bu yaklaşım ortak bias kaynağını temsil ettiği varsayımına dayanır ve deneyle doğrulanmalıdır.
- Gelecekte CH penceresinin kendi ortalamasını DC merkez olarak kullanma seçeneği ayrı bir deney/özellik olarak incelenebilir; bu öneride BIAS kanalı ortalamasının yerini sessizce almaz.

## 4. Örnek sayısı ve eksik pencereler

- Her kanal için hedef 1000 okuma denemesidir.
- `sample_count` geçerli örnek sayısını, `invalid_count` başarısız okumaları ifade eder. Normal durumda `sample_count + invalid_count = 1000).
- Örneğin `sample_count=996`, `invalid_count=4` ise pencere atılmaz; ölçülebilen özellikler ve kalite alanları kaydedilir. Python sonradan `sample_count < 1000` kayıtlarını filtreleyebilir.
- Özellikler yalnızca geçerli örneklerden hesaplanır. RMS/standart sapma için geçerli örnek sayısı matematiksel olarak yetersizse ilgili alan boş/geçersiz olur.
- `zero_count) yalnızca geçerli örneklerde ham kodu tam 0 olanları sayar; `invalid_count) ile birbirinden bağımsızdır.

## 5. Alan adlarıyla ilgili açık karar

Copilot notundaki `adc_iqr = p95 - p05` ifadesi hesap olarak bir yayılım aralığıdır ancak geleneksel IQR adlandırmasıyla uyuşmaz. Bu nedenle öneri:
- `adc_p95_minus_p05 = adc_p95 - adc_p05`
- Gerçek interquartile range istenirse daha sonra `adc_iqr = adc_p75 - adc_p25` alanı ayrı eklenir.

Bu adlandırma, Python tarafında alanın yanlış yorumlanmasını önler.

## 6. Henüz sabitlenecek küçük uygulama ayrıntıları

1. Yüzdeliklerin kesin enterpolasyon yöntemi.
2. ADC sürücüsü/ESPHome bileşeninde hata durumlarının gerçekte hangi biçimde yakalanabildiği. Bileşen başarısız okumayı ayırt edemiyorsa hata sayacı varmış gibi davranılmayacak.
3. `adc_rms_ac` için BIAS penceresinin hangi ölçüm döngüsüyle eşleştirileceği, GRV-005-03/04 zaman ve kayıt sözleşmesinde netleştirilecek.

## 7. Sonraki adım

Bu öneri alan adları, matematik ve kalite davranışı açısından gözden geçirilir. Kilitlenince GRV-005-03'te PZEM/ADC zaman hizalaması, ardından GRV-005-04'te CSV satır yapısı tanımlanır. Kod, bu tanımlar ve veri şeması netleşmeden hazırlanıp KOD klasörüne taşınmaz.

## Geçmişi koruma

GRV-002, GRV-004, ALT09, ALT10, GRV-005-01 ve GRV-005-02 v01 öneri dosyası değiştirilmez. Bu belge yeni birleştirilmiş öneri sürümüdür.
