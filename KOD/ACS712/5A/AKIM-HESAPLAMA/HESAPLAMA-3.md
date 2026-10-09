# Hesaplama-3 — AC RMS, toplam RMS ve kalibrasyon (5A)

## AC bileşen RMS

mean = sum(VIOUT[i]) / N

V_AC_RMS = sqrt(sum((VIOUT[i] − mean)^2) / N)

I_AC_RMS ≈ V_AC_RMS / 0.185

Bu yöntem pencere ortalamasını çıkarır; **DC akım bileşeni korunmaz**.

## DC+AC toplam RMS

Gerçek sıfır akım ofseti V0 ayrı ölçülür:

I_TOTAL_RMS ≈ sqrt(sum(((VIOUT[i] − V0) / 0.185)^2) / N)

Bu yöntem DC bileşeni de içerir. AC ve DC karışık dalga biçiminde yalnız AC RMS ile toplam RMS aynı değildir.

## Test ve kalibrasyon

- 50 Hz periyodu 20 ms'dir; pencere süresini gerçek örnek zaman damgalarından belirle.
- N=1000, 1000 örnek demektir; otomatik olarak 1 kS/s değildir.
- 1 kS/s örnekleme 500 Hz Nyquist sınırına sahiptir; harmonik/anti-alias gereksinimini değerlendir.
- ADC girişi kırpılıyorsa, sensör saturasyona yaklaşıyorsa veya örnek aralığı düzensizse sonuç güvenilmez olabilir.
- Sıfır akımda V0 ve bilinen birkaç DC/AC akım noktasında duyarlılık kalibrasyonu yap.
- Nominal 185 mV/A yalnız başlangıç katsayısıdır; sıcaklık ve VCC etkileri ölçülmelidir.
