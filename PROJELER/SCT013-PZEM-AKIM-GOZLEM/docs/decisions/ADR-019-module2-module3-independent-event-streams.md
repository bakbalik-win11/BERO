# ADR-019 — Modül 2/3 bağımsız kayıt akışları ve olay-zaman temelli kararlı alan eşleştirmesi

- **Tarih:** 2026-11-01
- **Durum:** KABUL EDİLDİ — mimari karar
- **Kapsam:** SCT013 + PZEM uygulaması; Faz 2 veri toplama ve T008 kararlı alan eğitimi
- **İlişkili kayıtlar:** ADR-010, T007, T008, Python veri hattı mimarisi

## Bağlam

Modül 2 ve Modül 3 farklı ölçüm ve olay akışları üretir. UDP yayınındaki paket kimliği, zaman ve SSR ON/OFF bilgisi olay/zaman çizgisini tarif eder; tek başına SCT veya PZEM ölçüm kaydı değildir. Bu nedenle mikrodenetleyici tarafında olay kaydı ile ölçüm kaydını zorla tek kayda bağlamak doğru değildir. İlişkilendirme Python tarafında, veriler HA geçmişinden PC'ye alındıktan sonra yapılacaktır.

## Karar

### Modül 2

Modül 2 iki bağımsız kayıt akışını Home Assistant'a aktarır:

1. **Ölçüm akışı:** Modül 2'nin mevcut SCT okuma sistemiyle ürettiği SCT ölçüm kayıtları.
2. **Olay akışı:** UDP yayınıyla aldığı paket/BOOT_ID/EVENT_ID, zaman ve SSR ON/OFF bilgisi.

UDP olay kaydı, SCT ölçüm kaydının alanı veya zorunlu eşleştirilmiş eki değildir. Olay paketi geldikçe kendi başına kaydedilir; SCT ölçümü geldikçe kendi başına kaydedilir.

### Modül 3

Modül 3 iki işi aynı sistemde yürütür:

1. **UDP yayın akışı:** Paket/BOOT_ID/EVENT_ID, saat bilgisi ve SSR ON/OFF olaylarını yayınlar.
2. **Home Assistant kayıt akışı:** PZEM ölçümlerini ve aldığı/ürettiği aradaki yayın/olay bilgilerini ayrı kayıt akışları olarak HA'ya aktarır.

PZEM ölçüm kaydı ile olay/yayın kaydı HA'da ayrı kalır. UDP yayın düzeni mevcut paket protokolü ve port/adres kararlarıyla korunur; bu ADR mevcut protokolün ayrıntılarını değiştirmez.

### Python ve kararlı alan eğitimi

Python, HA'dan alınan bağımsız kayıt akışlarını sonradan zaman ve olay bilgisi üzerinden birlikte değerlendirir:

1. SCT ölçümleri, PZEM ölçümleri ve olay/yayın kayıtları ayrı kaynak akışları olarak içeri alınır; ham state, entity_id, birim, kaynak timestamp/timezone ve kaynak kökeni korunur.
2. BOOT_ID ve EVENT_ID, mevcut oldukları yerde olay dizisini/cihaz açılışını ayırt etmek için kullanılır.
3. Olay timestamp'leri ve ON/OFF geçişleri kullanılarak yükün açık/kapalı ve geçiş zaman çizgisi yeniden kurulur.
4. PZEM ve SCT kararlılığı birbirinden bağımsız hesaplanır.
5. Olay/zaman çizgisi, kararlı pencerelerin sınırlarını ve yük durumunu yorumlamak/eşleştirmek için yardımcı kanıt olarak kullanılır.
6. Yalnız zaman bakımından örtüşen ve kendi ölçüm akışında kararlı bulunan PZEM/SCT pencereleri eşleştirilir.
7. Geçerli PZEM değeri, eşleşen SCT kararlı penceresi için proje referans etiketi olur; mutlak ground truth sayılmaz.

## Değişmez ilkeler

- ESP/HA tarafında ölçüm ve olay kayıtları bağımsızdır; birebir örnek eşleştirmesi veya aynı anda kayıt zorunluluğu yoktur.
- UDP olayının alınma zamanı ile paketin taşıdığı kaynak olay zamanı farklıysa ikisi karıştırılmaz; mevcut veri alanları izin verdiği ölçüde kaynak zaman korunur.
- Python tarafındaki eşleştirme sonradan ve tekrar üretilebilir biçimde yapılır; zaman toleransı, kararlılık eşiği ve pencere uzunluğu gerçek HA örnekleri incelendikten sonra belirlenir.
- Zaman damgaları yapay olarak yuvarlanmaz veya akışlar aynı örnekleme hızına zorlanmaz.
- Geçiş/yerleşme alanları kararlı eğitim penceresi olarak etiketlenmez; ayrı tutulur.
- Eksik/geçersiz olay paketi, timeout, NaN, -1.0 ve parse hataları silinmez; gerekçesiyle işaretlenir ve etiketleme dışında tutulur.
- Sürekli ham ADC dalga biçimi arşivleme kararı değişmez.
- Bu karar donanım/firmware entegrasyonunun yapıldığı veya test edildiği anlamına gelmez.

## Kabul gerekçesi

Bu ayrım, Modül 2 ve Modül 3'ün kendi görevlerini bağımsız sürdürmesini sağlar; olay zaman çizgisi ise Python'da SCT/PZEM kararlı pencerelerini bağlamlandırmak ve eğitim verisini doğru bölmek için kullanılabilir. Ölçüm ve olay kayıtlarının bağımsız saklanması kaynak verinin kaybolmasını ve ESP tarafında hatalı birebir eşleştirme varsayımını önler.
