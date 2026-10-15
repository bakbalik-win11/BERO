# GRV-004 — Alt Görev 2: Fiziksel Okuma

- **Kart:** ESP32D1
- **Test:** GPIO32, GPIO33 ve GPIO34 üzerinde fiziksel okuma
- **Sonuç:** Üç GPIO'nun tamamında 1,65 V okundu.
- **Bias yöntemi:** Trafo bias kullanılıyor; bias yapısının ayrı görevi GRV-003'tür.
- **Besleme notu:** Ne PZEM ne de SCT013 sensörleri enerjiyi ESP'den almıyor; sensör beslemesi ESP'den sağlanmıyor.
- **Durum:** Fiziksel okuma OK.

**Not:** Bu kayıt fiziksel test bilgisidir. Ölçüm cihazı ve ölçüm noktası ayrıntısı ayrıca belirtilmediğinden varsayılmamıştır.

Önceki numaralandırmada bu kayıt GRV-003 altındaydı. Görev sırası düzenlendiği için kayıt GRV-004'e taşındı.

## Sonraki seviye — ESPHome üç kanal canlı okuma

- **Sonuç:** YAML derlenmiş yapılandırma ile cihaza bağlanıldı; PZEM ve üç ADC sensörü logda göründü.
- **Kod:** [Tam YAML](KOD/esp32d1-pzem-sct-3kanal.yaml)
- **Log kaydı:** [Bağlantı ve sensör log özeti](LOG/esp32d1-logs.md)
- **Seviye raporu:** [GRV-004 ana raporu](README.md)
- **Not:** Bu aşama saniyelik ADC güncellemesidir. 1000 örnek × 3 kanal hızlı kararlılık testi henüz yapılmadı.
