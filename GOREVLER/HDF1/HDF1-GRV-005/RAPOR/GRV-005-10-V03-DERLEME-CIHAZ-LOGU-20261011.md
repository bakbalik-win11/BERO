# GRV-005-10 v03 — Derleme ve cihaz logu kaydı

- Tarih: 2026-10-11
- Cihaz: `esp32d1`, ESP32 rev3.1, 2 çekirdek
- ESPHome: 2026.9.1
- Firmware derleme zamanı (cihaz logu): 2026-10-11 10:52:48 +0300
- Kod: [GRV-005-10 v03 YAML](../KOD/GRV-005-10-TEK-KANAL-1000-ORNEK-ISTATISTIK-v03.yaml)
- İlgili kod raporu: [GRV-005-10 v03 açıklaması](../KOD/GRV-005-10-TEK-KANAL-1000-ORNEK-ISTATISTIK-v03.md)

## Sonuç

**PASS — kullanıcı derleme yaptığını ve aşağıdaki cihaz logunu bildirdi.** Logda art arda altı 1000 örnekli pencere ve gerçek `window_duration_ms` alanı mevcut. Bu, bu log kesitinde pencere istatistiklerinin ve süre ölçümünün çalıştığını doğrular.

## Cihazdan gelen pencere sonuçları

| Log saati | sample_count | window_duration_ms | zero_count | adc_mean | adc_std | adc_rms_raw | adc_rms_ac |
|---|---:|---:|---:|---:|---:|---:|---|
| 10:54:25.722 | 1000 | 10024 | 0 | 1863.719000 | 14.875191 | 1863.778303 | NA_NO_BIAS |
| 10:54:35.724 | 1000 | 10002 | 0 | 1863.991000 | 17.728147 | 1864.075219 | NA_NO_BIAS |
| 10:54:45.719 | 1000 | 9997 | 0 | 1864.585000 | 19.432097 | 1864.686153 | NA_NO_BIAS |
| 10:54:55.726 | 1000 | 10002 | 0 | 1864.227000 | 10.976154 | 1864.259280 | NA_NO_BIAS |
| 10:55:05.767 | 1000 | 10000 | 0 | 1863.658000 | 18.166151 | 1863.746447 | NA_NO_BIAS |
| 10:55:15.790 | 1000 | 10058 | 0 | 1864.582000 | 13.110193 | 1864.628043 | NA_NO_BIAS |

## Derleme ve bağlantı gözlemleri

- ESPHome API bağlantısı ve handshake başarılı.
- Cihaz ESP32 rev3.1, 2 çekirdek olarak raporlanmış.
- Firmware derleme zamanı: 10:52:48 +0300.
- `Boot seems successful; resetting boot loop counter` satırı mevcut.
- ESPHome, `minimum_chip_revision: "3.1"` ve `sram1_as_iram: true` ayarlarını öneren uyarılar vermiş. Bunlar bu logda fatal hata olarak görünmüyor; bu testin kapsamı dışında ve ayrı değerlendirilmelidir.
- `safe_mode took a long time for an operation (65 ms), max is 50 ms` uyarısı var; tek başına bu ölçüm penceresinin başarısız olduğu anlamına gelmez.

## Süre değerlendirmesi

Altı pencerenin ölçülen süreleri 9997–10058 ms aralığında. Ortalama süre yaklaşık 10013.8 ms'dir. Bu nedenle `update_interval: 10ms` nominal hedefinin pratikte yaklaşık 10 saniyelik pencere verdiği gözlenmiştir; tam 10.000 ms garantisi yoktur.

## Sınırlar

- `invalid_count=NOT_TRACKED`: gerçek ADC sürücü hataları ölçülmüş değildir.
- `adc_rms_ac=NA_NO_BIAS`: BIAS örneklenmediği için BIAS merkezli AC RMS yoktur.
- Bu sonuç GPIO33 tek kanal içindir; 4 kanal zamanlama, PZEM eşlemesi, CSV üretimi ve gerçek akım kalibrasyonu doğrulanmış değildir.
- Bu rapor kullanıcı tarafından sağlanan loga dayanır; bağımsız derleme çalıştırması iddia etmez.

## Sonraki adım

GRV-005-10 tek kanal örnek penceresi ve süre ölçümü aşaması PASS olarak işaretlenebilir. Bir sonraki adımdan önce hedefi ayrı tut: BIAS merkezli RMS gerekecekse BIAS örneklerinin aynı pencere ve uygun zamanlama sözleşmesiyle alınması gerekir. Dört kanal ve PZEM entegrasyonuna doğrudan atlanmamalıdır.
