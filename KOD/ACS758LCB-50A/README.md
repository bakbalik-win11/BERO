# ACS758LCB 50 A — kod ve hesaplama rehberi

## Klasör haritası

- [Örnek Kod-1 — ESP32 dahili ADC ile ham örnekleme](ORNEK-KOD-1/README.md)
- [Örnek Kod-2 — ESP32 + MCP3208 SPI ham örnekleme](ORNEK-KOD-2/README.md)
- [Örnek Kod-3 — ESPHome temel ADC izleme](ORNEK-KOD-3/README.md)
- [Akım hesaplama yöntemleri](AKIM-HESAPLAMA/README.md)
- [Hesaplama-1 — Ofset çıkarma ve RMS](AKIM-HESAPLAMA/HESAPLAMA-1.md)
- [Hesaplama-2 — Voltajdan amper](AKIM-HESAPLAMA/HESAPLAMA-2.md)
- [Hesaplama-3 — DC ortalama ve AC RMS ayrımı](AKIM-HESAPLAMA/HESAPLAMA-3.md)

## Önce model kodunu doğrula

ACS758LCB ailesinde “50 A” için en az iki farklı varyant önemlidir:
- 050B çift yönlü: tipik 40 mV/A, ±50 A.
- 050U tek yönlü: tipik 60 mV/A, 0…50 A.

Örneklerin hesaplaması varsayılan olarak 050B/40 mV/A içindir. Gerçek modülün varyantı doğrulanmadan kalibrasyon sabiti olarak kullanma.

## Ölçüm zinciri

1. Sensör VIOUT analog gerilimini üretir.
2. ADC bu gerilimi ham koda dönüştürür.
3. ADC kodundan gerilim hesabında gerçek VREF, bit çözünürlüğü ve varsa giriş bölücü/kazanç kullanılır.
4. Sıfır akım ofseti ölçülüp çıkarılır.
5. DC için ortalama; AC akım için ofset çıkarılmış örneklerin RMS değeri hesaplanır.
6. Amper ölçeği üretici nominal hassasiyetiyle başlatılır, referans ölçümle kalibre edilir.

Kodlar öğrenme ve kontrollü test örnekleridir; BERO donanımında derlenmiş veya fiziksel testten geçmiş değildir.
