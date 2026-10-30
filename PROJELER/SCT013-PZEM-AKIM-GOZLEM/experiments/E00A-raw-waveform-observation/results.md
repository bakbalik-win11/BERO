# E00A sonuç kaydı

**Durum:** PLANLANDI — firmware, fiziksel bağlantı ve ölçüm henüz yapılmadı.

| Koşul | Multimetre DC (V) | Hedef hız (S/s) | Kayıt süresi (s) | Örnek sayısı | Yaklaşık gerçek hız (S/s) | Ortalama ADC | Min | Max | Tepe-tepe | Std. sapma | Ham dosya |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Bias trafosu 3,3 V (10k/10k ölçüm bölücüsü üzerinden) | | 2000 | | | | | | | | | data/raw/E00A/bias_trafo_3v3.csv |
| Bias Vmid (doğrudan) | | 2000 | | | | | | | | | data/raw/E00A/bias_vmid.csv |

## Karşılaştırma
- ADC ham değerleri ve analogReadMilliVolts farkı:
- Multimetre ile ADC mV tahmini arasındaki fark:
- İki noktanın zaman içindeki değişimi:
- Örnek sayısı / gerçekleşen hız değerlendirmesi:
- Sonraki adım:

## HEDEF / LOG / SONUÇ

### HEDEF
Bias trafosunun L78L33 3,3 V çıkışını ve bias Vmid noktasını ayrı ayrı ADC ile okumak; ham değer, mV tahmini ve kısa dönem değişimi karşılaştırmak.

### LOG
- Gerçek ESP32 kart modeli ve GPIO:
- Bias trafosu fiziksel bileşen/bağlantı kontrolü:
- Ölçüm bölücüsünün direnç değerleri:
- Ortak GND bağlantısı:
- Firmware sürümü/commit:
- Her koşulun multimetre ölçümü, süresi, örnek sayısı, istatistikleri ve ham kayıt yolu:
- Yapılmayan kontroller:

### SONUÇ
- Verinin desteklediği yorum:
- Ölçüm sınırlamaları:
- Sonraki adım:

Ölçüm yapılmadan sonuç veya kabul kararı yazılmaz. Ham CSV dosyaları varsayılan olarak Git'e eklenmez.
