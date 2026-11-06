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


## 2026-11-06 — Modül 2 CH1-1T 2 Hz ilk cihaz logu

- E14 deney firmware'i `exp/modul2-ch1-2hz-20261106` dalında korundu; YAML blob SHA `afe5a689832b4d78b78c1bd1a0d8971301d2caaf`. Cihaz logu ESPHome 2026.10.2 derleme zamanını, API bağlantısını ve GPIO32/33/34/35 ADC init OK sonuçlarını gösteriyor.
- Kısa cihaz logunda CH1 128 yayın ve 0,500 s medyan aralıkla nominal 2 Hz; CH2 32 yayın / 2,000 s; CH3 32 yayın / 2,001 s gözlendi. CH1 tek tek aralıkları 0,335–0,669 s olduğundan uzun süreli tam zamanlama garantisi verilmez.
- Modül 3 EVENT_ID 1897 ON ve 1898 OFF paketleri aynı BOOT_ID ile Modül 2'ye ulaştı ve HA entity'lerine yayınlandı. Bu iki olay için kayıp görülmedi; genel kayıpsızlık veya fiziksel SSR anahtarlaması kanıtlanmadı.
- Kullanıcının yüksüz olarak tanımladığı koşulda ON aralığında üç kanal medyanları yükseldi; OFF sonrası yaklaştı. OFF'tan yaklaşık 3 s sonra CH1'de 0,491 A tekil tepe görüldü. Tek çevrim neden tayini için yeterli değildir; ham veri korunacak, filtre/eşik kararı verilmeyecek.
- Ham log ve ön analiz: [cihaz logu](logs/module2/2026-11-06-module2-ch1-2hz-device-log.txt), [analiz](logs/module2/2026-11-06-module2-ch1-2hz-log-analysis.md). Kaynak log SHA-256 `b2f0e86f0053eb24c3455a7ee279cbdc1805c72dae5e7b4f8dbacc130a4d562d`.
- **Durum:** Kısa cihaz çalışma doğrulaması LOG İLE DESTEKLENDİ; E14 açık. Uzun süreli 2 Hz, tekrarlı ON/OFF çevrimleri, PZEM/HA History eşleşmesi ve fiziksel SSR doğrulaması bekliyor.


## 2026-11-06 — E14 üç örnekleme hızı karşılaştırması

- Kullanıcı fiziksel olarak ölçüm hattında yük olmadığını doğruladı. Modül 3 ON/OFF mesajları fiziksel yükün açık/kapalı olduğu anlamına gelmez; yalnızca olay işaretidir. 100 W akkor ampul kullanıcı tarafından yalnızca test başlatma talimatı verildiğinde fiziksel olarak açılacak.
- E14 deney YAML'ı ayrı dalda güncellendi: `exp/modul2-ch1-2hz-20261106`. Yeni düzen CH1=500 ms (2 Hz), CH2=1 s (1 Hz), CH3=2 s (0,5 Hz). Üç kanalda sample_duration=100 ms, K=24.22 sabit.
- CH2 her 1 saniyede okunur; her ikinci çevrimde CH3 ve ortak bias da okunur. CH1 bağımsız 500 ms aralığını korur.
- Yeni YAML blob SHA: `9bc6237ea9a312b6ff22a4f16c99c0f5f96fd382`. Henüz Validate/Compile, OTA veya cihaz testi yapılmadı.
- **Sonraki sıra:** YAML Validate + Compile → OTA → yüksüz baz çizgi → kullanıcı talimatıyla 100 W akkor ampul ON → kararlı yük kaydı → ampul OFF ve kapanış kaydı. Fiziksel açma/kapama kullanıcı kontrolündedir.


- 2026-11-06 genişletilmiş yüksüz kayıt (5 dk 37 sn, 4.104 satır) arşivlendi: [ham log](logs/module2/2026-11-06-module2-idle-extended-source.txt), [analiz](logs/module2/2026-11-06-module2-ch1-2hz-log-analysis.md). Kullanıcı kayıt boyunca fiziksel yük olmadığını doğruladı; UDP ON/OFF yalnız olay işaretidir.
- Eski firmware ile CH1 674 yayın / 0,500 s medyan; CH2 169 / 2,000 s; CH3 168 / 2,000 s. CH1 tekil aralıkları 0,004–1,158 s; düzenli 2 Hz garantisi henüz yok. Yüksüz gösterge medyanları CH1 0,2725 A, CH2 0,216 A, CH3 0,252 A; fiziksel akım olarak yorumlanmaz.


## 2026-11-06 — PZEM History geçiş değerlerinin paket ortalaması olarak değerlendirilmesi

- Kullanıcı, PZEM History grafiğinde açma/kapama geçişlerinde görünen akımın anlık fiziksel akım olarak yorumlanmaması gerektiğini belirtti. Tarif edilen beşli örnek: `1,1,1,1,1 → 1,0`; `1,1,1,1,0 → 0,8`. Bu, önceki örneklerin geçiş sonrasındaki değere katkı verdiği paket/beşli ortalama davranışıyla uyumludur.
- **KULLANICI GÖZLEMİ / HESAP:** Geçiş kenarındaki PZEM ara değerleri kararlı SCT/PZEM alan istatistiklerine katılmayacak. PZEM'in kararlı açık/kapalı alanları durum ve zaman aralığı belirlemede kullanılabilir; PZEM mutlak ground truth değildir.
- PZEM'in iç firmware/Modbus ortalama algoritması incelenmedi. Kesin iç algoritma iddiası yoktur; kayıt gözlenen History davranışının yorumudur.
- SCT örnekleme hızı karşılaştırmasında PZEM referans ölçütü değildir. Üç SCT kanalı kendi kararlı ON alanlarında ayrı ayrı ve ortak yük davranışına göre değerlendirilecektir.
- Ayrıntı: [PZEM History geçiş davranışı gözlemi](logs/module3/2026-11-06-pzem-history-packet-average-observation.md).
- Sonraki kanal eşleştirme deneyi için kullanıcı başlangıcı 2026-11-06 12:01:00 (+03:00); CH1←önceki SCT3, CH2←önceki SCT1, CH3←önceki SCT2. Yeni CSV bekleniyor.


## 2026-11-06 — E14 ikinci ve üçüncü karşılaştırma gözlemleri

- **2. Üç örnekleme hızı:** CH1=2 Hz, CH2=1 Hz, CH3=0,5 Hz düzeninde kullanıcı ilk gözleminde CH2'nin daha az sapma gösterdiğini bildirdi. Bu henüz nitel gözlemdir; referans ve sayısal sapma yeni veriyle hesaplanacak. CH2'nin daha doğru olduğu veya 1 Hz'in üstünlüğü henüz kanıtlanmış değildir.
- **3. Fiziksel kanal değişimi:** Donanım kanalları değiştirildi. Yeni eşleştirme 12:01 (+03:00) itibarıyla CH1←önceki SCT3, CH2←önceki SCT1, CH3←önceki SCT2. Amaç sensör/yerleşim etkisini ESP/ADC kanal etkisinden ayırmaktır. Yeni CSV bekleniyor.
- E14'nin üç adımı ve kanıt sınırları: [E14 deney kaydı](experiments/E14-module2-single-channel-2hz/README.md).

## 2026-11-06 — E14 üçüncü test basamağı: kodda örnekleme profilini kaydırma
- Deney zinciri: (1) PZEM History geçiş davranışını değerlendirme ve geçiş örneklerini kararlı istatistiklerden dışlama; (2) kod/GPIO eşlemesi sabitken üç fiziksel SCT sensörünü değiştirerek sensör etkisini araştırma; (3) fiziksel sensör yerleşimini sabit tutup örnekleme profillerini kodda kaydırma.
- Sensör eşlemeleri: ilk yerleşim SCT1→CH1, SCT2→CH2, SCT3→CH3; ilk değişim SCT1→CH3, SCT2→CH1, SCT3→CH2; 12:15 ikinci değişim SCT1→CH2, SCT2→CH3, SCT3→CH1. Son yerleşim bu aşamada sabit.
- Kullanıcı gözlemi: sensörler değişmesine rağmen CH2 tekrar daha az sapmalı/kararlı göründü; neden henüz kesin değil.
- Yeni firmware profili: CH1=1 Hz, CH2=0,5 Hz, CH3=2 Hz. Önceki sıra CH1=2 Hz, CH2=1 Hz, CH3=0,5 Hz.
- sample_duration=100ms, K=24.22, GPIO ve entity eşlemesi sabit. CH1 1 s, CH2 2 s, CH3 500 ms. Ortak bias CH2'nin okunduğu çevrimde okunur.
- Beklenti: avantaj CH1'e taşınırsa 1 Hz profil hipotezi desteklenir; CH2'de kalırsa GPIO/ADC veya kanala özgü etki olasılığı güçlenir.
- YAML yazıldı; Validate/Compile, OTA ve cihaz testi henüz yapılmadı.

## 2026-11-06 — E14 uzun kayıt sonrası örnekleme profilinin CH3'e taşınması

- 12:30 sonrası HA History CSV'si 12:30:00–12:47:15 aralığını kapsıyor: CH1 1.036, CH2 518, CH3 2.072, PZEM 105 kayıt.
- PZEM yaklaşık 0,46–0,48 A kararlı bölümlerinde, bölüm başı/sonundan ikişer saniye dışlanarak hesaplanan standart sapmalar: CH1 0,0212 A; CH2 0,0340 A; CH3 0,0191 A. Bu kayıtta en düşük sapma CH3'tedir; CH1 yakındır. Önceki kısa kayıt sonucu uzun kayıtta aynı şekilde sürmemiştir.
- Kullanıcı kararı: 1 Hz profil CH1'den CH3'e taşınacak. CH1 eski CH3'ün 2 Hz profilini alır; CH2 0,5 Hz'de kalır; CH3 1 Hz olur.
- Güncel profil: CH1 GPIO32=2 Hz (500 ms), CH2 GPIO33=0,5 Hz (2 s), CH3 GPIO34=1 Hz (1 s). sample_duration=100ms, K=24.22, GPIO/entity ve fiziksel sensör eşlemesi sabit. Bias CH2 ile 2 saniyelik taramada okunur.
- Firmware YAML deney dalına işlendi. **Validate/Compile, OTA ve fiziksel cihaz testi henüz yapılmadı.** E14 açık.
- Ayrıntı: [E14 deney kaydı](experiments/E14-module2-single-channel-2hz/README.md).


## 2026-11-06 12:52 — E14 yeni örnekleme koduyla kayıt başlangıcı

- Kullanıcı, yeni kodla kayıt başlangıcını 12:52 (+03:00) olarak bildirdi.
- Aktif profil: CH1=2 Hz, CH2=0,5 Hz, CH3=1 Hz; her kanalda sample_duration=100 ms, K=24.22.
- Deney amacı tek bir kanalı seçmek değil, üç kanalın da aynı fiziksel koşullarda tutarlı ve tekrarlanabilir ölçüm üretmesini değerlendirmektir.
- Bu kayıt başlangıcı kullanıcı bildirimidir; yeni cihaz logu/HA History verisi henüz incelenmedi. Fiziksel yük durumu ayrıca doğrulanmadan varsayılmayacaktır.
- Ayrıntı: [E14 deney kaydı](experiments/E14-module2-single-channel-2hz/README.md).


## 2026-11-06 — E14 12:52 sonrası yeni profil ilk HA History analizi

- Kullanıcının sağladığı `history (41).csv` toplam 57.116 satır ve 11:00:00–12:59:09 (+03:00) aralığını kapsıyor. Yeni profil analizi yalnız 12:52:00 sonrasına uygulandı.
- HA timestamp'lerinde yayın ritmi: CH1 852 kayıt / 0,500 s medyan; CH2 214 kayıt / 2,000 s; CH3 426 kayıt / 1,000 s. Yeni 2 Hz / 0,5 Hz / 1 Hz profilinin HA tarafında çalıştığı destekleniyor.
- İlk altı tam ON kararlı alanında (ON+8 s ile OFF−5 s): CH1 n=324, ortalama 0,4758 A, std 0,0274 A; CH2 n=78, ortalama 0,4737 A, std 0,0261 A; CH3 n=162, ortalama 0,4699 A, std 0,0226 A. Medyanlar sırasıyla 0,4701 / 0,4713 / 0,4653 A.
- PZEM yüksek akım örnekleri 0,470–0,473 A bandında, ortalama 0,4715 A. PZEM yüksek güç örnekleri yaklaşık 91,2–110,4 W.
- Bu kısa kayıtta CH3 std sapması en düşük olsa da altı çevrim örnekleme hızının nedensel etkisini veya kanal üstünlüğünü kanıtlamaz. Kullanıcı hedefi üç kanalın birlikte tutarlı ve tekrarlanabilir olmasıdır; profil değişikliği/kanal eleme kararı alınmadı.
- Ham CSV bu commit'e eklenmedi; analiz kullanıcı tarafından sağlanan konuşma dosyasından yapıldı.
- Ayrıntı ve yöntem: [E14 deney kaydı](experiments/E14-module2-single-channel-2hz/README.md).


## 2026-11-06 — E15 tek SCT kanalında yayın aralığı deneyi açıldı

- **HEDEF:** Üç kanallı ortak çalışma düzenini devreden çıkarıp yalnız CH1-1T/GPIO32 ile yayın aralığının gözlenen sıçrama davranışına etkisini incelemek.
- **Deney matrisi:** A=500 ms (2 Hz), B=1 s (1 Hz), C=2 s (0,5 Hz); her tur 30 dakika. Sıra A→B→C.
- **Sabitler:** sample_duration=100 ms, K=24.22, aynı fiziksel SCT/1T/kablo/ADC pin/ölçülen iletken ve aynı fiziksel yük/kararlı koşul. Turlar arasında yalnız interval satırı değişecek.
- **Deney kodu:** [E15 tek kanal YAML](firmware/experiments/bero-modul2-e15-single-sct-interval.yaml). Ana üç kanallı firmware üzerine yazılmadı. ESPHome cihaz kimliği esp32d1 korundu. CH2/CH3 SCT ve GPIO35 bias ADC okumaları kapalı; UDP 4210 olay alıcısı tüm turlarda aynı bırakıldı.
- **Değerlendirme:** Ardışık yayın farkı dağılımı, sıçrama genliği yüzdelikleri, ortak eşik üzerindeki sıçrama sayısı, dakika başına ve 1.000 yayın başına oranlar, SD ve gerçek HA timestamp aralıkları.
- **Yorum sınırı:** 2 saniyelik örnekleme iki yayın arasında oluşup kaybolan kısa olayları kaçırabilir. Bu nedenle sayımlar gerçek fiziksel sıçrama olaylarının tam sayısı değil, yayın akışında gözlenen sıçramalardır. Ortak sıçrama eşiği sonuçlar görülmeden belirlenecek.
- **KANIT / DURUM:** Protokol ve ayrı YAML depoya eklendi. ESPHome Validate/Compile, OTA ve fiziksel ölçüm yapılmadı. E15 PLANLANDI/HAZIRLANDI; test başladı veya tamamlandı denemez.
- Ayrıntı: [E15 protokolü](experiments/E15-single-sct-publish-interval/README.md), [sonuç defteri](experiments/E15-single-sct-publish-interval/results.md).


## 2026-11-06 — E15 tur süresi revizyonu

- Kullanıcı kararıyla E15'in her tur süresi 30 dakikadan **10 dakikaya** indirildi. A/B/C sırası ve 500ms → 1s → 2s aralıkları değişmedi.
- Nominal kayıt beklentileri: A yaklaşık 1.200, B 600, C 300 CH1 sonucu. Gerçek kayıt adedi HA timestamp'lerinden belirlenecek.
- sample_duration=100ms, K=24.22 ve tek SCT/CH1 donanım koşulu sabit. Yalnız tur süresi revize edildi.

## 2026-11-06 — E15 ilk cihaz çalışma kontrolü

- E15 A turu için ESPHome 2026.10.2 cihaz logu incelendi. API bağlantısı/handshake başarılı; ESP32D1 Wi-Fi bağlantısı mevcut.
- GPIO32 / ADC1_CH4, 12 dB ADC başlatma, config ve calibration durumları OK. ct_clamp sample_duration=100ms ve update_interval=never olarak raporlandı.
- 28.492 saniyelik kısa logda 58 CH1 akım yayını bulundu; medyan yayın aralığı 0.500s, gözlenen aralık 0.427–0.577s.
- Modül 3 UDP EVENT_ID=314 / STATE=OFF paketi alındı ve olay text_sensor alanlarına yayınlandı. UDP STATE fiziksel yük durumunun kanıtı değildir.
- **Durum:** İlk cihaz çalışma kontrolü LOG İLE DESTEKLENDİ. Bu kayıt 10 dakikalık A turu değildir; A/B/C tur sonuçları ve sıçrama karşılaştırması bekliyor. Logdaki yapılandırma adı esp32d1.yaml olduğundan depo E15 YAML snapshot'ı ile binary arasında birebir hash bağı kurulmadı.
- [Ham log](logs/module2/2026-11-06-e15-a-500ms-initial-device-log.txt); [analiz](logs/module2/2026-11-06-e15-a-500ms-initial-device-log-analysis.md); [E15 sonuç defteri](experiments/E15-single-sct-publish-interval/results.md).


## E15 ana hedef ve üç yayın aralığı için beklenen sonuç — 2026-11-06

**Kullanıcı tarafından netleştirilen ana hedef:** Katsayısız CH1-1T akım çıktısında, kararlı fiziksel koşul içindeki tekil ölçümlerin kendi ortalamasına yakınlığını iyileştirmek. Değerlendirme standart sapmayı tek başına hedef almayacaktır. Esas konu, ortalamadan sapmaların **ne sıklıkta** oluştuğu ve oluştuğunda **ne kadar büyük** olduğudur.

**E15'in bu üç turlu deneyine ait beklenti:** 500 ms, 1 s ve 2 s yayın aralıklarında bu sapma davranışının belirgin biçimde değişmemesi beklenmektedir. Deneyin sorusu, yayın aralığını değiştirmekle tekil ölçümlerin ortalamaya yakınlığının değişip değişmediğidir. Üç turda benzer sonuç çıkması, yayın aralığının bu kararlı durum sapma davranışında belirgin etkisi olmadığı yönünde kanıt sağlayacaktır; farklılık çıkması ise ayrıca incelenecektir. Bu beklenti sonuç değildir ve ölçümle sınanacaktır.

**Ana değerlendirme ölçütleri:**
- Her turun aynı kuralla seçilmiş kararlı bölümlerinde ortalama akım referans alınır; her tekil ölçüm için mutlak ortalamadan sapma hesaplanır: |I[n] − ortalama|.
- Önceden belirlenmiş ortak tolerans bandının dışında kalan tekil ölçümlerin adedi ve toplam geçerli ölçümlere oranı: sapma sıklığı.
- Tolerans dışı ölçümlerin ortalama, P95 ve maksimum mutlak sapması: sapma miktarı.
- Tüm ölçümlerde mutlak sapmanın medyanı ve P95'i de raporlanır; böylece yalnız eşik dışındaki değerler değil genel yakınlık da görünür.
- Tur süreleri ve yayın adetleri farklı olduğundan sıklık hem ölçüm başına oran (%) hem 1.000 yayın başına adet olarak verilir. Dakika başına adet yardımcı göstergedir.
- Tolerans bandı sonuçlar görülmeden, üç tur için ortak biçimde belirlenmelidir. Sayısal tolerans henüz kararlaştırılmamıştır; belirlenmeden eşik dışı sayım üzerinden üstünlük ilan edilmeyecektir.

**Zaman notu / kullanıcı bildirimi:** Görseldeki mevcut K=24.22 uygulanmış kararlı durum gözlemi 2026-11-06 saat 13:49'da başladı. Kullanıcı 14:00'te yeni koda geçmeyi planladığını bildirdi. Bu zaman bilgisi kullanıcı beyanıdır; görsel tek başına tam kayıt aralığı veya 10 dakikalık tur tamamlandığını kanıtlamaz.

**Yorum sınırı:** Daha seyrek yayın aralığı iki yayın arasında oluşup kaybolan sapmaları örneklemeyebilir. Bu nedenle üç turdaki benzerlik/farklılık yalnız yayımlanmış tekil değerlerin gözlenen davranışı için yorumlanacaktır; örneklenmeyen fiziksel olayların yokluğu anlamına gelmez.


## Kullanıcı tarafından netleştirilen eğitim penceresi sınırı — 2026-11-06

Bu kural, önceki simetrik SCT/PZEM kararlı-aralık kesişimi tarifini **eğitim penceresinin sınırlandırılması bakımından** ayrıntılandırır:

- Açılışta SCT ve PZEM kendi akışlarında bağımsız değerlendirilir.
- SCT kararlı duruma ulaşmış olsa bile PZEM henüz kararlı değilse eğitim başlamaz; PZEM'in kararlı olması beklenir.
- **Eğitim başlangıcı:** SCT kararlı VE PZEM kararlı koşullarının ikisi de ilk kez sağlandığında, yani iki kararlılık başlangıcının daha geç olanı.
- **Eğitim bitişi:** SCT akımın kesildiğini algıladığı anda. PZEM'in kapanış gecikmesi veya mavi serinin daha sonra düşmesi beklenmez.
- Eğitim çıktısına yalnızca bu başlangıç ve bitiş arasında kalan K=24.22 katsayısı uygulanmış SCT tekil ölçümleri alınır. PZEM ölçümleri kararlılık/etiket referansı olarak kullanılır; SCT tekil değerleri PZEM'e eşitlenmez, timestamp üzerinden birebir eşleştirilmez ve interpolasyon yapılmaz.
- Sabit bir süre, önceden seçilmiş zaman dilimi veya PZEM'in gecikmeli kapanış zamanı pencere sınırı değildir. Süre, verideki koşulların gerçekleşmesinin sonucudur.
- SCT kararlılık tespitinde tekil sıçramaların nasıl tolere edileceği henüz belirlenmemiştir. Bu istisna/kararlılık algoritması ayrı bir tasarım kararıdır; eşik veya pencere parametresi uydurulmayacaktır.
- Ham CSV ve tüm özgün ölçümler korunur; yalnızca seçilen SCT eğitim alt kümesi ayrı türetilmiş çıktı olarak üretilir.

Mantıksal ifade:

`start = max(SCT_STABLE_START, PZEM_STABLE_START)`

`end = SCT_CURRENT_CUTOFF`

Seçim aralığı `[start, end)` biçimindedir. `start >= end` ise eğitim örneği üretilmez ve açık dışlama nedeni raporlanır.

**Görsel yorum:** Kırmızı seri SCT, mavi seri PZEM'dir. Açılışta kırmızı önce yükselip kararlı olabilir; mavi daha sonra kararlı yatay seviyeye gelir. Eğitim ancak ikisi de kararlı olduğunda başlar. Kapanışta kırmızı SCT daha erken düşer; pencere orada biter, mavi PZEM'in gecikmeli düşüşü eğitim aralığını uzatmaz.

**Uygulama durumu:** Bu kayıt kullanıcı tarafından onaylanan pencere mantığıdır. SCT tekil sıçramalarına tolerans gösterecek kararlılık tespit algoritması ve parametreleri henüz belirlenmemiştir; otomatik uçtan uca Python uygulaması tamamlanmış sayılmaz.



## 2026-11-06 — Katsayı terminolojisi düzeltmesi

Önceki kayıtlarda geçen **“katsayısız”** ifadesi yanlıştı ve düzeltildi. E15/T008 kapsamında değerlendirilen SCT akım çıktısı, firmware'de `ct_clamp` filtresindeki `multiply: 24.22` ile katsayı uygulanmış değerdir. Amaç katsayıyı yok saymak değil; PZEM referanslı kararlı alanlardan mevcut K=24.22 katsayısını değerlendirmek ve gerekirse iyileştirmektir. Ham ADC/ct_clamp öncesi değer ile katsayı uygulanmış akım çıktısı birbirine karıştırılmayacaktır. Bu düzeltme ölçüm akışının ne olduğuna ilişkindir; yeni katsayı henüz hesaplanmış veya kabul edilmiş değildir.


## E15 B — 1 saniye kısa cihaz kontrolü (2026-11-06)

- Kullanıcı B turu kodunu cihaza yükledi ve kısa kontrol logunu paylaştı.
- ESPHome 2026.10.2; ESP32 rev3.1; derleme zamanı 14:12:57 +03:00. API çözümleme/bağlantı/handshake başarılı.
- GPIO32 / ADC1_CH4, 12 dB ADC init/config/calibration OK. ct_clamp sample_duration=100ms ve update_interval=never.
- CH1 katsayı uygulanmış akım entity'si 44 kez yayımlandı; 14:13:38.343–14:14:21.374 aralığında yaklaşık 43.0 saniye.
- Gerçek yayın aralığı medyanı 1.000 s; min 0.966 s; max 1.038 s; ortalama yaklaşık 1.001 s. Kısa kontrol B'nin 1 Hz ritmini doğruluyor.
- UDP EVENT_ID=370 / STATE=OFF alındı ve HA olay entity'lerine aktarıldı.
- OFF öncesi 33 ölçümün ortalaması yaklaşık 0.47085 A; OFF sonrası ilk değer 0.196 A. Bu yalnız betimleyici olay öncesi/sonrası gözlemidir; UDP STATE tek başına fiziksel yük durumunu kanıtlamaz.
- Log yaklaşık 43 saniyedir; 10 dakikalık B turu veya A/B/C sapma karşılaştırması değildir.
- ESPHome logu validated config cache'in esp32d1.yaml için kullanıldığını bildiriyor. Çalışan binary'nin depodaki B YAML snapshot'ıyla birebir hash eşleşmesi bu logla kanıtlanmıyor.
- [Ham log](../../logs/module2/2026-11-06-e15-b-1s-short-device-check.txt) ve [teknik analiz](../../logs/module2/2026-11-06-e15-b-1s-short-device-check-analysis.md) arşivlendi. B turunun resmi 10 dakikalık kaydı henüz tamamlanmadı.


## 2026-11-06 — E16 D/E/F ölçüm penceresi deneyi planlandı

Kullanıcı onayıyla E15'ten ayrı E16 deneyi planlandı. E15 A/B/C'de `sample_duration=100ms` sabit, yayın aralığı 500ms/1s/2s idi. E16 D/E/F'de bunun tersi uygulanacak: `interval=1s` sabit; yalnız `sample_duration` D=50ms, E=100ms, F=200ms olacak. Her tur 10 dakika; sıra D → E → F; toplam nominal kayıt 30 dakika.

- Tek kanal CH1-1T / sarı / GPIO32 (ADC1_CH4), K=24.22, 12dB ADC, aynı SCT ve fiziksel koşullar sabit.
- UDP 4210 olay alıcısı korunur; UDP kontrol döngüsü 100ms kalır. CH2/CH3 ve ayrı GPIO35 bias ADC okuması devre dışıdır.
- Öncelikli analiz çıktısı ct_clamp `on_raw_value` katsayısız çıktısıdır; ham ADC örneği olarak adlandırılmaz.
- D firmware dosyası oluşturuldu. Derleme, OTA ve gerçek cihaz doğrulaması henüz yapılmadı.
- Deney planı: [E16 README](experiments/E16-single-sct-window-duration/README.md); D YAML: [firmware](firmware/experiments/bero-modul2-e16-single-sct-window-d-50ms.yaml).


## 2026-11-06 15:01 — E16 D turu başladı

- Kullanıcı bildirimi: E16 D testi 15:01 (+03:00) itibarıyla başlatıldı.
- Aktif deney ayarı: tek SCT CH1-1T / sarı / GPIO32 (ADC1_CH4); `sample_duration=50ms`; yayın aralığı `interval=1s` (nominal 1 Hz); K=24.22; ADC attenuation 12dB.
- D turu hedef süresi 10 dakika; yaklaşık hedef bitiş 15:11 (+03:00). Ardından E=100ms ve F=200ms turları aynı 1s yayın aralığıyla yürütülecek.
- D firmware açıklamalarındaki E16 değişken tanımı düzeltildi; yapılandırma değerleri değiştirilmedi. YAML: `firmware/experiments/bero-modul2-e16-single-sct-window-d-50ms.yaml`.
- **Kanıt sınırı:** Başlangıç zamanı kullanıcı bildirimidir. Bu kayıt cihaz logu, OTA doğrulaması veya 10 dakikalık HA History kaydının tamamlandığı anlamına gelmez. Veri/log geldiğinde ayrıca incelenecek.
- Ayrıntı: [E16 deney kaydı](experiments/E16-single-sct-window-duration/README.md).


## 2026-11-06 — E16 D ön test kontrol logu incelendi

- Kullanıcının sağladığı kısa ESPHome logu 15:00:21.591–15:00:52.446 aralığını kapsıyor; 15:01 D turu başlangıcından hemen önce alınmış kontrol kaydıdır.
- ESPHome 2026.10.2, build 14:59:40; API bağlantısı/handshake başarılı; GPIO32 / ADC1_CH4, 12dB ADC init/config/calibration OK; ct_clamp sample_duration=50ms.
- 31 katsayısız CH1 yayını; medyan aralık 1.0005s (0.969–1.031s). Farklı ADC örnek sayısı 588–658 / 50ms (medyan 621).
- Kısa katsayısız çıktı özeti n=31, ortalama 0.014573, medyan 0.018340, popülasyon SD 0.006285, min 0.004460, max 0.021140. İlk düşük değerlerden sonra 15:00:32 civarında üst seviyeye geçiş var; kısa kesit tek kararlı pencere kabul edilmedi.
- Log validated config cache'in `esp32d1.yaml` için kullanıldığını söylüyor; depodaki D YAML ile binary arasında birebir hash eşleşmesi kanıtlanmıyor. Kısa kontrol logu 10 dakikalık D kaydı değildir.
- Ham log: [kontrol logu](logs/module2/2026-11-06-e16-d-50ms-pretest-control-log.txt); [analiz](logs/module2/2026-11-06-e16-d-50ms-pretest-control-log-analysis.md). Kaynak SHA-256: `f6b799c818552b7b14dd6bb42a4d7aeb1d4c18e72e6208efa0a4670da9355a60`.


## 2026-11-06 — E16 E turu firmware hazırlandı

- E turu YAML dosyası eklendi: `firmware/experiments/bero-modul2-e16-single-sct-window-e-100ms.yaml`.
- D turuna göre tek ayar farkı `ct_clamp.sample_duration: 50ms → 100ms`; SCT yayın aralığı `interval=1s` sabit.
- Tek kanal CH1-1T / GPIO32 / ADC1_CH4; K=24.22; ADC 12dB; UDP 4210 alıcısı korunuyor. CH2/CH3 ve ayrı GPIO35 ADC okuması yok.
- E16 değerlendirmesinin odağı fiziksel olarak doğrulanmış kararlı ON bölümlerindeki katsayısız ct_clamp çıktısının kararlılığıdır. OFF davranışı saklanır, ancak ON kararlılığı ölçütüne katılmaz.
- Kod depoya eklendi; derleme, OTA veya E turu başlangıcı henüz doğrulanmadı.


## 2026-11-06 — E16 E turu başlatıldı

- Kullanıcı bildirimi: yeni E16 kodu 15:16'da teste alındı.
- Yapılandırma: CH1-1T / GPIO32 / ADC1_CH4; `sample_duration=100ms`; `interval=1s`; K=24.22; ADC 12dB; UDP 4210 alıcısı korunur.
- Hedef süre 10 dakika; yaklaşık bitiş 15:26 (+03:00).
- Öncelikli analiz, fiziksel olarak doğrulanmış kararlı ON bölümlerindeki katsayısız ct_clamp çıktısının kararlılığıdır. OFF verisi korunur fakat ON kararlılığı başarı ölçütüne katılmaz.
- **Kanıt sınırı:** Başlangıç saati kullanıcı bildirimidir; cihaz logu, OTA/build doğrulaması veya 10 dakikalık HA History kaydı henüz görülmedi.
- Ayrıntı: [E16 deney kaydı](experiments/E16-single-sct-window-duration/README.md).


## 2026-11-06 — E16 E turu HA History analizi

- 15:16:00–15:26:00 (+03:00) aralığında 600 katsayısız CH1 yayını bulundu; medyan yayın aralığı 1.000s.
- Kararlı ON seçiminde SSR çevrimleri sınır olarak, PZEM akımı yükün kararlılığını kontrol etmek için kullanıldı. ON çevrimlerinin ilk/son 5 saniyesi çıkarıldı; 293 SCT değeri analiz edildi.
- PZEM 0.465–0.469 A. Katsayısız SCT ortalama 0.019264 A, medyan 0.019118 A, popülasyon SD 0.001034 A, CV %5.37, P05–P95 0.018083–0.020759 A, maksimum 0.027513 A.
- Çevrim içi ardışık farkların P95'i 0.002772 A, P99'u 0.006566 A. Ortak sıçrama eşiği önceden tanımlanmadığı için sıçrama adedi raporlanmadı.
- E sonucu tek başına pencere seçimi değildir; D/F aynı yöntemle karşılaştırılmalı.
- Analiz: [E16-E HA History](logs/module2/2026-11-06-e16-e-100ms-ha-history-analysis.md).
- Kaynak CSV SHA-256: `3338f48b30c6db379797bed89ffd6b68dcd04384ead8e1f31e6c9cb10be6dde3`. Ham CSV 3.86 MB; bu commit'e kopyalanmadı.


## 2026-11-06 — E16 F turu firmware hazırlandı

- F turu YAML eklendi: `firmware/experiments/bero-modul2-e16-single-sct-window-f-200ms.yaml`.
- E turuna göre tek ölçüm ayarı farkı `ct_clamp.sample_duration: 100ms → 200ms`; SCT yayın aralığı `interval=1s` sabit.
- Tek kanal CH1-1T / GPIO32 / ADC1_CH4; K=24.22; ADC 12dB; UDP 4210 alıcısı korunur. CH2/CH3 ve ayrı GPIO35 ADC okuması yok.
- Analiz odağı fiziksel olarak doğrulanmış kararlı ON bölümlerindeki katsayısız ct_clamp çıktısıdır. OFF verisi saklanır ancak ON kararlılığı ölçütüne katılmaz.
- YAML depoya eklendi; derleme, OTA veya F turu başlangıcı henüz doğrulanmadı.


## 2026-11-06 — İlk aşama: SCT ON eğitim istatistiği ve K katsayısı belirleme ilkeleri

Kullanıcı kararıyla eğitim/kalibrasyon istatistiği ile ilerideki canlı yük-değişimi istatistiği birbirinden ayrıldı. İlk aşamanın hedefi, fiziksel yük ON ve kararlı iken SCT'nin katsayısız ct_clamp çıktısından temsilî değer üretmek ve PZEM referansıyla K katsayısını belirlemektir.

- Eğitim verisine yalnız fiziksel olarak doğrulanmış, PZEM kararlılığıyla kontrol edilmiş ON alanları alınır. ON başlangıç geçişi ve OFF sonrası ölçümler eğitim hesabına girmez; OFF ham verisi arşivde korunur.
- UDP STATE fiziksel yük durumunun kanıtı değildir; olay işaretleyicisi olarak kullanılır. PZEM referanstır, mutlak ground truth olarak tanımlanmaz.
- Aday merkez kestiriciler: aritmetik ortalama, medyan ve önceden oranı belirlenmiş trimmed mean. Yayılım: SD, MAD / 1.4826×MAD, IQR, P05/P95. IQR uç değerleri otomatik silmez; işaretler. Ham veri değişmez kalır.
- Ardışık SCT yayınları bağımsız deney örnekleri sayılmaz; ON çevrimleri ayrı tekrarlar olarak özetlenir ve çevrimler arası tutarlılık değerlendirilir.
- K için aynı kararlı ON aralığından PZEM/SCT oranları çevrim bazında hesaplanır. Nihai kestirici, birleştirme yöntemi, minimum örnek sayısı, ON yerleşme süresi ve tolerans henüz kesinleştirilmemiştir. Birden fazla yük seviyesinde doğrulama gerekir.
- Her veri setinde SCT/sensör ve sarım bilgisi, GPIO/ADC, attenuation, sample_duration, interval, update_interval, K, YAML/commit/build, PZEM zaman serisi, yük, ON aralıkları, BOOT_ID/EVENT_ID, saat dilimi, kaynak CSV hash'i ve calibration_id kaydedilir.
- E15/E16 okuma parametrelerini değerlendirmeye veri sağlar; tek başına nihai K istatistiğini seçmez. Canlı yük değişimi algoritması bu belgenin kapsamı dışındadır.
- Ayrıntılı yöntem ve parametre kayıt şeması: [SCT ON eğitim verisi ve katsayı belirleme istatistiği](docs/ON-training-calibration-statistics.md).


## 2026-11-06 — E15 A/B/C + E16 D/E/F kararlı ON karşılaştırması

- Kullanıcının sağladığı `history (48).csv` (4,123,366 byte; SHA-256 `53bdf3315195688a1e6f47f9cebb6c46db95d1b7a4bb5029e4e183a457db01b5`) analiz edildi.
- Karşılaştırma yalnız katsayısız ct_clamp ON ölçümlerini içerir. Her SSR ON çevriminin ilk/son 5 saniyesi çıkarıldı; test penceresinden önce başlamış ON çevrimleri dışlandı; PZEM akımı seçilmiş ON aralıklarında kontrol edildi. OFF sonrası veriler ana istatistiğe alınmadı.
- A/B/C (100ms sample_duration; interval 500ms/1s/2s): ON n=581/271/135; medyan 0.019185/0.018939/0.018892 A; SD 0.001237/0.000712/0.000811 A.
- D/E/F (interval 1s; sample_duration 50/100/200ms): ON n=292/293/300; medyan 0.018682/0.019118/0.018869 A; SD 0.001745/0.001034/0.000820 A.
- D turunun SD'si 0.035284 A maksimum tekil değer nedeniyle belirgin yükseldi; D MAD 0.000572 A. IQR dışı değerler silinmedi, yalnız işaretlendi.
- Altı turda PZEM ON örnekleri yaklaşık 0.463–0.469 A. K oranları aday gösterge olarak hesaplandı; nihai katsayı seçilmedi.
- F aralığı CSV'deki 15:36:16–15:46:16 1 Hz segmentinden eşleştirildi; kullanıcı başlangıç bildirimi ve cihaz build/OTA logu ayrıca doğrulanmadı. A/B/C aralıkları cadence geçişlerinden eşleştirildi; binary/YAML hash doğrulaması yok.
- Tam yöntem, tablolar, trimmed mean, IQR işaretleri, K oranları ve yorum: [A–F kararlı ON karşılaştırma raporu](logs/module2/2026-11-06-e15-e16-a-f-on-only-comparison.md).

## 2026-11-06 — Eğitim yöntemi kararı: her ON çevriminde SCT–PZEM medyan çifti

Kullanıcı kararı: İlk katsayı eğitiminde her fiziksel olarak doğrulanmış kararlı ON çevrimi ayrı bir eğitim gözlemidir. Aynı kararlı zaman aralığında SCT ve PZEM okumalarının medyanları ayrı ayrı hesaplanır. Her ON çevriminin eğitim girdisi tek bir (SCT medyanı, PZEM medyanı) çiftidir; aritmetik ortalama merkez kestiricisi olarak kullanılmaz.

- Başlangıç SCT okuma tercihi tek kanal/tek yayın ve 500 ms aralıktır. Paket içine çoklu örnek eklenmeyecek; paket boyutu ve ESP firmware yükü artırılmayacaktır.
- 30 saniyelik kararlı aralıkta SCT için nominal yaklaşık 60 yayın beklenir. PZEM aynı zaman aralığındaki kendi geçerli okumalarıyla ayrı medyanlanır; SCT ile aynı örnek sayısına sahip olduğu varsayılmaz.
- Her çevrim için n_SCT, n_PZEM, ortak kararlı zaman aralığı, iki medyan ve yayılım ölçüleri kaydedilir. Çevrim katsayısı adayı K_j = PZEM_medyan / SCT_medyan olarak türetilebilir.
- Tek tek yayınlar bağımsız deney tekrarı sayılmaz; ON çevrimleri tekrarlı gözlemlerdir. Çevrimler arası nihai K birleştirme yöntemi henüz kararlaştırılmamıştır.
- Medyan merkezdir; MAD ve diğer yayılım ölçüleri medyanın tutarlılığını değerlendirmek için raporlanır. PZEM pratik referanstır, mutlak ground truth değildir.
- Minimum geçerli PZEM örnek sayısı ve kararlı pencere/yerleşme parametreleri henüz belirlenmemiştir.

Ayrıntı: [ON eğitim verisi ve katsayı belirleme istatistiği](docs/ON-training-calibration-statistics.md).

## 2026-11-06 — Sabit yükle ilk eğitim kapsamı

Medyan tabanlı ON çevrimi SCT–PZEM çifti yöntemi ilk aşamada sabit yükle eğitim içindir. Aynı fiziksel yük ve çalışma koşulunda tekrarlanan ON çevrimleri ayrı eğitim çiftleri üretir. Farklı yük/akım seviyeleri aynı havuzda birleştirilmez; sonraki aşamada her sabit yük seviyesi ayrı eğitim grubu olarak incelenir. Tek bir sabit yükte elde edilen K sonucu tüm akım aralığına genellenmez. Ayrıntı: [eğitim istatistiği](docs/ON-training-calibration-statistics.md).

## 2026-11-06 — İlk sabit yük eğitimi için training_config.yaml

- `config/training_config.yaml` oluşturuldu. Dosya, sabit yükte her ON–OFF çevrimi için tek SCT–PZEM medyan çifti üretme kararının Python parametre sözleşmesidir.
- Eğitim penceresi başlangıcı: SCT ve PZEM'in bağımsız kararlılık başlangıçlarından daha geç olanı. Bitiş: SCT akım kesilme anı; PZEM'in gecikmeli OFF düşüşü beklenmez.
- Merkez kestiricisi `median`; yayılım raporu MAD/IQR. Aritmetik ortalama eğitim merkez değeri değildir.
- Fiziksel sıfır-akım referansı I007 yüksüz havuzuna bağlandı. Bu referans ON eğitim çiftine katılmaz; SCT'nin ON sonundaki akım kesilmesini belirleme eşiğinin ileride türetilmesine kaynak olur.
- I007 taban dağılımı, SCT/PZEM kararlılık yöntemi/eşikleri ve minimum örnek sayıları henüz belirlenmedi. Bunlar `null` bırakıldı; ölçülmemiş eşik veya çalışır algoritma uydurulmadı.
- Entity kimlikleri T007 gerçek HA dışa aktarımıyla doldurulacak. Bu dosya parametre taslağıdır; uçtan uca çalışan Python uygulaması değildir.
- **Durum:** Yapılandırma dosyası depoya eklendi ve yeniden okunarak doğrulandı. Python uygulaması ve eşiklerin veriyle belirlenmesi beklemede.
- Dosya: [training_config.yaml](config/training_config.yaml).
