# Klasör rehberi — Türkçe adlar ve çalışma akışı

Bu rehber, proje klasörlerinin ne işe yaradığını ve birbirleriyle nasıl ilişkili olduğunu açıklar.

## İsimlendirme kararı

Klasörlerin GitHub'daki gerçek adlarını şimdilik değiştirmiyoruz. Örneğin `hardware/` klasörünün yanına Türkçe karşılığı olarak **Donanım** yazıyoruz. Bunun nedeni mevcut bağlantıların, GitHub Actions kurallarının, betiklerin ve dosyalardaki göreli yolların bozulmasını önlemek.

Bu nedenle:
- **İngilizce yol:** GitHub'da açılacak gerçek klasör/dosya adıdır.
- **Türkçe ad:** Klasörün veya dosyanın amacını kolayca anlaman için açıklamasıdır.
- Yeni dosya bağlantısı verirken asistan her zaman gerçek GitHub yolunu da paylaşmalıdır.

## Kısa Türkçe karşılık listesi

Klasör listesini okurken şu karşılıkları kullan:

- `HISTORY` - Geçmiş ve oturum kayıtları
- `analysis` - Analiz
- `calibration` - Kalibrasyon
- `data` - Veri ve ölçüm kayıtları
- `docs` - Teknik belgeler
- `experiments` - Deneyler
- `hardware` - Donanım
- `schema` - Veri şemaları
- `tasks` - Görev kartları

Bu açıklamalar Türkçe rehber niteliğindedir; klasörlerin GitHub'daki gerçek adları ve bağlantıları aynı kalır.

## 1. Klasörlerin genel şeması

```text
SCT013-PZEM-AKIM-GOZLEM/  (SCT-013 + PZEM Akım Gözlem Sistemi)
│
├── README.md                 (Proje tanıtımı ve ana bağlantılar)
├── AGENTS.md                 (Çalışma kuralları)
├── STATUS.md                 (Güncel durum ve tek aktif görev)
├── ROADMAP.md                (Fazlar ve başarı ölçütleri)
├── KLASOR_REHBERI.md         (Bu rehber: Türkçe klasör adları)
├── SESSION_PROTOCOL.md       (Oturum başlatma ve kapatma yöntemi)
├── GUN_SONU_KONTROLU.md      (Günlük kapanış listesi)
│
├── tasks/                    (Görev Kartları: hangi işi yapacağız?)
├── hardware/                 (Donanım: elimizde ne var, güvenli mi?)
├── docs/                     (Belgeler: kapsam, teknik bilgi, kararlar)
├── experiments/              (Deneyler: neyi, nasıl test edeceğiz?)
├── calibration/              (Kalibrasyon: ölçümü referansa göre ayarlama)
├── schema/                   (Veri şemaları ve geçersiz veri kuralları)
├── data/                     (Veri: örnekler ve ölçüm dosyaları)
├── analysis/                 (Analiz: ölçümleri nasıl değerlendireceğiz?)
└── HISTORY/                  (Geçmiş: hangi oturumda ne yapıldı?)
```

## 2. Ana klasörler — Türkçe karşılıkları ve amaçları

| Gerçek klasör adı | Türkçe karşılığı | Burada ne tutulur? |
|---|---|---|
| `tasks/` | Görev Kartları | Her işin amacı, adımları, bağımlılıkları ve kabul ölçütü. |
| `hardware/` | Donanım | Fiziksel parça envanteri, analog ön uç ve güvenlik kontrolü. |
| `docs/` | Teknik Belgeler | Proje kapsamı, arka plan bilgileri, kaynaklar, açık sorular ve mimari karar kayıtları. |
| `experiments/` | Deneyler | Deneyin protokolü, hangi koşullarda yapıldığı ve gerçek sonuçları. |
| `calibration/` | Kalibrasyon | Kalibrasyon prosedürü ve her kalibrasyonun kimliği/kaydı. |
| `schema/` | Veri Şemaları | JSON kayıtlarının beklenen alanları ve geçersiz/şüpheli ölçüm kuralları. |
| `data/` | Veri | Şema denemeleri için küçük örnekler; yerel ham ve işlenmiş verinin düzeni. |
| `analysis/` | Analiz | Hesaplanacak metrikler ve analiz ilkeleri. Deney verisi olmadan sonuç iddiası yazılmaz. |
| `HISTORY/` | Oturum Geçmişi | Önceki çalışmalar, gün sonu notları ve oturum kayıt şablonu. |

## 3. `docs/` alt klasörleri

| Gerçek yol | Türkçe karşılığı | Amacı |
|---|---|---|
| `docs/background/` | Teknik Arka Plan | SCT ile PZEM arasındaki farklar, örnekleme ve özetleme hakkında açıklamalar. |
| `docs/decisions/` | Mimari Kararlar (ADR) | Tasarım kararları, gerekçeleri ve kararların hangi kanıta dayandığı. |
| `docs/sources/` | Kaynaklar | Teknik iddialarda kullanılan üretici belgeleri ve diğer kaynakların listesi. |
| `docs/open-questions.md` | Açık Sorular | Henüz yanıtlanmamış ve kanıt bekleyen teknik sorular. |
| `docs/00-scope.md` | Proje Kapsamı | Projenin neyi yapacağı ve neyi yapmayacağı. |

Bir soru yalnızca tartışıldı diye kapanmış sayılmaz. Soru deney veya kaynakla yanıtlanmışsa sonuç ve kanıt bağlantısı eklenir.

## 4. `hardware/` — Donanım altındaki dosyalar

| Gerçek yol | Türkçe karşılığı | Amacı |
|---|---|---|
| `hardware/inventory.md` | Fiziksel Donanım Envanteri | Kullanılacak gerçek SCT, PZEM, MCU, ADC, analog devre, referans cihaz ve yükleri kanıtla tanımlamak. |
| `hardware/frontend.md` | Analog Ön Uç | Burden, bias, filtre, ADC giriş aralığı, VREF ve clipping ile ilgili bilgiler. |
| `hardware/safety-checklist.md` | Güvenlik Kontrol Listesi | Şebeke bağlantısından önce yetkin kişi tarafından incelenmesi gereken güvenlik maddeleri. |

BERO'da bir bileşen sayfasının bulunması, o parçanın fiziksel olarak bu deney düzeneğinde kullanıldığını kanıtlamaz.

## 5. `tasks/` — Görev kartları

| Gerçek yol | Türkçe görev adı | Ne zaman kullanılır? |
|---|---|---|
| `tasks/README.md` | Görev Sırası ve Bağımlılıklar | Hangi görevin sırada olduğunu ve hangi işlere bağlı bulunduğunu görmek için. |
| `tasks/T001-hardware-inventory.md` | T001 — Donanım Envanteri | Fiziksel parçaları etiket/fotoğraf gibi kanıtlarla tanımlamak için. |
| `tasks/T002-safety-checklist.md` | T002 — Güvenlik İncelemesi | Şebeke deneyi öncesindeki güvenlik maddelerini yetkin kişiye inceletmek için. |
| `tasks/T003-reference-and-error-target.md` | T003 — Referans Cihazı ve Hata Hedefi | Referans ampermetreyi, yük seviyelerini ve ölçüm öncesi kabul hedeflerini belirlemek için. |
| `tasks/T004-analog-frontend.md` | T004 — Analog Ön Uç | Gerçek bileşenlere göre giriş aralığını ve clipping koşullarını değerlendirmek için. |
| `tasks/T005-noise-floor.md` | T005 — E01 Gürültü Tabanı | Yüksüz ofset ve gürültüyü önceden yazılmış protokolle ölçmek için. |
| `tasks/T006-calibration.md` | T006 — SCT Kalibrasyonu | SCT ölçümünü referans cihazıyla karşılaştırıp calibration_id kaydetmek için. |
| `tasks/_template.md` | Görev Kartı Şablonu | Gelecekte yeni bir görev oluşturulacağı zaman. |

**Çalışma kuralı:** Önce `STATUS.md` içindeki **Aktif görev** satırına bak. Aynı oturumda bu görev üzerinde çalış; yeni fikirleri mevcut işin içine katma.

## 6. `experiments/` — Deney klasörleri

Her deney klasöründe üç temel dosya bulunur. Her biri farklı bir soruya cevap verir:

- `protocol.md` — **Nasıl deneyeceğiz?** Yöntem, koşullar ve kabul ölçütü.
- `metadata.yaml` — **Hangi koşullarda yaptık?** Donanım, yapılandırma ve deney bilgileri.
- `results.md` — **Gerçekte ne oldu?** Yalnızca deney sonrası gözlenen sonuçlar. Deney yapılmadıysa bu açıkça yazılır.

| Gerçek klasör | Türkçe deney adı |
|---|---|
| `experiments/E01-noise-floor/` | E01 — Yüksüz Ofset ve Gürültü Tabanı |
| `experiments/E02-resistive-steady/` | E02 — Kararlı Rezistif Yük |
| `experiments/E03-pzem-step-response/` | E03 — PZEM Adım Yanıtı ve Yerleşme Süresi |
| `experiments/E04-pzem-field-timing/` | E04 — PZEM Alanlarının Güncellenme Zamanı |
| `experiments/E05-sample-rate-compare/` | E05 — Örnekleme Hızı Karşılaştırması |
| `experiments/E06-load-scenarios/` | E06 — Yük Senaryoları ve Clipping |

- `experiments/_template/` — Yeni deney klasörleri için şablon.
- `experiments/README.md` — Deneylerin kısa listesi ve genel kurallar.

## 7. `calibration/`, `schema/`, `data/` ve `analysis/`

### Kalibrasyon
- `calibration/PROCEDURE.md` — Kalibrasyon prosedürü.
- `calibration/calibrations.csv` — Kalibrasyon kayıt tablosu. Eski kayıtların üzerine yazmak yerine yeni calibration_id eklenir.

### Veri şemaları
- `schema/FIELDS.md` — Veri alanlarının sözlüğü.
- `schema/window_record.schema.json` — SCT pencere kaydının biçim kuralları.
- `schema/pzem_read.schema.json` — PZEM okuma kaydının biçim kuralları.
- `schema/invalid-rules.md` — Geçersiz ve şüpheli okumaların nasıl ele alınacağı.

### Veri
- `data/README.md` — Veri saklama kuralları.
- `data/samples/` — Şema denemelerinde kullanılan küçük örnek kayıtlar; gerçek deney sonucu değildir.
- `data/raw/` ve olay ham kayıtları — Yerel ham veriler için öngörülen alanlar; `.gitignore` nedeniyle normalde Git'e eklenmez.
- `processed/` — İşlenmiş küçük çıktılar için kullanılan adlandırma.

### Analiz
- `analysis/README.md` — Analiz ilkeleri.
- `analysis/metrics.md` — SCT/PZEM farkı, pencere değişkenliği, gecikme, clipping ve hata oranı metrikleri.

## 8. Oturum yönetimi ve çalışma sırası

| Gerçek dosya | Türkçe karşılığı | Kullanım zamanı |
|---|---|---|
| `AGENTS.md` | Çalışma Kuralları | Her oturumun başlangıcında okunur. |
| `STATUS.md` | Güncel Durum | Aktif görev ve gerçek ilerleme için ilk bakılacak kaynaktır. |
| `ROADMAP.md` | Yol Haritası | Fazların ve başarı ölçütlerinin genel görünümü. |
| `SESSION_PROTOCOL.md` | Oturum Protokolü | Başlangıç, uygulama ve kapanış kuralları. |
| `GUN_SONU_KONTROLU.md` | Gün Sonu Kontrolü | Oturum sonunda kayıtlarla gerçek GitHub durumunu karşılaştırmak için. |
| `HISTORY/SESSION_LOG.md` | Oturum Günlüğü | Ne yapıldı, ne doğrulandı, ne kaldı ve sıradaki adım. |
| `HISTORY/SESSION_TEMPLATE.md` | Oturum Kaydı Şablonu | Yeni bir oturum kaydı açarken. |

Önerilen sıra:

1. `AGENTS.md` ve `STATUS.md` dosyalarını oku.
2. Aktif görev kartını aç ve kabul ölçütünü anla.
3. Yalnız o görevin gerektirdiği dosyalarda çalış.
4. İşin sonucunu ilgili hedef dosyaya kaydet; kanıt yoksa tamamlandı deme.
5. İlgili kontrolleri çalıştır; `STATUS.md` ve `HISTORY/SESSION_LOG.md` dosyalarını güncelle.
6. PR / otomatik kontrol durumunu yeniden açıp doğrula.

## Önemli sınır

Bu rehber klasörlerin amacını ve mevcut iş akışını açıklıyor. Fiziksel donanımın doğru olduğunu, deneylerin yapıldığını veya verilerin doğrulandığını kendi başına kanıtlamaz. Mevcut proje durumu için her zaman `STATUS.md` ve ilgili kanıtlar esas alınır.
