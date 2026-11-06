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

## Kanal kimliği ve değişebilir fiziksel yapılandırma

Kanalın kalıcı kimliği yalnızca `CH1`, `CH2`, `CH3` olmalıdır. Fiziksel geçiş/sarım sayısı kanal kimliğinin parçası değildir; kullanıcı tarafından değiştirilebilir bir donanım yapılandırmasıdır.

Eğitim kayıtlarında bu iki bilgi ayrı alanlarda tutulur:
- `channel_id`: `CH1`, `CH2` veya `CH3` — fiziksel ölçüm girişini tanımlar.
- `turn_count`: ilgili deney/kurulum sırasında doğrulanmış fiziksel geçiş/sarım sayısı — zaman içinde değişebilir.

Geçiş sayısı değiştiğinde kanal kimliği sabit kalır; donanım yapılandırma kaydı ve ilgili deney/eğitim metadata'sı yeni değerle güncellenir. Eski veriler kendi toplandıkları dönemin `turn_count` değeriyle korunur; geçmiş kayıtlar yeni geçiş sayısına göre geriye dönük değiştirilmez. Mümkünse yapılandırma değişikliği tarih/saat ve deney kimliğiyle ilişkilendirilir.

Depodaki mevcut donanım notlarında başlangıç eşlemesi CH1 sarı/GPIO32 = 1 geçiş, CH2 yeşil/GPIO33 = 4 geçiş, CH3 mavi/GPIO34 = 3 geçiş olarak kayıtlıdır. Bu değerler yalnız mevcut kayıtlı durumdur; kalıcı özellik veya değişmez kanal adı değildir. Gerçek bağlantı ve geçiş sayısı her deney/kurulum değişikliğinde doğrulanmalıdır.

`CH1-1T`, `CH2-4T`, `CH3-3T` biçimleri kalıcı kanal kimliği olarak kullanılmayacaktır. Bunlar en fazla belirli bir tarihteki kanal + fiziksel yapılandırmayı anlatan geçici gösterimler olabilir; kod, entity ve eğitim seti anahtarlarında `channel_id` ile `turn_count` ayrı tutulmalıdır.

## Kapsam dışı / değiştirmeyen kararlar

- Üç kanallı test firmware'ini tek kanala indirmez.
- ADR-022'nin BOOT_ID + EVENT_ID paket eşleştirme kuralını değiştirmez.
- ADR-024'ün eksik/bozuk paketleri eğitim dışında bırakma kuralını değiştirmez.
- ADR-026'nın gelen-kutu/arşiv ve iki bağımsız Python programı sınırını değiştirmez.
- Kararlılık eşiklerini, pencere süresini, model biçimini veya katsayıyı belirlemez.
- Üç kanallı ham veriyi arşivden silmez veya yalnız bir kanalı saklama zorunluluğu getirmez.

## Uygulama durumu

Bu ADR veri mimarisi kararıdır. Firmware, HA entity adları veya Python kodu bu kararla değiştirilmiş değildir. Gerçek kanal bağlantıları ve her deneydeki sarım/geçiş sayıları doğrulanmalıdır; geçiş sayısı kanal kimliğinden bağımsız ve değişebilir metadata'dır. T007/T008 uygulaması ve gerçek tek-kanal eğitim çıktısı henüz tamamlanmamıştır.
