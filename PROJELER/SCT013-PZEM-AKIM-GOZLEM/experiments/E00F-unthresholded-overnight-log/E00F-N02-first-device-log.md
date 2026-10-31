# E00F-N02 — Dört ADC kanalı ilk cihaz logu

- Tarih: 2026-10-30
- Kaynak: kullanıcı tarafından sağlanan ESPHome logu (KULLANICI RAPORU)
- ESPHome: 2026.10.1
- Cihaz: ESP32 rev. 3.1, hostname esp32d2
- Derleme zamanı: 2026-10-30 23:12:09 +0300
- Log başlangıcı: 23:13:34
- Log bitişi: 23:16:58
- OTA/API: cihaza bağlantı ve Home Assistant API bağlantısı başarılı
- Güvenli açılış: 23:14:28.959 satırında "Boot seems successful"

## Yapılandırma doğrulaması

Dört ADC girişi de başlatılmış; her biri 12 dB attenuation, samples=1, average sampling mode ve 1 saniye update interval ile raporlanmış:

| Kanal | GPIO | ADC kanalı | Başlangıç durumu |
|---|---:|---:|---|
| SCT RAW | 32 | ADC1_CH4 | Handle Init / Config / Calibration / Overall Init: OK |
| SCT voltaj | 33 | ADC1_CH5 | Handle Init / Config / Calibration / Overall Init: OK |
| Bias RAW | 34 | ADC1_CH6 | Handle Init / Config / Calibration / Overall Init: OK |
| Bias voltaj | 35 | ADC1_CH7 | Handle Init / Config / Calibration / Overall Init: OK |

CT Clamp: sample_duration 0.20 s, update_interval 2.00 s. Firmware'de mevcut 24.22 akım çarpanı korunmuştur. Bu logda çarpanın kendisi ayrı bir test değildir.

## Logdan çıkarılan istatistikler

Aralık 23:13:35–23:16:58. Sensör yayın satırları sayılmıştır; bu kısa başlangıç kesiti uzun dönem gürültü karakterizasyonu değildir.

| Entity | Kayıt | Min | Maks | Ortalama | Birim |
|---|---:|---:|---:|---:|---|
| SCT GPIO32 RAW | 204 | 1819 | 1865 | 1849.75 | count |
| SCT GPIO33 ADC Voltage | 204 | 1.644 | 1.671 | 1.66029 | V |
| Bias GPIO34 RAW | 204 | 1824 | 1872 | 1849.67 | count |
| Bias GPIO35 ADC Voltage | 204 | 1.600 | 1.677 | 1.65978 | V |
| SCT013 Raw AC | 102 | 0.00000 | 0.01416 | 0.003511 | V |
| SCT013 Akim | 102 | 0.000 | 0.343 | 0.08504 | A |

GPIO35 voltajındaki 1.600 V değeri yalnızca bir kayıtta görülmüştür. Bu tek kayıt çıkarıldığında kalan 203 değerin ortalaması yaklaşık 1.66007 V, popülasyon standart sapması yaklaşık 0.00679 V'tur. Tekil değer hata olarak silinmemiş, aykırı gözlem olarak not edilmiştir.

CT Clamp pencerelerinin 102 kaydında 47 sıfır, 55 sıfırdan farklı akım değeri vardır. Sıfırdan farklı akım değerlerinin minimumu 0.041 A, medyanı 0.155 A'dır. En yüksek değer 0.343 A'dır. Hatta yük olup olmadığı bu log metninden belirlenemez; yüksüz koşul kullanıcı tarafından ayrıca teyit edilmelidir. Yüksüzse bu değerler gerçek yük akımı değil, ölçüm zincirinin yüksüz çıktı davranışıdır.

## SPS alanının yorumu

CT Clamp debug satırlarında 2,672–3,310 farklı örnek ve 13,360–16,550 SPS görülmüştür; bu kesitte ortalama yaklaşık 15,783 SPS'tir. Bu değerler CT Clamp'in 200 ms ölçüm penceresindeki kabul edilen farklı örneklerinden türetilen çalışma göstergesidir. Dört ADC entity'sinin 1 saniyelik yayın aralığıyla karıştırılmamalı; bağımsız donanım ADC örnekleme hızı veya doğrulanmış sürekli ham örnekleme hızı olarak sunulmamalıdır.

## Örnek log ve yorum

```text
[23:13:34.511][C][adc:131]: Pin: GPIO32
[23:13:34.537][C][adc:131]: Overall Init: OK
[23:13:34.555][C][adc:017]: ADC Sensor 'BERO E00F SCT GPIO33 ADC Voltage'
[23:13:34.608][C][adc:131]: Overall Init: OK
[23:13:34.608][C][adc:017]: ADC Sensor 'BERO E00F Bias GPIO34 RAW'
[23:13:34.632][C][adc:131]: Overall Init: OK
[23:13:34.634][C][adc:017]: ADC Sensor 'BERO E00F Bias GPIO35 ADC Voltage'
[23:13:34.649][C][adc:131]: Overall Init: OK
[23:13:36.144][S][sensor]: 'BERO E00F SCT013 Raw AC' >> 0.00752 V
[23:13:36.145][S][sensor]: 'BERO E00F SCT013 Akim' >> 0.182 A
[23:14:28.959][I][safe_mode:154]: Boot seems successful; resetting boot loop counter
```

Yorum: Dört ADC kanalının başlatılması ve sensör değerlerinin yayımlanması doğrulanmıştır. Bu, ilk cihaz çalışma doğrulamasıdır; analog girişlerin fiziksel doğruluğu, pin bağlantı kalitesi, yüksüz gürültü seviyesi veya akım kalibrasyonu doğrulanmış değildir.

## Hata / uyarı durumu

Logda ERROR veya [E] satırı görülmemiştir. Açılışta ESP32 framework ayarlarına ilişkin üç optimizasyon uyarısı vardır (flash_chip, minimum_chip_revision, sram1_as_iram); bu kesitte ADC başlatma veya bağlantı hatası görülmemiştir.

## Sonraki adım

Kullanıcının sabah Home Assistant geçmiş dökümü bekleniyor. Dört ADC kanalı ile SCT Raw AC ve akım geçmişi aynı zaman aralığında incelenecek. Fiziksel yük durumu ve kablo/sensör konumu kullanıcı teyidiyle kaydedilecek. Bu kısa log tek başına yüksüz deney sonucunu kapatmaz.

## Durum

**İlk firmware çalışma doğrulaması: başarılı (kullanıcı loguna göre). Uzun süreli E00F gözlemi ve sabah HA geçmiş analizi: bekleniyor.**


## Home Assistant ara geçmiş dökümü — 2026-10-30

- **Kaynak:** Kullanıcının yüklediği `history (17).csv`; 651 satır, 3 sütun. Dosya Git'e ham veri olarak eklenmedi; bu raporda özetlendi.
- **Zaman aralığı:** CSV UTC zaman damgaları 20:15:00–20:17:32.469Z; Türkiye yerel saatiyle 23:15:00–23:17:32.469 (+03:00). Bu yaklaşık 2 dakika 32 saniyelik ara kesittir; sabaha kadar süren gece kaydı değildir.
- **Entity kayıt sayıları:** Akım 47; Raw AC 47; GPIO32 RAW 135; GPIO33 voltaj 131; GPIO34 RAW 149; GPIO35 voltaj 142. Farklı sayılar, entity'lerin ayrı yayın/değişim kayıtlarından oluştuğunu gösterir; satır satır eşzamanlı ölçüm kabul edilmez.

| Entity | n | Min | Maks | Ortalama | Popülasyon SD |
|---|---:|---:|---:|---:|---:|
| SCT GPIO32 RAW | 135 | 1826 | 1863 | 1847.50 count | 8.45 count |
| SCT GPIO33 ADC Voltage | 131 | 1.640 | 1.672 | 1.65849 V | 6.93 mV |
| Bias GPIO34 RAW | 149 | 1824 | 1868 | 1848.33 count | 9.02 count |
| Bias GPIO35 ADC Voltage | 142 | 1.600 | 1.677 | 1.65899 V | 8.38 mV |
| SCT013 Raw AC | 47 | 0 | 0.011806 | 0.003747 V | 3.72 mV |
| SCT013 Akim | 47 | 0 | 0.285943 | 0.09075 A | 0.09018 A |

- Akım entity'sinde 17 sıfır ve 30 sıfırdan farklı kayıt vardır. Bu kesitte yük durumu kullanıcı tarafından ayrıca belirtilmediği için sıfırdan farklı değerler gerçek yük akımı veya yüksüz gürültü diye sınıflandırılmamıştır.
- GPIO35 voltajında 1.600 V tek kayıt olarak görülür; otomatik dışlanmamıştır.
- **Önemli sınır:** CSV, HA geçmişindeki yayınlanan entity durumlarını içerir. 200 ms içindeki ham ADC örneklerini veya tüm ESPHome DEBUG Raw AC/N/SPS satırlarını içermez.
- **Yorum:** SCT ve bias voltaj ortalamaları bu kısa kesitte birbirine yakındır; ancak kanallar eşzamanlı örneklenmediği, kayıt sayıları farklı olduğu ve kesit kısa olduğu için korelasyon/nedensellik sonucu çıkarılamaz. Uzun dönem gece tabanı veya drift kararı verilemez.
- **Sonraki adım:** Cihaz mevcut yapılandırmayla sabaha kadar çalışmaya bırakılacak. Sabah alınacak tam HA geçmiş dökümünde zaman aralığı ve her entity'nin kapsama oranı doğrulanacak; bu ara kesitle birlikte değerlendirilecek. Fiziksel yük durumu ve kablo/sensör konumu kullanıcı teyidiyle kayda alınacak.


## Tam gece Home Assistant geçmiş analizi — 2026-10-31

- **Kaynak:** Kullanıcının yüklediği `history (19).csv`; 177.370 satır, 3 sütun, 6 entity. Dosya 16.171.115 bayt; SHA-256: `5bec07f210f744f14aa5d509538f69105e32dcb0e4c2e76c0aa4c44377a91ac2`. Ham CSV Git'e eklenmedi.
- **Zaman aralığı:** 2026-10-30 20:15:00.000Z – 2026-10-31 07:07:48.897Z; Türkiye saatiyle 23:15:00 – 10:07:48.897. Toplam 10 saat 52 dakika 48.897 saniye. Bu, önceki 651 satırlık/2 dk 32 sn ara CSV'den farklı olarak gece boyunca uzanan dökümdür.
- **Entity kayıtları:** SCT Akım 19.114 (19.113 sayısal), Raw AC 19.114 (19.113 sayısal), GPIO33 voltaj 33.560 (33.559 sayısal), GPIO35 voltaj 34.603 (34.602 sayısal), GPIO32 RAW 34.708 (34.707 sayısal), GPIO34 RAW 36.271 (36.270 sayısal). Entity kayıt adetleri farklıdır; satırlar eşzamanlı ölçüm olarak ele alınmamıştır.
- **Kayıt sürekliliği:** Medyan aralık Akım/Raw AC için 2.000 s; dört ADC entity'sinde yaklaşık 1.001–1.003 s. En uzun boşluk Akım/Raw AC'de 44.003 s; GPIO32 RAW'da 21.160 s; GPIO33 voltajda 21.159 s; GPIO34 RAW'da 20.820 s; GPIO35 voltajda 20.820 s. Kayıt gece boyunca sürmüştür, ancak kesintisiz ve eşzamanlı örnekleme değildir.

### Ham geçmiş istatistikleri

| Entity | n (sayısal) | Min | Medyan | Ortalama | Maks | SD |
|---|---:|---:|---:|---:|---:|---:|
| SCT Akım | 19.113 | 0 A | 0.192920 A | 0.194878 A | 2.665238 A | 0.110286 A |
| SCT Raw AC | 19.113 | 0 V | 0.007965 V | 0.008046 V | 0.110043 V | 0.004553 V |
| GPIO32 SCT RAW | 34.707 | 1600 | 1841 | 1838.598 | 2121 | 10.145 count |
| GPIO33 SCT ADC Voltage | 33.559 | 1.419 V | 1.653 V | 1.650747 V | 2.075 V | 8.692 mV |
| GPIO34 Bias RAW | 36.270 | 1535 | 1840 | 1839.009 | 2011 | 9.766 count |
| GPIO35 Bias ADC Voltage | 34.602 | 1.503 V | 1.653 V | 1.651577 V | 1.779 V | 7.938 mV |

- Akım entity'sinde 1.461 sıfır, 17.652 sıfırdan farklı sayısal kayıt vardır. Bu veri tek başına fiziksel yükün açık/kapalı olduğunu kanıtlamaz.
- Akım ve Raw AC kanalları neredeyse tam aynı yayın zamanlarına sahiptir. 19.113 eşleştirilmiş kayıtta korelasyon yaklaşık 1.000'dır ve Akım = Raw AC × 24.22 bağıntısı sayısal hassasiyet sınırında sağlanır. Dolayısıyla bu iki entity bağımsız sensör teyidi değildir; aynı CT Clamp yolunun katsayı öncesi ve sonrası çıktılarıdır.
- Akım medyanı 0.192920 A, Raw AC medyanı 0.007965 V'tur. Kullanıcının fiziksel yük durumu ayrıca teyit edilmeden bu değerler gerçek yük akımı veya kesin yüksüz taban olarak sınıflandırılmaz.

### SCT ve bias kanallarının karşılaştırılması

- GPIO32 SCT RAW ile GPIO34 Bias RAW için en yakın zaman damgası eşleştirmesi (en fazla 1.2 s fark) 34.600 çift verdi. Farkın (SCT−Bias) medyanı 0 count, ortalaması −0.377 count, SD'si 12.673 count; %25–%75 aralığı −6 ile +5 count, %5–%95 aralığı −20 ile +19 count. Mutlak fark çiftlerin %51.5'inde 5 count veya altında, %65.8'inde 10 count veya altındadır.
- GPIO32 ve GPIO34 RAW medyanları sırasıyla 1841 ve 1840 count; GPIO33 ve GPIO35 voltaj medyanları her ikisi de 1.653 V'tur. Bu uzun gözlemde merkez değerler birbirine yakındır.
- RAW/voltaj entity'leri ayrı ADC okumalarıdır ve eşzamanlı değildir. Yakın zaman damgası eşleştirmesi yalnız betimleyici karşılaştırmadır; fiziksel girişlerin aynı anda aynı sinyali gördüğünü veya CT'nin primerden akım almadığını kanıtlamaz.
- GPIO32–GPIO33 yakın zamanlı kayıtlarının korelasyonu yaklaşık 0.327'dir; bu iki farklı ADC dönüşüm yolunun eşzamanlı/aynı örnekler olduğu varsayılmamalıdır.

### Dikkat çeken olay

- En yüksek akım/Raw AC yayını 2026-10-31 02:24:02.363Z (Türkiye saati 05:24:02.363) anında 2.665238 A / 0.110043 V'tur. En yüksek akım değerlerinin bir bölümü 05:23:38–05:24:02 yerel saat aralığında kümelenmiştir.
- Tepe anına en yakın GPIO32/34 RAW kayıtları yaklaşık 1843/1841 count; GPIO33/35 voltajları yaklaşık 1.649/1.653 V'tur. Ancak ADC yayınları ile CT Clamp pencereleri eşzamanlı değildir ve ADC kayıtları yaklaşık 1 s aralıklıdır. Bu nedenle tepeyi gerçek yük olayı, temas, elektriksel parazit veya yazılım/örnekleme anomalisi olarak sınıflandırmak mümkün değildir.
- Maksimum değer otomatik silinmemiştir. Ham veride aykırı olay olarak korunmuştur.

### LOG / SONUÇ / SINIR

- **LOG:** CSV Python/pandas ile okundu; satır/entity sayıları, zaman kapsamı, kayıt aralıkları, dağılımlar, en yakın zaman damgalı RAW karşılaştırması ve akım–Raw AC bağıntısı hesaplandı.
- **SONUÇ:** Gece geçmişi 10 saat 52 dakika 49 saniyeye yakın bir zaman aralığını kapsıyor ve altı entity'nin tamamında kayıt var. SCT ve bias merkez değerleri birbirine yakındır. Bununla birlikte akım/Raw AC zincirinde yaklaşık 0.193 A medyan çıktı ve 2.665 A tekil tepe bulunması, fiziksel yük durumu teyit edilmeden yüksüz taban sonucu ilan etmeyi engeller.
- **YORUM SINIRI:** HA geçmişi 200 ms pencerelerin içindeki ham ADC örneklerini, her pencerenin N/SPS debug satırlarını veya örnek bazında zamanlamayı içermez. Kayıtların varlığı yüksek hızlı örnekleme doğrulaması değildir. Bu CSV'den RMS dalga şekli, 50 Hz faz ilişkisi, harmonik, PF veya gerçek akım doğruluğu çıkarılmaz.
- **AÇIK:** Kullanıcıdan gece boyunca fiziksel primer/CT durumu (yük gerçekten bağlı mıydı, CT hangi iletkeni ve kaç turu görüyordu; kola temasın hangi saatlerde sürdüğü) teyidi bekleniyor. Varsa ESPHome DEBUG logu ayrıca incelenmeli.
- **DURUM:** Tam gece CSV analizi yapıldı; E00F-N02 deneyinin fiziksel koşul doğrulaması ve nihai yorumu açık. Deney TAMAMLANDI olarak işaretlenmedi.


## Kullanıcının gece koşulu beyanı — 2026-10-31

- **KULLANICI BEYANI:** Gece gözlemi sırasında sistemin boşta olduğu; kola temasın 00:30 Türkiye saati sonrasında devam etmediği ve akkor ampulün henüz deney yükü olarak kullanılmadığı önceki kullanıcı mesajlarında belirtildi.
- **YORUM:** 05:24:02 Türkiye saatindeki 2.665238 A tepe, bildirilen 00:30 sonrası kol temasına bağlanamaz. Sistem boşta beyanı doğruysa, 0.192920 A medyan ve diğer sıfırdan farklı akım yayınları gerçek deney yükü akımı olarak değil, yüksüz koşuldaki CT/ADC/ct_clamp zinciri çıktısı olarak ele alınmalıdır.
- **KANIT SINIRI:** Bu fiziksel koşul kullanıcı beyanıdır; CSV tek başına primer iletkendeki gerçek akımı veya CT'nin fiziksel konumunu doğrulamaz. Bu nedenle 2.665 A tepe bir anomali olarak korunur; nedeni henüz belirlenmiş değildir.


## ESPHome DEBUG takip logu — 2026-10-31

- **Kaynak:** Kullanıcının yüklediği `esp32d2-logs (13).txt`; ESPHome API üzerinden alınmış ESP32D2 logu. Dosya 146.513 bayt, 1.987 satır; kaynak SHA-256: `0839285eb41bf7aa6eb89fc5f6332a6efb7ac22be3b684b01a116825e2899033`. Ham log `docs/technical-reviews/logs/2026-10-31-e00f-n02-debug-followup.log` olarak arşivlendi.
- **Zaman:** Log başlangıcı 10:18:09.342, son satır 10:23:46.835 (cihaz log saati); CT Clamp DEBUG pencereleri 10:18:09.865–10:23:45.851. Yaklaşık 5 dk 37 sn.
- **Cihaz/yapılandırma:** ESPHome 2026.10.1, ESP32 rev3.1, `esp32d2`; Wi-Fi bağlı, API log bağlantısı başarılı. CT Clamp sample_duration 0.20 s, update_interval 2.00 s. Dört ADC kanalı GPIO32/33/34/35 için 1 s update interval, samples=1, average mode, ADC1, 12 dB. Bu logda ERROR/`[E]` yok; açılışta framework optimizasyonlarıyla ilgili üç uyarı var.
- **Pencere sayısı:** 169 CT Clamp DEBUG penceresi. `different samples` N aralığı 2.820–3.309, medyan 3.165. Logdaki SPS aralığı 14.100–16.545, medyan 15.825. Her satırda SPS = N / 0.20 s = N × 5 tam eşleşiyor. Bu nedenle N ve SPS bağımsız iki metrik değil; SPS, kabul edilen farklı örnek sayısının 200 ms pencereye oranı. Gerçek ADC dönüşüm hızı olarak yorumlanmamalı.
- **Raw AC ve akım:** Yayınlanan Raw AC 0–0.02511 V; akım 0–0.608 A. En yüksek eşleşmiş kayıt 10:22:23.917'de DEBUG Raw AC Value 0.025A / N=3.201 / 16.005 SPS; 10:22:23.973'te Raw AC 0.02511 V ve akım 0.608 A yayınlandı. DEBUG satırındaki `Raw AC Value` sayısı yayınlanan Raw AC voltajıyla eşleşiyor; satır sonundaki `A` birimi bu nedenle fiziksel akım birimi olarak kabul edilmemeli. Raw AC voltajı ve akım yine aynı CT Clamp yolunun katsayı öncesi/sonrası çıktılarıdır.
- **N/SPS ilişkisi:** Raw AC voltajı ile N/SPS arasındaki örnek korelasyonu yaklaşık 0.116; bu kısa kesitte N/SPS değişimi yüksek Raw AC değerlerini açıklamıyor. N/SPS aralığındaki değişim kendi başına hata veya örnekleme arızası kanıtı değildir.
- **Eşzamanlılık sınırı:** 10:22:23.917 tepe penceresine yakın yavaş ADC kayıtlarında SCT GPIO32 RAW 1844 count, Bias GPIO34 RAW 1846 count; voltajlar 1.654 V ve 1.660 V. Bu ADC okumaları 1 s aralıkla ve CT Clamp'in 200 ms penceresiyle eşzamanlı değil; dolayısıyla tepeyi doğrulamaz veya çürütmez.
- **Önceki gece olayıyla ilişki:** Bu takip logu 10:18–10:23 yerel cihaz saati aralığındadır; önceki HA CSV'sindeki 05:24:02 civarı 2.665238 A olayını içermiyor. Bu logdan gece tepesinin nedeni belirlenemez.
- **Yorum:** DEBUG alanları istenen N/SPS görünürlüğünü sağladı. Örnek sayısı ile SPS arasında beklenen matematiksel bağ doğrulandı; ancak N/SPS dalgalanması ile Raw AC büyüklüğü arasında bu kesitte anlamlı bir ilişki görülmedi. Ham değerler korunur; eşik, katsayı, YAML veya donanım değişikliği yapılmadı.
- **Sonraki adım:** E00F-N02 açık tutulacak. 05:24 olayını açıklamak için aynı saat aralığından DEBUG logu mevcut değilse yeni tekrar ölçümünde log ile HA zamanını eşleştirerek yakalamak gerekir. Ham dalga şekli veya eşzamanlı ADC örnekleri olmadan fiziksel neden ataması yapılmayacak.


## Kullanıcı değerlendirmesi ve sonraki test kararı — 2026-10-31

### Aykırı tepeye ilişkin değerlendirme

- **KULLANICI BİLDİRİMİ:** Evde kedi bulunuyor. Kullanıcı, gece kaydındaki tekil sıçramanın deney açısından önemli bir bulgu olarak büyütülmemesi gerektiğini belirtti.
- **YORUM:** 05:24:02.363 Türkiye saati civarındaki 2.665238 A / 0.110043 V kaydı ham veriden silinmeyecek; ancak tek başına deneyin ana sonucu veya arıza kanıtı sayılmayacak. Kedi veya kablo/sensör düzeneğine olası temas yalnızca açıklama ihtimalidir; olayın nedeni doğrulanmadı. Bu nedenle kayıt **tekil, nedeni belirlenememiş aykırı gözlem** olarak tutulur.
- **ÖNCELİK:** Analizin odağı bu sıçrama değil, yüksüz koşuldaki genel SCT/bias davranışı ve bilinen bir yük uygulandığında oluşacak tekrarlanabilir farktır.

### Sonraki test — akkor yük altında kontrollü karşılaştırma

- **Önerilen kimlik:** E00F-N03 (E00F mevcut ölçüm zinciriyle kontrollü akkor yük gözlemi). Bu adlandırma öneridir; test henüz başlatılmadı.
- **HEDEF:** Yüksüz koşulda gözlenen CT Clamp çıktısının bilinen bir akkor yük açıldığında nasıl değiştiğini, mevcut donanım ve YAML ayarlarını değiştirmeden gözlemek.
- **Yük:** İlk tercih 100 W akkor ampul. Ampulün etiketi/gerçek gücü kullanıcı tarafından doğrulanır; LED ampul bu ilk dirençli yük testinin yerine kullanılmaz.
- **Kurulum:** Mevcut ESP32D2 ve E00F yapılandırması korunur. CT yalnız tek bir yalıtılmış faz iletkenini çevrelemeli; faz ve nötr birlikte CT içinden geçirilmemeli. Tur sayısı ve fiziksel yerleşim test öncesi kayda alınır. 220–240 V bağlantı ve yük değişimi güvenli, kapalı düzenekte yapılır.
- **Koşul sırası:** (1) yük kapalı başlangıç kaydı, (2) akkor yük açık kararlı kayıt, (3) yük tekrar kapalı kayıt. Her bölümde aynı CT konumu/tur sayısı ve aynı firmware ayarları korunur. Olay saatleri not edilir; ESPHome DEBUG logu ile Home Assistant geçmişinin zamanları birlikte saklanır.
- **Kaydedilecekler:** SCT Akım ve Raw AC; GPIO32 SCT RAW, GPIO33 SCT ADC voltajı, GPIO34 Bias RAW, GPIO35 Bias ADC voltajı; cihaz DEBUG logu; yükün etiketi/gücü, CT iletkeni ve tur sayısı, koşul başlangıç-bitiş saatleri.
- **SONUÇ ÖLÇÜTÜ:** Yüksüz/açık/yüksüz bölümlerin dağılımları ve zaman grafikleri karşılaştırılır. Yük açıkken değişim görülmesi bu zincirin yüke tepki verdiğini gösterir; tek başına kalibrasyon veya ±%4 doğruluk kanıtı değildir. Yük kapatılınca başlangıç davranışına dönüş ayrıca incelenir.
- **DEĞİŞMEYECEKLER:** Bu test öncesinde katsayı 24.22, eşik/lambda, ADC pinleri, cihaz kimliği veya donanım değiştirilmez. Tekil 05:24 sıçraması nedeniyle ek filtre/threshold eklenmez.
- **SONRAKİ AŞAMA:** E00F-N03 tamamlandıktan sonra, daha hızlı ham dalga görünümü için E08 Aşama 3'teki ADC Continuous/DMA tasarımına geçilir. E08 firmware'i henüz yazılmadı; mevcut E00F One-shot/ct_clamp ile aynı ADC1 biriminde eşzamanlı çalıştırılacağı varsayılmaz.
- **DURUM:** E00F-N02 analiz ve takip logu kaydedildi; deneyin fiziksel koşul doğrulaması/nihai kapanışı ayrı tutulur. E00F-N03 planlandı, henüz uygulanmadı.


## E00F-N03 sonraki testin kısmi sonucu — 2026-10-31

Önceki bölümde planlanan 100 W akkor testi kullanıcı tarafından 10:32'de başlatıldı. İlk ESPHome DEBUG kesiti yük öncesi Raw AC medyanı 0.004 V, yük sonrası medyanı 0.019 V gösterdi. Test yük kapatma ve kapanış sonrası ölçüm alınmadığı için devam ediyor. Ayrıntı ve sınırlamalar: [E00F-N03 kısmi gözlem raporu](E00F-N03-incandescent-step-observation.md); koşul kaydı [E00F-N03 experiment.yaml](E00F-N03-experiment.yaml).
