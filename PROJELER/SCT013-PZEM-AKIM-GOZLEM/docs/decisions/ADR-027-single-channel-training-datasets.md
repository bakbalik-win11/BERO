# ADR-027 — Tek kanallı SCT eğitim veri setleri ve kanal kimliği

- **Tarih:** 2026-11-06
- **Durum:** KABUL EDİLDİ — kullanıcı kararı
- **İlişkili görevler:** [T007 — Home Assistant verisini PC'ye aktarma](../../tasks/T007-python-architecture.md), [T008 — kararlı alan eşleştirme ve etiketleme](../../tasks/T008-stable-window-matching.md)
- **İlişkili mimari:** [Python veri hattı mimarisi](../architecture/python-program-architecture.md)

## Bağlam

Modül 2'nin üç SCT kanalını birlikte okuyan test/ölçüm kodu, donanım ve kanal davranışlarını aynı deney oturumunda gözlemlemek için kullanılabilir. Ancak üç kanalın ölçüm çıktısını tek bir eğitim veri setinde birleştirmek, kanalın fiziksel bağlantı ve sarım/geçiş özelliklerini birbirine karıştırır. Eğitim verisinin hangi fiziksel SCT kanalından geldiği açıkça izlenmelidir.

## Karar

1. **Test ve veri toplama kodu üç kanalı birlikte okuyabilir.** Üç kanallı test firmware'i bu kararla sınırlandırılmaz.
2. **Ham arşiv tüm kanalları koruyabilir.** Home Assistant dışa aktarımındaki mevcut SCT kanallarının kayıtları tek kaynak dosyada bulunabilir; kaynak CSV değişmeden arşivlenir.
3. **Her eğitim veri seti tek bir SCT kanalından oluşur.** Bir eğitim örneğinde aynı anda CH1, CH2 ve CH3 SCT ölçümleri birleştirilmez.
4. **Kanallar ayrı veri setleri ve ayrı model değerlendirmeleri üretir.** CH1 verisiyle eğitilen model CH2 veya CH3 için kendiliğinden geçerli kabul edilmez. Kanallar arası aktarım ancak ayrı deney ve doğrulamayla değerlendirilebilir.
5. **PZEM akımı proje referans akışıdır.** Seçilen tek SCT kanalının geçerli kararlı alanları, aynı BOOT_ID + EVENT_ID paketine ait PZEM akışının geçerli kararlı alanlarıyla mevcut ADR-022/023/024/025 kurallarına göre eşleştirilir. PZEM mutlak ground truth olarak tanımlanmaz.
6. Her eğitim seti ve türetilmiş kayıt, en azından seçilen kanal kimliğini, fiziksel sarım/geçiş bilgisini, kaynak dosya/hash bilgisini, firmware/kod sürümünü, calibration_id bilgisini (varsa gerçek değer; yoksa uydurulmaz) ve kullanılan PZEM referans akışını izlenebilir biçimde taşımalıdır.
7. Ham kayıt, tek kanal seçimi veya eğitim için dönüştürülürken değiştirilmez. Kanal seçimi ve eğitim verisi ayrı türetilmiş çıktılardır.

## Kanal kimliği ve adlandırma

Kod, HA entity ve Python veri hattında aynı kanal kimliğinin kullanılması hedeflenir. Önerilen okunabilir kimlik biçimi:

- `CH1-1T`
- `CH2-4T`
- `CH3-3T`

Bu biçimde CH numarası fiziksel ölçüm kanalını, T sayısı fiziksel geçiş/sarım bilgisini belirtir. Depodaki mevcut donanım notlarında başlangıç eşlemesi CH1 sarı/GPIO32 = 1 geçiş, CH2 yeşil/GPIO33 = 4 geçiş, CH3 mavi/GPIO34 = 3 geçiş olarak kayıtlıdır. Bu eşleme kod/entity adlarına uygulanmadan önce gerçek bağlantıyla doğrulanmalıdır; mevcut YAML/entity etiketinde eski veya farklı bir ad bulunabilir. Fiziksel bağlantı ya da geçiş sayısı değişirse donanım kaydı, kod kimliği ve veri metadata'sı birlikte güncellenir.

`CH1-1T` biçimi bu ADR'de **önerilen adlandırma standardıdır**; mevcut firmware, entity veya klasör adlarının bu standarda dönüştürüldüğü iddia edilmez.

## Kapsam dışı / değiştirmeyen kararlar

- Üç kanallı test firmware'ini tek kanala indirmez.
- ADR-022'nin BOOT_ID + EVENT_ID paket eşleştirme kuralını değiştirmez.
- ADR-024'ün eksik/bozuk paketleri eğitim dışında bırakma kuralını değiştirmez.
- ADR-026'nın gelen-kutu/arşiv ve iki bağımsız Python programı sınırını değiştirmez.
- Kararlılık eşiklerini, pencere süresini, model biçimini veya katsayıyı belirlemez.
- Üç kanallı ham veriyi arşivden silmez veya yalnız bir kanalı saklama zorunluluğu getirmez.

## Uygulama durumu

Bu ADR veri mimarisi kararıdır. Firmware, HA entity adları veya Python kodu bu kararla değiştirilmiş değildir. Gerçek kanal bağlantıları ve sarım/geçiş sayıları kod standardına geçirilmeden önce teyit edilmelidir. T007/T008 uygulaması ve gerçek tek-kanal eğitim çıktısı henüz tamamlanmamıştır.
