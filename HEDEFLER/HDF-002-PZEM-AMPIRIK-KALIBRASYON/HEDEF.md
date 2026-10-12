# HDF-002 — Ölçüm Karakterini Öğrenmek, Gerçek Dalgayı Yakalamak ve Akımı ESP'de Hesaplamak

**Durum:** Açık — hedef mimarisi ve çalışma zinciri tanımlanıyor; donanım kurulumunun, yeni deneylerin, model başarısının veya ±%4 doğruluğun tamamlandığı iddia edilmiyor.  
**Güncelleme:** 2026-10-12  
**Önceki hedef:** HDF-001 / GRV-001 geçmiş çalışmadır. Mevcut kodlar, loglar ve tecrübeler yeniden kullanılacak; eski kayıtlar silinmeyecek veya üzerine yazılmayacak.

## 1. Nihai hedef

BERO sahasına taşındığında amaç, **tek bir ESP'nin SCT + BIAS sinyalinden akımı gerçek zamanlı hesaplaması ve hesaplanan akımı Home Assistant'a/sisteme sunmasıdır.** Bu ESP, masaüstünde eğitilmiş ve doğrulanmış bir modelin küçük, sahada çalışabilir karşılığı gibi davranacaktır.

Ayrı Modbus PZEM donanımı ölçüm ve doğrulama referansı olarak kalır. Nihai SCT ESP'sinin PZEM'e sürekli bağımlı olması şart değildir. Gerilim (V) ve güç faktörü (PF) gibi PZEM verileri ancak modelin bağımsız testlerdeki başarımını anlamlı ölçüde iyileştirdiği gösterilirse modele girdi olarak eklenir. Öncelik, SCT + BIAS ile yeterli başarımı sağlayan en sade modeldir.

**Pratik hedef:** PZEM referansına göre yaklaşık ±%4 bağıl akım hatasına ulaşmayı araştırmak. Bu bir hedef olup doğrulanmış sonuç değildir. Sıfıra yakın akımda bağıl hata tek başına uygun olmadığından mutlak amper hatası da raporlanır.

## 2. Mimari — ayrı görevler, ayrı beslemeler

Planlanan ilk altyapı beş ESP işlevinden oluşur:

1. **SCT ölçüm ESP #1:** 1T SCT + kendisine ait BIAS ölçümü.
2. **SCT ölçüm ESP #2:** 2T SCT + kendisine ait BIAS ölçümü.
3. **SCT ölçüm ESP #3:** 3T yerine seçilecek/değiştirilecek SCT + kendisine ait BIAS ölçümü.
4. **PZEM ESP:** Ayrı Modbus PZEM donanımından ölçüm verilerini okur; akım, gerilim ve PF değerlerini HA'ya aktarır.
5. **Zamanlayıcı/kontrol ESP:** Solid-state röleyi belirlenen sabit aralıklarla açıp kapatır ve kontrol denemelerinin kayıtlarını tutar.

Bu beşli, başlangıç altyapısı ve veri üretme düzenidir. Nihai hedefin mutlaka beş ESP ile tamamlanması gerekmez; model geliştirme sırasında birden fazla SCT zinciri kullanılabilir, son saha çözümü için tek ölçüm ESP'si hedeflenir.

### 2.1 Besleme ve sinyal sınırı

- ESP'lerin beslemeleri ölçüm kanallarından beslenmeyecektir; ESP beslemesi ve analog ölçüm kanalı ayrı işlevlerdir.
- SCT/BIAS/ADC devresinin gerektirdiği sinyal referansı ve GND bağlantıları elektriksel tasarımda doğru biçimde kurulacaktır. Beslemeleri ayırmak, sinyal referansını gelişigüzel kaldırmak anlamına gelmez.
- PZEM kendi ayrı donanım ve okuma zincirinde kalır.
- Solid-state rölenin anahtarladığı devre ve elektriksel sınırlar fiziksel bağlantı aşamasında açıkça kaydedilir. Rölenin aç/kapa yapması ESP ölçüm zamanlamasının yerine geçmez; yalnızca planlanan kontrol/kayıt penceresini veya tasarımda belirlenen devreyi yönetir.
- Her donanım değişikliği, bağlantı koşulları ve ölçüm sonuçları tarihli deneme kaydıyla belgelenir.

## 3. Görev 1 — Fiziksel altyapı ve deneme kayıtları

İlk iş; üç SCT + BIAS ölçüm zincirini, ayrı PZEM okuma zincirini ve sabit aralıkla çalışan solid-state röle kontrolünü fiziksel olarak kurmak ve kayıt altına almaktır.

- Beslemeler ve sinyal bağlantıları ayrı ayrı kontrol edilir.
- Her ESP'nin hangi sensör/kanala bağlı olduğu açıkça kaydedilir.
- Kullanılan kod sürümü, derleme sonucu, gerçek cihaz logları, ölçülen değerler, hata ve değişiklikler deneme kaydına eklenir.
- Başarısız denemeler de saklanır; önceki çalışan kodun üzerine yazılmaz.
- Bu aşama tamamlandı diye dalga kalitesi veya akım doğruluğu varsayılmaz.

## 4. Görev 2 — En kaliteli SCT dalga okuma yöntemi

Amaç, yalnızca çok sayıda örnek üretmek değil, SCT dalgasının biçimini, genliğini ve değişimini doğru temsil eden kaliteli ham veri elde etmektir.

İncelenecek noktalar:

- Dalga biçimini ve tepe noktalarını temsil etmeye yeterli gerçek örnekleme hızı.
- Örnekler arası zaman aralığı ve zamanlama düzenliliği.
- ADC çözünürlüğü, gürültü, kırpılma/saturasyon ve analog giriş devresinin etkisi.
- SCT ile BIAS verisinin ilişkisinin korunması.
- Wi-Fi/HA aktarımının örnekleme döngüsünü bozmaması ve örnek kaybına neden olmaması.
- Gerçek örnekleme hızı ve veri kaybı ölçülmeden update_interval ayarının gerçekleşmiş örnekleme hızı sayılmaması.

Önce GRV-004, GRV-005 ve HDF-001/GRV-001 içindeki kodlar, loglar ve deney tecrübeleri okunur. Var olan kanıt yeterliyse aynı deney tekrarlanmaz. Gerekirse yalnızca mevcut kayıtlarla yanıtlanamayan soruya yönelik küçük doğrulama yapılır.

Tercih edilen veri yolu: SCT ve BIAS ham örneklerini düzenli toplamak, örnek sırasını ve zaman bilgisini korumak, veriyi paketler hâlinde HA'ya aktarmak. Standart ESPHome ADC güncelleme aralığı tek başına kaliteli ve düzenli dalga örneklemesini kanıtlamaz. Ham ADC kodu ile voltaj çıktısı birbirinden açıkça ayrılır.

## 5. HA, ham veri ve masaüstüne güvenli aktarım

SCT ölçüm ESP'leri ve PZEM ESP verileri Home Assistant'a aktarılır. HA, yüksek hızlı dalganın tek tek sensör geçmişi kayıtlarına zorla dönüştürüldüğü varsayılan çözüm değildir; ham örneklerin uygun paketleme ve saklama yolu ayrıca doğrulanır.

Ham veri, değiştirilmemiş kaynak kayıt olarak korunur. Mantıksal arşiv bölümleri:
- raw: değiştirilmemiş ham SCT/BIAS ve PZEM kayıtları;
- validated: aktarım bütünlüğü kontrol edilmiş kayıtlar;
- regions: dalga içindeki aday/kararlı bölgelerin sınırları ve özellikleri;
- labeled: onaylanmış etiketli bölgeler;
- datasets: birleştirilmiş, sürümlü veri kümeleri;
- models: formül/model sürümleri ve parametreleri;
- validation: bağımsız test ve PZEM karşılaştırma sonuçları;
- reports: işlem günlükleri ve raporlar.

Bu isimler hedef arşiv düzenini anlatır; klasörlerin veya aktarımın çalışır durumda kurulduğu anlamına gelmez.

## 6. Python 1 — HA'dan masaüstüne taşıma, doğrulama ve güvenli silme

Python 1 masaüstünde tıkla-çalıştır biçiminde çalışır.

1. HA'da yeni oluşan verileri bulur ve alır.
2. Aktarım kapsamını, dosya yapısını, satır/kayıt sayılarını ve mümkün olduğunda sağlama toplamını kontrol eder.
3. Veriyi masaüstündeki/Mac'teki kalıcı arşive yazar.
4. Yazılan dosyayı yeniden okuyarak kaydın gerçekten mevcut ve bütün olduğunu doğrular.
5. Ancak bu doğrulama başarılı olunca, yalnızca doğrulanan aktarım kapsamındaki HA kopyasını siler.
6. Aktarım, doğrulama veya kalıcı yazma başarısız olursa kaynak veriyi silmez; hata ve işlem sonucu raporlanır.
7. Yeniden çalıştırma durumunda aynı kayıtların kontrolsüz çoğaltılmasını ve henüz aktarılmamış kayıtların silinmesini önler.

Ham kaynak kaydı değiştirilmez. Python 1 akım hesaplamaz veya bölgeleri etiketlemez; güvenilir veri taşıma ve arşivleme sorumluluğunu üstlenir.

## 7. Python 2 — SCT dalgasında kararlı bölgeleri bulma ve etiketleme

Python 2 masaüstünde tıkla-çalıştır biçiminde çalışır. Görevi, SCT dalga kaydından kararlı akım bölgelerini bulmak ve güvenilir referansla etiketlemektir.

### 7.1 Aç/kapa pencereleri ve kararlı bölge

Sabit aralıklarla aç/kapa kontrolü, kayıt pencereleri üretmek için kullanılabilir. Buradaki amaç PZEM ile zaman damgası eşlemek değildir. Kayıt penceresinin içindeki SCT dalgasından kararlı genlik bölgeleri seçilir; yük açılma/kapanma geçişleri model eğitimine alınmaz.

Pencerenin uzunluğu, dalganın kalitesi ve kararlı bölgeyi bulmaya yetecek veriyle belirlenir. 1000 örnek gibi sabit bir örnek sayısı nihai hedef değildir.

### 7.2 “Aynı akım/genlik” kararını verme

Hangi SCT genlik veya dalga özelliği aralığının aynı akım seviyesini temsil edeceği baştan keyfî bir sabit olarak seçilmez. Python 2, gerçek etiketli kayıtlarla aşağıdaki adayları değerlendirmeye uygun veri üretir:

- BIAS ilişkisi korunmuş AC RMS;
- tepe ve tepe-tepe genliği;
- dalga şekli ve kararlılık ölçüleri;
- zaman içinde genlik değişimi ve gürültü;
- yeterli örnek olduğunda farklı pencerelerdeki özelliklerin tutarlılığı.

Bunların hepsinin nihai modele girmesi şart değildir. Bunlar, hangi ölçünün farklı kayıtlar arasında kararlı bölgeyi en iyi temsil ettiğini incelemek için aday özelliklerdir.

### 7.3 Etiketleme

- SCT ve BIAS ham kaydı korunur; bölgeler ve etiketler ayrı dosyalara yazılır.
- PZEM ayrı Modbus donanımından gelen referans akımı sağlar; V ve PF bilgileri de korunur.
- Etiketleme, birebir aynı zaman damgalarını aramak yerine deney/yük durumu ve kararlı bölge bağlamına dayanır.
- Zaman bilgisi yardımcı kayıt olabilir; tek başına aynı fiziksel durumu kanıtlamaz.
- Eşleşmesi/etiketi güvenilir olmayan bölge zorla etiketlenmez.
- Aynı nominal yükün her seferinde aynı akımı çektiği varsayılmaz; mevcut PZEM referansı ve kayıt bağlamı kullanılır.

Python 2'nin çıktısı; bölge başlangıç/bitiş bilgisi, SCT/BIAS kaynak kaydı, çıkarılan özellikler, atanan PZEM etiketi (I, ayrıca varsa V ve PF), etiketleme gerekçesi ve güven/kalite notudur. Eşik ve toleranslar kanıt olmadan uydurulmaz; kayıtlı veri üzerinden geliştirilir.

## 8. Python 3 — Gelen kayıtları birleştirme, geçmişi koruma ve F(x) arama

Python 3 de masaüstünde tek tıkla çalışır.

1. Python 2'nin bıraktığı gelen kayıt klasörünü tarar.
2. Dosya şeması, zorunlu alanlar, etiketler, kayıt kimlikleri ve tekrar kayıtları kontrol eder.
3. Geçerli yeni kayıtları birleştirilmiş veri kümesine ekler.
4. Yeni kayıtların ana veri kümesine başarıyla eklendiğini ve sonuç dosyasının okunabildiğini doğrular.
5. Ancak bundan sonra gelen klasördeki işlenmiş kayıtları arşivler veya klasörü boşaltır. Hata durumunda kaynak kayıtları korur.
6. Yeni etiketli veriyi geçmişteki doğrulanmış veriyle birleştirir; eski ham veri, etiketler, veri kümeleri ve modellerin üzerine kontrolsüz yazmaz.
7. Birikimli veriyle yeni F(x) adaylarını araştırır ve mevcut aktif modelle karşılaştırır.

### 8.1 Tek bir formül türüne bağlı kalmama

Karşılaştırılabilecek model aileleri arasında şunlar bulunur:

- doğrusal modeller;
- parçalı doğrusal modeller;
- bölge/aralık tabanlı formüller;
- uygun olduğunda polinom modeller;
- veri miktarı ve doğrulama sonuçları destekliyorsa başka hafif modeller.

Araştırılan ilişki başlangıçta I_tahmin = F(SCT_özellikleri, BIAS, V, PF) biçimindedir. BIAS, V veya PF'nin mutlaka gerekli olduğu baştan kabul edilmez. Gerekli girdiler bağımsız testlerle seçilir. Amaç, eğitim verisine ezber yapan en karmaşık formül değil, yeni kayıtlarda da iyi çalışan en sade yeterli modeldir.

Python 3 her çalıştırmada veri kümesi sürümünü, kullanılan özellikleri, model adaylarını, parametreleri, doğrulama sonuçlarını ve seçilen adayı raporlar. Yeni model eskisinin üzerine yazılmaz.

## 9. Python 4 — Yapay zekâ ile eğitim, ham veriden test ve sürekli iyileştirme

Python 4 masaüstünde tıkla-çalıştır biçiminde çalışır. BERO'ya taşındığında da düzenli aralıklarla yeni doğrulanmış veriyi inceleyerek model geliştirme sürecinin devam etmesi hedeflenir.

- Mevcut F(x) modelinin hangi veri ve koşullarda başarılı/başarısız olduğunu inceler.
- Uygun makine öğrenmesi yöntemleriyle alternatifler eğitir; basit doğrusal/parçalı modellerle karşılaştırmayı sürdürür.
- Python 2'nin etiketleme sürecinden geçen ham SCT + BIAS kayıtlarını, etiketli kararlı bölgelerle karşılaştırır.
- Eğitimde kullanılan kayıtları bağımsız test diye sunmaz. Veri kaynağı ve model sürümü izlenir; mümkün olduğunda ayrı kayıt oturumları veya bağımsız bölgeler test için ayrılır.
- Aynı fiziksel bölgenin türev kayıtlarının eğitim ve test tarafına sızması engellenir.
- Tahmin hatası, akım seviyesine göre hata, kararlılık, veri kapsamı ve model karmaşıklığı raporlanır.
- Python 3'ün formül adaylarıyla Python 4'ün AI adayları aynı bağımsız test ölçütleri üzerinden karşılaştırılır.
- Yeni veri geldiğinde eğitim/analiz tekrarlanabilir; her model ve rapor ayrı sürüm olarak saklanır.

**Sürekli iyileştirme ilkesi:** Python 4 sürekli analiz ve yeni model adayı üretimi yapabilir. Ancak sahadaki ESP modeli kontrolsüz biçimde kendi kendine değiştirilmez. Yeni model önce bağımsız testten geçer, mevcut modelle karşılaştırılır, sürümü ve geri dönüş yolu kaydedilir; ardından onaylı dağıtım ile ESP'ye aktarılır.

## 10. Modelin ESP'de çalıştırılması ve PZEM ile başarım

Geliştirme sırasında farklı SCT ESP'leri ve ayrı PZEM ESP'si veri üretmek için kullanılabilir. Nihai saha çözümünde hedef, **tek bir SCT ESP'sinin seçilmiş öğrenilmiş modeli çalıştırıp akım (A) üretmesi** ve bu sonucu sisteme/HA'ya vermesidir.

Model, masaüstünde eğitilir ve ESP'nin hesaplama/bellek sınırlarına uygun bir biçime dönüştürülür. ESP ham dalgadan gerekli özellikleri çıkarır, seçilen modeli çalıştırır ve akım tahminini üretir. Etiketleme, kapsamlı model araması ve eğitim ESP'de yapılmaz.

Ayrı Modbus PZEM doğrulama referansı olarak kalır. V/PF'nin nihai ESP tarafından Modbus üzerinden ayrıca okunması ancak doğrulama, bu girdilerin gerekli olduğunu gösterirse değerlendirilir; başlangıçta zorunlu değildir.

Başarım raporu en azından şunları kapsar:
- tahmin edilen akım ve PZEM referansı;
- mutlak amper hatası ve uygun koşullarda bağıl yüzde hata;
- MAE ve RMSE;
- farklı akım seviyelerindeki hata dağılımı;
- kararlı bölge ve geçiş koşullarının ayrımı;
- ±%4 hedefinin hangi aralıklarda karşılandığı/karşılanmadığı;
- PZEM referansının kendi ölçüm sınırları ve veri yetersizliği notları.

Yüksek korelasyon tek başına doğru akım ölçümü anlamına gelmez; sürekli fazla/eksik ölçüm ayrıca görülmelidir. Eğitim başarımı saha başarımı olarak sunulmaz.

## 11. Güncel model döngüsü

Saha ve masaüstü arasındaki planlanan gelişim döngüsü:

1. ESP'ler SCT + BIAS dalgasını, ayrı PZEM ESP'si de PZEM ölçümlerini toplar.
2. Veriler HA'da birikir.
3. Python 1 doğrular, arşivler ve ancak kalıcı kopya doğrulandıktan sonra HA kopyasını siler.
4. Python 2 ham SCT kayıtlarından kararlı bölgeleri bulur ve güvenilir PZEM referansıyla etiketler.
5. Python 3 yeni etiketleri geçmiş veriyle birleştirir, F(x) adaylarını yeniden arar ve model sürümlerini kaydeder.
6. Python 4 alternatif AI modellerini eğitir, ham veri/etiketli bölge üzerinden bağımsız test yapar ve iyileşmeyi raporlar.
7. Seçilen model sınav ESP'sine yüklenir; ayrı PZEM ile karşılaştırılır.
8. Başarımı doğrulanmış model onaylı sürüm olarak saha ESP'sine dağıtılır.
9. Yeni saha verisi geldikçe döngü tekrarlanır; önceki model, veri ve raporlar korunur.

## 12. Kayıt, güvenlik ve çalışma disiplini

- HDF-001/GRV-001 ve GRV-004/GRV-005 içindeki geçmiş kod, log ve tecrübeler korunur; gereksiz tekrar yapılmaz.
- ESP adları kullanıcı istemedikçe değiştirilmez; mevcut ad esp32d1 korunur.
- Her kod sürümünün yanında hedefi, kullanılan donanımı, yapılan işi, deneme koşullarını, logları, doğrulananları ve açık kalan noktaları anlatan bir .md kaydı bulunur.
- Derleme, cihazda çalışma, veri aktarımı, dalga kalitesi ve akım doğruluğu farklı doğrulama seviyeleridir; biri diğerinin kanıtı sayılmaz.
- Kullanıcı tarafından doğrulanmamış derleme veya donanım sonucu başarılı olarak yazılmaz.
- Ham veri ve geçmiş model sürümleri silinmez veya üzerine yazılmaz.
- Otomatik silme yalnızca kalıcı kopyanın doğrulanması ve aktarım kapsamının net olması sonrasında yapılır.
- Yeni fiziksel test, mevcut kayıtlar soruyu yanıtlamadığında ve eksik kanıtı sağlamak için gerekli olduğunda düşünülür; kullanıcı gereksiz testlerle boğulmaz.

## 13. Tamamlanma ölçütleri

HDF-002 ancak şu kanıtlar elde edildiğinde tamamlanmış sayılır:

1. Üç SCT + BIAS ölçüm zinciri, ayrı PZEM zinciri ve röle kontrol altyapısı koşullarıyla kaydedilmiş olmalı.
2. SCT dalgasını kaliteli ve düzenli temsil eden okuma yöntemi gerçek kayıtlarla değerlendirilmiş olmalı.
3. Ham veri HA'dan masaüstü/Mac arşivine bütünlük doğrulamasıyla taşınmalı; doğrulanmadan kaynak silinmemeli.
4. Python 2 kararlı SCT bölgelerini bulup güvenilir referanslarla gerekçeli biçimde etiketlemeli; geçiş bölgeleri eğitim dışında tutulmalı.
5. Python 3 birikimli veri kümesini koruyarak doğrusal, parçalı, bölge tabanlı ve uygun diğer F(x) adaylarını karşılaştırmalı.
6. Python 4 alternatif AI modellerini eğitmeli ve veri sızıntısı olmadan bağımsız test sonuçları üretmeli.
7. Seçilen model tek saha ESP'sinde akım (A) üretmeli ve sonucu sisteme/HA'ya aktarabilmeli.
8. Ayrı Modbus PZEM referansına göre hata raporu üretilmeli; yaklaşık ±%4 hedefinin hangi koşullarda sağlandığı veya sağlanmadığı gösterilmeli.
9. Yeni verilerle model iyileştirme döngüsü sürümlü, geri alınabilir ve doğrulamaya bağlı biçimde çalışmalı.

**Kanıt sınırı:** Bu belge HDF-002'nin güncellenmiş hedefini ve tasarlanan iş akışını tanımlar. Donanım kurulumunun, veri hattının, Python programlarının, modelin veya sürekli iyileştirme döngüsünün tamamlandığını; ayrıca ±%4 başarım elde edildiğini iddia etmez.


---

## 2026-10-12 — Güncel yöntem kararı: önce etiketli veri, sonra optimum paket ve F(x)

**Bu bölüm, HDF-002 içindeki önceki taslak akışlarda paket optimizasyonunun zamanlamasıyla ilgili ifadelerle çelişirse güncel ve geçerli yöntem kararını belirtir.** Önceki kayıtlar silinmez; bu kararın gerekçesi ve geçmişi korunur.

### Hedef 1'den devralınan durum

HDF-001'de ESP veri okuma yeteneklerini inceleyen işe yarar testler yapıldı. Bu testlerden öğrenilenler HDF-002'de kullanılabilir. HDF-001'in dondurulması, veri okuma testlerinin tamamının başarısız olduğu anlamına gelmez; başarısız kalan bölüm, zaman odaklı eşleştirme üzerinden F(x) hesaplamaya geçme yaklaşımıdır.

MCP/SCT tarafındaki entegre veya işlenmiş çıktı, ham SCT davranışının doğrudan aynısı değildir. Ölçüm zinciri örnekleme, kümülasyon/entegrasyon ve matematiksel işlem uygulamış olabilir. PZEM'in çıktısı da kendi ölçüm zincirinin hesaplanmış sonucudur. Bu iki çıktıyı yalnızca zaman damgalarına göre eşlemek, aynı fiziksel akım olayını temsil ettiklerini kanıtlamaz. Son testlerde istatistiklerin beklenen biçimde tutturulamaması bu yöntemin temel varsayımını sorgulamamıza neden oldu.

### HDF-002'nin ilk kazanımı: aynı akım alanından etiketlenmiş veri hazırlamak

HDF-002'nin ilk önceliği F(x) hesaplamak veya en yüksek örnekleme hızını seçmek değildir. İlk öncelik, **aynı fiziksel akım alanını/olayını temsil eden SCT bölgelerini belirlemek ve bunları PZEM'in sabit referans alanlarıyla gerekçeli biçimde etiketleyerek korunmuş bir veri kümesi hazırlamaktır.**

- PZEM tarafındaki akım değeri, gerilim ve güç faktörü bağlamıyla birlikte `(I, V, PF)` olarak korunur.
- SCT tarafındaki ham dalga, BIAS bilgisi, cihaz/kanal kimliği ve deney koşulları korunur.
- Zaman damgaları yardımcı bağlamdır; eşleşmenin tek ölçütü değildir.
- Benzer V/PF tek başına aynı fiziksel akım olayı olduğunu kanıtlamaz. Eşleştirme deney/yük durumu ve ölçüm bölgelerinin temsil ettiği fiziksel koşulla gerekçelendirilmelidir.
- Etiketi güvenilir biçimde atanamayan bölge zorla etiketlenmez.
- Ham kaynak veriler değiştirilmez; ham veri, aday bölgeler, etiketli veri ve türetilmiş veri ayrı tutulur.

Bu etiketli veri kümesi, F(x) henüz başarılı olmasa bile başlı başına bir kazanımdır ve sonraki paket/model deneylerinde yeniden kullanılacaktır.

### Yeni ara adım: Python ile optimum paketi seçmek

Etiketli veri hazırlandıktan sonra yeni bir Python adımı devreye girer. Bu kod, farklı paket/pencere/okuma seçeneklerini **aynı akım alanına ait etiketlenmiş veri üzerinde** değerlendirir ve sonraki paket testleri için gerekçeli aday veya optimum paket seçimini üretir.

Değerlendirme yalnızca örnek sayısına veya istatistiksel kararlılığa dayanmaz. Uygun olduğu ölçüde şunlar raporlanır:

- etiketli akım alanını temsil etme kalitesi;
- aynı olay içindeki tekrarların tutarlılığı;
- örnek kaybı, zamanlama düzeni ve paket bütünlüğü;
- paket/özellik seçimiyle hesaplanan akım hatası ve yanlılık;
- akım seviyesine ve deney koşuluna göre sonuçlar;
- karar vermeye yetecek etiketli veri olup olmadığı.

En düşük değişkenlik tek başına en doğru akım tahmini anlamına gelmez. Yeterli kanıt yoksa kod kesin optimum ilan etmek yerine adayları ve eksik kanıtı raporlar.

### Güncellenmiş sıra

1. **Ham veri ve ölçüm karakteri:** HDF-001'deki işe yarar okuma kodları, loglar ve deneyim tekrar test yapmadan incelenir; mevcut kanıt yeterliyse tekrar edilmez.
2. **Aynı akım alanını belirle ve etiketle:** SCT/BIAS bölgelerini, PZEM'in sabit `(I, V, PF)` referans alanları ve deney bağlamıyla eşleştir. Güvenilir etiketli veri kümesini oluştur ve koru.
3. **Python — optimum paket adayı seçimi:** Etiketli veri üzerinde paket/pencere/okuma alternatiflerini karşılaştır; ölçütleri ve karar gerekçesini kaydet.
4. **Paket testleri:** Seçilen paketleri etiketlenmiş veri üzerinde test et. Paket testleri kaldırılmamıştır; doğru veri temelinin sonrasına taşınmıştır.
5. **F(x) hesaplama:** Etiketli veriden bir veya daha fazla basit F(x) adayı üret ve gerçek akım tahmini hesapla.
6. **Hata analizi ve iyileştirme:** Tahminleri PZEM referansıyla aynı akım olayları/alanları üzerinde karşılaştır. Hata görünür olduktan sonra model ve paket seçimini iyileştir.
7. **Bağımsız doğrulama ve saha ESP'si:** Aynı fiziksel olayın türev kayıtlarını eğitim ve testte karıştırmadan bağımsız değerlendirme yap; doğrulanmış modeli ancak onaylı sürüm olarak ESP'ye taşı.

### Çalışma felsefesi

**Hedef 1:** ESP'nin veri okuma yeteneklerini sınamak ve işe yarar teknik bilgiyi edinmek. Veri okuma deneyimleri korunmuştur; ancak eski zaman merkezli F(x) yöntemi dondurulmuştur.

**Hedef 2:** Felsefeyi etiketlenmiş veriye kaydırmak. Önce elmayı elmayla eşleştir; aynı akım alanından etiketli veri hazırla. Sonra optimum paketi seç, paket testlerini yap, F(x)'i hesapla ve hatayı ölç.

**Çalışma döngüsü:** Etiketle → paket seç → paketleri test et → F(x) hesapla → hatayı gör → iyileştir.

### Kanıt sınırı

Bu kayıt yöntem ve iş akışı kararıdır. Etiketli veri kümesinin hazır olduğunu, optimum paketin bulunduğunu, paket testlerinin geçtiğini, F(x)'in başarılı olduğunu veya ±%4 hedefinin sağlandığını iddia etmez.

## 2026-10-12 — Yeni yöntem kararı: fiziksel alan eşleme ve kayıtlı ham veriyle ESP paketleme testi

### Temel düşünce: tek fiziksel olay, iki ölçüm resmi

Gerçek hayatta bir fiziksel akım/yük olayı vardır. PZEM bu olayı kendi ölçüm penceresi, paketleme ve iç hesaplama zinciriyle; SCT ise kendi ölçüm penceresi ve örnekleriyle temsil eder. Bu iki temsilin paket boylarının, örnek sayılarının, güncelleme zamanlarının veya işlem adımlarının aynı olması beklenmez.

Bu nedenle bütün akışları veya paketleri birebir eşitlemek hedef değildir. PZEM'in iç matematiğini baştan sona çözmek de ilk eşleme adımının ön koşulu değildir. Gerekli olan, PZEM çıktısının neyi temsil ettiğini ve karşılaştırılan fiziksel alanın uygunluğunu değerlendirecek kadar bağlamı bilmektir.

### Aşama 1 — Sabit fiziksel alanları işaretleme ve gerçek hatayı görme

1. PZEM ve SCT kayıtlarında aynı fiziksel çalışma olayına karşılık geldiği savunulabilir, karşılaştırılabilir/sabit alanları belirle ve etiketle.
2. PZEM referansını kendi alanına, SCT ham verisini kendi alanına bağla. Alanların süreleri ve boyları farklı kalabilir; sırf boyları farklı diye veri zorla yeniden örneklenmez veya kesilip eşitlenmez.
3. SCT verisinden hesaplanan akımı ilgili PZEM referansıyla karşılaştır; gerçek akım hatasını ve hangi koşullarda büyüdüğünü ölç.
4. Yalnızca zaman yakınlığı veya V/PF benzerliği, tek başına aynı fiziksel olayın kanıtı sayılmaz. Eşleşme belirsizse zorla etiketleme yapma.

### Aşama 2 — Kayıtlı ham veriyle ESP çıktısını eşleyerek paketlemeyi iyileştirme

Bu aşamada aynı kayıtlı SCT ham verisi tekrar kullanılabilir. Ham örneklerin zaman/indeks bilgileri, ESP'nin bu örneklerden ürettiği çıktılarla ilişkilendirilir; böylece her çıktının hangi örnek aralığından ve hangi paketleme/hesaplama yolundan geldiği incelenir.

- Aynı ham kayıt üzerinde farklı paketleme/pencereleme ve hesaplama adaylarını karşılaştır.
- Paketleme değişikliğinin veri kaybı, örnek bütünlüğü, zamanlama, tekrar edilebilirlik ve akım tahmini üzerindeki etkisini ölç.
- Kayıtlı veriden üretilen ESP çıktısı ile ham örnek aralığı arasındaki eşleme, PZEM ve SCT akışlarının tümünü aynı uzunluğa getirmek anlamına gelmez.
- Amaç, PZEM'in iç algoritmasını birebir kopyalamak değil; SCT ham verisinden, aynı fiziksel olaylarda PZEM'in akım referansına ve gerçek akıma yaklaşan bir çıktı üretip üretemediğimizi sınamaktır. Bu, “PZEM'in iç algoritması çözüldü” iddiası değildir.
- Aynı kayıttan türetilen komşu/benzer bölgeler eğitim ve bağımsız test kümelerine sızıntı yaratacak şekilde dağıtılmamalıdır. Paketleme/model seçimi sonrasında ayrı veri bölgelerinde bağımsız doğrulama yapılır.

### Sınırlar ve kanıt durumu

Bu bölüm yeni bir yöntem kararıdır. Henüz sabit alanların etiketlendiği, ham örnek–ESP çıktı eşlemesinin kurulduğu, en iyi paketlemenin bulunduğu veya PZEM benzeri çıktının başarılı olduğu iddia edilmez. Testler yapıldıkça gözlem, veri/kod sürümü, koşullar ve sonuçlar ayrı kayıtlarla eklenir; ham veriler ve eski deney kayıtları korunur.

