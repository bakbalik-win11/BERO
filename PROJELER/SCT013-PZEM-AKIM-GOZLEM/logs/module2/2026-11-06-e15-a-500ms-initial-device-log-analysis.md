# E15 A turu — ilk cihaz çalışma kontrolü

**Tarih:** 2026-11-06  
**Kaynak log:** [ham cihaz logu](2026-11-06-e15-a-500ms-initial-device-log.txt)  
**Cihaz:** ESP32D1 / `esp32d1`  
**ESPHome:** 2026.10.2  
**Yapılandırma:** `esp32d1.yaml`  
**Deney hedefi:** E15 A turu, CH1-1T / GPIO32, 500 ms tetikleme

## Hedef ve kapsam

Bu kayıt, E15'in 10 dakikalık A turu değildir. Firmware'in derlenip cihaza yüklenmesinden sonraki ilk kısa çalışma kontrolüdür. Amaç tek SCT kanalının ölçüm üretmesini, ADC'nin başlatılmasını ve Modül 3 UDP olayının alınmasını doğrulamaktır.

## Logdan doğrulananlar

- ESPHome API bağlantısı ve handshake başarılı.
- Cihaz ESP32 rev3.1 olarak tanımlandı; Wi-Fi bağlı ve IP adresi `192.168.0.35`.
- GPIO32 / ADC1_CH4, 12 dB, tek ADC sample; ADC handle, config, calibration ve overall init durumları `OK`.
- ct_clamp ölçüm penceresi `0.10s`; kendi update interval değeri `never`.
- CH1-1T ham akım ve katsayı uygulanmış akım entity'leri yayın üretti.
- Logda 58 akım yayını var. İlk ve son yayın zamanları 13:45:55.199–13:46:23.691 (+03:00); kapsanan süre yaklaşık 28.492 saniye.
- Ardışık yayın aralıklarının medyanı 0.500 s; gözlenen aralık 0.427–0.577 s. Bu kısa kayıt nominal 2 Hz davranışını destekler; 10 dakikalık devamlılığı doğrulamaz.
- Modül 3'ten `BOOT_ID=C2A28BE410D5E83391CC4F05B51D6B90, EVENT_ID=314, STATE=OFF` paketi alındı. Ham olay, BOOT_ID, EVENT_ID ve STATE text_sensor'larına yayınlandı.

## Kısa akım özeti

UDP OFF paketinin cihaz tarafından alındığı zaman 13:46:11.525 (+03:00) olarak loglandı. Bu zaman çizgisine göre yayınlar betimleyici olarak iki gruba ayrıldı:

| Bölüm | n | Ortalama | Medyan | Popülasyon SD | Min–maks |
|---|---:|---:|---:|---:|---:|
| UDP OFF öncesi | 33 | 0.4639 A | 0.468 A | 0.0332 A | 0.306–0.506 A |
| UDP OFF ve sonrası | 25 | 0.1655 A | 0.164 A | 0.0259 A | 0.110–0.203 A |

Bu bölme yalnızca UDP olay zamanına göre yapılmıştır. UDP STATE fiziksel yük durumunun kanıtı değildir; dolayısıyla tablo bir ON/OFF yük doğrulaması veya nedensellik sonucu değildir. İlk 0.306 A yayını cihaz açılışına yakın olduğu için kararlı çalışma ortalaması gibi yorumlanmamalıdır.

## ADC örnek sayısı gözlemi

ct_clamp debug satırlarında ilk açılış örneği 7 farklı örnek / 70 SPS olarak görünüyor; sonraki ölçümlerde yaklaşık 1.155–1.318 farklı örnek / 100 ms ve 11.550–13.180 SPS değerleri var. İlk satır başlangıç/yerleşme anına aittir; sonraki pencerelerle aynı kararlı koşul gibi birleştirilmemelidir.

## Uyarılar ve sınırlar

- `flash_chip`, `minimum_chip_revision` ve `sram1_as_iram` mesajları optimizasyon önerileridir; bu logda derleme/çalışma hatası olarak görünmüyor.
- Bu log, A turunun 10 dakika sürdüğünü göstermez.
- Fiziksel yükün gerçekten açılıp kapandığını kanıtlamaz.
- Derlenen cihaz yapılandırmasının adı logda `esp32d1.yaml` olarak geçer. Depodaki E15 YAML kaynak dosyası ile çalışan binary arasında birebir hash eşleştirmesi bu logla kanıtlanmış değildir.
- Bu kısa kontrol, E15'in sıçrama sıklığı/şiddeti hakkında karşılaştırmalı sonuç üretmez.

## Sonuç

**İlk cihaz çalışma kontrolü LOG İLE DESTEKLENDİ.** ESP32D1 bağlantısı, GPIO32 ADC başlatması, CH1-1T yayınları ve UDP olay alımı gözlendi. E15 A turunun resmi 10 dakikalık kaydı ve B/C karşılaştırmaları hâlâ beklemededir.
