# ACS712 20A — kod ve hesaplama

- [Örnek Kod-1 — ESP32 ADC raw](ORNEK-KOD-1/README.md)
- [Örnek Kod-2 — MCP3208 SPI raw](ORNEK-KOD-2/README.md)
- [Örnek Kod-3 — ESPHome ADC izleme](ORNEK-KOD-3/README.md)
- [Akım hesaplama](AKIM-HESAPLAMA/README.md)
- [Hesaplama-1 — ADC raw, volt ve amper](AKIM-HESAPLAMA/HESAPLAMA-1.md)
- [Hesaplama-2 — DC ofset ve akım](AKIM-HESAPLAMA/HESAPLAMA-2.md)
- [Hesaplama-3 — AC RMS ve kalibrasyon](AKIM-HESAPLAMA/HESAPLAMA-3.md)

Varyant: **±20 A**, tipik **100 mV/A**. Formül: I = (VIOUT − V0) / 0.100. V0 gerçek sıfır akım ofsetidir. ADC girişindeki bölücü oranını tersine çevir; 5 V sensör çıkışını 3,3 V ADC'ye doğrudan bağlama. Tüm örnekler doğrulanmamış başlangıç kodudur.
