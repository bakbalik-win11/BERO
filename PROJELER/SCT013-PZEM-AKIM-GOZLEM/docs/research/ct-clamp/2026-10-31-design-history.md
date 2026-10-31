# ESPHome ct_clamp — tasarım tarihçesi ve geliştirici niyeti

**Araştırma tarihi:** 2026-10-31  
**Kapsam:** İlk PR/commit, PR incelemeleri, issue tartışmaları, 2021'de eklenen tekrar filtresi ve güncel kaynak kod.

## Kısa sonuç

ct_clamp, 2019'da CT (Current Transformer) akım pensiyle tek fazlı AC akımı ölçmek için eklenmiş bir ESPHome sensörüdür. Ana kod katkısı Jesse Hills'e (@jesserockz) aittir. Jesse, kodun büyük bölümünü OpenEnergyMonitor EMonLib'den aldığını ve ESP üzerinde harici güç monitörüyle karşılaştırarak “accurate enough” bulduğunu açıklamıştır. Otto Winter (@OttoWinter) PR incelemesinde mimari değişiklikler yapmış; örneklemenin ESPHome ana döngüsünü bloke etmesini önlemiştir.

Bileşen SCT013'e özel değildir: ilk geliştiricinin kullandığı CT modeli CTL-10-CLS'dir. ADC ve ADS1115 gibi farklı gerilim kaynaklarını VoltageSampler arayüzünden kabul edecek şekilde tasarlanmıştır. Ancak rastgele AC gerilimin genel RMS ölçeri de değildir; CT pensinden tek fazlı AC akım (A) elde etmeye yöneliktir.

200 ms varsayılanı resmî dokümantasyonda 50 Hz'de 10 tam çevrim olarak açıklanır. İlk kodda 60 s, ct_clamp'e özel gerekçeyle değil genel polling şemasının varsayılanı olarak kullanılmıştır. 60 s seçimini açıklayan geliştirici yorumu bulunamadı.

2021'de eklenen last_value filtresinin gerekçesi PR'de açıkça “duplicate samples” ve doğruluk iyileştirmesi olarak belirtilmiştir. Bellek tasarrufu veya ADC dönüşüm sayısını azaltmak olarak açıklanmamıştır. Mevcut kodda source_->sample() eşitlik kontrolünden önce çağrıldığı için filtre ADC çağrısını durdurmaz; alınmış aynı değerin istatistiklere ikinci kez eklenmesini engeller.

## 1. Kim yazdı, ilk commit ne zaman?

- İlk PR: [esphome/esphome#559 — Add CT Clamp component](https://github.com/esphome/esphome/pull/559), 26 Mayıs 2019'da açıldı.
- İlk bileşen commit'i: [3089ffa — Add CT Clamp component (#559)](https://github.com/esphome/esphome/commit/3089ffa8e73ee6daaa453704342a616ccef5c948), 29 Mayıs 2019.
- Commit author: Jesse Hills (@jesserockz).
- Commit committer: Otto Winter (@OttoWinter); commit mesajında co-author olarak da belirtilir.

**Değerlendirme:** “Jesse yazdı, Otto mimari inceleme ve katkı yaptı” ifadesi kayıtlarla uyumludur. Otto, yalnızca birleştiren kişi değildir; PR'de doğrudan kod ve tasarım önerileri sunmuştur.

## 2. Hangi ihtiyaçtan doğdu?

PR açıklaması: “Adds sensor code for CT (Current Transformer) Clamps.”

Jesse'nin PR yorumu:

> “I took the bulk of this code from EMonLib”

Aynı yorumda ESP üzerinde çalıştığını harici bir güç monitörüyle yan yana test ettiğini ve sonuçları “accurate enough” bulduğunu belirtir. [PR #559](https://github.com/esphome/esphome/pull/559).

Jesse test düzeneğini de tarif etmiştir: CTL-10-CLS pens, burden/direnç bölücü devresi üzerinden D1 Mini A0 pinine bağlanmış; evin tek fazlı ana canlı hattında kullanılmış ve akıllı sayaçla karşılaştırılmıştır.

**Kaynakların desteklediği sonuç:** İhtiyaç, ESPHome üzerinde CT pensiyle evin/tek fazlı hattın akımını okuyabilen bir sensördür. İlk hedefin enerji sayacı, güç kalitesi analizörü veya laboratuvar sınıfı RMS cihazı olduğuna dair açıklama yoktur.

## 3. SCT013'e özel mi, genel RMS bileşeni mi?

**SCT013'e özel değil.** İlk PR yazarı CTL-10-CLS kullandığını söyler. Kod belirli bir CT modelini veya dönüşüm katsayısını sabitlemez. Otto'nun PR incelemesindeki gerekçe:

> “other voltage sensors like ADS1115 can't be used with this component”

Otto, doğrudan analogRead'e bağlı kalınmamasını ve voltage_sampler::VoltageSampler arayüzünün kullanılmasını önermiştir. Böylece ADC ve ADS1115 gibi kaynaklar aynı bileşene bağlanabilir.

**Genel AC RMS ölçer de değil.** Resmî doküman bileşeni CT Clamp Current Sensor olarak tanımlar; CT pensi sinyalinden tek fazlı AC akımı ölçer ve amper cinsinden çıktı üretir. [ESPHome resmî dokümantasyonu](https://beta.esphome.io/components/sensor/ct_clamp/).

## 4. sample_duration neden 200 ms?

İlk commit'te sample_duration varsayılanı 200ms olarak tanımlanmıştır. Resmî dokümantasyon:

> “Defaults to 200ms which would be 10 whole cycles on a 50Hz system.”

Yani 50 Hz için 200 ms = 10 tam şebeke çevrimi. Dokümantasyon daha uzun örnekleme süresinin doğruluğu artırabileceğini de söyler.

Ancak ilk geliştiricinin özellikle neden 10 çevrimi seçtiğini, bunun deneyle mi belirlendiğini veya hangi tepki süresi/doğruluk uzlaşımını hedeflediğini açıklayan bir PR yorumu ya da commit gerekçesi bulamadım. PR sırasında Jesse'nin ara örneğinde sample_size: 1637 ve bunun ESP8266'da 50 Hz için 10 çevrim olduğu notu vardır; birleştirilen sürümde yapılandırma zaman tabanlı sample_duration: 200ms biçimine dönüşmüştür.

**Sonuç:** 200 ms'nin 50 Hz'de 10 çevrim olduğu belgelenmiştir. Bunun ötesinde özel tasarım gerekçesi kanıtlanmamıştır.

## 5. update_interval neden 60 saniye?

İlk commit'in Python şeması genel cv.polling_component_schema('60s') kullanır. Bu, ct_clamp'e özel bir zamanlama algoritması değildir; genel ESPHome polling bileşeni varsayılanıdır.

İlk commit'in test YAML'ında update_interval: 5s verilmiştir. Jesse'nin PR içindeki ara örneğinde 500ms vardır. Dolayısıyla geliştirici test sırasında 60 saniyeye bağlı kalmamıştır.

İncelenen kayıtlarda “60 s seçildi çünkü ...” açıklaması bulunamadı. Enerji tasarrufu, Home Assistant kayıt yükü veya ölçüm hassasiyeti için özel seçildiğini söylemek varsayım olur.

60 s örnekleme penceresi değildir: sample_duration ölçüm penceresinin süresini, update_interval yeni pencerenin ne sıklıkla başlatılacağını belirler.

## 6. last_value_ == value filtresi neden eklendi?

Filtre ilk sürümde yoktur. [PR #2283 — Improves ct_clamp component accuracy](https://github.com/esphome/esphome/pull/2283) ile Ekim 2021'de eklenmiştir.

PR açıklamasındaki gerekçe:

> “Improves accuracy avoiding duplicated samples”

Açıklama, ESPHome'un 1000 SPS'ye kadar örnek isteyebildiğini, ADS1115'in ise nadiren 860 SPS'den daha fazlasını sağlayabildiğini belirtir. Kod yorumu:

> “Assuming a sine wave, avoid requesting values faster than the ADC can provide them”

### Filtrenin yaptığı ve yapmadığı

Mevcut kod sırası:
1. source_->sample() çağrılır ve analog kaynaktan değer istenir.
2. NaN değilse son değerle karşılaştırılır.
3. Değer aynıysa fonksiyondan çıkılır; örnek sayısı ve toplamlar artırılmaz.
4. Değer farklıysa last_value_ güncellenir ve örnek istatistiklerine katılır.

Buna göre:
- **Belgelenmiş amaç:** Yinelenen ADC değerlerinin ayrı örnekler gibi hesaba katılmasını önleyerek doğruluğu artırmak.
- **Bellek:** PR'de bellek tasarrufu hedefi yoktur. Eklenen durum bir float değeridir.
- **ADC çağrı sayısı:** Azaltılmaz. source_->sample() karşılaştırmadan önce çağrıldığı için filtre dönüşüm/okuma talebini kesmez; yalnızca aynı değerin toplama yeniden katılmasını engeller.
- **Performans:** PR bunu performans optimizasyonu olarak tanımlamaz; gerekçe doğruluktur.

Bu filtre, aynı ADC sayısının tekrarlandığı her durumda ölçümün yanlış olduğu anlamına gelmez. ADC kuantalaması nedeniyle farklı gerçek dalga biçimi anları aynı sayısal değeri üretebilir. PR, tekrarların ADC dönüşüm hızının aşılması bağlamında sorun oluşturduğunu varsayar; her donanım ve örnekleme koşulunda kusursuz ayırt etme garantisi vermez.

## 7. İlgili PR ve issue tartışmaları

### PR #559 — ilk bileşen (Mayıs 2019)
- Jesse, kodun büyük bölümünü EMonLib'den aldığını ve harici güç monitörüyle test ettiğini belirtti.
- Otto, doğrudan analogRead kullanımının platform bağımlılığı yaratacağını ve ADS1115 gibi başka gerilim kaynaklarını dışarıda bırakacağını söyledi; VoltageSampler arayüzünü önerdi.
- Otto, ilk örnekleme yaklaşımının ESPHome ana döngüsünü yaklaşık 100 ms veya daha fazla yavaşlatabileceğini belirtti. update() yalnızca örneklemeyi başlatacak, gerçek örnekleme loop() içinde ve zaman aşımıyla bitecek şekilde asenkron yapıya geçirdi.
- Bu, ana döngüyü bloke etmeme niyetinin doğrudan geliştirici açıklamasıdır.

### Issue #457 / PR #647 — ADS1115 ve başlangıç offset'i (Haziran–Temmuz 2019)
- Kullanıcılar yeniden başlatma sonrasında değerin yaklaşık 0,50 A'dan başlayıp yavaşça normale geldiğini bildirdi.
- Otto, sebebin ESP8266 ADC aralığına göre 0,5 V başlangıç offset'i varsayımı ve offset üzerindeki düşük geçiren filtre olduğunu açıkladı; ADS1115 yüksek gain modunda bu varsayım uygun değildi.
- [PR #647](https://github.com/esphome/esphome/pull/647), açılışta offset kalibrasyonu ve ADS1115 continuous_mode desteği ekledi.
- Bu tartışma, farklı ADC kaynaklarıyla çalışmanın gerçek saha sorunları doğurduğunu gösterir.

### PR #2283 — yinelenen örnekleri eleme (Ekim 2021)
- PR doğrudan doğruluk iyileştirmesi olarak tanımlanmıştır.
- ESPHome döngüsünün ADS1115 dönüşüm hızından hızlı çağrılabilmesi ve aynı analog değerin yinelenmesi problemine odaklanır.
- last_value_ filtresi bu PR'de eklenmiştir; ilk tasarımın parçası değildir.

## 8. Hedef kullanım kategorileri: kanıtın söylediği

| Olası hedef | Kaynakların desteklediği değerlendirme |
|---|---|
| Enerji ölçümü (Wh/kWh) | **Hayır / kanıt yok.** Bileşen akım sensörüdür; enerji entegrasyonu bu bileşenin işi olarak tanımlanmamış. |
| Yük takibi | **Evet, pratik kullanım olarak uyumlu.** Geliştiricinin ev ana hattında CT pensini akıllı sayaçla karşılaştırması bunu destekler. |
| Ev otomasyonu | **Evet, platform bağlamı bu.** ESPHome sensörü olarak Home Assistant'a sunulur; özel kullanım hedefi ayrıca beyan edilmemiştir. |
| Home Assistant'ta kabaca akım görmek | **Uyumlu.** Geliştirici “accurate enough” der; laboratuvar doğruluğu iddiası yoktur. |
| Hassas RMS ölçümü | **Bu şekilde tanımlanmamış.** Doğruluk iyileştirmeleri vardır; hassasiyet standardı, hata bütçesi veya kalibrasyon garantisi belirtilmemiştir. |
| Genel AC RMS ölçer | **Hayır.** CT clamp kaynaklı tek fazlı AC akımı ölçen bileşendir. |

## 9. BERO açısından anlamı

BERO'nun ct_clamp kullanımı, orijinal tasarım hedefiyle aynı temel sınıftadır: CT pensinden gelen analog sinyal üzerinden AC akım gözlemek. Ancak ESPHome geliştiricilerinin belgelenmiş hedefi BERO'nun kararlı pencere eşleştirme, PZEM referanslı etiketleme veya eğitim veri seti oluşturma işi değildir; bunlar BERO'nun üst katman hedefleridir.

- update_interval: 60s zorunlu bir aralık değildir; ilk örneklerde 5 s ve 500 ms de kullanılmıştır.
- sample_duration: 200ms, 50 Hz'de 10 çevrimdir; daha uzun pencerenin BERO'daki etkisi E10 deneyiyle ölçülmelidir.
- last_value_ filtresi ADC çağrı hızını düşürmez; aynı sayısal dönüşün istatistiğe yinelenmesini önlemeyi hedefler. Bu nedenle num_samples değerini ham ADC dönüşüm sayısı olarak yorumlamamak gerekir.
- PR'deki ADC hızları 2021'deki ADS1115 bağlamına aittir; BERO ESP32 ADC'sinde aynı hız/tekrar davranışı olduğu varsayılmamalıdır.

## 10. Kaynaklar

1. İlk PR: https://github.com/esphome/esphome/pull/559
2. İlk commit (29 Mayıs 2019): https://github.com/esphome/esphome/commit/3089ffa8e73ee6daaa453704342a616ccef5c948
3. ADS1115 iyileştirme PR'si: https://github.com/esphome/esphome/pull/647
4. İlgili issue #457: https://github.com/esphome/issues/issues/457
5. Yinelenen örnekleri önleme PR'si: https://github.com/esphome/esphome/pull/2283
6. last_value_ değişikliğini içeren commit: https://github.com/esphome/esphome/commit/c33077bc61a214df23d82753ae9077898c280786
7. ESPHome resmî ct_clamp dokümantasyonu: https://beta.esphome.io/components/sensor/ct_clamp/
8. ESPHome 2026.10.1 kaynak kodu: https://github.com/esphome/esphome/blob/4ea26ed/esphome/components/ct_clamp/ct_clamp_sensor.cpp

---
**Kanıt standardı:** Geliştirici alıntıları PR/issue metinlerinden; varsayılanlar ilk commit ve resmî dokümantasyondan; bugünkü filtre sırası 2026.10.1 kaynak kodundan alınmıştır. Geliştiricinin açıklamadığı 60 s seçimi ve 200 ms'nin tarihsel tercih gerekçesi varsayılmamıştır.
