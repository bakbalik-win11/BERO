# GRV-005-11 v01 — CH0 + BIAS 1000 örnek penceresi

## Hedef
GPIO33 / CH0-1T ve GPIO32 / BIAS kanallarından ayrı ayrı 1000 ham ADC callback örneği toplamak; `bias_mean` ve BIAS merkezli `adc_rms_ac` üretmek.

## Donanım
- ESP32-D1
- CH0 / 1T: GPIO33
- BIAS: GPIO32
- ESPHome ADC, `raw: true`, `attenuation: 12db`
- İki kanal için `update_interval: 10ms`

## Hesaplar
- `adc_mean`: CH0 ortalaması.
- `adc_std`: CH0 örnek standart sapması (N−1).
- `adc_rms_raw`: CH0 ham ADC RMS.
- `bias_mean`: BIAS kanalının 1000 örneğinin ortalaması.
- `adc_rms_ac`: `sqrt(mean((CH0 - bias_mean)^2))). Kod bunu toplam ve kareler toplamıyla hesaplar; her örneği bellekte tutmaz.
- `zero_count`, `bias_zero_count`: geçerli ve tam sıfır olan örneklerin sayısı.
- `invalid_count=NOT_TRACKED`: ESPHome ADC callback'leri sürücü seviyesindeki tüm okuma girişimlerini/hatalarını görünür kılmaz.

## Pencere ve eşzamanlılık sınırı
Her iki sensör kendi callback'inde 1000 geçerli örneğe ulaşana kadar veri biriktirir. Sonuç, her iki kanal da 1000'e ulaştığında bir kez loglanır. Başlangıç zamanı ilk kanaldan gelen ilk geçerli callback'te başlar; süre, ikinci kanal 1000'e ulaştığında biter.

Bu, aynı genel toplama penceresinde iki kanaldan 1000'er örnek toplandığını doğrular; iki ADC dönüşümünün donanım seviyesinde aynı anda gerçekleştiğini veya örneklerin birebir eşzamanlı eşleştiğini **garanti etmez**. Bu ilk BIAS/RMS doğrulama sürümünün sınırıdır.

## Güvenli kullanım
- Kod, kullanıcının mevcut cihaz yapılandırmasının tamamının yerine geçecek bağımsız test YAML'ıdır. `esp32d1` adını korur; canlı cihazdaki aynı adlı yapılandırmanın üzerine yükleme yapmadan önce mevcut yapılandırmanın yedeğini sakla.
- Önce derle; derleme başarılıysa yükleme kararını ayrıca ver.
- Derleme/cihaz testi henüz doğrulanmadı.
- Bu kod yeni pencereyi bir kez raporlar; sürekli pencere sıfırlaması/sonraki pencereler bu ilk testte tasarlanmamıştır.
- Kanal pinleri fiziksel bağlantı planıyla doğrulanmalıdır; GPIO32 BIAS varsayımı testten önce kontrol edilmelidir.

## Beklenen log alanları
`channel=CH0-1T bias_channel=BIAS sample_count=1000 bias_sample_count=1000 window_duration_ms=... invalid_count=NOT_TRACKED zero_count=... bias_zero_count=... adc_mean=... adc_std=... adc_rms_raw=... bias_mean=... adc_rms_ac=...`

## Kabul ölçütleri
1. YAML derlenmeli.
2. Cihaz logunda tek sonuç satırı görünmeli.
3. `sample_count=1000` ve `bias_sample_count=1000` olmalı.
4. `window_duration_ms` sıfırdan büyük olmalı.
5. `bias_mean` ve `adc_rms_ac` sonlu sayılar olmalı.
6. Sonuç yalnızca ilk CH0+BIAS toplama testini PASS yapar; 4 kanal, PZEM eşlemesi ve CSV kapsam dışıdır.
