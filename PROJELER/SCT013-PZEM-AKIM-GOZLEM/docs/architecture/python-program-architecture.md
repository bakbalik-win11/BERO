# Python veri hattı mimarisi

**Faz:** Faz 2 — Bulunan kodu PZEM ile eğitmek  
**İlk görev:** [T007 — Home Assistant verisini PC'ye aktarma](../../tasks/T007-python-architecture.md)  
**Durum:** Taslak; 2026-11-06 tarihinde iki bağımsız Python programı ve kullanıcı kontrollü gelen-kutu/arşiv akışı kararlaştırıldı. Fiziksel klasör yolları ve uygulama henüz belirlenmedi.

## Amaç

Home Assistant'tan kullanıcı tarafından dışa aktarılarak PC'deki gelen-kutu klasörüne bırakılan PZEM-004T V3.0 referans akışı ile mevcut SCT ölçüm kodunun entity geçmişlerini kalıcı yerel arşive almak. Bu iş iki bağımsız Python programına ayrılır: Python-1 gelen-kutudaki dosyaları doğrulayıp arşivler; Python-2 yalnız arşivlenmiş veriyi analiz eder. Analiz aşamasında PZEM ve SCT akışları BOOT_ID + EVENT_ID ile paketlenir, kararlılıkları bağımsız belirlenir ve geçerli eşleşen kararlı alanlarda PZEM akımı SCT verisine referans etiketi olur.

## Veri akışının hedef sırası

### Aşama A — Python-1: gelen-kutu ve arşivleme

1. **Kullanıcı bırakır:** Kullanıcı HA History'den aldığı dışa aktarım dosyasını belirlenen gelen-kutu klasörüne kendisi bırakır.
2. **Dosya alımı:** Python-1 gelen-kutudaki yeni dosyayı bulur; HA'ya bağlanmaz ve Recorder veritabanına erişmez.
3. **Doğrulama:** Dosya biçimi, okunabilirlik, kayıt yapısı ve dosya hash'i kontrol edilir. PZEM/SCT entity kayıtları, timestamp ve birimler korunur.
4. **Arşivleme:** Doğrulama başarılıysa kaynak dosya içeriği değiştirilmeden yerel arşivin uygun alt klasörüne taşınır. Gelen-kutu işlenmiş dosya bakımından boşalır.
5. **Hata/tekrar yönetimi:** Doğrulanamayan dosya silinmez; hata/karantina alanında tutulur veya güvenli biçimde gelen-kutuda bırakılır. Aynı hash'e sahip dosya ikinci kez arşivlenmez. Her işlem loglanır.

### Aşama B — Python-2: analiz

6. **İnceleme ve hazırlama:** Python-2 yalnızca Python-1'in arşivine bakar; dosya biçimi, entity_id, birim, timestamp, boşluk, tekrar ve geçersiz state dağılımını raporlar.
7. **Kararlılık:** Her akışın kararlı pencerelerini kendi güncelleme hızına ve gözlenen dağılımına göre belirler.
8. **Eşleştirme:** Aynı BOOT_ID + EVENT_ID paket aralığında iki tarafta da geçerli/kararlı bölge olup olmadığını değerlendirir; geçerli protokolde tanımlanan gerçek örtüşme koşulu ayrıca uygulanır.
9. **Etiketleme:** Geçerli PZEM akımını eşleşen SCT penceresine referans etiketi olarak ekler.
10. **Öğrenme:** Önce K=24.22'yi değerlendirir; veri desteklerse yeni katsayı/model sürümü üretir.

### Klasör kararının sınırı

Gelen-kutu, arşiv, hata/karantina ve log alanları mantıksal rollerdir. Gerçek klasör yolu, klasörlerin fiziksel konumu, arşiv alt klasörleme kuralı ve Python-1'in klasörü tarama/izleme biçimi terminalde birlikte kararlaştırılacaktır. Bu belge henüz fiziksel klasör oluşturulduğunu veya çalışan bir izleyici bulunduğunu iddia etmez.


## Kararlılık ve eşleştirme kuralı (ADR-022 / ADR-023 — geçerli)

**Önce paket kimliği, sonra bağımsız kararlılık analizi.** ADR-019 tarihsel kararındaki timestamp kesişimiyle iki sensör örneğini eşleştirme yaklaşımı ADR-022 ile geçersiz kılınmıştır. TIME alanı da ADR-023 ile olay protokolünden çıkarılmıştır.

1. Modül 3 PZEM akışı, kendi olay kayıtlarıyla; Modül 2 SCT akışı, aldığı aynı olay kayıtlarıyla kendi içinde sıralanır.
2. Her iki akış olay işaretleri arasındaki paket aralıklarına ayrılır.
3. Paket aralıkları yalnız BOOT_ID + EVENT_ID ile eşleştirilir. EVENT_ID tek başına benzersiz değildir.
4. PZEM kararlılığı yalnız PZEM değerlerinden; SCT kararlılığı yalnız SCT değerlerinden bağımsız tespit edilir.
5. Her iki tarafta geçerli ve karşılaştırılabilir kararlı bölge bulunmayan paket eğitim örneği üretmez. Geçiş/yerleşme bölümleri kararlı kabul edilmez.
6. İki modülün ölçüm örnekleri timestamp ile birebir eşleştirilmez; kararlı pencere başlangıç/bitiş timestamp kesişimi de paket eşleştirme şartı değildir.
7. Timestamp/timezone yalnızca aynı modül içindeki ölçüm ve olay kayıtlarının yerel sırasını kurmak, paket sınırlarını belirlemek ve kaynak izini korumak için kullanılır.
8. PZEM akımı geçerli paket aralığındaki SCT kararlı bölgesine proje referans etiketi olur; mutlak ground truth değildir.

Güncel olay biçimi: `BERO_EVT,BOOT_ID=<32 HEX>,EVENT_ID=N,STATE=ON|OFF`. TIME alanı yoktur. Ayrıntı: [ADR-022](../decisions/ADR-022-packet-marker-segmented-training-streams.md) ve [ADR-023](../decisions/ADR-023-event-identity-without-time.md).


## Eğitim akışlarının History'de açık adlandırılması (ADR-027)

Gün içindeki deneyler ve genel gözlem için History'de fiziksel kanal adları `CH1`, `CH2`, `CH3` kullanılır. Birden fazla deney aynı History dışa aktarımında bulunabilir; bunların tümü eğitim verisi değildir.

Bir kod/ölçüm yapılandırması kesinleştikten ve özellikle eğitim verisi alınmasına karar verildikten sonra, ilgili ESPHome/kaynak kodundaki kanal/entity adı küçük bir değişiklikle eğitim işaretli ada çevrilir. Kullanılacak adlar sabittir:

| Eğitim akışı adı | Fiziksel kanal |
|---|---|
| `CH1-E` | CH1 |
| `CH2-E` | CH2 |
| `CH3-E` | CH3 |

`-E` eki yalnız eğitim amacıyla yayınlanan History akışını ayırt eder. Sarım/geçiş sayısı, katsayı, filtre veya hesaplama yöntemi bu adın parçası değildir; gerekiyorsa ilgili deney/eğitim kodunda tanımlanır. Kodda eğitim işareti bulunmayan genel `CH1` / `CH2` / `CH3` akışları otomatik olarak eğitim verisi kabul edilmez.

Python-1 dosyayı, içerik ve entity adlarını değiştirmeden doğrular ve arşivler; kaynak CSV'de `CH1-E`, `CH2-E`, `CH3-E` bulunmasını kabul koşulu yapmaz. Python-2 eğitim hazırlama aşamasında bu üç adı açık eşleme listesi olarak kullanır ve yalnız ilgili eğitim akışını seçer. Eski bir genel deney kaydından eğitim kopyası üretilecekse kaynak arşiv korunur; isimlendirme ve kanal seçimi ayrı türetilmiş kopyada yapılır.

Bu adlandırma, History'de biriken çok sayıdaki deney kaydı arasından yalnızca eğitim amacıyla özellikle işaretlenmiş akışı seçmek içindir. Firmware/HA entity değişikliği kullanıcı tarafından eğitim kaydı başlatılmasına karar verildiğinde yapılır; mevcut çalışan deney kodları kendiliğinden değiştirilmez.


## Şimdilik kesinleştirilmeyenler

- HA'dan PC'ye aktarım yöntemi (API, geçmiş dışa aktarımı veya dosya aktarımı).
- Gerçek entity_id listesi ve kullanılacak PZEM/SCT alanları.
- Kaynak export biçimi ve kayıt boyutu.
- Python dosya/modül sayısı ve çalıştırma biçimi.
- Kararlılık eşikleri, pencere süresi ve eşleştirme toleransı.
- Eğitim/ayrı doğrulama veri bölme yöntemi.

Bu kararlar gerçek HA örnek verisi görülmeden varsayılmayacak.

## Veri koruma kuralları

- Kaynak timestamp, timezone/offset, entity_id, state ve unit korunur.
- PZEM ve SCT güncelleme hızları aynı kabul edilmez; yapay zaman yuvarlama/senkronizasyon yapılmaz.
- -1.0, NaN, timeout ve parse hataları etiketlemeden çıkarılır; ham kaynak kayıt silinmez.
- Sıfır değerler doğrulanmadan otomatik silinmez.
- Her etiketli SCT pencere kaydında gerçek calibration_id bulunur; yoksa uydurulmaz.
- Kaynak dosya hash'i, analiz kodu sürümü ve dışlama özeti sonuçla birlikte saklanır.

## Parçalar ve ilerleme

| ID | Parça | Durum | Görev |
|---|---|---|---|
| PY-01 | Python-1: gelen-kutudan dosya alımı, doğrulama ve arşivleme | BEKLEMEDE | T007 |
| PY-02 | Python-2: arşivlenmiş PZEM/SCT kaynak akışlarını inceleme | BEKLEMEDE | T007 |
| PY-03 | Ayrı kararlılık pencereleri | BEKLEMEDE | T008 |
| PY-04 | Ortak pencere eşleştirme ve etiketleme | BEKLEMEDE | T008 |
| PY-05 | K=24.22 ve model değerlendirme | BEKLEMEDE | T006 |

## İlk teslimat

İlk olarak kullanıcı küçük bir gerçek HA export örneğini gelen-kutu klasörüne bırakır. Python-1 dosyayı doğrulayıp arşive taşır; Python-2 arşivdeki dosyayı okur ve entity, satır, zaman aralığı, birim ve geçersiz değer özetini üretir. Kod, gerçek örnek çıktı/log ve yorum depoya eklenmeden T007 tamamlanmış sayılmaz.

Bu belge hedef mimariyi tanımlar; aktarımın veya Python uygulamasının hazır/çalışır olduğunu iddia etmez.


## Tarihsel ADR-019 notu — güncel uygulamada geçerli değildir

ADR-019 ilk tasarım aşamasında iki akışın timestamp bakımından örtüşen kararlı pencerelerini eşleştirmeyi tarif ediyordu. Bu yaklaşım [ADR-022](../decisions/ADR-022-packet-marker-segmented-training-streams.md) ile paket kimliği önceliğine dönüştürüldü; olay mesajındaki TIME alanı da [ADR-023](../decisions/ADR-023-event-identity-without-time.md) ile kaldırıldı.

Bu nedenle bu mimari belgede geçerli tek yöntem yukarıdaki ADR-022/023 bölümüdür: önce akışları BOOT_ID + EVENT_ID ile paketle, sonra her akışta kararlılığı bağımsız belirle. Timestamp iki modülün örneklerini eşleştirmez. ADR-019 yalnız karar tarihçesi olarak korunur.


## Paket bütünlüğü ve eksik ON/OFF işaretleri (ADR-024 — geçerli karar)

Paketleme her ölçüm akışında bağımsız yapılır:

- Modül 3 PZEM akışı yalnız Modül 3'ün kendi olay kayıtlarıyla; Modül 2 SCT akışı yalnız Modül 2'nin aldığı olay kayıtlarıyla bölümlenir.
- Her akışta ON başlangıcı ve onu izleyen OFF bitişi bulunan aralık tamamlanmış paket adayıdır. Eksik başlangıç/bitiş veya tutarsız olay kimliği/sırası varsa aralık tamamlanmış kabul edilmez.
- Yeni ON, önceki paket kapanmadan gelirse önceki açık aralık eksik/bozuk olarak işaretlenir; yeni ON yeni paket adayı başlatır. BOOT_ID değişiminde açık kalan önceki boot aralığı tamamlanmamış kapatılır.
- EVENT_ID boşlukları, tekrarlar ve beklenmeyen STATE sırası ayrıca raporlanır. Tanı kodları: INCOMPLETE_EVENT, MISSING_ON, MISSING_OFF, EVENT_ID_GAP, DUPLICATE_EVENT, STATE_ORDER_ERROR, BOOT_CHANGED_WITH_OPEN_PACKET.
- İki akışın paketleri yalnız BOOT_ID + EVENT_ID ile eşleştirilir. Her iki tarafta aynı paket aralığı doğrulanmadan eğitim örneği oluşturulmaz. Tek taraftaki tam paket, diğer taraftaki eksik aralığı geçerli yapmaz.
- ON/OFF sınırlarının varlığı kararlılık kanıtı değildir; PZEM ve SCT kararlılığı kendi ölçüm değerlerinden bağımsız belirlenir.

Mevcut Modül 3 → UDP 4210 → Modül 2 aktarımı korunur. Bu karar UDP'yi kaldırmaz, yeni HA helper/merkezi HA mimarisi kurmaz ve olay mesajına TIME alanı eklemez. Güncel protokol ADR-023'teki TIME'sız biçimdir.

**Uygulama durumu:** Bu bölüm kabul kuralıdır. Python kodu, gerçek HA export testi ve örnek çıktı henüz mevcut değildir. Ayrıntı: [ADR-024](../decisions/ADR-024-python-packet-completeness-validation.md).


## Tam ham kayıtta öğrenilmiş SCT modelinin değerlendirilmesi (ADR-025)

Eğitim için PZEM ve SCT akışlarının kendi içlerinde kararlı bulunan uygun alanları eşleştirilir; PZEM bu aşamada proje referansıdır. Eğitim alanları seçilse bile deneyin ham kaydının tamamı korunur. Açılma, kapanma ve geçiş bölgeleri de öğrenilmiş katsayı/model ile ayrıca incelenir.

Tam kayıt değerlendirmesinde Python'a deneyin bilinen ON/OFF koşulu ve yük aralığı verilir (örneğin OFF=0 A, ON yaklaşık 1 A). SCT'nin OFF tabanı, ON seviyesi, geçiş davranışı ve bilinen aralıkla tutarlılığı değerlendirilir. PZEM'in geçişteki ardışık okumaları SCT'nin her örneği için noktasal doğruluk referansı yapılmaz; bu değerlerle tam kayıt üzerinde hata puanı üretilmez. Bilinmeyen ara geçiş akımları uydurulmaz. Sonuç, bilinen deney koşullarına göre SCT davranış/tutarlılık değerlendirmesidir; bağımsız örnek referansı olmadan mutlak doğruluk testi değildir.

Tek katsayı veya Python'ın veriden seçeceği alan bazlı katsayılar ve alan sınırları henüz belirlenmemiştir. Algoritma, en küçük kareler yöntemi ve kabul eşiği bu ADR ile seçilmez. Ayrı SCT üzerinde eğitilmiş modeli çalıştıracak olası Modül 4 fikri ayrı bir gelecek önerisidir.

Ayrıntı: [ADR-025](../decisions/ADR-025-raw-data-sct-model-behavior-validation.md). Python uygulaması ve gerçek ham kayıt çıktısı henüz yoktur.


## İki ayrı öğrenme hedefi ve gelecekteki saha ESP'si

**Birinci ve mevcut hedef — ON akım ölçüm doğruluğu:** PZEM'in kararlı yükte verdiği akım referansıyla SCT'nin aynı kararlı yük koşulunda doğru akımı verebilmesi. Eğitim yalnız ON dönemindeki kararlı SCT/PZEM alanlarının geçerli eşleştirmesinden oluşur. İlk modelin kabulü bu hedefe göre değerlendirilir.

**İkinci ve sonraki hedef — OFF/gürültü ayrımı:** Deney paketlerindeki OFF okumaları ON akım kalibrasyonuna karıştırılmaz. Ancak zaman içinde biriken OFF örnekleri ayrı bir veri havuzunda saklanıp birleştirilebilir. İleride bu veriyle yüksüz/gürültü dağılımı, kapalı durum eşiği veya ayrı bir sınıflandırıcı geliştirilebilir. Gerekirse ayrıca aç-kapa döngüsü olmadan, ölçülen hatta yük yokken uzun süreli yüksüz kayıt alınır. Bu çalışma ilk hedefin parçası değildir.

**Gelecek çalışma mimarisi fikri:** Python, yeni veriler geldikçe analiz/model geliştirme tarafı olabilir; doğrulanmış eşik veya model sürümü ileride sahada hesaplama ve sınıflandırma yapan bir ESP'ye aktarılabilir. Bu ESP, model aktarım yöntemi, güncelleme güvenliği ve çalışma mimarisi henüz tasarlanmamış bir gelecek hedeftir. Mevcut Python hattı veya ESP firmware'i bu kabiliyete sahipmiş gibi kabul edilmez.


## Kalibrasyon referansının niteliği ve model seçimi

Kalibrasyonun amacı yalnız sabit yüklerde çalışacak bir SCT sistemi üretmek değildir. Sabit/kararlı yükler, eğitim sırasında PZEM ve SCT'nin aynı fiziksel koşulu temsil eden ölçüm alanlarını güvenilir biçimde eşleştirmek için kontrollü referans sağlar. PZEM ve SCT'nin fiziksel tepki, örnekleme ve hesaplama yöntemleri farklı olduğundan açılma/kapanma geçişleri veya bu geçişler arasında interpolasyonla üretilen değerler katsayı öğrenme referansına katılmaz.

Eğitim adayı yalnızca:
1. Tam ve geçerli ON/OFF olay paketi,
2. SCT'nin kendi ON ölçüm akışında bağımsız tespit edilmiş kararlı alanı,
3. PZEM'in kendi ON ölçüm akışında bağımsız tespit edilmiş kararlı alanı,
4. Bu iki kararlı alanın zaman bakımından gerçek örtüşmesi
koşullarını sağlayan bölümdür. OFF olayı paketi kapatır; OFF örnekleri ON akım kalibrasyonuna katılmaz.

Model biçimi önceden sabitlenmez. Yeterli farklı yük ve akım aralığı verisi biriktikten sonra tek katsayı, doğrusal hata modeli, polinom veya parçalı/akım alanına özgü doğrusal modeller karşılaştırılabilir. Model seçimi yalnız eğitim uyumuna göre değil, ayrılmış yük/oturum doğrulamasına göre yapılmalıdır. Sabit yükler eğitim referansını üretir; nihai kullanımda değişken canlı yük davranışı ayrıca sınanır.

2026-11-05 ilk 100 W ön karşılaştırması yaklaşık %3.34 merkez farkı göstermiştir; bu ilk gözlemdir, eğitim sonucu veya tüm aralık doğruluğu değildir. K=24.22 korunmuştur. Ayrıntı: [E12 ilk CSV değerlendirmesi](../../experiments/E12-sct-stability-window-and-response/README.md).


## İki programın sınırları ve veri güvenliği (ADR-026 — kabul edildi)

- Python-1 yalnızca kullanıcının gelen-kutu klasörüne bıraktığı dosyaları işler. Home Assistant Recorder veritabanına doğrudan erişmez; HA geçmişini kendiliğinden silmez veya HA'ya yazmaz.
- Başarılı doğrulamadan sonra dosyanın kendisi, içeriği değiştirilmeden arşive taşınır. Kaynak dosyanın hash'i, dosya adı, işlem zamanı, kod sürümü ve doğrulama sonucu loglanır.
- Başarısız veya okunamayan dosya kaybolmaz. Hata/karantina davranışı ve fiziksel klasör yolu terminaldeki klasör tasarımında kesinleştirilecektir.
- Python-2 yalnız arşivden okur; HA'ya bağlanmaz, gelen-kutuyu boşaltmaz ve arşivdeki kaynak dosyayı değiştirmez.
- Gelen-kutu/arşiv/hata/log klasörlerinin gerçek yolu ve alt klasörleme politikası henüz seçilmemiştir.

Ayrıntı: [ADR-026](../decisions/ADR-026-python-inbox-archive-workflow.md). Bu karar mimari sınırı belirler; iki programın kodlandığı veya test edildiği anlamına gelmez.


## Tek kanallı SCT eğitim veri setleri (ADR-027 — kabul edildi)

Üç kanallı test firmware'i ve çok kanallı ham arşiv korunabilir; ancak her eğitim veri seti yalnızca tek SCT kanalını içerir. CH1, CH2 ve CH3 ayrı veri setleri ve ayrı model değerlendirmeleri üretir. Bir kanalda öğrenilen model başka kanala otomatik uygulanmaz. PZEM akımı proje referans akışıdır ve seçilen SCT kanalının kararlı alanlarıyla mevcut BOOT_ID + EVENT_ID paket kuralları içinde eşleştirilir.

Eğitim çıktısı seçilen kanal kimliğini, fiziksel geçiş/sarım bilgisini, kaynak dosya/hash'i, firmware/kod sürümünü, calibration_id bilgisini (gerçekse) ve PZEM referans akışını izlenebilir tutmalıdır. Ham arşiv değiştirilmez; kanal seçimi ayrı türetilmiş çıktıdır.

Kalıcı kanal kimliği `CH1`, `CH2`, `CH3` olmalıdır. Fiziksel geçiş/sarım sayısı (`turn_count`) kanal kimliğine gömülmez; deney/kurulum bazında değişebilir metadata olarak tutulur. Depodaki mevcut 1/4/3 geçiş değerleri yalnız mevcut kayıtlı durumu gösterir. Değişiklik olduğunda yeni deney kayıtları yeni `turn_count` değerini taşır; geçmiş kayıtlar değiştirilmez. `CH1-1T` benzeri birleşik adlar kalıcı kanal veya eğitim seti anahtarı olarak kullanılmaz.

Ayrıntı: [ADR-027](../decisions/ADR-027-single-channel-training-datasets.md).
