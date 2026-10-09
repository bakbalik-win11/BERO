# ZMCT103C — Akım hesaplama yöntemleri

## Dosyalar
- [Hesaplama-1 — Bias çıkarma ve RMS](HESAPLAMA-1.md)
- [Hesaplama-2 — Burden direnci ve akım oranı](HESAPLAMA-2.md)
- [Hesaplama-3 — Kalibrasyon ve örnekleme](HESAPLAMA-3.md)

## Temel zincir
Primer AC akımı → CT sekonder akımı → burden gerilimi → bias/koruma → ADC raw → bias çıkarma → RMS → amper kalibrasyonu.

Çıplak ZMCT103C nominal oranı 1000:1'dir; 5 A primerde 5 mA sekonder. İdeal burden hesabında 50 Ω → 0,25 V RMS; 100 Ω → 0,50 V RMS; 200 Ω → 1,00 V RMS. Bunlar ADC'ye doğrudan bağlanabilir demek değildir. Bias ve ADC giriş aralığı kontrol edilmelidir. Op-amp'lı modülün kazancı ayrıca kalibre edilir.