# T008 — PZEM/SCT kararlı alan eşleştirme ve etiketleme

- **Durum:** BEKLEMEDE
- **Faz:** Faz 2 — Bulunan kodu PZEM ile eğitmek
- **Bağımlılık:** T007'nin gerçek Home Assistant dışa aktarımını PC'ye taşıması ve veri alanlarını koruduğunu doğrulaması.
- **Hedef:** Modül 2 SCT ve Modül 3 PZEM akışlarını olay işaretleriyle paket aralıklarına ayırmak; aynı BOOT_ID/EVENT_ID aralığındaki bağımsız kararlı ölçüm bölgelerinden eğitim verisi oluşturmak.

## Veri akışı ve paketleme

1. Modül 3 PZEM ölçümlerini normal şekilde yayınlar. SSR ON/OFF değiştiğinde bir kez olay mesajı üretir.
2. Modül 3 aynı `BERO_EVT` mesajını hem UDP 4210 ile Modül 2'ye gönderir hem de kendi PZEM kayıt akışına ayrı bir olay kaydı olarak ekler.
3. Modül 2 SCT ölçümlerini normal şekilde yayınlar. Aldığı aynı UDP olay mesajını SCT kayıt akışına ayrı olay kaydı olarak ekler.
4. Ölçüm örneklerinin içine sürekli BOOT_ID/EVENT_ID/zaman alanı yazılmaz. ESP'ler kararlılık analizi, kırpma, eşleştirme veya katsayı hesabı yapmaz.
5. Python, her modülün kendi akışında olay işaretlerinin arasındaki ölçümleri paket aralıklarına ayırır. Paket anahtarı `BOOT_ID + ON_EVENT_ID`'dir; iki modüldeki ON başlangıçları aynı anahtarla eşleşmelidir. Her akışta ON'dan sonraki ilk durum olayı OFF olmalı; iki akıştaki OFF kapanışları da aynı `BOOT_ID + OFF_EVENT_ID` anahtarını taşımalıdır. Normal ON→OFF çevriminde `OFF_EVENT_ID = ON_EVENT_ID + 1` beklenir. ON ile OFF arasında EVENT_ID boşluğu veya beklenmeyen ara olay varsa paket reddedilir.
6. HA geçmişinde olay işareti ile ölçüm entity'leri ayrıysa timestamp önce her modülün kendi kayıtlarını olay işaretleri çevresinde sıralamak için kullanılır. Paket bütünlüğü ve ortak ON paket kimliği doğrulandıktan sonra timestamp, SCT ve PZEM'in bağımsız kararlı aralıkları arasında zaman kesişimi bulunup bulunmadığını değerlendirmek için kullanılır. Timestamp paket eşleştirme anahtarı değildir; tekil ölçümler timestamp ile birebir eşleştirilmez veya interpolasyonla eşleştirilmez.

## Kullanıcı tarafından netleştirilen eğitim penceresi sınırı — 2026-11-06

Bu kural, önceki simetrik SCT/PZEM kararlı-aralık kesişimi tarifini **eğitim penceresinin sınırlandırılması bakımından** ayrıntılandırır:

- Açılışta SCT ve PZEM kendi akışlarında bağımsız değerlendirilir.
- SCT kararlı duruma ulaşmış olsa bile PZEM henüz kararlı değilse eğitim başlamaz; PZEM'in kararlı olması beklenir.
- **Eğitim başlangıcı:** SCT kararlı VE PZEM kararlı koşullarının ikisi de ilk kez sağlandığında, yani iki kararlılık başlangıcının daha geç olanı.
- **Eğitim bitişi:** SCT akımın kesildiğini algıladığı anda. PZEM'in kapanış gecikmesi veya mavi serinin daha sonra düşmesi beklenmez.
- Eğitim çıktısına yalnızca bu başlangıç ve bitiş arasında kalan K=24.22 katsayısı uygulanmış SCT tekil ölçümleri alınır. PZEM ölçümleri kararlılık/etiket referansı olarak kullanılır; SCT tekil değerleri PZEM'e eşitlenmez, timestamp üzerinden birebir eşleştirilmez ve interpolasyon yapılmaz.
- Sabit bir süre, önceden seçilmiş zaman dilimi veya PZEM'in gecikmeli kapanış zamanı pencere sınırı değildir. Süre, verideki koşulların gerçekleşmesinin sonucudur.
- SCT kararlılık tespitinde tekil sıçramaların nasıl tolere edileceği henüz belirlenmemiştir. Bu istisna/kararlılık algoritması ayrı bir tasarım kararıdır; eşik veya pencere parametresi uydurulmayacaktır.
- Ham CSV ve tüm özgün ölçümler korunur; yalnızca seçilen SCT eğitim alt kümesi ayrı türetilmiş çıktı olarak üretilir.

Mantıksal ifade:

`start = max(SCT_STABLE_START, PZEM_STABLE_START)`

`end = SCT_CURRENT_CUTOFF`

Seçim aralığı `[start, end)` biçimindedir. `start >= end` ise eğitim örneği üretilmez ve açık dışlama nedeni raporlanır.

**Görsel yorum:** Kırmızı seri SCT, mavi seri PZEM'dir. Açılışta kırmızı önce yükselip kararlı olabilir; mavi daha sonra kararlı yatay seviyeye gelir. Eğitim ancak ikisi de kararlı olduğunda başlar. Kapanışta kırmızı SCT daha erken düşer; pencere orada biter, mavi PZEM'in gecikmeli düşüşü eğitim aralığını uzatmaz.

**Uygulama durumu:** Bu kayıt kullanıcı tarafından onaylanan pencere mantığıdır. SCT tekil sıçramalarına tolerans gösterecek kararlılık tespit algoritması ve parametreleri henüz belirlenmemiştir; otomatik uçtan uca Python uygulaması tamamlanmış sayılmaz.

## Python analiz adımları

1. T007 örnek dosyasındaki gerçek entity_id ve birimleri kullan; bilinmeyen entity adları uydurma.
2. Her modülün olay işareti dizisini kontrol et; ON başlangıç anahtarlarının ve OFF kapanış anahtarlarının iki akışta da aynı olduğunu doğrula. OFF, aynı akışta ON'u izleyen ilk durum olayı olmalı ve normal çevrimde EVENT_ID bir artmalıdır. Eksik, yinelenen, sıra dışı veya eşleşmeyen işaretleri raporla; ON–OFF arasındaki EVENT_ID boşluğunda paketi reddet. Eksik aralığı tahminle doldurma.
3. Geçersiz PZEM değerlerini (-1.0, NaN, timeout, parse/alan hatası) etiketlemeden çıkar; kayıtları silme, dışlama nedenini say.
4. PZEM kararlılığını kendi paket aralığındaki PZEM değerlerinden; SCT kararlılığını kendi paket aralığındaki SCT değerlerinden bağımsız değerlendir. Eşik, tolerans ve minimum süre gerçek veriden sonra belirlenir.
5. PZEM'in yükseliş/düşüş ve yerleşme geçişlerini; SCT'nin kendi geçiş/yerleşme bölümlerini kararlı eğitim bölgesinden çıkar.
6. Her iki akışta bağımsız kararlı aralıkları yalnız kendi ON paketinin ölçümlerinden tespit et; geçiş/yerleşme alanlarını kararlı eğitim aralığına katma.
7. Aynı ON paketindeki SCT ve PZEM kararlı aralıklarının zaman kesişimini hesapla. Yalnız kesişen aralık eğitim etiketi adayıdır. Kesişim yoksa etiket üretme; ham kayıtları koru ve `NO_STABLE_OVERLAP` gibi açık dışlama nedeni raporla. Zaman kesişimi paket eşleştirme anahtarı değildir, eğitim etiketi uygunluğu koşuludur.
8. Tekil SCT/PZEM örneklerini timestamp üzerinden birebir eşleştirme veya interpolasyon yapma. Sabit gecikme varsayma. HA timestamp'lerinin iki akış arasında karşılaştırılabilirliğini, olay sırasını ve kararlı aralık sınırlarını gerçek dışa aktarım üzerinde doğrula; doğrulanmamış zaman hassasiyeti iddiasında bulunma.
9. PZEM akımını referans etiket olarak ekle; PZEM mutlak ground truth değildir.
10. Eğitim çıktısına ON başlangıç işaretinin paket kimliği olan `BOOT_ID` ve `EVENT_ID` alanlarını Python ekler. Ham ESP ölçüm kayıtları değiştirilmez.
11. Kaynak dosya/hash, analiz kodu sürümü, kayıt özeti, örnek eşleşme ve yorumunu depoda sakla.

## Kabul ölçütü

- En az bir gerçek yük olayında iki modülün aynı ON başlangıç işaretini `BOOT_ID + EVENT_ID` ile eşleştirdiği ve her iki akışta karşılık gelen OFF kapanışını doğru sırada doğruladığı gösterilmiş.
- Her iki akışta kararlı bölge tespiti bağımsız yapılmış ve geçiş bölgeleri dışlanmış.
- En az bir tam ON paketinde SCT ve PZEM kararlı aralıklarının ortak zaman kesişimi bulunmuş; yalnız bu kesişimden eğitim etiketi üretilmiş.
- Kararlı aralıklar örtüşmüyorsa etiket üretilmediği ve `NO_STABLE_OVERLAP` gibi dışlama nedeninin raporlandığı gösterilmiş.
- Paket kimliği `BOOT_ID + ON_EVENT_ID` ile kurulmuş; timestamp yalnız aynı ON paketindeki kararlı aralıkların zaman örtüşmesini değerlendirmek için kullanılmış. Tekil örnekler birebir eşleştirilmemiş veya interpolasyonla eşleştirilmemiş.
- Eksik/yinelenen/geçersiz olay ve ölçüm kayıtları raporlanmış; ON–OFF EVENT_ID boşluğu ve iki akışta OFF kimliği uyuşmazlığı paket reddine yol açmış; ham kayıtlar korunmuş.
- HA timestamp sırası ve iki akış arasında karşılaştırılabilirlik gerçek dışa aktarım üzerinde kontrol edilmiş.
- Veri kökeni, kod sürümü, örnek çıktı ve yorum depoda kayıtlı.

## Dışlama durumları

Paket bütünlüğü kodları: `MISSING_ON`, `MISSING_OFF`, `EVENT_ID_GAP`, `OFF_EVENT_MISMATCH`, `DUPLICATE_EVENT`, `STATE_ORDER_ERROR`, `BOOT_CHANGED_WITH_OPEN_PACKET`, `INCOMPLETE_EVENT`.

Paket bütünlüğü doğrulandıktan sonraki etiket uygunluğu kodları: `NO_STABLE_SCT`, `NO_STABLE_PZEM`, `NO_STABLE_OVERLAP`. Bu iki grup ayrı raporlanır; ham kayıtlar hiçbir durumda silinmez.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Paket işaretli bağımsız akışlardan PZEM referanslı kararlı alan eğitim verisi üretmek.
- **LOG:** T007 veri aktarımı henüz tamamlanmadı; bu kart kapsamında eşleştirme yapılmadı.
- **SONUÇ:** T008 BEKLEMEDE; T007 kabul ölçütleri sağlanınca açılacak. Mimari karar ADR-022'de kayıtlıdır.


## 2026-11-06 — Katsayı terminolojisi düzeltmesi

Önceki kayıtlarda geçen **“katsayısız”** ifadesi yanlıştı ve düzeltildi. E15/T008 kapsamında değerlendirilen SCT akım çıktısı, firmware'de `ct_clamp` filtresindeki `multiply: 24.22` ile katsayı uygulanmış değerdir. Amaç katsayıyı yok saymak değil; PZEM referanslı kararlı alanlardan mevcut K=24.22 katsayısını değerlendirmek ve gerekirse iyileştirmektir. Ham ADC/ct_clamp öncesi değer ile katsayı uygulanmış akım çıktısı birbirine karıştırılmayacaktır. Bu düzeltme ölçüm akışının ne olduğuna ilişkindir; yeni katsayı henüz hesaplanmış veya kabul edilmiş değildir.
