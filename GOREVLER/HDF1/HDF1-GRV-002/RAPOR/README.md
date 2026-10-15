# GRV-002 — ESP32D1 + PZEM-004T V3.0

## Amaç

ESP32D1 kartına PZEM-004T V3.0 eklemek, ESPHome üzerinden UART/Modbus iletişimini incelemek ve yapılandırma ile logu görev geçmişinde saklamak.

## Donanım

- MCU: ESP32D1
- Ölçüm modülü: PZEM-004T V3.0
- UART hızı: 9600 baud
- PZEM adresi: logda 0x01

## Kayıtlar

- [Görev YAML dosyası](../KOD/ESP32D1-PZEM-V3.yaml)
- [Log özeti ve kanıt notları](../RAPOR/LOG-2026-10-10.md)
- [Sensör kod arşivindeki BERO deney kaydı](../../../KOD/PZEM-004T/BERO-TEST-ESP32D1-PZEM-V3/)

## Mevcut bulgular

1. ESP32D1, ESPHome API üzerinden erişilebilir ve Wi-Fi'ye bağlıdır.
2. ESPHome UART ve PZEMAC bileşenlerini başlatmıştır.
3. Paylaşılan logda Modbus yanıt zaman aşımı, kısmi yanıt ve parse failed uyarıları vardır.
4. Kullanıcının verdiği YAML ile logda yazan UART pinleri farklıdır: YAML TX=GPIO16/RX=GPIO17; log TX=GPIO17/RX=GPIO16. Bu fark doğrulanmadan yapılandırma başarılı ölçüm sürümü sayılmayacaktır.
5. Kullanıcı daha sonra bağlantıların söküldüğünü ve GND'nin ortak olmadığını bildirmiştir. Bu durum logdaki haberleşme hatalarını yorumlarken dikkate alınmalıdır.

## Durum

**Teşhis sürüyor.** Bu görev kaydı yapılandırma ve log kanıtını korur; mevcut log tek başına PZEM'den geçerli ölçüm alındığını kanıtlamaz.

## Sonraki doğrulama adımları

- Fiziksel UART pin eşleşmesini kodla karşılaştır.
- PZEM arayüzünün elektriksel izolasyonunu ve lojik seviyelerini doğrula; ESP32 GPIO'larına 5 V uygulama.
- Bağlantı düzeni güvenli olarak doğrulanmadan GND ortaklaması yapma.
- Güvenli bağlantı kurulduktan sonra yeni log al ve geçerli ölçüm değerlerini doğrula.
- Yeni test sonucu bu göreve yeni tarihli kayıt olarak eklenmeli; eski log sessizce değiştirilmemeli.
