# Proje durumu

**Uzun vadeli yön:** Tek bir akım ölçerle sınırlı olmayan, göreve göre sensör ve donanımı değişebilen ESP tabanlı sistemler; model/katsayı öğrenimi ve ileride başka görevler için örüntü algılama. Bu vizyon [proje felsefesinde](docs/project-philosophy.md) açıklanır; E00A'nın SCT'siz bias-only alt koşulu kapatıldı; E00A'nın diğer işleri açık, yeni aktif hazırlık E00B SCT bağlı/akımsız ADC gözlemidir.

**Genel görünüm:** [İlerleme ağacı — PROGRESS_TREE.md](PROGRESS_TREE.md). Deneylerin nedenini, kod/kanıt durumunu ve sonraki karar kapısını izlemek için [Deney ve karar izleme defteri](EXPERIMENT_LEDGER.md) kullanılır. Projenin kişisel veri kümesi, model öğrenimi ve kabul edilebilir sınırlarına ilişkin yaklaşım [proje felsefesinde](docs/project-philosophy.md) kayıtlıdır. Depoyu baştan sona okumadan genel resmi görmek için önce ilerleme ağacına, ardından bu dosyadaki güncel duruma bak.

**Son güncelleme:** 2026-10-30 — E08 grafik standardı kullanıcı tarafından onaylandı: zaman ekseninde mavi Bias GPIO34 RAW, kırmızı SCT GPIO32 RAW ve yeşil olay işareti. Kullanıcı daha hızlı örnekleme ile salınımları ayrıntılı görmek istedi. Sıradaki hazırlık, ESP32D2 kimliği ve mevcut GPIO eşlemeleri korunarak ADC continuous/DMA tabanlı iki kanallı ham edinim tasarımıdır; ilk hedef 1 kS/s/kanal (toplam 2 kconversion/s), 200 ms ham pencere. Bu henüz tasarım/plan aşamasıdır; firmware yazılmadı, derlenmedi veya cihaza yüklenmedi. Grafik standardı ve hızlandırma planı: [E08 yüksek hızlı edinim hazırlığı](experiments/E08-sct-characterization/stage-03-high-speed-capture.md).\n\n**Önceki güncelleme:** 2026-10-30 — E00B uzun logu kaydedildi; 351 geçerli yayın/kanal üzerinden SCT ve bias karşılaştırması olumlu (RAW fark +0.82 count, ADC voltaj farkı −1.4 mV). Ham log ve analiz E00B klasöründe. Fiziksel primer akım/CT montaj koşulu logdan bağımsız doğrulanmış değil. Sonraki yük koşulunda mevcut dört kanallı E00B firmware’i aynı noktaları izlediği için kod değişikliği gerektirmiyor; koşul ayrı log ve sonuç olarak kaydedilecek. E00A’nın diğer işleri açık kalır.\n\n**Önceki güncelleme:** 2026-10-30 — E00A'nın SCT bağlı olmayan bias-only alt adımı, son ESP32D2 logu ve taban dalgalanması yorumu ile KAPATILDI. GPIO35 gözlenen standart sapma 6.474 mV; GPIO34 RAW 6.97 count. Bu, tüm ölçüm zincirinin dalgalanmasıdır; ADC'nin tek başına gürültüsü değildir. RAW=0 başlangıçları eşleştirme dışı bırakıldı. E00A bütünü açık: 3.3 V bölücü koşulu ve ham CSV/grafik eksik. Önceki E00A-S01 GND referans testi kaydedildi; GPIO34 0 count, GPIO35 kararlı bölümde 0.142 V; floating giriş teşhisi destekleniyor. Elektriksel çözüm adayı Vmid'e yüksek değerli pasif bias direnci; kesin değer ve jack topolojisi doğrulanacak. Ayrıntı E00A-S01 raporunda. E00A henüz açık. Önceki durum: E00A açıldı; ilk iki multimetre referansı kaydedildi: L78L33 çıkışı 3,31 V, breadboard bias orta noktası/Vmid 1,65 V (KULLANICI BİLDİRİMİ). Bu ESP32 ADC ölçümü değildir. Her ADC koşulu için 30 saniyelik gözlem planlandı. Ayrı/geçici 10k/10k ölçüm bölücüsü bias devresinin parçası değildir ve fiziksel olarak kurulmuş sayılmaz. ESP32D2 için E00A firmware'i depoya eklendi; kullanıcı derlendiğini ve çalıştığını bildirdi (KULLANICI RAPORU). ADC sayısal logu ve ham kayıt henüz bekleniyor. 2026-10-29 — Gün sonu çapraz kontrolü: E00A'da ham ADC kaydı ve bilgisayarda zaman grafiği temel hedef; istatistikler yardımcı. T007 mimari taslağı, edinim kanıtı oluşana kadar beklemede. PZEM/akım formülü/MCP3208 ilk aşamanın kapsamı değil.  
**Belge denetimi:** TAMAMLANDI — temel durum/karar dosyaları, deney sırası, hedef alan sözlüğü ve 87 Markdown dosyasındaki göreli bağlantı hedefleri kontrol edildi; bulunan tek kırık göreli bağlantı düzeltildi. Bu yalnızca depo belgelerinin denetimidir; fiziksel veya yazılım doğrulaması değildir. **Fiziksel deney hazırlığı:** BEKLEMEDE — seçilecek kart/GPIO gerçek kart üzerindeki pinout ile eşleştirilmeli, ADR-007'deki 10 µF değişikliği fiilen uygulanıp kayda geçirilmeli, ham kayıt formatı ve yerel dosya yolu kullanılmalıdır. JSON Schema validator, YAML parser, firmware derlemesi, CI ve fiziksel test bu turda çalıştırılmadı. İlk teknik deney E00A olarak korunuyor.  
**Aktif faz:** Faz 1 — SCT analog ön uç ve yüksüz ölçüm hazırlığı  
**Sıradaki iş:** E00B firmware'i kullanıcı bildirimiyle derlendi; sırada gerçek kart pinout/GPIO32-33 doğrulaması, fiziksel bağlantı, cihaza yükleme ve SCT bağlı/primer akımsız logudur. Bias GPIO34/35, SCT GPIO32/33 planı korunur. E00A'nın 3,3 V bölücü koşulu ve ham CSV/grafik işi ayrıca açık kalır. E00A — bias trafosu DC noktalarının ADC gözlemi (AÇILDI; ilk multimetre referansı kaydedildi). L78L33 çıkışı 3,31 V (kullanıcı multimetre bildirimi); breadboard bias orta noktası/Vmid 1,65 V (kullanıcı multimetre bildirimi). Her koşul için 30 saniye planlandı. 3,3 V ölçüm aparatı olarak ayrı/geçici 10k/10k bölücü düşünüldü; ADC sınırları doğrulanmadan bağlantı yapılmayacak. SCT bağlı değil. GPIO34 yalnız gerçek ESP32-WROOM-32D kart/pinout doğrulanırsa kullanılacak. Sonrasında E00 ve T005/E01 hazırlığı gelir. [E00A — Ham sinyal kaydı ve temel istatistikler](experiments/E00A-raw-waveform-observation/README.md) AÇILDI; ilk iki multimetre referansı kaydedildi: L78L33 çıkışı 3,31 V, breadboard Vmid 1,65 V; ESP32D2 firmware'i kullanıcı bildirimiyle derlendi/çalıştı; GPIO34 raw ve GPIO35 voltaj sensörlerinin logu bekleniyor. 30 saniyelik ham CSV/grafik henüz yok; ardından [E00 — Bias ADC karşılaştırması](experiments/E00-bias-adc-baseline/protocol.md) ve [T005 — ADC temel okumaları ve E01 gürültü tabanı](tasks/T005-noise-floor.md). E00A'nın ilk hedefi ADC'den ne okunduğunu görmek, ham örnekleri kaydetmek ve bilgisayarda görselleştirmektir. Grafik bu aşamada temel inceleme aracıdır; istatistikler yardımcıdır. PZEM karşılaştırması, akım formülü/kalibrasyon ve MCP3208 ilk adımın kapsamı değildir. T005 — PLANLANDI. İlk önce SCT bağlamadan bias noktasında `analogRead()` ham sayısı ile `analogReadMilliVolts()` karşılaştırılacak; sonra SCT bağlıyken akım yok durumunda aynı iki okuma yapılacak; uzun E01 gürültü kaydı daha sonraya bırakıldı. T003, PZEM'e göre ±%4 bağıl sapma ve Python `OK` karar kuralı belirlenerek kapatıldı. T001 envanter ve T002 güvenlik kontrolü, kullanıcının tamamladığını bildirdiği bilgiler esas alınarak kaydedilip kapatıldı.  
**Öncelikli SCT:** SCT013-030 (30 A / 1 V)  
**PZEM:** Esas kaynak [DONANIM/PZEM-004T/README.md](../../DONANIM/PZEM-004T/README.md); CT modeli kullanıcı tarafından PZCT-02 (0–100 A) olarak belirtildi.  
**Bias üretim alt devresi:** TAMAMLANDI — kullanıcı onayı. RN130421 + KBU6M + 2200 µF / 35 V + L78L33; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) kondansatör. Bağımsız ölçüm raporu bu kayda eklenmedi.  
**SCT/bias devresi:** Kullanıcı tarafından tarif edilen bağlantıda SCT dişi jack üzerinden breadboard bias alt devresine bağlanır; alt devrede 2 × 10 kΩ dirençle orta nokta ve orta noktadan GND'ye mevcut 104 (100 nF) kondansatör vardır. ADR-007 planına göre bu kondansatör sökülmeden aynı Vmid–GND noktalarına paralel 10 µF elektrolitik kondansatör eklenecek (pozitif uç Vmid, negatif uç GND); fiziksel uygulama henüz doğrulanmadı. Bias yaklaşık 1,65 V kabul edilir; bu aşamada ayrıca ölçülmesi şart değildir. Harici ADC kullanılmayacak; ESP32 dahili ADC kullanılacak, MCP3208 sonraya bırakıldı. Bias'ın ayrı kayıt alanı olması yazılım/veri kaydı aşamasında ele alınacak. ADC GPIO/pin planı firmware aşamasına aittir. T004 hobi düzeyi belgeleme kapsamıyla tamamlandı; laboratuvar düzeyinde ADC aralığı/clipping hesabı T004 kapanış şartı değildir.  
**PF ve akım ölçümüne ilişkin teknik not:** [PF değişimi ve akım ölçümüne etkisi](docs/architecture/pf-and-current-measurement.md). PZEM'in gerilim ölçümü doğrudan hattan, akım ölçümü harici CT'den gelir; yayınlanan PF bu ölçüm zincirinin birleşik sonucudur. PZEM PF ve akım değerleri SCT karşılaştırmasında birlikte kaydedilecek. Farklı PF koşullarındaki SCT-PZEM hata davranışı [E09](experiments/E09-pf-current-relationship/README.md) kapsamında incelenecek; aktif ilk deney sırası değişmez.

**SCT/PZEM eğitim ve gözlem mimarisi:** [Hedef mimari notu](docs/architecture/sct-pzem-labeling-and-calibration.md) ve [eğitim + ham akış gözlem belgesi](docs/architecture/training-and-dynamic-observation.md). Aynı SSR aç-kapa deneyinden (1) PZEM/SCT ortak kararlı alanlarını etiketleyip model eğitme ve aynı etiketli veride eğitim içi uyum raporu, (2) aynı olayın geçişler dahil tam ham SCT akışında model tahminini PZEM zaman serisiyle ortak zaman ekseninde gözleyip tepki/gecikme incelemesi yapılması hedeflenir. Bu iki rapor ayrıdır. Firmware, algoritma, model ve deneyler henüz yapılmadı.  
**SSR:** SAMM Market 5 V, 2 kanallı kart; tedarikçi kodu İzmo9659, SKU MP02637. Giriş mantığı ve kart üzerindeki SSR'nin tam kodu doğrulanmalı.  
**RTC:** İki DS3231 modülünde de 2032 tipi pil bulunuyor. RTC kodunun çalıştığı ve güç kesilip yeniden verildikten sonra saatin korunduğu daha önce test edildi; bu bilgi esas alınır ve test tekrar istenmeyecek. Yüksek hızlı örnekleme zamanlaması ESP32 monoton zamanlayıcısına aittir.  
**Deney durumu:** Donanım henüz kurulmadı; E00A bias trafosu 3,3 V ve Vmid ADC karşılaştırması, E01 yüksüz gürültü kaydı, E07 eski planı, E08 karakterizasyon planı ve kalibrasyon YAPILMADI. Donanım henüz kurulmadı; E00 bias-only ADC karşılaştırması, E01 yüksüz gürültü kaydı, E07 eski planı, E08 yeni karakterizasyon planı ve kalibrasyon YAPILMADI. Güncel SCT karakterizasyon sırası [E08](experiments/E08-sct-characterization/README.md): (1) yüksüz uzun okuma, (2) 100 W akkorla 1/2/4 kablo turu × 1/2/2,5 kS/s matrisi, (3) aynı matrisin 150 W akkor ve 8,5 W LED'de tekrarı, (4) sonuçlardan sonra aç-kapa davranışı. Aynı pencere örneklerinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanacak; yardımcı istatistikler ve gerçekleşen örnekleme hızı kaydedilecek. PZEM veya başka ESP'nin ortalama akımı yalnız genel deney notudur; SCT pencereleriyle zaman eşleştirmesi yapılmaz. Kararlılık eşiği, pencere sayısı ve kesin kayıt süresi önceden sabitlenmez. Önceki [E07 protokolü](experiments/E07-sct-stability-step-tests/protocol.md) fiziksel olarak uygulanmadı; güncel plan için E08 esas alınır. E00A öncelikli ilk deneydir; ardından T005/E00-E01 hazırlığı gelir. 30 saniye asgari başlangıç referansıdır, üst sınır değildir; kesin süre belirlenmedi. PZEM ve diğer ESP kartları ölçülen hattan beslenmez; beslemeleri ayrıdır.

## Oturum sürekliliği
- Yeni oturumda başlangıç protokolü uygulanır: güncel main/son commit kontrol edilir; AGENTS, STATUS, ROADMAP, open-questions, ilgili görev/deney ve son günlük kaydı okunup karşılaştırılır.
- Başlangıç raporunda okunan kaynaklar, mevcut durum, hedef ve kabul koşulları kısaca belirtilir. Önceden kaydedilmiş bilgiler depoda aranıp kontrol edilmeden kullanıcıdan tekrar istenmez.
- Kullanıcı beyanı, üretici belgesi, hipotez, hesap ve ölçüm sonucu ayrı tutulur; commit sonrası dosyalar yeniden okunur, test/CI çalışmadıysa açıkça yazılır.

## Bildirilen stok

| Bileşen | Adet / özellik | Kaynak |
|---|---:|---|
| SCT013-030 (30 A / 1 V) | 7 | Kullanıcının verdiği envanter bilgisi; jack çıkışlı |
| SCT013-100A-1V | 10 | Kullanıcı bildirimi; jack çıkışlı |
| SCT013 toplamı | 17 | Kullanıcının verdiği envanter bilgisi |
| ESP32-C3 SuperMini | 1 | Envanter kaydı / önceki SSR düğümü |
| ESP32 ölçüm düğümü | 1 | Envanter kaydı / önceki PZEM düğümü |
| PZEM-004T | V3.0 | Kullanıcı bildirimi |
| Masaüstü güç kaynağı | 5 V / 1,8 A | Kullanıcı bildirimi |
| Test yükleri | 100 W ve 150 W ampuller ana deney yükleri; 5 W LED ampul farklı PF için | Planlanan test yükleri; gerçek güç, akım ve PF ilgili testte ölçülecek |
| Breadboard bias alt devresi | Mevcut kayıt: 2 × 10 kΩ ve Vmid–GND arasında 104 (100 nF); ilk SCT bağlantılı ölçümden önce aynı noktalara paralel 10 µF elektrolitik eklenmesi planlandı (pozitif Vmid, negatif GND) | Mevcut durum kullanıcı bildirimi; değişiklik bekliyor |
| Jack yuvaları ve bağlantı/ölçüm parçaları | Tam takım mevcut | Kullanıcı bildirimi |

## Mevcut bilgi
- Önceki BERO'daki SCT, PZEM, ESP32, MCP3208, SSR ve DS3231 teknik kaynakları proje referanslarına bağlandı.
- Bias üretim alt devresi, kullanıcının onayıyla tamamlandı sayılıyor; bağımsız voltaj ölçüm raporu eklenmedi.
- SCT013 sinyalinin breadboard bias devresi üzerinden ESP32'nin dahili ADC'sine alınması planlanıyor. 8 kanallı analog arayüz kartı mevcut değildir. MCP3208 sonraki aşamaya ayrılmıştır.
- PZEM için mevcut BERO kaydı kullanılıyor; bağlı CT modeli PZCT-02 (0–100 A) olarak belirtildi.
- SSR kartının tam giriş tetik mantığı ve fiziksel SSR parça kodu doğrulanmalı.
- Deneyler ve kalibrasyon sonuçları henüz eklenmedi.

## Karar kapıları
- [ ] G1 — SCT modeli PZEM referans akışına göre önceden belirlenen ±%4 hedefinde değerlendirildi; veri, sınırlamalar ve clipping durumu kaydedildi. Bu, bağımsız mutlak doğruluk kanıtı değildir.
- [ ] G2 — PZEM okuma durumu izleniyor; geçersiz okumalar özetlerden dışlanıyor.
- [ ] G3 — örnekleme hızı hedef yüklerde ölçülmüş metriklerle gerekçelendirilmiş.

## Sıradaki işler
1. [x] [T003 — PZEM tabanlı model hata hedefi](tasks/T003-reference-and-error-target.md): ±%4 bağıl sapma; Python geçerli örneklerde `OK` kararı verir.
2. [x] [T004 — Analog ön uç](tasks/T004-analog-frontend.md): mevcut jack/bias bağlantısı, SCT modelleri ve ESP32 dahili ADC yaklaşımı belgelendi.
3. [ ] [T005 — E01 gürültü tabanı](tasks/T005-noise-floor.md): donanım kurulduktan sonra yüksüz ADC verisini toplama ve grafikleme.
4. E00/E01 temel okumaları sonrasında [E08 SCT karakterizasyon planı](experiments/E08-sct-characterization/README.md) uygulanacak; E07 önceki, uygulanmamış plan olarak korunur.

## Açık engeller
- Donanım henüz kurulmadı. Gerçek bağlantı kurulurken SCT jack–breadboard bias bağlantısı ve ESP32 ADC pini uygulanacak donanımla eşleştirilecek; firmware/pin planlama aşamasında GPIO seçimi yapılacak. T004 kapsamında laboratuvar düzeyinde ADC aralığı/clipping hesabı istenmiyor.
- T005 için gerçek donanım kurulumundan sonra yüksüz veri toplama, süreyi belirleme ve grafik üretme bekleniyor.
- SSR'nin hangi iki AC yükü anahtarlayacağı, GPIO eşlemesi ve giriş mantığının düşük gerilimde doğrulanması.
- T003 TAMAMLANDI: model tahmini geçerli PZEM akımından ±%4 bağıl sapma içindeyse Python sonucu `OK` işaretler. Kararlı alan gözlemi ve SCT istatistikleri ayrı görev/deneylerde ele alınır. Test yükleri ilgili test kaydında beyan edilecek.

Firmware, deney ve kalibrasyon sonuçları henüz eklenmedi. E07 protokolü eklendi; kararlılık eşiği/pencere sayısı henüz belirlenmedi ve fiziksel test yapılmadı.

## Öncelikli ilk deney — E00A (2026-10-29)

E00A, E00/E01 hazırlığından önce gelir. E00A için ilk iki koşul bias trafosu L78L33 çıkışı ve Vmid'dir; her koşulda 30 saniyelik ADC gözlemi planlanır. Örnekleme hızı firmware aşamasında belirlenecek. Ortalama, min/max, tepe-tepe aralığı, standart sapma, gerçek süre ve örnek sayısı ana çıktılardır. Grafik yalnızca istatistikleri yorumlamak veya şüpheli örnekleri incelemek için üretilir. Farklı hızlar, üç ESP32 eşzamanlaması, yavaş oynatma, DMA veya çift buffer ilk kabul koşulu değildir. Fiziksel ölçüm yapılmadı.

## İlk test sıralaması — 2026-10-29

1. E00: SCT bağlı değil; bias orta noktası → ADC GPIO. `analogRead()` ham sayısı ve `analogReadMilliVolts()` aynı döngüde okunup voltmetreyle karşılaştırılacak.
2. SCT bağlı, ölçülen hatta akım yok: aynı iki okuma tekrar edilecek.
3. Ardından E01'in uzun yüksüz kayıt/grafik ve gürültü özeti yapılacak.

E00 protokolü: [Bias-only ADC baseline](experiments/E00-bias-adc-baseline/protocol.md). Henüz fiziksel ölçüm yapılmadı.

## 2026-10-29 belge incelemesi

- Kullanıcının sağladığı SCT013_30A_1V_ESP32_Raporu.docx ve ct-akım-trafosu-satürasyonu.txt okundu.
- SCT013-030 nominal oranı, gerilim çıkışlı modelde dahili burden bilgisi ve genel satürasyon riskleri donanım referanslarına eklendi.
- [ADR-007](docs/decisions/ADR-007-bias-midpoint-capacitor.md) kapsamında mevcut 100 nF kondansatöre paralel 10 µF eklenmesi, E00A'nın ilk SCT bağlantılı koşulundan önce planlandı. Fiziksel değişiklik ve sonuç ölçümü henüz yapılmadı; ADC GPIO'suna ek 100 nF kararı verilmedi.
- Rapordaki genel ESP32/ADS1115/RMS örnek kodları BERO firmware'i olarak alınmadı.
- Fiziksel ölçüm, ADC okuması, firmware testi ve kalibrasyon yapılmadı.


## Bias kondansatörü — aktif donanım notu

- Mevcut kayıtlı devrede bias orta noktasından GND'ye 104 (100 nF) bulunur.
- [ADR-007](docs/decisions/ADR-007-bias-midpoint-capacitor.md) 10 kΩ + 10 kΩ bölücü ve 50 Hz SCT sinyali için orta noktadaki mevcut 100 nF'ye paralel 10 µF eklenmesini önerir. Değişiklik E00A'nın ilk SCT bağlantılı koşulundan önce planlanmıştır; fiziksel olarak yapılana kadar tamamlandı sayılmaz.
- ADC pinine ayrıca 100 nF eklenmesi opsiyoneldir; ilk E01 ölçümünde aynı anda ikinci değişken eklememek için şimdilik planlanmadı.


## 2026-10-29 — E08 SCT karakterizasyon planı

Kullanıcıyla mutabık kalınan sıra E08 olarak kaydedildi: (1) SCT yüksüz uzun okuma ile temel gürültü/bias davranışı, (2) 100 W akkor ile 1/2/4 kablo turu × 1/2/2,5 kS/s matrisi, (3) aynı matrisin 150 W akkor ve 8,5 W LED'de tekrarı, (4) sonuçlar görüldükten sonra aç-kapa ve kararlı görünen bölgelerin incelenmesi. Her pencerenin aynı örneklerinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanır; yardımcı istatistikler ve gerçekleşen örnekleme hızı kaydedilir. PZEM/başka ESP ortalama akımı varsa genel koşul notudur; SCT ile zaman eşleştirmesi yapılmaz. Kararlılık eşiği, pencere sayısı ve kesin kayıt süresi önceden belirlenmez.

[E08 açıklaması](experiments/E08-sct-characterization/README.md) · [Protokol](experiments/E08-sct-characterization/protocol.md). E08 planlandı; fiziksel ölçüm yapılmadı. Aktif sıradaki iş hâlâ T005/E00-E01 yüksüz temel ölçüm hazırlığıdır; E08 bunun ardından uygulanacak.


## Model yaklaşımı — kapsam notu (2026-10-29)

BERO piyasaya sürülecek evrensel bir akım ölçer değildir. Evdeki sınırlı aygıt ve yüklerden zamanla büyüyen birleşik veri kümesi üzerinde öğrenen kişisel model hedeflenir. Eğitim kümesinde çok iyi sonuç veya aşırı öğrenme otomatik başarısızlık sayılmaz; hedef mevcut ev içi veri kümesine uyumu geliştirmektir. Eğitim sonucu, birleşik etiketli veri kümesi sonucu ve varsa eğitimde kullanılmamış kayıt sonucu ayrı raporlanır; bu ayrım ticari genelleme sertifikası için değil, gelişimi izlemek içindir.

Daha önce görülmemiş veya çok yüksek akımlı bir yükün ADC aralığını aşması, doygunluk oluşturması ya da modelin anlamlı tahmin üretememesi kabul edilebilir. Her yükü ölçmek şart değildir; bu durumlar kaydedilir ve ölçülmeyen akım için değer uydurulmaz. Ayrıntı: [proje felsefesi](docs/project-philosophy.md). Bu değişiklik yalnızca dokümantasyondur; model kodu ve fiziksel ölçüm yoktur.

## 2026-10-30 — PF fiziksel yorum ilkesinin yaygınlaştırılması

Düşük PF'nin aynı gerilim ve aktif güç koşulunda RMS akımı artırabileceği, BERO için yalnız E09 notu değil genel fiziksel yorumlama ilkesi olarak kaydedildi. Yüksek akım veya SCT genliği tek başına ölçüm hatası sayılmayacak; PZEM'in V/W/I/PF alanları ve yük türü birlikte değerlendirilecek. Sonuçlar yük/PF bağlamında raporlanacak; ±%4 kararlı alan uyum eşiği değiştirilmeyecek. PF-hata ilişkisi sebep-sonuç olarak varsayılmayacak.

İlke; [proje felsefesine](docs/project-philosophy.md), [PF teknik notuna](docs/architecture/pf-and-current-measurement.md), [SCT-PZEM etiketleme mimarisine](docs/architecture/sct-pzem-labeling-and-calibration.md), [E09](experiments/E09-pf-current-relationship/README.md), [E08 yük karşılaştırma aşamasına](experiments/E08-sct-characterization/stage-03-load-comparison.md) ve [analiz metriklerine](analysis/metrics.md) işlendi. Yalnızca dokümantasyon güncellendi; firmware, fiziksel test, ölçüm veya model değerlendirmesi yapılmadı. Aktif E00A → E00/T005/E01 → E08 sırası değişmedi.


## 2026-10-30 — E00A açılışı ve ilk referans verisi

- **HEDEF:** Bias trafosunun L78L33 çıkışı ve Vmid noktası için ESP32 ADC davranışını kısa, 30 saniyelik gözlemlerle incelemek.
- **LOG:** Kullanıcı L78L33 DC çıkışını multimetreyle 3,31 V ölçtüğünü bildirdi. Kayıt E00A results.md ve experiment.yaml içine KULLANICI BİLDİRİMİ olarak işlendi. Her ADC koşulunun süresi 30 saniye olarak güncellendi. Ayrı/geçici 10k/10k ölçüm bölücüsünün bias devresinin parçası olmadığı açıklandı.
- **SONUÇ:** İlk kaynak referansı var; ADC ölçümü yok. Gerçek ESP32-WROOM-32D kart/pinout, ADC attenuation ve giriş sınırları doğrulanmadan 3,31 V bağlantısı yapılmayacak. Firmware/derleme/ADC ham kayıt henüz yok.
- **Sonraki adım:** Gerçek kartı ve GPIO34 pinout'unu doğrula; ADC aralığına göre ölçüm bağlantısını kesinleştir; ardından iki koşul için 30 saniyelik kayıt al.


2026-10-30 ek kayıt: Kullanıcı bias breadboard orta noktasını multimetreyle 1,65 V okuduğunu bildirdi. Bu değer L78L33 çıkışından ayrı bir DC referans noktasıdır; ADC ölçümü değildir.


## 2026-10-30 — E00A ESP32D2 firmware kaydı

- **Durum:** KOD UYGULANDI; derleme/çalışma kullanıcı bildirimiyle raporlandı. Ölçüm sonucu bekleniyor.
- **Firmware:** [esp32d2-e00a-adc.yaml](experiments/E00A-raw-waveform-observation/firmware/esp32d2-e00a-adc.yaml).
- **Yapılandırma:** ESP-IDF; GPIO34 ADC raw; GPIO35 ADC voltaj; 12 dB attenuation; her sensör için 1 s güncelleme.
- **Kanıt:** Kullanıcı kodun derlendiğini ve çalıştığını bildirdi. Derleme/cihaz logu henüz paylaşılmadı.
- **Açık:** Fiziksel bağlantı düzeni, ADC sayısal değerleri, 30 saniyelik ham CSV, istatistik ve zaman grafiği.
- **Sonraki adım:** Kullanıcının göndereceği log ve sensör değerlerini incele; sonucu results.md'ye ekle.


**2026-10-30 — E00A-S01 GND referans testi:** Kullanıcının paylaştığı logda GPIO34 GND'de 0 count; GPIO35 yaklaşık 175 saniyelik kararlı bölümde 0.142 V gösterdi. Önceki açık giriş dalgalanması floating giriş teşhisini destekliyor. Bu sonuç ADC'nin tüm aralık doğruluğunu kanıtlamaz. Elektriksel çözüm adayı, jack/CT bağlantısı doğrulandıktan sonra ADC düğümünü Vmid'e yüksek değerli (ilk prototip değerlendirmesi 47–100 kΩ) dirençle biaslamak; kesin değer ve bağlantı henüz onaylanmadı. Ayrıntı: [E00A-S01 raporu](experiments/E00A-raw-waveform-observation/reports/E00A-S01-gnd-reference-stability.md). E00A açık; Vmid ve SCT testleri yapılmadı.


**2026-10-30 — E00A düzeltmesi:** GPIO34 count kanalı bağlı değildir; 0 count değeri GND testi kanıtı değildir ve yorum dışıdır. Yeni GPIO35 logu 1.678 V'tan başlayıp yaklaşık 25 saniyede 0.699 V'a düşüyor; kullanıcı Vmid'i multimetrede sabit yaklaşık 1.65 V DC olarak bildiriyor. ADC ile multimetre uyuşmazlığı var; kök neden henüz belirlenmedi. Önce GPIO35 pinindeki gerilim ESP32 GND referansıyla doğrudan ölçülürken eşzamanlı log alınacak. Kablo/ortak GND doğrulanmadan bias direnci veya yazılım filtresi eklenmeyecek. Ayrıntı: E00A results.md ve S01 raporu.


## E00A güncel adım — 2026-10-30

- **Adım 2:** GPIO35 voltaj sensörüne önceki GND logundaki 0.142 V tabanını çıkaran `max(0, x - 0.142)` filtresi eklendi; GPIO34 raw kanalı korundu.
- **Kod durumu:** Kullanıcı güncel firmware'in derlendiğini bildirdi (KULLANICI RAPORU). Kod commit'i `9eae26000a1dc460191bec68581cec0ac9ab9397`.
- **Hedef:** GND girişinde düzeltilmiş voltajı 0.000 V göstermek.
- **Henüz doğrulanmadı:** Güncel firmware ile alınmış GND logu yok. 0.142 V geçici ofset; genel ADC kalibrasyonu değil.
- **Sıradaki tek adım:** GPIO35 GND bağlantısındayken güncel logdan düzeltilmiş değerin 0.000 V olduğunu doğrula; sonra Vmid/multimetre karşılaştırmasına geç.



## E00A — Adım 2 güncel sonuç ve sıradaki kontrol (2026-10-30)

- **Sıfır kontrolü:** Kullanıcı logunda GPIO35 düzeltilmiş voltajı 49/49 kayıtta, yaklaşık 48 saniye boyunca 0.000 V. Kullanıcı Adım 2 hedefinin sağlandığını bildirdi.
- **GPIO34:** 0 count kayıtları fiziksel bağlantı olmadığı için yorum dışı.
- **Kod:** Değiştirilmeyecek.
- **Sıradaki işlem:** Aynı log oturumunda bias trafosuna enerji verilecek; GPIO35'in bias/Vmid altındaki düzeltilmiş voltajı izlenecek. Bias açık logu ve eşzamanlı multimetre değeri henüz bekleniyor.


## 2026-10-30 — E00A Adım 2 karar düzeltmesi
- **HEDEF:** GND sıfır gösterimi ile bias Vmid gerçek DC okuması arasındaki çelişkiyi çözmek.
- **LOG:** Ofsetli logda GND koşulunda 49/49 GPIO35 örneği 0.000 V. Bias açık logunda kararlı bölümün 85 filtreli örnek ortalaması yaklaşık 1.525 V; kullanıcı multimetre Vmid bildirimi 1.654 V. Çıkarılan 0.142 V geri eklendiğinde hesaplanan filtresiz tahmin yaklaşık 1.667 V; fark yaklaşık +0.013 V.
- **SONUÇ:** Sabit 0.142 V sıfırlama gerçek DC seviyeyi bozduğu için kaldırıldı. GND'deki 0.142 V gözlemi gizlenmeyecek. Ofsetsiz firmware depoya yazıldı; yeni derleme/cihaz testi henüz yapılmadı.
- **Sonraki tek adım:** Kullanıcı ofsetsiz YAML'ı derleyip cihaza yükleyecek; aynı Vmid koşulunda yeni log alınacak. E00A tamamlanmadı.


## 2026-10-30 — E00A RAW/voltaj karşılaştırma firmware'i

- **HEDEF:** GPIO34 RAW count değerinden nominal voltaj tahmini üretmek; GPIO35 ESPHome ADC voltajıyla karşılaştırmak ve aradaki işaretli farkı yayınlamak.
- **LOG:** Firmware'e GPIO34 RAW sensörü, `RAW × 3.1 / 4095` nominal voltaj tahmini, GPIO35 ofsetsiz ADC voltajı ve `GPIO35 - GPIO34 tahmini` fark sensörü eklendi. Kullanıcı yeni YAML'ın derlemeye alındığını bildirdi; derleme sonucu henüz bildirilmedi.
- **SONUÇ:** Değişiklik GitHub'a kaydedildi ve dosya yeniden okunarak doğrulandı. Derleme başarılı veya cihazda çalışıyor olarak henüz işaretlenemez. RAW dönüşüm katsayısı nominal tahmindir; kalibrasyon değildir.
- **Bağlantı koşulu:** Karşılaştırma için GPIO34 ve GPIO35 aynı 1.654 V Vmid noktasına bağlanmalı. GPIO34 bağlantısız kalırsa RAW voltajı ve fark sensörü geçerli karşılaştırma değildir.
- **Sonraki adım:** Derleme sonucunu al; başarılıysa cihaz yüklemesi ve aynı Vmid noktasında multimetre eşzamanlı logu.


## 2026-10-30 — E00A bias-only / SCT bağlı değil: RAW ve voltaj ilk karşılaştırma logu

### HEDEF
SCT bağlamadan bias Vmid noktasını ESP32D2'nin GPIO34 RAW ve GPIO35 ADC voltaj kanallarında gözlemek; multimetre bildirimi olan 1.654 V ile karşılaştırmak. Sonraki uzun logda RAW ve voltaj serilerinin korelasyonunu incelemek için başlangıç gözlemi oluşturmak.

### LOG
- Kaynak: Kullanıcının paylaştığı `Yapıştırılan metin(20261030-123911).txt`; ESPHome 2026.9.1; ESP32 rev3.1; cihaz `esp32d2`; log bağlantısı 192.168.0.66.
- ADC GPIO34 (ADC1_CH6) ve GPIO35 (ADC1_CH7) başlatma, konfigürasyon ve kalibrasyon durumları OK; iki sensörün güncelleme aralığı 1 s.
- Kullanıcının multimetre bildirimi: Vmid = **1.654 V**. Bu değer kullanıcı raporudur; bu logda multimetre ölçümünün zaman damgası yoktur.
- İlk bölümde GPIO34 RAW = 0 count ve GPIO35 = 0.142 V görülüyor. Ardından GPIO34 yaklaşık 1837–1871 count bölgesine geçiyor; GPIO35 de yaklaşık 1.65–1.68 V bandına oturuyor.
- Kararlı görünen bölümde (yaklaşık 15:37:46–15:39:03): GPIO34 RAW gözlemi yaklaşık 1829–1871 count; RAW nominal voltaj tahmini yaklaşık 1.385–1.416 V; GPIO35 ADC voltajı yaklaşık 1.650–1.679 V; fark sensörü yaklaşık +0.250…+0.294 V.
- RAW nominal tahmini firmware formülüdür: `count × 3.1 / 4095`; kalibre edilmiş voltaj değildir.
- Logda iki kanalın yayınları aynı saniyede ve aynı anda gerçekleşmiyor; GPIO34 ve GPIO35 ayrı ADC kanallarıdır. Bu nedenle bu kısa kayıt tek başına örnek-örnek korelasyon katsayısı veya tam eşzamanlılık kanıtı değildir.
- Logda trafo enerjilendirme anı ayrıca işaretlenmediğinden, ilk geçişi belirli bir trafo ON/OFF zamanına atamıyoruz. Kullanıcının gözlemi: kondansatörlerle birlikte değerler belirgin biçimde oturuyor.

### SONUÇ
- Bias-only gözleminde GPIO35 voltaj okuması kararlı bölümde kullanıcının bildirdiği 1.654 V multimetre değerine yakındır (yaklaşık 1.650–1.679 V).
- Aynı kararlı bölümde GPIO34 RAW'dan nominal hesaplanan voltaj yaklaşık 1.4 V'tur ve GPIO35'ten yaklaşık 0.27 V düşüktür. Bu fark henüz nedenlendirilmemiştir; RAW dönüşüm katsayısı nominaldir ve iki kanal ayrı ADC okumalarıdır.
- Bu test SCT davranışını, akım ölçümünü veya bias devresinin SCT yükü altındaki davranışını göstermez. Yalnızca SCT'siz bias/ADC zincirinin ilk karşılaştırmasıdır.
- Kullanıcının sonraki adımı: daha uzun RAW + voltaj logu paylaşmak. O kayıtta zaman serilerini eşleştirip korelasyon (Pearson ve/veya Spearman), eğim/kesişim, fark ve kararlı/geçiş bölümlerini inceleyeceğiz. Ham logdaki örnekleme zamanları korunmalı; farklı zaman damgaları körlemesine satır satır eşleştirilmeyecek.
- E00A tamamlanmadı; bu kayıt ön gözlemdir.


## 2026-10-30 — Güncel SCT'siz deney kapanışı

SCT bağlı değilken bias Vmid koşulunda son log analiz edildi ve bu alt deney kapatıldı. 603 geçerli zaman eşleşmesi; GPIO35 1.665138 V ortalama / 6.474 mV std; GPIO34 RAW 1846.80 count ortalama / 6.97 count std. Pearson r=-0.0201. RAW sıfır başlangıç kayıtları eşleştirmeye alınmadı. Bu sonuç ADC'ye özgü gürültü değil, SCT'siz bias+bağlantı+ADC ölçüm zincirinin gözlenen dalgalanmasıdır. E00A'nın 3.3 V ayrı bölücü koşulu ve ham CSV/zaman grafiği tamamlanmadığı için E00A bütünü açık kalır. Sıradaki teknik koşul: SCT bağlı, ölçülen hatta akım yok; önceki tabanla karşılaştırma.


## 2026-10-30 — E00B açıldı: SCT bağlı, akımsız hat ADC gözlemi

- Bias referans kanalları korunuyor: GPIO34 RAW (ADC1_CH6), GPIO35 voltaj (ADC1_CH7).
- SCT kanalları önerisi: GPIO32 RAW (ADC1_CH4), GPIO33 voltaj (ADC1_CH5).
- Kart adayı ESP32-WROOM-32D; gerçek geliştirme kartı pinout'u doğrulanmadan bağlantı yapılmayacak.
- Öncelikli sensör SCT013-030 (30 A / 1 V). Harici ADC kullanılmıyor.
- Deney PLANLANDI; firmware, fiziksel bağlantı, derleme ve ölçüm henüz yapılmadı.
- Ayrıntı: [E00B README](experiments/E00B-sct-connected-no-current/README.md), [experiment.yaml](experiments/E00B-sct-connected-no-current/experiment.yaml), [results.md](experiments/E00B-sct-connected-no-current/results.md).


## 2026-10-30 — E00B firmware derlemesi bildirildi
- **Durum:** HAZIRLANDI / DERLENDİ (KULLANICI RAPORU). E00B firmware'i depoya eklendi: [esp32d2-e00b-sct-no-current.yaml](experiments/E00B-sct-connected-no-current/firmware/esp32d2-e00b-sct-no-current.yaml).
- **HEDEF:** SCT bağlı/primer akımsız gözlem için dört ADC kanalını (GPIO34/35 bias, GPIO32/33 SCT) tek firmware'de toplamak.
- **LOG:** Kullanıcı 2026-10-30 tarihinde kodun derlendiğini bildirdi. Firmware commit: `20fbe9b4a99d057ef579d882bfd83d23f4ef199e`. ESPHome yayın aralığı 1 s; yüksek hızlı ham örnekleme değildir.
- **SONUÇ:** Derleme başarılı kullanıcı raporudur. Cihaza yükleme, gerçek pinout/fiziksel bağlantı ve deney ölçümü henüz doğrulanmadı. E00B TAMAMLANDI değildir.
- **Sonraki adım:** Gerçek kart pinout'unu doğrula; ardından güvenli fiziksel bağlantı ve cihaz logu.


## 2026-10-30 — E00B ilk cihaz logu kaydedildi
- **Durum:** CİHAZ LOGU ALINDI; fiziksel koşulların tam doğrulaması bekliyor.
- **HEDEF:** Dört ADC kanalının cihaz üzerinde çalıştığını ve SCT bağlı/akımsız koşulun ilk gözlemlerini kaydetmek.
- **LOG:** ESPHome 2026.9.1 / ESP32 rev3.1; GPIO34/35/32/33 ADC1 başlatma ve kalibrasyon OK. Kararlı bölüm 16:20:41 sonrası, 110 örnek/kanal. Bias RAW ortalaması 1854.14 count; SCT RAW 1853.45 count. Bias voltaj 1.6651 V; SCT voltaj 1.6639 V. İlk açılış geçişindeki 0 count ve 0.142 V değerleri analiz dışı bırakıldı.
- **YORUM:** Bias ve SCT kanalları bu log kesitinde birbirine yakın. Nominal RAW voltaj tahmini ile kalibre ADC voltajı arasındaki yaklaşık 0.25 V fark fiziksel devre düşümü olarak yorumlanamaz.
- **SONUÇ:** Cihaz bağlantısı ve dört ADC kanalının başlatılması doğrulandı. Primer akımın sıfır olduğu ve fiziksel SCT bağlantısı yalnız logdan bağımsız doğrulanamıyor.
- **Sonraki adım:** Fiziksel kurulum/akımsız koşulu not et ve daha uzun kararlı kayıt al.
- **Kayıt:** [E00B results](experiments/E00B-sct-connected-no-current/results.md), [ham log](experiments/E00B-sct-connected-no-current/logs/2026-10-30-e00b-esp32d2-startup-and-observation.log).


## 2026-10-30 — ESP32D2 / SCT013-030 hazır ct_clamp yapılandırması kaydedildi

- **Durum:** UYGULANDI (GitHub depo kaydı). Kullanıcının paylaştığı ve cihaz loglarında çalıştığı görülen ESPHome yapılandırması `firmware/esp32d2.yaml` dosyasına kaydedildi. Bu oturumda yeniden derleme veya cihaza yükleme yapılmadı.
- **HEDEF:** Hazır ESPHome `ct_clamp` paketiyle çalışan temel ölçüm yapılandırmasını, tek seferlik 24.22 katsayısını ve mevcut bağlantı/örnekleme ayarlarını kaybetmeden korumak.
- **LOG:** ESP32D2 kimliği korunmuştur. SCT013-030 → mevcut yaklaşık 1.65 V bias → GPIO33; ADC1 / 12 dB; `sample_duration: 200ms`; `update_interval: 2s`; katsayı 24.22; yayın eşiği 0.35 A. 150 W akkor testinde pens 0.616 A / ESP32 yaklaşık 0.615 A; kettle düşük akım kesitinde yaklaşık 0.637 A / 0.656 A; kettle kaynama kesitinde pens 6.39 A / ESP32 yaklaşık 6.15 A. 8.35 W LED'de pens 0.041 A iken 0.35 A eşiği nedeniyle yayınların çoğu 0.000 A; ara sıra 0.508 A ve 0.372 A sıçramaları görüldü. Bu ölçüm ve pens değerleri kullanıcı raporu/loglarıdır.
- **SONUÇ:** 150 W ve kettle koşullarında gözlenen farklar yaklaşık ±%4 hedefinin içinde. 41 mA LED akımı mevcut eşik tarafından bastırıldığı için düşük akım kabiliyeti henüz gösterilmedi. Katsayı değiştirilmedi. Kod açıklamasındaki ilk 0.30 A ifadesi, lambda'nın fiilen uyguladığı 0.35 A ile tutarlı olacak şekilde depo kopyasında düzeltildi; çalışan lambda mantığı değiştirilmedi.
- **Kayıt:** [firmware/esp32d2.yaml](firmware/esp32d2.yaml), [firmware/README.md](firmware/README.md).
- **Açık kalan:** Ham test loglarının kalıcı dosya olarak eklenmesi ve 0.35 A eşik davranışının düşük akım için değerlendirilmesi. Bu kayıt E00A/E00B/E08 planlarının kabul ölçütlerini tamamlamaz veya fiziksel doğrulama iddiası oluşturmaz.


## 2026-10-30 — Kettle ölçüm karşılaştırmaları rapora eklendi

- **Durum:** UYGULANDI — rapor ve durum kaydı GitHub'a yazıldı.
- **HEDEF:** Bu sohbet içinde paylaşılan kettle pens/ESP32 karşılaştırmalarını koşullarına göre ayrı kaydetmek; belirsiz 0.437 A bildirimini doğrulanmış kettle sonucu gibi göstermemek.
- **LOG:** Kettle düşük/kararlı kesiti: pens 0.637 A, ilk 20 ESP32 yayınının ortalaması yaklaşık 0.656 A (+%3.0). Kettle kaynama kesiti: pens 6.39 A, 22 ESP32 yayınının ortalaması yaklaşık 6.15 A (−%3.8). Daha sonraki ayrı logda pens 0.437 A bildirilmiş; 74 ESP32 yayınının ortalaması 0.664 A, son 0.910 A sıçraması çıkarıldığında 0.660 A. Bu son kaydın yük/koşul eşleşmesi teyit edilmediğinden kettle olarak sınıflandırılmadı.
- **SONUÇ:** İlk iki kettle kesiti kullanıcı tarafından belirlenen ±%4 sınırının içinde; kaynama kesiti sınıra yakındır. 0.437 A bildirimi ile log arasında yaklaşık +%52 fark vardır, ancak eşzamanlı ve aynı yük koşulu doğrulanmadan teknik sonuç çıkarılamaz. Katsayı 24.22 ve lambda eşiği 0.35 A değiştirilmedi.
- **Açık kalan:** 0.437 A pens okumasının hangi yük/koşula ait olduğu ve logla eşzamanlı olup olmadığı.
- **Kanıt:** [Firmware ve ölçüm raporu](firmware/README.md); [YAML](firmware/esp32d2.yaml).
