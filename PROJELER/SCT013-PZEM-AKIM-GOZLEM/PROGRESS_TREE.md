# BERO — İlerleme Ağacı

> **Amaç:** Depoyu baştan sona okumadan projenin genel yapısını, nerede olduğumuzu ve sıradaki adımı kabaca görebilmek. Bu dosya bir özet/navigasyon haritasıdır; ayrıntılı kayıtların yerine geçmez.

## Şu an nerede?

- **Aktif faz:** Faz 1 — SCT analog ön uç ve yüksüz ölçüm hazırlığı.
- **E00F-N03:** 100 W akkor yük 10:32'de açıldı, kullanıcı beyanına göre 10:39'da kapatıldı. İkinci DEBUG kaydında Raw AC 10:39:27–10:39:29 arasında başlangıç tabanına döndü. Aç-kapa gözlemi desteklendi; CT yerleşimi kullanıcı tarafından doğrulandı: yalnız faz, tek geçiş (1 tur). PZEM karşılaştırması ve genel kabul ölçütleri ayrı aşamada. [Kısmi rapor](experiments/E00F-unthresholded-overnight-log/E00F-N03-incandescent-step-observation.md).
- **Depo belge tutarlılığı denetimi:** TAMAMLANDI; 87 Markdown dosyasındaki göreli bağlantı hedefleri kontrol edildi ve bulunan tek kırık bağlantı düzeltildi.
- **E00B firmware:** HAZIRLANDI ve kullanıcı bildirimiyle DERLENDİ; fiziksel pinout, bağlantı, cihaza yükleme ve ölçüm bekliyor.
- **İlk teknik deney (denetim sonrası):** E00A — ham ADC kaydı ve temel istatistikler.
- **E00A durumu:** SCT bağlı olmayan bias-only Vmid alt adımı son ESP32D2 loguyla KAPATILDI. 603 geçerli eşleşme; GPIO35 standart sapma 6.474 mV, GPIO34 RAW standart sapma 6.97 count. RAW=0 başlangıç kayıtları eşleştirme dışı. E00A bütünü AÇIK: L78L33 3.3 V ayrı bölücü koşulu ve ham CSV/zaman grafiği henüz yok.
- **E00A ilk hedefi:** SCT bağlamadan bias trafosunun L78L33 çıkışını (ilk multimetre bildirimi 3,31 V; KULLANICI BİLDİRİMİ) ve ardından yaklaşık 1,65 V Vmid noktasını ESP32 ADC ile ayrı ayrı gözle. Her koşul 30 saniye planlandı. 3,3 V için ayrı/geçici 10k/10k ölçüm bölücüsü henüz kurulmadı; ADC bağlantısı öncesi kart/pinout ve ADC sınırları doğrulanacak. GPIO34 fiziksel kart/pinout doğrulanırsa kullanılacak. Firmware dosyası mevcut; kullanıcı derleme/çalışma bildirdi. ADC sayısal sonuçları ve ölçüm kaydı henüz yok. ESP32 dahili ADC ham sayılarını oku, kaydet ve bilgisayarda görselleştir; kaydın/paketin sinyali ne ölçüde temsil ettiğini gözlemle. PZEM, akım formülü/kalibrasyon ve MCP3208 bu ilk adımın kapsamında değil. Donanım bağlantısı öncesi gerçek kart/pinout ve bias düzeni kontrol edilir.
- **Yeni deney:** [E00B — SCT bağlı, akımsız hat ADC gözlemi](experiments/E00B-sct-connected-no-current/README.md) FIRMWARE DERLENDİ (KULLANICI RAPORU). Bias GPIO34/35 korunur; SCT için GPIO32 RAW ve GPIO33 voltaj tanımlandı. Gerçek kart pinout'u doğrulanmadan fiziksel bağlantı yapılmayacak.
- **Sonraki adımlar:** E00B pinout/bağlantı doğrulaması, cihaza yükleme ve akımsız koşul logu; E00A'nın 3.3 V koşulu ve ham CSV/grafik gereksinimi açık kalır.
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


### E00A — Adım 2 karar düzeltmesi (2026-10-30)
0.142 V yazılım ofseti kaldırılıyor. GND'de 0.000 V göstermesi, bias açıkken gerçek DC seviyeyi 0.142 V aşağı kaydırdı. Bias logundaki filtreli ortalama yaklaşık 1.525 V; ofset geri eklendiğinde hesaplanan filtresiz tahmin yaklaşık 1.667 V ve kullanıcı multimetre bildirimi 1.654 V ile fark yaklaşık 13 mV. Sıfırlama gerçeği gizlediği için GND'deki 0.142 V korunacak. Ofsetsiz firmware'in derlenmesi/cihazda çalışması henüz bekleniyor. Ayrıntı: [E00A sonuç kaydı](experiments/E00A-raw-waveform-observation/results.md).


## 2026-10-30 — SCT'siz bias-only alt adım kapanışı

Son esp32d2-logs.txt kaydı analiz edildi. SCT bağlı değilken Vmid koşulunda GPIO35 ortalama 1.665138 V, standart sapma 6.474 mV; GPIO34 RAW ortalama 1846.80 count, standart sapma 6.97 count. Bu, ölçüm zincirinin gözlenen taban dalgalanmasıdır; ADC'ye özgü gürültü olarak ayrıştırılmamıştır. Ayrıntı [E00A sonuç kaydında](experiments/E00A-raw-waveform-observation/results.md). E00A'nın diğer koşulları açık.


## 2026-10-30 — E00B deney açılışı

SCT bağlı, izlenen iletkende akım yok koşulu için E00B açıldı. Bias GPIO34/35 kanalları korunuyor; SCT analog düğümü için GPIO32 RAW ve GPIO33 voltaj kanalları önerildi (ESP32-WROOM-32D ADC1_CH4/CH5). Gerçek geliştirme kartı pinout'u henüz fiziksel doğrulanmadı. Firmware ve fiziksel deney yapılmadı. Ayrıntı [E00B](experiments/E00B-sct-connected-no-current/README.md).


## 2026-10-30 — E00B yüksüz karşılaştırma sonucu

E00B uzun cihaz logu kaydedildi; 351 geçerli yayın/kanal analizinde SCT ve bias seviyeleri pratik olarak aynı çıktı (RAW fark +0.82 count; ADC voltaj farkı −1.4 mV). [E00B raporu](experiments/E00B-sct-connected-no-current/results.md) ve [ham log](experiments/E00B-sct-connected-no-current/logs/2026-10-30-e00b-esp32d2-long-observation.log). Sonraki yük koşulu ayrı kayıt olacak; mevcut firmware dört kanalı okumaya devam edebilir.


## 2026-10-30 — E08 Aşama 2 açıldı

100 W akkor yük altında SCT013-030 testi hazırlık durumunda açıldı. İlk koşul 1 tur × 1.000 örnek/s; tam matris 1/2/4 tur × 1/2/2,5 kS/s. Mevcut E00B firmware'i 1 saniyelik yayın yaptığı için E08 yüksek hızlı edinimine uygun değil. Ayrı firmware, gerçek örnekleme hızı doğrulaması ve fiziksel ölçüm bekleniyor. [Aşama 2 protokolü](experiments/E08-sct-characterization/stage-02-100w-matrix.md).


## 2026-10-30 — E08 gözlem yaklaşımı güncellendi

100 W akkor yük gözleminde mevcut E00B firmware'i değiştirilmeden kullanılacak. 1 saniyelik yayınlar yük altındaki sinyal alanlarının düşük hızlı davranışını görmeye yarayacak. Yüksek hızlı örnekleme ve hızlandırma testleri sonraki aşamaya bırakıldı. Fiziksel test/log henüz yok.


## 2026-10-30 — ESP32D2 / SCT013-030 hazır ct_clamp kodu kaydı

Kullanıcının cihazda kullandığı hazır ESPHome `ct_clamp` yapılandırması [firmware/esp32d2.yaml](firmware/esp32d2.yaml) olarak kaydedildi. Katsayı 24.22, eşik 0.35 A, GPIO33, 200 ms örnekleme penceresi ve 2 s yayın aralığı korunmuştur. 150 W akkor ve kettle testlerinde yaklaşık ±%4 hedefi içinde kullanıcı raporlu karşılaştırmalar vardır. 8.35 W LED / 0.041 A testi eşik nedeniyle görünür akım üretmedi; düşük akım konusu açık. Bu, mevcut çalışan saha yapılandırmasının kaydıdır; E00A/E00B/E08 yol haritası kabul ölçütlerinin tamamlandığı anlamına gelmez. Ayrıntı: [firmware/README.md](firmware/README.md).
