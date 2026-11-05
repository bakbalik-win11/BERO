# E11 — Modül 2/3 birlikte yüksüz hat uzun süreli gözlem ve olay aktarımı

**Durum: UYGULANDI — 2026-11-05 yüksüz uzun gözlem ve olay karşılaştırması analiz edildi.** Aşağıdaki eski hazırlık adımları tarihsel plan olarak korunur; sonuç özeti en alttadır.

## 1. HEDEF

Aynı oturumda iki bağımsız çıktıyı incelemek:

1. **Yüksüz ölçüm tabanı:** Modül 3/PZEM yüksüz hatta hangi akım değerini gösteriyor; Modül 2'nin üç SCT kanalı yüksüz durumda ne yayınlıyor? PZEM gerilim ve PF ölçümleri de kendi akışında izlenecek.
2. **Olay aktarım güvenilirliği:** Modül 3'ün SSR ON/OFF geçişlerinde ürettiği olayların kaçı Modül 2'ye ulaşıyor? Uzun oturumda eksik, yinelenen veya sırası bozuk olay sayısı belirlenecek.

## 2. DENEY DÜZENEĞİ

- Modül 2 (ESP32D1): üç SCT kanalı ve ortak bias ile sürekli ölçüm/yayın yapar; UDP 4210 olay alıcısı açık kalır.
- Modül 3 (ESP32 WROOM/PZEM): PZEM ölçümlerini sürekli yayınlar; SSR olay döngüsü çalışır ve BOOT_ID/EVENT_ID/STATE olaylarını HA'ya ve UDP 4210'a gönderir.
- İzlenen hatta **yük bağlı olmayacaktır**. SSR'nin kontrol ettiği çıkışta da bu deney sırasında ölçülecek bir yük bulunmayacaktır; dolayısıyla SSR'nin mantıksal ON/OFF döngüsü sürse de test hattında yük akımı oluşturulması hedeflenmez.
- Modül 2 ve Modül 3 kendi ayrı beslemeleriyle çalışır; modül besleme akımı izlenen hattın akım ölçüm yoluna dahil edilmez.
- Modül 2'nin üç SCT kanalı birlikte açık kalır. Kanal seçmek için jumper/düğme eklenmesi bu deneyin kapsamı değildir.

## 3. UYGULAMA SIRASI

### A — Fiziksel hazırlık
**2026-11-05 güncellemesi:** Kullanıcı Modül 3 fiziksel montajının tamamlandığını bildirdi. Bu kullanıcı bildirimidir; bağlantıların doğruluğu ve montajın elektriksel güvenliği ayrıca kontrol edilmelidir. Enerjili devrede bağlantı değişikliği yapılmaz. Bu adımın ardından kısa ortak açılış kontrolüne geçilebilir.

### B — Kısa eşzamanlı açılış kontrolü
İki modül aynı anda başlatılır. Uzun teste geçmeden önce:
- Modül 3 PZEM gerilim, akım, PF ve diğer mevcut alanları yayınlıyor mu?
- Modül 2 üç SCT kanalında sürekli ölçüm/yayın yapıyor mu?
- Modül 3 BOOT_ID ve EVENT_ID üretiyor, SSR mantıksal ON/OFF olaylarını kaydediyor mu?
- Modül 3'te gönderilen bir ON ve bir OFF olayı Modül 2 logunda alınıp HA entity'lerine aktarılıyor mu?
- Açılış, Wi-Fi ve UDP tarafında belirgin hata/yeniden başlama var mı?

Kısa kontrol logları incelenmeden uzun test başlatılmaz. Yetişmezse uzun test sonraki uygun zamana bırakılır.

### C — Uzun yüksüz çalışma
Kısa kontrol uygunsa sistem kesintisiz uzun gözleme alınır. Hedef, sistemi ertesi gün akşama kadar yüksüz çalışır durumda bırakmaktır. Gerçek başlangıç/bitiş zamanı ve kesinti varsa süreleri logdan kaydedilir. SSR'nin mevcut 40 s ON / 20 s OFF döngüsü sürdürülür. Test için lamba veya başka yük yakılmaz.

## 4. KAYDEDİLECEK GÖZLEMLER

**PZEM / Modül 3**
- Gerilim, akım, PF ve mevcut diğer PZEM alanlarının değer ve kayıt davranışı.
- Yüksüz akımın sıfır, sıfıra yakın veya geçersiz değer davranışı; değerler peşinen sıfıra yuvarlanmaz/silinmez.
- BOOT_ID, EVENT_ID, STATE, SSR geçişleri, Wi-Fi kopma/yeniden başlama kayıtları.

**SCT / Modül 2**
- Üç kanalın ham ve filtrelenmiş akım çıktıları ile bias değeri.
- Yüksüz durumda sıfır/sıfıra yakın değerlerin dağılımı ve zaman içindeki değişimi.
- UDP olay alım logları ve HA olay entity yayınları.

**Olay aktarımı**
- Modül 3'te üretilen olay sayısı ve EVENT_ID aralığı.
- Modül 2'de alınan olay sayısı ve EVENT_ID aralığı.
- BOOT_ID + EVENT_ID + STATE eşleşmesi.
- Eksik, yinelenen, ters sıralı veya yalnız bir tarafta görünen olaylar.
- Modül 3 gönderim logu ile Modül 2 alım logu ayrı kaynaklar olarak karşılaştırılır. Yalnız HA geçmişindeki eksiklikten UDP kaybının nerede oluştuğu kesinleştirilmez.

## 5. BEKLENEN ÇIKTILAR VE SINIRLAR

- Çıktı 1: PZEM yüksüz akım davranışı ve Modül 2'nin üç SCT kanalının yüksüz taban davranışı.
- Çıktı 2: Uzun oturumda Modül 3'ün ürettiği ON/OFF olayları ile Modül 2'nin aldığı olayların sayısal karşılaştırması.
- Bu deney **yük altı eğitim verisi üretmez**; yüksüz taban ve olay aktarım davranışını gözler.
- SSR'nin HA/firmware mantıksal durumu fiziksel SSR anahtarlamasının elektriksel kanıtı değildir. Fiziksel anahtarlama ayrıca ve güvenli biçimde doğrulanmadıkça doğrulanmış sayılmaz.
- PZEM ve SCT'nin aynı anda yayın yapması, örneklerin birebir eşzamanlı olduğu anlamına gelmez. Bu deneyde örnek bazında timestamp eşleştirmesi yapılmaz.

## 6. KABUL / TAMAMLAMA

Deney ancak gerçek uzun loglar alındıktan sonra değerlendirilir. En azından:
- iki modülün kısa başlangıç logları,
- uzun oturumun başlangıç/bitiş bilgisi ve kesinti/yeniden başlama notları,
- PZEM ve üç SCT kanalı için yüksüz özet,
- Modül 3 gönderim ve Modül 2 alım olaylarının BOOT_ID/EVENT_ID bazında karşılaştırması,
- ölçüm ve olay aktarımı için ayrı yorumlar

depolandığında sonuç raporu hazırlanır. Ölçüm yapılmadan sonuç veya kayıp oranı yazılmaz.

## 7. İŞLETİM MODLARI HAKKINDA NOT

- Modül 2 tek başına SCT ölçüm/gözlem amacıyla çalıştırılabilir; Modül 3'ün zaman/olay bilgisi o tekil gözlem için zorunlu değildir.
- Modül 3 tek başına PZEM gözlemi için çalıştırılabilir.
- Modül 2 ve Modül 3 birlikte eğitim verisi/olay paketleri için kullanılacaksa iki ölçüm akışı ve Modül 3 olay üretimi birlikte aktif olmalıdır.
- İleride yalnız PZEM okunacak bir oturumda SSR ON/OFF döngüsünü yazılımdan devre dışı bırakmak mümkün bir işletim seçeneğidir; bu deneyde döngü açık tutulur. Bu kayıt firmware değişikliği veya böyle bir seçeneğin mevcut kodda hazır olduğu iddiası değildir.
- Deneylerin uygulanma sırası sabit değildir. Gerçek ihtiyaç, donanımın hazır oluşu ve gözlenen bulgulara göre Faz 2 deney önceliği değiştirilebilir. Bu esneklik, görevlerin teknik bağımlılıklarını veya mevcut ADR kararlarını kendiliğinden değiştirmez.

## 8. GÜVENLİK

220–240 V bağlantıların kurulumu/denetimi yetkin kişi tarafından, uygun muhafaza ve koruma ile yapılmalıdır. Modüllerin ayrı beslemesi ile izlenen hattın ölçüm bağlantıları karıştırılmamalıdır. CT sekonderi üretici talimatına aykırı biçimde açık bırakılmamalıdır. Yüksüz testte hatta yanlışlıkla yük bağlanmadığı ve SSR çıkışının güvenli durumda olduğu montaj öncesi kontrol edilmelidir.


## Görsel fiziksel teyit — kullanıcı bildirimi

Kullanıcı, Modül 2 ve Modül 3'ün birlikte çalıştığı bu ilk ortak çalışmada Modül 3'ün SSR çıkışına bağlı akkor ampulün yanıp sönmesini kendi gözleriyle gördüğünü ve fiziksel ON/OFF davranışını teyit ettiğini bildirdi. Bu, logların gösterdiği yazılım/ağ kayıtlarından ayrı bir kullanıcı gözlemidir.

**Kanıtın sınırı:** Kullanıcı görsel teyidi, test sırasında ampulün fiziksel olarak yanıp söndüğünü destekler. Modül 3 logunda OFF geçişlerinde `GPIO_OFF_READBACK_MISMATCH` uyarısı yine mevcuttur; bu uyarı silinmiş veya teknik olarak çözülmüş sayılmaz. Modül 2 logunda EVENT_ID 31, 32 ve 33 alımları vardır; EVENT_ID 34 alıcı logunda görünmediğinden UDP aktarımının bu kısa testte tamamen kayıpsız olduğu iddia edilmez.

Bu kayıt, **Modül 2 + Modül 3 ilk ortak çalışma / fiziksel SSR gözlem teyidi** olarak arşivlenmiştir. E11 yüksüz uzun gözlemi değildir.

Ham loglar:
- `logs/dual-module/2026-11-05-modul2-ilk-ortak-calisma.txt` (1070 satır)
- `logs/dual-module/2026-11-05-modul3-ilk-ortak-calisma.txt` (362 satır)



## 2026-11-05 — Yüksüz uzun gözlem sonucu

- Modül 3 EVENT_ID 6–97 aralığında 92 olay gönderimi kaydedildi; Modül 2 alıcı logunda 85 olay göründü. Görünmeyenler: 14, 16, 24, 34, 36, 41, 42. Görünür eşleşme 85/92 = %92.4'tür.
- Bu fark kesin UDP kaybı olarak adlandırılmaz; HA alıcı geçmişinde/logunda görünmeme ile gerçek ağ kaybı bu veriyle ayrıştırılamaz.
- Yüksüz SCT medyanları yaklaşık: SCT1 0.163 A, SCT2 0.170 A, SCT3 0.157 A. P95: SCT1 0.341 A, SCT2 0.306 A, SCT3 0.259 A.
- Ortak bias yaklaşık 1.663 V (min 1.573 V, max 1.729 V, std yaklaşık 0.0069 V).
- PZEM yüksüz akım 0.0 A kaydetti.
- Bu E11 verisi yüksüz taban/olay aktarım gözlemidir; ON akım kalibrasyonu veya eğitim verisi değildir.
- Sonuç, olay aktarımının tamamen kayıpsız olduğunu kanıtlamaz. Fiziksel SSR gözlemi ayrıca 2026-11-05 ilk ortak yüklü çalışma kaydında tutulur; bu E11 yüksüz deneyiyle karıştırılmaz.

**E11 sonucu:** Yüksüz ölçüm tabanı ve olay görünürlüğü için gözlem tamamlandı. Daha sonra Python'da olay paket bütünlüğü değerlendirmesine girdi olabilir; OFF/yüksüz örnekleri ON kalibrasyon eğitimine katılmaz.
