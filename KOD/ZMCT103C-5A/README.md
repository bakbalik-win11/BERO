# ZMCT103C 5 A — kod ve hesaplama rehberi

## Klasör yapısı

- [Örnek Kod-1 — ESP32 ADC ham örnekleme](ORNEK-KOD-1/README.md)
- [Örnek Kod-2 — MCP3208 SPI ham örnekleme](ORNEK-KOD-2/README.md)
- [Örnek Kod-3 — ESPHome ADC izleme](ORNEK-KOD-3/README.md)
- [Akım hesaplama yöntemleri](AKIM-HESAPLAMA/README.md)
- [Hesaplama-1 — Bias çıkarma ve RMS](AKIM-HESAPLAMA/HESAPLAMA-1.md)
- [Hesaplama-2 — Burden ve akım oranı](AKIM-HESAPLAMA/HESAPLAMA-2.md)
- [Hesaplama-3 — Kalibrasyon ve örnekleme](AKIM-HESAPLAMA/HESAPLAMA-3.md)

ZMCT103C **AC akım trafosudur**, Hall sensörü değildir ve DC ölçmez. Çıplak CT nominal oranı 5 A primer → 5 mA sekonder (1000:1). Sekonder akımı burden ile gerilime çevrilmeli; negatif AC yarım dalga ADC'ye doğrudan uygulanmamalıdır.

Op-amp'lı modülün çıkışı potansiyometre/kazanca bağlı olabilir. Kart çıkışı için sabit A/V değeri varsayma; kalibrasyon yap.

Tüm kodlar başlangıç/test örneğidir; BERO donanımında derlenmiş veya fiziksel olarak doğrulanmış değildir.