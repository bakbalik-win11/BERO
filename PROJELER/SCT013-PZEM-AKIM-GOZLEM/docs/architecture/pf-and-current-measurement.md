# PF değişimi ve akım ölçümüne etkisi — BERO teknik notu

**Durum:** Teknik gerekçe ve deney hipotezi; BERO üzerinde doğrulanmış sonuç değildir.

## Neden bu not var?

Önceki değerlendirmelerde PF, SCT'nin akım algılama biçimiyle gereğinden fazla iç içe düşünülmüştü. BERO açısından bunlar ayrı ölçüm zincirleridir:

- **SCT-013:** Akım trafosu üzerinden iletkendeki akıma bağlı analog sinyal üretir. SCT tek başına PF ölçmez.
- **PZEM-004T 100 A varyantı:** Gerilimi ölçüm girişlerine doğrudan bağlı hattan algılar; akımı harici CT üzerinden algılar. Modül ayrıca aktif güç ve PF değerlerini raporlar. PF, yalnızca CT'den alınan bağımsız bir ölçüm değildir; cihazın gerilim ve akım ölçümlerini/aktif güç ölçümünü kullanarak oluşturduğu ölçüm sonucudur. PZEM'in iç hesaplama ve örnekleme ayrıntıları, mevcut proje kayıtlarından kesinleştirilmiş değildir.

Dolayısıyla PZEM'in PF değeri ile SCT'nin analog akım sinyali aynı ölçüm yöntemi veya aynı algılama zinciri değildir.

## PF'nin akım büyüklüğüyle ilişkisi

Sinüzoidal koşullarda aktif güç:

`P = V_{RMS} \\times I_{RMS} \\times PF`

Buna göre aynı gerilim ve aktif güçte PF azaldığında gereken RMS akım artar. Bu, yalnızca teorik bir düzeltme değil, sonuçları yorumlarken korunması gereken fiziksel bir olasılıktır: düşük PF'li yükte daha yüksek RMS akım ve SCT sinyal genliği, tek başına ölçüm hatası değildir. Bununla birlikte gerçek yüklerde gerilim ve aktif güç de değişebileceği için bu ilişki ölçülen V, W, PF ve I değerleriyle sınanır; yalnızca nominal güç etiketinden sonuç çıkarılmaz.

Doğrusal olmayan yüklerde (ör. anahtarlamalı LED sürücüleri) gerçek PF yalnızca faz açısının kosinüsü değildir. Akım dalga şekli bozulması da PF'yi etkileyebilir. Bu durumda akımın örneklenmesi, pencere özellikleri ve RMS çıkarımı önem kazanır.

## PZEM PF yayınının SCT karşılaştırmasındaki rolü

PZEM'in yayınladığı PF değeri bu çalışma için özellikle kaydedilmelidir. PZEM-004T 100 A varyantında gerilim ölçümü doğrudan ölçüm hattından, akım ölçümü harici CT üzerinden alınır; cihaz aktif güç ve PF değerlerini de raporlar. Dolayısıyla PF alanı, PZEM'in gerilim ve CT akım ölçüm zincirinden üretilen birleşik bir sonuçtur. PF'nin CT'den bağımsız ayrı bir algılayıcıdan geldiği varsayılmamalıdır.

BERO'da PF yayınının rolü iki yönlüdür:

1. **Yük koşulunu tanımlamak:** Aynı aktif güçte veya farklı yüklerde PF değişirken PZEM akımının nasıl değiştiğini görmek.
2. **SCT karşılaştırmasını bağlama oturtmak:** PZEM PF değeriyle birlikte PZEM akımı ve SCT'den elde edilen akım tahmini kaydedilerek SCT-PZEM farkının farklı PF koşullarında değişip değişmediğini incelemek.

Bu, PZEM PF değerinin SCT'yi doğrudan etkilediği anlamına gelmez. PF, yükün gerilim-akım ilişkisi ve dalga şekli hakkında PZEM'in raporladığı bir göstergedir; SCT-PZEM farkıyla ilişkisi deneysel olarak incelenecek bir gözlemdir. PZEM'in PF algoritması ve iç ölçüm penceresi bilinmediğinden PF, SCT örnekleriyle anlık/milisaniyelik eşdeğer kabul edilmez. Önce PZEM akım, PF ve güncelleme davranışı birlikte kaydedilir.

E09 deney bağlantısı: [PF koşulu ile SCT/PZEM akım karşılaştırması](../../experiments/E09-pf-current-relationship/README.md). Bu deney PZEM'in PF ve CT akım yayınını birlikte kaydederek SCT-PZEM farkını farklı yük koşullarında inceleyecektir.

## BERO için deney yaklaşımı

Amaç PF'yi SCT'den tahmin etmek veya PF ölçer geliştirmek değildir. Amaç, farklı yük/PF koşullarında SCT verisinden PZEM akımına ne kadar iyi ulaşıldığını gözlemek ve PF bilgisinin modele eklenmesinin gerekli olup olmadığını deneyle belirlemektir.

1. Önce PF modele girdi verilmeden SCT tabanlı model kurulur.
2. Farklı yüklerin (özellikle 100 W/150 W akkor ve 8,5 W LED) ortak kararlı SCT-PZEM alanları etiketlenir; aynı alanlara ait PZEM akım, PF, gerilim ve aktif güç değerleri birlikte saklanır.
3. SCT özellikleri ile PZEM akımı arasındaki fark; yük türü ve PZEM'in raporladığı PF bağlamında incelenir. Düşük PF'li yükte daha yüksek SCT akım genliği görülmesi otomatik olarak ölçüm hatası sayılmaz.
4. Model aynı etiketli eğitim verisi üzerinde değerlendirilir; hata ve ±%4 sınırında kalan örnek oranı yük ve PF grubu bazında raporlanır.
5. Daha sonra aynı veri ve koşullarla PF girdili model denenebilir. PF girdisinin sağladığı fark, PF'siz sonuçla karşılaştırılır.

Bu karşılaştırma, PF'nin yararlı olup olmadığını gösteren bir deneydir; önceden PF'nin zorunlu olduğu varsayılmaz.

## Yorumlama sınırları

- Düşük PF, aynı aktif güçte RMS akımın artmasına yol açabilir; SCT'nin daha yüksek okuması bu nedenle tek başına hata değildir.
- SCT'nin daha yüksek okuması tek başına doğru olduğunu da kanıtlamaz; PZEM akım referansı ve ölçüm koşullarıyla karşılaştırılır.
- Bir sonuç `OUT_OF_RANGE` olduğunda, düşük PF koşulunda akımın fiziksel olarak artmış olabileceği önce yükün V/W/PF/I kayıtlarıyla kontrol edilir. Fiziksel akım artışı ile SCT-PZEM ölçüm farkı birbirine karıştırılmaz. ±%4 metriği, aynı kararlı alanın PZEM referans akımına uyumu ölçer; yükler arası akım seviyelerinin aynı olmasını şart koşmaz.
- PF düşüşü tek başına SCT örnekleme hızını azaltmaz veya ölçümü geciktirmez. Gecikme ve ölçüm farkları; sensör, ADC, örnekleme, filtreleme, pencereleme ve PZEM güncelleme davranışı üzerinden ayrıca incelenmelidir.
- PZEM'in PF değerinin nasıl hesaplandığı ve hangi örnekleme/ortalama pencerelerini kullandığı, mevcut donanım kaydında ayrıntılı olarak doğrulanmış değildir. İç algoritmaya ilişkin kesin iddia kurulmaz.
- PZEM'in doğrudan hat gerilimi ölçmesi, PF değerinin bağımsız bir hat sensöründen geldiği anlamına gelmez; cihaz gerilim ve CT akım ölçümlerini birlikte kullanarak güç/PF sonuçlarını raporlar.
- PZEM'in PF yayını SCT-PZEM karşılaştırmasında önemli bir gözlem alanıdır: PZEM akımı ve PF birlikte kaydedilir, SCT akım tahmin hatası PF koşuluna göre incelenir. Bu ilişki deneysel olarak gözlenir; PF'nin CT akım ölçümünü tek başına bozduğu veya geciktirdiği önceden varsayılmaz.

## Kaynak ve kanıt sınıfları

- **Üretici/ürün dokümanı:** [PZEM-004T V3.0 kullanım kılavuzu](https://eshop.tdmetal.cz/user/documents/upload/PZEM-004T-V3.0-Datasheet-User-Manual.pdf) ve [BERO PZEM donanım kaydı](../../../../DONANIM/PZEM-004T/README.md). PZEM'in gerilim, akım, aktif güç ve PF alanlarını raporladığını; 100 A varyantının harici CT kullandığını destekler.
- **Teknik açıklama:** [Analog Devices — Current Transformer Phase Error](https://www.analog.com/en/resources/technical-articles/accurate-measurement-of-power-and-energy-using-the-ade7753.html). CT faz hatasının güç/PF ölçümüne etkisi ile akım büyüklüğü ölçümünü birbirinden ayırmak için başvuru.
- **Ölçüm ilkesi:** [Fluke — True-RMS vs average-responding meters](https://www.fluke.com/en-us/learn/blog/electrical/what-is-true-rms). Doğrusal olmayan yüklerde dalga şekli ve ölçüm yönteminin önemini açıklar.

Bu kaynaklar BERO'daki SCT/ESP32 zincirinin doğruluğunu kanıtlamaz. BERO'ya özgü sonuçlar deney kaydıyla elde edilecektir.

## HEDEF / LOG / SONUÇ

- **HEDEF:** PZEM'in yayınladığı PF ile CT üzerinden ölçtüğü akımın, SCT tabanlı akım tahminiyle ilişkisinin farklı yüklerde gözlenmesi; PF bilgisinin modele katkısının deneyle belirlenmesi.
- **LOG:** PZEM akım, PF, gerilim ve aktif güç alanlarının aynı kayıt bağlamında tutulması; SCT özellikleri ve tahmin hatasıyla ilişkilendirilmesi planlandı.
- **SONUÇ:** PF modele baştan zorunlu girdi yapılmaz. Önce PF'siz model ve PF'ye göre hata gözlemi; ardından gerekirse PF'li model karşılaştırması yapılır. Henüz fiziksel ölçüm veya model deneyi yapılmamıştır.
