# I010 — 18 W yük düşük yük ayrışma deneyi

## Amaç

Mevcut 15 W ampulün HA grafiklerinde kirli/bozucu davranış gösterdiğine ilişkin kullanıcı gözlemi nedeniyle kontrollü test yükü olmaktan çıkarılmasının ardından, yeni **18 W yükün** OFF durumundan istatistiksel olarak ayrışıp ayrışmadığını incelemek.

## Deney kararı ve başlangıç durumu

- Önceki 13 W planı kullanıcı tarafından düzeltildi; **yeni test yükü 18 W'tır**.
- Kullanıcı 6 Kasım 2026 tarihinde 18 W yük ile yeni teste geçileceğini bildirdi.
- Kullanıcı bildirimi: **6 Kasım 2026 saat 17:43 (+03:00) itibarıyla 18 W yük ON yapıldı; I010 başladı.** Saniye düzeyinde zaman bilinmiyor.
- Mevcut 15 W ampul kullanılmayacak.
- 18 W tek başına test edilecek; 57 W veya başka yükle birleştirilmeyecek.
- CH1-1T, firmware ve ölçüm parametreleri mümkün olduğunca sabit tutulmalı; gerçek bağlantı ve yazılım koşulları başlangıçta ayrıca kaydedilecek.

## Analiz yöntemi

- Fiziksel OFF ve 18 W ON çevrimleri ayrı segmentlenecek.
- Tekil örnek sıçramaları karar sayılmayacak; ham veride korunacak.
- K uygulanmış CH1 çıktısı için eşik üstünde kalma süresi, devamlılık, pencere medyanı, MAD ve zaman kararlılığı incelenecek.
- 5, 10, 20, 30 ve 60 saniyelik aday pencereler karşılaştırılacak; bunlar henüz onaylanmış karar süreleri değildir.
- PZEM akım ve güç kayıtları aynı zaman pencerelerinde kendi geçerli timestamp'leriyle ayrı özetlenecek.
- ON/OFF dağılımlarının örtüşmesi ve çevrimler arası tekrarlanabilirlik raporlanacak.
- Ham kayıt değiştirilmeyecek; geçişler ve sıçramalar silinmeyecek.

## Beklenen yanıt

Temel soru, 18 W ON durumunun OFF referansından yeterli süre ve kararlılıkla ayrışıp ayrışmadığıdır. Sonuç yalnızca bu 18 W yük ve mevcut ölçüm zinciri için geçerli olacaktır; tek başına genel eşik oluşturmaz.

**Durum: BAŞLADI — ilk görsel gözlem mevcut, toplu veri analizi bekleniyor.**

## Düzeltme kaydı

Önceki taslakta 13 W yazılmıştı. Kullanıcının son bildirimiyle deney yükü **18 W** olarak düzeltildi. 13 W deneyi plan kapsamında değildir.


## Gerçek başlangıç kaydı — 18 W

- Kullanıcı bildirimi: **17:43 (+03:00), 6 Kasım 2026 — 18 W ON.**
- Bu zaman kullanıcı bildirimidir; saniye hassasiyeti ve CSV/PZEM zaman serisiyle doğrulama henüz yoktur.
- Analiz, I010 planındaki süre-temelli ON/OFF karşılaştırmasına göre yapılacaktır. Tekil sıçramalar sınıflandırma kararı sayılmayacak.


## İlk kullanıcı gözlemi — 18 W ON/OFF ayrımı

- Kullanıcının 6 Kasım 2026 tarihli gözlemi: **K=24.22 uygulanmış CH1 çıktısında 0.20 A altı OFF davranışıyla uyumlu; 18 W yükte ON/OFF ayrımı grafikte görülüyor.**
- Bu, ilk görsel/operasyonel gözlemdir; henüz CSV üzerinden süre-temelli istatistiksel doğrulama değildir.
- 0.20 A sınırı şimdilik bu deney için desteklenen aday OFF eşiği olarak not edilir; genellenmiş veya nihai eşik ilan edilmez.
- Doğrulamada tekil sıçramalar değil, 0.20 A çevresindeki seviyenin ne kadar süre devam ettiği, pencere medyanı/MAD ve ON/OFF çevrimlerinin tekrarlanabilirliği incelenecek.
- 18 W ON durumunun OFF'tan ayrılması, yalnızca mevcut ampul ve ölçüm koşulları için gözlemdir; diğer yük seviyelerine genellenmez.


## Analiz hedeflerinin ayrılması — iki bağımsız soru

I010 verisi iki ayrı istatistiksel hedef için kullanılacaktır. Bu hedefler birbirinin yerine geçmez:

### A. Akım var / akım yok kararını öğrenmek

- Amaç: Fiziksel OFF ile 18 W ON durumunu zaman içinde güvenilir biçimde ayırabilecek kanıtı bulmak.
- Referans: PZEM akım ve güç serileri ile kullanıcı tarafından bildirilen fiziksel ON/OFF zamanları birlikte kullanılacak; PZEM pratik referanstır, mutlak ground truth değildir.
- CH1 karar girdisi: K=24.22 uygulanmış akım çıktısı.
- 0.20 A, kullanıcı gözlemine dayalı **aday OFF sınırıdır**. Tekil örneğe uygulanmayacak; süre, ardışık devamlılık ve zaman penceresi davranışıyla sınanacak.
- Uzun 18 W ON/OFF çevrimleri, kararın çevrimler arasında tekrarlanabilirliğini ölçmek için sürdürülecek.

### B. Akım hesaplanamadı alanını çerçevelemek

Bu hedef, ON/OFF kararından ayrıdır. Amaç yalnızca sınıf etiketi vermek değil; ölçümün OFF referansına ne kadar yakın, ne kadar dalgalı ve ne kadar kararsız olduğunu nicel olarak tarif etmektir.

Her zaman penceresi için en az şu özetler üretilecek:
- pencere medyanı ve OFF medyanından farkı;
- MAD ve mümkünse IQR/P05/P95;
- pencere içi tepe-tepe aralığı ve zamana göre medyan değişimi;
- eşik çevresinde geçirilen süre ve en uzun kesintisiz süre;
- OFF referans dağılımıyla örtüşme/ayrışma;
- ölçüm sayısı, gerçek kapsanan süre ve timestamp boşlukları.

Bu çerçeve, `CURRENT_NOT_COMPUTABLE` alanını tanımlamaya yardım eder. Tek bir sayı veya tek eşik şimdiden belirlenmeyecek; pencere uzunlukları ve karar sınırları deney sonuçlarıyla seçilecek.

## 18:00 veri kontrol noktası ve devam planı

- Kullanıcı 18:00'de mevcut veriyi paylaşacağını bildirdi. Bu veri ilk analiz/kontrol noktası olarak ele alınacak; deneyin tamamlandığı anlamına gelmez.
- İlk veri kontrolünden sonra kullanıcı uzun 18 W ON/OFF aç-kapa testine devam edecek.
- İlk veri kesiti ile sonraki uzun aç-kapa kaydı ayrı veri bölümleri olarak saklanacak ve zaman damgaları korunacak; analizde aynı I010 deneyinin ayrı kayıt dilimleri olarak ilişkilendirilecek.
- 15 W içeren tüm dönemler I010 kontrollü karşılaştırmasından hariç tutulacak; ham veri silinmeyecek.
