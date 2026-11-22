# SCT013-030 — 30 A / 1 V akım trafosu

## 1. Bu klasör ne için?

YHDC SCT013-030 (30 A / 1 V) sensörünün teknik referansı, bağlantısı, analog ölçüm şartları ve BERO projesindeki test notları burada tutulur. Bu model, çıkışında **gerilim veren** SCT013 çeşididir; 100 A / 50 mA olan SCT013-000 ile karıştırılmamalıdır.

## 2. Hızlı teknik özet

| Özellik | Bilgi |
|---|---|
| Model | SCT013-030 |
| Nominal primer akımı | 30 A RMS AC |
| Nominal çıkış | 1 V RMS AC @ 30 A |
| Nominal hassasiyet | Yaklaşık 33,33 mV/A RMS |
| Maksimum giriş bilgisi | Bazı YHDC veri sayfası kopyalarında 60 A olarak listelenir; bu, 60 A'da doğruluk/uzun süreli çalışma garantisi değildir |
| Çekirdek / yapı | Bölünebilir ferrit çekirdek, kelepçe tipi |
| Kablo / konnektör | Yaklaşık 1 m kablo, 3,5 mm üç kontaklı fiş |
| Frekans | Üretici dokümanlarında 50 Hz–1 kHz |
| Çalışma sıcaklığı | Üretici dokümanlarında -25 °C–+70 °C |
| Dahili yük direnci | Gerilim çıkışlı modelde vardır; ek burden direnci normalde eklenmez |

**Hesap:** 30 A girişte 1 V RMS ⇒ 1 V / 30 A ≈ 0,03333 V/A. Örneğin ideal nominal oranda 3 A ≈ 0,1 V RMS, 15 A ≈ 0,5 V RMS. Bunlar hesap değeridir; gerçek sensör kalibrasyonla doğrulanır.

## 3. Bağlantı ve yön

- Kelepçeyi yalnızca **tek bir iletkenin** etrafına kapat. Faz ve nötrü birlikte kelepçelemek, akımlar birbirini götürdüğü için yaklaşık sıfır okuma oluşturabilir.
- Çeneler tamamen kapanmalı; temas yüzeyleri temiz olmalı.
- Gövdedeki **IP oku**, üreticinin primer akım referans yönünü belirtir. Yön, özellikle gerilim-akım faz ilişkisi ve aktif güç hesabında önemlidir. Yalnızca RMS büyüklüğü ölçülüyorsa akım yönünü ters çevirmek ideal olarak RMS değerini değiştirmez.
- Çıkış uçları K/L olarak işaretlenmiş olabilir. Bu bir DC besleme girişi değildir; sensör AC gerilim üretir. Uçları değiştirmek dalga biçiminin faz işaretini ters çevirebilir. Faz ölçümü yapılacaksa aynı yön ve kablolama standardını bütün kanallarda koru.
- Fişin tip/ring/sleeve bağlantısını yalnızca görünüşten varsayma. Üretici çizimini ve elindeki fiş/kabloyu süreklilik ölçümüyle doğrula; bazı fiş şemalarında bir kontak NC gösterilir.

## 4. ESP32 / MCP3208 analog ön uç

SCT013-030'un 1 V RMS çıkışı sinüzoidal kabul edilirse tepe değeri yaklaşık 1,414 V'tur. ESP32/MCP3208 tek beslemeli ADC girişine negatif AC doğrudan uygulanamaz; sinyal uygun bir DC bias çevresinde tutulmalıdır.

BERO testlerinde konuşulan yaklaşık 1,67 V bias ve 3,12 V ADC referansı için teorik nominal sinyal aralığı:
- Alt tepe: 1,67 − 1,414 ≈ 0,256 V
- Üst tepe: 1,67 + 1,414 ≈ 3,084 V

Üst tepe 3,12 V referansa çok yakındır. Bias toleransı, gerçek RMS çıkış, şebeke bozulması ve geçici darbeler için pay azdır. ADC girişinin **0 V ile VREF arasında** kaldığını osiloskopla kontrol et; VREF'i aşma. 30 A üzerindeki akımda çıkış 1 V RMS'i aşabileceği için kırpılma riski artar. Bu hesap ideal sinüs varsayımıdır, güvenlik garantisi değildir.

- Gerilim çıkışlı SCT013 için sırf akım trafosu olduğu için harici burden direnci ekleme; dahili direnç bulunur. Ek yük, oranı ve ölçümü değiştirir.
- Bias, ADC giriş empedansı, koruma elemanları ve RC filtre gerçek devre şemasına göre değerlendirilmelidir.
- Ölçüm sırasında sensörün çıkışını ve ADC pinini aynı anda gözlemek, bias ve kırpılmayı ayırmaya yardımcı olur.
- Sensörün sekonder devresini, özellikle model kimliği belirsizken, açık devre bırakmanın güvenli olduğunu varsayma.

## 5. RMS ve kalibrasyon

1. Akım olmayan durumda bias merkezini ve ADC gürültüsünü kaydet.
2. Bilinen bir referans akımla, tercihen True-RMS ölçerle, birden çok noktada test et.
3. Ham ADC sayımlarından bias ortalamasını çıkar; RMS hesabında sinyalin DC biasını akım olarak sayma.
4. Sensör oranını gerçek referansla kalibre et. Nominal başlangıç ölçeği yaklaşık 33,33 mV/A RMS'tir; gerçek ADC kodu dönüşümü ayrıca VREF, ADC çözünürlüğü ve analog kazanca bağlıdır.
5. Dalga biçiminde tepe noktalarının ADC alt/üst sınırına yapışmadığını doğrula.
6. RMS penceresi ve örnek zaman damgalarını kaydet. Düzensiz örnekleme aralıklarını eşit aralıklıymış gibi kabul etmek RMS sonucunu bozabilir.

## 6. BERO geçmişinden önemli test uyarıları

- MCP3204/MCP3208 ile sıfıra yakın veya sabit/tekrarlayan okumalar görülmesi tek başına sensör arızasını kanıtlamaz.
- Daha önce ADC fiziksel olarak çıkarıldığında da benzer RX örüntüleri görüldüğü için SPI aktarımı, CS zamanlaması, TX/RX baytları ve okuma kodu ayrıca doğrulanmalıdır.
- SPI hata sayacının sıfır olması, alınan verinin doğru kanalı ve doğru sayısal değeri temsil ettiğini kanıtlamaz.
- Her testte sensör modeli, ADC modeli, VREF, bias, SPI pinleri/hızı/modu, ham RX baytları ve gerçek referans akımını birlikte kaydet.

## 7. Sınırlar ve güvenlik

Bu sensör şebeke iletkeninin etrafına takılır; kelepçeyi açıp kapatırken canlı iletkene veya çıplak bakıra dokunma. Sensörün yalıtım beyanı tüm montajı otomatik olarak güvenli yapmaz. Şebeke tarafındaki işler uygun yetkinlikle yapılmalıdır. Sensör, tek başına elektrik çarpmasına karşı koruma veya sertifikalı enerji sayacı değildir.

## 8. Kaynaklar

- YHDC SCT013 ürün ailesi / üretici sayfası ve veri sayfası bağlantıları: https://en.yhdc.com/product/SCT013-401.html
- SCT013-030 PDF kopyası (YHDC dokümanının dağıtılmış kopyası): https://naylampmechatronics.com/img/cms/000154/SCT013-030-0-30A-0-1V.pdf
- Seeed Studio'da barındırılan SCT013 veri sayfası PDF'si: https://files.seeedstudio.com/wiki/AC_Current_Sensor/Datasheet_of_SCT013.pdf
- OpenEnergyMonitor SCT-013 ailesi açıklaması: https://community.openenergymonitor.org/t/about-split-core-cts-sct-013-family/481

> Üretici dokümanlarının bazı kopyalarında tablo alanları eksik veya çeviri hatalı olabilir. Fiziksel sensörün etiketi ve tam model kodu birincil doğrulamadır.

## 9. BERO için ek teknik notlar — 2026-10-29

Kaynaklar: kullanıcı tarafından sağlanan SCT013_30A_1V_ESP32_Raporu.docx (14 sayfa) ve ct-akım-trafosu-satürasyonu.txt. Aşağıdaki bilgiler kaynak raporu/hesabı özetler; BERO'da fiziksel ölçüm yapıldığı anlamına gelmez.

- SCT013-030 nominal ilişkisi 30 A AC RMS girişte yaklaşık 1 V AC RMS çıkıştır. Nominal dönüşüm yaklaşık 30 A/V, yani 33,33 mV/A'dır. Sinüzoidal 1 V RMS için tepe değer yaklaşık 1,414 V'tur. Gerçek sensör ve analog zincir bu notla kalibre edilmiş sayılmaz.
- Gerilim çıkışlı SCT013-030 içinde burden direnci bulunur; ek burden direnci normalde eklenmez.
- AC çıkış tek beslemeli ADC'ye doğrudan uygulanamaz; BERO'nun mevcut bias devresi ve fiilî sinyal kuplajı esas alınır.
- Rapordaki ESP32 ADC attenuation/doğrusallık ve RMS örnekleri genel uygulama bilgisidir; BERO'ya firmware olarak aktarılmamıştır. İlk aşama planı dahili ESP32 ADC'dir; MCP3208 sonraya bırakılmıştır.
- Satürasyon belgesi aşırı primer akımı, sekonder burden ve DC ofseti gibi genel CT risklerini anlatır. BERO'da satürasyon gözlendiğine dair ölçüm yoktur.
- Kullanıcı tarafından bildirilen stok: 7 adet SCT013-030; bu kayıt bağımsız fiziksel sayım değildir.

### Kaynaklar
- YHDC ürün ailesi: https://en.yhdc.com/product/SCT013-401.html
- SCT013-030 veri sayfası kopyası: https://naylampmechatronics.com/img/cms/000154/SCT013-030-0-30A-0-1V.pdf
- Seeed Studio SCT013 veri sayfası: https://files.seeedstudio.com/wiki/AC_Current_Sensor/Datasheet_of_SCT013.pdf


## 10.1 Bağlantı teması kaynaklı gürültü gözlemi – 2026-11-22

### Kullanıcı gözlemi

- **Önceki gün (2026-11-21):** Gürültü okunmadığı düşünülen SCT bağlantısında pinlerin tam oturmadığı/temasın yeterli olmadığı sonradan fark edildi.
- **Bugün (2026-11-22):** Bağlantı yenilendi. Yenilemeden sonra SCT okumasında gürültü görüldü.
- Bu gözlem kullanıcı tarafından bildirildi; sayısal ham kayıt, gürültü genliği, örnekleme süresi veya CSV henüz paylaşılmadı.

### Teknik yorum

Önceki gün gürültü görülmemesi, SCT013 sensörünün veya ölçüm zincirinin gerçekten düşük gürültülü olduğunu kanıtlamıyordu. Yetersiz mekanik oturma/elektriksel temas, sinyalin ADC'ye eksik veya kesintili ulaşmasına ve gürültünün görünmemesine neden olmuş olabilir.

Bağlantı yenilendikten sonra gürültünün görünmesi, ilk gözlemin sensör gürültü karakterizasyonu olarak kullanılamayacağını gösterir. Bununla birlikte yalnızca bu olay, görülen gürültünün kaynağının sensör, kablo, konnektör, bias devresi veya ADC olduğunu tek başına belirlemez.

### BERO için çıkarılan ders

1. Gürültü tabanı veya yüksüz sinyal kararlılığı değerlendirilmeden önce SCT fiş/pin bağlantısının tam oturduğu ve mekanik olarak sabit olduğu kontrol edilmelidir.
2. Sessiz/0'a yakın okuma doğrudan “sensör gürültüsüz” veya “ADC gürültüsü düşük” şeklinde yorumlanmamalıdır.
3. Sensör, kablo, fiş ve ADC girişi ayrı ayrı kontrol edilmeden gürültü kaynağına ilişkin kök neden kararı verilmemelidir.
4. Bağlantı yenilemesi/yeniden oturtma yapıldıysa bu değişiklik deney günlüğüne yazılmalı; önceki ve sonraki kayıtlar aynı fiziksel bağlantı koşuluymuş gibi karşılaştırılmamalıdır.

### Durum ve kanıt sınırı

- **Kullanıcı gözlemi:** Pinlerin tam oturmaması ve bağlantı yenilenince gürültünün görülmesi.
- **Doğrulanmamış:** Gürültünün genliği, spektrumu, sürekliliği ve fiziksel kaynağı.
- **Karar:** Önceki sessiz bağlantı gözlemi, SCT013 gürültü tabanı veya ADC noise-floor kanıtı olarak kullanılmayacaktır.


## 10.2 V1.6 kodundaki filtrelerin kapsamı – 2026-11-22 açıklaması

Kullanıcı, bağlantı yenilemesi sonrasında gürültü göründüğünü belirtirken mevcut kodda filtre bulunduğunu hatırlattı. Depodaki MOD2-GRV001/V1.6/V1.6-TEST-A0A1-TEK-FONKSIYON-KX-30MA.yaml dosyası incelendi.

V1.6 içindeki ilgili işlemlerin gerçek kapsamı:

1. ct_clamp:
   - ADS1115 ham diferansiyel okumalarını 200 ms sample_duration penceresinde biriktirerek RMS akım büyüklüğü üretir.
   - ESPHome ct_clamp RMS hesabı DC ortalamayı varyans yaklaşımıyla çıkarır: RMS = sqrt(E[x²] - E[x]²). Bu, DC biası bastıran ve pencere içinde ölçüm yapan bir işleme/filtreleme adımıdır.
   - Ancak pencere içindeki AC gürültü enerjisini ayıklamaz; AC gürültü de RMS hesabına katkı yapar. Dolayısıyla bu işlem, yüksüz AC gürültüsünü otomatik olarak yok eden bir düşük geçiren veya hareketli ortalama filtresi değildir.
   - 200 ms pencere tek bir RMS istatistiği üretir; update_interval: 1s bu sonucun yayın/güncelleme aralığıdır. Bu ayar tek başına ardışık RMS sonuçlarını yumuşatmaz.
2. calibrate_linear:
   - Ölçüm değerine baz ölçek uygular (1.0 -> 27.59).
   - Gürültü bastırma filtresi değildir.
3. Lambda:
   - Üstel K(x) düzeltmesini uygular.
   - NaN veya negatif/değersiz akımı sıfırlar.
   - Gürültüyü zamana göre yumuşatmaz.
4. Template yayın sensörü:
   - Düzeltilmiş akım <= 0.030 A ise Home Assistant'a 0.000 A yayınlar.
   - Bu, 30 mA altı yayın eşiğidir; 30 mA üzerindeki dalgalanmaları süzmez.
5. update_interval: 1s:
   - Sonucun güncellenme aralığıdır; tek başına filtreleme yapmaz.

Düzeltme ve netleştirme: “Kodda filtre var” ifadesi doğrudur. V1.6'da ct_clamp'in 200 ms RMS penceresi DC ortalamayı çıkarır ve pencere içi AC enerjiyi RMS olarak ölçer; calibrate_linear ve K(x) fiziksel ölçeği/katsayıyı düzeltir; template sensörü 30 mA ve altını sıfırlar. Ancak ct_clamp AC gürültüyü ayıklamaz: bu gürültünün RMS karşılığı 30 mA eşiğini aşarsa yayın sensöründe akım gibi görünür. Bu yüzden bağlantı yenilendikten sonra gürültünün görünmesi kodda hiçbir filtre olmadığı anlamına gelmez; mevcut filtre zincirinin AC gürültüyü bastırmak üzere tasarlanmadığı anlamına gelir. Bağlantı teması düzeltildikten sonra ölçümün görünür hale gelmesi, önceki sessiz okumanın güvenilir noise-floor ölçümü olmadığını destekler; ancak yeni görülen gürültünün kaynağını tek başına belirlemez.

### Ekli Home Assistant geçmiş CSV'sinin sınırı

Kullanıcının 2026-11-22 tarihinde paylaştığı history (37)(1).csv dosyası incelendi:
- Toplam 680 satır / 3 sütun.
- PZEM gerilim sensörü: 633 kayıt.
- PZEM frekans sensörü: 41 kayıt.
- sensor.esp32d2_bero_akim_sensoru: yalnızca bir kayıt, 0.0 A (2026-11-22 17:00:00 UTC).
- Akım sensörü için zaman serisi veya gürültü dağılımı bulunmuyor.

Bu CSV, bağlantı yenilemesi sonrası SCT gürültüsünün büyüklüğünü/kararlılığını hesaplamak için yeterli değildir. Bu nedenle bu dosyadan akım gürültüsü metriği çıkarılmamıştır.

### Sonraki ölçümde kaydedilecekler

- Bağlantı ve pinlerin tam oturduğu fiziksel olarak kontrol edilsin.
- Akım sensörünün yüksüz ham/işlenmiş verisi yeterli süre boyunca kaydedilsin.
- 30 mA yayın eşiği nedeniyle HA'ya sıfırlanan bölge ile iç ölçüm değeri birbirinden ayrılsın.
- Mümkünse V1.6 iç sensör değeri (bero_akim_a0_a1_internal) ve yayın sensörü birlikte kaydedilsin.
- Gürültü kaynağına karar vermeden önce SCT fişi/kablosu, ADC girişleri, bias/topoloji ve ölçüm yazılımı ayrı ayrı kontrol edilsin.

Durum: Kod kapsamı incelendi; CSV akım zaman serisi sağlamıyor; yeni gürültü için nicel sonuç henüz yok.


## 10.3 Ham RMS değerini ayrı veri sütununda saklama önerisi – 2026-11-22

### Öneri

V1.6'nın mevcut kalibre edilmiş akım yayınını değiştirmeden, aynı ct_clamp ölçümünün filtreler öncesi ham RMS değerini ayrıca kaydetmek önerildi.

Amaç:
- Bağlantı/temas sorunu sonrası sinyalin gerçekten ortaya çıkıp çıkmadığını görmek.
- Kalibrasyon düzeltmesinin ham ölçüme etkisini ayırmak.
- 30 mA yayın eşiğinin altında kalan ölçümü ayrıca inceleyebilmek.
- Filtrelenmiş/kalibre edilmiş ana değer ile teşhis amaçlı ham değeri aynı zaman penceresinde karşılaştırmak.

### Önemli terminoloji

Önerilen “ham” sütun, anlık ADS1115 ADC örneği değildir.

V1.6 zincirinde ct_clamp:
- Kaynak analog örnekleri 200 ms boyunca toplar.
- DC ortalamayı çıkarır.
- AC RMS değerini hesaplar.

Dolayısıyla filtreler öncesi değer, **200 ms pencereyle hesaplanmış kalibrasyon öncesi RMS gerilimidir (V RMS)**. Bu değer ham dalga biçimi veya tekil ADC kodları değildir.

### Düşük müdahaleli uygulama fikri

ESPHome sensör otomasyonundaki on_raw_value tetikleyicisi, sensör değeri filtreleri uygulanmadan önce çağrılır. Mevcut ct_clamp sensörünün bu tetikleyicisinden alınan değer ayrı bir teşhis sensörüne/CSV sütununa aktarılabilir.

Bu yaklaşım, aynı ADS1115 girişini ikinci bir ct_clamp bileşeniyle yeniden örnekletmekten daha az müdahalelidir. Böylece ikinci örnekleme yolunun zamanlama ve kaynak yükü oluşturması önlenir.

### Önerilen veri sütunları

| Alan | Birim | Açıklama |
|---|---|---|
| sct_raw_rms_v | V RMS | ct_clamp 200 ms RMS sonucu; calibrate_linear ve K(x) öncesi |
| sct_calibrated_current_a | A | Baz ölçek ve K(x) düzeltmesi sonrası, 30 mA yayın eşiği öncesi |
| sct_published_current_a | A | Mevcut V1.6 Home Assistant değeri; 30 mA ve altı sıfırlanır |

Ham RMS sütunu V cinsinden açıkça adlandırılmalıdır; doğrudan amper olarak sunulmamalıdır. Amper cinsinden karşılaştırma için ayrıca baz ölçekli ve kalibre edilmiş sütun gerekir.

### Değişmezler ve doğrulama

- Mevcut V1.6 akım hesaplama ve yayın davranışı değiştirilmemelidir.
- Yeni teşhis alanı ilk aşamada yalnızca veri toplama amacıyla kullanılmalıdır.
- Ham RMS değerinin on_raw_value üzerinden geldiği, zaman damgasının aynı ct_clamp güncellemesine ait olduğu doğrulanmalıdır.
- Yeni alanın Home Assistant recorder/veri tabanı yükü gözlenmelidir.
- Bu öneri henüz YAML'a uygulanmadı, derlenmedi veya donanımda test edilmedi.

Durum: Tasarım önerisi; mevcut V1.6 davranışına değişiklik yapılmadı.


## 10.4 V1.6-DIAG1 boşta logu ve ct_clamp NaN davranışı – 2026-11-22

Kullanıcının yüksüz/enerjisiz koşulda paylaştığı ilk DIAG1 cihaz logu analiz edildi.

- Yaklaşık iki dakikalık kayıtta akım yayın sensörü 119 kez 0.000 A verdi.
- Ham RMS sensörü 116 kez NaN, dört kez 0.000500 V verdi.
- Dört ct_clamp debug kaydında `Raw AC Value: 0.001A after 2 different samples (10 SPS)` görüldü.
- İki ADS1115 debug kaydında `Got Voltage=0.000000V` görüldü.

ESPHome ct_clamp kaynak kodu incelendi: örnekleme penceresi başında örnek sayacı sıfırlanır; aynı ADC değeri yeni örnek olarak sayılmaz; pencere sonunda hiç farklı örnek yoksa ct_clamp `publish_state(NAN)` çağırır. Bu nedenle sabit 0 V / değişmeyen ADC değerlerinde NaN oluşması mümkündür. Ana V1.6 akım yayın lambda'sındaki NaN -> 0 dönüşümü ayrı bir işlemdir ve Home Assistant akım sensörünün 0.000 A göstermesini açıklar; ham RMS sensöründeki NaN'ın nedeni bu dönüşüm değildir.

`2 different samples (10 SPS)` ifadesi, 200 ms pencerede kabul edilen iki farklı örnek sayısından hesaplanır; ADS1115'in fiziksel örnekleme hızının 10 SPS olduğunu kanıtlamaz.

Dört adet 0.000500 V ham RMS kaydının kaynağı belirlenemedi. Bu ilk yüksüz log, SCT gürültü tabanı hesabı için yeterli değildir. Yük altında kısa bir kontrol ve ardından kontrollü yüksüz tekrar gerekir.

Ayrıntılı sayım, seçilmiş ham log satırları ve kaynak kodu yorumu:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.6/LOGS/2026-11-22-V1.6-DIAG1-ILK-BOS-OLCU-LOG-ANALIZI.md`

Durum: Firmware derlenmiş ve cihazda çalışır durumda; DIAG1 ham RMS ölçümü yüksüz testte henüz doğrulanmış bir noise-floor kaydı üretmedi.


Ayrıca DIAG1'de görülen 0.000500 V ham RMS değeri V1.6 zincirinden geçirilirse yaklaşık 0.01610 A verir; bu 30 mA eşiğinin altında olduğundan ana akım sensörünün 0.000 A göstermesi beklenir. Bu hesap, ham gerilim ile yayın akımı arasındaki farkı açıklar; ham değerin fiziksel kaynağını belirlemez.


## 10.5 DIAG1 – history (39)(1).csv etkin ölçüm bulguları – 2026-11-22

Kullanıcının paylaştığı 456 satırlı Home Assistant history CSV'sinde:
- ESP32D2 ham RMS sensöründe 21:29:05 TSİ sonrasında yük/akım mevcutken düzenli sayısal değerler gözlendi.
- Etkin kararlı bölümde 11 ham RMS değeri 0.003421–0.003627 V; ortalama 0.003526 V.
- Bu 11 değerin V1.6 kalibrasyon zincirinden hesaplanan karşılığı 0.108564–0.114981 A; ortalama 0.111825 A.
- Ham RMS ve HA akım sensörünün toplam 13 ardışık eşleştirmesinde hesaplanan akım, yayınlanan akımla eşleşti. Ham RMS zamanından akım template sensörü zamanına ortalama 0.6868 s fark bulundu. Bu, ct_clamp tetik zamanı ile 1 saniyelik template update zamanlamasına uygundur; analog faz gecikmesi değildir.
- Boşta 0.000500 V, V1.6 zincirinde yaklaşık 0.01610 A verir; 30 mA eşiğinin altında olduğu için HA akım sensörü 0.000 A yayınlar.
- Etkin bölümde PZEM 0.054 A gösterirken SCT zinciri yaklaşık 0.112 A göstermiştir. PZEM kendi V×I×PF sonuçlarıyla uyumludur; ancak aynı iletken/yük/ölçüm anı koşulları bağımsız olarak kanıtlanmadığından farkın sebebi belirlenememiştir. PZEM 0.030–0.054 A ölçümleri V1.6 kalibrasyon serisinin 0.067 A alt sınırının altındadır; bu CSV ile K(x) değiştirilmemelidir.

Detaylı eşleştirme, hesaplar ve sınırlamalar:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.6/LOGS/2026-11-22-V1.6-DIAG1-HISTORY-39-CSV-ANALIZI.md`

Durum: DIAG1 ham RMS veri yolu ve V1.6 yazılım dönüşüm eşleşmesi doğrulandı. Fiziksel akım doğruluğu/PZEM farkı henüz çözülmedi.


## 10.6 DIAG1 deney hedefi ve başarı kararı – 2026-11-22

Kullanıcı, DIAG1 deneyinin kabul ölçütünü netleştirdi: hedef yaklaşık 8.5 W seviyesinde SCT013-030 (30 A / 1 V) ile **akım var/yok ayrımını** yapabilmektir. PZEM ile amper değerlerinin birebir eşleşmesi bu deneyin hedefi değildir.

history (39)(1).csv'de yüksüz durumda ana akım sensörü 0.000 A; yük etkin durumdayken ham RMS sayısal ve akım sensörü yaklaşık 0.11 A; yük kapandığında ana akım sensörü yeniden 0.000 A görünmektedir. Bu nedenle test, kullanıcının belirlediği düşük güçte var/yok algılama kriterine göre **BAŞARILI** kabul edilir.

Bu karar, mutlak akım doğruluğu, güç/enerji ölçümü veya tüm 30 A ölçüm aralığının kalibrasyonu için başarı beyanı değildir. PZEM ile sayısal amper farkı ayrı çalışma konusudur; DIAG1'in akım var/yok algılama sonucunu başarısız yapmaz. CSV'deki PZEM ham ölçümleri korunur ve ayrı gözlem olarak yorumlanır.

Ayrıntılı analiz ve kullanıcı tarafından netleştirilen kabul ölçütü:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.6/LOGS/2026-11-22-V1.6-DIAG1-HISTORY-39-CSV-ANALIZI.md`


## 10.7 Üretici karakteristik aralığı ve düşük akımda ölçüm hassasiyeti – 2026-11-22

### Üretici belgelerinden doğrulananlar

İki farklı üretici belgesi birbirinden ayrılarak değerlendirilmelidir:

1. YHDC'nin 2015 tarihli SCT013-030 ürün spesifikasyonu, 30A/1V model için rated input 0–30 A, rated output 0–1 V, accuracy ±1% ve linearity ≤0.2% ifadelerini verir. Bu tabloda ayrıca 1 A gibi açık bir minimum akım sınırı yazılmamıştır.
   - Dağıtılmış PDF kopyası: https://www.mouser.com/datasheet/2/744/101990028_SCT_013_030_Datasheet-2487857.pdf
2. PowerUC/YHDC SCT013 ürün ailesinin karakteristik grafiklerinde 5A/1V modelinin ilk işaretli akım noktası 1 A; 30A/1V modelinin ilk işaretli akım noktası 6 A'dır. 30A/1V grafiğinde 6 A için yaklaşık 0.1994 V, 12 A için 0.3995 V, 30 A için 0.9994 V gösterilir.
   - Üretici aile PDF'si: https://poweruc.com/wp-content/uploads/2023/07/2025040819322782.pdf

**Yorum sınırı:** Grafiklerdeki ilk nokta, sensörün bunun altında çalışmadığı veya kesin alt sınırın 6 A olduğu anlamına gelmez. Yalnızca yayımlanmış karakteristik grafiğin o model için 6 A'dan başladığını gösterir. Aynı şekilde 0–30 A tablo ifadesi de SCT + kablo + ADS1115 + yazılım zincirinin 0.1 A seviyesinde ±1% doğruluk sağlayacağını tek başına kanıtlamaz. Üretici belgelerindeki genel doğruluk/doğrusallık ifadesi ile düşük akımda ayrıntılı test verisinin bulunması aynı şey değildir.

### Nominal çıkışın düşük akımda küçülmesi

30A/1V nominal oranından teorik hassasiyet:

- 1 V / 30 A = 33.33 mV/A RMS
- 1.0 A → yaklaşık 33.3 mV RMS
- 0.5 A → yaklaşık 16.7 mV RMS
- 0.1 A → yaklaşık 3.33 mV RMS
- 0.065 A → yaklaşık 2.17 mV RMS

Bunlar ideal nominal oran üzerinden hesap değerleridir; gerçek sensör/ADC ölçümü değildir.

Akım küçüldükçe sensör çıkış gerilimi de küçülür. Kablo/konnektör, ADC giriş gürültüsü, bias kararlılığı, örnekleme zamanlaması, kuantalama ve RMS algoritmasının toplam etkisi ölçülen AC sinyaline göre daha belirgin hale gelir. Bu, tüm ölçüm zincirinin düşük seviyede sinyal/gürültü oranını zorlar.

### BERO deneyinden çıkarılan sonuç

- BERO'nun 30A/1V örneğinde yaklaşık 0.1 A mertebesinde yük varlığının algılanması, üretici karakteristik grafiğindeki en düşük 6 A noktasından çok aşağıda işlevsel algılama yapılabildiğini gösterir.
- Bu başarı, 0.1 A civarında mutlak akım doğruluğu veya üreticinin yayımladığı ±1% toleransın sağlandığı anlamına gelmez.
- Yaklaşık 15 W altındaki ölçüm doğruluğu, kullanıcının mevcut uygulama hedefi için öncelikli değildir. Ana tasarım kararı bu nedenle düşük akım ucunu zorlayarak kalibrasyon eğrisini tekrar parçalamak değildir.

### Tek K(x) fonksiyonunun fiziksel yorumu

BERO'da bulunan:

`K(x)=26.89+5.39\,e^{-x/0.882}`

fonksiyonu, bu deney düzeneğinin (SCT013-030, fiziksel bağlantı, ADS1115 No.10, analog giriş koşulları, örnekleme ve RMS/yazılım zinciri) pratik aralıktaki toplam davranışını düzelten ampirik bir modeldir. Bu ifade CT çekirdeğinin evrensel fizik denklemi veya farklı SCT/ADC kurulumlarına aktarılabilecek üretici modeli değildir.

Bölgesel katsayı geçişleri yerine tek ve sürekli fonksiyonun kabul edilmesi, test edilen pratik aralıkta daha tutarlı bir model sağlamıştır. Düşük uçtaki sınırlı hassasiyet bu kararın bilinen kullanım sınırı olarak korunur.

Durum: Üretici belgesi ve BERO saha/kalibrasyon sonuçlarıyla yorumlandı; burada verilen mV/A alt seviye değerleri nominal oran hesabıdır, yeni donanım testi değildir.


## 10.8 YHDC 30A/1V üretici grafiğinin BERO V1.6 K(x) ile karşılaştırılması – 2026-11-22

Kullanıcının paylaştığı YHDC SCT013 aile grafik sayfasındaki SCT013(30A/1V) panelinin işaretli noktaları V1.6 ölçeği ve tek K(x) fonksiyonundan geçirildi. Nominal 6–30 A aralığında ortalama hesaplanan sapma -10.46% (aralık -10.60% ... -10.40%) çıktı. 36 A işaretli noktası üretici grafiğinde gösterildiği için tabloda/çizimde tutuldu, ancak 30 A nominal aralığın dışında olduğundan ortalamaya alınmadı.

Bu sonuç, üreticinin yaklaşık 30 A/V nominal transfer oranı ile BERO V1.6'nın ampirik yüksek akım katsayısı 26.89 A/V arasında yaklaşık %10.4 ölçek farkı olduğunu gösterir. Bu, V1.6'nın kendi sensör/ADC zincirinde aynı hata bulunduğunu kanıtlamaz; üretici eğrisi ile BERO sisteminin kalibrasyon ölçeği farklı dayanaklara sahiptir. Bu karşılaştırma K(x) fonksiyonunu değiştirme gerekçesi değildir.

Üretici grafiği 30A/1V için 6 A'dan başladığından 6 A altındaki davranış bu görselle karşılaştırılamaz. Grafik başlangıcının 6 A olması sensörün kesin alt sınırının 6 A olduğu anlamına gelmez. Düşük akımda sinyalin küçülmesi ve toplam ölçüm zincirinin göreli gürültü etkisi ayrı konudur.

Hesap yöntemi, yedi noktanın tablosu, 6–30 A istatistiği ve yorum sınırları:
- [Ayrıntılı karşılaştırma raporu](YHDC-30A-1V-GRAFIGI-V1.6-KX-KARSILASTIRMA-2026-11-22.md)
- [Karşılaştırma grafiği (SVG)](YHDC-30A-1V-GRAFIGI-V1.6-KX-KARSILASTIRMA-2026-11-22.svg)

Durum: Üretici grafik değerleri üzerinden matematiksel karşılaştırma yapıldı; yeni fiziksel BERO donanım testi yapılmadı.

## 10.9 Üretici grafiği – BERO ADS1115/K(x) – PZEM kanıtlarının ayrılması ve pens ampermetre önerisi – 2026-11-22

YHDC 30A/1V üretici grafiği, üreticinin laboratuvar/karakterizasyon verisidir. BERO V1.6 K(x) fonksiyonu ise gerçek BERO kurulumunda ADS1115 diferansiyel RMS ölçümleri, kalibrasyon deneyleri, fiziksel bağlantı ve yazılım zincirinin toplam ampirik davranışından elde edilmiştir. Üretici grafik noktalarının K(x)'ten geçirilmesi matematiksel bir karşılaştırmadır; BERO donanımında yeni ölçüm yapılmış anlamına gelmez.

V1.6 saha deneylerinde BERO akım sonuçlarının PZEM ile karşılaştırılması, BERO'nun kendi pratik çalışma aralığındaki kalibrasyonunu desteklemiştir. Bununla birlikte PZEM burada karşılaştırma referansıdır; izlenebilir laboratuvar standardı olarak kabul edilmemelidir. Mevcut V1.6 veri karşılaştırmasının yaklaşık 17.5 A seviyesine kadar uzanması, 30 A tam ölçeğin tamamının doğrulandığı anlamına gelmez.

### Önerilen bağımsız kontrol

Yüksek akımda, mümkünse AC True-RMS pens ampermetreyle ek saha karşılaştırması yapılması önerilir. Aynı kararlı yük aralığında üç değer kaydedilmelidir:
- BERO: SCT013 + ADS1115 + V1.6 K(x)
- PZEM: aynı devredeki akım ölçümü
- Pens ampermetre: tek bir faz veya nötr iletkeninden alınan bağımsız akım ölçümü

Pens yalnızca tek iletkeni çevrelemelidir; faz ve nötr birlikte ölçülmemelidir. Yük, priz, kablo, SCT ve ölçü aletlerinin nominal sınırları aşılmamalıdır. Marka/model, AC ölçüm aralığı ve doğruluk bilgisi; yük tanımı, zaman aralığı ve üç akım değeri birlikte kaydedilmelidir. Birden çok kararlı tekrar alınmadan ve ölçüm koşulları eşleştirilmeden K(x) katsayısı değiştirilmemelidir.

Pens ampermetre kontrolü **öneri aşamasındadır; henüz gerçekleştirilmiş değildir**. Üretici grafiği karşılaştırmasının hesap ayrıntısı ve grafik:
- [YHDC 30A/1V – V1.6 K(x) karşılaştırma raporu](YHDC-30A-1V-GRAFIGI-V1.6-KX-KARSILASTIRMA-2026-11-22.md)
- [Karşılaştırma grafiği (SVG)](YHDC-30A-1V-GRAFIGI-V1.6-KX-KARSILASTIRMA-2026-11-22.svg)

## 10.10 MOD3 çamaşır makinesi ısıtma bloğunda basit pens kontrolü – 2026-11-22

MOD3-AKM001 uzun pamuklu saha kaydındaki ısıtma bloğu, BERO ölçümünü pratik biçimde bağımsız kontrol etmek için seçilmiştir:
- Zaman: 17:24:12–17:38:56 (Europe/Istanbul)
- PZEM: yaklaşık 8.28 A
- BERO V1.6: raporlanan farktan türetilen yaklaşık 8.17 A
- Isıtma gücü: yaklaşık 1.81 kW

**Kontrol:** Benzer bir uzun pamuklu programda, ısıtma evresinin kararlı bölümünde pens ampermetreyle akım okunur. Pens yalnızca tek iletkeni çevreler. Pens okuması, önceki kayıttaki PZEM 8.28 A ve BERO yaklaşık 8.17 A ile karşılaştırılır. Birkaç kısa tekrar yeterlidir.

Bu deney ticari ölçüm cihazı geliştirme veya laboratuvar kalibrasyonu değildir; pratik bir çapraz kontroldür. Pens yaklaşık 8 A gösterip PZEM ve BERO sonuçlarını desteklerse, BERO'nun bu saha noktasında gerçek akımı izlediğine dair ek güven elde edilir.

Pens kontrolü tek başına üretici eğrisinden farkın CT örneğinde mi yoksa ADS1115/analog ölçüm zincirinde mi oluştuğunu ayıramaz; bunun için ham RMS çıkışın ayrıca ölçülmesi gerekir ki bu basit kontrolün kapsamı değildir. Tek nokta tüm akım aralığını kanıtlamaz.

Durum: Pens kontrolü öneri aşamasında; henüz ölçülmedi. V1.6 K(x) değiştirilmez. MOD3-AKM001 kapalı kalır.

