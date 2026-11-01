# SCT-013 – PZEM Akım Gözlem | Yol Haritası

Bu projede yalnızca **iki ana faz** vardır. Faz 1 kodu bulup ±%4 hedefini sağlama aşamasıydı. Faz 2 ise BERO sistemini pratik biçimde yeniden kurma, modülleri devreye alma ve çalışan sistemi geliştirme aşamasıdır. Eski deney kayıtları tarihsel arşiv olarak korunur.

## Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak

<badge> TAMAMLANDI </badge>

**Hedef:** SCT013 akım gözlemi için çalışan bir kod yolu bulmak ve PZEM karşılaştırmalarında ±%4 sapma hedefini sağlamak.

**Sonuç:** Dış kaynaklı ESPHome ct_clamp kodu kullanılarak hedefe ulaşıldı. Dört karşılaştırma koşulunun tamamı ±%4 sınırında:

| Yük koşulu | Referans | Kod sonucu | Sapma |
|---|---:|---:|---:|
| 100 W akkor | 0,446–0,447 A | 0,4471 A | yaklaşık %0 |
| 150 W akkor | 0,616 A | 0,615 A | −%0,2 |
| Kettle düşük/kararlı | 0,637 A | 0,656 A | +%3,0 |
| Kettle kaynama | 6,39 A | 6,15 A | −%3,8 |

Bu sonuçlar kullanıcı tarafından paylaşılan karşılaştırmalar ve kayıtlarla desteklenmektedir. Harici kodun kaynağı depoda bulunmasa da Faz 1 hedefi açısından sonuç kabul edilmiştir.

**Faz 1 kapsamındaki eski çalışmalar:** E00A, E00B, E00, E01–E08, E00F ve ilgili alt adımlar bu ana fazın tarihsel kayıtlarıdır. Hedefe ulaşıldığı için Faz 1 kapsamında kalan, henüz yapılmamış deneyler ve işler **KAPATILDI — HEDEFE ULAŞILDI**. Bu ifade, yapılmamış deneylerin fiziksel olarak gerçekleştirildiği anlamına gelmez.

Ayrıntılı geçmiş: [ADR-009](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md), [Faz 1 deney arşivi](experiments/README.md).

## Faz 2 — Pratik yeniden kurulum ve sistem geliştirme

<badge color="success"> AKTİF FAZ </badge>

**Ana hedef:** Faz 1'de çalışan akım okuma yaklaşımını ve depoda biriken kod/donanım bilgisini başlangıç noktası alarak BERO'nun modüler sistemini yeniden kurmak, ESP düğümlerini tek tek devreye almak ve gerçek kullanım sonuçlarıyla geliştirmek.

Faz 2 yeni bir başlangıçtır; ancak geçmişi silmek anlamına gelmez. Kayıtlı YAML'lar, kodlar, donanım notları, loglar ve kararlar başlangıç referanslarıdır. Uygun olduklarında yeniden kullanılır, gerekirse somut ihtiyaca göre uyarlanır. Bunların hiçbiri yeni fiziksel kurulumun test edildiği anlamına gelmez.

### Çalışma yaklaşımı

1. Önce aynı işi yapan çalışan kodu, örnek projeyi, kütüphaneyi veya hazır modül çözümünü bul ve değerlendir.
2. Gerçek donanım/kart/pin bilgilerini doğrula; bilinmeyen bağlantı veya parça özelliğini varsayma.
3. Bir seferde tek modül ve tek temel işlevle başla. Gereken en az kod uyarlamasını yap.
4. Yapılandırma/derleme kontrolünü, fiziksel bağlantıyı ve gerçek çalışma testini ayrı aşamalar olarak doğrula.
5. Başarılı kodla birlikte gerçek cihaz logunu/çıktısını ve teknik yorumunu depoda sakla.
6. Başka modüllerle entegrasyonu, tekil işlevler çalıştıktan sonra yap.
7. Manyetik teori, ESP32 ADC iç mimarisi, harici ADC/SPI gibi konular somut bir arıza, ölçüm çelişkisi, güvenlik ihtiyacı veya açık tasarım kararı gerektirirse derinleştirilir. Sırf teorik kapsamı genişletmek için uygulama hedefi ertelenmez.

### Faz 2 görev sırası

1. **T009 — Modülleri ve ESP düğümlerini pratik olarak yeniden devreye alma (üst görev).**
   - Modül modül yürütülecek genel devreye alma çerçevesidir.
2. **T010 — Modül 2: ESP32D1 üçlü SCT okuma modülü — KAPATILDI.**
   - E11 sıralı üç-SCT kodu 100 W akkor ampul deneyinde çalıştı; üç kanaldan aynı deney oturumunda veri alındı.
   - Mevcut kapsam için üç kanallı okuma ve gözlem yeterli kabul edildi. Yeni yüklerin UNIT doğrulaması bu görevin devamı değildir.
   - Sonraki yük doğrulamaları PZEM ile birlikte T007/T008 veri hattında ele alınacaktır.
   - Ayrıntı: [T010 kapanış kaydı](tasks/T010-module2-triple-sct-bringup.md).
3. **T007 — Home Assistant → PC veri aktarımı.**
   - PZEM ve SCT modülleri gerçek veri ürettiğinde HA geçmişi PC'ye alınır.
   - Entity kimliği, kaynak timestamp, birim ve ham durum korunur.
4. **T008 — PZEM/SCT kararlı alan eşleştirme ve etiketleme.**
   - İki akışın kararlılığı ayrı değerlendirilir.
   - Olay işaretleri her iki akışı `BOOT_ID + EVENT_ID` paket aralıklarına böler; aynı paket aralığındaki bağımsız kararlı SCT/PZEM bölgeleri eşleştirilir. Timestamp iki sensör arasında eşleştirme anahtarı değildir.
   - PZEM proje referansı olarak SCT pencerelerine etiketlenir; mutlak ground truth sayılmaz.
5. **T006 — Katsayı/model değerlendirmesi.**
   - İlk karşılaştırmada K=24.22 başlangıç değeri olarak incelenir.
   - Yalnız eşleşmiş veriler sistematik ve tekrarlanabilir sapma gösterirse iyileştirme yapılır.
   - Her yeni sürüm gerçek veri ve yeni calibration_id ile kaydedilir.
5. **Sürekli geliştirme.** Gerçek kullanım veya testten doğan yeni ihtiyaçlar küçük ve doğrulanabilir adımlarla ele alınır.

### Faz 2 ilk kabul kapısı

- En az bir seçilmiş modülün gerçek kartı, bağlantısı ve temel işlevi doğrulanmış olmalı.
- Kullanılan kodun kaynağı/sürümü veya depodaki referansı belli olmalı.
- Yapılandırma derleme kontrolünden geçmiş olmalı.
- Gerçek cihaz çıktısı/logu ve yorumuyla birlikte kaydedilmiş olmalı.
- Test edilmemiş modüller açıkça beklemede kalmalı.

## Kapsam sınırları

Bu proje enerji analizörü, güç kalitesi analizörü, PF hesaplayıcı, FFT/THD veya harmonik analiz projesi değildir. PZEM'in kendi alanları referans kaydı olarak tutulabilir; SCT'den PF veya faz açısı hesaplanmaz. Sürekli ham ADC/50 Hz dalga kaydı ve örnek başına timestamp, açık ve gerekçeli yeni bir ihtiyaç olmadıkça proje hedefi değildir.

## Karar ve tarihçe

- [ADR-009 — ±%4 hedefi ve Faz 1 kapanışı](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md)
- [ADR-010 — PZEM referanslı kararlı alan öğrenmesi](docs/decisions/ADR-010-pzem-stable-window-learning-focus.md)
- [ADR-011 — Projeyi iki faza ayırma](docs/decisions/ADR-011-two-phase-project-structure.md)
- [ADR-014 — Faz 2 pratik yeniden başlangıç](docs/decisions/ADR-014-phase2-practical-restart.md)
- [ADR-022 — Paket işaretleriyle akış bölümleme ve eğitim verisi oluşturma](docs/decisions/ADR-022-packet-marker-segmented-training-streams.md)
- [T009 — Modül/ESP devreye alma](tasks/T009-practical-system-bringup.md)
- [Faz 1 deney arşivi](experiments/README.md)


## 2026-11-01 — Faz 2 veri hattı ve düşük akım uygulama planı

Faz 2 için ayrıntılı yürütme planı [burada](docs/plans/2026-11-01-phase2-data-and-low-current-execution-plan.md) tutulur. Ana görev sırası değişmez: T009 → T010 → T007 → T008 → T006. T010 pratik modül devreye alma tamamlanmadan veri/öğrenme hattı görevleri aktif göreve alınmaz. 0,4 A fiziksel alt sınır olarak kabul edilmez; eski E00F yapılandırmasındaki 0,35 A filtresi güncel ESP32D1 Modül 2'ye atfedilmez. Bölgesel model kararı eşleşmiş ve tekrarlanabilir veriye bağlıdır. Bu planlama kaydı firmware veya ölçüm sonucu değildir.


## 2026-11-01 — Paket işaretli eğitim akışı kararı

Modül 3, olay mesajını kendi PZEM akışına ayrı kayıt olarak ekler ve aynı mesajı UDP 4210 üzerinden Modül 2'ye yollar. Modül 2 aldığı mesajı kendi SCT akışına aynı biçimde ayrı kayıt olarak ekler. Python her akışı paket işaretleriyle böler, BOOT_ID + EVENT_ID ile aralıkları eşleştirir ve her sensörün kararlılığını kendi verisinden bağımsız bulur. Timestamp, iki sensörün ölçümlerini eşleştirme anahtarı değildir. Ayrıntı ve ADR-019 üzerindeki değişiklik: [ADR-022](docs/decisions/ADR-022-packet-marker-segmented-training-streams.md). Firmware henüz değiştirilmedi.
