# Oturum günlüğü

Bu günlük proje durumunun kronolojisidir. Her anlamlı depo çalışması sonunda yeni kayıt eklenir; eski kayıtlar korunur.

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
- **Açık kalanlar:** Gerçek parçanın kalıcı fotoğraf kanıtı; PZEM'in gerçek varyantı/CT'si; MCU/ADC ve analog ön uç; True-RMS referans cihazı ve yük senaryoları.
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
