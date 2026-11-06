# I009 — 57 W ve 57 W + 15 W yük basamakları

## Amaç

OFF referansından düşük yük davranışına, oradan hesaplanabilir akım bölgesine geçişi istatistiksel olarak incelemek. Bu deney iki ardışık fakat ayrı yük koşulundan oluşur:

1. 57 W tekil yük.
2. 57 W + 15 W birleşik yük.

Amaç yalnızca amper değerinin doğruluğunu ölçmek değildir. Her yük koşulunun OFF davranışından ayrışmasını, SCT çıktısının dağılımını ve güvenilir akım hesabına elverişli olup olmadığını incelemektir. 57 W veya birleşik yükün hesaplanabilir olduğu önceden varsayılmaz.

## Deney başlangıç durumu

- Tarih: 2026-11-06
- Kullanıcı planı: 42 W deneyinden sonra yaklaşık 5 dakika içinde 57 W deneyine geçmek; ardından 57 W + 15 W denemek.
- Gerçek 57 W başlangıç saati: **bekleniyor**.
- Gerçek birleşik yük başlangıç saati: **bekleniyor**.
- Ölçüm kodu: Kullanıcı, mevcut kodun aynı kalacağını belirtti. Firmware/build hash'i ayrıca doğrulanmadı.
- Ölçüm kanalı: Önceki CH1-1T deney zinciri; yeni fiziksel bağlantı teyidi yok.
- Analiz edilen SCT sinyali: K çarpımı öncesindeki katsayısız ct_clamp çıktısı; tekil ADC ham örneği değildir.

## Değişmez deney koşulları

- İki basamak boyunca kod ve ölçüm parametreleri değiştirilmez.
- İki yük koşulu ayrı veri sınıflarıdır; birleştirilerek tek grup yapılmaz.
- Fiziksel ON/OFF zamanları kullanıcı gözlemi ve PZEM zaman serisiyle belirlenir. UDP/SSR işareti tek başına fiziksel yük kanıtı sayılmaz.
- Ham veri korunur; geçiş ve sıçrama örnekleri silinmez. Kararlı alan istatistikleri için ayrı seçim maskesi uygulanır.
- PZEM, zaman penceresi ve yük durumunu destekleyen pratik referanstır; mutlak ground truth değildir.
- 57 W + 15 W birleşik yük sonucu, 57 W tekil yük sonucundan ayrı tutulur.

## Analiz yöntemi

Her yük basamağında fiziksel ON/OFF çevrimleri ayrı segmentlenir. Geçiş bölgeleri kararlı ON/OFF özetlerine katılmaz; ancak ham kayıtta korunur.

Her çevrim ve durum için:
- SCT medyanı ve MAD,
- P05/P95/P99,
- örnek sayısı,
- zaman dilimli medyan değişimi,
- ON–OFF medyan farkı ve çevrimler arası tutarlılık

hesaplanır. PZEM akım ve güç değerleri aynı zaman aralıklarında kendi geçerli örnekleriyle ayrı özetlenir; SCT ile örnek sayısı eşit varsayılmaz.

OFF / 15 W / 42 W / 57 W / 57 W+15 W dağılımları ayrı gruplar olarak karşılaştırılır. Aynı kayıtlar 5, 10, 20, 30 ve 60 saniyelik pencerelerde incelenerek kısa ve uzun pencerelerdeki ayrışma değerlendirilir. Bu süreler analiz adaylarıdır; karar gecikmesi veya eşik olarak onaylanmış değildir.

## Karar sınırı

Üç çıktı birbirinden ayrıdır:
- `NO_CURRENT`: OFF referansıyla yeterli istatistiksel uyum.
- `CURRENT_PRESENT`: Akım varlığına yeterli kanıt ve hesaplama için yeterli kararlılık.
- `CURRENT_NOT_COMPUTABLE`: Akım olasılığı var, ancak mevcut pencere/dağılım hesaplanabilir değer üretmek için yeterli değil.

57 W veya birleşik yükte hesaplanabilirlik sonucu önceden atanmaz. Sonuçlar medyan, MAD, dağılım örtüşmesi ve tekrarlı çevrim tutarlılığıyla belirlenecektir.

## Bekleyen kayıtlar

- Gerçek 57 W başlangıç/bitiş zamanı ve CSV.
- Gerçek 57 W + 15 W başlangıç/bitiş zamanı ve CSV.
- Her iki basamakta PZEM güç/akım zaman serisi.
- Firmware/build doğrulaması varsa ilgili log ve hash.

**Durum: PLANLANDI.** Bu dosya deney planıdır; deneylerin başladığını veya tamamlandığını göstermez.
