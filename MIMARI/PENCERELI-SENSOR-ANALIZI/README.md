# BERO — Pencereli Sensör Analizi ve Davranış Çıkarımı

**Belge türü:** Üst seviye mimari tasarım  
**Durum:** TASARIM / GELİŞTİRME İLKESİ; genel amaçlı çalışan sistem olarak doğrulanmadı.  
**İlk uygulama:** [SCT013 + PZEM akım gözlem sistemi](../../PROJELER/SCT013-PZEM-AKIM-GOZLEM/README.md)

## 1. Amaç

BERO'nun amacı yalnızca tek bir sensörün değerini okumakla sınırlı kalmamalıdır. Farklı sensörlerden gelen ölçümlerin zaman pencereleri içinde anlamlı özelliklere dönüştürülmesi ve bu özelliklerden sistem/donanım davranışlarının çıkarılabilmesi hedeflenir.

Bu belge, SCT013 deneylerinde edinilen yazılım ve ölçüm tecrübelerini sensörden bağımsız bir mimari seviyeye taşır. SCT013 ilk uygulamadır; mimarinin tamamı veya tek referansı değildir.

Temel akış:

~~~text
SENSÖR
  |
  v
KATMAN 1 — VERİ TOPLAMA
  |
  v
KATMAN 2 — ÖZELLİK ÇIKARMA
  |
  v
KATMAN 3 — DAVRANIŞ ÇIKARIMI
~~~

Katmanlar ortak bir çerçeve sağlar. Her sensörün elektriksel arayüzü, örnekleme hızı, pencere uzunluğu, matematiksel işlemi ve kalibrasyonu kendine özgüdür.

## 2. Katman 1 — Veri toplama

### Sorumluluk

Fiziksel sensörün veya dijital ölçüm kaynağının verisini almak ve sonraki katmanların kullanabileceği güvenilir, izlenebilir ölçüm girdisi oluşturmak.

### Alt işler

1. **Kaynak adaptörü:** ADC, I2C, SPI, UART/Modbus, pulse veya başka bir arayüzden veri alır.
2. **Zaman bilgisi:** Kaynağın timestamp'i, saat dilimi ve mümkünse ölçüm/pencere başlangıç-bitiş zamanları korunur.
3. **Geçerlilik kontrolü:** NaN, timeout, parse hatası, bağlantı hatası ve sensörün izin verilen aralığı dışındaki değerler gerçek sıfırdan ayrı tutulur.
4. **Örnek yönetimi:** Örnek sayısı, örnek aralığı, stale/tekrar durumu ve veri kaybı gerekiyorsa izlenir.
5. **Pencere oluşturma:** Özellik çıkarma için gereken örnekler belirli süre veya örnek sayısı boyunca gruplanır.
6. **Sınırlı tamponlama ve yayın:** Gerekli örnekler geçici bellekte tutulabilir; özellik kayıtları ve olay bilgisi üst sisteme aktarılır.

### BERO için kayıt sınırı

BERO'nun mevcut kararında sürekli ham ADC dalga biçimi arşivlenmez. Gerekli olduğunda sınırlı event buffer veya teşhis logu kullanılabilir; normal veri hattında pencere/özellik özetleri, zaman bilgisi, kaynak kimliği ve kalite bilgisi korunur.

Bir sensörün Home Assistant'a saniyede bir yayın yapması, sensörün yalnızca saniyede bir örneklendiği anlamına gelmez. **Örnekleme hızı**, **işleme penceresi** ve **yayın aralığı** ayrı kavramlardır ve her uygulamada açıkça belgelenmelidir.

## 3. Katman 2 — Özellik çıkarma

### Sorumluluk

Katman 1'den gelen örnek penceresini, sensörün sinyal türüne uygun sayısal özelliklere dönüştürmek.

Bu katman **ct_clamp** gibi bir algoritmanın yer aldığı yerdir. **ct_clamp**, BERO'nun tüm mimarisi değil; CT/AC akım sinyali için kullanılabilen belirli bir özellik çıkarma uygulamasıdır.

### Örnek özellikler

| Sensör / sinyal türü | Olası pencere özellikleri | Dikkat |
|---|---|---|
| SCT / AC akım trafosu | AC RMS, ortalama, tepe, değişkenlik | Bias/DC bileşeni ve sensör katsayısı doğru ele alınmalı |
| ACS712 / Hall akım | DC ortalama, AC RMS, tepe | Ortalama DC akım bileşenini taşıyabilir; otomatik olarak atılmaz |
| Mikrofon | RMS, tepe, tepe-tepe, frekans özellikleri | RMS tek başına dB SPL değildir; mikrofon ve kazanç kalibrasyonu gerekir |
| İvmeölçer | Eksen bazında ortalama, RMS, tepe, varyans | Eksen, yerçekimi bileşeni, montaj ve bant genişliği dikkate alınır |
| Gerilim trafosu | AC RMS, tepe, frekans özellikleri | Güvenli analog ön uç ve uygun izolasyon gerekir |
| Sıcaklık / nem | Ortalama, medyan, min, max, eğim | AC RMS çoğu uygulamada anlamlı özellik değildir |
| Basınç / seviye | Ortalama, medyan, aralık, değişim hızı | Sensör transfer fonksiyonu ve dinamik tepki önemlidir |
| Pulse / debi / devir | Darbe sayısı, frekans, periyot | Örnek dizisi yerine olay/zaman sayımı daha uygundur |

Özellik listesi zorunlu bir katalog değildir. Gerçek kullanım amacına göre seçilir.

### CT için AC RMS örneği

Bir pencere içindeki örnekler xᵢ, pencere ortalaması x̄ ve örnek sayısı N ise:

~~~text
AC_RMS = sqrt( sum((x_i - mean(x))^2) / N )
~~~

Bu, pencere ortalamasına göre AC bileşeninin RMS değeridir ve matematiksel olarak aynı pencerenin standart sapmasıyla eşdeğerdir (N paydalı tanım). ESPHome **ct_clamp** uygulamasının yaklaşımı budur. Her sensöre uygulanacak evrensel formül değildir.

### Tekrar eden değerler

Aynı sayısal değerin tekrar gelmesi her zaman hatalı veya eski örnek anlamına gelmez. Yavaş sıcaklık/basınç sensöründe tekrar, gerçek sabit durumu gösterebilir. Yinelenen örnekleri eleme kararı; kaynağın dönüşüm yenileme davranışı biliniyorsa ve örnek zamanlamasıyla birlikte değerlendiriliyorsa alınır.

### Fiziksel birime dönüşüm

Özellikten amper, volt, derece, bar, rpm veya başka bir fiziksel birime geçiş ayrı bir adımdır. Katsayı ve transfer fonksiyonu sensör modeli, analog ön uç, besleme, ADC, montaj ve kalibrasyon koşullarına bağlı olabilir. Bir sensörün katsayısı diğer sensöre taşınmaz.

## 4. Pencere kavramlarını birbirinden ayır

BERO'da "pencere" sözcüğü iki ayrı seviyede kullanılabilir:

1. **Özellik penceresi:** Ham örneklerin RMS/ortalama/tepe gibi tek bir özellik kaydına dönüştürüldüğü kısa aralık. Örneğin mevcut SCT uygulamasındaki **ct_clamp sample_duration**.
2. **Kararlılık penceresi:** Art arda üretilmiş özellik kayıtlarının bir süre boyunca kararlı olup olmadığını değerlendiren daha uzun aralık.

Bu iki pencere aynı şey değildir. Bir **ct_clamp** penceresinin kararlı olması, yükün uzun süre kararlı olduğunu tek başına kanıtlamaz. BERO'nun SCT-PZEM çalışmasında PZEM ve SCT kararlılığı ayrı belirlenir; zaman bakımından örtüşen kararlı alanlar eşleştirilir.

## 5. Katman 3 — Davranış çıkarımı

### Sorumluluk

Katman 2'nin ürettiği özellikleri, zaman ilişkilerini, olay bilgilerini ve birden fazla sensörden gelen kanıtı değerlendirerek bir durum/olay hakkında çıkarım yapmak.

### Olası yöntemler

- Eşik ve histerezis tabanlı kurallar.
- Birden fazla pencere boyunca durum geçişi / süre koşulları.
- Sensörler arası zaman eşleştirme ve korelasyon.
- İstatistiksel sınıflandırma.
- Yeterli etiketli veri oluştuğunda makine öğrenmesi.

### Örnek — çamaşır makinesi (gelecek senaryo)

| Girdi özelliği | Olası çıkarım | Kanıt sınırı |
|---|---|---|
| SCT akım RMS yükselmesi | Bir elektrik yükü devreye girmiş olabilir | Tek başına hangi yükü olduğunu söylemez |
| İvmeölçer RMS yükselmesi | Mekanik hareket/titreşim artmış olabilir | Montaj ve makine zemini etkiler |
| Mikrofon RMS/frekans değişimi | Ses kaynağı veya çalışma evresi değişmiş olabilir | Tek başına su akışını kanıtlamaz |
| Akım + titreşim + ses zaman örüntüsü | Belirli çalışma fazı adayı | Kural/model, tekrarlı çevrimlerle doğrulanmalıdır |

Örneğin "akım var + titreşim var + su sesi yok = sıkma fazı" başlangıçta yalnızca bir hipotezdir. Farklı çevrimlerde etiketli verilerle doğrulanmadan kesin sınıflandırma kuralı sayılmaz.

## 6. Katmanlar arası ortak veri sözleşmesi

Her uygulama kendi protokolünü kullanabilir; ancak mümkün olduğunca aşağıdaki anlamları taşıyan alanlar korunmalıdır:

| Alan | Anlam |
|---|---|
| sensor_id | Sensörün fiziksel/lojik kimliği |
| channel_id | Sensör kanalının kimliği |
| source | ADC, I2C, UART/Modbus, pulse vb. kaynak |
| timestamp | Kaynak ölçüm zamanı ve timezone |
| window_start, window_end | Özellik penceresinin sınırları |
| sample_count | Pencerede değerlendirilen örnek sayısı |
| validity | Geçerli, eksik, stale, timeout, aralık dışı vb. durum |
| feature_name, feature_value, unit | Çıkarılan özelliğin adı, değeri ve birimi |
| calibration_id | Yalnız gerçek bir kalibrasyon kaydı varsa kimliği |
| event_id, boot_id | İlgili olay/cihaz oturumu varsa ilişkilendirme |

Bu tablo mevcut çalışan bir BERO veri şeması iddiası değildir; farklı uygulamaların ortak anlamları kaybetmemesi için önerilen mimari sözleşmedir. Mevcut HA entity'leri ve Python veri hattı bu sözleşmeye aşamalı uyarlanabilir.

## 7. Katmanlar arası ortak ilkeler

- Örnekleme, pencere süresi ve yayın aralığı ayrı tanımlanır.
- Hata/timeout ile gerçek sıfır birbirine dönüştürülmez.
- Kaynak timestamp, timezone, entity/sensör kimliği, birim ve ham kaynak değeri mümkün olduğunca korunur.
- Ölçüm, üretici belgesi, kullanıcı bildirimi, hesap ve hipotez ayrı etiketlenir.
- Sürekli ham dalga arşivi varsayılan değildir; veri saklama amacı ve gereksinimi açık olmalıdır.
- Kalibrasyon katsayısı sensör/kanal/ön uç kimliğiyle ilişkilendirilir; bilinmeyen kimlik uydurulmaz.
- Özellik çıkarma ve davranış sınıflandırma birbirinden ayrı tutulur.
- Bir davranış sonucu, onu destekleyen sensör özellikleri ve zaman aralığıyla izlenebilir olmalıdır.

## 8. İlk uygulama: SCT013 + PZEM

İlk uygulama ve kanıtlar: [SCT013-PZEM proje kaydı](../../PROJELER/SCT013-PZEM-AKIM-GOZLEM/README.md).

Mevcut uygulamadan gelen örnekler:

- [Sensör okuma kalıpları ve açıklamalı YAML örnekleri](../../PROJELER/SCT013-PZEM-AKIM-GOZLEM/firmware/patterns/README.md)
- [ESPHome ct_clamp tasarım sentezi](../../PROJELER/SCT013-PZEM-AKIM-GOZLEM/docs/research/ct-clamp/2026-10-31-synthesis-copilot-claude-independent.md)
- [Log 63 gerçek ölçüm analizi](../../PROJELER/SCT013-PZEM-AKIM-GOZLEM/logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-analysis.md)

**Mevcut durum:** SCT/CT için çalışan **ct_clamp** uygulaması ve gerçek log örnekleri proje klasöründe kayıtlıdır. Genel amaçlı sensör çerçevesi tasarım belgesidir. Analog DC örnek YAML'ı referans şablondur; derleme/OTA/fiziksel doğrulama yapılmış sayılmaz. Mikrofon, ivmeölçer ve diğer sensörler henüz BERO'ya entegre edilmiş değildir.

PZEM'in rolü de sınırlıdır: mevcut SCT projesinde kararlı pencerelerin karşılaştırılması/etiketlenmesi için proje referansıdır; bütün sensörler için genel ground truth değildir.

## 9. Yeni sensör ekleme akışı

1. Sensör modeli, elektriksel arayüzü, beslemesi ve üretici transfer fonksiyonu belgelenir.
2. Kart/pin ve elektriksel sınırlar gerçek donanımda doğrulanır.
3. Önce kaynak okuma ve geçerlilik davranışı tek başına gözlenir.
4. Örnekleme hızı, özellik penceresi ve yayın aralığı birbirinden ayrılarak belirlenir.
5. Sensör sinyaline uygun özellikler seçilir; gerekçesi yazılır.
6. Fiziksel birime dönüşüm ve kalibrasyon ayrı ele alınır.
7. Gerçek log, test koşulları ve yorum saklanır.
8. Davranış çıkarımı ancak tekrarlı, zaman ilişkisi korunmuş ve etiketli örnekler oluştuktan sonra eklenir.

## 10. Geliştirme sınırı ve doğrulama

Bu mimari belgesi bir tasarım yönüdür; çalışan yazılım, ESPHome bileşeni veya tamamlanmış davranış sınıflandırma sistemi değildir. Her yeni uygulama için kaynak kod/şablonun derlenmesi, gerçek bağlantı ve donanım testi, gerçek çıktı/log ve beklenen-gözlenen davranış karşılaştırması ayrı ayrı kaydedilir. Bir aşamanın tamamlanması diğer aşamaların da tamamlandığı anlamına gelmez.

SCT013-PZEM uygulamasının görev sırası ve aktif işleri kendi [STATUS](../../PROJELER/SCT013-PZEM-AKIM-GOZLEM/STATUS.md) ve [ROADMAP](../../PROJELER/SCT013-PZEM-AKIM-GOZLEM/ROADMAP.md) dosyalarında yönetilmeye devam eder. Bu mimari kaydı T010 veya diğer Faz 2 görevlerinin sırasını değiştirmez.


## 10. Sensörden bağımsız veri değerlendirme disiplini

SCT013 çalışmasında geliştirilen yaklaşım yalnız akım sensörüne özgü değildir. BERO'nun farklı sensörlerinden gelen zaman serileri de ham ölçümün korunması, uygun pencerelerde özellik çıkarılması ve zaman içindeki davranışın değerlendirilmesi ilkeleriyle ele alınabilir.

Örneğin CO₂ sensörü de zaman içinde değişen bir fiziksel büyüklük ölçer. Tek bir ppm değerine bakmak yerine, sensörün tepki süresi ve ortamın değişim dinamiğine uygun pencerelerde şu özellikler hesaplanabilir:
- Ortalama ve medyan CO₂ seviyesi.
- Pencere içindeki minimum ve maksimum.
- Değişim aralığı ve değişim hızı (ppm/dakika gibi).
- Belirli bir seviyenin üzerinde geçirilen süre.
- Havalandırma açılmadan önceki ve açıldıktan sonraki eğilim farkı.

Bu özellikler, CO₂'nin tekil bir anlık değerinden daha açıklayıcı olabilir. Örneğin havalandırma başladıktan sonra CO₂'nin düşüş eğimi ve belirli bir aralığa dönme süresi, hava değişiminin davranışını incelemek için kullanılabilir. Ancak CO₂ düşüşü tek başına fanın debisini veya havalandırma verimini kanıtlamaz; oda hacmi, kişi sayısı, kapı/pencere durumu, dış ortam CO₂ seviyesi ve hava akış yolu gibi koşullar da sonucu etkiler.

**Ortak olan yöntem; pencereleme, özellik çıkarma, kalite kontrolü, zaman ilişkisi kurma ve davranış değerlendirmesidir. Sensöre özel olan ise örnekleme sıklığı, pencere uzunluğu, fiziksel birim, tepki süresi, filtre ve geçerlilik koşullarıdır.** SCT'nin 200 ms özellik penceresi CO₂'ye taşınmaz. Her sensör için üretici özellikleri ve gerçek ortam davranışı dikkate alınarak ayrı parametre seçilir.

Örnek olarak Senseair S8 bir NDIR CO₂ sensör ailesidir ve UART/Modbus üzerinden dijital ölçüm verir. S8 varyantları arasında ölçüm aralığı, doğruluk ve tepki süresi farklılıkları bulunabilir; ürün varyantı kesinleşmeden tek bir teknik değer varsayılmaz. Üretici ürün sayfası ve ilgili varyantın veri sayfası esas alınmalıdır: https://senseair.com/product/s8/.

Bu yaklaşım BERO'da bir **veri değerlendirme disiplini** oluşturur: ham ölçüm sensöre özgü biçimde alınır ve korunur; sensöre uygun zaman pencerelerinde türetilmiş özellikler üretilir; daha üst katmanda tek veya çoklu sensör davranışları değerlendirilir. Böylece aynı yazılım/mimari ilkeler farklı sensörlere uyarlanabilir, ancak sensörlerin fiziksel özellikleri ve parametreleri birbirine kopyalanmaz.


## 11. ct_clamp araştırmasından çıkan algoritma okuryazarlığı ve sensörler arası uyarlama

SCT013 çalışmasının önemli çıktılarından biri yalnızca çalışan bir akım okuma kodu bulmak değildir. ESPHome ct_clamp bileşeninin kaynak kodu, geçmiş PR'ları ve farklı yapay zekâ incelemeleri birlikte araştırılarak algoritmanın içindeki işlemler, bunların gerekçeleri ve sınır durumları incelenmiştir. Araştırma sentezi: [ct_clamp üç kaynaklı teknik sentez](../../PROJELER/SCT013-PZEM-AKIM-GOZLEM/docs/research/ct-clamp/2026-10-31-synthesis-copilot-claude-independent.md).

Bu incelemede somut olarak:
- CT örneklerinden DC ofseti ayırıp AC bileşeninin RMS değerini standart sapma yaklaşımıyla hesaplama,
- örnekleme penceresi ile yeni ölçümün başlama/yayın aralığının farklı kavramlar olması,
- ADC'nin aynı sayısal değeri tekrar vermesi durumunda yinelenen örneğin istatistiğe ikinci kez katılmaması,
- NaN/negatif karekök gibi sayısal sınır durumlarının ele alınması,
- çoklu CT örnekleyicilerinin eşzamanlı çalışmasından doğan örnekleme sorunları
araştırılmıştır.

Bu araştırma, bir algoritmanın adını veya kodunu başka sensöre kopyalamak anlamına gelmez. Asıl kazanım, bir ölçüm algoritmasının hangi aşamalardan oluştuğunu ve her işlemin hangi fiziksel/veri koşulunda anlamlı olduğunu anlayabilmektir. Örneğin aynı sayısal sıcaklık değerinin tekrar gelmesi çoğu zaman gerçek ve geçerli bir sabit durumu gösterebilir; ct_clamp içindeki tekrar eleme davranışı sıcaklık veya basınç sensörüne otomatik olarak taşınamaz.

### PZEM ve SCT'nin zaman davranışından öğrenilenler

PZEM ve SCT karşılaştırması, farklı sensör/ölçüm zincirlerinin aynı fiziksel olay karşısında farklı güncelleme sıklığı ve yerleşme davranışı gösterebileceğini ortaya koymuştur. BERO bu nedenle tekil örnekleri doğrudan birbirine eşlemek yerine her ölçüm akışının kendi zaman davranışını ve kararlılığını ayrı değerlendirmeyi benimser. Kararlı alanların zaman örtüşmesi daha sonra bulunur. PZEM'in burada kullanılması, onun bütün sensörler için mutlak ground truth olduğu anlamına gelmez.

SCT'nin daha hızlı sonuç üretmesi kısa süreli geçişleri daha ayrıntılı gözlemleme olanağı sağlar; daha yavaş tepki veren CO₂, sıcaklık veya başka sensörlerde ise uygun pencere ve karar süresi daha uzun olabilir. Örnekleme hızı, özellik penceresi ve yayın aralığı her sensör için ayrı belirlenmelidir.

### Titreşim verisine olası uyarlama

İvmeölçer/titreşim verisi de zaman serisi olarak benzer üst düzey değerlendirme akışına alınabilir:
- ham ivme örneklerini ve zaman damgalarını koruma,
- sensör bant genişliği ve ölçülmek istenen mekanik olaya uygun örnekleme,
- uygun pencerelerde RMS, standart sapma, tepe değer, tepe faktörü veya gerektiğinde frekans özellikleri çıkarma,
- ardışık pencerelerde seviye ve dağılım değişimini izleme,
- motorun çalışma/duruş çevrimlerini ve uzun dönem titreşim eğilimlerini değerlendirme.

Titreşim için ct_clamp RMS formülü, 200 ms pencere, ADC tekrar filtresi veya SCT eşikleri doğrudan kopyalanmaz. İvmeölçer eksenleri, montaj yeri, örnekleme frekansı, sensör bant genişliği, mekanik rezonanslar ve hedeflenen arıza/olay türü ayrı değerlendirilir. RMS tek başına tüm mekanik arızaları ayırt etmez; tepe, kurtosis ve frekans alanı özellikleri ancak ihtiyaç ve veri gerekçelendirirse eklenir.

**Mimari sonuç:** BERO sensörler arasında tek bir sabit algoritma kullanmaz; sensör fiziğine göre uyarlanan ortak bir veri değerlendirme metodolojisi kullanır. Ortak disiplin; ham veriyi koruma, geçerlilik kontrolü, zaman penceresi kurma, sinyale uygun özellik çıkarma ve zaman içindeki davranışı yorumlamadır. Sensöre özgü parametreler ve matematiksel işlemler ayrı doğrulanır.
