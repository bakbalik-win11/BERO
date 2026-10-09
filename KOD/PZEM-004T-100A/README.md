# PZEM-004T-100A — kod ve hesaplama rehberi

## Klasör yapısı

- [Örnek Kod-1 — Arduino/ESP32 ve PZEM-004T V3.0 kütüphanesi](ORNEK-KOD-1/README.md)
- [Örnek Kod-2 — ESPHome PZEMAC](ORNEK-KOD-2/README.md)
- [Örnek Kod-3 — UART/Modbus teşhis notları](ORNEK-KOD-3/README.md)
- [Ölçüm ve enerji hesaplama](HESAPLAMA/README.md)
- [Hesaplama-1 — Gerçek güç, görünür güç ve PF](HESAPLAMA/HESAPLAMA-1.md)
- [Hesaplama-2 — Enerji ve birim dönüşümü](HESAPLAMA/HESAPLAMA-2.md)
- [Hesaplama-3 — Haberleşme ve kalibrasyon kontrolü](HESAPLAMA/HESAPLAMA-3.md)

## Önemli

PZEM, SCT013 veya ACS758 gibi ham analog sensör değildir. AC gerilim/akım örneklemesini, güç ve enerji hesaplamasını modülün kendisi yapar; MCU seri arayüzden ölçüm kayıtlarını okur. Bu nedenle kod tarafının odağı ADC RMS algoritması değil, doğru UART bağlantısı, sürüm uyumluluğu, haberleşme ve ölçüm doğrulamasıdır.

Örnekler PZEM-004T V3.0 kaynaklarına göre hazırlanmıştır. Direnc.net ürün PDF'sindeki gerçek modül sürümü V3.0 olarak doğrulanmadı; kütüphaneyi kullanmadan önce kart sürümünü kontrol et. Kodlar BERO donanımında fiziksel olarak test edilmemiştir.