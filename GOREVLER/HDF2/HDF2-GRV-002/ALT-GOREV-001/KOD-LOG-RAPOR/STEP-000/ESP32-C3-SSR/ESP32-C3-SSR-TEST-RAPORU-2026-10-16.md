# PROJE BERO — ESP32-C3-SSR Test Raporu

**Tarih:** 2026-10-16  
**Aşama:** STEP-000 — mevcut sistemin incelenmesi ve kanıtların arşivlenmesi  
**Cihaz / ESPHome adı:** `esphome-web-0424f4`  
**Home Assistant görünen adı:** `ESP32-C3-SSR`  
**Firmware:** ESPHome 2026.9.1  
**Derleme zamanı (log):** 2026-10-16 14:49:09 +0300  
**Test logu:** [ESP32-C3-SSR-LOG-2026-10-16.txt](./ESP32-C3-SSR-LOG-2026-10-16.txt)  
**YAML:** [esphome-web-0424f4.yaml](./esphome-web-0424f4.yaml)

## 1. Testin amacı

SSR'ın 40 saniye ON / 20 saniye OFF döngüsünü, olayların zaman damgasıyla loglanmasını ve UDP olay yayınının çalıştığını mevcut YAML ve kullanıcı tarafından sağlanan ESPHome logu üzerinden değerlendirmek. Kod değiştirilmedi; bu rapor mevcut kanıtların değerlendirmesidir.

## 2. Sonuç özeti

- **Fiziksel ON/OFF uyumu:** Kullanıcının gözlemiyle ON/OFF davranışı fiziksel olarak görüldü. Bu, bu test için işlevsel gözlem kanıtıdır.
- **Zaman damgalı SSR olay logları:** Logda `COMMAND_ON`, `COMMAND_OFF`, GPIO geri okuma sonuçları ve döngü başlangıç olayları tarih-saat ile yazılıyor.
- **UDP olay yayını:** Logda `UDP_EVENT_SENT` satırları ve `BOOT_ID` / `EVENT_ID` / `STATE` alanları görülüyor. Bu, ESP'nin gönderim çağrısının başarılı olduğunu gösterir; tek başına alıcıda paketin alındığını kanıtlamaz.
- **Beklemeye alınan hata:** DS3231 iletişim/yazma hatası ve ON sırasında GPIO geri okuma uyuşmazlığı logda mevcut. Kullanıcının kararı doğrultusunda, gözlenen ON/OFF testini engellemediği kabul edilerek şimdilik beklemeye alındı. Bu karar, hataların çözüldüğü anlamına gelmez.

## 3. Logdan doğrudan kanıtlar

### 3.1 Başlangıç ve bağlantı

- ESPHome API bağlantısı başarılı; cihaz IP adresi `192.168.0.111`.
- Çip `ESP32-C3 rev0.4`; Wi-Fi bağlı.
- Log saati: `2026-10-16 18:23:43`; SNTP senkronizasyonu `18:23:44` civarında başarılı.

### 3.2 SSR döngüsü ve UDP olayları

Log örnekleri:

- `18:23:52` — `EVENT_ID=2, STATE=OFF`; `COMMAND_OFF`; `GPIO_OFF_CONFIRMED`; switch OFF.
- `18:24:12` — `EVENT_ID=3, STATE=ON`; `COMMAND_ON`; `GPIO_ON_READBACK_MISMATCH`; switch ON.
- `18:24:52` — `EVENT_ID=4, STATE=OFF`; `GPIO_OFF_CONFIRMED`; switch OFF.
- `18:25:12` — `EVENT_ID=5, STATE=ON`; `GPIO_ON_READBACK_MISMATCH`; switch ON.
- `18:25:52` — `EVENT_ID=6, STATE=OFF`; `GPIO_OFF_CONFIRMED`; switch OFF.

Görünen örneklerde ON ve OFF olayları yaklaşık 40 saniyelik aralıklarla sırayla ilerliyor. Logun başlangıcında döngünün hangi fazında olunduğu bilinmediğinden, bu örneklerden tek başına tam ilk çevrimin süresini çıkarmıyoruz. Kullanıcı ayrıca fiziksel ON/OFF uyumunu gözle doğruladığını bildirdi.

### 3.3 Zaman kaynağı / DS3231 hatası

Logda aşağıdaki hatalar var:

- `Communication with DS3231 failed!`
- `I2C write failed at register 0x00`
- Buna rağmen `BERO_RTC_WRITE_COMMAND_SENT` mesajı yazılmış.
- SNTP senkronizasyonu başarılı ve NTP saat sensörü geçerli zaman yazdırıyor.

YAML içindeki olay zaman damgası seçimi RTC geçerliyse RTC'yi, değilse NTP'yi kullanacak şekilde yazılmış. Ancak bu logda DS3231 bileşeni FAILED ve yazma hatası verdiğinden, RTC sensörünün geçerli zaman döndürmesi tek başına fiziksel RTC'nin sağlıklı çalıştığını kanıtlamaz. Bu nedenle RTC hatası kapatılmadı; ayrıca incelenmek üzere beklemede tutuldu.

### 3.4 GPIO geri okuma uyuşmazlığı

ON olaylarında `GPIO_ON_READBACK_MISMATCH` görülürken OFF olaylarında `GPIO_OFF_CONFIRMED` görülüyor. YAML'da GPIO6 için `inverted: true` ayarı var. Bu uyuşmazlık, yazılımdaki ham GPIO seviyesi beklentisinin tersleme ayarıyla uyumsuz olmasından kaynaklanabilir; mevcut log tek başına kesin neden belirtmez. Kullanıcının fiziksel ON/OFF gözlemi nedeniyle bu uyarı şimdilik beklemeye alınmıştır. Sonraki uygun aşamada, SSR kontrolünü değiştirmeden GPIO mantığı ve ölçüm noktası doğrulanabilir.

## 4. YAML incelemesi

- SSR çıkışı: GPIO6, `inverted: true`, `restore_mode: ALWAYS_OFF`.
- Döngü zamanlaması: `millis()` ile geçen süre hesaplanıyor; 40 saniyeye kadar ON, 40–60 saniye aralığında OFF, ardından yeni döngü başlıyor.
- Her olayda artan `EVENT_ID` ve yeniden başlatma başına üretilen `BOOT_ID` UDP paketine ekleniyor.
- UDP hedefi broadcast adresi `255.255.255.255:4210`.
- Olaylar RTC/NTP kaynak bilgisiyle loglanıyor; zaman yoksa `TIME=UNAVAILABLE` yazılıyor.
- ESPHome switch durumunun logda ON/OFF görünmesi yazılım durumunu doğrular; tek başına SSR yük tarafındaki elektriksel durumu kanıtlamaz. Fiziksel gözlem ayrıca kullanıcı tarafından bildirildi.

## 5. Karar ve durum

**Karar:** Kullanıcının bildirdiği fiziksel ON/OFF uyumu bu aşama için gözlendi. Logdaki DS3231 ve GPIO geri okuma hataları testin devamını durdurmadığından şimdilik beklemeye alındı; hatalar gizlenmedi ve rapora işlendi.

**Bu raporla doğrulananlar:** ESPHome API bağlantısı, SNTP senkronizasyonu, zaman damgalı SSR olay logları, tekrarlayan ON/OFF switch durumları ve ESP tarafından UDP gönderim logları.

**Henüz doğrulanmayanlar:** UDP alıcısının paketi gerçekten alması; Home Assistant geçmişinde olayların kalıcı ve ayrı kayıt olarak saklanması; DS3231'in sağlıklı iletişimi; ON sırasında GPIO geri okuma uyuşmazlığının kesin nedeni.

**Kod durumu:** Kullanıcının sağladığı YAML aynen arşivlendi; bu rapor hazırlanırken kodda değişiklik yapılmadı. Bu kayıt bir derleme veya fiziksel test PASS beyanı değildir.

## 6. Dosyalar

- [YAML — esphome-web-0424f4.yaml](./esphome-web-0424f4.yaml)
- [Log — ESP32-C3-SSR-LOG-2026-10-16.txt](./ESP32-C3-SSR-LOG-2026-10-16.txt)

