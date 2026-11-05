## 2026-11-05 — Sonraki oturumun ilk işi: yüksüz/gürültü CSV kaydı

Kullanıcı bu gece sistem yüksüzken Home Assistant History kaydı alacağını bildirdi. Bir sonraki oturum açıldığında ilk olarak bu yüksüz CSV dosyası kullanıcıdan istenecek; kullanıcı sağlayınca ayrı OFF/yüksüz gürültü veri havuzunun ilk kaydı olarak analiz edilecek.

- SCT1 sarı/GPIO32: fiziksel 1 geçiş (YAML/entity etiketi 2T kalmış olabilir).
- SCT2 yeşil/GPIO33: nötr hattında 4 geçiş.
- SCT3 mavi/GPIO34: faz hattında 3 geçiş.
- GPIO35: ortak bias.
- Her oturum ayrı analiz edilecek; ham dağılımlar korunarak zaman içinde ortak havuzda biriktirilecek.
- Tur sayısına bölme yaklaşık normalize karşılaştırmadır, kesin kalibrasyon değildir. Kanal/hat konumu, kazanç ve K farkları nedeniyle ham değerler de raporda tutulacak.
- Amaç: yüksüz tabanın tipik seviyesi, üst yüzdelikleri ve tekrarlayan en yüksek değerleri görmek; henüz eşik belirlemek değil.
- Bu kayıt ON kalibrasyonuna katılmayacak.


## 2026-11-05 — I007 uzun süreli fiziksel sıfır-akım gürültü bandı

I007 tek gecelik test değil; başlangıç hedefi yaklaşık 7–10 gün, gerekirse kullanıcı kararıyla daha uzun sürecek veri toplama çalışmasıdır. Kullanıcı her gün/uygun oturum sonunda HA History CSV sağlayacak. Her oturum ayrı analiz edilecek; geçerli ham kayıtlar depodaki kümülatif havuza eklenerek güncellenecek. Her ekleme öncesi mevcut havuz depodan okunacak, tekrarlar kontrol edilecek, yeni kayıtlar eklenecek ve güncel kümülatif veri/özet tekrar depoya yazılacak. İlk gerçek CSV geldiğinde gerçek kolonlara göre veri şeması belirlenecek.

**Fiziksel referans:** Kullanıcının teyidine göre ölçülen hatta hiçbir yük bağlı değil ve ESP/PZEM/modüller bu hattan beslenmiyor; dolayısıyla gerçek hat yük akımı fiziksel olarak 0 A. SCT'nin sıfırdan farklı okuması bu koşuldaki ölçüm tabanı/gürültü çıktısıdır; sıfır koşulu PZEM göstergesinden varsayılmıyor.

Hedef uzun dönem SCT1/2/3 gürültü bandını, üst yüzdelikleri ve oturumlar arası değişimi belirlemek; şu aşamada eşik/model seçmek değildir. Ham ölçümler korunacak, tur-normalize karşılaştırma yalnız yardımcı olacak. Bu havuz ON kalibrasyonundan ayrı tutulacak.
