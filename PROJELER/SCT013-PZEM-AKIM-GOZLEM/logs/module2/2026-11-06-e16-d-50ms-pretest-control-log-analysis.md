# E16 D — 50ms ön test / kontrol logu analizi

**Tarih:** 2026-11-06  
**Log aralığı:** 15:00:21.591–15:00:52.446 (+03:00)  
**Kaynak:** Kullanıcının sağladığı ESPHome OTA/API logu  
**Ham dosya SHA-256:** `f6b799c818552b7b14dd6bb42a4d7aeb1d4c18e72e6208efa0a4670da9355a60`

## Kısa sonuç

Bu log, E16 D firmware yapılandırmasının cihazda çalıştığını ve tek CH1 kanalının ölçüm/yayın döngüsünün çalıştığını destekleyen **kısa ön test kontrolüdür**. Kullanıcının 15:01 olarak bildirdiği 10 dakikalık D turunun kendisi değildir; log 15:00:52'de biter ve yalnızca yaklaşık 31 saniye kapsar.

## Yapılandırma ve bağlantı doğrulamaları

- ESPHome 2026.10.2; firmware derleme zamanı 14:59:40 (+03:00).
- ESP32 rev3.1; cihaz IP 192.168.0.35.
- API çözümleme, bağlantı ve handshake başarılı.
- Log, `esp32d1.yaml` için validated config cache kullanıldığını bildiriyor. Bu nedenle çalışan binary'nin E16 D YAML dosyasıyla byte/hash düzeyinde birebir eşleşmesi bu logdan kanıtlanamaz.
- CH1 ADC: GPIO32 / ADC1 kanal 4, attenuation 12dB; Handle Init, Config, Calibration ve Overall Init sonuçlarının tamamı OK.
- ct_clamp Sample Duration: 0.05s (50ms); Update Interval: never.
- Katsayısız çıktı entity'si: `BERO Mod2 CH1-1T Faz Ham Akim`; K=24.22 uygulanmış entity ayrıca yayımlanıyor.

## Kısa akış sayımları ve zamanlama

- ct_clamp debug ölçümü: 31 kayıt.
- Katsayısız template entity yayını: 31 kayıt.
- İlk/son katsayısız yayın: 15:00:22.422–15:00:52.446; kapsanan süre yaklaşık 30.024 saniye.
- Katsayısız entity yayın aralığı: ortalama 1.0008s; medyan 1.0005s; minimum 0.969s; maksimum 1.031s. Bu kısa pencerede nominal 1Hz ritimle uyumlu.
- Her 50ms ölçüm penceresinde farklı ADC örnek sayısı 588–658; medyan 621. Logdaki SPS değerleri 11,760–13,160; ortalama yaklaşık 12,432 SPS.

## Katsayısız ct_clamp çıktısının betimleyici özeti

31 katsayısız yayın için, kararlı alan seçimi yapılmadan tüm kısa kontrol kayıtları:
- Ortalama: 0.014573
- Medyan: 0.018340
- Popülasyon SD: 0.006285
- Minimum: 0.004460
- Maksimum: 0.021140

İlk 10 değer yaklaşık 0.00446–0.00710 bandındayken 15:00:32.449'da 0.01718'e geçiyor ve devamında çoğunlukla 0.01658–0.02114 aralığında. Bu nedenle tüm 31 değerin ortalaması iki farklı seviye içeren kısa kontrolü tek bir kararlı yük ortalaması gibi temsil etmez. Bu geçişin fiziksel nedeni logdan belirlenemez; UDP event veya fiziksel yük durumu hakkında bu logda kanıt yoktur.

Katsayısız değerler ham ADC örnekleri değildir; ct_clamp hesaplamasının K çarpanı uygulanmadan önceki çıktısıdır.

## Uyarılar ve hata durumu

- `flash_chip`, `minimum_chip_revision` ve `sram1_as_iram` önerileri optimizasyon uyarılarıdır; logda ADC/API başlangıcını engelleyen hata görülmüyor.
- UDP olay alımına ilişkin bu kısa kesitte paket alındığını gösteren bir satır bulunmuyor. Bu, UDP alıcısının kesinlikle çalışmadığını kanıtlamaz; yalnızca bu log kesitinde olay görülmediğini belirtir.

## Kanıt sınırı / sonraki adım

Bu kayıt, D turunun 10 dakika sürdüğünü veya HA History verisinin tamamlandığını kanıtlamaz. Kullanıcı D turunu 15:01'de başlattığını bildirmişti; bu log o başlangıçtan hemen önce alınmış ön test kontrolüdür. 15:01–15:11 HA History kaydı ayrı alınmalı ve D turunun asıl analizi o veri üzerinden yapılmalıdır.

Ham log: [2026-11-06-e16-d-50ms-pretest-control-log.txt](2026-11-06-e16-d-50ms-pretest-control-log.txt)
