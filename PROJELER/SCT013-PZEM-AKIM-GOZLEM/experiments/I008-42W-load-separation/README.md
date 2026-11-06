# I008 — 42 W yük davranışı / OFF ve 15 W karşılaştırması

## Oturum başlangıç kaydı

- Tarih: 2026-11-06
- Kullanıcının bildirdiği fiziksel yük başlangıcı: 17:00 (+03:00)
- Yük: 42 W (kullanıcı mevcut yükün 42 W olduğunu belirtti; önceki 47 W tahmini düzeltilmiştir)
- Ölçüm kodu/firmware: Kullanıcı bildirimiyle 15 W deneyindeki kod aynı; bu notta firmware hash'i veya cihaz loguyla bağımsız doğrulama yapılmamıştır.
- Kanal: CH1-1T / SCT013 30A/1V / GPIO32 / ADC1_CH4 (önceki deney zinciriyle aynı olduğu kullanıcı bağlamından aktarılmıştır; fiziksel bağlantı ayrıca doğrulanmadı).
- Analiz edilen SCT alanı: K çarpımı öncesi katsayısız ct_clamp çıktısı; ADC'nin tekil ham örneği değildir.
- Deney amacı: 42 W koşulunun OFF ve 15 W davranışlarından istatistiksel olarak ne ölçüde ayrıştığını, özellikle kısa ve uzun karar pencerelerinde değerlendirmek.
- Bu bir K katsayısı eğitimi değildir. 42 W ayrı yük seviyesi olarak tutulur.

## Deney kuralları

- Kod ve ölçüm ayarları deney boyunca değiştirilmez.
- Fiziksel ON/OFF zamanları kullanıcı gözlemiyle kaydedilir; SSR/UDP olayları tek başına fiziksel yük kanıtı değildir.
- PZEM akım/güç timestamp'leri yeni ve güncel kayıtlarla doğrulanır.
- Ham kayıt korunur; geçişler silinmez.
- ON ve OFF çevrimleri ayrı segmentlenir. Kararlı alanlar geçişlerden ayrı değerlendirilir.
- 42 W verisi 15 W veya OFF dağılımına karıştırılmaz; ayrı yük sınıfıdır.

## Analiz planı

Her fiziksel ON/OFF çevrimi için SCT medyanı, MAD, P05/P95/P99, örnek sayısı ve zaman kararlılığı hesaplanır. PZEM akım/güç serisi ayrı olarak aynı zaman pencerelerine hizalanır; PZEM ölçümleri kendi geçerli örnekleriyle özetlenir.

Aynı kayıttan 5, 10, 20, 30 ve 60 saniyelik karar pencereleri denenerek:
- OFF / 15 W / 42 W dağılım ayrışması,
- pencere uzunluğuna göre medyan ve MAD kararlılığı,
- sınıflar arası dağılım örtüşmesi,
- karar için gereken gözlem süresi
incelenir.

Kısa pencerede ayrışma yoksa sonuç zorla AKIM VAR veya AKIM YOK yapılmaz; `CURRENT_NOT_COMPUTABLE` olasılığı korunur.

## Durum

**BAŞLADI — yalnızca başlangıç saati ve 42 W yük bilgisi kullanıcı bildirimiyle kayıtlıdır.** CSV, gerçek PZEM değerleri, süre ve sonuçlar henüz alınmadı.
