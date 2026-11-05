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
4. Her iki modülde ON başlangıcı ve karşılık gelen OFF kapanışı aynı kimlik/sıra düzeniyle doğrulanmışsa paket bütünlüğünü kabul eder; eksik veya uyumsuz işaretli aralıkları eğitim dışı bırakır ve nedenini raporlar.
5. Her ON paketinde PZEM kararlılığını yalnız PZEM değerlerinden; SCT kararlılığını yalnız SCT değerlerinden bağımsız tespit eder.
6. PZEM'in yükseliş/düşüş ve yerleşme geçişlerini; SCT'nin kendi geçiş/yerleşme bölümlerini eğitim kararlı alanından çıkarır.
7. Aynı ON paketindeki bağımsız SCT ve PZEM kararlı aralıklarının zaman kesişimini hesaplar. Yalnız kesişen zaman aralığı karşılaştırılabilir eğitim adayıdır. Kesişim yoksa etiket üretilmez; ham kayıt korunur ve `NO_STABLE_OVERLAP` gibi açık bir dışlama nedeni raporlanır.
8. PZEM değeri bu örneğin proje referans etiketidir; mutlak ground truth değildir.
9. Eğitim çıktısına paket kimliği olan ON başlangıcının `BOOT_ID` ve `EVENT_ID` bilgilerini Python ekler. Ham ölçüm kayıtlarının içine ESP tarafından sürekli olay kimliği yazılmaz.

**Paket eşleştirme anahtarı `BOOT_ID + ON_EVENT_ID` birleşimidir; zaman değildir.** Bu kimlik, iki modüldeki aynı fiziksel ON başlangıç işaretini ve dolayısıyla paket başlangıcını tanımlar. Karşılık gelen OFF kapanış işareti her akışta ayrıca doğrulanır; OFF işaretinin EVENT_ID değeri ON ile aynı değildir. Paket bütünlüğü doğrulandıktan sonra zaman damgaları, aynı ON paketi içindeki SCT ve PZEM kararlı aralıklarının zaman bakımından kesişip kesişmediğini belirlemek için kullanılır. Bu kesişim paket eşleştirme anahtarı değil, eğitim etiketi üretmeye uygunluk koşuludur. Tekil SCT/PZEM örnekleri timestamp üzerinden birebir eşleştirilmez, interpolasyonla eşleştirilmez ve sabit gecikme varsayılmaz. HA timestamp'lerinin iki akış arasında karşılaştırılabilirliği, olay sırası ve kararlı aralık sınırları gerçek dışa aktarım üzerinde doğrulanmadan zaman hassasiyeti hakkında ek iddia kurulmaz.

## BOOT_ID, EVENT_ID ve TIME alanlarının kesin görevi

- **BOOT_ID:** Modül 3'ün her açılışında/yeniden başlatılmasında bir kez yeni kimlik üretilir. Aynı açılış oturumu boyunca bütün SSR olaylarında sabit kalır. Her ON/OFF olayında yeniden üretilmez.
- **EVENT_ID:** Modül 3'te her yeni SSR durum değişiminde artan olay/paket numarasıdır. Aynı BOOT_ID oturumunda sıralı ilerler. Yeniden başlatma sonrası sayaç yeniden başlayabilir; bu nedenle tek başına benzersiz değildir.
- **TIME:** Olayın üretildiği tarih-saat bilgisidir. Her BERO_EVT olay mesajında bulunur ve Modül 2'ye aynı içerikle aktarılır. Oturumun tarih/saat izini ve olayın kendi akışı içindeki yerini korumaya, yeniden başlatma ve tanılama kayıtlarına yarar. TIME, Modül 2 SCT ile Modül 3 PZEM örneklerini zaman üzerinden eşleştirmek için kullanılmaz.
- **Tekil eşleştirme anahtarı:** BOOT_ID + EVENT_ID birleşimidir. TIME bu anahtarın yerine geçmez; EVENT_ID'nin farklı açılışlarda tekrar edebilmesini ayırt etmeye yardımcı olan BOOT_ID'dir.
- **Modül 2**, Modül 3'ten aldığı BOOT_ID, EVENT_ID, STATE ve TIME alanlarını aynen korur. Modül 2 kendi BOOT_ID'sini bu olay eşleştirmesinde kullanmaz.

Örnek olay biçimi:

`BERO_EVT,BOOT_ID=XXXXXXXX,EVENT_ID=N,STATE=ON|OFF,TIME=YYYY-MM-DD HH:MM:SS`

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
