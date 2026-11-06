# E16-E (100ms) — Home Assistant History analizi

**Tarih:** 2026-11-06  
**Test aralığı:** 15:16:00–15:26:00 (+03:00)  
**Yapılandırma:** CH1-1T / GPIO32 / ADC1_CH4; `sample_duration=100ms`; `interval=1s`; K=24.22; ADC 12dB.  
**Kaynak:** Kullanıcının sağladığı `history (47).csv`  
**Kaynak SHA-256:** `3338f48b30c6db379797bed89ffd6b68dcd04384ead8e1f31e6c9cb10be6dde3`  
**Kaynak boyutu:** 3,862,196 byte; 44,769 satır; 16 entity.

## 1. Kayıt bütünlüğü ve zaman aralığı

- Katsayısız CH1 entity: `sensor.esp32d1_bero_mod2_ch1_1t_faz_ham_akim`.
- E turunun 10 dakikalık analiz aralığında 600 katsayısız CH1 kaydı var.
- İlk kayıt 15:16:00.331, son kayıt 15:25:59.329 (+03:00).
- Yayın aralığı medyanı 1.000s; P95 1.0311s. Gözlenen en kısa/en uzun aralık 0.630s / 1.371s.
- Bu, HA History dışa aktarımındaki 10 dakikalık E aralığının 1 Hz hedefiyle yaklaşık 600 kayıt içerdiğini doğrular.

## 2. Kararlı ON pencerelerinin seçimi

SSR kontrol entity'sindeki ON/OFF zamanları çevrim sınırlarını belirlemek için kullanıldı; tek başına fiziksel akım kanıtı sayılmadı. ON bölümleri PZEM akım entity'siyle kontrol edildi.

Her SSR ON çevriminde geçiş etkisini azaltmak için ilk 5 saniye ve çevrimin bitiminden önceki son 5 saniye dışarıda bırakıldı. 15:26:00 test bitiş sınırı da uygulandı. Bu seçimle 10 çevrimden toplam 293 katsayısız SCT ölçümü alındı.

Bu seçilmiş kararlı ON alt aralıklarında PZEM ölçümleri:
- Çevrim başına 2–5 PZEM kaydı.
- Çevrim ortalamaları yaklaşık 0.4660–0.4684 A.
- Tüm seçilmiş PZEM kayıtlarının gözlenen min/max aralığı 0.465–0.469 A.

PZEM kararlı yük koşulunu destekliyor. UDP STATE fiziksel durum belirlemek için kullanılmadı.

## 3. Katsayısız SCT çıktısı — kararlı ON

Değerler ct_clamp `on_raw_value` çıktısıdır; ham ADC örnekleri değildir. K=24.22 çarpanı uygulanmadan önceki akım çıktısıdır.

| Ölçüt | Sonuç |
|---|---:|
| Örnek sayısı | 293 |
| Ortalama | 0.019264 A |
| Medyan | 0.019118 A |
| Popülasyon SD | 0.001034 A |
| CV | %5.37 |
| MAD | 0.000481 A |
| 1.4826 × MAD | 0.000713 A |
| P05 | 0.018083 A |
| P95 | 0.020759 A |
| P99 | 0.022383 A |
| P95–P05 genişliği | 0.002676 A |
| Ortalama ± 2 SD | 0.017196–0.021331 A |
| Minimum | 0.017413 A |
| Maksimum | 0.027513 A |

En yüksek değer 15:24:53.329'da (9. ON çevrimi) 0.027513 A olarak görüldü. Bu uç değer silinmedi; tam veri istatistiklerinde tutuldu.

## 4. Çevrim bazında ortalama

| ON çevrimi | n | Ortalama (A) | SD (A) |
|---:|---:|---:|---:|
| 1 | 30 | 0.019097 | 0.000840 |
| 2 | 30 | 0.019125 | 0.000870 |
| 3 | 30 | 0.019515 | 0.000685 |
| 4 | 30 | 0.019503 | 0.000813 |
| 5 | 30 | 0.019259 | 0.000830 |
| 6 | 30 | 0.019123 | 0.001433 |
| 7 | 30 | 0.019262 | 0.001191 |
| 8 | 30 | 0.018976 | 0.000619 |
| 9 | 30 | 0.019614 | 0.001712 |
| 10 | 23 | 0.019132 | 0.000644 |

Çevrim ortalamaları 0.018976–0.019614 A aralığında. Çevrimler arası merkez değerler birbirine yakın; 6. ve özellikle 9. çevrimde çevrim içi dağılım daha geniş.

## 5. Ardışık farklar

Her ON çevriminin içinde ardışık katsayısız yayın farkı `|x[n]-x[n-1]|` hesaplandı; çevrim sınırları arasında fark alınmadı.

- n=283 fark.
- Medyan: 0.000687 A.
- P95: 0.002772 A.
- P99: 0.006566 A.
- Maksimum: 0.008845 A.

Önceden belirlenmiş ortak bir sıçrama eşiği bulunmadığı için sıçrama sayısı üretilmedi; eşik sonradan seçilmedi.

## 6. Değerlendirme

- E turunda 100ms pencere ve 1s yayın aralığıyla 10 dakikalık kayıt yaklaşık 600 katsayısız yayın içeriyor.
- PZEM ON akımı seçilmiş pencerelerde 0.465–0.469 A aralığında kaldı; dolayısıyla SCT dağılımını açıklamak için büyük bir yük akımı değişimi görünmüyor.
- Kararlı ON SCT çıktısının CV değeri %5.37; P05–P95 bandı 2.676 mA genişliğinde.
- Tekil yüksek değerler mevcut; özellikle 9. çevrim maksimumu 0.027513 A. Ham kayıt korunmalı, uç değer çıkarılmamalı.
- Bu sonuç tek başına 100ms'nin iyi/kötü olduğunu göstermez. E16 D=50ms ve F=200ms ile aynı ON pencere seçim kuralı ve aynı metriklerle karşılaştırılmalıdır.
- E turu sonucu, D/F karşılaştırması tamamlanmadan örnekleme penceresi seçimi için nihai karar değildir.

## 7. Kaynak ve kanıt sınırı

- Bu analiz, kullanıcı tarafından yüklenen CSV'den üretildi. Kaynak dosyanın SHA-256 değeri yukarıda kayıtlıdır.
- CSV'nin tüm ham satırları burada analiz edildi; ancak 3.86 MB kaynak CSV bu commit ile GitHub'a kopyalanmadı. Orijinal dışa aktarım kullanıcı tarafından sağlanan dosyadır. Bu Markdown dosyası kaynak bütünlük hash'ini ve yeniden üretilebilir seçim/hesap yöntemini kaydeder.
- Cihaz OTA/build logu bu CSV ile birlikte sunulmadı; CSV, HA'da ölçüm yayınlarının varlığını ve zamanlamasını gösterir, çalışan firmware binary'sinin kaynak YAML hash'iyle birebir eşleştiğini kanıtlamaz.
