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

1. Modül 1 – Bias Trafosu
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
- Yeni bir oturumda sırasıyla: (1) bu README okunur, (2) `DURUM.md` üzerinden aktif modül ve görev belirlenir, (3) aktif görevin bulunduğu modülün `TARIHCE.md` dosyası okunur, (4) aktif görev klasörü ve ilgili sürüm kayıtları incelenir.
- Bir görevdeki çalışma tamamlanıp görev/çalışma oturumu kapatılırken önce ilgili modülün `TARIHCE.md` dosyası güncellenir. Ardından gerekiyorsa görev kayıtları ve en son `DURUM.md` güncellenir. Tarihçe güncellemesi yapılmadan çalışma tamamlanmış kabul edilmez.
- Tarihçe kaydında tarih, görev kimliği, yapılan çalışma/deneme, gözlenen sonuç, edinilen tecrübe ve alınan karar bulunur. İlgili YAML sürümü, LOG ve RAPOR yolları eklenir. Sonuç doğrulanmadıysa doğrulanmış gibi yazılmaz.
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
