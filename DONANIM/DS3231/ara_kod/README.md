# Proje BERO — Ara Kod Kaydı

## Güncel birleşik test
- [Birleşik DS3231 + NTP + SSR YAML](../examples/ds3231_ssr_40on_20off.yaml)
- [2026-10-16 derleme ve çalışma logu](../logs/2026-10-16_ESP32-C3-SSR_Build_Runtime_Log.md)

## Hedef
ESP32-C3 SuperMini üzerinde DS3231 RTC ile NTP zamanını karşılaştırmak, NTP'den RTC'ye yazmayı doğrulamak ve SSR kontrolünü zaman damgalı olaylarla test etmek.

## Donanım / yapılandırma
- ESP32-C3 SuperMini, ESPHome 2026.9.1, ESP-IDF
- DS3231 I²C: SDA GPIO0, SCL GPIO1, adres 0x68, 50 kHz
- I²C taramasında ayrıca 0x57 görüldü; bu cihazın kimliği bu test kapsamında doğrulanmadı.
- SSR kontrol pini GPIO6; mevcut YAML'da `inverted: true` deneniyor.
- SSR çevrimi: 40 saniye ON / 20 saniye OFF.
- Wi-Fi SSID/parola `secrets.yaml` üzerinden alınır.

## Sonuç özeti — 2026-10-16
- ESPHome firmware'i 13:49:02'de derlenmiş; cihaz açılmış ve API bağlantısı kurulmuş.
- NTP senkronizasyonu gerçekleşmiş.
- RTC metin sensörü ilerleyen zaman değerleri üretmiş; bu tek başına RTC'nin doğru bağımsız çalıştığını kanıtlamaz.
- DS3231 başlangıç iletişim hatası devam etmiş.
- NTP'den RTC'ye yazma sırasında `I2C write failed at register 0x00` görülmüş; yazma başarısız kabul edilir.
- 40 s ON / 20 s OFF yazılım olayları loglanmış.
- `inverted: true` ile fiziksel SSR giriş/çıkış davranışı doğrulanmamış.
- Pilin güç kesilince zamanı koruması test edilmemiş.

## Devam görevi
**HDF-002 / DS3231 yazma hatasının kaynağını ayırma**
1. Kullanılan external component'in kaynak kodunda başlatma, register okuma ve register yazma fonksiyonlarını incele.
2. Başlangıçtaki `Communication with DS3231 failed` hatasının hangi I²C işlemiyle tetiklendiğini bul.
3. `I2C write failed at register 0x00` hatasının dönüş koşulunu belirle.
4. Mümkünse SSR çevrimini ve pin yapılandırmasını değiştirmeden, RTC yazma doğrulamasını ayrı bir deney olarak ele al.
5. Başarı ölçütü: NTP yazma eyleminden sonra RTC register değerleri okunup NTP zamanı ile karşılaştırılmalı; yalnızca komutun çağrılması PASS sayılmaz.

## Açık sınırlamalar
- Donanım arızası ve sürücü hatası arasında henüz karar verilmedi.
- GPIO yazılım durumu fiziksel SSR çıkışının kanıtı değildir.
- Yeni testler derlenip çalıştırılmadan başarılı kabul edilmez.
