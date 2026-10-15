# GRV-004 — BIAS + 1T/2T/3T ADC adlandırma seviyesi

- **Tarih:** 2026-10-10
- **Cihaz:** `esp32d1` / ESP32D1
- **Durum:** Kullanıcı tarafından başarılı olarak bildirildi; yüklenen ESPHome loguyla bağlantı ve sensör başlangıcı doğrulandı.
- **BIAS fiziksel referansı:** GPIO32 üzerinde multimetreyle 1,65 V.
- **Bağlantı kontrolü:** Kullanıcı tarafından OK olarak doğrulandı.
- **BIAS sensör adı:** `BIAS Ham Voltaj` — GPIO32.
- **1T sensör adı:** `1T Ham Voltaj` — GPIO33.
- **2T sensör adı:** `2T Ham Voltaj` — GPIO34.
- **3T sensör adı:** `3T Ham Voltaj` — GPIO35.
- **PZEM:** UART/Modbus ayarları korundu (TX GPIO16, RX GPIO17, 9600 baud).
- **ADC ayarları:** 12 dB attenuation, 1 saniye güncelleme, 3 ondalık basamak.

## Kaydedilen dosyalar

- **Kod:** [Tam YAML](KOD/esp32d1-bias-1t-2t-3t.yaml)
- **Log ve analiz:** [ESPHome log özeti](LOG/esp32d1-bias-1t-2t-3t-log.md)
- **Ana rapor:** [GRV-004 ana raporu](README.md)

## Logda doğrulananlar

- ESPHome 2026.9.1; derleme zamanı 2026-10-10 16:13:06 +0300.
- Cihaz 192.168.0.8 adresinde bulunmuş; API bağlantısı ve handshake başarılı.
- Dört ADC kanalının da başlatma, yapılandırma ve kalibrasyon durumu OK.
- PZEM ve ADC sensörleri canlı değer yayımlamış.
- GPIO32 / BIAS: 56 örnekte 1.519–1.669 V.
- GPIO33 / 1T: 56 örnekte 1.646–1.668 V.
- GPIO34 / 2T: 56 örnekte 1.644–1.668 V.
- GPIO35 / 3T: 56 örnekte 1.647–1.662 V.

## Önemli gözlem

BIAS çoğunlukla 1.654–1.669 V civarındayken son iki görünen BIAS örneği 1.617 V ve 1.519 V. Diğer üç kanal aynı bölümde yaklaşık 1.651–1.664 V aralığında. Bu sapmanın nedeni henüz belirlenmedi; fiziksel 1,65 V referansıyla yeniden kontrol edilmesi gereken bir bulgudur.

## Başarı / kapsam

**Başarıldı:** yapılandırma cihazda çalışıyor; PZEM ve BIAS/1T/2T/3T sensörleri logda veri yayımlıyor. Log ve bu seviyede ne başarıldığı bu MD raporuna eklendi.

**Henüz yapılmadı:** 1000 örnek × 3 kanal hızlı kararlılık testi. Bu log saniyelik güncellemelerdir.

Önceki `esp32d1-pzem-sct-3kanal.yaml` ve önceki raporlar değiştirilmeden bırakılmıştır.
