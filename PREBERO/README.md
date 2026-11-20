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

### Kod sürümleme

Görev kimliği ile kod sürümü birbirinden bağımsızdır.

Örnek:

- Görev: `MOD2-GRV001`
- Kod sürümü: `V1.0`

Aynı görevde kod geliştirildiğinde görev kimliği değişmez; kod sürümü ilerletilir. İlk sürüm `V1.0` olarak başlatılır. Küçük geliştirmeler `V1.1`, `V1.2` gibi; kapsamlı değişiklikler `V2.0` gibi yeni bir ana sürümle gösterilir. Sürüm artışının gerekçesi görev kayıtlarında açıklanır.

### Kod içinde kimlik bilgisi

Her kod dosyasının başında en az şu bilgiler bulunur:

- Proje: `PREBERO`
- Modül: ilgili modül numarası
- Görev: tam görev kimliği
- Kod sürümü: sürüm numarası
- Amaç: kodun yaptığı iş
- Donanım bağlantıları ve beklenen davranış

ESP üzerinde çalışan kodda bu bilgiler kaynak kod başlığında bulunur. Uygun olduğunda açılış loguna da modül, görev ve sürüm bilgisi yazdırılır. Böylece kod dosyasına veya ESP loguna bakıldığında hangi modülün hangi görev sürümünün çalıştığı anlaşılır.

### Dosya ve çıktı düzeni

Her görevin kendi klasörü bulunur. Göreve ait tüm çalışmalar bu klasörde tutulur:

- `KOD/`: Kaynak kodlar ve sürümlü kod dosyaları.
- `VERI/`: Deney verileri ve ham/işlenmiş veri çıktıları.
- `LOG/`: Gerçek çalışma logları ve test kayıtları.
- `RAPOR/`: Analizler, sonuç yorumları ve deney raporları.

Dosya adlarında gerektiğinde görev kimliği ve kod sürümü birlikte kullanılır. Örnek: `MOD2-GRV001_V1.0.yaml`.

Başarılı bir kod sürümü, o sürümle alınmış gerçek test logu ve logun teknik yorumu aynı görev klasöründe saklanır. Test edilmemiş veya doğrulanmamış kod başarılı/kararlı sürüm olarak işaretlenmez.

## Takip ve dokümantasyon sorumluluğu

- `README.md`: Projenin yapısını, adlandırma ve çalışma kurallarını açıklar. Güncel ilerleme takibi yapmaz.
- `DURUM.md`: Aktif modülü, aktif görevi ve genel ilerlemeyi gösteren tek güncel takip dosyasıdır.
- Göreve özgü teknik ayrıntılar, kod, veri, log ve raporlar ilgili görev klasöründe tutulur.
- Yeni bir oturumda çalışmaya başlamadan önce bu README ve `DURUM.md` okunur; ardından üzerinde çalışılacak görevin kendi klasörü incelenir.
- Ana dizindeki `DONANIM/` ve `ENVANTER/` ortak donanım ve envanter bilgilerinin tek kaynağıdır. Bu bilgiler PREBERO altında kopyalanmaz.

### ESP cihaz adı ve YAML teslim standardı

- Her modülde kullanılan ESP cihazına verilen ad/kimlik sabittir. Kod sürümü veya YAML güncellendiğinde ESP cihaz adı değiştirilmez.
- ESP cihaz adı, ilgili modülün donanım ve ağ kimliğiyle tutarlı tutulur. Zorunlu bir değişiklik gerekirse önce gerekçesi açıklanır ve kayıt altına alınır; kendiliğinden yeniden adlandırma yapılmaz.
- Home Assistant / ESPHome için YAML istendiğinde yalnızca değişen bölüm değil, yapılandırmanın tamamı verilir.
- Verilen YAML eksiksiz, doğrudan kopyalanıp kullanılabilir tek bir kod bloğu içinde sunulur. Kullanıcı özellikle istemedikçe parçalı YAML veya "... mevcut ayarları koruyun" gibi eksik bırakılmış bölümler verilmez.
- Her YAML'ın başında amacı, ilgili modül ve görev kimliği, kod sürümü, donanım bağlantıları ve beklenen çalışma davranışı açıklanır.
- YAML verilmeden önce mevcut yapı ve bağlantılarla çelişki olup olmadığı kontrol edilir. Bilinmeyen bağlantı veya değerler varsayılmaz; gerekiyorsa kullanıcıdan netleştirilir.
