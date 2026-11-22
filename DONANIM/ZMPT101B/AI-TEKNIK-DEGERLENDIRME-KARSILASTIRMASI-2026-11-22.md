# BERO – Gerçek PF Araştırması / Beş AI Teknik Değerlendirme Yanıtının Karşılaştırılması

- Tarih: 2026-11-22
- Kaynak görüşler: Copilot (ilk yanıt), Google, Gemini, Claude ve Copilot (ek yanıt)
- Kapsam: SCT013 + ZMPT101B + ADS1115 ile sayısal gerçek güç faktörü (True PF) araştırması
- Durum: Teknik sentez ve deney planı; donanım sonucu değildir
- İlgili metodoloji: [PF Sayısal Hesaplama ve İstatistik Metodolojisi](PF-SAYISAL-HESAPLAMA-VE-ISTATISTIK-METODOLOJISI.md)

## 1. Yönetici sonucu

Beş değerlendirme yanıtı da temel PF matematiğinin doğru olduğu ve mevcut donanımla araştırmaya başlanabileceği konusunda birleşiyor. En isabetli ortak uyarı şudur:

**Önce ADS1115 ölçüm zincirinin gerçek zamanlama, örnekleme ve kanal yanıtı karakterize edilmeli; ADS1115'in nihai True PF ölçümüne yeterli olduğu henüz kabul edilmemelidir.**

Claude'un değerlendirmesi ölçülmemiş değerleri tahmin olarak işaretlemesi, ADC dönüşümünün zaman davranışını sensör gecikmesinden ayırması ve yalnızca dirençli yükle faz doğrulamasının yeterli olmadığını açıklaması bakımından daha temkinli ve güçlüdür. Diğer yanıtların yararlı önerileri aşağıdaki teknik düzeltmelerle korunmuştur.

Bu not bir model oylaması değildir. Teknik karar, ölçüm ve deney sonuçlarına dayanacaktır.

## 2. Beş değerlendirme yanıtının ortaklaştığı noktalar

1. Gerçek PF için temel hesap:
   - P = ortalama(v_ac × i_ac)
   - Vrms = sqrt(ortalama(v_ac²))
   - Irms = sqrt(ortalama(i_ac²))
   - S = Vrms × Irms
   - PF = P / S
2. Yalnızca cos(phi) hesabı, harmonikli/bozulmuş dalga biçimlerinde gerçek PF'nin yerine geçmez.
3. ADS1115 iki ölçüm kanalını aynı anda örneklemez; girişleri MUX üzerinden ortak ADC dönüşüm zincirini kullanır.
4. Gerilim-akım kanal zamanlaması ve sensörlerin analog faz yanıtı ayrı karakterize edilmelidir.
5. PZEM karşılaştırma cihazıdır; mutlak doğruluk standardı veya ground truth kabul edilmeyecektir.
6. Yeni ADC satın alma kararı, ölçüm yapılmadan verilmemelidir.

## 3. ADS1115 örnekleme hızı: tahmini değer ile ölçülen değer ayrımı

TI ADS1115 veri sayfası 8–860 SPS programlanabilir dönüşüm hızını, 16-bit delta-sigma mimarisini, MUX giriş yapısını ve single-cycle settling özelliğini belirtir. 860 SPS, cihazın tek dönüşüm zincirinin azami dönüşüm hızıdır; iki kanalın her biri için ayrı ayrı 860 SPS değildir.

İki kanal dönüşümlü taranırsa, yalnızca dönüşüm hızına dayanan ideal üst sınır kanal başına yaklaşık 430 örnek/saniyedir. I²C komutları, MUX ayarı, veri okuma, işlemci/RTOS yükü ve kullanılan sürücü gerçek hızı düşürebilir. Bu nedenle:

- 350–400 SPS/kanal rakamları Copilot, Google ve Gemini yanıtlarında tahmin olarak geçmektedir; BERO'da ölçülmüş sonuç değildir.
- 430 SPS/kanal da ölçülmüş hız değil, dönüşümlü kullanım için teorik ideal üst sınırdır.
- Gerçek kanal başı SPS, kanal arası zaman ofseti ve jitter deneyle raporlanacaktır.
- 50 Hz'de 350–430 SPS, kanal başına yaklaşık 7–8,6 örnek/periyot demektir. Bu, temiz temel bileşen üzerinde deney yapmaya imkân verebilir; yüksek harmonikli dalga biçimini yeterli doğrulukla yeniden oluşturduğunu göstermez.
- 400 SPS/kanal varsayımında Nyquist sınırı 200 Hz'dir. 50 Hz temel bileşenin 5. harmoniği 250 Hz olduğundan bu sınırın üzerindedir. 200 Hz sınırındaki bileşen de Nyquist noktasında olduğundan güvenilir biçimde dalga biçimi olarak yeniden oluşturulmuş sayılmaz.
- Dar akım darbeleri ve yüksek harmonik içeren SMPS, LED sürücü, triyak/dimmer ve inverter yüklerde RMS/PF hatası beklenebilir; hata büyüklüğü deneyle bulunmalıdır.

**Karar:** ADS1115 ile temel bileşen ve zamanlama araştırması yapılabilir. Harmonikli yüklerde True PF doğruluğu henüz bilinmiyor.

## 4. ALERT/RDY zaman damgası ve delta-sigma dönüşümünün anlamı

ALERT/RDY, dönüşüm verisinin hazır olduğunu bildirir. Kesme anında alınan zaman damgası, dönüşümün tamamlanma/sonucun hazır olma zamanını belirtir; analog girişin tek bir fiziksel andaki nokta örneği olarak yorumlanmamalıdır.

ADS1115 delta-sigma dönüşüm ve dijital filtreleme kullandığından her dönüşümün etkin zaman karşılığı ve gecikmesi ayrıca ele alınmalıdır. Bu nedenle veri kaydında en az şu zamanlar ayrı tutulmalıdır:

- dönüşüm hazır sinyalinin zaman damgası (t_rdy)
- I²C veri okuma zamanı (t_read)
- kanal kimliği ve dönüşüm sıra numarası
- ham ADC kodu
- ADC yapılandırması ve seçili data rate
- atlanan/tekrarlanan dönüşüm ve tampon taşması bilgisi

Kesme işleyicisi mümkün olduğunca kısa tutulmalı; I²C okuma ve veri işleme görev/buffer tarafında yapılmalıdır.

Single-shot veya continuous mode için bu aşamada kesin karar verilmemiştir. Her iki yaklaşımın gerçek kanal sırası, dönüşüm kaybı ve zamanlama davranışı test edilmelidir. ALERT/RDY kullanılması tek başına analog örnekleme anını kesinleştirmez.

## 5. Zaman hizalama ve enterpolasyon

- Her gerilim ve akım kaydı kendi kanal kimliği ve zaman damgasıyla saklanmalıdır.
- Kanal zaman farkı sabit varsayılmamalı; ortalama, minimum, maksimum ve standart sapması ölçülmelidir.
- Ortak zaman ızgarasına enterpolasyon, iki seriyi hesapta eşleştirmeye yardımcı olabilir.
- Enterpolasyon, ADC'nin örneklemediği yüksek frekanslı içeriği geri getirmez ve düşük örnekleme hızını telafi etmez.
- Örnekler eşit aralıklı değilse basit sum/N ortalaması zaman ortalamasını tam temsil etmeyebilir. Zaman ağırlıklı integrasyon veya ortak zaman ızgarasına yeniden örnekleme değerlendirilmelidir.
- Trapez integrasyonu düzensiz zaman aralıklarında kullanılabilecek bir yaklaşımdır; ancak yetersiz bant genişliği veya ciddi örnek kaybını çözmez.

ADC dönüşüm/filtre gecikmesi, ZMPT101B analog katı gecikmesi ve SCT013 ölçüm yolu gecikmesi tek bir sabit faz katsayısına gömülmemelidir. Sensör faz yanıtı frekansa bağlı olabileceği için temel bileşen düzeltmesi yüksek harmonikler için otomatik olarak geçerli sayılmaz.

## 6. Pencereleme ve DC ofset: önemli kavram ayrımı

Şebeke frekansına yakın tam sayıda periyot içeren pencereler, zaman alanı RMS ve aktif güç hesaplarının tekrarlanabilirliğini artırır. Sıfır geçişleri veya başka bir frekans tahmin yöntemi pencere sınırlarına yardımcı olabilir.

Ancak **spektral sızıntı (spectral leakage) esas olarak FFT/frekans alanı analizindeki pencereleme olgusudur.** Tam periyot penceresi zaman alanı P/RMS/PF hesapları için yararlı bir tercih olsa da her zaman alanı hesabının matematiksel olarak geçerli olmasının mutlak önkoşulu şeklinde sunulmamalıdır. Tam periyot olmayan pencere, dalga biçimi ve yük değişimine bağlı sınır etkisi ve pencereler arası salınım oluşturabilir.

DC bias için:
- Ham kanal ortalaması (mean_v_raw, mean_i_raw) ayrıca kaydedilmelidir.
- Tam veya yeterince tam periyot içeren AC penceresinde pencere ortalamasını çıkarmak ADC biasını azaltmak için uygundur.
- Tam periyot olmayan pencerede ortalama çıkarılması, AC dalganın pencere içindeki artık bileşenini de ofset gibi çıkarabilir.
- Gerekirse yavaş DC değişimini izleyen DC-blocker/yüksek geçiren filtre değerlendirilebilir; filtre kesim frekansı ve faz etkisi kaydedilmelidir.
- SCT013 ve ZMPT101B transformatör tabanlı ölçüm yolları olduğundan bunlarla şebeke tarafındaki gerçek DC bileşen ölçülemez. Burada amaç ADC/analog çıkış biasını izlemek ve AC bileşeni ayırmaktır.

## 7. Dirençli yük testi: gerekli ama tek başına yeterli değil

Kettle, ısıtıcı veya uygun rezistif yük, ilk genel doğrulama için yararlıdır. Beklenen PF yaklaşık 1'dir. Bu test kanal polaritesini, temel genlik ölçeklerini, sinyal kırpılmasını ve ölçüm zincirinin ilk kararlılığını kontrol etmeye yardımcı olur.

Ancak yalnızca PF'nin 1'e yakın çıkması, faz gecikmesinin hassas biçimde bulunduğunu kanıtlamaz. Küçük faz hatalarında cos(phi) eğrisi 0 derece çevresinde yataydır; bu nedenle bir miktar faz hatası PF sonucunda çok küçük görünebilir.

Faz doğrulamasının sonraki aşamasında güvenli ve bilinen faz ilişkisine sahip kontrollü bir reaktif test yükü veya uygun düşük gerilimli test düzeneği kullanılmalıdır. Ev tipi motorun faz açısı önceden bilinen standart referans gibi kabul edilmemelidir.

## 8. Düşük akım eşiği: hazır sayı alınmayacak

Google ve Gemini yanıtlarında 0,15 A, 0,25 A, 35 VA veya 50 mA gibi örnek eşikler önerilmiştir. Bunlar BERO ölçümüyle belirlenmiş değerler değildir ve doğrudan firmware'e taşınmayacaktır.

BERO'nun önceki SCT013 30A/1V deneylerinde düşük akım bölgesinde yaklaşık 0,3–0,5 A altında ölçüm güvenilirliğinin zayıfladığı; yaklaşık 0,5 A civarının daha gerçekçi alt çalışma bölgesi olduğu gözlenmişti. Bu geçmiş gözlem PF için otomatik eşik değildir; PF daha hassas zaman/faz ve gürültü koşullarına sahiptir.

Yeni PF kolunda:
1. Yüksüz kayıtla kanal gürültü tabanı ölçülecek.
2. Bilinen yüklerde Irms ve S davranışı karşılaştırılacak.
3. Kabul edilebilir hata aralığına göre eşik belirlenecek.
4. Eşik altındaki PF, 0 veya 1 olarak değil invalid/below_threshold olarak kaydedilecek.

## 9. İstatistiksel veri alanları

Pencere başına en az:
- pencere başlangıç/bitiş zamanları, süre ve pencere kimliği
- gerilim/akım örnek sayıları
- kanal başına örnek aralığı ortalama, std, minimum ve maksimum değerleri
- kanal zaman ofseti ve varsa kayıp örnek sayısı
- ham ortalama/ofset, std, min/max ve peak
- Vrms, Irms, aktif güç P, görünür güç S, PF
- şebeke frekansı tahmini ve çevrim sayısı
- clipping, low-current, timing, buffer-overrun ve valid bayrakları

İlave analizler:
- PF ve güç değerleri için ortalama, std, medyan, IQR ve MAD
- uzun süreli sürüklenme için gerekirse Allan sapması
- tekrarlanabilirlik ile doğruluğun ayrı raporlanması
- zaman bağımlılığı varsa bootstrap'ta bağımsız pencere varsayımı yerine blok örnekleme değerlendirilmesi
- yeterli örnekleme hızı ve uygun anti-alias koşulları sağlandığında FFT/THD analizi

N = sqrt(S² - P²) hesaplanırsa bunu genel sinüzoidal olmayan durumda klasik reaktif güç Q olarak adlandırmamak gerekir. Daha doğru adlandırma toplam aktif olmayan güç (N_nonactive) olur. THD ve temel bileşen ayrımı ayrıca yapılmalıdır.

## 10. PGA ve analog giriş sınırları

PGA'daki ±2.048 V veya ±4.096 V seçimi ADC'nin diferansiyel tam ölçek aralığıdır; analog giriş pinlerinin besleme raylarının üzerine çıkabileceği anlamına gelmez. ADS1115 analog pinlerinde izin verilen gerilim, besleme gerilimi sınırlarıyla ayrıca kısıtlıdır.

- PGA aralığı, sensörün diferansiyel genliği ve ortak-mod gerilimiyle birlikte seçilmelidir.
- 3.3 V ile beslenen kartta pinlerin güvenli giriş aralığı ayrıca doğrulanmalıdır.
- “±2.048 V seçilirse kesin kırpılır” veya “±4.096 V tüm 0–3.3 V sinyal için otomatik güvenlidir” gibi genellemeler yapılmamalıdır.
- ZMPT101B kartının çıkışı ve SCT013 bias devresi ölçülmeden PGA ayarı kesinleştirilmemelidir.

## 11. Osiloskop ve şebeke güvenliği

FNIRSI 2D15P kılavuzu, cihazın güç kablosundaki koruyucu toprak ile topraklandığını belirtir. Bu nedenle cihazın taşınabilir/bataryalı görünmesi, her durumda girişlerinin yalıtılmış ve şebekeden bağımsız olduğu anlamına gelmez.

- Osiloskop probunun ground klipsi faz veya nötre bağlanmayacaktır.
- İki kanalın ground uçları ortak kabul edilerek bağlantı planlanacaktır.
- Şebeke üzerinde doğrudan prob bağlantısı yapılmayacaktır.
- İlk deneyler yalnızca güvenli, galvanik olarak izole düşük gerilimli AC sinyalle yapılacaktır.
- Ototransformatör tek başına galvanik izolasyon sağlamaz.
- ZMPT101B kartının transformatör içermesi, komple modül/kurulumun otomatik olarak güvenli olduğunu kanıtlamaz.
- USB ile bilgisayara bağlı ESP32, osiloskop ve sensör ground ilişkisi ayrıca değerlendirilmelidir.

## 12. Birleştirilmiş deney sırası

### Faz 0 – Şebekesiz ADC zamanlama testi
1. ADS1115 ve ESP32 ile iki girişe aynı güvenli düşük gerilimli DC seviyeyi uygula.
2. Kanal başına dönüşüm hazır zamanı, I²C okuma zamanı, örnek aralığı, jitter ve kayıp dönüşümleri kaydet.
3. Bu DC deneyi yalnızca dönüşüm döngüsü ve zamanlama istatistiğini gösterir; kanal faz kaymasını göstermez.

### Faz 1 – Ortak 50 Hz sinüs testi
1. Her iki ADC kanalına aynı, güvenli düşük genlikli, ADC aralığı içinde kalan ve uygun DC bias taşıyan 50 Hz sinyal uygula.
2. Aynı sinyalin iki kanalda ölçülen genlik ve faz farkını zaman damgalarıyla incele.
3. Mümkünse single-shot ve continuous taramayı karşılaştır.
4. Wi-Fi kapalı/açık ve farklı I²C koşullarında gerçek SPS ve jitter farkını kaydet.
5. Ham veriyi sakla; önce Python/offline analiz yap.

### Faz 2 – Sensörlerin ayrı karakterizasyonu
1. ZMPT101B kartı geldiğinde PCB revizyonu, op-amp, pinler, besleme, bias ve çıkış salınımını görsel ve ölçümsel olarak doğrula.
2. İlk testte şebeke kullanma; güvenli izole düşük gerilimli AC kaynakla çıkışın ofset, genlik, simetri ve faz davranışını incele.
3. SCT013 ölçüm yolunun genlik ve faz davranışını uygun güvenli test düzeneğinde ayrı incele.

### Faz 3 – Birleşik dirençli yük testi
Her iki analog zincir ve ADC zamanlaması ayrı ayrı bilindikten sonra dirençli yükte Vrms, Irms, P, S ve PF hesaplanır. PF≈1 ilk kontrol kriteridir; tek başına faz doğrulaması sayılmaz.

### Faz 4 – Reaktif yük ve düşük akım testleri
Bilinen faz ilişkisine sahip güvenli test düzeneğiyle faz telafisi sınanır. Düşük akım eşiği yüksüz gürültü ve tekrarlı yük verisinden çıkarılır.

### Faz 5 – Harmonikli yükler ve mimari kararı
SMPS, LED, dimmer ve inverter yüklerde dalga biçimi, crest factor, PF ve referans farkları incelenir. ADS1115'in yüksek harmonikleri temsil etme sınırı veriyle ortaya konur. Sonuç yetersizse daha hızlı/eşzamanlı ADC değerlendirilir.

## 13. İlk deney için net karar

**İlk deney ZMPT101B veya şebeke bağlantısı değil, ADS1115'in şebekesiz zamanlama karakterizasyonudur.**

İlk olarak DC testi ile dönüşüm periyotları ve jitter ölçülecek; ardından aynı 50 Hz düşük gerilimli sinyal iki kanalda karşılaştırılarak kanal yanıtı ve göreli faz farkı incelenecektir. Sadece DC sinyal üzerinden kanal faz kayması hesaplanamaz.

Ölçüm yazılımı ilk aşamada PF üretmek zorunda değildir. Önce ham veri, zaman damgası ve ADC durum bilgisi doğru kaydedilmelidir.

## 14. Deney öncesi açık kalan konular

- ADS1115 gerçek kanal başı SPS ve jitter: ölçülmedi.
- MUX/kanal geçişinin etkin zaman farkı: ölçülmedi.
- ALERT/RDY olayının analog girişe göre etkin zaman karşılığı: ölçülmedi.
- ZMPT101B hazır kartın gerçek PCB revizyonu ve çıkış faz yanıtı: kart fiziksel olarak incelenmedi.
- SCT013 ve ZMPT101B toplam faz yanıtı: ölçülmedi.
- ADS1115 ile harmonikli yüklerde True PF hatası: ölçülmedi.
- Düşük akım PF geçerlilik eşiği: belirlenmedi.
- PF hesaplama firmware'i: yazılmadı/doğrulanmadı.

## 15. Kaynaklar

- Texas Instruments – ADS1115 ürün sayfası ve veri sayfası: https://www.ti.com/product/ADS1115
- Texas Instruments – ADS111x veri sayfası PDF: https://www.ti.com/lit/ds/symlink/ads1115.pdf
- FNIRSI 2D15P kullanım kılavuzu: https://www.manualslib.com/manual/4108609/Fnirsi-2d15p.html

Kaynaklardaki üretici özellikleri ile BERO'da henüz ölçülmemiş uygulama performansı birbirinden ayrı tutulmalıdır.


## 16. Copilot ek değerlendirmesi – teknik inceleme ve düzeltmeler

Kullanıcı tarafından 2026-11-22 tarihinde ek bir Copilot yanıtı sağlandı. Bu yanıt, önceki dört görüşün ortak sonucu olan “önce zamanlama ve senkronizasyonu karakterize et” yaklaşımını destekliyor. Ancak ADS1115 zaman hesabında önemli bir iç tutarsızlık ve benimsenmemesi gereken bazı sabit eşikler içeriyor.

### 16.1 Önemli zaman hesabı düzeltmesi

Copilot ek yanıtında:
- Bir kanalın yaklaşık 2,32 ms aralıkla,
- İki kanal dönüş sırasının yaklaşık 4,65 ms'de tamamlandığı,
- 2,32 ms kanal kaymasının 50 Hz'de yaklaşık 41,8° oluşturduğu

ifade ediliyor.

Bu üç sayı 860 SPS ayarıyla doğrudan tutarlı değildir.

TI veri sayfasına göre seçilen data rate 860 SPS olduğunda nominal tek dönüşüm süresi:
- 1 / 860 = 1,163 ms

İki kanal ideal olarak dönüşümlü ve her kanal için bir dönüşüm kullanılarak taranırsa örnek sıra yaklaşık şöyledir:

- A dönüşümü: t = 0
- B dönüşümü: t ≈ 1,163 ms
- A dönüşümü: t ≈ 2,326 ms
- B dönüşümü: t ≈ 3,489 ms

Bu ideal hız varsayımında:
- Her kanalın kendi tekrar aralığı yaklaşık 2,326 ms, yani yaklaşık 430 SPS olur.
- Ardışık A ve B dönüşüm tamamlanmaları arasındaki nominal aralık yaklaşık 1,163 ms olur.
- 50 Hz için 1,163 ms yaklaşık 20,9°'dir.
- 2,326 ms ise 50 Hz'de yaklaşık 41,9°'dir; fakat bu ideal dönüşümlü dizide aynı kanalın ardışık örnekleri arasındaki süredir, A-B kanal farkı değildir.

Gerçek I²C/sürücü çevrimi 1,163 ms'den uzun olabilir. Dolayısıyla bu nominal zaman hesabı BERO'nun gerçek gecikmesi olarak kabul edilmez. Copilot'un 2,32 ms değerini “kanallar arası kayma” olarak kullanması hatalıdır; gerçek t_A, t_B, dönüşüm hazır ve okuma zamanları deneyle kaydedilmelidir.

Kaynak: TI ADS1115 ürün sayfası ve ADS111x veri sayfası. Ürün sayfası 8–860 SPS, MUX ve single-cycle settling özelliklerini belirtir: https://www.ti.com/product/ADS1115

### 16.2 8,6 örnek/periyot ve “gerçek PF için yetersiz” hükmü

430 SPS/kanal varsayımı altında 50 Hz için:
- 430 / 50 = 8,6 örnek/periyot
- Nyquist sınırı 430 / 2 = 215 Hz

400 SPS/kanal varsayımı için Nyquist sınırı 200 Hz olur. Dolayısıyla “ADS1115 iki kanalda kesin 200 Hz üstünü ölçemez” ifadesi, 400 SPS varsayımı açıkça belirtilmeden genel değer olarak yazılmamalıdır.

8,6 örnek/periyot temel 50 Hz sinüsü üzerinde deney yapmayı tamamen anlamsız kılmaz. Saf veya düşük harmonikli dalgalarda zaman hizalama ve doğru kanal modeli ile sınırlı deneyler yapılabilir. Ancak bu örnekleme hızı 5. harmonik olan 250 Hz'i dahi Nyquist sınırı altında tutmaz; dar akım darbeleri ve yüksek harmoniklerin toplam RMS/aktif güç üzerindeki katkısı güvenilir biçimde yakalanmayabilir.

Bu nedenle:
- “ADS1115 gerçek PF için kesinlikle yetersizdir” hükmü henüz BERO ölçümüyle kanıtlanmış değildir.
- “ADS1115 True PF için yeterlidir” hükmü de kanıtlanmış değildir.
- Doğru karar, ölçülen örnekleme hızı ve hedeflenen harmonik bant genişliği üzerinden hata bütçesi oluşturarak verilecektir.

### 16.3 Önerilen alternatif ADC'ler ve kullanıcı proje kararı

Copilot MCP3208, MCP3202, ADS7868/ADS7865, STM32 ADC/DMA ve ESP32-S3 ADC/DMA seçeneklerini listeliyor.

BERO için:
- **MCP3208 yeniden öneri listesine alınmayacaktır.** Kullanıcı bu entegreyle daha önce uzun ve verimsiz bir deney süreci yaşamış, yeniden ele almak istemediğini açıkça belirtmiştir.
- Yeni ADC satın alma kararı şimdilik ertelenmiştir.
- İleride yükseltme gerekirse eşzamanlı örnekleme, kanal sayısı, etkin örnekleme hızı, analog giriş aralığı, anti-alias filtre, sürücü karmaşıklığı ve veri aktarım yükü birlikte değerlendirilecektir.
- Sadece “yüksek SPS” ifadesi ADC seçmek için yeterli kriter değildir.

### 16.4 Sabit geçerlilik eşikleri kabul edilmiyor

Copilot'un aşağıdaki başlangıç değerleri BERO tarafından ölçülmüş değildir:
- S < 1 VA
- N < 8 periyot
- clipping oranı > 0,1%
- jitter > 1% periyot
- eksik örnek oranı > 0,1%
- Vrms < 20 V
- Irms < 0,05 A

Bunlar doğrudan firmware veya kabul testi kriteri yapılmayacaktır. Eşikler yüksüz gürültü kayıtları, kanal kalibrasyonu, hata bütçesi ve tekrarlı yük deneyleriyle belirlenecektir.

PF işaretinin geçerlilik kontrolü de uygulama yönüne göre tanımlanmalıdır. Tek yönlü tüketim senaryosunda pozitif PF beklenebilir; çift yönlü güç akışında negatif aktif güç/PF işaret bilgisi taşıyabilir. Genel matematiksel sınır, kullanılan işaret tanımına göre |PF| ≤ 1 olup negatif işaret otomatik olarak ölçüm hatası sayılmamalıdır.

### 16.5 Dirençli 100 W yük ve PZEM önerisinin yeri

100 W dirençli yükte PZEM karşılaştırması, sensörler ve ADC zamanlama testleri tamamlandıktan sonraki kontrollü doğrulama aşamasına aittir. Bu, ilk deney değildir.

İlk deney sırası değişmiyor:
1. ADS1115 ile şebekesiz DC zamanlama testi.
2. İki ADC kanalına aynı izole, düşük gerilimli 50 Hz sinyali vererek kanal aralığı ve göreli faz yanıtını inceleme.
3. Ham veriyi bilgisayarda analiz etme.
4. Sensörleri ayrı karakterize etme.
5. Güvenli koşullar ve ölçüm zinciri doğrulandıktan sonra dirençli yük deneyine geçme.

Osiloskopla doğrudan şebeke üzerinde ölçüm önerisi bu plana alınmamıştır. İlk analog testler galvanik olarak izole düşük gerilimli kaynakla yapılacaktır. Ototransformatör tek başına izolasyon sağlamaz.

### 16.6 İstatistik önerilerinin değerlendirilmesi

Yararlı alanlar:
- zaman damgası, örnek sayısı, gerçek etkin SPS
- jitter, kayıp örnek, clipping
- Vrms, Irms, P, S, PF ve geçerlilik
- DC offset, crest factor ve yeterli bant genişliği sağlanırsa THD
- pencere bazında medyan, IQR, standart sapma ve güven aralığı

Daha sonra değerlendirilecekler:
- yüzde 95 güven aralığı için bootstrap; ardışık pencerelerde zaman bağımlılığı varsa blok bootstrap
- pencere dışı PF kararlılığı ve autocorrelation
- P, S ve PF arasındaki korelasyonlar

P, S ve PF matematiksel olarak birbirine bağlı değişkenler olduğundan korelasyon katsayıları tek başına ölçüm doğruluğunu göstermez. İlk aşama için öncelik değildir.

Copilot'un metninde RMS denklemleri biçimlendirme sırasında karekök işareti olmadan görünmektedir. Gerçek RMS tanımında karekök zorunludur: Vrms = sqrt(mean(v²)), Irms = sqrt(mean(i²)). Bu bir içerik hatası değil, metin aktarım/biçimlendirme kaybı olabilir; özgün yanıtın matematik görünümü ayrıca teyit edilmemiştir.

### 16.7 Bu ek yanıt sonrası nihai karar

Copilot ek yanıtı ana araştırma yaklaşımını değiştirmiyor. Ancak 2,32 ms ve 41,8° hesabı düzeltilmelidir; bu değerler ölçülmüş kanal kayması olarak kullanılmayacaktır.

**İlk deney hâlâ şebekesiz ADS1115 zamanlama karakterizasyonudur.** PF firmware'i veya nihai ADC kararı bu aşamada yazılmayacaktır.



## 17. Claude Faz 1 kodları ve Gemini'nin son sentezi

Claude, Faz 1 için iki taslak dosya sağladı:
- ESP32 + ADS1115 single-shot / ALERT-RDY RAM yakalama sketch'i: kullanıcı yüklemesi `bero_phase1_capture.ino`
- Zamanlama, sıra takası, sinüs uyumu, interpolasyon ve PF hata bütçesi Python betiği: kullanıcı yüklemesi `bero_phase1_analysis.py`

Gemini, RAM tamponu, g/h sıra takası, joint_fit ile artık gecikme ve 50/75/100/125 Hz taraması önerilerini destekledi. Kod incelemesi ve sentetik test sonuçları ayrı kayıtta tutuldu:
- [Faz 1 Claude Kodu ve Gemini Sentezi İncelemesi](FAZ1/FAZ1-CLAUDE-KODU-GEMINI-INCELEMESI-2026-11-22.md)

Önemli sonuçlar:
- Python sözdizimi kontrol edildi ve sentetik `--simulate` çalıştırıldı; bu donanım testi değildir.
- Sentetik 20 µs artık gecikme yaklaşık 20,07 µs olarak bulundu; aynı simülasyonda 125 Hz testi gecikmeyi güvenilir geri bulamadı (yaklaşık 12,68 µs ortalama ve 32,85 µs blok std). 125 Hz doğruluk kalibrasyonu olarak kabul edilmedi.
- M2'nin sentetik sapması trapez kuralının genel hatası değildir; iki lineer interpolasyonun ürününü birleşik ızgarada trapezle entegre etme uygulamasının sayısal hatası olabilir.
- Arduino sketch'i henüz derlenmedi, karta yüklenmedi ve ADS1115 ile denenmedi.
- FNIRSI 2D15P sinyal jeneratörünün dokümanında bağımsız DC offset ayarı açıkça gösterilmedi. +0,9 V offset bulunduğu varsayılmayacak; çıkış ölçülecek veya ayrı biaslı AC-kuplaj ağı tasarlanacaktır.
- Gemini'nin şebekeye bağlı 10 µF kapasitör ve R||C testleri bu aşamaya alınmadı. İlk analog testler izole düşük gerilimle yapılacaktır.
- İlk deney kararı değişmedi: şebekesiz DC zamanlama testi, ardından aynı düşük gerilimli 50 Hz sinyalin iki ADS1115 diferansiyel kanalında karşılaştırılması.
