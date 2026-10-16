# PROJE BERO — HEDEF 2 / GRV-001 / ALT GRV-2
# SSR → PZEM UDP Haberleşme ve Ölçümle Zaman Eşleştirme Raporu

- **Tarih:** 2026-10-16
- **Görev:** Hedef 2 → HDF2-GRV-001 — Hedef 2 test donanımının kurulması
- **Alt görev:** Alt GRV-2 — SSR olaylarının PZEM ESP'ye iletilmesi ve ölçüm değişimiyle karşılaştırılması
- **Kayıt türü:** Gerçek cihaz derleme/OTA çalışma loglarına dayalı test raporu
- **ESPHome:** 2026.9.1
- **Durum:** UDP olay teslimi doğrulandı; SCT/ADC osiloskop testi bu çalışmanın parçası değildir ve tamamlanmış sayılmaz.

## 1. Amaç

SSR kontrol ESP'sinin ON/OFF olaylarını LAN üzerinden UDP ile ayrı PZEM ESP'sine göndermesi; PZEM tarafının bu olayları gerçekten alıp almadığının ve PZEM ölçüm değerleriyle zamansal uyumun incelenmesi.

## 2. Kullanılan cihazlar ve dosyalar

### Gönderici — ESP32-C3-SSR
- IP: `192.168.0.111`
- ESPHome cihaz adı: `esphome-web-0424f4`
- SSR kontrol GPIO: GPIO6, YAML'da `inverted: true`
- UDP hedefi: `255.255.255.255:4210`
- Olay biçimi: `BERO_EVT,BOOT_ID=<id>,EVENT_ID=<sayı>,STATE=<ON|OFF>`
- Kod: [ds3231_ssr_40on_20off.yaml](https://github.com/bakbalik-win11/BERO/blob/main/DONANIM/DS3231/examples/ds3231_ssr_40on_20off.yaml)
- Gerçek çalışma logu: [SSR UDP runtime logu](https://github.com/bakbalik-win11/BERO/blob/main/DONANIM/SSR/logs/2026-10-16_ESP32-C3-SSR_UDP_RUNTIME_TEST.md)

### Alıcı ve referans ölçüm — ESP32-WR1-PZEM
- IP: `192.168.0.52`
- ESPHome cihaz adı: `esphome-web-2a35cc`
- PZEM UART: TX GPIO17, RX GPIO16, 9600 baud
- PZEM güncelleme aralığı: yaklaşık 5 saniye
- UDP dinleme portu: 4210
- Kod: [esp32_wr1_pzem.yaml](https://github.com/bakbalik-win11/BERO/blob/main/DONANIM/PZEM/examples/esp32_wr1_pzem.yaml)
- Gerçek çalışma logu: [PZEM UDP runtime logu](https://github.com/bakbalik-win11/BERO/blob/main/DONANIM/PZEM/logs/2026-10-16_ESP32-WR1-PZEM_UDP_RUNTIME_TEST.md)

## 3. Yapılan işlem sırası

1. ESP32-C3-SSR YAML'ı ESPHome 2026.9.1 ile derlendi ve OTA üzerinden `192.168.0.111` cihazına yüklendi.
2. SSR tarafında `UDP_EVENT_SENT` kayıtları ve artan `EVENT_ID` değerleri gözlendi.
3. ESP32-WR1-PZEM YAML'ı ESPHome 2026.9.1 ile derlendi ve OTA üzerinden `192.168.0.52` cihazına yüklendi.
4. PZEM tarafında `UDP_LISTENING port=4210` ve gönderici adresi `192.168.0.111` olan `UDP_EVENT_RECEIVED` kayıtları gözlendi.
5. Aynı log kesitlerinde ON/OFF olaylarıyla PZEM akım/güç ölçümleri karşılaştırıldı.

## 4. Gerçek UDP alım kanıtı

PZEM ESP logunda aşağıdaki olaylar alındı:

| Saat (2026-10-16) | EVENT_ID | Durum |
|---|---:|---|
| 15:01:31.995 | 22 | OFF |
| 15:01:51.889 | 23 | ON |
| 15:02:31.999 | 24 | OFF |
| 15:02:51.995 | 25 | ON |
| 15:03:31.988 | 26 | OFF |
| 15:03:51.987 | 27 | ON |
| 15:04:31.887 | 28 | OFF |
| 15:04:51.987 | 29 | ON |
| 15:05:31.885 | 30 | OFF |
| 15:05:51.989 | 31 | ON |
| 15:06:31.886 | 32 | OFF |
| 15:06:51.988 | 33 | ON |

Tüm bu olaylarda `BOOT_ID=AF39B8E4` aynı kaldı ve `EVENT_ID` ilerledi. Bu, olay paketlerinin yalnızca gönderici logunda oluşturulmadığını; PZEM alıcısının da bunları aldığına ilişkin doğrudan çalışma zamanı kanıtıdır.

## 5. PZEM ölçümlerindeki gözlem

Gerçek çalışma logunda yaklaşık olarak:

| Ölçüm | ON aralıklarında gözlenen | OFF aralıklarında gözlenen |
|---|---:|---:|
| Akım | 0.052–0.053 A | 0.000 A |
| Güç | 7.7–7.9 W | 0.00 W |
| Gerilim | yaklaşık 225.9–228.3 V aralığında | yaklaşık aynı aralık |
| Frekans | yaklaşık 49.9–50.0 Hz | yaklaşık aynı aralık |

Akım ve güç değerleri, alınan ON/OFF olaylarıyla zamansal olarak örtüşüyor. PZEM yaklaşık 5 saniyede bir güncellendiği için bu gözlem, hızlı geçiş zamanlamasının hassas ölçümü veya tam örnek eşzamanlaması değildir.

## 6. Test sonucu

| Kontrol | Sonuç | Kanıt sınırı |
|---|---|---|
| SSR firmware derleme ve OTA bağlantısı | PASS | Cihaz logu |
| SSR tarafında UDP gönderim olayı | PASS | `UDP_EVENT_SENT` kayıtları |
| PZEM tarafında UDP portunun dinlenmesi | PASS | `UDP_LISTENING port=4210` |
| SSR'den gelen UDP paketinin PZEM'de alınması | PASS | `UDP_EVENT_RECEIVED`, kaynak IP ve payload mevcut |
| BOOT_ID sabitliği / EVENT_ID ilerlemesi | PASS | Alınan olay dizisi |
| ON/OFF ile PZEM akım/güç değişiminin zamansal örtüşmesi | Gözlendi | PZEM güncellemesi yaklaşık 5 saniyede bir |
| SCT/BIAS ham ADC verisi | TEST EDİLMEDİ | Bu haberleşme testinin kapsamı dışında |
| Osiloskopla dalga biçimi doğrulaması | TEST EDİLMEDİ | Bu çalışmada yeni fiziksel osiloskop kaydı yok |
| DS3231 saat yazma | FAIL / açık sorun | `I2C write failed at register 0x00` |
| GPIO6 geri okuma ile SSR fiziksel çıkışının kanıtlanması | DOĞRULANMADI | GPIO geri okuması fiziksel yük çıkışını kanıtlamaz |

**Sonuç:** SSR → PZEM UDP olay teslimi gerçek cihaz loglarıyla doğrulanmıştır. ON/OFF olaylarıyla PZEM akım/güç ölçümleri arasında beklenen zamansal ilişki gözlenmiştir. Bu sonuç, SCT/ADC ölçüm zincirinin veya osiloskop testinin başarılı olduğunu göstermez.

## 7. Açık işler ve devam noktası

1. **Bu haberleşme adımının devamı:** Olay paketlerini ve PZEM ölçümlerini Mac Mini üzerinde zaman damgalı dosyaya/CSV'ye kaydetmek ve Python ile eşleştirmek. Bu kayıt henüz yapılmış sayılmaz.
2. DS3231 başlatma ve register `0x00` yazma hatasını ayrı iş olarak incelemek.
3. GPIO6 geri okuma uyuşmazlığını yazılımın mantıksal durumu ile fiziksel pin seviyesi bakımından ayırmak. Fiziksel SSR/yük gözlemi bu loglardan ayrı değerlendirilmelidir.
4. Hedef 2'nin ana ölçüm hattında GRV-007/GRV-008 kapsamındaki ESP32-WROOM dahili ADC, SCT/BIAS ham veri yakalama ve osiloskop kayıtları ayrı testlerdir. Bu rapor bunları PASS olarak işaretlemez.
5. SCT ölçüm ESP'lerine bu aşamada UDP olay dinleme eklenmeyecek; olay/ölçüm eşleştirme ilk olarak Mac Mini Python tarafında yapılacaktır.

## 8. Kaynak kayıtlar

- [HDF2-GRV-001 donanım kurulum kaydı](https://github.com/bakbalik-win11/BERO/blob/main/GOREVLER/HDF2/HDF2-GRV-001/README.md)
- [SSR UDP çalışma testi](https://github.com/bakbalik-win11/BERO/blob/main/DONANIM/SSR/logs/2026-10-16_ESP32-C3-SSR_UDP_RUNTIME_TEST.md)
- [PZEM UDP çalışma testi](https://github.com/bakbalik-win11/BERO/blob/main/DONANIM/PZEM/logs/2026-10-16_ESP32-WR1-PZEM_UDP_RUNTIME_TEST.md)
- [EVENT_ID Faz A raporu](https://github.com/bakbalik-win11/BERO/blob/main/DONANIM/SSR/logs/2026-10-16_EVENT_ID_FAZ_A.md)
- [HDF2 2026-10-16 günlük ilerleme raporu](https://github.com/bakbalik-win11/BERO/blob/main/GOREVLER/HDF2/HDF2-GRV-003/RAPOR/2026-10-16_HDF2_GUNLUK_ILerleme_RAPORU.md)

---
**Kayıt ilkesi:** Bu rapor yeni bir tarihli kayıttır. Önceki YAML, log ve raporların üzerine yazmaz; onları kaynak olarak gösterir.
