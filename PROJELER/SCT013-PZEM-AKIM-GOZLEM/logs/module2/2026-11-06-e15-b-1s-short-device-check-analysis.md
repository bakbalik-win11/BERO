# E15 B turu — 1 saniye kısa cihaz kontrolü

Tarih: 2026-11-06, yerel saat +03:00

## Doğrulananlar
- ESPHome 2026.10.2; ESP32 rev3.1; derleme zamanı 14:12:57 +03:00.
- API çözümleme, bağlantı ve handshake başarılı.
- GPIO32 / ADC1_CH4, 12 dB ADC: handle init, config, calibration ve overall init OK.
- ct_clamp sample_duration=0.10s; update_interval=never.
- CH1 katsayı uygulanmış akım entity'si 44 kez yayımlandı.
- İlk/son yayın: 14:13:38.343 / 14:14:21.374; aralık yaklaşık 43.031 saniye.
- Yayın aralığı: medyan 1.000 s; minimum 0.966 s; maksimum 1.038 s; ortalama 1.001 s.
- UDP EVENT_ID=370, STATE=OFF alındı; BOOT_ID ve olay alanları HA text_sensor entity'lerine yayımlandı.

## Betimleyici akım gözlemi
- OFF öncesi örnekler: n=33, ortalama yaklaşık 0.47085 A.
- UDP OFF alım zamanı 14:14:11.459. Sonraki ilk CH1 yayını 14:14:12.343'te 0.196 A; sonraki değerler yaklaşık 0.142–0.220 A aralığında.
- Bu yalnızca logdaki olay öncesi/sonrası farkın betimlemesidir. UDP STATE=OFF fiziksel yük durumunun bağımsız kanıtı değildir.

## Kanıt sınırları
- Log, validated config cache'in esp32d1.yaml için yüklendiğini söylüyor; depodaki B YAML ile binary arasında birebir kaynak/hash eşleşmesi doğrulanmıyor.
- Kayıt yaklaşık 43 saniyedir; 10 dakikalık B turu değildir.
- Bu kısa kontrol A/B/C sıçrama sıklığı/genliği karşılaştırmasına dahil edilmez.
- Flash/chip revision/SRAM uyarıları optimizasyon önerileridir; sensör/UDP başlatmasını engellememiştir.

## Sonuç
Kısa cihaz kontrolü başarılı: cihaz çevrimiçi, ADC/ct_clamp başlatması başarılı, CH1 yaklaşık 1 saniyede bir yayımlanıyor ve UDP alıcısı olay alıyor. B turunun resmi 10 dakikalık kaydı tamamlanmış değildir.
