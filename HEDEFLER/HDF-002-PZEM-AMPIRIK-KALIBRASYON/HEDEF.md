# HDF-002 — BERO Kümülatif Öğrenme ve Sahaya Geri Besleme Sistemi

**Durum:** Açık — mimari hedef tanımlandı; ilk uygulama basamağı HA verisini kümülatif biriktirmektir.  
**Açılış tarihi:** 2026-10-11  
**Öncelik:** Önce veri havuzu; ardından masaüstü işleme/öğrenme ve ESP'ye geri besleme.  
**Koruma:** HDF-001 ve ona bağlı tüm kodlar, raporlar, loglar ve deneyler tarihsel kayıt olarak korunur. Mevcut çalışan YAML değiştirilmez.

## 1. Hedef

Proje BERO'yu yalnızca bir sensör kalibrasyon deneyi olarak değil, uçtan uca bir **veri toplama → kümülatif veri havuzu → masaüstünde öğrenme → model karşılaştırma → başarı ölçümü → sahaya geri besleme** sistemi olarak kurmak.

ESP'nin akım hesaplaması veya model eğitmesi zorunlu değildir. ESP mevcut sensörlerden veri/öznitelik üretip ileten uç cihaz olarak kalabilir. Akım tahmini, model seçimi, davranış öğrenme ve model üretme masaüstü Python tarafında yapılabilir. Başarılı ve ESP'nin uygulayabileceği çıktı varsa parametre/fonksiyon ESP'ye aktarılır; aktarım ve geri okuma doğrulanır.

Sensör tipi veya adı veri havuzunun merkezî anahtarı değildir. Tüm sensör verileri ortak veri düzeninde saklanabilir; eğitim ve model karşılaştırması gerektiğinde sensör, kanal, analog koşullandırma zinciri veya çalışma koşuluna göre ayrı gruplarda yürütülür. Farklı sensörlerin katsayılarının otomatik olarak birbirine aktarılacağı varsayılmaz.

## 2. Mimari katmanlar

### Katman 1 — Home Assistant veri biriktirme

**Görev**
- Home Assistant'ta mevcut olan sensör, ADC öznitelikleri ve referans değerlerini okumaya uygun veri kaynağı oluşturmak.
- Zaman damgası, entity/sensör kimliği, ölçüm değeri ve birimi korumak.
- Verileri artımlı ve kümülatif biçimde biriktirmek.
- Veri kaybı, tekrar kayıt ve boşlukları görünür kılmak.

**İlk teslimat budur.** İlk adımda mevcut HA verisinin nerede ve hangi entity'lerde bulunduğu envanterlenir; veri toplama/uzun süreli saklama düzeni kurulur. Yeni donanım testi veya YAML değişikliği bu adımın ön koşulu değildir.

### Katman 2 — Masaüstüne güvenli aktarım ve arşiv

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

### Katman 3 — Kümülatif eğitim verisi

Masaüstü programı tüm tarihsel veriyi okur; yeni veriler geldikçe veri kümesini genişletir. Mümkün olan öznitelikler arasında ADC RMS, ADC STD, MIN, MAX, RANGE, ortalama/medyan, bias, yüzdelikler ve kaynaktaki diğer ölçülebilir alanlar bulunur.

Mevcutsa PZEM akımı, gücü, voltajı ve PF referans etiketleri zaman/ölçüm penceresiyle eşleştirilir. Eşleşme belirsizliği, zaman farkı ve eksik değerler kaydedilir; sessizce uydurma değer doldurulmaz. PZEM bulunmayan örnekler davranış/anomali öğrenmede yine kullanılabilir, fakat PZEM'e karşı denetimli akım başarısı hesabında etiketli örnek sayılmaz.

Tüm sensörler ortak havuzda tutulur. Eğitim sırasında sensör/kanal/koşullandırma kimliği modele özellik olarak verilebilir veya veriler ayrı modellerle işlenebilir. Hangi yaklaşımın daha iyi olduğu deneyle değerlendirilir.

### Katman 4 — Model yarışması

Tek bir model baştan dayatılmaz. Veri miktarı ve niteliği uygunsa şu seçenekler karşılaştırılabilir:
- Global doğrusal model / basit kalibrasyon katsayısı
- Polynomial model
- Bölgesel veya parçalı (piecewise) k katsayıları/fonksiyonlar
- Random Forest
- XGBoost veya benzeri yöntemler (kurulum ve veri desteği uygunsa)
- Davranış profilleri ve gözetimsiz anomali yöntemleri

Basit model, daha karmaşık modelle aynı veya daha iyi bağımsız sonuç veriyorsa tercih edilir. Bölgesel katsayılar yalnızca eğitim hatasını düşürdüğü için seçilmez; her bölgede yeterli örnek ve bağımsız doğrulama aranır. Sensör bazında ayrı eğitim mümkündür; sensör adlarının ortak havuzda bulunması buna engel değildir.

### Katman 5 — Başarı ölçümü ve seçim

PZEM etiketli akım modelleri için raporlanabilecek ölçütler:
- MAE
- RMSE
- Ortalama sapma/bias
- Maksimum mutlak hata
- Yüzde hata (sıfıra yakın değerlerde ayrıca ele alınarak)
- Tanımlanan tolerans içinde kalan örnek oranı

Ön hedef olarak **akım hatası ≤ %10** değerlendirilebilir; bu, kullanıcı tarafından nihai kabul kuralı olarak ayrıca onaylanana kadar öneri niteliğindedir. Sıfıra yakın akımda yüzde hata yerine belirlenmiş mutlak hata/deadband uygulanır; sayısal eşik veri ve uygulama gereksinimi görülmeden uydurulmaz.

Eğitim ve test verileri ayrılır. Mümkün olduğunda aynı ölçüm oturumu/yük koşulunun tekrarları iki tarafa da dağıtılmaz. Uzun süreli öğrenmede yeni günler/oturumlar üzerinde ayrıca değerlendirme yapılır. Bir haftalık veya daha uzun çalışma süresi mümkündür; süre tek başına başarı kanıtı değildir.

### Katman 6 — Davranış ve risk öğrenme

Akım tahmininden bağımsız bir hedef olarak normal davranış örüntüleri öğrenilebilir:
- Bilinen çalışma profillerini tanıma (ör. cihazların çalışma döngüleri)
- Yeni veya alışılmadık örüntüleri işaretleme
- Anomali puanı üretme
- Akım tahmini belirsizken de davranışın olağandışı olup olmadığını raporlama

“Bilinmeyen profil” doğrudan “tehlike” demek değildir. Sistem normal/anormal adayını, güven düzeyini ve gerekçeyi ayırır. Elektriksel güvenlik riski hakkında kesin karar, yalnızca profil benzerliğine dayandırılmaz.

### Katman 7 — ESP'ye geri besleme

Masaüstü, karşılaştırma sonucunda uygun bulunan modelin uygulanabilir fonksiyonunu veya katsayılarını ve sürüm/metadata bilgisini üretir. ESP:
- örnekleri/öznitelikleri toplar ve iletir,
- kendisine gönderilen desteklenen parametre/fonksiyonu uygular,
- mümkün olan sonucu/aktif sürümü geri bildirir.

ESP'nin model eğitmesi veya modeller arasında seçim yapması zorunlu değildir. Masaüstü aktarılabilir bir çıktı üretemezse veya ESP tarafındaki uygulama yolu henüz mevcut değilse bu sınır açıkça raporlanır; aktarım gerçekleşmiş gibi gösterilmez. Her aktarımda gönderilen sürüm ve ESP'den geri okunan sürüm/değer karşılaştırılır. Mevcut YAML korunur; ESP tarafındaki uygulama gerekiyorsa ayrı ve yeni kod sürümü olarak hazırlanır, mevcut çalışan dosyanın üzerine yazılmaz.

## 3. İki masaüstü programı

### Program 1 — BERO Data Collector

**Tek işi veri almak ve güvenli biçimde arşivlemektir.**
- Home Assistant'tan mevcut veriyi/ölçüm entity'lerini okur.
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

Her iki programın kodu tam ve kopyalanabilir olacak; yanında aynı sürüm adına sahip açıklama .md dosyası bulunacaktır. Programlar masaüstünden çalıştırılabilecek şekilde hazırlanır. Gerekli HA adresi/erişim anahtarı gibi ortam ayarları kod içine sabit sır olarak yazılmaz; yerel yapılandırmadan alınır.

## 4. İlk uygulama sırası

1. **GRV-007 — HA veri kaynağı ve kümülatif biriktirme:** Mevcut HA entity ve kayıt yapısını incele; veri şemasını ve artımlı toplama yolunu belirle. İlk teslimat veri biriktirme olmalıdır.
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
