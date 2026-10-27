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

- **Durum:** UYGULANDI; [PR #8](https://github.com/bakbalik-win11/BERO/pull/8) açık, otomatik kontrol sonucu bekleniyor.
- **Hedef ve kabul ölçütü:** Önceki BERO donanım çalışmalarındaki SCT013-100A-1V, SCT013-30A-1V ve PZEM-004T V3.0 Markdown kayıtlarını yeni projede tekrar araştırma/yazma gerektirmeden kullanmak; kaynakları korumak ve proje-özel eksikleri ayrı göstermek.
- **Yapılan:** Üç donanım README'si `hardware/references/` altına kaynak yolu ve kopya tarihi belirtilerek aktarıldı. Referans dizin indeksi ve proje README bağlantıları eklendi. `hardware/inventory.md`, T001, `STATUS.md` ve `docs/open-questions.md` genel donanım bilgisini yeniden toplamak yerine mevcut referansları kullanacak ve yalnızca bu projeye özgü seçim/eksikleri kaydedecek şekilde güncellendi.
- **Doğrulama:** Kopyalar, `DONANIM/` altındaki kaynak Markdown içeriklerinden oluşturuldu. Önceki test notları geçmiş kayıt olarak işaretlendi; yeni deney veya kalibrasyon sonucu üretilmedi. PR kapanış kontrolü [PR #8 Checks](https://github.com/bakbalik-win11/BERO/pull/8/checks) üzerinden doğrulanacak.
- **Açık kalanlar:** Bu projede kullanılacak SCT varyantı; PZEM'in 10 A/100 A seçeneği ve CT modeli; gerçek MCU/ADC, VREF/bias/analog ön uç; referans cihazı ve yük senaryoları.
- **Sonraki adım:** PR kontrolünü doğrula ve değişikliği `main` dalına al. Ardından T001'i sadece proje-özel eksikleri kapatmak için sürdür.
- **Kanıt:** [Proje referans indeksi](../hardware/references/README.md); [güncel envanter](../hardware/inventory.md); [T001](../tasks/T001-hardware-inventory.md); [çalışma dalı](https://github.com/bakbalik-win11/BERO/tree/docs/import-hardware-reference-md).
