# ADR-026 — İki Python programı: gelen-kutu, doğrulama ve yerel arşiv

- **Tarih:** 2026-11-06
- **Durum:** KABUL EDİLDİ — kullanıcı mimari kararı
- **İlişkili görev:** [T007 — Home Assistant verisini PC'ye aktarma ve Python başlangıcı](../../tasks/T007-python-architecture.md)
- **İlişkili mimari:** [Python veri hattı mimarisi](../architecture/python-program-architecture.md)

## Bağlam

Home Assistant Recorder veritabanını BERO veri aktarım deposu gibi kullanmak ve aktarım sonrasında HA geçmişini temizlemek uygun bulunmadı. Kullanıcı HA History'den dışa aktardığı dosyayı kendisi PC'de belirlenen bir klasöre bırakacaktır. Bu klasör, Python tarafından işlenecek gelen-kutu olacaktır. Kullanıcı her seferinde yeni veriyi boş gelen-kutu alanına bırakmayı hedefler.

## Karar

BERO veri hattı iki bağımsız Python programından oluşacaktır.

### Python-1 — gelen-kutu alıcısı ve arşivleyici

1. Kullanıcı HA dışa aktarım dosyasını kendisi gelen-kutu klasörüne bırakır.
2. Python-1 gelen-kutudaki dosyayı okur; dosya biçimini, okunabilirliğini ve kayıt yapısını doğrular.
3. Kaynak dosya hash'i hesaplanır; yinelenen içerik ikinci kez arşivlenmez.
4. Doğrulama başarılıysa dosyanın kendisi içeriği değiştirilmeden yerel arşivin uygun bir alt klasörüne taşınır. Başarılı işlem sonrasında gelen-kutu işlenmiş dosya bakımından boş kalır.
5. Doğrulama başarısızsa kaynak dosya silinmez. Dosya hata/karantina alanında tutulur veya güvenli biçimde gelen-kutuda bırakılır; hata nedeni loglanır.
6. Her işlem için kaynak dosya adı, hash, işlem zamanı, dosya/kayıt özeti, kod sürümü ve sonuç kaydı tutulur.

### Python-2 — arşiv analiz programı

1. Yalnızca Python-1 tarafından arşivlenmiş dosyaları girdi kabul eder.
2. Home Assistant'a bağlanmaz ve gelen-kutu klasörünü yönetmez.
3. Arşivdeki kaynak dosyaları değiştirmez; analiz çıktıları kaynak arşivden ayrı tutulacaktır.
4. PZEM/SCT akışlarını inceleme, kararlılık, paketleme, eşleştirme ve etiketleme çalışmaları bu programın kapsamındadır.

## Veri güvenliği ve kapsam

- Home Assistant Recorder veritabanı bu iş akışında doğrudan okunmaz, değiştirilmez veya temizlenmez.
- Python-1, HA tarafında otomatik silme/temizlik yapmaz. Dosyanın gelen-kutudan arşive taşınması, kullanıcının PC'ye bıraktığı dosyanın yerel işlenmesidir.
- Doğrulama tamamlanmadan kaynak dosya taşınmaz veya silinmez.
- Kaynak dosya arşivde özgün içeriğiyle korunur; parse/normalize edilmiş analiz verisi kaynak dosyanın üzerine yazılmaz.
- Aynı hash ile yinelenen dosya saptanırsa işlem sonucu loglanır; sessizce ikinci bir kopya oluşturulmaz.

## Henüz kararlaştırılmayanlar

- Gelen-kutu, arşiv, hata/karantina ve log klasörlerinin fiziksel konumları ve adları.
- Arşiv alt klasörleme kuralı (tarih, deney, dosya grubu veya başka bir anahtar).
- Python-1'in klasörü tek seferlik tarama, periyodik kontrol veya olay tabanlı izleme biçiminde çalışması.
- HA dışa aktarımının gerçek CSV biçimi, sütun adları ve varsa ek metadata biçimi.
- Python programlarının paketlenmesi, çalıştırılması ve log formatı.

Bu ayrıntılar terminalde klasör yapısını konuşup oluştururken ve gerçek export örneği incelenirken belirlenecektir. Bu ADR herhangi bir fiziksel klasörün oluşturulduğunu veya Python kodunun hazır olduğunu iddia etmez.

## Kabul gerekçesi

Kullanıcı veri dosyasını bilinçli olarak kendisi gelen-kutuya bırakır; ilk program yalnızca dosyayı güvenli biçimde arşivler; ikinci program arşiv üzerinde bağımsız analiz yapar. Böylece HA Recorder veritabanına müdahale edilmez ve kaynak verinin PC'deki özgün kopyası korunur.
