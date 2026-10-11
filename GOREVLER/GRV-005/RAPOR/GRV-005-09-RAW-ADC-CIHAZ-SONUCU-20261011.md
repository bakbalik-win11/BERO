# GRV-005-09 — Tek kanal raw ADC cihaz sonucu

- Tarih: 2026-10-11
- Cihaz: `esp32d1` / ESP32 rev3.1
- ESPHome: 2026.9.1
- Firmware derleme zamanı logda: 2026-10-11 10:35:52 +0300
- Kanal: GPIO33 / 1T
- Durum: Kullanıcı loguyla cihazda çalıştığı doğrulandı; etiketleme sorunu tespit edildi.

## 1. Logdan doğrulananlar

- API üzerinden `esp32d1 @ 192.168.0.8` bağlantısı ve handshake başarılı.
- Uygulama ESPHome 2026.9.1 ile derlenmiş; cihaz ESP32 rev3.1, iki çekirdek.
- `[I][grv005_raw]` loglarında GPIO33 için `raw ADC value` değerleri yaklaşık saniyede bir görülüyor.
- Paylaşılan log kesitindeki ham değerler yaklaşık 1853–1872 aralığında.
- Değerler birbirine yakın ve canlı örnekler üretiliyor; bu test yalnızca o anki GPIO33 değerlerini gösterir. Girişin elektriksel olarak neyi temsil ettiği, test koşulu/bağlantı bilgisi olmadan belirlenemez.
- Logdaki `Boot seems successful` kaydı, cihazın güvenli açılış sayaç sıfırlamasına ulaştığını gösteriyor.

## 2. Tespit edilen etiketleme problemi

Log iki satır üretiyor:
- Özel lambda: `GPIO33 raw ADC value = 1856`
- ESPHome sensör durumu: `'GRV005 1T Raw ADC Test' >> 1856 V`

İlk satır ham ADC kodu olarak loglanıyor. İkinci satır ise aynı değeri `V` birimiyle gösteriyor. Yaklaşık 1850 değerinin volt olduğu anlamına gelmez; bu, ham modun sensör varlık sunumunda yanlış birimle etiketlenmesidir. Home Assistant grafiklerinde/arayüzünde yanlış fiziksel birimle yorumlanmaması için birim ve sensör sunumu düzeltilmelidir.

## 3. Sonuç

**Başarılı:** Tek kanal `raw: true` ile düzenli sayısal çıktı üretiyor; test cihaz üzerinde çalıştı.

**Düzeltilmesi gereken:** Sensörün durum satırı `V` birimi gösteriyor. Sonraki ayrı sürümde raw değerin birim etiketi `count`/ADC count olarak ayarlanmalı veya sensörün HA'ya yanlış birimle sunulması engellenmeli. Bu değişiklik derlenip doğrulanmadan eski v01 dosyası değiştirilmemelidir.

## 4. Kapsam sınırı

- Bu test 1000 örnek penceresini doğrulamaz.
- Dört kanalın örnekleme zaman ilişkisini doğrulamaz.
- ADC okuma hatalarını algılamaz; `invalid_count` doğrulanmamıştır.
- PZEM hizalaması, istatistik üretimi ve CSV üretimi yoktur.
- Ham kodların fiziksel akıma dönüştürülmesi bu testin kapsamında değildir.

## 5. Sonraki adım

Yeni bir v02 tanılama YAML'ı hazırlanarak sensörün birim sunumu düzeltilecek; ardından yalnızca derleme yapılacak. v01 tarihsel kayıt olarak korunacak. Canlı cihazın yapılandırması açık karar olmadan değiştirilmemelidir.
