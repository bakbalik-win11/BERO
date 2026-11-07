# BERO — Mimari

Bu klasör, BERO'nun tek bir sensör veya deneyden bağımsız, tekrar kullanılabilir mimari ilkelerini tutar.

## Ana mimari

- [Pencereli sensör analizi ve davranış çıkarımı](PENCERELI-SENSOR-ANALIZI/README.md) — veri toplama, özellik çıkarma ve davranış çıkarımı katmanları; veri sözleşmesi, pencere türleri, sensör adaptörleri ve uygulama kuralları.

## Mimari ile uygulama arasındaki sınır

- **MIMARI/**: Sensörlerden bağımsız ilkeler, ortak veri akışı, arayüzler ve tasarım kararları.
- **PROJELER/**: Bu ilkelerin belirli donanım ve kullanım senaryolarında uygulandığı projeler.
- **DONANIM/** ve **ENVANTER/**: Fiziksel donanım ve stok kayıtları.

Mimari belgelerde bir sensöre ait pin, katsayı veya özel algoritma evrensel kural olarak tanımlanmaz. Uygulama kanıtları kendi proje klasörlerinde tutulur; mimari belge bunlara bağlantı verir.

## İlk uygulama

[SCT013 + PZEM akım gözlem sistemi](../PROJELER/SCT013-PZEM-AKIM-GOZLEM/README.md), pencereli sensör analizinin ilk somut uygulamasıdır. Buradaki deneyler mimariyi besler; ancak SCT'ye özgü sonuçlar diğer sensörlere doğrudan genellenmez.

## Durum

Bu klasör mimari tasarım ve yönlendirme kaydıdır. Burada tanımlanan genel davranış sınıflandırma sistemi henüz tamamlanmış/çalışan bir ürün değildir. Her uygulama, kod, derleme ve gerçek donanım kanıtıyla ayrı doğrulanır.


## BERO'nun kapsamı: çoklu sensörlü ev gözlem sistemi

BERO tek bir akım ölçer veya yalnızca SCT013 projesi değildir. Hedef, farklı fiziksel değişkenleri ölçen sensörlerin ortak bir gözlem ve davranış çıkarımı çatısı altında bir araya gelmesidir. Akım ölçümü bu sensörlerden yalnızca biridir; AC akımın yanında uygun sensör ve ölçüm ön ucuyla DC akımın izlenmesi de olası kullanım alanıdır.

Kullanıcının belirttiği mevcut/planlanan sensör örnekleri:
- Su kuyusunda sıcaklık değişimini izleyen sensör.
- Kuyudaki basınçtan su seviyesini/su derinliğini çıkaran basınç sensörü.
- Evin girişinde şehir şebekesi su basıncını ölçen sensör.
- Elektriksel yüklerin AC akımını izleyen SCT tabanlı ölçüm; uygun donanımla DC akım ölçümü de.

Bu sensörler aynı fiziksel büyüklüğü ölçmez ve aynı algoritmayı kullanmaz. Her sensör kendi birimi, kalibrasyonu, örnekleme aralığı, geçerlilik kontrolü ve özellik çıkarma yöntemiyle ele alınır. Ortak BERO mimarisi, bu farklı ölçümleri zaman ve kaynak kimliği korunarak bir araya getirip daha üst düzey davranışlar hakkında çıkarım yapmayı hedefler.

## Geliştirme ortamı ile canlı kurulumun ayrımı

Şu anki SCT013-PZEM çalışması, kullanıcının diğer evde yürüttüğü hazırlık/geliştirme çalışmasıdır. Bu ortamda ölçüm zinciri, veri toplama, arşivleme ve analiz yöntemleri hazırlanıp doğrulanmaktadır. Kullanıcı açıkça belirtmiştir: şu anda canlı BERO kurulumunda çoklu sensörlerle birlikte çalışan bir uygulama yürütülmemektedir.

Dolayısıyla yukarıdaki çoklu sensör örnekleri BERO'nun sistem kapsamını ve hedeflenen sensör ailesini açıklar; mevcut canlı sistemde bu sensörlerin entegre olduğu veya ortak algoritmayla çalıştığı anlamına gelmez. Sensör entegrasyonları aşamalı ve ayrı ayrı doğrulanacaktır.


## Havalandırma ve iç ortam gözlemi — çoklu sensör örneği

Kullanıcının belirttiği önemli kullanım alanlarından biri binanın iç ortam hava kalitesi ve havalandırma sistemidir. Bu alan yalnızca CO₂ ölçümünden ibaret değildir; temiz hava besleme ve egzoz kanalları, fan/motor davranışı, gürültü ve titreşim birlikte gözlemlenebilir.

Olası ölçüm katmanları:
- **CO₂:** İç ortam hava kalitesinin ve havalandırma ihtiyacının göstergelerinden biri.
- **Akım:** Fan/motorun devrede olma durumu, yük çekişi, çalışma süresi ve zaman içindeki elektriksel davranış değişimi.
- **Gürültü:** Havalandırma sisteminin ses seviyesindeki ve ses karakterindeki değişimler.
- **Titreşim:** Fan, motor, yataklama ve bağlantıların mekanik davranışındaki değişimler.
- **Hava akışı/debi ve basınç:** Temiz hava beslemesi ile egzozun gerçekten ne kadar hava taşıdığını değerlendirmek için ayrı ölçüm katmanı.

Akım sensörünün BERO'daki rolü bu örnekte özellikle önemlidir: Akım ölçümü yalnızca bir cihazın elektrik tüketimini okumak için değil, evdeki farklı motorlu/elektrikli ekipmanların çalışma karakterini izlemek ve diğer sensörlerin gözlemleriyle ilişkilendirmek için tekrar kullanılabilir bir parametredir. Bu nedenle SCT/akım ölçümü, çoklu sensörlü sistemde farklı kullanım alanlarına taşınabilecek ortak bir gözlem girdisi olarak ele alınır.

Sensörler birbirinin yerine geçmez. Örneğin fan akımı motorun elektriksel olarak çalıştığına dair kanıt sağlayabilir; fakat tek başına yeterli hava debisi veya doğru temiz hava beslemesini kanıtlamaz. CO₂, akım, gürültü, titreşim ve gerekiyorsa debi/basınç verileri zaman ilişkileriyle birlikte değerlendirilmelidir. Birden fazla sensörün aynı anda gözlem yapması, tek bir ölçümden çıkarılamayacak davranış değişimlerini araştırma imkânı sağlar.

Bu havalandırma senaryosu BERO'nun hedeflenen kullanım alanlarından biridir; mevcut canlı BERO kurulumunda entegre ve çalışan bir havalandırma uygulaması olduğu anlamına gelmez. Mevcut SCT013-PZEM çalışması diğer evdeki hazırlık/geliştirme çalışması olarak kalır; bu vizyon kısa vadeli SCT veri toplama görevlerini değiştirmez.


## Kalıcı haberleşme omurgası

BERO'nun kalıcı haberleşme omurgası **RS485** olarak kararlaştırılmıştır. ESP tabanlı ölçüm düğümleri verilerini RS485 üzerinden bölgesel düğümlere aktaracak şekilde geliştirilecektir. Wi-Fi şimdilik geçici haberleşme/aktarım yoludur; kalıcı omurga değildir.

RS485 fiziksel haberleşme katmanıdır. PZEM-014 ile RS485 üzerinden kullanılacak Modbus RTU, BERO bölgesel düğümleri arasındaki uygulama mesajlaşma protokolüyle aynı karar değildir. Düğümler arası mesaj çerçevesi, adresleme, bus erişimi, baud hızı, topoloji ve elektriksel ayrıntılar henüz belirlenmemiştir. PZEM-014 henüz kullanılmamış; ekranlı ESP'ler de henüz devreye alınmamıştır.

Karar kaydı: [ADR-001 — BERO kalıcı haberleşme omurgası olarak RS485](DECISIONS/ADR-001-rs485-communication-backbone.md).


### RS485 omurga kablolama yaklaşımı

Kullanıcı kararı: RS485 A/B hattı CAT kablo üzerinden taşınacak; aynı kablo ile transformatör kaynaklı besleme gerilimi de bölgesel düğüme götürülecek ve düğüm noktasında 5 V'a düşürülecek. Bu özel BERO kablosu, mevcut Ethernet kablosundan dış kılıf rengiyle ayırt edilecek. CAT kablonun kesin kategorisi/damar tahsisi, transformatör çıkış gerilimi, akım ve mesafeye göre gerilim düşümü, yerel dönüştürücü ve koruma tasarımı henüz belirlenmedi. Bu kablo Ethernet/LAN portlarına takılmayacak; fiziksel renk ayrımı yanında uçlar da açıkça etiketlenmeli.

Ayrıntı: [ADR-001 — RS485 omurgası ve kablolama kararı](DECISIONS/ADR-001-rs485-communication-backbone.md).
