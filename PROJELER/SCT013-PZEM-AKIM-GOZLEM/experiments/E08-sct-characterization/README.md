# E08 — SCT sinyalini tanıma

## Neden yapıyoruz?
E08, SCT-013 ve ESP32 dahili ADC ölçüm zincirinin davranışını kendi verisi üzerinden anlamak için planlanır. Amaç PZEM ile zaman eşleştirmesi veya laboratuvar düzeyinde doğruluk doğrulaması değildir. Örnekleme hızı, hesaplama yöntemi, SCT içinden geçirilen kablo tur sayısı ve yük durumunun sonuçlara etkisi incelenecektir.

## Aşamalar
1. [Yüksüz uzun okuma](stages/01-no-load-long-read.md): temel gürültü, bias ve pencere değişkenliği.
2. [100 W akkor matrisi](stages/02-100w-matrix.md): ilk tam karşılaştırma.
3. [150 W akkor ve 8,5 W LED](stages/03-load-comparison.md): yük seviyesi/türü etkisi.
4. [Aç-kapa testi](stages/04-on-off-response.md): geçişler ve kararlı görünen bölgeler.

## Ortak karşılaştırma
- Hedef hızlar: 1.000, 2.000 ve 2.500 örnek/s; gerçekleşen hız ayrıca kaydedilir.
- Kablo turu: 1, 2 ve 4.
- Her pencerenin aynı örnek kümesinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanır. Ortalama, standart sapma, minimum, maksimum ve örnek sayısı da kaydedilir.
- Yöntemlerin ham sayıları doğrudan birbirine göre sıralanmaz; her yöntemin kendi değişkenliği ve hız/tur değişimine duyarlılığı incelenir.
- PZEM veya başka ESP'nin ortalama akımı varsa genel deney notu olarak yazılabilir; SCT pencereleriyle zaman eşleştirmesi yapılmaz.
- Kararlılık eşiği, gereken pencere sayısı ve kesin kayıt süresi sonuçlar görülmeden belirlenmez.

Durum: PLANLANDI. Fiziksel kurulum ve ölçüm yapılmadı.
