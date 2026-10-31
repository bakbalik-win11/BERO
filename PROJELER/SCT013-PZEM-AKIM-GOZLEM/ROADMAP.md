# SCT-013 – PZEM Akım Gözlem | Yol Haritası

Bu projede yalnızca **iki ana faz** vardır. Eski deney numaraları ve çok aşamalı tasarım kayıtları Faz 1 tarihçesidir; yeni aktif iş listesi değildir.

## Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak

<badge> TAMAMLANDI </badge>

**Hedef:** SCT013 akım gözlemi için çalışan bir kod yolu bulmak ve PZEM karşılaştırmalarında ±%4 sapma hedefini sağlamak.

**Sonuç:** Dış kaynaklı ESPHome \`ct_clamp\` kodu kullanılarak hedefe ulaşıldı. Dört karşılaştırma koşulunun tamamı ±%4 sınırında:

| Yük koşulu | Referans | Kod sonucu | Sapma |
|---|---:|---:|---:|
| 100 W akkor | 0,446–0,447 A | 0,4471 A | yaklaşık %0 |
| 150 W akkor | 0,616 A | 0,615 A | −%0,2 |
| Kettle düşük/kararlı | 0,637 A | 0,656 A | +%3,0 |
| Kettle kaynama | 6,39 A | 6,15 A | −%3,8 |

Bu sonuçlar paylaşılan deney logları ve karşılaştırma kayıtlarıyla desteklenmektedir. Harici kodun kaynağı bu depoda bulunmasa da Faz 1 hedefi açısından sonuç kabul edilmiştir.

**Faz 1 kapsamındaki eski çalışmalar:** E00A, E00B, E00, E01–E08, E00F ve ilgili alt adımlar bu ana fazın tarihsel çalışma kayıtlarıdır. Hedefe ulaşıldığı için Faz 1 kapsamında kalan, henüz yapılmamış tüm deneyler ve işler **KAPATILDI — HEDEFE ULAŞILDI**. Bu ifade, yapılmamış deneylerin fiziksel olarak gerçekleştirildiği anlamına gelmez. Gerçekleşmiş ölçüm ve loglar kendi sonuç dosyalarında korunur.

**Kapanış kararı:**
- Dış kodla ±%4 hedefi sağlandı; Faz 1 kapandı.
- Faz 1 için tasarlanan ama yapılmamış deneyler yeniden açılmayacak.
- Ham 50 Hz dalga aktarımı, örnek başına timestamp ve DMA/ADC Continuous geliştirme işleri yapılmayacak.
- Faz 1'de bulunan çalışan ölçüm yolu korunacak; gereksiz yere yeniden yazılmayacak.

Ayrıntılı geçmiş: [ADR-009](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md), [Faz 1 deney arşivi](experiments/README.md).

## Faz 2 — Bulunan kodu PZEM ile eğitmek

<badge color="success"> AKTİF FAZ </badge>

**Hedef:** Faz 1'de bulunan çalışan SCT kodunu PZEM-004T V3.0 referans akışıyla karşılaştırmak; PZEM'in kararlı alanlarını ve SCT'nin kararlı alanlarını ayrı ayrı bulmak; zaman bakımından örtüşen alanları eşleştirmek; SCT verisini PZEM ile etiketlemek; zamanla katsayıyı/modeli iyileştirmek.

Bu faz BERO boyunca süren bir öğrenme döngüsüdür. PZEM proje referansıdır; kusursuz veya mutlak ground truth kabul edilmez.

### İş sırası

1. **T007 — Home Assistant verisini PC'ye aktarma (ilk aktif iş).**
   - Gerçek HA entity geçmişlerini PC'ye alacak en küçük ve sürdürülebilir veri aktarım yolunu kur.
   - PZEM ve mevcut SCT entity'lerini, kaynak zaman damgalarını ve birimleri koru.
   - İlk adımda model veya deney tasarlama; önce verinin eksiksiz ve tekrar işlenebilir biçimde PC'ye ulaşmasını sağla.
2. **T008 — PZEM ve SCT kararlı alanlarını bulma, eşleştirme ve etiketleme.**
   - PZEM ve SCT akışlarının kararlılığını birbirinden bağımsız değerlendir.
   - Aynı yük/olay içindeki zaman bakımından örtüşen kararlı alanları eşleştir.
   - Geçersiz PZEM kayıtlarını etiket dışında tut; dışlanan kayıtların sayısını ve nedenini koru.
   - PZEM akımını eşleşen SCT penceresinin etiketi olarak kaydet.
3. **T006 — Mevcut katsayıyı ve modeli değerlendirme.**
   - İlk karşılaştırmada mevcut K=24.22 değerini değiştirme.
   - Etiketli kararlı alanlarda sapmayı hesapla.
   - Yalnız veri sistematik ve tekrarlanabilir bir sorun gösterirse katsayı/model değişikliğini değerlendir.
   - Her yeni model/katsayıyı yeni calibration_id ile sürümle; önceki sürümü koru.
4. **Sürekli öğrenme.**
   - Yeni veri geldikçe aynı döngüyü tekrarla.
   - Yeni deneyler yalnız gerçek bir karar sorusunu cevaplamak gerektiğinde, yeni deney numaralarıyla tasarlanır. Şu anda Faz 2 için yeni deney planı açılmış değildir.

### Faz 2'nin ilk kabul kapısı

- Home Assistant'tan alınan PZEM ve SCT kayıtları PC'de okunabilir.
- Kaynak entity kimliği, birim, timestamp ve dışa aktarma aralığı korunur.
- Ham kayıt üzerinde tekrar çalışılabilir bir Python aktarım/okuma akışı vardır.
- Örnek veri ve aktarım logu depoda saklanır; sonuç yorumu eklenir.

### ct_clamp için sıra kararı

Mevcut çalışan \`ct_clamp\` kodu şimdilik korunur. Önce Faz 2 verisiyle PZEM/SCT kararlı alan eşleştirmesi yapılır. Eşleşmiş veride tekrarlanabilir sapma veya açıklanamayan davranış görülürse \`ct_clamp\` kaynak kodu hedefli olarak incelenir. Salt merakla algoritma değiştirilmez. Bu inceleme Faz 2 veri değerlendirmesinden sonra gelir.

## Kapsam sınırları

Bu proje enerji analizörü, güç kalitesi analizörü, PF hesaplayıcı, FFT/THD veya harmonik analiz projesi değildir. PZEM'in kendi alanları referans kaydı olarak tutulabilir; SCT'den PF veya faz açısı hesaplanmaz. Sürekli ham ADC arşivi ve yüksek hızlı ham dalga edinimi Faz 1 kapanışında kapsamdan çıkarılmıştır.

## Karar ve tarihçe

- [ADR-009 — ±%4 hedefi ve ara işlerin kapanışı](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md)
- [ADR-010 — PZEM referanslı öğrenme odağı](docs/decisions/ADR-010-pzem-stable-window-learning-focus.md)
- [ADR-011 — İki fazlı proje yapısı](docs/decisions/ADR-011-two-phase-project-structure.md)
- [Faz 1 deney arşivi](experiments/README.md)
- [Faz 2 Python mimarisi](docs/architecture/python-program-architecture.md)
