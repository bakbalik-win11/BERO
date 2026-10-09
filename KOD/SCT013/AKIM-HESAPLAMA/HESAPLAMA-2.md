# Hesaplama-2 — Sensör çıkışının volt RMS değerinden amper

## Fikir

Önce bias kaldırılarak ve ADC ölçeği uygulanarak sensör çıkışının AC RMS gerilimi bulunur. Ardından sensörün nominal oranı veya kalibrasyon sabiti kullanılır.

`I_rms = V_sensor_rms × (I_rated / V_rated)`

### SCT013-030

30 A'da 1 V RMS nominal çıkış:

`I_rms ≈ V_sensor_rms × 30`

Örnek: 0,20 V RMS sensör çıkışı → yaklaşık 6 A RMS.

### SCT013-100

100 A'da 1 V RMS nominal çıkış:

`I_rms ≈ V_sensor_rms × 100`

Örnek: 0,20 V RMS sensör çıkışı → yaklaşık 20 A RMS.

Bunlar nominal oranla hesap örnekleridir; gerçek doğruluk için referans akımla kalibrasyon gerekir.

## Bias ve ADC ölçeği

Örneklerin voltajı `V_i` ise AC bileşen:

`V_ac_rms = sqrt(sum((V_i - mean(V))^2) / N)`

Bu gerilim ADC pininde ölçülüyorsa ve arada bölücü/kazanç varsa, sensör çıkışına geri dönmek için analog devre oranı uygulanmalıdır. ADC VREF ve bit çözünürlüğü tek başına gerçek voltaj doğruluğunu garanti etmez.

## Burden direnci ayrımı

SCT013-030 ve SCT013-100 gibi 1 V çıkışlı modellerde dahili burden bulunduğundan SCT013-000 (100 A / 50 mA) için kullanılan harici burden örneğini doğrudan kopyalama. Yanlış yük direnci ölçüm oranını değiştirir.

## Kalibrasyon

Bilinen bir akımda referans True-RMS ampermetre kullan. Yazılımın gösterdiği akımla referans arasındaki oranı birden fazla noktada ölç. Tek noktada düzeltme, tüm aralıkta doğruluğu kanıtlamaz.
