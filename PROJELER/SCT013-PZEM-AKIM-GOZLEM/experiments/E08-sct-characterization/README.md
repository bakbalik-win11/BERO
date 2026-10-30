# E08 — SCT sinyalini tanıma

## Neden yapıyoruz?
E08, SCT-013 ve ESP32 dahili ADC ölçüm zincirinin davranışını kendi verisi üzerinden anlamak için planlanır. Amaç PZEM ile zaman eşleştirmesi veya laboratuvar düzeyinde doğruluk doğrulaması değildir. Örnekleme hızı, hesaplama yöntemi, SCT içinden geçirilen kablo tur sayısı ve yük durumunun sonuçlara etkisi incelenecektir.

## Aşamalar
1. [Yüksüz uzun okuma](stage-01-no-load.md): temel gürültü, bias ve pencere değişkenliği.
2. [100 W akkor matrisi](stage-02-100w-matrix.md): ilk tam karşılaştırma.
3. [150 W akkor ve 8,5 W LED](stage-03-load-comparison.md): yük seviyesi/türü etkisi.
4. [Aç-kapa testi](stage-04-on-off.md): geçişler ve kararlı görünen bölgeler.

## Ortak karşılaştırma
- Hedef hızlar: 1.000, 2.000 ve 2.500 örnek/s; gerçekleşen hız ayrıca kaydedilir.
- Kablo turu: 1, 2 ve 4.
- Her pencerenin aynı örnek kümesinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanır. Ortalama, standart sapma, minimum, maksimum ve örnek sayısı da kaydedilir.
- Yöntemlerin ham sayıları doğrudan birbirine göre sıralanmaz; her yöntemin kendi değişkenliği ve hız/tur değişimine duyarlılığı incelenir.
- PZEM veya başka ESP'nin ortalama akımı varsa genel deney notu olarak yazılabilir; SCT pencereleriyle zaman eşleştirmesi yapılmaz.
- Kararlılık eşiği, gereken pencere sayısı ve kesin kayıt süresi sonuçlar görülmeden belirlenmez.

Durum: AŞAMA 2 AÇILDI — HAZIRLIK. 100 W fiziksel ölçüm henüz yapılmadı; mevcut E00B firmware'i yüksek hızlı E08 edinimini karşılamaz.


## Grafik standardı — kullanıcı tarafından onaylandı (2026-10-30)

E08 grafiklerinde kullanıcının paylaştığı örnek görünüm esas alınır:
- X ekseni: gerçek zaman damgası.
- Y ekseni: ilk görünümde ADC RAW count; voltaj grafiği ayrı eksende/ayrı panelde sunulur.
- Mavi çizgi: bias referansı (GPIO34 RAW).
- Kırmızı çizgi: SCT sinyali (GPIO32 RAW).
- Yeşil kesikli dikey çizgi: açıkça kaydedilmiş ampul/SSR açılma olayı. Olay kaydı yoksa çizgi tahminî olarak işaretlenir ve grafikte açıkça “tahminî” denir.
- Aynı zaman ekseninde yüksüz başlangıç bölümü ve yük altındaki salınım birlikte gösterilir.
- Grafik çizgileri ham örneklerden üretilir; araya veri uydurulmaz. Örnekleme hızı, kanal başına gerçekleşen hız ve örnek sayısı başlık/alt yazıda belirtilir.

Önceki 1 saniyelik ESPHome grafiği yavaş örneklemeli aliasing/stroboskopik görünümü gösterir; gerçek 50 Hz dalga şeklini temsil etmez. Daha hızlı örnekleme grafiği ayrı bir ham veri edinim aşamasında üretilecektir. Görsel biçim onaylıdır; bu, önceki örnekleme hızının yeterli olduğu anlamına gelmez.
