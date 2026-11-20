## 2026-11-16 — ADS1115 teslimatı sonrası yeni ölçüm modülü kararı
- Kullanıcı değerlendirmesi: mevcut ölçüm zincirinin ölçüm kalitesinden genel olarak memnun; mevcut yapı BERO'nun şu anki gözlem amacına hizmet ediyor.
- Plan: yeni ADS1115 sensör/modülleri teslim edildiğinde mevcut modül sökülecek ve yeni modül yapısı kurulacak.
- Bu ifade kullanıcı değerlendirmesi ve gelecek çalışma planıdır; yeni modül henüz kurulmuş, derlenmiş veya test edilmiş değildir. Mevcut ölçüm kalitesine ilişkin yeni bir sayısal doğrulama bu notla yapılmış sayılmaz.
- Yeni modül kurulurken mevcut çalışan ölçüm zincirinin ayarları ve sonuçları korunacak; değişiklikler yeni modül/deney kaydı altında izlenecek.

## 2026-11-16 — E21 çamaşır makinesi kısa/uzun tam program kayıtları ve ilk nitel gözlem
- Kullanıcı düzeltmesi: **kısa ve uzun kayıtların ikisi de baştan sona tam programdır**. Kısa kayıt yalnızca ısınma evresi değildir.
- Kısa kayıt dosyası: `wm-kısa-prg-2026-11-14.csv` (önceki sohbet kaydında bildirilen ad); uzun kayıt dosyası: `wm-uzun pamuklu 60 - 2026-11-14.csv` (kullanıcı kitaplığı ekran görüntüsünde görülen ad).
- Uzun kayıt program etiketi dosya adına göre **Pamuklu 60°**; paneldeki gerçek program adı/ayarların tam teyidi ayrı tutulur.
- Kullanıcının daha önce paylaştığı görsel ve sohbetten gelen ilk nitel yorum: **ısıtma, tamburun sağa-sola dönüşleri ve sıkma davranışları gözlenebiliyor**. Bu, ön gözlem notudur; kesin evre sınıflandırması veya zaman ölçümü değildir.
- Her iki kayıt için ayrı RECORD_ID kullanılır: `WM-20261114-02` kısa, `WM-20261114-01` uzun. PROGRAM_ID henüz atanmadı.
- Ham CSV'lerin kullanıcı kitaplığında bulunması, bunların repo arşivine kopyalandığı veya Python ile analiz edildiği anlamına gelmez. İçerik analizi, zaman serisi korelasyonu ve daha fazla program kaydı sonraki aşamadır.
- E21 durumu: **ön kayıt/gözlem mevcut; veri toplama ve analiz devam edecek**. Çalışma yapılmamış gibi PLANLANDI durumunda bırakılmayacak; analiz tamamlandı da denmeyecek.



## 2026-11-14 — E24 güncellemesi: 3 ADS1115 + 1 ESP32 / 6 SCT test hedefi
- Kullanıcı netleştirmesi: eldeki iki ADS1115'ten **biri çalışıyor, diğeri arızalı**.
- Yeni siparişlerin teslimi bekleniyor; sipariş adedi ve teslim içeriği bu kayıtta varsayılmadı.
- Güncel test hedefi: **tek ESP32 + 3 ADS1115 + 6 SCT**. Her ADS için ayrı SDA/SCL çifti tercih ediliyor; klasik ESP32'de yalnız iki donanımsal I²C kontrolcüsü olduğundan üçüncü hat (öncelikle yazılımsal I²C) gerçek kart/framework üzerinde doğrulanmalı.
- Üç ADS modülü tek tek doğrulandıktan sonra üç bus birlikte çalıştırılacak; altı kanal önce güvenli DC seviyelerle, ardından analog giriş güvenliği doğrulanırsa SCT ile test edilecek.
- Kayıt metrikleri: kanal başına efektif SPS, altı kanal çevrim süresi, dönüşüm/okuma gecikmesi, jitter, I²C hata/timeout, eksik/tekrar örnek.
- İlk testte RS485 yok. Firmware, pin planı ve fiziksel test henüz yapılmadı. Ayrıntı: [E24 protokolü](experiments/E24-ads1115-multi-bus-expansion/README.md).

## 2026-11-14 — E24 ilk test kapsamı ve nihai tek ESP hedefi netleştirildi
- Kullanıcı düzeltmesi: **nihai hedef tek ESP32 üzerinde 6 SCT kanalını okumak**; 12 kanal hedefi iki aynı 6 kanallı düğümün tekrarıdır.
- İlk aşama nihai tasarım değildir: eldeki 2 ADS1115 + 1 ESP32 ile **4 SCT kanalını birlikte okuma** testi yapılacak.
- Dört kanallı testte ADC erişimi yanında kanal çevrim süresi, gecikme, hata/timeout ve veri kaybı incelenecek.
- Sonraki aşamada aynı ESP32 üzerinde 3 ADS1115 ile 6 SCT hedefine geçilecek. Klasik ESP32'de iki donanımsal I²C kontrolcüsü bulunduğundan üçüncü ADS bağlantı yöntemi ayrıca çözülecek.
- Altı kanallı fiziksel modül şu anda hazır değil; imalat öncesi ilk doğrulama dört kanalla yapılacak.
- E24 ayrıntısı: [E24 protokolü](experiments/E24-ads1115-multi-bus-expansion/README.md).

## 2026-11-14 — E24 çoklu ADS1115 test planı ve 12 SCT simetrik mimari adayı
- Kullanıcı kararı: yeni modül imalatından önce eldeki **2 ADS1115** ile ilk test yapılacak. Modüllerden biri önceki denemede çalışmamış olabilir; arızalı olduğu kesin değil, yeniden kontrol edilecek.
- İlk test: iki ADS1115'i ayrı ayrı doğrulamak; ardından tek ESP32 üzerinde iki ayrı donanımsal I²C bus/SDA-SCL çiftiyle birlikte okuma, dönüşüm/okuma süresi ve hata davranışını ölçmek.
- Kullanıcı mimari adayı: **2 aynı ESP32 ölçüm düğümü; her ESP başına 3 ADS1115 ve 6 SCT kanalı; her ADS için ayrı SDA/SCL çifti; her ölçüm ESP'sinde 1 RS485 dönüştürücü; toplam 12 SCT**.
- **Önemli doğrulama:** klasik ESP32'de iki donanımsal I²C kontrolcüsü vardır. Üçüncü ayrı donanımsal I²C hattı doğrudan varsayılamaz. Üç ADS/ESP hedefi için üçüncü yazılımsal I²C, I²C çoklayıcı veya ortak bus/ayrı adres seçeneği test edilip kararlaştırılacak. Bu nedenle 12 kanal mimarisi kesinleşmiş değildir.
- Kullanıcı, ilk iki ADS testi başarılı olursa tedarik/gümrük gecikmelerine karşı **10 adet ADS1115 yedek stok siparişi** vermeyi planlıyor. Sipariş henüz verilmedi; mevcut eldeki iki modül ayrı envanter kalemi.
- **E24: PLANLANDI.** Kod, bağlantı şeması, derleme ve donanım testi henüz yapılmadı. Ayrıntı: [E24 protokolü](experiments/E24-ads1115-multi-bus-expansion/README.md).
## 2026-11-14 — E21 ilk tam çamaşır makinesi program kaydı planlandı
- Kullanıcı bugün gün içinde bir tam programı baştan sona kaydetmeyi planlıyor; makinenin başlatılacağı zaman için evden haber bekleniyor. Kayıt henüz başlamadı.
- İlk çekim kimliği: **WM-20261114-01**. Geçici açıklama etiketi: **UZUN**; paneldeki gerçek program adı henüz bilinmiyor.
- Kalıcı sınıflandırma kuralı: her çekim ayrı RECORD_ID alır (`WM-YYYYMMDD-NN)); aynı program adı ve anlamlı ayar kombinasyonları doğrulanınca PROGRAM_ID (`WMP-NNN`) atanır. PROGRAM_ID şimdilik atanmadı.
- Ham CSV korunacak; metadata, analiz ve segment tablosu ayrı dosyalar olacak. İlk kayıt önce baştan sona alınacak, ardından tarafsız akım bölümleri çıkarılacak.
- Kayıt şablonu: [WM-20261114-01](logs/washing-machine/WM-20261114-01/README.md). E21 standardı: [E21 README](experiments/E21-washing-machine-program-analysis/README.md).

## 2026-11-14 — E23 yeni modülle ADS1115 sıçrama araştırmasının devamı
- Kullanıcı kararı: Önceki E19 enerjili-hat/yüksüz-iletken gözleminde görülen sıçramalar, aç/kapa mekanizması/kodları aktif düzenden çıkarıldıktan ve yeni modül kurulduktan sonra yeniden uzun kayıt alınarak araştırılacak.
- Fiziksel koşul kullanıcı tarafından netleştirildi: gözlenen hatta aç/kapa yapılmıyor, röle bu hatta bağlı değil; anahtarlama başka ESP üzerinden yürütülüyor. Önceki HA switch state geçişleriyle zaman yakınlığı nedensellik veya ölçülen hattın röleyle anahtarlanması kanıtı değildir.
- Önceki E19 istatistikleri karşılaştırma baseline'ı olarak korunur; E19 oturumu kapanmıştır. Sıçramaların fiziksel nedeni açık kalır.
- Yeni modülün donanım/firmware/ADS ayarları henüz kesinleştirilmedi. Akşam uzun kayıt ve karşılaştırma henüz yapılmadı.
- **E23: PLANLANDI — yeni modül ile ADS1115 yüksüz sıçrama karşılaştırması.** Yeni kayıt önceki E19 raporuyla aynı istatistikler üzerinden kıyaslanacak; koşul farkları açıkça kaydedilecek.
- Ayrıntı: [E23 deney protokolü](experiments/E23-ads1115-spike-new-module-comparison/README.md).

## 2026-11-14 — E19 ADS1115 sıçrama yorumuna kullanıcı düzeltmesi ve yeni modül karşılaştırması
- Kullanıcı fiziksel koşulu netleştirdi: ADS1115'in ölçtüğü hatta aç/kapa yapılmıyor; röle bu hatta bağlı değil. Anahtarlama başka bir ESP tarafından yürütülüyor; ADS1115 ESP'siyle aynı cihaz değil.
- Önceki rapordaki 72 sapma örneğinin 57'sinin HA switch state geçişine 10 saniye içinde denk gelmesi yalnızca zamansal yakınlıktır. Bu ilişki artık ölçülen hatta anahtarlama veya doğrudan röle etkisi olarak yorumlanmayacak.
- Güncel hipotez: ayrı ESP'deki anahtarlama sırasında oluşan olası parazit/kuplaj ADS1115 ölçüm zincirini etkiliyor olabilir. Mekanizma ve nedensellik kanıtlanmadı.
- Kullanıcı bugün aç/kapa mekanizmasını/kodlarını çıkaracağını, kodları yenileyip yeni modül oluşturacağını ve akşam uzun kayıt alacağını bildirdi. Yeni kayıt önceki E19 istatistikleriyle aynı metrikler üzerinden karşılaştırılacak.
- Önceki E19 yüksüz gözlem raporu sayısal temel olarak korunur; sıçrama nedeni açık kalır. Yeni kayıt henüz alınmadı.
- Ayrıntı: [E19 sıçrama nedeni yeniden değerlendirme ve karşılaştırma planı](logs/ads1115/2026-11-14-E19-spike-cause-reassessment.md).

## 2026-11-14 — E19 ADS1115 enerjili-yüksüz gözlem CSV analizi ve test kapanışı

- Kullanıcının `uzun 1115 boşta .csv` dosyası analiz edildi: 16.260 toplam satır; ADS1115 akım entity'sinde 1.679 kayıt, 1.669 sayısal state ve 10 `unavailable`.
- ADS1115 sayısal kayıtlarının 1.592'si (%95,39) 0,005 A veya altındadır. Bu grubun ortalaması 0,00122955 A, medyanı 0,00128425 A, örnek SD'si 0,00028426 A'dır. 76 adet tam sıfır state vardır.
- 0,040 A ve üzerindeki 72 state (%4,31) ayrı sapma grubu oluşturur; medyan 0,046599 A, ortalama 0,051456 A. En yüksek değer 0,353055 A'dır.
- Bu 72 örneğin 57'si (%79,17) en yakın HA switch entity state geçişinden 10 saniye içinde görülmüştür. Bu yalnızca zamansal yakınlıktır; fiziksel SSR hareketi veya nedensellik kanıtı değildir.
- PZEM akım entity'sinde yalnızca 3 state vardır: 0,0 A → unavailable → 0,0 A. Bu nedenle PZEM'in tüm kayıt boyunca sürekli sıfır gösterdiği ileri sürülmez.
- **Bu test kapatıldı:** enerjili hat / ölçülen iletkende yüksüz durumun uzun dönem gözlemi analiz edilip raporlandı. Sapmaların fiziksel nedeni teşhis edilmiş değildir.
- Ayrı enerjisiz hat taban testi yapılmış veya kapanmış sayılmaz. ADS1115 A0/A1 ortak-mod ve giriş ray güvenliği doğrulaması açık kalır; bu rapor yeni enerjili test için güvenlik onayı değildir.
- Ham CSV'nin dosya boyutu ve SHA-256 değeri rapora işlendi. Ham 1,4 MB CSV Git'e eklenmedi; rapor, özet istatistik CSV'si ve 0,005 A üzerindeki 77 örneklik olay dökümü depoya eklendi.
- [İstatistiksel rapor](logs/ads1115/2026-11-14-E19-energized-no-load-statistical-report.md) · [Özet istatistikler](logs/ads1115/2026-11-14-E19-energized-no-load-statistics.csv) · [Olay örnekleri](logs/ads1115/2026-11-14-E19-energized-no-load-event-samples.csv).


## 2026-11-13 — Modül envanteri yeniden düzenlendi: Modül 4 planı

- **Modül 1:** bağımsız bias trafosu / taşınabilir bias güç kutusu korunacak. Envanterde mevcut fiziksel varlık olarak kalır.
- **Modül 2:** üç kanallı biaslı SCT okuma modülü; Modül 1'in bias yapısını da içeren eski kurulum. Kullanıcı bildirimi: fiziksel modül **İMHA EDİLDİ**.
- **Modül 3:** PZEM ve aç/kapa rölesi içeren eski kurulum. Kullanıcı bildirimi: eski modül **İMHA EDİLDİ**. Modül 3'ün eski röle/kontrol yapısı yeni modüle taşınmayacak.
- **Modül 4:** yeni ESP32 + ADS1115 + 100 A / 1 V SCT + PZEM-004T V3 ölçüm modülü olarak oluşturulacak. PZEM-004T V3, yeni Modül 4 tasarımında kullanılacak bileşen olarak planlandı; fiziksel yeniden bağlantı/çalışma henüz doğrulanmadı.
- Modül 2 ve 3'ün eski firmware/YAML, log, deney ve karar kayıtları **silinmeyecek**; tarihsel arşiv olarak korunacak. Modül 4 ayrı YAML ve ayrı firmware kimliğiyle geliştirilecek.
- 30 A / 1 V ADS1115 kodu değiştirilmeden korunacak. 100 A / 1 V için ayrı sensör tanımı ve ayrı kalibrasyon/sonuç kaydı tutulacak.
- Modül 4'ün pinleri, ADS1115 giriş bağlantısı/güvenliği, PZEM UART pinleri ve seri haberleşme ayarları donanım kontrolü sonrasında belirlenecek. Bu kayıt kodun hazır, derlenmiş veya cihaza yüklenmiş olduğu anlamına gelmez.
- İlgili çalışma: [E22 — 100 A / 1 V SCT + ADS1115 karakterizasyonu](experiments/E22-sct100a-1v-ads1115-characterization/README.md).

## 2026-11-13 — E22 planlandı: SCT 100 A / 1 V – ADS1115 karakterizasyonu

- Kullanıcı bildirimi: elinde **8 adet 100 A / 1 V SCT** bulunuyor. Adet/model etiketi fiziksel envanter kontrolünde teyit edilecek.
- Kullanıcı kararı: 100 A / 1 V sensör için mevcut 30 A / 1 V firmware'inden ayrı bir YAML/kod snapshot'ı tutulacak; iki sensörün katsayıları ve sonuçları birbirine karıştırılmayacak.
- Kullanım fikri: 100 A / 1 V sensör, ileride ana hat gibi daha yüksek akım aralığı beklenen noktalarda değerlendirilebilir. Kullanıcıya göre 30 A / 1 V sensör mevcut kullanım noktalarının çoğuna yeterli; 100 A sensörler alternatif/yüksek aralık stoğu olarak korunacak.
- **Önemli teknik beklenti:** 100 A / 1 V sensörün akım başına çıkışı, 30 A / 1 V sensöre göre nominal olarak daha düşüktür. Bu nedenle 100 A modeli düşük akım hassasiyetini otomatik olarak iyileştirmez; yüksek akım aralığı/headroom açısından değerlendirilir.
- Deney amacı: 100 A / 1 V sensörün ADS1115 + ESP32 + mevcut RMS yazılım zincirindeki çalışma aralığını, kararlılığını, gürültüsünü, tekrarlanabilirliğini ve PZEM referansına göre davranışını karakterize etmek.
- Deneyde sensör modeli, bağlantı, ADS1115 gain/rate, ct_clamp penceresi, update interval ve kalibrasyon katsayısı ayrı kaydedilecek. 30 A / 1 V katsayısı 100 A / 1 V'e kopyalanmayacak; 100 A kodu ayrı katsayı alanı taşıyacak. Katsayı test verisi olmadan belirlenmiş sayılmayacak.
- Planlanan ayrı firmware yolu: `firmware/experiments/esp32d2-ads1115-sct100a-1v.yaml`. Bu dosya henüz oluşturulmadı; test öncesi mevcut çalışan ADS1115 YAML'ı temel alınarak ayrı snapshot üretilecek. Canlı 30 A / 1 V kodu üzerine yazılmayacak.
- Karşılaştırma: mümkünse aynı kararlı yük koşullarında 30 A / 1 V ve 100 A / 1 V ayrı oturumlarda PZEM'e karşı gözlenecek. Düşük, orta ve güvenli biçimde erişilebilen daha yüksek akım noktaları seçilecek; gerçek akım her basamakta PZEM ile kaydedilecek.
- **Güvenlik kapısı:** SCT sekonderi, primer iletkenden akım geçerken açık devre bırakılmayacak. ADS1115 giriş ortak-mod ve GND–VDD sınırları, sensör çıkış seviyesi ve giriş koruması fiziksel olarak doğrulanmadan enerjili test yapılmayacak. Test akımı/hat bağlantısı uygun koruma ve güvenli düzenekle sınırlanacak.
- Durum: **PLANLANDI — kod, derleme, OTA ve fiziksel test yapılmadı.** Sonuç veya kalibrasyon iddiası yok.
- Ayrıntılı protokol: [E22 README](experiments/E22-sct100a-1v-ads1115-characterization/README.md).

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
- Kaynak ayrımı: kullanıcının 606 satırlık çalışan YAML'ı 27.60 katsayısı ve UDP alıcısı içerir; iki değişiklik uygulanmış tam 606 satırlık snapshot [burada](firmware/experiments/esp32d2-ads1115-ct-clamp-live-27.60-003A-1s.yaml) saklandı. Depodaki kısa referans YAML farklıdır.
- Derleme/OTA çıktısı bu oturumda mevcut değildir; kodun cihazda çalışması kullanıcı canlı test bildirimiyle desteklenmektedir, bağımsız derleme doğrulaması değildir.

## 2026-11-13 — E21 ilk çamaşır makinesi kaydı başladı; ON/OFF kod temizliği yapılacak

- Kullanıcı bildirimi: kayıt 20:42'de, çamaşır makinesi programı devam ederken ortasından başlatıldı; bu nedenle **kaba ve kısmi kayıt** olarak değerlendirilecek. Program bitene kadar kayıt sürdürülecek.
- **YAPILACAK İŞ:** Artık ihtiyaç kalmadığı için canlı/aktif firmware ve ilgili kodlardan ON/OFF olay mekanizması tamamen çıkarılacak.
- Kapsam taraması: Modül 2, Modül 3 ve bunlarla ilişkili diğer kodlar; UDP ON/OFF gönderme/alma, olay parser'ı, BOOT_ID/EVENT_ID/STATE alanları, olay entity'leri ve yalnız bu mekanizmaya bağlı yardımcı değişkenler.
- Ölçüm, sensör okuma, HA akım verisi ve kayıt akışı korunacak. Tarihsel ADR, deney, log ve arşiv dosyaları silinmeyecek; yalnız aktif koddan çıkarılacak.
- Bu bir yapılacak iş kaydıdır; henüz kod değişikliği, derleme, OTA veya fiziksel doğrulama yapılmadı.

## 2026-11-13 — E21 ilk test kapsamı netleştirildi

- İlk test yalnızca **bir çamaşır makinesi programının baştan sona kaba kaydıdır**; ayrıntılı evre sınıflandırması, tekrar testi veya eğitim modeli hedeflenmiyor.
- İlk çıktı: tek akım grafiği, belirgin genel değişimler ve dikkat çeken zaman aralıkları.
- İlk kayıttan sonra farklı sensörler seçilip sisteme aşamalı olarak eklenecek; çoklu sensör kombinasyonları sonraki aşamadır. Sensör türü/bağlantısı henüz kararlaştırılmadı.
- [E21 güncel protokolü](experiments/E21-washing-machine-program-analysis/README.md).

## 2026-11-13 — Yeni hedef E21: çamaşır makinesi program davranışı analizi

- **AKTİF HEDEF:** Çamaşır makinesinin seçilen bir programını baştan sona SCT-013 + ADS1115 akım zaman serisiyle gözlemlemek; elektriksel davranış evrelerini, sürelerini, geçişlerini ve tekrar eden örüntülerini çıkarmak.
- Kullanıcı kararı: PZEM ile bağımsız kararlı alan eşleştirmesi/eğitim ve bu amaçla aç-kapa deneyleri artık gerekli değil; mevcut ölçüm zinciri pratik hedefi karşılıyor.
- Önceki kararlı-alan eğitim/kalibrasyon iş akışı **KAPATILDI — HEDEFE ULAŞILDI**. Bu ifade tüm olası akım koşullarında laboratuvar doğruluğu veya nihai donanım güvenliği sertifikası değildir; 13 Kasım testlerinin pratik hedefi karşıladığına dair kullanıcı kararıdır.
- E20, 18 W aç/kapa tepki deneyi plan aşamasındaydı; yeni hedef için gereksiz bulunduğu için **KAPATILDI — YAPILMADI**. Fiziksel deney tamamlanmış sayılmaz.
- E19, E20, T008/T006, ADR'ler, loglar, eski protokoller ve ham veriler silinmez; tarihsel arşiv olarak korunur. Firmware, YAML, katsayı ve ayarlar bu kararla değiştirilmedi.
- PZEM yeni hedefte zorunlu eğitim referansı değildir; varsa yardımcı karşılaştırma/bağlam verisi olarak korunabilir.
- **E21 protokolü:** [Çamaşır makinesi program davranışı analizi](experiments/E21-washing-machine-program-analysis/README.md).
- **Karar kaydı:** [ADR-026](docs/decisions/ADR-026-close-stable-window-training-open-washer-analysis.md).
- **Açık güvenlik koşulu:** ADS1115 A0/A1 ortak-mod ve giriş ray sınırlarının fiziksel doğrulaması yapılmış sayılmaz; uygun doğrulama olmadan enerjili test güvenli kabul edilmez.



## 2026-11-13 — E20 18 W fiziksel aç/kapa tepki deneyi açıldı

- E19 18 W sabit yük baz gözlemi tamamlandıktan sonra yeni ve ayrı dinamik tepki deneyi E20 açıldı.
- Amaç: aynı SCT-013 30A/1V + ADS1115 zincirinin 18 W fiziksel yük açma/kapatma geçişini, OFF sonrası yüksüz tabana dönüşünü, gecikme/sıçrama ve beş çevrimde tekrarlanabilirliğini incelemek.
- Önerilen sıra: başlangıç OFF 180 s; 5 çevrim × (ON 60 s + OFF 60 s); son OFF 180 s. Gerçek süreler oturumda kaydedilecek.
- ADS1115 gain 2.048, 860 SPS, continuous, 200 ms pencere, 2 s yayın, accuracy_decimals 2 ve 0.05 A filtre korunacak; katsayı değiştirilmeyecek.
- Fiziksel yük anahtarlaması operatörce doğrulanacak. PZEM akım/güç geçişi fiziksel ON/OFF doğrulaması; SSR/UDP olayları tek başına fiziksel durum kanıtı değildir.
- E20 dinamik geçiş testi olduğundan geçiş örneklerine ±%4 uygulanmaz; kararlı ON/OFF seviyeleri ve çevrimler ayrı analiz edilir.
- **Durum:** PLANLANDI; fiziksel test ve CSV henüz yok.
- [E20 deney protokolü](experiments/E20-ads1115-18w-on-off-response/README.md); [sonuç defteri](experiments/E20-ads1115-18w-on-off-response/results.md).


## 2026-11-13 — E19 18 W sabit yük gözlemi tamamlandı; aç/kapa testine geçiş

- `history (59).csv` analiz edildi (3.798 satır; SHA-256 `64de1d73afa4f716eef93793d62911b247dd18dd4d2063efd8aec077da5c9b52`).
- Ortak pencere 18:54:17.903–19:00:02.859 (+03:00): ADS1115 + aynı SCT n=173, ortalama 0.078715 A, SD=0.000373 A; PZEM n=18, ortalama 0.079500 A, SD=0.000514 A; PZEM güç n=32, ortalama 18.269 W.
- ADS1115/PZEM ortalama farkı −0.000785 A / yaklaşık −%0.99; bu 18 W oturumunda ±%4 beklentisinin içindedir. Bu tek oturumluk gözlemdir; tüm aralık için kabul veya kalibrasyon değildir.
- Yüksüz ön bölümde ADS1115 0.00 A kayıtları, yük oturduktan sonra yaklaşık 0.0787 A kararlı değerler gözlendi. Aynı SCT sensörünün ADS1115 ölçüm zinciriyle eski dahili ADC yolunda sorun yaşanan düşük akım bölgesine indiği yönünde umut verici kanıt oluştu.
- 18 W sabit yük baz gözlemi kapatıldı; ADS1115 zinciri BERO için umut verici ana ölçüm adayı olarak değerlendirilecek. Nihai donanım onayı verilmedi.
- Sonraki aşama: aç/kapa tepki deneyi. Fiziksel ON/OFF, PZEM akım/güç ve SCT davranışıyla doğrulanacak; UDP/SSR olayı tek başına fiziksel durum kanıtı değildir. CSV'deki SSR OFF olaylarından sonra PZEM'in 18 W göstermeyi sürdürmesi bu ayrımı doğruluyor.
- ADS1115 A0/A1 common-mode ve giriş ray güvenliği fiziksel doğrulaması açık kalır.
- Ayrıntı: [E19 18 W test raporu](logs/ads1115/2026-11-13-E19-18w-test.md), [E19 sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md), [oturum kaydı](HISTORY/SESSION_LOG-2026-11-13-E19-low-current-range.md).


## 2026-11-13 — E19 57 W sabit yük testi açıldı

- Kullanıcı düzeltmesi: sıradaki yük 58 W değil **57 W**; başlangıç saati **18:32 (+03:00)**.
- 57 W sürekli bağlı sabit yük oturumu açıldı; bu aşamada yalnız başlangıç bildirimi vardır, cihaz logu/CSV veya ölçüm sonucu yoktur.
- 150 W CSV deneyiminden sabit yük yöntemine eklenen not: ilk yaklaşık iki dakikada PZEM akım/güç yükselişi gözlendi. Yeni testlerde ilk 3 dakika geçici bölge sayılacak; kararlı pencere saatle değil, PZEM ve ADS/SCT serilerinin gerçekten oturmasıyla seçilecek.
- PZEM aynı ortak kararlı pencerenin referansıdır; nominal watt teorik akım hesabı kalibrasyon girdisi değildir.
- İlk 57 W karşılaştırmasında gain 2.048, 860 SPS, 200 ms, 2 s, accuracy_decimals 2, 0.05 A filtre ve çalışan katsayı korunacak. 0.512 gain / 3 basamak yayın ertelendi.
- Bias/common-mode ve ADS1115 A0/A1 giriş sınırları fiziksel olarak doğrulanmadan enerjili teste devam edilmemeli.
- Rapor: [E19 57 W test kaydı](logs/ads1115/2026-11-13-E19-57w-test.md); sabit yük yöntem notları: [test yükleri indeksi](test-loads/README.md).


## 2026-11-13 — E19 150 W sonucu kaydedildi; 58 W testi açıldı

- 150 W sabit yük CSV'si (`history (56).csv`) ortak kararlı 18:16:30–18:24:30 (+03:00) penceresinde analiz edildi.- PZEM n=39, ortalama 0.65472 A, SD=0.00092 A; güç ortalaması 149.69 W.
- ADS1115 n=241, ortalama 0.66279 A, SD=0.00172 A; PZEM'e göre +%1.23.
- Modül 2 CH1-1T n=480, ortalama 0.60402 A, SD=0.01357 A; PZEM'e göre -%7.74.
- İlk yaklaşık iki dakikadaki lamba oturma bölümü kararlı karşılaştırma dışında tutuldu. Yük deney boyunca sürekli bağlı sabit yük olarak ele alındı; SSR olayları yük ON/OFF etiketi yapılmadı.
- K=27.60'ın çalışan binary'de kullanıldığı henüz doğrulanmadı. Bu varsayımla hesaplanan K≈27.26 koşullu hesaptır; hiçbir katsayı değiştirilmedi.
- Gain 2.048, 860 SPS, 200 ms pencere, 2 s güncelleme, accuracy_decimals 2 ve 0.05 A filtre korundu.
- **Aşama 4: 58 W sabit yük testi PLANLANDI.** İlk karşılaştırmada aynı firmware/ayarlar korunacak; 0.512 gain ve accuracy_decimals 3 değişiklikleri ertelendi.
- Bias/common-mode ve A0/A1 giriş güvenliği enerjili test öncesi açık ön koşuldur.
- Rapor: [150 W karşılaştırma](logs/ads1115/2026-11-13-E19-150w-comparison.md); [58 W planı](logs/ads1115/2026-11-13-E19-58w-test-plan.md).
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

## 2026-11-20 — E19 ADS1115 düşük akım karakterizasyonu kapatıldı
- E19 kapsamında 18 W, 42 W, 57 W, 100 W ve 150 W sabit yük karşılaştırmaları sonuç defterine işlendi.
- ADS1115 + SCT ortalama akımının PZEM karşılaştırma ortalamasına göre farkı: 18 W −%0,99; 42 W +%0,125; 57 W +%0,647; 100 W yaklaşık %0,00 (aynı çalışma noktasındaki uyum, bağımsız doğrulama değil); 150 W +%1,23.
- Test edilen koşulların tamamı ±%4 kabul hedefinin içindedir. Bağımsız karşılaştırma oturumlarında mutlak fark en fazla %1,23'tür.
- **E19 KAPATILDI — test edilen koşullarda hedef aşıldı.** Bu sonuç tüm akım aralığına genellenmez; yaklaşık 2 A ikincil hedefi yapılmadı.
- ADS1115 A0/A1 common-mode ve GND–VDD giriş güvenliği fiziksel olarak doğrulanmış sayılmaz; bu güvenlik kapısı yeni donanım çalışmalarında ayrıca ele alınacaktır.
- Ayrıntılar: [E19 README](experiments/E19-ads1115-low-current-alternative/README.md) · [E19 sonuç defteri](experiments/E19-ads1115-low-current-alternative/results.md).


## 2026-11-20 — E20 yapılmadan kapatıldı: ölçüm kriterine ulaşılması
- E19'da 18 W, 42 W ve 57 W düşük akım noktalarında ADS1115 + SCT ölçümü PZEM karşılaştırma ortalamasına sırasıyla −%0,99, +%0,125 ve +%0,647 farkla sonuçlandı. Kayıtlı 18–150 W koşullarının tamamı ±%4 proje kriterinin içindedir.
- Bu nedenle E20'nin planlanan 18 W fiziksel ON/OFF çevrimleri, temel akım ölçümü hedefi karşılandığından proje açısından gerekli görülmedi ve **KAPATILDI — YAPILMADAN**.
- E20 kapsamında fiziksel çevrim, gecikme, OFF sonrası tabana dönüş veya tekrarlanabilirlik ölçümü yapılmadı; sonuç/CSV yoktur. E19 sabit yük sonuçları E20 dinamik performans kanıtı değildir.
- Kapanışın nedeni hedeflenen kriterlerde akım ölçümünün elde edilmesidir; güvenlik doğrulaması veya tüm akım aralığı onayı değildir.
- Ayrıntılar: [E20 deney kaydı](experiments/E20-ads1115-18w-on-off-response/README.md) · [E20 sonuç defteri](experiments/E20-ads1115-18w-on-off-response/results.md).


## 2026-11-20 — Çamaşır ve bulaşık gözlem modülü klasörleri oluşturuldu
- GitHub deposunda iki ayrı cihaz alanı açıldı: [Çamaşır makinesi](devices/washing-machine/README.md) ve [Bulaşık makinesi](devices/dishwasher/README.md).
- Her cihaz için hardware, firmware, data/raw, data/processed, analysis/python, analysis/results, analysis/reports ve experiments klasörleri oluşturuldu.
- Planlanan gözlem kanalları kullanıcıyla konuşulan kapsam doğrultusunda akım, ses ve titreşimdir. Kesin sensör modelleri, ESP32 kart varyantı, pinler, I²C çoklayıcı bağlantısı ve kayıt parametreleri henüz doğrulanmadı.
- Klasörler hazırlandı; fiziksel imalat, firmware, bağlantı, derleme ve ölçüm yapılmış sayılmaz.
- **Modül numarası kararı açık:** MEMORY.md Modül 4/5'i çamaşır/bulaşık olarak anıyor; E22 README ise Modül 4'ü ESP32 + ADS1115 + 100 A / 1 V SCT + PZEM olarak tanımlıyor. Çakışma kullanıcı onayı olmadan çözülmeyecek.
