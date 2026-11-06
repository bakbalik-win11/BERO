# E15 A/B/C + E16 D/E/F — Kararlı ON karşılaştırması

**Tarih:** 2026-11-06  
**Dal:** `exp/modul2-ch1-2hz-20261106`  
**Kaynak:** Kullanıcının sağladığı `history (48).csv`  
**Kaynak boyutu:** 4,123,366 byte  
**Kaynak SHA-256:** `53bdf3315195688a1e6f47f9cebb6c46db95d1b7a4bb5029e4e183a457db01b5`

## 1. Amaç

A/B/C yayın aralığı ve D/E/F ct_clamp ölçüm penceresi deneylerini, yalnız fiziksel yükün ON olduğu ve PZEM akımının kararlı yük koşulunu desteklediği bölümlerde karşılaştırmak. Ana seri CH1-1T katsayısız `ct_clamp on_raw_value` çıktısıdır; bu değer ham ADC örneği değildir. K=24.22 uygulanmış entity ana istatistik tablosuna alınmamıştır.

## 2. Tur eşleştirmeleri ve kanıt durumu

| Tur | Ayar | CSV'de kullanılan pencere (+03:00) | Gerçek yayın medyanı | Durum |
|---|---|---|---:|---|
| A | sample_duration 100ms, interval 500ms | 14:00:57–14:10:57 | 0.500 s | Zaman penceresi CSV cadence değişiminden eşleştirildi |
| B | sample_duration 100ms, interval 1s | 14:13:38–14:23:38 | 1.000 s | Zaman penceresi CSV cadence değişiminden eşleştirildi |
| C | sample_duration 100ms, interval 2s | 14:27:38–14:37:38 | 2.000 s | Zaman penceresi CSV cadence değişiminden eşleştirildi |
| D | sample_duration 50ms, interval 1s | 15:01:00–15:11:00 | 1.000 s | Başlangıç kullanıcı bildirimi; pencere bu bildirime göre seçildi |
| E | sample_duration 100ms, interval 1s | 15:16:00–15:26:00 | 1.000 s | Kullanıcı bildirimi ve önceki E16-E analiz aralığıyla eşleşiyor |
| F | sample_duration 200ms, interval 1s | 15:36:16–15:46:16 | 1.000 s | CSV'deki son yaklaşık 10 dakikalık 1 Hz segmentinden eşleştirildi; başlangıç bildirimi/cihaz logu bu dosyada yok |

A/B/C pencereleri deney sırası ve HA timestamp cadence geçişlerine göre eşleştirildi. D/E pencereleri kullanıcı tarafından bildirilen test zamanlarına dayandırıldı. F penceresi CSV'nin son 10 dakikalık 1 Hz segmentinden F deneyi olarak eşleştirildi; kullanıcı başlangıç bildirimi ve cihaz build/OTA logu ayrıca doğrulanmadı. CSV tek başına sample_duration değerini göstermez. D/E/F sample_duration etiketleri deney YAML planlarından gelir; çalışan binary'nin YAML ile birebir eşleştiği bu CSV ile kanıtlanmaz.

## 3. Ortak ON veri seçimi

- SSR kontrol entity'si yalnız ON çevrim sınırlarını bulmak için kullanıldı; UDP STATE fiziksel yük kanıtı olarak kullanılmadı.
- Her ON çevriminin ilk 5 saniyesi ve OFF öncesindeki son 5 saniyesi çıkarıldı.
- Test penceresinden önce başlamış ON çevrimleri tamamen dışarıda bırakıldı. Böylece altı turda yalnız pencere başladıktan sonra başlayan ON çevrimleri alındı.
- PZEM akımı bu ON alt aralıklarında kontrol edildi; altı turda seçilen PZEM kayıtları yaklaşık 0.463–0.469 A aralığında kaldı.
- OFF ve geçiş örnekleri ana ON istatistiklerine katılmadı. Ham CSV değişmedi.
- Her ON çevrimi ayrı tekrar olarak ele alındı. Ardışık SCT yayınları bağımsız deney tekrarı sayılmadı.

Bu ortak seçim kuralı, E16-E önceki raporundaki ilk/son 5 saniye dışlama yaklaşımını korur. Sonraki eğitim mimarisi kararında tanımlanan SCT kararlı başlangıcı + PZEM kararlı başlangıcı kesişimi ve SCT akım kesilme bitişi daha kesin pencere kuralıdır; bu rapor, o otomatik kararlılık algılayıcısı henüz tanımlanmadığından SSR sınırları ve PZEM kontrolüyle yapılmış karşılaştırmadır.

## 4. Kararlı ON katsayısız SCT dağılımı

Birim A. SD popülasyon standart sapmasıdır. MAD ham medyan mutlak sapmadır. IQR dışı sayısı Tukey 1.5×IQR sınırları dışındaki ölçümlerdir; silinmemiş, yalnız işaretlenmiştir.

| Tur | ON n | ON çevrimi | Ortalama | Medyan | SD | MAD | P05–P95 | Maksimum | IQR dışı |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 581 | 10 | 0.019405 | 0.019185 | 0.001237 | 0.000491 | 0.018150–0.021124 | 0.028936 | 27 (%4.65) |
| B | 271 | 10 | 0.019044 | 0.018939 | 0.000712 | 0.000451 | 0.018048–0.020301 | 0.022418 | 4 (%1.48) |
| C | 135 | 9 | 0.018972 | 0.018892 | 0.000811 | 0.000518 | 0.017789–0.020225 | 0.023293 | 2 (%1.48) |
| D | 292 | 10 | 0.018985 | 0.018682 | 0.001745 | 0.000572 | 0.017483–0.020649 | 0.035284 | 11 (%3.77) |
| E | 293 | 10 | 0.019264 | 0.019118 | 0.001034 | 0.000481 | 0.018083–0.020759 | 0.027513 | 10 (%3.41) |
| F | 300 | 10 | 0.019053 | 0.018869 | 0.000820 | 0.000407 | 0.018126–0.020336 | 0.023017 | 14 (%4.67) |

## 5. Merkez kestirici karşılaştırması

| Tur | Ortalama (A) | Medyan (A) | %10 trimmed mean (A) |
|---|---:|---:|---:|
| A | 0.019405 | 0.019185 | 0.019240 |
| B | 0.019044 | 0.018939 | 0.019001 |
| C | 0.018972 | 0.018892 | 0.018928 |
| D | 0.018985 | 0.018682 | 0.018763 |
| E | 0.019264 | 0.019118 | 0.019159 |
| F | 0.019053 | 0.018869 | 0.018946 |

Merkez kestiriciler aynı veri üzerinde birbirine yakın, fakat D gibi uç değerli turlarda ortalama daha fazla etkileniyor. Medyan ve trimmed mean daha dirençli. Trimmed mean burada yalnızca karşılaştırma adayıdır; %10 kırpma oranı nihai parametre olarak onaylanmış değildir.

## 6. PZEM kontrolü ve aday K oranları

| Tur | PZEM n | PZEM ortalama (A) | PZEM min–max (A) | PZEM ort. / SCT ort. | Çevrim K oranlarının medyanı* |
|---|---:|---:|---:|---:|---:|
| A | 36 | 0.467333 | 0.466–0.469 | 24.083 | 24.102 |
| B | 21 | 0.466762 | 0.465–0.468 | 24.510 | 24.560 |
| C | 35 | 0.466371 | 0.463–0.469 | 24.579 | 24.500 |
| D | 29 | 0.466448 | 0.465–0.469 | 24.569 | 24.700 |
| E | 32 | 0.467063 | 0.465–0.469 | 24.246 | 24.356 |
| F | 28 | 0.465929 | 0.464–0.467 | 24.454 | 24.370 |

*Çevrim K oranı: her ON çevriminde PZEM ortalaması / SCT ortalaması; tabloda çevrim oranlarının medyanı verilmiştir. PZEM yayınları SCT örneklerinden çok daha seyrektir; bunlar birebir eşzamanlı örnek çiftleri değildir. Bu yüzden K oranları aday/karşılaştırmalı göstergedir, nihai kalibrasyon katsayısı değildir.

Mevcut K=24.22 ile karşılaştırıldığında oranlar turdan tura değişmektedir. Tek bir 10 dakikalık tur veya farklı okuma ayarları arasında çıkan oranlarla nihai K seçilmemelidir. Önce aynı merkez kestiricinin çevrim bazında tutarlılığı ve farklı yük seviyelerinde doğrulaması gerekir.

## 7. İlk değerlendirme

1. **Merkez değerler birbirine yakın:** Altı turun kararlı ON medyanları 0.018682–0.019185 A aralığında. Yayın/ölçüm penceresi değişikliği, bu tek yük koşulunda medyanı dramatik biçimde değiştirmemiştir.
2. **B turu en düşük klasik SD/CV'yi verdi:** CV yaklaşık %3.74. F turu %4.30, C %4.27, E %5.35, A %6.37. D %9.19 ile en yüksek; ancak D'deki tekil büyük değer SD'yi belirgin yükseltiyor.
3. **Robust yayılım daha yakın sonuç veriyor:** MAD 0.000407–0.000572 A aralığında. D'nin MAD değeri diğerlerinden çok uzak değil. Bu, D'de geniş SD'nin büyük ölçüde uç değer etkisinden kaynaklandığını destekliyor.
4. **IQR işaretleme anlamlı bir inceleme aracı:** A'da 27, D'de 11, E'de 10 ve F'de 14 ölçüm 1.5×IQR sınırları dışında. Bunlar silinmedi. Özellikle D maksimumu 0.035284 A, IQR üst sınırı yaklaşık 0.021091 A üzerindedir.
5. **Örnekleme sıklığı ve ölçüm penceresi birbirinden ayrılmalı:** A/B/C farklı yayın hızlarına sahip olduğu için aynı süre içinde örnek sayıları farklıdır. D/E/F ise 1 Hz sabit yayınla karşılaştırılır. A/B/C ile D/E/F farkları tek bir nedenin etkisi olarak yorumlanamaz.
6. **Ölçüm penceresi için ilk görünüm:** D=50ms daha fazla uç değer/dağılım etkisi göstermiş; E=100ms ve F=200ms daha dar SD/MAD değerleri üretmiş. E ve F arasında F'nin MAD ve SD'si daha düşük. Ancak her biri tek oturum ve tek yük seviyesi olduğundan nihai seçim değildir.
7. **K katsayısı henüz belirlenmedi:** PZEM'in kararlı ON ortalamaları benzer olsa da tur bazlı K oranları farklı. Merkez kestirici seçimi, çevrimler arası birleştirme ve çoklu yük seviyesi doğrulaması tamamlanmalıdır.

## 8. Sınırlar

- F penceresi CSV segmentinden eşleştirilmiştir; F'nin kullanıcı tarafından bildirilen başlangıç zamanı ve cihaz logu bu analiz dosyasında mevcut değildir.
- A/B/C zamanları CSV'deki cadence geçişlerinden eşleştirilmiştir; her tur için firmware build/hash doğrulaması yoktur.
- CSV HA History export'udur; çalışan firmware binary'sinin depodaki YAML ile birebir eşleştiğini kanıtlamaz.
- Her tur tek oturumdur. Çevrimler aynı oturum içinde kümelenmiş tekrarlar olup bağımsız donanım/oturum tekrarı değildir.
- IQR sınırı dışındaki örnekler otomatik hata değildir; gerçek kısa olay, sensör davranışı veya ölçüm anomalisi olabilir. Ham veriler korunmalıdır.
- Bu analizde PZEM, ON kararlılığını kontrol eden proje referansıdır; mutlak ground truth olarak kabul edilmez.

## 9. Sonraki karar

Bu sonuçlar, eğitim aşamasında **medyan + MAD'ı merkez/yayılım adayları olarak öne çıkarıyor**; ortalama ve %10 trimmed mean karşılaştırma olarak korunmalı. IQR, uç değerleri silmek için değil, işaretlemek ve etkilerini ayrı raporlamak için kullanılmalı. Nihai kestirici ve K hesabı kararı henüz verilmemelidir.

Canlı yük değişimi için kayan pencere/Hampel algoritması bu raporun konusu değildir; eğitim istatistiğinden ayrı tasarlanacaktır.
