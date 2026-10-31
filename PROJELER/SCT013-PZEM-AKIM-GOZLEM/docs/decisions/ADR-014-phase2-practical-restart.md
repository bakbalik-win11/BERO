# ADR-014 — Faz 2'nin pratik yeniden başlangıç ve sistem geliştirme olarak tanımlanması

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ
- **İlişkili kararlar:** ADR-009, ADR-010, ADR-011, ADR-012, ADR-013
- **Karar kaynağı:** Kullanıcı yönlendirmesi

## Bağlam ve geriye dönük değerlendirme

Faz 1'de çalışan bir SCT akım okuma kod yolu bulundu ve kullanıcının paylaştığı dört yük karşılaştırmasında ±%4 hedefi sağlandı. Böylece temel hedef olan akım okuyabilme konusunda çalışan bir başlangıç elde edildi.

Sonraki çalışmalarda, pratik çalışan kod ve modül örneklerini bulup uygulamak ve bunları geliştirmek yerine manyetik teoriye ve ESP32 dahili ADC mimarisine gereğinden fazla derinleşildi. Akım okuma hedefinde ilerleme sağlanamayan noktalarda konu daha temel teorik/elektronik incelemelere doğru genişledi. Kullanıcı bu yönelimi hobi projesinin pratik geliştirme doğasına uygun bulmadığını belirtti.

Bu değerlendirme, manyetik teori veya ADC bilgisinin yanlış olduğu anlamına gelmez. Sorun, bu derinliğin gerçek bir uygulama engeli veya somut teşhis ihtiyacı ortaya çıkmadan ana çalışma yönü hâline gelmesidir. Önceki araştırmalar, ölçüm kayıtları ve kararlar tarihsel teknik bilgi olarak korunur.

## Karar

**Faz 2, Faz 1 kodunu yalnız PZEM ile eğitme aşaması değildir. Faz 2, BERO sisteminin pratik olarak yeniden kurulup devreye alınacağı ve geliştirileceği yeni başlangıçtır.**

Çalışma yaklaşımı:

1. Önce aynı işi yapan çalışan kod, örnek proje, kütüphane veya hazır modül uygulaması aranır ve incelenir.
2. Depodaki mevcut YAML'lar, kodlar, loglar ve donanım kayıtları başlangıç referansı olarak kullanılır. Bunlar yeni kurulumun sorgulanamaz veya değiştirilemez taslağı sayılmaz.
3. Donanım ve ESP düğümleri modül modül, tek işlevden başlayarak devreye alınır.
4. Her aşamada gereken en az kod değişikliği yapılır; önce derleme/konfigürasyon, sonra uygun düşük gerilim bağlantısı ve gerçek çıktı doğrulanır.
5. Başarılı kod, gerçek log/çıktı ve çıktının yorumu depoda saklanır.
6. Teori, manyetik devre ayrıntıları, ESP32 ADC iç mimarisi veya alternatif ADC mimarileri ancak somut bir arıza, ölçüm çelişkisi, güvenlik gereği veya uygulama kararı bunları gerektirirse derinlemesine incelenir.
7. Sistem pratik olarak çalışır hâle getirildikten sonra PZEM referansı, Home Assistant veri aktarımı, kararlı alan eşleştirme ve katsayı/model geliştirme adımları yürütülür.

## Faz 2 çalışma sırası

1. **T009 — Modülleri ve ESP düğümlerini pratik olarak yeniden devreye alma.** Donanım bağlantıları, kart seçimi/pin eşlemesi, çalışan kod örneği seçimi, minimum uyarlama, derleme ve gerçek işlev testi. Modül sırası kullanıcıyla belirlenir.
2. **T007 — Home Assistant → PC veri aktarımı.** PZEM ve SCT düğümleri gerçek entity ürettiğinde başlar.
3. **T008 — PZEM/SCT kararlı alan eşleştirme ve etiketleme.**
4. **T006 — Mevcut K=24.22 katsayısı/model değerlendirmesi ve verinin gerekçelendirdiği iyileştirme.**
5. **Sürekli geliştirme —** Yeni ihtiyaçlar gerçek kullanım veya test sırasında ortaya çıktıkça ele alınır.

## Sınırlar

- Faz 1'in ±%4 sonucu korunur; fakat Faz 2 sisteminin tamamının çalıştığı veya yeni üç kanallı Modül 2'nin doğrulandığı anlamına gelmez.
- ESPHome YAML ve diğer kod kayıtları silinmez. Yeni kurulumda bunlar başlangıç referansı olarak değerlendirilir; gerektiğinde kontrollü biçimde uyarlanır.
- Önceden araştırılmış ADC/analog konular yeniden açılmak zorunda değildir. Yalnız somut ihtiyaç olduğunda ele alınır.
- Sürekli ham ADC/50 Hz dalga arşivi, FFT/THD, harmonik analiz, güç kalitesi ve enerji analizörü proje kapsamına eklenmez.
- Şebeke tarafı güvenliği ve gerekli elektriksel doğrulamalar pratik yaklaşım nedeniyle atlanmaz.

## Sonuç

Faz 2'nin ana hedefi, kayıtlı kod ve edinilmiş donanımdan hareketle BERO'nun modüler sistemini çalışır hâle getirmek ve ardından gerçek kullanımdan gelen ihtiyaçlarla geliştirmektir. PZEM referanslı veri eğitimi bu fazın sonraki alt aşamasıdır; Faz 2'nin tamamı değildir.

**Durum:** Kapsam ve çalışma ilkesi karara bağlandı. Donanımın yeniden kurulması, ESP düğümlerinin derlenmesi/yüklenmesi ve fiziksel testler bu ADR ile yapılmış sayılmaz.
