# PZEM-004T — kod rehberi

Bu klasör, PZEM-004T ailesinin ortak kod ve hesaplama arşividir; 10 A ve 100 A varyantlarına ait örnekler birlikte tutulur.

## Örnek kodlar

- [Örnek Kod-1 — Arduino/ESP32 UART ile ölçüm okuma](ORNEK-KOD-1/README.md)
- [Örnek Kod-2 — ESPHome UART yaklaşımı](ORNEK-KOD-2/README.md)
- [Örnek Kod-3 — Haberleşme hata ayıklama](ORNEK-KOD-3/README.md)
- [Örnek Kod-4 — Arduino/ESP32 ek örnek](ORNEK-KOD-4/README.md)
- [Örnek Kod-5 — ESPHome PZEMAC başlangıç örneği](ORNEK-KOD-5/README.md)
- [Örnek Kod-6 — UART/Modbus teşhis notları](ORNEK-KOD-6/README.md)

## Hesaplama

- [Hesaplama ve ölçüm yorumlama](HESAPLAMA/README.md)
- [Hesaplama-1 — Gerçek güç, görünür güç ve PF](HESAPLAMA/HESAPLAMA-1.md)
- [Hesaplama-2 — Enerji ve birim dönüşümü](HESAPLAMA/HESAPLAMA-2.md)
- [Hesaplama-3 — Haberleşme ve kalibrasyon kontrolü](HESAPLAMA/HESAPLAMA-3.md)

PZEM, SCT013 veya ACS758 gibi ham analog sensör değildir. AC gerilim/akım örneklemesini, güç ve enerji hesaplamasını modülün kendisi yapar; MCU seri arayüzden ölçüm kayıtlarını okur. Kod tarafında doğru UART bağlantısı, sürüm uyumluluğu, haberleşme ve ölçüm doğrulaması önemlidir.

Kaynak: https://github.com/mandulaj/PZEM-004T-v30

**Kodlar örnektir; BERO donanımında derlenmiş veya fiziksel olarak test edilmiş olduğu ayrıca belirtilmedikçe test edilmiş kabul edilmemelidir.**
