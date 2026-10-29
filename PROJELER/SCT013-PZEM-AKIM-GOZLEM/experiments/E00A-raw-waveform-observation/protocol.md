# E00A — Protokol: ham sinyal kaydı ve temel istatistikler

## Ön koşullar
- İlk uygulama adayı envanterdeki klasik ESP32-WROOM-32D kartı ve GPIO34 (ADC1_CH6, giriş-only) olarak belirlenmiştir. Bu henüz fiziksel doğrulama değildir: kullanılacak geliştirme kartının üzerindeki model/işaret ve pinout, kablo bağlamadan önce eşleştirilmelidir. Kart farklıysa GPIO34 varsayılmayacak; uygun ADC1 GPIO yeniden seçilip buraya ve `experiment.yaml` dosyasına yazılacaktır.
- Ölçüm girişine şebeke gerilimi bağlanmaz. Bias-only ve SCT yüksüz adımlarında fiziksel bağlantı güvenli biçimde kontrol edilir.
- Bias orta noktası için [ADR-007](../../docs/decisions/ADR-007-bias-midpoint-capacitor.md) kapsamında mevcut 100 nF'ye paralel 10 µF eklenmesi planlanmıştır. Bu değişiklik E00A'nın ilk SCT bağlantılı koşulundan önce uygulanmalı; fiziksel olarak yapılana kadar tamamlandı sayılmaz. Gerçek kurulum, kayda başlamadan kontrol edilip LOG'a yazılır. Üç koşul aynı bias düzeniyle kaydedilmelidir.
- Bu ilk adımda bir ESP32 ve 2 kS/s hedefi yeterlidir. 2 kS/s doğrulanmış sonuç değil, mevcut başlangıç değeridir.

## Ham kayıt biçimi ve dosya yolu
- Her koşul için yerel CSV dosyası: `data/raw/E00A/bias_only.csv`, `data/raw/E00A/sct_yuksuz.csv`, `data/raw/E00A/100w_akkor.csv`. Ham dosyalar varsayılan olarak Git'e eklenmez.
- CSV sütunları: `sample_index,adc_raw`; her satır bir ham ADC örneğidir. `sample_index` sıfırdan başlar, `adc_raw` ise dönüştürülmemiş ADC ham sayısıdır. Ham dosyaya amper veya mV değeri yazılmaz.
- Her koşulun hedef hızı, gerçek geçen süresi, örnek sayısı ve firmware sürümü/commit'i `results.md` LOG alanına yazılır. Yaklaşık gerçekleşen hız `sample_count / elapsed_seconds` olarak hesaplanır; hedef hızla aynı olduğu varsayılmaz.
- İlk uygulamada her örneğe zaman damgası eklemek zorunlu değildir; örnek başına zaman damgasının örnekleme yükü yaratabileceği için toplam edinim süresi ölçülür. Bu nedenle bu format tek tek örnek aralıklarının kusursuzluğunu kanıtlamaz.

## Her adım için zorunlu kayıt: HEDEF → LOG → SONUÇ
- **HEDEF:** Adımın cevaplayacağı soru ve ölçülebilir kabul koşulu.
- **LOG:** Gerçek bağlantı/koşul, hedef hız, kayıt başlangıç-bitiş bilgisi veya geçen süre, örnek sayısı, ham dosya yolu ve hesaplanan istatistikler. Yapılmayan işlem de açıkça yazılır.
- **SONUÇ:** Yalnız kaydın desteklediği yorum, belirsizlikler ve bir sonraki adıma geçme gerekçesi. Ölçüm yoksa “sonuç yok/ölçülmedi” yazılır.

## Adımlar
1. **Bias-only:** SCT jack'i bağlı değilken ham ADC örneklerini yaklaşık 1 saniye kaydet.
2. **SCT yüksüz:** SCT'yi bağla, ölçülen hatta akım olmadığını doğrula ve aynı şekilde kayıt al.
3. **100 W akkor:** Aynı sensör/bağlantı düzeninde ampul açıkken kayıt al; yük durumunu not et.
4. Her kayıt için hedef hız, gerçek geçen süre, örnek sayısı ve mümkünse yaklaşık gerçekleşen örnekleme hızını kaydet.
5. Ham örnekleri değiştirmeden yerel dosyada sakla. Ham veri varsayılan olarak Git'e eklenmez.
6. Her kayıt için ortalama, minimum, maksimum, tepe-tepe aralığı ve standart sapma hesapla. Sonuçları koşullara göre tek tabloda karşılaştır.
7. Beklenen örnek sayısını hedef hız × gerçek kayıt süresi ile yaklaşık hesapla ve okunan örnek sayısıyla karşılaştır.
8. Her koşulun ham ADC örneklerini bilgisayarda ADC-değer/zaman grafiğinde görselleştir. Bu grafik ilk incelemenin temel çıktısıdır; canlı grafik veya gelişmiş osiloskop arayüzü zorunlu değildir. Grafiğin yanında istatistikleri karşılaştır ve kaydın neyi gösterdiğini/sınırlamalarını yaz.

## Yorumlama
- İlk amaç ham ADC örneklerini kaydetmek ve bilgisayarda görselleştirmektir; istatistikler grafiğin yorumlanmasına ve üç koşulun karşılaştırılmasına yardımcı olur.
- Ortalama, min/max, tepe-tepe aralığı ve standart sapma ham ADC değerlerinin tanımlayıcı istatistikleridir; doğrudan akım ölçümü değildir.
- Standart sapma yalnız gürültüyü ölçmez; yükün oluşturduğu gerçek AC sinyal de bu değeri artırabilir.
- Örnek sayısının hedefle eşleşmesi, örnekleme aralıklarının kusursuz olduğunu veya hiç örnek kaybolmadığını kanıtlamaz.
- Kayıtları sonradan yavaş oynatmak, gerçek ADC örnekleme hızını değiştirmez.
- İlk adımda 1 ve 2,5 kS/s hızlarını her koşulda denemek, üç ESP32'yi eşzamanlamak, her örneğe zaman damgası eklemek, DMA veya çift buffer kurmak şart değildir. İstatistikler belirli bir soruyu yanıtsız bırakırsa sonraki karşılaştırma buna göre tasarlanır.

## Kabul ölçütü
Üç koşul için ham kayıtların ve kayıt metadatasının mevcut olması; her kayıtta hedef hız, gerçek süre ve örnek sayısının bulunması; ortalama, min/max, tepe-tepe aralığı ve standart sapmanın hesaplanması; koşulların karşılaştırıldığı kısa bir sonuç notunun yazılması. Gerekirse tanı grafiği üretilir. Paketleme/aktarımın bir sonraki adımı için basit yaklaşımın yeterliliğine dair karar gerekçelendirilir.

## Durum
PLANLANDI. Fiziksel ölçüm ve yazılım uygulaması yapılmadı.


## Her adımın kaydı: HEDEF / LOG / SONUÇ
- **HEDEF:** Adımın cevaplayacağı soru ve kabul koşulu.
- **LOG:** Gerçek bağlantı/koşul, hedef hız, geçen süre, örnek sayısı, ham dosya yolu, hesaplanan istatistikler, gözlemler ve protokolden sapmalar. Yapılmayan işlem de açıkça yazılır.
- **SONUÇ:** Yalnız kaydın desteklediği yorum, belirsizlikler ve bir sonraki adıma geçme gerekçesi. Ölçüm yoksa sonuç uydurulmaz; ölçülmediği belirtilir.


## YAML yapılandırması
Deneyin planlanan koşulları [experiment.yaml](experiment.yaml) dosyasında açıklamalı olarak tutulur. YAML'daki hedef değerler planı temsil eder; gerçekleşen süre, örnek sayısı, gerçek örnekleme hızı, donanım bağlantısı ve sapmalar LOG'a yazılır. Firmware YAML dosyasını okumadığı sürece bu dosya çalışma zamanındaki ayarları değiştirmez.
