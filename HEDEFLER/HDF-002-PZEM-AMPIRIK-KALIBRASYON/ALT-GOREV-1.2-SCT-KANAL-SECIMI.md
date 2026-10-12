# HDF-002 — Alt Görev 1.2
## SCT kanal seçimi ve iki katmanlı prototip mimarisi

### Karar

Prototipte kullanılacak üç SCT kanalı:

- **ESP32D #1 → 1T SCT**
- **ESP32D #2 → 2T SCT**
- **ESP32E → 4T SCT**

3T SCT okumalarında yaşanan sorun nedeniyle mevcut prototipte 4T SCT kullanılacaktır. Bu, geçici seçim olarak değil, prototipin güncel sensör eşlemesi için alınmış yeni karar olarak kaydedilir. 3T ile ilgili geçmiş sorun ve deneyimler korunur; bu karar 3T sorununun çözüldüğü anlamına gelmez.

### İki katmanlı mimari

Bu düzen aynı zamanda iki katmanlı bir yapı oluşturur:

1. **Ölçüm katmanı:** Üç ayrı ESP kendi SCT sensörünü ve o kanala ait BIAS değerini okur. Ham kayıtlar sensör ve cihaz kimliğiyle korunur.
2. **Referans ve deney kontrol katmanı:** PZEM ESP yalnızca kendi PZEM cihazını okur; ayrı SSR kontrol ESP'si yükün deney döngüsünü yönetir. Bu işlevler SCT ESP'lerinin ölçüm görevini üstlenmez.

SSR için 55 saniye açık + 5 saniye kapalı döngüsü başlangıç zamanlama adayı olarak ayrıca kaydedilmiştir; optimum olduğu henüz doğrulanmış değildir.

### Kayıt ve kanıt sınırı

- 3T SCT'nin eski sorun kayıtları korunur ve 4T kayıtlarıyla karıştırılmaz.
- Her SCT kanalının kendi BIAS değerinin ölçülmesi yeni donanım modifikasyonu gerektirir; bu modifikasyon ayrı alt görevde takip edilir.
- Bu kayıt mimari ve sensör seçimi kararını tanımlar. Yeni düzenin kurulduğu veya üç sensörün başarıyla okunduğu iddia edilmez.

### Ek karar — kanal adı veride korunur, sarım sayısına göre ön bölme yapılmaz

- `1T`, `2T` ve `4T` etiketleri fiziksel kanal yapılandırmasını tanımlar; hesaplama öncesi bölme oranı değildir.
- Her veri kaydında `channel_id` (1T/2T/4T), `esp_id` ve ilgili `bias_id` korunur. Kalibrasyon parametresi aynı kanal kimliğiyle eşleştirilir.
- BIAS düzeltmesinden sonra veriler sarım sayısına göre önceden bölünmeden kalibrasyona girer. Ham kayıtlar korunur; dönüştürülmüş sonuçlar ayrı tutulur.
- Her kanal için ayrı (K) katsayısı deneysel aday olarak değerlendirilebilir. (K), en iyi sarım sayısını kanıtlamaz; yalnızca ampirik ilişki hakkında ipucu verir. Tek katsayının farklı akım seviyelerinde yeterliliği doğrulanmalıdır.
- (K) yeterli olmazsa daha genel kanal bazlı (F(x)) değerlendirilir. Hangi sarımın daha iyi olduğu; ham veri kalitesi, PZEM'e göre hata ve bağımsız doğrulama sonuçlarıyla değerlendirilir.
- Bu karar, ön bölmenin kesin olarak hataya neden olduğunun kanıtı değildir; amaç kalibrasyon öncesinde sarım oranı varsayımını veriye dayatmamaktır.

**İlgili aşamalar:** Alt Görev 1.1 (BIAS-kanal ilişkilendirmesi), P1 (kimlikleri koruyan arşiv), P2 (kanal bazlı olay eşlemesi/etiket), P3–P4 (ön bölmesiz ilk (F(x)) ve doğrulama), P5–P6 (aynı kanal/katsayı kimliğiyle paketleme ve canlı sınama).

**Kanıt sınırı:** Bu karar prototipin montajının, hesaplamanın veya kalibrasyonun tamamlandığını göstermez.

### Araştırma sorusu — ayrı model mi, ortak F(x) mi?

Üç ölçüm ESP'sinin her biri için ayrı kalibrasyon/model eğitimi yapmak mı gerekir, yoksa 1T/2T/4T kanal kimlikleri korunarak tek bir ortak (F(x)) bütün ilgili bölgelerde yeterli olabilir mi? Bu karar önceden verilmeyecek.

- Her kanalın ham verisi ve kendi BIAS kaydı ayrı tutulur; sarım sayısına göre ön bölme yapılmaz.
- Kanal bazlı K/F(x) adayları ile ortak F(x), aynı türde PZEM ile eşleştirilmiş kayıtlar ve bağımsız test ölçütleriyle karşılaştırılır.
- Düşük/değişken akım (ör. bilgisayar masası) ve farklı/yüksek yük koşulları (ör. tost makinesi) ayrı bağlamlar olarak değerlendirilir.
- Ortalama hata yanında hata dağılımı, mutlak amper hatası ve tekrarlanabilirlik raporlanır.
- K katsayısı yalnızca ipucudur; tek başına en iyi sarımı veya model mimarisini seçmez.

**Kanıt sınırı:** Bu bir araştırma sorusudur; ayrı modellerin ya da tek ortak modelin üstünlüğü henüz kanıtlanmamıştır.

### İleri mimari araştırması — ESP32-P4-Pico

ESP32-P4-Pico, HDF-002 sonrasında BERO'nun nihai saha akım ölçüm ESP'si adayı olarak kaydedilir. 1T/2T/4T ile yapılan üç ayrı ölçüm zinciri araştırma/veri üretme aşamasında kalır; bunlardan elde edilen kanıtlar P4-Pico'da kullanılacak model mimarisini belirlemeye yardımcı olur.

Araştırılacak seçenek: kanal/sarım kimliklerine göre ayrı K/F(x) modelleri çalıştırmak mı, yoksa ortak F(x) kullanmak mı? P4-Pico'nun GPIO ve ölçüm giriş eşlemesi, ADC bağlantısı ve gerçek örnekleme performansı ayrıca doğrulanır. GPIO'ların fiziksel sarım sayısını değiştirdiği varsayılmaz; üç modelin GPIO'larla farklı sarım yapılandırmalarını yönetmesi şu an için bir mimari fikirdir.

**Kanıt sınırı:** P4-Pico'nun nihai saha kartı olarak seçimi yön olarak kaydedilmiştir; uygunluk, bağlantı ve çalışma başarısı henüz test edilmemiştir.

