# Akım Hesaplama — yöntemler

Bu klasör sensör okumasından RMS ve ampere giden farklı yolları ayırır.

1. [Hesaplama-1 — Raw ADC kodlarından RMS](HESAPLAMA-1.md)
2. [Hesaplama-2 — Volt RMS ve SCT013 oranı](HESAPLAMA-2.md)
3. [Hesaplama-3 — EmonLib kalibrasyon yaklaşımı](HESAPLAMA-3.md)

Önerilen debug sırası: (1) ham ADC verisi doğru mu? (2) bias/orta nokta doğru mu? (3) dalga biçimi kırpılıyor mu? (4) volt dönüşümü doğru mu? (5) RMS doğru mu? (6) sensör oranı ve referans akımla kalibrasyon doğru mu?

Bu adımların herhangi birinde hata varsa son amper değeri de hatalı olur.
