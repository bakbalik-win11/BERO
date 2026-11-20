# PREBERO

## Amaç

PREBERO, BERO sistemine geçmeden önce modülleri hazırlamak, ölçüm ve gözlem yöntemlerini geliştirmek ve hedefleri doğrulamak için yürütülen çalışma alanıdır.

PREBERO bir modül ve görev yapısıdır. Her modülün hedefi, görevleri ve çalışma çıktıları kendi klasöründe tutulur.

## Çalışma ilkeleri

- Modül hedefleri birbirinden bağımsız ve açıktır.
- Her modülün altında görevler bulunur.
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
- Kodda yapılan her yeni değişiklikte sürüm numarası artırılır. Örneğin `V1.0` → `V1.1` → `V1.2`.
- Her yeni sürüm ayrı dosya olarak kaydedilir; önceki sürümün içeriği değiştirilmez, üzerine yazılmaz veya silinmez.
- Sürüm numarası değişikliğin kapsamını veya önemini değil, kod revizyonunun sırasını gösterir.
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

### Sürümlü dosya, log ve rapor düzeni

- Her kod değişikliği yeni bir sürüm dosyası oluşturur. Eski sürüm dosyaları değiştirilmez, üzerine yazılmaz ve silinmez.
- Kod dosyası adı: `MOD2-GRV001_V1.0.yaml` biçimindedir.
- Her sürümün logları ve raporları aynı görev klasöründe, o sürümün kimliğiyle ayrılmış alt klasörlerde tutulur:
  - `KOD/MOD2-GRV001_V1.0.yaml`
  - `LOG/MOD2-GRV001_V1.0/`
  - `RAPOR/MOD2-GRV001_V1.0/`
- Log ve rapor dosyaları da ait oldukları görev kimliği ve kod sürümüyle adlandırılır. Gerekirse dosya adına tarih ve test sıra numarası eklenir.
- Bir kod sürümünün test durumu yalnızca o sürümün gerçek test kanıtına göre güncellenir. Yeni sürüm önceki sürümün loglarını veya raporlarını devralmış sayılmaz.
- Başarısız, eksik veya başarılı testlerin tüm kayıtları ilgili sürümün altında korunur. Yeni yama yeni sürüm olarak açılır; önceki sürüm aynen kalır.

## Takip ve dokümantasyon sorumluluğu

- `README.md`: Projenin yapısını, adlandırma ve çalışma kurallarını açıklar. Güncel ilerleme takibi yapmaz.
- `DURUM.md`: Aktif modülü, aktif görevi ve genel ilerlemeyi gösteren tek güncel takip dosyasıdır.
- Göreve özgü teknik ayrıntılar, kod, veri, log ve raporlar ilgili görev klasöründe tutulur.
- Yeni bir oturumda çalışmaya başlamadan önce bu README ve `DURUM.md` okunur; ardından üzerinde çalışılacak görevin kendi klasörü incelenir.
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
