# STEP-000 — İki ESP'yi Home Assistant'a ayrı bağlama

**Tarih:** 2026-10-16  
**Hedef:** ESP32-WR1-PZEM ve ESP32-C3-SSR cihazlarının Home Assistant'ta birbirinden bağımsız görünmesi  
**Durum:** YAML tarafı hazır görünüyor; Home Assistant arayüzünde iki cihazın da mevcut olduğu ve entity'lerin güncellendiği henüz doğrulanmadı.

## 1. Mevcut kanıtlar

### ESP32-WR1-PZEM
- YAML: [esphome-web-2a35cc.yaml](./ESP32-WR1-PZEM/esphome-web-2a35cc.yaml)
- Cihaz adı: `ESP32-WR1-PZEM`
- IP: `192.168.0.52`
- YAML içinde `api:` ve `wifi:` yapılandırmaları mevcut.
- PZEM sensörleri: gerilim, akım, güç, enerji, frekans ve güç faktörü.
- 2026-10-16 logunda ESPHome API bağlantısı ve PZEM okumaları görülüyor.

### ESP32-C3-SSR
- YAML: [esphome-web-0424f4.yaml](./ESP32-C3-SSR/esphome-web-0424f4.yaml)
- Cihaz adı: `ESP32-C3-SSR`
- IP: `192.168.0.111`
- YAML içinde `api:` ve `wifi:` yapılandırmaları mevcut.
- HA'ya sunulabilecek entity'ler: `BERO SSR Kontrol`, `BERO NTP Saat`, `BERO DS3231 RTC Saat` ve `BERO DS3231 Saati NTP'den Yaz` butonu.
- 2026-10-16 logunda ESPHome API bağlantısı ve Wi-Fi bağlantısı görülüyor.
- SSR olayları ayrıca UDP yayınıyla gönderiliyor; bu UDP mesajlarının kendisi şu an ayrı bir Home Assistant entity'si değildir. PZEM ESP'sinin UDP alıcısında loglanması, HA geçmişinde olayların kalıcı kaydı olduğunu kanıtlamaz.

## 2. Yapılacak işlem — iki cihazı ayrı ayrı doğrula

Home Assistant arayüzünde:

1. **Ayarlar → Cihazlar ve hizmetler → ESPHome** bölümünü aç.
2. `ESP32-WR1-PZEM` cihazı zaten listeleniyorsa açıp bağlantı ve entity durumlarını kontrol et. Listede yoksa ESPHome entegrasyonundan cihaz eklemeyi başlatıp `192.168.0.52` adresini gir.
3. Aynı işlemi `ESP32-C3-SSR` için yap. Listede yoksa `192.168.0.111` adresini kullan.
4. İki cihazın ayrı cihaz kayıtları olarak göründüğünü doğrula.
5. PZEM entity'lerinin güncellendiğini; SSR switch ve saat entity'lerinin görünür olduğunu kontrol et.
6. Gözlenen durumu ve test saatini bu rapora/loga ekle.

> Cihaz zaten entegreyse ikinci kez ekleme. Önce mevcut entegrasyon kaydını kontrol et.

## 3. Başarı ölçütleri

- [ ] PZEM cihazı Home Assistant'ta ayrı cihaz olarak görünüyor.
- [ ] PZEM gerilim, akım, güç, enerji, frekans ve güç faktörü entity'leri görünüyor ve güncelleniyor.
- [ ] SSR cihazı Home Assistant'ta ayrı cihaz olarak görünüyor.
- [ ] SSR kontrol anahtarı ve saat entity'leri görünüyor.
- [ ] Her iki cihaz için bağlantı durumu ve test zamanı kaydedildi.

## 4. Sınırlar ve sonraki adım

Bu rapor YAML'ların Home Assistant API entegrasyonuna yönelik yapılandırmasını ve mevcut ESPHome loglarını belgelemektedir. Home Assistant arayüzüne bu oturumdan doğrudan erişim olmadığı için entegrasyonların gerçekten eklenmiş olduğu veya entity'lerin HA'da güncellendiği iddia edilmemektedir.

İki cihazın ayrı ayrı HA bağlantısı doğrulandıktan sonra, SSR ON/OFF olaylarını HA'da zaman damgalı ve kalıcı geçmişe kaydetme işi ayrı adım olarak ele alınacaktır. Mevcut UDP log satırları, HA olay geçmişinin yerine geçmez.

**Kod değişikliği:** Yapılmadı. Mevcut YAML'larda `api:` zaten var; doğrulanmamış bir bağlantı sorununu çözüyormuş gibi gereksiz firmware değişikliği yapılmadı.
