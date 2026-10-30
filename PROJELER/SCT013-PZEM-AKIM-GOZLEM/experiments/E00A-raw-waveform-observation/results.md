# E00A sonuç kaydı

**Durum:** FIRMWARE KODU DEPOYA EKLENDİ — kullanıcı kodun derlendiğini ve çalıştığını bildirdi; ADC değerleri ve cihaz logu bekleniyor.

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


## 2026-10-30 — ESP32D2 ADC firmware ilk çalıştırma bildirimi

### HEDEF
GPIO34 ve GPIO35 üzerinden iki ayrı ESP32 ADC kanalını kullanarak aynı deney girişini iki farklı çıktı türüyle gözlemek: GPIO34 ham ADC sayısı, GPIO35 kalibrasyonlu voltaj tahmini.

### LOG
- Kullanıcı, ESPHome yapılandırmasının **derlendiğini ve çalıştığını** bildirdi (KULLANICI RAPORU).
- Tam yapılandırma depoya eklendi: [firmware/esp32d2-e00a-adc.yaml](firmware/esp32d2-e00a-adc.yaml).
- Cihaz adı: esp32d2; framework: ESP-IDF; GPIO34: ADC raw; GPIO35: ADC voltaj; attenuation: 12 dB; sensör güncelleme aralığı: 1 s.
- Bu kayıt anında derleme çıktısı/cihaz logu henüz paylaşılmadı; ADC sayısal değerleri, fiziksel pin bağlantıları, gözlem süresi ve ham CSV mevcut değil.
- 1 saniyelik sensör güncellemesi, 30 saniyelik ham ADC kaydı veya 2 kS/s edinim olarak yorumlanmaz.

### SONUÇ
- **Kod durumu:** Kullanıcı bildirimiyle derlendi ve çalıştı.
- **Ölçüm durumu:** Henüz yorumlanmadı. GPIO34 ham sayısı ile GPIO35 voltaj tahmininin gerçek değerleri ve kararlılığı log geldikten sonra değerlendirilecek.
- Bu bildirim tek başına ADC doğruluğunu, Vmid bağlantısını veya 30 saniyelik deney kabul ölçütlerini kanıtlamaz.
- **Sonraki adım:** Kullanıcı ESPHome/cihaz logunu ve Home Assistant'ta görülen iki sensörün değerlerini paylaşacak; değerlendirme sonrasında bu dosyaya eklenecek.


## 2026-10-30 — E00A-S01 GND referans testi

### HEDEF
SCT bağlı değilken GPIO34 ve GPIO35 girişlerini GND'ye referanslayıp uzun logda kararlılığı görmek; floating giriş davranışını ayırmak.

### LOG
- Kaynak: Kullanıcının paylaştığı `Yapıştırılan metin(8).txt`; ESPHome 2026.9.1, ESP32 rev3.1.
- Kullanıcı bildirimi: GPIO34 ve GPIO35 GND'ye bağlandı.
- GPIO34 raw: 14:49:11–14:52:24 arasında görünen her kayıtta 0 count.
- GPIO35 calibrated voltage: ilk bölümde 0.181–0.195 V, 14:49:24'te 2.405 V sıçrama, sonra düşüş; yaklaşık 14:49:29–14:52:24 arasında 0.142 V sabit.
- Kararlı bölüm yaklaşık 175 saniye; sensör bağlı değil.
- ADC Handle Init, Config, Calibration ve Overall Init her iki kanalda OK.
- Sensör güncelleme aralığı 1 s; bu yüksek hızlı ham örnekleme değildir.
- GPIO34 ve GPIO35 ayrı fiziksel ADC kanallarıdır; aynı analog örneğin count/volt karşılığı değildir.
- Ayrıntılı analiz: [E00A-S01 raporu](reports/E00A-S01-gnd-reference-stability.md).

### SONUÇ
GND'ye referanslama ile giriş kararlılığı gözlendi. Önceki açık giriş dalgalanması floating giriş teşhisini destekler. GPIO35'in GND'de 0.142 V göstermesi ADC voltaj tabanı/ofseti açısından açık sorudur; neden kesinleşmedi. Bu kayıt ADC'nin tam aralık doğruluğunu, 1.65 V davranışını veya SCT ölçümünü kanıtlamaz.

### Elektriksel karar adayı
Yazılımsal sıfırlama yerine ADC girişinin sensör yokken de tanımlı DC seviyede kalması hedeflenir. Jack/CT topolojisi doğrulandıktan sonra ADC düğümüne Vmid'e karşı 47–100 kΩ yüksek değerli bias direnci prototip olarak değerlendirilecek. Bu değer aralığı henüz doğrulanmış tasarım/BOM değildir. İlk sonraki test: tek kanalda Vmid bias, multimetreyle DC doğrulama, 60 saniye log.


## Düzeltme — GPIO34 bağlı değil; GPIO35 Vmid logu (2026-10-30)

Kullanıcı düzeltmesi: GPIO34 count kanalı bağlı değildir. GPIO34'ün 0 count değeri fiziksel GND testi kanıtı değildir; yorum dışıdır.

Yeni logda GPIO35 ADC voltajı 14:57:02'de 1.678 V ile başlıyor; ilk bölümde yaklaşık 1.651–1.744 V arasında değişiyor, ardından belirgin biçimde düşerek 14:57:26'da 0.699 V'a ulaşıyor. Kullanıcı Vmid'in multimetrede sabit yaklaşık 1.65 V DC olduğunu bildiriyor. ADC logu ile multimetre arasında uyuşmazlık vardır. Kök neden belirlenmedi; ADC arızası sonucu çıkarılamaz.

Sonraki ayırıcı test: GPIO34 yorum dışı. Yalnız GPIO35 bağlı olacak. Multimetre siyah probu ESP32 GND, kırmızı probu doğrudan GPIO35 pininde tutulurken aynı anda log alınacak; Vmid düğümü ayrıca ölçülecek. Kablo sürekliliği ve ortak GND doğrulanmadan direnç veya yazılım filtresi eklenmeyecek.
