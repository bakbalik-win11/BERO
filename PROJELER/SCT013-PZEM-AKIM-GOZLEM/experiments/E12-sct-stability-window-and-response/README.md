# E12 — SCT kararlı alan tespiti, PZEM örtüşmesi ve tepki süresi

**Durum:** PLANLANDI / ilk gözlem oturumu verisi bekleniyor  
**Tarih:** 2026-11-05  
**Faz:** Faz 2  
**İlişkili işler:** T007 (HA → PC), T008 (kararlı alan eşleştirme/etiketleme), T006 (sonraki katsayı/model değerlendirmesi)

## Amaç

SCT'nin PZEM'e göre daha sık ölçüm sonucu üretmesinin, yük değişimlerini daha erken ve daha ayrıntılı yakalamaya yardımcı olup olmadığını incelemek. İlk odak SCT1 (sarı kanal, GPIO32).

Bu deney üç teknik soruyu kapsar:

1. **SCT kararlı alan algoritması:** Geçişten sonra SCT değerleri ne kadar sürede belirli bir seviye çevresinde toplanıyor? Ortalama, standart sapma/dağılım ve ardışık pencere ortalamalarının değişimi ile tekrarlanabilir kararlı alan bulunabilir mi?
2. **PZEM–SCT kararlı alan örtüşmesi:** PZEM ve SCT kararlılığı kendi akışlarında bağımsız tespit edildiğinde, zaman bakımından örtüşen bölümler eğitim adayı oluşturuyor mu? Aynı timestamp'e denk gelen tekil örnekler doğrudan eşleştirilmeyecek.
3. **SCT tepki süresi ve kısa ölçüm penceresi:** SCT yük değişimini PZEM'den daha erken yakalıyor mu? 200 ms'den kısa sample_duration ile kararlılık ve tekrarlanabilirlik korunabiliyor mu?

## Neden SCT?

PZEM'in daha seyrek güncellenmesi, kısa süreli yük davranışlarını ayrıntılı izlemeyi sınırlayabilir. SCT/ct_clamp akışı daha sık sonuç ürettiğinden geçiş sonrası yerleşme ve makine çalışma evreleri daha ayrıntılı gözlenebilir. Bu doğrulanmış sonuç değil, E12'nin sınayacağı hipotezdir.

Çamaşır makinesi gibi aygıtlarda yalnızca akım seviyesini bilmek değil; motor, pompa ve rezistansın devreye girme/çıkma davranışlarını yakalamak önemlidir. SCT'nin hızlı tepki potansiyeli bu nedenle ayrıca incelenecektir.

## Mevcut referans düzeni

- Öncelikli kanal: Modül 2 SCT1, sarı kablo, GPIO32.
- SCT2 GPIO33 ve SCT3 GPIO34 gözlem kanallarıdır; üç kanal sıralı okunduğu için örnekleri eşzamanlı kabul etme.
- Ortak bias: GPIO35.
- Mevcut ct_clamp ayarı: sample_duration 200 ms, update_interval 2 s.
- Mevcut katsayı: K=24.22; ilk referans analizinde değiştirilmeyecek.
- PZEM proje referansıdır; kusursuz ground truth değildir.
- Olay işaretleri BOOT_ID + EVENT_ID + ON/OFF; tam ON/OFF penceresi paket bütünlüğü için kullanılır.

## İlk gözlem oturumu — 2026-11-05

### Planlanan koşullar
- Saat: 20:07–20:37 (+03:00), hedef 30 dakika.
- Yük: 100 W akkor ampul.
- Kullanıcının ön bilgisi/hedefi: PZEM kararlı ON alanında yaklaşık 0,471–0,472 A; bu değerler sonuç yerine geçmez.
- SSR döngüsü: 40 saniye ON / 20 saniye OFF.
- Amaç: PZEM ve SCT1 kararlı alanlarını bağımsız belirleyip zaman örtüşmesini elle ön değerlendirmek. Python uygulaması henüz yazılmış değildir.

### 20:12 fiziksel kablo değişikliği
Kullanıcı 20:12 civarında kablo yapısında küçük bir fiziksel değişiklik yaptığını bildirdi. Değişikliğin tam niteliği henüz belirtilmedi. Analizde 20:12 öncesi ve sonrası ayrı bölümler olarak ele alınmalı. Logda etki görünmüyorsa fiziksel etkinin olmadığı sonucu çıkarılmamalı.

### Sarım ve değer bildirimi
Kullanıcı, SCT1'in kod tanımında 2 tur bulunmasına rağmen fiziksel kabloda şu anda tek geçiş olduğunu ve gözleminde yaklaşık 0,470 A civarında değer gördüğünü bildirdi. Bu kullanıcı gözlemidir; ham logla doğrulanmadan kalibrasyon/doğruluk sonucu sayılamaz.

### İlk oturumun kanıt durumu
Bu protokol kaydı oluşturulurken 20:07–20:37 tam Modül 2 ve Modül 3 logları sonuç dosyasına eklenmemiştir. Kararlı alan, iki akış örtüşmesi veya SCT'nin PZEM'den hızlı olduğu henüz doğrulanmamıştır.

## İlk algoritma taslağı — eşikler henüz belirlenmedi

SCT1'in yayınlanan değerleri üzerinde kayan/ardışık pencereler değerlendirilecek:
- Her pencerede örnek sayısı, ortalama ve standart sapma hesaplanır.
- Ardışık pencere ortalamaları arasındaki mutlak/bağıl değişim izlenir.
- Dağılımın ve ortalama değişiminin belirli süre boyunca kabul koşulunda kalması kararlı alan adayı oluşturur.
- ON/OFF olayına göre geçiş sonrası yerleşme süresi ayrıca raporlanır.
- Pencere boyu, minimum süre ve eşikler gerçek veri incelendikten sonra seçilir; şimdiden sayısal eşik uydurulmaz.
- Benzer ortalamaya sahip ancak dağılımı farklı pencereler ayrıştırılır; yinelenen değer/quantization ve güncelleme sıklığı dikkate alınır.

## ON/OFF paketleme, eğitim ve OFF alanının kapsamı

1. Her akışta BOOT_ID + EVENT_ID ile tam ON/OFF paket bütünlüğünü doğrula. ON olayı paketi başlatır; eşleşen OFF olayı paketi kapatır.
2. Eksik açılış/kapanış, sıra bozukluğu veya boot değişimi olan aralıkları tamamlanmış paket/eğitim adayı sayma; ham kaydı koru.
3. **OFF alanı eğitim verisi değildir.** OFF okumaları hiçbir koşulda SCT/PZEM eğitim eşleştirmesine veya eğitim örneği üretimine alınmaz. OFF, bu ilk aşamada sıfır/kapalı durum kabulüdür ve paket sınırını kapatmak için kullanılır.
4. SCT kararlı alanlarını yalnız SCT'nin ON ölçüm verisinden, PZEM kararlı alanlarını yalnız PZEM'in ON ölçüm verisinden bağımsız tespit et.
5. İki ON kararlı aralığın zaman kesişimini hesapla. Yalnız kesişen bölüm eşleşmiş eğitim penceresi adayıdır.
6. PZEM geçiş/yerleşme örneklerini SCT örnekleri için noktasal referans yapma.
7. Ham kayıt kesilmez/silinmez. Eğitim yalnız ON kararlı örtüşmesinden oluşur; modelin sonraki davranış testi tam ham kayda, ON/OFF ve geçişler dahil, uygulanabilir.

**OFF/yüksüz taban istatistiği ayrı ve sonraki aşamaya bırakılmış isteğe bağlı bir araştırmadır.** Gerekirse aç-kapa döngüsü olmadan, ölçülen hatta yük bağlı değilken uzun bir kayıt alınır. Bu kayıttan yüksüz taban dağılımı ve olası gürültü/kapalı durum eşiği çıkarılabilir. Bu çalışma E12'nin ilk eğitim hedefi değildir ve OFF verisini eğitim örneğine dönüştürmez.

Bu yaklaşım ADR-024 ve güncellenmiş ADR-025 ile uyumludur. Timestamp tekil örnekleri birebir eşleştirmek için değil, bağımsız ON kararlı aralıkların kesişimini bulmak için kullanılır.

## Tepki süresi ve kısa pencere karşılaştırması

İlk referans koşulu mevcut ayarlardır: sample_duration 200 ms, update_interval 2 s, K=24.22. Daha kısa sample_duration değerleri sonraki kontrollü alt deneyde (ör. 150 ms ve 100 ms) değerlendirilebilir; kesin sıra henüz kararlaştırılmadı.

Karşılaştırmada mümkün olduğunca aynı yük ve fiziksel düzen korunur; yalnız sample_duration değiştirilir. update_interval, K, yük ve diğer firmware ayarları sabit tutulur. Ölçüm dağılımı, pencere ortalaması, geçiş algılama gecikmesi ve tekrarlanabilirlik karşılaştırılır. Daha hızlı fakat daha gürültülü veya sistematik olarak farklı sonuç veren ayar başarılı sayılmaz. Firmware değişikliği/OTA kullanıcı onayı ve kontrollü test olmadan yapılmaz.

## Kabul ve karar soruları

- SCT1 ON döneminde tekrarlanabilir kararlı alanlar üretiyor mu? OFF kararlılığı eğitim kabul ölçütü değildir.
- Kararlı alan başlangıcı/bitişi istatistiksel olarak belirlenebilir mi?
- SCT1 kararlı alanı PZEM kararlı alanıyla yeterli zaman örtüşmesi gösteriyor mu?
- Tam ON/OFF olay paketleri ON kararlı alanlarını doğru sınırlandırıyor mu? Eğitim adayı yalnız ON kararlı SCT/PZEM örtüşmesinden mi oluşuyor?
- 20:12 kablo değişikliği öncesi/sonrası ölçülebilir fark var mı?
- SCT'nin olaydan sonra kararlı alana ulaşma süresi nedir?
- Daha kısa örnekleme penceresi denenmeye değer mi?

## Açık işler

- [ ] 20:07–20:37 Modül 2 ve Modül 3 tam loglarını al.
- [ ] 20:12 öncesi/sonrası SCT1 karşılaştırmasını yap.
- [ ] Her ON/OFF çevriminde tam olay paketi ve olay alımını kontrol et; OFF yalnız paket kapatma için kullanılsın.
- [ ] Eğitim adaylarının yalnız ON içindeki bağımsız SCT/PZEM kararlı alan kesişimlerinden oluştuğunu doğrula.
- [ ] OFF/yüksüz taban istatistiğini ilk aşama dışında, ayrı ve isteğe bağlı yüksüz uzun kayıt çalışması olarak tut.
- [ ] SCT1 kararlı alan adaylarını ortalama, dağılım ve ardışık pencere değişimiyle çıkar.
- [ ] PZEM kararlı alanlarını bağımsız çıkar ve zaman kesişimini hesapla.
- [ ] İlk ön değerlendirme raporunu oluştur; eşikleri kanıta göre belirle.
- [ ] Kısa sample_duration karşılaştırmasını ayrı kontrollü alt deney olarak planla/uygula.

**Uygulama durumu:** Python algoritması henüz yazılmadı. Bu belge deney tasarımıdır. Firmware/YAML değişikliği, derleme veya OTA bu kayıtla yapılmadı. E12 tamamlandı sayılmaz.

## İlgili kararlar
- [ADR-024 — Python ON/OFF paket bütünlüğü](../../docs/decisions/ADR-024-python-packet-completeness-validation.md)
- [ADR-025 — ham kayıtta model davranışı değerlendirmesi](../../docs/decisions/ADR-025-raw-data-sct-model-behavior-validation.md)
- [Python veri hattı mimarisi](../../docs/architecture/python-program-architecture.md)
