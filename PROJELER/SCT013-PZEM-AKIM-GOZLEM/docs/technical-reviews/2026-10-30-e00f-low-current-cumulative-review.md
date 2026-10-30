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


## 9. Son Claude/Copilot değerlendirmesi ve düşük akım sinyal ayrışması

**Kaynak/kanıt ayrımı:** Bu bölüm, kullanıcının Claude ve Copilot ile yaptığı son değerlendirmeyi, daha önce paylaşılan Google RAW denemesine ilişkin yorumları ve 2026-10-30 tarihli yeni ESPHome cihaz logunu birlikte kaydeder. Claude/Copilot yorumları bağımsız BERO ölçümü değildir; aşağıdaki cihaz logu ve pens değeri kullanıcı tarafından sağlanmıştır.

### 9.1 Düşük akım hipotezinin güncel yorumu

- Önceki raw: false LED logunda bildirilen Raw AC Value aralığı yaklaşık 0.003–0.013 V; yüksüz log aralığı yaklaşık 0.004–0.011 V idi. Aralıkların örtüşmesi düşük akım sinyalinin mevcut ölçüm zincirinde yüksüz tabandan güvenilir biçimde ayrışmayabileceği hipotezini destekler.
- Bu aralık örtüşmesi tek başına istatistiksel ayrışmazlığı kanıtlamaz. Örnek sayısı, eşzamanlı koşul bilgisi ve aynı kurulumdan yeterli sayıda pencere gerekir.
- Claude/Copilot değerlendirmesinde 1 mV kalibre gerilim adımı ana neden olarak öne çıkarılmadı; normal raw: false yolunun daha temiz, raw: true denemesinin daha gürültülü göründüğü belirtildi. Bununla birlikte raw: true denemesi veri birimini ve ölçeği de değiştirdiğinden 1 mV kuantizasyon etkisini tek başına izole etmez. Bu nedenle kuantizasyon hipotezi ana açıklama olarak desteklenmiyor, fakat kesin olarak çürütülmüş de sayılmıyor.
- Güncel en makul çalışma hipotezi, yaklaşık 40 mA seviyesindeki sinyalin mevcut SCT + bias + ESP32 ADC + ct_clamp zincirinin taban değişkenliğine göre küçük kalmasıdır. Bu, “40 mA hiçbir koşulda ölçülemez” anlamına gelmez; yalnızca mevcut düzen ve eldeki kayıtlarla güvenilir ayrım gösterilemediğini ifade eder.
- Google'ın raw: true kodu ana E00F firmware'ine alınmamıştır. Mevcut çalışan yapılandırma korunur.

### 9.2 Üç sarımlı E00F teşhis denemesi — 2026-10-30

**HEDEF:** Mevcut çalışan ct_clamp kodunu değiştirmeden primer iletkeni SCT çekirdeğinden üç kez geçirmenin yaklaşık 0.04 A düşük akım gözlemine etkisini görmek.

**LOG:**
- Kullanıcı bildirimi: SCT içinden geçen aynı iletken üç sarım yapıldı; ampul/yük yanıyordu ve pens ampermetre yaklaşık 0.04 A gösteriyordu. Yük tipi bu log kesitinde ayrıca tanımlanmadı.
- Cihaz: esp32d2; ESPHome 2026.9.1; GPIO33 / ADC1 / 12 dB; ct_clamp penceresi 0.20 s; güncelleme 2 s.
- Çalışan E00F zinciri: raw: false, 24.22 çarpanı ve 0.35 A sıfırlama eşiği korundu. Firmware değişikliği bildirilmedi.
- 12 Raw AC Value penceresi (V): 0.009, 0.006, 0.014, 0.007, 0.007, 0.011, 0.011, 0.007, 0.010, 0.008, 0.012, 0.004.
- Özet: ortalama 0.00883 V; medyan 0.0085 V; minimum 0.004 V; maksimum 0.014 V.
- Her pencerede 3,175–3,350 farklı kabul edilen örnek ve 15,875–16,750 raporlanan SPS görüldü. Bu SPS, kaynak kod incelemesinde belirtildiği gibi gerçek ADC dönüşüm hızı değildir.
- 12/12 yayınlanan akım değeri 0.000 A oldu.

**SONUÇ / HESAP:**
- Üç primer tur için amper-tur yaklaşımıyla 0.04 A × 3 = 0.12 A-tur eşdeğeri elde edilir. Bu, gerçek hat akımının 0.12 A olduğu anlamına gelmez ve sensör çıkışının tam üç kat olacağını garanti etmez.
- Logdaki en yüksek Raw AC değeri 0.014 V × 24.22 = yaklaşık 0.339 A ölçek karşılığıdır. Bu değer dahi 0.35 A filtresinin altındadır; dolayısıyla 12 pencerenin de 0.000 A yayınlaması mevcut lambda eşiğiyle tutarlıdır.
- Raw AC aralığı 0.004–0.014 V, önceki yüksüz 0.004–0.011 V ve LED 0.003–0.013 V aralıklarıyla büyük ölçüde örtüşür. Bu yeni 12 pencerelik kayıt, üç sarımın düşük akım sinyalini tabandan güvenilir biçimde ayırdığını göstermemektedir. Ancak eşzamanlı, aynı kurulumdan alınmış yeni yüksüz referans ve daha geniş pencere dizisi olmadığı için istatistiksel ayrışmazlık da kesinleştirilmiş değildir.
- Bu deneme kalibrasyon sonucu değildir; üç sarımlı düzenin ±%4 doğruluğa ulaştığı iddia edilmez.

### 9.3 Tek sarımın korunması ve tur sayısının yeri

Kullanıcının son değerlendirmesi doğrultusunda ana ölçüm düzeninde **tek sarım standart yaklaşım olarak korunacaktır**. Gerekçe, tek sarımda daha önce bildirilen orta/yüksek akım sonuçlarının hedefe yakın olmasıdır:

| Koşul | Pens / referans | SCT / ESP32 | Yaklaşık sapma |
|---|---:|---:|---:|
| 100 W akkor | 0.447 A | 0.446–0.447 A | yaklaşık 0 ila −%0.2 |
| 150 W akkor | 0.616 A | 0.615 A | yaklaşık −%0.2 |
| Kettle kaynama | 6.39 A | 6.15 A | −%3.76 |

Bunlar kullanıcı tarafından raporlanan saha karşılaştırmalarıdır; bağımsız laboratuvar doğrulaması değildir. 100 W ve 150 W sonuçları düşük/orta akım bölgesinde, kettle sonucu yüksek akım bölgesinde olumlu saha uyumunu gösterir. Tek sarımlı düzen bu nedenle mevcut referans kurulum olarak kalır. Üç sarımlı E00F denemesi düşük akım teşhis notudur; E08'in planlanmış 1/2/4 tur matrisiyle karıştırılmaz ve o planı değiştirmez.

### 9.4 Python'da bölgesel kalibrasyon yaklaşımı

**Önerilen çalışma yönü — henüz uygulanmadı:** Tek bir evrensel çarpan yerine, SCT kararlı pencere istatistikleri ile geçerli PZEM kararlı pencere referanslarından akım bölgelerine göre kalibrasyon fonksiyonları öğrenmek.

1. Önce düşük, orta ve yüksek akım bölgelerinde yeterli sayıda kararlı ve eşleştirilmiş pencere biriktirilir. PZEM proje referansıdır; kusursuz ground truth olarak kabul edilmez.
2. İlk model her bölge için basit doğrusal fonksiyonla denenebilir: I_hat = a*X + b. X, tek bir anlık okuma değil, SCT penceresinden hesaplanan seçilmiş istatistiktir.
3. Veriler doğrusal modelin yetersiz olduğunu gösterirse parçalı doğrusal fonksiyon veya başka bir model karşılaştırılır. Bölge sınırları önceden keyfî seçilmez; veri dağılımı ve kararlı pencere kapsamıyla belirlenir.
4. Eğitimde kullanılan pencerelerle aynı pencereler üzerinde elde edilen uyum, bağımsız doğrulama sonucu gibi sunulmaz. Ayrı tutulan pencerelerle de değerlendirme yapılır.
5. sensor_id, calibration_id, turn_count, firmware_version, analog ön uç ve yük profili kayıtla ilişkilendirilir. Ana düzen tek sarım olduğundan standart kayıt turn_count=1 olur; farklı turla alınan deney verisi ayrı koşul olarak etiketlenir.
6. PZEM'e göre ±%4 hedefi korunur. Sinyal yüksüz tabandan güvenilir biçimde ayrılamıyorsa Python bunu düzeltmiş gibi göstermez; ilgili bölgeyi geçersiz veya düşük güvenilirlikte işaretler.

**SONUÇ:** Araştırma odağı, fiziksel tur sayısını artırmayı ana çözüm yapmak yerine tek sarımlı donanımı koruyup Python'da bölgesel model kalibrasyonu geliştirmektir. Bu bir tasarım yönüdür; henüz eğitim verisi, model, fonksiyon katsayısı veya bağımsız doğrulama sonucu yoktur.


## 10. Gemini'nin formül ve parçalı kalibrasyon önerisi — teknik karar

### 10.1 ct_clamp matematiğinin kontrolü

Gemini'nin verdiği varyans açılımı ESPHome 2026.9.1 kaynak koduyla uyumludur:

`mean = sample_sum_ / num_samples_`

`mean_square = sample_squared_sum_ / num_samples_`

`variance = mean_square - mean * mean`

Varyans pozitifse karekök alınır; değilse AC RMS sıfır bırakılır. Kaynak kod ayrıca NaN örnekleri ve ardışık olarak aynı sayısal ADC değerlerini atlar. Bu nedenle `num_samples_`, bütün ADC dönüşümlerinin sayısı değildir; kabul edilen farklı ardışık değer sayısıdır. Logdaki SPS de bu sayının pencere süresine oranıdır.

**Terim düzeltmesi:** Formüldeki `mean`, donanımdaki yaklaşık 1.65 V bias noktasının ayrıca ölçülüp çıkarılması değildir. Her örnekleme penceresinin kendi örnek ortalamasıdır. Dolayısıyla bunu “fiziksel bias ölçümü” değil, pencere ortalamasının çıkarılması olarak adlandırmak daha doğrudur.

Kaynak: ESPHome 2026.9.1 `ct_clamp_sensor.cpp` (update/loop; mean, mean-square, variance, deduplication).

### 10.2 Model biçimi için karar

**KARAR — parçalı doğrusal model ilk model olarak doğrudan uygulanmayacak.**

Uygulama sırası:
1. İlk aday, tek sarımlı ve aynı edinim tanımına sahip kararlı SCT pencerelerinden tek doğrusal modeldir: `I_hat = a*X + b`.
2. Model artıkları (residuals) akım bölgesine göre sistematik eğilim gösterirse, yeterli veri varsa parçalı doğrusal model karşılaştırmaya alınır.
3. Parçalı model seçilirse geçişlerde süreklilik ve monotonluk kontrol edilir; bölge sınırları 0.1 V / 0.5 V gibi örnek sayılarla önceden sabitlenmez, veriden seçilir.
4. Daha karmaşık model, yalnız eğitim verisi hatasını düşürdüğü için seçilmez. Ayrı tutulan kararlı pencerelerde karşılaştırmalı performans ve model karmaşıklığı birlikte değerlendirilir.
5. PZEM geçerli ve kararlı proje referansıdır; kusursuz ground truth değildir. ±%4 hedefi PZEM'e göre raporlanır.

### 10.3 Sinyal geçerlilik kapısı, sıfır akımdan ayrılacak

Gemini'nin `RMS < noise threshold => 0 A` dalı doğrudan model çıktısı olarak kabul edilmeyecek.

- Yüksüz tabandan güvenilir biçimde ayrışmayan pencere, otomatik olarak `0 A` ilan edilmez; `INVALID`, `BELOW_DETECTION` veya `LOW_CONFIDENCE` gibi ayrı kalite durumu ile işaretlenir.
- Gerçek sıfır akım, düşük ama algılanamayan akım ve geçersiz sinyal birbirinden ayrılmalıdır.
- Gürültü/ayrışma sınırı yüksüz kayıt dağılımı ve yük koşulu kayıtlarından deneysel olarak belirlenir; keyfî RMS eşiği atanmaz.
- Bu kapı, regresyon modelinin dışında bir veri-kalitesi/algılanabilirlik kararıdır. Model, tabandan ayrılamayan sinyalden akım bilgisi üretemez.

### 10.4 Model girdisi: ct_clamp RMS ile E08 ham RMS aynı kabul edilmeyecek

E00F `ct_clamp` RMS'i, ESPHome'un One-shot ADC örneklerinden ve ardışık aynı sayısal değerleri atlayan döngüsünden üretilir. E08 ise planlandığı gibi zaman bilgili ham ADC örneklerini alıp Python'da pencere istatistikleri üretecektir. Örnek kümesi, örnekleme davranışı ve hesaplama yolu farklı olabileceğinden bu iki RMS serisi aynı özellik gibi birleştirilmeyecek.

T006/Python eğitiminde hangi SCT özelliğinin kullanılacağı, ilgili edinim yolunun gerçek kayıtları görüldükten sonra seçilir. E08 ham örnekleri kullanılırsa RMS tanımı aynı örnek kümesinden, pencere ortalaması çıkarılarak ve örnek sayısı/zaman bilgisi korunarak hesaplanır. `ct_clamp` verisi ayrı kaynak/özellik olarak tutulabilir; ham RMS ile eşdeğer olduğu varsayılmaz.

### 10.5 Gemini'ye yöneltilecek ek soru gereği

Bu incelemede Gemini'ye doğrudan mesaj gönderilebilen bir bağlantı bulunmadığından soru iletilmedi. Teknik karar, ESPHome 2026.9.1 kaynak kodu ve BERO'nun mevcut veri mimarisi üzerinden verildi. Gemini'nin önerisindeki temel formül kabul edildi; modelin doğrudan parçalı uygulanması ve gürültü altı sinyalin sıfır akım sayılması kabul edilmedi.

**Durum:** Tasarım kararı kaydedildi; Python kodu, eğitim verisi, model katsayıları ve fiziksel test henüz yoktur.


## 11. Gemini'nin son değerlendirmesi — eleştirel inceleme ve karar

### 11.1 Ardışık aynı ADC kodlarının atlanması: kabul

ESPHome ct_clamp döngüsünde last_value_ == value ise örnek atlanır. Bu işlem yalnızca örnek sayısını düşürmez; aynı ADC kodunun zaman içinde uzun süre tekrarlandığı run'ları tek temsile indirger. Böylece sample_sum_ ve sample_squared_sum_ üzerinden hesaplanan dağılım, sabit aralıklı bütün ADC okumalarının zaman ağırlıklı dağılımıyla aynı olmak zorunda değildir.

Bu nedenle E00F RMS sonucu, bütün ADC dönüşümlerinin klasik zaman ağırlıklı RMS'i olarak yorumlanmayacak. Sapmanın büyüklüğü mevcut özet logdan hesaplanamaz; aynı sinyalin zaman bilgili ham ADC örnekleriyle karşılaştırma gerekir.

### 11.2 Bias ofseti ve sayısal hassasiyet: kısmen kabul

Varyansın E[x²] - E[x]² biçiminde hesaplanması, sabit bir DC ofseti ideal matematikte giderir. Bu nedenle 1.65 V bias değerindeki sabit/sıcaklık kaynaklı küçük kayma tek başına otomatik olarak sahte AC RMS üretir denemez.

Buna karşılık pencere içinde değişen bias, düşük frekanslı dalgalanma veya başka bir ofset hareketi pencere varyansına katkı yapabilir. Ayrıca birbirine yakın iki büyük sayının farkından küçük varyans elde edildiği için kayan nokta sayısal hassasiyeti incelenmeye değer bir hipotezdir. Bu etkinin BERO'daki büyüklüğü ham örnekler ve aynı algoritmanın kontrollü yeniden oynatımı olmadan doğrulanmış değildir.

### 11.3 Tek doğrusal modelin yetersizliği: kabul, ölçüt genişletildi

Artıkların SCT özelliğine göre sistematik eğrilik göstermesi tek doğrusal modelin yetersizliğine işaret edebilir. Ancak tek bir U biçimli grafik tek başına model değiştirme kararı değildir. Artıkların akım aralığı, yük profili, sensör kimliği ve bağımsız olay/oturum bazında tekrarlanabilirliği incelenir.

Sıfırdan geçmeyen I = aX + b modelinin sıfır girdide negatif veya pozitif çıktı vermesi de tek başına doğrusal modelin yetersizliğini kanıtlamaz; sıfır/algılanabilirlik davranışı modelin geçerlilik alanı ve ayrı kalite kapısıyla ele alınır.

### 11.4 Parçalı model ve çapraz doğrulama: kısmen kabul

Parçalı model gerekirse süreklilik ve pozitif eğim/monotonluk kontrol edilir. Ancak en fazla iki bölge sınırı şimdiden zorunlu kural yapılmayacak; bölge sayısı ve eşikler veriyle gerekçelendirilecek.

Mevcut yük noktaları ve koşul çeşitliliği sınırlıdır. Aynı olayın ardışık pencerelerini rastgele eğitim ve doğrulama kümelerine bölmek veri sızıntısı yaratabilir. Veri yeterli olduğunda bölme, mümkün olduğunca bağımsız yük olayı/oturum veya tekrar grupları üzerinden yapılır. Bugünkü kayıtlar kapsamlı cross-validation için yeterli kabul edilmez.

### 11.5 Gürültü varyans oranı: 1.0–1.2 önerisi reddedildi

variance_window / variance_noise oranı tanımlayıcı bir özellik olarak incelenebilir; ancak 1.0–1.2 aralığı BERO verisinden türetilmediği için karar eşiği olarak kullanılmayacak. Üstelik E00F'nin ardışık aynı ADC kodlarını atlaması, yük ve yüksüz varyanslarını zaman ağırlığı bakımından farklı biçimde etkileyebilir.

Önce aynı edinim yöntemi, aynı örnekleme/işleme yolu ve karşılaştırılabilir pencerelerle yüksüz taban ve yük koşulu dağılımları toplanır. Eşik, ancak bu dağılımlar ve yanlış kabul/ret davranışı incelendikten sonra belirlenir. Belirsiz pencereler otomatik sıfır veya otomatik pozitif akım sayılmaz; kalite durumu olarak korunur. Belirsiz örnekleri regresyon eğitimine ağırlık vererek sokmak varsayılan yöntem değildir; önce referans etiketi ve sinyal ayrışması güvenilir olmalıdır.

### 11.6 Model girdisi: E00F ve E08 ayrımı korunuyor

Gemini'nin mevcut esp32d2 E00F akışında kullanılabilir özelliğin ct_clamp çıktısı olduğu yönündeki tespiti mevcut firmware bağlamında doğrudur. Ancak bu, BERO'nun gelecekteki eğitim girdisini bugünden ct_clamp ile sınırlamaz. E08'in planlanan ham ADC edinimi ayrı bir veri yoludur; Python'da ham örneklerden özellikler gerçek kayıtlar elde edilince ayrıca değerlendirilebilir.

E00F ct_clamp özelliği ve E08 Python ham-örnek özelliği aynı tanım/sampling population gibi birleştirilmeyecek. Hangi yol T006 modeline girecekse eğitim verisinin tamamında aynı özellik tanımı ve izlenebilir edinim kimliği korunur.

### 11.7 SNR < 1 yorumu: fiziksel sınır kabul, mutlak ifade düzeltiliyor

Sinyal gürültüden güvenilir biçimde ayrılamıyorsa tek pencereye dayanarak güvenilir akım büyüklüğü tahmin edilemez; modelin gürültüyü akım gibi uydurmasına izin verilmeyecek. Bu konuda Gemini'nin temel uyarısı kabul edilir.

Ancak SNR < 1 ifadesi, hiçbir istatistiksel bilgi bulunamayacağı anlamına gelmez. Tek pencere zayıf olsa da yeterli sayıda bağımsız/tekrarlı pencerenin birlikte değerlendirilmesi dağılımlar arasında ayrışma gösterebilir. Böyle bir ayrışma gösterilse bile tek pencere tahmininin belirsizliği ayrıca raporlanmalıdır.

KARAR: Ayrışma kanıtı varsa tahmin; ayrışma yetersizse akım değeri yerine kalite/belirsizlik durumu. Gerçek 0 A, algılanabilir düşük akım, algılanamayan düşük akım ve geçersiz veri birbirinden ayrılacaktır. Yazılım fiziksel olarak taşınmayan bilgiyi üretemez.

### 11.8 Son karar özeti

- Zaman ağırlığı/dedup sorunu: KABUL; etkisi ham örnekle henüz ölçülmedi.
- Sabit bias kaymasının doğrudan sahte RMS yaptığı iddiası: KABUL DEĞİL; dinamik bias ve kayan nokta hassasiyeti araştırma hipotezi.
- Artık eğriliği: KABUL; tek başına karar ölçütü değil.
- En fazla iki parçalı bölge: ŞİMDİLİK KABUL DEĞİL.
- Varyans oranı 1.0–1.2 eşiği: RED; veri temelli eşik henüz yok.
- E00F ct_clamp girdisi: MEVCUT AKIŞ İÇİN KABUL; gelecekte E08 ham Python özelliklerini dışlamaz.
- SNR < 1'de güvenilir tek-pencere akım tahmini yapılamayacağı: KABUL; tekrarlı pencere istatistiğinin bilgi taşıyamayacağı iddiası KABUL DEĞİL.

Durum: Bu bir teknik karar/inceleme kaydıdır. Yeni veri toplanmadı, firmware veya Python kodu değiştirilmedi, model eğitilmedi ve fiziksel test yapılmadı.


## 12. Google değerlendirmesi — kaynak kod ve istatistik açısından denetim

### 12.1 raw:false ve 1 mV basamağı: sorun gerçek, hata yüzdesi kanıtlanmadı

ESPHome ESP32 ADC kalibre yolunda ham ADC kodunu kalibrasyon API'siyle tam sayı mV'ye dönüştürür ve Volt cinsinden float döndürür. Bu nedenle kaynak örnek değerinin 1 mV basamaklı olması doğrudur. BERO'daki 24.22 A/V katsayısıyla 0.041 A için yaklaşık 1.69 mV RMS hesabı aritmetik olarak doğrudur.

Bununla birlikte 1 mV / 1.69 mV oranı, RMS akım hatasının doğrudan yüzde 59 veya Google'ın ileri sürdüğü yaklaşık yüzde 50 olduğu anlamına gelmez. Kuantizasyonun RMS'e etkisi dalga tepe genliği, ADC kod/bias hizası, ADC gürültüsü ve örneklerin zaman dağılımına bağlıdır. Sonuç: düşük akımda önemli kuantizasyon riski **KABUL**; belirli hata yüzdesi **HENÜZ KANITLANMADI**.

### 12.2 raw:true + multiply:0.85 önerisi: reddedildi

Google'ın 0.85 çarpanı için kaynak, birim veya ESP32'ye özgü kalibrasyon kanıtı yoktur. ESPHome dokümanında 12 dB için verilen genel eski ölçek örneği 0.00095238 V/count'tur; ESPHome bu yöntemin çipler arasında değişebileceğini ve genel olarak kalibre edilmiş gerilim yolunun tercih edilmesini belirtir. Bu genel çarpan da BERO kartı için doğrulanmış kalibrasyon katsayısı değildir.

Daha kritik nokta: ct_clamp, loop() içinde ADC kaynağının sample() metodunu doğrudan çağırır. ADC sensörünün normal publish/filter zincirindeki filters işleminin ct_clamp'in doğrudan sample() çağrısından önce uygulandığı varsayılamaz. Dolayısıyla ADC sensörüne filters: - multiply: 0.85 eklemek, ct_clamp'e float ölçeklenmiş voltaj vereceği anlamına gelmez. Ham count dönüşümünün gerçekten ct_clamp örnekleme yoluna uygulanması için kaynak/uygulama mimarisi ayrıca tasarlanmalı ve doğrulanmalıdır.

raw:true ham count yolunu kullanmak, ADC'nin fiziksel çözünürlüğünü artırmaz; kalibre edilmiş mV dönüşümündeki tam sayı mV basamağını atlar ama ham ADC'nin kendi kod çözünürlüğü, doğrusal olmama, gürültü ve çip değişkenliği devam eder. 0.85 çarpanlı YAML denemesi yapılmayacak.

### 12.3 SNR ve gürültü RMS birleşimi: koşullu kabul

Vsignal ve Vnoise bağımsız/ilişkisiz ve sıfır ortalamalı bileşenlerse varyansları toplanır; toplam RMS kareler toplamının karekökü olur. Bu bağıntı düşük sinyalde taban gürültüsünün etkisini açıklamak için yararlıdır. Ancak E00F'nin ardışık aynı değerleri atlayan örnekleme yöntemi nedeniyle bu ilişkinin BERO'daki sayısal etkisi ayrıca ölçülmelidir.

Noise floor'un varlığı tek başına model eğrisinin asla sıfıra yaklaşamayacağını kanıtlamaz. Gürültü tabanı ve belirsizliği uygun, aynı edinim yoluyla toplanmış veriyle modellenebilir. Gürültü çıkarımı da tabanın kararlılığı ve sinyal-gürültü bağımsızlığı gösterilmeden uygulanmayacak.

### 12.4 Dedup, zamanlama ve CPU jitter: kısmen kabul, iddia düzeltiliyor

Ardışık aynı sayısal değerleri atlama, zaman ağırlıklı örnek dağılımını değiştirebilir. Ancak bunun dalga biçimini fiziksel olarak üçgen/kare şekle dönüştürdüğü ifadesi doğru değildir. Algoritma, tekrarları sıkıştırılmış ve zaman damgası taşımayan kabul edilmiş değerler kümesinin standart sapmasını hesaplar.

ESPHome ct_clamp kodu yüksek frekanslı loop isteği başlatır; sabit zaman aralıklı ADC örnekleme zamanlayıcısı tanımlamaz. Logdaki N ve SPS, kabul edilen farklı değer sayısı ve bunun pencereye oranıdır; gerçek ADC dönüşüm hızı değildir. 8–11 kS/s fiziksel dönüşüm hızı veya CPU jitter ölçümü olarak kullanılamaz. CPU jitter miktarı mevcut logdan çıkarılamaz.

200 ms, nominal 50 Hz'de 10 periyoda karşılık gelir; ancak şebekeye faz senkronizasyonu anlamına gelmez. Gerçek frekans ve örnekleme zamanlaması ayrı ölçülmelidir.

### 12.5 Z > 3 kuralı: reddedildi

Normal dağılım altında yaklaşık %99.73 değeri, gözlemlerin ±3 sigma aralığında kalma olasılığıdır; Z > 3 gözleminin gerçek yük olma olasılığı değildir. Tek taraflı Z > 3, ancak yüksüz dağılımın uygunluğu ve durağanlığı varsayımı altında yanlış alarm olasılığına ilişkin bir eşik olabilir. Yükün gerçek olma olasılığını hesaplamak için yük ve yüksüz koşullarının dağılımları, ön olasılıklar ve karar maliyetleri gerekir.

Beş dakikalık taban kaydı da kanıtlanmış yeterlilik süresi değildir. T005/E01 mevcut sırası korunacak; kayıt süresi ve tekrarlı oturum gereksinimi gerçek dağılım ve kararlılık incelendikten sonra belirlenecek. Z > 3 otomatik yük tespiti veya Z <= 3 otomatik sıfır akım kuralı olarak kullanılmayacak.

### 12.6 Residual analizi ve bölgesel eşikler: yöntem kabul, Google'ın çıkarımı reddedildi

Residual plot ve akım aralıklarına göre hata özeti, T006 model değerlendirmesinde kullanılabilecek tanı araçlarıdır. Ancak <1 A, 1–3 A ve >3 A sınırları BERO verisinden türetilmemiştir. Kettle'da bildirilen yaklaşık −%3.8 fark, mevcut ±%4 kabul sınırının içindedir; tek başına tek doğrusal modelin başarısızlığını göstermez. Mevcut yük noktaları ve eşleşmiş kararlı pencere sayısı bölgesel model kararı için yeterli değildir.

### 12.7 Nihai karar

- raw:false 1 mV basamağı: **KABUL**; düşük akım için risk, hata yüzdesi ölçülmedi.
- raw:true + multiply:0.85: **RED**; çarpan temelsiz ve ADC filters zincirinin ct_clamp sample() çağrısına uygulanacağı varsayımı yanlış.
- RMS gürültü birleşimi: **KOŞULLU KABUL**; bağımsız bileşen varsayımı ve BERO edinim yöntemi etkisi dikkate alınmalı.
- Dedup zaman ağırlığı: **KABUL**; dalga şeklinin kare/üçgen olduğu iddiası **RED**.
- 8–11 kS/s gerçek ADC hızı ve CPU jitter sonucu: **RED**; log yalnız farklı kabul edilen değer sayısını gösterir.
- Z > 3 = %99.7 gerçek yük: **RED**.
- Residual analizi: **KABUL**; Google'ın akım bölgeleri ve kettle örneğinden model yetersizliği çıkarımı **RED**.
- Mevcut E00F YAML, katsayı, eşik, pin ve cihaz kimliği değiştirilmeyecek. E00A/E00B deney sırası korunacak. T006 model analizi, ilgili görev sırası geldiğinde ve eşleşmiş kararlı veri oluştuğunda yapılacak.

**Durum:** Bu bölüm kaynak kod/doküman incelemesi ve matematiksel değerlendirmedir. raw:true denemesi, YAML değişikliği, derleme/flash, yeni ADC kaydı, Python residual analizi veya fiziksel test yapılmadı.

**Kaynaklar:** [ESPHome ADC dokümantasyonu](https://esphome.io/components/sensor/adc/), [ESPHome ct_clamp kaynak kodu](https://api-docs.esphome.io/ct__clamp__sensor_8cpp_source), [ESPHome ct_clamp dokümantasyonu](https://esphome.io/components/sensor/ct_clamp/), [ESPHome ESP32 ADC uygulaması](https://github.com/esphome/esphome/blob/dev/esphome/components/adc/adc_sensor_esp32.cpp).


### 12.8 Kullanıcı düzeltmesi — raw:true daha önce denendi ve sonuç kötüleşti

Önceki bölümde raw:true yolunun yalnızca öneri olarak yeniden ele alınması gerektiği izlenimi oluşmamalıdır. Kullanıcı, BERO'da raw:true yolunun daha önce denendiğini ve raw:false mevcut akışa göre daha kötü/gürültülü sonuç verdiğini hatırlattı. Bu, önceki oturum kaydında da raw:true denemesinin daha gürültülü göründüğü şeklinde yer alıyordu; bu deneme 1 mV kuantizasyonunu tek başına izole etmemişti.

**Düzeltilmiş karar:** raw:true mevcut aşamada yeni deney adayı değildir; daha önceki olumsuz kullanıcı test sonucu nedeniyle yeniden açılmayacaktır. Google'ın eklediği multiply:0.85 önerisi de kaynak/kalibrasyon temeli ve doğru sample() entegrasyon yolu gösterilmediğinden kabul edilmez. Önceki raw:true denemesinin tam olarak 0.85 çarpanıyla yapıldığına dair bu kayıtlarda kanıt yoktur; bu iki şeyi aynı deneymiş gibi yazmıyoruz.

Bu düzeltme önceki raw:true deney sonucunu karar gerekçesine ekler. Mevcut YAML değiştirilmez; raw:true tekrar testi planlanmaz. raw:false 1 mV basamağının gerçek düşük-akım hatasına etkisi ise ayrı ve henüz cevaplanmamış teknik sorudur.


## 13. E00F sıfır-yük ct_clamp logu — 2026-10-30

### 13.1 Kaynak ve edinim ayarları

- **KANIT:** Kullanıcının paylaştığı cihaz logu; ham metin [arşivlendi](logs/2026-10-30-e00f-zero-load-ct-clamp.log).
- Cihaz: ESP32 rev3.1, ESPHome 2026.9.1; GPIO33 / ADC1_CH5, 12 dB attenuation.
- ADC: raw=false, samples=1, sampling_mode=avg.
- ct_clamp: 200 ms pencere, 2 s yayın aralığı.
- Akım dönüşümü: multiply 24.22; ardından x < 0.35 A => 0 A yazılım eşiği.
- Kayıtta 180 ct_clamp penceresi var; zaman aralığı yaklaşık 22:13:14.620–22:19:12.625.
- Debug satırındaki Raw AC Value birim eki A olarak görünür; ancak multiply uygulanmadan önceki büyüklük bu yapılandırmada ADC kaynak sensörünün Volt cinsinden pencere RMS/standart sapma değeridir. Bu nedenle aşağıdaki özet V cinsinden yorumlanır.

### 13.2 Logdan hesaplanan özet

| Ölçüt | Sonuç |
|---|---:|
| Pencere sayısı | 180 |
| Raw AC minimum / maksimum | 0.000 / 0.032 V |
| Raw AC ortalaması | 0.00562 V |
| Raw AC medyanı | 0.005 V |
| Pencereler arası standart sapma | 0.00500 V |
| %90 yüzdelik | 0.010 V |
| %95 yüzdelik | 0.01205 V |
| %99 yüzdelik | 0.02742 V |
| Yayınlanan 0.000 A | 173 / 180 |
| Yayınlanan sıfır dışı değer | 7 / 180 (%3.89) |

Sıfır dışı yayınların ham logdaki karşılıkları:

| Raw AC (V, yaklaşık) | Yayınlanan akım |
|---:|---:|
| 0.029 | 0.692 A |
| 0.017 | 0.417 A |
| 0.025 | 0.613 A |
| 0.017 | 0.412 A |
| 0.032 | 0.770 A |
| 0.027 | 0.660 A |
| 0.015 | 0.353 A |

**SONUÇ — KULLANICI KOŞULU YÜKSÜZ OLARAK BİLDİRDİ:** Bu kayıt, mevcut E00F zincirinde sıfır-yük durumunda 7/180 pencerede sıfır dışı akım yayınlandığını gösteriyor. Bunlar bu test koşulunda yanlış pozitif akım yayınlarıdır. Ham log tek başına sıçramaların CT manyetik gürültüsünden mi, ADC/analog girişinden mi, EMI'den mi veya edinim algoritmasından mı kaynaklandığını ayıramaz.

Logdaki kabul edilen farklı örnek sayısı 2446–3231, raporlanan SPS 12230–16155 aralığındadır. Bu sayılar ct_clamp dedup filtresinden sonra kabul edilen farklı ardışık değerlerin sayımıdır; fiziksel ADC dönüşüm hızı olarak yorumlanmayacaktır.

### 13.3 40 mA hedefi ile karşılaştırma

- **ÜRETİCİ BELGESİ:** SCT013-030 nominali 30 A RMS girişte 1 V RMS çıkıştır. Nominal hassasiyet yaklaşık 33.3 mV/A'dır; 40 mA için nominal çıkış yaklaşık **1.33 mV RMS** olur. Üretici PDF'si ±1% doğruluk ve ≤0.2% lineerlik yazar, fakat 40 mA gibi alt uçta doğruluğun garanti edildiği minimum akım açıkça belirtilmez.
- **MEVCUT E00F KALİBRASYONU:** 24.22 A/V katsayısı kullanıldığında 40 mA'ya karşılık gelen giriş büyüklüğü yaklaşık **1.65 mV RMS** olur. Bu, nominal CT oranından ayrı tutulmalıdır; 24.22 A/V mevcut yazılım katsayısıdır.
- **ÖLÇÜM:** Bu yüksüz logun Raw AC medyanı 5 mV, ortalaması 5.62 mV ve pencereler arası standart sapması yaklaşık 5 mV'dur. 40 mA için hesaplanan 1.33–1.65 mV hedef sinyal bu yüksüz dağılımdan küçük kalmaktadır.
- **HESAP / VARSAYIM:** Sinyal ve yüksüz bileşenler ilişkisiz kabul edilip RMS kareleri üzerinden birleşirse, 5 mV taban ile 1.65 mV sinyalin toplamı yaklaşık 5.26 mV olur; artış yalnızca 0.26 mV'dur. Bu, logdaki 1 mV gösterim basamağından ve yaklaşık 5 mV pencere saçılmasından küçüktür. Bu hesap sinyalin bu edinim zincirinde güvenilir biçimde ayrışmasının zor olduğunu gösterir; bağımsız bileşen varsayımı ayrıca doğrulanmamıştır.
- **YAZILIM KAPISI:** 0.35 A lambda eşiğinin kaynak girişindeki karşılığı 0.35 / 24.22 = 0.01445 V civarındadır. 40 mA hedefi mevcut katsayıyla yaklaşık 1.65 mV olduğundan bu eşik tarafından bilerek bastırılır. Bu nedenle mevcut E00F YAML ile 40 mA'nın 0.000 A yayınlanması, sensörün fiziksel olarak hiç sinyal üretmediğini tek başına kanıtlamaz; yazılım eşiği zaten 350 mA altını sıfırlamaktadır.
- **KARAR:** 0.35 A eşiği bir sensör minimumu değil, E00F'nin yazılım filtresidir. Bu logdan 40 mA ölçülebilir/ölçülemez şeklinde mutlak CT hükmü çıkarılmayacak; ancak mevcut E00F zincirinde 40 mA'nın yüksüz tabandan ayrıştığına dair kanıt yoktur.

## 14. Dış kaynak ve GitHub depo taraması — düşük akım çözümleri

### 14.1 Üretici dokümanları ve topluluk ölçüm deneyimi

- **ÜRETİCİ BELGESİ:** YHDC SCT013-030 PDF'si 30 A RMS / 1 V RMS, ±1% accuracy ve ≤0.2% linearity değerlerini verir; gerilim çıkışlı tipte örnekleme/burden direncinin sensör içinde olduğunu gösteren bağlantı şeması vardır. PDF, 40 mA alt-uç doğruluk garantisini açıkça tanımlamaz. Bu nedenle 30 A/1 V sensörde harici burden direncini büyütmek geçerli bir çözüm olarak önerilmeyecek.
- **ÜRETİCİ BELGESİ:** YHDC ürün ailesinde 5 A/1 V ve 10 A/1 V gibi daha düşük tam ölçekli varyantlar da bulunur. Nominal hassasiyetleri sırasıyla 200 mV/A ve 100 mV/A'dır; 40 mA için teorik çıkışları 8 mV ve 4 mV olur. Bunlar 30 A/1 V modelin 1.33 mV çıkışından daha yüksek sinyal üretir; ancak 40 mA'da doğruluk garantisi olduğu anlamına gelmez.
- **KULLANICI RAPORU / TOPLULUK:** OpenEnergyMonitor tartışmasında 50 A SCT013 modelinin doğruluk aralığının 10–120% (5–60 A) olduğu, 30–100 mA için bu CT'nin uygun olmadığı belirtilmiş; daha düşük aralıklı CT veya primeri çok tur geçirmek önerilmiştir. Bu yorum 50 A model hakkındadır; BERO'daki 30 A/1 V model için üretici garantisi gibi genellenmeyecek.
- **KULLANICI RAPORU / TOPLULUK:** Aynı toplulukta çok turlu primer kullanımının efektif akım aralığını düşürdüğü, fakat üst akım kapasitesini de tur sayısı oranında azalttığı açıklanır. BERO'nun önceki üç tur denemesi yüksüz tabanla örtüşen 4–14 mV pencereler verdiği için 40 mA ayrışma çözümü olarak doğrulanmış değildir.
- **TEKNİK ÖRNEK:** Analog Devices eğitim sayfasında farklı bir 15 mV/A akım probu 5 primer turla 75 mV/A'ya çıkarılmış; 35–45 mA tepe akımlı sinyal ham halde gürültü içinde zor görülmüş, dijital ortalama/iz ortalamasıyla daha net gösterilmiştir. Bu farklı prob ve ölçüm cihazı örneğidir; SCT013-030/ESP32 performans kanıtı değildir.

### 14.2 GitHub depolarındaki uygulama kalıpları

GitHub açık kaynak kodu/dokümantasyon araması yapıldı; GitHub Copilot tarafından BERO koduna değişiklik yaptırılmadı.

1. **rb-amp/rbamp-esp-idf — CT seçimi:** Dokümantasyon, beklenen maksimum akımı karşılayan en küçük SCT013 modelini seçmeyi; aşırı büyük CT'nin düşük akım çözünürlüğünü düşürdüğünü belirtir. Sorun giderme notunda 100 A CT ile yaklaşık 0.2 A lambanın gürültü tabanına yaklaşabileceği yazılıdır. Ayrıca düşük akım için 5 A CT ve yüksek akım için 30 A/100 A CT'yi ayrı kanallarda kullanıp ana tarafta geçiş yapma örüntüsü sunulur. Bu, depo dokümantasyonunda önerilen mimaridir; 40 mA'da ölçüm doğruluğu kanıtı değildir.
2. **SparkFun/SparkFun_ADE7953_Arduino_Library — yüksüz taban:** Kütüphane yüksüz durumda çoklu RMS register örneklerinden baseline ortalaması alır ve sqrt(reading² - baseline²) işlemiyle kareler alanında çıkarır. Kod ayrıca PGA kazancı ve analog yüksek geçiren filtre kullanır. Bu yöntem ADE7953 donanımına özgüdür; ESPHome ct_clamp zincirine doğrudan kopyalanmayacak. BERO açısından değerli nokta, taban ölçümünün ayrı ve açık bir kalibrasyon aşaması olmasıdır.
3. **danpeig/ESP32EnergyMonitor — edinim/kalibrasyon:** ESP32 ve SCT013 kullanan örnek projede akım sensörü için ayrı kalibrasyon aracı, referans ampermetreyle katsayı belirleme ve 1 V çıkışlı CT'de harici burden direnci eklememe yaklaşımı vardır. Proje 100 A/50 mA akım çıkışlı CT örneğini esas alır; BERO'nun 30 A/1 V CT'sine doğrudan devre kopyası değildir.
4. **dardhal/ESP32-ADS1115-CT-Power-Measurement — harici ADC uyarısı:** Depo sahibi ADS1115 continuous mode ile ESPHome ct_clamp kullanırken yavaş/güvenilmez ölçümler bildirmiştir. Harici ADC tek başına çözüm değildir; örnekleme modu, veri hızı ve yazılım entegrasyonu birlikte doğrulanmalıdır.

### 14.3 BERO'daki yardımcı sensörler açısından not

- **HESAP:** SCT013-100 100 A/1 V nominal hassasiyeti 10 mV/A olduğundan 40 mA'da yaklaşık 0.4 mV üretir; 40 mA için 30 A/1 V modelden de daha zayıf bir gerilim sinyali verir.
- **ÜRETİCİ BELGESİ:** ZMCT103C çıplak CT datasheet'i 5 A primerde 5 mA sekonder ve 50 Ω burden ile 250 mV verir; 40 mA'da yaklaşık 2 mV hesaplanır. Aynı dokümandaki ≤0.2% linearity aralığı 5–120% olduğundan 40 mA, 5 A nominalin %0.8'i ile bu belirtilen aralığın altındadır. BERO'daki Ayzek modülünün gerçek burden/ön uç devresi ayrıca doğrulanmadan çıplak CT hesabı modül çıkışı kabul edilmeyecek.
- **ÜRETİCİ BELGESİ:** ACS712-05B için nominal hassasiyet 185 mV/A'dır; 40 mA'da yaklaşık 7.4 mV değişim beklenir. Allegro datasheet'i 47 nF filtre koşulunda 2 kHz bant genişliğinde 21 mV peak-to-peak gürültü verir. Bu nedenle ACS712-5A da yalnızca daha yüksek hassasiyetli olduğu için otomatik olarak 40 mA çözümü sayılmayacak; filtre/bant genişliği ve modül gürültüsü birlikte incelenecek.

### 14.4 BERO için sonuç ve öncelik

1. Mevcut 30 A/1 V SCT013-030, 40 mA'yı nominal olarak yalnızca 1.33 mV RMS seviyesinde temsil eder. E00F'nin yüksüz logunda medyan 5 mV RMS kaynak tabanı ve 5 mV pencere saçılması görülmüştür. Bu nedenle mevcut zincirde 40 mA güvenilir biçimde ayrışmıyor.
2. E00F'deki 0.35 A yazılım eşiği 40 mA'yı tasarım gereği sıfırlar. Mevcut YAML değiştirilmeyecek; bu eşik davranışı ölçüm donanımının minimum akım kabiliyetiyle karıştırılmayacak.
3. İlk çözüm adayı 30 A CT'nin burden direncini değiştirmek değildir; bu model gerilim çıkışlı ve burden sensör içindedir.
4. Düşük akım gerçekten proje gereksinimiyse, önce daha düşük nominal akım CT'nin aynı koşulda taban/sinyal ayrışması karşılaştırılmalı. 5 A/1 V varyantı teorik olarak 6 kat daha yüksek çıkış üretir ama 40 mA doğruluğu üretici dokümanıyla garanti edilmemiştir.
5. Analog ön yükselteç, ADC'nin kendi kuantizasyon/gürültü etkisi baskınsa fayda sağlayabilir; CT'nin kendi manyetik gürültüsünü veya kabloya alınmış EMI'yi ortadan kaldırmaz. Kazanç 30 A tam aralıkta doyuma neden olabilir; düşük akım özel kanalı veya seçilebilir kazanç gerekir.
6. Harici ADC seçimi yalnız bit sayısına göre yapılmayacak. PGA giriş aralığı, gerçek örnekleme hızı, 50 Hz başına örnek sayısı ve ESPHome entegrasyonu birlikte incelenecek.
7. Öncelik sırası değişmiyor: E00A/E00B ve E01 taban çalışmaları; ardından planlı E08 1/2/4 tur yüksek hızlı edinim karşılaştırması. Üç tur denemesi 40 mA çözümü olarak kabul edilmeyecek. Bu oturumda firmware, devre, sensör veya deney sırası değiştirilmedi.

**Bu bölümün sınırı:** GitHub kod/doküman araştırması ve mevcut logun sayısal analizi yapıldı. Yeni fiziksel ölçüm, osiloskop ölçümü, Python model eğitimi, YAML değişikliği, derleme veya cihaza yükleme yapılmadı.

**Dış kaynaklar:** [YHDC SCT013-030 datasheet](https://naylampmechatronics.com/img/cms/000154/SCT013-030-0-30A-0-1V.pdf), [YHDC SCT013 ürün ailesi](https://en.yhdc.com/product/SCT013-401.html), [OpenEnergyMonitor düşük akım tartışması](https://community.openenergymonitor.org/t/getting-low-currents-with-sct013-50a/14035), [Analog Devices CT eğitim notu](https://wiki.analog.com/university/courses/alm1k/alm-current-transformer), [Allegro ACS712 datasheet](https://www.allegromicro.com/-/media/files/datasheets/acs712-datasheet.pdf), [ZMCT103C datasheet](https://macrogroup.ru/upload/iblock/074/q7ualcq97gdch22ecqzmiotaqaykpxto/ZMCT103C-specification.pdf).
