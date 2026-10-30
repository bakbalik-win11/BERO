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

**Amaç:** 0.006 V değerinin hangi koşula ait olduğunu ve aynı kayıtta N/SPS bulunup bulunmadığını belirlemek.

- Mevcut ESPHome loglarında Raw AC Value, after N different samples, SPS, zaman damgası ve yük/SSR durumu aranır.
- Aynı zaman aralığına ait pens değeri varsa not edilir.
- Eşleşme yoksa sonuç “eşleşme kanıtı yok” olarak kalır; geçmiş değerler geriye dönük eşleştirilmez.

**Kabul:** Her kayıt için yük koşulu ve zaman bilgisi ya kanıtla eşleşir ya da açıkça “bilinmiyor” olarak işaretlenir.

### D1 — Yüksüz SCT bağlı gözlem

**Amaç:** SCT bağlı, primer akım yok koşulunda Raw AC Value, farklı örnek sayısı ve raporlanan SPS dağılımını görmek.

- Mevcut firmware ve donanım ayarları değiştirilmez.
- Birden fazla ardışık pencerenin logu saklanır.
- Raw AC Value gerilim olarak değerlendirilir; SPS gerçek ADC hızı sayılmaz.

**Kabul:** Pencere sayısı, süre, N ve raporlanan SPS dağılımı kaydedilir; ölçüm koşulu belirtilir.

### D2 — 8.35 W LED gözlemi

**Amaç:** D1 ile aynı kurulumda düşük yükün pencere istatistiklerini nasıl değiştirdiğini görmek.

- Yük açık/kapalı durumu kayıt başında ve sonunda açıkça belirtilir.
- Pens okuması kararlı koşulda kaydedilir.
- Mümkünse PZEM değeri ve okuma zamanı ayrıca not edilir; PZEM'in bu düşük akımda geçerli/kararlı olduğu varsayılmaz.
- Mevcut 0.35 A filtresi korunur; debug RMS zaten filtre öncesi kaydedilir.

**Kabul:** D1 ve D2 aynı firmware/bağlantı/kurulum koşulunda karşılaştırılabilir; pencere etiketleri ve referans okuma koşulu kayıtta bulunur.

### D3 — Orta yük kontrolü

**Amaç:** D1/D2 farkının yalnızca yük değişimiyle mi yoksa genel ölçüm zinciriyle mi ilişkili olduğunu daha önce uyumlu sonuç alınan akkor yükte kontrol etmek.

- 100 W veya 150 W akkor koşulu kullanılır; gerçek kullanılan yük kayda yazılır.
- Pens okuması ve ESP32 logu aynı kararlı koşula bağlanır.
- 24.22 katsayısı ve eşik değiştirilmez.

**Kabul:** Aynı kurulumda düşük yük ve orta yük davranışları yan yana raporlanır; sapma oranı yalnız eşleşmiş ölçümlerden hesaplanır.

### D4 — Ayrı ham ADC teşhisi (yalnız gerekirse)

**Amaç:** Kalibre edilmiş Volt çıktısı yerine ham ADC count davranışını gözlemek.

- Mevcut çalışan YAML kopyalanıp ayrı teşhis yapılandırması oluşturulmadan ana dosyaya dokunulmaz.
- raw: true kullanılırsa ct_clamp çıkışı akım diye sunulmaz. 24.22 ve 0.35 A eşikleri bu yapılandırmada kullanılmaz; çıktı RAW count istatistiği olarak adlandırılır.
- raw: true aynı değerleri atlama mekanizmasını kaldırmaz; yalnız sayısal temsil biçimini değiştirir.

**Kabul:** Ham count verisi ve pencere istatistikleri ayrı birimlerle kaydedilir; mevcut E00F akım sensörüyle karıştırılmaz.

### D5 — E08 ham edinim ve algoritma karşılaştırması

**Amaç:** Bias RAW ve SCT RAW örneklerini zaman bilgisiyle alıp aynı örnek kümesinde alternatif istatistikleri hesaplamak.

- E08 planındaki GPIO34 Bias RAW ve GPIO32 SCT RAW eşlemesi, esp32d2 kimliği ve mevcut pin kararları korunur.
- İlk hedef kanal başına 1 kS/s, 200 ms penceredir; gerçek hız örnek sayısı ve zaman damgasıyla doğrulanır.
- ADC Continuous/DMA, aynı ADC1 biriminde One-shot sürücüsüyle eşzamanlı çalıştırılmaz.
- Mevcut E00F ct_clamp ile E08 ham edinimi aynı anda çalışıyormuş gibi varsayılmaz; gerekirse ardışık test yapılır.
- PC'de aynı ham örneklerden mean, bias-subtracted RMS, absolute peak, peak-to-peak ve örnek sayısı hesaplanır.

**Kabul:** Gerçek kanal hızları, pencere süreleri, ham örnek sayıları ve hesaplanan istatistikler raporlanır. Firmware yazılması, derlenmesi, flash edilmesi ve fiziksel ölçüm ayrı durumlar olarak kaydedilir.

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
- n_distinct_samples
- reported_sps (gerçek ADC hızı değildir)
- published_current_a (varsa)
- pens akım değeri, cihaz/okuma zamanı ve kararlı koşul notu
- PZEM akımı ve okuma zamanı (varsa; düşük akım geçerliliği ayrıca not edilir)
- yorum, kanıt türü ve sınırlamalar

## 7. Sonuç ve sonraki tek adım

**Sonuç:** Kaynak kod davranışı açıklığa kavuştu; düşük akım hatasının büyüklüğü ve nedeni henüz açıklığa kavuşmadı. Katsayı eğitimi için erken. Önce D0 mevcut log eşleştirmesi, ardından aynı kurulumda D1 yüksüz ve D2 LED gözlemi yapılmalıdır.

**Sonraki adım:** Kullanıcının mevcut E00F loglarında Raw AC Value, farklı örnek sayısı ve SPS satırlarının birlikte bulunup bulunmadığını incelemek; yoksa D1/D2 için yeni kayıt protokolünü uygulamak. Bu raporun yazılması fiziksel test yapılmış anlamına gelmez.

## 8. Kaynak ve sürüm notu

- ESPHome kaynak kodu: 2026.9.1; ct_clamp_sensor.cpp, ct_clamp_sensor.h, adc_sensor_esp32.cpp, adc_sensor.h kaynak incelemesi.
- BERO mevcut dosyaları: firmware/esp32d2.yaml, firmware/README.md, experiments/E08-sct-characterization/README.md, experiments/E08-sct-characterization/stage-03-high-speed-capture.md.
- Kaynak kod incelemesi ile kullanıcı tarafından sağlanan deney logları ayrı kanıt sınıflarıdır. Simülasyon çıktıları BERO ölçümü sayılmaz.
