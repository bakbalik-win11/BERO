# I007 — Uzun dönem fiziksel sıfır-akım SCT gürültü havuzu

Bu dizin, ölçülen iletkende fiziksel yük akımının 0 A olduğu uzun süreli gözlem oturumlarını ve bunlardan oluşturulacak kümülatif veri havuzunu barındırır.

## İş akışı

1. Kullanıcı her gün veya uygun oturum sonunda Home Assistant History CSV sağlar.
2. Her kaynak CSV önce bağımsız incelenir ve oturum raporu hazırlanır.
3. Mevcut kümülatif dosya ve oturum indeksi depodan okunur.
4. Yeni oturumun ham kayıtları değiştirilmeden eklenir; zaman/entity/değer tekrarları kontrol edilir.
5. Kaynak oturum arşivi, oturum indeksi, kümülatif veri ve özet güncellenerek depoya yazılır.
6. İlk CSV'nin gerçek kolonları görülmeden kümülatif veri şeması sabitlenmez. Ölçüm içermeyen boş veya sentetik veri dosyası oluşturulmaz.

## Fiziksel ve ölçümsel bağlam

- Ölçülen hatta yük bağlı değildir; ESP, PZEM ve modüller bu ölçüm hattından beslenmez. Kullanıcının teyidine göre gerçek yük akımı fiziksel olarak 0 A'dır.
- SCT1 sarı/GPIO32: fiziksel 1T.
- SCT2 yeşil/GPIO33: nötr hattı, 4T.
- SCT3 mavi/GPIO34: faz hattı, 3T.
- GPIO35: ortak bias.
- Ham kanal ölçümleri korunur. Tur başına normalize edilmiş değer yalnız yardımcı kıyaslamadır.
- Her oturum ve kümülatif rapor kanal başına örnek sayısı, medyan, P95, P99, maksimum, saçılım ve zaman davranışını içerir.
- Havuz ON kalibrasyonundan ve PZEM–SCT ON eşleştirmesinden ayrıdır. İlk hedef yaklaşık 7–10 gün; kullanıcı isterse daha uzun devam eder. Yeterli oturumlar arası veri oluşmadan eşik/model belirlenmez.

## Dosya düzeni

İlk gerçek HA CSV'si geldikten sonra gerçek veri kolonları, boyut ve satır yapısına göre aşağıdaki içerik oluşturulacaktır:
- oturum bazlı değişmez kaynak CSV arşivleri;
- oturum indeksi ve kalite kontrol/özet kayıtları;
- ham kayıtları bir araya getiren kümülatif veri dosyası;
- kümülatif istatistik/dağılım raporu.

Henüz CSV gelmediği için bu dizinde ölçüm verisi veya kümülatif sayısal sonuç bulunmamaktadır.


## İlk oturum kaydı — 2026-11-05

İlk deneme verisi işlendi. PZEM akımının 0.0 A olarak kaldığı iki uzun aralık seçildi: 19:08:27–20:03:53 ve 20:54:08–21:16:05 (Europe/Istanbul). Aradaki yük çevrimleri bu ilk sıfır-akım özetine alınmadı. Kullanıcının fiziksel düzenek teyidi: hatta yük yok ve modüller bu hattan beslenmiyor; gerçek yük akımı 0 A.

- Oturum raporu: [sessions/2026-11-05-session-01.md](sessions/2026-11-05-session-01.md)
- Kümülatif oturum özeti: [cumulative-session-summary.csv](cumulative-session-summary.csv)

İlk oturumdaki akım entity medyanları SCT1=0.1603 A, SCT2=0.1698 A, SCT3=0.1567 A; P95 değerleri sırasıyla 0.3327 A, 0.2930 A, 0.2550 A'dır. Bunlar ilk gözlem özetidir; eşik değildir. Yeni oturumlarda bu CSV'ye yeni satır eklenecek, ham oturum raporları ayrı korunacaktır.


## Filtrelenmiş türev veri kararı — 2026-11-05

Kullanıcı kararı: kaynak/ham I007 kayıtları hiçbir zaman filtrelenerek üzerine yazılmayacak veya silinmeyecek. Ham akış değişmez kanıt olarak tutulacak; bunun yanında aynı kayıttan ayrı bir **filtrelenmiş/türetilmiş yüksüz akış** üretilebilecek. Filtreli akışın amacı fiziksel sıfır akım koşulunda kısa süreli sıçramaları bastırıp sistemin yüksüz durumunu daha kararlı temsil etmektir. Bu türev akış ON kalibrasyonuna veya ON eğitim eşleştirmesine eklenmez.

Önerilen analiz yaklaşımı (henüz kodlanmadı ve parametreleri belirlenmedi):
- Kayan pencere içinde merkez/dağılım hesapla; tekil uç değerlere duyarlı basit ortalama yerine medyan ve MAD gibi sağlam istatistikleri de değerlendir.
- Merkezden sapmayı tek başına yeterli sayma: sapmanın büyüklüğü ve ardışık örneklerde ne kadar süre devam ettiği birlikte değerlendirilsin.
- Kısa süreli tekil sıçramayı filtreli akışta bastır/işaretle; devam eden yükselişi gerçek durum değişimi adayı olarak koru.
- Her örnek için ham değer, filtrelenmiş değer, aykırı-değer bayrağı ve kullanılan pencere/parametre kimliği izlenebilir olsun.
- Filtre penceresi, sapma sınırı ve devam süresi deneyle seçilecek; henüz sabit eşik yok.

Bu tasarımın amacı ham veriyi kaybetmeden ikinci bir analiz katmanı oluşturmaktır. İlk deneme I007 oturumlarının kopyası üzerinde çevrimdışı yapılmalı; firmware'e filtre gömülmesi ancak çevrimdışı sonuçlar ve yük geçişi testleri görüldükten sonra değerlendirilmeli.

## Örnekleme hızı hedefi — kullanıcı önerisi, test bekliyor

Kullanıcı, SCT akım akışında yaklaşık her 0,5 saniyede bir yeni ölçüm çıktısı, yani saniyede 2 örnek (2 Hz) hedefini önerdi. Bu henüz ölçülmüş/uygulanmış bir performans değildir; test hedefidir.

Mevcut Modül 2 firmware kaynağında interval=2s ile üç SCT kanalı sıralı okunuyor; bu, her kanal için nominal yaklaşık 0,5 Hz (2 saniyede bir) güncelleme demektir. Her kanalın sample_duration değeri 200 ms. SCT1→SCT2→SCT3 arasında 250 ms bekleme bulunduğundan mevcut üç kanal sıralı çevrimi, her kanala 500 ms'de bir güncelleme verecek şekilde yalnızca interval değerini değiştirmekle hızlandırılamaz. Üç kanalın her birinde 2 Hz hedefi için edinim sırası, örnek süresi ve kanal eşzamanlılığı/önceliği yeniden tasarlanıp ölçülmelidir.

İlk testte iki ayrı hedef raporlanmalı:
1. Öncelikli tek kanal (SCT1) için 2 Hz çıktının gerçek zaman damgalarıyla sağlanıp sağlanamadığı.
2. Üç kanal birlikte açıkken her kanalın sürdürülebilir güncelleme hızı, zaman kayması, örnek kaybı, gürültü ve akım değerlerinin mevcut referansa göre değişimi.

2 Hz veri üretmek, her ölçümün 500 ms boyunca örneklendiği anlamına gelmez. Mevcut 200 ms sample_duration korunarak 500 ms aralıklarla sonuç üretmek ayrı bir tasarım hedefidir. K=24.22 ve diğer koşullar ilk hız testinde sabit tutulmalı; firmware değişikliği kullanıcı onayıyla ayrı kontrollü testte yapılmalıdır.


## 2026-11-07 — CH1 yüksüz 10 saat kaydı ve kapalı alan kararı (ADR-031)

Kullanıcı kararı: Bu 10 saatlik CH1 fiziksel yüksüz kayıt, ilk kapalı alan sınırını belirlemek için yeterli kabul edildi. Bu karar için 7–10 günlük çoklu oturum bekleme koşulu aranmayacaktır. Çoklu oturum verileri ileride oturumlar arası değişimi incelemek için eklenebilir; mevcut CH1 kararının ön koşulu değildir.

- 36.002 CH1 akım örneği ve 36.002 CH1 ham SCT örneği incelendi.
- K=24.22 uygulanmış akım P95: 0,23587365 A; ham SCT P95: 0,00973880.
- Seçilen kapalı alan üst sınırı: **0,24 A**. Bu eşikte örneklerin %96,33'ü eşik altında/eşit; %3,67'si üzerindedir.
- Sıçramalar temizlenmedi; karar P95 ve pratik yuvarlama ile verildi.
- Kaynak CSV kullanıcı isteğiyle depoya eklenmedi; yalnızca istatistiksel özet saklandı.
- Ayrıntı: [CH1 istatistik özeti](sessions/2026-11-07-ch1-closed-area-threshold.md), [ADR-031](../../docs/decisions/ADR-031-ch1-idle-closed-area-threshold.md).

Bu karar CH1 ve bu yüksüz koşulla sınırlıdır; diğer kanallara otomatik genellenmez. I007 çoklu oturum karakterizasyonu ek araştırma olarak sürebilir, ancak mevcut kapalı alan kararının ön koşulu değildir.
