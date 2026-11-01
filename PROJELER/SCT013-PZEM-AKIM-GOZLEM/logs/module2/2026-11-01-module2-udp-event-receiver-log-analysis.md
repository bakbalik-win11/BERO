# 2026-11-01 — Modül 2 UDP olay alıcısı / ESP32D1 log analizi

## HEDEF
Modül 2'nin Modül 3'ten UDP 4210 üzerinden gelen BERO_EVT mesajını alıp BOOT_ID, EVENT_ID ve STATE alanlarını Home Assistant'a yayınlayıp yayınlamadığını incelemek. Aynı logda SCT sıralı okuma ve cihaz çalışma uyarılarını da kontrol etmek.

## KAYNAK
- Kullanıcı dosyası: `Yapıştırılan metin(20261101-161914).txt`
- Boyut: 63.333 bayt; 823 satır.
- SHA-256: `b4139aa2e6e6a3efb8bd70d358f7604359d297ad059662652e07c0da58a53d67`
- ESPHome 2026.10.1; derleme zamanı 2026-11-01 19:15:41 +0300.
- Modül 2: `esp32d1`, 192.168.0.33.
- HA API istemcisi: 192.168.0.26.
- Modül 3 kaynak IP: 192.168.0.70.

## UDP / HA SONUCU — LOG İLE DESTEKLENDİ
19:18:07.736'da Modül 2, 192.168.0.70 adresinden aşağıdaki paketi aldı:

```text
BERO_EVT,BOOT_ID=53A14E04372DEB0E67FA07270AC69561,EVENT_ID=59,STATE=ON
```

Ardından:
- `UDP_EVENT_RECEIVED` logu oluştu.
- `HA_EVENT_PUBLISHED` logu oluştu.
- `BERO Mod2 Olay Kaydi` ham mesajı aynen yayınladı.
- BOOT_ID, EVENT_ID ve STATE ayrı text_sensor entity'lerine doğru ayrıştırıldı.
- HA API bağlantısı logda başarılı.

**Sonuç:** Modül 3 → Modül 2 UDP alımı ve Modül 2'nin HA'ya olay alanlarını yayınlaması en az bir gerçek ON paketi için doğrulandı.

**Sınır:** Bu log kesitinde yalnız bir alım olayı görülüyor: EVENT_ID=59 / STATE=ON. OFF paketinin Modül 2 tarafından alındığı bu dosyada gösterilmiyor. Tek paket, tüm çevrimlerin kayıpsız iletildiğini veya HA Recorder veritabanına kalıcı yazıldığını tek başına kanıtlamaz. Recorder doğrulaması HA geçmişinden ayrıca yapılmalıdır.

## SCT OKUMA / CİHAZ ÇALIŞMASI — LOG İLE DESTEKLENDİ
- Üç ADC kaynağı GPIO32/33/34 ve ortak bias GPIO35 başlatılmış; ADC init/config/calibration durumları OK.
- Üç ct_clamp kanalı 200 ms sample_duration ile başlatılmış.
- 43 SCT1, 43 SCT2 ve 43 SCT3 yayın örneği; 43 ortak bias örneği incelendi.
- SCT sıralı çevrim START/COMPLETE işaretleri yaklaşık 2 saniyelik çevrimle uyumlu.
- Bias gözlemi: min 1.648 V, max 1.674 V, ortalama 1.6613 V (n=43).
- Akım sensörlerinde sıfır yayınlar çoğunlukta: SCT1 40/43, SCT2 35/43, SCT3 30/43 sıfır. Sıfır dışı filtrelenmiş akım değerleri sırasıyla 0.043–0.093 A (3 örnek), 0.017–0.081 A (8 örnek), 0.019–0.134 A (13 örnek).

**Yorum sınırı:** Logun alındığı andaki yük koşulu bu kayıtla tanımlanmamıştır. Bu nedenle sıfır/seyrek akım değerleri donanım arızası veya ölçüm başarısı olarak sınıflandırılamaz; yük durumu bilinmeden kanal doğruluğu, UNIT/PZEM sapması veya kalibrasyon sonucu çıkarılmaz.

## UYARILAR / HATA DENETİMİ
- Derleme/başlangıçta üç ESP32 optimizasyon önerisi vardır: `flash_chip: generic`, `minimum_chip_revision: "3.1"`, `sram1_as_iram: true`. Bunlar hata değil, isteğe bağlı bellek/IRAM optimizasyon uyarılarıdır.
- 19:18:23.980'da bir kez `safe_mode took a long time for an operation (70 ms), max is 50 ms` uyarısı görülür. Tekil gözlem; tekrarlanırsa çevrim zamanlaması ve loop yükü incelenmelidir.
- Logda ESPHome [E] / ERROR, UDP_RECV_FAILED, UDP_INVALID_PACKET veya UDP_BIND_FAILED kaydı görülmedi.
- Başlangıç satırı validated config cache kullanıldığını ve o açılışta config validation'ın atlandığını söylüyor; binary'nin derlenmiş/çalışmış olduğunu gösterir, ancak bu log tek başına güncel YAML için bağımsız `config check` çıktısı değildir.

## DEPO KODU / KANIT SINIRI
- `firmware/bero-modul2-esp32d1.yaml` yeni, açıklamalı Modül 2 kaynak snapshot'ı olarak kaydedildi.
- Kaynak, depodaki LOAD-15W-003 Modül 2 YAML'ı üzerine UDP 4210 alıcısı ve HA olay entity'leri eklenerek oluşturuldu; mevcut cihaz kimliği `esp32d1`, GPIO eşlemesi, K=24.22, 200 ms örnekleme ve 2 s sıralı çevrim korundu.
- Paylaşılan log, çalışan firmware'de UDP alımı ve HA yayınına kanıt sağlar. Ancak logun üretildiği derleme ile yeni kaydedilen YAML dosyasının byte-byte aynı kaynak olduğu bu dosya üzerinden doğrulanmamıştır.
- Yeni kaynak snapshot'ı için ayrıca ESPHome config check/derleme ve OTA testi yapılmadan bu yeni dosya bağımsız olarak "doğrulandı" sayılmayacaktır.

## SONUÇ / DURUM
- UDP ON olayının alınması ve HA entity yayınları: **DOĞRULANDI — tek paket kanıtı**.
- OFF olayı, birden fazla ardışık olay, kayıpsızlık ve Recorder kalıcılığı: **AÇIK / DOĞRULANMADI**.
- SCT ölçüm altyapısının açılması ve sıralı yayınlar: **LOG İLE DESTEKLENDİ**; yük koşulu belirsiz olduğundan akım doğruluğu yorumu yok.
- Tekil 70 ms safe_mode uyarısı takip edilmeli; şu an kritik hata kanıtı değildir.

## Seçilmiş kanıt
[Modül 2 UDP ve SCT log kanıtı](2026-11-01-module2-udp-event-receiver-evidence.log)
