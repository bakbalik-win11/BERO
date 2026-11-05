# SCT013 – PZEM Akım Gözlem

## BERO üst mimarisi

Bu klasör BERO'nun sensörden bağımsız mimarisinin kendisi değil, ilk SCT013 + PZEM uygulamasıdır. Ortak üç katmanlı yapı (veri toplama → özellik çıkarma → davranış çıkarımı) ve sensörler arası tasarım ilkeleri [BERO Mimari](../../MIMARI/README.md) altında tutulur. Bu projedeki SCT/CT'ye özgü ayarlar ve kanıtlar burada kalır.

## Projenin amacı

BERO'nun bu alt projesi, SCT013 akım sensöründen elde edilen ölçüm çıktısını çalışan bir kod yolu üzerinden izlemek ve PZEM-004T V3.0 referans akışıyla karşılaştırarak zaman içinde geliştirmektir.

Proje iki ana fazdan oluşur:

- **Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak: TAMAMLANDI.** Dış kaynaklı ESPHome ct_clamp koduyla hedef sağlandı.
- **Faz 2 — Pratik yeniden kurulum ve sistem geliştirme: AKTİF.** Kayıtlı kod ve çalışan örneklerden yararlanarak modüller ve ESP düğümleri tek tek devreye alınacak; ardından PZEM referanslı veri aktarımı, kararlı alan eşleştirme ve model iyileştirmesi yapılacak.

Bu proje enerji analizörü, güç kalitesi analizörü veya harmonik analiz sistemi değildir.

## Faz 1 — kapanış sonucu

Dış kaynaklı çalışan kodla yapılan karşılaştırmalar:

| Yük koşulu | Referans | Kod sonucu | Sapma |
|---|---:|---:|---:|
| 100 W akkor | 0,446–0,447 A | 0,4471 A | yaklaşık %0 |
| 150 W akkor | 0,616 A | 0,615 A | −%0,2 |
| Kettle düşük/kararlı | 0,637 A | 0,656 A | +%3,0 |
| Kettle kaynama | 6,39 A | 6,15 A | −%3,8 |

Dört karşılaştırmanın tamamı ±%4 sınırındadır. Faz 1 hedefi sağlandığı için bu fazın yapılmamış deney ve işleri de kapatılmıştır. Eski deney kayıtları silinmez; [Faz 1 deney arşivinde](experiments/README.md) tutulur. Kapatılan bir planın fiziksel olarak yapılmış olduğu iddia edilmez. Karar: [ADR-009](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md).

## Faz 2 — güncel çalışma

Faz 2, yeni bir pratik başlangıçtır: önce çalışan kod/örnek bulunur, kayıtlı YAML ve donanım bilgileri başlangıç referansı olarak kullanılır, modüller ve ESP düğümleri tek tek devreye alınır. Her modül için derleme, bağlantı ve gerçek donanım çıktısı ayrı doğrulanır. Başarılı kod, gerçek log/çıktı ve yorum depoda saklanır.

Genel üst görev **T009 — modülleri ve ESP düğümlerini pratik olarak yeniden devreye alma**. İlk somut modül görevi **T010 — Modül 2 ESP32D1 üçlü SCT okuma modülü**. Manyetik teori veya ESP32 ADC iç mimarisi, somut bir sorun veya uygulama kararı gerektirmediği sürece çalışma odağı yapılmaz. Önceki araştırmalar tarihsel teknik referans olarak korunur.

Modüller çalışır ve gerçek Home Assistant entity akışları oluşur hâle geldikten sonra:
1. T007 — HA → PC veri aktarımı.
2. T008 — PZEM ve SCT kararlı alanlarını ayrı bulma, örtüşen alanları eşleştirme ve PZEM ile etiketleme.
3. T006 — mevcut K=24.22 katsayısını değerlendirme; yalnız veri gerekçelendirirse iyileştirme.

Faz 2 kapsamı: [ADR-014](docs/decisions/ADR-014-phase2-practical-restart.md). Üst görev: [T009](tasks/T009-practical-system-bringup.md). İlk modül görevi: [T010](tasks/T010-module2-triple-sct-bringup.md).

## Çalışan ölçüm baseline'ı

- ESP32D2 / E00F.
- ESPHome ct_clamp.
- SCT giriş GPIO33.
- sample_duration: 200ms.
- update_interval: 2s.
- Mevcut katsayı K=24.22.

Bu ayarlar Faz 1'deki çalışan yolun tarihsel referansıdır. Faz 2'de yeni modül/ESP kurulumuna başlangıç noktası olabilir; yeni donanım ve işlev gerektirirse kontrollü biçimde uyarlanabilir. Her değişiklik ayrı kaydedilir ve derleme/gerçek donanım testiyle doğrulanır. [Firmware kaydı](firmware/esp32d2.yaml).

## Donanım referansları

- Öncelikli SCT: [SCT013-030 — 30 A / 1 V](hardware/references/SCT013-30A-1V.md).
- Diğer SCT/CT stokları: [donanım envanteri](hardware/inventory.md).
- PZEM-004T V3.0: [proje referansı](hardware/references/PZEM-004T-V3.0.md); PZEM'e bağlı CT modeli PZCT-02 (0–100 A) olarak kaydedilmiştir.
- Bias alt devresi: breadboard üzerinde 2 × 10 kΩ ve 104/100 nF kondansatör; [analog ön uç kaydı](hardware/frontend.md).
- ESP32D2, ESP32-WROOM ve diğer kartlar: [donanım envanteri](hardware/inventory.md).
- SSR ve DS3231, olay/zamanlama altyapısının donanım referanslarıdır.

## Öncelikli okuma sırası

1. [AGENTS.md](AGENTS.md) — çalışma protokolü.
2. [STATUS.md](STATUS.md) — güncel aktif görev.
3. [ROADMAP.md](ROADMAP.md) — yalnız iki ana faz.
4. [PROGRESS_TREE.md](PROGRESS_TREE.md) — genel görünüm.
5. [tasks/README.md](tasks/README.md) — Faz 2 görev sırası.
6. [T009](tasks/T009-practical-system-bringup.md) — genel devreye alma üst görevi.
7. [T010](tasks/T010-module2-triple-sct-bringup.md) — ilk somut modül görevi.
8. [T007](tasks/T007-python-architecture.md) — sonraki veri aktarımı adımı.
9. [Python veri hattı mimarisi](docs/architecture/python-program-architecture.md).
10. [Deney arşivi](experiments/README.md) — Faz 1 tarihçesi.
11. [Karar kayıtları](docs/decisions/).

## Kapsam dışı

- Enerji analizörü veya güç kalitesi ölçümü.
- SCT'den PF/faz açısı hesabı.
- FFT, THD ve harmonik analiz.
- Sürekli ham ADC/50 Hz dalga kaydı ve örnek başına timestamp.
- Faz 1'de hedefe ulaşmak için artık gerekmeyen deneylerin yeniden açılması.

## Sensör okuma mimarisi ve tekrar kullanılabilir kod

ESPHome `ct_clamp` araştırmasından çıkan ortak sensör okuma yaklaşımı ve açıklamalı YAML örnekleri [firmware/patterns/README.md](firmware/patterns/README.md) altında tutulur.

- CT/AC akım: [ct-clamp-ac-rms-reference.yaml](firmware/patterns/ct-clamp-ac-rms-reference.yaml)
- Analog DC gerilim: [adc-dc-voltage-observer.yaml](firmware/patterns/adc-dc-voltage-observer.yaml)

Bu örnekler mevcut cihaz firmware'lerinin yerine geçmez. Her yeni sensörde pin, elektriksel aralık, sensör transfer fonksiyonu ve uygun sinyal işleme yöntemi doğrulanır. YAML'lar henüz derlenmiş veya fiziksel donanımda test edilmiş değildir.


## Kararlı alan eğitimi — olay ve ölçüm akışlarının ayrılması

Modül 2 ve Modül 3'te ölçüm verileri ile UDP olay/yayın verileri bağımsız kayıt akışlarıdır. Modül 2 SCT okumalarını ve aldığı UDP BERO_EVT/BOOT_ID/EVENT_ID/STATE olaylarını HA'ya ayrı ayrı aktarır. Modül 3 SSR durum değişiminde TIME içermeyen BERO_EVT mesajını UDP ile yayınlar; PZEM ölçümlerini ve olay kaydını HA'ya ayrı ayrı aktarır. Python SCT ve PZEM kararlılığını yalnızca kendi ölçüm akışlarından bağımsız tespit eder. UDP paket/zaman/ON-OFF bilgisi yalnızca deney ve olay çerçevesidir; kararlılığı veya kararlı alan sınırlarını belirlemez. Python önce Modül 2 SCT ve Modül 3 PZEM akışlarını kendi olay işaretleriyle paket aralıklarına böler; paketler BOOT_ID + EVENT_ID ile eşleştirilir. Her akışın kararlılığı yalnız kendi ölçüm değerlerinden bağımsız tespit edilir; ON–OFF aralığı otomatik olarak kararlı sayılmaz. Zaman damgaları akış içi olay sırasını ve paket sınırlarını kurmak için kullanılır; iki sensör örneğini timestamp ile birebir eşleştirme anahtarı değildir. TIME alanı olay protokolünden kaldırılmıştır. Geçerli karar sırası: [ADR-022](docs/decisions/ADR-022-packet-marker-segmented-training-streams.md) ve TIME alanını geçersiz kılan [ADR-023](docs/decisions/ADR-023-event-identity-without-time.md).


## Eğitim verisinin ON-only ilkesi

BERO'nun bu projesinde eğitim verisi **yalnız yükün açık (ON) olduğu dönemdeki kararlı SCT/PZEM alanlarının zaman örtüşmesinden** oluşturulur. Kapalı (OFF) alanlar hiçbir zaman eğitim verisi değildir ve iki sensör arasında eşleştirilmez. OFF olayı, ON paketini kapatır; ilk aşamada kapalı durum sıfır kabul edilir. Tam ON/OFF paket bütünlüğü, eğitim örneğinin geçerli deney aralığından geldiğini doğrulamak içindir; OFF okumalarını eğitime katmak için değildir.

OFF/yüksüz okumalar ON akım kalibrasyonuna katılmaz. Ancak farklı deneylerde biriken OFF örnekleri ileride ayrı bir veri havuzunda birleştirilerek gürültü tabanı ve kapalı durum eşiği/sınıflandırması için kullanılabilir. Gerekirse aç-kapa döngüsü olmadan, hatta yük bağlı değilken uzun bir yüksüz kayıt alınır. Bu ikinci öğrenme hedefi ilk aşama değildir. Uzun vadede Python'da geliştirilen ve doğrulanan eşik/modelin sahada hesaplama yapan ESP'ye aktarılması hedeflenebilir; bu mimari henüz tasarlanmamış/uygulanmamıştır.

Ayrıntı ve uygulama kuralı: [ADR-025](docs/decisions/ADR-025-raw-data-sct-model-behavior-validation.md) ve [E12](experiments/E12-sct-stability-window-and-response/README.md).

## Eğitim ve tam ham veri değerlendirmesi (ADR-025)

PZEM, SCT katsayısını/modelini öğrenmek için uygun kararlı alanların eşleştirilmesinde proje referansıdır. Eğitim için kararlı alanlar seçilse bile deneyin ham verisinin tamamı korunur. Öğrenilmiş model, açılma/kapanma ve geçişler dahil tam SCT kaydına ayrıca uygulanır.

Bu ikinci değerlendirmede Python'a deneyin bilinen ON/OFF koşulu ve yük aralığı verilir. PZEM'in geçişteki ardışık okumaları SCT'nin her örneği için noktasal doğruluk referansı yapılmaz. Bilinmeyen ara geçiş akımları uydurulmaz; sonuç bilinen deney koşullarına göre SCT davranış/tutarlılık değerlendirmesidir, mutlak doğruluk iddiası değildir. Tek veya alan bazlı katsayı seçimi gerçek veriye bırakılır.

Ayrıntı: [ADR-025](docs/decisions/ADR-025-raw-data-sct-model-behavior-validation.md).
