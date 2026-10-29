# BERO — İlerleme Ağacı

> **Amaç:** Depoyu baştan sona okumadan projenin genel yapısını, nerede olduğumuzu ve sıradaki adımı kabaca görebilmek. Bu dosya bir özet/navigasyon haritasıdır; ayrıntılı kayıtların yerine geçmez.

## Şu an nerede?

- **Aktif faz:** Faz 1 — SCT analog ön uç ve yüksüz ölçüm hazırlığı.
- **Depo belge tutarlılığı denetimi:** TAMAMLANDI; 87 Markdown dosyasındaki göreli bağlantı hedefleri kontrol edildi ve bulunan tek kırık bağlantı düzeltildi.
- **Deney başlangıcı:** BEKLEMEDE — gerçek ESP32 kart/GPIO ve fiziksel bağlantı kontrolü gerekiyor; bu belge denetimi fiziksel test veya firmware doğrulaması değildir.
- **İlk teknik deney (denetim sonrası):** E00A — ham ADC kaydı ve temel istatistikler.
- **E00A durumu:** PLANLANDI; firmware, fiziksel kayıt ve ölçüm henüz yapılmadı.
- **E00A koşulları:** bias-only → SCT bağlı/yüksüz → SCT bağlı/100 W akkor; ilk geçişte tek ESP32, hedef 2 kS/s, koşul başına yaklaşık 1 saniye. ADR-007'deki 10 µF + mevcut 100 nF bias düzeni ilk SCT bağlantılı koşuldan önce planlandı; fiziksel uygulama henüz yok.
- **Sonraki adımlar:** E00 bias ADC karşılaştırması → T005 / E01 yüksüz temel okuma ve gürültü tabanı.
- **Temel kural:** Her adımda HEDEF / LOG / SONUÇ; deney kodunda açıklamalar ve açıklamalı YAML.

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
│   ├── E00A Ham sinyal/istatistik ........ SIRADAKİ — PLANLANDI
│   │   ├── A. Bias-only
│   │   ├── B. SCT bağlı, yüksüz
│   │   └── C. 100 W akkor yük
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
├── 7. Python analizi ve etiketleme
│   └── Kararlı bölgeleri belirleme, PZEM'i eğitim referansı olarak kullanma
│
└── 8. İyileştirme ve bakım
    └── Sonuçlara göre ayarları geliştirme; değişiklik geçmişini koruma
```

Faz 2–8, yol haritasındaki daha sonraki iş alanlarıdır; bu görünüm onların uygulandığı veya tamamlandığı anlamına gelmez. Deney numaraları ve sıralaması için [deney indeksi](experiments/README.md), görev durumları için [görev listesi](tasks/README.md), ayrıntılı sıra için [ROADMAP.md](ROADMAP.md) kullanılır.

## Depoda nereye bakılır?

| Deneyin nedenini, uygulama kodunu ve kanıtını birlikte izlemek | [EXPERIMENT_LEDGER.md](EXPERIMENT_LEDGER.md) |

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
