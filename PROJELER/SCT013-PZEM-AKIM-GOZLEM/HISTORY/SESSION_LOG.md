## 2026-10-30 — Bias breadboard Vmid multimetre referansı eklendi

- **HEDEF:** E00A için bias devresinin breadboard orta noktasına ait ilk DC referansını kaydetmek.
- **LOG:** Kullanıcı, bias breadboard üzerinden multimetre ile orta noktada **1,65 V** okuduğunu bildirdi. Bu değer E00A results.md, experiment.yaml ve metadata.yaml dosyalarına KULLANICI BİLDİRİMİ olarak işlendi. L78L33 çıkışındaki 3,31 V referansından ayrı tutuldu.
- **SONUÇ:** İki multimetre referansı kayıtlı: L78L33 çıkışı 3,31 V DC; breadboard bias orta noktası/Vmid 1,65 V DC. Bu değerler ESP32 ADC ölçümü değildir. ADC bağlantısı ve 30 saniyelik kayıt henüz yapılmadı.
- **Doğrulama:** İlgili E00A sonuç/YAML kayıtları, STATUS, PROGRESS_TREE ve EXPERIMENT_LEDGER güncellendi; commit sonrası yeniden okunacak.
- **Sonraki adım:** Gerçek kart/pinout ve ADC sınırları doğrulandıktan sonra iki noktayı ESP32 ADC ile ayrı ayrı gözlemek.
- **Kanıt:** [E00A sonuç kaydı](../experiments/E00A-raw-waveform-observation/results.md), [E00A deney YAML](../experiments/E00A-raw-waveform-observation/experiment.yaml).

## 2026-10-30 — E00A açıldı ve ilk multimetre referansı eklendi

- **Durum:** DENEY KAYDI AÇILDI; yalnız ilk multimetre referansı kullanıcı tarafından bildirildi. ESP32 ADC testi yapılmadı.
- **HEDEF:** E00A'yı 30 saniyelik kısa ADC gözlemleriyle başlatmak ve ilk donanım referansını kaybetmeden depoya eklemek.
- **LOG:** Kullanıcı bias trafosunun L78L33 DC çıkışını multimetreyle **3,31 V** ölçtüğünü bildirdi. Değer E00A results.md ve experiment.yaml içine KULLANICI BİLDİRİMİ olarak kaydedildi. Her ADC koşulu 30 saniye olarak güncellendi. 3,3 V için düşünülen harici 10k/10k bölücünün bias devresinin parçası olmadığı, ayrı/geçici ölçüm aparatı olduğu açıklandı.
- **SONUÇ:** 3,31 V kaynak referansı kaydedildi; ESP32 ADC ham değeri, analogReadMilliVolts sonucu, Vmid değeri ve 30 saniyelik kayıt henüz yok. Gerçek WROOM-32D kart/pinout ve ADC attenuation/giriş sınırı doğrulanmadan bağlantı yapılmayacak.
- **Depoya yazılanlar:** E00A README, protocol, results, metadata.yaml, experiment.yaml; STATUS, ROADMAP, PROGRESS_TREE, EXPERIMENT_LEDGER.
- **Doğrulama sınırı:** GitHub yazımları dosya bazında commit edildi. Commit sonrası çapraz yeniden okuma bu kaydın hazırlanması sırasında henüz yapılmadı. Firmware yazılmadı/derlenmedi; fiziksel ADC testi yapılmadı.
- **Sonraki adım:** Gerçek kart/GPIO ve ADC sınırını doğrula; ardından A/B koşullarını 30 saniye kaydet.
- **Kanıt:** [E00A sonuç kaydı](../experiments/E00A-raw-waveform-observation/results.md), [protokol](../experiments/E00A-raw-waveform-observation/protocol.md), [STATUS](../STATUS.md).

## 2026-10-30 — E00A bias trafosu DC noktalarının ADC gözlemi olarak hazırlandı

- **Durum:** DOKÜMANTASYON UYGULANDI; firmware ve fiziksel deney yapılmadı.
- **HEDEF:** Kullanıcının netleştirdiği sırayı depoda tek anlamlı protokole dönüştürmek: SCT olmadan önce bias trafosunun L78L33 3,3 V çıkışını, ardından bias Vmid noktasını ESP32 ADC ile gözlemek.
- **LOG:** E00A README, protocol, metadata.yaml, experiment.yaml ve results.md güncellendi. Deney indeksi, STATUS, ROADMAP, PROGRESS_TREE ve EXPERIMENT_LEDGER da yeni kapsamla eşitlendi. 3,3 V çıkış için harici 10k/10k ölçüm bölücüsü tanımlandı; Vmid ikinci koşulda doğrudan ADC'ye bağlanacak. GPIO34 yalnız fiziksel WROOM-32D pinout doğrulanırsa kullanılacak. Ham CSV yolları data/raw/E00A altında tanımlandı.
- **SONUÇ:** Deney sırası ve kayıt alanları hazır. 3,3 V ADC'ye doğrudan bağlanmayacak; 10k/10k bölücü ile ADC düğümü yaklaşık 1,65 V olacak. SCT bu deneyde yok. Firmware yazılmadı/derlenmedi, kart görülmedi, bias trafosu fiziksel olarak doğrulanmadı, multimetre ölçümü ve ADC kaydı alınmadı.
- **Doğrulama:** E00A dokümanları ve bağlı durum dosyaları GitHub main üzerinde yazıldı. Commit sonrası tam çapraz yeniden okuma bu kaydın oluşturulması sırasında henüz yapılmadı.
- **Sonraki adım:** Kullanıcı bias trafosunu bulduğunda gerçek kart/pinout ve devre GND'si kontrol edilir; multimetre ile 3,3 V ve Vmid ölçülür; sonra ilk ADC firmware'i hazırlanır.

# Oturum günlüğü

## 2026-10-29 — E07 SCT kararlılık basamak testi planlandı

- **Durum:** UYGULANDI — deney protokolü ve bağlı proje durum kayıtları depoya yazıldı; fiziksel deney yapılmadı.
- **Hedef ve kabul ölçütü:** Yalnız SCT sinyalinden kararlı bölgeleri belirlemeye yönelik sınırlı bir deney planını kaydetmek. Kararlılık eşiği ve gereken pencere sayısı deney sonuçlarından çıkarılacak; önceden varsayılmayacak.
- **Yapılan:** E07 protokolü, metadata ve boş sonuç kaydı oluşturuldu. Üç tur tanımlandı; her turda boşta, 100 W akkor, 150 W akkor ve 8,5 W LED basamakları var. Örnekleme hızı turdan tura 1 / 2 / 2,5 kS/s hedefleriyle değişecek. Her 200 ms başlangıç penceresinde aynı örneklerden RMS, Peak, Peak-to-Peak ve yardımcı istatistikler hesaplanıp Python'da analiz edilecek.
- **Kapsam sınırı:** Bu deney PZEM ile kararlı alan eşleştirmeyi hedeflemez. Üç turdan sonra eldeki veri değerlendirilir; yalnız önemli ve cevapsız bir soru varsa yeni deney önerilir.
- **Doğrulama:** E07 protokolü, metadata ve results dosyaları GitHub'a yazıldı. Bu oturumda donanım kurulmadı, firmware derlenmedi, örnek alınmadı ve fiziksel ölçüm yapılmadı. STATUS, ROADMAP ve deney indeksi E07 bağlantısıyla güncellendi.
- **Açık kalanlar:** ESP32 kartı/ADC GPIO'su ve fiziksel örnekleme uygulaması donanım/firmware aşamasında seçilecek. Gerçek örnekleme hızı ölçülecek. Kararlılık eşiği ve ardışık pencere sayısı sonuçlardan çıkarılacak.
- **Sonraki adım:** Mevcut temel ADC ve yüksüz hazırlık sırasını tamamla; E07'yi kodlamadan önce bu protokolü esas al.
- **Kanıt:** [E07 protokolü](../experiments/E07-sct-stability-step-tests/protocol.md); [E07 metadata](../experiments/E07-sct-stability-step-tests/metadata.yaml); [E07 sonuç kaydı](../experiments/E07-sct-stability-step-tests/results.md); [STATUS](../STATUS.md); [ROADMAP](../ROADMAP.md).


## 2026-10-29 — İlk deney SCT bağlanmadan ADC API'lerini karşılaştırmak

- **Durum:** PLAN UYGULANDI; fiziksel deney yapılmadı.
- **Kullanıcı hedefi:** Testlere temel basamaktan başlamak ve iki fonksiyonun farkını gözlemleyerek anlamak.
- **Sıra:** (1) SCT bağlı değilken bias orta noktası ADC GPIO'suna; aynı döngüde `analogRead()` ham sayısı ve `analogReadMilliVolts()` mV çıktısı, voltmetre karşılaştırmasıyla kaydedilecek. (2) SCT bağlanıp ölçülen hatta akım yokken aynı iki okuma tekrarlanacak. (3) Daha sonra E01 uzun yüksüz kayıt, grafik ve gürültü analizi.
- **Ham ADC açıklaması:** 12 bit için nominal ham aralık 0–4095. İdeal ve doğrusal 0–3,3 V varsayımıyla 1,65 V → 1,65/3,3×4095 ≈ 2048; bu yalnız teorik örnektir. Gerçek ESP32 ham değeri ölçümle gelir; model, attenuation ve ADC doğrusal olmaması nedeniyle 2048 olmak zorunda değildir. `analogReadMilliVolts()` kalibrasyon destekli tahmindir, hassas voltmetre garantisi değildir.
- **Depoya eklenenler:** [E00 protokolü](../experiments/E00-bias-adc-baseline/protocol.md), [E00 metadata](../experiments/E00-bias-adc-baseline/metadata.yaml); T005, STATUS, ROADMAP ve görev indeksi yeni sıraya göre güncellendi.
- **Sonraki adım:** Gerçek ESP32 kart modeli ve ADC GPIO'sunu mevcut envanterden/pin planından doğrula; kodda pin/attenuation seçimini ondan sonra kesinleştir. Ölçüm yapılmadan sonuç yazma.
- **Doğrulama sınırı:** Dosyalar GitHub'a yazıldı; fiziksel kurulum, firmware derleme/çalıştırma ve ölçüm yapılmadı.


Bu günlük proje durumunun kronolojisidir. Her anlamlı depo çalışması sonunda yeni kayıt eklenir; eski kayıtlar korunur.

## 2026-10-29 — Paralel bias kondansatörlerinin görevleri ve bağlantı şeması

- **Durum:** DOKÜMANTASYON GÜNCELLENDİ; fiziksel kurulum ve E01 ölçümü yapılmadı.
- **İnceleme:** Kullanıcının açıklamasındaki 10 µF'nin 50 Hz'de düşük empedanslı baypas sağlaması ve 104 (100 nF)'ün daha yüksek frekanslarda tamamlayıcı olabilmesi teknik olarak makul; ancak paraziti tamamen yok ettiği iddiası desteklenmiyor.
- **Karar:** Mevcut 104 yerinde kalacak; 10 µF elektrolitik Vmid–GND arasına paralel eklenecek. Elektrolitik pozitif uç Vmid, negatif uç GND.
- **Şema düzeltmesi:** ADR-007'ye iki SCT çıkış ucunu da gösteren bağlantı notu eklendi: uç A bias düğümüne, uç B seçilecek ESP32 ADC pinine. GPIO34 her ESP32 kartında yoktur; ESP32-C3'te GPIO34 bulunmaz. BERO'nun ADC pini henüz seçilmedi.
- **Sınırlar:** Kondansatörlerin fiziksel etkisi ölçülmedi. Wi-Fi/Bluetooth/röle parazitlerinin tamamen giderileceği veya ADC gürültüsünün sıfırlanacağı iddia edilmiyor.
- **Değiştirilen dosyalar:** [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md), [analog ön uç](../hardware/frontend.md).
- **Sonraki adım:** Fiziksel düzenekte paralel bağlantıyı kur, gerçek ADC pinini kart modeline göre doğrula ve E01 yüksüz ölçümünü kaydet.

## 2026-10-29 — Bias orta noktası kondansatörünün kaynaklarla değerlendirilmesi

- **Durum:** UYGULANDI — ADR ve bağlı proje kayıtları güncellendi; fiziksel devre değişikliği bekliyor.
- **Hedef ve kabul ölçütü:** 10 nF / 100 nF / 10 µF seçeneklerinin 50 Hz'deki etkisini, BERO'nun 2 × 10 kΩ bias bölücüsü ve ESP32 ADC yaklaşımı bağlamında değerlendirmek; ilk E01 düzenine uygulanabilir bir öneri kaydetmek.
- **Değerlendirme:** Kapasitif reaktans Xc = 1/(2πfC). 50 Hz'de 10 nF ≈ 318 kΩ, 100 nF ≈ 31,8 kΩ, 10 µF ≈ 318 Ω. Eşit 10 kΩ bölücünün Thevenin direnci yaklaşık 5 kΩ olduğundan, 10 µF orta noktayı 50 Hz bileşenine karşı çok daha düşük empedansla referanslar. 100 nF her devrede 'yanlış' değildir; fakat burada tek başına 10 µF kadar güçlü 50 Hz bypass sağlamaz.
- **Karar:** [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md) oluşturuldu. E01 öncesi mevcut orta nokta 100 nF kondansatörünün yerinde bırakılıp aynı Vmid–GND noktalarına 10 µF elektrolitik eklenerek paralel bağlanması önerildi. ADC GPIO'suna ayrıca 100 nF bağlanması opsiyonel bırakıldı ve ilk E01 kurulumuna alınmadı; etkisi kaynak empedansı/bant genişliğine bağlıdır.
- **Kaynaklar:** [OpenEnergyMonitor CT sensörü arayüzü](https://docs.openenergymonitor.org/electricity-monitoring/ct-sensors/interface-with-arduino.html) 10 µF değerini ve düşük AC reaktans hedefini destekler. [Espressif ADC kılavuzu](https://docs.espressif.com/projects/esp-idf/en/v4.4.8/esp32/api-reference/peripherals/adc.html) ADC pad'inde 100 nF kondansatörün senaryoya bağlı gürültü azaltma seçeneği olduğunu ve örneklemenin de yardımcı olabileceğini belirtir; bu, gürültünün sıfırlanacağı veya her kurulumda 100 nF zorunlu olduğu anlamına gelmez.
- **Depo değişiklikleri:** ADR-007 ve ADR indeksi; hardware/frontend.md, hardware/inventory.md, STATUS.md, ROADMAP.md, T005 kartı, E01 protokolü/metadata ve açık sorular güncellendi. Eski 'henüz karar verilmedi' ifadeleri güncel öneriyle uzlaştırıldı.
- **Doğrulama ve sınırlar:** Dokümantasyon commit'leri oluştu. Son doğrulama için main dalındaki değişmiş dosyalar yeniden okunacak. Kondansatörler fiziksel olarak henüz eklenmedi; E01 verisi alınmadı; gürültü seviyesinde düşüş ölçülmedi. GPIO34 bu kararla seçilmiş değil.
- **Sonraki adım:** E01 kurulumundan önce mevcut 104'ü sökmeden Vmid–GND arasına paralel 10 µF elektrolitik ekleyip polaritesini kontrol et; fiziksel olarak kullanılan değeri metadata'ya yaz. ADC pinine ek 100 nF'ı aynı anda ekleme. Daha sonra E01 ölçümünü al.
- **Kanıt:** [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md); [analog ön uç](../hardware/frontend.md); [STATUS](../STATUS.md); [E01 protokolü](../experiments/E01-noise-floor/protocol.md); [E01 metadata](../experiments/E01-noise-floor/metadata.yaml).

## 2026-10-29 — SCT013-030 raporu ve CT satürasyon notunun BERO'ya işlenmesi

- **Durum:** UYGULANDI — teknik notlar ilgili dosyalara işlendi; oturum günlüğü bu kayıtla eşitlendi.
- **Hedef ve kabul ölçütü:** Kullanıcının sağladığı iki belgeyi mevcut BERO kayıtlarıyla karşılaştırıp SCT013-030 teknik bilgisini doğru konumlara eklemek; genel önerileri proje kararı/deney sonucu gibi göstermemek; mevcut bias kondansatörünü sessizce değiştirmemek.
- **Yapılan:** Ana SCT013-030 kaydı, proje içi referans kopyası, donanım envanteri, analog ön uç, STATUS, ROADMAP, görev indeksi, açık sorular, T005/E01 kartı ve E01 protokol/metadata kaydı güncellendi.
- **Kaynaklardan alınan bilgiler:** Nominal 30 A RMS → yaklaşık 1 V RMS, nominal oran 30 A/V (yaklaşık 33,33 mV/A), gerilim çıkışlı modelde dahili burden ve genel CT satürasyon riskleri.
- **Kondansatör ayrımı:** Rapor örnekte 10 µF öneriyor; BERO'daki mevcut fiziksel devre kaydı 104 (100 nF). Sonraki ADR-007 kararı 104'ü kaldırmak yerine 10 µF'yi paralel eklemek oldu.
- **Doğrulama:** Dosya güncelleme çağrıları commit SHA'ları döndürdü. Bu yazım sırasında bütün dosyaların commit sonrası yeniden okuma denetimi henüz yapılmadı; otomatik PR/CI kontrolü çalıştırılmadı. Fiziksel test, ADC örneklemesi, firmware derlemesi veya kalibrasyon yapılmadı.
- **Açık kalanlar:** Değiştirilen bütün dosyaların tekrar okunması ve bağlantı/metadata tutarlılığının kontrolü; kondansatör seçiminin ayrı teknik incelemesi.
- **Sonraki adım:** Dosyaları GitHub'dan yeniden okuyarak içeriği ve main durumunu doğrula. Ardından yalnız kondansatörün devredeki rolünü ve seçimini mevcut bağlantı üzerinden ele al.
- **Kanıt:** [Ana SCT013-030 kaydı](https://github.com/bakbalik-win11/BERO/blob/main/DONANIM/SCT013-30A-1V/README.md); [proje referansı](https://github.com/bakbalik-win11/BERO/blob/main/PROJELER/SCT013-PZEM-AKIM-GOZLEM/hardware/references/SCT013-30A-1V.md); [analog ön uç](https://github.com/bakbalik-win11/BERO/blob/main/PROJELER/SCT013-PZEM-AKIM-GOZLEM/hardware/frontend.md); [STATUS](https://github.com/bakbalik-win11/BERO/blob/main/PROJELER/SCT013-PZEM-AKIM-GOZLEM/STATUS.md); [E01 protokolü](https://github.com/bakbalik-win11/BERO/blob/main/PROJELER/SCT013-PZEM-AKIM-GOZLEM/experiments/E01-noise-floor/protocol.md).

## 2026-10-27 — Oturum sürekliliği ve bilgi kaynağı kurallarının güçlendirilmesi

- **Durum:** UYGULANDI; değiştirilen dosyalar GitHub'dan yeniden okunarak doğrulandı.
- **Hedef ve kabul ölçütü:** Yeni çalışma günlerinde proje bağlamının tekrar kurulmasını kolaylaştırmak; başlangıç kanıtını görünür kılmak; bilinen bilgilerin gereksiz yere yeniden sorulmasını ve kullanıcı beyanlarının bağımsız ölçüm gibi sunulmasını önlemek.
- **Yapılan:**
  - `AGENTS.md` başlangıç adımlarına okunan kaynakları ve branch/commit bilgisini raporlama, önceki bilgileri depoda arama ve yalnız eksik/çelişkili alanı sorma kuralları eklendi.
  - `AGENTS.md` kanıt kuralları kullanıcı beyanı/raporu, üretici belgesi, hipotez, hesap ve ölçülmüş sonuç ayrımını açıklaştırdı.
  - `SESSION_PROTOCOL.md` başlangıç ve kapanış kontrol listelerine kaynak/commit görünürlüğü, tekrar soru sormadan önce depo taraması ve kanıt etiketlerinin doğru kullanımı eklendi.
  - `STATUS.md` içine oturum sürekliliği kuralları özeti eklendi.
- **Doğrulama:** Üç dosya güncellendikten sonra GitHub'dan yeniden okunacak ve içerik kontrol edilecek. Bu değişiklik yalnızca çalışma protokolünü güçlendirir; CI/PR kontrolünün çalıştığı veya donanımın test edildiği anlamına gelmez.
- **Açık kalanlar:** Otomatik PR/CI kontrolü bu işlem kapsamında çalıştırılmadı.
- **Sonraki adım:** Her anlamlı oturumda güncel depo kayıtlarını okuyup karşılaştırarak bu kuralları uygulamak.
- **Kanıt:** [AGENTS.md](../AGENTS.md); [SESSION_PROTOCOL.md](../SESSION_PROTOCOL.md); [STATUS.md](../STATUS.md).

## 2026-10-27 — Gün sonu incelemesi, T004 kapanışı ve T005 planının eşitlenmesi

- **Durum:** UYGULANDI; değiştirilen proje kayıtları GitHub'dan yeniden okunarak doğrulandı. Fiziksel deney yapılmadı.
- **Hedef ve kabul ölçütü:** Gün sonu kontrolü ve oturum protokolünü uygulamak; bugünkü gerçek çalışmayı kaydetmek; T004 durumunu görev indeksi, STATUS ve ROADMAP ile eşitlemek; kullanıcının donanım kurulumunun henüz yapılmadığı ve T005'in 30 saniyeden uzun sürebileceği bilgisini E01 kayıtlarına işlemek.
- **Yapılan:**
  - T004 görev kartı `TAMAMLANDI` olarak kaydedildi. Hobi kapsamındaki belge çıktısı tamamlandı; bu, fiziksel kurulumun veya elektriksel ölçümün yapıldığı anlamına gelmez.
  - `hardware/frontend.md` SCT dişi jack bağlantısı, breadboard bias alt devresi (2 × 10 kΩ, orta nokta ve GND'ye 100 nF), yaklaşık 1,65 V bias kabulü, SCT013-030 ve SCT013-100A-1V modelleri ve ESP32 dahili ADC yaklaşımıyla eşitlendi.
  - T005 ve E01 protokol/metadata kayıtlarına şu kullanıcı bilgileri eklendi: donanım henüz kurulmadı; PZEM ve diğer ESP kartları ölçülen hattan beslenmiyor; hatta akım yokken ADC verisi zaman grafiğinde incelenecek; 30 saniye üst sınır değil, daha uzun ve gerekirse saatler süren kayıt mümkün ama süre kesinleşmedi.
  - `STATUS.md`, `ROADMAP.md`, `tasks/README.md` ve `docs/open-questions.md` T004/T005 durumuyla tutarlı olacak şekilde güncellendi. SCT jack–bias bağlantısını yeniden soran açık maddeler kaldırıldı; pin eşlemesi sonraki firmware/pin planlama işine bırakıldı.
- **Doğrulama:** Güncellenen T004, `hardware/frontend.md`, T005, E01 `protocol.md`, E01 `metadata.yaml`, `STATUS.md`, `ROADMAP.md`, `tasks/README.md` ve `docs/open-questions.md` dosyaları GitHub'dan yeniden okundu. Dosya durumları birbirine göre kontrol edildi. Bu oturumda fiziksel donanım kurulmadı, ADC verisi alınmadı, grafik üretilmedi ve otomatik PR kontrolü çalıştırılmadı.
- **Açık kalanlar:** T005/E01 fiziksel kurulum ve veri toplama bekliyor. SCT için kullanılacak model test bazında kayda yazılacak. ADC GPIO/pin planı firmware aşamasında belirlenecek. SSR yük/GPIO/trigger ayrıntıları açık.
- **Sonraki adım:** Donanım kurulduğunda hatta akım yokken ADC ham verisini topla; gerçek kayıt süresini ve yapılandırmayı metadata'ya yaz; zaman grafiği, örnek sayısı, ortalama, min/max ve ofset giderilmiş gürültü RMS'ini üret.
- **Kanıt:**
  - [T004 görev kartı](../tasks/T004-analog-frontend.md)
  - [Analog ön uç kaydı](../hardware/frontend.md)
  - [T005 görev kartı](../tasks/T005-noise-floor.md)
  - [E01 protokolü](../experiments/E01-noise-floor/protocol.md)
  - [E01 metadata](../experiments/E01-noise-floor/metadata.yaml)
  - [STATUS](../STATUS.md), [ROADMAP](../ROADMAP.md), [görev indeksi](../tasks/README.md), [açık sorular](../docs/open-questions.md)

## 2026-10-27 — T002 güvenlik kontrolünün kapatılması

- **Durum:** UYGULANDI; güncellenen dosyalar GitHub'dan yeniden okunarak doğrulandı.
- **Hedef ve kabul ölçütü:** Kullanıcının T002'yi okuyup tüm kontrolleri tamamladığı beyanını görev kaydına işlemek; görev indeksi, kontrol listesi, yol haritası ve proje durumunu eşitlemek.
- **Yapılan:** Kullanıcı beyanına göre hardware/safety-checklist.md maddeleri işaretlendi. T002 kartı ve görev indeksi TAMAMLANDI yapıldı. ROADMAP.md Faz 0.2 işaretlendi; STATUS.md aktif görevi T003 yaptı; README.md güvenlik kaydına bağlantı eklendi.
- **Doğrulama:** Güncellenen dosyalar GitHub'dan yeniden okundu. Kontrol listesindeki durum, T002 kartı, görev indeksi, ROADMAP ve STATUS birbirleriyle tutarlı hale getirildi.
- **Açık kalanlar:** Kontrollerin tamamlandığı kullanıcı beyanıdır; asistan fiziksel kurulumu bağımsız incelemedi. Kontrolü yapan kişinin yetkin rolü ayrıca kaydedilmedi. Bu nedenle fiziksel güvenliğin bağımsız doğrulandığı iddia edilmiyor. T003'te hata kabul hedefi açık; T004 analog ön uç çalışması henüz başlamadı.
- **Sonraki adım:** T003 kapsamında önceki pens ampermetre adayı referans cihazı için ölçüm hata kabul hedefi seçeneklerini dayanak ve ödünleşimleriyle hazırlamak; kullanıcı onayıyla kaydetmek.
- **Kanıt:** [T002](../tasks/T002-safety-checklist.md), [kontrol listesi](../hardware/safety-checklist.md), [görev indeksi](../tasks/README.md), [ROADMAP](../ROADMAP.md), [STATUS](../STATUS.md).


## 2026-10-27 — T001 kapanışı ve depo tutarlılık düzeltmesi

- **Durum:** UYGULANDI ve depo kayıtları yeniden okunarak doğrulandı.
- **Hedef ve kabul ölçütü:** T001'i kullanıcı beyanlarını esas alarak kapatmak; aynı işi yeniden istemeye yol açan eski durumları, açık soruları ve yol haritası kayıtlarını birbiriyle uyumlu hale getirmek.
- **Yapılan:** T001 görev kartı TAMAMLANDI durumuna getirildi. Kullanıcının beyan ettiği envanter/bias devresi T001 kapsamında kabul edildi; GPIO, harici ADC ve analog kuplaj ayrıntıları sonraki ilgili görevlere bırakıldı. T002 aktif görev yapıldı. Görev indeksi, ROADMAP, STATUS, açık sorular ve donanım envanteri güncellendi. önceki pens ampermetre adayı referans cihazı olarak kaydedildi. DS3231 için kullanıcının çalışan kod, güç kesilip yeniden verildiğinde saat koruma testi ve iki modülde 2032 tipi pil beyanı kaydedildi. Test yüklerinin önceden belirlenmesi şartı kaldırıldı; yükler test sırasında kullanıcı tarafından beyan edilecek.
- **Doğrulama:** Güncellenen T001, envanter, STATUS, ROADMAP, görev indeksi ve açık sorular dosyaları GitHub'dan yeniden okundu. T001 durumu TAMAMLANDI; kalan işler bölümünde tekrar eden bias maddesi yok. Bu oturumda fiziksel elektriksel test yapılmadı; kullanıcı tarafından bildirilen testler kullanıcı beyanı olarak kaydedildi.
- **Açık kalanlar:** SCT fotoğraflarının gerçek dosya olarak GitHub'a eklenmesi ayrıca çözülmeli; şu anki metin referansları resim dosyalarının depoda bulunduğu anlamına gelmez. T002 güvenlik incelemesi, T003 hata hedefi ve sonraki analog ön uç/deney çalışmaları henüz yapılmadı.
- **Sonraki adım:** T002 güvenlik kontrolünü, gerçek kontrol maddelerini kullanıcı adına varsaymadan ve yalnızca mevcut kanıta dayanarak ele almak.
- **Kanıt:** [T001](../tasks/T001-hardware-inventory.md), [STATUS](../STATUS.md), [ROADMAP](../ROADMAP.md), [envanter](../hardware/inventory.md), [açık sorular](../docs/open-questions.md).


## 2026-10-26 — Oturum kapanış protokolünün eklenmesi

- **Durum:** DOĞRULANDI; PR birleştirilmesi bekleniyor.
- **Hedef ve kabul ölçütü:** Oturum başlangıcını/kapanışını görünür yapmak ve eksik durum günlüğünü PR denetimiyle yakalamak.
- **Yapılan:** SESSION_PROTOCOL.md, HISTORY şablonu/günlüğü, güncel STATUS/ROADMAP ve GitHub Actions denetimi eklendi. Fiziksel donanım veya deney durumunda değişiklik yapılmadı.
- **Doğrulama:** GitHub Actions oturum kapanış kontrolü PR #2 üzerinde başarılı çalıştı: https://github.com/bakbalik-win11/BERO/actions/runs/40234585403
- **Açık kalanlar:** Protokol PR'ı henüz main'e birleştirilmedi. Donanım ve deneyler hâlâ yapılmadı.
- **Sonraki adım:** PR #2'yi birleştir; sonraki proje değişikliğinde kontrolün tekrar çalıştığını izle; ardından donanım envanterini doğrula.
- **Kanıt:** PR: https://github.com/bakbalik-win11/BERO/pull/2 ; workflow run: https://github.com/bakbalik-win11/BERO/actions/runs/40234585403

## 2026-10-26 — Gün sonu kontrolünün sadeleştirilmesi ve kayıt düzeltmesi

- **Durum:** DOĞRULANDI (belge içeriği ve önceki kapanış kontrolü).
- **Hedef ve kabul ölçütü:** Kullanıcının teknik ayrıntıları tek başına değerlendirmek zorunda kalmadan gün sonu kapanışını kontrol edebilmesi; güncel olmayan durum metinlerinin fark edilmesi.
- **Yapılan:** GUN_SONU_KONTROLU.md eklendi ve README/AGENTS içinden bağlandı. STATUS.md, PR #2'nin birleştirildiği ve oturum kapanış kontrolünün geçtiği bilgisiyle güncellendi.
- **Doğrulama:** PR #2 birleştirilmiş durumda: https://github.com/bakbalik-win11/BERO/pull/2 . Kapanış kontrolü başarılı: https://github.com/bakbalik-win11/BERO/actions/runs/40234658507 . Bu kayıt için teslimat ve otomatik kontrol durumu PR #3 Checks sekmesinden kontrol edilir: https://github.com/bakbalik-win11/BERO/pull/3/checks.
- **Açık kalanlar:** Fiziksel donanım envanteri, kalibrasyon ve E01–E06 deneyleri yapılmadı. Otomasyon günlük kaydının varlığını/biçimini denetler; teknik doğruluğu bütünüyle garanti etmez.
- **Sonraki adım:** Bir sonraki gerçek çalışma oturumunda GUN_SONU_KONTROLU.md listesini uygula ve ilk somut iş olarak fiziksel donanım envanterini doğrula.
- **Kanıt:** [Gün sonu kontrolü](../GUN_SONU_KONTROLU.md), [mevcut durum](../STATUS.md), [oturum protokolü](../SESSION_PROTOCOL.md), PR #3: https://github.com/bakbalik-win11/BERO/pull/3.

## 2026-10-26 — Düzeltme: PR #2 durum kaydının açıklığa kavuşturulması

- **Durum:** DOĞRULANDI.
- **Hedef ve kabul ölçütü:** Günlükteki eski “PR #2 henüz birleştirilmedi” satırının artık güncel durum gibi okunmasını engellemek.
- **Yapılan:** Önceki tarihli kayıt silinmedi. Bu düzeltme, söz konusu cümlenin yalnızca o kayıt hazırlanırken geçerli olduğunu; PR #2 birleştirildikten sonra güncelliğini yitirdiğini açıkça belirtir. Güncel durum için STATUS.md ve en yeni tarihli günlük kaydı esas alınmalıdır.
- **Doğrulama:** PR #2 birleştirildi: https://github.com/bakbalik-win11/BERO/pull/2 . Oturum kapanış kontrolü başarılı: https://github.com/bakbalik-win11/BERO/actions/runs/40234658507 . Gün sonu kontrol listesi PR #3 ile main'e alındı: https://github.com/bakbalik-win11/BERO/pull/3.
- **Açık kalanlar:** Donanım envanteri, kalibrasyon ve E01–E06 deneyleri yapılmadı. Otomatik kontrol, kayıt yapısını denetler; deney doğruluğunu garanti etmez.
- **Sonraki adım:** Gün sonunda [GUN_SONU_KONTROLU.md](../GUN_SONU_KONTROLU.md) listesini kullan; sonraki teknik iş olarak donanım envanterini doldur.
- **Kanıt:** [STATUS.md](../STATUS.md), [gün sonu kontrolü](../GUN_SONU_KONTROLU.md), PR #2, PR #3 ve [PR #4 kontrol sekmesi](https://github.com/bakbalik-win11/BERO/pull/4/checks).

## 2026-10-26 — Arşiv incelemesi ve görev kartlarının eklenmesi

- **Durum:** UYGULANDI; değişiklikler PR #5 dalında hazır.
- **Hedef ve kabul ölçütü:** Mevcut yol haritasındaki ilk altı işi açık bağımlılıkları ve kanıtlanabilir kabul ölçütleri olan görev kartlarına dönüştürmek; deney veya donanım doğrulaması yapıldığı izlenimini vermemek.
- **Yapılan:** tasks/ altında T001–T006 kartları, sıralama tablosu ve şablon eklendi. STATUS.md içindeki aktif görev T001 olarak belirlendi; ROADMAP.md ve README.md ilgili kartlara bağlandı. Kullanıcının tek seferde bir somut göreve odaklanması ve bilinmeyen bilgilerin tahminle doldurulmaması kuralı eklendi.
- **Doğrulama:** PR #5 kontrolü: https://github.com/bakbalik-win11/BERO/pull/5/checks. Bu PR dokümantasyonla sınırlıdır; donanım envanteri, güvenlik onayı, kalibrasyon ve E01–E06 deneyleri yapılmadı.
- **Açık kalanlar:** Görev kartlarının sahada uygulanması; ilk somut görev T001. PR'ın son durumu PR #5 üzerinden izlenir.
- **Sonraki adım:** T001 için fiziksel donanım etiketlerini/kanıtlarını topla.
- **Kanıt:** PR #5: https://github.com/bakbalik-win11/BERO/pull/5 ; kontrol sekmesi: https://github.com/bakbalik-win11/BERO/pull/5/checks.

## 2026-10-26 — Türkçe klasör rehberinin eklenmesi

- **Durum:** UYGULANDI; PR #6 açık, otomatik kontrol sonucu bekleniyor.
- **Hedef ve kabul ölçütü:** Mevcut klasör adlarının Türkçe karşılıklarını ve amaçlarını tek bir rehberde açıklamak; var olan teknik yolları, bağlantıları ve otomasyon kurallarını bozmamak.
- **Yapılan:** KLASOR_REHBERI.md eklendi; README.md ve STATUS.md üzerinden erişim bağlantısı verildi. İngilizce klasör yolları korundu. Fiziksel donanım, kalibrasyon veya deney durumunda değişiklik yapılmadı.
- **Doğrulama:** PR #6 kontrol sekmesi: https://github.com/bakbalik-win11/BERO/pull/6/checks. Rehberin yolları ve dosya adları main dalındaki ağaçla karşılaştırıldı.
- **Açık kalanlar:** Otomatik kapanış kontrolünün nihai sonucunun görülmesi.
- **Sonraki adım:** PR kontrolünün geçtiğini doğrula; sonra aynı T001 görevine devam et.
- **Kanıt:** PR #6: https://github.com/bakbalik-win11/BERO/pull/6 ; kontrol sekmesi: https://github.com/bakbalik-win11/BERO/pull/6/checks.


## 2026-10-26 — Kısa Türkçe klasör karşılıklarının eklenmesi

- **Durum:** UYGULANDI; PR incelemesi bekleniyor.
- **Hedef ve kabul ölçütü:** HISTORY, analysis, calibration, data, docs, experiments, hardware, schema ve tasks adlarının yanına kısa Türkçe karşılıklarını eklemek; gerçek klasör adlarını ve mevcut bağlantıları korumak.
- **Yapılan:** KLASOR_REHBERI.md dosyasına `HISTORY - Geçmiş ve oturum kayıtları`, `analysis - Analiz`, `calibration - Kalibrasyon`, `data - Veri ve ölçüm kayıtları`, `docs - Teknik belgeler`, `experiments - Deneyler`, `hardware - Donanım`, `schema - Veri şemaları` ve `tasks - Görev kartları` listesi eklendi. STATUS.md içindeki klasör rehberi satırı da güncellendi. Gerçek klasör adları değiştirilmedi.
- **Doğrulama:** Değişiklikler `docs/turkce-klasor-etiketleri` dalına yazıldı. Klasör adları ve içerik eşlemesi gözden geçirildi; PR kontrolleri tamamlanınca sonuç ayrıca doğrulanacak.
- **Açık kalanlar:** Değişikliklerin ana dala birleştirilmesi ve otomatik oturum kapanış kontrolünün sonucu.
- **Sonraki adım:** PR kontrolünün başarılı olduğunu doğrulayıp değişikliği main dalına al.
- **Kanıt:** [Klasör rehberi](../KLASOR_REHBERI.md); [değişiklik dalı](https://github.com/bakbalik-win11/BERO/tree/docs/turkce-klasor-etiketleri).


## 2026-10-27 — Önceki SCT/PZEM Markdown kayıtlarının projeye alınması
- **Durum:** UYGULANDI ve doğrulandı; [PR #8](https://github.com/bakbalik-win11/BERO/pull/8) birleştirildi.
- **Hedef ve kabul ölçütü:** Önceki BERO donanım çalışmalarındaki SCT013-100A-1V, SCT013-30A-1V ve PZEM-004T V3.0 Markdown kayıtlarını yeni projede tekrar araştırma/yazma gerektirmeden kullanmak; kaynakları korumak ve proje-özel eksikleri ayrı göstermek.
- **Yapılan:** Üç donanım README'si `hardware/references/` altına kaynak yolu ve kopya tarihi belirtilerek aktarıldı. Referans dizin indeksi ve proje README bağlantıları eklendi. `hardware/inventory.md`, T001, `STATUS.md` ve `docs/open-questions.md` genel donanım bilgisini yeniden toplamak yerine mevcut referansları kullanacak ve yalnızca bu projeye özgü seçim/eksikleri kaydedecek şekilde güncellendi.
- **Doğrulama:** Üç kopya kaynak `DONANIM/` Markdown içerikleriyle karşılaştırıldı ve proje bağlantıları yeniden okundu. [PR #8 Checks](https://github.com/bakbalik-win11/BERO/pull/8/checks) oturum-kapanış kontrolü başarılı oldu. PR #8, `ff2938fe2cacecda047053c010ea871601f4c369` birleştirme commit'i ile `main` dalına alındı. Yeni deney veya kalibrasyon sonucu üretilmedi.
- **Açık kalanlar:** Bu projede kullanılacak SCT varyantı; PZEM'in 10 A/100 A seçeneği ve CT modeli; gerçek MCU/ADC, VREF/bias/analog ön uç; referans cihazı ve yük senaryoları.
- **Sonraki adım:** T001'i sadece proje-özel eksikleri kapatmak için sürdür.
- **Kanıt:** [Proje referans indeksi](../hardware/references/README.md); [güncel envanter](../hardware/inventory.md); [T001](../tasks/T001-hardware-inventory.md); [PR #8](https://github.com/bakbalik-win11/BERO/pull/8); [birleştirme commit'i](https://github.com/bakbalik-win11/BERO/commit/ff2938fe2cacecda047053c010ea871601f4c369).


## 2026-10-27 — PR #8 aktarımının kapanış kaydının doğrulanması

- **Durum:** DOĞRULANDI.
- **Hedef ve kabul ölçütü:** Donanım referanslarının projeye aktarılması işinin PR, otomatik kontrol ve ana dala alınma durumunu güncel kayıtta kanıtla göstermek.
- **Yapılan:** PR #8'in birleştirildiği ve oturum-kapanış kontrolünün başarılı olduğu önceki oturum girdisinde açıkça kaydedildi; STATUS.md bu günlük kaydına bağlandı.
- **Doğrulama:** [PR #8 Checks](https://github.com/bakbalik-win11/BERO/pull/8/checks) başarılı; [birleştirme commit'i](https://github.com/bakbalik-win11/BERO/commit/ff2938fe2cacecda047053c010ea871601f4c369) `main` dalında. Bu doğrulama belge/süreç kontrolüdür; fiziksel deney veya kalibrasyon sonucu değildir.
- **Açık kalanlar:** Yeni projeye özgü SCT seçimi, PZEM varyantı/CT, gerçek MCU/ADC ve analog ön uç, referans cihazı ve yük senaryoları.
- **Sonraki adım:** T001 görevine yalnızca proje-özel eksikleri kapatmak üzere devam et.
- **Kanıt:** [PR #8](https://github.com/bakbalik-win11/BERO/pull/8); [PR #8 Checks](https://github.com/bakbalik-win11/BERO/pull/8/checks); [proje durumu](../STATUS.md).


## 2026-10-27 — SCT013-030 önceliği ve stok bildiriminin kaydı

- **Durum:** UYGULANDI; PR ve oturum kapanış kontrolü bekleniyor.
- **Hedef ve kabul ölçütü:** Kullanıcının seçtiği öncelikli SCT modelini ve bildirilen bileşen stoklarını envantere eklemek; sayım yapılmış veya deney gerçekleştirilmiş gibi göstermemek.
- **Yapılan:** SCT013-030 (30 A / 1 V) bu projede ilk tercih olarak kaydedildi. Kullanıcı 7 adet SCT013-030, 10 adet SCT013-100A-1V ve 10 adet 100 nF / 50 V seramik kondansatör bulunduğunu bildirdi. Envanter, T001, STATUS ve açık sorular bu kararla güncellendi. Kondansatörler devrede belirli bir noktaya atanmadı.
- **Doğrulama:** `hardware/inventory.md`, `STATUS.md`, T001 ve açık sorular aynı SCT önceliği ve stok beyanları açısından çapraz kontrol edildi. İlk otomatik oturum kapanış kontrolü, bu kayıtta zorunlu `**Doğrulama:**` başlığının bulunmadığını bildirdi; başlık biçimi bu düzeltmede tamamlanıyor ve kontrol PR #10 üzerinden yeniden çalıştırılacak.
- **Kanıt ve sınırlama:** SCT etiketi görünen bir görsel bu oturumda sunuldu; görsel henüz depoya `hardware/photos/` altında dosya olarak eklenmedi. Stok adetleri kullanıcı bildirimidir; bağımsız fiziksel sayım yapılmadı. Deney veya kalibrasyon sonucu üretilmedi.
- **Açık kalanlar:** Gerçek parçanın kalıcı fotoğraf kanıtı; PZEM'in gerçek varyantı/CT'si; MCU/ADC ve analog ön uç; alternatif karşılaştırma cihazı ve yük senaryoları.
- **Sonraki adım:** PR kapanış kontrolünü doğrula; sonra T001'de yalnızca kalan proje-özel donanım kanıtlarını tamamla.
- **Kanıt:** [Güncel envanter](../hardware/inventory.md); [T001](../tasks/T001-hardware-inventory.md); [proje durumu](../STATUS.md); [proje referans klasörü](../hardware/references/README.md).


## 2026-10-27 — Bias trafosu alt devresinin ilk tarifinin kaydı

- **Durum:** UYGULANDI; PR ve otomatik kontrol bekleniyor.
- **Hedef ve kabul ölçütü:** Kullanıcının mevcut bias alt devresini tekrar tasarlatmadan, bilinen bileşenleri ve açık kalan şema ayrıntılarını envantere geçirmek.
- **Yapılan:** RN130421 6 V / 2,0 VA trafo, L78L33 TO-92 regülatör ve 2 × 10 kΩ bölücü ile yaklaşık 1,65 V orta nokta tarifi `hardware/inventory.md` ve T001'e eklendi. “Bias trafosu” kullanıcının devre adı olarak kaydedildi. Kondansatör stokundaki 100 nF / 50 V seramiklerden kaçının hangi konumda kullanıldığı bilinmiyor olarak bırakıldı.
- **Doğrulama:** STATUS, envanter, T001 ve açık soruların aynı parça/topoloji bilgilerini kullandığı kontrol edildi. RN130421 ürün kaydı ve L78L veri sayfası referansları eklendi. Bu oturumda şema, fiziksel bağlantı, osiloskop ölçümü veya kalibrasyon sonucu sunulmadığı için devre işlevi doğrulanmış sayılmadı.
- **Açık kalanlar:** AC sekonderin doğrultma/filtre düzeni; kondansatör değerleri ve yerleri; direnç bölücünün bağlantı uçları; SCT sinyalinin bias düğümüne kuplajı; biasın şebeke dalgalanmasını takip etmesi iddiasının nasıl gerçekleştirildiği.
- **Sonraki adım:** Devrenin sade bir şema/fotoğrafını veya bağlantı listesini kayda geçir; özellikle doğrultucu ve kondansatörlerin yerini, 10 kΩ çiftinin bağlantılarını ve SCT sinyalinin bias noktasına giriş yolunu netleştir.
- **Kanıt:** [Donanım envanteri](../hardware/inventory.md); [T001](../tasks/T001-hardware-inventory.md); [açık sorular](../docs/open-questions.md); [RN130421 ürün bilgisi](https://www.ozdisan.com/p/General-Type-Transformers-471/el-kom-rn130421-516747); [L78L veri sayfası](https://docs.rs-online.com/5d09/0900766b8135fb6a.pdf).


## 2026-10-27 — Bias trafosu yerleşimi ve köprü doğrultucunun netleştirilmesi

- **Durum:** UYGULANDI; PR ve otomatik kapanış kontrolü bekleniyor.
- **Hedef ve kabul ölçütü:** Kullanıcının açıkladığı fiziksel yerleşimi envantere doğru ayırmak: kutu içindeki trafo/doğrultucu/regülatör ile ayrı breadboarddaki 10 kΩ bias bölücüsü.
- **Yapılan:** RN130421 + KBU6M + L78L33 bileşenlerinin korunaklı kutuda olduğu; 2 × 10 kΩ dirençli yaklaşık 1,65 V bias bölücüsünün ayrı breadboardda olduğu kaydedildi. KBU6M, 6 A / 1000 V köprü doğrultucu olarak eklendi. KBU6M ürün ailesi veri sayfası bağlantısı eklendi. Envanter, STATUS, T001 ve açık sorular güncellendi.
- **Doğrulama:** Dosyalar çapraz kontrol edildi; KBU6M özellikleri üretici veri sayfasıyla karşılaştırıldı. Yerleşim ve kablolama ayrıntıları kullanıcı beyanına dayanır. Fiziksel fotoğraf/şema, kondansatörlerin tam konumları veya elektriksel ölçüm bu oturumda sunulmadı; deney/kalibrasyon yapılmadı.
- **Açık kalanlar:** Köprü sonrası filtre kondansatörü ve regülatör bypass kapasiteleri/konumları; regülatör çıkışı ile ayrı breadboard arasındaki +3,3 V/GND bağlantısı; SCT sinyalinin 1,65 V bias noktasına kuplajı; 1,65 V değerinin ölçüm kanıtı.
- **Sonraki adım:** Bu bağlantıları varsa mevcut şema veya fotoğrafla belgelemek; şebeke tarafını açmadan ilerlemek.
- **Kanıt:** [Donanım envanteri](../hardware/inventory.md); [T001](../tasks/T001-hardware-inventory.md); [açık sorular](../docs/open-questions.md); [Vishay KBU6M ailesi veri sayfası](https://www.vishay.com/doc/?98732=).


## 2026-10-27 — ESP32 stokları, PZEM fotoğrafı, SSR referansı ve bias alt devresinin durumu

- **Durum:** UYGULANDI; PR ve otomatik kapanış kontrolü bekleniyor.
- **Hedef ve kabul ölçütü:** Kullanıcının sunduğu ESP32 stok bilgilerini ve PZEM modülünü envantere eklemek; depodaki SSR referansını projeye bağlamak; tamamlandığı onaylanan temiz bias üretim alt devresini yeniden açık soru olarak tutmamak.
- **Yapılan:** 2 adet ESP32-WROOM-32D, 1 adet ESP32-WROOM-32E ve 1 adet ESP32-WROOM-32S kullanıcı bildirimi olarak kaydedildi. Kullanıcının paylaştığı modül fotoğrafı PZEM-004T V3.0 olarak envantere işlendi; 10 A / 100 A varyantı ve CT modelinin fotoğrafla kesinleştirilemediği belirtildi. Depodaki `DONANIM/SSR/README.md` ve aday veri sayfası notu proje `hardware/references/` altına kopyalandı; SSR modeli doğrulanmamış olarak kaldı. Bias üretim alt devresi kullanıcı onayıyla tamamlandı olarak işaretlendi: RN130421 + KBU6M + 2200 µF / 35 V + L78L33 ve ayrı breadboardda 2×10 kΩ ile orta noktadan GND'ye 104 (100 nF) seramik.
- **Doğrulama:** README, STATUS, inventory, references index, T001 ve open-questions çapraz kontrol edildi. Fotoğraf bu sohbet içinde görüldü ancak dosya olarak repository'ye yüklenmedi. Stok adetleri kullanıcı beyanıdır; fiziksel sayım veya bağımsız elektriksel ölçüm yapılmadı.
- **Açık kalanlar:** PZEM akım varyantı/CT; proje için seçilecek ESP32 kartı ve ADC/VREF; SCT sinyalinin bias noktasına kuplajı ve analog ön uç değerleri; SSR'nin bu projede kullanılıp kullanılmayacağı ve fiziksel modeli; referans cihazı ve yükler.
- **Sonraki adım:** PR kontrolünü doğrula. Sonrasında T001'in kalan proje-özel kararlarını kapat; bias üretim alt devresi için ek bileşen bilgisi isteme.
- **Kanıt:** [Güncel envanter](../hardware/inventory.md); [proje durumu](../STATUS.md); [T001](../tasks/T001-hardware-inventory.md); [SSR referansı](../hardware/references/SSR.md); [PR dalı](https://github.com/bakbalik-win11/BERO/tree/docs/add-ssr-esp32-stock-complete-bias).


## 2026-10-27 — Mevcut PZEM kaydının esas alınması ve PZCT-02'nin tanımlanması

- **Durum:** TAMAMLANDI; [PR #14](https://github.com/bakbalik-win11/BERO/pull/14) birleştirildi ve otomatik kapanış kontrolü başarılı.
- **Hedef ve kabul ölçütü:** PZEM için mevcut BERO donanım kaydını kullanmak; kullanıcının fotoğrafı yalnızca mevcut modül/CT bağlantısını gösterme amacıyla paylaştığını kaydetmek ve bağlı CT modelini kesinleştirmek.
- **Yapılan:** `DONANIM/PZEM-004T/README.md` esas kaynak olarak gösterildi. Kullanıcı CT modelini PZCT-02 (0–100 A) olarak belirtti; fotoğraf bu CT'nin PZEM'e bağlı olduğunu gösteriyor. Envanter ve proje durumu 100 A harici CT konfigürasyonuyla eşitlendi. PZEM varyantı/CT modeline ilişkin açık soru kaldırıldı; README, T001 ve open-questions güncellendi.
- **Doğrulama:** PR #14 oturum kapanış kontrolü başarılı: [GitHub Actions](https://github.com/bakbalik-win11/BERO/actions/runs/40551531106). Mevcut BERO PZEM kaydı okundu. Fotoğrafı ayrıca repo dosyası olarak eklemeye gerek yok.
- **Açık kalanlar:** ESP32/kart ve ADC/VREF seçimi; SCT sinyalinin bias noktasına kuplajı ve analog ön uç değerleri; PZEM okuma zamanlaması/kararlılığı deneyleri; referans cihazı ve yükler; SSR'nin bu projede kullanılıp kullanılmayacağı.
- **Sonraki adım:** T001 kapsamında yalnızca kalan proje-özel bağlantı ve MCU/ADC kararlarına devam et; mevcut PZEM belgesini veya CT modelini yeniden sorma.
- **Kanıt:** [Ana PZEM donanım kaydı](../../../DONANIM/PZEM-004T/README.md); [proje envanteri](../hardware/inventory.md); [proje durumu](../STATUS.md); [PR #14](https://github.com/bakbalik-win11/BERO/pull/14); [birleştirme commit'i](https://github.com/bakbalik-win11/BERO/commit/8ca4fc05b5955cc29671aafa11c5126e4e62585a).

## 2026-10-27 — Çözümlenmiş PZEM sorusunun son envanter satırlarından temizlenmesi

- **Durum:** UYGULANDI; PR #15 kontrolü tekrar çalıştırılacak.
- **Hedef ve kabul ölçütü:** PZCT-02 ve PZEM varyantı çözümlenmişken envanterdeki eski soru satırlarını temizlemek; STATUS ve oturum günlüğünü güncel tutmak.
- **Yapılan:** Donanım envanterindeki “Kalan proje-özel bilgiler” bölümünden PZEM'in 10 A / 100 A varyantını yeniden soran madde kaldırıldı. STATUS'taki sıradaki iş ESP32/kart, ADC/VREF ve analog ön uç olarak düzeltildi. PZEM ve CT bilgisi mevcut `DONANIM/PZEM-004T/README.md` ile ilişkili kalır.
- **Doğrulama:** İlk PR #15 kapanış denetimi yeni tarihli oturum girdisi eksikliğini bildirdi; bu günlük girdisi o nedenle eklendi. [PR #15 Checks](https://github.com/bakbalik-win11/BERO/pull/15/checks) üzerinden sonuç yeniden doğrulanacak.
- **Açık kalanlar:** Kullanılacak ESP32 kartı/modülü ve ADC/VREF; SCT sinyalinin tamamlanmış bias noktasına kuplajı ve analog ön uç değerleri; referans cihazı/yükler ve deneyler.
- **Sonraki adım:** PR #15 kontrolünü tamamla; ardından yalnız kalan proje-özel donanım kararlarını sırayla sor.
- **Kanıt:** [Güncel envanter](../hardware/inventory.md); [proje durumu](../STATUS.md); [PR #15](https://github.com/bakbalik-win11/BERO/pull/15).

## 2026-10-27 — Dört ESP32 kartı ve SSR elektriksel özelliklerinin kaydı

- **Durum:** UYGULANDI; PR ve otomatik kapanış kontrolü bekleniyor.
- **Hedef ve kabul ölçütü:** İlk aşamadaki dört ESP32 geliştirme kartını ve mevcut dört kanallı SSR kartının kullanıcı tarafından sağlanan özelliklerini tutarlı şekilde envantere geçirmek; önceki SSR belirsizliğini azaltırken okunamayan model kodunu uydurmamak.
- **Yapılan:** İlk aşama kartları 2× ESP32-WROOM-32D, 1× ESP32-WROOM-32E ve 1× genel ESP-WROOM-32 tabanlı NodeMCU ESP32 Bluetooth olarak kaydedildi. Dört kanallı SSR kartı OMRON (kullanıcı beyanı), fototriyak izolasyon, zero-cross, LOW 0–0,5 V / belirsiz 0,5–2,5 V / HIGH 2,5–20 V; kanal başına 75–264 VAC, bildirilen 0,1–2 A ve nominal 100–240 VAC değerleriyle kaydedildi. Kaynak `DONANIM/SSR/` belgesi ve proje referans kopyaları güncellendi. SSR'nin tam model kodu okunamadığından G3MB yalnız karşılaştırma kaynağı olarak kaldı.
- **Doğrulama:** Kullanıcının kart fotoğrafları ve sağladığı teknik bilgiler esas alındı; bağımsız elektriksel test/ölçüm yapılmadı. README, STATUS, envanter, T001, açık sorular, SSR kaynak dosyaları ve proje kopyaları eşitlendi.
- **Açık kalanlar:** Fiziksel ADC/VREF; SCT kuplajı, burden/filtre ve ADC giriş aralığı; SSR tam model kodu, giriş akımı, termal yükleme sınırları, kontrol GPIO'su; referans cihazı ve deney yükleri.
- **Sonraki adım:** ADC ve VREF seçimini netleştir; ardından SCT analog ön uç bağlantısını belgele. SSR kontrol/ yük ataması ayrı bir karar olarak kalır.
- **Kanıt:** [Proje envanteri](../hardware/inventory.md); [proje durumu](../STATUS.md); [SSR referansı](../hardware/references/SSR.md); [ana SSR kaydı](../../../../DONANIM/SSR/README.md).

## 2026-10-27 — DS3231 RTC'nin ölçüm projesine eklenmesi

- **Durum:** UYGULANDI; PR ve otomatik kapanış kontrolü bekleniyor.
- **Hedef ve kabul ölçütü:** Kullanıcının DS3231 kullanım kararını proje envanterine işlemek; BERO'daki mevcut donanım referansını kopyalamak ve teknik özellikleri üretici belgesiyle doğrulamak.
- **Yapılan:** [`DONANIM/DS3231/README.md`](../../../DONANIM/DS3231/README.md) temel alınarak proje içi [DS3231 referansı](../hardware/references/DS3231.md) oluşturuldu. Resmî veri sayfası bağlantısı ayrı dosyaya kopyalandı. DS3231; takvim/saat tabanlı ölçüm zaman damgaları için seçildi. Referans, resmî veriler olarak I²C 400 kHz, adres 0x68, VCC 2,3–5,5 V, ±2 ppm (0–40 °C), ±3,5 ppm (-40…+85 °C), iki alarm ve pil yedekleme özelliklerini kaydeder. Önceki ESP32-C3 GPIO0/GPIO1 pin planı bu projeye aktarılmadı.
- **Doğrulama:** Analog Devices resmî ürün sayfası ve DS3231 Rev. 10 PDF kullanıldı. BERO'daki 16 Ekim RTC/NTP logu yalnız önceki RTC okuma örneğinin kanıtı sayıldı; bu projede pil kesinti testi yapılmış olarak işaretlenmedi.
- **Açık kalanlar:** Gerçek breakout kart revizyonu, pil ve olası şarj devresi, I²C pull-up seviyesi ve SDA/SCL pinleri; ilk saat ayarlama yöntemi ve saat dilimi. ADC/VREF ve SCT analog ön uç kararları da açık.
- **Sonraki adım:** DS3231 modülünün pin ve pil devresini doğrula; I²C pinlerini seçilen ESP32 kartının pin planına göre belirle.
- **Kanıt:** [DS3231 proje referansı](../hardware/references/DS3231.md); [resmî veri sayfası](https://www.analog.com/media/en/technical-documentation/data-sheets/ds3231.pdf); [güncel envanter](../hardware/inventory.md); [açık sorular](../docs/open-questions.md).

## 2026-10-27 — Satın alma bağlantısıyla SSR kanal sayısının düzeltilmesi

- **Durum:** UYGULANDI; PR ve otomatik kapanış kontrolü bekleniyor.
- **Hedef ve kabul ölçütü:** Kullanıcının gerçek ürün bağlantısını esas alarak önceki yanlış dört-kanal kaydını düzeltmek ve elektriksel özellikleri satıcı sayfasına bağlamak.
- **Yapılan:** Kullanıcının verdiği [SAMM Market 5V 2 Kanal Solid State Röle Kartı](https://market.samm.com/5v-2-kanal-solid-state-role-karti) satın alma kaynağı olarak kaydedildi. Ürün adı, tedarikçi kodu İzmo9659, SKU MP02637 ve 2 kanal bilgisi işlendi. Satıcı sayfasındaki 5 V DC / iki kanal açıkken 160 mA, giriş gerilim açıklaması, 75–264 VAC ve 0,1–2 A/kanal, nominal 100–240 VAC, fototriyak ve zero-cross bilgileri kaydedildi. Kaynak `DONANIM/SSR/` dosyaları ve proje referansları 2 kanallı ürünle eşitlendi.
- **Doğrulama:** Ürün sayfası kaynak alındı. Sayfada “low level trigger” ifadesi ile LOW=kapalı/HIGH=açık gerilim açıklaması olası bir belirsizlik oluşturuyor; kontrol girişinin gerçek mantığı düşük gerilimli, şebekeden bağımsız masa testinde doğrulanmadan GPIO davranışı kesin kabul edilmeyecek. Fiziksel SSR entegresinin tekil model kodu doğrulanmadı.
- **Açık kalanlar:** Hangi iki AC yükün anahtarlanacağı, kontrol GPIO'ları, tetik mantığı, giriş akımı ve termal sınırlar.
- **Sonraki adım:** İki kanalın yüklerini belirle; sonra düşük gerilimli giriş mantığı testini planla.
- **Kanıt:** [SAMM Market ürün sayfası](https://market.samm.com/5v-2-kanal-solid-state-role-karti); [SSR kaynak kaydı](../../../DONANIM/SSR/README.md); [proje envanteri](../hardware/inventory.md); [açık sorular](../docs/open-questions.md).


## 2026-10-27 — T001 stok ve 8 kanallı analog arayüz bilgilerinin eşitlenmesi

- **Durum:** UYGULANDI; envanter ve proje yönlendirme dosyaları ana dala commit edildi. Teknik kabul maddeleri açık olduğundan T001 henüz TAMAMLANDI değil.
- **Hedef ve kabul ölçütü:** Kullanıcının bildirdiği tüm T001 donanım ayrıntılarını tek bir yerde bırakmayıp ana envanter, görev kartı, proje durumu, yol haritası, açık sorular ve analog ön uç notları arasında tutarlı biçimde kaydetmek; bilinmeyen elektriksel ayrıntıları uydurmamak.
- **Yapılan:** T001 kullanıcı envanter notu oluşturuldu/güncellendi; 7 adet SCT013 30 A / 1 V, 10 adet SCT013 100 A / 1 V, jack yuvaları, masaüstü 5 V / 1,8 A güç kaynağı, lamba test yükü ve bağlantı parçalarının mevcut olduğu kaydedildi. Kullanıcının önceden hazırladığı 8 kanallı, kanal başına ayrı bias/direnç ağı olan kart ve isteğe bağlı MCP ADC bilgisi işlendi. T001 görev kartı, tasks/README, STATUS, ROADMAP, hardware/inventory, docs/open-questions, hardware/frontend ve proje README tutarlılaştırıldı.
- **Doğrulama:** Her değişiklik GitHub Contents API üzerinden commit sonucu döndürdü. Commitler: T001 envanter notu `1d12b7b`; görev kartı `b2f6faf`; görev listesi `34b8163`; STATUS `74fa8f5`; ana envanter `42a00d5`; ROADMAP `4b5a5bc`; açık sorular `7148525`; analog ön uç `357d966`; README `aae2126`. Bu oturumda fiziksel elektriksel ölçüm, donanım testi veya deney çalıştırılmadı.
- **Açık kalanlar:** Gerçekte kullanılacak ADC modeli/revizyonu ve VREF; SCT AC sinyalinin bias noktasına kuplajı; kanal başına direnç/filtre değerleri ve güvenli ADC aralığı. Referans cihazı/yük seviyeleri T003 kapsamındadır.
- **Sonraki adım:** Önce mevcut BERO kayıtlarından ADC/MCU seçeneklerini kontrol et; kullanıcıyı bilinen stok veya hazır kart ayrıntılarını yeniden vermeye zorlama. Kalan gerçek proje-özel kararları birer birer ele al.
- **Kanıt:** [T001 envanter özeti](../docs/inventory/T001-fiziksel-donanim-envanteri.md); [ana donanım envanteri](../hardware/inventory.md); [aktif görev](../tasks/T001-hardware-inventory.md); [STATUS](../STATUS.md); [ROADMAP](../ROADMAP.md); [açık sorular](../docs/open-questions.md).


## 2026-10-27 — Depo tutarlılığı kuralının çalışma protokolüne eklenmesi

- **Durum:** UYGULANDI.
- **Hedef ve kabul ölçütü:** Depo bilgilerinin kullanıcı için kritik olduğu önceliğini kalıcı proje çalışma kuralına dönüştürmek; ilgili belgeleri çapraz kontrol etme ve commit sonrası yeniden okuma yükümlülüğünü açıkça belirtmek.
- **Yapılan:** AGENTS.md içine depo tutarlılığı ve kullanıcı önceliği bölümü eklendi. İlgili görev, durum, yol haritası, açık sorular, envanter/teknik belgeler ve oturum günlüğünün aynı iş kapsamında kontrol edilmesi kuralı yazıldı.
- **Doğrulama:** AGENTS.md güncellemesi GitHub tarafından commit edildi: `67d5392e52650a8b496e6f4a864de135f4a4e2bb`.
- **Açık kalanlar:** Kullanıcı hesabındaki ChatGPT Memory kapalı olduğundan bu tercihi kişisel belleğe kaydetmek mümkün değil; kullanıcı isterse Settings → Personalization → Memory üzerinden etkinleştirebilir.
- **Sonraki adım:** Bu projede her anlamlı depo oturumunda yeni çalışma kuralını uygula ve kullanıcıya commit/kanıt bağlantılarını ver.
- **Kanıt:** [AGENTS.md](../AGENTS.md); [depo çalışma protokolü](../SESSION_PROTOCOL.md).


## 2026-10-27 — SCT/PZEM kararlı alan etiketleme ve model doğrulama hedefinin netleştirilmesi

- **Durum:** Hedef mimari ve proje notları güncellendi; firmware, algoritma ve deneyler yapılmadı.
- **Hedef ve kabul ölçütü:** Kullanıcının açıkladığı yöntemi eski zaman-temelli önerilerden ayırarak kaydetmek: PZEM entegrasyonu ile paket bağlamını kullanıp SCT/PZEM kararlı alanlarını belirlemek, etiketli SCT verisiyle Python'da kalibrasyon modeli çıkarmak ve modeli çok paketli ham veride sınayıp gerekirse iyileştirmek.
- **Yapılan:** `docs/architecture/sct-pzem-labeling-and-calibration.md` hedef mimari notu ayrıntılandırıldı. Temel yöntemin salt zaman damgası veya sabit olay-sonrası süre olmadığı; paket bağlamı ve kararlılık algoritması/istatistikleriyle alan etiketleme olduğu açıklandı. Kalibrasyon döngüsüne bulunan (f(x)) fonksiyonunu çok paketli ham akışta deneme ve sonuçlara göre iyileştirme adımları eklendi. STATUS.md'deki hedef özeti de düzeltildi.
- **Doğrulama:** GitHub dosya güncellemeleri commit sonuçları döndürdü. Mimari notu commit'i [1edc9a7](https://github.com/bakbalik-win11/BERO/commit/1edc9a7e81eb8c5decd12cfb29cec7deb500ef22); STATUS güncellemesi [e12e711](https://github.com/bakbalik-win11/BERO/commit/e12e711b41dcadb14dee927233838251f1a050c4). Önceki arşivlenmiş teknik raporlar ve Markdown derlemesi incelendi; bu belgelerdeki yaklaşık 3 s geçiş maskesi eski başlangıç önerisi olarak ele alındı, nihai etiketleme kuralı yapılmadı.
- **Açık kalanlar:** Paket bilgisinin PZEM ve SCT örneklerine nasıl ulaştırılacağı; kararlı alan algoritması/istatistik eşikleri; etiket şeması; (f(x)) biçimi, referans ölçüm ve doğrulama ölçütleri. ADR-003/ADR-006 mevcut durumlarıyla otomatik olarak değiştirilmedi.
- **Sonraki adım:** Kullanıcı T001 kapsamında mimariyi anlatmaya devam ederken hedefi dinle; algoritma, paket alım mimarisi veya model biçimi konusunda erken karar verme. Uygulama ve deneyleri mevcutmuş gibi kaydetme.
- **Kanıt:** [Hedef mimari notu](../docs/architecture/sct-pzem-labeling-and-calibration.md); [STATUS](../STATUS.md); [arşivlenmiş BERO Markdown derlemesi](https://github.com/bakbalik-win11/BERO/blob/09775fe58f608cf31161c8a04636c6836b24f03d/PROJELER/SCT013-PZEM-AKIM-GOZLEM/docs/decisions/ADR-003-pzem-as-slow-label.md).


## 2026-10-27 — Eğitim referansının PZEM olarak netleştirilmesi
- **Kullanıcı kararı:** Projenin referansı PZEM'dir; hedef SCT verisini PZEM okumalarıyla etiketleyerek/eğiterek model oluşturmaktır. önceki pens ampermetre adayı ve True RMS gereksinimi bu projeden çıkarılacaktır.
- **Dokümantasyon:** T003, donanım envanteri, STATUS ve ROADMAP bu karara göre güncellendi. Geçmiş kayıtlardaki alternatif cihaz notları bu karara göre sadeleştirildi.

- **Karar düzeltmesi:** Önceki oturum notlarında adı geçen alternatif pens ampermetre adayı proje referansı değildir. Kullanıcının netleştirdiği üzere PZEM, SCT verisini etiketleme/eğitme için temel referanstır; proje hedefinde True RMS cihaz şartı bulunmaz.


## 2026-10-27 — T003 kapsamının daraltılması
- **Kullanıcı kararı:** PZEM kararlı anlarını gözlemleme, SCT kararlı an istatistiklerini çıkarma ve bu alanları eşleştirme T003 işi değildir; bunlar ayrı görev/deney kapsamında ele alınacaktır.
- **Yapılan:** T003 yalnız PZEM'e göre model kabul hata hedefini tanımlayacak şekilde düzenlendi. Görev indeksi, STATUS, ROADMAP ve açık sorular aynı kapsamla eşitlendi.


## 2026-10-27 — T003 model kabul hedefinin belirlenmesi
- **Kullanıcı kararı:** PZEM akım okumasına göre ±%4 bağıl sapma yeterlidir. Python, geçerli PZEM referansı sıfırdan farklı olduğunda bağıl sapmayı hesaplayacak; sapma %4 veya altındaysa `OK`, üzerindeyse `OUT_OF_RANGE` verecek.
- **Kapsam sınırı:** PZEM kararlı anlarını gözlemleme, SCT kararlı an istatistiklerini çıkarma ve alan eşleştirme T003 dışında, ilgili görev/deneylerde kalır.
- **Yapılan:** T003 TAMAMLANDI yapıldı; görev indeksi, proje kapsamı, STATUS, ROADMAP, açık sorular ve hedef mimari aynı kararla güncellendi. Aktif görev T004 oldu.


## 2026-10-27 — 8 kanallı arayüz kaydının düzeltilmesi

- **Kullanıcı düzeltmesi:** 8 kanallı analog arayüz kartı yoktur. Mevcut devre breadboard üzerindeki bias alt devresidir.
- **Yapılan:** Güncel proje belgelerindeki 8 kanallı kart ve kanal başına ayrı bias/direnç ağı iddiaları kaldırıldı. Güncel donanım tarifi 2 × 10 kΩ dirençli orta nokta ve orta noktadan GND'ye 104 (100 nF) kondansatörlü breadboard bias devresi olarak düzeltildi. Bu aşamada harici ADC kullanılmayacak; MCP3208 sonraki aşamaya ayrılmıştır.
- **Not:** Bu günlükteki önceki satırlar tarihsel kayıt olarak kalır; güncel donanım durumu değildir.


## 2026-10-27 — Gün 1: depo hafızası, fikirden göreve ilerleme ve kullanıcı beyanı ilkesi

- **Durum:** UYGULANDI; değiştirilen dosyalar GitHub'dan yeniden okunarak doğrulandı.
- **Hedef:** Sohbet geçmişine bağımlılığı azaltmak; proje hafızasını depoda tutmak; fikirleri erkenden göreve zorlamadan aşamalı ilerleme düzenini korumak.
- **Yapılan:** Kişisel çalışma/iletişim notları kök dizindeki `KISISEL_NOTLAR.md` dosyasına eklendi. Mükerrer `tasks/TASK-001-hardware-inventory.md` kaldırıldı; `tasks/T001-hardware-inventory.md` esas kayıt olarak bırakıldı. `ILKELER.md` içine kullanıcının bir işi yaptığını veya tamamladığını açıkça bildirmesi halinde bunun proje kaydında tamamlanmış kabul edilmesi ve aynı işi gereksiz yere tekrar istememe ilkesi eklendi. T001, T002 ve STATUS metinleri bu anlayışla sadeleştirildi.- **Doğrulama:** `KISISEL_NOTLAR.md`, `ILKELER.md`, T001, T002 ve STATUS GitHub'dan yeniden okundu. Eski TASK-001 dosyasının artık bulunmadığı ve ROADMAP/görev indeksinde eski dosya adına referans olmadığı kontrol edildi. İlgili commitler: mükerrer dosyanın kaldırılması `69fcc53330dd9db16c001d1e761fc9745ec94af4`; kullanıcı beyanı ilkesi ve kayıt güncellemeleri `80a8362b2fd7916fa201a3d7a2d9c6f4cd7e44e2`, `a35dd953d43e95b3927589e2a2b6526dff542a2b`, `c4eb17ba58f460bf09c801693af3e351f032d3e8`, `a291c519741f793c5f968e652ae24b138ffa7bf9`.
- **Açık kalanlar:** Bu kayıt, tüm deponun baştan sona kapsamlı tutarlılık denetiminin yapıldığı anlamına gelmez. Sohbet bağlamından bağımsız devam edebilmek için her yeni oturumda protokoldeki gibi güncel depo kaynakları okunup karşılaştırılmalıdır.
- **Sonraki adım:** Her anlamlı yeni bilgi ortaya çıktığında doğru dosyaya anında kaydet; oturum sonunda ilgili görev, STATUS, ROADMAP ve günlük kayıtlarının birbiriyle uyumunu kontrol et.
- **Kanıt:** [Kişisel notlar](../../../KISISEL_NOTLAR.md); [proje ilkeleri](../ILKELER.md); [T001](../tasks/T001-hardware-inventory.md); [T002](../tasks/T002-safety-checklist.md); [STATUS](../STATUS.md); [ROADMAP](../ROADMAP.md).


## 2026-10-29 — E08 planının depo genelinde eşitlenmesi

- **Kullanıcı kararı:** SCT'yi tanıma deneyleri şu sırayla yapılacak: (1) yüksüz uzun okuma, (2) 100 W akkor ampulde hız × kablo turu karşılaştırması, (3) aynı karşılaştırmanın 150 W akkor ve 8,5 W LED'de tekrarı, (4) ardından aç-kapa davranışı.
- **Karşılaştırma kapsamı:** Hedef hızlar 1/2/2,5 kS/s; iletken turu 1/2/4; aynı örnek penceresinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak. Ortalama, standart sapma, min/max, örnek sayısı ve gerçekleşen örnekleme hızı da kaydedilecek. PZEM veya başka ESP ortalama akımı varsa yalnız genel koşul notu; E08'de SCT pencereleriyle zaman eşleştirmesi yapılmayacak.
- **Gerekçe:** Yüksüz kayıt temel gürültü/bias davranışını; 100 W matrisi hız ve tur etkilerini; 150 W ve LED karşılaştırması yük türü/seviyesi etkisini; aç-kapa testi geçiş ve kararlı görünen bölgeleri anlamak için planlandı. Kararlılık eşiği, gereken pencere sayısı ve kesin kayıt süresi önceden belirlenmeyecek.
- **Depoda yapılanlar:** E08 açıklaması, protokolü, metadata'sı, sonuç şablonu ve dört aşama gerekçe dosyası eklendi. `experiments/README.md`, `STATUS.md`, `ROADMAP.md`, proje `README.md`, `docs/open-questions.md` ve `tasks/README.md` E08 kapsamı/bağlantılarıyla eşitlendi. E07 protokolü/metadata/results dosyalarına E08 güncel planına yönlendirme eklendi; E07 geçmişteki uygulanmamış tasarım olarak korunuyor.
- **Aktif iş sırası:** T005 ve E00/E01 yüksüz temel ADC ölçüm hazırlığı hâlâ sıradaki iş; E08 planlandı fakat uygulanmadı.
- **Doğrulama:** E08 dosyaları, deney indeksi ve ana durum belgeleri GitHub'dan yeniden okundu; aşama bağlantıları kontrol edilip README'deki dosya yolları düzeltildi. Fiziksel donanım kurulumu, firmware derlemesi, test veya ölçüm yapılmadı.
- **Kanıt:** [E08 açıklaması](../experiments/E08-sct-characterization/README.md), [protokol](../experiments/E08-sct-characterization/protocol.md), [STATUS](../STATUS.md), [ROADMAP](../ROADMAP.md), [açık sorular](../docs/open-questions.md).


## 2026-10-29 — E00A ham sinyal gözlemi paketleme öncesine alındı

- **Kullanıcı kararı:** Paketleme/aktarımı tasarlamadan önce ham SCT sinyalini görmek; kaydı PC'de yavaş oynatmak ve farklı örnekleme hızlarında hem dalgayı hem temel istatistikleri karşılaştırmak. Bu, sonraki deneylerden önce yapılacak eğitici bir gözlem adımıdır.
- **Deney koşulları:** (1) SCT olmadan bias-only, (2) SCT bağlı ve yüksüz, (3) SCT bağlı 100 W akkor ampul. Başlangıç karşılaştırma hızları 1, 2 ve 2,5 kS/s; gerçek hız kaydedilecek. Her kayıt için ham ADC-zaman grafiği, yavaş oynatma, ortalama, min/max, peak-to-peak, standart sapma, örnek sayısı ve süre incelenecek. Akım hesabı bu deneyin amacı değil.
- **Mimari kararı:** Çift buffer, DMA, her örneğe zaman damgası ve ayrıntılı veri kaybı ölçümü şimdilik zorunlu değil. Basit aktarım yeterli değilse E00A gözlemlerinden sonra karar verilecek. PC'de yavaş oynatma örnekleme hızını düşürmez; yalnız görüntüleme hızıdır.
- **Depo değişiklikleri:** `experiments/E00A-raw-waveform-observation/` README, protocol, metadata ve results eklendi. Deney indeksi, proje README, STATUS, ROADMAP, tasks README ve open-questions E00A'yı mevcut E00/E01 ve paketleme kararından önce konumlandıracak şekilde güncellendi.
- **Durum/doğrulama:** Plan depoya kaydedildi; fiziksel ölçüm, firmware geliştirme/derleme ve grafik üretimi yapılmadı. E00A henüz uygulanmadı.
- **Kanıt:** [E00A açıklaması](../experiments/E00A-raw-waveform-observation/README.md), [protokol](../experiments/E00A-raw-waveform-observation/protocol.md), [STATUS](../STATUS.md), [ROADMAP](../ROADMAP.md).


## 2026-10-29 — E00A ilk geçişinin istatistik merkezli sadeleştirilmesi

- **Kullanıcı kararı:** Grafik görmek tek başına yeterli çıktı değil; deneyin anlamlı sonuç üretmesi öncelikli. İlk geçişte üç koşulun istatistikleri karşılaştırılsın; grafik gerektiğinde açıklayıcı/tanı aracı olsun.
- **Güncellenen plan:** Bias-only, SCT yüksüz ve 100 W akkor koşullarında tek ESP32 ile yaklaşık 1 saniyelik ham kayıt; ilk hedef 2 kS/s. Ortalama, min/max, tepe-tepe aralığı, standart sapma, örnek sayısı, kayıt süresi ve yaklaşık gerçekleşen hız karşılaştırılacak. Ham kayıtlar yerelde saklanacak.
- **Kapsam sınırı:** 1 ve 2,5 kS/s ek kayıtları, yavaş oynatma, üç ESP32'yi eşzamanlama, DMA ve çift buffer ilk aşamanın şartı değil. İlk istatistikler bir soruyu cevapsız bırakırsa sonraki deney buna göre tasarlanacak. Bu karar daha sonraki örnekleme hızı deneyini iptal etmez.
- **Depoda güncellenenler:** E00A README/protocol/metadata/results; deney indeksi; STATUS; ROADMAP; proje README; görev indeksi; açık sorular; bu oturum günlüğü.
- **Doğrulama sınırı:** Bu kayıt bir plan değişikliğini belgelemektedir. Fiziksel kurulum, firmware derleme, örnekleme veya ölçüm yapılmadı.


## 2026-10-29 — Her adımda HEDEF / LOG / SONUÇ kuralı

- **Kullanıcı kararı:** BERO'daki her çalışma ve deney adımında hedef, yapılan işin kaydı (log) ve sonuç düzenli tutulacak.
- **Kural:** HEDEF, cevaplanacak soru ve kabul ölçütüdür. LOG, gerçekte yapılan işlem, ayarlar, süre/örnek sayısı, ham veri yolu, gözlemler ve sapmalardır. SONUÇ, kanıtın desteklediği yorum, sınırlamalar ve sonraki adımdır. İşlem yapılmadıysa açıkça yazılır; veri yokken sonuç uydurulmaz.
- **Depoya eklenen:** AGENTS.md çalışma protokolü, E00A protocol.md ve results.md bu standarda göre güncellendi.
- **Doğrulama sınırı:** Bu bir dokümantasyon/iş akışı kararıdır. Donanım deneyi veya firmware testi yapılmadı.


## 2026-10-29 — Deney koşullarının açıklamalı YAML ile kaydı

- **HEDEF:** Deney kodunun/firmware'inin hangi deney koşullarını temsil ettiğini açıkça belgelemek ve aynı koşulları daha sonra yeniden kurmayı kolaylaştırmak.
- **LOG:** Kullanıcı, açıklamalı YAML dosyalarının da eklenmesini ve kodların deney koşullarını içermesini istedi. E00A için `experiment.yaml` planlandı; genel çalışma kuralı, E00A README/protocol/results bağlantıları eklendi.
- **SONUÇ:** YAML deneyin planlanan koşullarını ve açıklamalarını kayıt altına alır. Firmware YAML'ı gerçekten okumadığı sürece bu dosya otomatik çalışma ayarı değildir. Henüz firmware yazılmadı, derlenmedi ve fiziksel ölçüm yapılmadı.


## 2026-10-29 — YAML ve kod koşullarının atlanamaz proje kuralı

- **HEDEF:** Deney kodlarının hangi deney koşullarında çalıştığını her zaman anlaşılır kılmak ve bu gerekliliği kalıcı depo kuralına dönüştürmek.
- **LOG:** Kullanıcının açık talebi doğrultusunda AGENTS.md'ye atlanamaz uygulama maddeleri eklendi; ILKELER.md'ye kalıcı proje ilkesi eklendi. Deney YAML'ı, kod içi açıklamalar, protokol, sonuç ve oturum günlüğünün tutarlı tutulması şartı yazıldı.
- **SONUÇ:** Bundan sonra deney kodu hazırlama işinde açıklamalı YAML ve kodun deney koşullarını açıklayan yorumları zorunludur; her adımda HEDEF / LOG / SONUÇ tutulur. Bu oturumda yalnızca kural belgelendi; firmware veya fiziksel deney yapılmadı.


## 2026-10-29 — Depo sürekliliği kullanıcı önceliği

- **HEDEF:** Proje bilgisinin ve önceki kararların kaybolmamasını BERO'nun en üst çalışma önceliği olarak kaydetmek.
- **LOG:** Kullanıcı, deponun proje başarısından daha önemli olduğunu ve kaybolmak istemediğini belirtti. AGENTS.md'nin oturum başlangıcına ve ILKELER.md'nin başına açık öncelik kuralı eklendi.
- **SONUÇ:** Her oturumda önce mevcut depo bağlamı okunacak; yeni kararlar aynı çalışma akışında kaydedilecek; yazılan dosyalar yeniden okunarak doğrulanacak. Teknik çalışma yapılamasa bile alınan karar ve sonraki adım korunacak. Bu kayıt bir süreç kuralıdır; fiziksel deney yapılmadı.


## 2026-10-29 — İlerleme ağacı fikri

- **HEDEF:** Projenin genel ilerlemesini, tamamlanan işleri, aktif adımı ve sıradaki işi tek bakışta anlaşılır kılmak; proje hafızasının kaybolma riskini azaltmak.
- **LOG:** Kullanıcı depo yapısında ilerleme ağacı gerekip gerekmediğini sordu. Mevcut STATUS.md, ROADMAP.md, tasks/README.md ve experiments/README.md incelendi. I004 fikri IDEA_BACKLOG.md'ye eklendi.
- **SONUÇ:** Öneri, mevcut kayıtların yerine geçen ikinci bir görev sistemi değil; bunlara bağlantı veren kısa bir gezinme/ilerleme görünümü oluşturmak. Henüz ayrı ağaç dosyası oluşturulmadı; fikir değerlendirme aşamasında.


## 2026-10-29 — Genel ilerleme ağacı oluşturuldu

- **HEDEF:** Kullanıcının deponun bütün dosyalarını okumak zorunda kalmadan BERO'nun genel yapısını, mevcut fazını ve sıradaki adımını kabaca görebilmesini sağlamak.
- **LOG:** `PROGRESS_TREE.md` oluşturuldu. Fazlar, tamamlanan hazırlık işleri, E00A'nın sıradaki deney olması ve sonraki ana alanlar özetlendi. STATUS.md'ye ağaç bağlantısı eklendi; AGENTS.md'ye aktif durum değiştikçe ağacı STATUS ile birlikte güncel tutma kuralı eklendi.
- **SONUÇ:** Ağaç genel bakış/navigasyon içindir; görev ve deney belgelerinin yerine geçmez. Yazılan dosyalar yeniden okunarak doğrulanacak. Fiziksel deney veya firmware testi yapılmadı.


## 2026-10-29 — Depo bütünlüğü denetimi ve tutarlılık düzeltmeleri

- **HEDEF:** Depo, projenin teknik başarısından daha öncelikli olduğu için aktif kararları, deney sırasını, görev durumlarını ve yönlendirme bağlantılarını tutarlı tutmak; eksik kayıtları tamamlamak.
- **LOG — yapılan değişiklikler:**
  - `calibration/PROCEDURE.md` ve `tasks/T006-calibration.md`, PZEM'in eğitim/değerlendirme referans akışı olduğu, True-RMS referans cihazının zorunlu olmadığı ve ±%4 hedefinin PZEM'e göre uyumu ifade ettiği şekilde güncellendi.
  - `experiments/E02-resistive-steady/protocol.md` aynı referans ve kararlı alan yaklaşımıyla güncellendi.
  - `ROADMAP.md` içindeki yinelenen T003 bağlantısı kaldırıldı; olaydan sonra sabit 3 saniye etiketleme maddesi, deney verisiyle kararlı/geçiş alanı belirleme ilkesiyle değiştirildi.
  - `STATUS.md` eski E07 sonraki iş maddesi E08'in güncel plan olduğu şekilde düzeltildi; G1 açıklaması PZEM'e uyum hedefi olarak netleştirildi.
  - `PROGRESS_TREE.md` güncel deney sırası ve sabit zaman maskesinin nihai etiket kuralı olmadığı bilgisiyle güncellendi.
  - `IDEA_BACKLOG.md` içindeki I004, oluşturulmuş `PROGRESS_TREE.md` dosyasına bağlı olarak GÖREVE ALINDI durumuna getirildi.
  - `AGENTS.md` içindeki yinelenen HEDEF/LOG/SONUÇ bölümü tekilleştirildi.
  - E00 için eksik `results.md` oluşturuldu ve deney indeksine bağlandı. Dosya açıkça ölçüm yapılmadığını belirtiyor.
  - E08 Aşama 1 için yinelenen ayrıntı dosyası, tek esas belge olan `stage-01-no-load.md` dosyasına yönlendirildi; geçmiş dosya silinmedi.
- **SONUÇ:** Belirtilen dosyalar GitHub'a yazıldı. Bu çalışma yalnızca belge/bağlantı tutarlılığı düzenlemesidir; firmware derlenmedi, fiziksel donanım kurulmadı, deney/ölçüm yapılmadı ve otomatik kontrol/CI çalıştırılmadı.
- **Açık kalanlar:** Depodaki bütün dosyaların içerik ve bağlantı denetimi henüz tamamlanmadı. Kalan deney metadata/protokol dosyalarında eski alanlar, adlandırma farklılıkları ve başka çelişkiler için tarama sürdürülmeli.
- **Sonraki adım:** Değiştirilen dosyaları GitHub'dan yeniden okuyup içeriklerini doğrula; ardından proje içindeki Markdown/YAML bağlantılarını ve karar ifadelerini tarayarak kalan bulguları düzelt.
- **Kanıt:** [Kalibrasyon prosedürü](../calibration/PROCEDURE.md), [T006](../tasks/T006-calibration.md), [E02](../experiments/E02-resistive-steady/protocol.md), [STATUS](../STATUS.md), [ROADMAP](../ROADMAP.md), [İlerleme ağacı](../PROGRESS_TREE.md), [Deney indeksi](../experiments/README.md), [E00 sonuç kaydı](../experiments/E00-bias-adc-baseline/results.md).

## 2026-10-29 — Tutarlılık denetimi: eski etiket ve kalibrasyon ifadeleri

- **HEDEF:** PZEM'in proje içi referans olduğu, sabit 3 saniyenin nihai etiket kuralı olmadığı ve bağımsız True-RMS referans cihazının zorunlu tutulmadığı kararlarını ana belgelerle eşitlemek.
- **LOG:** Proje README'sindeki “3 s başlangıç süresi” ifadesi deney verisiyle kararlı/geçiş alanı belirleme ilkesiyle değiştirildi. ROADMAP'teki “en az üç seviyede kalibrasyon” maddesi, PZEM referanslı model değerlendirmesi ve eğitim/değerlendirme ayrımıyla netleştirildi. Açık sorulardaki “bağımsız referans” ifadesi PZEM'e göre düşük akım kararlılığı ve ±%4 sapma sorusuna dönüştürüldü.
- **SONUÇ:** Üç belgedeki güncel karar ifadeleri yazım sonrası yeniden okunarak doğrulandı. Fiziksel deney, firmware derlemesi ve CI çalıştırılmadı.
- **Açık kalanlar:** Depodaki tüm deney protokolleri/metadata dosyaları ve Markdown bağlantılarının tam denetimi sürüyor; bu değişiklikler tam denetimin bittiği anlamına gelmez.
- **Sonraki adım:** Deney belgeleri arasında YAML şeması, sonuç kayıtları ve kabul ölçütlerini karşılaştırmak; kırık bağlantıları topluca doğrulamak.
- **Kanıt:** [Proje README](../README.md); [ROADMAP](../ROADMAP.md); [Açık sorular](../docs/open-questions.md).

## 2026-10-29 — Deney şablonları ve YAML rollerinin netleştirilmesi

- **HEDEF:** Yeni deney belgelerinin tutarlı, gereksiz laboratuvar varsayımlarından arınmış ve HEDEF / LOG / SONUÇ düzenine uygun başlamasını sağlamak.
- **LOG:** Genel protokol şablonundan zorunlu VREF ve referans cihazı alanları çıkarıldı; deneyle ilgili olmayan alanların yalnız gerektiğinde kullanılması belirtildi. Sonuç şablonu HEDEF / LOG / SONUÇ düzenine geçirildi. Metadata şablonunda varsayılan 2 kS/s, 200 ms, 1 s polling gibi deney yapılmadan kesinleşmiş sayılabilecek değerler null yapıldı. E00 metadata'sındaki sabit ADC çözünürlüğü ve referans cihazı alanları kaldırıldı. E00A README'sinde metadata.yaml ile experiment.yaml rollerinin farkı açıklandı.
- **SONUÇ:** Beş dosya GitHub'dan yeniden okunarak yazılan içerikle eşleştiği doğrulandı. Firmware derlemesi, fiziksel deney, YAML parser veya CI çalıştırılmadı.
- **Açık kalanlar:** E01–E08 metadata/protokol dosyalarında eski şablon alanlarının anlamı, güncel kararlarla uyumu ve dosyalar arası bağlantılar incelenmeye devam ediyor.
- **Sonraki adım:** Deney metadata dosyalarını ortak alanlar ve yanlış varsayımlar açısından taramak; deney sonuç şablonlarının HEDEF / LOG / SONUÇ standardıyla uyumunu karşılaştırmak.
- **Kanıt:** [Protokol şablonu](../experiments/_template/protocol.md); [sonuç şablonu](../experiments/_template/results.md); [metadata şablonu](../experiments/_template/metadata.yaml); [E00 metadata](../experiments/E00-bias-adc-baseline/metadata.yaml); [E00A README](../experiments/E00A-raw-waveform-observation/README.md).

## 2026-10-29 — Deney sonuç kayıtlarının ortak yapıya alınması

- **HEDEF:** E01–E08 sonuç dosyalarında, deney yapılmamış olsa bile durumun ve sonraki adımın tutarlı biçimde kaydedilmesini sağlamak.
- **LOG:** E01, E02, E03, E04, E05, E06, E07 ve E08 sonuç kayıtlarına HEDEF / LOG / SONUÇ bölümü eklendi. E07'nin tarihsel ve uygulanmamış plan olduğu korunurken fiziksel ölçüm/derleme yapılmadığı açıkça belirtildi.
- **SONUÇ:** Sekiz sonuç dosyasının her biri GitHub'dan yeniden okunarak ortak bölümlerin bulunduğu doğrulandı. Fiziksel deney, firmware derlemesi, YAML doğrulaması veya CI çalıştırması yapılmadı.
- **Açık kalanlar:** Metadata dosyalarındaki eski ortak alanlar ve planlanmış değerlerin anlamı; protokol–metadata–results arasındaki bağlantılar; Markdown bağlantılarının tüm depoda doğrulanması.
- **Sonraki adım:** Metadata dosyalarını güncel proje kararlarına göre taramak; ardından bağlantı denetimi ve durum kayıtlarının çapraz kontrolünü tamamlamak.
- **Kanıt:** [E01 sonuçları](../experiments/E01-noise-floor/results.md); [E06 sonuçları](../experiments/E06-load-scenarios/results.md); [E08 sonuçları](../experiments/E08-sct-characterization/results.md); diğer E02–E05 ve E07 sonuç dosyaları aynı klasörlerdedir.

## 2026-10-29 — Eski deney metadata alanlarının temizlenmesi

- **HEDEF:** Deney metadata dosyalarında dış referans cihazı varmış veya zorunluymuş izlenimi veren kullanılmayan alanları kaldırmak.
- **LOG:** E02, E03 ve E04 metadata.yaml dosyalarındaki boş reference_meter alanı kaldırıldı. Bu deneyler için dış True-RMS/referans ölçer şartı tanımlanmıyor; proje referansı gerektiğinde PZEM akışıdır.
- **SONUÇ:** Üç dosya değişiklikten sonra yeniden okundu ve eski alanın kaldırıldığı doğrulandı. E01/E05/E06 metadata dosyalarındaki aynı alanlar sonraki denetim adımında ele alınacak. Test/CI çalıştırılmadı.
- **Açık kalanlar:** Metadata dosyalarında aynı alanın E01/E05/E06 sürümleri, eski varsayılan ayarların gerçekten deney planına ait olup olmadığı ve bütün bağlantıların geçerliliği.
- **Sonraki adım:** Kalan metadata alanlarını aynı ilkeyle gözden geçirmek; ardından STATUS/PROGRESS_TREE ve dosya bağlantılarını denetlemek.
- **Kanıt:** [E02 metadata](../experiments/E02-resistive-steady/metadata.yaml); [E03 metadata](../experiments/E03-pzem-step-response/metadata.yaml); [E04 metadata](../experiments/E04-pzem-field-timing/metadata.yaml).

## 2026-10-29 — GitHub Copilot depo değerlendirmesi ve durum etiketlerinin netleştirilmesi

- **HEDEF:** Copilot tarafından verilen bağımsız depo yorumunu mevcut dosyalarla karşılaştırmak; doğrulanan bulguları düzeltmek, yalnızca yorum niteliğindeki önerileri doğrudan proje kararı saymamak.
- **LOG:** Copilot raporu; çalışan Python/firmware kodu ve gerçek ölçüm bulunmaması, Python mimarisinin taslak olması, GPIO/pin eşlemesinin açık kalması ve dokümantasyon tamamlanmasıyla teknik doğrulamanın ayrılması konularında mevcut depoyla genel olarak örtüşüyor. Depo ağacında proje klasörü altında `.py` dosyası bulunmadığı doğrulandı. T001 ve T004 görev kartlarının durum metinleri, TAMAMLANDI etiketinin envanter/belgeleme kapsamına ait olduğunu ve fiziksel doğrulama anlamına gelmediğini daha açık ifade edecek şekilde güncellendi. Copilot raporundaki E00 → E00A sırası önerisi mevcut kayıttaki E00A → E00/T005/E01 kararıyla farklıdır; bunu sessizce değiştirmedim. Bu sıra ancak ilgili protokoller karşılaştırılarak ve proje kararının gerekçesi netleştirilerek değiştirilebilir.
- **SONUÇ:** T001 ve T004 kartları GitHub'dan yeniden okunarak değişiklikleri doğrulandı. Copilot'ın “%100 Python” iddiası bu denetimde proje dosyalarında doğrulanmadı; proje mimarisi belgesi Python kullanımını hedef olarak anlatıyor, fakat tamamlanmış kod olduğunu söylemiyor. Copilot'ın genel puanları/yorumları ölçüm kanıtı değildir. Fiziksel deney, firmware derlemesi ve CI çalıştırılmadı.
- **Açık kalanlar:** E00A/E00/T005/E01 sıralamasının gerekçesini ana protokoller ve kullanıcı kararıyla bir kez daha çapraz kontrol etmek; schema/FIELDS.md ile gerçek/planlanan kayıt formatlarını eşleştirmek; bütün proje içi bağlantıları otomatik veya dosya bazında doğrulamak; STATUS/ROADMAP/PROGRESS_TREE ile görev durumlarının satır satır uyumunu bitirmek.
- **Sonraki adım:** Depo denetimine devam; henüz deney başlatılmayacak.
- **Kanıt:** [T001](../tasks/T001-hardware-inventory.md); [T004](../tasks/T004-analog-frontend.md); [Python mimarisi taslağı](../docs/architecture/python-program-architecture.md); [STATUS](../STATUS.md); [Copilot değerlendirmesi kullanıcı tarafından bu oturumda sağlandı].

## 2026-10-29 — Depo güvenlik kapısı ve ilk ölçüm öncesi bias planının eşitlenmesi

- **HEDEF:** Depo tutarlılığı tamamlanmadan fiziksel deneye geçilmesini önlemek; deney metadata'sındaki eski referans alanlarını temizlemek ve ADR-007 kondansatör planını E00A → E00 → E01 sırasıyla tutarlı hâle getirmek.
- **LOG:** `experiments/E01-noise-floor/metadata.yaml`, `E05-sample-rate-compare/metadata.yaml` ve `E06-load-scenarios/metadata.yaml` dosyalarından artık kullanılmayan `reference_meter: null` alanları kaldırıldı. ADR-007'nin 10 µF ekleme zamanlaması E01 öncesinden ilk SCT bağlantılı ölçüm olan E00A öncesine taşındı; böylece E00A koşulları arasında ve E00/E01'e geçerken planlanan bias düzeni sabit tutulacak. E00A protokolü, `experiment.yaml`, E01 metadata'sı, STATUS, PROGRESS_TREE ve açık sorular aynı planla eşitlendi. STATUS ve ilerleme ağacına depo güvenlik kapısının açık olduğu, denetim bitmeden deney başlatılmayacağı eklendi.
- **SONUÇ:** Değişen her dosya GitHub'dan yeniden okunarak yeni içerik doğrulandı. Bu kayıt yalnız plan belgelerinin tutarlılığını gösterir; 10 µF fiziksel olarak eklenmedi, donanım kurulmadı, firmware yazılmadı/derlenmedi, ölçüm veya CI çalıştırılmadı.
- **Açık kalanlar:** Depodaki durum sözlüğü ile tüm görev kartlarının etiketlerini çapraz kontrol etmek; `schema/FIELDS.md` ile deney kayıtları arasındaki alanların gerçek/önerilen statüsünü netleştirmek; kritik göreli bağlantıları doğrulamak; son STATUS/ROADMAP/PROGRESS_TREE/log uyum kontrolünü yapmak.
- **Sonraki adım:** Depo denetimine devam; E00A hâlâ planlanan ilk teknik deneydir, fakat güvenlik kapısı kapanana kadar başlatılmayacaktır.
- **Kanıt:** [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md); [E00A protokolü](../experiments/E00A-raw-waveform-observation/protocol.md); [E00A experiment.yaml](../experiments/E00A-raw-waveform-observation/experiment.yaml); [E01 metadata](../experiments/E01-noise-floor/metadata.yaml); [STATUS](../STATUS.md); [PROGRESS_TREE](../PROGRESS_TREE.md); [Açık sorular](../docs/open-questions.md).

## 2026-10-29 — Şema kapsamı ve eksik T007 görev kartı

- **HEDEF:** Veri alanları sözlüğünün henüz çalışan şema/doğrulama kodu olmadığını açıklaştırmak; şema alanlarını E00A ham ADC çıktısıyla karıştırmamak; görev indeksinde referans verilen T007 kartı eksikliğini gidermek.
- **LOG:** `schema/FIELDS.md` içine kapsam/uygulama durumu notu eklendi: belge hedef alan sözlüğüdür, uygulanan Python doğrulama kodu değildir; E00A'da akım RMS'i veya calibration_id üretilmiş varsayılmaz. PZEM şema dosyasında zorunlu olan `synthetic_example` alanı sözlüğe eklendi. `hardware/frontend.md` içindeki 10 µF kondansatör zamanlaması E00A öncesi planla eşitlendi. Görev indeksinde ve mimari belgede T007'ye atıf olduğu hâlde `tasks/T007-python-architecture.md` dosyası bulunmadığı için görev kartı oluşturuldu; kart mimari taslağını ve açık kararları kaydediyor, kod üretimini iddia etmiyor.
- **SONUÇ:** `schema/FIELDS.md`, `hardware/frontend.md` ve yeni T007 kartı GitHub'dan yeniden okunarak doğrulandı. Repo ağacında `schema/pzem_read.schema.json` ve `schema/window_record.schema.json` dosyaları mevcut; önceki aramada farklı dosya adları kullanıldığı için 404 alınmıştı. Bu JSON Schema dosyaları için bu oturumda validator çalıştırılmadı. Proje klasöründe `.py` dosyası yok; Python uygulaması ve testleri yok.
- **Açık kalanlar:** JSON Schema alanlarının FIELDS.md ile tam alan bazında karşılaştırılması; schema validator ve YAML parser erişilebilirliğinin belirlenmesi; göreli Markdown bağlantılarının hedefleriyle kontrolü; STATUS/ROADMAP/PROGRESS_TREE ve görev kartlarının son uyum kontrolü.
- **Sonraki adım:** Kalan çapraz kontrolleri tamamlamak; fiziksel deney ve firmware işi başlatmamak.
- **Kanıt:** [FIELDS.md](../schema/FIELDS.md); [PZEM JSON Schema](../schema/pzem_read.schema.json); [SCT pencere JSON Schema](../schema/window_record.schema.json); [Python mimarisi](../docs/architecture/python-program-architecture.md); [T007 görev kartı](../tasks/T007-python-architecture.md); [Analog ön uç](../hardware/frontend.md).

## 2026-10-29 — Şema alan adları ve görev indeksi bağlantısı

- **HEDEF:** JSON Schema ile FIELDS.md arasındaki alan adlarını açık eşleştirmek ve T007 görev kartını görev indeksinden doğrudan açılabilir yapmak.
- **LOG:** `schema/FIELDS.md` içindeki genel PZEM alan grubu, `voltage_V`, `current_A`, `active_power_W`, `energy_Wh`, `frequency_Hz`, `power_factor` alan adlarıyla açıklandı. `tasks/README.md` içindeki T007 satırı yeni oluşturulan görev kartına bağlantı verecek şekilde güncellendi.
- **SONUÇ:** İki dosya da GitHub'dan yeniden okunup değişiklikler doğrulandı. JSON Schema dosyalarının JSON olarak ayrıştırılması ve required/property listelerinin incelenmesi başarılı oldu; alan adlarının sözlükte açıkça yer alması gereken eksik ifadeler düzeltildi. JSON Schema validator, YAML parser, CI veya fiziksel test çalıştırılmadı.
- **Açık kalanlar:** Kritik Markdown göreli bağlantılarının hedefleriyle kontrolü; `STATUS.md`, `ROADMAP.md`, `PROGRESS_TREE.md`, görev listesi ve günlükte son durum uyumu; varsa kalan eski kondansatör zamanlaması ifadelerinin taranması.
- **Sonraki adım:** Son çapraz denetim ve günlük kapanış kaydı.
- **Kanıt:** [FIELDS.md](../schema/FIELDS.md); [PZEM JSON Schema](../schema/pzem_read.schema.json); [SCT pencere JSON Schema](../schema/window_record.schema.json); [Görev listesi](../tasks/README.md); [T007 görev kartı](../tasks/T007-python-architecture.md).

## 2026-10-29 — Depo belge tutarlılığı denetimi kapanışı

- **HEDEF:** Ana depo durumunu, görev/deney sırasını, şema sözlüğünü ve Markdown göreli bağlantılarını son kez çapraz kontrol etmek; denetim sonucu ile deney hazırlığını birbirinden ayırmak.
- **LOG:** Proje altındaki 87 Markdown dosyasındaki göreli bağlantı hedefleri depo ağacıyla kontrol edildi. Bir kırık bağlantı bulundu: bu günlükte kök dizindeki `KISISEL_NOTLAR.md` bağlantısı bir üst dizini yanlış gösteriyordu; `../../../KISISEL_NOTLAR.md` olarak düzeltildi. Görev listesinde T007'ye atıf olduğu hâlde kart dosyası bulunmadığı tespit edildi; `tasks/T007-python-architecture.md` oluşturuldu ve görev indeksine bağlantısı eklendi. T001/T003/T004 tamamlanma ifadeleri belge/karar kapsamıyla sınırlandırıldı. JSON Schema dosyaları JSON olarak ayrıştırıldı; `FIELDS.md` içindeki PZEM alan adları ve `synthetic_example` alanı şemalarla daha açık eşleştirildi. E00A → E00/T005/E01 sırası STATUS, PROGRESS_TREE, deney protokolleri ve ADR-007 ile karşılaştırıldı; 10 µF ekleme planı ilk SCT bağlantılı ölçüm olan E00A öncesine eşitlendi.
- **SONUÇ:** STATUS ve PROGRESS_TREE güncellendi: belge tutarlılığı denetimi tamamlandı; deney başlangıcı hâlâ beklemede. Değiştirilen dosyalar yazımdan sonra yeniden okundu. Markdown bağlantı kontrolü göreli hedeflerin varlığını denetler; başlık anchor'larının render edildiğini garanti etmez. JSON Schema validator, YAML parser, firmware derlemesi, CI ve fiziksel test çalıştırılmadı.
- **Kalan deney ön koşulları:** Gerçek kullanılacak ESP32 kartı ve ADC destekli GPIO'su belirlenip kart pinout'u ile doğrulanmalı; ADR-007'deki 10 µF fiziksel olarak uygulanırsa fiilî bağlantı metadata'ya yazılmalı; firmware ve gerçek kayıt hazırlığı E00A'dan önce yapılmalı. Bu işler belge tutarlılığı denetiminin tamamlanmasından ayrıdır.
- **Sonraki adım:** E00A için gerçek kart/GPIO ve ölçüm hazırlıklarını depoda kesinleştirmek; ardından yalnız kullanıcı fiziksel düzene hazır olduğunda ilk deney adımına geçmek.
- **Kanıt:** [STATUS](../STATUS.md); [PROGRESS_TREE](../PROGRESS_TREE.md); [Görev indeksi](../tasks/README.md); [T007](../tasks/T007-python-architecture.md); [FIELDS](../schema/FIELDS.md); [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md); [Günlükte düzeltilen kök bağlantısı](../../../KISISEL_NOTLAR.md).

## 2026-10-29 — Copilot bağımsız denetim raporunun karşılaştırılması

- **HEDEF:** Copilot raporundaki bulguları güncel depo kararlarıyla karşılaştırmak; zaten çözülmüş konuları tekrar açmadan gerçek kalan sorunları ayırmak.
- **LOG:** Güncel `tasks/README.md`, `STATUS.md`, `ROADMAP.md`, `docs/open-questions.md` ve `schema/FIELDS.md` okundu. B1 bulgusu, görev durumlarının belge/karar kapsamı ve bağımsız fiziksel doğrulama sınırı zaten açıklandığı için mevcut belgelerde büyük ölçüde karşılanmış kabul edildi. B3 bulgusu, E00A → E00/T005/E01 sırası ve E08'in daha sonraki plan olduğu kaydedildiği için güncel kararla çelişmiyor. B5 bulgusu, `FIELDS.md` hedef alan sözlüğünü uygulanan koddan ve E00A ham ADC çıktısından açıkça ayırdığı için zaten karşılanmış. B2'deki kart/GPIO belirsizliği gerçek bir deney ön koşulu olarak korundu; kart modeli ve pinout'u fiziksel uygulamadan önce seçilip doğrulanmalı. Python mimarisinin taslak olması bilinçli ve uygulama öncesi durumdur; erken kesinleştirme yapılmadı. STATUS üst satırındaki “denetim sürüyor” ifadesi, altındaki tamamlanma kaydıyla çeliştiğinden düzeltildi.
- **SONUÇ:** Yalnızca STATUS güncellik ifadesi değiştirildi. Deney sırası, görev durumları ve hedef şema kararları değiştirilmedi. Copilot raporunun tamamı yeniden açılacak bir hata listesi olarak değil, mevcut dosyalarla karşılaştırılan bağımsız görüş olarak kullanıldı.
- **Doğrulama sınırı:** STATUS ve oturum günlüğü GitHub'a yazıldıktan sonra yeniden okunacak. Bu çalışma fiziksel kurulum, firmware derlemesi, YAML doğrulaması, JSON Schema validator veya CI çalıştırması değildir.
- **Açık kalanlar:** Gerçek ESP32 kartı ve ADC GPIO'su seçilip pinout ile doğrulanacak; ADR-007'de planlanan 10 µF kondansatörün fiziksel kurulumu teyit edilecek; E00A firmware ve kayıt hazırlığı yapılacak.
- **Sonraki adım:** Deney hazırlıklarını mevcut sıraya göre sürdür; fiziksel olarak bilinmeyenleri varsayımla kapatma.
- **Kanıt:** [STATUS](../STATUS.md); [Görev indeksi](../tasks/README.md); [ROADMAP](../ROADMAP.md); [Açık sorular](../docs/open-questions.md); [Alan sözlüğü](../schema/FIELDS.md); [Copilot raporu kullanıcı tarafından sağlandı].


## 2026-10-29 — Copilot denetimi sonrası E00A hazırlık kapısı netleştirildi

- **Değerlendirme:** Copilot raporundaki temel ayrım doğru: belge tutarlılığı denetiminin tamamlanması fiziksel deney hazırlığının tamamlandığı anlamına gelmez. T001–T004 durumları kendi kayıtlı kapsamlarıyla okunmalıdır; T001/T002 kullanıcı beyanına, T003 karar belgelemesine, T004 ön uç belgelemesine dayanır ve hiçbiri E00A'nın fiziksel/firmware doğrulaması değildir.
- **Yeni açıklık:** STATUS belgesinde belge denetimi ile fiziksel hazırlık ayrı durumlar olarak ifade edildi. E00A için ham CSV formatı ve yerel dosya yolları belirlendi: `sample_index,adc_raw`; gerçekleşen ortalama hız `sample_count / elapsed_seconds` üzerinden hesaplanacak. Tek tek örnek zaman damgaları ilk geçişte zorunlu değil.
- **Donanım adayı:** Envanterdeki klasik ESP32-WROOM-32D ve GPIO34 (ADC1_CH6) ilk uygulama adayı olarak yazıldı. Bu bir tasarım adayıdır; gerçek geliştirme kartı ve dışarı çıkarılmış pin eşleşmesi fiziksel olarak doğrulanmadan kablo bağlanmayacak. Kart farklıysa GPIO yeniden seçilecek.
- **ADR-007:** Mevcut 100 nF ile planlanan paralel 10 µF fiziksel olarak hâlâ ayrıdır. 10 µF eklenmeden ve gerçek bağlantı LOG'a geçirilmeden ilk SCT bağlantılı koşul başlatılmaz.
- **Kapsam düzeltmesi:** PZEM zaman damgası/logging entegrasyonu E00A'nın ham ADC gözlemi için ön koşul değildir; bu, ileride PZEM/SCT etiketleme işinde ele alınır. E00A'da gerçek kart/GPIO, fiilî bias düzeni, firmware sürümü, kayıt süresi, örnek sayısı ve ham dosya yolu kaydedilecektir.
- **Doğrulama sınırı:** Bu değişiklikler yalnızca depo plan/dokümantasyonudur. Firmware yazılmadı veya derlenmedi; YAML/JSON Schema doğrulayıcısı, CI ve fiziksel ölçüm bu oturumda çalıştırılmadı. GPIO34 ve kondansatör düzeni fiziksel olarak doğrulanmış sayılmaz.

## 2026-10-29 — Deney ve karar izlenebilirliği güçlendirildi

- **Neden:** Kullanıcı önceki çalışmalarda deney kodlarını ve kod/karar gerekçelerini bulmakta zorlandığını belirtti. Bu oturumun amacı deney yapmak değil, depoda her basamağın nedenini, uygulamasını, kanıtını ve sonraki kararını izlenebilir kılmaktır.
- **Karar:** `EXPERIMENT_LEDGER.md` oluşturuldu. Her deney için “neden, soru/hipotez, karar gerekçesi, gerçek uygulama, kanıt, sonuç, sonraki basamak” bağını tarif eder.
- **Kod ve sonuç ayrımı:** Henüz oluşturulmamış firmware dosyası için yol uydurulmayacak. Protokol/YAML dosyasının varlığı kodun çalıştığını göstermez. Planlandı, kodlandı, derlendi, çalıştırıldı, ölçüldü ve yorumlandı durumları ayrı tutulacak.
- **Gezinme:** Proje `README.md`, `PROGRESS_TREE.md` ve `STATUS.md` üzerinden yeni izleme defterine bağlantı eklendi.
- **Doğrulama sınırı:** Depo dosyaları GitHub'a yazıldı; fiziksel test, firmware derlemesi, YAML parser, CI veya otomatik bağlantı testi bu değişiklik kapsamında çalıştırılmadı.
- **Sonraki adım:** Tek aktif teknik basamak E00A olarak kalır. Fiziksel deney günü geldiğinde önce kart/pinout ve bias kurulumunu doğrula; ardından yalnız bu basamağın kodunu ve ölçüm kaydını oluştur. Daha sonraki deneyleri erkenden kodlama.
- **Kanıt:** [Deney ve karar izleme defteri](../EXPERIMENT_LEDGER.md); [STATUS](../STATUS.md); [İlerleme ağacı](../PROGRESS_TREE.md).

## 2026-10-29 — İlk hedef kapsamı düzeltildi: ham ADC'yi gör ve anla

- **Kullanıcının netleştirdiği amaç:** SCT013'ten ESP32 ADC'sine gelen veride ne okunduğunu görmek, veriyi bilgisayarda görselleştirmek ve kayıt/paketin sinyali temsil etmeye yeterli olup olmadığını anlamak.
- **Öncelik:** İlk adımda gerçek ham ADC örneklerini oku → yerel dosyaya kaydet → bilgisayarda grafiğe dök → kaydın neyi gösterdiğini ve sınırlamalarını açıkla.
- **Kapsam dışı:** PZEM karşılaştırması, akım formülü/kalibrasyon ve MCP3208 bu ilk ham gözlem adımına eklenmeyecek. Daha sonra ancak somut bir soru gerektirirse ele alınır.
- **Depo güncellemesi:** `EXPERIMENT_LEDGER.md`, `STATUS.md` ve `PROGRESS_TREE.md` bu önceliğe göre güncellendi.
- **Durum:** Yalnızca dokümantasyon güncellendi. Firmware oluşturulmadı, derlenmedi ve fiziksel ölçüm yapılmadı.
- **Sonraki adım:** E00A protokolünü bu hedefle uyumlu, tek bir basit kayıt/görselleştirme adımı olacak şekilde sadeleştirmek; ardından gerçek kart/pinout doğrulamasından sonra uygulamak.


## 2026-10-29 — Proje felsefesi: kişisel veri kümesi ve kabul edilebilir sınırlar

- **Neden:** Kullanıcı BERO'nun ticari/evrensel akım ölçer olmadığını; evdeki sınırlı aygıtlardan toplanan birleşik veri kümesinin zamanla büyümesini ve modelin bu veri kümesinde çok iyi öğrenmesinin sorun sayılmamasını açıkladı.
- **Karar:** Aşırı öğrenme bu proje için otomatik kusur veya başarısızlık ölçütü değildir. Amaç gözlenen ev içi aygıt ve yüklerde modele giderek daha iyi uyum kazandırmaktır. Eğitim kümesi, birleşik etiketli veri kümesi, varsa ayrılmış kayıt ve etiketsiz kayıt davranışı ayrı raporlanır; bu ayrım ticari genelleme iddiası için değil, gelişimi izlemek içindir.
- **Sınırlar:** Kaynak makinesi gibi görülmemiş veya yüksek akımlı bir yük ADC aralığını aşabilir ya da model tahmin üretemeyebilir. Bu kabul edilebilir; her yükü ölçmek zorunlu değildir. Doygunluk ve başarısızlık davranışı kaydedilebilir, ölçülmeyen akım için sayı uydurulmaz.
- **Depo değişiklikleri:** [Proje felsefesi](../docs/project-philosophy.md) oluşturuldu; README, STATUS, PROGRESS_TREE ve EXPERIMENT_LEDGER bağlantı/notları güncellendi.
- **Doğrulama:** Yeni belgeler yeniden okunarak kontrol edilecek. Bu çalışma yalnızca plan/felsefe dokümantasyonudur; Python/model kodu yazılmadı, firmware derlenmedi ve fiziksel ölçüm yapılmadı.
- **Sonraki adım:** E00A ilk ham ADC gözlemi olarak kalır. Gerçek veriler geldikçe Python görevleri, model eğitimi ve geçmiş sürümlerle karşılaştırma somut veri biçimlerine göre tasarlanır.


## 2026-10-29 — BERO uzun vadeli yönü genişletildi

Kullanıcı, BERO'nun tek bir akım ölçerle sınırlı olmadığını açıkladı. İleride eldeki MCP/Modbus modülleri ve olası ESP32-P4 dahil farklı ESP32 kartları görevlerine göre kullanılabilir. Akım verisini okuma/tahmin etme ve PZEM referansıyla etiketleme bir olası görev hattıdır. Başka örnek fikirler, çamaşır makinesi sesinden su alma olayını veya su akış sensöründen boşaltma olayını algılamaktır.

Bunlar uzun vadeli vizyon ve örnek fikirlerdir; uygulanmış mimari veya doğrulanmış özellik değildir. Ortak ilke, sensörleri ve donanımı göreve göre değişebilen, belirli işi kendi verisi ve başarı ölçütleriyle yapan özelleşmiş ESP tabanlı sistemlerdir.

**Aktif adım değişmedi:** E00A ile ESP32 dahili ADC ham örneklerini oku, kaydet ve bilgisayarda görselleştir. Bu adım MCP/Modbus/P4 entegrasyonu veya model geliştirmesiyle genişletilmeyecek.

Ayrıntı: [Proje felsefesi](../docs/project-philosophy.md). Dokümantasyon güncellendi; firmware, Python/model kodu veya fiziksel ölçüm yapılmadı.


## 2026-10-29 — Gün sonu kontrolü ve gelecekteki oturum için devir

- **Durum:** UYGULANDI — depo kayıtları çapraz kontrol edildi; E00A kapsam çelişkileri düzeltildi. Fiziksel deney yapılmadı.
- **HEDEF ve kabul ölçütü:** Günün kararlarını gelecekteki oturumun yeniden kurabileceği şekilde korumak; aktif ilk adımı, deney kapsamını ve görev sırasını birbiriyle tutarlı tutmak; uygulama yapılmadıysa bunu açıkça belirtmek.
- **Yapılan:** Güncel main commit'i kontrol edildi; `AGENTS.md`, `STATUS.md`, `ROADMAP.md`, `docs/open-questions.md`, E00A README/protocol/YAML, görev indeksi, proje README'si, ilerleme ağacı ve oturum günlüğü okundu. E00A belgelerindeki eski “istatistik ana çıktı, grafik yalnız tanı” ifadeleri, kullanıcının hedefiyle çeliştiği için düzeltildi: ham ADC kaydı ve bilgisayarda zaman grafiği temel çıktıdır; istatistikler yardımcıdır. T007 mimari görevi, gerçek edinim sonuçları ve aktarım gereksinimleri oluşana kadar BEKLEMEDE durumuna alındı. T007 taslağı silinmedi.
- **SONUÇ:** Aktif ilk adım E00A olarak kaldı. İlk adımda PZEM, akım formülü, MCP3208, model eğitimi veya çoklu ESP mimarisi eklenmeyecek. Uzun vadeli göreve özel ESP sistemleri vizyonu felsefe/STATUS/deney defteri/günlükte korunuyor; bu bir uygulama iddiası değildir.
- **Doğrulama:** Değiştirilen dosyalar GitHub'a yazıldıktan sonra yeniden okunarak içerik eşleşmesi kontrol edildi. Main dalının son commit'i ve dosya SHA'ları kontrol edildi. Bu oturumda firmware yazılmadı veya derlenmedi; YAML parser, JSON Schema validator, CI ve fiziksel test çalıştırılmadı. Donanım kartı/GPIO ve ADR-007'deki 10 µF fiziksel değişikliği hâlâ deney ön koşullarıdır.
- **Açık kalanlar:** E00A öncesinde gerçek geliştirme kartı/pinout doğrulanacak; 10 µF paralel kondansatör fiziksel olarak uygulanıp kaydedilecek; ardından yalnız E00A için firmware ve yerel CSV/grafik hazırlığı yapılacak.
- **Sonraki tek adım:** E00A başlamadan önce gerçek ESP32 kartını ve pinout üzerindeki ADC GPIO eşleşmesini doğrula. Donanım görülmeden GPIO34 kesinleşmiş sayılmayacak.
- **Kanıt:** [STATUS](../STATUS.md); [ROADMAP](../ROADMAP.md); [E00A açıklaması](../experiments/E00A-raw-waveform-observation/README.md); [E00A protokolü](../experiments/E00A-raw-waveform-observation/protocol.md); [E00A YAML](../experiments/E00A-raw-waveform-observation/experiment.yaml); [T007](../tasks/T007-python-architecture.md); [görev indeksi](../tasks/README.md).


## 2026-10-30 — Kararlı alan eğitimi ve ham aç-kapa gözlem modelinin netleştirilmesi

- **Durum:** UYGULANDI — mimari ve bağlı plan belgeleri güncellendi; uygulama/deney yapılmadı.
- **HEDEF ve kabul ölçütü:** Kullanıcının tarif ettiği aynı SSR aç-kapa deneyinden iki ayrı çıktı üreten yaklaşımı açıkça belgelemek: ortak kararlı alanlardan PZEM etiketli SCT modeli eğitmek ve aynı olayın geçişler dahil tam ham SCT akışında model tahmini ile PZEM akışını zaman ekseninde gözlemlemek. Eğitim verisi içi uyum ile dinamik davranış incelemesini karıştırmamak.
- **Yapılan:** [Eğitim ve ham akış gözlem mimarisi](../docs/architecture/training-and-dynamic-observation.md) oluşturuldu; Mermaid akış diyagramı ve yalnızca temsili zaman serisi grafiği eklendi. Mimari ana notu, kalibrasyon prosedürü, T006, analiz metrikleri, E02 protokolü, STATUS, ROADMAP ve PROGRESS_TREE yeni yaklaşımla ilişkilendirildi. T006 ve prosedürdeki ilk aşamada eğitim dışı kayıt zorunluluğu kaldırıldı; ilk raporun aynı etiketli eğitim verisindeki uyum olduğu ve bunun bağımsız genelleme kanıtı olmadığı açıklandı.
- **SONUÇ:** Kararlı alan eğitimi, aynı veride eğitim içi ±%4 uyum raporu ve tam ham aç-kapa akışında ayrı dinamik gözlem birbirinden ayrıldı. PZEM istek/yanıt süresinin cihazın iç ölçüm güncelleme gecikmesiyle aynı olmadığı kaydedildi. Aktif ilk teknik sıra E00A → E00/T005/E01 olarak değişmedi; E08 yalnız SCT karakterizasyonu olarak kaldı.
- **Doğrulama:** Yeni belge ve güncellenen dosyalar commit sonrasında yeniden okunacak. Bu oturumda firmware/Python kodu yazılmadı, derleme/CI çalıştırılmadı, fiziksel deney veya model eğitimi yapılmadı. Grafikteki değerler temsili olup ölçüm değildir.
- **Açık kalanlar:** Kararlılık ölçütleri, pencere/özellik seçimi, gerçek zaman kaynağı/alanları, PZEM güncelleme gecikmesi, model biçimi ve gerçek veri akışı uygulama aşamalarında belirlenecek.
- **Sonraki adım:** E00A ham ADC gözlemi için gerçek ESP32 kartı/GPIO ve fiziksel bağlantı hazırlığına mevcut sırayla devam et; bu uzun vadeli model mimarisini E00A'ya taşımaya çalışma.
- **Kanıt:** [Mimari diyagram ve zaman grafiği](../docs/architecture/training-and-dynamic-observation.md); [ana mimari notu](../docs/architecture/sct-pzem-labeling-and-calibration.md); [T006](../tasks/T006-calibration.md); [kalibrasyon prosedürü](../calibration/PROCEDURE.md); [STATUS](../STATUS.md); [ROADMAP](../ROADMAP.md).


## 2026-10-30 — E00A ESP32D2 firmware depoya kaydedildi

- **Durum:** UYGULANDI — firmware dosyası ve deney kayıtları main dalına işlendi. Derlenme/çalışma bilgisi kullanıcı raporudur; bağımsız log kontrolü henüz yapılmadı.
- **Hedef ve kabul ölçütü:** ESP32D2 / ESP-IDF üzerinde E00A ADC firmware'ini kod olarak saklamak; GPIO34 ham ADC ve GPIO35 voltaj çıktılarını ayrı kanallarda tanımlamak; kod/protokol/sonuç/durum kayıtlarını eşlemek.
- **Yapılan:** `experiments/E00A-raw-waveform-observation/firmware/esp32d2-e00a-adc.yaml` oluşturuldu. `experiment.yaml`, `README.md`, `protocol.md`, `results.md`, proje `STATUS.md`, `ROADMAP.md` ve `EXPERIMENT_LEDGER.md` güncellendi. Kullanıcı, ESPHome kodunun derlendiğini ve çalıştığını bildirdi.
- **Doğrulama:** GitHub yazma işlemleri başarılı döndü. Firmware derleme logu, cihaz logu, YAML bağımsız parser kontrolü, CI ve fiziksel ADC ölçüm sonuçları bu oturumda alınmadı. Kodun çalışma bilgisi KULLANICI RAPORU olarak etiketlendi.
- **Açık kalanlar:** GPIO34/GPIO35 fiziksel bağlantı ayrıntısı; sensörlerden gelen sayısal değerler; ESPHome/cihaz logu; 30 saniyelik ham kayıt ve zaman grafiği.
- **Sonraki adım:** Kullanıcının paylaşacağı logları incelemek, ham ADC/voltaj değerlerini yorumlamak ve sonucu E00A results.md dosyasına eklemek.
- **Kanıt:** [Firmware](../experiments/E00A-raw-waveform-observation/firmware/esp32d2-e00a-adc.yaml); [E00A sonuç kaydı](../experiments/E00A-raw-waveform-observation/results.md); [STATUS](../STATUS.md).


## 2026-10-30 — E00A-S01 GND referans testi ve floating giriş teşhisi

- **HEDEF:** SCT bağlı değilken ADC girişlerinin GND referansında kararlılığını sınamak; önceki açık giriş dalgalanmasının nedenini belirlemek.
- **LOG:** Kullanıcı GPIO34 ve GPIO35'i GND'ye çektiğini bildirdi. Paylaşılan ESPHome 2026.9.1 logunda GPIO34, 14:49:11–14:52:24 aralığında görünen örneklerde 0 count. GPIO35 başlangıçta 0.181–0.195 V, kısa süreli 2.405 V sıçrama ve düşüş sonrası yaklaşık 14:49:29–14:52:24 arasında 0.142 V sabit. Kararlı bölüm yaklaşık 175 saniye. ADC init/config/calibration OK. GPIO34 raw count ve GPIO35 kalibre voltaj iki ayrı kanaldır.
- **SONUÇ:** GND referansı girişleri kararlı hale getirdi; önceki geniş dalgalanma floating giriş davranışıyla uyumlu. ADC arızası kanıtı yok; tam ADC doğruluğu da kanıtlanmadı. GPIO35'in 0.142 V tabanı açık soru.
- **Elektriksel çözüm adayı:** SCT jack topolojisi doğrulandıktan sonra ADC düğümüne Vmid'e karşı yüksek değerli pasif bias direnci (ilk prototip değerlendirmesi 47–100 kΩ). Kesin değer/bağlantı onaylanmadı; GND pull-down BERO'nun 1.65 V merkezli sinyal yaklaşımı için çözüm değil.
- **Sonraki adım:** Bir ADC kanalında Vmid bias deneyi, multimetre kontrolü ve 60 saniye log; sonra SCT bağlantısı. E00A açık.
- **Kanıt:** [E00A-S01 raporu](../experiments/E00A-raw-waveform-observation/reports/E00A-S01-gnd-reference-stability.md); kaynak kullanıcı logu `Yapıştırılan metin(8).txt`.



## 2026-10-30 — E00A Adım 2: voltaj sıfır noktası düzeltmesi derlendi

- **HEDEF:** GPIO35 voltaj çıktısının GND referansında sıfır göstermesi.
- **LOG:** Önceki GND logunda kararlı görülen 0.142 V tabanını çıkarmak için GPIO35'e `max(0, x - 0.142)` filtresi eklendi; GPIO34 ham ADC kanalı korundu. Firmware [dosyası](../experiments/E00A-raw-waveform-observation/firmware/esp32d2-e00a-adc.yaml) commit `9eae26000a1dc460191bec68581cec0ac9ab9397`. Kullanıcı kodun derlendiğini bildirdi.
- **SONUÇ:** Derleme kullanıcı bildirimiyle başarılı. Yeni firmware ile GPIO35 GND ölçümünün 0.000 V'a indiği henüz logla doğrulanmadı. 0.142 V geçici ofsettir; genel ADC kalibrasyonu değildir.
- **Sonraki adım:** GND bağlantısında düzeltilmiş GPIO35 değerini logla doğrula; ardından Vmid ve multimetre karşılaştırması yap.



## 2026-10-30 — E00A Adım 2 sıfır çıktısı logu

- **HEDEF:** GPIO35 voltaj sensörünün GND koşulunda yazılım düzeltmesi sonrası 0.000 V göstermesini doğrulamak.
- **LOG:** Kullanıcının `Yapıştırılan metin(10).txt` kaynağındaki ESPHome 2026.9.1 logunda GPIO35, 15:13:08.379–15:13:56.381 arasında 49 kaydın tamamında 0.000 V yayınladı. ESP32 rev3.1; ADC init/config/calibration OK; güncelleme aralığı 1 s. GPIO34 48 kez 0 count gösterdi, ancak fiziksel bağlantısı olmadığı için yorum dışı bırakıldı.
- **SONUÇ:** Kullanıcı Adım 2 amacına ulaşıldığını bildirdi; log, GPIO35 düzeltilmiş çıktısının yaklaşık 48 saniye boyunca sıfır kaldığını destekliyor.
- **Sonraki adım:** Kullanıcı kodu değiştirmeden aynı log oturumunda bias trafosuna enerji verecek. Sonraki kayıtlar Vmid tepkisini gösterecek; henüz bias açık sonucu yok.


## 2026-10-30 — E00A Adım 2: sıfırlama filtresi kaldırıldı

- **HEDEF:** GND'de sıfır gösterme denemesinin Vmid gerçek DC okumasına etkisini değerlendirip doğru ölçüm yaklaşımını seçmek.
- **LOG:** Önceki ofsetli cihaz logunda GPIO35 GND koşulunda 49/49 örnekte 0.000 V gösterdi. Aynı oturumun bias açık bölümünde 85 kararlı örnek yaklaşık 1.525 V ortalama verdi. Kullanıcı multimetre Vmid değerini 1.654 V bildirdi. 0.142 V filtre ofseti geri eklendiğinde hesaplanan filtresiz tahmin yaklaşık 1.667 V; fark yaklaşık 13 mV. Bu 1.667 V doğrudan ham log ölçümü değil, filtreli çıktıdan türetilmiş hesaptır. GPIO34 bağlı olmadığından yorum dışı.
- **SONUÇ:** GND'de 0.000 V görüntüsü gerçek sıfır ölçümü değildi; filtre ADC voltajından sabit 0.142 V çıkarıyordu. Bu işlem Vmid'i de aynı miktarda düşürerek gerçek DC okumayı bozdu. Yazılımsal ofset kaldırıldı; GND'de görülen 0.142 V gözlemi korunacak.
- **UYGULAMA:** Firmware GPIO35 lambda filtresi ve “Corrected” sensör adı kaldırılarak revize edildi. Yeni revizyon henüz derlenmedi veya cihaza yüklenmedi.
- **SONRAKİ KARAR KAPISI:** Ofsetsiz firmware derlemesi ve aynı Vmid noktasında multimetreyle eşzamanlı cihaz logu.
- **KANIT:** [E00A sonuçları](experiments/E00A-raw-waveform-observation/results.md); kullanıcı logu `Yapıştırılan metin(20261030-121627).txt`.


## 2026-10-30 — E00A RAW voltaj tahmini ve ADC fark sensörü

- **HEDEF:** GPIO34 ham count değerini nominal voltaj tahminine çevirmek, GPIO35 ADC voltajıyla karşılaştırmak ve farkı loglamak.
- **LOG:** Firmware'e GPIO34 RAW count, RAW'dan voltaj tahmini, GPIO35 ofsetsiz ADC voltajı ve işaretli fark sensörü eklendi. Kullanıcı YAML'ın derlemeye alındığını bildirdi; derleme sonucu henüz paylaşılmadı.
- **SONUÇ:** Firmware dosyası GitHub'a kaydedildi ve yeniden okunarak doğrulandı. Derleme ve cihazda çalışma henüz doğrulanmış değil. RAW formülü nominal tahmin; ADC kalibrasyonu değildir.
- **AÇIK:** GPIO34'ün GPIO35 ile aynı 1.654 V noktasına bağlanması; derleme sonucu; cihaz logu; multimetre karşılaştırması.
- **Sonraki adım:** Derleme sonucunu ve ardından cihaz logunu kaydet.


## 2026-10-30 — E00A bias-only / SCT bağlı değil: RAW ve voltaj ilk karşılaştırma logu

### HEDEF
SCT bağlamadan bias Vmid noktasını ESP32D2'nin GPIO34 RAW ve GPIO35 ADC voltaj kanallarında gözlemek; multimetre bildirimi olan 1.654 V ile karşılaştırmak. Sonraki uzun logda RAW ve voltaj serilerinin korelasyonunu incelemek için başlangıç gözlemi oluşturmak.

### LOG
- Kaynak: Kullanıcının paylaştığı `Yapıştırılan metin(20261030-123911).txt`; ESPHome 2026.9.1; ESP32 rev3.1; cihaz `esp32d2`; log bağlantısı 192.168.0.66.
- ADC GPIO34 (ADC1_CH6) ve GPIO35 (ADC1_CH7) başlatma, konfigürasyon ve kalibrasyon durumları OK; iki sensörün güncelleme aralığı 1 s.
- Kullanıcının multimetre bildirimi: Vmid = **1.654 V**. Bu değer kullanıcı raporudur; bu logda multimetre ölçümünün zaman damgası yoktur.
- İlk bölümde GPIO34 RAW = 0 count ve GPIO35 = 0.142 V görülüyor. Ardından GPIO34 yaklaşık 1837–1871 count bölgesine geçiyor; GPIO35 de yaklaşık 1.65–1.68 V bandına oturuyor.
- Kararlı görünen bölümde (yaklaşık 15:37:46–15:39:03): GPIO34 RAW gözlemi yaklaşık 1829–1871 count; RAW nominal voltaj tahmini yaklaşık 1.385–1.416 V; GPIO35 ADC voltajı yaklaşık 1.650–1.679 V; fark sensörü yaklaşık +0.250…+0.294 V.
- RAW nominal tahmini firmware formülüdür: `count × 3.1 / 4095`; kalibre edilmiş voltaj değildir.
- Logda iki kanalın yayınları aynı saniyede ve aynı anda gerçekleşmiyor; GPIO34 ve GPIO35 ayrı ADC kanallarıdır. Bu nedenle bu kısa kayıt tek başına örnek-örnek korelasyon katsayısı veya tam eşzamanlılık kanıtı değildir.
- Logda trafo enerjilendirme anı ayrıca işaretlenmediğinden, ilk geçişi belirli bir trafo ON/OFF zamanına atamıyoruz. Kullanıcının gözlemi: kondansatörlerle birlikte değerler belirgin biçimde oturuyor.

### SONUÇ
- Bias-only gözleminde GPIO35 voltaj okuması kararlı bölümde kullanıcının bildirdiği 1.654 V multimetre değerine yakındır (yaklaşık 1.650–1.679 V).
- Aynı kararlı bölümde GPIO34 RAW'dan nominal hesaplanan voltaj yaklaşık 1.4 V'tur ve GPIO35'ten yaklaşık 0.27 V düşüktür. Bu fark henüz nedenlendirilmemiştir; RAW dönüşüm katsayısı nominaldir ve iki kanal ayrı ADC okumalarıdır.
- Bu test SCT davranışını, akım ölçümünü veya bias devresinin SCT yükü altındaki davranışını göstermez. Yalnızca SCT'siz bias/ADC zincirinin ilk karşılaştırmasıdır.
- Kullanıcının sonraki adımı: daha uzun RAW + voltaj logu paylaşmak. O kayıtta zaman serilerini eşleştirip korelasyon (Pearson ve/veya Spearman), eğim/kesişim, fark ve kararlı/geçiş bölümlerini inceleyeceğiz. Ham logdaki örnekleme zamanları korunmalı; farklı zaman damgaları körlemesine satır satır eşleştirilmeyecek.
- E00A tamamlanmadı; bu kayıt ön gözlemdir.


## 2026-10-30 — E00A SCT'siz bias-only log analizi ve alt adım kapanışı

- **HEDEF:** SCT bağlı değilken alınan son ESP32D2 logunu analiz edip taban dalgalanmasını tanımlamak; RAW sıfırlarını eşleştirmeme kuralını uygulamak ve yalnız bu deney koşulunu kapatmak.
- **LOG:** Kullanıcının `esp32d2-logs.txt` dosyası analiz edildi. 618'er kayıt bulunan dört sensör serisinde ilk 14 GPIO34 RAW=0 kaydı ve ilk geçişteki stale 0.000 V nominal tahmin eşleştirmeden çıkarıldı. Zaman damgasıyla 603 geçerli çift elde edildi. GPIO34 RAW: 1846.80±6.97 count; nominal RAW voltaj: 1.398007±0.005303 V; GPIO35: 1.665138±0.006474 V; ortalama fark: +0.267131 V. Pearson r=-0.0201, Spearman rho=-0.0200. Kullanıcının Vmid multimetre bildirimi 1.654 V olup logla eşzamanlı değildir.
- **SONUÇ:** SCT'siz ölçüm zincirinde GPIO35 için gözlenen dalgalanma yaklaşık 6.5 mV standart sapmadır; bunu ADC'nin tek başına taban gürültüsü olarak nitelemek mümkün değildir. RAW nominal voltaj formülü kalibre değildir ve iki ADC kanalı tam eşzamanlı değildir. Yazılım offseti/filtre eklenmeyecek. SCT bağlı olmayan bias-only alt adım KAPATILDI; E00A bütünü açık kaldı.
- **DOĞRULAMA:** Önceki sonuç kaydı ve durum belgeleri okundu. Bu oturumda fiziksel bağlantı, yeni firmware derlemesi, CSV ham örnek edinimi veya fiziksel test yapılmadı. Güncelleme yalnız paylaşılan logun analiz ve dokümantasyon kaydıdır.
- **SONRAKİ ADIM:** SCT bağlı fakat ölçülen hatta akım yok koşulunu ayrı kaydet; önceki SCT'siz taban ile karşılaştır. E00A'nın 3.3 V koşulu ve ham CSV/grafik gereksinimleri açık kalır.
- **KANIT:** [E00A sonuçları](../experiments/E00A-raw-waveform-observation/results.md); kullanıcı logu `esp32d2-logs.txt`.


## 2026-10-30 — E00B SCT bağlı/akımsız deneyinin açılması ve GPIO planı

- **HEDEF:** E00A'daki SCT'siz bias-only alt koşulundan sonra SCT bağlanmış fakat primer akımı sıfır olan koşulu ayrı deney olarak açmak; bias referans kanallarını koruyup SCT için iki yeni ADC1 GPIO belirlemek.
- **LOG:** E00B README, experiment.yaml ve results.md oluşturuldu. Bias GPIO34 RAW (ADC1_CH6) ve GPIO35 voltaj (ADC1_CH7) olarak korundu. SCT RAW için GPIO32 (ADC1_CH4), SCT voltaj için GPIO33 (ADC1_CH5) önerildi. ESP32-WROOM-32D aday kart; gerçek geliştirme kartı pinout'u fiziksel doğrulanmadı.
- **SONUÇ:** E00B PLANLANDI. Firmware, derleme, fiziksel bağlantı ve ölçüm yapılmadı. GPIO32/33 yalnız pinout doğrulaması sonrası bağlanacak.
- **SONRAKİ ADIM:** Gerçek WROOM-32D geliştirme kartındaki GPIO32/33 etiketlerini pinout ile doğrula; sonra açıklamalı tam ESPHome firmware'ini hazırla.
- **DOĞRULAMA:** Yeni E00B dosyaları oluşturuldu ve GitHub'dan yeniden okunarak doğrulandı. İndeks, STATUS, PROGRESS_TREE, ROADMAP ve ledger güncellendi; commit sonrası yeniden okunmaları bekleniyor.
- **KANIT:** [E00B README](../experiments/E00B-sct-connected-no-current/README.md); [E00B experiment.yaml](../experiments/E00B-sct-connected-no-current/experiment.yaml); [E00B results](../experiments/E00B-sct-connected-no-current/results.md).


## 2026-10-30 — E00B firmware eklendi ve derleme bildirimi kaydedildi
- **HEDEF:** E00B için açıklamalı dört kanallı ESPHome firmware'ini depoya koymak; deney planı, sonuç kaydı ve proje durumunu eşlemek.
- **LOG:** Başlangıçta AGENTS.md, STATUS.md, ROADMAP.md, docs/open-questions.md, E00B README/experiment.yaml/results.md, PROGRESS_TREE.md ve EXPERIMENT_LEDGER.md okundu. E00B firmware dosyası oluşturuldu: `experiments/E00B-sct-connected-no-current/firmware/esp32d2-e00b-sct-no-current.yaml`. Kullanıcı kodun derlendiğini bildirdi (KULLANICI RAPORU). experiment.yaml, README, results, STATUS, ROADMAP, PROGRESS_TREE, EXPERIMENT_LEDGER ve deney indeksi güncellendi.
- **SONUÇ:** Firmware depoya uygulandı; kullanıcı bildirimiyle derlendi. Bu, cihazda çalıştığı veya fiziksel deneyin yapıldığı anlamına gelmez. GPIO32/33 gerçek kart pinout doğrulaması bekliyor. 1 s sensor update aralığı yüksek hızlı ADC örnekleme değildir.
- **DOĞRULAMA:** Firmware ve deney belgeleri GitHub'a yazıldı. Bu kayıtta ESPHome derleme komutu yeniden çalıştırılmadı; kullanıcı derleme çıktısı paylaşmadı. Cihaza yükleme, pinout, fiziksel bağlantı ve ölçüm yapılmadı. Dosyalar bu oturumun son adımında yeniden okunarak doğrulanacak.
- **SONRAKİ ADIM:** Gerçek kart/pinout ve bağlantıyı doğrula; sonra firmware'i yükleyip SCT bağlı/primer akımsız logu al.


## 2026-10-30 — E00B ilk cihaz logunun analizi ve depoya kaydı
- **HEDEF:** Kullanıcının paylaştığı ESPHome logunu ham haliyle saklamak, açılış geçişini ayırmak, dört kanalın kararlı değerlerini özetlemek ve sonuçları deney kayıtlarına eklemek.
- **LOG:** Ham log dosyası `experiments/E00B-sct-connected-no-current/logs/2026-10-30-e00b-esp32d2-startup-and-observation.log` olarak eklendi. ESPHome 2026.9.1 / ESP32 rev3.1. GPIO34/35/32/33 ADC1 başlatma ve kalibrasyon OK. Kararlı pencerede 110 örnek/kanal: Bias RAW 1854.14 count (SD 9.64); SCT RAW 1853.45 count (SD 8.22); Bias voltaj 1.6651 V (SD 0.0079); SCT voltaj 1.6639 V (SD 0.0063). İlk yaklaşık 9 saniyedeki RAW=0 ve 0.142 V başlangıç değerleri hariç tutuldu.
- **YORUM:** Dört kanal çalışıyor. Kararlı kesitte Bias ve SCT değerleri yakın. Nominal RAW dönüşümü ile kalibre ADC voltajı arasındaki fark ölçekleme farkıdır; devredeki fiziksel gerilim farkı değildir.
- **SONUÇ:** Ham log, analiz ve metadata depoya kaydedildi. Cihazın API üzerinden çalışması doğrulandı. Primer akımın sıfır olması ve fiziksel SCT montajı logla tek başına doğrulanamıyor; deneyin fiziksel koşulları tam doğrulanmış sayılmıyor.
- **DOĞRULAMA:** Ham log GitHub'a yazıldı; results.md, experiment.yaml ve README güncellendi. STATUS/ledger/session log güncellemesi bu kayıtla yapılıyor.
- **SONRAKİ ADIM:** Fiziksel SCT montajı ve primer akım=0 koşulunu kullanıcı kaydıyla teyit et; daha uzun kararlı pencere al.


## 2026-10-30 — E00B uzun logu kaydedildi ve olumlu sonuç raporlandı

- **Durum:** Ham log ve analiz GitHub main dalına yazıldı; dosyalar commit sonrası yeniden okunarak doğrulandı.
- **HEDEF:** SCT bağlı yüksüz hat ile bias referansının daha uzun kayıt üzerinden yakınlığını değerlendirmek.
- **LOG:** Kullanıcının sağladığı 222,578 baytlık uzun ESPHome logu `experiments/E00B-sct-connected-no-current/logs/2026-10-30-e00b-esp32d2-long-observation.log` yoluna eklendi. Açılış geçişi çıkarıldıktan sonra dört kanalın her birinde 351 geçerli yayın değeri analiz edildi. RAW ortalamaları bias 1852.56, SCT 1853.37 count; fark +0.82 count. ADC voltaj ortalamaları bias 1.6646 V, SCT 1.6632 V; fark −1.4 mV.
- **SONUÇ:** E00B yüksüz karşılaştırması olumlu; bu log penceresinde anlamlı bias kayması görülmedi. GPIO kanalları eşzamanlı örnek değildir; 1 saniyelik ESPHome yayınları yüksek hızlı örnekleme değildir. Fiziksel primer akım/CT montajı logdan bağımsız kanıtlanmış değildir. SCT RAW maksimum 1941 count sonraki yük kayıtlarında izlenecek.
- **Sonraki adım:** Dört kanallı E00B firmware'ini değiştirmeden tut; sonraki yük koşulunu ayrı deney/log olarak tanımla. E00A'nın açık işleri ayrıca korunur.


## 2026-10-30 — E08 Aşama 2 / 100 W akkor testi açıldı

- **Durum:** HAZIRLIK; test kaydı açıldı, fiziksel test başlamadı.
- **HEDEF:** 100 W akkor yük altında SCT013-030 sinyalini 1/2/4 iletken turu ve 1/2/2,5 kS/s hedefleriyle karakterize etmek.
- **LOG:** İlk koşul 1 tur × 1.000 örnek/s olarak tanımlandı. E08 aşama dosyası, E08 sonuç kaydı, metadata, STATUS, ROADMAP, PROGRESS_TREE ve deney defteri güncellendi. Mevcut E00B YAML'ın 1 saniyelik yayın yaptığı ve yüksek hızlı örnekleme sağlamadığı tespit edildi.
- **SONUÇ:** Henüz ölçüm yok. E08 için ayrı yüksek hızlı ADC firmware'i hazırlanmalı; gerçek örnekleme hızı ayrıca doğrulanmalı. Mevcut E00B firmware'i E08 testi için kullanılamaz.
- **Sonraki adım:** E08 koşullarına uygun, açıklamalı yüksek hızlı ADC firmware'i hazırlamak; derleme ve gerçek kart/pinout doğrulamasından sonra ilk 1 tur × 1 kS/s koşulunu uygulamak.


## 2026-10-30 — E08 100 W gözleminde firmware kararı düzeltildi

- **Kullanıcı kararı:** Yeni koda geçilmeyecek. Mevcut E00B kodu korunacak.
- **HEDEF:** 100 W akkor yük altında mevcut 1 saniyelik sensör yayınlarıyla SCT/bias ölçüm alanlarının yük davranışını gözlemek.
- **LOG:** Önceki oturumda yüksek hızlı firmware'e geçiş önerilmişti; kullanıcı bunun şu an gerekli olmadığını belirtti. Deney protokolü bu karara göre düzeltildi.
- **SONUÇ:** Bu kayıt düşük hızlı gözlem niteliğindedir; yüksek hızlı örnekleme testi değildir. Hızlandırma denemeleri sonraki aşamada yapılacaktır. Fiziksel ampul testi ve log henüz alınmadı.


## 2026-10-30 — ESP32D2 cihaz kimliği değişmez kuralı eklendi

- **HEDEF:** ESP32D2 cihaz kimliğinin firmware/YAML düzenlemelerinde yanlışlıkla değiştirilmesini engellemek.
- **LOG:** Kullanıcının açık talebiyle proje `AGENTS.md` dosyasına kesin ve öncelikli kural eklendi: ESP32D2 kimliği değiştirilemez; ESPHome `esphome.name` alanı mevcut kimlikle aynen korunur; her YAML değişikliğinde önce/sonra kontrolü zorunludur; farklılık varsa değişiklik geri alınır.
- **SONUÇ:** Kural dokümantasyona işlendi. Firmware dosyası bu işlem kapsamında değiştirilmedi. Kuralın sonraki tüm ESPHome/YAML çalışmalarında uygulanması zorunludur.
