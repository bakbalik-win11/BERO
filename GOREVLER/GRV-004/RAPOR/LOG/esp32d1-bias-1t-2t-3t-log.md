# GRV-004 — BIAS + 1T/2T/3T ESPHome Log Kaydı

- **Tarih:** 2026-10-10
- **Kaynak:** Kullanıcının bu aşamada yüklediği 457 satırlık `esp32d1-logs (3).txt` logu.
- **ESPHome:** 2026.9.1
- **Derleme zamanı:** 2026-10-10 16:13:06 +0300
- **Cihaz:** `esp32d1`, ESP32 rev3.1, 2 çekirdek
- **IP:** 192.168.0.8
- **Bağlantı:** API resolve, connect ve handshake başarılı.
- **Wi-Fi:** Connected YES; sinyal -58 dB.
- **PZEM UART:** TX GPIO16, RX GPIO17, 9600 baud, 8N1; Modbus adresi 0x01.
- **ADC:** GPIO32/BIAS, GPIO33/1T, GPIO34/2T, GPIO35/3T; 12 dB; Samples 1; 1 s update interval.
- **ADC başlatma:** Dört ADC sensöründe de Handle Init, Config, Calibration ve Overall Init OK.

## Örnek sonuçları — yüklenen logun tamamından hesaplandı

| Sensör | Örnek sayısı | Minimum | Maksimum |
|---|---:|---:|---:|
| BIAS Ham Voltaj (GPIO32) | 56 | 1.519 V | 1.669 V |
| 1T Ham Voltaj (GPIO33) | 56 | 1.646 V | 1.668 V |
| 2T Ham Voltaj (GPIO34) | 56 | 1.644 V | 1.668 V |
| 3T Ham Voltaj (GPIO35) | 56 | 1.647 V | 1.662 V |

| PZEM sensörü | Örnek sayısı | Minimum | Maksimum |
|---|---:|---:|---:|
| Gerilim | 11 | 233.0 V | 233.8 V |
| Akım | 11 | 0.028 A | 0.029 A |
| Güç | 11 | 1.60 W | 2.00 W |
| Enerji | 11 | 10387 Wh | 10387 Wh |
| Frekans | 11 | 49.9 Hz | 50.0 Hz |
| Güç faktörü | 11 | 0.24 | 0.29 |

## Dikkat çeken bulgu

BIAS örneklerinin çoğu yaklaşık 1.654–1.669 V civarındayken son bölümde GPIO32 okuması **1.617 V** ve ardından **1.519 V** olarak görünüyor. Aynı son bölümde diğer üç ADC kanalı yaklaşık 1.651–1.664 V aralığında kalıyor.

Bu iki BIAS düşüşü logda gerçekten mevcut; atılmadı veya normal aralıkla gizlenmedi. Bunun sebebi bu logla tek başına belirlenemez. Fiziksel 1.65 V referansı ile tekrar kontrol edilmesi gereken bir gözlemdir.

## Sonuç

- **Başarılı:** Cihazla API bağlantısı kuruldu; PZEM ve dört ADC sensörü başlatıldı ve canlı örnekler yayımlandı.
- **Başarılı:** BIAS ve 1T/2T/3T adları logda görülüyor.
- **İzlenecek konu:** BIAS kanalında görülen 1.617 V ve 1.519 V düşüşleri.
- **Henüz yapılmadı:** 1000 örnek × 3 kanal hızlı kararlılık testi. Bu kayıt saniyelik ESPHome güncellemeleridir; hızlı test değildir.
- **Uyarılar:** ESP32 revizyonu için minimum_chip_revision ve SRAM1/IRAM ayar önerileri var; logda başlatmayı engelleyen hata görülmüyor.

## Kaynak log

Ham kullanıcı logu 457 satırdır ve bu özetin dayanağıdır. Buradaki ölçüm aralıkları sensör satırlarının tamamı taranarak çıkarılmıştır.
