# 2026-11-01 — Modül 3 WROOM TIME'sız olay akışı log analizi

## Test kimliği
- Cihaz: ESP32 WROOM / `bero-modul3-wroom`
- ESPHome: 2026.10.1
- Derleme zamanı: 2026-11-01 18:47:11 +0300
- Cihaz IP: 192.168.0.70
- Kaynak log SHA-256: `49d22fc15d18af762637c337ac1269ccbc85be9de6b7869f2e8d74bfdcad60a9`
- Test YAML snapshot SHA-256: `14cd0f30c6bf44e452ee06747538f6d8c9915411408e2c67019c3020ce20a476`

## Gözlenen sonuçlar
- UART TX GPIO19, RX GPIO18 ve 9600 baud yapılandırması loglandı.
- PZEM sensörleri başlatıldı ve yaklaşık 5 saniyede bir değer yayınladı.
- Gözlenen gerilim yaklaşık 227.6–228.2 V; akım yaklaşık 0.035–0.036 A; frekans 49.9–50.0 Hz.
- Wi-Fi bağlı; RSSI -70 dBm.
- BOOT_ID: `53A14E04372DEB0E67FA07270AC69561` (32 hex karakter).
- Görünen olaylar EVENT_ID 2/OFF, 3/ON, 4/OFF. Aynı BOOT_ID korunmuş.
- Her görünen olay için HA_EVENT_PUBLISHED ve UDP_EVENT_SENT logu var; HA text_sensor aynı BERO_EVT metnini yayınlamış.
- Olay metinlerinde TIME alanı bulunmuyor.
- 18:49:47.657 OFF → 18:50:07.661 ON: yaklaşık 20.004 s.
- 18:50:07.661 ON → 18:50:47.653 OFF: yaklaşık 39.992 s.
- Bu aralıklar 40 s ON / 20 s OFF faz sırasıyla uyumlu.

## Açık bulgu
İki OFF olayında `GPIO_OFF_READBACK_MISMATCH` görülüyor. ON olaylarında `GPIO_ON_CONFIRMED` var. Kodda `turn_off()` çağrısından hemen sonra aynı lambda içinde GPIO23 okunuyor. Çıkış güncellemesi ile okuma arasında zamanlama yarışı olasılığı vardır; ancak bu yalnızca hipotezdir. Fiziksel GPIO seviyesi veya SSR'nin yükü gerçekten kestiği bu logla kanıtlanmaz.

## Kanıt sınırları
- Log yaklaşık 35 mA boşta akım düzeyini gösterir; yük altı davranış testi değildir.
- UDP_EVENT_SENT, gönderim çağrısının başarılı olduğunu gösterir; Modül 2'nin paketi aldığını göstermez.
- HA olay entity'sinin yerel yayınlandığı loglanmıştır; Recorder geçmişine kalıcı yazıldığı ayrıca kontrol edilmemiştir.
- Fiziksel SSR anahtarlaması bağımsız ölçümle doğrulanmamıştır.

## Sonuç
**KISMİ DOĞRULANDI.** PZEM okuma/yayın, TIME'sız olay kimliği üretimi, HA olay yayını, UDP gönderim çağrısı ve 40/20 çevrim faz sırası logla destekleniyor. OFF GPIO readback, fiziksel SSR ve Modül 2 UDP alımı açık kalıyor.
