# 2026-10-30 — E00F düşük akım / ct_clamp zinciri toplu teknik değerlendirmesi

- **Durum:** KAYNAK KOD İNCELEMESİ TAMAMLANDI; deney planı hazırlandı. Bu kayıt kapsamında firmware değiştirilmedi, derleme/flash yapılmadı ve yeni fiziksel ölçüm alınmadı.
- **Amaç:** Gemini, Google, Claude ve GitHub Copilot değerlendirmelerinde tekrar eden iddiaları tek bir kanıt hiyerarşisinde toplamak; E00F ct_clamp düşük akım davranışını mevcut E00B/E00A/E08 sırasıyla karıştırmadan incelemek.
- **Kapsam:** Eski çalışan E00F yapılandırması (esp32d2, GPIO33, ADC1, raw: false, ct_clamp 200 ms, 24.22 çarpanı, 0.35 A yayın eşiği). E08 yüksek hızlı ham edinim planı ayrı tutulur.

## 1. Yönetici özeti

Şu an katsayı 24.22'nin hatalı olduğu sonucuna varmak için yeterli kanıt yok. 100 W ve 150 W akkor gözlemleri ile iki kettle koşulunun ±%4 çevresindeki sonuçları, bu katsayının bazı yüklerde işe yaradığını gösteriyor; ancak bunlar düşük akımda algoritmanın doğru çalıştığını kanıtlamaz.

0.041 A olarak bildirilen LED akımının 0.35 A filtresi nedeniyle Home Assistant'a sıfır/ölçüm dışı yayınlanması beklenen davranıştır. Bununla birlikte 0.006 V Raw AC Value değerinin aynı LED açık ölçüm penceresine ait olduğu kanıtlanmamıştır. Bu iki sayıdan 3.5 kat hata sonucu çıkarmak şu aşamada geçerli değildir.

Kaynak kod incelemesinde doğrulanan en önemli algoritmik özellik, ct_clamp döngüsünün ardışık aynı sayısal ADC değerlerini last_value_ == value kontrolüyle atlamasıdır. Böylece hesaplanan RMS, pencere boyunca alınan bütün dönüşümlerin zaman ağırlıklı RMS'i değildir; kabul edilen farklı değerler kümesinin standart sapmasına dayanır. Bu davranış düşük sinyal genliği ve kuantizasyon koşullarında araştırılmaya değerdir; fakat BERO'daki hata büyüklüğü henüz ölçülmemiştir.

**Karar:** Katsayı, eşik, pin, cihaz kimliği, örnekleme penceresi ve çalışan YAML değiştirilmeyecek. İlk iş mevcut kanıtları eşleştirmek ve kontrollü kayıt almaktır. Gerekirse daha sonra ayrı bir teşhis firmware'i hazırlanır. E08 ham edinimi kendi planı ve ADC kaynak çakışması kurallarıyla ayrı yürütülür.

## 2. Kanıt sınıfları

### 2.1 Kaynak kodla doğrulananlar

ESPHome 2026.9.1 kaynak incelemesi:

1. ct_clamp her ölçüm penceresinin sonunda sample_squared_sum_, sample_sum_ ve num_samples_ üzerinden DC ortalamayı ve AC standart sapmasını hesaplar.
2. Döngüde source_->sample() çağrılır. NaN değerler ve last_value_ ile tam eşit olan ardışık sayısal değerler birikime alınmaz.
3. Bu nedenle num_samples_, ADC dönüşüm sayısı değil, kabul edilen farklı değer sayısıdır.
4. Raporlanan SPS, bu kabul edilen örnek sayısının pencere süresine oranıdır; fiziksel ADC dönüşüm hızı olarak yorumlanamaz.
5. ADC yapılandırmasında samples: 1, her sample() çağrısında tek dönüşüm demektir; 200 ms boyunca yalnızca bir dönüşüm alınması demek değildir.
6. sampling_mode: avg, tek dönüşümlü bu ayarda birden fazla ADC okumasını ortalamaz.
7. ESP32 ADC kaynağında raw: false kalibrasyon yolundan tam sayı mV alıp Volt'a dönüştürür. Bu yolda çıktı 1 mV adımlıdır. raw: true ise farklı birim/ölçek olan ham ADC count üretir.
8. Raw AC Value debug metni kaynakta A ekiyle yazdırılsa da kaynak sensör Volt olduğunda bu sayı akım değil RMS gerilimidir.
9. ct_clamp debug satırı pencere hesabı sonunda yazılır; mevcut satır kendi başına SSR olay kimliği, LED durumu veya PZEM okuma zamanını taşımaz.
10. ESP32 ADC1 birimi için One-shot ve Continuous sürücülerin aynı anda kullanılacağı varsayılmamalıdır. E08 firmware tasarımında mevcut ADC one-shot sensörleriyle kaynak çakışması önlenmelidir.

### 2.2 Depo ve kullanıcı loglarıyla desteklenenler

- Eski E00F YAML'da esp32d2, GPIO33, ADC1/12 dB, raw: false, 200 ms pencere, 2 s yayın aralığı, 24.22 çarpanı ve 0.35 A eşik filtresi bulunur.
- 150 W akkor için bildirilen yaklaşık 0.616 A; ESP32 yaklaşık 0.615 A ile uyumludur.
- Kettle düşük/kararlı koşulunda pens 0.637 A, ESP32 ilk 20 yayın ortalaması yaklaşık 0.656 A (+%3.0) bildirilmiştir.
- Kettle kaynama koşulunda pens 6.39 A, ESP32 22 yayın ortalaması yaklaşık 6.15 A (−%3.8) bildirilmiştir.
- 8.35 W LED için pens 0.041 A bildirilmiş; 0.35 A eşiği bu seviyeyi bastırmaktadır. Bu testte görülen ara sıra yüksek yayınlar geçerli ölçüm kabul edilmemiştir.
- Önceki bir logda 0.006 V Raw AC Value gözlemi raporlanmıştır; bu değerin LED testiyle aynı fiziksel koşula ve aynı 200 ms pencereye ait olduğu gösterilmemiştir.

Bu değerler kullanıcı tarafından sağlanan deney bildirimleridir; bağımsız laboratuvar doğrulaması değildir.

### 2.3 Henüz hipotez olanlar

- Ardışık aynı ADC değerlerini atlama davranışının düşük akımda RMS'i anlamlı ölçüde bozması.
- 1 mV kalibre edilmiş gerilim adımının 41 mA civarında önemli nicemleme etkisi yaratması.
- ADC gürültüsü/bias dalgalanmasının düşük akım ölçümüne katkısı.
- float birikim hassasiyetinin BERO sonuçlarında anlamlı hata üretmesi.
- 0.006 V değerinin yüksüz taban, LED sinyali veya geçici olay olması.

Bu hipotezlerden hiçbiri mevcut BERO loglarıyla nicel olarak doğrulanmış değildir.

## 3. Sayısal ölçek ve sınırlar

Eski E00F ölçeğinde I = 24.22 × V_AC,RMS kabul edilirse:

| Akım | Beklenen RMS gerilim |
|---:|---:|
| 0.041 A | yaklaşık 1.69 mV |
| 0.1 A | yaklaşık 4.13 mV |
| 0.2 A | yaklaşık 8.26 mV |
| 0.5 A | yaklaşık 20.64 mV |
| 6.39 A | yaklaşık 264 mV |

41 mA için beklenen sinyalin 1 mV adımlı kalibre edilmiş ADC gerilim çıktısına yakın büyüklükte olması, düşük akımın ayrıca incelenmesini gerektirir. Ancak bu tek başına ölçüm hatasının nedenini veya büyüklüğünü kanıtlamaz. ADC'nin efektif çözünürlüğü, doğrusal olmama, gürültü, bias, örneklerin zaman dağılımı ve deduplication birlikte değerlendirilmelidir.

6.39 A için yaklaşık 264 mV RMS, sinüs varsayımı altında yaklaşık 373 mV tepe genliğidir. 1.65 V bias çevresinde yaklaşık 1.277–2.023 V aralığı hesaplanır. Bu kaba hesap, 12 dB ADC üst sınıra çarpıldığı iddiasını desteklemez; gerçek dalga şekli ve donanım ölçümü olmadan clipping kesin olarak dışlanmış da sayılmaz.

## 4. Ayrıştırılmış teşhis aşamaları ve test planı

### D0 — Mevcut kanıtların eşleştirilmesi

**Amaç:** 0.006 V değerinin hangi koşula ait olduğunu belirlemek ve ct_clamp örnek sayısı değişkenliğini gerçek loglardan çıkarmak.

Her 200 ms pencere için mümkünse aynı kayıt grubunda şu alanlar çıkarılır: zaman/pencere sırası, yük/SSR durumu, Raw AC Value (Volt), N different samples, raporlanan SPS ve yayınlanan akım. N, kabul edilen farklı sayısal değer sayısıdır; SPS gerçek ADC dönüşüm hızı değildir.

**N dağılımı zorunlu çıktısı:** Pencere sayısı, N min/max, ortalama, medyan, standart sapma, p5/p95 ve frekans dağılımı; aynı özetler SPS için de verilir. Mümkünse her pencerenin Raw AC, N ve SPS üçlüsü korunur.

**Float32 sınırı:** N dağılımı float birikim şüphesini incelemek için gerekli girdilerden biridir; tek başına float32 hatasını kanıtlamaz. Gerçek ADC örnek dizisi debug satırında bulunmadığından yalnız N ile birebir yeniden oynatma yapılamaz. Gerçek quantized sample dizisi elde edilirse aynı pencere float32 ve float64 ile yeniden hesaplanabilir. Yalnız N varsa simülasyon varsayımlı duyarlılık analizi olarak etiketlenir.

**Kabul:** Mevcut logdan çıkarılabilen alanlar sayısal dağılımlarıyla raporlanır; bulunmayan alanlar “logda yok” diye işaretlenir. 0.006 V ile 0.041 A geçmişe dönük aynı pencereye bağlanmaz.

### D1 — SCT bağlı, primer akımsız taban

**Amaç:** Yüksüz halde Raw AC Value tabanını ve pencere değişkenliğini ölçmek.

- Mevcut firmware, bağlantı, 200 ms pencere ve yayın ayarları değiştirilmez.
- Yüksüz durum kararlı hâle geldikten sonra en az **30 geçerli pencere** kaydedilir. Koşul/anahtarlama değişiminden sonraki ilk 200 ms pencere dışarıda bırakılır; 30 geçerli pencere için en az 31 pencere yakalanır.
- Her pencere için Raw AC Value, N ve raporlanan SPS birlikte saklanır.
- Ortalama, medyan, standart sapma, min/max, p5/p95 ve MAD raporlanır.

**Taban yorumları — önceden hüküm değil, ayrıştırılacak seviyeler:**
- Yaklaşık 0 V: debug tabanı sıfıra yakın.
- Yaklaşık 0.006 V: önceki logda görülen seviyenin yüksüz koşulda tekrarlanıp tekrarlanmadığı.
- Yaklaşık 0.0017 V: 24.22 katsayısıyla 0.041 A'ya karşılık gelen gerilim ölçeği. Bu üçüncü değer yüksüz taban için beklenen eşik değildir; LED akımının ölçek karşılığıdır.

**Standart sapma ölçütü:** D1'de keyfî mutlak Volt sınırı konmaz. D1'in ölçülen SD'si ve medyanı ampirik yüksüz referans dağılımı olur. D2/D3 ayrışmasında D1 medyanı + 3×D1 SD karşılaştırma sınırı kullanılır; dağılım normal değilse medyan + 3×MAD ayrıca raporlanır. Bu sınır kalibrasyon veya ±%4 akım kabul sınırı değildir.

**Kabul:** En az 30 geçerli pencere, ilk geçiş penceresinin dışlanması, tüm pencere alanları ve dağılım istatistikleri bulunmalıdır. Aksi hâlde test “eksik kayıt” kalır.

### D2 — 8.35 W LED düşük akım testi

**Amaç:** D1 ile aynı ölçüm düzeninde LED yükünün yüksüz tabandan ayrışıp ayrışmadığını görmek.

- D1 ile aynı ESP32, firmware, pin, ADC ayarları ve fiziksel bağlantı korunur.
- LED kararlı ON durumuna geldikten sonra en az **30 geçerli pencere** kaydedilir; anahtarlama sonrası ilk 200 ms pencere dışarıda bırakılır ve en az 31 pencere yakalanır.
- Her pencere için Raw AC Value, N, raporlanan SPS ve yayınlanan akım saklanır.
- Pens değeri kararlı koşulda okunur; okuma zamanı ve yük durumu not edilir. PZEM varsa ayrıca yazılır; düşük akımda geçerliliği peşinen varsayılmaz.
- D1/D2 medyan, SD, MAD ve N/SPS dağılımları karşılaştırılır.

**Ayrışma ölçütü:** D2 medyan Raw AC, D1 medyan + 3×D1 SD sınırını aşıyorsa LED sinyalinin yüksüz tabandan ayrıldığı desteklenir. Normal dağılım varsayımı uygun değilse medyan + 3×MAD karşılaştırması da verilir. Aşmıyorsa “bu kurulumda tabandan güvenilir ayrışma gösterilemedi” denir; akım yok sonucu çıkarılmaz.

**Kabul:** En az 30 geçerli pencere, ilk geçiş penceresinin dışlanması, eşleşmiş D1 kurulum bilgisi, pens okuma zamanı ve pencere bazında Raw AC/N/SPS kayıtları bulunmalıdır.

### D3 — Akkor yük kontrolü ve taban etkisi

**Amaç:** Yüksüz tabanın, daha önce uyumlu saha sonucu alınan yaklaşık 0.447 A ve 0.616 A seviyelerindeki gözleme etkisini ayırmak.

- Aynı fiziksel kurulumda mevcut akkor yük test edilir. Gerçek yük/ampul etiketi ve pens okuması kaydedilir; iki akım seviyesi de mevcut değilse elde olan seviye ile test yapılır.
- Her kararlı yük koşulunda en az 30 geçerli 200 ms pencere kaydedilir; yük açıldıktan sonraki ilk pencere dışarıda bırakılır.
- Raw AC, N, SPS, yayınlanan akım ve pens okuma zamanı birlikte saklanır.
- D1 yüksüz medyanı/SD'si ile D3 yük medyanı/SD'si yan yana raporlanır.
- Ham yük Raw AC ve sqrt(max(V_load² − V_no_load², 0)) biçimindeki olası kareler farkı tahmini ayrı gösterilebilir. İkinci hesap yalnız bağımsız/ilişkisiz gürültü varsayımına dayalı tanısal modeldir; ölçülmüş sinyalden otomatik çıkarılmaz ve katsayıyı değiştirmek için tek başına kullanılmaz.
- 0.447 A ve 0.616 A için beklenen gerilim ölçekleri 24.22 katsayısıyla hesaplanır. Pens/ESP32 farkı yalnız aynı kararlı koşul ve zaman aralığı eşleşmişse yüzde sapma olarak raporlanır. ±%4 hedefi akım karşılaştırması içindir; Raw AC SD'ye uygulanmaz.

**Kabul:** D1 taban dağılımı ile D3 yük dağılımı, pencere bazında N/SPS ve eşleşmiş pens/ESP32 sonuçlarıyla karşılaştırılabilir olmalıdır.

### D4 — Ayrı RAW ADC teşhisi (yalnız kanıta dayalı tetikleyiciyle)

**Amaç:** Kalibre edilmiş Volt temsili ile ham ADC count temsilini ayrı teşhis yapılandırmasında karşılaştırmak.

D4'e yalnız aşağıdakilerden biri D0–D3 verisiyle gösterilirse geçilir:
1. N değişkenliği Raw AC sıçramalarıyla birlikte değişiyor ve mevcut log bunu açıklamaya yetmiyor.
2. Yüksüz taban ve SD ölçülmüş olmasına rağmen LED/akkor farkı açıklanamıyor.
3. 1 mV kalibre gerilim adımı şüphesi D1–D3 sonrasında hâlâ açık ve ham count verisi olmadan ayrıştırılamıyor.

- Ana E00F YAML değiştirilmez; ayrı teşhis yapılandırması hazırlanır.
- raw: true kullanılırsa çıktı ADC RAW count birimidir; akım değildir. 24.22 çarpanı ve 0.35 A eşiği bu yapılandırmaya taşınmaz.
- raw: true tek başına ardışık aynı değerleri atlama davranışını kaldırmaz ve float32 etkisini izole etmez. Deduplication etkisi için aynı gerçek örnek dizisi atlamalı/atlamasız ve float32/float64 çevrimdışı hesaplarla karşılaştırılmalıdır.
- D4, E08 ADC Continuous edinimiyle aynı anda aynı ADC1 biriminde One-shot çalıştırmaz.

**Kabul:** RAW count verisinin birimi/yapılandırması açıkça etiketlenir; ana akım sensöründen ayrı tutulur ve hangi belirsizliği test ettiği önceden yazılır.

### D5 — E08 ham edinim ve algoritma karşılaştırması

**Amaç:** Bias RAW ve SCT RAW örneklerini zaman bilgisiyle alıp aynı örnek kümesinde alternatif istatistikleri hesaplamak.

- E08 planındaki GPIO34 Bias RAW ve GPIO32 SCT RAW eşlemesi ile esp32d2 kimliği korunur.
- İlk hedef kanal başına 1 kS/s, 200 ms penceredir; gerçek hız örnek sayısı ve zaman damgasıyla doğrulanır.
- ADC Continuous/DMA ve One-shot aynı ADC1 biriminde eşzamanlı çalıştırılmaz. Eski E00F ct_clamp ile yeni Continuous edinim aynı anda çalıştırılamaz.
- Karşılaştırma gerekiyorsa **sıralı** yapılır: aynı fiziksel yük, CT tur sayısı, bias/bağlantı ve kararlı koşul korunur; önce bir edinim modu, sonra diğeri çalıştırılır. Her kayıt öncesi yük/koşul yeniden teyit edilir.
- PC'de ham örneklerden mean, bias-subtracted RMS, absolute peak, peak-to-peak ve örnek sayısı hesaplanır.

**Kabul:** Gerçek kanal hızları, pencere süreleri, ham örnek sayıları, modlar arası koşul eşitliği ve hesaplanan istatistikler raporlanır. Firmware yazılması, derlenmesi, flash edilmesi ve fiziksel ölçüm ayrı durumlar olarak kaydedilir.

## 5. Değiştirilmeyecekler

Bu teşhis planı boyunca, açık kullanıcı kararı olmadan:
- esphome.name: esp32d2 değiştirilmeyecek.
- Çalışan E00F/E00B YAML pinleri ve cihaz kimliği değiştirilmeyecek.
- E00F raw: false, 24.22 katsayısı, 0.35 A filtresi ve 200 ms penceresi değiştirilmeyecek.
- MCP3208 eklenmeyecek.
- Ölçülmemiş bir sonuç “doğrulandı” veya “tamamlandı” olarak yazılmayacak.

## 6. Raporlama şablonu

Her test kaydı şu alanları taşımalıdır:

- test_id, tarih/saat ve firmware dosyası/sürümü
- fiziksel yük ve durum (OFF/ON), mümkünse SSR BOOT_ID / EVENT_ID
- window_start ve window_end (varsa; yoksa açıkça “logda yok”)
- raw_ac_voltage_v
- n_distinct_samples ve reported_sps (SPS gerçek ADC hızı değildir)
- pencere başına published_current_a (varsa)
- her koşul için pencere sayısı; N ve SPS min/max/ortalama/medyan/SD/p5/p95; Raw AC min/max/ortalama/medyan/SD/p5/p95 ve MAD
- pens akım değeri, cihaz/okuma zamanı ve kararlı koşul notu
- PZEM akımı ve okuma zamanı (varsa; düşük akım geçerliliği ayrıca not edilir)
- anahtarlama sonrası dışlanan ilk pencere ve dışlama gerekçesi
- yorum, kanıt türü ve sınırlamalar

## 7. Sonuç ve sonraki tek adım

**Sonuç:** Kaynak kod davranışı açıklığa kavuştu; düşük akım hatasının büyüklüğü ve nedeni henüz açıklığa kavuşmadı. Katsayı eğitimi için erken. Önce D0 mevcut log eşleştirmesi, ardından aynı kurulumda D1 yüksüz ve D2 LED gözlemi yapılmalıdır.

**Sonraki adım:** Kullanıcının mevcut E00F loglarında Raw AC Value, farklı örnek sayısı ve SPS satırlarının birlikte bulunup bulunmadığını incelemek; yoksa D1/D2 için yeni kayıt protokolünü uygulamak. Bu raporun yazılması fiziksel test yapılmış anlamına gelmez.

## 8. Kaynak ve sürüm notu

- ESPHome kaynak kodu: 2026.9.1; ct_clamp_sensor.cpp, ct_clamp_sensor.h, adc_sensor_esp32.cpp, adc_sensor.h kaynak incelemesi.
- BERO mevcut dosyaları: firmware/esp32d2.yaml, firmware/README.md, experiments/E08-sct-characterization/README.md, experiments/E08-sct-characterization/stage-03-high-speed-capture.md.
- Kaynak kod incelemesi ile kullanıcı tarafından sağlanan deney logları ayrı kanıt sınıflarıdır. Simülasyon çıktıları BERO ölçümü sayılmaz.
