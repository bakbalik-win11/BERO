# E17 — CH1 düşük akım bölgesi: sürekli küçük yük gözlemleri

**Tarih:** 2026-11-07  
**Faz:** Faz 2  
**Durum:** AÇIK — 18 W kaydı sürüyor  
**İlişkili karar:** [ADR-031 — CH1 kapalı alan üst sınırı](../../docs/decisions/ADR-031-ch1-idle-closed-area-threshold.md)

## Amaç

CH1'in 0,24 A kapalı alan sınırının üzerindeki düşük akım davranışını kontrollü, sürekli bağlı küçük yüklerle gözlemek. Bu deneyin amacı düşük akım bölgesinde CH1'e zorla sayısal ölçüm yaptırmak veya K katsayısını kalibre etmek değildir. Amaç, fiziksel yük bulunduğunda SCT'nin verdiği tepkiyi görmek ve hesaplanmaması gereken alanı pratik olarak ayırmaktır.

## Mevcut alan sınıflandırması

- 0–0,24 A: CH1 kapalı alanı.
- 0,24–0,41 A: **hesaplanmadı alanı**; bu aralıkta yazılım sayısal akım değeri üretmeyecek.
- 0,41 A üzeri: hesaplanacak alan adayı; ilk güvenilir okuma sınırı kontrollü deneylerle doğrulanacaktır.

Bu sınırlar mevcut CH1 kurulumu ve K=24.22 bağlamındadır; diğer kanallara veya başka sensörlere otomatik genellenmez.

## E17-A — 18 W akkor ampul, sürekli açık

### HEDEF

18 W küçük akkor ampul bağlıyken PZEM referans akımını ve SCT CH1 tepkisini gözlemek. Röle anahtarlama etkisini deneyden çıkarmak.

### Bağlantı ve koşullar

- Yük: 18 W akkor ampul.
- Ampul, deney süresince sürekli yanık; açma/kapama çevrimi yok.
- Röle bu deneyde kullanılmıyor; dolayısıyla röle tetikleme/anahtarlama etkisi bulunmuyor.
- PZEM, hatta bağlı yükün referans akım/gerilim verisini üretiyor.
- SCT tarafında CH1 izleniyor.
- Kullanıcının bildirdiği deney başlangıcı: **10:21, 2026-11-07 (Europe/Istanbul)**.
- 10:14 civarındaki grafik hareketi PZEM'i devreye alma/bağlantı denemeleriyle ilişkilendirildi; deney başlangıcı sayılmayacak ve E17-A verisine dahil edilmeyecek.
- Firmware, K katsayısı ve örnekleme ayarlarında bu deney için değişiklik bildirimi yoktur; gerçek ayarlar CSV geldiğinde doğrulanacaktır.

### İlk ekran gözlemi — 10:21 sonrası

Kullanıcının paylaştığı HA grafiğinin lejantındaki son değerler:
- PZEM gerilimi: 227,1 V.
- PZEM akımı: 0,078 A.
- CH1 hesaplanmış akım entity'si: 0,277 A.
- CH1 ham SCT entity'si: 0,01145 A olarak görüntüleniyor.

Grafikte CH1 hesaplanmış akım eğrisi 10:21 sonrasında yaklaşık 0,28–0,30 A çevresinde seyrediyor. Bu, CH1'in fiziksel yük varlığına tepki verdiğine ilişkin **ilk ekran gözlemidir**; kararlılık veya tekrar edilebilirlik sonucu değildir. PZEM'in 0,078 A okuması 18 W / 227,1 V için beklenen yaklaşık 0,079 A düzeyiyle uyumludur (basit güç/gerilim hesabı; ampulün gerçek çalışma gücü ayrıca ölçülmedi).

### Geçici yorum ve kullanıcı kararı

CH1'in 18 W yükte tepki verdiği görülüyor; ancak 0,277–0,30 A çıktısı 0,24–0,41 A hesaplanmadı alanına düşüyor. Bu nedenle:
- Fiziksel yük/ana akım varlığı algılanabilir.
- Bu aralıkta CH1 sayısal akım değeri kabul edilmeyecek ve yazılım tarafından hesaplanmayacak.
- Bu bölge daha sonra farklı/daha hassas bir sensörle ayrı çalışma konusu olabilir.
- Bu gözlem K=24.22 kalibrasyonuna veya CH1'in düşük akımda doğru ölçtüğü iddiasına kanıt değildir.

### Kayıt planı

HA History kaydı bir süre daha sürdürülecek. Ham CSV kullanıcı tarafından sağlandığında gerçek kolonlar, zaman damgaları, örnek sayısı, dağılım ve zaman içindeki kararlılık incelenecek. Ham CSV varsayılan olarak depoya eklenmeyecek; kullanıcı tercihi doğrultusunda istatistik ve yorum saklanacak.

## E17-B — 15 W mini buzdolabı ampulü, sürekli açık (sonraki ayrı deney)

Kullanıcı, 18 W kaydından sonra 15 W mini buzdolabı ampulüyle sürekli açık ayrı bir kayıt almak istedi. Kullanıcı bu ampulün farklı tepkiler verdiğini belirtti.

- E17-B, E17-A'dan ayrı oturum olarak kaydedilecek.
- Ampulün tam çalışma koşulu ve deney başlangıç saati o oturumda not edilecek.
- 18 W ve 15 W verileri tek zaman serisi veya tek deney sonucu gibi birleştirilmeyecek.
- Farklı tepki gözlemi şu an **kullanıcı bildirimi/ön beklenti** niteliğindedir; henüz yeni 15 W kaydıyla doğrulanmış değildir.

## Sonuç durumu

E17-A açıktır. Şu an yalnızca ekran görüntüsü üzerinden ilk tepki gözlemi vardır. Uzun kayıt analizi, istatistiksel kararlılık, tekrarlanabilirlik ve nihai deney sonucu henüz yoktur. E17-B henüz başlatılmamıştır.
