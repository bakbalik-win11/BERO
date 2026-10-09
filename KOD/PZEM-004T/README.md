# PZEM-004T — kod rehberi

## Klasör haritası

- [Örnek Kod-1 — Arduino/ESP32 UART ile ölçüm okuma](ORNEK-KOD-1/README.md)
- [Örnek Kod-2 — ESPHome UART yaklaşımı](ORNEK-KOD-2/README.md)
- [Örnek Kod-3 — Haberleşme hata ayıklama](ORNEK-KOD-3/README.md)
- [Hesaplama ve ölçüm yorumlama](HESAPLAMA/README.md)

Bu rehber PZEM-004T V3.0 ve mandulaj kütüphanesi için başlangıç noktasıdır. Eski PZEM sürümleriyle uyumluluk varsayma. Kart etiketini ve ürün PDF'sini kontrol et.

PZEM ölçüm değerlerini kendi içinde hesaplayıp UART üzerinden sayısal olarak sunar. ESP32 tarafında analog ADC/RMS kodu yazmak yerine haberleşme, veri geçerliliği ve Home Assistant aktarımı test edilir.

Kaynak: https://github.com/mandulaj/PZEM-004T-v30

**Kodlar örnektir; BERO donanımında derlenmiş veya fiziksel olarak test edilmiş değildir.**