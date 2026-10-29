# Aşama 1 — Yüksüz SCT uzun okuma

## Neden yapıyoruz?
Yük bağlamadan ölçüm zincirinin kendi davranışını görmek istiyoruz. Böylece yük altında görülen küçük değişimlerin temel ADC gürültüsü veya bias değişkenliğiyle karıştırılması riskini azaltabiliriz.

## Uygulama
- SCT ve bias bağlı olacak; ölçülen iletkenden akım geçmeyecek.
- Uzun kayıt alınır. İlk gözlemlerden sonra uygun süre belirlenir; kesin süre baştan dayatılmaz.
- 1, 2 ve 2,5 kS/s hedeflerinde kayıt alınır; gerçekleşen hız ayrıca kaydedilir.
- İlk pencere varsayımı 200 ms'dir. RMS, mutlak Peak, Peak-to-Peak, ortalama, standart sapma, min/max ve örnek sayısı çıkarılır.

## İncelenecekler
Bias/ortalama zamanla değişiyor mu? Pencereler ne kadar değişken? Hedef ve gerçek hız farklı mı? Yüksüz sinyalde yöntemler nasıl davranıyor? Bu aşama yük altındaki performansı veya gerçek akım doğruluğunu tek başına belirlemez.