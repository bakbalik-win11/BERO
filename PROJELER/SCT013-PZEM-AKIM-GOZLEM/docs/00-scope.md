# Kapsam ve başarı ölçütleri

## Amaç
SCT-013 benzeri CT'den ADC örnekleri toplayıp özet akım özellikleri çıkarmak; bu kayıtları PZEM'in akım, gerilim ve PF okumalarıyla zaman ekseninde karşılaştırmak.

## Kapsam dışı
- Enerji analizörü geliştirmek.
- Güç kalitesi ölçmek.
- SCT verisinden PF veya faz açısı hesaplamak.
- FFT, THD veya harmonik analiz.
- PZEM'i kusursuz veya sertifikalı ölçüm standardı kabul etmek; PZEM okumaları bu projede SCT verisini etiketlemek/eğitmek için temel referanstır. Modelin başarısı PZEM'e uyum üzerinden değerlendirilir, mutlak ölçüm doğruluğu iddiası değildir.

PZEM'in kendi PF çıktısı kayıt alanıdır; SCT'den PF hesaplanmayacaktır.

## Başlangıç kararları
- 2 kS/s SCT örnekleme.
- Nominal 200 ms SCT özet penceresi.
- Yaklaşık 1 s başlangıç PZEM sorgusu.
- Olay sonrası yaklaşık 3 s geçiş etiketi.
- Normalde özet, olay çevresinde kısa ham kayıt.

Bunlar tasarım başlangıçlarıdır; bu donanımda deneysel doğrulamaları henüz yapılmadı.

## Başarı ölçütleri
1. Fiziksel donanım zinciri ve calibration_id belgelenmiş.
2. Gerçek örnekleme hızı, sample_count, pencere süresi ve clipping ölçülmüş.
3. Geçersiz PZEM okumaları işaretlenmiş ve istatistiklere katılmamış.
4. SCT/PZEM zaman eşleştirme varsayımları açık.
5. 1 / 2 / 2,5 kS/s aynı yüklerde karşılaştırılmış.
6. Her deneysel iddia kendi protokolü ve veri kaydıyla desteklenmiş.

Kapsam veya önemli tasarım kararı değişirse ADR aç.
