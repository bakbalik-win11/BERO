# T007 — Home Assistant verisini PC'ye aktarma ve Python başlangıcı

- **Durum:** DEVAM EDİYOR — manuel HA History CSV dışa aktarımı gösterildi; iki programlı gelen-kutu/arşiv mimarisi kararlaştırıldı; klasörlerin fiziksel konumu ve Python uygulaması henüz oluşturulmadı
- **Faz:** Faz 2 — Pratik yeniden kurulum ve sistem geliştirme (veri aktarımı alt aşaması)
- **Bağımlılık:** T009 kapsamında PZEM ve SCT düğümlerinin temel işlevlerinin gerçek donanımda çalışması ve Home Assistant'ta gerçek entity üretmesi.
- **Hedef:** Kullanıcının manuel olarak bıraktığı HA dışa aktarım dosyalarını PC'deki gelen kutusundan doğrulanmış yerel arşive taşıyan ilk Python programını kurmak. Ayrı ikinci Python programı yalnızca bu arşivi okuyarak inceleme/analiz yapacaktır.

## Mevcut ilerleme — 2026-11-05

Kullanıcı, Home Assistant History arayüzünden Modül 2 SCT ve Modül 3 PZEM/SSR/olay geçmişini aynı CSV dosyasına herhangi bir HA otomasyonu veya özel kod yazmadan dışa aktarabildi. `history (32).csv` ilk gerçek örnektir. Böylece veriye manuel erişim yolu gösterilmiştir. Bu, T007'nin tamamlandığı anlamına gelmez: dosyayı kaynak olarak koruyan, tekrar çalıştırılabilir Python okuma/inceleme hattı henüz oluşturulmamıştır.

## Kabul edilen çalışma modeli — iki bağımsız Python programı (2026-11-06)

Kullanıcı HA dışa aktarım dosyasını kendisi belirlenen gelen-kutu klasörüne bırakacaktır. İlk Python programı bu klasördeki dosyaları okuyup doğrular; başarılı dosyayı içeriğini değiştirmeden yerel arşivin uygun bir alt klasörüne taşır. Böylece gelen-kutu alanı sonraki dosyalar için boşalır. Kullanıcının dosyayı bırakması dışında HA tarafında otomatik aktarım veya Recorder veritabanına müdahale yapılmaz.

- **Python-1 — dosya alım/arşivleme:** Gelen kutusundaki dosyayı bulur, biçimini ve kayıt yapısını inceler, kaynak dosyanın hash'ini ve aktarım sonucunu kaydeder. Başarılı dosyayı arşive taşır. Okunamayan veya doğrulamadan geçemeyen dosyayı silmez; ayrı hata/karantina alanına alır veya güvenli biçimde yerinde bırakır. Aynı içeriğin ikinci kez arşivlenmesini hash kontrolüyle önler.
- **Python-2 — analiz:** Yalnızca Python-1 tarafından arşivlenmiş dosyaları girdi kabul eder. HA'ya bağlanmaz, gelen kutusunu yönetmez ve arşivdeki kaynak dosyaları değiştirmez.
- Gelen kutusu, arşiv, hata/karantina ve log alanları mantıksal rollerdir. Gerçek klasör yolları, alt klasörleme kuralı, dosya türü ve programın çalışma/izleme biçimi terminalde klasör yapısı görüşülürken belirlenecektir; bu ADR/T007 kararı fiziksel yol varsaymaz.
- Arşivleme öncesinde dosya bütünlüğü doğrulanmadan kaynak dosya taşınmaz veya silinmez. Başarılı işlemde kaynak dosyanın kendisi arşivde korunur; içerik yeniden yazılmaz.
- Home Assistant Recorder veritabanı bu iş akışında doğrudan okunmaz, değiştirilmez veya temizlenmez. HA History'den dışa aktarılan dosya kullanıcı tarafından gelen kutusuna bırakılır.

## Neden T009 sonrasında?

Veri aktarımı için önce PZEM ve SCT düğümlerinin gerçek veriyi Home Assistant'a yayınlıyor olması gerekir. Faz 2'nin ilk hedefi veri analizi değil, modülleri pratik olarak yeniden devreye alıp temel işlevlerini doğrulamaktır. T009 kabul koşulları karşılandıktan ve gerçek entity listesi görüldükten sonra T007 başlatılır.

## Bilinen hedef

- Home Assistant geçmişinden PZEM ve mevcut SCT entity kayıtları alınacak.
- Veriler PC'de Python ile işlenecek.
- Kaynak entity_id, state/value, unit, timestamp ve mevcutsa attributes korunacak.
- PZEM ve SCT farklı güncelleme hızlarında olabilir; aktarım bunları yapay olarak eşitlemeyecek.
- Aynı dışa aktarılan dosya tekrar analiz edilebilir olmalı.

## Bu görevde yapılacaklar

1. Home Assistant'ta gerçek PZEM ve SCT entity_id listesini belirle; tahmin etme.
2. Kullanıcının HA History'den aldığı gerçek dışa aktarım dosyasının biçimini/alanlarını incele.
3. Python-1 için gelen-kutu → doğrulama → arşivleme akışını geliştir; fiziksel klasör yapısını terminalde kararlaştır.
4. Kaynak dosya adı, hash'i, aktarım zamanı, dosya/kayıt sayıları ve kullanılan kod sürümünü işlem kaydına ekle.
5. Hatalı/tekrarlı dosya davranışını test et; doğrulanmamış dosyanın kaybolmadığını kanıtla.
6. Python-2'nin yalnız arşivden okuma sınırını ve giriş sözleşmesini tanımla.
7. Başarılı kod, örnek log/çıktı ve yorumunu depoda sakla.

## Bu görevde yapılmayacaklar

- Faz 1 deneylerini yeniden açmak.
- Sürekli ham ADC veya 50 Hz dalga kaydı geliştirmek.
- Şimdiden sabit örnekleme/polling aralığı veya kararlılık eşiği belirlemek.
- PZEM ve SCT timestamp'lerini aynı zamana yuvarlamak veya yapay senkronize etmek.
- K=24.22 katsayısını değiştirmek.
- \`ct_clamp\` kaynak kodunu değiştirmek.
- Henüz veri görmeden yeni deney serisi tasarlamak.

## Kabul ölçütü

- Kullanıcının gelen kutusuna bıraktığı gerçek HA dışa aktarım dosyası Python-1 tarafından okunabilmeli.
- Dosya doğrulandıktan sonra kaynak içeriği değiştirilmeden arşive taşınmalı; gelen kutusu işlenmiş dosya bakımından boşalmalı.
- Okuma/doğrulama başarısızsa dosya kaybolmamalı ve hata nedeni loglanmalı.
- Aynı dosyanın hash ile yinelenmesi önlenmeli.
- PZEM ve SCT kayıtları entity_id bazında ayrıştırılabilmeli; timestamp, birim ve kaynak değerleri korunmalı.
- Python-2 yalnız arşivden veri okuyacak şekilde ayrılmalı.
- Kod, gerçek örnek çıktı/log ve yorumu depoya eklenmeli.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Faz 2'nin ilk veri yolunu kurmak.
- **LOG:** Kullanıcının manuel HA History CSV dışa aktarımı daha önce gösterildi. 2026-11-06 tarihinde iki bağımsız Python programı ve gelen-kutu/arşiv iş akışı kararlaştırıldı. Fiziksel klasör yapısı ve Python kodu henüz oluşturulmadı.
- **SONUÇ:** T007 DEVAM EDİYOR. Mimari kararı kaydedildi; uygulama ve gerçek dosya testi tamamlanmadı.


## Tek kanallı eğitim veri seti kararı — ADR-027 (2026-11-06)

- Üç SCT kanalını birlikte okuyan test/veri toplama kodu korunabilir; bu kodun üç kanallı olması eğitim verisinin de üç kanallı olacağı anlamına gelmez.
- Kaynak HA CSV'si ve arşiv, içerdiği tüm SCT kanallarını ham haliyle koruyabilir.
- Python-2'nin eğitim veri seti üretiminde kanal seçimi açık olmalıdır. Her eğitim seti yalnızca bir SCT kanalından oluşur; CH1, CH2 ve CH3 için ayrı setler ve ayrı model değerlendirmeleri hazırlanır.
- Seçilen kanalın SCT kararlı alanları, PZEM referans akışının geçerli kararlı alanlarıyla ADR-022/023/024/025 paket ve pencere kuralları içinde değerlendirilir.
- Kanal kimliği, fiziksel geçiş/sarım bilgisi, kaynak CSV/hash, firmware/kod sürümü ve calibration_id izlenebilir metadata olmalıdır.
- Önerilen adlandırma: `CH1-1T`, `CH2-4T`, `CH3-3T`. Mevcut fiziksel bağlantı/sarım eşlemesi kod ve entity adlarına uygulanmadan önce doğrulanacaktır. Bu aşamada firmware/entity isimleri değiştirilmemiştir.

Ayrıntı: [ADR-027](../docs/decisions/ADR-027-single-channel-training-datasets.md).
