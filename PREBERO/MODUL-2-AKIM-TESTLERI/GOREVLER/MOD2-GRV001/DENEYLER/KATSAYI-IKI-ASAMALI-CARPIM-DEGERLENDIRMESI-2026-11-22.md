# İki aşamalı katsayı çarpımı değerlendirmesi – 2026-11-22

## Durum
**Değerlendirme kapatıldı. Fiziksel deney yapılmadı; yöntem mevcut haliyle biasın yerine geçen doğrulanmış bir çözüm olarak kabul edilmedi.**

## Amaç
Bias devresiyle uğraşmak yerine mevcut kalibrasyon katsayısını iki ayrı katsayıya bölüp ardışık çarparak aynı akım sonucuna ulaşma önerisini teknik olarak değerlendirmek.

## Değerlendirilen yöntem
Mevcut akım hesabının genel biçimi:

\[
I = RMS(ADC) \times K
\]

Önerilen iki aşamalı biçim:

\[
I = RMS(ADC) \times K_1 \times K_2
\]

Eğer K1 ve K2 sabit çarpanlarsa ve yalnızca K1 × K2 = K koşulu sağlanıyorsa, iki ifade matematiksel olarak aynıdır. Katsayının iki parçaya ayrılması tek başına yeni ölçüm bilgisi üretmez ve ölçüm hatasını, gürültüyü veya bias ihtiyacını azaltmaz.

## Bias ile farkı
Bias, analog sinyalin ADC girişine göre referans/çalışma noktasını etkileyen donanımsal bir düzenlemedir. Sabit çarpanlar ise ölçülen RMS sonucunu ölçekler. Ölçüm yolunda bias kaynaklı veya bias ihtiyacına bağlı bir DC referans/başlangıç noktası sorunu varsa, yalnızca iki sabit çarpanı çarpmak bu sorunu otomatik olarak gidermez.

İki katsayı ancak farklı ve bağımsız olarak tanımlanmış kalibrasyon aşamalarını temsil ediyorsa operasyonel olarak anlamlı olabilir. Örneğin bir katsayı ADC gerilim ölçeğini, diğeri sensör/akım dönüşümünü temsil edebilir. Ancak bu ayrımın fiziksel veya izlenebilir referanslarla ayrı ayrı belirlenmesi gerekir; keyfî bir bölme değildir.

## Mevcut proje verisiyle ilişki
- Kullanılan referans katsayı K=27.59 olarak korunmaktadır.
- Önceki bias kanal çapraz deneylerinde yaklaşık 0.47 A çalışma bölgesinde biaslı kolun üç tekrarda da daha yüksek ortalama ve PZEM'e göre daha düşük MAPE verdiği kaydedilmiştir. Bu bulgu biasın ölçüm sonucuna katkısını destekler; PZEM ground truth değildir.
- 150 W oturumlarında kanal ve oturum bazında farklılıklar görülmüştür. Bu kayıtlar tek başına iki katsayılı yaklaşımın biası ikame edebileceğini göstermez.
- Bu değerlendirme için yeni ADC ölçümü, yeni PZEM eşleştirmesi veya yeni ham log alınmamıştır.

## Karar
1. K değerini iki sabit sayıya bölüp çarpmak, mevcut tek K uygulamasına matematiksel olarak eşdeğerdir; bu nedenle tek başına ayrı bir deney/iyileştirme olarak sürdürülmeyecektir.
2. K=27.59 değiştirilmeyecek.
3. Çalışan YAML ve firmware değiştirilmeyecek.
4. Bias bağlantısı bu değerlendirme nedeniyle değiştirilmemiştir.
5. İleride iki katsayılı yapı kullanılacaksa, K1 ve K2'nin ayrı fiziksel/ölçümsel anlamı ve bağımsız kalibrasyon yöntemi önceden tanımlanmalıdır.

## Kapanış sınırı
Kapatılan konu, “mevcut katsayıyı iki sabit çarpana ayırmanın bias yerine geçip geçmeyeceği” önerisinin matematiksel değerlendirmesidir. Bu bir donanım deneyi veya yeni kalibrasyon doğrulaması değildir. MOD2-GRV001 görevi ve diğer açık deneyler bu kayıtla kapatılmış sayılmaz.
