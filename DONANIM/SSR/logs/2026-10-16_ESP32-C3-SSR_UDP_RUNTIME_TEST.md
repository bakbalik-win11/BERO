# PROJE BERO — ESP32-C3-SSR UDP Çalışma Zamanı Logu

- Tarih: 2026-10-16
- ESPHome: 2026.9.1
- Cihaz: ESP32-C3 rev0.4
- IP: 192.168.0.111
- Wi-Fi: AKFISH
- Kaynak: Kullanıcının paylaştığı ESPHome OTA logu
- Kod: `DONANIM/DS3231/examples/ds3231_ssr_40on_20off.yaml`

## Sonuç özeti

- **Derleme:** PASS. Log, firmware'in 2026-10-16 14:49:09 +0300 tarihinde derlendiğini gösteriyor.
- **OTA/API bağlantısı:** PASS. ESPHome 192.168.0.111 adresindeki cihaza bağlandı.
- **Wi-Fi:** Bağlı; sinyal -69 dB, kanal 2, alt ağ 255.255.255.0, ağ geçidi 192.168.0.1.
- **UDP gönderici:** Çalışma zamanı logunda `UDP_EVENT_SENT` satırları var. Bu, ESP'nin datagramı gönderim çağrısının başarılı olduğunu gösterir; tek başına PZEM alıcısına ulaştığını kanıtlamaz.
- **SSR çevrimi:** ON/OFF durum geçişleri ve olay kimlikleri loglanıyor.
- **DS3231:** Hâlâ başarısız. `Communication with DS3231 failed!` ve `I2C write failed at register 0x00` kayıtları mevcut. NTP senkronizasyonu başarılı; RTC yazma komutunun çağrılmış olması RTC yazmasının başarılı olduğu anlamına gelmez.
- **GPIO geri okuma:** ON sırasında `GPIO_ON_READBACK_MISMATCH` kaydı var. Fiziksel SSR/yük çıkışı bu logla doğrulanmış sayılmaz.

## Gerçek logdan önemli satırlar

```text
INFO ESPHome 2026.9.1
INFO Successfully connected to esphome-web-0424f4 @ 192.168.0.111
[14:50:57.563][I][app:151]: ESPHome version 2026.9.1 compiled on 2026-10-16 14:49:09 +0300
[14:50:57.670][C][i2c:119]: Found device at address 0x57
[14:50:57.671][C][i2c:119]: Found device at address 0x68
[14:50:57.777][E][ds3231:055]: Communication with DS3231 failed!
[14:51:25.014][D][sntp:099]: Synchronized time: 2026-10-16 14:51:24
[14:51:25.027][I][main:434]: BERO_NTP_SYNC_OK: NTP time synchronized.
[14:51:25.027][E][ds3231:027]: I2C write failed at register 0x00
[14:51:25.028][I][main:367]: BERO_RTC_WRITE_COMMAND_SENT: DS3231 write action called.
[14:51:31.949][I][bero_udp:190]: UDP_EVENT_SENT BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=2,STATE=OFF
[14:51:31.984][I][bero_event:196]: BERO_SHARED_EVENT BOOT_ID=AF39B8E4 EVENT_ID=2 STATE=OFF
[14:51:31.985][I][bero_event:142]: TIME=2026-10-16 14:51:31 SOURCE=RTC EVENT=COMMAND_OFF
[14:51:31.985][I][bero_event:142]: TIME=2026-10-16 14:51:31 SOURCE=RTC EVENT=GPIO_OFF_CONFIRMED
[14:51:51.882][I][bero_udp:190]: UDP_EVENT_SENT BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=3,STATE=ON
[14:51:51.885][I][bero_event:196]: BERO_SHARED_EVENT BOOT_ID=AF39B8E4 EVENT_ID=3 STATE=ON
[14:51:51.907][I][bero_event:142]: TIME=2026-10-16 14:51:51 SOURCE=RTC EVENT=GPIO_ON_READBACK_MISMATCH
[14:52:31.887][I][bero_udp:190]: UDP_EVENT_SENT BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=4,STATE=OFF
[14:52:31.928][I][bero_event:196]: BERO_SHARED_EVENT BOOT_ID=AF39B8E4 EVENT_ID=4 STATE=OFF
```

## Teknik yorum

1. `BOOT_ID=AF39B8E4` bu açılışta sabit kalmış.
2. Görünen olaylar EVENT_ID 2, 3, 4 sırasıyla OFF, ON, OFF. EVENT_ID 1'in ilgili kesitte görünmemesi, olayın hiç oluşmadığını kanıtlamaz; bu paylaşılan log parçasında yok.
3. UDP gönderim satırları oluşuyor. UDP alıcısının mesajı aldığı henüz gösterilmedi; PZEM logunda `UDP_EVENT_RECEIVED` görülmesi gerekiyor.
4. DS3231 iletişim/yazma hatası, UDP başarısından ayrı bir açık sorundur.
5. GPIO pad geri okuması fiziksel SSR çıkışını kanıtlamaz; ON davranışı ayrıca ölçülmelidir.

## Sonraki adımlar

1. PZEM ESP'ye alıcı firmware'ini derle ve yükle.
2. PZEM logunda `UDP_LISTENING port=4210` ve `UDP_EVENT_RECEIVED` satırlarını ara.
3. Alıcıya ulaşım yoksa Wi-Fi istemci izolasyonu/broadcast davranışı ve gerekirse ağın yönlendirilmiş broadcast veya unicast seçeneğini incele.
4. DS3231 hatasını ayrı bir donanım/I2C incelemesi olarak takip et.
