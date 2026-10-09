# Hesaplama-1 — Ofset çıkarma ve AC RMS

## Amaç

Hall sensörünün VIOUT çıkışı sıfır akımda orta gerilim civarındadır. Bu DC ofseti çıkarmadan doğrudan RMS almak, akım sinyaline ofsetin de dahil olmasına neden olur.

## Formüller

N örneğin ortalaması:
`V0_est = sum(V[i]) / N`

AC bileşenin RMS değeri:
`V_AC_RMS = sqrt(sum((V[i] - V0_est)^2) / N)`

050B için ideal nominal akım RMS tahmini:
`I_RMS ≈ V_AC_RMS / 0.040`

050U için nominal hassasiyet kullanılıyorsa:
`I_RMS ≈ V_AC_RMS / 0.060`

Bu oranlar VIOUT gerilimi içindir. ADC girişinde bölücü varsa VIOUT ölçeğine geri dönülmelidir.

## Pseudocode

```cpp
double mean = 0.0;
for (size_t i = 0; i < N; ++i) mean += voltage[i];
mean /= N;

double sumSq = 0.0;
for (size_t i = 0; i < N; ++i) {
  const double ac = voltage[i] - mean;
  sumSq += ac * ac;
}
const double vAcRms = sqrt(sumSq / N);
const double currentRms = vAcRms / 0.040; // yalnızca 050B nominali
```

## Sınırlamalar

- Pencere tam sayıda şebeke periyodunu kapsamazsa, dalga şekli bozuksa veya örnek aralıkları düzensizse sonuç etkilenebilir.
- Ortalama alma, pencere boyunca gerçek DC akım bileşenini de kaldırır. DC akımı ölçmek istiyorsan bu algoritma doğru yöntem değildir.
- Örnekleme hızı sinyalin frekansına uygun seçilmeli ve analog anti-alias filtre değerlendirilmelidir.
- Ham örnekler kırpılıyorsa hesaplama sonucu güvenilir değildir.
