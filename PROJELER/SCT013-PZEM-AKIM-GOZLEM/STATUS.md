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
