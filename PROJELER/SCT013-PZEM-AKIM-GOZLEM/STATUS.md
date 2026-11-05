## 2026-11-05 — Sonraki oturumun ilk işi: yüksüz/gürültü CSV kaydı

Kullanıcı bu gece sistem yüksüzken Home Assistant History kaydı alacağını bildirdi. Bir sonraki oturum açıldığında ilk olarak bu yüksüz CSV dosyası kullanıcıdan istenecek; kullanıcı sağlayınca ayrı OFF/yüksüz gürültü veri havuzunun ilk kaydı olarak analiz edilecek.

- SCT1 sarı/GPIO32: fiziksel 1 geçiş (YAML/entity etiketi 2T kalmış olabilir).
- SCT2 yeşil/GPIO33: nötr hattında 4 geçiş.
- SCT3 mavi/GPIO34: faz hattında 3 geçiş.
- GPIO35: ortak bias.
- Her oturum ayrı analiz edilecek; ham dağılımlar korunarak zaman içinde ortak havuzda biriktirilecek.
- Tur sayısına bölme yaklaşık normalize karşılaştırmadır, kesin kalibrasyon değildir. Kanal/hat konumu, kazanç ve K farkları nedeniyle ham değerler de raporda tutulacak.
- Amaç: yüksüz tabanın tipik seviyesi, üst yüzdelikleri ve tekrarlayan en yüksek değerleri görmek; henüz eşik belirlemek değil.
- Bu kayıt ON kalibrasyonuna katılmayacak.


## 2026-11-05 — I007 uzun süreli fiziksel sıfır-akım gürültü bandı

I007 tek gecelik test değil; başlangıç hedefi yaklaşık 7–10 gün, gerekirse kullanıcı kararıyla daha uzun sürecek veri toplama çalışmasıdır. Kullanıcı her gün/uygun oturum sonunda HA History CSV sağlayacak. Her oturum ayrı analiz edilecek; geçerli ham kayıtlar depodaki kümülatif havuza eklenerek güncellenecek. Her ekleme öncesi mevcut havuz depodan okunacak, tekrarlar kontrol edilecek, yeni kayıtlar eklenecek ve güncel kümülatif veri/özet tekrar depoya yazılacak. İlk gerçek CSV geldiğinde gerçek kolonlara göre veri şeması belirlenecek.

**Fiziksel referans:** Kullanıcının teyidine göre ölçülen hatta hiçbir yük bağlı değil ve ESP/PZEM/modüller bu hattan beslenmiyor; dolayısıyla gerçek hat yük akımı fiziksel olarak 0 A. SCT'nin sıfırdan farklı okuması bu koşuldaki ölçüm tabanı/gürültü çıktısıdır; sıfır koşulu PZEM göstergesinden varsayılmıyor.

Hedef uzun dönem SCT1/2/3 gürültü bandını, üst yüzdelikleri ve oturumlar arası değişimi belirlemek; şu aşamada eşik/model seçmek değildir. Ham ölçümler korunacak, tur-normalize karşılaştırma yalnız yardımcı olacak. Bu havuz ON kalibrasyonundan ayrı tutulacak.


## 2026-11-05 — I007 filtre yaklaşımı ve SCT 2 Hz hedefi

Kullanıcı kararları kayda alındı:
- I007 ham yüksüz kayıtları değişmez biçimde korunacak; filtrelenmiş/türetilmiş yüksüz veri ayrı akış/dosya olarak üretilecek.
- Kısa tekil sıçramalar kayan pencere, sağlam merkez/dağılım ve süre koşuluyla filtrelenebilir/işaretlenebilir; belirli süre devam eden yükseliş korunmalı. Pencere uzunluğu, sapma sınırı ve devam süresi henüz belirlenmedi.
- Kullanıcı SCT'den yaklaşık 0,5 saniyede bir yeni çıktı (2 Hz) hedefliyor. Mevcut Modül 2 firmware üç kanalı 2 saniyelik çevrimde sıralı okur; dolayısıyla kanal başına nominal hız yaklaşık 0,5 Hz'dir. Mevcut 200 ms örnek süresi ve üç kanallı sıralı yapı nedeniyle yalnız çevrim aralığını 500 ms yapmak üç kanalda 2 Hz sağlamaz.
- Tek SCT1 kanalı için 2 Hz ve üç kanalın her biri için 2 Hz ayrı fizibilite hedefleri olarak test edilecek. Firmware değişikliği yapılmadı.

Ayrıntılı test planı: [E13 — Yüksüz gürültü filtresi ve SCT örnekleme hızı](experiments/E13-idle-noise-filter-and-sampling-rate/README.md). E12'nin tepki süresi kapsamına 2 Hz hedefi de eklendi. I007 ham/filtreli veri kararı [I007 veri havuzu](data/off-noise/README.md) altında kayıtlı.


## 2026-11-05 — Canlı ölçüm mimarisi netleştirme

Kullanıcı kararı: Üç SCT kanalının okunması eğitim/veri toplama aşaması içindir. Canlı çalışan eğitilmiş ESP yalnızca tek SCT kanalını okuyacak ve her 500 ms'de bir yeni sonuç üretecek (2 Hz). Üç kanalın her birinde 2 Hz hedefi canlı mimarinin gereksinimi değildir. Mevcut Modül 2 üç kanallı eğitim firmware'i bu nedenle değiştirilmez; tek kanallı canlı ESP ayrı hedef mimaridir.

Filtre için ilk tasarım adayı: 2 Hz akışta 4 saniyelik kayan pencere = 8 örnek. Ham veri korunacak; tekil sıçramalar ayrı türetilmiş filtreli akışta işaretlenecek/bastırılacak; devam eden yükseliş gerçek yük başlangıcı olabileceği için korunacak. 4 saniye/8 örnek nihai parametre değil, deney adayıdır. Pencere, sapma sınırı, ardışık devam koşulu ve algılama gecikmesi E13'te test edilecek.

Ayrıntı: [E13 — Yüksüz gürültü filtresi ve SCT örnekleme hızı](experiments/E13-idle-noise-filter-and-sampling-rate/README.md).


## 2026-11-05 — BERO kullanım vizyonu genişletildi: davranış izleme ve arıza/anomali takibi

Kullanıcı, BERO'nun yalnızca ev makinelerinin programını veya çalışma evresini tahmin eden bir sistem olarak tanımlanmaması gerektiğini açıkladı. Makine/program tanıma hedeflerden yalnızca biridir. Uzun vadeli hedef, akım davranışlarını izleyerek ekipman ve hatların normal çalışma karakterini öğrenmek, zaman içindeki değişimleri görünür kılmak ve olası anormal durumları işaretlemektir.

Öngörülen kullanım alanları:
1. **Çalışma karakteri ve durum çıkarımı:** çamaşır makinesi gibi cihazların çalışma evreleri, motor/rezistans devreye girme-çıkma davranışları ve çalışma düzenleri.
2. **Arıza/anomali belirtileri:** havalandırma motoru veya su kuyusu hidroforu gibi ekipmanlarda akım seviyesinin, çalışma süresinin, devreye girme sıklığının ya da davranış örüntüsünün normalden sapması. Bu çıktılar doğrudan kesin arıza teşhisi değil, olası sorun/bakım incelemesi uyarısı olarak ele alınmalıdır.
3. **Uzun dönemli hat/ekipman izleme:** günlük/haftalık/aylık akım eğilimleri, baz seviyedeki kademeli yükselişler, ani değişimler ve karşılaştırmalı grafikler.

Bu vizyon mevcut SCT013-PZEM alt projesinin anlık görevlerini değiştirmez; mevcut odak ölçüm yolunu güvenilir kılmak, veri toplamak ve davranış çıkarımına uygun veri altyapısını oluşturmaktır. Kısa vadeli çamaşır makinesi denemeleri daha geniş sistemin ilk kullanım senaryolarından biridir; nihai ürün tanımı değildir.

Ölçüm kararlılığı bu nedenle yalnızca yüksüz/yüklü ayrımına indirgenmez. Tekil sıçramaları filtreleme, kısa süreli örnek toplama, süreklilik kontrolü, pratik eşik kullanımı ve uzun dönem trend analizi ileride deneyle değerlendirilebilecek yöntemlerdir. Şu aşamada belirli bir filtre, eşik, algoritma veya arıza sınıflandırma yöntemi kesinleştirilmemiştir. Ham ölçümlerin korunması ve türetilmiş/filtrelenmiş verinin ayrı tutulması esastır.
