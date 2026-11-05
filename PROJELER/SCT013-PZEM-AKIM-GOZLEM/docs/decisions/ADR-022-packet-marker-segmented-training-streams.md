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
3. Her iki akışta aynı fiziksel ON başlangıç işaretini `BOOT_ID + EVENT_ID` ile doğrular. Paket kimliği, ON başlangıç işaretinin kimliğidir; çünkü `EVENT_ID` her SSR durum değişiminde artar ve onu izleyen OFF işaretinin kendi farklı `EVENT_ID` değeri vardır. OFF işareti, ilgili akışta ON paketini kapatan beklenen sonraki durum olayı olarak ayrıca doğrulanır.
4. Her iki modülde ON başlangıç işaretinin `BOOT_ID + ON_EVENT_ID` kimliği aynı olmalıdır. Her akışta bu ON olayını izleyen OFF kapanışı ayrıca doğrulanır; karşılık gelen OFF işaretleri iki akışta da aynı `BOOT_ID + OFF_EVENT_ID` kimliğini taşımalıdır. Normal ON→OFF çevriminde `OFF_EVENT_ID = ON_EVENT_ID + 1` olmalıdır. ON ile OFF arasında olay numarası boşluğu, farklı OFF kimliği veya eksik kapanış varsa paket bütünlüğü reddedilir; neden raporlanır.
5. Her ON paketinde PZEM kararlılığını yalnız PZEM değerlerinden; SCT kararlılığını yalnız SCT değerlerinden bağımsız tespit eder.
6. PZEM'in yükseliş/düşüş ve yerleşme geçişlerini; SCT'nin kendi geçiş/yerleşme bölümlerini eğitim kararlı alanından çıkarır.
7. Aynı ON paketindeki bağımsız SCT ve PZEM kararlı aralıklarının zaman kesişimini hesaplar. Yalnız kesişen zaman aralığı karşılaştırılabilir eğitim adayıdır. Kesişim yoksa etiket üretilmez; ham kayıt korunur ve `NO_STABLE_OVERLAP` gibi açık bir dışlama nedeni raporlanır.
8. PZEM değeri bu örneğin proje referans etiketidir; mutlak ground truth değildir.
9. Eğitim çıktısına paket kimliği olan ON başlangıcının `BOOT_ID` ve `EVENT_ID` bilgilerini Python ekler. Ham ölçüm kayıtlarının içine ESP tarafından sürekli olay kimliği yazılmaz.

**Paket eşleştirme anahtarı `BOOT_ID + ON_EVENT_ID` birleşimidir; zaman değildir.** Bu kimlik, iki modüldeki aynı fiziksel ON başlangıç işaretini ve dolayısıyla paket başlangıcını tanımlar. Karşılık gelen OFF kapanış işareti her akışta ayrıca doğrulanır; OFF işaretinin EVENT_ID değeri ON ile aynı değildir. Paket bütünlüğü doğrulandıktan sonra zaman damgaları, aynı ON paketi içindeki SCT ve PZEM kararlı aralıklarının zaman bakımından kesişip kesişmediğini belirlemek için kullanılır. Bu kesişim paket eşleştirme anahtarı değil, eğitim etiketi üretmeye uygunluk koşuludur. Tekil SCT/PZEM örnekleri timestamp üzerinden birebir eşleştirilmez, interpolasyonla eşleştirilmez ve sabit gecikme varsayılmaz. HA timestamp'lerinin iki akış arasında karşılaştırılabilirliği, olay sırası ve kararlı aralık sınırları gerçek dışa aktarım üzerinde doğrulanmadan zaman hassasiyeti hakkında ek iddia kurulmaz.

## BOOT_ID, EVENT_ID ve zaman damgasının kesin görevi

- **BOOT_ID:** Modül 3'ün her açılışında/yeniden başlatılmasında bir kez yeni kimlik üretilir. Aynı açılış oturumu boyunca bütün SSR olaylarında sabit kalır.
- **EVENT_ID:** Modül 3'te her SSR durum değişiminde artan uint32 olay numarasıdır. Normal SSR çevrimi ON→OFF şeklinde ilerlediği için bir ON olayını izleyen OFF olayının numarası bir sonraki değerdir. ON ve OFF farklı EVENT_ID taşır.
- **Olay mesajı:** ADR-023 uyarınca yalnızca `BERO_EVT,BOOT_ID=<32 HEX>,EVENT_ID=N,STATE=ON|OFF` alanlarını taşır. Mesajda TIME alanı yoktur.
- **HA timestamp'i:** Home Assistant Recorder'ın her entity kaydına verdiği timestamp, olay mesajının alanı değildir. Yalnızca ilgili modülün kendi kayıtlarını sıralamak ve gerçek dışa aktarımda karşılaştırılabilirliği ayrıca doğrulandıktan sonra aynı ON paketi içindeki kararlı aralıkların zaman kesişimini incelemek için kullanılabilir.
- **Paket eşleştirme anahtarı:** ON başlangıç işaretinin `BOOT_ID + ON_EVENT_ID` birleşimidir. Karşılık gelen OFF kapanış anahtarı `BOOT_ID + OFF_EVENT_ID` olarak ayrı doğrulanır. İki akışta ON anahtarları aynı; OFF anahtarları da aynı olmalıdır. Normal çevrimde OFF_EVENT_ID, ON_EVENT_ID'nin bir fazlasıdır. Bu şart sağlanmıyorsa paket reddedilir.
- **Modül 2:** Modül 3'ten aldığı BOOT_ID, EVENT_ID ve STATE alanlarını aynen korur. Modül 2 kendi BOOT_ID'sini veya EVENT_ID'sini üretmez; olaya TIME eklemez.

Örnek olay biçimi:

`BERO_EVT,BOOT_ID=<32 HEX>,EVENT_ID=N,STATE=ON|OFF`

ADR-023, ADR-022'nin önceki TIME içeren olay biçimini ve TIME alanı açıklamalarını geçersiz kılar. Çelişki halinde TIME'sız mesaj biçimi ve ADR-023 geçerlidir.

## Fiziksel kurulum ve kodlama sırası

- Modül 3 şu anda masa üstünde, nihai fiziksel montajı yapılmamış durumdadır. Bu durum kullanıcı bildirimi olarak kaydedilmiştir.
- Önce mevcut masa üstü bağlantı düzeninde firmware hazırlanır; yapılandırma/derleme, düşük gerilimli işlev testleri, PZEM okuma, SSR mantıksal ON/OFF ve olay üretimi, UDP gönderim/alım ve HA kayıt davranışı ayrı ayrı doğrulanır.
- Testler ve kod davranışı doğrulandıktan sonra kullanıcı modülün fiziksel montajını/toplamasını yapacaktır. Montajın tamamlanması veya saha bağlantılarının doğrulanması önceden varsayılmaz.
- Kodun derlenmesi tek başına donanımın çalıştığını kanıtlamaz. Her aşama gerçek log/çıktı ile kaydedilir; başarısız veya henüz denenmemiş adım açık bırakılır.

## Hata ve veri bütünlüğü

- UDP olayı Modül 2'ye ulaşmazsa veya iki akıştaki BOOT_ID/EVENT_ID dizisi uyuşmazsa ilgili paket aralığı eksik olarak işaretlenir; tahminle tamamlanmaz ve eğitimden çıkarılır.
- Aynı olay mesajının yinelenmesi, Python tarafında aynı BOOT_ID/EVENT_ID için tekrar olarak tanınır; yinelenen işaret yeni paket aralığı oluşturmaz.
- Geçersiz/eksik olay mesajı normal SCT/PZEM ölçüm kaydı gibi yorumlanmaz.
- ON–OFF aralığı otomatik olarak kararlı kabul edilmez. Kararlılık algoritmaları, toleranslar ve minimum süre gerçek HA verisi üzerinde Python tarafında geliştirilecektir.

## ADR-019 ile ilişki

Bu karar, ADR-019'un bağımsız ölçüm akışları ve ayrı olay işaretleri ilkesini korur. ADR-022, paket/olay kimliğinin nasıl doğrulanacağını netleştirir: iki akışın ON başlangıç işaretleri `BOOT_ID + EVENT_ID` ile eşleştirilir; OFF kapanışları her akışta ayrıca doğrulanır. Timestamp örtüşmesi paket kimliği veya paket eşleştirme anahtarı değildir. Bununla birlikte, aynı ve bütünlüğü doğrulanmış ON paketi içindeki bağımsız SCT/PZEM kararlı aralıklarının zaman kesişimi, eğitim etiketi üretmeye uygunluğun zorunlu koşuludur. Kesişim yoksa etiket üretilmez. ADR-019 tarihsel kayıt olarak korunur; paket kimliği ile eğitim adayı uygunluğunu ayıran bu açıklama ADR-022'de geçerlidir.

## Uygulama durumu ve kanıt sınırı

Bu ADR mimari karardır. Modül 2/Modül 3 YAML değişikliği, derleme, OTA, UDP alım testi, HA Recorder sıralama testi veya fiziksel doğrulama bu kayıtla yapılmış sayılmaz. Firmware değişiklikleri ayrı adımda uygulanıp gerçek logla doğrulanacaktır.
