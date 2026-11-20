# PREBERO

## Amaç

PREBERO, BERO sistemine geçmeden önce modülleri hazırlamak, ölçüm ve gözlem yöntemlerini geliştirmek ve hedefleri doğrulamak için yürütülen çalışma alanıdır.

PREBERO bir modül ve görev yapısıdır. Her modülün hedefi, görevleri ve çalışma çıktıları kendi klasöründe tutulur.

## Çalışma ilkeleri

- Modül hedefleri birbirinden bağımsız ve açıktır.
- Her modülün altında görevler bulunur.
- Her modülün kökünde, o modülde edinilen tecrübeyi ve gelişim sürecini izleyen bir `TARIHCE.md` bulunur.
- Her görev kendi kodunu, verisini, loglarını, analizini ve raporunu barındırır.
- Görev tamamlandıkça aynı modülde sonraki görev açılır.
- Ortak donanım bilgileri ve envanter PREBERO içinde kopyalanmaz; ana dizindeki DONANIM ve ENVANTER kullanılır.
- Bu başlangıç yapısı yalnızca PREBERO'nun yeniden tanımlandığı bu sohbet kararlarına dayanır.

## Modüller

1. Modül 1 – Şebeke Karakterini Koruyan Bias
2. Modül 2 – Masaüstü 4 Kanal / Akım Testleri
3. Modül 3 – Çamaşır Makinesi
4. Modül 4 – Bulaşık Makinesi
5. Modül 5 – Ana Pano

## Kimlik ve adlandırma standardı

### Modül ve görev kimliği

Her görev, depo genelinde benzersiz olacak şekilde modül numarası ve görev sıra numarasıyla tanımlanır.

Standart biçim:

`MOD2-GRV001`

- `MOD2`: Modül numarası.
- `GRV`: Görev.
- `001`: İlgili modül içindeki görev sıra numarası.
- Her modül görev numarasına `001` ile başlar.
- Görev kimliği görev boyunca sabit kalır; görev veya kod geliştikçe değiştirilmez.
- Başka görevlerde, raporlarda, kodlarda ve kayıtlarda atıf yapılırken tam görev kimliği kullanılır.

### Kod test durumu

Kod sürümü ile test durumu birbirinden bağımsız alanlardır. Her kod dosyasının başlığında ikisi ayrı ayrı yazılır:

```yaml
# KOD SÜRÜMÜ  : V1.0
# TEST DURUMU : GELİŞTİRME
```

Test durumu aşağıdaki sırayla ilerler:

1. `GELİŞTİRME`: Henüz gerçek donanımda test edilmedi.
2. `TEST EDİLDİ`: Gerçek donanımda çalıştırılarak denendi; bu ifade tek başına başarılı olduğu anlamına gelmez.
3. `DOĞRULANDI`: Tanımlanan test koşullarında beklenen sonuç alındı ve sonuç kayıt altına alındı.
4. `KARARLI`: Doğrulanmış sürüm, belirtilen kullanım amacı için kullanıma hazır kabul edildi.

Test durumu yalnızca ilgili aşamanın kanıtı elde edildiğinde değiştirilir. Her durum değişikliğinde test koşulu, gerçek log ve sonuç yorumu ilgili görevin `LOG/` ve `RAPOR/` klasörlerinde saklanır. Kod sürümü, test durumu değişti diye otomatik olarak artırılmaz; kodda değişiklik yapıldığında sürümleme kuralına göre ayrıca artırılır.

### Kod sürümleme

Görev kimliği ile kod sürümü birbirinden bağımsızdır. Kod sürümü, kodun her yeni revizyonunu tanımlar.

**Her türlü kod değişikliği yeni bir sürüm dosyası oluşturur.** Değişikliğin küçük veya büyük olması, iyileştirme ya da hata düzeltmesi olması, yeni özellik eklemesi, donanım/pin bağlantısı değiştirmesi veya kodun tamamen farklı bir mimariye taşınması bu kuralı değiştirmez.

- İlk kod dosyası `V1.0` olarak başlatılır.
- Aynı teknik yaklaşım ve geliştirme çizgisinde yapılan her kod değişikliğinde ana sürüm sabit kalır, sıra numarası artırılır. Örnek: `V1.0` → `V1.1` → `V1.2` → `V1.123`. Sıra numarası için üst sınır yoktur.
- Yeni bir teknik yaklaşım veya farklı bir mimariye geçildiğinde ana sürüm artırılır ve sıra numarası sıfırlanır. Örnek: `V1.123` → `V2.0`.
- Bir testin başarısız olması tek başına ana sürümü artırmaz. Aynı teknik yaklaşımda düzeltme ve denemelere devam ediliyorsa mevcut ana sürümün sıra numarası artırılır. Başarısızlık sonrasında farklı bir teknik yola veya mimariye geçilirse yeni ana sürüm açılır.
- Ana sürüm değişikliğinin gerekçesi, neden önceki teknik yaklaşımın bırakıldığıyla birlikte ilgili görev kayıtlarında açıklanır.
- Her yeni sürüm ayrı dosya olarak kaydedilir; önceki sürümün içeriği değiştirilmez, üzerine yazılmaz veya silinmez.
- Sürüm numarası değişikliğin kapsamını veya önemini değil, kod revizyonunun sırasını ve teknik yaklaşım çizgisini gösterir.
- Kod değişikliği yapılmadan yalnızca test durumu güncelleniyorsa yeni kod sürümü oluşturulmaz.
- Her sürümün kendi test durumu, logları ve raporları bulunur. Yeni sürüm önceki sürümün test sonucunu devralmaz.
- Sürüm artışının nedeni ilgili sürümün görev kayıtlarında belirtilir.

Örnek: Tek satırlık hata düzeltmesi de yeni sürümdür; kapsamlı bir kod mimarisi değişikliği de yeni sürümdür. Her ikisi de bir sonraki sürüm numarasını alır.

### Kod içinde kimlik bilgisi

Her kod dosyasının başında en az şu bilgiler bulunur:

- Proje: `PREBERO`
- Modül: ilgili modül numarası
- Görev: tam görev kimliği
- Kod sürümü: sürüm numarası
- Amaç: kodun yaptığı iş
- Donanım bağlantıları ve beklenen davranış

ESP üzerinde çalışan kodda bu bilgiler kaynak kod başlığında bulunur. Uygun olduğunda açılış loguna da modül, görev ve sürüm bilgisi yazdırılır. Böylece kod dosyasına veya ESP loguna bakıldığında hangi modülün hangi görev sürümünün çalıştığı anlaşılır.

### Sürümlü görev çıktı düzeni

Her görev klasöründe YAML, LOG ve RAPOR çıktıları kod sürümüne göre tekrarlanan sürüm klasörlerinde tutulur. Her sürüm kendi kodunu ve yalnızca o sürüme ait test kanıtlarını birlikte barındırır.

Örnek görev yapısı:

```text
MOD2-GRV001/
├── GOREV.md
├── VERI/
├── V1.0/
│   ├── MOD2-GRV001_V1.0.yaml
│   ├── LOG/
│   └── RAPOR/
├── V1.1/
│   ├── MOD2-GRV001_V1.1.yaml
│   ├── LOG/
│   └── RAPOR/
└── V2.0/
    ├── MOD2-GRV001_V2.0.yaml
    ├── LOG/
    └── RAPOR/
```

- Sürüm klasörü doğrudan görev klasörünün altında açılır: `V1.0/`, `V1.1/`, `V2.0/` gibi.
- YAML dosyası sürüm klasöründe ve `MOD2-GRV001_V1.0.yaml` biçiminde adlandırılır.
- Her sürüm klasörünün kendi `LOG/` ve `RAPOR/` alt klasörleri bulunur.
- Log ve rapor dosyaları görev kimliği ve kod sürümüyle adlandırılır. Gerekirse dosya adına tarih ve test sıra numarası eklenir.
- `VERI/` görev klasöründe ortak veri alanı olarak kalır; sürümle ilişkili test logları ve sonuç raporları ise ilgili sürüm klasöründedir.
- Bir kod sürümünün test durumu yalnızca o sürümün gerçek test kanıtına göre güncellenir. Yeni sürüm önceki sürümün loglarını veya raporlarını devralmaz.
- Başarısız, eksik veya başarılı testlerin tüm kayıtları ilgili sürümün altında korunur. Yeni yama yeni sürüm klasöründe açılır; önceki sürüm aynen kalır.
- Kod değişmeden yalnızca test durumu güncellenirse yeni sürüm klasörü açılmaz; mevcut sürümün ilgili kayıtları tamamlanır.

## Dokümantasyon ayrımı

- `README.md` kalıcı ilkeleri ve standartları anlatır: proje yapısı, modül/görev kimlikleri, kod sürümleme, ESP kimliği, YAML teslimi ve dosyalama kuralları. Güncel iş akışını veya ilerleme durumunu takip etmez.
- `DURUM.md` projenin güncel akışını gösteren tek takip dosyasıdır: hangi modülde ve görevde olduğumuz, mevcut çalışma aşaması, ilerleme, bekleyen işler ve sıradaki adım burada tutulur.
- Her modülün kökündeki `TARIHCE.md`, o modülde görevler boyunca edinilen tecrübeyi, önemli denemeleri, sonuçları ve teknik kararların gerekçelerini kronolojik olarak kaydeder. **Test loglarının veya raporların kopyası değildir.** Log ve raporların ne gösterdiğini, bunlardan ne öğrendiğimizi ve hangi teknik sonuca/karara ulaştığımızı özetler; ayrıntılı kanıtın bulunduğu görev ve sürüm kayıtlarına referans verir.
#### Oturum açılış sırası

Çalışmaya her yeniden başlandığında sıra değişmez:

1. `DURUM.md` okunur; aktif modül ve en son üzerinde çalışılan görev buradan belirlenir.
2. Belirlenen modülün `TARIHCE.md` dosyası okunur; o modülde daha önce edinilen tecrübe ve teknik kararlar hatırlanır.
3. `DURUM.md` içinde belirtilen son görev klasörüne girilir; `GOREV.md`, son kod sürümü ve ilgili LOG/RAPOR kayıtları incelenir.
4. Çalışmaya bu bağlam üzerinden devam edilir. Başka modüllerin dosyaları gereksiz yere açılmaz.

#### Oturum kapatış sırası

Bir görevden çıkarken, başka modüle geçerken veya çalışma oturumunu bitirirken:

1. Önce ilgili modülün `TARIHCE.md` dosyasına o oturumda edinilen tecrübe aktarılır.
2. Tarihçe, log ve raporların kopyası olarak değil; ne yapıldığını, ne gözlendiğini, ne öğrenildiğini ve hangi kararın alındığını özetleyecek şekilde yazılır. Ayrıntılı kanıtlara görev/sürüm yollarıyla referans verilir.
3. Ardından `DURUM.md` güncellenir: aktif modül, son çalışılan görev, mevcut aşama, bekleyen işler ve bir sonraki somut adım açıkça belirtilir.
4. Böylece başka bir modüle geçilse veya aynı göreve aylar sonra dönülse bile çalışma kaldığı yerden sürdürülebilir.

Tarihçe ve durum güncellemesi yapılmadan oturum kapatılmış veya başka göreve geçilmiş sayılmaz.

Tarihçe kaydında tarih, görev kimliği, yapılan çalışma/deneme, gözlenen sonuç, edinilen tecrübe ve alınan karar bulunur. İlgili YAML sürümü, LOG ve RAPOR yolları eklenir. Sonuç doğrulanmadıysa doğrulanmış gibi yazılmaz.
- Ana dizindeki `DONANIM/` ve `ENVANTER/` ortak donanım ve envanter bilgilerinin tek kaynağıdır. Bu bilgiler PREBERO altında kopyalanmaz.

### Fiziksel ESP kimliği ve görev kimliği ayrımı

- Her fiziksel ESP cihazı, ortak `ENVANTER/` içinde kendisine ait kalıcı ve benzersiz envanter kimliğiyle izlenir. Kimlik cihaza aittir; modül, görev veya kod sürümü değişince değişmez.
- ESP cihaz adı (ESPHome node adı / Home Assistant cihaz kimliği) fiziksel cihazın sabit adıdır. Kod sürümü veya görev değiştiğinde kendiliğinden değiştirilmez.
- Modül ve görev kimliği yazılımın hangi çalışmaya ait olduğunu belirtir; fiziksel ESP kimliğinin yerine geçmez.
- Bir ESP başka modülde veya görevde yeniden kullanılırsa fiziksel kimliği aynı kalır; yalnızca o sürümün görev bilgisi değişir.
- Görev dosyasında kullanılan fiziksel ESP envanter kimliği ve ESPHome cihaz adı açıkça belirtilir. Cihaz henüz seçilmediyse kimlik uydurulmaz; atama yapılana kadar bu durum belirtilir.
- ESP kaynak kodu/YAML başlığında en az fiziksel ESP envanter kimliği, sabit ESPHome cihaz adı, modül, görev, kod sürümü ve test durumu bulunur. Açılış logunda da mümkün olduğunda bu kimlikler gösterilir.

### ESP cihaz adı ve YAML teslim standardı

- Her modülde kullanılan ESP cihazına verilen ad/kimlik sabittir. Kod sürümü veya YAML güncellendiğinde ESP cihaz adı değiştirilmez.
- ESP cihaz adı, ilgili modülün donanım ve ağ kimliğiyle tutarlı tutulur. Zorunlu bir değişiklik gerekirse önce gerekçesi açıklanır ve kayıt altına alınır; kendiliğinden yeniden adlandırma yapılmaz.
- Home Assistant / ESPHome için YAML istendiğinde yalnızca değişen bölüm değil, yapılandırmanın tamamı verilir.
- Verilen YAML eksiksiz, doğrudan kopyalanıp kullanılabilir tek bir kod bloğu içinde sunulur. Kullanıcı özellikle istemedikçe parçalı YAML veya "... mevcut ayarları koruyun" gibi eksik bırakılmış bölümler verilmez.
- Her YAML'ın başında amacı, ilgili modül ve görev kimliği, kod sürümü, donanım bağlantıları ve beklenen çalışma davranışı açıklanır.
- YAML verilmeden önce mevcut yapı ve bağlantılarla çelişki olup olmadığı kontrol edilir. Bilinmeyen bağlantı veya değerler varsayılmaz; gerekiyorsa kullanıcıdan netleştirilir.


### Kendi kendini açıklayan kod / YAML başlığı

Her ESPHome YAML veya başka bir gömülü yazılım dosyası, yalnızca kodu yazan kişinin değil; dosyayı daha sonra inceleyen başka bir mühendis veya yapay zekâ aracının da çalışmayı anlayabileceği teknik açıklamayı kendi içinde taşımalıdır. Kod dosyası, ilgili yazılım sürümünün teknik kimlik kartıdır.

Başlık, kullanılan teknolojiye göre aşağıdaki bilgileri içermelidir:

- Proje, modül ve tam görev kimliği.
- Fiziksel ESP envanter kimliği ve sabit ESPHome cihaz adı.
- Kod sürümü ve o sürüme ait test durumu.
- Modülün/kodun amacı ve ölçtüğü veya kontrol ettiği iş.
- Donanım modeli ve gerçek bağlantılar: GPIO, I²C/SPI/UART, sensör uçları, besleme ve ortak GND gibi bağlantılar.
- Ölçüm ve çalışma parametreleri: örnekleme, kazanç, pencere süresi, güncelleme aralığı, eşikler, katsayılar ve filtreler.
- Kalibrasyon/katsayı notları: hesap yöntemi, kullanılan gözlem ve doğrulama sınırı.
- Haberleşme protokolleri: mesaj biçimi, port, kaynak/hedef, zaman aşımı ve ilgili davranışlar.
- Home Assistant entity'leri veya dışarıya sunulan arayüzler.
- Beklenen çalışma davranışı; maddeler halinde ve gözlenebilir şekilde.
- Güvenlik uyarıları ve donanımın güvenli kullanım sınırları.
- Bilinen sorunlar, sınırlamalar ve henüz doğrulanmamış noktalar.

Her bilgi kendi kanıt seviyesine uygun ifade edilir: doğrulanmış, ölçülmüş/gözlenmiş, üretici dokümanından alınmış, kullanıcı bildirimi veya henüz denenmemiş varsayım. Tek ölçümden türetilen katsayı kesin kalibrasyon gibi sunulmaz. Bilinmeyen pin, bağlantı veya parametre uydurulmaz.

Kod değiştiğinde yeni sürüm dosyasının başlığı da o sürümün gerçek içeriğine göre güncellenir. Eski sürümün başlığı ve dosyası geriye dönük değiştirilmez. Test durumu yalnızca gerçek derleme, yükleme ve donanım test kanıtına göre yazılır. Hazırlandı, derlendi, cihaza yüklendi ve fiziksel olarak doğrulandı ifadeleri birbirinin yerine kullanılmaz.

Bu açıklama, kodu tek başına inceleyen bir kişinin temel amacı, donanım bağlantılarını, çalışma parametrelerini, beklenen davranışı ve test sınırlarını anlayabilmesini sağlamalıdır. Ancak fiziksel modülün tüm imalat ayrıntıları kod başlığına bırakılmaz; modülün `IMALAT/` dosyası esas alınır.



**Genel bias orta nokta standardı:** Bias orta noktası, uygun bir DC kaynağın iki eşit değerli dirençle seri bölünmesi ve iki direncin birleşim noktasından alınır. Orta nokta gerilimi, ideal ve yüksüz durumda kaynak geriliminin yaklaşık yarısıdır. Örneğin 3,3 V kaynak ve iki adet 10 kΩ direnç kullanıldığında orta nokta yaklaşık 1,65 V olur. Bu yapı belirli bir trafoya özgü değildir; uygun DC kaynakla uygulanabilen genel bir gerilim bölücü yaklaşımıdır. Ancak kaynak gerilimi değişirse orta nokta da değişir; 1,65 V her kaynakta sabit kalmaz. Kaynağın uygunluğu, yük etkisi, direnç güç/tolerans değerleri ve kondansatör bağlantıları uygulama bazında değerlendirilir.

Bir modülde kullanılacak bias devresinin direnç ve kondansatör bileşenleri, gerçek devre ve ölçümle belirlendikten sonra değerleri, toleransları ve bağlantı biçimleriyle tarif edilir. Böylece “bias şu dirençlerden ve şu kondansatörden oluşur” şeklinde yeniden kurulabilir bir standart oluşturulur. 1,65 V seviyesinin elde edilmesi, genel orta nokta yapısının belirli bir kaynakla uygulanmasıdır; kaynak ve uygulama ayrıntıları ilgili modülün imalat dosyasında ayrıca belgelenir. Doğrulanmamış değerler standart olarak yayımlanmaz.

### Modül imalat dosyası

Her modülün kökünde, görevlerden ve kod sürümlerinden bağımsız bir `IMALAT/` klasörü ve bunun içinde `IMALAT.md` bulunur. Bu dosya, modül fiziksel olarak sökülse bile aynı donanımın yeniden imal edilmesini ve kurulmasını sağlayacak ana teknik kayıttır.

Önerilen düzen:

```text
MODUL-X-.../
├── IMALAT/
│   ├── IMALAT.md
│   ├── SEMALAR/
│   ├── FOTOGRAFLAR/
│   └── EKLER/
├── TARIHCE.md
└── ... görev klasörleri ...
```

İmalat dosyası ve ekleri gerektiğinde şu bilgileri kapsar:

- Modülün fiziksel amacı, kapsamı ve genel çalışma düzeni.
- Gerçekleşmiş fiziksel yerleşim, montaj ve kutulama.
- Elektrik/elektronik bağlantı şemaları ve bağlantı noktaları.
- Kablo listesi: renk, kesit/tip biliniyorsa, başlangıç ve bitiş noktası.
- Malzeme/komponent listesi: gerçek model ve kullanılan adet.
- Besleme gereksinimleri, gerilimler, ortak referans ve izolasyon bilgileri.
- Kullanılan ESP'nin envanter kimliği ve sabit cihaz adı.
- Montaj, sökme ve yeniden kurulum adımları.
- Gerçek montaj fotoğrafları ve şema dosyalarına referanslar.
- Güvenlik uyarıları, bilinen fiziksel sınırlamalar ve kontrol listesi.

İmalat dosyası modülün fiziksel yapısını bütün olarak anlatır. YAML başlığı ise belirli bir yazılım sürümünün kullandığı pinleri, bağlantıları ve parametreleri açıklar. İkisi birbirinin yerine geçmez; aralarında çelişki varsa çelişki giderilmeden modül yeniden kurulmuş veya doğrulanmış sayılmaz.

**Doğruluk kuralı:** Yalnızca gerçekten kurulmuş, gözlenmiş veya ölçülmüş bilgiler gerçekleşmiş imalat bilgisi olarak yazılır. Taslak, öneri ve henüz denenmemiş bağlantılar açıkça bu şekilde etiketlenir. Bilinmeyen alanlar boş/atanmadı/ doğrulanmadı olarak bırakılır; tahminle doldurulmaz. İmalat değişiklikleri tarihçeye ve ilgili görevin kayıtlarına bağlanır.

### Kod, imalat ve tarihçe birlikte nasıl kullanılır?

- `IMALAT/IMALAT.md`: Modül fiziksel olarak nasıl yapılır, bağlanır, sökülür ve yeniden kurulur?
- YAML/kod başlığı: Bu belirli yazılım sürümü hangi donanımı ve bağlantıları kullanır, nasıl çalışır?
- Görev ve sürüm klasörleri: Bu sürümle hangi geliştirme ve testler yapıldı; gerçek kanıt ve sonuç nedir?
- `TARIHCE.md`: Süreçte ne öğrenildi, hangi teknik kararlar neden alındı?

Amaç, modül fiziksel olarak sökülse veya başka bir ESP'ye taşınsa bile imalat bilgisi, teknik tecrübe, test kanıtı ve son kod sürümü üzerinden yeniden üretilebilir olmasıdır. ESP değişirse fiziksel ESP kimliği ve cihaz adı yeni donanıma göre envanterden atanır; görev ve yazılım sürümü bilgileri ayrı tutulur.
