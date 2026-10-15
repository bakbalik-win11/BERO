# GRV-006-03 — Native API echo v01 aday dosyaları

**Hedef:** Python tarafından tek bir tamsayıyı ESP'ye göndermek, ESP'nin aldığı sayıyı bir `text_sensor` üzerinden geri yayımlaması ve Python'ın gönderilen/okunan değerleri karşılaştırması.

**Donanım:** `esp32d1` (ESP32), mevcut v06 ADC kanalları GPIO32–35 ve PZEM UART GPIO16–17; bu pinler değiştirilmedi.

## Hazırlanan adaylar

- `GRV-006-03-esp32d1-api-echo-v01-ADAY.yaml`: GRV-005-14 v06'nın ayrı kopyasına `api.actions` içinde `grv006_echo` eklendi. `value: int` alır; `GRV006 Echo` adlı template text sensor durumunu yayınlar ve loga yazar.
- `GRV-006-03-native-api-discovery-v01.py`: ESPHome Native API'ye salt okunur bağlantı kurar, cihaz ve entity/action listesini gösterir; cihazda işlem başlatmaz.

## Teknik dayanak

ESPHome Native API'nin kullanıcı tanımlı actions ve değişkenler desteği resmî belgede açıklanmıştır: https://esphome.io/components/api/ . Python istemcisi `aioesphomeapi`: https://github.com/esphome/aioesphomeapi .

## Doğrulama durumu

- [x] Depodaki v06 YAML ve eski API bağlantı kayıtları incelendi.
- [x] Mevcut API arayüzü seçildi; PZEM UART iletişimine dokunulmadı.
- [x] Tam aday YAML ayrı `TASLAK` klasörüne konuldu; v06 korunuyor.
- [ ] ESPHome 2026.9.1 üzerinde derleme yapılmadı.
- [ ] Aday cihaza yüklenmedi.
- [ ] Python bağımlılığı yerel Mac ortamında kontrol edilmedi.
- [ ] Gerçek Python→ESP→geri okuma yapılmadı.

**Sonraki adım:** Önce aday YAML derleme uyumluluğunu doğrulamak; sonra Python tarafında servis çağrısı ve entity state aboneliğiyle geri okuma yapmak. Bu adımın PASS sonucu yoktur. Derleme onayı gelmeden kod `KOD` klasörüne taşınmaz.

## Kayıt disiplini

Önceki GRV-005 v06 çalışan YAML, ham log ve raporlar değiştirilmedi. Bu dosyalar öneri/aday seviyesindedir.
