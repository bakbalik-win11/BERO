## 2026-11-13 — E19 100 W yorum düzeltmesi ve 150 W testinin açılması

- 100 W ortak pencerede ADS1115 ortalaması 0.469881 A (n=84), PZEM 0.469882 A (n=34), Modül 2 CH1-1T 0.434240 A (n=167). Bu, aynı oturumdaki gözlemsel karşılaştırmadır; aynı noktadan türetilen K ile uyum bağımsız kalibrasyon doğrulaması değildir.
- ADS1115 açılış logundaki `Sample rate: 7` değeri 7 SPS değil, 860 SPS enum/register kodudur. 200 ms'de 174–177 farklı örnek logu 860 SPS ayarıyla uyumludur. Önceki hız uyuşmazlığı yorumu geri çekildi.
- Depodaki E19 YAML katsayısı 30.0 başlangıç doğrusu; yorumda geçen 27.60 ile çalışan binary eşleştirilmedi. K değişmedi.
- ADS1115 gain 2.048, 200 ms pencere, 2 s güncelleme, 0.05 A filtresi ve accuracy_decimals 2 korunuyor. Gain 0.512, filtre veya yayın hassasiyeti değişikliği yapılmadı.
- SSR OFF sonrası akım ve GPIO readback mismatch nedeniyle fiziksel anahtarlama doğrulanmadı; UDP olayları fiziksel yük etiketi değil.
- **Aşama 3 açıldı: 150 W akkor sabit yük testi — PLANLANDI.** Mevcut ADS1115/PZEM ayarları değiştirilmeden ortak kararlı kayıt alınacak. Ölçüm/log henüz yok.
- Ayrıntı: [E19 README](experiments/E19-ads1115-low-current-alternative/README.md), [sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md), [100 W düzeltme raporu](logs/ads1115/2026-11-13-E19-three-module-100w-comparison.md).

## 2026-11-13 — E19 üç modül ortak yük karşılaştırması kaydedildi

- Ortak kesişim 17:48:27–17:51:13 (+03:00): ADS1115 ortalaması 0.469881 A (n=84), PZEM 0.469882 A (n=34), Modül 2 CH1-1T 0.434240 A (n=167). Modül 2/PZEM farkı yaklaşık -7.59%; yalnız bu oturum için gözlemsel sonuçtur.
- ADS1115 yayın hassasiyeti 0.01 A'dır. Açılış logu Gain 2 / Sample rate 7 gösterirken depodaki E19 YAML 2.048 / 860 bekliyor; 860 SPS uygulandığı doğrulanmadı.
- UDP olayları alınıp HA'ya yayımlandı. Modül 3'te OFF readback mismatch uyarıları var; PZEM akımı OFF sonrasında sürüyor. Fiziksel OFF doğrulanmadı; olaylar gerçek yük ON/OFF etiketi olarak kullanılmayacak.
- Katsayı değiştirilmedi; ESP32D1 K=24.22 korunuyor. ADS1115 katsayısı ve ±%4 kabul sonucu henüz belirlenmedi.
- Ayrıntı: [E19 üç modül karşılaştırma kaydı](logs/ads1115/2026-11-13-E19-three-module-100w-comparison.md).

## 2026-11-13 — E19 Aşama 1 ilk ADS1115 logu kaydedildi; Aşama 2 100 W katsayı testi açıldı

- ADS1115 I2C taramasında 0x48 bulundu; ESP32D2 GPIO21 SDA / GPIO22 SCL, 3.3 V ve ADDR-GND bağlantısı kullanıcı loguyla desteklendi.
- Önceki düşük hızlı A0-A1 denemesinde yüksüz 8–39 µV; yaklaşık 60 W yükte -12.8 mV ile +13.1 mV arasında değişen okumalar görüldü. Bu log 7 SPS ve yaklaşık 1 s yayın aralığındadır; RMS akım/katsayı ölçümü değildir. Seyrek örnekleme aliasing görünümü oluşturabilir.
- Mevcut ESP32D1 logunda ham ct_clamp 0.13757–0.13954 A, K uygulanmış çıktı 3.332–3.380 A; loglanan hız 6.700–6.920 SPS. Aynı zamanlı PZEM bu kesitte yoktur; 3.35 A gerçek akım diye kabul edilmedi.
- Yeni ESP32D2 ADS1115 + ct_clamp YAML depoya eklendi: 860 SPS, A0_A1, gain 2.048, continuous mode, 200 ms pencere, 2 s güncelleme. Derleme ve yeni YAML ile fiziksel çalışma henüz doğrulanmadı.
- **Aşama 2 açıldı:** 100 W akkor sabit yükte ESP32D1 + ESP32D2 + PZEM ortak kararlı alan karşılaştırması. Amaç ADS1115 katsayısını PZEM referansıyla belirlemek; mevcut D1 K=24.22 değiştirilmez.
- **Durum:** Aşama 1 LOG İLE DESTEKLENDİ; Aşama 2 PLANLANDI. 100 W ölçümü, katsayı ve ±%4 sonucu yok.
- Kayıtlar: [E19 README](experiments/E19-ads1115-low-current-alternative/README.md), [sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md), [ilk log](logs/ads1115/2026-11-13-E19-ads1115-first-bringup.md), [YAML](firmware/experiments/esp32d2-ads1115-ct-clamp.yaml).

## 2026-11-09 — E19 için ESPHome ADS1115 + ct_clamp mimarisi kaynak koduyla doğrulandı

- ESPHome 2026.10.2 resmi dokümanı ADS1115 gerilim sensörünün ct_clamp kaynağı olarak kullanılabildiğini doğruluyor. ADS1115 hub'da `continuous_mode: true` özellikle ct_clamp için öneriliyor.
- Doğru YAML yapısı iki sensör platformudur: `platform: ads1115` (differential A0_A1, gain/sample_rate ve kaynak ID) → `platform: ct_clamp` (`sensor: kaynak_id`, sample_duration, update_interval ve kalibrasyon).
- Paylaşılan taslaktaki `sensor_id` alanı ve ADS1115'e ait `multiplexer/gain/ads1115_id` alanlarının ct_clamp altında tanımlanması düzeltilmelidir.
- `gain: 0.256` ±0.256 V tam ölçek aralığıdır; 16x harici analog yükseltme değildir. Diferansiyel okuma ortak-mod parazitini reddetmeye yardımcı olabilir; paraziti sıfırlamaz. AIN pinleri GND–VDD sınırları içinde kalmalıdır.
- `update_interval: 2s` ile `sample_duration: 200ms` iki ayrı parametredir: her 2 saniyelik çevrimde 200 ms örnek penceresi alınır; bu kesintisiz 2 saniyelik kayıt değildir.
- ESPHome 2026.10.2 C++ kaynak kodu incelendi: ct_clamp örnekleme sırasında yüksek frekanslı loop kullanır, tekrar eden aynı ADC değerlerini atlar, kare toplamı/ortalama ile pencere sonunda RMS hesaplar. İşlemci yükü optimize edilmiştir fakat sıfır değildir.
- Kalibrasyon örnek noktaları (0.1 → 0.4) deneysel değer değildir; gerçek yük ve PZEM karşılaştırmasıyla çıkarılacak.
- **Durum:** Kaynak kod/dokümantasyon incelemesi tamamlandı; YAML henüz gerçek ESP32/ADS1115 donanımında derlenmedi veya ölçülmedi. Bias'sız bağlantı kart incelemesi ve güvenli giriş kontrolü bekliyor.
- Ayrıntı: [E19 deney notu](experiments/E19-ads1115-low-current-alternative/README.md) ve [protokol](experiments/E19-ads1115-low-current-alternative/protocol.md).

## 2026-11-09 — E19 ADS1115 düşük akım alternatifi planlandı

- Kullanıcı bir adet ADS1115 kartı sipariş ettiğini bildirdi; yaklaşık bütçe 250 TL.
- Hedef: mevcut SCT-013 + bias + ESP32 ADC yolunu değiştirmeden, SCT-013 30A/1V + ADS1115 alternatifini özellikle 0,5 A altında denemek.
- Mevcut ölçüm yolu referans olarak korunacak; aynı yük/hat koşullarında PZEM karşılaştırma referansı olacak.
- Harici bias olmadan çalışma araştırılacak; ADS1115 kartının gerçek giriş devresi, AIN pin sınırları ve common-mode yolu doğrulanmadan doğrudan bağlantı yapılmayacak.
- İlk koşulda tur sayısı sabit tutulacak; PGA, veri hızı, RMS penceresi ve single-ended/differential seçenekleri kontrollü değişkenler olarak ayrı incelenecek.
- Kullanıcının hedefi hafta sonu ilk denemeleri yapmak; kesin deney tarihi teslimat ve güvenli hazırlığa bağlı.
- **Durum:** PLANLANDI. Kart henüz teslim alınmadı; fiziksel bağlantı, kod, derleme, ölçüm ve log yok. ±%4 başarı veya bias'sız çalışma sonucu iddia edilmiyor.
- Kayıt: [E19 README](experiments/E19-ads1115-low-current-alternative/README.md), [protokol](experiments/E19-ads1115-low-current-alternative/protocol.md), [sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md).

## 2026-11-07 — Ölçülebilir alan başlangıcı 78 W olarak kabul edildi (LOAD-78W-001)

- Kullanıcı kararı: mevcut CH1 kurulumunda ölçülebilir alanın başlangıcı 78 W'tır; bu noktadan itibaren sayısal akım değeri verilecek.
- Düzenek: 57 W + 18 W akkor ampul, sürekli açık; PZEM aktif güç kullanıcı bildirimi 78,10 W.
- Paylaşılan HA ekranının son değerleri: PZEM 0,341 A, CH1 0,366 A, ham SCT 0,01512 A. Anlık ekran değerleri arasındaki fark yaklaşık %7,33; ±%4 doğrulaması değildir.
- 78 W için CSV ve kararlı pencere istatistiği yoktur; bu nedenle karar mevcut sabit yük gözlemleri ve ekran kanıtıyla sınırlıdır.
- 18 W ve 57 W hesaplanmadı karakteristiği korunur; 100 W kısa CSV güçlü karşılaştırma kaydıdır.
- K=24.22/firmware değiştirilmedi. Ayrıntı: [LOAD-78W-001](test-loads/78w-mixed-incandescent/README.md).

## 2026-11-07 — E17 sürekli düşük yük gözlemleri: 18 W ve 57 W

- E17-A 18 W sürekli açık oturumunun 10:30–12:00 (+03:00) CSV bölümü analiz edildi: PZEM ortalama 0,07824 A / 17,635 W; CH1 5.401 örnek, ortalama 0,30571 A, SD 0,04477 A, CV %14,64, P95 0,36962 A, maksimum 1,29129 A.
- E17-B 57 W sürekli açık oturumu 13:00–14:10 (+03:00) analiz edildi: PZEM ortalama 0,26307 A / 59,8405 W; CH1 4.201 örnek, ortalama 0,35550 A, SD 0,01786 A, CV %5,02, P95 0,38632 A, maksimum 0,49263 A.
- 57 W oturumunda CH1 dağılımı 18 W'a göre daha dar; büyük sıçramalar daha azdır. Bu iki oturumun gözlemsel karşılaştırmasıdır, nedensellik kanıtı değildir.
- Her iki CH1 ortalaması 0,24–0,41 A hesaplanmadı alanındadır; akım doğruluğu/kalibrasyon sonucu çıkarılmaz.
- Test yükü kayıtları: [18 W](test-loads/18w-incandescent/README.md), [57 W](test-loads/57w-incandescent/README.md). Deney kaydı: [E17](experiments/E17-low-current-continuous-load-observation/README.md).

## 2026-11-05 — BERO kapsamı ve hazırlık ortamı / canlı sistem ayrımı

Kullanıcı açıklaması ve kapsam kararı:
- BERO tek bir akım ölçer değil, farklı fiziksel değişkenleri izleyen sensörlerden oluşması hedeflenen çoklu sensörlü ev gözlem sistemidir.
- Akım sensörü bu bütünün yalnızca bir bileşenidir. Uygun sensör ve ölçüm ön ucuyla AC akımın yanında DC akım ölçümü de hedeflenebilir.
- Kullanıcının belirttiği sensör örnekleri: su kuyusunda sıcaklık değişim sensörü; kuyu basıncından su seviyesini/su derinliğini çıkaran basınç sensörü; ev girişinde şehir şebekesi su basıncını ölçen sensör.
- SCT013-PZEM akım ölçümünden başlanmasının nedeni BERO'nun akımla sınırlı olması değil; akımı güvenilir ölçmek, canlı okumak ve başka program/algoritma çıktılarıyla ilişkilendirmek teknik olarak zor bir başlangıç problemi olmasıdır.
- Mevcut SCT013-PZEM çalışması diğer evde yürütülen hazırlık/geliştirme çalışmasıdır.
- Şu anda canlı BERO sisteminde çoklu sensörlerle yürüyen entegre bir uygulama yoktur. Depodaki sensör ailesi ve çoklu sensör mimarisi hedef kapsamı/gelecek yönünü anlatır; mevcut canlı kurulumun durumu olarak sunulamaz.
- Mevcut kısa vadeli iş, SCT akım ölçüm zincirini ve veri toplama/analiz altyapısını hazırlamaktır. Sensör entegrasyonları ileride ayrı ayrı doğrulanacaktır.

## 2026-11-05 — Temel ilke: ham verinin uzun süreli korunması ve geçmiş veriden yeniden bilgi üretimi

Kullanıcı kararı: BERO ham ölçümleri uzun süreli saklamalıdır. Ham veri yalnızca bugünkü analiz için değil, ileride geliştirilecek ve bugün henüz öngörülmeyen yöntemlerle yeniden incelenmek için de korunacaktır. Geçmiş ham veriden sonradan yeni özellikler, davranış örüntüleri, trendler, sınıflandırmalar ve bakım/anomali göstergeleri üretilebilir.

Uygulama ilkeleri:
- Ham kayıtlar değişmez biçimde korunur; filtreleme veya temizleme ham kaydın üzerine yazmaz.
- Filtrelenmiş, normalize edilmiş, etiketlenmiş ve özellik çıkarılmış veriler ayrı türetilmiş katmanlardır.
- Türetilmiş çıktıların dayandığı ham veri aralığı ile işlem/model sürümü izlenebilir olmalıdır.
- Yeni algoritmalar mümkün olduğunca geçmiş ham veri üzerinde de çalıştırılarak karşılaştırılır.
- Uzun dönemli saklama; zaman damgası, kaynak/kanal kimliği ve veri bütünlüğü korunarak tasarlanır.

BERO hobi/araştırma projesidir. Anomali uyarıları otomatik servis veya ekonomik işlem başlatmadığından farklı yöntem ve eşikler deneysel olarak denenebilir. Yanlış uyarılar yöntem sınırlarını anlamak için geri bildirimdir; ham veri kaybı ise gelecekteki analiz imkânını ortadan kaldırabilir.

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


## 2026-11-05 — E14 kısa tek-kanal 2 Hz denemesi kaydedildi

Kullanıcı kararı: 2026-11-06 akşamı, veri/donanım durumu uygunsa kısa bir deney yapılabilir. Modül 2 bu amaçla deney alanı olarak kullanılabilir; yalnız SCT1 (sarı/GPIO32, fiziksel 1 geçiş) okunarak yaklaşık 500 ms / 2 Hz yeni ölçüm sonucu hedeflenecek. İlk karşılaştırmada K=24.22 ve sample_duration=200 ms sabit tutulacak; gerçek çıktı aralığı HA timestamp'leriyle doğrulanacak.

Bu çalışma E14 olarak kaydedildi. Mevcut üç kanallı çalışan YAML korunacak; deney sürümü ayrı tutulacak ve gerekirse geri dönülebilecek. Firmware değişikliği, derleme veya OTA henüz yapılmadı. E14 kısa akşam oturumu adayıdır; Cumartesi uzun çalışma önceliğini değiştirmez. Deneyler arasında öncelik, kullanıcının o günkü veri ve donanım durumuna göre esnekçe belirlenebilir.

Ayrıntı: [E14 — Modül 2 tek SCT kanalında 2 Hz ölçüm denemesi](experiments/E14-module2-single-channel-2hz/README.md).


## 2026-11-06 — Tek kanallı SCT eğitim verisi kararı (ADR-027)

Kullanıcı kararı:
- Test ve veri toplama firmware'i üç SCT kanalını birlikte okuyabilir.
- Ham HA dışa aktarımı ve arşiv birden fazla SCT kanalının kayıtlarını koruyabilir.
- Her eğitim veri seti yalnızca tek bir SCT kanalından oluşur. CH1, CH2 ve CH3 ayrı veri setleri ve ayrı model değerlendirmeleri üretir.
- PZEM akımı proje referansıdır; seçilen kanalın SCT kararlı alanları mevcut BOOT_ID + EVENT_ID paket kuralları içinde PZEM kararlı alanlarıyla değerlendirilir.
- Kanal kimliği ve fiziksel geçiş/sarım bilgisi eğitim çıktısında izlenebilir olmalıdır.

Önerilen ortak kanal kimliği biçimi `CH1-1T`, `CH2-4T`, `CH3-3T` şeklindedir. Depodaki fiziksel eşleme (CH1 sarı/GPIO32 = 1 geçiş; CH2 yeşil/GPIO33 = 4 geçiş; CH3 mavi/GPIO34 = 3 geçiş) kod/entity adlarına uygulanmadan önce doğrulanmalıdır. Bu adlandırma standardı önerilmiştir; firmware veya HA entity adları henüz değiştirilmemiştir.

Ayrıntı: [ADR-027](docs/decisions/ADR-027-single-channel-training-datasets.md). T007/T008 veri hattı uygulaması ve gerçek eğitim çıktısı tamamlanmış değildir.


## 2026-11-06 — ADR-027 kanal kimliği / değişebilir geçiş sayısı netleştirmesi

Kullanıcı düzeltmesi: CH2 için kayıtlı 4 geçiş ve CH3 için kayıtlı 3 geçiş değerleri ileride değişebilir. Bu nedenle geçiş sayısı kalıcı kanal kimliğine eklenmeyecek.

- Kalıcı kanal kimliği yalnız `CH1`, `CH2`, `CH3` olacaktır.
- Fiziksel geçiş/sarım sayısı `turn_count` adıyla ayrı, değişebilir donanım/deney metadata'sı olarak tutulacaktır.
- Mevcut 1/4/3 geçiş bilgisi yalnız mevcut kayıtlı fiziksel durumu ifade eder; sabit özellik değildir.
- Yapılandırma değiştiğinde yeni kayıtlar yeni `turn_count` değerini taşır; eski eğitim/ham veriler toplandıkları zamanki değerle korunur.
- `CH1-1T`, `CH2-4T`, `CH3-3T` birleşik biçimleri kalıcı kanal kimliği olarak kullanılmayacaktır.

ADR-027 ve Python mimarisi bu ayrımla güncellendi. Firmware ve HA entity isimleri değiştirilmedi.


## 2026-11-06 — Eğitim verisi için History kanal adlandırması netleştirildi (ADR-027)

Kullanıcı kararı:
- Gün içindeki genel deneylerde ve gözlemde History kanal adları genel kalır: `CH1`, `CH2`, `CH3`. History'de çok sayıda deney kaydı bulunabilir; bunlar otomatik olarak eğitim verisi değildir.
- Kod/ölçüm yapılandırması kesinleştikten ve özellikle eğitim verisi toplanmasına karar verildikten sonra ilgili kodda küçük bir adlandırma değişikliği yapılır. Eğitim amaçlı akış adı `CH1-E`, `CH2-E` veya `CH3-E` olur.
- `-E` eki eğitim amacıyla yayınlanan History akışını işaretler; fiziksel kanal kimliğini, sarım sayısını veya hesaplama yöntemini tanımlamaz.
- Python-1 kaynak CSV'yi içerik/entity adlarını değiştirmeden arşivler; bu üç eğitim adının CSV'de bulunması Python-1'in genel dosya kabul koşulu değildir.
- Python-2/eğitim hazırlama aşaması `CH1-E`, `CH2-E`, `CH3-E` adlarını açık seçim anahtarları olarak kullanır. Genel `CH1` / `CH2` / `CH3` deney kayıtları kendiliğinden eğitim setine alınmaz.
- Eski bir deney kaydı sonradan eğitim için seçilirse kaynak arşiv değiştirilmez; kanal seçimi ve eğitim adı ayrı türetilmiş kopyada uygulanır.
- Sarım sayısı, katsayı ve hesaplama yöntemi gerektiğinde deney/eğitim kodunda tanımlanır; kanal adına eklenmez.

Bu karar ADR-027, Python mimarisi, T007, ROADMAP ve STATUS belgelerine işlendi. Firmware/HA entity kodu değiştirilmedi; gerçek eğitim kaydı henüz başlatılmadı.


## 2026-11-06 — E15 eğitim kanal adı / History doğrulama deneyi planlandı

Kullanıcı isteğiyle E15 oluşturuldu: günlük deney adları CH1/CH2/CH3 olarak kalırken, eğitim verisi alınmasına karar verildiğinde kodda küçük adlandırma değişikliği yapılarak CH1-E/CH2-E/CH3-E akışlarının Home Assistant History'de görünmesi ve CSV dışa aktarımında gerçek entity_id değerleriyle doğrulanması sınanacak.

- Deney dosyası: [E15 — Eğitim işaretli kanal adlarının Home Assistant History doğrulaması](experiments/E15-training-channel-history-naming/README.md).
- Yalnız adlandırma alanları değişecek; pin, ölçüm hesabı, K, sample_duration, update_interval, okuma sırası ve olay protokolü korunacak.
- Önce çalışan YAML ve Git SHA sabitlenecek; deney YAML ayrı dosyada hazırlanacak.
- Görünen ad ile gerçek entity_id ayrı ayrı kontrol edilecek; HA entity registry'nin eski entity_id'yi koruma ihtimali varsayılmayacak.
- Python ve eğitim veri üretimi bu deneyin kapsamı değildir.
- **Durum: PLANLANDI.** Kod değişikliği, derleme, OTA, History kaydı ve CSV doğrulaması yapılmadı.


## 2026-11-06 — ADR-028: Kararlı alan SCT ile kapanacak

Kullanıcı kararı:
- Kararlı alan, aynı ON paketi içinde SCT ve PZEM kendi akışlarında birlikte kararlı olduğunda açılır.
- Kararlı alan, SCT kendi akışında kararlılığını kaybettiğinde kapanır.
- PZEM kararlılığı yalnızca başlangıç koşuludur; bitiş tetikleyicisi değildir.
- Gerekçe: Yük OFF olduğunda PZEM akımı gecikmeli gösterebilir. SCT yük değişimini daha erken yakaladığı için PZEM'in OFF/kararsız görünmesi beklenmez.
- OFF olay işareti ON paket bütünlüğünü kapatma/doğrulama görevini sürdürür; kararlı alanın istatistiksel bitiş ölçütü değildir.

Karar [ADR-028](docs/decisions/ADR-028-stable-window-sct-boundaries.md) olarak kaydedildi ve [E12](experiments/E12-sct-stability-window-and-response/README.md) deney belgesine işlendi.

**Henüz belirlenmeyenler:** SCT kararlılık kaybının istatistiksel tanımı, pencere boyu, dağılım/ortalama değişimi sınırları ve devam süresi. Bunlar veriden belirlenecek; eşik uydurulmayacak.

**Uygulama durumu:** Python algoritması yazılmadı. Firmware/YAML değişikliği, derleme veya OTA yapılmadı. E12 devam ediyor; tamamlanmış değildir.


## 2026-11-06 — Python çalışma ortamı için taşınabilir SSD kararı (ADR-029)

Kullanıcı kararı:
- BERO Python-1 ve Python-2'nin kaynak kodları, çalışma paketleri/bağımlılıkları, yapılandırmaları, gelen-kutu, ham arşiv, işlenmiş veriler, eğitim çıktıları ve logları harici SSD üzerinde tutulacaktır.
- Hedef platformlar Microsoft Surface 11 (Snapdragon X Elite, Windows ARM64) ve Mac mini 2024 (Apple M4, macOS ARM64) olarak belirlendi.
- Windows ve macOS için ayrı platforma özgü başlatıcı/çalıştırma paketleri hazırlanacak; ortak Python kaynak kodu ve veri yapısı korunacaktır.
- Programlar sabit sürücü harfine veya bilgisayara özgü mutlak yola bağımlı olmayacak; SSD köküne göre göreli yollar kullanacaktır.
- SSD üzerinde işlem belirgin performans kaybı yaratırsa geçici veriler RAM'de veya bilgisayarın yerel geçici alanında işlenebilir. Kalıcı sonuçlar ve kayıtlar SSD'ye yazılır; yerel geçici alan kalıcı depo değildir.

**Açık teknik kararlar:** SSD dosya sistemi, runtime/bağımlılık paketleme yöntemi, başlatıcı biçimi, çevrimdışı ilk kurulum ve geçici alan politikası henüz belirlenmedi.

Karar [ADR-029](docs/decisions/ADR-029-portable-ssd-python-runtime.md) ve [Python veri hattı mimarisi](docs/architecture/python-program-architecture.md) ile [T007](tasks/T007-python-architecture.md) belgelerine işlendi.

**Uygulama durumu:** Yalnız mimari karar kaydedildi. SSD klasörleri, Python paketleri ve Windows/macOS çalıştırma testleri henüz oluşturulmadı. T007 devam ediyor.


## 2026-11-06 — Küçük Python görevleri ve kesinti sonrası güvenli devam kararı (ADR-030)

Kullanıcı kararı: Python hattı tek ve uzun çalışan bir programa dönüşmemeli. Küçük, bağımsız görev Python'ları kullanılmalı; bir görev kilitlendiğinde veya hata verdiğinde sistemin geri kalanı durmamalı ve daha önce işlenen veri/çıktı kaybolmamalıdır.

Karar ilkeleri:
- Her görev tek sorumluluklu, açık girdili/çıktılı ve yeniden başlatılabilir olur.
- RAW kaynaklar değişmez korunur.
- Başarılı görev adımları ve checkpoint bilgileri SSD'de tutulur; yeniden çalıştırma son güvenli noktadan devam eder.
- Yarım çıktı tamamlanmış sonuç olarak yayımlanmaz; çıktı doğrulandıktan sonra nihai konuma alınır.
- Girdi hash'i, görev/sürüm, durum, çıktı ve hata bilgisi işlem kaydına yazılır.
- Aynı girdi yeniden işlendiğinde yinelenen çıktı/arşiv oluşturulmaz.
- Tek dosyanın veya görevin hatası diğer bağımsız işleri durdurmaz.

Karar [ADR-030](docs/decisions/ADR-030-resumable-small-python-jobs.md), [Python mimarisi](docs/architecture/python-program-architecture.md) ve [T007](tasks/T007-python-architecture.md) belgelerine işlendi.

**Uygulama durumu:** Yalnız mimari karar kaydedildi. Görev çalıştırıcı, checkpoint, atomik çıktı ve kurtarma mekanizması henüz uygulanmadı/test edilmedi. T007 devam ediyor.


## 2026-11-06 — Python programları ve alt görevleri taslaklandı

Kullanıcı isteğiyle Python kodlamasına geçmeden önce program envanteri açıldı. Mevcut iki ana program sınırı taslak olarak korundu:
- PY-01 — BERO Importer: gelen-kutu dosyalarının güvenli kabulü, hash/tekrar kontrolü, CSV doğrulama, RAW arşiv ve karantina.
- PY-02 — BERO Analyzer: arşiv envanteri, veri profili, olay paket doğrulama, ayrı PZEM/SCT kararlılık analizi, örtüşme, tek kanallı etiketleme, tam kayıt değerlendirmesi ve raporlama.

Her ana program küçük görev modüllerine ayrıldı. Program tanımları ve görev listeleri taslak durumundadır; kullanıcıyla okunup kontrol edilecek, gerekirse değiştirilecektir. Kodlama veya algoritma doğrulaması yapılmadı.

- [Python program envanteri](docs/python-programs/README.md)
- [PY-01 — BERO Importer](docs/python-programs/PY-01-importer.md)
- [PY-02 — BERO Analyzer](docs/python-programs/PY-02-analyzer.md)

**Sonraki çalışma:** Envanter ve PY-01/PY-02 tanımları kullanıcıyla sırayla gözden geçirilecek. Görev sınırları onaylanmadan kodlamaya başlanmayacak.


## 2026-11-06 — PY-01 arşiv/oturum tasarımı örnekle sabitlenecek

Kullanıcı kararı ve çalışma yöntemi:
- PY-01 ilk aşamada kullanıcı tarafından başlatılacak; gelen-kutusunu bir kez tarayıp bulunan dosyaları işleyecek ve tamamlanınca kapanacak. Sürekli izleme ilk sürüm kapsamında değildir; veri doğrudan bu çalışma alanında oluşursa ileride yeniden değerlendirilebilir.
- Arşiv klasörlemesi (tarih/oturum/hash) ve deney/oturum bilgisinin program ekranında nasıl seçileceği veya manifestte nasıl tutulacağı henüz kesinleştirilmedi.
- Bu tasarım soyut anlatımla sabitlenmeyecek. Yarın çalışan bir örnek/prototip hazırlanıp gerçek CSV akışı üzerinde denenecek; kullanıcı örneği görüp deneyerek uygun yapıyı belirledikten sonra karar depoda sabitlenecek.
- Örnekle deneme yapılmadan arşiv klasör yapısı, oturum alanları veya manifest biçimi hakkında nihai karar alınmayacak.

PY-01 taslağı kullanıcı incelemesinde kalır. Kodlama ve gerçek dosya testi henüz yapılmadı.


## 2026-11-06 — Gün sonu: eğitim yaklaşımı netleşti, yarın SCT/PZEM eğitim verisi sabitleme

Kullanıcının gün sonu değerlendirmesi:
- Genel akım okuma aşamasında sistemden SCT verisi alınabiliyor; eğitim için kullanılabilecek kararlılıkta alanları belirleme hedefi tanımlı. Kararlılık algoritmasının sayısal ölçütleri ve uygulaması henüz tamamlanmış değildir.
- Kullanıcı, eğitim felsefesinin ve ne tür veri istendiğinin bugün paylaşılan ekran görüntüsüyle de sabitlendiğini belirtti. Bu kayıt, ekran görüntüsünün içeriğine dair yeni teknik ayrıntı üretmez; kullanıcı teyidini gün sonu ilerleme notu olarak kaydeder.
- Yarınki ilk çalışma: eğitim amacıyla kullanılacak SCT ve PZEM verilerinin seçilmesi/sabitlenmesi. Öncelik, uygun kararlı alanların gerçek veride belirlenmesi ve eğitim için kullanılacak veri kapsamının netleştirilmesidir.
- PY-01 taslağı kullanıcı incelemesinde kalır; arşiv/oturum tasarımı yarın örnek/prototip üzerinden denenerek kararlaştırılacaktır.

**Durum sınırı:** Bu oturumda yeni SCT/PZEM CSV analizi, Python algoritması, eğitim etiketi/modeli, firmware/YAML değişikliği, derleme veya OTA yapılmadı. Eğitim verisi henüz üretilmiş/sabitlenmiş değildir. T007 → T008 → T006 görev sırası korunur.


## 2026-11-06 — E16 planlandı: yüksüz/düşük akım ON/OFF davranışı

- Kullanıcının HA ekran görüntüsünde PZEM 230,2 V / 0,000 A; Modül 2 CH1-1T akım göstergesi 0,204 A ve Raw AC göstergesi 0,00842 olarak görünüyordu (Raw AC birimi ekran görüntüsünden kesinleştirilmedi). SCT grafiğinde yaklaşık 0,18–0,30 A çevresinde basamaklı seviye ve tekil sıçramalar vardı. Bunlar tek ekran gözlemidir, deney sonucu değildir.
- Kullanıcı, 18 W yükte SCT'nin akım genliğini doğru okumaktan ziyade ON/OFF değişimini algılıyor olabileceğini bildirdi. Bu ayrı ve henüz doğrulanmamış hipotezdir.
- [E16](experiments/E16-sct-on-off-response-idle-low-current/README.md) açıldı. Gece boyunca PZEM V/A, SCT CH1 akım/Raw AC ve Modül 3 gönderim + Modül 2 alım olayları HA History'de kaydedilecek; sabah CSV dışa aktarılıp analiz edilecek.
- Fiziksel yük koşulu ayrıca not edilecek; PZEM 0,000 A tek başına fiziksel yüksüzlüğün kanıtı kabul edilmeyecek. 18 W koşulu bu geceki yüksüz kayıtla karıştırılmayacak.
- Firmware/K/sample_duration/update_interval/pin ve olay döngüsünde değişiklik yapılması planlanmıyor. Eğitim etiketi veya katsayı üretilmeyecek.
- **Durum:** PLANLANDI; gece kaydı ve CSV henüz alınmadı, analiz yapılmadı.


## 2026-11-07 — CH1 kapalı alan eşiği belirlendi (ADR-031)

- Kullanıcının sağladığı HA History kaydında fiziksel olarak akım bulunmayan hatta yaklaşık 10 saatlik CH1 verisi incelendi: 36.002 CH1 akım ve 36.002 CH1 ham SCT örneği.
- K=24.22 uygulanmış akım P95 değeri 0,23587365 A; ham SCT P95 değeri 0,00973880.
- Kullanıcı kararı: **CH1 kapalı alan üst sınırı 0,24 A**. Bu eşikte örneklerin %96,33'ü 0,24 A veya altında; %3,67'si üzerindedir. Sıçramalar temizlenmedi ve karar için ayrıca filtrelenmedi.
- Ham CSV depoya eklenmedi; kullanıcı isteği doğrultusunda yalnızca istatistiksel dayanak kaydedildi.
- Yeni alan ayrımı: 0–0,24 A kapalı; 0,24 A ile ilk güvenilir akım okuması arası hesaplanmadı; ilk güvenilir okuma ve üzeri hesaplanacak.
- İlk güvenilir akım okumasının sayısal sınırı henüz belirlenmedi. Sonraki deneylerin hedefi bu sınırı kontrollü yüklerle bulmaktır.
- Bu eşik CH1 ve bu yüksüz kayıt koşuluna özgüdür; CH2/CH3'e genellenmez. E16 ON/OFF gözlemi ayrı kalır.
- I007 çoklu oturum gürültü karakterizasyonu bu ilk karar için ön koşul olmaktan çıkarıldı; ileride oturumlar arası değişimi incelemek için sürdürülebilir.
- Ayrıntı: [I007 özet](data/off-noise/sessions/2026-11-07-ch1-closed-area-threshold.md), [ADR-031](docs/decisions/ADR-031-ch1-idle-closed-area-threshold.md).


## 2026-11-07 — E17 18 W sürekli yük gözlemi açıldı

- Kullanıcı 18 W akkor ampul deneyini 10:21'de başlattı (Europe/Istanbul). Ampul deney boyunca sürekli yanıyor; röle devrede değil ve röle anahtarlama etkisi bulunmuyor.
- 10:14 civarındaki grafikteki hareket PZEM'i devreye alma/bağlantı denemeleriyle ilişkili hazırlık dönemi olarak ayrıldı; deney başlangıcı kabul edilmedi.
- İlk HA ekran gözleminde PZEM 227,1 V / 0,078 A; CH1 akım entity'si yaklaşık 0,277 A ve ham SCT entity'si 0,01145 A gösteriyordu. CH1 eğrisi 10:21 sonrasında yaklaşık 0,28–0,30 A çevresinde görünüyor.
- Kullanıcı kararı: CH1'in 0,24–0,41 A hesaplanmadı alanında fiziksel tepki görülse bile sayısal akım değeri kabul edilmeyecek/üretilmeyecek. Bölge ileride farklı sensörle ele alınabilir.
- 18 W kaydı sürüyor; ekran görüntüsü ilk gözlemdir, kararlılık/tekrar edilebilirlik sonucu değildir. CSV analizi bekleniyor.
- Sonraki ayrı deney adayı: 15 W mini buzdolabı ampulü sürekli açık kayıt. Kullanıcı bu ampulün farklı tepki verdiğini bildirdi; bu henüz yeni kayıtla doğrulanmış sonuç değildir.
- Ayrıntı: [E17 protokolü ve ilk gözlem](experiments/E17-low-current-continuous-load-observation/README.md).

**Durum sınırı:** E17-A AÇIK; E17-B BAŞLATILMADI. Firmware, YAML, K katsayısı veya eşik değiştirilmedi. Kalibrasyon/eğitim etiketi üretilmedi.



## 2026-11-07 — E17-A 18 W kaydında ek ekran gözlemi

- Sonraki HA History ekranında PZEM 226,2 V / 0,078 A; güç yaklaşık 17,5–17,8 W; CH1 akım 0,325 A; ham SCT 0,01341 A olarak görünüyor.
- CH1 eğrisi yük devredeyken yaklaşık 0,28–0,33 A bandında; tekil tepe değerleri yaklaşık 0,5 A'ya yaklaşıyor. Yaklaşık grafik gözlemidir, CSV istatistiği değildir.
- CH1 0,325 A değeri 0,24–0,41 A hesaplanmadı alanındadır. Tepki, doğru genlik ölçümü olarak yorumlanmayacak.
- E17-A kaydı sürüyor; nihai sonuç için CSV analizi bekleniyor. [E17](experiments/E17-low-current-continuous-load-observation/README.md).


## 2026-11-07 — E17-A SSR arka plan olaylarının ayrıştırılması

- Arka planda SSR ON/OFF döngüsü vardır; SSR, 18 W ampulün ve PZEM/SCT tarafından gözlenen ölçüm hattının anahtarlayıcısı değildir.
- Ampul sürekli yanık kalır. SSR olayları veri kaydında ayrı olay akışı olarak korunur ancak ölçüm hattının yük ON/OFF etiketi olarak kullanılmaz.
- CH1 sıçramalarının SSR olaylarıyla zaman çakışması tek başına nedensellik göstermez. Ayrıntı: [E17](experiments/E17-low-current-continuous-load-observation/README.md).



## 2026-11-07 — E17-A amacı netleştirildi: SSR anahtarlama etkisini ayır

- E17-A'nın amacı SSR anahtarlamasının SCT üzerindeki etkisini incelemek değil, sürekli bağlı 18 W yükün davranışını bu etkiden mümkün olduğunca bağımsız gözlemlemektir.
- Kullanıcı, önceki gün SSR anahtarlamasının CH1 sinyalini etkilediğini ve anahtarlama sırasında sinyalin normal kapalı alan seviyesinin de altına düşebildiğini bildirdi. Grafikte yaklaşık 10:19'daki belirgin düşüş bu etkiyle ilişkilendirildi; zaman eşleşmesi CSV ile doğrulanacaktır.
- SSR, 18 W ampulün ölçüm hattına bağlı değildir; ampul sürekli yanar. SSR ON/OFF olayları ayrı metadata olarak tutulur; yük durumu etiketi yapılmaz. Anahtarlama geçişleriyle ilişkili CH1 düşüşleri sürekli yükün kararlı seviyesi/kapalı tabanı sayılmaz.
- Ayrıntı: [E17](experiments/E17-low-current-continuous-load-observation/README.md).



## 2026-11-07 — E17-A CSV analizi için PZEM/SCT pik korelasyonu planlandı

- CSV geldiğinde CH1 ham SCT ve hesaplanmış akım pikleri; PZEM gerilim, akım, aktif güç, PF ve frekans serileriyle zaman ekseninde karşılaştırılacak.
- Gerçek kolonlar, birimler, timestamp ve her serinin güncelleme/örnekleme aralığı doğrulanacak. Piklerin öncesi-sırası-sonrası, tepe genliği, aralıkları, eşzamanlılık ve olası gecikme incelenecek.
- SSR olayları ayrı metadata olarak kalacak; ölçüm hattının yük durumu etiketi yapılmayacak. Anahtarlama zamanları olası etki pencerelerini ayırmak için kullanılabilir.
- Korelasyon nedensellik sayılmayacak; PZEM çözünürlüğü/güncelleme hızı yetersizse sonuç “ayırt edilemedi” olarak raporlanacak. CSV henüz gelmedi; analiz yapılmadı. [E17](experiments/E17-low-current-continuous-load-observation/README.md).


## 2026-11-07 — E17 korelasyonunda PZEM/SCT zaman çözünürlüğü ayrımı

- Kullanıcı, PZEM akımının paket/okuma döngüsüyle daha seyrek; SCT verisinin daha sık yenilendiğini belirtti. Analiz bu asenkron güncelleme yapısını dikkate alacak.
- PZEM'de aynı değerin birden fazla SCT örneği boyunca görünmesi, her SCT pikinde yeni PZEM ölçümü yapıldığı anlamına gelmez. Timestamp ve gerçek güncelleme aralıkları ayrı çıkarılacak.
- SCT pikleri PZEM güncellemeleri arasında ise bire bir anlık eşleştirme yapılmayacak; son yayınlanan PZEM değeri ile yeni PZEM ölçümünü birbirinden ayıracağız. Aradaki PZEM ölçümleri interpolasyonla uydurulmayacak.
- Veri çözünürlüğü hızlı pik korelasyonuna yetmiyorsa bu sınırlılık sonuçta açıkça belirtilecek. Ayrıntı: [E17](experiments/E17-low-current-continuous-load-observation/README.md).


## 2026-11-07 — E18 CH1 bias hattı kontrol deneyi planlandı

- Kullanıcı, E17 düşük akım ampul deneylerinden ayrı olarak CH1 SCT sensörünü çıkarmayı ve uzun kayıt almayı önerdi.
- Bağlantı yöntemi netleştirildi: CH1 SCT çıkarılacak; CH1 ölçüm noktası boşta bırakılmayacak, ortak bias okuyan hatta bağlanacak.
- Amaç, SCT sinyali olmadan CH1 ölçüm zincirinin sıçrama üretip üretmediğini gözlemek. Bu deney ESP ADC arızasını tek başına kanıtlamaz; bias hattı, bağlantı, ortak parazit ve yazılım etkileri de değerlendirme kapsamındadır.
- Firmware/YAML, K, sample_duration, update_interval ve diğer kanallar değiştirilmeden uzun Home Assistant History kaydı alınacak. Ortak bias ve varsa CH2/CH3 kontrol serileri korunacak.
- Fiziksel bağlantı ve kayıt henüz yapılmadı; deney **PLANLANDI** durumundadır. [E18 protokolü](experiments/E18-ch1-bias-line-control/README.md).


## 2026-11-07 — BERO kalıcı haberleşme omurgası: RS485 (ADR-001)

Kullanıcı kararı:
- BERO'nun kalıcı haberleşme omurgası RS485 olacaktır.
- ESP tabanlı düğümler ölçüm/veri kayıtlarını RS485 üzerinden bölgesel düğümlere aktaracaktır.
- Wi-Fi şimdilik geçici haberleşme/aktarım yoludur; kalıcı omurga değildir.
- PZEM-014 AC RS485 Modbus Güç Tüketim Ölçer + USB henüz hiç kullanılmamıştır; RS485/Modbus RTU okuma çalışması ve ekranlı ESP'lerin canlı gösterimi sonraki uygulama adımlarıdır.
- Modbus RTU cihaz okuma protokolü ile BERO düğümleri arası mesajlaşma protokolü birbirine karıştırılmayacaktır.

Bu kayıt mimari kararıdır. RS485 bağlantısı, düğümler arası aktarım, PZEM-014 okuması ve ekranlar henüz fiziksel olarak devreye alınmamış/doğrulanmamıştır. Topoloji, adresleme, mesaj çerçevesi, baud hızı ve transceiver seçimi açık bırakılmıştır.

Ayrıntı: [MIMARI/DECISIONS/ADR-001](../../MIMARI/DECISIONS/ADR-001-rs485-communication-backbone.md).


## 2026-11-07 — RS485 omurga kablo yaklaşımı netleştirildi

Kullanıcı tarafından belirlenen fiziksel yaklaşım:
- RS485 A/B haberleşmesi CAT kablo üzerinden taşınacak.
- RS485 A/B hattının yanında 24 V DC ana besleme aynı CAT kabloyla bölgesel düğüme taşınacak; düğüm noktasında DC-DC dönüştürücüyle 5 V'a indirilecek.
- Bu BERO kablosu, mevcut Ethernet kablosundan dış kılıf rengiyle ayırt edilecek.

Kesin CAT tipi ve damar/pair tahsisi, 24 V DC ana beslemenin kapasitesi, düğüm akımı, kablo mesafesi/gerilim düşümü, 5 V dönüştürücü, sigorta/koruma ve referans-topraklama ayrıntıları henüz hesaplanmadı. Kablo uçları Ethernet/LAN portlarına bağlanmamalı; farklı renk tek başına yeterli güvenlik önlemi sayılmayıp uçlar da etiketlenmelidir.

Bu kayıt kablolama yaklaşımını belgeliyor; gerçek kablo kurulumu veya elektriksel doğrulama yapıldığı anlamına gelmez. [ADR-001](../../MIMARI/DECISIONS/ADR-001-rs485-communication-backbone.md).


## 2026-11-07 — E16, E17 ve E18 kapatıldı; odak Python ve yük davranışı eğitimine geçti

Kullanıcı kararları:
- **E16 KAPATILDI:** CH1 alt sınırı ve bunun altındaki ölü/hesaplanmayan bölge belirlendi. Aynı düşük akım alanında ON/OFF gözlemini tekrar etmek artık yeni karar üretmeyecek.
- **E17 KAPATILDI:** E17-A 18 W ve E17-B 57 W kayıtları analiz edildi. E17-C 15 W mini buzdolabı ampulü deneyi aynı gerekçeyle tekrarlı/anlamsız bulundu ve yapılmadan kapatıldı.
- **E18 KAPATILDI:** Kullanıcı gözlemine göre bias hattı üzerinden CH1, tekil sıçramalar dışında stabil. Dalgalanmanın ana kaynağı bias hattı olarak değerlendirilmiyor; kalan alt akım davranışı sensörün ölçüm alt sınırı/ölü bölgesi kapsamında ele alınacak. Bu, sıçramaların fiziksel nedeninin kesin teşhisi değildir.

### Yeni çalışma odağı

Öncelik artık **Python veri hattı ve eğitim/analiz aşamasıdır**:
1. T007 — Home Assistant History verisini PC'ye alma, doğrulama ve değişmez ham arşiv.
2. T008 — SCT/PZEM akışlarını olay paketleriyle bölümleme, bağımsız kararlı alan analizi ve etiketleme.
3. Eğitim/analiz araştırması — çamaşır makinesi gibi programlı cihazların gerçek yük bileşenleri ve evreleri (rezistans, motor, pompa, valf vb.) hangi akım davranışlarını üretir; bu davranışlar SCT verisinde birbirinden ayrılabilir mi?
4. SCT uygunluk değerlendirmesi — gözlem, güç/akım genliği ve geçiş tepkisi kabiliyetlerini ayrı ayrı incele. Özellikle 2 A altındaki performansın hangi aralıkta güvenilir olduğu henüz kanıtlanmış değildir; eğitim verisiyle araştırılacaktır.

**Kapsam notu:** SCT'nin düşük akımda sayısal ölçüm doğruluğu ile cihaz/program evresi sınıflandırmasına yetecek davranış bilgisini taşıması farklı sorulardır. Birincisindeki sınırlılık ikincisini otomatik olarak başarısız kılmaz; sınıflandırma başarısı da ölçüm doğruluğunu kanıtlamaz. Sonuçlar gerçek veri analiziyle verilecektir. Bu aşamada 2 A altında SCT yeterlidir/yetersizdir hükmü verilmemiştir.

## 2026-11-09 — E19'a yaklaşık 2 A ikincil doğrulama hedefi eklendi

Kullanıcı kararı/fikri: ADS1115 alternatifi düşük akım denemesinde başarılı olursa, uygun deneysel kalibrasyon katsayısıyla yaklaşık 2 A civarında da kullanılabilirliği araştırılacak.

- Bu hedef, E19'un 0,5 A altı ana hedefini değiştirmez; ikincil doğrulama bölgesidir.
- Kalibrasyon katsayısı önceden belirlenmeyecek. SCT gerçek çıkışı, ADS1115 ham/ct_clamp verisi ve aynı kararlı yük koşulundaki PZEM referansı kullanılarak çıkarılacak.
- Yaklaşık 2 A'da gain/headroom, clipping, kararlılık, tekrar edilebilirlik ve PZEM'e göre sapma kontrol edilecek.
- Düşük akım ve 2 A bölgesinde tek katsayının yeterli olduğu varsayılmayacak; aralıklar arası doğrusal davranış ayrıca incelenecek.
- **Durum:** Fikir ve test hedefi kaydedildi. ADS1115 kartı henüz teslim/deney aşamasında; 2 A performansı ve katsayı doğrulanmış değildir.
- Ayrıntı: [E19 README](experiments/E19-ads1115-low-current-alternative/README.md), [protokol](experiments/E19-ads1115-low-current-alternative/protocol.md), [sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md).

## 2026-11-09 — E19 sonrası aday mimari: aynı ESP'de çift ölçüm yolu

Kullanıcı, ADS1115 başarılı olursa aynı ESP üzerinde iki ölçüm yolunun kullanılabileceği bir yapı tarif etti:
- Mevcut ESP32 dahili ADC + bias yolu normal/yüksek akım ölçümünü izler.
- I²C ADS1115 aynı SCT kanalını ikinci yoldan ölçer.
- Yaklaşık 1 A altındaki bölgede yazılım ADS1115 sonucunu; eşik üstünde mevcut ESP32 ADC sonucunu kullanır.
- Yaklaşık 2 A çevresi ADS1115 için ayrıca doğrulanacak; tek katsayı varsayılmayacak.

Bu, şu aşamada **aday yazılımsal aralık seçimi mimarisidir**; fiziksel analog anahtarlama kararı değildir. Eşik 1 A olarak önerilmiştir ancak henüz doğrulanmamıştır. Eşik çevresinde histerezis, zamanlama/ölçüm penceresi uyumu ve yol değişiminde süreksizlik testleri gereklidir.

**Elektriksel ön koşul:** SCT sinyalini ESP32 ADC bias ağı ve ADS1115 girişine aynı anda vermeden önce iki analog ön ucun giriş empedansı, bias/common-mode, koruma ve gerilim sınırları incelenecek. Paralel bağlantı otomatik olarak güvenli kabul edilmeyecek; gerekirse tamponlama/ayırma veya analog anahtarlama çözülecek.

**Durum:** Yalnızca fikir ve sonraki mimari adım kaydedildi. Kart teslimi, bağlantı, firmware, derleme ve ölçüm doğrulaması bekleniyor. Ayrıntılar E19 README ve protokolüne eklendi.
