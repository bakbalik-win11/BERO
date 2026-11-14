## E24 — Çoklu ADS1115 / 12 SCT simetrik düğüm mimarisi (PLANLANDI)
- Hedef taslak: iki aynı ESP32 ölçüm düğümü; her birinde 3 ADS1115, 6 SCT kanalı ve bir RS485 dönüştürücü; toplam 12 SCT.
- Kullanıcı, her ADS1115 için ayrı SDA/SCL çifti istiyor. İlk fiziksel test modül imalatından önce eldeki iki ADS1115 ile yapılacak; birinin önceki testte çalışmamış olabileceği yeniden kontrol edilecek.
- Klasik ESP32'de iki donanımsal I²C kontrolcüsü vardır. Üç ADS için üçüncü bağımsız hat gereksinimi; yazılımsal I²C, I²C çoklayıcı veya farklı bağlantı mimarisi seçenekleriyle test edilmeden kesinleşmiş değildir.
- İlk iki ADS testi; ayrı modül kontrolü, iki I²C bus üzerinden aynı ESP'de okuma, dönüşüm/okuma süresi, hata ve veri kaybı kaydı içerir.
- Test sonrası kullanıcı 10 ADS1115 yedek stok siparişi planlıyor; sipariş/teslim henüz gerçekleşmedi.
- [E24 deney ve mimari planı](experiments/E24-ads1115-multi-bus-expansion/README.md).
## E23 — ADS1115 sıçrama araştırmasının yeni modülle sürdürülmesi (PLANLANDI)
- E19'un 2026-11-14 enerjili-hat/yüksüz-iletken uzun kayıt istatistikleri kapanmıştır; ancak sıçramaların fiziksel nedeni çözülmüş değildir.
- Kullanıcı kararı: Aç/kapa mekanizması ve ilgili kodlar mevcut düzenden çıkarılıp yeni modül yapısı kurulduktan sonra uzun süreli yüksüz kayıt alınacak; sonuçlar E19 baseline'ıyla karşılaştırılacaktır.
- Kullanıcı fiziksel koşulu: gözlenen hatta aç/kapa yapılmıyor ve röle bu hatta bağlı değil; anahtarlama başka bir ESP üzerinden gerçekleşiyor. Bu nedenle önceki HA switch state zaman yakınlığı fiziksel röle etkisi/ölçülen hattın anahtarlanması kanıtı olarak yorumlanmayacaktır.
- Yeni modülün gerçek bağlantı ve yazılım ayarları test öncesi kaydedilecek. Önceki ve yeni düzenek farklıysa farklar karşılaştırmada açık tutulacak.
- Durum: **E23 PLANLANDI**; modül, kayıt, analiz ve sonuç henüz yok. E21 çamaşır makinesi analizi gibi mevcut hedefleri kendiliğinden iptal etmez; ayrı teknik araştırma olarak izlenir.
- [E23 protokolü](experiments/E23-ads1115-spike-new-module-comparison/README.md).

## Sonraki donanım tasarımı — tek ESP32 ölçüm düğümü (PLANLANDI)

Kullanıcının 2026-11-13 tarihli kararı:
- Tek ESP32 üzerinde iki SCT kanalı.
- Bir ADS1115.
- PZEM-004T V3 aynı ESP32'ye UART üzerinden bağlanacak.
- Harici bias devresi olmadan ölçüm hedefleniyor.
- 1 saniye yayın; yazılımsal alt eşik ve spike filtresi yok, ham ölçüm korunacak.

Bu aşama yalnız mimari planıdır. Kart/Modül 1 pinleri, UART TX/RX, I²C pinleri/adresi, ADS1115 giriş eşlemesi, kanal tarama zamanlaması, PZEM güncelleme sıklığı ve ADS1115 ortak-mod/giriş ray güvenliği doğrulanmadan YAML hazırlanmış veya entegrasyon tamamlanmış sayılmaz.

Ön koşul: ADS1115 enerjili-yüksüz gözleminden ayrı olarak ölçülen hattın enerjisiz olduğu taban testi yapılacak. İki test ayrı raporlanacak. [13 Kasım filtresiz gözlem raporu](logs/ads1115/2026-11-13-E19-energized-no-load-unthresholded-observation.md).

## Güncel çalışma hedefi — Çamaşır makinesi program davranışı analizi

### Sonraki bakım işi — ON/OFF olay altyapısının aktif koddan çıkarılması

Kullanıcı kararı: ON/OFF olay mekanizmasına artık ihtiyaç yoktur. Modül 2, Modül 3 ve ilişkili aktif kodlar taranarak UDP olay gönderme/alma, olay çözümleme, BOOT_ID/EVENT_ID/STATE alanları, olay entity'leri ve yalnız bu akışa bağlı yardımcı kodlar kaldırılacaktır. Akım ölçümü, sensör okuma ve Home Assistant ölçüm/veri kayıt akışı korunacaktır. Tarihsel ADR'ler, deney protokolleri, loglar ve arşiv kodları kanıt/tarihçe olarak silinmeyecektir. Bu iş henüz uygulanmamıştır; kaldırma öncesi bağımlılık taraması, sonrasında derleme ve gerçek cihaz doğrulaması gerekir.


<badge color="success"> AKTİF HEDEF </badge>

Önceki PZEM kararlı-alan eşleştirmesiyle eğitim/kalibrasyon üretme iş akışı, kullanıcının 13 Kasım 2026 tarihli kararıyla kapatılmıştır. Mevcut SCT-013 + ADS1115 zincirinin farklı yük ve akım seviyelerindeki pratik gözlemleri hedefi karşılamıştır. Bu karar geçmiş deneylerin silinmesi veya ölçüm zincirinin laboratuvar düzeyinde doğrulanması anlamına gelmez.

**Yeni hedef:** Çamaşır makinesinin seçilen bir programını baştan sona akım zaman serisiyle izlemek; çalışma evrelerini, sürelerini, geçişlerini ve tekrar eden örüntülerini tanımak.

- İlk adım tek bir tam programın ham HA geçmişini kaydetmek.
- Program adı, sıcaklık, sıkma devri, seçenekler ve yaklaşık yük kullanıcıdan kaydedilecek.
- Evre adları yalnız akım eğrisinden kesin varsayılmayacak; kullanıcı gözlemi/panel bilgisiyle doğrulanacak.
- Ham CSV korunacak; türetilmiş evre tablosu ve yorum ayrı saklanacak.
- PZEM zorunlu eğitim kaynağı değil; mevcutsa yardımcı karşılaştırma olarak tutulabilir.
- Ölçüm firmware'i/katsayısı değiştirilmeden ilk program kaydı alınacak.
- E21 kabul ölçütleri ve sınırlar: [E21 protokolü](experiments/E21-washing-machine-program-analysis/README.md).
- Karar: [ADR-026](docs/decisions/ADR-026-close-stable-window-training-open-washer-analysis.md).

**Önceki iş akışının kapanışı:** PZEM/SCT kararlı alanlarını eşleştirip eğitim etiketi üretme ve bu amaçla E20 aç/kapa deneyi yürütme gereği kapatıldı. E20 fiziksel olarak yapılmadı; planı tarihsel kayıt olarak korunur. E19 ölçümleri ve önceki tüm deneyler silinmez. T008/T006'nın bu eski eğitim hedefiyle ilgili kalan işleri yeni hedefin ön koşulu değildir.

# SCT-013 – PZEM Akım Gözlem | Yol Haritası

Bu projede yalnızca **iki ana faz** vardır. Faz 1 kodu bulup ±%4 hedefini sağlama aşamasıydı. Faz 2 ise BERO sistemini pratik biçimde yeniden kurma, modülleri devreye alma ve çalışan sistemi geliştirme aşamasıdır. Eski deney kayıtları tarihsel arşiv olarak korunur.

## Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak

<badge> TAMAMLANDI </badge>

**Hedef:** SCT013 akım gözlemi için çalışan bir kod yolu bulmak ve PZEM karşılaştırmalarında ±%4 sapma hedefini sağlamak.

**Sonuç:** Dış kaynaklı ESPHome ct_clamp kodu kullanılarak hedefe ulaşıldı. Dört karşılaştırma koşulunun tamamı ±%4 sınırında:

| Yük koşulu | Referans | Kod sonucu | Sapma |
|---|---:|---:|---:|
| 100 W akkor | 0,446–0,447 A | 0,4471 A | yaklaşık %0 |
| 150 W akkor | 0,616 A | 0,615 A | −%0,2 |
| Kettle düşük/kararlı | 0,637 A | 0,656 A | +%3,0 |
| Kettle kaynama | 6,39 A | 6,15 A | −%3,8 |

Bu sonuçlar kullanıcı tarafından paylaşılan karşılaştırmalar ve kayıtlarla desteklenmektedir. Harici kodun kaynağı depoda bulunmasa da Faz 1 hedefi açısından sonuç kabul edilmiştir.

**Faz 1 kapsamındaki eski çalışmalar:** E00A, E00B, E00, E01–E08, E00F ve ilgili alt adımlar bu ana fazın tarihsel kayıtlarıdır. Hedefe ulaşıldığı için Faz 1 kapsamında kalan, henüz yapılmamış deneyler ve işler **KAPATILDI — HEDEFE ULAŞILDI**. Bu ifade, yapılmamış deneylerin fiziksel olarak gerçekleştirildiği anlamına gelmez.

Ayrıntılı geçmiş: [ADR-009](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md), [Faz 1 deney arşivi](experiments/README.md).

## Faz 2 — Pratik yeniden kurulum ve sistem geliştirme

<badge color="success"> AKTİF FAZ </badge>

**Ana hedef:** Faz 1'de çalışan akım okuma yaklaşımını ve depoda biriken kod/donanım bilgisini başlangıç noktası alarak BERO'nun modüler sistemini yeniden kurmak, ESP düğümlerini tek tek devreye almak ve gerçek kullanım sonuçlarıyla geliştirmek.

Faz 2 yeni bir başlangıçtır; ancak geçmişi silmek anlamına gelmez. Kayıtlı YAML'lar, kodlar, donanım notları, loglar ve kararlar başlangıç referanslarıdır. Uygun olduklarında yeniden kullanılır, gerekirse somut ihtiyaca göre uyarlanır. Bunların hiçbiri yeni fiziksel kurulumun test edildiği anlamına gelmez.

### Çalışma yaklaşımı

1. Önce aynı işi yapan çalışan kodu, örnek projeyi, kütüphaneyi veya hazır modül çözümünü bul ve değerlendir.
2. Gerçek donanım/kart/pin bilgilerini doğrula; bilinmeyen bağlantı veya parça özelliğini varsayma.
3. Bir seferde tek modül ve tek temel işlevle başla. Gereken en az kod uyarlamasını yap.
4. Yapılandırma/derleme kontrolünü, fiziksel bağlantıyı ve gerçek çalışma testini ayrı aşamalar olarak doğrula.
5. Başarılı kodla birlikte gerçek cihaz logunu/çıktısını ve teknik yorumunu depoda sakla.
6. Başka modüllerle entegrasyonu, tekil işlevler çalıştıktan sonra yap.
7. Manyetik teori, ESP32 ADC iç mimarisi, harici ADC/SPI gibi konular somut bir arıza, ölçüm çelişkisi, güvenlik ihtiyacı veya açık tasarım kararı gerektirirse derinleştirilir. Sırf teorik kapsamı genişletmek için uygulama hedefi ertelenmez.

### Faz 2 görev sırası

1. **T009 — Modülleri ve ESP düğümlerini pratik olarak yeniden devreye alma (üst görev).**
   - Modül modül yürütülecek genel devreye alma çerçevesidir.
2. **T010 — Modül 2: ESP32D1 üçlü SCT okuma modülü — KAPATILDI.**
   - E11 sıralı üç-SCT kodu 100 W akkor ampul deneyinde çalıştı; üç kanaldan aynı deney oturumunda veri alındı.
   - Mevcut kapsam için üç kanallı okuma ve gözlem yeterli kabul edildi. Yeni yüklerin UNIT doğrulaması bu görevin devamı değildir.
   - Sonraki yük doğrulamaları PZEM ile birlikte T007/T008 veri hattında ele alınacaktır.
   - Ayrıntı: [T010 kapanış kaydı](tasks/T010-module2-triple-sct-bringup.md).
3. **T007 — Home Assistant → PC veri aktarımı.**
   - PZEM ve SCT modülleri gerçek veri ürettiğinde HA geçmişi PC'ye alınır.
   - Entity kimliği, kaynak timestamp, birim ve ham durum korunur.
4. **T008 — PZEM/SCT kararlı alan eşleştirme ve etiketleme.**
   - İki akışın kararlılığı ayrı değerlendirilir.
   - Olay işaretleri her iki akışı `BOOT_ID + EVENT_ID` paket aralıklarına böler; aynı paket aralığındaki bağımsız kararlı SCT/PZEM bölgeleri eşleştirilir. Timestamp iki sensör arasında eşleştirme anahtarı değildir.
   - PZEM proje referansı olarak SCT pencerelerine etiketlenir; mutlak ground truth sayılmaz.
5. **T006 — Katsayı/model değerlendirmesi.**
   - İlk karşılaştırmada K=24.22 başlangıç değeri olarak incelenir.
   - Yalnız eşleşmiş veriler sistematik ve tekrarlanabilir sapma gösterirse iyileştirme yapılır.
   - Her yeni sürüm gerçek veri ve yeni calibration_id ile kaydedilir.
5. **Sürekli geliştirme.** Gerçek kullanım veya testten doğan yeni ihtiyaçlar küçük ve doğrulanabilir adımlarla ele alınır.

### Faz 2 ilk kabul kapısı

- En az bir seçilmiş modülün gerçek kartı, bağlantısı ve temel işlevi doğrulanmış olmalı.
- Kullanılan kodun kaynağı/sürümü veya depodaki referansı belli olmalı.
- Yapılandırma derleme kontrolünden geçmiş olmalı.
- Gerçek cihaz çıktısı/logu ve yorumuyla birlikte kaydedilmiş olmalı.
- Test edilmemiş modüller açıkça beklemede kalmalı.

## Kapsam sınırları

Bu proje enerji analizörü, güç kalitesi analizörü, PF hesaplayıcı, FFT/THD veya harmonik analiz projesi değildir. PZEM'in kendi alanları referans kaydı olarak tutulabilir; SCT'den PF veya faz açısı hesaplanmaz. Sürekli ham ADC/50 Hz dalga kaydı ve örnek başına timestamp, açık ve gerekçeli yeni bir ihtiyaç olmadıkça proje hedefi değildir.

## Karar ve tarihçe

- [ADR-009 — ±%4 hedefi ve Faz 1 kapanışı](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md)
- [ADR-010 — PZEM referanslı kararlı alan öğrenmesi](docs/decisions/ADR-010-pzem-stable-window-learning-focus.md)
- [ADR-011 — Projeyi iki faza ayırma](docs/decisions/ADR-011-two-phase-project-structure.md)
- [ADR-014 — Faz 2 pratik yeniden başlangıç](docs/decisions/ADR-014-phase2-practical-restart.md)
- [ADR-022 — Paket işaretleriyle akış bölümleme ve eğitim verisi oluşturma](docs/decisions/ADR-022-packet-marker-segmented-training-streams.md)
- [T009 — Modül/ESP devreye alma](tasks/T009-practical-system-bringup.md)
- [Faz 1 deney arşivi](experiments/README.md)


## 2026-11-01 — Faz 2 veri hattı ve düşük akım uygulama planı

Faz 2 için ayrıntılı yürütme planı [burada](docs/plans/2026-11-01-phase2-data-and-low-current-execution-plan.md) tutulur. Ana görev sırası değişmez: T009 → T010 → T007 → T008 → T006. T010 pratik modül devreye alma tamamlanmadan veri/öğrenme hattı görevleri aktif göreve alınmaz. 0,4 A fiziksel alt sınır olarak kabul edilmez; eski E00F yapılandırmasındaki 0,35 A filtresi güncel ESP32D1 Modül 2'ye atfedilmez. Bölgesel model kararı eşleşmiş ve tekrarlanabilir veriye bağlıdır. Bu planlama kaydı firmware veya ölçüm sonucu değildir.


## 2026-11-01 — Paket işaretli eğitim akışı kararı

Modül 3, olay mesajını kendi PZEM akışına ayrı kayıt olarak ekler ve aynı mesajı UDP 4210 üzerinden Modül 2'ye yollar. Modül 2 aldığı mesajı kendi SCT akışına aynı biçimde ayrı kayıt olarak ekler. Python her akışı paket işaretleriyle böler, BOOT_ID + EVENT_ID ile aralıkları eşleştirir ve her sensörün kararlılığını kendi verisinden bağımsız bulur. Timestamp, iki sensörün ölçümlerini eşleştirme anahtarı değildir. Ayrıntı ve ADR-019 üzerindeki değişiklik: [ADR-022](docs/decisions/ADR-022-packet-marker-segmented-training-streams.md). Firmware henüz değiştirilmedi.

## 2026-11-01 — Modül 2/3 olay aktarımı güncel durum

- Modül 2 ESP32D1 üç-SCT okuma + UDP 4210 olay alıcısı kaynak dosyası depoda bulunuyor.
- Modül 3 WROOM PZEM + SSR olay kaynağı kaynak dosyası depoda bulunuyor.
- Modül 2 uzun logu dört olayın (59 ON, 61 ON, 62 OFF, 64 OFF) UDP alımı ve HA yayın çağrısını destekliyor; 60 ve 63 bu logda görünmüyor.
- HA History ekran görüntüsü ayrı kesitte 70 OFF ve 71 ON olaylarını iki modülün olay entity'lerinde gösteriyor.
- Fiziksel SSR anahtarlaması, tüm olayların kayıpsız teslimi, kaynak YAML/binary birebirliği ve Python T007/T008 hattı tamamlanmış değildir.
- Kanıt: [uzun olay analizi](logs/module2/2026-11-01-module2-on-off-extended-analysis.md).
- T010 kapalıdır; T007 → T008 → T006 sırası korunur. T009 genel pratik devreye alma üst görevidir.


## 2026-11-01 — Python paket bütünlüğü ve eksik olay davranışı (ADR-024)

Python, Modül 3 PZEM ve Modül 2 SCT akışlarını kendi olay işaretleriyle bağımsız paketler. Bir akışta ON başlangıcı veya OFF bitişi eksik/uyuşmazsa o aralık tamamlanmış paket sayılmaz. İki tarafta aynı BOOT_ID + EVENT_ID paket aralığı doğrulanmadan eğitim örneği üretilmez. Eksik olaylar ve sıra hataları raporlanır; tahminle tamamlanmaz. Yeni ON açık pakete gelirse önceki aralık geçersiz sayılır ve yeni ON yeni paket adayı başlatır. Mevcut UDP ve HA aktarım yapısı korunur; yeni helper/merkezi HA mimarisi kurulmaz. Ayrıntı: [ADR-024](docs/decisions/ADR-024-python-packet-completeness-validation.md). Python uygulaması henüz yapılmamıştır.


## 2026-11-01 — Faz 2 deney sırasının esnek yürütülmesi

Faz 2 içindeki deneylerin uygulanma sırası sabit bir takvim değildir. Donanımın hazır oluşu, ortaya çıkan ihtiyaç ve gerçek test bulgularına göre deney öncelikleri değiştirilebilir. Bu, ana görevlerin teknik bağımlılıklarını (T009/T010 ve veri hattı için T007 → T008 → T006), ADR kararlarını veya deney kabul koşullarını kendiliğinden değiştirmez.

İlk ortak deney önceliği **E11 — Modül 2/3 birlikte yüksüz hat uzun süreli gözlem ve olay aktarımı** olarak belirlendi. Modül 3 montajı sonrası kısa eşzamanlı açılış kontrolü yapılacak; uygun bulunursa iki modül ölçülen hatta yük olmadan uzun süre çalıştırılacak. Ayrıntı: [E11 protokolü](experiments/E11-idle-dual-module-observation/README.md).

### İşletim modları

- Modül 2, üç SCT kanalını sürekli okuyarak tek başına gözlem yapabilir.
- Modül 3, PZEM alanlarını tek başına gözlemleyebilir.
- İki modül birlikte eğitim verisi/olay paketleri için kullanılacaksa iki ölçüm akışı ve Modül 3'ün BOOT_ID/EVENT_ID/STATE olay üretimi birlikte aktif olmalıdır.
- Yalnız PZEM gözleminde SSR ON/OFF döngüsünü ileride devreden çıkarmak bir işletim seçeneğidir; E11'de döngü açık kalır. Firmware değişikliği bu kayıtla yapılmamıştır.
- Modül 2'nin üç SCT kanalı birlikte çalışmaya devam eder; kanal seçici jumper/düğme eklenmesi mevcut ihtiyaç değildir.


## 2026-11-01 — ADR-025: eğitim ve tam ham kayıt değerlendirmesi

Eğitim aşamasında yalnızca SCT ve PZEM akışlarının kendi içlerinde bağımsız tespit edilen uygun kararlı alanları eşleştirilir; PZEM bu eğitim pencereleri için proje referansıdır. Deneyin ham SCT kaydının tamamı korunur. Öğrenilen katsayı/model daha sonra ON, OFF, açılma, kapanma ve geçişler dahil tam ham SCT kaydına uygulanır.

Tam kayıt davranış değerlendirmesinde Python'a deneyin bilinen ON/OFF koşulu ve bilinen yük aralığı verilir. PZEM'in geçiş sırasındaki ardışık okumaları SCT örnekleri için noktasal referans yapılmaz; bilinmeyen ara akımlar uydurulmaz. Bu değerlendirme bilinen deney koşullarına göre davranış/tutarlılık incelemesidir, bağımsız noktasal referans olmadan mutlak doğruluk iddiası değildir. Tek veya çoklu katsayı seçimi gerçek veriye bırakılır.

Ayrıntı: [ADR-025](docs/decisions/ADR-025-raw-data-sct-model-behavior-validation.md) ve [Python veri hattı mimarisi](docs/architecture/python-program-architecture.md).

## 2026-11-01 — Gün sonu çalışma durumu

- E11, Modül 3 nihai montajı ve iki modülün kısa ortak açılış kontrolü öncesinde **PLANLANDI** durumundadır; deney sonucu yoktur.
- T009 pratik modül devreye alma üst görevi **AKTİF** kalır. T010 üçlü SCT okuma görevi kapalıdır; görev tablosu bu durumla tutarlı tutulur.
- T007/T008/T006 veri hattı sırası ve bağımlılıkları ADR-025 ile değiştirilmemiştir.
- Bugün yeni firmware/Python uygulaması, derleme/OTA veya fiziksel deney doğrulaması yapılmamıştır.


## 2026-11-06 — E15 eğitim kanal adlandırma doğrulaması planlandı

Eğitim amaçlı `CH1-E`, `CH2-E`, `CH3-E` adlarının koddan Home Assistant cihaz/entity kayıtlarına ve History CSV dışa aktarımına doğru taşındığını doğrulamak için [E15](experiments/E15-training-channel-history-naming/README.md) planlandı. Deneyde yalnız adlandırma alanları değiştirilecek; ölçüm hesabı, pinler ve zamanlama korunacak. Kod değişikliği, derleme, OTA ve fiziksel doğrulama henüz yapılmadı.

## 2026-11-06 — Eğitim veri seti kanal kapsamı ve History işaretlemesi (ADR-027)

Test ve günlük deney kodları üç SCT kanalını birlikte okuyabilir. Gün içindeki deneylerde Home Assistant History'de genel kanal adları `CH1`, `CH2`, `CH3` kullanılır; bu kayıtlar kendiliğinden eğitim verisi sayılmaz. Bir kod/ölçüm yapılandırması kesinleşip özellikle eğitim verisi toplanmasına karar verildiğinde, ilgili kodda küçük bir adlandırma değişikliği yapılarak eğitim akışı `CH1-E`, `CH2-E` veya `CH3-E` adıyla yayınlanır. `-E` eğitim işaretidir; fiziksel kanal kimliği, sarım sayısı veya hesaplama yöntemi değildir.

Python-1 kaynak History CSV'sini değiştirmeden doğrular ve arşivler; bu üç adın dosyada bulunması Python-1 kabul koşulu değildir. Python-2/eğitim hazırlama aşaması bu adları açık seçim/eşleme anahtarı olarak kullanır. Genel deney kayıtları eğitim setine otomatik alınmaz. Eski bir deneyden eğitim kopyası üretilecekse kaynak arşiv korunur; seçim ve adlandırma ayrı türetilmiş kopyada yapılır. Sarım sayısı, katsayı ve hesaplama yöntemi gerektiğinde ilgili kodda tanımlanır; kanal adına gömülmez.

Her eğitim veri seti tek bir SCT kanalından oluşur; CH1, CH2 ve CH3 için ayrı setler ve ayrı model değerlendirmeleri yürütülür. PZEM akımı proje referansıdır. Üç kanallı test firmware'i, günlük deney adları ve ham arşiv bu kararla değiştirilmez.

Ayrıntı: [ADR-027](docs/decisions/ADR-027-single-channel-training-datasets.md) ve [Python veri hattı mimarisi](docs/architecture/python-program-architecture.md). T007/T008 uygulaması ve gerçek eğitim çıktısı tamamlanmış değildir.


## 2026-11-07 — CH1 yüksüz kapalı alan sınırı ve sonraki deney hedefi

CH1 için fiziksel yüksüz koşulda alınan yaklaşık 10 saatlik HA History kaydı (36.002 örnek) üzerinden K=24.22 uygulanmış akımın P95 değeri 0,23587365 A bulundu. Kullanıcı kararıyla CH1 kapalı alan üst sınırı **0,24 A** olarak sabitlendi. Bu eşikte ölçümlerin %96,33'ü 0,24 A veya altındadır. Ham CSV depoya eklenmedi; istatistiksel özet [I007 raporunda](data/off-noise/sessions/2026-11-07-ch1-closed-area-threshold.md) tutulur.

Sonraki ölçüm hedefi, **0,24 A ile ilk güvenilir akım okuması arasındaki hesaplanmadı alanının** üst sınırını kontrollü yük deneyleriyle belirlemektir. İlk güvenilir okumanın sayısal değeri henüz belirlenmedi. Bu karar yalnız CH1 ve incelenen yüksüz koşula aittir; CH2/CH3'e genellenmez. Ayrıntı: [ADR-031](docs/decisions/ADR-031-ch1-idle-closed-area-threshold.md).


## 2026-11-07 — E16/E17/E18 kapanışı ve program davranışı araştırması

E16, E17 ve E18 kullanıcı kararıyla kapatıldı. CH1'in yüksüz kapalı alan sınırı ve düşük akım hesaplanmayan bölgesi mevcut kurulum için tanımlanmıştır; aynı bölgeyi tekrarlayan deneyler açılmayacaktır. E18 bias hattı gözleminde tekil sıçramalar dışında stabil davranış bildirilmiştir; bias hattı ana dalgalanma kaynağı olarak araştırılmayacaktır.

### Yeni araştırma sorusu: SCT programlı cihaz davranışını ayırt edebilir mi?

Çamaşır makinesi benzeri cihazlarda program boyunca devreye giren yükler ve alt sistemler ayrı ayrı incelenecek: örneğin rezistans/ısıtıcı, tambur motoru, tahliye veya devirdaim pompası, su giriş valfi ve kilit/yardımcı yükler. Bunların gerçek güç/akım değerleri, aynı anda çalışma durumları, açma-kapama örüntüleri ve süreleri cihaz modeline/programına göre değişir; bu nedenle şimdiden sabit akım seviyeleri veya evre imzaları varsayılmayacaktır.

Araştırma şu soruları cevaplamalı:
- Hangi alt yükler programın hangi evrelerinde çalışıyor; aynı anda hangileri birleşiyor?
- Her evrede SCT akım genliği, kararlı dağılımı, geçiş yönü/süresi ve tekrar düzeni nasıl görünüyor?
- PZEM proje referansı ve SCT akışı birlikte kullanıldığında evreleri etiketlemek mümkün mü?
- Eğitim ve test kayıtları arasında cihaz/program/evre ayrımı korunarak genellenebilirlik ölçülebilir mi?
- SCT'nin özellikle 2 A altındaki ölçüm ve davranış ayırt etme kabiliyeti hangi aralıkta yeterli? Bu henüz açık araştırma sorusudur.

**Önemli ayrım:** SCT'nin güç/akım genliğini doğru hesaplaması, geçişleri gözlemlemesi ve program evresini sınıflandırmaya yetecek örüntü üretmesi üç ayrı performans ölçütüdür. Her biri ayrı veri ve metriklerle değerlendirilecektir. Bu aşamada SCT'nin 2 A altında yeterli veya yetersiz olduğu sonucuna varılmamıştır.

### Uygulama sırası

1. T007 — HA History CSV alımını, kaynak doğrulamasını ve ham arşivi kur.
2. T008 — olay paket bütünlüğü, bağımsız kararlılık analizi ve PZEM referans etiketlemesini uygula.
3. Gerçek cihaz yük/evre envanterini ve deney senaryolarını araştır; önce mevcut SCT/PZEM kayıtlarıyla veri analizi yap.
4. Eğitim ve bağımsız test kümeleri oluştur; sınıflandırma başarısını ve hata türlerini ölç.
5. Bulgulara göre SCT'nin kullanım alanını tanımla; gerekirse farklı sensörlerle karşılaştırmayı ayrı karar olarak aç.

Bu çalışma, Faz 2'nin Python/veri/öğrenme odağıdır. E16/E17/E18 yeniden açılmamıştır.
