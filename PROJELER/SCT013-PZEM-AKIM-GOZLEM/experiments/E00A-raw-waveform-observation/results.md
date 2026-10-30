# E00A sonuç kaydı

**Durum:** AÇILDI / İLK REFERANS VERİSİ KAYDEDİLDİ — multimetre ölçümü kullanıcı tarafından bildirildi; ESP32 ADC kaydı henüz yapılmadı.

| Koşul | Multimetre DC (V) | Hedef hız (S/s) | Kayıt süresi (s) | Örnek sayısı | Yaklaşık gerçek hız (S/s) | Ortalama ADC | Min | Max | Tepe-tepe | Std. sapma | Ham dosya |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Bias trafosu 3,3 V (ayrı 10k/10k ölçüm bölücüsü planı; ADC henüz bağlanmadı) | **3,31** | Henüz belirlenmedi | **30 (plan)** | — | — | — | — | — | — | — | data/raw/E00A/bias_trafo_3v3.csv |
| Bias Vmid (breadboard orta noktası; doğrudan ADC koşulu henüz yapılmadı) | **1,65** | Henüz belirlenmedi | **30 (plan)** | — | — | — | — | — | — | — | — | data/raw/E00A/bias_vmid.csv |

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
- 2026-10-30 — Kullanıcı bildirimi: bias trafosunun L78L33 DC çıkışı multimetreyle 3,31 V ölçüldü. Kanıt türü: KULLANICI BİLDİRİMİ; multimetre marka/modeli, fotoğraf ve bağımsız tekrar bu kayıtta yok.
- 2026-10-30 — Kullanıcı bildirimi: bias breadboard üzerindeki Vmid/orta nokta multimetreyle 1,65 V okundu. Kanıt türü: KULLANICI BİLDİRİMİ; bu okuma breadboard üzerindeki bias orta noktasına aittir, ESP32 ADC ölçümü değildir.
- 30 saniye, her ADC koşulu için planlanan gözlem süresidir; henüz gerçekleştirilmedi.
- Gerçek ESP32 kart modeli ve GPIO:
- Bias trafosu fiziksel bileşen/bağlantı kontrolü:
- Ölçüm bölücüsünün direnç değerleri:
- Ortak GND bağlantısı:
- Firmware sürümü/commit:
- Her koşulun multimetre ölçümü, süresi, örnek sayısı, istatistikleri ve ham kayıt yolu: L78L33 çıkışı 3,31 V ve breadboard Vmid orta noktası 1,65 V (ikisi de kullanıcı multimetre bildirimi); ADC kayıtları henüz yok.
- Yapılmayan kontroller:

### SONUÇ
- İlk referanslar: L78L33 çıkışı 3,31 V; breadboard bias orta noktası 1,65 V olarak multimetreyle raporlandı. Bunlar iki ayrı DC noktasının kullanıcı tarafından bildirilen multimetre okumalarıdır; ESP32 ADC ölçümü değildir ve 30 saniyelik kararlılığı göstermez.
- Verinin desteklediği yorum:
- Ölçüm sınırlamaları:
- Sonraki adım:

Ölçüm yapılmadan sonuç veya kabul kararı yazılmaz. Ham CSV dosyaları varsayılan olarak Git'e eklenmez.
