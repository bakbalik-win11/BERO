# ADR-022 — Paket işaretleriyle akış bölümleme ve eğitim verisi oluşturma

- **Tarih:** 2026-11-01
- **Durum:** KABUL EDİLDİ — kullanıcıyla netleştirilen mimari karar; firmware uygulaması bekliyor
- **Kapsam:** Modül 2 SCT akışı, Modül 3 PZEM/SSR akışı, UDP olay yayını ve Python eğitim veri hattı
- **İlişkili kayıtlar:** ADR-019, T007, T008

## Bağlam

PZEM ve SCT farklı hızlarda ölçüm üretir. Özellikle yük kapanırken/açılırken PZEM'in ölçümü basamaklı ve gecikmeli değişebilir; SCT ise değişimi daha hızlı gösterebilir. Ölçüm örneklerini timestamp üzerinden birebir eşleştirmek, PZEM'in geçiş değerlerini SCT'nin farklı fiziksel durumdaki değerleriyle eşleştirerek eğitim etiketini bozabilir.

ESP'lerin her ölçüm kaydına sürekli zaman/paket bilgisi eklemesi de gereksiz işlem ve kayıt yükü oluşturur. ESP'ler kararlılık analizi, kırpma, eşleştirme veya katsayı hesaplama yapmayacaktır.

## Karar

### 1. Ölçüm akışları bağımsız kalır

- Modül 3 PZEM'i kendi bağlantısından okumaya ve mevcut PZEM ölçüm yayınlarını sürdürmeye devam eder.
- Modül 2 SCT ölçümlerini kendi okuma düzeninde üretmeye devam eder.
- Ölçüm kayıtlarının içine her örnek için BOOT_ID, EVENT_ID veya zaman alanı eklenmez.
- PZEM ve SCT ölçüm yayın hızları birbirine zorlanmaz.

### 2. Modül 3 olay işaretinin kaynağıdır

SSR durumu değiştiğinde Modül 3 tek bir olay mesajı oluşturur. Mesajın biçimi mevcut UDP protokolüyle aynıdır:

`BERO_EVT,BOOT_ID=XXXXXXXX,EVENT_ID=N,STATE=ON|OFF,TIME=YYYY-MM-DD HH:MM:SS`

- Modül 3 aynı olay mesajını UDP port 4210 üzerinden Modül 2'ye yayınlar.
- Modül 3 aynı mesajı kendi PZEM kayıt akışına, PZEM ölçümlerinin arasına ayrı bir olay kaydı olarak ekler.
- Olay mesajı sürekli veya her PZEM ölçümünde tekrarlanmaz; yalnızca olay değiştiğinde üretilir.
- Modül 3 kendi yerel PZEM olay kaydını UDP paketini geri dinleyerek oluşturmaz; olayın kaynağı kendisidir.

### 3. Modül 2 aynı olay kaydını SCT akışına ekler

- Modül 2 UDP 4210 üzerinden Modül 3'ün olay mesajını dinler.
- Geçerli mesajı kendi SCT kayıt akışına ayrı bir olay kaydı olarak ekler.
- Modül 2 BOOT_ID/EVENT_ID/STATE/TIME değerlerini yeniden üretmez veya bağımsız sayaçla değiştirmez; aldığı olay mesajının içeriğini korur.
- Modül 2'nin SCT ölçüm kayıtlarına her örnek için olay alanı eklenmez.

### 4. Olay kaydı ile ölçüm kaydı arasındaki biçim

Olay işareti, ölçüm değerinin alanı değildir; ölçüm akışında araya giren ayrı bir kayıttır. Modül 2 ve Modül 3'ün HA tarafına aktardığı olay işaretinin metin biçimi aynı olmalıdır. Python, her modülün ölçüm kayıtları ile o modüle ait olay işaretlerini kendi akışı içinde sıraya koyarak paket sınırlarını yeniden kurar.

HA dışa aktarımında kayıtlar ayrı entity geçmişlerinde bulunuyorsa Python, her modülün kendi entity kayıtları ve olay işaretleri arasında yerel sıralamayı kurmak için HA kaynak timestamp'lerini kullanabilir. Bu işlem yalnızca aynı modül içindeki olay işaretinin hangi kayıtların arasına düştüğünü bulmak içindir; Modül 2 ve Modül 3 ölçümlerini timestamp ile birbirine eşleştirmek değildir.

### 5. Python'ın görevi

1. Modül 3 PZEM akışındaki olay işaretlerini okuyarak PZEM kayıtlarını ardışık paket aralıklarına ayırır.
2. Modül 2 SCT akışındaki aynı olay işaretlerini okuyarak SCT kayıtlarını aynı paket aralıklarına ayırır.
3. İki modülün aralıklarını `BOOT_ID + EVENT_ID` ile eşleştirir.
4. Her paket aralığında PZEM kararlılığını yalnız PZEM değerlerinden; SCT kararlılığını yalnız SCT değerlerinden bağımsız tespit eder.
5. PZEM'in yükseliş/düşüş ve yerleşme geçişlerini; SCT'nin kendi geçiş/yerleşme bölümlerini eğitim kararlı alanından çıkarır.
6. Aynı paket/olay içindeki karşılaştırılabilir kararlı yük bölgelerinden eğitim örneği oluşturur. PZEM değeri bu örneğin proje referans etiketidir; mutlak ground truth değildir.
7. Eğitim çıktısına `BOOT_ID` ve `EVENT_ID` bilgisini Python ekler. Paket numarası eğitim örneğinin deney/olay kimliğidir; her ham ölçümün içine ESP tarafından yazılmaz.

**Eşleştirme anahtarı paket kimliğidir; zaman değildir.** PZEM ve SCT'nin kararlı pencerelerinin timestamp kesişimi, başlangıç/bitiş eşitliği veya sabit gecikme eşleştirme şartı değildir. Zaman damgası paket işaretinin zamanını ve her akışın kendi iç sırasını korumak için tutulur; iki sensörün örneklerini zaman bazında eşleştirmek için kullanılmaz.

## Hata ve veri bütünlüğü

- UDP olayı Modül 2'ye ulaşmazsa veya iki akıştaki BOOT_ID/EVENT_ID dizisi uyuşmazsa ilgili paket aralığı eksik olarak işaretlenir; tahminle tamamlanmaz ve eğitimden çıkarılır.
- Aynı olay mesajının yinelenmesi, Python tarafında aynı BOOT_ID/EVENT_ID için tekrar olarak tanınır; yinelenen işaret yeni paket aralığı oluşturmaz.
- Geçersiz/eksik olay mesajı normal SCT/PZEM ölçüm kaydı gibi yorumlanmaz.
- ON–OFF aralığı otomatik olarak kararlı kabul edilmez. Kararlılık algoritmaları, toleranslar ve minimum süre gerçek HA verisi üzerinde Python tarafında geliştirilecektir.

## ADR-019 ile ilişki

Bu karar, ADR-019'un bağımsız ölçüm akışları ve ayrı olay işaretleri ilkesini korur. Ancak ADR-019 içindeki iki akışın timestamp bakımından örtüşen kararlı pencerelerinin kesişimini eğitim eşleştirme şartı yapan bölümünü **geçersiz kılar ve onun yerine paket aralığı eşleştirmesini getirir**. ADR-019 tarihsel kayıt olarak korunur; çelişki halinde bu ADR-022 geçerlidir.

## Uygulama durumu ve kanıt sınırı

Bu ADR mimari karardır. Modül 2/Modül 3 YAML değişikliği, derleme, OTA, UDP alım testi, HA Recorder sıralama testi veya fiziksel doğrulama bu kayıtla yapılmış sayılmaz. Firmware değişiklikleri ayrı adımda uygulanıp gerçek logla doğrulanacaktır.
