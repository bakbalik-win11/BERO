# Deney ve karar izleme defteri

> **Bu dosyanın amacı:** Deney kodunu, deneyin neden yapıldığını, alınan kararları ve kanıtlanan sonucu birbirinden koparmamak. Bu dosya bir navigasyon/özet defteridir; ayrıntılı protokol, kod ve sonuç kayıtlarının yerine geçmez.

## Her basamakta korunacak kayıt

Her deney veya teknik adım için şu sorular cevaplanır:

1. **Neden?** Hangi belirsizliği veya pratik sorunu çözmeye çalışıyoruz?
2. **Soru ve hipotez:** Deney hangi soruya cevap verecek; beklenti varsa bunun hipotez olduğu açık mı?
3. **Karar ve gerekçe:** Neyi seçtik, hangi alternatifleri neden şimdilik seçmedik?
4. **Uygulama:** Gerçekte kullanılan kart, pin, devre, firmware/kod sürümü ve ayarlar neler?
5. **Kanıt:** Ham dosya, log, hesap veya gözlem nerede? Yapılmayan kontroller açıkça yazılmış mı?
6. **Sonuç:** Kanıt neyi destekliyor, neyi desteklemiyor?
7. **Sonraki basamak:** Sonuç nedeniyle hangi adım seçildi ve neden?

**Kural:** Kod/protokol dosyasının depoda bulunması, kodun çalıştığı veya deneyin yapıldığı anlamına gelmez. “Planlandı”, “kodlandı”, “derlendi”, “kartta çalıştırıldı”, “ölçüldü” ve “sonuç yorumlandı” ayrı durumlar olarak kaydedilir. Sonuç çıkmadıysa bu da açıkça yazılır.

## Kod ile açıklama arasındaki bağ

- Deneyin **sorusu, gerekçesi ve adımları**: ilgili deneyin `README.md` / `protocol.md` dosyaları.
- Deneyin **kısa kimliği ve planlanan koşulları**: ilgili `metadata.yaml` ve varsa `experiment.yaml`. YAML dosyalarının firmware tarafından otomatik okunduğu varsayılmaz.
- Deneyin **gerçek uygulama kodu**: kod gerçekten oluşturulduğunda firmware/yazılım dosyasının tam depo yolu bu deftere ve deneyin protokolüne eklenir. Kod henüz yoksa “uygulama kodu henüz oluşturulmadı” denir; dosya yolu uydurulmaz.
- Deneyin **gerçek uygulama kaydı ve sonuçları**: ilgili deneyin `results.md`; ham veri varsa yerel `data/raw/` yolunda tutulur ve varsayılan olarak Git'e eklenmez.
- Deneyin **karar gerekçesi**: değişmeyen tasarım kararıysa ilgili ADR; yalnızca o deneye özgü seçimse deney protokolü ve oturum günlüğü.
- Depodaki **son durum ve sıradaki tek adım**: `STATUS.md`; büyük resim ve gezinme için `PROGRESS_TREE.md`.

## Basamak defteri

| Basamak | Neden yapılıyor? | Karar / gerekçe | Uygulama ve kanıt durumu | Sonraki karar kapısı |
|---|---|---|---|---|
| Hazırlık: envanter ve kapsam | Eldeki donanımı ve projenin sınırlarını bilmek; yanlış varsayımla kod yazmamak | İlk aşamada ESP32 dahili ADC; MCP3208 sonraya. Proje enerji/güç kalitesi analizörü değil | Donanım ve kararlar belgelenmiş; bazı bilgiler kullanıcı beyanına dayanır. Bağımsız fiziksel doğrulama olduğu varsayılmaz | Gerçek kart ve ADC pinini fiziksel pinout ile eşleştir |
| E00A — ham ADC gözlemi | SCT bağlanınca ham ADC dağılımının bias-only ve yüksüz duruma, ardından 100 W akkor yük koşuluna göre değişip değişmediğini görmek | İlk geçişte tek ESP32, 2 kS/s hedefi ve yaklaşık 1 s/koşul; önce temel istatistikler, grafik yalnız gerektiğinde | **PLANLANDI.** Firmware/uygulama kodu, kayıt ve fiziksel ölçüm henüz yapılmadı. Protokol: [E00A](experiments/E00A-raw-waveform-observation/README.md). CSV planı ve yerel yollar protokolde | Kart/GPIO pinout'u ve fiziksel bias düzeni doğrulandıktan sonra ilk ham kayıt |
| E00 — bias ADC API karşılaştırması | SCT bağlı değilken ham ADC sayısı ile mV API'sinin ne gösterdiğini anlamak | Temel, anlaşılır bir okuma; SCT'li koşuldan ayrı tut | **PLANLANDI.** Kod ve ölçüm henüz yok. [Protokol](experiments/E00-bias-adc-baseline/protocol.md) | E00A gözlemi ve fiziksel hazırlık sonrası gerçek okumaları kaydet |
| T005 / E01 — yüksüz temel okuma ve gürültü | Yüksüz sinyalin zaman içindeki davranışını görmek | Uzun kayıt, ilk kısa gözlemlerden sonra; gereksiz analiz eklememek | **PLANLANDI.** Fiziksel ölçüm yok. [T005](tasks/T005-noise-floor.md) | E00/E00A kanıtı temel kayıt planını destekliyor mu? |
| E08 — SCT karakterizasyonu | Önceki temel adımların ardından yük, kablo turu ve örnekleme hızı değişimlerinin etkisini incelemek | Temel hazırlıklar tamamlanmadan öne alınmayacak; E07 eski/uygulanmamış plan olarak kalır | **PLANLANDI.** Ölçüm yok. [E08](experiments/E08-sct-characterization/README.md) | Yalnız önceki sonuçlar ihtiyaç gösterirse uygulanır |

## Deney kodu eklendiğinde zorunlu bağlantı

Her yeni kod dosyası için:
- Dosya yolu ve ilgili commit/sürüm kaydedilir.
- Kodun hangi deney adımını gerçekleştirdiği belirtilir.
- Derleme kontrolü ile fiziksel çalıştırma birbirinden ayrılır.
- Kullanılan gerçek kart/GPIO ve ayarlar deney LOG'una yazılır.
- Sonuçlar ham veri veya log ile ilişkilendirilir.
- Sonraki kararın hangi bulguya dayandığı belirtilir.

## Kanıt ve durum dili

- **PLANLANDI:** soru, gerekçe ve kabul koşulu belirlendi; uygulama yapılmış demek değildir.
- **KODLANDI:** kod depoda mevcut; derlendiği veya çalıştığı anlamına gelmez.
- **DERLENDİ:** belirtilen ortamda derleme sonucu kaydedildi.
- **UYGULANDI:** hedef dosya/değişiklik depoya işlendi; fiziksel deney yapıldığı anlamına gelmez.
- **ÇALIŞTIRILDI:** kodun belirtilen donanım/yazılım ortamında çalıştırıldığına dair kayıt var.
- **ÖLÇÜLDÜ:** protokol, koşul ve veri/log ile gözlem kaydedildi.
- **YORUMLANDI:** sonuç ve sınırlamalar kanıta dayalı olarak yazıldı.

Bu durumlar birbirinin yerine kullanılamaz. Önceki kararlar silinmez; karar değişirse eski gerekçe ve değişiklik nedeni tarihçede korunur.

## Kapsam düzeltmesi — kullanıcının asıl ilk hedefi (2026-10-29)

**Öncelik:** Kullanıcı önce akım formülü/kalibrasyon yapmak değil, SCT013 → ESP32 dahili ADC hattında ne okunduğunu görmek ve anlamak istiyor.

İlk öğrenme soruları:
1. ADC'den hangi ham sayılar okunuyor?
2. Ham örnekleri bilgisayarda görselleştirebiliyor muyuz?
3. Bir kayıt/paket sinyal davranışını temsil etmeye yeterli mi; kayıt sırasında belirgin bilgi kaybı var mı?
4. Gözlemden çıkan bir sonraki soru nedir?

**Kapsam dışı — ilk ham gözlem aşamasında:** PZEM karşılaştırması, akım formülü/kalibrasyon, MCP3208, enerji analizi ve gereksiz karmaşık edinim mimarisi. Bunlar sırf proje dosyalarında geçtiği için ilk adıma eklenmez; ancak ileride somut bir soru gerektirirse yeniden ele alınabilir.

**İlk aşama başarı ölçütü:** Gerçek ESP32 ADC ham örneklerini kaydedebilmek, bunları bilgisayarda görselleştirebilmek ve seçilen kayıt/paketin neyi gösterdiğini ve neleri kanıtlamadığını açıklayabilmek. Bu aşamada ham ADC sayıları amper değeri değildir; akım hesaplandığı veya kalibre edildiği iddia edilmez.

**Durum:** Bu, kapsam ve öncelik düzeltmesidir; bugün firmware yazılmadı, kart çalıştırılmadı ve ölçüm yapılmadı. Mevcut E00A protokolü uygulanmaya başlamadan önce bu hedefe göre sadeleştirilip uyumlu hâle getirilecek.


## Proje felsefesi düzeltmesi — kişisel veri kümesi ve aşırı öğrenme (2026-10-29)

Kullanıcının açıkladığı hedef: BERO piyasaya sürülecek evrensel bir akım ölçer değil; evdeki sınırlı aygıt ve yüklerden zamanla büyüyen birleşik veri kümesi üzerinde öğrenen kişisel bir modeldir. Modelin eğitim verisinde çok iyi sonuç vermesi, hatta aşırı öğrenme (overfitting), bu proje için otomatik bir kusur veya başarısızlık sayılmaz. Amaç gözlenen ev içi aygıtlara uyumu zamanla geliştirmektir.

Yeni kayıtlar, etiketler, analizler ve model sürümleri izlenebilir biçimde korunacak; yeni model sonuçları önceki sürümlerle karşılaştırılacaktır. Eğitim sonucu, birleşik etiketli veri kümesi sonucu, varsa ayrılmış kayıt sonucu ve etiketsiz kayıtların davranış incelemesi birbirinden ayrı raporlanır. Bu ayrım ticari sertifikasyon amacı taşımaz; model gelişimini dürüstçe izlemek içindir.

Daha önce görülmemiş veya olağan dışı yüksek akımlı bir yükün (ör. ev tamiratında kullanılan kaynak makinesi) ADC aralığını aşması, doygunluk oluşturması veya modelin tahmin üretememesi kabul edilebilir. Her yükü ölçmek proje şartı değildir. Böyle bir olayın doygunluk/başarısızlık davranışı kayıt altına alınabilir; ölçülmeyen akım için değer uydurulmaz.

Ayrıntılı ve kalıcı yaklaşım: [BERO proje felsefesi](docs/project-philosophy.md).

**Durum:** Felsefe ve plan dokümantasyonu güncellendi; model kodu, akım hesabı, fiziksel ölçüm veya doğrulama yapılmadı.


## Uzun vadeli vizyonun genişletilmesi (2026-10-29)

BERO'nun yönü tek bir akım ölçerle sınırlı değildir. Kullanıcı, eldeki MCP ve Modbus modülleri ile farklı ESP32 seçeneklerinin (ileride ESP32-P4 dahil olabilir) göreve göre kullanılabileceğini; akım okuma/tahmin, PZEM referansıyla etiketleme ve yeterli veriye dayalı model/katsayı güncelleme hattının gelecekte kurulabileceğini belirtti. Bu, henüz uygulanmış mimari değil, uzun vadeli vizyondur.

Daha ileri örnek fikirler: çamaşır makinesinde ses örüntüsünden su alma başlangıcını algılamak veya su akış sensöründen boşaltma olayını belirlemek. Bunlar seçilmiş görev veya doğrulanmış özellik değildir; farklı sensör ve donanımla belirli bir işi başarıyla yapan özelleşmiş ESP düğümleri fikrini anlatır.

**Ortak ilke:** Donanım/sensör göreve göre değişebilir; her düğümün başarısı kendi görev verisi ve açık kabul ölçütleriyle değerlendirilir. İlk adıma tüm donanım ve görevleri eklemiyoruz.

**Aktif basamak değişmedi:** E00A ile ESP32 dahili ADC ham örneklerini oku, kaydet ve bilgisayarda görselleştir. MCP/Modbus/P4 entegrasyonu, akım tahmini, PZEM etiketleme ve kendini yeniden eğiten veri hattı gelecekteki işlerdir.

Ayrıntı: [Proje felsefesi](docs/project-philosophy.md).


## E09 — PF koşulu ile SCT/PZEM akım karşılaştırması (planlandı)

PZEM'in yayınladığı PF, PZEM'in doğrudan hat gerilimi ölçümü ve CT üzerinden akım ölçümüyle ilişkili birleşik bir sonuç olarak ele alınır. E09'da PZEM gerilim, akım, aktif güç ve PF alanları birlikte kaydedilecek; SCT özellikleri ve SCT-PZEM akım farkı yük/kararlı alan bağlamında incelenecektir. Düşük PF'li yükte daha yüksek SCT akım genliği otomatik hata sayılmaz. PF ile hata arasındaki ilişki gözlem olarak raporlanır; doğrudan sebep-sonuç varsayılmaz. İlk model PF'siz denenir; gerekirse aynı koşullarda PF girdili modelle karşılaştırılır.

**Deney:** [E09 — PF koşulu ile SCT/PZEM akım karşılaştırması](experiments/E09-pf-current-relationship/README.md). E09 uzun vadeli plan olarak eklendi; E00A → E00/T005/E01 → E08 aktif sırası değişmedi. Fiziksel ölçüm yapılmadı.

## 2026-10-30 — PF fiziksel yorum ilkesi ve sonuç değerlendirme

**Fiziksel dayanak:** Aynı gerilim ve aktif güç koşulunda düşük PF daha yüksek RMS akıma yol açabilir. Bu nedenle yüksek akım veya SCT genliği tek başına ölçüm hatası değildir.

**Karar:** PZEM gerilim, aktif güç, akım ve PF değerleri yük türüyle birlikte kaydedilir. SCT-PZEM farkı ve ±%4 eğitim verisi içi uyum aynı yük/ortak kararlı alan bağlamında değerlendirilir. `OUT_OF_RANGE` sonucu doğrudan PF'ye bağlanmaz; yükün fiziksel davranışı, SCT/ADC zinciri ve PZEM güncelleme davranışı ayrı ayrı incelenir. PF-hata ilişkisi gözlem olarak raporlanır, nedensellik varsayılmaz.

**Kapsam:** Proje felsefesi, PF teknik notu, etiketleme mimarisi, E09, E08 yük karşılaştırma aşaması ve analiz metrikleri bu ilkeye göre güncellendi. E00A → E00/T005/E01 → E08 aktif sırası korunur. Değişiklik dokümantasyondur; deney/ölçüm/model çalıştırması yapılmadı.
