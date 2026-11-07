# E17 — CH1 düşük akım bölgesi: sürekli küçük yük gözlemleri

**Tarih:** 2026-11-07  
**Faz:** Faz 2  
**Durum:** AÇIK — 18 W kaydı sürüyor  
**İlişkili karar:** [ADR-031 — CH1 kapalı alan üst sınırı](../../docs/decisions/ADR-031-ch1-idle-closed-area-threshold.md)

## Amaç

CH1'in 0,24 A kapalı alan sınırının üzerindeki düşük akım davranışını kontrollü, sürekli bağlı küçük yüklerle gözlemek. Bu deneyin amacı düşük akım bölgesinde CH1'e zorla sayısal ölçüm yaptırmak veya K katsayısını kalibre etmek değildir. Amaç, fiziksel yük bulunduğunda SCT'nin verdiği tepkiyi görmek ve hesaplanmaması gereken alanı pratik olarak ayırmaktır.

## Mevcut alan sınıflandırması

- 0–0,24 A: CH1 kapalı alanı.
- 0,24–0,41 A: **hesaplanmadı alanı**; bu aralıkta yazılım sayısal akım değeri üretmeyecek.
- 0,41 A üzeri: hesaplanacak alan adayı; ilk güvenilir okuma sınırı kontrollü deneylerle doğrulanacaktır.

Bu sınırlar mevcut CH1 kurulumu ve K=24.22 bağlamındadır; diğer kanallara veya başka sensörlere otomatik genellenmez.

## E17-A — 18 W akkor ampul, sürekli açık

### HEDEF

18 W küçük akkor ampul bağlıyken PZEM referans akımını ve SCT CH1 tepkisini gözlemek. Röle anahtarlama etkisini deneyden çıkarmak.

### Bağlantı ve koşullar

- Yük: 18 W akkor ampul.
- Ampul, deney süresince sürekli yanık; açma/kapama çevrimi yok.
- Röle bu deneyde kullanılmıyor; dolayısıyla röle tetikleme/anahtarlama etkisi bulunmuyor.
- PZEM, hatta bağlı yükün referans akım/gerilim verisini üretiyor.
- SCT tarafında CH1 izleniyor.
- Kullanıcının bildirdiği deney başlangıcı: **10:21, 2026-11-07 (Europe/Istanbul)**.
- 10:14 civarındaki grafik hareketi PZEM'i devreye alma/bağlantı denemeleriyle ilişkilendirildi; deney başlangıcı sayılmayacak ve E17-A verisine dahil edilmeyecek.
- Firmware, K katsayısı ve örnekleme ayarlarında bu deney için değişiklik bildirimi yoktur; gerçek ayarlar CSV geldiğinde doğrulanacaktır.


### SSR anahtarlama etkisi — deneyden ayrıştırma

Bu deney, SSR anahtarlamasının SCT üzerindeki etkisini incelemek için değil, bu etkiden mümkün olduğunca bağımsız biçimde sürekli bağlı küçük yükün davranışını gözlemek için yürütülmektedir.

Kullanıcının önceki günkü gözlemine göre SSR anahtarlaması CH1 sinyalini etkileyebilmektedir. Anahtarlama sırasında CH1 sinyali normal yüksüz/kapalı alan seviyesinin de belirgin biçimde altına inebilmektedir. Kullanıcı, paylaşılan grafikte yaklaşık 10:19 civarındaki keskin düşüşü bu anahtarlama etkisiyle ilişkilendirmiştir.

Bu nedenle:
- SSR, 18 W ampulün bağlı olduğu ölçüm hattını anahtarlamaz; ampul sürekli yanık kalır.
- SSR'nin ayrı arka plan ON/OFF olayları veri içinde bulunabilir; ancak bu olaylar E17-A'nın yük ON/OFF durumu değildir.
- SSR anahtarlamasıyla ilişkili geçici CH1 düşüşleri, 18 W sürekli yükün kararlı seviyesi veya kapalı alan tabanı olarak değerlendirilmez.
- E17-A'nın temel değerlendirme aralığı, SSR anahtarlama geçişlerinden etkilenmeyen sürekli yük davranışıdır. Olay zamanları CSV analizinde işaretlenerek olası etkilenmiş örnekler ayrı tutulur.
- Anahtarlama etkisinin kendisi ayrı bir araştırma konusudur; E17-A'nın ana amacı değildir.

**Kanıt niteliği:** SSR anahtarlamasının CH1'i etkilediği önceki deney gözlemi kullanıcı tarafından bildirilmiştir. 10:19 civarındaki grafik düşüşü ekran görüntüsünden görülen olaydır; zaman eşleşmesi ve etki büyüklüğü ham CSV ile doğrulanmalıdır.

### SSR olay akışı — fiziksel yük hattından bağımsız

Deney sırasında arka planda bir SSR ON/OFF döngüsü çalışmaktadır; ancak bu SSR, 18 W ampulün bağlı olduğu ve PZEM/SCT CH1 tarafından gözlenen ölçüm hattını anahtarlamamaktadır. 18 W ampul deney boyunca sürekli yanık kalır.

Bu nedenle:
- SSR ON/OFF olayları HA/veri kaydında bulunabilir; bunlar ayrı olay akışı/arka plan bilgisi olarak korunur.
- Bu olaylar 18 W ölçüm hattındaki fiziksel yükün ON/OFF durumu veya deney yükünün geçiş zamanları olarak etiketlenmeyecektir. Önceki gözlemlerde SSR anahtarlamasının SCT sinyalini etkilediği bildirildiğinden, olay zamanları olası parazit/etki zamanlarını ayırmak için metadata olarak korunacaktır.
- CH1 sıçramaları SSR olaylarıyla zaman bakımından çakışsa bile tek başına nedensellik veya yük anahtarlaması kanıtı sayılmaz.
- İleride istenirse SSR olay zamanları ile CH1 değişimleri ayrı bir korelasyon incelemesinde karşılaştırılabilir; ancak bu deneyde olay akışı yük durumunu belirlemek için kullanılmaz.

**Deney koşulu / kullanıcı bildirimi:** SSR arka planda anahtarlama yapıyor; ölçüm hattına bağlı değil.

### İlk ekran gözlemi — 10:21 sonrası

Kullanıcının paylaştığı HA grafiğinin lejantındaki son değerler:
- PZEM gerilimi: 227,1 V.
- PZEM akımı: 0,078 A.
- CH1 hesaplanmış akım entity'si: 0,277 A.
- CH1 ham SCT entity'si: 0,01145 A olarak görüntüleniyor.

Grafikte CH1 hesaplanmış akım eğrisi 10:21 sonrasında yaklaşık 0,28–0,30 A çevresinde seyrediyor. Bu, CH1'in fiziksel yük varlığına tepki verdiğine ilişkin **ilk ekran gözlemidir**; kararlılık veya tekrar edilebilirlik sonucu değildir. PZEM'in 0,078 A okuması 18 W / 227,1 V için beklenen yaklaşık 0,079 A düzeyiyle uyumludur (basit güç/gerilim hesabı; ampulün gerçek çalışma gücü ayrıca ölçülmedi).


### Güncel ekran gözlemi — 2026-11-07, yaklaşık 10:26

Kullanıcının sonraki HA History ekran görüntüsündeki lejant son değerleri:
- PZEM gerilimi: 226,2 V.
- PZEM akımı: 0,078 A.
- PZEM aktif güç grafiği: yük devredeyken yaklaşık 17,5–17,8 W.
- CH1 hesaplanmış akım: 0,325 A.
- CH1 ham SCT değeri: 0,01341 A.

Grafikte PZEM güç çizgisi yaklaşık 10:20 civarında 17,5–17,8 W seviyesine çıkıyor. CH1 hesaplanmış akımı bu geçişte kısa süreli değişim gösterdikten sonra yaklaşık 0,28–0,33 A bandında seyrediyor; tekil tepe değerleri yaklaşık 0,5 A'ya yaklaşıyor. Bu zaman grafiği gözlemidir; CSV istatistiği değildir.

**Yorum:** PZEM'in 0,078 A / yaklaşık 17,5–17,8 W gösterimi ile CH1'in 0,325 A göstermesi, CH1'in bu küçük yükte tepki verdiğini ancak akım genliğini PZEM referansıyla uyumlu ölçmediğini gösteren ek bir ekran kanıtıdır. 0,325 A, 0,24–0,41 A hesaplanmadı alanındadır; sayısal akım olarak kabul edilmez. Ham SCT 0,01341 A ayrı ham entity değeridir; amper cinsinden PZEM akımıyla doğrudan karşılaştırılmaz.

Bu ekran görüntüsü E17-A'nın devam eden aynı oturumuna ait ek gözlemdir. 10:20 civarındaki güç yükselişi grafikte görünmektedir; kullanıcının bildirdiği deney başlangıç saati 10:21 olarak korunur. Ekran çözünürlüğünden daha kesin olay zamanı çıkarılmaz. Kararlılık/tekrar edilebilirlik için HA History CSV analizi beklenir.

### Geçici yorum ve kullanıcı kararı

CH1'in 18 W yükte tepki verdiği görülüyor; ancak 0,277–0,30 A çıktısı 0,24–0,41 A hesaplanmadı alanına düşüyor. Bu nedenle:
- Fiziksel yük/ana akım varlığı algılanabilir.
- Bu aralıkta CH1 sayısal akım değeri kabul edilmeyecek ve yazılım tarafından hesaplanmayacak.
- Bu bölge daha sonra farklı/daha hassas bir sensörle ayrı çalışma konusu olabilir.
- Bu gözlem K=24.22 kalibrasyonuna veya CH1'in düşük akımda doğru ölçtüğü iddiasına kanıt değildir.

## CSV geldiğinde yapılacak korelasyon incelemesi — PLAN

18 W sürekli yük oturumunda CH1 ham SCT ve hesaplanmış akım serisindeki tepe/sıçrama zamanları, aynı zaman aralığındaki PZEM değişkenleriyle karşılaştırılacaktır.

### Karşılaştırılacak kanallar
- PZEM gerilimi (V)
- PZEM akımı (A)
- PZEM aktif gücü (W)
- PZEM güç faktörü (PF)
- PZEM frekansı (Hz)
- SCT CH1 ham SCT serisi ve CH1 hesaplanmış akım serisi

### İnceleme adımları
1. CSV'de gerçek entity/kolon adları, birimler, timestamp ve örnekleme aralıkları doğrulanır.
2. Zaman damgaları ortak zaman eksenine taşınır; PZEM ve SCT güncelleme hızları farklıysa bu fark açıkça raporlanır. Veri olmayan noktalara ölçüm uydurulmaz.
3. CH1 pikleri ham SCT ve hesaplanmış akım serilerinde ayrı ayrı belirlenir; pik zamanları, genlikleri ve aralıkları çıkarılır.
4. Her pik çevresinde PZEM V/A/W/PF/Hz değerlerinin öncesi-sırası-sonrası karşılaştırılır. Yalnız aynı zaman damgasındaki tek noktaya bakılmaz; mevcut örnekleme çözünürlüğüne uygun zaman pencereleri kullanılır.
5. Piklerin PZEM değişimleriyle eşzamanlılığı, gecikmesi ve tekrarlanabilirliği incelenir. Uygunsa korelasyon/çapraz korelasyon ve pik dışı temel dönem karşılaştırmaları yapılır.
6. SSR ON/OFF olayları ayrı metadata olarak kullanılır. SSR ölçüm hattını anahtarlamadığı için olaylar yük durumu etiketi sayılmaz; anahtarlama anları olası etki/parazit pencerelerini ayırmak için ayrıca işaretlenir.
7. Sonuç, elektriksel değişimle uyumlu bulgu, SCT/ölçüm zinciri davranışıyla uyumlu bulgu veya mevcut veri çözünürlüğüyle ayırt edilemeyen durum olarak sınıflandırılır.

### Yorum sınırı
Korelasyon tek başına nedensellik kanıtı değildir. PZEM Hz ve PF gibi değerlerin çözünürlüğü/güncelleme sıklığı CH1 piklerini yakalamaya yetmeyebilir; bu durumda “ilişki yok” değil, “mevcut kayıt çözünürlüğüyle gösterilemedi” denir. Bu analiz E17-A'nın 0,24–0,41 A hesaplanmadı alanında sayısal akım üretme kararını değiştirmez.

**Durum:** CSV bekleniyor; analiz henüz yapılmadı.

### Kayıt planı

HA History kaydı bir süre daha sürdürülecek. Ham CSV kullanıcı tarafından sağlandığında gerçek kolonlar, zaman damgaları, örnek sayısı, dağılım ve zaman içindeki kararlılık incelenecek. Ham CSV varsayılan olarak depoya eklenmeyecek; kullanıcı tercihi doğrultusunda istatistik ve yorum saklanacak.

## E17-B — 15 W mini buzdolabı ampulü, sürekli açık (sonraki ayrı deney)

Kullanıcı, 18 W kaydından sonra 15 W mini buzdolabı ampulüyle sürekli açık ayrı bir kayıt almak istedi. Kullanıcı bu ampulün farklı tepkiler verdiğini belirtti.

- E17-B, E17-A'dan ayrı oturum olarak kaydedilecek.
- Ampulün tam çalışma koşulu ve deney başlangıç saati o oturumda not edilecek.
- 18 W ve 15 W verileri tek zaman serisi veya tek deney sonucu gibi birleştirilmeyecek.
- Farklı tepki gözlemi şu an **kullanıcı bildirimi/ön beklenti** niteliğindedir; henüz yeni 15 W kaydıyla doğrulanmış değildir.

## Sonuç durumu

E17-A açıktır. Şu an yalnızca ekran görüntüsü üzerinden ilk tepki gözlemi vardır. Uzun kayıt analizi, istatistiksel kararlılık, tekrarlanabilirlik ve nihai deney sonucu henüz yoktur. E17-B henüz başlatılmamıştır.
