# YHDC SCT013-030 (30A/1V) üretici grafiği – BERO V1.6 K(x) karşılaştırması

- Tarih: 2026-11-22
- Kaynak: Kullanıcının paylaştığı YHDC SCT013 aile karakteristik grafiği; `SCT013(30A/1V)` panelindeki etiketli noktalar okunmuştur.
- Hesap tipi: Üretici grafiğindeki Vout değerlerine BERO V1.6 başlangıç ölçeği ve K(x) fonksiyonu uygulanarak teorik karşılaştırma.
- Durum: Matematiksel karşılaştırma; BERO donanımında yeni test yapılmadı.

## 1. Üretici grafiğinden okunan noktalar

| Üretici giriş akımı (A) | Üretici çıkışı (V) |
|---:|---:|
| 6 | 0.1994 |
| 12 | 0.3995 |
| 15 | 0.4997 |
| 18 | 0.5996 |
| 24 | 0.7997 |
| 30 | 0.9994 |
| 36 | 1.1993 |

Grafikte 30A/1V panelinin ilk işaretli noktası 6 A'dır. Bu, sensörün 6 A altında çalışmadığı anlamına gelmez; yalnızca bu üretici grafiğinde 6 A altı için karakteristik noktası gösterilmemiştir. 36 A noktası panelde çizilmiş olsa da 30 A nominal giriş sınırının dışındadır; karşılaştırma tablosunda gösterilir ama 6–30 A nominal aralık ortalamasına katılmaz.

## 2. BERO V1.6 fonksiyonuna uygulama yöntemi

V1.6 YAML zincirindeki başlangıç ölçeği `1.0 V → 27.59 A` olduğundan, üretici grafiğindeki her Vout için önce aynı taban ölçeği uygulanır:

`x = Vout × 27.59`

Sonra BERO'nun tek fonksiyonu hesaplanır:

`K(x) = 26.89 + 5.39 × exp(-x / 0.882)`

V1.6'nın düzeltilmiş akım çıktısı:

`I_BERO = x × K(x) / 27.59 = Vout × K(x)`

Üretici grafiğindeki giriş akımı `I_ref` kabul edilerek sapma:

`Sapma (%) = (I_BERO - I_ref) / I_ref × 100`

Bu sıralama önemlidir: K(x) girdisi üretici grafiğindeki gerçek giriş akımı değil, Vout'un V1.6 başlangıç ölçeği 27.59 ile hesaplanan ham taban akımıdır.

## 3. Hesap sonuçları

| Üretici giriş (A) | Vout (V) | V1.6 taban x (A) | K(x) | V1.6 akımı (A) | Sapma |
|---:|---:|---:|---:|---:|---:|
| 6 | 0.1994 | 5.5014 | 26.9005 | 5.3640 | -10.60% |
| 12 | 0.3995 | 11.0222 | 26.8900 | 10.7426 | -10.48% |
| 15 | 0.4997 | 13.7867 | 26.8900 | 13.4369 | -10.42% |
| 18 | 0.5996 | 16.5430 | 26.8900 | 16.1232 | -10.43% |
| 24 | 0.7997 | 22.0637 | 26.8900 | 21.5039 | -10.40% |
| 30 | 0.9994 | 27.5734 | 26.8900 | 26.8739 | -10.42% |
| 36* | 1.1993 | 33.0887 | 26.8900 | 32.2492 | -10.42% |

*36 A noktası 30 A nominal giriş aralığının dışındadır.*

**Nominal 6–30 A aralığı:**
- Ortalama bağıl sapma: **-10.46%**
- En küçük sapma: **-10.60%**
- En büyük sapma: **-10.40%**
- Üretici verilerinden hesaplanan gerekli katsayı `I_ref/Vout`: yaklaşık 30.01–30.09 A/V; ortalama yaklaşık 30.03 A/V.
- V1.6 fonksiyonunun bu noktalardaki etkin katsayısı: 6 A noktasında 26.9005; 12 A ve üzerindeki noktalarda yaklaşık 26.8900 A/V.

## 4. Grafiğin gösterdiği şey

Bu üretici veri setinde 6–30 A boyunca Vout / Iref oranı yaklaşık sabittir; üretici eğrisi bu gösterilen aralıkta doğrusaldır. V1.6 fonksiyonu ise ilk üretici noktası olan 6 A'da dahi taban x≈5.50 A değerine ulaşır ve etkin katsayısı 26.90 civarına iner; sonraki noktalarda yüksek akım asimptotu 26.89'a çok yakındır.

Bu nedenle üretici eğrisine V1.6 ölçeği uygulandığında yaklaşık -10.4% seviyesinde, neredeyse sabit bir ölçek farkı görülür. Bu sonuç **V1.6'nın kendi BERO ölçüm zincirinde aynı oranda hata yaptığı anlamına gelmez**. Üretici grafik eğrisi, üretici nominal 30A/1V hassasiyeti ve BERO V1.6'nın ampirik/kuruluma özgü kalibrasyon ölçeği doğrudan aynı şey değildir. V1.6, BERO'nun gerçek SCT013 örneği + ADS1115 No.10 + bağlantı/analog koşulları + yazılım zinciri ve PZEM referansıyla elde edilmiş deneysel modeldir.

Bu karşılaştırma, nominal 30 A/V üretici transferini V1.6'nın 27.59 taban ölçeği ve 26.89 yüksek akım katsayısı ile aynı kabul edemeyeceğimizi gösterir. Farkın olası kaynağı sensör örneği/parti hassasiyeti, analog aktarım/ölçek, veri sayfası grafik toleransı veya ölçüm zinciri olabilir; bu hesap bunlardan hangisinin neden olduğunu belirlemez.

## 5. Düşük akım hakkında ne söyler, ne söylemez?

- Bu üretici grafiği 30A/1V modeli için 6 A'dan başlar; 6 A altındaki karakteristik gösterilmediğinden düşük akım doğrusallığı hakkında bu grafikle karşılaştırma yapılamaz.
- İlk 6 A noktasının kendisi, sensörün 6 A altına inemeyeceği veya 6 A'nın kesin alt sınır olduğu anlamına gelmez.
- Dolayısıyla bu hesap, kullanıcının belirttiği düşük akımda üreticinin grafikle doğrulama göstermemesi konusunu destekler; düşük akım sapmasının boyutunu üretici verisinden hesaplamaz.
- 5A/1V paneli ayrı sensör modelidir ve grafikte ilk nokta 1 A'dır. Bu 30A/1V için 1 A alt sınırı olarak kullanılamaz.

## 6. Sonuç / proje kararı

1. Üretici grafiğindeki 30A/1V noktaları V1.6 fonksiyonuna matematiksel olarak uygulandı.
2. Nominal 6–30 A aralığında yaklaşık -10.46% sabit ölçek farkı çıktı.
3. Bu fark V1.6 katsayısını değiştirmek veya bölgesel kalibrasyona dönmek için kanıt değildir; üretici nominal eğrisi ile BERO'nun ampirik kalibrasyon ölçeğinin farklı olduğunu gösterir.
4. V1.6 kendi BERO donanım deneyleri ve PZEM karşılaştırması üzerinden kabul edilmiş referans olarak korunur.
5. PF araştırması ana hedef değildir; uzun vadeli isteğe bağlı araştırma konumunda kalır.
6. Bu hesap, gerçek donanımda ölçülmüş yeni bir sonuç olarak sunulmayacaktır.

Grafik: `YHDC-30A-1V-GRAFIGI-V1.6-KX-KARSILASTIRMA-2026-11-22.svg`

## Laboratuvar karakteristiği ile gerçek şebeke koşullarının karşılaştırma sınırı

Üretici karakteristik eğrisi kontrollü laboratuvar koşullarında oluşturulmuş referans veri olarak değerlendirilir. Kullanıcının paylaştığı test yöntemi bağlamına göre üretici tarafında primer akımı bir akım üreteciyle oluşturulmaktadır. Ancak erişilebilen YHDC SCT013-030 ürün spesifikasyonu; nominal giriş/çıkış, doğruluk, doğrusallık ve frekans aralığını listelerken karakteristik eğrinin test kaynağını, uygulanan dalga şeklinin bozulma seviyesini, test frekansını ve diğer ayrıntılı laboratuvar koşullarını açıkça tarif etmemektedir. Bu nedenle akım üreteci bilgisi proje notunda kullanıcı tarafından aktarılan test yöntemi bağlamı olarak tutulur; veri sayfasından bağımsız olarak doğrulanmış ayrıntı gibi sunulmaz.

BERO saha koşulları farklıdır:
- Gerçek şebeke gerilimi, laboratuvar kaynağının geriliminden farklı olabilir.
- Yükün türü, güç elektroniği ve çalışma modu primer akımının sinüs biçimini ve harmonik içeriğini değiştirebilir.
- Akım trafosunun gördüğü asıl büyüklük primer akımdır. Şebeke gerilimi farkı tek başına CT oranının değiştiğini kanıtlamaz; ancak bağlı yükün çektiği akımı ve dalga şeklini etkileyebilir.
- Gerçek dalga şekli, frekans bileşenleri ve ölçüm cihazlarının RMS hesap yöntemi farklıysa üretici laboratuvar eğrisiyle saha sonucu birebir aynı olmak zorunda değildir.

Bu nedenle üretici grafiğindeki yaklaşık %10,4 eğim/ölçek farkı tek başına BERO kalibrasyon hatası veya sensör kusuru olarak yorumlanmaz. Üretici verisi nominal/laboratuvar karakteristiğini; BERO K(x) ise kendi SCT013 örneği, ADS1115 ve yazılım zincirinin gerçek saha koşullarındaki ampirik davranışını temsil eder.

Planlanan basit pens ampermetre kontrolünün amacı laboratuvar deneyini yeniden üretmek değildir. Çamaşır makinesinin ısıtma evresinde, gerçek şebeke koşullarında yaklaşık 8 A için PZEM ve BERO sonucunu bağımsız akım okumasıyla kontrol etmektir. Pens sonucu PZEM ve BERO'yu desteklerse bu gerçek kullanım koşulunda yeterli pratik güven sağlar; üretici laboratuvar eğrisiyle farkın tek başına nedenini belirlemez.

## 7. Basit saha kontrolü: pens ampermetre – MOD3 ısıtma bloğu

Bu kontrolün amacı ticari/sertifikalı bir akım ölçer geliştirmek veya laboratuvar kalibrasyonu yapmak değildir. Amaç, BERO V1.6 sonucunun gerçek yük akımıyla uyumunu pratik bir bağımsız ölçümle kontrol etmektir.

MOD3-AKM001 uzun pamuklu programındaki ısıtma bloğu bunun için uygun adaydır:
- Zaman aralığı: 17:24:12–17:38:56 (Europe/Istanbul).
- PZEM akımı: yaklaşık 8.28 A.
- BERO V1.6 akımı: raporlanan ortalama farktan türetilen yaklaşık 8.17 A.
- Isıtma gücü: yaklaşık 1.81 kW.

**Yapılacak basit kontrol:** Çamaşır makinesinin benzer bir uzun programında ısıtma evresinin kararlı bölümünde pens ampermetreyle tek bir akım kontrolü (tercihen birkaç kısa tekrar) alınır. Pens yalnızca tek iletkeni çevrelemelidir; faz ve nötr birlikte ölçülmez. Okunan yaklaşık değer, mevcut PZEM 8.28 A ve BERO 8.17 A saha sonuçlarıyla karşılaştırılır.

**Yorum:**
- Pens de yaklaşık 8 A civarında sonuç verirse, PZEM ve BERO ölçümlerini bu çalışma noktasında bağımsız olarak destekler.
- Pens belirgin biçimde farklı sonuç verirse, önce yükün aynı çalışma evresinde ve kararlı olduğundan emin olunur; sonra ölçüm tekrar edilir.
- Bu tek nokta tüm 0–30 A aralığının doğruluğunu veya üretici toleransını kanıtlamaz. Sadece yaklaşık 8 A saha noktasında iç rahatlatan bir çapraz kontroldür.

Üretici grafiği laboratuvar karakteristiğidir; BERO ise kendi ADS1115 ölçüm zincirinin çıktısını ve PZEM ile saha karşılaştırmasını kullanır. Pens sonucu PZEM ve BERO ile uyuşursa, BERO kurulumunun bu noktadaki gerçek akımı doğru izlediği yönünde ek kanıt elde edilir. Üretici eğrisinden görülen ölçek farkının sensör örneğinden mi yoksa analog/ölçüm zincirinden mi kaynaklandığını yalnızca pens ölçümü tek başına ayıramaz.

Güvenlik: Pens, yalıtımı sağlam ve erişilebilir tek iletken üzerinde kullanılmalı; açıkta canlı iletken oluşturulmamalı ve devre/ekipman sınırları aşılmamalıdır.

**Durum:** Basit pens kontrolü önerilmiştir; henüz yapılmış bir ölçüm değildir. V1.6 K(x) değiştirilmez. MOD3-AKM001'in kapalı görevi yeniden açılmaz; kontrol ayrı ek doğrulamadır.

## 8. PowerUC ürün sayfası ve YHDC aile PDF'si – belge sınırları

Kullanıcının sağladığı üretici ürün sayfası:
- https://www.poweruc.pl/products/split-core-current-transformer-sct013-rated-input-5a-100a

Sayfanın bağladığı YHDC markalı SCT013 aile PDF'si:
- https://poweruc.com/wp-content/uploads/2023/07/2025040819322782.pdf

İncelenen PDF'nin ilk sayfasında ve grafik sayfasında görülen açık bilgiler:
- Çekirdek malzemesi ferrit.
- Frekans aralığı 50 Hz–1 kHz olarak yazılmıştır.
- SCT013-030 için rated input 30 A ve rated output 1 V verilmiştir.
- Accuracy satırında `0.5/1%` yazmaktadır; bu gösterimin hangi doğruluk sınıfına, koşula veya model varyantına karşılık geldiği PDF'de açıklanmamıştır.
- Elektriksel parametreler için açıkça “typical values” (tipik değerler) denmekte ve gerçek değerlerin ürünün fiilî ölçümüne tabi olduğu belirtilmektedir.
- Grafiklerde SCT013 30A/1V için 6 A → 0.1994 V, 12 A → 0.3995 V, 15 A → 0.4997 V, 18 A → 0.5996 V, 24 A → 0.7997 V ve 30 A → 0.9994 V noktaları yer alır.

### Test düzeneği konusunda ne açıklanmış?

Bu ürün sayfası ve PDF; ölçümde kullanılan akım kaynağının tipini, primer akım dalga şeklinin sinüs saflığını/harmonik içeriğini, test yükünü, test sıcaklığını veya grafik noktalarının nasıl üretildiğini açıklamamaktadır. Kullanıcının üreticinin akım üreteciyle kontrollü test yaptığı yönündeki değerlendirmesi proje bağlamında not edilmiştir; ancak bağlantılı açık teknik belgeler bu cihazı ve test dalga şeklini açıkça tarif etmediğinden bağımsız olarak belgelenmiş bir şart gibi gösterilmemelidir.

### Eski ve yeni belge değerleri birbirine karıştırılmamalı

Daha önce incelenen 2015 tarihli SCT013-030 ürün spesifikasyonunun dağıtılmış kopyasında accuracy ±1% ve linearity ≤0.2% ifadeleri bulunuyordu. PowerUC'nin burada incelenen aile PDF'sinde ise Accuracy satırı `0.5/1%` şeklindedir ve ayrı bir linearity değeri verilmemiştir. PDF, `0.5/1%` ifadesinin anlamını açıklamaz. Bu nedenle belgelerden biri diğerine çevrilerek tek ve kesin bir doğruluk sınırı üretilemez; kaynak ve belge sürümleri ayrı tutulmalıdır.

### BERO karşılaştırmasına etkisi

Üreticinin kendi PDF'si elektriksel değerleri tipik değer olarak tanımladığı ve gerçek ürün değerini fiilî ölçüme bağladığı için, grafikteki yaklaşık 30 A/V karakteristiği her bir SCT örneği ve her gerçek şebeke/yük koşulu için değişmez bir saha transferi garantisi olarak okunmamalıdır. Gerçek şebeke gerilimi ve yük tipi primer akım dalga şeklini etkileyebilir; SCT doğrudan gerilim değil, kelepçelendiği iletkendeki akımı algılar. Bu nedenle kıyaslamada CT'nin gördüğü akım dalga şekli önemlidir.

Yaklaşık -10.46% fark, yalnızca yayımlanan tipik karakteristik grafiği ile BERO'nun ampirik ADS1115/K(x) ölçeğinin matematiksel karşılaştırmasıdır. Bu farkın nedenini (sensör örneği, analog bağlantı/ölçek, dalga şekli veya diğer koşullar) bu belgeler tek başına belirlemez. MOD3 ısıtma evresinde planlanan basit pens kontrolü, gerçek kullanım koşulunda BERO ve PZEM'in akımını pratik olarak çapraz kontrol etmek içindir; üretici laboratuvar deneyini tekrar etmek değildir.

Durum: PowerUC ürün sayfası ve YHDC aile PDF'si incelendi; PDF'nin ilk sayfası görüntü üzerinden kontrol edildi. PDF'de test kaynağı/dalga şekli açıklaması bulunamadı. BERO üzerinde yeni fiziksel ölçüm yapılmadı.
