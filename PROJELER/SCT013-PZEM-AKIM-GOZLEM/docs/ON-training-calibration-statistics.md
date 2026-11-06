# SCT ON eğitim verisi ve katsayı belirleme istatistiği

**Durum:** Tasarım ilkeleri kaydedildi; nihai istatistiksel kestirici ve sayısal kabul eşikleri deneylerle seçilecek.  
**Tarih:** 2026-11-06  
**Kapsam:** İlk aşama — doğru ON verisini seçmek, SCT'nin temsilî katsayısız çıktısını belirlemek ve PZEM referansıyla K katsayısını hesaplamak.

## 1. Amaç ve aşama ayrımı

İlk aşamanın amacı, fiziksel yük ON ve kararlı durumdayken SCT'nin ürettiği katsayısız `ct_clamp` çıktısından güvenilir bir temsilî değer elde etmek ve bunu PZEM akım referansıyla eşleştirerek K katsayısını belirlemektir.

Bu belge **canlı yük değişimi algoritmasını tanımlamaz**. Eğitimde veri seçimi ve kalibrasyon için kullanılan istatistikler ile daha sonra canlı akışta kullanılacak değişim/kararlılık istatistikleri ayrı tasarlanacaktır.

Öncelikli SCT serisi, `on_raw_value` ile yayımlanan katsayısız `ct_clamp` çıktısıdır. Bu değer ham ADC örnekleri değildir. K uygulanmış entity ayrıca korunur; ilk aşamadaki istatistiksel değerlendirme katsayısız seri üzerinden yapılır.

## 2. Eğitim verisi kabul kuralları

1. **Fiziksel ON doğrulanmalıdır.** UDP `STATE=ON/OFF` tek başına fiziksel yük durumunun kanıtı değildir; yalnız olay işaretleyicisidir. Gerçek yük durumu deney kaydıyla doğrulanır.
2. **ON başlangıç geçişi kalibrasyon örneği değildir.** Yükün ve ölçüm zincirinin yerleşme/geçiş bölgesi, kararlı alan başlamadan önce dışarıda tutulur.
3. **PZEM kararlılığı kontrol ölçütüdür.** PZEM'in geçiş/ara değerleri kararlı ON örneklerine katılmaz. PZEM mutlak ground truth olarak değil, bu proje için referans olarak kullanılır.
4. **Yalnız kararlı ON alanları kullanılır.** Her ON çevriminin geçerli kararlı aralığı ayrı tanımlanır ve ayrı özetlenir.
5. **OFF sonrası örnekler eğitimden çıkarılır.** OFF verisi ham arşivde korunur; ON katsayısı hesabına veya ON kararlılık istatistiğine girmez.
6. **Ham veri silinmez/değiştirilmez.** Uç değer adayları işaretlenir; ham serinin üzerine yazılmaz. Filtrelenmiş/elenmiş türev veri ayrı üretilir.
7. **Tekrarlı ON çevrimleri ayrı tekrar kabul edilir.** Ardışık 1 saniyelik yayınlar bağımsız deney gözlemleri gibi sayılmaz. Çevrim bazında özetler ve çevrimler arası tutarlılık raporlanır.

ON başlangıcından kaç saniye çıkarılacağı ve PZEM kararlılık koşulunun sayısal tanımı henüz evrensel sabit değildir. Deney protokolünde önceden belirtilir; sonuç görüldükten sonra değiştirilmez. E16-E analizindeki ilk/son 5 saniye çıkarımı o analize ait seçim kuralıdır, tüm deneylere otomatik uygulanacak nihai kural değildir.

## 3. Eğitimde karşılaştırılacak merkez ve yayılım istatistikleri

Aynı seçilmiş kararlı ON örnekleri üzerinde en az şu merkez kestiricileri karşılaştırılır:

- **Aritmetik ortalama:** Bütün ölçümlerin ortalaması; uç değerlere duyarlıdır.
- **Medyan:** Tipik merkez değer için sağlam aday; uç değerlerden ortalamaya göre daha az etkilenir.
- **Kırpılmış ortalama (trimmed mean):** Alt ve üst kuyruklardan önceden belirlenmiş oran çıkarılarak hesaplanır. Kırpma oranı sonuçlara bakılarak seçilmez.

Dağılım/saçılım için birlikte raporlanacak parametreler:

- Örnek sayısı (n), ortalama, medyan ve standart sapma (SD).
- Q1, Q3 ve IQR = Q3 − Q1.
- MAD = median(|x − median(x)|); gerekirse normal dağılım ölçeğine dönüştürülmüş sağlam yayılım (1.4826 × MAD).
- P05, P95 ve P95 − P05.
- Her ON çevriminin ayrı merkez ve yayılımı; çevrim merkezlerinin çevrimler arası dağılımı.

**IQR uç değer işaretleme:** Alt sınır Q1 − 1.5 × IQR, üst sınır Q3 + 1.5 × IQR olarak hesaplanabilir. Bu sınırların dışındaki noktalar otomatik silinmez; yalnızca uç değer adayı olarak etiketlenir. Küçük örneklemli pencerelerde, özellikle son 3–5 ölçümde, çeyrekler kararsız olabileceğinden bu kuralın tek başına karar vermesi beklenmez.

Hampel filtresi (kayan medyan + MAD) canlı akış için aday yöntemdir; eğitim verisinin merkez kestiricisini seçme kararıyla karıştırılmaz. Eğitim aşamasında öncelik tam kararlı ON dağılımını ve çevrimler arası tekrarlanabilirliği değerlendirmektir.

## 4. K katsayısının hesaplanması ve doğrulanması

Her geçerli ON çevrimi için aynı zaman aralığından:

- (S_j): katsayısız SCT çıktısının seçilen merkez kestiricisi,
- (P_j): PZEM akımının aynı kararlı aralıktaki referans özeti.

Oran tabanlı aday katsayı (K_j = P_j / S_j) olarak hesaplanır. Birden fazla ON çevriminin katsayıları ayrı raporlanır; çevrimler arası dağılım incelenmeden tek katsayı kesinleştirilmez. Nihai birleştirme yöntemi (ör. çevrim katsayılarının medyanı veya tüm geçerli eşleşmelerin ortak kestirimi) deney sonuçlarıyla seçilecektir.

Bu oran yaklaşımı, sıfır ofsetinin ihmal edilebilir olduğu ve ilgili aralıkta doğrusal ölçek ilişkisinin makul olduğu varsayımını içerir. Bu varsayım farklı akım seviyelerinde kontrol edilmelidir. Tek yük seviyesinden bulunan K, tüm akım aralığında doğrulanmış kabul edilmez. Birden fazla kararlı yük seviyesinde aynı yöntem tekrarlanmalı; katsayı ve artık/sapma davranışı karşılaştırılmalıdır.

PZEM bu projede kalibrasyon eşleştirmesinin referansıdır; mutlak ve hatasız ground truth olduğu iddia edilmez. Kullanıcı tarafından daha önce belirtilen ±%4 hedefi, bu istatistiksel seçim için ayrıca açıkça kabul edilmeden otomatik eşik olarak uygulanmaz.

## 5. Kaydedilecek ölçüm ve deney parametreleri

Her veri seti ve her firmware turu için aşağıdaki bilgiler kaydedilir:

### SCT / ESP ölçüm zinciri
- SCT model ve oranı (ör. SCT013 30A/1V), fiziksel sensör kimliği.
- Fiziksel sarım/geçiş sayısı; ölçülen iletken ve sensörün iletken üzerindeki konumu/yönü.
- ESP kartı/modeli, GPIO ve ADC kanal eşlemesi (mevcut CH1-1T: GPIO32 / ADC1_CH4).
- ADC attenuation (mevcut deneylerde 12dB).
- `sample_duration` (ct_clamp ölçüm penceresi).
- `interval` (ölçümün tetiklenme/yayın aralığı); `update_interval` ayarı.
- K katsayısı ve katsayısız/katsayılı entity kimlikleri.
- Bias/burden devresi ve bağlantı değişikliği olup olmadığı.
- YAML dosya yolu, Git dalı/commit/blob kimliği, ESPHome sürümü ve cihaz build/OTA log bilgisi.

### PZEM / yük / zaman eşleştirmesi
- PZEM model/firmware mümkünse, ölçülen akım entity'si ve zaman damgaları.
- Yük türü, nominal bilgisi ve fiziksel ON/OFF doğrulama yöntemi.
- ON çevrim başlangıç/bitiş zamanları; BOOT_ID + EVENT_ID yalnız olayları eşleştirmek için saklanır.
- Kararlı ON aralığının başlangıç/bitişi ve seçim gerekçesi.
- PZEM kararlı aralık özeti; geçiş örneklerinin dışlandığı aralık.
- Saat dilimi (Türkiye oturumlarında +03:00), kaynak CSV adı ve SHA-256.
- `calibration_id`, analiz kodu/sürümü ve üretilen veri/rapor sürümü.

Bir ölçüm parametresi değiştiğinde aynı kalibrasyon serisiymiş gibi birleştirilmez; değişiklik ve yeni kalibrasyon kimliği kaydedilir.

## 6. E15/E16 deneylerinin bu karardaki yeri

- **E15**, `sample_duration=100ms` sabitken SCT yayın aralığını 500ms / 1s / 2s karşılaştırır.
- **E16**, `interval=1s` sabitken `sample_duration` değerini 50ms / 100ms / 200ms karşılaştırır.
- Bu deneyler, eğitimde kullanılacak ölçüm penceresi ve okuma parametrelerini seçmeye veri sağlar. Tek başlarına K katsayısının nihai istatistiksel kestiricisini belirlemezler.
- E16-E'de 10 ON çevriminden seçilen 293 katsayısız SCT değeri için hesaplanan istatistikler ilgili analiz raporundadır. D ve F aynı veri seçme kuralıyla analiz edilmeden ölçüm penceresi seçilmez.

## 7. İlk aşama çıktısı

İlk aşama tamamlandığında her geçerli yük seviyesi için:
1. Ham ve seçilmiş kararlı ON veri aralıkları,
2. Merkez/yayılım istatistiklerinin karşılaştırması,
3. ON çevrimleri arası tekrarlanabilirlik,
4. PZEM–SCT eşleşmeleri ve aday K değerleri,
5. Seçilen kestiricinin gerekçesi, sınırları ve doğrulama sonuçları,
6. Ölçüm parametreleri ve kaynak veri hash'leri

birlikte arşivlenir.

**Eğitim çiftinin merkez kestiricisi medyandır; aritmetik ortalama eğitim temsilî değeri olarak kullanılmayacaktır.** Ortalama ve trimmed mean yalnızca dağılımı betimlemek veya yöntem karşılaştırmalarında yardımcı istatistik olarak raporlanabilir. IQR/Hampel eşikleri, sayısal kararlılık/yerleşme koşulları, minimum örnek sayısı ve kabul toleransı henüz kesinleştirilmemiştir; bunlar deney protokolünde önceden tanımlanacaktır.

## 2026-11-06 — ON çevrimi bazında SCT–PZEM medyan eğitim çifti

**Kullanıcı kararı:** İlk katsayı eğitiminde her fiziksel olarak doğrulanmış kararlı ON çevrimi ayrı bir eğitim gözlemi olacaktır. Aynı kararlı zaman aralığı içinde SCT ve PZEM serileri ayrı ayrı medyanla özetlenecek; o ON çevriminin eğitim kaydı bu iki medyandan oluşan SCT–PZEM çifti olacaktır.

### Uygulama sırası

1. Fiziksel olarak doğrulanmış her ON–OFF çevrimi ayrı ele alınır. ON başlangıcından sonra SCT ve PZEM akışları kendi kararlılık koşullarıyla ayrı ayrı izlenir. Eğitim penceresi, iki akışın da kararlı olduğu ilk anda başlar; yani `start = max(SCT_STABLE_START, PZEM_STABLE_START)`. Böylece açılışta önce kararlı olan akışın tek başına bulunduğu bölüm eğitime girmez.
2. SCT için tek kanal/tek yayın akışı korunur. Başlangıç okuma tercihi 500 ms yayın aralığıdır; paket içine birden fazla ölçüm doldurulmaz. Paket boyutu ve firmware yükü artırılmaz.
3. Eğitim penceresi, SCT'nin akımın kesildiğini gösteren düşüş anında biter: `end = SCT_CURRENT_CUTOFF`. PZEM'in kapanış gecikmesi beklenmez; mavi PZEM serisinin daha sonra düşmesi pencereyi uzatmaz. Başka bir deyişle pencere, SCT ve PZEM'in birlikte kararlı hale geldiği andan SCT'nin düşmeye başladığı ana kadardır. Bu aralıktaki SCT değerlerinin medyanı o ON çevriminin temsilî SCT değeridir.
4. Aynı eğitim penceresi içinde kalan geçerli PZEM akım okumalarının medyanı ayrıca hesaplanır. PZEM örnek sayısı SCT'den az olabilir; PZEM'e 60 örnek varmış gibi davranılmaz. İki seri aynı pencere sınırını paylaşır, ancak yayın zamanları bire bir eşleştirilmez veya interpolasyon yapılmaz.
5. Her ON çevrimi için tek eğitim çifti kaydedilir: (SCT_cycle_median, PZEM_cycle_median). Çevrim katsayısı adayı K_j = PZEM_cycle_median / SCT_cycle_median olarak hesaplanabilir.
6. Birden fazla ON çevrimi, birbirinden bağımsız tekil yayınlar gibi değil, tekrarlı çevrim gözlemleri olarak değerlendirilir. Çevrimler arası nihai K birleştirme yöntemi ayrıca kararlaştırılacaktır.

### İstatistiksel sınırlar

- Aritmetik ortalama, ilk eğitim temsilî değeri olarak kullanılmayacaktır. Kullanıcı kararıyla merkez kestirici medyandır.
- Medyanın kaç değerden hesaplandığı her iki kaynak için ayrı n_SCT ve n_PZEM alanlarıyla kaydedilir. SCT için 30 saniyelik kararlı aralıkta 500 ms yayınla yaklaşık 60 değer beklenir; bu sayı sabit garanti değil, nominal beklentidir.
- SCT ve PZEM medyanları aynı eğitim penceresinden hesaplanır. Pencere başlangıcı iki akışın da kararlı olduğu daha geç başlangıçtır; pencere bitişi SCT akımının kesildiği andır. PZEM'in gecikmeli kapanışı beklenmez. Yayın zamanları bire bir eşleşmiş kabul edilmez; pencere sınırları ve geçerli örnek sayıları kaydedilir.
- Her ON çevriminin medyanı eğitim çiftidir. Çevrimler arası medyan, ancak çevrim bazlı eğitim çiftleri oluştuktan sonra ayrı bir özet olarak kullanılabilir; ham çevrim çiftlerinin yerini almaz.
- MAD ve diğer yayılım ölçüleri medyanın güvenilirliğini/tekrarlanabilirliğini değerlendirmek için raporlanır; merkez değer yerine geçirilmez.
- PZEM bu proje için pratik referanstır, mutlak ground truth değildir. Geçerli PZEM örnek sayısı için asgari eşik henüz belirlenmemiştir; bu eşik sonuçlara bakıldıktan sonra seçilmeyecektir.
- 500 ms yayın tercihi daha fazla gözlem sağlar; daha fazla örnek bağımsız deney sayısını artırmaz. Tekrarlı ON çevrimleri esas deney birimidir.

**Durum:** Sabit yükle ilk eğitimde medyan tabanlı ON-çevrimi eğitim çifti yöntemi ve pencere mantığı kullanıcı tarafından onaylandı. 500 ms SCT yayın aralığı başlangıç tercihi olarak kabul edildi. Kararlılık tespitinin sayısal eşikleri/yerleşme koşulları, minimum PZEM örnek sayısı ve çevrimler arası nihai K birleştirme yöntemi açık parametrelerdir.

### Sabit yük koşulu — önemli kapsam sınırı

Bu medyan çifti yöntemi **sabit yükle yapılan ilk eğitim/kalibrasyon deneyi** içindir. Tek bir test serisinde yük tipi, fiziksel bağlantı ve çalışma koşulu sabit tutulur; aynı yükün tekrarlanan ON çevrimlerinden SCT–PZEM medyan çiftleri üretilir. Böylece aynı çalışma noktasında ölçüm zincirinin tekrarlanabilirliği ve o nokta için K adayı değerlendirilir.

Farklı güç/akım seviyelerindeki yükler aynı havuzda tek medyana indirgenmez. Daha sonra farklı sabit yük seviyeleri ayrı eğitim grupları olarak ölçülür; her seviyenin ON çevrim medyan çiftleri ve K davranışı kendi içinde değerlendirilir. Katsayının çalışma aralığı boyunca sabit kalıp kalmadığı ancak bu ayrı çalışma noktaları karşılaştırıldıktan sonra söylenebilir. Tek bir sabit yük deneyinden tüm akım aralığına genelleme yapılmaz.