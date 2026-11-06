# E13 — Yüksüz gürültü filtresi ve SCT örnekleme hızı

**Durum:** PLANLANDI — uygulama/firmware değişikliği yapılmadı  
**Tarih:** 2026-11-05  
**Faz:** Faz 2  
**İlişkili kayıtlar:** I007 yüksüz gürültü havuzu, E12 tepki süresi, T007 HA→PC, T008 kararlı alan analizi

## Amaç

Fiziksel akımın 0 A olduğu yüksüz durumda SCT'nin kısa süreli sıçramalarını, gerçek zamanlı davranışı kaybetmeden ayırt etmek ve SCT çıktısını yaklaşık 0,5 saniyede bir (2 Hz) üretme hedefinin mevcut donanım/yazılım düzeninde uygulanabilirliğini ölçmek.

Bu deney iki ayrı ama ilişkili soruyu inceler:
1. Ham ölçümleri koruyarak kısa süreli aykırı okumaları filtrelenmiş yüksüz akışta bastırabilir miyiz?
2. SCT başına 500 ms çıktı aralığı (2 Hz) sürdürülebilir mi; tek kanal ve üç kanal durumlarında gerçek hız nedir?

## Kullanıcı kararları ve ilk gözlem dayanağı

- I007 fiziksel sıfır akım havuzu ayrı tutulur; ON kalibrasyon/eğitim verisine karıştırılmaz.
- Ham kaynak veri değişmez biçimde korunur. Filtreli/türetilmiş akış ikinci bir veri katmanıdır; ham kaydın yerine geçmez.
- Kısa süreli tekil sıçramalar filtreli akışta bastırılabilir/işaretlenebilir; yeterli süre devam eden yükseliş gerçek durum değişimi adayı olarak korunmalıdır.
- Filtre penceresi, sapma sınırı ve devam süresi henüz belirlenmedi.
- Kullanıcının hedefi SCT'den yaklaşık her 0,5 saniyede bir yeni çıktı, yani 2 Hz almaktır. Bu henüz ölçülmüş veya uygulanmış değildir.

I007 ilk CSV'sinde iki uzun fiziksel sıfır-akım aralığı analiz edildi. Bu aralıklardaki SCT akım entity'lerinin medyanları yaklaşık 0,157–0,170 A; P95 değerleri yaklaşık 0,255–0,333 A aralığındadır. SCT1 maksimumu 0,506 A, SCT2 maksimumu 0,655 A olarak kaydedilmiştir. Bu maksimumlar tekil uç değerlerdir; süreklilikleri ve nedenleri ayrıca analiz edilmeden eşik olarak kullanılamaz. Önceki çevrimsel HA History kaydında bu iki maksimumun her biri tek kayıt örneği olarak görünmüş, önceki/sonraki değerler daha düşük seviyeye dönmüştür. History örnekleme aralığı, gerçek elektriksel sıçramanın tam süresini kanıtlamaz.

## Mevcut firmware referansı — değişiklik yapılmadan önce

Kaynak: firmware/bero-modul2-esp32d1.yaml

- Üç SCT kanalı sıralı okunur: SCT1 → SCT2 → SCT3.
- Her kanalın ct_clamp sample_duration değeri 200 ms.
- Kanal geçişleri arasında 250 ms bekleme vardır.
- Sıralı okuma script'i 2 saniyede bir çağrılır.
- Dolayısıyla her kanal için mevcut nominal yeni çıktı hızı yaklaşık 0,5 Hz'dir (kanal başına 2 saniyede bir).
- K=24.22.
- Kanallar eşzamanlı örneklenmiş kabul edilemez.

Yalnızca 2 saniyelik çağrı aralığını 500 ms yapmak üç kanalın her birine 2 Hz sağlayamaz. Mevcut sıralı yapıdaki üç adet 200 ms ölçüm ve gecikmeler zaten 500 ms toplam bütçeyi aşar. Üç kanalın her birinde 2 Hz isteniyorsa edinim mimarisi/kanal sıralaması/örnek süresi yeniden ele alınmalıdır. Tek öncelikli kanala 2 Hz sağlamak ayrı ve daha dar bir hedeftir.

## Deney A — yüksüz filtre yaklaşımı (önce çevrimdışı)

1. I007 ham oturumunu salt okunur kaynak olarak kullan.
2. Ham değer dizisini ve timestamp'leri değiştirmeden tut.
3. Kayan pencere üzerinde merkez ve saçılım hesapla. Medyan ve MAD gibi sağlam istatistikleri basit ortalamaya alternatif olarak karşılaştır.
4. Merkezden sapma büyüklüğü ile ardışık örneklerde devam süresini birlikte kullan.
5. Tekil kısa sıçramayı işaretle veya filtreli seride bastır; devam eden yükselişi otomatik olarak silme.
6. Çıktıda en az şu alanları koru: timestamp, entity_id, raw_value, filtered_value, outlier_flag, window_id/parameter_id.
7. Farklı pencere uzunlukları ve devam sürelerini aynı ham oturum üzerinde karşılaştır; sonuçları ham/filtreli grafik ve istatistiklerle raporla.

Kabul ölçütü:
- Ham kayıt birebir korunmalı.
- Filtreli seri tekil kısa sıçramaları azaltmalı.
- Süreklilik gösteren kontrollü ON geçişini bastırmamalı.
- Filtre gecikmesi ve yanlış bastırma oranı raporlanmalı.
- Eşikler tek I007 oturumuna bakılarak nihai seçilmemeli; 7–10 günlük havuz biriktikçe yeniden değerlendirilmelidir.

## Deney B — 2 Hz örnekleme

Aşamalar:
1. Mevcut düzenin gerçek kanal başına çıktı aralığını History timestamp'lerinden ölç ve referansla.
2. Önce SCT1 tek kanalında 500 ms hedefli prototipin sürdürülebilirliğini ölç.
3. Ardından üç kanal açıkken her kanalın timestamp aralıklarını, sıra kaymasını ve eksik/tekrarlı güncellemeleri ölç.
4. Aynı kararlı yükte (başlangıçta uygun bir rezistif yük) mevcut 2 saniyelik referans ile daha hızlı akışı karşılaştır.
5. Gürültü dağılımı, kararlı alan medyanı, standart sapma, tepki gecikmesi ve örnek kaybını raporla.

Sabit tutulacaklar:
- İlk karşılaştırmada K=24.22.
- Mümkünse sample_duration=200 ms.
- Aynı CT, sarım, kablo yerleşimi ve yük.
- Değişen tek unsur örnek çıktı hızı/edinim düzeni olmalı.

Kabul ölçütü:
- Kanal başına gerçek 500 ms civarı çıktı aralığı timestamp'lerle kanıtlanmalı.
- Tekrarlanabilirlik ve kararlı yük seviyesi kabul edilemez ölçüde bozulmamalı.
- Üç kanalın eşzamanlı olduğu varsayılmamalı; gerçek örnekleme zamanları korunmalı.
- Hedef üç kanalda sağlanamıyorsa tek kanal 2 Hz veya farklı kanal önceliği açıkça raporlanmalı.

## Güvenlik ve uygulama sınırı

Bu belge yalnız deney planıdır. Firmware YAML henüz değiştirilmedi, derleme/OTA yapılmadı. Kullanıcı onayı ve kontrollü test olmadan mevcut çalışan firmware'e müdahale edilmeyecek. I007 ham yüksüz veri havuzu filtreleme denemesi nedeniyle değiştirilmez.

## Açık işler

- [ ] I007 ham CSV oturumunu kaynak olarak doğrula ve hash'ini kaydet.
- [ ] HA History timestamp aralıklarından mevcut SCT kanal başına gerçek güncelleme hızını çıkar.
- [ ] Çevrimdışı kayan pencere/robust outlier filtre prototipini hazırla.
- [ ] Tekil sıçrama ve kontrollü kalıcı ON geçişi üzerinde filtre gecikmesini/yanlış bastırmayı test et.
- [ ] SCT1 tek kanal 2 Hz prototipini ayrı kontrollü test olarak planla.
- [ ] Üç kanal 2 Hz fizibilitesini gerçek timestamp ve örnek kaybıyla değerlendir.
- [ ] Deney sonuçlarını ve gerçek log örneklerini depoya ekle.

**Sonuç:** Henüz yok. E13 tamamlanmış değildir.


## 2026-11-05 — Canlı ESP mimarisi netleştirildi: tek kanal, 2 Hz

Kullanıcı açıklamasıyla hedef mimari kesinleştirildi:
- Eğitim/veri toplama aşamasında üç SCT kanalının okunması yararlıdır; mevcut Modül 2 bu amaçla kullanılabilir.
- Canlı çalışacak eğitilmiş ESP üç kanalı okumayacak. Tek bir SCT kanalından her 500 ms'de bir yeni ölçüm alacak: 2 Hz.
- Dolayısıyla canlı ESP için üç kanalın her birinde 2 Hz sağlama gereksinimi yoktur. E13'ün canlı örnekleme fizibilitesi tek kanal odağına indirgenmiştir.
- Mevcut Modül 2 üç kanallı eğitim firmware'i olduğu gibi kalır; bu hedef nedeniyle değiştirilmez. Tek kanallı canlı ESP ayrı hedef mimaridir ve henüz uygulanmış değildir.

## 4 saniyelik kayan filtre penceresi — ilk tasarım adayı

Kullanıcı, 2 Hz canlı ölçüm akışında yaklaşık 4 saniyelik kayan pencere kullanmayı önerdi. 2 Hz'de pencere başına 8 örnek bulunur. Amaç tekil kısa süreli sıçramaları karakterize edip yüksüz durum kararını daha kararlı hale getirmektir.

Bu değer **ilk test adayıdır; onaylanmış nihai parametre değildir**. Filtre tasarımında:
- Ham ölçüm her zaman ayrı ve değişmez tutulur.
- Sekiz örnekli kayan pencereden sağlam merkez/dağılım (ör. medyan ve MAD) çıkarılır.
- Tekil aykırı örnek ham akıştan silinmez; türetilmiş akışta işaretlenir veya filtreli durum değerine katılmaz.
- Ardışık örneklerde devam eden yükseliş, gerçek yük başlangıcı olabileceğinden otomatik olarak bastırılmaz.
- Pencere dolum süresi, filtre gecikmesi ve yük başlangıcını algılama gecikmesi ayrıca raporlanır.

4 saniye pencere ile sekiz örnek olması, sistemin mutlaka 4 saniye gecikmeli karar vereceği anlamına gelmez. Kayan pencere her 500 ms'de güncellenebilir; ancak hangi kararın ne zaman kesinleşeceği seçilen süre/ardışıklık mantığına bağlıdır. Bu davranış kontrollü ON/OFF geçişiyle test edilmelidir.

## E13 kapsam düzeltmesi

- Deney A: I007 ham yüksüz kayıtları üzerinde çevrimdışı filtre karşılaştırması; ham veriyi değiştirmez.
- Deney B: canlı hedef ESP için tek SCT kanalında 500 ms çıktı aralığının (2 Hz) sağlanması. Üç kanal hız testi canlı hedef için gerekli değildir; üç kanallı Modül 2 yalnız eğitim/veri toplama düzeni olarak kalır.
- Tek kanallı canlı ESP'de 4 saniyelik / 8 örnekli kayan filtre adayı, tekil sıçramayı bastırırken gerçek ON başlangıcını geciktirmeme açısından değerlendirilecek.

Açık işler ve kabul ölçütleri buna göre revize edilmelidir. Firmware henüz değiştirilmedi; 2 Hz ve filtre uygulaması test bekliyor.


## 2026-11-05 — Süreklilik kararının kullanıcı tarafından netleştirilmesi

Kullanıcı, filtre kararının tek bir 4 saniyelik pencereye bakılarak verilmesini istemediğini netleştirdi. Esas ayrım, 500 ms'lik tekil ve devam etmeyen ölçüm sıçraması ile sonraki örneklerde/pencerelerde de devam eden sistem davranışıdır.

- Canlı örnekleme 500 ms (2 Hz) olacaktır; her tek ölçüm ham veri olarak korunur.
- Yaklaşık 4 saniyelik kayan pencere ilk tasarım adayıdır (8 örnek). Pencere her yeni örnek geldikçe güncellenebilir.
- Tek bir 500 ms örneğinde görülen ve sonraki ölçümlerde devam etmeyen sıçrama, çamaşır makinesi gibi hedef yüklerin çalışma durumu olarak kabul edilmemelidir; filtreli karar katmanında geçici anomali olarak işaretlenmesi/bastırılması hedeflenir.
- Yükseliş sonraki örneklerde veya sonraki kayan pencere değerlendirmelerinde de sürüyorsa artık süreklilik gösteren bir sistem davranışı/yük adayı sayılmalıdır. Böyle bir yükseliş filtre tarafından tekil sıçrama diye silinmemelidir.
- Bu, tek pencere içinde eşik aşımı aramak değil, ardışık zaman değerlendirmeleri arasında devamlılık aramaktır.
- Çamaşır makinesi uygulaması için kullanıcı varsayımı: yarım saniyelik tekil bir akım hareketi makinenin anlamlı çalışma durumu değişimi değildir. Bu varsayım hedef uygulama bağlamında kullanılacak; başka yük türlerine genellenmeyecektir.

### E13 filtre doğrulama senaryoları

1. **Tek örnek sıçrama:** Bir 500 ms örnek yüksek, hemen sonraki örnekler normal seviyeye döner. Beklenti: ham kayıtta tutulur; filtreli durum kararında kalıcı yük olarak değerlendirilmez.
2. **Ardışık devam:** İlk yüksek örnekten sonra yükseliş sonraki örneklerde de sürer. Beklenti: süreklilik algılanır; gerçek yük davranışı adayı korunur.
3. **Pencere sınırını aşan devam:** Yükseliş bir 4 saniyelik pencere değerlendirmesinden sonraki kayan pencereye de taşar. Beklenti: sonraki pencere değerlendirmesi de yükselişi görür; tekil anomali muamelesi yapılmaz.
4. **Kısa aralıklı tekrarlar:** Tekil sıçramalar aralarda normale dönerek tekrarlanır. Beklenti: algoritma bunları kesintisiz yük varlığına dönüştürmez; tekrar sıklığı ayrıca raporlanır.
5. **Gerçek ON geçişi:** Kontrollü SSR ON ile kalıcı yükseliş başlatılır. Beklenti: filtre yükselişi bastırmaz; algılama gecikmesi ölçülür.

Kabul ölçütü: tek örnekli sıçrama ham veriden silinmemeli fakat canlı durum kararında kalıcı yük sayılmamalı; ardışık devam eden gerçek ON yükselişi ise belirlenen ve ölçülen gecikme içinde tanınmalıdır. Kaç ardışık örneğin/sürenin yeterli olacağı deneyle belirlenecek; henüz sabit bir sayı veya amper eşiği tanımlanmamıştır.


## 2026-11-05 — Tasarım yaklaşımı: kararlı pratik ölçüm, yöntem henüz açık

Kullanıcı, yüksüz gürültü konusunun tek başına büyük bir araştırma hedefine dönüştürülmemesi gerektiğini netleştirdi. BERO'nun ana hedefi, ev makinelerinin çalışma durumlarını gözlemleyebilecek kadar kararlı ve kullanışlı bir akım ölçüm sistemi geliştirmektir; gürültüyü teorik olarak tamamen açıklamak veya her düşük akımlı olayı mutlaka yakalamak değildir.

Henüz karar verilmemiş alternatifler:
- Ölçüm kodunda tekil/aşırı okumaları bastırmak veya filtrelemek.
- Ölçüm kodunda kısa bir süre boyunca örnek toplayıp daha kararlı bir çıktı üretmek.
- Süreklilik kontrolü uygulamak.
- Pratik bir akım eşiğinin altını yüksüz kabul etmek.
- Bu yöntemleri birlikte veya ayrı kullanmak.

Bunlar tasarım seçenekleri ve deney konularıdır; hiçbiri şu aşamada kesin mimari kararı değildir. Tek kanalda 500 ms'de bir ölçüm hedefi ayrı bir örnekleme hedefi olarak durur; 500 ms ham ölçümün mutlaka filtresiz biçimde üst katmana aktarılacağı anlamına gelmez.

Uygulama bağlamı: çamaşır makinesi su giriş solenoidi gibi düşük akımlı bir olay basit yüksüz eşiğinin altında kalabilir. Bu olayın kaçırılması, su sesi gibi başka bir gözlem sinyaliyle yakalanabiliyorsa kabul edilebilir bir mühendislik ödünleşimi olabilir. Sistem hedefi tüm olası düşük akım olaylarını tek SCT kanalıyla yakalamak değil, makinenin anlamlı çalışma durumlarını yeterli güvenilirlikle gözlemlemektir.

Dolayısıyla I007 yüksüz kayıtları faydalı bir veri havuzudur; ancak bu konu projenin ana hedefinin önüne geçmeyecek. Filtre türü, eşik, pencere süresi ve süreklilik şartı deneylerle belirlenecek. Mevcut 4 saniye/8 örnek önerisi yalnızca bir adaydır; zorunlu veya nihai karar değildir.



## 2026-11-06 — Yüksüz gözlem oturumu: üç SCT kanalında tek geçiş

Kullanıcı, bu oturum için test yaklaşımını değiştirdi. Önceki farklı sarım sayılarıyla (2, 3 ve 4 geçiş) yapılan kanal karşılaştırması yerine, akşamki yüksüz gözlemde üç SCT kanalının da **tek geçiş (1 turn)** olacak şekilde kullanılması planlandı.

### Güncel test düzeni
- Modül 2'nin üç SCT kanalı da kullanılacak: SCT1 GPIO32 (sarı), SCT2 GPIO33 (yeşil), SCT3 GPIO34 (mavi).
- Her üç kanalın fiziksel iletken geçiş sayısı: **1 tur**.
- Akşam kullanılacak kod, üç kanalın da tek geçiş düzenine göre okunmasını sağlayacak. Bu kayıt, firmware'in şimdiden değiştirildiği veya yüklendiği anlamına gelmez.
- Testin odağı, tek geçişte üç kanalın yüksüz davranışını açık biçimde gözlemlemek ve kanalların verdiği sonuçlardan genel bir karşılaştırma fikri edinmektir.
- Üç kanal sıralı okunduğundan örnekler eşzamanlı kabul edilmeyecek; her kanalın kendi timestamp'i ve gerçek güncelleme aralığı korunacak.
- Kullanıcı masanın/kurulum yerinin değiştiğini bildirdi. Bu fiziksel yerleşim, oturum koşulu olarak not edilir; ölçüm farkının nedeni olduğu peşinen kabul edilmez.

### Testin kapsamı ve yorum sınırı
Bu oturum, E13'te tanımlanan tek kanallı canlı ESP 2 Hz mimarisinin testi değildir. Üç kanallı Modül 2 üzerinde, üç SCT'nin aynı tek geçiş düzenindeki yüksüz davranışını gözlemleme çalışmasıdır. Bu nedenle sonuçlar tek kanal canlı mimarinin 2 Hz başarısını kanıtlamaz.

Üç kanalın birbirine yakın sonuç vermesi kanallar arası tutarlılık için ön gösterge olabilir; mutlak akım doğruluğunu veya kalibrasyonu tek başına kanıtlamaz. Kanallar arasında fark görülürse ham kayıt, kanal bazlı zaman aralıkları ve fiziksel bağlantı koşulları birlikte incelenir. Bu oturumda K veya filtre eşiği güncellendiği varsayılmaz.

### Açık işler
- [ ] Akşamki Modül 2 kodunu üç kanalda da 1 tur varsayımına göre hazırla ve yükle.
- [ ] Test öncesi üç SCT'nin fiziksel geçiş sayısının 1 olduğunu doğrula.
- [ ] Yüksüz oturumun ham HA/ESP kayıtlarını sakla.
- [ ] Her kanal için örnek sayısı, timestamp aralığı, merkez/dağılım ve uç değerleri ayrı değerlendir.
- [ ] Kanallar arası benzerlik/farkları gözlemle; tek oturumdan kalibrasyon sonucu çıkarma.
- [ ] Masa/kurulum yeri değişikliğini kayıt koşulu olarak koru; etkisini veri olmadan varsayma.

**Durum:** Test planı güncellendi; kod değişikliği, derleme/OTA ve test sonucu henüz kaydedilmedi. E13 tamamlanmış değildir.

## 2026-11-06 — Kullanıcı kararı: üç kanalda toplam 2 çevrim/s hedefi

Önceki tek kanallı canlı 2 Hz hedefi bu deneme için tek başına yeterli kabul edilmeyecek. Kullanıcı öncelikle Modül 2 üzerinde mümkünse üç SCT kanalının da dahil olduğu bir çevrimin saniyede iki kez üretilmesini denemek istiyor. Amaç, bu edinim düzeni sağlıklı çalışırsa aynı kodu akşamki yüksüz gözlemde de kullanmak; başarısız veya kararsızsa sonraki mimariyi ölçüm sonuçlarına göre değerlendirmektir.

### Deneme tanımı

- Hedef: SCT1, SCT2 ve SCT3'ün her birinden yeni ölçüm alınan tam sıralı çevrimin yaklaşık 500 ms'de bir tamamlanması (toplam çevrim hızı 2 Hz).
- Kanallar eşzamanlı değildir. Her kanalın kendi gerçek yayın zamanı ve örnek aralığı ayrı değerlendirilir.
- İlk canlı deneme 100 W sabit yük altında yapılır.
- Akşam yüksüz gözleminde aynı firmware/zamanlama korunması hedeflenir.
- Üç SCT fiziksel olarak birer tur (1T) kullanılacaktır: GPIO32 sarı, GPIO33 yeşil, GPIO34 mavi.
- K=24.22 sabit tutulur.
- Mevcut 200 ms ölçüm penceresi üç kanalın seri toplamında tek başına 600 ms gerektirdiğinden, 500 ms çevrim hedefiyle uyumlu değildir. İlk prototipte 100 ms sample_duration ve kanallar arası ilave 250 ms gecikmelerin kaldırılması değerlendirilecektir.
- 100 ms pencere 50 Hz'de yaklaşık beş şebeke periyodudur. Bu, mevcut 200 ms pencereye göre daha az örnekleme süresi sağlar; ölçüm kararlılığı ve 100 W yükteki merkez/dağılım sonuçları özellikle karşılaştırılmalıdır.
- 500 ms interval tek başına başarı kanıtı değildir. Üç kanalın gerçek HA timestamp aralıkları, çevrim tamamlama süresi, eksik/tekrarlı yayın ve kanal sırası incelenmeden 2 Hz sağlandı denmeyecektir.
- İlk denemede yalnız örnekleme süresi ve sıralama/zamanlama değişir; K ve fiziksel tur sayısı değiştirilmez. Kurulum ve kablo koşulları test boyunca sabit tutulur.

### Başarı değerlendirmesi

1. Üç kanalın her birinde yeni değerlerin yaklaşık 500 ms aralıklarla üretildiği gerçek timestamp'lerle doğrulanmalı.
2. Bir çevrimin bir sonraki çevrim başlamadan tamamlandığı; script çakışması, atlanan çevrim veya kanal güncelleme kaybı olmadığı gösterilmeli.
3. 100 W sabit yükte kanal başına merkez, dağılım, uç değer ve örnek aralığı raporlanmalı.
4. 100 ms pencerenin 200 ms referansa kıyasla ölçümü kabul edilemez ölçüde oynatıp oynatmadığı değerlendirilmeli. Bu karşılaştırma için mümkünse aynı CT/yük/yerleşim koşulundaki önceki 200 ms kayıt referans alınmalı; farklı koşullar varsa doğrudan eşdeğer deney gibi sunulmamalı.
5. Deneme sağlıklıysa aynı firmware ile yüksüz oturuma geçilmeli. Sağlıklı değilse akşam testine otomatik olarak devam edilmemeli; sonuç ve sınırlama kaydedilip mimari yeniden görüşülmeli.

**Durum:** Hedef ve test sırası kullanıcı tarafından belirlendi. Firmware henüz değiştirilmedi; derleme, OTA ve gerçek cihaz testi yapılmadı. Sonuç yok. E13 açık durumdadır.

### 2026-11-06 — İlk üç kanal 2 Hz firmware prototipi depoya işlendi

Modül 2 firmware dosyasında ilk prototip düzenlemesi yapıldı:
- Üç kanalın da `sample_duration` değeri 100 ms olarak ayarlandı.
- Her `component.update` çağrısından sonra 110 ms beklenecek şekilde sıralama düzenlendi. Böylece asenkron 100 ms ct_clamp ölçümünün tamamlanması için yaklaşık 10 ms pay bırakılır.
- Önceki 250 ms kanal arası beklemeler kaldırıldı.
- Tam sıralı çevrim 500 ms aralıkla başlatılacak şekilde ayarlandı.
- Üç kanalın firmware açıklama ve HA entity adları 1T olarak güncellendi: SCT1 GPIO32 sarı, SCT2 GPIO33 yeşil, SCT3 GPIO34 mavi.
- K=24.22 değiştirilmedi; UDP olay alıcısı ve diğer ağ/olay davranışı değiştirilmedi.

Kaynak firmware: `firmware/bero-modul2-esp32d1.yaml`  
Firmware commit: `85e4fcb3c170f17ffca91b3d662743bb039b4912`  
Bu dosya GitHub'dan tekrar okunarak üç adet 100 ms sample_duration, üç adet 110 ms bekleme ve 500 ms interval bulunduğu doğrulandı.

**Önemli doğrulama sınırı:** Bu değişiklik yalnızca depodaki YAML prototipidir. ESPHome derlemesi, cihaz yüklemesi/OTA ve gerçek HA timestamp testi henüz yapılmadı. Dolayısıyla üç kanalda 2 Hz üretildiği veya ölçümün sağlıklı olduğu iddia edilmez. Kullanıcı 100 W sabit yük altında ilk denemeyi yapacak; akşam yüksüz oturumuna ancak bu deneme sağlıklı bulunursa aynı kodla geçilecek.

### 2026-11-06 — Örnekleme hedefi düzeltmesi: tek kanal 2 Hz

Kullanıcı hedefi yeniden netleştirdi: amaç üç kanalın toplamda iki değer üretmesi veya üç kanalın her birinin 2 Hz çalışması değildir. Esas hedef, **tek bir SCT kanalının saniyede iki yeni değer (yaklaşık 500 ms örnek aralığı) üretmesidir**. Üç kanalın aynı anda örneklenmesi gerekmez; kanalların ölçüm zamanları birbirinden kayabilir.

Bu nedenle üç kanallı Modül 2 sıralı tarama firmware'inin 500 ms çevrimle çalıştırılması doğru yaklaşım değildir. Firmware tekrar 2 saniyelik üç kanal tarama düzenine alındı; 100 ms ölçüm penceresi ve 110 ms kanal arası bekleme prototip değişiklikleri korunmuştur. Böylece her kanal sıralı taramada yaklaşık 2 saniyede bir okunur. Bu düzen tek kanal 2 Hz hedefini sağlamaz.

Tek kanal 2 Hz fizibilitesi ayrı bir deneme olarak ele alınmalıdır: önce 100 W sabit yükte tek bir SCT kanalının 500 ms aralıkla sürdürülebilir ölçüm üretmesi doğrulanır. Sonrasında diğer kanalların aynı ESP'de sıralı ve kaymalı biçimde taranması, seçilen kanal başına hız korunarak tasarlanır. Üç kanala da 2 Hz zorunluluğu yoktur.

**Durum:** Önceki yanlış yorum düzeltilmiştir. Firmware henüz derlenmedi veya cihaza yüklenmedi. 100 W testi yapılmadı. Akşam yüksüz testine geçiş, tek kanal 2 Hz denemesinin sonucuna bağlıdır.
