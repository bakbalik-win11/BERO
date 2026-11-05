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
5. Python, her modülün kendi akışında olay işaretlerinin arasındaki ölçümleri paket aralıklarına ayırır. `EVENT_ID` her SSR durum değişiminde arttığı için ON başlangıç işaretinin `BOOT_ID + EVENT_ID` birleşimi paket kimliğidir; onu izleyen OFF kapanış işaretinin EVENT_ID değeri farklıdır. İki modüldeki ON başlangıçları aynı paket kimliğiyle eşleşmeli; karşılık gelen OFF kapanışları da her iki akışta sıra ve kimlik bakımından ayrıca doğrulanmalıdır.
6. HA geçmişinde olay işareti ile ölçüm entity'leri ayrıysa timestamp önce her modülün kendi kayıtlarını olay işaretleri çevresinde sıralamak için kullanılır. Paket bütünlüğü ve ortak ON paket kimliği doğrulandıktan sonra timestamp, SCT ve PZEM'in bağımsız kararlı aralıkları arasında zaman kesişimi bulunup bulunmadığını değerlendirmek için kullanılır. Timestamp paket eşleştirme anahtarı değildir; tekil ölçümler timestamp ile birebir eşleştirilmez veya interpolasyonla eşleştirilmez.

## Python analiz adımları

1. T007 örnek dosyasındaki gerçek entity_id ve birimleri kullan; bilinmeyen entity adları uydurma.
2. Her modülün olay işareti dizisini kontrol et; eksik, yinelenen veya eşleşmeyen BOOT_ID/EVENT_ID aralıklarını raporla. Eksik aralığı tahminle doldurma.
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
- Eksik/yinelenen/geçersiz olay ve ölçüm kayıtları raporlanmış; ham kayıtlar korunmuş.
- HA timestamp sırası ve iki akış arasında karşılaştırılabilirlik gerçek dışa aktarım üzerinde kontrol edilmiş.
- Veri kökeni, kod sürümü, örnek çıktı ve yorum depoda kayıtlı.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Paket işaretli bağımsız akışlardan PZEM referanslı kararlı alan eğitim verisi üretmek.
- **LOG:** T007 veri aktarımı henüz tamamlanmadı; bu kart kapsamında eşleştirme yapılmadı.
- **SONUÇ:** T008 BEKLEMEDE; T007 kabul ölçütleri sağlanınca açılacak. Mimari karar ADR-022'de kayıtlıdır.
