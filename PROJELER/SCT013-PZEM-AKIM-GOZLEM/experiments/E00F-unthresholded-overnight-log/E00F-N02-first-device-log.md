# E00F-N02 — Dört ADC kanalı ilk cihaz logu

- Tarih: 2026-10-30
- Kaynak: kullanıcı tarafından sağlanan ESPHome logu (KULLANICI RAPORU)
- ESPHome: 2026.10.1
- Cihaz: ESP32 rev. 3.1, hostname esp32d2
- Derleme zamanı: 2026-10-30 23:12:09 +0300
- Log başlangıcı: 23:13:34
- Log bitişi: 23:16:58
- OTA/API: cihaza bağlantı ve Home Assistant API bağlantısı başarılı
- Güvenli açılış: 23:14:28.959 satırında "Boot seems successful"

## Yapılandırma doğrulaması

Dört ADC girişi de başlatılmış; her biri 12 dB attenuation, samples=1, average sampling mode ve 1 saniye update interval ile raporlanmış:

| Kanal | GPIO | ADC kanalı | Başlangıç durumu |
|---|---:|---:|---|
| SCT RAW | 32 | ADC1_CH4 | Handle Init / Config / Calibration / Overall Init: OK |
| SCT voltaj | 33 | ADC1_CH5 | Handle Init / Config / Calibration / Overall Init: OK |
| Bias RAW | 34 | ADC1_CH6 | Handle Init / Config / Calibration / Overall Init: OK |
| Bias voltaj | 35 | ADC1_CH7 | Handle Init / Config / Calibration / Overall Init: OK |

CT Clamp: sample_duration 0.20 s, update_interval 2.00 s. Firmware'de mevcut 24.22 akım çarpanı korunmuştur. Bu logda çarpanın kendisi ayrı bir test değildir.

## Logdan çıkarılan istatistikler

Aralık 23:13:35–23:16:58. Sensör yayın satırları sayılmıştır; bu kısa başlangıç kesiti uzun dönem gürültü karakterizasyonu değildir.

| Entity | Kayıt | Min | Maks | Ortalama | Birim |
|---|---:|---:|---:|---:|---|
| SCT GPIO32 RAW | 204 | 1819 | 1865 | 1849.75 | count |
| SCT GPIO33 ADC Voltage | 204 | 1.644 | 1.671 | 1.66029 | V |
| Bias GPIO34 RAW | 204 | 1824 | 1872 | 1849.67 | count |
| Bias GPIO35 ADC Voltage | 204 | 1.600 | 1.677 | 1.65978 | V |
| SCT013 Raw AC | 102 | 0.00000 | 0.01416 | 0.003511 | V |
| SCT013 Akim | 102 | 0.000 | 0.343 | 0.08504 | A |

GPIO35 voltajındaki 1.600 V değeri yalnızca bir kayıtta görülmüştür. Bu tek kayıt çıkarıldığında kalan 203 değerin ortalaması yaklaşık 1.66007 V, popülasyon standart sapması yaklaşık 0.00679 V'tur. Tekil değer hata olarak silinmemiş, aykırı gözlem olarak not edilmiştir.

CT Clamp pencerelerinin 102 kaydında 47 sıfır, 55 sıfırdan farklı akım değeri vardır. Sıfırdan farklı akım değerlerinin minimumu 0.041 A, medyanı 0.155 A'dır. En yüksek değer 0.343 A'dır. Hatta yük olup olmadığı bu log metninden belirlenemez; yüksüz koşul kullanıcı tarafından ayrıca teyit edilmelidir. Yüksüzse bu değerler gerçek yük akımı değil, ölçüm zincirinin yüksüz çıktı davranışıdır.

## SPS alanının yorumu

CT Clamp debug satırlarında 2,672–3,310 farklı örnek ve 13,360–16,550 SPS görülmüştür; bu kesitte ortalama yaklaşık 15,783 SPS'tir. Bu değerler CT Clamp'in 200 ms ölçüm penceresindeki kabul edilen farklı örneklerinden türetilen çalışma göstergesidir. Dört ADC entity'sinin 1 saniyelik yayın aralığıyla karıştırılmamalı; bağımsız donanım ADC örnekleme hızı veya doğrulanmış sürekli ham örnekleme hızı olarak sunulmamalıdır.

## Örnek log ve yorum

```text
[23:13:34.511][C][adc:131]: Pin: GPIO32
[23:13:34.537][C][adc:131]: Overall Init: OK
[23:13:34.555][C][adc:017]: ADC Sensor 'BERO E00F SCT GPIO33 ADC Voltage'
[23:13:34.608][C][adc:131]: Overall Init: OK
[23:13:34.608][C][adc:017]: ADC Sensor 'BERO E00F Bias GPIO34 RAW'
[23:13:34.632][C][adc:131]: Overall Init: OK
[23:13:34.634][C][adc:017]: ADC Sensor 'BERO E00F Bias GPIO35 ADC Voltage'
[23:13:34.649][C][adc:131]: Overall Init: OK
[23:13:36.144][S][sensor]: 'BERO E00F SCT013 Raw AC' >> 0.00752 V
[23:13:36.145][S][sensor]: 'BERO E00F SCT013 Akim' >> 0.182 A
[23:14:28.959][I][safe_mode:154]: Boot seems successful; resetting boot loop counter
```

Yorum: Dört ADC kanalının başlatılması ve sensör değerlerinin yayımlanması doğrulanmıştır. Bu, ilk cihaz çalışma doğrulamasıdır; analog girişlerin fiziksel doğruluğu, pin bağlantı kalitesi, yüksüz gürültü seviyesi veya akım kalibrasyonu doğrulanmış değildir.

## Hata / uyarı durumu

Logda ERROR veya [E] satırı görülmemiştir. Açılışta ESP32 framework ayarlarına ilişkin üç optimizasyon uyarısı vardır (flash_chip, minimum_chip_revision, sram1_as_iram); bu kesitte ADC başlatma veya bağlantı hatası görülmemiştir.

## Sonraki adım

Kullanıcının sabah Home Assistant geçmiş dökümü bekleniyor. Dört ADC kanalı ile SCT Raw AC ve akım geçmişi aynı zaman aralığında incelenecek. Fiziksel yük durumu ve kablo/sensör konumu kullanıcı teyidiyle kaydedilecek. Bu kısa log tek başına yüksüz deney sonucunu kapatmaz.

## Durum

**İlk firmware çalışma doğrulaması: başarılı (kullanıcı loguna göre). Uzun süreli E00F gözlemi ve sabah HA geçmiş analizi: bekleniyor.**


## Home Assistant ara geçmiş dökümü — 2026-10-30

- **Kaynak:** Kullanıcının yüklediği `history (17).csv`; 651 satır, 3 sütun. Dosya Git'e ham veri olarak eklenmedi; bu raporda özetlendi.
- **Zaman aralığı:** CSV UTC zaman damgaları 20:15:00–20:17:32.469Z; Türkiye yerel saatiyle 23:15:00–23:17:32.469 (+03:00). Bu yaklaşık 2 dakika 32 saniyelik ara kesittir; sabaha kadar süren gece kaydı değildir.
- **Entity kayıt sayıları:** Akım 47; Raw AC 47; GPIO32 RAW 135; GPIO33 voltaj 131; GPIO34 RAW 149; GPIO35 voltaj 142. Farklı sayılar, entity'lerin ayrı yayın/değişim kayıtlarından oluştuğunu gösterir; satır satır eşzamanlı ölçüm kabul edilmez.

| Entity | n | Min | Maks | Ortalama | Popülasyon SD |
|---|---:|---:|---:|---:|---:|
| SCT GPIO32 RAW | 135 | 1826 | 1863 | 1847.50 count | 8.45 count |
| SCT GPIO33 ADC Voltage | 131 | 1.640 | 1.672 | 1.65849 V | 6.93 mV |
| Bias GPIO34 RAW | 149 | 1824 | 1868 | 1848.33 count | 9.02 count |
| Bias GPIO35 ADC Voltage | 142 | 1.600 | 1.677 | 1.65899 V | 8.38 mV |
| SCT013 Raw AC | 47 | 0 | 0.011806 | 0.003747 V | 3.72 mV |
| SCT013 Akim | 47 | 0 | 0.285943 | 0.09075 A | 0.09018 A |

- Akım entity'sinde 17 sıfır ve 30 sıfırdan farklı kayıt vardır. Bu kesitte yük durumu kullanıcı tarafından ayrıca belirtilmediği için sıfırdan farklı değerler gerçek yük akımı veya yüksüz gürültü diye sınıflandırılmamıştır.
- GPIO35 voltajında 1.600 V tek kayıt olarak görülür; otomatik dışlanmamıştır.
- **Önemli sınır:** CSV, HA geçmişindeki yayınlanan entity durumlarını içerir. 200 ms içindeki ham ADC örneklerini veya tüm ESPHome DEBUG Raw AC/N/SPS satırlarını içermez.
- **Yorum:** SCT ve bias voltaj ortalamaları bu kısa kesitte birbirine yakındır; ancak kanallar eşzamanlı örneklenmediği, kayıt sayıları farklı olduğu ve kesit kısa olduğu için korelasyon/nedensellik sonucu çıkarılamaz. Uzun dönem gece tabanı veya drift kararı verilemez.
- **Sonraki adım:** Cihaz mevcut yapılandırmayla sabaha kadar çalışmaya bırakılacak. Sabah alınacak tam HA geçmiş dökümünde zaman aralığı ve her entity'nin kapsama oranı doğrulanacak; bu ara kesitle birlikte değerlendirilecek. Fiziksel yük durumu ve kablo/sensör konumu kullanıcı teyidiyle kayda alınacak.
