# PROJE BERO — EVENT_ID FAZ A KAYDI
Tarih: 2026-10-16

## Amaç
SSR ESP'nin ON/OFF durum geçişlerinde, diğer cihazların daha sonra kullanabileceği ortak bir olay kimliği üretmesi.

## Yapılan kod değişikliği
Dosya: `DONANIM/DS3231/examples/ds3231_ssr_40on_20off.yaml`

- Her açılışta `esp_random()` ile yeni `BOOT_ID` oluşturulur.
- `EVENT_ID` açılışta 0'dan başlar.
- SSR'nin ON ve OFF geçişlerinde EVENT_ID bir artırılır.
- Seri loga şu biçimde olay yazılır:
  `BERO_SHARED_EVENT BOOT_ID=XXXXXXXX EVENT_ID=N STATE=ON|OFF`
- Bu kimlik RTC saatinden bağımsızdır; RTC/DS3231 yazma hatası çözülmüş sayılmaz.
- Mevcut SSR çevrimi ve GPIO yapılandırması değiştirilmedi.

## Doğrulama durumu
- GitHub YAML değişikliği kaydedildi.
- Derleme yapılmadı; ESP'ye yüklenmedi; donanım üzerinde test edilmedi.
- Bu nedenle Faz A henüz çalışma zamanı açısından PASS değildir.
- `BOOT_ID` rastgele 32 bit değerdir; çakışma olasılığı düşüktür ama matematiksel olarak sıfır değildir.
- UDP yayın/alıcı kodu eklendi (aşağıdaki dosyalar). Bu değişiklikler henüz derlenmedi, ESP'lere yüklenmedi ve gerçek ağda test edilmedi.

## Devam adımı
1. YAML'ı ESPHome ile derle.
2. Cihazda en az bir ON ve bir OFF geçişini gözle.
3. Logdaki BOOT_ID'nin aynı açılış boyunca sabit, EVENT_ID'nin ardışık ve STATE'in ON/OFF olduğunu doğrula.
4. PZEM ESPHome yapılandırması kullanıcı tarafından sağlandı ve `DONANIM/PZEM/examples/esp32_wr1_pzem.yaml` konumuna kaydedildi. UART GPIO17/GPIO16, 9600 baud ve `pzemac` sensörleri korunuyor. UDP olay alıcısı henüz eklenmedi.

## Kabul ölçütü
En az şu iki ardışık kaydın gerçek cihaz logunda görülmesi:
```
BERO_SHARED_EVENT BOOT_ID=XXXXXXXX EVENT_ID=1 STATE=ON
BERO_SHARED_EVENT BOOT_ID=XXXXXXXX EVENT_ID=2 STATE=OFF
```
Yukarıdaki satırlar örnektir; gerçek test çıktısı değildir.


## Mimari kararı — SCT ölçüm ESP'leri olay dinlemeyecek
Karar tarihi: 2026-10-16

- ESP-SSR yalnızca `BOOT_ID`, `EVENT_ID`, `STATE` olaylarını üretir/yayınlar.
- PZEM ESP kendi PZEM ölçümünü sürdürürken olay mesajlarını da dinler.
- 1T / 2T / 4T ESP'lerine ilk aşamada olay dinleme, UDP alma veya EVENT_ID işleme eklenmez.
- SCT ESP'leri yüksek hızlı ham veri toplama işine odaklanır; kendi kayıtlarına yerel timestamp, raw ve bias verileri yazılır.
- Mac Mini'deki Python, SSR olay kayıtlarını ve ölçüm loglarını sonradan zaman aralıklarına göre eşleştirir.
- Böylece olay ilişkilendirmesi, yüksek hızlı SCT örnekleme döngüsüne ek yük getirmez.

## Önerilen minimum prototip sırası
1. ESP-SSR: BOOT_ID/EVENT_ID/STATE üretimini logda doğrula.
2. ESP-SSR -> PZEM ESP: UDP olay mesajı aktarımını ekle; mevcut PZEM ölçümlerini koru ve alıcı logunda doğrula.
3. Mac Mini: iki bağımsız logu Python ile eşleştir.
4. Ancak bu üç adım doğrulandıktan sonra 1T, 2T ve 4T ham veri akışlarını ayrı ayrı sisteme dahil et.
5. MCP gerekliliğini sonuçlara ve ölçüm kalitesine göre daha sonra değerlendir.

## Veri eşleştirme uyarısı
SCT örneklerine EVENT_ID yazılmayacaksa, Python olayları SCT verisiyle zaman damgası ve olayın geçerli olduğu zaman aralığı üzerinden eşleştirir. Cihazların saatlerinin aynı doğrulukta olduğu varsayılmamalı; Mac Mini alım zamanı ve cihaz zaman damgalarının farkı ayrıca ölçülüp belgelenmelidir.

## Durum
UDP yayın/alıcı kodu depoya eklendi. UDP haberleşmesi gerçek cihazlarda henüz doğrulanmadı; Python log eşleştirmesi henüz uygulanmadı.


## Gerçek cihaz testi — 2026-10-16

Kullanıcının paylaştığı ESPHome OTA loguna göre, UDP eklenmiş SSR firmware'i **derlenmiş ve cihaza yüklenmiş; cihaz API üzerinden erişilebilir**.

- Derleme zamanı: 2026-10-16 14:49:09 +0300 (ESPHome 2026.9.1).
- UDP gönderim çağrıları loglanmış: `BOOT_ID=AF39B8E4`, `EVENT_ID=2 STATE=OFF`, `EVENT_ID=3 STATE=ON`, `EVENT_ID=4 STATE=OFF`.
- Bu kayıtlar gönderici tarafında UDP gönderiminin çağrıldığını gösterir; PZEM alıcısına teslimat henüz doğrulanmadı.
- NTP senkronizasyonu başarılı.
- DS3231 hâlâ hata veriyor: `Communication with DS3231 failed!` ve `I2C write failed at register 0x00`.
- ON sırasında `GPIO_ON_READBACK_MISMATCH` var; fiziksel SSR çıkışı henüz doğrulanmış değil.

Ayrıntılı kanıt ve gerçek log satırları: [2026-10-16 ESP32-C3-SSR UDP çalışma zamanı testi](./2026-10-16_ESP32-C3-SSR_UDP_RUNTIME_TEST.md).

**Güncel durum:** SSR gönderici derleme ve çalışma zamanı açısından doğrulandı; UDP alıcı teslimatı, fiziksel SSR çıkışı ve DS3231 sorunu açık işlerdir.
