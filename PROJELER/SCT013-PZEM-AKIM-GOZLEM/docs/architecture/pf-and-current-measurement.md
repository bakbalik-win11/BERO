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

Buna göre aynı gerilim ve aktif güçte PF azaldığında gereken RMS akım artar. Bu nedenle düşük PF'li bir yükte SCT'nin daha yüksek akım genliği/ölçümü göstermesi otomatik olarak hata sayılmamalıdır; fiziksel olarak beklenen akım artışı olabilir.

Doğrusal olmayan yüklerde (ör. anahtarlamalı LED sürücüleri) gerçek PF yalnızca faz açısının kosinüsü değildir. Akım dalga şekli bozulması da PF'yi etkileyebilir. Bu durumda akımın örneklenmesi, pencere özellikleri ve RMS çıkarımı önem kazanır.

## BERO için deney yaklaşımı

Amaç PF'yi SCT'den tahmin etmek veya PF ölçer geliştirmek değildir. Amaç, farklı yük/PF koşullarında SCT verisinden PZEM akımına ne kadar iyi ulaşıldığını gözlemek ve PF bilgisinin modele eklenmesinin gerekli olup olmadığını deneyle belirlemektir.

1. Önce PF modele girdi verilmeden SCT tabanlı model kurulur.
2. Farklı yüklerin (özellikle 100 W/150 W akkor ve 8,5 W LED) ortak kararlı SCT-PZEM alanları etiketlenir.
3. Model aynı etiketli eğitim verisi üzerinde değerlendirilir; hata ve ±%4 sınırında kalan örnek oranı yük bazında raporlanır.
4. Daha sonra aynı veri ve koşullarla PF girdili model denenebilir. PF girdisinin sağladığı fark, PF'siz sonuçla karşılaştırılır.

Bu karşılaştırma, PF'nin yararlı olup olmadığını gösteren bir deneydir; önceden PF'nin zorunlu olduğu varsayılmaz.

## Yorumlama sınırları

- Düşük PF, aynı aktif güçte RMS akımın artmasına yol açabilir; SCT'nin daha yüksek okuması bu nedenle tek başına hata değildir.
- SCT'nin daha yüksek okuması tek başına doğru olduğunu da kanıtlamaz; PZEM akım referansı ve ölçüm koşullarıyla karşılaştırılır.
- PF düşüşü tek başına SCT örnekleme hızını azaltmaz veya ölçümü geciktirmez. Gecikme ve ölçüm farkları; sensör, ADC, örnekleme, filtreleme, pencereleme ve PZEM güncelleme davranışı üzerinden ayrıca incelenmelidir.
- PZEM'in PF değerinin nasıl hesaplandığı ve hangi örnekleme/ortalama pencerelerini kullandığı, mevcut donanım kaydında ayrıntılı olarak doğrulanmış değildir. İç algoritmaya ilişkin kesin iddia kurulmaz.
- PZEM'in doğrudan hat gerilimi ölçmesi, PF değerinin bağımsız bir hat sensöründen geldiği anlamına gelmez; cihaz gerilim ve CT akım ölçümlerini birlikte kullanarak güç/PF sonuçlarını raporlar.

## Kaynak ve kanıt sınıfları

- **Üretici/ürün dokümanı:** [PZEM-004T V3.0 kullanım kılavuzu](https://eshop.tdmetal.cz/user/documents/upload/PZEM-004T-V3.0-Datasheet-User-Manual.pdf) ve [BERO PZEM donanım kaydı](../../../../DONANIM/PZEM-004T/README.md). PZEM'in gerilim, akım, aktif güç ve PF alanlarını raporladığını; 100 A varyantının harici CT kullandığını destekler.
- **Teknik açıklama:** [Analog Devices — Current Transformer Phase Error](https://www.analog.com/en/resources/technical-articles/accurate-measurement-of-power-and-energy-using-the-ade7753.html). CT faz hatasının güç/PF ölçümüne etkisi ile akım büyüklüğü ölçümünü birbirinden ayırmak için başvuru.
- **Ölçüm ilkesi:** [Fluke — True-RMS vs average-responding meters](https://www.fluke.com/en-us/learn/blog/electrical/what-is-true-rms). Doğrusal olmayan yüklerde dalga şekli ve ölçüm yönteminin önemini açıklar.

Bu kaynaklar BERO'daki SCT/ESP32 zincirinin doğruluğunu kanıtlamaz. BERO'ya özgü sonuçlar deney kaydıyla elde edilecektir.

## HEDEF / LOG / SONUÇ

- **HEDEF:** PF farklılığının SCT tabanlı akım tahmin hatasına etkisini ve PF bilgisinin modele katkısını deneyle görmek.
- **LOG:** Bu not, kullanıcıyla yapılan teknik değerlendirmeyi ve test edilebilir hipotezleri kaydeder.
- **SONUÇ:** PF modele baştan zorunlu girdi yapılmaz. İlk karşılaştırma PF'siz modelle başlar; PF'li model ancak karşılaştırma amacıyla eklenir. Henüz fiziksel ölçüm veya model deneyi yapılmamıştır.
