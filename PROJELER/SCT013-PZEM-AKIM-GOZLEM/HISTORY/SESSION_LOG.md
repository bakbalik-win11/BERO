# Oturum günlüğü

Bu günlük proje durumunun kronolojisidir. Her anlamlı depo çalışması sonunda yeni kayıt eklenir; eski kayıtlar korunur.

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
