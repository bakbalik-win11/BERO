# SCT013 – PZEM Akım Gözlem

## Bu çalışmanın yeri

Bu klasör, BERO'nun akım gözlem alt projesidir. BERO'nun tamamı değildir.

## Şu anki amaç

Önce masaüstündeki **Modül 4 (ESP32D2 + ADS1115 + SCT)** ile hedeflediğimiz akım aralığında ölçüm alabildiğimizi gözlemliyoruz. ADS1115 + SCT düzeniyle istenen aralıkta akım okunabildiğine dair mevcut deney kayıtları vardır. Şimdi aynı masaüstü düzeneğinde bias'lı ve bias'sız bağlantıyı karşılaştıracağız.

Bu karşılaştırmanın amacı bias'ın ölçüme gerçekten gerekli bir katkı sağlayıp sağlamadığını anlamaktır. Ardından iki yapının sinyalini osiloskopta birlikte inceleyeceğiz. **Bias gerekli mi sorusunun cevabı henüz verilmedi.**

Bias gerekli bulunursa, PREBERO Modül 5/6/7 için bias'ın ESP beslemesinden üretilmesi mi yoksa Modül 1'deki trafo/güç kutusu yapısının ikizlerinin yapılması mı gerektiğini ayrıca değerlendireceğiz. Bu besleme mimarisi de henüz seçilmedi.

## Çalışma sırası

1. Modül 4'te aynı ölçüm zinciriyle bias'lı ve bias'sız gözlem.
2. Bias'lı ve bias'sız sinyalleri osiloskopta inceleme.
3. Ölçüm ve sinyal gözlemlerine dayanarak bias gerekliliğine karar verme.
4. Bias gerekiyorsa PREBERO Modül 5/6/7 için bias besleme yöntemini seçme.
5. Ölçüm zinciri hedeflenen kullanım için yeterliyse PREBERO saha gözlemlerine geçme.

Bu sıra dışında yeni bir ölçüm mimarisi, çok kanallı sistem veya eğitim/veri hattı şu anki işin ön koşulu değildir. Önce elimizdeki masaüstü ölçüm düzeneğinin yeterliliğini ve bias ihtiyacını netleştiriyoruz.

## PREBERO

PREBERO, BERO'nun kurulacağı eve taşınma gerçekleşene kadar Sarıyer'deki mevcut evde yürütülecek hazırlık, gözlem ve veri toplama dönemidir. Bu kapsamda:
- **Modül 5:** Çamaşır makinesi gözlemi.
- **Modül 6:** Bulaşık makinesi gözlemi.
- **Modül 7:** Ana elektrik hattı + PZEM gözlemi.

Modül 5, 6 ve 7'nin tamamı PREBERO kapsamındadır. Bu modüller henüz imal edilmiş veya çalışır durumda kabul edilmez.

## Önceki çalışmaların yeri

Önceki SCT/ADC denemeleri, ADS1115 düşük akım karşılaştırmaları, PZEM gözlemleri ve eski Modül 2/3 çalışmaları tarihsel teknik kayıt olarak korunur. Bunlar bugünkü çalışma sırasını belirleyen aktif görevler değildir. Önceki ölçüm sonuçları, yalnızca gerçekten test edilmiş koşullarla sınırlı kanıt olarak değerlendirilir.

Ayrıntılı bias karar sırası: [ADR-034](docs/decisions/ADR-034-module4-bias-comparison-and-prebero-bias-supply.md).
Modül kimlikleri ve PREBERO tanımı: [ADR-033](docs/decisions/ADR-033-module-identities-desktop-and-prebero.md).

## Çalışan ölçüm baseline'ı

- ESP32D2 / E00F.
- ESPHome ct_clamp.
- SCT giriş GPIO33.
- sample_duration: 200ms.
- update_interval: 2s.
- Mevcut katsayı K=24.22.

Bu ayarlar önceki çalışan ölçüm yolunun tarihsel referansıdır. Güncel Modül 4 bias karşılaştırmasında kullanılan ayarlar ayrıca deney kaydında sabitlenecek; bu tarihsel baseline otomatik olarak yeni deneyin ayarı kabul edilmeyecektir. Her değişiklik ayrı kaydedilir ve derleme/gerçek donanım testiyle doğrulanır. [Firmware kaydı](firmware/esp32d2.yaml).

## Donanım referansları

- Öncelikli SCT: [SCT013-030 — 30 A / 1 V](hardware/references/SCT013-30A-1V.md).
- Diğer SCT/CT stokları: [donanım envanteri](hardware/inventory.md).
- PZEM-004T V3.0: [proje referansı](hardware/references/PZEM-004T-V3.0.md); PZEM'e bağlı CT modeli PZCT-02 (0–100 A) olarak kaydedilmiştir.
- Bias alt devresi: breadboard üzerinde 2 × 10 kΩ ve 104/100 nF kondansatör; [analog ön uç kaydı](hardware/frontend.md).
- ESP32D2, ESP32-WROOM ve diğer kartlar: [donanım envanteri](hardware/inventory.md).
- SSR ve DS3231, olay/zamanlama altyapısının donanım referanslarıdır.

## Öncelikli okuma sırası

1. [AGENTS.md](AGENTS.md) — çalışma protokolü.
2. [STATUS.md](STATUS.md) — güncel aktif görev.
3. [ROADMAP.md](ROADMAP.md) — yalnız iki ana faz.
4. [PROGRESS_TREE.md](PROGRESS_TREE.md) — genel görünüm.
5. [ADR-034](docs/decisions/ADR-034-module4-bias-comparison-and-prebero-bias-supply.md) — güncel bias deney sırası.
6. [Modül envanteri ve PREBERO](README.md#prebero).
7. [Deney arşivi](experiments/README.md) — önceki teknik çalışmalar.
11. [Karar kayıtları](docs/decisions/).

## Kapsam dışı

- Enerji analizörü veya güç kalitesi ölçümü.
- SCT'den PF/faz açısı hesabı.
- FFT, THD ve harmonik analiz.
- Sürekli ham ADC/50 Hz dalga kaydı ve örnek başına timestamp.
- Faz 1'de hedefe ulaşmak için artık gerekmeyen deneylerin yeniden açılması.

## Sensör okuma mimarisi ve tekrar kullanılabilir kod

ESPHome `ct_clamp` araştırmasından çıkan ortak sensör okuma yaklaşımı ve açıklamalı YAML örnekleri [firmware/patterns/README.md](firmware/patterns/README.md) altında tutulur.

- CT/AC akım: [ct-clamp-ac-rms-reference.yaml](firmware/patterns/ct-clamp-ac-rms-reference.yaml)
- Analog DC gerilim: [adc-dc-voltage-observer.yaml](firmware/patterns/adc-dc-voltage-observer.yaml)

Bu örnekler mevcut cihaz firmware'lerinin yerine geçmez. Her yeni sensörde pin, elektriksel aralık, sensör transfer fonksiyonu ve uygun sinyal işleme yöntemi doğrulanır. YAML'lar henüz derlenmiş veya fiziksel donanımda test edilmiş değildir.


## Kararlı alan eğitimi — olay ve ölçüm akışlarının ayrılması

Modül 2 ve Modül 3'te ölçüm verileri ile UDP olay/yayın verileri bağımsız kayıt akışlarıdır. Modül 2 SCT okumalarını ve aldığı UDP BERO_EVT/BOOT_ID/EVENT_ID/STATE olaylarını HA'ya ayrı ayrı aktarır. Modül 3 SSR durum değişiminde TIME içermeyen BERO_EVT mesajını UDP ile yayınlar; PZEM ölçümlerini ve olay kaydını HA'ya ayrı ayrı aktarır. Python SCT ve PZEM kararlılığını yalnızca kendi ölçüm akışlarından bağımsız tespit eder. UDP paket/zaman/ON-OFF bilgisi yalnızca deney ve olay çerçevesidir; kararlılığı veya kararlı alan sınırlarını belirlemez. Python önce Modül 2 SCT ve Modül 3 PZEM akışlarını kendi olay işaretleriyle paket aralıklarına böler; paketler BOOT_ID + EVENT_ID ile eşleştirilir. Her akışın kararlılığı yalnız kendi ölçüm değerlerinden bağımsız tespit edilir; ON–OFF aralığı otomatik olarak kararlı sayılmaz. Zaman damgaları akış içi olay sırasını ve paket sınırlarını kurmak için kullanılır; iki sensör örneğini timestamp ile birebir eşleştirme anahtarı değildir. TIME alanı olay protokolünden kaldırılmıştır. Geçerli karar sırası: [ADR-022](docs/decisions/ADR-022-packet-marker-segmented-training-streams.md) ve TIME alanını geçersiz kılan [ADR-023](docs/decisions/ADR-023-event-identity-without-time.md).


## Eğitim verisinin ON-only ilkesi

BERO'nun bu projesinde eğitim verisi **yalnız yükün açık (ON) olduğu dönemdeki kararlı SCT/PZEM alanlarının zaman örtüşmesinden** oluşturulur. Kapalı (OFF) alanlar hiçbir zaman eğitim verisi değildir ve iki sensör arasında eşleştirilmez. OFF olayı, ON paketini kapatır; ilk aşamada kapalı durum sıfır kabul edilir. Tam ON/OFF paket bütünlüğü, eğitim örneğinin geçerli deney aralığından geldiğini doğrulamak içindir; OFF okumalarını eğitime katmak için değildir.

OFF/yüksüz okumalar ON akım kalibrasyonuna katılmaz. Ancak farklı deneylerde biriken OFF örnekleri ileride ayrı bir veri havuzunda birleştirilerek gürültü tabanı ve kapalı durum eşiği/sınıflandırması için kullanılabilir. Gerekirse aç-kapa döngüsü olmadan, hatta yük bağlı değilken uzun bir yüksüz kayıt alınır. Bu ikinci öğrenme hedefi ilk aşama değildir. Uzun vadede Python'da geliştirilen ve doğrulanan eşik/modelin sahada hesaplama yapan ESP'ye aktarılması hedeflenebilir; bu mimari henüz tasarlanmamış/uygulanmamıştır.

Ayrıntı ve uygulama kuralı: [ADR-025](docs/decisions/ADR-025-raw-data-sct-model-behavior-validation.md) ve [E12](experiments/E12-sct-stability-window-and-response/README.md).

## Eğitim ve tam ham veri değerlendirmesi (ADR-025)

PZEM, SCT katsayısını/modelini öğrenmek için uygun kararlı alanların eşleştirilmesinde proje referansıdır. Eğitim için kararlı alanlar seçilse bile deneyin ham verisinin tamamı korunur. Öğrenilmiş model, açılma/kapanma ve geçişler dahil tam SCT kaydına ayrıca uygulanır.

Bu ikinci değerlendirmede Python'a deneyin bilinen ON/OFF koşulu ve yük aralığı verilir. PZEM'in geçişteki ardışık okumaları SCT'nin her örneği için noktasal doğruluk referansı yapılmaz. Bilinmeyen ara geçiş akımları uydurulmaz; sonuç bilinen deney koşullarına göre SCT davranış/tutarlılık değerlendirmesidir, mutlak doğruluk iddiası değildir. Tek veya alan bazlı katsayı seçimi gerçek veriye bırakılır.

Ayrıntı: [ADR-025](docs/decisions/ADR-025-raw-data-sct-model-behavior-validation.md).


## 2026-11-05 — Kalibrasyon ve eğitim yaklaşımının güncel özeti

Sabit yükler nihai kullanımın sınırı değil, PZEM ve SCT'nin aynı fiziksel koşuldaki bağımsız kararlı ON alanlarını güvenilir biçimde eşleştirerek doğru kalibrasyon referansı üretmenin aracıdır. Farklı fiziksel tepki ve hesaplama yöntemleri nedeniyle geçiş/interpolasyon değerleri katsayı eğitimine katılmaz. İlk 100 W ön karşılaştırması yaklaşık %3.34 merkez farkı göstermiştir; bu henüz Python eğitimi veya tüm aralık doğrulaması değildir. K=24.22 korunur. Farklı yüklerden yeterli veri toplandıktan sonra tek katsayı, doğrusal, polinom veya parçalı model seçenekleri bağımsız doğrulamayla değerlendirilecektir. Canlı çamaşır makinesi kaydı sonraki davranış/doğrulama aşamasıdır. Ayrıntı: [E12](experiments/E12-sct-stability-window-and-response/README.md).


## Uzun vadeli kullanım vizyonu — davranış izleme ve anomali tespiti

Bu alt proje, BERO'nun daha geniş hedefinin ilk akım ölçüm uygulamasıdır. BERO yalnızca ev makinelerinin programını veya çalışma evresini tahmin etmek için tasarlanmamaktadır. Uzun vadeli kullanım alanları şunlardır:

- **Çalışma karakteri çıkarımı:** çamaşır makinesi gibi cihazların çalışma evrelerini ve normal çevrim davranışlarını tanımak.
- **Ekipman anomali/arıza belirtileri:** havalandırma motoru veya kuyu hidroforu gibi ekipmanlarda akım seviyesi, çalışma süresi, devreye girme sıklığı ve davranış örüntüsündeki sapmaları izlemek. Sistem ilk aşamada kesin arıza teşhisi iddiasında bulunmaz; olası anomaliyi/bakım ihtiyacını işaretler.
- **Uzun dönem trend takibi:** hat veya ekipmanın akım seviyesinin günler/haftalar/aylar içindeki değişimini grafiklemek; kademeli yükselişleri, ani değişimleri ve normal çalışma bandından sapmaları görünür kılmak.

Çamaşır makinesi programı/evresi tahmini bu hedeflerden yalnızca biridir ve mevcut geliştirme için pratik bir başlangıç senaryosudur. Kısa vadeli testlerin hedefi ölçüm zincirini ve veri altyapısını güvenilir hâle getirmektir; uzun vadeli anomali analizi için de aynı tarihçeli ham veriden yararlanılacaktır.

Ölçüm kararlılığı yalnızca boş/yüklü ayrımı değildir. Tekil sıçrama filtreleme, örnekleri kısa süre toplama, süreklilik kontrolü ve pratik eşik gibi seçenekler deneylerle karşılaştırılabilir. Henüz belirli bir algoritma veya eşik seçilmemiştir. Ham ölçümler korunur; filtrelenmiş, özellik çıkarılmış ve trend verileri ayrı türetilmiş katmanlar olarak ele alınır.


## Örnek uzun dönem kullanım: hidrofor ve basınç tankı davranışının izlenmesi

Kuyu hidroforunun kısa aralıklarla sık devreye girip çıkması, basınçlı tankın hava ön şarjını kaybetmesi, diyafram hasarı veya tankın suyla dolması gibi durumlarla ilişkili olabilir. Benzer biçimde kat kaloriferi/ısıtma devresindeki genleşme tankının davranışı da uzun dönemli pompa çevrimleri ve basınç davranışıyla birlikte izlenebilir.

BERO'nun olası yaklaşımı anlık bir akım değerinden arıza teşhisi koymak değildir. Ekipmanın kendi normal davranışını zaman içinde öğrenmek; devreye girme sayısı, çalışma süresi, duruş aralığı ve akım karakterindeki değişimleri gün/hafta/ay ölçeğinde karşılaştırmaktır. Kullanıcı belirlediği koşullarda, örneğin normal döneme göre belirgin ve kalıcı sık çevrime girme görüldüğünde bildirim isteyebilir: "Hidrofor normalden sık devreye giriyor; basınç tankı, diyafram, ön şarj ve tesisat kontrolü önerilir."

Sık çevrime girme tek başına tank arızasını kanıtlamaz; su kaçağı, çekvalf, basınç şalteri, pompa kapasitesi veya tüketim düzeni gibi başka nedenler de araştırılmalıdır. Bu nedenle bildirim, kesin arıza teşhisi değil, ölçülen davranışa dayalı bakım/inceleme uyarısı olarak tasarlanmalıdır. Kullanıcı eşik ve bildirim sıklığını belirleyebilmelidir.

Bu örnek BERO'nun temel fikrini genişletir: ev ve ekipmanlar uzun dönemli elektriksel davranışlarıyla izlenir; geçmiş veriden yeni özellikler ve uyarılar üretilir. Ev, zaman içinde öğrenilen ve değişimi izlenen yaşayan bir sistem gibi ele alınır.


## Temel veri ilkesi — ham veriyi uzun süreli koruma ve geçmişten yeniden bilgi üretme

BERO'da ham ölçüm kayıtları uzun süreli ve değişmez biçimde korunur. Ham veri, yalnızca bugünkü analiz için kullanılan geçici girdi değildir; gelecekte geliştirilecek yeni filtreler, özellik çıkarım yöntemleri, davranış modelleri ve karşılaştırmalar için tarihsel kaynaktır.

Bugün gürültü, anlamsız veya kullanılmayan veri gibi görünen bir kayıt, ileride yeni bir analiz yaklaşımıyla anlamlı bir davranış göstergesine dönüşebilir. Bu nedenle geçmiş kayıtlar yeni yöntemlerle yeniden işlenebilir; geçmişteki ham veriden sonradan yeni özellikler, eğilimler, sınıflandırmalar ve bakım/anomali göstergeleri üretilebilir. Bu yaklaşım, geçmiş veriyi yeniden kullanılabilir bir bilgi kaynağı olarak ele alır.

Uygulama ilkeleri:
- Ham kayıtlar üzerine yazılmaz ve filtreleme/temizleme sırasında kaybedilmez.
- Filtrelenmiş, normalize edilmiş, etiketlenmiş ve özellik çıkarılmış veriler ham kayıttan ayrı türetilmiş çıktılar olarak saklanır.
- Her türetilmiş çıktının hangi ham veri aralığına ve hangi işlem/model sürümüne dayandığı izlenebilir olmalıdır.
- Yeni bir algoritma geliştirildiğinde, mümkün olduğu ölçüde yalnızca canlı veriye değil geçmiş ham veri arşivine de uygulanarak sonuçlar karşılaştırılır.
- Saklama süresi ve kapasite planı, uzun dönemli davranış analizi ihtiyacını gözetir; veri saklama mimarisi netleştirilirken zaman damgası, kaynak/kanal kimliği ve veri bütünlüğü korunur.

BERO bir hobi ve araştırma platformudur. Yanlış veya gereksiz bir anomali uyarısının servis çağrısı ya da otomatik bir ekonomik/operasyonel işlem başlatması söz konusu değildir. Bu nedenle farklı analiz yöntemleri ve eşikler rahatça denenebilir; sonuçları karşılaştırılır ve yorumlanır. Deney özgürlüğü, ham verinin korunması ve sonuçların dürüstçe değerlendirilmesiyle birlikte yürütülür.


## Bu alt projenin BERO içindeki yeri ve geliştirme ortamı

BERO, tek bir akım ölçer değil, farklı fiziksel değişkenleri izleyen sensörlerden oluşması hedeflenen çoklu sensörlü bir ev gözlem sistemidir. Akım sensörü bu sensörlerden yalnızca biridir. BERO kapsamındaki sensör örnekleri arasında su kuyusunda sıcaklık değişimi, kuyudaki basınçtan su derinliği çıkarımı ve ev girişinde şehir şebekesi su basıncı ölçümü de bulunur. Elektrik tarafında AC akım gözleminin yanında uygun sensör/ön uç ile DC akım ölçümü de ayrı bir yetenek alanıdır.

SCT013 + PZEM alt projesi bu geniş sistemin ilk ve teknik açıdan zor başlangıç uygulamasıdır. Buradan başlanmasının nedeni BERO'nun akım ölçümünden ibaret olması değil; akımı güvenilir biçimde ölçmek, canlı okumak ve zaman içinde başka programların/algoritmaların çıktılarıyla ilişkilendirmek zor bir mühendislik problemi olduğu için önce bu temel hattın hazırlanmasının tercih edilmesidir.

**PREBERO saha ortamı / nihai BERO ayrımı:** BERO'nun kurulacağı evdeki kiracı çıkıp taşınma gerçekleşene kadar, hazırlık ve saha veri toplama çalışmaları Sarıyer'deki mevcut evde yürütülür. Bu geçici dönem PREBERO'dur. Modül 5 çamaşır makinesini, Modül 6 bulaşık makinesini, Modül 7 ise mevcut evin ana elektrik hattını PZEM ile birlikte izlemek için planlanır. Amaç veri toplamak ve nihai BERO kurulumundan önce proje ilerlemesi sağlamaktır. Bu modüllerin imal edilmiş veya çalışır durumda olduğu iddia edilmez.


## PREBERO tanımı ve modül envanteri

**PREBERO**, BERO'nun kurulacağı eve henüz taşınılamadığı, o evdeki kiracı çıkana kadar Sarıyer'deki mevcut evde yürütülen hazırlık, gözlem, deney ve veri toplama dönemidir. Mevcut evdeki çamaşır makinesi, bulaşık makinesi ve ana elektrik hattı izlenerek veri toplanır; cihaz davranışları incelenir ve BERO'ya geçmeden önce proje ilerletilir. PREBERO nihai BERO kurulumu değildir.

| Modül | Tanım | Durum / amaç |
|---|---|---|
| **1** | Bias trafosu / güç kutusu | Mevcut, korunuyor. Modül 4 masaüstü biaslı/bias'sız karşılaştırma deneylerinde kullanılacak. |
| **2** | Eski üç kanallı biaslı SCT modülü | Fiziksel olarak imha edildi. ADS1115 ile istenen sınırlar içinde akım okunabildiği için eski fiziksel düzeneğe ihtiyaç kalmadı; kod ve kayıtlar tarihsel arşiv. |
| **3** | Eski PZEM + SSR olay modülü | Fiziksel olarak imha edildi; eski kod ve kayıtlar tarihsel arşiv. |
| **4** | Günlük masaüstü ESP32D2 + ADS1115 + SCT ölçüm düzeneği | Mevcut çalışma/deney düzeneği. Biaslı ve bias'sız ölçüm karşılaştırmaları burada yürütülür. |
| **5 — PREBERO** | Çamaşır makinesi gözlem modülü | Sarıyer'deki mevcut evde çamaşır makinesinden veri toplamak için imal edilecek. |
| **6 — PREBERO** | Bulaşık makinesi gözlem modülü | Sarıyer'deki mevcut evde bulaşık makinesinden veri toplamak için imal edilecek. |
| **7 — PREBERO** | Ana hat + PZEM gözlem modülü | Sarıyer'deki mevcut evin ana elektrik hattını PZEM ile birlikte izlemek için geliştirilecek. |

**Modül 5, 6 ve 7'nin tamamı PREBERO kapsamındadır.** Modül 7 tek başına PREBERO değildir. Bu üç modülün ortak amacı mevcut evde gözlem ve veri toplamak; BERO'nun kurulacağı eve geçmeden önce teknik ilerleme sağlamaktır.

Modül 5 ve 6 aynı elektronik tasarımın iki fiziksel kopyasıdır. Birincil gözlem kanalları ses ve titreşim, akım kanalı yardımcı/bağlamsal veridir. Her modül için ESP32-D + vidalı terminal shield, MAX4466, MPU6050, SCT013 30 A / 1 V ve ADS1115 planlanır. MPU6050 ve ADS1115 ayrı I²C bus'larında tutulacaktır; pinler fiziksel kart/shield kontrolünden sonra belirlenecektir. Ayrıntılar: [Modül 5 — Çamaşır makinesi](devices/washing-machine/README.md), [Modül 6 — Bulaşık makinesi](devices/dishwasher/README.md), [ADR-032](docs/decisions/ADR-032-washing-dishwasher-twin-sensor-modules.md).

**E22 bir modül değildir.** Modül 4'te bir kanalda 30 A / 1 V, diğer kanalda 100 A / 1 V SCT karşılaştırması yapılması fikridir; henüz bağlantı veya ölçüm yoktur: [E22 deney kaydı](experiments/E22-sct100a-1v-ads1115-characterization/README.md).

Güncel kimlik ve PREBERO kapsamının bağlayıcı kararı: [ADR-033](docs/decisions/ADR-033-module-identities-desktop-and-prebero.md).
