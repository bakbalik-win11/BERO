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
5. Python, her modülün kendi akışında olay işaretlerinin arasındaki ölçümleri paket aralıklarına ayırır. PZEM ve SCT paket aralıklarını `BOOT_ID + EVENT_ID` ile eşleştirir.
6. HA geçmişinde olay işareti ile ölçüm entity'leri ayrıysa timestamp yalnızca aynı modülün kendi kayıtlarını olay işareti çevresinde sıralamak için kullanılabilir. İki modülün ölçümleri timestamp ile eşleştirilmez.

## Python analiz adımları

1. T007 örnek dosyasındaki gerçek entity_id ve birimleri kullan; bilinmeyen entity adları uydurma.
2. Her modülün olay işareti dizisini kontrol et; eksik, yinelenen veya eşleşmeyen BOOT_ID/EVENT_ID aralıklarını raporla. Eksik aralığı tahminle doldurma.
3. Geçersiz PZEM değerlerini (-1.0, NaN, timeout, parse/alan hatası) etiketlemeden çıkar; kayıtları silme, dışlama nedenini say.
4. PZEM kararlılığını kendi paket aralığındaki PZEM değerlerinden; SCT kararlılığını kendi paket aralığındaki SCT değerlerinden bağımsız değerlendir. Eşik, tolerans ve minimum süre gerçek veriden sonra belirlenir.
5. PZEM'in yükseliş/düşüş ve yerleşme geçişlerini; SCT'nin kendi geçiş/yerleşme bölümlerini kararlı eğitim bölgesinden çıkar.
6. Aynı `BOOT_ID + EVENT_ID` paket aralığındaki karşılaştırılabilir kararlı yük bölgelerini eğitim örneği olarak eşleştir. Timestamp kesişimi, sabit gecikme veya birebir örnek eşleşmesi kullanma.
7. PZEM akımını referans etiket olarak ekle; PZEM mutlak ground truth değildir.
8. Eğitim çıktısına `BOOT_ID` ve `EVENT_ID` alanlarını Python ekler. Ham ESP ölçüm kayıtları değiştirilmez.
9. Kaynak dosya/hash, analiz kodu sürümü, kayıt özeti, örnek eşleşme ve yorumunu depoda sakla.

## Kabul ölçütü

- En az bir gerçek yük olayında iki modülün aynı BOOT_ID/EVENT_ID olay işaretleriyle paket aralığı oluşturulmuş.
- Her iki akışta kararlı bölge tespiti bağımsız yapılmış ve geçiş bölgeleri dışlanmış.
- En az bir aynı paket aralığı içindeki PZEM/SCT kararlı veri çifti eğitim örneği olarak üretilmiş.
- Eşleştirme paket kimliğiyle yapılmış; timestamp birebir eşleştirme anahtarı olarak kullanılmamış.
- Eksik/yinelenen/geçersiz olay ve ölçüm kayıtları raporlanmış.
- Veri kökeni, kod sürümü, örnek çıktı ve yorum depoda kayıtlı.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Paket işaretli bağımsız akışlardan PZEM referanslı kararlı alan eğitim verisi üretmek.
- **LOG:** T007 veri aktarımı henüz tamamlanmadı; bu kart kapsamında eşleştirme yapılmadı.
- **SONUÇ:** T008 BEKLEMEDE; T007 kabul ölçütleri sağlanınca açılacak. Mimari karar ADR-022'de kayıtlıdır.
