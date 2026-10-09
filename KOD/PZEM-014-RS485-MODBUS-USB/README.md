# PZEM-014 RS485 Modbus + USB — kod ve hesaplama rehberi

## Klasör yapısı
- [Örnek Kod-1 — Python + USB–RS485 + Modbus RTU](ORNEK-KOD-1/README.md)
- [Örnek Kod-2 — ESP32 + RS485 UART](ORNEK-KOD-2/README.md)
- [Örnek Kod-3 — Home Assistant / ESPHome notları](ORNEK-KOD-3/README.md)
- [Hesaplama klasörü](HESAPLAMA/README.md)
- [Hesaplama-1 — Gerçek güç, görünür güç ve PF](HESAPLAMA/HESAPLAMA-1.md)
- [Hesaplama-2 — Enerji ve birim dönüşümü](HESAPLAMA/HESAPLAMA-2.md)
- [Hesaplama-3 — Modbus ve ölçüm doğrulama](HESAPLAMA/HESAPLAMA-3.md)

PZEM kendi içinde ölçüm yapar; MCU ham ADC örneklerini hesaplamaz. Kod tarafının odağı Modbus RTU, RS485 kablolaması, USB seri portu ve register değerlerinin yorumlanmasıdır. PZEM-014 0–10 A ve dahili şöntlüdür; PZEM-016 0–100 A ve harici CT kullanır.

Örnekler okuma odaklıdır; enerji sıfırlama ve fabrika kalibrasyon komutları kullanılmaz. Kodlar BERO donanımında fiziksel testten geçmemiştir.