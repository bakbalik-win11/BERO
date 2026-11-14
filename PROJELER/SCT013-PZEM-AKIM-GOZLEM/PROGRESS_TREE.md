## 2026-11-14 — E24 üç ADS1115 / tek ESP32 / altı SCT test planı güncellendi
- Kullanıcı bildirimi: mevcut iki ADS1115'ten biri çalışıyor, biri arızalı; yeni siparişlerin teslimi bekleniyor.
- Güncel test hedefi doğrudan **1 ESP32 + 3 ADS1115 + 6 SCT**; önceki iki ADS/dört SCT ara test planı güncellendi.
- Her ADS için ayrı SDA/SCL çifti tercih ediliyor. Klasik ESP32'de iki donanımsal I²C kontrolcüsü bulunduğundan üçüncü hattın yazılımsal I²C ile sağlanması kart/framework/ESPHome üzerinde gerçek derleme ve cihaz testiyle kanıtlanmalı.
- Test: üç ADS'yi tek tek doğrula → üç bus'ı birlikte doğrula → altı kanalı güvenli DC ile test et → analog giriş güvenliği doğrulanırsa SCT'lere geç → kanal hızı, tam çevrim, gecikme/jitter, hata/timeout ve kayıp örnekleri izle.
- İlk testte RS485 yok; ikinci altı kanallı düğüm ve 12 SCT, ilk düğüm doğrulanınca ele alınacak.
- [E24 protokolü](experiments/E24-ads1115-multi-bus-expansion/README.md).

## 2026-11-14 — E24 test basamağı ve 6 SCT tek ESP hedefi netleştirildi
- Nihai hedef: **tek ESP32 üzerinde 6 SCT kanalı** (3 ADS1115 planı; üçüncü I²C erişim yöntemi doğrulanacak).
- İlk test: eldeki 2 ADS1115 + 1 ESP32 ile **4 SCT kanalını** birlikte okuma; gecikme, çevrim süresi, hata/timeout ve veri kaybını kaydetme.
- İki aynı altı kanallı düğümün tekrarıyla toplam 12 SCT hedefleniyor.
- Altı kanallı fiziksel modül şu anda hazır değil; ilk aşama dört kanal doğrulaması.
- [E24 protokolü](experiments/E24-ads1115-multi-bus-expansion/README.md).

## 2026-11-14 — E24 çoklu ADS1115 testi ve 12 SCT mimari adayı
- **E24 PLANLANDI:** Yeni modül imalatından önce eldeki iki ADS1115 ayrı ayrı kontrol edilecek; daha önce çalışmadığı düşünülen kart özellikle yeniden denenecek.
- İlk ortak test: tek ESP32 üzerinde iki ayrı donanımsal I²C bus ile iki ADS1115'i yönetmek; okuma gecikmesi, çevrim süresi, hata ve veri kaybını ölçmek.
- 12 kanal hedef taslağı: 2 eş ESP32 düğümü × (3 ADS1115 + 6 SCT + 1 RS485).
- Klasik ESP32 iki donanımsal I²C kontrolcüsüne sahiptir; üçüncü ayrı SDA/SCL çifti için ek yöntem doğrulanmalıdır. Üç ADS/ESP henüz kanıtlanmış değildir.
- Test başarılı olursa kullanıcı 10 adet ADS1115 yedek stok sipariş etmeyi planlıyor; sipariş henüz verilmedi.
- [E24 protokolü](experiments/E24-ads1115-multi-bus-expansion/README.md).
## 2026-11-14 — E21 ilk tam çamaşır makinesi kaydı ayrıldı
- Bugün bir tam programın baştan sona kaydı planlandı; makinenin başlatılacağı haber bekleniyor, kayıt henüz başlamadı.
- RECORD_ID: **WM-20261114-01**; geçici etiket **UZUN**. Panel programı ve ayarlar henüz bildirilmedi.
- Kalıcı PROGRAM_ID (`WMP-NNN`) program adı ve ayarlar doğrulandıktan sonra atanacak. Tekrar çekimleri ayrı RECORD_ID ile aynı PROGRAM_ID altında gruplanabilir.
- [Kayıt metadata şablonu](logs/washing-machine/WM-20261114-01/README.md) · [E21 protokolü](experiments/E21-washing-machine-program-analysis/README.md).

## 2026-11-14 — E23 ADS1115 sıçrama araştırması yeni modülle devam edecek
- E19 enerjili-hat/yüksüz-iletken uzun kayıt analizi kapalı; fiziksel sıçrama nedeni açık.
- Kullanıcı kararı: aç/kapa mekanizması/kodları çıkarılmış yeni modül yapısıyla uzun kayıt alınacak ve E19 baseline'ıyla istatistiksel karşılaştırma yapılacak.
- Ölçülen hatta röle bağlı değil ve bu hatta aç/kapa yapılmıyor; ayrı ESP'deki anahtarlamayla zaman yakınlığı nedensellik sayılmayacak.
- **E23 PLANLANDI**; yeni modül, kayıt ve analiz henüz gerçekleştirilmedi.
- [E23 protokolü](experiments/E23-ads1115-spike-new-module-comparison/README.md).

## 2026-11-14 — ADS1115 enerjili-yüksüz uzun gözlem kapatıldı

- Uzun HA History CSV istatistiksel olarak analiz edildi; ADS1115 taban grubu (n=1.592, ort. 0,00122955 A, SD 0,00028426 A) ve 0,040 A üzeri 72 sapma örneği raporlandı.
- 72 sapmanın 57'si en yakın HA switch state geçişinden 10 saniye içinde; zamansal ilişki nedensellik/gerçek SSR kontak kanıtı değildir.
- PZEM akım entity'si yalnızca 0,0 A → unavailable → 0,0 A state'leri içerir; tüm kayıt boyunca sürekli sıfır olduğu iddia edilmez.
- Bu enerjili-hat/yüksüz-iletken gözlem testi **KAPATILDI**. Ayrı enerjisiz hat testi ve ADS1115 giriş güvenliği doğrulaması açık kalır.
- [İstatistiksel rapor](logs/ads1115/2026-11-14-E19-energized-no-load-statistical-report.md).


## 2026-11-13 — Modül 1–4 yaşam döngüsü ve E22 Modül 4 olarak güncellendi

- Modül 1 bağımsız bias trafosu/güç kutusu korunacak.
- Modül 2 (üç kanallı biaslı eski SCT modülü) ve Modül 3 (PZEM + aç/kapa rölesi eski modülü) kullanıcı bildirimiyle imha edildi. Eski kod ve kayıtlar depodan silinmeyecek; tarihsel arşivdir.
- Yeni Modül 4: ESP32 + ADS1115 + 100 A / 1 V SCT + PZEM-004T V3. Ayrı YAML/firmware kimliğiyle hazırlanacak; eski Modül 2/3 kodu taşınmayacak.
- Modül 3'ün eski röle/kontrol düzeni Modül 4'e dahil değil. PZEM-004T V3'ün Modül 4'te yeniden kullanımı plan; fiziksel bağlantı ve haberleşme doğrulaması bekliyor.
- Modül 4 pinleri, ADS1115 giriş güvenliği ve PZEM UART ayarları henüz belirlenmedi. Kod/derleme/OTA/ölçüm yapılmış değildir.
- Ayrıntı: [E22 Modül 4 protokolü](experiments/E22-sct100a-1v-ads1115-characterization/README.md).

## 2026-11-13 — E19 ADS1115 enerjili-yüksüz hat / 1 s yayın ve alt eşik kararı

- ESP32D2 OTA logu ve 1 saniyelik ct_clamp yayın yapılandırması kaydedildi: [rapor](logs/ads1115/2026-11-13-E19-energized-no-load-1s-raw-log-report.md), [tam log](logs/ads1115/2026-11-13-E19-energized-no-load-1s-ota-log.txt).
- Logda ESPHome 2026.10.2, ADS1115 I²C 0x48, 200 ms ct_clamp penceresi ve 1.000 s update interval görülüyor. Tekrarlanan ct_clamp ham çıktısı ve HA sensör yayını 0.000 A.
- Kullanıcı kararı: 0.005 A alt eşik kaldırıldı; alt eşik ve spike filtresi yok. ct_clamp sonucu 0.000 A ise 0.000 A yayınlanır.
- [Alt eşiksiz 27.60 / 1 s YAML snapshot](firmware/experiments/esp32d2-ads1115-ct-clamp-live-27.60-1s-unthresholded.yaml) depoya kaydedildi. Bu snapshot ayrıca derlenip OTA edilmedi; mevcut log, 0.005 A filtreli sürümden.
- Test koşulu enerjili hat / ölçülen iletkende yük yok. Enerjisiz hat testi ayrı yapılacak.
- ADS1115 A0/A1 ortak-mod ve giriş ray sınırı güvenlik doğrulaması hâlâ açık.

## 2026-11-13 — ADS1115 filtresiz enerjili-yüksüz hat gözlemi ve yeni tek-modül planı

- Kullanıcı bildirimi/grafik gözlemi: ESP32D2 + ADS1115 + SCT, 200 ms ct_clamp penceresi ve 1 s yayınla çalıştırıldı; yazılımsal alt eşik ve spike filtresi kaldırılmış durumda.
- Test koşulu: hat enerjili, ölçülen iletkende yük/akım yok; PZEM grafikte 0.000 A gösteriyor.
- HA grafiklerinde normal ADS1115 tabanı yaklaşık 0.001 A; yaklaşık 0.048 A seviyesinde seyrek, dar sıçramalar görüldü. İlk yaklaşık 10 dakikalık kesitte 1, sonraki yaklaşık 13 dakikalık kesitte 2 sıçrama gözlendi. Ham CSV olmadığı için örnek sayısı, kesin spike genişliği ve istatistiksel dağılım hesaplanmadı.
- Kullanıcı kararı: alt eşik, ortalama veya spike filtresi eklenmeyecek; ham ölçüm korunacak. Bu, mevcut gözlem koşuluna ait geçici işletim kararıdır; spike nedeni teşhis edilmedi.
- Sonraki deney: aynı ölçüm zinciriyle, ölçülen hattın enerjisiz olduğu ayrı taban gözlemi. Enerjili-yüksüz ve enerjisiz koşullar ayrı değerlendirilecek.
- Yarın için tasarım planı: tek ESP32 üzerinde 2 SCT kanalı + 1 ADS1115 + PZEM-004T V3; harici bias olmadan ölçüm hedefi; 1 s yayın; alt eşik/spike filtresi yok. Pinler, UART, I²C, giriş ortak-mod/rail güvenliği ve zamanlama henüz tasarlanıp doğrulanmadı. Kod/derleme/OTA/entegrasyon yapılmadı.
- [Deney raporu](logs/ads1115/2026-11-13-E19-energized-no-load-unthresholded-observation.md).
- Depodaki 27.60/0.03A/1s YAML snapshot'ı bu geceki filtresiz sürüm değildir; bu nedenle onu filtresiz kod diye kullanmayın. Filtresiz tam YAML snapshot henüz depoya kaydedilmedi.

## 2026-11-13 — E19 ADS1115 alt eşik 0,03 A ve 1 saniye yayın canlı denemesi

- Kullanıcı bildirimi: yeni ESP32D2/ADS1115 kodu, tekil sıçramalar (spike) hariç genel olarak başarılı bulundu.
- Değişiklik nedeni: PZEM akım göstermeye devam ederken ADS1115/ct_clamp tarafının yazılım eşiği nedeniyle 0,00 A yayınlaması. Alt eşik 0,05 A'dan 0,03 A'ya indirildi.
- Aynı denemede ct_clamp yayın aralığı 2 saniyeden 1 saniyeye alındı. 200 ms RMS örnekleme penceresi, 860 SPS, gain 2.048, katsayı 27.60 ve UDP 4210 olay alıcısı korunuyor.
- 1 saniye yayın aralığı daha sık sonuç üretir; 200 ms ölçüm penceresini değiştirmez.
- Spike'lar başarılı kararlı davranış değerlendirmesine dahil edilmedi; ham log/CSV ve spike sayısı/büyüklüğü henüz sağlanmadığından nedenleri hakkında yorum yapılmadı.
- [Canlı test raporu](logs/ads1115/2026-11-13-E19-003A-threshold-1s-live-test.md) · [iki satırlık değişiklik kaydı](logs/ads1115/2026-11-13-e19-ads1115-003a-1s.patch).
- Kaynak ayrımı: kullanıcının 606 satırlık çalışan YAML'ı 27.60 katsayısı ve UDP alıcısı içerir; depodaki kısa referans YAML farklıdır. Bu committe tam 606 satırlık YAML snapshot'ı depoya kopyalanmadı; değişiklik patch'i ve test raporu saklandı.
- Derleme/OTA çıktısı bu oturumda mevcut değildir; kodun cihazda çalışması kullanıcı canlı test bildirimiyle desteklenmektedir, bağımsız derleme doğrulaması değildir.

## 2026-11-13 — Yeni hedef E21: çamaşır makinesi program davranışı analizi

- Kullanıcı kararıyla PZEM kararlı-alan eşleştirmesi/eğitim ve bu amaçla aç-kapa deneyi ihtiyacı kapatıldı; mevcut ADS1115 + SCT ölçüm zinciri pratik hedefi karşılıyor.
- Eski E19/E20, T008/T006, ADR, YAML, log ve ham veri kayıtları silinmez; tarihsel arşivdir.
- E20 18 W aç/kapa tepki protokolü plan aşamasındaydı; yeni hedef için gereksiz olduğundan **KAPATILDI — YAPILMADI**. Fiziksel deney tamamlandı iddiası yoktur.
- **Yeni aktif hedef:** E21 — çamaşır makinesi program davranış analizi. Bir tam programın akım zaman serisi kaydedilecek; evre adayları, süreleri, geçişleri ve tekrar eden örüntüleri incelenecek.
- PZEM yeni hedefte zorunlu eğitim etiketi değildir; varsa yardımcı karşılaştırma verisi olarak tutulur.
- Ham CSV korunacak; program/ayar/yük bilgileri kullanıcı bildirimiyle kaydedilecek; evre isimleri yalnız grafik üzerinden kesinleştirilmeyecek.
- [E21 protokolü](experiments/E21-washing-machine-program-analysis/README.md) · [ADR-026 karar kaydı](docs/decisions/ADR-026-close-stable-window-training-open-washer-analysis.md).
- ADS1115 A0/A1 ortak-mod ve giriş ray güvenliği fiziksel doğrulaması hâlâ açık koşuldur.



## 2026-11-13 — E19 57 W sabit yük oturumu açıldı
- Yük düzeltmesi: 58 W değil 57 W; başlangıç 18:32 (+03:00), kullanıcı bildirimi.
- 57 W sabit yük testi AÇILDI; log/CSV ve sonuç bekleniyor.
- 150 W gözleminden yöntem notu: ilk ~2 dakika PZEM akım/güç yükselişi; yeni sabit yüklerde ilk 3 dakika geçici bölge kabul edilecek, kararlılık ayrıca zaman serilerinden doğrulanacak.
- PZEM ortak kararlı pencerenin referansı; nominal watt teorik akım hesabı referans değildir.
- İlk karşılaştırmada ADS1115/ct_clamp ayarları ve çalışan K sabit; gain 0.512 ve accuracy_decimals 3 ertelendi.
- Bias/common-mode ve A0/A1 gerilim güvenliği doğrulanmadan enerjili test sürdürülmemeli.
- [57 W kayıt](logs/ads1115/2026-11-13-E19-57w-test.md); [sabit yük yöntem notları](test-loads/README.md).


## 2026-11-13 — E19 150 W sabit yük sonucu ve 58 W sonraki test
- 150 W CSV ortak kararlı penceresi 18:16:30–18:24:30 (+03:00): PZEM 0.65472 A (n=39), ADS1115 0.66279 A (n=241, +%1.23), Modül 2 CH1-1T 0.60402 A (n=480, -%7.74).
- PZEM güç ortalaması 149.69 W; ilk yaklaşık iki dakika lamba oturma dönemi karşılaştırma penceresinden çıkarıldı.
- K=27.60 çalışan binary ile eşleştirilmedi; K≈27.26 yalnız koşullu hesap, uygulanmadı. Firmware/katsayı değiştirilmedi.
- Gain 2.048, 860 SPS, 200 ms, 2 s, accuracy_decimals 2 ve 0.05 A filtre korundu.
- **Sonraki: 58 W sabit yük testi PLANLANDI.** İlk turda aynı ayarlar korunacak; gain 0.512 ve accuracy_decimals 3 değişiklikleri ertelendi.
- Bias/common-mode ve ADS1115 giriş gerilimi güvenliği enerjili test öncesi doğrulanmalı.
- Rapor: [150 W](logs/ads1115/2026-11-13-E19-150w-comparison.md); [58 W planı](logs/ads1115/2026-11-13-E19-58w-test-plan.md).
## 2026-11-13 — E19 100 W yorum düzeltmesi ve 150 W test planı
- 100 W ortak oturumda ADS1115 0.469881 A (n=84), PZEM 0.469882 A (n=34), Modül 2 CH1-1T 0.434240 A (n=167) ortalamaları kaydedildi. Bu tek oturum gözlemidir; aynı noktadan türetilen katsayı bağımsız doğrulama değildir.
- ADS1115 açılış logundaki Sample rate: 7 değeri 7 SPS değil, 860 SPS enum/register kodudur; 200 ms'de 174–177 farklı örnek bununla uyumludur. Önceki hız uyuşmazlığı yorumu düzeltildi.
- Depodaki E19 YAML 30.0 doğrusu içerirken log değerlendirmesinde 27.60 geçmektedir; çalışan binary/katsayı kaynağı eşleştirilmedi. K değiştirilmedi.
- Gain 2.048, 200 ms, 2 s, 0.05 A filtre ve 2 basamak yayın korunuyor. Gain 0.512 veya diğer değişiklikler uygulanmadı; bias/common-mode güvenliği açık.
- SSR fiziksel OFF doğrulanmadı; UDP olayları yük ON/OFF etiketi sayılmıyor.
- **Aşama 3: 150 W sabit yük testi PLANLANDI.** Mevcut ayarlar korunarak ADS1115/PZEM ortak kararlı alanı kaydedilecek; sonuç/log henüz yok.
- Ayrıntı: [E19 README](experiments/E19-ads1115-low-current-alternative/README.md), [sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md), [100 W raporu](logs/ads1115/2026-11-13-E19-three-module-100w-comparison.md).

## 2026-11-13 — E19 üç modül ortak yük karşılaştırması
- Ortak 17:48:27–17:51:13 penceresinde ADS1115 0.469881 A (n=84), PZEM 0.469882 A (n=34), ESP32D1 CH1-1T 0.434240 A (n=167) ortalama verdi.
- ESP32D1 CH1-1T, PZEM ortalamasından yaklaşık %7.59 düşük ve daha değişkendi; bu tek oturum sonucu, katsayı kararı değildir.
- ESP32D2 açılış logu Gain 2 / 7 SPS gösterdi; depodaki E19 YAML 2.048 / 860 ayarıyla eşleşme kanıtlanmadı.
- UDP olay aktarımı loglandı; SSR OFF readback mismatch ve OFF sonrası akım nedeniyle fiziksel yük kesilmesi doğrulanmadı.
- Katsayılar değiştirilmedi; ADS1115 katsayısı ve ±%4 başarısı ilan edilmedi.
- Ayrıntı: [E19 üç modül karşılaştırma kaydı](logs/ads1115/2026-11-13-E19-three-module-100w-comparison.md).


## 2026-11-13 — E19 ADS1115 ilk donanım logu ve 100 W katsayı testi
- ADS1115 I2C 0x48 bulundu; A0-A1 diferansiyel okumalar yüksüz durumda 8–39 µV, yaklaşık 60 W yükte önceki düşük hızlı logda yaklaşık -12.8 mV ile +13.1 mV arasında değişti.
- Önceki ADS logu 7 SPS / yaklaşık 1 s yayın aralığı olduğundan RMS akım veya katsayı ölçümü değildir; aliasing olasılığı not edildi.
- ESP32D1 mevcut zincir logunda ham ct_clamp 0.13757–0.13954 A; K uygulanmış çıktı 3.332–3.380 A; 6.700–6.920 SPS. Aynı kesitte PZEM referansı bulunmadığından sonuç gerçek akım sayılmadı.
- ESP32D2 ADS1115 + ct_clamp YAML kaydedildi; henüz derleme/OTA/860 SPS donanım doğrulaması yok.
- E19 Aşama 2 açıldı: 100 W akkor sabit yükte ESP32D1, ESP32D2 ve PZEM ortak kararlı alanını karşılaştırıp ADS1115 katsayısını belirlemek. Test henüz yapılmadı.
- Ayrıntılar: [E19](experiments/E19-ads1115-low-current-alternative/README.md), [ilk log](logs/ads1115/2026-11-13-E19-ads1115-first-bringup.md), [YAML](firmware/experiments/esp32d2-ads1115-ct-clamp.yaml).

## 2026-11-07 — 78 W ölçülebilir alan başlangıcı

- Kullanıcı kararı: mevcut CH1 kurulumunda sayısal değer verilecek ölçülebilir alan 78 W'ta başlar.
- 57 W + 18 W karma yükte PZEM gücü 78,10 W bildirildi; HA ekran son değerleri PZEM 0,341 A / CH1 0,366 A / ham SCT 0,01512 A.
- Ekran son değerleri farkı yaklaşık %7,33; ±%4 doğrulaması değildir. 78 W CSV/kararlı pencere istatistiği henüz yoktur.
- Ayrıntı: [LOAD-78W-001](test-loads/78w-mixed-incandescent/README.md). K=24.22 değişmedi.

## 2026-11-07 — E17 18 W ve 57 W sürekli yük istatistikleri

- 18 W ve 57 W HA History CSV kayıtları analiz edilerek ayrı test-yükü karakteristiklerine dönüştürüldü.
- 18 W: 90 dk (10:30–12:00 +03:00), PZEM 0,07824 A / 17,635 W; CH1 n=5.401, ortalama 0,30571 A, medyan 0,29920 A, SD 0,04477 A, CV %14,64, P95 0,36962 A, maksimum 1,29129 A.
- 57 W: 70 dk (13:00–14:10 +03:00), PZEM 0,26307 A / 59,8405 W; CH1 n=4.201, ortalama 0,35550 A, medyan 0,35403 A, SD 0,01786 A, CV %5,02, P95 0,38632 A, maksimum 0,49263 A.
- İki oturumda CH1 ortalaması 0,24–0,41 A hesaplanmadı alanındadır. Ölçüm doğruluğu/kalibrasyon iddiası yoktur.
- 57 W dağılımı 18 W'a göre daha dardır; oturum farkı gözlemdir, nedensellik kanıtı değildir.
- Ham CSV dosyaları Git'e eklenmedi; dosya adları, boyutları ve SHA-256 değerleri test-yükü kayıtlarına yazıldı.
- Ayrıntılar: [18 W](../test-loads/18w-incandescent/README.md), [57 W](../test-loads/57w-incandescent/README.md), [E17](../experiments/E17-low-current-continuous-load-observation/README.md).

## 2026-11-01 — ADR-025

- Kararlı SCT/PZEM alanları katsayı öğrenmek için kullanılır; ham kayıt korunur.
- Öğrenilmiş SCT modeli tam ham kayıtta da incelenir.
- Bu incelemede Python bilinen yük koşulunu kullanır; PZEM geçiş okumaları örnek başına referans değildir.
- Mimari karar kaydedildi; uygulama ve gerçek veri testi beklemede. Ayrıntı: [ADR-025](docs/decisions/ADR-025-raw-data-sct-model-behavior-validation.md).

## 2026-11-01 — E11 yüksüz iki modül uzun süreli gözlem planı

- İlk ortak deney olarak E11 planlandı: Modül 2 ve Modül 3 birlikte çalışacak; ölçülen hatta yük bulunmayacak.
- Modül 3 PZEM akım/gerilim/PF akışını, Modül 2 üç SCT kanalını sürekli yayınlayacak.
- Modül 3'ün 40 s ON / 20 s OFF mantıksal SSR döngüsü sürerken Modül 3 gönderim olayları ile Modül 2 alım olayları BOOT_ID + EVENT_ID + STATE üzerinden karşılaştırılacak.
- Önce kısa ortak açılış ve log kontrolü; başarılıysa ertesi gün akşama kadar hedeflenen yüksüz uzun gözlem.
- Deney sırası ihtiyaç ve donanım hazır oluşuna göre değişebilir; bu esneklik Faz 2 görev bağımlılıklarını değiştirmez.
- Modül 2 üç SCT kanalı açık kalır; kanal seçici jumper/düğme eklenmesi planlanmıyor.
- **Durum:** Yalnız planlama kaydı. Montaj, deney, log ve sonuç henüz yok. [E11 protokolü](experiments/E11-idle-dual-module-observation/README.md).

## 2026-11-01 — Python ON/OFF paket bütünlüğü kararı (ADR-024)

- Mevcut UDP/HA olay aktarımı korunur; yeni HA helper veya merkezi HA mimarisi kurulmaz.
- Modül 3 PZEM ve Modül 2 SCT akışları kendi ON/OFF olaylarıyla bağımsız paketlenir.
- ON başlangıcı veya OFF bitişi eksik/uyuşmazsa ilgili akış aralığı tamamlanmış paket değildir; Python bunu tanı koduyla raporlar.
- İki akışta aynı BOOT_ID + EVENT_ID paket aralığı doğrulanmadan eğitim örneği oluşturulmaz.
- Yeni ON açık pakete gelirse önceki paket eksik/bozuk olarak kapatılır ve yeni ON yeni paket adayı başlatır; BOOT_ID değişiminde açık paket tamamlanmamış sayılır.
- ADR-024 mimari kabul kuralıdır; Python kodu ve gerçek export testi henüz yapılmadı.

## 2026-11-01 — Modül 2/3 uzun ON/OFF olay aktarımı

- Modül 2 uzun logunda EVENT_ID 59 ON, 61 ON, 62 OFF ve 64 OFF alındı; her biri için HA_EVENT_PUBLISHED var.
- EVENT_ID 60 ve 63 bu alıcı logunda yok; kayıpsız aktarım sonucu çıkarılamaz.
- Ayrı HA History ekran görüntüsünde EVENT_ID 70 OFF ve 71 ON, Modül 2 ve Modül 3 olay kayıtlarında görünüyor; SSR HA entity mantıksal Kapalı/Açık durumlarını gösteriyor.
- 70 OFF → 71 ON arası 20 saniye. Fiziksel SSR kontak anahtarlaması ve Recorder DB kalıcılığı bağımsız doğrulanmadı.
- Kanıt ve analiz: [uzun ON/OFF analizi](logs/module2/2026-11-01-module2-on-off-extended-analysis.md), [seçilmiş kanıt](logs/module2/2026-11-01-module2-on-off-extended-evidence.log).
- Modül 2/3 kod başlıkları ve README protokol açıklamaları güncel mimariye göre düzenlendi; kod mantığı değiştirilmedi.
- T010 kapalı; T007/T008 Python veri aktarımı ve paketleme uygulaması henüz yapılmadı.


## 2026-11-01 — Modül 2 UDP olay alıcısı ilk gerçek paket kanıtı

- Yeni kaynak: [firmware/bero-modul2-esp32d1.yaml](firmware/bero-modul2-esp32d1.yaml). LOAD-15W-003 üç-SCT sıralı ölçüm temeli korunarak UDP 4210 dinleyicisi ve HA olay entity'leri eklendi.
- Gerçek Modül 2 logunda Modül 3 kaynak IP 192.168.0.70'ten EVENT_ID=59 / STATE=ON paketi alındı; ham mesaj ile BOOT_ID/EVENT_ID/STATE HA entity'lerine yayınlandı.
- [Seçilmiş log kanıtı](logs/module2/2026-11-01-module2-udp-event-receiver-evidence.log); [log analizi](logs/module2/2026-11-01-module2-udp-event-receiver-log-analysis.md).
- **Doğrulama sınırı:** Tek ON paketi doğrulandı. OFF alımı, çoklu olay/kayıpsızlık, Recorder kalıcılığı ve yeni kaydedilen YAML'ın bağımsız derleme/OTA testi açık.
- T010 kapalı kalır; olay alıcısı bu göreve eklenen yeni bir entegrasyon kaydıdır. T007/T008 veri aktarımı ve Python paketleme işleri ayrı aşamalardır.

## 2026-11-01 — Paket işaretli akış bölümleme kararı (ADR-022)

- Modül 3, SSR olay değişiminde tek `BERO_EVT` mesajı üretir; aynı mesajı kendi PZEM akışına ayrı kayıt olarak ekler ve UDP 4210 ile Modül 2'ye gönderir.
- Modül 2, aldığı aynı mesajı kendi SCT akışına ayrı kayıt olarak ekler; olay kimliğini yeniden üretmez.
- Ölçüm kayıtlarına örnek başına zaman/paket alanı eklenmez. ESP'ler kararlılık, kırpma, eşleştirme veya katsayı hesabı yapmaz.
- Python her akışı olay işaretleriyle paket aralıklarına böler; aralıkları BOOT_ID + EVENT_ID ile eşleştirir.
- PZEM ve SCT kararlılığı kendi akışlarında bağımsız tespit edilir; geçiş/yerleşme bölümleri kırpılır. Eğitim etiketi Python tarafından paket kimliğiyle eklenir.
- Timestamp iki sensörün ölçümlerini eşleştirme anahtarı değildir; HA dışa aktarımında yalnızca aynı modül içindeki kayıt sırasını yeniden kurmak için gerekebilir.
- ADR-019'un timestamp kesişimi şartı bu kararla geçersiz kılındı. [ADR-022](docs/decisions/ADR-022-packet-marker-segmented-training-streams.md).
- **Uygulama durumu:** Yalnızca mimari dokümantasyon. Firmware, derleme, OTA, UDP ve HA kayıt sıralaması henüz değiştirilmedi/doğrulanmadı.

## 2026-11-01 — T008 kararlı alan eşleştirme prensibi netleştirildi

- SCT ve PZEM kararlılığı kendi ölçüm akışlarından bağımsız tespit edilir; zaman veya UDP olayları kararlılık ölçütü değildir.
- Paket/zaman/SSR ON-OFF yalnızca deneyin olay çerçevesini sağlar.
- Eğitim verisi, iki bağımsız kararlı aralığın zaman kesişimidir. Örnek: SCT 10–16 s, PZEM 12–14 s ise ortak bölüm 12–14 s.
- Eşit başlangıç/bitiş veya eşit süre gerekmez. Zaman damgası yalnız kesişim hesabında kullanılır; zaman bazlı kararlılık penceresi yoktur.
- ON–OFF aralığı kendiliğinden kararlı değildir. Eşik/tolerans/minimum süre gerçek HA verisinden sonra belirlenecek.
- [ADR-019](docs/decisions/ADR-019-module2-module3-independent-event-streams.md); [Python veri hattı mimarisi](docs/architecture/python-program-architecture.md).


## 2026-11-01 — LOAD-15W-003 çok turlu UNIT kıyası hazırlandı

- Tek 15 W yük için tek oturum planlandı: SCT1 faz 2T, SCT3 faz 3T, SCT2 nötr 4T; UNIT bağımsız referans.
- Karşılaştırma: SCT1↔UNIT×2, SCT3↔UNIT×3, SCT2↔UNIT×4; ayrıca tur sayısına bölünmüş normalize değerler UNIT ile kıyaslanacak.
- [Test planı](test-loads/15w-2t-3t-4t/README.md) ve [YAML snapshot](firmware/archive/LOAD-15W-003-2026-11-01-esp32d1-15w-2t-3t-4t-unit.yaml) eklendi.
- Kanallar aynı çevrimde sıralı okunur; eşzamanlı örnekleme değildir. K=24.22, 200 ms, 250 ms slot ve 2 s çevrim korunur.
- 15 W tekil yük UNIT baseline'ı ve fiziksel log yok. Derleme/OTA/deney yapılmadı; durum PLANLANDI/HAZIRLANDI.

## 2026-11-01 — LOAD-42W-002 kısa log denetimi

- 68 saniyelik kısa logda 34 çevrim tamamlandı; Wi-Fi ve ADC başlatmaları normal, hata satırı yok.
- Ortalama: SCT1 0.25106 A; SCT2 0.24150 A; SCT3 0.34732 A; bias 1.66147 V.
- SCT3/SCT1 oranı 1.383; 2T/1T davranışı için takip gerekiyor.
- Raw AC entity'lerinde birim/semantik hatası tespit edildi: filtre öncesi ham akım A iken entity V olarak etiketlenmiş. Firmware henüz düzeltilmedi.
- HA Recorder/History kök nedeni doğrulanmadı; API server dinliyor fakat HA client bağlantısı ve Recorder yazımı logla kanıtlanmıyor.
- [Kısa log ve teşhis notu](logs/module2/2026-11-01-load-42w-002-short-log-ha-diagnostic.md). Test açık.

## 2026-11-01 — LOAD-42W-002 üç SCT / HA uzun kayıt

- 42 W ampul altında üç kanallı uzun süreli HA geçmiş gözlemi açıldı: [test kaydı](test-loads/42w-bulb/README.md).
- SCT1 faz 1T/GPIO32; SCT2 nötr 1T/GPIO33; SCT3 faz 2T/GPIO34; ortak bias GPIO35.
- Kullanıcı YAML'ın derlendiğini bildirdi; [kod snapshot](firmware/archive/LOAD-42W-002-2026-11-01-esp32d1-three-sct-ha-history.yaml).
- HA Recorder/History, OTA/cihaz çalışması ve uzun kayıt henüz doğrulanmadı. Test AÇIK.
- Bu yeni test T010'u yeniden açmaz; T010 kapalıdır.

## 2026-11-01 — Faz 2 veri hattı ve düşük akım yürütme planı

- [Ayrıntılı yürütme planı](docs/plans/2026-11-01-phase2-data-and-low-current-execution-plan.md) eklendi; STATUS ve ROADMAP'ten bağlandı.
- Görev sırası korundu: T009 → T010 → T007 → T008 → T006. T010 aktif kalır.
- 0.4 A fiziksel alt sınır ve güncel Modül 2'de 0.35 A eşik bulunduğu iddiaları kabul edilmedi; mevcut kanıt bunları desteklemiyor.
- Düşük akım nedeni henüz ayrıştırılmadı; K, firmware, eşik, pin ve deney ayarları değiştirilmedi.
- Bu değişiklik bir planlama kaydıdır; yeni derleme, OTA veya fiziksel ölçüm değildir.

## 2026-11-01 — Gün sonu kapanışı

- Bu sohbet kapsamında BERO'ya ait kod, YAML, donanım veya deney değişikliği yapılmadı; Claude hizmeti ve genel kod denetim promptu BERO dışı konulardı.
- Faz 2 / T010 aktif kaldı. E10 hâlâ PLANLANDI; yeni log, derleme, OTA veya fiziksel ölçüm eklenmedi.
- Sonraki çalışma: T010 kanal testlerinden kontrollü biçimde devam etmek; E10 protokolünü ayrı ve sabit değişkenli deney olarak yürütmek.

## 2026-10-31 — ct_clamp hipotez sicili ve sonraki deney sırası

- Bu sohbetin H1–H19 sınıflandırması tek bir [hipotez sicilinde](docs/research/ct-clamp/2026-10-31-hypothesis-register-and-next-experiments.md) toplandı.
- Kaynak kod/tarihçe bulguları, BERO saha desteği, hipotezler, açık araştırma soruları ve kanıtsız iddialar ayrıldı.
- Sonraki ölçüm sırası: T010 kanal davranışı; E10 200→500→1000→200 ms; ayrı last_value A/B; ardından T007→T008→T006.
- E10 hâlâ planlandı; bu kayıt sırasında YAML/firmware/K değiştirilmedi, derleme/OTA ve fiziksel deney yapılmadı.

## 2026-10-31 — BERO sensörden bağımsız mimari kaydı

- Depo kökünde [MIMARI](../../MIMARI/README.md) alanı oluşturuldu.
- [Pencereli Sensör Analizi ve Davranış Çıkarımı](../../MIMARI/PENCERELI-SENSOR-ANALIZI/README.md) üç katmanı tanımlar: veri toplama, özellik çıkarma, davranış çıkarımı.
- SCT013-PZEM bu mimarinin ilk uygulama/kanıt alanıdır; sensöre özgü pin, katsayı ve algoritmalar genel ilke sayılmaz.
- Özellik penceresi ile kararlılık penceresi ayrıldı; sürekli ham ADC saklama kararı değiştirilmedi.
- Yeni mimari belge tasarım kaydıdır; genel davranış sınıflandırması veya yeni sensör entegrasyonu tamamlanmış değildir.

## 2026-10-31 — Sensör okuma kalıpları

- ct_clamp araştırmasından hareketle genel sensör veri yolu ile CT'ye özgü AC RMS algoritması ayrıştırıldı.
- Açıklamalı referans YAML'lar eklendi: [CT / AC RMS](firmware/patterns/ct-clamp-ac-rms-reference.yaml), [analog DC ADC](firmware/patterns/adc-dc-voltage-observer.yaml).
- Ayrıntı ve sensör türüne göre seçim rehberi: [firmware/patterns/README.md](firmware/patterns/README.md).
- Patterns rehberinde gerçek Log 63 örnek çıktısı (0,12763 V Raw AC / 3,091 A / 3.656 kabul edilmiş örnek) gösterildi; tarihsel kanıt, yeni şablon testi değildir.
- Şablonlar henüz derlenmedi veya donanımda test edilmedi; mevcut ESP32D1/ESP32D2 firmware'leri değiştirilmedi.
- firmware/esp32d1.yaml ile daha sonraki üç kanallı T010 kaydı arasında içerik tutarsızlığı tespit edildi; mevcut dosya korunarak ayrı not edildi.

## 2026-10-31 — ESPHome ct_clamp üç kaynaklı sentez

- Claude, GitHub Copilot ve bağımsız inceleme; PR #559, #1906, #1915, #1916, #2283, #4229 ve #4236 kayıtlarıyla sentezlendi.
- 2019 ilk geliştirme ile 2021 algoritma/iyileştirme adımları ayrıştırıldı. Copilot'un 200 ms, 60 s ve performans gerekçeleri kanıt düzeyine göre düzeltildi.
- [Sentez raporu](docs/research/ct-clamp/2026-10-31-synthesis-copilot-claude-independent.md).
- Firmware, K=24.22, sample_duration ve update_interval değişmedi; fiziksel test yapılmadı.

## 2026-10-31 — ESPHome ct_clamp tasarım tarihçesi araştırıldı

- **DURUM:** Kaynak araştırması tamamlandı ve ayrı rapor olarak arşivlendi; firmware/YAML, K katsayısı ve fiziksel deney değişmedi.
- **İLK GELİŞTİRME:** PR #559 (26.05.2019); ilk bileşen commit'i 3089ffa (29.05.2019), author Jesse Hills; Otto Winter co-author/committer ve mimari inceleme katkısı.
- **KÖKEN/AMAÇ:** Jesse, kodun büyük bölümünü OpenEnergyMonitor EMonLib'den aldığını ve CTL-10-CLS ile D1 Mini üzerinde akıllı sayaç karşılaştırması yaptığını açıkladı. SCT013'e özel değil; CT clamp akım ölçümü için.
- **200 ms:** Resmî dokümanda 50 Hz'de 10 tam çevrim. İlk geliştiricinin 10 çevrimi neden seçtiğine ilişkin daha özel gerekçe bulunamadı.
- **60 s:** İlk kodda genel polling_component_schema varsayılanı; ct_clamp'e özel geliştirici gerekçesi bulunamadı. PR test örneklerinde 5 s ve 500 ms de var.
- **last_value filtresi:** PR #2283 / commit c33077bc (12.10.2021); PR gerekçesi yinelenen örnekleri atarak doğruluğu artırmak. ADC sample çağrısını engellemez; aynı değerin istatistik toplamına tekrar eklenmesini önler. Bellek/ADC dönüşüm tasarrufu hedefi belgelenmemiştir.
- **ANA KAYIT:** [Tasarım tarihçesi raporu](docs/research/ct-clamp/2026-10-31-design-history.md); [arşiv indeksi](docs/research/ct-clamp/README.md).
- **BERO ETKİSİ:** 200 ms/2 s/K=24.22 ayarları değiştirilmedi. E10 deneyi planlandığı gibi ayrı gözlem deneyi olarak kalır.

## 2026-10-31 — GitHub Copilot raporu arşivi

- GitHub Copilot tarafından hazırlanmış ct_clamp raporu, özgün metni korunarak TXT biçiminde arşivlendi.
- Üç kaynak ayrı tutuluyor: kullanıcı raporu, Copilot raporu ve bağımsız teknik inceleme. [Arşiv indeksi](docs/research/ct-clamp/README.md).
- Copilot raporundaki ifadeler doğrulanmış bulgu/karar olarak kabul edilmedi.
## 2026-10-31 — ESPHome ct_clamp teknik rapor arşivi

- Kullanıcının sağladığı dört sayfalık raporun metin aktarımı Markdown olarak arşivlendi; bağımsız kaynak kod/BERO Log 63 incelemesi ayrı Markdown raporu olarak oluşturuldu.
- Raporlar ve kapsam farkları: [ct_clamp rapor arşivi](docs/research/ct-clamp/README.md).
- Araştırma kaydıdır; firmware/K değişikliği veya yeni fiziksel test değildir.
## 2026-10-31 — ESPHome ct_clamp teknik rapor arşivi

- Kullanıcının sağladığı DOCX özgün haliyle arşivlendi; bağımsız kaynak kod/BERO Log 63 incelemesi ayrı Markdown raporu olarak oluşturuldu.
- Raporlar ve kapsam farkları: [ct_clamp rapor arşivi](docs/research/ct-clamp/README.md).
- Araştırma kaydıdır; firmware/K değişikliği veya yeni fiziksel test değildir.
## 2026-10-31 — BREAD-TOASTER-001 / Log 63

- Ekmek kızartma makinesi için, önceki TOASTER-001 tost makinesi kaydından ayrı BREAD-TOASTER-001 testi açıldı.
- UNIT 3,30 A kullanıcı bildirimi; PZEM değil ve SCT loguyla tam zaman eşleşmesi belgelenmedi.
- Log 63'te ilk açılış yayını dışlandıktan sonra 50 SCT yayını: ortalama 3,09636 A; medyan 3,094 A; min–maks 3,071–3,144 A; CV %0,433.
- Kararlı Raw AC ortalaması 0,127843 V; SPS ortalaması 18.117.
- UNIT'e göre aritmetik fark −%6,17; eşzamanlılık teyitsiz olduğundan doğruluk sonucu değil.
- K=24.22 ve firmware değişmedi; Python/modelleme yapılmadı; PZEM yok.
- [Test kaydı](test-loads/bread-toaster/README.md); [analiz](logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-analysis.md); [seçilmiş kanıt](logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-evidence.txt).
- Tam ham TXT GitHub'a aktarılmadı; kaynak dosya 32.064 bayt / 449 satır, SHA-256 `cf9254185e591650a06a990e5bc0f567ee499ba4ec541c4bb8748b132513f896`.
- Test açık; tekrarlı log ve eşzamanlı UNIT/PZEM kararlı pencere bekleniyor.

## 2026-10-31 — Toplu yük karşılaştırması

- [Tüm yükler ve karma yükler raporu](test-loads/COMPARATIVE-RESULTS-2026-10-31.md) oluşturuldu.
- Referans farkı ile kendi iç kararlılığı (SD/CV) ayrı gösterildi; eşzamanlılığı doğrulanmayan referans farkları hata sayılmadı.
- 0,30 A altı deneylerde ±%4 kabul/ret uygulanmadı. K=24.22 değişmedi.

## 2026-10-31 — TOASTER-001 / Log 62 ham arşiv ve analiz

- **HEDEF:** Mevcut K=24.22 ile tost makinesinin yüksek akım davranışını karakterize etmek; katsayıyı değiştirmemek.
- **LOG:** 934 satır / 68.572 bayt; kaynak SHA-256 `4790b00e69aaba791339f6d43aa13041efe373c5a87b9ed7fd4c1f481ce551f2`; tam ham log GitHub'a arşivlendi.
- **KARARLI BÖLGE:** İlk 119 yayın, 21:52:30.185–21:56:26.262; ortalama 7,1900 A, medyan 7,188 A, min–maks 7,135–7,264 A, SD 0,0247 A, CV %0,344.
- **REFERANS SINIRI:** UNIT 7,89 A kullanıcı bildirimi; zaman eşleşmesi doğrulanmadığından −%8,87 yalnız aritmetik farktır. PZEM yok.
- **GEÇİŞ:** Son yayın 6,096 A; tek örnek, termostat OFF kanıtı değil.
- **SONUÇ:** K=24.22 sabit; test açık. [Test kaydı](test-loads/toaster/README.md), [analiz](logs/module2/2026-10-31-toaster-001-module2-sct1-log62-analysis.md), [ham log](logs/module2/2026-10-31-toaster-001-module2-sct1-log62-full.txt).

## 2026-10-31 — MIXED-LOAD-57W-15W-001 / Log 59

- **YÜK:** 57 W akkor + 15 W ampul; UNIT 0,303 A'nın test boyunca sabit kaldığı kullanıcı bildirimi.
- **LOG:** 179 SCT-1 yayını; 21:20:18.203–21:26:14.218 (+03:00); kaynak 99.807 bayt / 1.349 satır; SHA-256 `6e7dea5c6c8991a6d4f915ebd6182f3de82b151d5726066700840f21a7d7124a`.
- **SONUÇ:** SCT ortalama 0,329553 A; medyan 0,328 A; CV %4,48. Teste özgü ±%5,6 bandı 0,286032–0,319968 A; 31/179 (%17,32) yayın band içinde, 148/179 (%82,68) üstünde. Ortalama sapma +%8,76.
- **ALT EŞİK:** 0,250 A ve altında yayın yok (%0); tüm yayınlar 0,250 A üzerinde.
- **KARAR:** Bu testte ±%5,6 tolerans hedefi karşılanmadı. 0,250 A alt eşiğinin korunması ayrı ve olumlu gözlemdir. Firmware/K değişmedi; test AÇIK.
- **DOSYALAR:** [Test kaydı](test-loads/mixed-57w-15w/README.md); [analiz](logs/module2/2026-10-31-mixed-load-57w-15w-001-module2-sct1-analysis.md); [tam ham log](logs/module2/2026-10-31-mixed-load-57w-15w-001-module2-sct1-full.txt).

## 2026-10-31 — Modül 2 SCT-1 / 100 W ct_clamp karşılaştırması

- Paylaşılan logda SCT-1 için 200 ms ct_clamp pencereleri ve akım çıktıları gözlendi.
- Son beş kararlı ESP32D1 değeri ortalama 0,589 A (aralık 0,578–0,597 A).
- Kullanıcı aynı test koşulunda PENS değerini 0,427 A bildirdi.
- Fark 0,162 A; ESP32D1, PENS değerinden yaklaşık %37,9 yüksek.
- Tek noktadan katsayı değiştirilmedi; nominal 30 A/V geçici olarak korundu.
- [SCT-1 karşılaştırma kaydı](logs/module2/2026-10-31-sct1-100w-ct-clamp-comparison.txt).
- **T010:** SCT-1 akım çıktısı logla desteklendi; ölçek/kalibrasyon doğrulanmadı. SCT-2 ve SCT-3 bekliyor.

## 2026-10-31 — SCT-1 / 100 W ilk kanal denemesi

- SCT-1 ön panel 1 numaralı girişe bağlandı ve 100 W ampul açıldı (KULLANICI BİLDİRİMİ).
- Ortak bias değeri ESPHome logunda görüldü; sayısal değer bu bildirimde paylaşılmadı.
- U200B+ göstergesinde 0,433 A görüldü (KULLANICI BİLDİRİMİ).
- GPIO32 ADC sayısal log örneği henüz bu kayıtla ilişkilendirilmedi; 0,433 A ESP32 ADC sonucu değildir.
- Ayrıntı: [SCT-1 100 W test kaydı](logs/module2/2026-10-31-sct1-100w-test.txt).
- Sonuç: SCT-1 denemesi kullanıcı bildirimiyle yapıldı; ADC log analizi ve SCT-2/SCT-3 testleri bekliyor. T010 AKTİF.

# BERO — İlerleme Ağacı

## Güncel konum

**FAZ 2 AKTİF — pratik yeniden kurulum ve sistem geliştirme.** Faz 1'de çalışan akım okuma kod yolu bulundu ve kullanıcının dört karşılaştırmasında ±%4 hedefi sağlandı. Faz 2'de sistem modül modül yeniden devreye alınacak; PZEM referanslı veri işleme daha sonraki alt aşamadır.

## İki fazlı proje ağacı

- **FAZ 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak: TAMAMLANDI**
  - Dış kaynaklı ESPHome ct_clamp kodu kullanıldı.
  - 100 W akkor: yaklaşık %0 sapma.
  - 150 W akkor: −%0,2.
  - Kettle düşük/kararlı: +%3,0.
  - Kettle kaynama: −%3,8.
  - Yapılmamış Faz 1 işleri hedefe ulaşıldığı için kapatıldı; kayıtlar arşivde.

- **FAZ 2 — Pratik yeniden kurulum ve sistem geliştirme: AKTİF**
  1. **T009 — Modül/ESP devreye alma üst görevi:** DEVAM EDİYOR.
  2. **T010 — Modül 2 ESP32D1 üçlü SCT + tek ortak bias modülü:** AKTİF.
  3. **T007 — HA → PC veri aktarımı:** PZEM/SCT entity'leri çalışınca.
  4. **T008 — PZEM/SCT kararlı alan eşleştirme/etiketleme:** T007 sonrasında.
  5. **T006 — K=24.22 katsayı/model değerlendirmesi:** T008 sonrasında.

## Faz 2 geliştirme ilkesi

Önce çalışan kod/örnek bulunur, donanım doğrulanır ve tek modül tek işlev şeklinde devreye alınır. Teori ve iç mimari araştırması yalnız somut arıza, uygulama engeli veya karar ihtiyacı varsa derinleştirilir. Başarılı kod ile gerçek log/çıktı ve yorum depoda saklanır. Eski YAML ve araştırmalar tarihsel referans olarak korunur; yeni donanımda test edilmiş sayılmaz.

## Korunan referans

- E00F ESP32D2 YAML ve eski ESP yapılandırmaları kayıtlıdır; yeni kurulumun değiştirilemez şablonu değildir.
- 200 ms pencere, 2 s yayın ve K=24.22 önceki çalışan ölçüm yolunun tarihsel değerleridir.
- Yeni üç SCT + bias Modül 2 bağlantısı ve yeni ESP pin eşlemesi henüz doğrulanmadı.

### 2026-10-31 ilk firmware açılışı

- Dört ADC sensörü (GPIO32/33/34/35) logda başlatıldı; tüm ADC setup durumları OK.
- ESPHome 2026.10.1 firmware'i açıldı; Wi-Fi/API bağlantısı başarılı.
- GPIO35 ortak bias örnekleri 1.643–1.668 V.
- SCT/ampul bağlantısı yoktu; üç SCT kanalı için 100 W test sonucu değildir.
- [İlk açılış log kanıt dökümü](logs/module2/2026-10-31-first-boot-no-load.txt).
- **T010:** Firmware açılışı ve ADC başlatma LOG İLE DESTEKLENDİ; 100 W kanal testleri bekliyor.

## Modül 2 — Üçlü SCT Okuma Modülü

- **ESPHome kimliği:** `esp32d1` / `ESP32D1`; temel başlangıç YAML'ı eklendi.
- **Kutu içeriği:** 3 SCT jack girişi, gömülü ESP32 kartı + GPIO shield, ortak bias mini breadboard.
- **Besleme:** ESP32 harici 5 V DC ile beslenecek; USB portundan PC bağlantısına erişim bulunacak.
- **Bias:** Tek kayıtlı bias devresi; tek ortak bias beslemesi üç SCT girişine dağıtılacak. Ortak bias düğümü tek ADC noktasından izlenecek.
- **ADC hedefi:** 3 bağımsız SCT sinyali + 1 ortak bias izleme = 4 ADC giriş noktası.
- **Bildirilen eşleştirmeler:** 1. dişi yuva sarı → GPIO32; 2. dişi yuva yeşil → GPIO33; 3. dişi yuva mavi → GPIO34; ortak bias turuncu → GPIO35.
- **Açık noktalar:** ESP32 kart/shield modeli, jack tip/ring/sleeve pinout'unun fiziksel teyidi, USB ile harici 5 V'un birlikte kullanım koşulları, bias ADC RAW/voltaj gösterimi.
- **Durum:** Tasarım tanımlandı; fiziksel bağlantı, YAML sensörleri, derleme ve donanım testi yapılmadı.
- **Görev:** [T010](tasks/T010-module2-triple-sct-bringup.md).
- **Karar:** [ADR-015](docs/decisions/ADR-015-module2-esp32d1-triple-sct.md).

## Dosya navigasyonu

| Bilgi | Dosya |
|---|---|
| Güncel durum | [STATUS.md](STATUS.md) |
| Yol haritası | [ROADMAP.md](ROADMAP.md) |
| Görev sırası | [tasks/README.md](tasks/README.md) |
| İlk aktif görev | [T009](tasks/T009-practical-system-bringup.md) |
| HA → PC aktarımı | [T007](tasks/T007-python-architecture.md) |
| Kararlı alan eşleştirme | [T008](tasks/T008-pzem-sct-stable-window-labeling.md) |
| Katsayı/model değerlendirmesi | [T006](tasks/T006-calibration.md) |
| Faz 1 deney geçmişi | [Deney arşivi](experiments/README.md) |
| Yeni Faz 2 kararı | [ADR-014](docs/decisions/ADR-014-phase2-practical-restart.md) |

## HEDEF / LOG / SONUÇ

- **HEDEF:** Faz 2'nin pratik başlangıç yaklaşımını, görev sırasını ve Modül 2'nin mevcut tasarım durumunu tek görünümde göstermek.
- **LOG:** ADR-014, T009 ve ana proje yönergeleri oluşturuldu/güncellendi.
- **SONUÇ:** Faz 1 tamamlandı; Faz 2 pratik yeniden kurulum ve geliştirme olarak aktif. T009 ilk görev. Bu belge donanımın çalıştığına veya firmware'in test edildiğine kanıt değildir.

## 2026-10-31 — FIXED-LOAD-0130A-001 planlandı

- 0,130 A sabit yük gözlem testi açıldı; durum PLANLANDI, ölçüm/log henüz yok.
- 0,130 A kullanıcı bildirimi; ölçüm cihazı ve fiziksel yük kimliği/gücü belirtilmedi.
- Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35; K=24.22 korunacak, yazılımsal sıfır eşiği eklenmeyecek.
- 0,30 A altı düşük akım gözlem alanında ±%4 kabul/ret uygulanmayacak.
- [Test planı](test-loads/fixed-load-0130a/README.md).

## 2026-10-31 — FIXED-LOAD-0130A-001 ilk log analizi

- SCT-1 logu incelendi: n=556; ortalama 0,203637 A; medyan 0,203 A; min–maks 0,157–0,291 A; SD 0,017971 A.
- 0,130 A hedefi UNIT/PZEM referansı olarak doğrulanmadı; fiziksel yük kimliği de bilinmiyor. Sapma hesabı yapılmadı.
- Durum: log analizi yapıldı; test referans ve kurulum teyidi beklediği için açık.
- [Test kaydı](test-loads/fixed-load-0130a/README.md); [analiz](logs/module2/2026-10-31-fixed-load-0130a-001-sct1-analysis.md).

## 2026-10-31 — LOAD-42W-001 açıldı

- 42 W ampul düşük akım gözlem testi açıldı.
- UNIT 0,174 A kullanıcı bildirimi; kararlılık ve ölçüm zamanı henüz teyit edilmedi.
- Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35; K=24.22 ve mevcut firmware korunacak.
- 0,30 A altı gözlem bölgesi; ±%4 kabul/ret uygulanmaz.
- SCT logu ve fiziksel ampul ayrıntıları bekleniyor.
- [Test kaydı](test-loads/42w-bulb/README.md).

## 2026-10-31 — LOAD-42W-001 / Log 57 gözlemi

- 42 W test yükü altında 96 SCT-1 yayını analiz edildi (21:09:28–21:12:38).
- SCT ortalaması 0,252438 A; medyan 0,251 A; aralık 0,221–0,295 A; CV %4,37.
- Raw AC ortalaması 0,0104248 V; ortak bias 1,663469 V.
- UNIT 0,174 A ile aynı zamanlı kararlı pencere doğrulanmadığından +%45,08 fark yalnız betimleyici; doğruluk sonucu değil.
- Test düşük akım gözlemi olarak açık. [Test kaydı](test-loads/42w-bulb/README.md); [analiz](logs/module2/2026-10-31-load-42w-001-log57-analysis.md).


## 2026-10-31 — LOAD-57W-001 / 57 W akkor testi açıldı

- 57 W akkor ampul test yükü ve UNIT 0,244 A başlangıç bildirimi kaydedildi.
- UNIT değerinin SCT ile aynı kararlı zaman penceresine ait olduğu henüz doğrulanmadı; PZEM verisi verilmedi.
- 0,30 A altı gözlem alanı; ±%4 kabul/ret yok.
- Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35; K=24.22 ve firmware korunacak.
- [Test kaydı](test-loads/57w-incandescent/README.md).


## 2026-10-31 — LOAD-57W-001 / Log 58

- 57 W akkor ampul testinde ESP32D1 Modül 2 / SCT-1 için 116 yayın analiz edildi.
- SCT ortalaması 0,304207 A; medyan 0,303 A; aralık 0,284–0,348 A; CV %3,00.
- Raw AC ortalaması 0,012562 V; ortak bias GPIO35 ortalaması 1,663073 V; GPIO32 ADC ortalaması 1,660694 V.
- UNIT 0,244 A başlangıç bildirimiyle aritmetik fark +%24,67; aynı zaman penceresi doğrulanmadığından doğruluk sonucu değildir. PZEM verisi yok.
- Test açık; firmware/K=24.22 değişmedi. [Test kaydı](test-loads/57w-incandescent/README.md); [analiz](logs/module2/2026-10-31-load-57w-001-module2-sct1-analysis.md); [tam log](logs/module2/2026-10-31-load-57w-001-module2-sct1-full.txt).

## 2026-10-31 — MIXED-LOAD-57W-15W-001 açıldı

- 57 W akkor + 15 W ampul karma yük testi açıldı; 15 W ampul tipi henüz belirtilmedi.
- Nominal etiket güçlerinin toplamı 72 W (hesap); gerçek güç ölçümü değildir.
- UNIT 0,303 A kullanıcı bildirimi; SCT ile zaman örtüşmesi/kararlılık doğrulanmadı.
- Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35; K=24.22 ve firmware kilitli.
- Eşleşmiş kararlı pencere elde edilirse ±%4 kıyası yapılabilir; test açık ve log bekliyor.
- Önceki LOAD-57W-001 bağımsız olarak açık kalır.
- [Test kaydı](test-loads/mixed-57w-15w/README.md).


## 2026-10-31 — IRON-001 kapatıldı; TOASTER-001 açıldı

- IRON-001 iki mevcut logla sınırlı gözlem raporu olarak kapatıldı; tüm termostat çevrimlerinin doğrulandığı iddia edilmez.
- Açık çevrimler: 9,2852 A (n=5) ve 9,3605 A (n=4). UNIT 10,16 A bildirimine göre aritmetik fark −%8,61 / −%7,87; eşzamanlılık teyitsiz.
- Kapalı/düşük akım: 40 yayın; 27 sıfır, 13 adet 0,011–0,092 A. Yaklaşık 104 s kayıt boşluğu süre hesabına katılmadı.
- TOASTER-001 tost makinesi testi AÇIK; fiziksel ölçüm bekleniyor. Güç ve referans cihazı bilinmiyor; Modül 2/K=24.22 korunacak.
- [IRON-001 raporu](test-loads/iron/README.md); [TOASTER-001 planı](test-loads/toaster/README.md).


## 2026-10-31 — TOASTER-001 / Log 62 ön değerlendirmesi

- İlk 119 SCT yayını yaklaşık 236 s boyunca 7,1900 A ortalama ve %0,344 CV ile kararlı.
- UNIT 7,89 A'ya göre aritmetik fark −%8,87; zaman eşleşmesi teyitsiz, doğruluk sonucu değil.
- Son tek yayın 6,096 A olarak ayrı geçiş verisi tutuldu.
- K=24.22 değişmedi; test açık.
- [TOASTER-001 raporu](test-loads/toaster/README.md).

## 2026-10-31 — E10 ct_clamp pencere süresi deneyi planlandı

- Faz 2 / T010 altında E10 gözlem protokolü açıldı.
- Tek değişken sample_duration: 200 → 500 → 1000 → 200 ms geri dönüş.
- update_interval: 2s, K=24.22, ESPHome 2026.10.1, SCT-1 GPIO32 ve ortak bias GPIO35 sabit.
- Deney yükü BREAD-TOASTER-001; Log 63 tarihsel 200 ms tabanı.
- Kullanıcı raporu, Copilot raporu ve bağımsız teknik inceleme protokolde ayrı ayrı referanslandı; simülasyonlar ölçüm sayılmadı.
- **Durum:** Yalnız planlandı. YAML/OTA/fiziksel ölçüm/log yok.
- [E10 protokolü](experiments/E10-ct-clamp-window-duration/README.md); [sonuç defteri](experiments/E10-ct-clamp-window-duration/results.md).


## 2026-11-01 — Modül 2 üretim kontrolleri için durum düzeltmesi

- Kullanıcı teyidi: modül ilk üretildiğinde üç SCT kanalının her birinde okuma kontrolü yapıldı.
- Kullanıcı teyidi: üç kanala ayrı bias değil, tek ortak bias noktası kullanıldı; üretim sırasında ölçüldü ve görseli daha önce paylaşıldı.
- Modül 2 ile test yükleri çalıştırıldı; gerçek cihaz logları/analizleri ve derleme-fiziksel çalışma kayıtları depoda mevcut.
- Bu kontroller yeniden yapılacak iş değildir. Önceki “kanal/bias/cihaz çıktısı bekliyor” anlatımı güncel kabul edilmeyecek.
- E10 200→500→1000→200 ms deneyi ayrı olarak PLANLANDI; henüz uygulanmadı.
- firmware/esp32d1.yaml mevcut hâli tek ct_clamp kanalı GPIO32 + ortak bias GPIO35 gösterir; fiziksel ilk kanal kontrolüyle firmware'in üç kanalı aynı anda ölçtüğü iddiası birbirinden ayrıdır.


## 2026-11-01 — Modül 2: taşınabilir tek kablolu ortak bias tasarımı

- Modül 2'nin sahibi ve imalatçısı kullanıcıdır; imalat ve test anlatımları birinci el proje kaynağı olarak ele alınır.
- Taşınabilirlik için tek bias devresi ve tek ortak bias kablosu kullanılmıştır; bu hat üç SCT kanalına ortak bias dağıtır.
- Üç SCT sinyal bağlantısı bağımsızdır; bias üç ayrı devre değildir. Breadboard bias görüntüsü daha önce paylaşılmış, ortak bias üretim sırasında ölçülmüştür.
- İlk üretimde üç SCT kanalının ayrı ayrı okuma kontrolü yapılmış; Modül 2 ile yük testleri çalıştırılmıştır. Mevcut cihaz logları, derleme ve fiziksel çalışma kayıtları depoda bulunur.
- Bunlar yeniden yapılacak işler değildir. E10 (200 → 500 → 1000 → 200 ms) hâlâ ayrı PLANLANDI deneyidir.
- Mevcut firmware YAML'ın tek SCT-1 kanalını göstermesi, fiziksel imalat ve ilk kanal kontrollerinin yapılmadığı anlamına gelmez; kod/konfigürasyon kapsamı ayrı bir tutarlılık konusudur.


## 2026-11-01 — LOAD-15W-004 / 15 W çok turlu uzun gözlem açıldı

- LOAD-15W-003'ten ayrı yeni oturum açıldı; önceki kayıt ve YAML üzerine yazılmadı.
- Faz UNIT 0,057 A ve nötr UNIT 0,059 A kullanıcı bildirimi olarak kaydedildi; zaman eşleşmesi teyitsiz.
- İlk yaklaşık 96 s log ön gözlemi: SCT1 0,18552 A, SCT2 0,24171 A, SCT3 0,07585 A; SCT3'te 11/48 sıfır; bias ortalama 1,66196 V.
- [LOAD-15W-004 deney kaydı](test-loads/15w-2t-3t-4t/LOAD-15W-004.md); [YAML snapshot](firmware/archive/LOAD-15W-004-2026-11-01-esp32d1-15w-2t-3t-4t-unit.yaml).
- AÇIK; uzun test, derleme/OTA ve HA Recorder doğrulaması yok. 0,30 A altında ±%4 kabul/ret uygulanmaz.


## 2026-11-01 — Kararlı alan eğitimi ana çerçevesi (ADR-019)

- Modül 2: SCT ölçümleri ile UDP'den alınan paket/zaman/SSR ON-OFF olayları HA'ya **ayrı kayıt akışları** olarak aktarılır.
- Modül 3: paket/zaman/SSR ON-OFF bilgisini UDP ile yayınlar; PZEM ölçümleri ve aradaki olay/yayın bilgileri HA'ya **ayrı kayıt akışları** olarak aktarılır.
- Python, SCT + PZEM + olay akışlarını sonradan kaynak zaman ve varsa BOOT_ID/EVENT_ID ile ilişkilendirir; olay çizgisinden yük durumunu çıkarır.
- SCT ve PZEM kararlılığı ayrı hesaplanır; zaman bakımından örtüşen kararlı pencereler eşleştirilir. PZEM eşleşen SCT penceresinin proje referans etiketidir.
- ESP/HA tarafında ölçüm ve olayın birebir eşleştirilmesi yoktur. Zaman toleransı/eşik/pencere süresi gerçek veri görülünce belirlenir.
- [ADR-019](docs/decisions/ADR-019-module2-module3-independent-event-streams.md); [Python veri hattı mimarisi](docs/architecture/python-program-architecture.md).
- Bu kayıt mimari karardır; firmware, UDP paketi veya fiziksel test değişikliği değildir.


## 2026-11-05 — E12 SCT kararlılık ve tepki süresi araştırması

- E12 planlandı: SCT1 kararlı alan tespiti; PZEM ve SCT kararlı alanlarının bağımsız belirlenip zaman kesişimiyle eşleştirilmesi; SCT tepki/yerleşme süresi ve daha kısa ölçüm penceresi araştırması.
- İlk gözlem adayı 20:07–20:37 100 W akkor oturumudur; 20:12 kablo değişikliği öncesi/sonrası ayrı incelenecek.
- İlk analizde 200 ms sample_duration, 2 s update_interval ve K=24.22 referans alınır.
- Deney sırası sabit değildir; kullanıcı ve asistan deneyleri ihtiyaca göre öne alabilir. Faz 2 görev bağımlılıkları korunur.
- **Durum:** Protokol kaydedildi; tam log analizi ve Python uygulaması beklemede. [E12](experiments/E12-sct-stability-window-and-response/README.md).


## 2026-11-05 — E11 sonucu ve E12 ilk veri gözlemi

- E11 yüksüz uzun gözlem analiz edildi: PZEM 0.0 A; SCT1/2/3 medyanları yaklaşık 0.163/0.170/0.157 A; olay görünürlüğü 85/92 (%92.4), kesin UDP kaybı hükmü verilmedi.
- E12 ilk 100 W CSV ön karşılaştırmasında 35 ON penceresi incelendi; SCT1/PZEM merkez farkı yaklaşık %3.34, 24/35 pencere ±%4 içinde. Bu ilk ön elemedir; bağımsız kararlılık algoritması ve Python eğitimi henüz yoktur.
- Kalibrasyon referansı yalnızca ON içindeki bağımsız SCT/PZEM kararlı alanlarının örtüşmesidir. Geçiş/interpolasyon değerleri katsayı öğrenimine katılmaz; ham kayıt korunur.
- K=24.22 değiştirilmedi. Hafta sonu farklı sabit yükler ve ilk Python veri hattı önceliklidir; canlı makine doğrulaması sonraki aşamadır.
- Ayrıntı: [E11](experiments/E11-idle-dual-module-observation/README.md), [E12](experiments/E12-sct-stability-window-and-response/README.md).


## 2026-11-06 — Eğitim yaklaşımı ve sonraki çalışma

- Kullanıcı, genel akım okuma aşamasına ulaşıldığını ve eğitim için kullanılabilecek kararlılıkta alanları hedeflediğimizi teyit etti; sayısal kararlılık algoritması henüz tamamlanmış değildir.
- Kullanıcı, eğitim felsefesinin ve istenen veri yaklaşımının bugün ekran görüntüsüyle de sabitlendiğini bildirdi.
- Yarın ilk iş, eğitim için kullanılacak SCT ve PZEM verisini gerçek kayıtlar üzerinden seçmek ve sabitlemek; kararlı alanların uygunluğunu değerlendirmektir.
- PY-01 arşiv/oturum tasarımı çalışan örnek üzerinden denenecek; henüz kesinleştirilmedi.
- Python eğitim/etiketleme uygulaması veya yeni model çıktısı bu oturumda üretilmedi. T007 → T008 → T006 sırası korunur.


## 2026-11-06 — E16: yüksüz/düşük akım ON/OFF davranışı planlandı

- HA ekran görüntüsünde PZEM 230,2 V / 0,000 A iken CH1 SCT akımı 0,204 A ve Raw AC göstergesi 0,00842 görünüyordu; grafikte SCT yaklaşık 0,18–0,30 A çevresinde basamaklıydı. Tek ekran görüntüsü sonuç değildir.
- Kullanıcının 18 W'ta SCT'nin genlik yerine aç/kapa değişimini algıladığı gözlemi doğrulanmamış hipotez olarak ayrı tutuldu.
- E16 gece boyu PZEM V/A, SCT CH1 akım/Raw AC ve iki modülün ON/OFF olay kayıtlarını toplama planıdır. Sabah HA History CSV'si incelenecek.
- Fiziksel yük koşulu ayrıca kaydedilecek; eğitim/kalibrasyon etiketi bu deneyden otomatik üretilmeyecek.
- Ayrıntı: [E16](experiments/E16-sct-on-off-response-idle-low-current/README.md). Durum PLANLANDI; veri ve analiz bekleniyor.


## 2026-11-07 — CH1 yüksüz kapalı alan eşiği (ADR-031)

- Yaklaşık 10 saatlik fiziksel yüksüz CH1 HA History kaydı incelendi: 36.002 ham SCT ve 36.002 K uygulanmış akım örneği.
- K=24.22 uygulanmış akım P95=0,23587365 A; ham SCT P95=0,00973880.
- Kullanıcı kararıyla CH1 kapalı alan sınırı 0,24 A seçildi; örneklerin %96,33'ü bu değerin altında/eşit.
- Sıçramalar filtrelenmedi. Ham CSV depoya eklenmedi; yalnız istatistiksel özet saklandı.
- 0,24 A ile ilk güvenilir okuma arasındaki bölge hesaplanmadı alanıdır; ilk güvenilir okuma ve üzeri hesaplanacak.
- İlk güvenilir okuma eşiği henüz bilinmiyor; sonraki deney hedefi bu sınırı bulmak.
- [I007 istatistik özeti](data/off-noise/sessions/2026-11-07-ch1-closed-area-threshold.md), [ADR-031](docs/decisions/ADR-031-ch1-idle-closed-area-threshold.md).


## 2026-11-07 — E17 CH1 düşük akım sürekli yük gözlemi

- E17 açıldı: CH1'in 0,24 A kapalı alan sınırı üzerindeki düşük akım davranışı sürekli küçük yüklerle incelenecek.
- E17-A: 18 W akkor ampul, 10:21 (Europe/Istanbul) başlangıç; ampul sürekli açık, röle devre dışı. 10:14 civarı PZEM devreye alma hazırlığı deney verisine dahil edilmiyor.
- İlk ekran gözlemi: PZEM 227,1 V / 0,078 A; CH1 yaklaşık 0,277–0,30 A bandında. Kullanıcı kararıyla 0,24–0,41 A aralığı hesaplanmadı alanıdır; burada fiziksel tepki görülse de sayısal akım değeri üretilmeyecek.
- 18 W uzun kayıt sürüyor; CSV analizi ve kararlılık değerlendirmesi beklemede.
- Sonraki ayrı oturum adayı E17-B: 15 W mini buzdolabı ampulü sürekli açık. Farklı tepki gözlemi henüz yeni kayıtla doğrulanmadı.
- Ayrıntı: [E17](experiments/E17-low-current-continuous-load-observation/README.md).


## 2026-11-07 — E18 CH1 bias hattı kontrol deneyi planlandı

- CH1 SCT sensörsüz kontrol deneyi açıldı. CH1 girişi boşta bırakılmayacak; ortak bias okuyan hatta bağlanacak.
- Uzun HA History kaydında CH1 ham SCT/hesaplanmış akım ile mevcutsa ortak bias ve CH2/CH3 serileri karşılaştırılacak.
- Amaç sensör sinyali olmadan ölçüm zinciri sıçramalarını araştırmak; tek başına ESP ADC arızası hükmü vermek değildir.
- Firmware ve ölçüm ayarları sabit kalacak. Fiziksel bağlantı, kayıt ve analiz bekliyor. [E18](experiments/E18-ch1-bias-line-control/README.md).


## 2026-11-07 — BERO kalıcı haberleşme omurgası RS485 olarak kararlaştırıldı

- RS485, BERO'nun kalıcı haberleşme omurgasıdır.
- ESP tabanlı ölçüm düğümleri verilerini RS485 üzerinden bölgesel düğümlere aktaracaktır.
- Wi-Fi geçici haberleşme/aktarım yolu olarak kalır; kalıcı omurga değildir.
- PZEM-014 henüz kullanılmamıştır. Modbus RTU ile PZEM okuma ve ekranlı ESP canlı gösterimi sonraki uygulama işleridir.
- BERO düğümleri arası mesajlaşma protokolü, adresleme, topoloji, baud hızı ve fiziksel katman ayrıntıları henüz kararlaştırılmamıştır.
- **Durum:** Mimari karar depoya işlendi; donanım/firmware/iletişim testi yapılmadı. [ADR-001](../../MIMARI/DECISIONS/ADR-001-rs485-communication-backbone.md).


## 2026-11-07 — RS485 fiziksel kablo yaklaşımı belirlendi

- RS485 A/B, CAT kablo üzerinden taşınacak.
- Transformatör beslemesi aynı kabloyla düğüme götürülecek ve yerinde 5 V'a dönüştürülecek.
- BERO RS485/besleme kablosu, mevcut Ethernet hattından dış kılıf rengiyle ayrılacak; uçlar ayrıca etiketlenecek ve LAN portlarına takılmayacak.
- CAT tipi/pair tahsisi, 24 V DC ana beslemenin kapasitesi, akım, mesafe-gerilim düşümü, dönüştürücü ve koruma tasarımı henüz belirlenmedi.
- **Durum:** Kablolama yaklaşımı kullanıcı kararı olarak kaydedildi; fiziksel kurulum ve elektriksel/haberleşme testi yapılmadı. [ADR-001](../../MIMARI/DECISIONS/ADR-001-rs485-communication-backbone.md).


## 2026-11-07 — E16, E17 ve E18 kapatıldı; Python/eğitim odağı

- **E16 KAPATILDI:** Kullanıcı kararıyla CH1 alt sınırı ve ölü/hesaplanmayan alan belirlendi; aynı alan için ayrı ON/OFF gözlemi tekrarlanmayacak.
- **E17 KAPATILDI:** E17-A 18 W ve E17-B 57 W analizleri mevcut; E17-C 15 W mini buzdolabı ampulü deneyi yeni bilgi üretmeyeceği ve aynı düşük akım alanını tekrar edeceği için yapılmadan kapatıldı.
- **E18 KAPATILDI:** Kullanıcı gözleminde bias hattı CH1'de tekil sıçramalar dışında stabil. Dalgalanmanın ana kaynağı bias hattı olarak sürdürülmeyecek; sıçramaların kesin nedeni teşhis edilmiş sayılmaz.
- **Yeni odak:** T007 Python-1 HA History alım/doğrulama/arşiv; T008 paket bütünlüğü, SCT/PZEM kararlı alan analizi ve etiketleme; ardından cihaz program evreleri için eğitim/bağımsız test.
- **Araştırma sorusu:** Çamaşır makinesi gibi programlı cihazlarda rezistans, motor, pompa, valf ve yardımcı yükler hangi akım/genlik/zaman örüntülerini üretir; bu örüntüler SCT verisinden ayırt edilebilir mi?
- SCT'nin 2 A altındaki performansı açık sorudur. Ölçüm doğruluğu, güç/akım gözlemi, geçiş tepkisi ve program evresi sınıflandırma başarısı ayrı ölçütlerdir. Yeterlilik sonucu veri analizi ve eğitim testinden sonra verilecektir.

## 2026-11-13 — E19 düşük akım çalışma sınırı aşaması
- [E19 deney tanımı](experiments/E19-ads1115-low-current-alternative/README.md): mevcut aşama katsayı kalibrasyonu değil; mevcut ayar/katsayıyla düşük akım davranışı ve alt çalışma sınırını belirleme.
- [E19 protokolü](experiments/E19-ads1115-low-current-alternative/protocol.md): ayarlar/katsayı sabit, yük basamakları aşağı doğru, PZEM aynı zaman penceresinde karşılaştırma referansı.
- [E19 sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md): 57 W ön gözlemi 0,265 A PZEM / 0,270 A ADS1115+SCT; kaba katsayı, kalibrasyon yapılmadı.
- [57 W test kaydı](logs/ads1115/2026-11-13-E19-57w-test.md): kullanıcı bildirimi, +0,005 A / yaklaşık +%1,89 hesap ve kanıt sınırı.
- [Oturum kaydı](HISTORY/SESSION_LOG-2026-11-13-E19-low-current-range.md).

### E19 — 57 W oturum kapanışı (18:40)
- Kullanıcı oturumu 18:40 (+03:00) itibarıyla kapattı.
- `history (57).csv` ön analizi: 18:35–18:40 ADS1115 n=150, mean 0.266212 A, SD 0.000985 A; PZEM n=18, mean 0.264500 A, SD 0.000514 A; fark yaklaşık +%0.647.
- Bu, 100 W'taki kaba PZEM ayarından sonra düşük akım karakterizasyonudur; bu aşamada katsayı değiştirilmez.
- Ayrıntı: [57 W test raporu](logs/ads1115/2026-11-13-E19-57w-test.md), [E19 sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md), [oturum kaydı](HISTORY/SESSION_LOG-2026-11-13-E19-low-current-range.md).

### E19 — 42 W basamağı açıldı (18:44)
- Kullanıcı bildirimi: 42 W nominal yük, başlangıç 18:44 (+03:00); 57 W basamağı 18:40'ta kapatıldı.
- Mevcut katsayı/ayar sabit; bu basamak kalibrasyon değil, düşük akım çalışma davranışı karakterizasyonudur.
- CSV ve kapanış bilgisi bekleniyor: [42 W test kaydı](logs/ads1115/2026-11-13-E19-42w-test.md).


## 2026-11-13 — E19 42 W sabit yük basamağı tamamlandı

- 42 W nominal yük oturumu kullanıcı tarafından 18:50'de kapatıldı (başlangıç 18:44, +03:00).
- CSV ortak kesiti 18:44:07–18:49:59: ADS1115 + SCT n=176, ortalama 0.189236 A, SD=0.001014 A, CV=%0.536; PZEM n=9, ortalama 0.189000 A, SD=0.001000 A.
- Ortalama fark yaklaşık +%0.125; PZEM örnek sayısı düşük olduğundan doğruluk kanıtı değildir. PZEM aktif güç ortalaması 43.452 W (n=31).
- Katsayı ve ayarlar değiştirilmedi. Sonuç düşük akım karakterizasyonu olarak kaydedildi; kalibrasyon/±%4 kabulü veya alt sınır kararı değildir.
- Ayrıntılar: [42 W test raporu](logs/ads1115/2026-11-13-E19-42w-test.md), [E19 sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md).


## 2026-11-13 — E19 18 W sabit yük gözlemi tamamlandı; aç/kapa testine geçiş

- `history (59).csv` analiz edildi (3.798 satır; SHA-256 `64de1d73afa4f716eef93793d62911b247dd18dd4d2063efd8aec077da5c9b52`).
- Ortak pencere 18:54:17.903–19:00:02.859 (+03:00): ADS1115 + aynı SCT n=173, ortalama 0.078715 A, SD=0.000373 A; PZEM n=18, ortalama 0.079500 A, SD=0.000514 A; PZEM güç n=32, ortalama 18.269 W.
- ADS1115/PZEM ortalama farkı −0.000785 A / yaklaşık −%0.99; bu 18 W oturumunda ±%4 beklentisinin içindedir. Bu tek oturumluk gözlemdir; tüm aralık için kabul veya kalibrasyon değildir.
- Yüksüz ön bölümde ADS1115 0.00 A kayıtları, yük oturduktan sonra yaklaşık 0.0787 A kararlı değerler gözlendi. Aynı SCT sensörünün ADS1115 ölçüm zinciriyle eski dahili ADC yolunda sorun yaşanan düşük akım bölgesine indiği yönünde umut verici kanıt oluştu.
- 18 W sabit yük baz gözlemi kapatıldı; ADS1115 zinciri BERO için umut verici ana ölçüm adayı olarak değerlendirilecek. Nihai donanım onayı verilmedi.
- Sonraki aşama: aç/kapa tepki deneyi. Fiziksel ON/OFF, PZEM akım/güç ve SCT davranışıyla doğrulanacak; UDP/SSR olayı tek başına fiziksel durum kanıtı değildir. CSV'deki SSR OFF olaylarından sonra PZEM'in 18 W göstermeyi sürdürmesi bu ayrımı doğruluyor.
- ADS1115 A0/A1 common-mode ve giriş ray güvenliği fiziksel doğrulaması açık kalır.
- Ayrıntı: [E19 18 W test raporu](logs/ads1115/2026-11-13-E19-18w-test.md), [E19 sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md), [oturum kaydı](HISTORY/SESSION_LOG-2026-11-13-E19-low-current-range.md).


## 2026-11-13 — E20 18 W fiziksel aç/kapa tepki deneyi açıldı

- E19 18 W sabit yük baz gözlemi tamamlandıktan sonra yeni ve ayrı dinamik tepki deneyi E20 açıldı.
- Amaç: aynı SCT-013 30A/1V + ADS1115 zincirinin 18 W fiziksel yük açma/kapatma geçişini, OFF sonrası yüksüz tabana dönüşünü, gecikme/sıçrama ve beş çevrimde tekrarlanabilirliğini incelemek.
- Önerilen sıra: başlangıç OFF 180 s; 5 çevrim × (ON 60 s + OFF 60 s); son OFF 180 s. Gerçek süreler oturumda kaydedilecek.
- ADS1115 gain 2.048, 860 SPS, continuous, 200 ms pencere, 2 s yayın, accuracy_decimals 2 ve 0.05 A filtre korunacak; katsayı değiştirilmeyecek.
- Fiziksel yük anahtarlaması operatörce doğrulanacak. PZEM akım/güç geçişi fiziksel ON/OFF doğrulaması; SSR/UDP olayları tek başına fiziksel durum kanıtı değildir.
- E20 dinamik geçiş testi olduğundan geçiş örneklerine ±%4 uygulanmaz; kararlı ON/OFF seviyeleri ve çevrimler ayrı analiz edilir.
- **Durum:** PLANLANDI; fiziksel test ve CSV henüz yok.
- [E20 deney protokolü](experiments/E20-ads1115-18w-on-off-response/README.md); [sonuç defteri](experiments/E20-ads1115-18w-on-off-response/results.md).


## 2026-11-15 — RT-209 ana modül kutusu fikri kaydedildi
- Ayrı imalat/modül dosyası açıldı: [BERO 12 Kanallı Ölçüm Modülü — RT-209](manufacturing/BERO-12CH-RT209/README.md).
- RT-209 yalnızca **kutu adayıdır**. İki ESP32 terminal shield, altı ADS1115, 12 SCT dişi jack, iki RS485 ve iki bağımsız reset butonu yerleşimi fikir düzeyindedir.
- Delikli board/pertinaks taşıyıcı, sökülebilir ESP32 soketleri ve panel jack bağlantısı düşünülüyor. Ölçülü yerleşim, elektriksel tasarım, imalat veya test yapılmadı.
