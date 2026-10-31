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

1. **T009 — Modülleri ve ESP düğümlerini pratik olarak yeniden devreye alma (ilk aktif iş).**
   - Modül kapsamı, gerçek ESP kartı, pin eşlemesi ve düşük gerilim bağlantıları belirlenir.
   - Çalışan kod/örnek seçilir, minimum uyarlama yapılır.
   - Derleme ve gerçek donanım testi ayrı doğrulanır.
   - Modülün gerçek çıktısı ve log yorumu depolanır.
   - Modül sırası kullanıcıyla kararlaştırılır; burada sabit bir ESP sırası dayatılmaz.
2. **T007 — Home Assistant → PC veri aktarımı.**
   - PZEM ve SCT modülleri gerçek veri ürettiğinde HA geçmişi PC'ye alınır.
   - Entity kimliği, kaynak timestamp, birim ve ham durum korunur.
3. **T008 — PZEM/SCT kararlı alan eşleştirme ve etiketleme.**
   - İki akışın kararlılığı ayrı değerlendirilir.
   - Zaman bakımından örtüşen kararlı alanlar eşleştirilir.
   - PZEM proje referansı olarak SCT pencerelerine etiketlenir; mutlak ground truth sayılmaz.
4. **T006 — Katsayı/model değerlendirmesi.**
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
- [T009 — Modül/ESP devreye alma](tasks/T009-practical-system-bringup.md)
- [Faz 1 deney arşivi](experiments/README.md)
