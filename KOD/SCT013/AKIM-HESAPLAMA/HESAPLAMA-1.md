# Hesaplama-1 — Raw ADC kodlarından RMS

## Fikir

ADC her örnekte bir raw kod verir. Örnekler biaslı bir AC sinyalini temsil ediyorsa önce penceredeki ortalama kod çıkarılır, sonra sapmaların karelerinin ortalaması alınır ve karekökü bulunur.

`mean = sum(raw[i]) / N`

`raw_rms = sqrt(sum((raw[i] - mean)^2) / N)`

Bu sonuç **ADC count birimindedir**, amper değildir.

## Volt'a dönüştürme

ADC'nin gerçek aktarım fonksiyonu biliniyorsa count RMS volt RMS'e çevrilebilir. İdeal doğrusal yaklaşımda:

`V_rms ≈ raw_rms × Vref / (2^bits - 1)`

MCP3208 için bits=12 ve kod aralığı 0–4095'tir. Bu basit yaklaşım ADC offset/gain hatalarını, giriş devresini, attenuasyonu veya analog kazancı düzeltmez; kalibrasyon gerekebilir.

## Akıma dönüştürme

Sensör çıkışındaki volt RMS hesaplandıysa:

- SCT013-030: `I_rms ≈ V_sensor_rms × 30 A/V`
- SCT013-100: `I_rms ≈ V_sensor_rms × 100 A/V`

**Dikkat:** ADC pininde ölçülen voltaj, bias dahil gerilimdir. Ortalama/bias çıkarılmadan `V_rms` alınırsa AC sinyali yerine DC bias da hesaplamaya katılır. Ayrıca ADC pinindeki RMS gerilimini sensörün çıkış RMS gerilimi sanma; arada bölücü/kazanç varsa bunu hesaba kat.

## N=1000 örneği

1000 örnek yalnızca pencere boyutudur. Eğer örnekler 1 ms aralıkla alınmışsa pencere yaklaşık 1 saniye sürer; 100 µs aralıkla alınmışsa yaklaşık 100 ms sürer. Örnekleme aralığı eşit değilse sıradan aritmetik ortalama RMS formülü zaman ağırlığını doğru temsil etmeyebilir.

## Kısa pseudocode

```cpp
double mean = 0;
for (int i = 0; i < N; i++) mean += raw[i];
mean /= N;

double sumSq = 0;
for (int i = 0; i < N; i++) {
  double d = (double)raw[i] - mean;
  sumSq += d * d;
}
double rawRms = sqrt(sumSq / N);
```

Bu algoritma ham sinyalin AC bileşen büyüklüğünü sayım cinsinden verir. Volt ve amper kalibrasyonu ayrı aşamalardır.
