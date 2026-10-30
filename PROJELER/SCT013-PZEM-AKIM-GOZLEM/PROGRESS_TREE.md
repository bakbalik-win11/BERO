# BERO — İlerleme Ağacı

> **Amaç:** Depoyu baştan sona okumadan projenin genel yapısını, nerede olduğumuzu ve sıradaki adımı kabaca görebilmek. Bu dosya bir özet/navigasyon haritasıdır; ayrıntılı kayıtların yerine geçmez.

## Şu an nerede?

- **Aktif faz:** Faz 1 — SCT analog ön uç ve yüksüz ölçüm hazırlığı.
- **Depo belge tutarlılığı denetimi:** TAMAMLANDI; 87 Markdown dosyasındaki göreli bağlantı hedefleri kontrol edildi ve bulunan tek kırık bağlantı düzeltildi.
- **Deney başlangıcı:** BEKLEMEDE — gerçek ESP32 kart/GPIO ve fiziksel bağlantı kontrolü gerekiyor; bu belge denetimi fiziksel test veya firmware doğrulaması değildir.
- **İlk teknik deney (denetim sonrası):** E00A — ham ADC kaydı ve temel istatistikler.
- **E00A durumu:** AÇILDI; ilk iki referans verisi var (L78L33 çıkışı 3,31 V; breadboard Vmid 1,65 V, kullanıcı multimetre bildirimleri); ESP32D2 için ESP-IDF firmware'i depoda; kullanıcı derlendiğini ve çalıştığını bildirdi. GPIO34 raw ve GPIO35 voltaj değerlerinin logu bekleniyor; 30 saniyelik ham kayıt henüz yok.
- **E00A ilk hedefi:** SCT bağlamadan bias trafosunun L78L33 çıkışını (ilk multimetre bildirimi 3,31 V; KULLANICI BİLDİRİMİ) ve ardından yaklaşık 1,65 V Vmid noktasını ESP32 ADC ile ayrı ayrı gözle. Her koşul 30 saniye planlandı. 3,3 V için ayrı/geçici 10k/10k ölçüm bölücüsü henüz kurulmadı; ADC bağlantısı öncesi kart/pinout ve ADC sınırları doğrulanacak. GPIO34 fiziksel kart/pinout doğrulanırsa kullanılacak. Firmware dosyası mevcut; kullanıcı derleme/çalışma bildirdi. ADC sayısal sonuçları ve ölçüm kaydı henüz yok. ESP32 dahili ADC ham sayılarını oku, kaydet ve bilgisayarda görselleştir; kaydın/paketin sinyali ne ölçüde temsil ettiğini gözlemle. PZEM, akım formülü/kalibrasyon ve MCP3208 bu ilk adımın kapsamında değil. Donanım bağlantısı öncesi gerçek kart/pinout ve bias düzeni kontrol edilir.
- **Sonraki adımlar:** E00 bias ADC karşılaştırması → T005 / E01 yüksüz temel okuma ve gürültü tabanı.
- **Temel kural:** Her adımda NEDEN / HEDEF / KOD / LOG / GÖRSELLEŞTİRME / SONUÇ; deney kodunda açıklamalar ve açıklamalı YAML.

Güncel ayrıntı ve durum için [STATUS.md](STATUS.md) esas alınır.

## Projenin kaba ağacı

```text
BERO — SCT013 + PZEM gözlem sistemi
│
├── 0. Hazırlık ve güvenlik
│   ├── T001 Donanım envanteri ............ TAMAMLANDI
│   ├── T002 Güvenlik kontrolü ............ TAMAMLANDI (kullanıcı beyanı)
│   └── T003 PZEM referans/hedef .......... TAMAMLANDI
│
├── 1. SCT analog ön uç ve temel okuma  ← ŞU AN
│   ├── T004 Analog ön uç belgeleme ....... TAMAMLANDI
│   ├── E00A Ham sinyal/istatistik ........ AÇILDI — ilk referans 3,31 V kaydedildi
│   │   ├── A. Bias trafosu L78L33 3,3 V (3,31 V multimetre bildirimi; ayrı ölçüm bölücüsü henüz kurulmadı)
│   │   ├── B. Bias Vmid (~1,65 V, doğrudan ADC)
│   │   └── SCT bu ilk deneyde bağlı değil
│   ├── E00 Bias ADC karşılaştırması ...... SONRA
│   └── T005 / E01 Yüksüz okuma-gürültü .... SONRA
│
├── 2. SCT veri edinimi
│   ├── Örnekleme hızı ve pencere
│   └── Temel sinyal istatistikleri
│
├── 3. PZEM veri edinimi
│   ├── Okuma zamanları ve alanlar
│   └── Geçersiz okumaların işlenmesi
│
├── 4. Kararlı alanların belirlenmesi ve akış ilişkisi
│   └── Deney/istatistik temelli alan seçimi; sabit zaman maskesi nihai kural değil
│
├── 5. Veri şeması ve kayıt
│   └── Özet kayıtlar + gerektiğinde kısa ham olay kesitleri
│
├── 6. Deneyler
│   ├── E03–E06: PZEM davranışı, hız ve yük senaryoları
│   ├── E07: önceki uygulanmamış plan (tarihçe)
│   └── E08: güncel SCT karakterizasyon planı (T005/E00/E01 sonrasında)
│
├── 7. Python analizi, etiketleme ve model
│   ├── Ortak kararlı alanlardan PZEM etiketli SCT eğitim verisi
│   ├── Aynı etiketli veride eğitim içi ±%4 uyum raporu
│   └── Aynı aç-kapa olayının ham akışında SCT tahmini + PZEM zaman grafiği
│       └── Tepki, yerleşme, PZEM okuma/güncelleme gecikmesi incelemesi
│
└── 8. İyileştirme ve bakım
    └── Sonuçlara göre ayarları geliştirme; değişiklik geçmişini koruma
```

Faz 2–8, yol haritasındaki daha sonraki iş alanlarıdır; bu görünüm onların uygulandığı veya tamamlandığı anlamına gelmez. Deney numaraları ve sıralaması için [deney indeksi](experiments/README.md), görev durumları için [görev listesi](tasks/README.md), ayrıntılı sıra için [ROADMAP.md](ROADMAP.md) kullanılır.

## Depoda nereye bakılır?

| Deneyin nedenini, uygulama kodunu ve kanıtını birlikte izlemek | [EXPERIMENT_LEDGER.md](EXPERIMENT_LEDGER.md) |
| Modelin amacı, veri kümesi yaklaşımı ve kabul edilebilir sınırlar | [docs/project-philosophy.md](docs/project-philosophy.md) |
| Kararlı alan eğitimi ve ham aç-kapa gözlem mimarisi | [training-and-dynamic-observation.md](docs/architecture/training-and-dynamic-observation.md) |

| İhtiyacın | İlk bakılacak dosya |
|---|---|
| Nerede kaldık, sıradaki iş ne? | [STATUS.md](STATUS.md) |
| Büyük resim / ilerleme ağacı | Bu dosya — `PROGRESS_TREE.md` |
| Fazlar ve karar kapıları | [ROADMAP.md](ROADMAP.md) |
| Uygulanacak görevler | [tasks/README.md](tasks/README.md) |
| Deneylerin listesi | [experiments/README.md](experiments/README.md) |
| Henüz göreve dönüşmeyen fikirler | [IDEA_BACKLOG.md](IDEA_BACKLOG.md) |
| Neden böyle karar verdik / geçmiş | [HISTORY/SESSION_LOG.md](HISTORY/SESSION_LOG.md) |
| Açık teknik sorular | [docs/open-questions.md](docs/open-questions.md) |
| Çalışma kuralları | [AGENTS.md](AGENTS.md) |

## Nasıl güncel tutulur?

1. Aktif faz, sıradaki adım veya durum değişirse bu ağaç ve [STATUS.md](STATUS.md) birlikte güncellenir.
2. Görev/deney ayrıntıları kendi dosyalarında kalır; bu dosyada uzun teknik ayrıntı kopyalanmaz.
3. Her değişiklikte HEDEF / LOG / SONUÇ kaydı tutulur.
4. Değişiklikten sonra dosya yeniden okunarak bağlantılar ve durumlar doğrulanır.
5. Bir adımın planlanması, fiziksel olarak uygulanmış olduğu anlamına gelmez.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Depoyu baştan sona okumadan genel ilerlemeyi ve doğru ayrıntı dosyasını bulabilmek.
- **LOG:** Bu navigasyon ağacı mevcut STATUS, ROADMAP, görev listesi, deney indeksi ve fikir havuzuna dayanarak oluşturuldu.
- **SONUÇ:** İlk sürüm genel yön bulma içindir; durum değiştikçe STATUS.md ile birlikte güncellenecek. Fiziksel deney veya firmware testi bu dosya nedeniyle yapılmış sayılmaz.


## Denetim notu — 2026-10-29
- PZEM, eğitim/değerlendirme referans akışıdır; kusursuz ground truth veya bağımsız True-RMS standardı olarak kabul edilmez.
- Kalibrasyon/model kabul hedefi T003'teki ±%4 PZEM-referans sapmasıdır; bağımsız mutlak doğruluk iddiası değildir.
- Sabit 3 saniyelik geçiş maskesi nihai etiketleme kuralı değildir. Kararlı alan ölçütleri deney ve analizle geliştirilecektir.
- Güncel sıra: E00A → E00/T005/E01 temel okumaları → E08 karakterizasyonu. E07 tarihsel/uygulanmamış plandır.


## 2026-10-30 — E00A ilk veri

L78L33 çıkışı 3,31 V ve breadboard bias orta noktası/Vmid 1,65 V multimetreyle kullanıcı tarafından raporlandı. Her ADC koşulu 30 saniye olarak planlandı. ADC ölçümü henüz alınmadı.


## 2026-10-30 — E00A firmware kaydı

E00A için ESP32D2 / ESP-IDF firmware'i [deney klasörüne](experiments/E00A-raw-waveform-observation/firmware/esp32d2-e00a-adc.yaml) eklendi. GPIO34 ham ADC, GPIO35 voltaj çıktısı üretir. Kullanıcı derlendiğini ve çalıştığını bildirdi; gerçek sensör logu ve ADC ölçüm yorumu bekleniyor. 1 saniyelik HA güncellemesi 30 saniyelik ham kayıt değildir.


- **2026-10-30 E00A-S01:** GND referans testi loglandı. GPIO34 0 count; GPIO35 kararlı bölümde 0.142 V. Floating giriş teşhisi destekleniyor; Vmid'e pasif bias direnci elektriksel çözüm adayı. E00A henüz tamamlanmadı. [S01 raporu](experiments/E00A-raw-waveform-observation/reports/E00A-S01-gnd-reference-stability.md).


### E00A — Adım 2: GPIO35 sıfır noktası yazılım düzeltmesi (2026-10-30)

GPIO35 voltaj sensörüne önceki GND logunda görülen 0.142 V tabanını çıkaran geçici filtre eklendi; GPIO34 ham ADC kanalı korundu. Kullanıcı kodun derlendiğini bildirdi. GND girişinde 0.000 V sonucu henüz yeni logla doğrulanmadı. Sonraki adım GND'de sıfır çıktısını kontrol etmek, ardından Vmid'i multimetreyle karşılaştırmaktır. Ayrıntı: [E00A sonuç kaydı](experiments/E00A-raw-waveform-observation/results.md).



**E00A Adım 2 güncellemesi (2026-10-30):** GPIO35 düzeltilmiş voltajı kullanıcı logunda 49/49 kayıtta yaklaşık 48 saniye boyunca 0.000 V; sıfır gösterimi hedefi sağlandı. Kod değiştirilmeden aynı log oturumunda bias trafosu enerjilendirilerek Vmid tepkisi izlenecek. Sonuç: [E00A results.md](experiments/E00A-raw-waveform-observation/results.md).
