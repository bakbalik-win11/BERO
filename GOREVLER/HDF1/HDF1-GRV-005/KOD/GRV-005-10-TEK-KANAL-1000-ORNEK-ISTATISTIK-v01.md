# GRV-005-10 — Tek kanal 1000 örnek istatistik penceresi

## Hedef
GPIO33 / 1T kanalından `raw: true` ADC çıktılarıyla 1000 geçerli callback örneği toplamak ve pencere sonunda tek bir özel log satırında temel istatistikleri üretmek.

## Donanım ve kapsam
- ESP32-D1 / ESP32 rev3.x
- GPIO33 / 1T
- ESPHome ADC, `raw: true`
- `update_interval: 10ms` — nominal olarak yaklaşık 10 saniyelik pencere; gerçek süre callback zamanlamasına bağlıdır.
- CSV yok, PZEM yok, dört kanal yok.

## Üretilen alanlar
- `sample_count`: pencerede kabul edilen sonlu, negatif olmayan ADC callback değerleri; hedef 1000.
- `invalid_count=NOT_TRACKED`: ESPHome ADC sensör callback'i tek başına sürücü seviyesindeki başarısız okumaları saymaya izin vermediği için sayı uydurulmaz.
- `zero_count`: değeri tam sıfır olan geçerli örnekler.
- `adc_mean`: aritmetik ortalama.
- `adc_std`: örnek standart sapması, payda N−1.
- `adc_rms_raw`: ham ADC kodlarının RMS değeri.
- `adc_rms_ac=NA_NO_BIAS`: bu tek-kanal sürümü BIAS kanalını okumaz. Önceden belirlenen BIAS merkezli AC RMS tanımını değiştirmemek için ortalamadan çıkarılmış başka bir değer bu alanın yerine konmaz.

## Pencere davranışı
Her 1000 kabul edilmiş örnekten sonra tek bir `[I][grv005_window]` log satırı yazılır ve sayaçlar bir sonraki pencere için sıfırlanır. Sensör `internal: true` olduğundan bu test sensörünü Home Assistant varlığı olarak sunmayı hedeflemez; örnek başına normal sensör durum loglarını da önlemeyi amaçlar.

## Doğrulama durumu
- Kaydedilen aşama: kod taslağı.
- Derleme: kullanıcı tarafından henüz bu sürüm için bildirilmedi.
- Cihaza yükleme ve 1000 örnekli log: henüz doğrulanmadı.
- Bu dosya önceki GRV-005-09 v01 dosyasının üzerine yazmaz.

## Test sonrası kabul ölçütleri
1. Derleme başarılı olmalı.
2. Cihaz logunda `sample_count=1000` içeren tek satır görünmeli.
3. `adc_mean`, `adc_std`, `adc_rms_raw` sonlu sayılar olmalı.
4. `zero_count` gözlenen ham örneklerle tutarlı olmalı.
5. `invalid_count=NOT_TRACKED` ve `adc_rms_ac=NA_NO_BIAS` alanları eksiklikleri açıkça göstermeli; bunlar PASS edilmiş ölçümler sayılmamalı.
6. Bu aşama ADC sürücü hatası yakalama, BIAS merkezli RMS, PZEM zaman eşleme veya CSV doğrulaması değildir.
