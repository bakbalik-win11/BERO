# SCT–PZEM Kararlılık Alanı Etiketleme ve Kalibrasyon Hedefi

**Durum:** Kullanıcı tarafından açıklanmış hedef mimari; uygulama/firmware ve deneyler henüz tamamlanmadı.  
**Kapsam:** T001 sırasında aktarılan mimariyi ve gelecekteki veri/modelleme akışını koruyan proje notu. Bu belge uygulanmış yazılım veya deney sonucu iddiası değildir.

## PF ve akım ölçümüne ilişkin ek bakış

PF'nin akım büyüklüğü ve SCT ölçümüne olası etkisi ayrı teknik notta kaydedilmiştir: [PF değişimi ve akım ölçümüne etkisi](pf-and-current-measurement.md). BERO'da amaç PF'yi SCT'den tahmin etmek değildir. İlk model PF girdisi olmadan denenir; farklı yük/PF koşullarındaki hata gözlenir. Gerekirse aynı veri ve koşullarla PF girdili model karşılaştırılır. Düşük PF'nin aynı aktif güçte RMS akımı artırabileceği dikkate alınır; yüksek SCT okuması otomatik hata sayılmaz, PZEM akımıyla karşılaştırılır.

## Ana hedef

Üç ayrı SCT örnekleme düğümünden ham/anlık sensör gerilimi örneklerini mümkün olduğunca az kayıpla toplamak. PZEM ve SCT'nin kararlı olduğu **alanları/dönemleri**, SSR olay paketleri ve geliştirilecek kararlılık algoritmaları/istatistikleriyle belirleyip etiketlemek. Python'da etiketlenmiş SCT verisi oluşturmak; bu veriyle her SCT için kalibrasyon katsayısı ve (f(x)) modelini çıkarmak. Ardından bulunan fonksiyonu çok sayıda paket/olay içeren ham veri üzerinde sınamak ve sonuçlara göre gerekirse modeli/algoritmayı iyileştirmek.

**Temel tasarım vurgusu:** Kullanıcının tarif ettiği yöntem salt zaman damgası veya olaydan sonra sabit bir süre sayarak etiketleme değildir. Esas yaklaşım **paket bağlamı + PZEM/SCT kararlı alanlarının belirlenmesi**dir. Zaman ve istek/yanıt bilgileri kayıtların izlenebilirliği ve inceleme için yararlı olabilir; fakat kararlılık etiketinin yerine geçmez. Sabit bir geçiş süresi (ör. eski teknik raporlardaki yaklaşık 3 s başlangıç maskesi) nihai etiketleme kuralı olarak varsayılmamalı; ancak deneylerde karşılaştırılacak başlangıç hipotezi olabilir.

## Hedef iş bölümü

- **ESP32-C3 SuperMini:** SSR anahtarlama ve zamanlama düğümü; ON/OFF olaylarını paket bilgisiyle yayımlar. Mevcut paket biçimi: `BERO_EVT,BOOT_ID=XXXXXXXX,EVENT_ID=N,STATE=ON|OFF`.
- **SCT örnekleme düğümleri:** 2 × ESP32-WROOM-32D ve 1 × ESP32-WROOM-32E. Her düğüm SCT sinyalinin ham/anlık gerilim örneklerini hızlı ve düşük kayıpla toplar ve veriyi Home Assistant'a aktarır. İlk aşamada ESP düğümlerinin akım/RMS hesabı yapması hedeflenmiyor.
- **PZEM düğümü:** PZEM'in raporladığı ölçüm alanları ve paket/olay bağlamı, PZEM'in kararlı olduğu alanları belirlemek ve SCT kararlılığıyla ilişkilendirmek için kullanılır. PZEM kusursuz/altın standart kabul edilmez; alanların aynı yanıtta gelmesi içeride eşzamanlı yenilendiklerini kanıtlamaz.
- **Home Assistant:** ESP düğümlerinden gelen verilerin aktarılacağı hedef sistem.
- **Python (Mac Mini/PC):** Veri birleştirme, kararlılık algoritmaları ve istatistikleri geliştirme, alan etiketleme, kalibrasyon katsayısı/(f(x)) modelini çıkarma, modelin ham veri üzerinde doğrulanması ve iteratif iyileştirme. Temel hesaplama/modelleme ESP'lerde veya Home Assistant'ta değil Python tarafında yapılır.

## İlk eğitim aşaması — ortak kararlı alan etiketleme kuralı

Bu bölüm, BERO'nun ilk eğitim aşamasında uygulanacak temel etiketleme yöntemini tanımlar.

1. SSR yükü açar veya kapatır. SSR'nin `BOOT_ID`, `EVENT_ID` ve `STATE=ON|OFF` bilgisi ilgili test olayını ve ON/OFF penceresini tanımlar.
2. Aynı olay penceresindeki PZEM akım kayıtları Python'da incelenir; PZEM'in kararlı olduğu alan/alanlar belirlenir.
3. Aynı olay penceresindeki SCT ham verisinden çıkarılan pencere istatistikleri ayrıca incelenir; SCT'nin kararlı olduğu alan/alanlar bağımsız olarak belirlenir.
4. Python, PZEM kararlı alanı ile SCT kararlı alanının **aynı SSR olay penceresi içinde örtüştüğü ortak aralığı** bulur. Eğitim için kabul edilen bölüm yalnızca bu ortak kararlı aralıktır. Yalnız PZEM'in veya yalnız SCT'nin kararlı olması yeterli değildir.
5. Ortak kararlı aralıkta yer alan SCT verisi, o aralığa karşılık gelen geçerli PZEM akım değeriyle etiketlenir. Etiket, PZEM'in proje içi referans değerini temsil eder; PZEM kusursuz veya bağımsız mutlak standart kabul edilmez.
6. Aynı işlem hem SSR ON (yük açma) penceresi hem de SSR OFF (yük kapama) penceresi için uygulanır. Böylece açma ve kapama davranışlarından ortak kararlı alan örnekleri elde edilir.
7. Geçiş, yerleşme ve kararlı olmayan alanlar eğitim etiketi olarak kullanılmaz; ihtiyaç halinde analiz amacıyla ayrı sınıflandırılıp korunabilir.

**Zaman yaklaşımı:** Burada amaç her SCT örneğini PZEM okumasıyla milisaniye hassasiyetinde eşleştirmek değildir. İki taraftaki kararlılık ayrı ayrı bulunur ve aynı SSR olay penceresindeki örtüşen alan seçilir. Zaman damgaları ile PZEM istek/yanıt zamanları bu alanların sırasını, örtüşmesini ve PZEM güncelleme gecikmesini incelemek için kullanılır. Olaydan sonra sabit N saniye beklemek, ortak kararlı alanı bulmanın yerine geçmez.

**Kararlılık ölçütleri:** PZEM ve SCT için eşikler, pencere sayıları ve algoritmalar önceden uydurulmaz; ilgili deney verileriyle belirlenir. Bu kurallar belirlenip uygulanana ve fiziksel veriyle sınanana kadar yöntem hedef tasarımdır, doğrulanmış sonuç değildir.

## İki bağlantılı iş hattı: eğitim ve dinamik gözlem

Ayrıntılı akış, zaman grafiği, gecikme yorumlama ve kayıt ilişkileri için [Kararlı alan eğitimi ve aç-kapa ham akış gözlemi](training-and-dynamic-observation.md) belgesini esas al.

- **Eğitim:** Aynı SSR olayındaki PZEM ve SCT kararlı alanlarının örtüşen ortak aralığından SCT verisi PZEM akımıyla etiketlenir; model bu kararlı etiketli veriyle eğitilir.
- **İlk uyum raporu:** Model, eğitildiği aynı etiketli kararlı alan verisine yeniden uygulanır. ±%4 sonucu eğitim verisi içi uyumdur; bağımsız genelleme başarımı değildir.
- **Dinamik gözlem:** Aynı olayın geçişler dahil tam SCT ham zaman akışına model uygulanır; SCT tahmini ve PZEM akışı zaman ekseninde birlikte çizilir. Tepki, yerleşme, gecikme ve zaman farkları incelenir. Bu grafik ayrı bir davranış raporudur; geçiş anları ±%4 eğitim metriğine karıştırılmaz.

PZEM'in yanıt zamanı iç ölçüm zamanını kesin olarak göstermez. İstek/yanıt, SCT örnek/pencere ve SSR olay zamanları ayrı tutulur; haberleşme süresi fiziksel ölçüm gecikmesiyle eşitlenmez. Ayrı holdout veri kümesi ilk aşamanın zorunlu koşulu değildir.

## Kalibrasyon ve model doğrulama döngüsü

1. Ortak kararlı alanlardan SCT başına etiketli eğitim verisini hazırla.
2. Python'da SCT başına katsayı ve/veya `f(x)` modelini eğit.
3. İlk uyum raporunda modeli aynı etiketli eğitim verisine yeniden uygula; ±%4 PZEM-referans ölçütünü bu eğitim verisi içi uyum olarak raporla.
4. Aynı SSR deneyinin geçişler dahil ham SCT akışına modeli uygula; SCT tahmini ve PZEM zaman serisini ortak zaman ekseninde dinamik gözlem için çiz.
5. Tepki, yerleşme, PZEM güncelleme/okuma süreleri ve gözlenen zaman farklarını ayrı raporla. Geçiş grafiğini eğitim verisi içi ±%4 metriğiyle karıştırma.
6. Hatalı etiketleri, veri kalitesini ve olaylar arası farkları incele; gerekirse kararlılık algoritmasını veya model biçimini geliştir.
7. **Kabul hedefi (T003):** Geçerli, sıfırdan farklı PZEM akımında `abs(prediction - pzem_current) / abs(pzem_current) <= 0.04` ise `OK`; değilse `OUT_OF_RANGE`. Sıfır/geçersiz referans bu yüzde kuralıyla sınıflandırılmaz. Bu ilk rapor bağımsız genelleme kanıtı değildir.

## Sarım deneyleri

Aynı iletkenin SCT içinden geçirilme sayısı ayrı deneylerde 1 sarım, 2 sarım ve 4 sarım olarak değiştirilecektir. Bu deneylerden elde edilen etiketli örnekler sensör davranışını modellemek için kullanılacaktır. Her deneyde sensör/kanal kimliği, sarım sayısı ve kalibrasyon/model sürümü korunmalıdır. Henüz deney verisi veya doğrulanmış model yoktur.

## Geçmiş belgelerle ilişki ve dikkat

- Önceki teknik raporlar ve ADR'ler yaklaşık 1 s PZEM sorgusu, zaman kayıtları ve olay sonrası yaklaşık 3 s geçiş maskesi gibi başlangıç önerileri içeriyor. Bunlar daha önce hazırlanmış önerilerdir; kullanıcının burada açıkladığı **kararlı alan bazlı etiketleme** hedefiyle aynı şey değildir.
- ADR-003 ve ADR-006 mevcut durumlarıyla otomatik olarak değiştirilmiş sayılmaz. Uygulama öncesinde bu belgeler, paket bilgisinin SCT/PZEM tarafında nasıl erişilebilir olacağı ve etiketlerin nasıl üretileceği açısından açıkça gözden geçirilmelidir.
- Zaman damgaları yardımcı metadata olabilir; zaman bazlı eşleştirme veya sabit zaman maskesi, kararlılık alanını belirleyen esas ölçüt olarak varsayılmamalıdır.

## Açık kalanlar

1. Paket bilgisinin PZEM ve SCT verileriyle nasıl ilişkilendirileceği ve hangi düğümlerin paketi doğrudan alacağı.
2. Kararlılık alanı tanımı, algoritması, istatistiksel eşikler ve etiket şeması.
3. Home Assistant'a aktarım şeması, örnekleme hızı, tamponlama ve kayıp ölçüm yöntemi.
4. Kalibrasyonda kullanılacak model biçimi, aynı eğitim verisindeki uyum raporunun ayrıntıları ve ileride ayrıca raporlanabilecek veri kümeleri.
5. Ham veride modelin çok paketli/olaylı koşullarda nasıl değerlendirileceği ve iyileştirme ölçütleri.

## Kayıt ilkesi

Bu belge kullanıcının açıkladığı hedefi kaydeder. Henüz yazılmamış SCT firmware'ini, yapılmamış deneyleri, belirlenmemiş algoritmaları veya doğrulanmamış kalibrasyon sonuçlarını mevcutmuş gibi göstermez.

## HA'dan PC'ye veri aktarımı

Veriler Home Assistant'ta toplandıktan sonra ayrı bir Python aktarım programı HA'dan kayıtları alıp PC'de saklayacaktır. Kararlılık analizi ve etiketleme de PC üzerinde çalışan Python programlarında yapılacaktır. PZEM akışı ile üç SCT kanalının kararlılık analizi ayrı yürütülecek; deneylerle geliştirilen kriterler kullanılarak etiketler üretilecektir. Aç/kapa olay paketleri verilerle ilişkilendirilecektir.

Bu bölüm hedef mimariyi tanımlar; aktarım ve analiz kodlarının uygulandığı anlamına gelmez.
