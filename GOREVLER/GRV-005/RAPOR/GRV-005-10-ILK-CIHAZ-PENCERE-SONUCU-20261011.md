# GRV-005-10 — İlk 1000 örnek cihaz sonucu

- Tarih: 2026-10-11
- Cihaz: `esp32d1`, ESP32 rev3.1, 2 çekirdek
- ESPHome: 2026.9.1
- Logdaki firmware derleme zamanı: 2026-10-11 10:47:19 +0300
- Kaynak: kullanıcının paylaştığı ESPHome API logu

## Sonuç

**PASS — 1000 callback örneğinden istatistik satırı üretildi.**

Paylaşılan kesitte art arda beş pencere `sample_count=1000` ile tamamlanmış. Her pencerede `invalid_count=NOT_TRACKED`, `zero_count=0`, ortalama, örnek standart sapması ve ham RMS yazdırılmış. `adc_rms_ac=NA_NO_BIAS` doğru biçimde belirsiz bırakılmış; bu tek kanal testinde BIAS örneklenmiyor.

| Log saati | sample_count | zero_count | adc_mean | adc_std | adc_rms_raw | adc_rms_ac |
|---|---:|---:|---:|---:|---:|---|
| 10:48:57.448 | 1000 | 0 | 1863.602000 | 19.781074 | 1863.706874 | NA_NO_BIAS |
| 10:49:07.451 | 1000 | 0 | 1866.569000 | 4.922140 | 1866.575483 | NA_NO_BIAS |
| 10:49:17.447 | 1000 | 0 | 1865.691000 | 5.403769 | 1865.698818 | NA_NO_BIAS |
| 10:49:27.446 | 1000 | 0 | 1864.649000 | 5.695809 | 1864.657691 | NA_NO_BIAS |
| 10:49:37.445 | 1000 | 0 | 1866.353000 | 12.497783 | 1866.394803 | NA_NO_BIAS |

## Önemli fark: pencere süresi alanı yok

GRV-005-10 v02 tasarımında loga `window_duration_ms` eklenmesi bekleniyordu. Ancak paylaşılan beş satırda bu alan görünmüyor. Dolayısıyla 1000 örneklik pencerenin tamamlandığı kanıtlandı, fakat bu log kesiti v02'nin süre alanını çalıştırdığını kanıtlamıyor. Olası açıklama, cihazda başka/önceki bir YAML derlemesinin çalışıyor olması veya yüklenen yapılandırmanın kaydedilen v02 ile aynı olmamasıdır. Mevcut log tek başına hangisi olduğunu belirlemiyor.

Firmware derleme zamanı 10:47:19; ilk pencere 10:48:57.448'de tamamlanmış. Bu zaman farkı tek başına pencere süresini göstermez. `window_duration_ms` olmadan 10 ms güncelleme aralığının gerçek gerçekleşme süresi çıkarılamaz.

## Yorum sınırları

- İlk pencerenin `adc_std=19.781074` değeri sonraki üç pencerenin yaklaşık 4.9–5.7 değerlerinden ve beşinci pencerenin 12.50 değerinden daha yüksek. Sebebi bu logdan belirlenemez; giriş koşulu ve sinyal kaydı olmadan gürültü, bağlantı veya yük değişimi diye sınıflandırılmamalı.
- Önceki ham ADC loglarında görülen yaklaşık 1853–1872 bandıyla ortalama seviyeleri genel olarak uyumlu görünse de yeni örneklerin dağılımı önceki kesitle aynı ölçüm penceresi değildir.
- `invalid_count=NOT_TRACKED` ADC sürücü hata sayımı değildir.
- Bu test BIAS merkezli AC RMS, dört kanal senkronluğu, PZEM hizalaması veya CSV üretimini doğrulamaz.

## Sonraki adım

1. Cihazda çalışan YAML'ın GRV-005-10 v02 olup olmadığını derlenen dosya ve yükleme kaydıyla karşılaştır.
2. `window_duration_ms` alanı görülecek şekilde logu yeniden al.
3. Mevcut çalışan cihaz yapılandırmasını değiştirmeden önce açık karar ver; ESP adı `esp32d1` korunmalı.
