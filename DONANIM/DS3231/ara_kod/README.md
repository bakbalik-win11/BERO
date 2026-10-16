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


## Son aşama kaydı — 2026-10-16 (13:58–14:00 logu)

- Son OTA firmware derleme zamanı logda 13:56:50 +0300 olarak görünüyor.
- NTP senkronizasyonu başarılı; DS3231 başlatma hatası ve register 0x00 yazma hatası devam ediyor.
- SSR yazılım döngüsü olayları üretiyor; ON aşamasında `GPIO_ON_READBACK_MISMATCH` görülüyor.
- **Bir sonraki iş:** GPIO6 lojik geri okuma mantığını `inverted: true` ile karşılaştır; ardından DS3231 harici bileşeninin init/read/write kaynak kodunu incele.
- **Değiştirmeden koru:** SSR 40 s ON / 20 s OFF döngüsü ve mevcut pin eşlemesi (SDA GPIO0, SCL GPIO1, SSR GPIO6).
- **Henüz doğrulanmadı:** RTC'ye başarılı yazma, DS3231'in bağımsız zaman okuması ve SSR'nin fiziksel çıkış/yük anahtarlaması.
- Bu kayıt güncellemesi firmware'i derlemez veya cihaza yüklemez; donanım testi yapılmadı.


## Yeni log değerlendirmesi — 2026-10-16, OTA 14:04:57

- Yeni çalışma da aynı temel sonucu verdi: NTP sync başarılı, DS3231 bileşen iletişimi FAILED ve register 0x00 yazması başarısız.
- RTC isimli text sensor ilerleyen saat gösteriyor ama bu, gerçek DS3231 register okumasının başarılı olduğunu kanıtlamıyor.
- SSR yazılım döngüsü OFF/ON olayları üretiyor; ON sırasında `GPIO_ON_READBACK_MISMATCH` tekrarlandı.
- Sıradaki işlem: önce GPIO6 geri okuma mantığını incele; ardından harici DS3231 bileşeninin init/read/write kaynak kodunu analiz et. Döngü 40 s ON / 20 s OFF olarak korunsun.
