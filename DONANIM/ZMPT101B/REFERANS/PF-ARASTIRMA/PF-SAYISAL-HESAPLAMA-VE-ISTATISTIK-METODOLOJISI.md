# BERO – Gerçek PF için Sayısal Hesaplama ve İstatistik Metodolojisi

- Kayıt tarihi: 2026-11-22
- Kapsam: SCT013 akım dalga biçimi + ZMPT101B gerilim dalga biçimi ile gerçek güç faktörü araştırması
- Durum: Araştırma metodolojisi / henüz donanımda doğrulanmadı
- İlgili ana mimari: `PREBERO/ORTAK-MIMARI/MODUL-3-4-ORTAK-ZAMAN-PENCERELI-VERI-TOPLAMA-MIMARISI.md`

## 1. Amaç ve kapsam

Amaç osiloskopta dalga biçimi çizmek veya yalnızca sinüsün şeklini görsel olarak incelemek değildir. Amaç, gerilim ve akım sinyallerini sayısal örnekler olarak toplamak; örneklerden aktif güç, RMS, görünür güç ve gerçek güç faktörünü matematiksel olarak hesaplamak; ardından bu ölçümlerin pencere bazındaki istatistiksel davranışını incelemektir.

- Akım kanalı: SCT013.
- Gerilim kanalı: potansiyometreli ZMPT101B modülü.
- Osiloskop: analog dalga biçimi, ofset, kırpılma, gürültü ve kanal gecikmesini teşhis etmek için yardımcı araçtır.
- Asıl hesap girdisi: zaman bilgisiyle kaydedilmiş sayısal gerilim ve akım örnekleri.

Bu araştırma, BERO'nun ana akım ölçüm yolunu veya kapanmış MOD2-GRV001 V1.6 kalibrasyonunu değiştirmez. PF araştırması ayrı bir araştırma koludur.

## 2. Temel matematik

Önce ham ADC kodları uygun ölçek ve sensör kalibrasyonlarıyla fiziksel büyüklüklere dönüştürülür. DC bias/offset bileşeni ölçülür ve AC bileşenler elde edilir.

Pencere başına:
- `v_ac[n] = v_raw[n] - mean(v_raw)`
- `i_ac[n] = i_raw[n] - mean(i_raw)`

Bu pencere ortalaması çıkarma, ADC'nin tek beslemeli biasını kaldırmaya yarar. Ofset ortalamaları ayrıca tanısal veri olarak saklanmalıdır. Gerçek bir DC bileşen ölçülmesi gereken farklı bir uygulama olursa pencere ortalamasını körlemesine çıkarmak uygun değildir; bu araştırma 50 Hz şebeke AC ölçümüne odaklanır.

Eşzamanlı/zaman hizalı örnekler için:
- `P = mean(v_ac[n] * i_ac[n])`
- `Vrms = sqrt(mean(v_ac[n]^2))`
- `Irms = sqrt(mean(i_ac[n]^2))`
- `S = Vrms * Irms`
- `PF = P / S`, yalnızca pencere geçerliyse ve `S` yeterli büyüklükteyse.

Bu yöntem sinüzoidal olmayan dalga biçimlerinde de gerçek PF'yi hesaplamayı hedefler. Yalnızca faz açısı ölçüp `cos(phi)` hesaplamak gerçek PF ile aynı değildir.

## 3. Pencere uzunluğu ve şebeke frekansı

50 Hz nominal şebekede bir periyot 20 ms'dir. Pencereyi tam sayıda şebeke periyoduna yakın seçmek, pencerenin dalga biçimini yarım/eksik çevrimde kesmesinden kaynaklanan dalgalanmayı azaltır. Örneğin 10 nominal çevrim 200 ms'dir.

Ancak 50 Hz tam sabit değildir. Sabit 200 ms pencere her durumda tam 10 gerçek çevrim anlamına gelmez. İleriki aşamada şebeke frekansının ölçülmesi veya sıfır geçişlerine göre pencere sınırlarının belirlenmesi değerlendirilecektir. İlk prototipte sabit pencere kullanılacaksa pencere süresi ve frekans farkı kayda alınmalıdır.

Örnekleme aralıkları eşit değilse basit aritmetik ortalama, zaman boyunca eşit ağırlıklı ortalama anlamına gelmeyebilir. Bu durumda örnek zamanları incelenmeli; gerekirse zaman ağırlıklı sayısal integrasyon veya ortak zaman ızgarasına yeniden örnekleme değerlendirilmelidir.

## 4. Örnek zamanları ve kanal hizalaması

Gerilim ve akım örneklerinin aynı pencereye ait olması tek başına yeterli değildir; her örneğin zaman karşılığı eşleşmelidir.

Faz/zaman farkı:
- `delta_phi = 360° * f * delta_t`
- 50 Hz'de 1 ms zaman farkı 18°'ye karşılık gelir.

Bu nedenle ADC kanallarının gerçek dönüşüm zamanları zaman damgasıyla ölçülmelidir. ADS1115 tek ADC dönüşüm çekirdeğini çoklayarak kullanır; kanalları eşzamanlı örneklemez. MUX değişimi, dönüşüm süresi ve kanal tarama düzeninin etkisi deneyle ölçülmeden sabit bir kanal gecikmesi varsayılmayacaktır.

Hizalama seçenekleri:
1. Ölçülmüş zaman damgalarına göre eşleşen örnekleri seçmek.
2. Gerekirse ortak zaman ızgarasına enterpolasyonla taşımak.
3. Dirençli yükte referans PF yaklaşık 1 iken toplam kanal/sensör faz hatasını değerlendirmek.
4. ZMPT101B analog ön ucu ve SCT013 ölçüm yolunun kendi faz gecikmelerini ayrıca karakterize etmek.

Enterpolasyon, zaman hizalamasına yardımcı olabilir; yetersiz örnekleme hızının kaybettirdiği dalga biçimi bilgisini geri getirmez.

## 5. İstatistiksel katman

Her hesaplama penceresinde aşağıdaki özetler tutulmalıdır:

| Alan | Amaç |
|---|---|
| `window_start`, `window_end`, `sample_count` | Pencere kapsamı ve örnek yeterliliği |
| `mean_v_raw`, `mean_i_raw` | Bias/ofset takibi |
| `std_v`, `std_i` | Sinyal dağılımı |
| `min_v`, `max_v`, `min_i`, `max_i` | Sınırlar, spike ve kırpılma incelemesi |
| `vrms`, `irms` | Etkin değerler |
| `active_power_w` | Ortalama anlık güç |
| `apparent_power_va` | Görünür güç |
| `pf_true` | Gerçek güç faktörü |
| `sample_interval_mean`, `sample_interval_std` | Örnekleme zamanlaması |
| `validity_flags` | Pencerenin geçerli/geçersiz nedenleri |

Pencereler arası analizde PF ortalaması, standart sapması, min/max ve dağılımı incelenebilir. PF tek başına raporlanmamalı; P, Vrms, Irms, S ve geçerlilik bayraklarıyla birlikte tutulmalıdır.

## 6. Düşük akım ve PF geçerliliği

S görünür güç küçüldüğünde `PF=P/S` oranı gürültüye duyarlı hale gelir. Düşük akımda SCT013 ölçüm gürültüsü ve ADC ofseti PF değerini kararsızlaştırabilir.

Bu nedenle:
- `Irms` için deneyle belirlenmiş geçerlilik eşiği gerekir.
- `S` veya aktif güç için de ölçüm gürültüsüne dayalı alt sınır değerlendirilebilir.
- Kırpılma, eksik örnek, zamanlama sapması veya ADC hatası olan pencereler geçersiz işaretlenmelidir.
- Eşik altındaki PF değeri 0 veya gerçek ölçüm gibi sunulmamalı; `invalid / below_threshold` olarak işaretlenmelidir.

Eşikler önceden tahminle sabitlenmeyecek; yüksüz kayıt ve bilinen yük deneylerinden çıkarılacaktır.

## 7. Kalibrasyon sırası ve doğrulama yükleri

Önerilen sıra:
1. ZMPT101B analog çıkışının DC ofset, genlik, simetri ve kırpılma davranışını güvenli izole düşük gerilim kaynağında kontrol etmek.
2. SCT013 ve ZMPT101B ham kanallarının örnekleme hızını ve zaman damgalarını ölçmek.
3. Her kanalın ofset ve RMS ölçeğini bağımsız kalibre etmek.
4. Kanal ve sensör faz/zaman farkını belirlemek.
5. Bilinen dirençli yükte PF yaklaşık 1 beklentisiyle tüm ölçüm zincirini doğrulamak.
6. Farklı güç kaynakları, motorlu yükler ve elektronik kontrollü yüklerde dalga biçimi ve PF dağılımını incelemek.
7. PZEM PF/aktif güç değerlerini karşılaştırma verisi olarak kaydetmek; PZEM'i ground truth kabul etmemek.

PZEM ile RMS/aktif güç karşılaştırması genlik kalibrasyonuna yardımcı olabilir; tek başına gerilim-akım kanal fazını doğrulamaz.

## 8. ADS1115 için özel kısıt

ADS1115'in azami data rate değeri 860 SPS'dir ve çoklu kanal dönüşümleri sıralıdır. İki kanalın ideal dönüşüm süreleri basitçe yarı yarıya bölünse bile gerçek sistemde MUX geçişi, dönüşüm zamanlaması ve yazılım okuma gecikmeleri ölçülmelidir. İki kanalın aynı anda örneklenmediği unutulmamalıdır.

Bu kayıt ADS1115'in PF için yeterli olduğunu iddia etmez. Önce gerçek örnekleme ve zamanlama ölçülecek; sonuçlar dalga biçimi doğruluğu için yetersiz kalırsa daha uygun eşzamanlı örnekleme mimarisi araştırılacaktır. Mevcut ADS1115 ile deney yapmak, ADC'nin nihai seçim olarak onaylandığı anlamına gelmez.

## 9. Güvenlik

İlk dalga biçimi ve zamanlama testleri güvenli, galvanik olarak izole düşük gerilimli AC kaynakla yapılacaktır. Ototransformatör tek başına galvanik izolasyon sağlamaz. Osiloskop probunun toprak bağlantısı ve bilgisayar/USB toprak referansı bilinmeden şebeke tarafına bağlanmayacaktır.

## 10. Kaynak ve karar ayrımı

Bu not, Gemini tarafından sunulan teknik değerlendirmedeki yararlı noktalarla BERO'nun mevcut ölçüm hedeflerinin birleştirilmesiyle oluşturulmuş proje metodolojisidir. Buradaki formüller matematiksel yöntemdir; ADS1115'in BERO'da yeterliliği, ZMPT101B faz gecikmesi, eşik değerleri ve PF doğruluğu henüz deneyle kanıtlanmamıştır.

## Durum

- Sayısal PF ve istatistik metodolojisi depoya kaydedildi.
- Fiziksel ZMPT101B kart testi yapılmadı.
- ADS1115 iki kanallı zaman hizası ölçülmedi.
- PF hesaplama firmware'i yazılmadı veya doğrulanmadı.
