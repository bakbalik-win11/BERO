## 2026-11-05 — BERO kapsamı ve hazırlık ortamı / canlı sistem ayrımı

Kullanıcı açıklaması ve kapsam kararı:
- BERO tek bir akım ölçer değil, farklı fiziksel değişkenleri izleyen sensörlerden oluşması hedeflenen çoklu sensörlü ev gözlem sistemidir.
- Akım sensörü bu bütünün yalnızca bir bileşenidir. Uygun sensör ve ölçüm ön ucuyla AC akımın yanında DC akım ölçümü de hedeflenebilir.
- Kullanıcının belirttiği sensör örnekleri: su kuyusunda sıcaklık değişim sensörü; kuyu basıncından su seviyesini/su derinliğini çıkaran basınç sensörü; ev girişinde şehir şebekesi su basıncını ölçen sensör.
- SCT013-PZEM akım ölçümünden başlanmasının nedeni BERO'nun akımla sınırlı olması değil; akımı güvenilir ölçmek, canlı okumak ve başka program/algoritma çıktılarıyla ilişkilendirmek teknik olarak zor bir başlangıç problemi olmasıdır.
- Mevcut SCT013-PZEM çalışması diğer evde yürütülen hazırlık/geliştirme çalışmasıdır.
- Şu anda canlı BERO sisteminde çoklu sensörlerle yürüyen entegre bir uygulama yoktur. Depodaki sensör ailesi ve çoklu sensör mimarisi hedef kapsamı/gelecek yönünü anlatır; mevcut canlı kurulumun durumu olarak sunulamaz.
- Mevcut kısa vadeli iş, SCT akım ölçüm zincirini ve veri toplama/analiz altyapısını hazırlamaktır. Sensör entegrasyonları ileride ayrı ayrı doğrulanacaktır.

## 2026-11-05 — Temel ilke: ham verinin uzun süreli korunması ve geçmiş veriden yeniden bilgi üretimi

Kullanıcı kararı: BERO ham ölçümleri uzun süreli saklamalıdır. Ham veri yalnızca bugünkü analiz için değil, ileride geliştirilecek ve bugün henüz öngörülmeyen yöntemlerle yeniden incelenmek için de korunacaktır. Geçmiş ham veriden sonradan yeni özellikler, davranış örüntüleri, trendler, sınıflandırmalar ve bakım/anomali göstergeleri üretilebilir.

Uygulama ilkeleri:
- Ham kayıtlar değişmez biçimde korunur; filtreleme veya temizleme ham kaydın üzerine yazmaz.
- Filtrelenmiş, normalize edilmiş, etiketlenmiş ve özellik çıkarılmış veriler ayrı türetilmiş katmanlardır.
- Türetilmiş çıktıların dayandığı ham veri aralığı ile işlem/model sürümü izlenebilir olmalıdır.
- Yeni algoritmalar mümkün olduğunca geçmiş ham veri üzerinde de çalıştırılarak karşılaştırılır.
- Uzun dönemli saklama; zaman damgası, kaynak/kanal kimliği ve veri bütünlüğü korunarak tasarlanır.

BERO hobi/araştırma projesidir. Anomali uyarıları otomatik servis veya ekonomik işlem başlatmadığından farklı yöntem ve eşikler deneysel olarak denenebilir. Yanlış uyarılar yöntem sınırlarını anlamak için geri bildirimdir; ham veri kaybı ise gelecekteki analiz imkânını ortadan kaldırabilir.

## 2026-11-05 — Sonraki oturumun ilk işi: yüksüz/gürültü CSV kaydı

Kullanıcı bu gece sistem yüksüzken Home Assistant History kaydı alacağını bildirdi. Bir sonraki oturum açıldığında ilk olarak bu yüksüz CSV dosyası kullanıcıdan istenecek; kullanıcı sağlayınca ayrı OFF/yüksüz gürültü veri havuzunun ilk kaydı olarak analiz edilecek.

- SCT1 sarı/GPIO32: fiziksel 1 geçiş (YAML/entity etiketi 2T kalmış olabilir).
- SCT2 yeşil/GPIO33: nötr hattında 4 geçiş.
- SCT3 mavi/GPIO34: faz hattında 3 geçiş.
- GPIO35: ortak bias.
- Her oturum ayrı analiz edilecek; ham dağılımlar korunarak zaman içinde ortak havuzda biriktirilecek.
- Tur sayısına bölme yaklaşık normalize karşılaştırmadır, kesin kalibrasyon değildir. Kanal/hat konumu, kazanç ve K farkları nedeniyle ham değerler de raporda tutulacak.
- Amaç: yüksüz tabanın tipik seviyesi, üst yüzdelikleri ve tekrarlayan en yüksek değerleri görmek; henüz eşik belirlemek değil.
- Bu kayıt ON kalibrasyonuna katılmayacak.


## 2026-11-05 — I007 uzun süreli fiziksel sıfır-akım gürültü bandı

I007 tek gecelik test değil; başlangıç hedefi yaklaşık 7–10 gün, gerekirse kullanıcı kararıyla daha uzun sürecek veri toplama çalışmasıdır. Kullanıcı her gün/uygun oturum sonunda HA History CSV sağlayacak. Her oturum ayrı analiz edilecek; geçerli ham kayıtlar depodaki kümülatif havuza eklenerek güncellenecek. Her ekleme öncesi mevcut havuz depodan okunacak, tekrarlar kontrol edilecek, yeni kayıtlar eklenecek ve güncel kümülatif veri/özet tekrar depoya yazılacak. İlk gerçek CSV geldiğinde gerçek kolonlara göre veri şeması belirlenecek.

**Fiziksel referans:** Kullanıcının teyidine göre ölçülen hatta hiçbir yük bağlı değil ve ESP/PZEM/modüller bu hattan beslenmiyor; dolayısıyla gerçek hat yük akımı fiziksel olarak 0 A. SCT'nin sıfırdan farklı okuması bu koşuldaki ölçüm tabanı/gürültü çıktısıdır; sıfır koşulu PZEM göstergesinden varsayılmıyor.

Hedef uzun dönem SCT1/2/3 gürültü bandını, üst yüzdelikleri ve oturumlar arası değişimi belirlemek; şu aşamada eşik/model seçmek değildir. Ham ölçümler korunacak, tur-normalize karşılaştırma yalnız yardımcı olacak. Bu havuz ON kalibrasyonundan ayrı tutulacak.


## 2026-11-05 — I007 filtre yaklaşımı ve SCT 2 Hz hedefi

Kullanıcı kararları kayda alındı:
- I007 ham yüksüz kayıtları değişmez biçimde korunacak; filtrelenmiş/türetilmiş yüksüz veri ayrı akış/dosya olarak üretilecek.
- Kısa tekil sıçramalar kayan pencere, sağlam merkez/dağılım ve süre koşuluyla filtrelenebilir/işaretlenebilir; belirli süre devam eden yükseliş korunmalı. Pencere uzunluğu, sapma sınırı ve devam süresi henüz belirlenmedi.
- Kullanıcı SCT'den yaklaşık 0,5 saniyede bir yeni çıktı (2 Hz) hedefliyor. Mevcut Modül 2 firmware üç kanalı 2 saniyelik çevrimde sıralı okur; dolayısıyla kanal başına nominal hız yaklaşık 0,5 Hz'dir. Mevcut 200 ms örnek süresi ve üç kanallı sıralı yapı nedeniyle yalnız çevrim aralığını 500 ms yapmak üç kanalda 2 Hz sağlamaz.
- Tek SCT1 kanalı için 2 Hz ve üç kanalın her biri için 2 Hz ayrı fizibilite hedefleri olarak test edilecek. Firmware değişikliği yapılmadı.

Ayrıntılı test planı: [E13 — Yüksüz gürültü filtresi ve SCT örnekleme hızı](experiments/E13-idle-noise-filter-and-sampling-rate/README.md). E12'nin tepki süresi kapsamına 2 Hz hedefi de eklendi. I007 ham/filtreli veri kararı [I007 veri havuzu](data/off-noise/README.md) altında kayıtlı.


## 2026-11-05 — Canlı ölçüm mimarisi netleştirme

Kullanıcı kararı: Üç SCT kanalının okunması eğitim/veri toplama aşaması içindir. Canlı çalışan eğitilmiş ESP yalnızca tek SCT kanalını okuyacak ve her 500 ms'de bir yeni sonuç üretecek (2 Hz). Üç kanalın her birinde 2 Hz hedefi canlı mimarinin gereksinimi değildir. Mevcut Modül 2 üç kanallı eğitim firmware'i bu nedenle değiştirilmez; tek kanallı canlı ESP ayrı hedef mimaridir.

Filtre için ilk tasarım adayı: 2 Hz akışta 4 saniyelik kayan pencere = 8 örnek. Ham veri korunacak; tekil sıçramalar ayrı türetilmiş filtreli akışta işaretlenecek/bastırılacak; devam eden yükseliş gerçek yük başlangıcı olabileceği için korunacak. 4 saniye/8 örnek nihai parametre değil, deney adayıdır. Pencere, sapma sınırı, ardışık devam koşulu ve algılama gecikmesi E13'te test edilecek.

Ayrıntı: [E13 — Yüksüz gürültü filtresi ve SCT örnekleme hızı](experiments/E13-idle-noise-filter-and-sampling-rate/README.md).


## 2026-11-05 — BERO kullanım vizyonu genişletildi: davranış izleme ve arıza/anomali takibi

Kullanıcı, BERO'nun yalnızca ev makinelerinin programını veya çalışma evresini tahmin eden bir sistem olarak tanımlanmaması gerektiğini açıkladı. Makine/program tanıma hedeflerden yalnızca biridir. Uzun vadeli hedef, akım davranışlarını izleyerek ekipman ve hatların normal çalışma karakterini öğrenmek, zaman içindeki değişimleri görünür kılmak ve olası anormal durumları işaretlemektir.

Öngörülen kullanım alanları:
1. **Çalışma karakteri ve durum çıkarımı:** çamaşır makinesi gibi cihazların çalışma evreleri, motor/rezistans devreye girme-çıkma davranışları ve çalışma düzenleri.
2. **Arıza/anomali belirtileri:** havalandırma motoru veya su kuyusu hidroforu gibi ekipmanlarda akım seviyesinin, çalışma süresinin, devreye girme sıklığının ya da davranış örüntüsünün normalden sapması. Bu çıktılar doğrudan kesin arıza teşhisi değil, olası sorun/bakım incelemesi uyarısı olarak ele alınmalıdır.
3. **Uzun dönemli hat/ekipman izleme:** günlük/haftalık/aylık akım eğilimleri, baz seviyedeki kademeli yükselişler, ani değişimler ve karşılaştırmalı grafikler.

Bu vizyon mevcut SCT013-PZEM alt projesinin anlık görevlerini değiştirmez; mevcut odak ölçüm yolunu güvenilir kılmak, veri toplamak ve davranış çıkarımına uygun veri altyapısını oluşturmaktır. Kısa vadeli çamaşır makinesi denemeleri daha geniş sistemin ilk kullanım senaryolarından biridir; nihai ürün tanımı değildir.

Ölçüm kararlılığı bu nedenle yalnızca yüksüz/yüklü ayrımına indirgenmez. Tekil sıçramaları filtreleme, kısa süreli örnek toplama, süreklilik kontrolü, pratik eşik kullanımı ve uzun dönem trend analizi ileride deneyle değerlendirilebilecek yöntemlerdir. Şu aşamada belirli bir filtre, eşik, algoritma veya arıza sınıflandırma yöntemi kesinleştirilmemiştir. Ham ölçümlerin korunması ve türetilmiş/filtrelenmiş verinin ayrı tutulması esastır.


## 2026-11-05 — E14 kısa tek-kanal 2 Hz denemesi kaydedildi

Kullanıcı kararı: 2026-11-06 akşamı, veri/donanım durumu uygunsa kısa bir deney yapılabilir. Modül 2 bu amaçla deney alanı olarak kullanılabilir; yalnız SCT1 (sarı/GPIO32, fiziksel 1 geçiş) okunarak yaklaşık 500 ms / 2 Hz yeni ölçüm sonucu hedeflenecek. İlk karşılaştırmada K=24.22 ve sample_duration=200 ms sabit tutulacak; gerçek çıktı aralığı HA timestamp'leriyle doğrulanacak.

Bu çalışma E14 olarak kaydedildi. Mevcut üç kanallı çalışan YAML korunacak; deney sürümü ayrı tutulacak ve gerekirse geri dönülebilecek. Firmware değişikliği, derleme veya OTA henüz yapılmadı. E14 kısa akşam oturumu adayıdır; Cumartesi uzun çalışma önceliğini değiştirmez. Deneyler arasında öncelik, kullanıcının o günkü veri ve donanım durumuna göre esnekçe belirlenebilir.

Ayrıntı: [E14 — Modül 2 tek SCT kanalında 2 Hz ölçüm denemesi](experiments/E14-module2-single-channel-2hz/README.md).


## 2026-11-06 — Tek kanallı SCT eğitim verisi kararı (ADR-027)

Kullanıcı kararı:
- Test ve veri toplama firmware'i üç SCT kanalını birlikte okuyabilir.
- Ham HA dışa aktarımı ve arşiv birden fazla SCT kanalının kayıtlarını koruyabilir.
- Her eğitim veri seti yalnızca tek bir SCT kanalından oluşur. CH1, CH2 ve CH3 ayrı veri setleri ve ayrı model değerlendirmeleri üretir.
- PZEM akımı proje referansıdır; seçilen kanalın SCT kararlı alanları mevcut BOOT_ID + EVENT_ID paket kuralları içinde PZEM kararlı alanlarıyla değerlendirilir.
- Kanal kimliği ve fiziksel geçiş/sarım bilgisi eğitim çıktısında izlenebilir olmalıdır.

Önerilen ortak kanal kimliği biçimi `CH1-1T`, `CH2-4T`, `CH3-3T` şeklindedir. Depodaki fiziksel eşleme (CH1 sarı/GPIO32 = 1 geçiş; CH2 yeşil/GPIO33 = 4 geçiş; CH3 mavi/GPIO34 = 3 geçiş) kod/entity adlarına uygulanmadan önce doğrulanmalıdır. Bu adlandırma standardı önerilmiştir; firmware veya HA entity adları henüz değiştirilmemiştir.

Ayrıntı: [ADR-027](docs/decisions/ADR-027-single-channel-training-datasets.md). T007/T008 veri hattı uygulaması ve gerçek eğitim çıktısı tamamlanmış değildir.


## 2026-11-06 — ADR-027 kanal kimliği / değişebilir geçiş sayısı netleştirmesi

Kullanıcı düzeltmesi: CH2 için kayıtlı 4 geçiş ve CH3 için kayıtlı 3 geçiş değerleri ileride değişebilir. Bu nedenle geçiş sayısı kalıcı kanal kimliğine eklenmeyecek.

- Kalıcı kanal kimliği yalnız `CH1`, `CH2`, `CH3` olacaktır.
- Fiziksel geçiş/sarım sayısı `turn_count` adıyla ayrı, değişebilir donanım/deney metadata'sı olarak tutulacaktır.
- Mevcut 1/4/3 geçiş bilgisi yalnız mevcut kayıtlı fiziksel durumu ifade eder; sabit özellik değildir.
- Yapılandırma değiştiğinde yeni kayıtlar yeni `turn_count` değerini taşır; eski eğitim/ham veriler toplandıkları zamanki değerle korunur.
- `CH1-1T`, `CH2-4T`, `CH3-3T` birleşik biçimleri kalıcı kanal kimliği olarak kullanılmayacaktır.

ADR-027 ve Python mimarisi bu ayrımla güncellendi. Firmware ve HA entity isimleri değiştirilmedi.


## 2026-11-06 — Eğitim verisi için History kanal adlandırması netleştirildi (ADR-027)

Kullanıcı kararı:
- Gün içindeki genel deneylerde ve gözlemde History kanal adları genel kalır: `CH1`, `CH2`, `CH3`. History'de çok sayıda deney kaydı bulunabilir; bunlar otomatik olarak eğitim verisi değildir.
- Kod/ölçüm yapılandırması kesinleştikten ve özellikle eğitim verisi toplanmasına karar verildikten sonra ilgili kodda küçük bir adlandırma değişikliği yapılır. Eğitim amaçlı akış adı `CH1-E`, `CH2-E` veya `CH3-E` olur.
- `-E` eki eğitim amacıyla yayınlanan History akışını işaretler; fiziksel kanal kimliğini, sarım sayısını veya hesaplama yöntemini tanımlamaz.
- Python-1 kaynak CSV'yi içerik/entity adlarını değiştirmeden arşivler; bu üç eğitim adının CSV'de bulunması Python-1'in genel dosya kabul koşulu değildir.
- Python-2/eğitim hazırlama aşaması `CH1-E`, `CH2-E`, `CH3-E` adlarını açık seçim anahtarları olarak kullanır. Genel `CH1` / `CH2` / `CH3` deney kayıtları kendiliğinden eğitim setine alınmaz.
- Eski bir deney kaydı sonradan eğitim için seçilirse kaynak arşiv değiştirilmez; kanal seçimi ve eğitim adı ayrı türetilmiş kopyada uygulanır.
- Sarım sayısı, katsayı ve hesaplama yöntemi gerektiğinde deney/eğitim kodunda tanımlanır; kanal adına eklenmez.

Bu karar ADR-027, Python mimarisi, T007, ROADMAP ve STATUS belgelerine işlendi. Firmware/HA entity kodu değiştirilmedi; gerçek eğitim kaydı henüz başlatılmadı.


## 2026-11-06 — E15 eğitim kanal adı / History doğrulama deneyi planlandı

Kullanıcı isteğiyle E15 oluşturuldu: günlük deney adları CH1/CH2/CH3 olarak kalırken, eğitim verisi alınmasına karar verildiğinde kodda küçük adlandırma değişikliği yapılarak CH1-E/CH2-E/CH3-E akışlarının Home Assistant History'de görünmesi ve CSV dışa aktarımında gerçek entity_id değerleriyle doğrulanması sınanacak.

- Deney dosyası: [E15 — Eğitim işaretli kanal adlarının Home Assistant History doğrulaması](experiments/E15-training-channel-history-naming/README.md).
- Yalnız adlandırma alanları değişecek; pin, ölçüm hesabı, K, sample_duration, update_interval, okuma sırası ve olay protokolü korunacak.
- Önce çalışan YAML ve Git SHA sabitlenecek; deney YAML ayrı dosyada hazırlanacak.
- Görünen ad ile gerçek entity_id ayrı ayrı kontrol edilecek; HA entity registry'nin eski entity_id'yi koruma ihtimali varsayılmayacak.
- Python ve eğitim veri üretimi bu deneyin kapsamı değildir.
- **Durum: PLANLANDI.** Kod değişikliği, derleme, OTA, History kaydı ve CSV doğrulaması yapılmadı.


## 2026-11-06 — ADR-028: Kararlı alan SCT ile kapanacak

Kullanıcı kararı:
- Kararlı alan, aynı ON paketi içinde SCT ve PZEM kendi akışlarında birlikte kararlı olduğunda açılır.
- Kararlı alan, SCT kendi akışında kararlılığını kaybettiğinde kapanır.
- PZEM kararlılığı yalnızca başlangıç koşuludur; bitiş tetikleyicisi değildir.
- Gerekçe: Yük OFF olduğunda PZEM akımı gecikmeli gösterebilir. SCT yük değişimini daha erken yakaladığı için PZEM'in OFF/kararsız görünmesi beklenmez.
- OFF olay işareti ON paket bütünlüğünü kapatma/doğrulama görevini sürdürür; kararlı alanın istatistiksel bitiş ölçütü değildir.

Karar [ADR-028](docs/decisions/ADR-028-stable-window-sct-boundaries.md) olarak kaydedildi ve [E12](experiments/E12-sct-stability-window-and-response/README.md) deney belgesine işlendi.

**Henüz belirlenmeyenler:** SCT kararlılık kaybının istatistiksel tanımı, pencere boyu, dağılım/ortalama değişimi sınırları ve devam süresi. Bunlar veriden belirlenecek; eşik uydurulmayacak.

**Uygulama durumu:** Python algoritması yazılmadı. Firmware/YAML değişikliği, derleme veya OTA yapılmadı. E12 devam ediyor; tamamlanmış değildir.
