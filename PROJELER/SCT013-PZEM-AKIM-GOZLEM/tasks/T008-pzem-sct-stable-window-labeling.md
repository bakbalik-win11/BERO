# T008 — PZEM/SCT kararlı alan eşleştirme ve etiketleme

- **Durum:** BEKLEMEDE
- **Faz:** Faz 2 — Bulunan kodu PZEM ile eğitmek
- **Bağımlılık:** T007'nin gerçek Home Assistant dışa aktarımını PC'ye taşıması ve veri alanlarını koruduğunu doğrulaması.
- **Hedef:** PZEM ve SCT akışlarında kararlı alanları ayrı ayrı belirlemek; aynı yük/olay içinde zaman bakımından örtüşen alanları eşleştirmek; geçerli PZEM akımını SCT penceresi için etiket olarak kaydetmek.

## Yapılacaklar

1. T007 örnek dosyasındaki gerçek entity_id ve birimleri kullan; bilinmeyen entity adları uydurma.
2. PZEM ve SCT kayıtlarının timestamp dağılımını, güncelleme aralıklarını, boşlukları ve tekrarları ayrı incele.
3. Geçersiz PZEM değerlerini (-1.0, NaN, timeout, parse/alan hatası) etiketlemeden çıkar; kayıtları silme, dışlama nedenini say.
4. PZEM kararlılığını kendi akışında, SCT kararlılığını kendi akışında değerlendir. Pencere yayılımı, min-max aralığı, eğim ve ardışık pencere tutarlılığı aday ölçütlerdir; eşikler gerçek veri görülmeden sabitlenmez.
5. Aynı olay içindeki zaman bakımından örtüşen kararlı alanları eşleştir. Sabit 3 saniye gecikme/maske varsayma.
6. PZEM akımını referans etiket olarak ekle; PZEM mutlak ground truth değildir.
7. Geçiş/yerleşme dinamiklerini kararlı etiketli alanlardan ayrı tut.
8. Kaynak dosya/hash, analiz kodu sürümü, kayıt özeti, örnek eşleşme ve yorumunu depoda sakla.

## Kabul ölçütü

- En az bir gerçek yük olayında PZEM ve SCT aynı olay bağlamında kayıtlı.
- İki akışın zaman ve kararlılık davranışı ayrı raporlanmış.
- En az bir ortak kararlı alan eşleştirilmiş ve PZEM etiketiyle işaretlenmiş.
- Dışlanan okumalar ve nedenleri sayılmış.
- Veri kökeni, kod sürümü, örnek çıktı ve yorum depoda kayıtlı.

## HEDEF / LOG / SONUÇ

- **HEDEF:** PZEM referanslı kararlı alan etiketleme yöntemini gerçek veride kurmak.
- **LOG:** T007 veri aktarımı henüz tamamlanmadı; bu kart kapsamında eşleştirme yapılmadı.
- **SONUÇ:** T008 BEKLEMEDE; T007 kabul ölçütleri sağlanınca açılacak.
