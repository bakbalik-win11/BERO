# HDF-002 — BERO Kümülatif Öğrenme ve Sahaya Geri Besleme Sistemi

**Durum:** Açık — mimari hedef tanımlandı; ilk uygulama basamağı HA verisini kümülatif biriktirmektir.  
**Açılış tarihi:** 2026-10-11  
**Öncelik:** Önce veri havuzu; ardından masaüstü işleme/öğrenme ve ESP'ye geri besleme.  
**Koruma:** HDF-001 ve ona bağlı tüm kodlar, raporlar, loglar ve deneyler tarihsel kayıt olarak korunur. Mevcut çalışan YAML değiştirilmez.

## 1. Hedef

Proje BERO'yu yalnızca bir sensör kalibrasyon deneyi olarak değil, uçtan uca bir **veri toplama → kümülatif veri havuzu → masaüstünde öğrenme → model karşılaştırma → başarı ölçümü → sahaya geri besleme** sistemi olarak kurmak.

**Öznitelik/veri ESP'si:** Sensörden mümkün olan en kaliteli sinyali, Python'ın sonradan öğrenebilmesi için en uygun veri biçiminde toplar; pencere başına RMS, STD, MIN, MAX, RANGE, BIAS ve elde edilebilen diğer öznitelikleri HA'ya gönderir. Başlangıç penceresi 1000 örnektir; kalite için uygun örnekleme hızı ve pencere süresi deneyimle değil, mevcut sinyal/veri kayıtları üzerinden değerlendirilir. **1000 ham örneğin kendisi normal akışta HA'ya gönderilmek zorunda değildir; temel veri ürünü öznitelik kaydıdır.** Ham örnekler yalnızca tanılama gerektiğinde ayrı tutulabilir. Bu ESP akım hesaplamaz, kalibrasyon yapmaz, model seçmez, bölgesel k üretmez ve öğrenmez. Python masaüstü tarafı veriden öğrenir ve modeller üretir. Başarılı ve uygulanabilir çıktı varsa parametre/fonksiyon bir ESP'ye geri aktarılabilir; aktarım ve geri okuma doğrulanır.

**Akım ölçen ESP:** Ayrı bir ESP, kendi örnekleme/hesaplama hızında klasik veya kalibre edilmiş formüllerle akımı hesaplayabilir ve hesaplanan akımı HA'ya ayrı bir ölçüm olarak gönderebilir. Bu ESP'nin işi öğrenme değildir; formülü uygular. Python'ın öğrendiği modelle aynı şey olduğu varsayılmaz. İki ESP'nin sonuçları HA/Python tarafında karşılaştırılabilir.

Sensör tipi veya adı veri havuzunun merkezî anahtarı değildir. Tüm sensör verileri ortak veri düzeninde saklanabilir; eğitim ve model karşılaştırması gerektiğinde sensör, kanal, analog koşullandırma zinciri veya çalışma koşuluna göre ayrı gruplarda yürütülür. Farklı sensörlerin katsayılarının otomatik olarak birbirine aktarılacağı varsayılmaz.

## 2. Mimari katmanlar

### Katman 1A — Öznitelik/veri ESP'si

- Sensörlerden hızlı örnekleme yap.
- Başlangıç ölçüm penceresi hedefi 1000 örnektir.
- Pencere başına RMS, STD, MIN, MAX, RANGE, BIAS ve mevcut diğer anlamlı öznitelikleri üret.
- Özniteliklerle birlikte zaman damgası, pencere süresi, kanal/entity kimliği ve geçerli örnek sayısı gibi kalite alanlarını ilet.
- Normal akışta 1000 ham örneği saklamak zorunlu değildir; öznitelik kaydı saklanır.
- Akım hesaplama, kalibrasyon ve model seçimi ESP'nin görevi değildir.

### Katman 2 — Home Assistant veri biriktirme

**Görev**
- Home Assistant'ta mevcut olan sensör, ADC öznitelikleri ve referans değerlerini okumaya uygun veri kaynağı oluşturmak.
- Zaman damgası, entity/sensör kimliği, ölçüm değeri ve birimi korumak.
- Verileri artımlı ve kümülatif biçimde biriktirmek.
- Veri kaybı, tekrar kayıt ve boşlukları görünür kılmak.

**İlk teslimat budur.** İlk adımda mevcut HA verisinin nerede ve hangi entity'lerde bulunduğu envanterlenir; veri toplama/uzun süreli saklama düzeni kurulur. Yeni donanım testi veya YAML değişikliği bu adımın ön koşulu değildir.

### Katman 3 — Masaüstüne güvenli aktarım ve arşiv

**Görev**
- HA'daki yeni kayıtları masaüstüne aktarmak.
- Masaüstünde kalıcı veri havuzuna eklemek.
- Dosya/ölçüm kimliği veya zaman aralığıyla mükerrer kayıtları önlemek.
- Aktarımın bütünlüğünü (kayıt sayısı, aralık, alanlar ve mümkünse checksum) doğrulamak.
- Aktarım doğrulanmadan HA'daki kaynak kayıtları silmemek.

Kullanıcının “HA'yı boşalt” isteği, yalnızca aktarımı doğrulanmış ve tekrar alınabilir kayıtların HA çalışma alanından temizlenmesi anlamındadır. Bu işlem tarihsel arşivi silmez. Ham veri masaüstündeki kalıcı arşivde korunur; temizlik sınırı açıkça yapılandırılır ve yanlışlıkla başka HA geçmişini silmez.

Önerilen masaüstü havuzu:

```text
BERO_DATASET/
  raw/
    2026/
    2027/
    ...
  normalized/
  manifests/
  models/
  reports/
  archive/
```

Ham kaynak kayıtları değiştirilmez. Normalleştirilmiş/eşleştirilmiş veri ve model çıktıları ayrı dosyalarda tutulur.

### Katman 4 — Kümülatif eğitim verisi

Masaüstü programı tüm tarihsel veriyi okur; yeni veriler geldikçe veri kümesini genişletir. Mümkün olan öznitelikler arasında ADC RMS, ADC STD, MIN, MAX, RANGE, ortalama/medyan, bias, yüzdelikler ve kaynaktaki diğer ölçülebilir alanlar bulunur.

Mevcutsa PZEM akımı, gücü, voltajı ve PF referans etiketleri zaman/ölçüm penceresiyle eşleştirilir. Eşleşme belirsizliği, zaman farkı ve eksik değerler kaydedilir; sessizce uydurma değer doldurulmaz. PZEM bulunmayan örnekler davranış/anomali öğrenmede yine kullanılabilir, fakat PZEM'e karşı denetimli akım başarısı hesabında etiketli örnek sayılmaz.

Tüm sensörler ortak havuzda tutulur. Eğitim sırasında sensör/kanal/koşullandırma kimliği modele özellik olarak verilebilir veya veriler ayrı modellerle işlenebilir. Hangi yaklaşımın daha iyi olduğu deneyle değerlendirilir.

### Katman 5 — Model yarışması

Tek bir model baştan dayatılmaz. Veri miktarı ve niteliği uygunsa şu seçenekler karşılaştırılabilir:
- Global doğrusal model / basit kalibrasyon katsayısı
- Polynomial model
- Bölgesel veya parçalı (piecewise) k katsayıları/fonksiyonlar
- Random Forest
- XGBoost veya benzeri yöntemler (kurulum ve veri desteği uygunsa)
- Davranış profilleri ve gözetimsiz anomali yöntemleri

Basit model, daha karmaşık modelle aynı veya daha iyi bağımsız sonuç veriyorsa tercih edilir. Bölgesel katsayılar yalnızca eğitim hatasını düşürdüğü için seçilmez; her bölgede yeterli örnek ve bağımsız doğrulama aranır. Sensör bazında ayrı eğitim mümkündür; sensör adlarının ortak havuzda bulunması buna engel değildir.

### Katman 6 — Başarı ölçümü ve seçim

PZEM etiketli akım modelleri için raporlanabilecek ölçütler:
- MAE
- RMSE
- Ortalama sapma/bias
- Maksimum mutlak hata
- Yüzde hata (sıfıra yakın değerlerde ayrıca ele alınarak)
- Tanımlanan tolerans içinde kalan örnek oranı

Ön hedef olarak **akım hatası ≤ %10** değerlendirilebilir; bu, kullanıcı tarafından nihai kabul kuralı olarak ayrıca onaylanana kadar öneri niteliğindedir. Sıfıra yakın akımda yüzde hata yerine belirlenmiş mutlak hata/deadband uygulanır; sayısal eşik veri ve uygulama gereksinimi görülmeden uydurulmaz.

Eğitim ve test verileri ayrılır. Mümkün olduğunda aynı ölçüm oturumu/yük koşulunun tekrarları iki tarafa da dağıtılmaz. Uzun süreli öğrenmede yeni günler/oturumlar üzerinde ayrıca değerlendirme yapılır. Bir haftalık veya daha uzun çalışma süresi mümkündür; süre tek başına başarı kanıtı değildir.

### Katman 7 — Davranış ve risk öğrenme

Akım tahmininden bağımsız bir hedef olarak normal davranış örüntüleri öğrenilebilir:
- Bilinen çalışma profillerini tanıma (ör. cihazların çalışma döngüleri)
- Yeni veya alışılmadık örüntüleri işaretleme
- Anomali puanı üretme
- Akım tahmini belirsizken de davranışın olağandışı olup olmadığını raporlama

“Bilinmeyen profil” doğrudan “tehlike” demek değildir. Sistem normal/anormal adayını, güven düzeyini ve gerekçeyi ayırır. Elektriksel güvenlik riski hakkında kesin karar, yalnızca profil benzerliğine dayandırılmaz.

### Katman 8 — ESP'ye geri besleme

Masaüstü, karşılaştırma sonucunda uygun bulunan modelin uygulanabilir fonksiyonunu veya katsayılarını ve sürüm/metadata bilgisini üretir. ESP:
- örnekleri/öznitelikleri toplar ve iletir,
- kendisine gönderilen desteklenen parametre/fonksiyonu uygular,
- mümkün olan sonucu/aktif sürümü geri bildirir.

ESP'nin model eğitmesi veya modeller arasında seçim yapması zorunlu değildir. Masaüstü aktarılabilir bir çıktı üretemezse veya ESP tarafındaki uygulama yolu henüz mevcut değilse bu sınır açıkça raporlanır; aktarım gerçekleşmiş gibi gösterilmez. Her aktarımda gönderilen sürüm ve ESP'den geri okunan sürüm/değer karşılaştırılır. Mevcut YAML korunur; ESP tarafındaki uygulama gerekiyorsa ayrı ve yeni kod sürümü olarak hazırlanır, mevcut çalışan dosyanın üzerine yazılmaz.

## 3. İki masaüstü programı

### Program 1 — BERO Data Collector

**Tek işi veri almak ve güvenli biçimde arşivlemektir.**
- Home Assistant'ta birikmiş sensör özniteliklerini ve mevcut PZEM referanslarını okur.
- Yeni kayıtları masaüstündeki kümülatif havuza ekler.
- Zaman damgası, entity/sensör kimliği, birim ve değerleri korur.
- Mükerrer kayıtları ve eksik aralıkları raporlar.
- Aktarım doğrulanınca yalnızca yapılandırılmış HA çalışma alanını temizleyebilir.
- Ham masaüstü arşivini silmez veya yeniden yazmaz.

### Program 2 — BERO Trainer

**Tek işi veriyi işlemek, modelleri karşılaştırmak ve aktarılabilir çıktıyı hazırlamaktır.**
- Kümülatif havuzun tüm uygun verisini okur.
- Temizleme/eşleştirme adımlarını ayrı türetilmiş dosyalara yazar.
- Akım/PZEM modellerini ve davranış/anomali modellerini ayrı hedefler olarak değerlendirir.
- Gerekirse sensör/kanal/bölge bazlı modeller ve k katsayıları üretir.
- Başarı tablosu, grafikler, hata örnekleri ve model sürüm raporu çıkarır.
- En iyi doğrulanmış modeli seçer ve ESP'ye aktarılacak dosyayı üretir.
- ESP'ye aktarım/geri okuma adımının sonucunu kaydeder.

Trainer, yeni veri geldikçe yeniden çalıştırılabilir; istenirse uzun süreli/planlı çalışma ile bir gün, bir hafta veya daha uzun dönem boyunca yeni veriyi kümülatif havuza ekleyip modelleri yeniden karşılaştırabilir. Eğitim süresi kendi başına başarı kanıtı değildir. Her iki programın kodu tam ve kopyalanabilir olacak; yanında aynı sürüm adına sahip açıklama .md dosyası bulunacaktır. Programlar masaüstünden çalıştırılabilecek şekilde hazırlanır. Gerekli HA adresi/erişim anahtarı gibi ortam ayarları kod içine sabit sır olarak yazılmaz; yerel yapılandırmadan alınır.

## 4. İlk uygulama sırası

1. **GRV-007 — ESP öznitelikleri ve HA veri biriktirme:** Mevcut ESP'nin ürettiği 1000 örnek pencere özelliklerini ve HA entity/kayıt yapısını incele; ham örnek yerine öznitelik kayıtlarının kümülatif birikmesini esas al. İlk teslimat veri biriktirme olmalıdır.
2. **GRV-008 — Masaüstü Collector ve güvenli aktarım/temizlik:** Veriyi BERO_DATASET havuzuna al; aktarımı doğrulamadan kaynak çalışma alanını temizleme.
3. **GRV-009 — Trainer ve model yarışması:** Mevcut tüm veriyi işle; PZEM etiketli akım modellerini ve davranış modellerini ayrı değerlendir; sonuçları kaydet.
4. **GRV-010 — Model çıktısı ve ESP geri besleme:** Seçilen fonksiyon/katsayıyı yeni sürüm olarak hazırla; desteklenen aktarım yolunu uygula; ESP'den geri okuyup doğrula.

Basamaklar arasında mevcut YAML'ı tekrar tekrar test etmeyi zorunlu kılan bir kapı yoktur. Mevcut kayıtlar önce kullanılır; veri eksikliği yalnızca ilgili alan/sonuç için belirtilir. Yeni fiziksel ölçüm, ancak modelin belirli bir belirsizliği çözmek için gerçekten gerektiği gösterilirse ayrı bir karar olarak ele alınır.

## 5. Kayıt ve koruma ilkeleri

- HDF-001 ve eski görevlerin kodu, logu, raporu ve ölçümü korunur.
- Ham veri hiçbir zaman normalleştirilmiş veriyle değiştirilmez.
- Yeni model, katsayılar ve raporlar sürüm/tarih bilgisiyle ayrı saklanır.
- Sensör isimleri veri havuzunu parçalamak için zorunlu değildir; ancak kaynak entity/kanal kimliği ve fiziksel ölçüm zinciri izlenebilirlik için korunur.
- Modelin eğitimde iyi sonuç vermesi, sahada doğrulandığı anlamına gelmez.
- Python'da model kurma, mevcut YAML'ın korunmasına engel değildir.
- Gerçek HA entity eşlemesi, API/Recorder erişimi ve ESP'nin desteklediği geri besleme yolu mevcut yapı incelenerek belirlenir; bunlar varsayılarak başarılı ilan edilmez.

## 6. HDF-001 ile ilişki

HDF-001 — Akımı Okuma, geçmiş denemeleri ve kanıtlarıyla birlikte tarihsel temel olarak korunur. HDF-002 onun dosyalarını yeniden başlatmaz veya üzerine yazmaz. HDF-002'nin odağı tek başına bir sensörün doğruluğunu tekrar tekrar sınamak değil, eldeki ve gelecekte birikecek veriden masaüstü öğrenme/karşılaştırma hattı kurmaktır.

## 7. Güncel durum

**Açık — hedef mimarisi kaydedildi.** İlk iş HA verisini kümülatif biriktirmektir. Collector, Trainer, model eğitimi veya ESP geri beslemesi henüz bu hedef belgesinde uygulanmış/başarılı olarak iddia edilmemektedir.


## 8. Öznitelik odaklı veri ilkesi (2026-10-11 ek açıklama)

Veri zincirinin standart ürünü 1000 ham ADC örneği değil, o pencereden çıkarılan anlamlı özniteliklerdir. Temel akış:

```text
Sensör → ESP → 1000 örnek → öznitelikler (RMS, STD, MIN, MAX, RANGE, BIAS, ...)
       → Home Assistant → kümülatif veri gölü → Python → öğrenme/model yarışması
       → başarı ölçümü → sonuç/model çıktısı → gerekiyorsa ESP'ye geri besleme
```

Özniteliklerin hangi sensörden geldiği kayıtta izlenebilir olmalıdır; ancak sensör adı, tüm veriyi ortak havuzda saklamaya engel değildir. Python bütün geçmiş veriyi birlikte okuyabilir; ardından bütünleşik veya sensör/kanal bazında modelleri karşılaştırabilir. Örnek rapor satırları (ör. “RMS MAE %18; RMS+STD %11; RMS+STD+RANGE %7”) yalnızca rapor biçimini anlatan örneklerdir, ölçülmüş BERO sonuçları değildir.

Hedefin merkezi sensör modelini kanıtlamak için sürekli aynı test döngüsünü tekrarlamak değil; mevcut özniteliklerden başlayarak modelleri fiilen denemek ve yalnızca sonuçların gösterdiği belirsizliklerde ölçüm zincirini tekrar incelemektir.


## 9. İki ESP rolünü birbirinden ayırma (2026-10-11 ek karar)

BERO mimarisinde iki ayrı uç cihaz rolü bulunabilir:

1. **Öznitelik/veri ESP'si:** Sinyal kalitesini ve öğrenme için uygun öznitelik üretimini önceler. Pencere örneklerini alır, öznitelikleri çıkarır ve HA'ya iletir. Akım hesaplamak zorunda değildir. Masaüstü Python bu veriden kalibrasyon ve davranış modellerini öğrenir.
2. **Formülle akım ölçen ESP:** Ayrı bir cihaz olarak klasik veya kalibre edilmiş formüllerle akımı hesaplayabilir; örnekleme hızı ve hesaplama yöntemi öznitelik ESP'sinden farklı/yavaş olabilir. Sonucu HA'ya ayrı bir entity/ölçüm olarak yazar.

Bu iki rol birbirini dışlamaz. HA, öznitelik ESP'sinden gelen özellikleri, formül ESP'sinin akım sonucunu ve varsa PZEM referansını birlikte biriktirir. Python bunları zaman ve kaynak kimliğiyle eşleştirerek hem model öğreniminde hem karşılaştırmada kullanabilir. Formül ESP'sinin akım sonucu tek başına referans/ground truth kabul edilmez; PZEM referansı varsa ayrı etiket olarak korunur.

Öznitelik ESP'si için başarı, öğrenmeye elverişli ve kaliteli veri üretmesidir; formül ESP'si için başarı, hesapladığı akımın bağımsız referansa yakınlığıdır. Bu iki başarı ölçütü ayrı raporlanır.

## 10. İlk uygulama için güncel karar — paketlenmiş öznitelik ve ham veri ayrımı (2026-10-11)

Bu bölüm, önceki olası mimari seçenekleri ilk uygulama sırası açısından netleştirir. **MCP'li/MCP'siz zincirlerin hangisinin daha iyi olduğuna karar vermek sonraya bırakılır.** Önce mevcut ESP'ler ve Mac Mini arasındaki veri toplama hattı çalıştırılır; yeni bir MCP karşılaştırma döngüsü açılmaz.

### ESP32-D1 — öznitelik paketini üret ve gönder
- Hızlı ve sağlıklı örnekleme yapar.
- Başlangıçta 1000 örneklik pencerelerden RMS, STD, MIN, MAX, RANGE, BIAS ve desteklenen diğer öznitelikleri çıkarır.
- Pencere sonuçlarını kimlik, sıra numarası, zaman bilgisi ve örnek sayısıyla paketler.
- Paketi RS485 Modbus üzerinden Mac Mini'ye sunar.
- Bu rolde ham örneklerin tamamını sürekli aktarmak zorunda değildir.

### ESP32-D2 — ham örnekleri üret ve gönder
- Kendi ADC zincirinden ham örnek pencerelerini toplar.
- Ham kayıtları mümkün olduğunca kayıpsız ve sıra bilgisi korunmuş biçimde Mac Mini'ye aktarılabilir hâle getirir.
- Ham örnekler, daha sonra RMS dışındaki öznitelikleri veya yeni analiz yöntemlerini denemek için tarihsel arşivde korunur.
- Ham pencere ile aynı döneme ait öznitelik/PZEM kayıtları varsa zaman ve kaynak bilgisiyle eşleştirilebilir.

D1 ve D2'nin bu görevleri ilk veri hattını kurmak için seçilmiş **iş bölümü**dür; MCP'nin nihai olarak kullanılacağı veya eleneceği kararı değildir. Gerekirse roller ileride değiştirilebilir; geçmiş dosyalar ve kayıtlar değiştirilmez.

### ESP32-E — diğer sensörler ve ayrı deney hattı
- ACS ve diğer sensörlerden veri toplayarak paralel veri/model deneylerine katılabilir.
- E'nin daha sonra Python tarafından seçilmiş ve bağımsız veride doğrulanmış bir akım fonksiyonunu uygulaması mümkündür; ilk veri toplama basamağının ön koşulu değildir.

### Mac Mini — ortak veri merkezi
Üç ESP, RS485 Modbus hattında ayrı cihaz adresleriyle çalışır; Mac Mini master olarak cihazları sorgular ve kayıtları dosyalara yazar. Her kayıt en azından kaynak ESP, fiziksel sensör/kanal, sıra numarası, zaman bilgisi ve veri türünü belirtmelidir. Modbus üzerinden taşınan pencere/öznitelik kayıtlarıyla ham örnek kayıtları ayrı sınıflarda saklanır. PZEM kendi ölçüm zamanıyla ayrı kaynak olarak kaydedilebilir; yalnızca HA'ya yakın zamanda yazılması aynı anda ölçüldüğünü kanıtlamaz.

Önerilen arşiv sınıfları:
- **Öznitelik akışı:** sürekli ve daha küçük kayıtlar.
- **Ham örnek akışı:** D2'nin ham pencereleri ve ileride belirlenen seyrek tanılama pencereleri.
- **Referans akışı:** PZEM değerleri ve kendi zaman damgaları.
- **Model/sonuç geçmişi:** eğitim verisi sürümleri, model sürümleri, metrikler ve raporlar.

### Başarı ölçütü
Akım modeli değerlendirmesinde kullanıcının daha önce belirlediği **±%4 kabul bandı** korunur. Önceki bölümde geçen %10 değeri bu ölçütün yerine geçmez; ±%4 nihai değerlendirme bandı olarak esas alınır. Sıfıra yakın akımda yüzde sapmanın matematiksel olarak anlamlı olmadığı bölge için ayrı bir mutlak hata/deadband kuralı ancak açıkça tanımlanarak eklenebilir; mevcut ±%4 ölçütü sessizce değiştirilmez.

### İlk somut iş
Yeni donanım deneyi veya MCP tartışması değil; mevcut USB–Mac veri yakalama çalışmasını temel alarak Mac Mini'de kayıt dosyalarını güvenilir biçimde yazan hattı ilerletmek, ardından aynı arşiv yaklaşımını RS485 Modbus kaynağına uyarlamaktır. Eski kodlar, YAML, loglar ve CSV'ler korunur; yeni sürümler yeni dosya adlarıyla eklenir.
