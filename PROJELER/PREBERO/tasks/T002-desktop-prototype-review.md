# T002 — Masaüstü prototip bağlantı incelemesi

- **Durum:** PLANLANDI
- **Amaç:** ESP32D2 + ADS1115 + SCT düzeneğinin gerçek bağlantılarını belgelemek.

## Fiziksel olarak doğrula
- SCT model etiketi ve sekonder çıkış yapısı.
- AIN0/AIN1 bağlantısı; varsa burden, koruma ve filtre.
- Bias bağlantısı ve Modül 1 bias kutusunun yeri.
- ADS1115 besleme, GND, ADDR ve gerçek I²C adresi.
- ESP32D2 SDA/SCL pinleri.
- Firmware sürümü, MUX, PGA, sample rate, continuous mode ve RMS pencere ayarları.

## Kabul ölçütü
Fotoğraf/şema ve fiziksel kontrolle teyit edilen bağlantı listesi. Görülmeyen/ölçülmeyen değerler bilinmiyor olarak kalır.

## Çıktı
[hardware/desktop-prototype-wiring.md](../hardware/desktop-prototype-wiring.md).
