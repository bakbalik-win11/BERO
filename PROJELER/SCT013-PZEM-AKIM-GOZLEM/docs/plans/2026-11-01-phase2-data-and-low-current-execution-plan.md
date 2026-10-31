# Faz 2 veri hattı ve düşük akım değerlendirmesi — uygulama planı

**Tarih:** 2026-11-01  
**Durum:** PLAN / görev sırasını değiştirmeyen uygulama notu  
**Ana kapsam:** Faz 2 — pratik yeniden kurulum ve sistem geliştirme  
**Aktif görev:** T010 — Modül 2 ESP32D1 üçlü SCT okuma modülü

## 1. Amaç

Mevcut SCT013 + ESPHome `ct_clamp` ölçüm yolunu, gerçek donanım ve veriyle değerlendirmek. K=24.22 başlangıç ölçeğini korumak; düşük akımda gözlenen ayrışma sorununu ölçüm zinciri katmanlarına ayırmak; PZEM/SCT veri eşleştirmesini ancak gerekli düğümler gerçek veri üretince yürütmek.

Faz 1 tamamlandı. Faz 2 aktif. Bu plan yeni bir ana faz veya görev sırası değişikliği oluşturmaz.

## 2. Önce korunacak kararlar

- Çalışan `ct_clamp` yolu araştırma/planlama gerekçesiyle değiştirilmez.
- Mevcut cihaz kimlikleri, pinler, bağlantı düzeni ve firmware ayarları doğrulanmadan değiştirilmez.
- K=24.22 başlangıç değeri olarak korunur; yeni katsayı ancak eşleşmiş veriyle gerekçelendirilir.
- E10 protokolündeki 200 → 500 → 1000 → 200 ms deney sırası, yalnız T010 kapsamında ve kendi kabul koşullarıyla uygulanır.
- PZEM proje referansıdır; kusursuz ground truth sayılmaz.
- Sürekli ham ADC dalga arşivi varsayılan hedef değildir. Gerekli HA tarihçesi ve pencere özellikleriyle sınırlı, tekrar işlenebilir veri dışa aktarımı hedeflenir.
- Deney, fiziksel çalışma veya derleme yapılmadan sonuç tamamlandı olarak işaretlenmez.

## 3. Planın önceki metinden düzeltilen noktaları

1. **T007, T008 ve T006 hemen başlatılmayacak.** Proje AGENTS.md ve ROADMAP.md, T010 modül devreye alma işini öncelemektedir. PZEM/SCT veri hattı alt aşaması, gerekli modüller çalışır veri ürettiğinde T007 → T008 → T006 sırasıyla başlayacaktır.
2. **0,4 A fiziksel alt sınır değildir.** Hipotez sicilinde H17 olarak kanıtsızdır. Bu değer güvenilirlik gözlemi/inceleme bölgesi olarak ele alınabilir; sensörün üretici sınırı veya kesin başarısızlık eşiği değildir.
3. **0,35 A filtresi güncel Modül 2'ye atfedilmeyecek.** Depodaki düşük akım teknik incelemesi bu eşiği eski E00F / ESP32D2 yapılandırmasında belgeliyor. Güncel ESP32D1 Modül 2 firmware'inde aynı eşik bulunduğu doğrulanmış değildir.
4. **Düşük akımın nedeni kesinleşmiş değildir.** SNR/taban değişkenliği, bias hareketi, ADC gerilim çözünürlüğü/kalibrasyon basamağı, `last_value` ile aynı kodların istatistik dışında kalması ve sayısal varyans hesabı olası etkenlerdir. Hangi etkinin baskın olduğu BERO ölçümüyle ayrıştırılmalıdır.
5. **Tek veya bölgesel katsayı kararı peşinen verilmeyecek.** Önce eşleşmiş kararlı pencerelerden tek K'nın davranışı analiz edilir. Bölgesel/doğrusal olmayan model ancak veri tekrarlanabilir bölgesel sapma gösterirse değerlendirilir.

## 4. Uygulama aşamaları ve geçiş kapıları

### Aşama 0 — T010 pratik modül devreye alma (şu an aktif)

**Amaç:** ESP32D1 Modül 2'nin üç SCT kanalı ve ortak bias ölçüm yolunu gerçek donanımda kontrollü şekilde doğrulamak.

**İş sırası:**
- Mevcut YAML ve cihaz kimliğini çalışma öncesi yeniden oku.
- GPIO32/SCT-1, GPIO33/SCT-2, GPIO34/SCT-3, GPIO35/ortak bias bağlantılarını gerçek kartta/terminal güzergâhında teyit et.
- Aynı referans yükle kanalları önce tek tek karşılaştır; her testte yük ve bağlantı koşulunu koru.
- Tekil testlerden sonra, ancak ihtiyaç varsa tek kanal ve çoklu kanal çalışma davranışını karşılaştır.
- Her koşulda ham log, zaman, yük durumu, Raw AC, yayınlanan akım, kabul edilmiş farklı örnek sayısı/SPS ve bias gözlemlerini kaydet.
- `last_value` filtresini kanıt olmadan kaldırma/değiştirme.

**Kabul kapısı:** Üç kanalın pin/bağlantı durumu ve temel okuma davranışı gerçek loglarla belgelenmeli; gerekli derleme/cihaz doğrulamaları tamamlanmalı; kalan belirsizlikler açıkça yazılmalı. T010 mevcut görev kabul ölçütleri sağlanmadan kapatılmaz.

### Aşama 1 — E10 pencere süresi gözlemi (T010 altındaki planlı deney)

**Durum:** PLANLANDI.  
**Düzenek:** E10 README'deki sabitler ve aynı BREAD-TOASTER-001 yükü.  
**Sıra:** 200 ms başlangıç kontrolü → 500 ms → 1000 ms → 200 ms geri dönüş.  
**Tek değişken:** `sample_duration`.

Her aşamada akım, Raw AC RMS, kabul edilmiş farklı örnek sayısı/SPS, bias, yayın aralığı ve yük olayları kaydedilir. CV düşmesi tek başına başarı veya doğruluk değildir. E10 kalibrasyon deneyi değildir; K=24.22 değiştirilmez.

T010'un modül kabulünü engellemeyen bir pencere-deneyi alt işi olarak ele alınır; ana görev sırasını değiştirmez.

### Aşama 2 — T007: Home Assistant → PC veri aktarımı

**Başlama koşulu:** İlgili PZEM ve SCT düğümleri kullanılabilir, gerçek veri üretiyor olmalı. T010 ve ilgili modül devreye alma engelleri çözülmeden T007 ana aktif görev yapılmaz.

**Hedef:** Tekrar işlenebilir bir HA geçmişi dışa aktarımı oluşturmak.

**Veri alanları:**
- Kaynak entity_id
- Ham state ve birim
- Kaynak timestamp ve timezone
- Varsa attributes ve geçerlilik bilgisi
- Dışa aktarım zamanı/yöntemi ve dosya biçimi

Ham kaynak kaydı silinmez veya normalize edilerek üzerine yazılmaz. Sürekli ham ADC edinimi başlatılmaz; HA'da zaten mevcut tarihçe ve sensör durum kayıtları kullanılır.

**Kabul:** En az bir gerçek örnek dışa aktarım dosyası, şema/alan incelemesi, timestamp/timezone doğrulaması ve yeniden çalıştırılabilir aktarım yöntemi kaydedilmelidir.

### Aşama 3 — T008: kararlı pencereler ve eşleştirme

**Girdi:** T007 ile alınmış gerçek PZEM ve SCT zaman serileri.

**Yöntem:**
- PZEM ve SCT kararlılığı ayrı değerlendirilir.
- Geçiş, termostat/motor döngüsü, timeout, NaN, -1.0 ve parse hataları görünür şekilde işaretlenir; ham kayıt korunur.
- Yalnız zaman bakımından örtüşen kararlı pencereler eşleştirilir.
- PZEM değeri, eşleşen SCT penceresinin proje etiketi/referansı olur; mutlak gerçek değer olduğu iddia edilmez.
- Eşleştirme yöntemi, tolerans ve pencere eşikleri gerçek örneğin güncelleme/timestamp davranışı görüldükten sonra belirlenir; önceden keyfî sabitlenmez.

**Kabul:** Kaynak zaman bilgileri korunmuş, pencere başlangıç/bitişleri ve eşleştirme gerekçesi gösterilebilir, tekrar üretilebilir bir etiketli veri kümesi.

### Aşama 4 — T006: K=24.22 ve model değerlendirmesi

**Girdi:** T008 tarafından üretilmiş eşleşmiş, kararlı ve geçerli örnekler.

**Analiz:**
- SCT akımı ile eşleşen PZEM akımı için mutlak ve yüzde sapma.
- Düşük/orta/yüksek akım bölgeleri; sınırlar ancak veri dağılımı görüldükten sonra seçilir.
- Yük, kanal ve tekrar etkileri ayrı tutulur.
- Tek K=24.22 modelinin artık/hata davranışı incelenir.
- Bölgesel doğrusal model yalnız yeterli tekrar ve bağımsız doğrulama örnekleri mevcutsa aday olur.
- Eğitim ve değerlendirme verisi aynı örneklerin yeniden kullanılmasıyla iyimserleştirilmez; mümkünse yük/oturum bazında ayrım yapılır.
- Her onaylı model sürümü gerçek `calibration_id` ile kaydedilir.

**Kabul:** Model kararı; veri kapsamı, hata dağılımı, tekrar sayısı ve sınırlamalarla birlikte raporlanmış olmalı. K değişikliği otomatik değildir.

### Aşama 5 — Düşük akım analizi (T010 ölçüm hazırlığı; T007/T008 verisiyle genişletme)

**Hedef:** Yaklaşık 0.4 A ve altındaki davranışı tek bir “başarısızlık eşiği” varsaymadan karakterize etmek.

**Ayrı tutulacak koşullar:**
- Yüksüz / CT bağlı fakat primer akımsız taban
- Çok düşük akım
- Düşük akım
- Orta akım kontrolü

Her koşulda aynı firmware ve mümkün olduğunca aynı fiziksel düzen korunur. Pencere bazında Raw AC RMS, kabul edilmiş farklı örnek sayısı, raporlanan SPS, bias ve yayınlanan akım kaydedilir. Referans cihaz değeri varsa cihaz ve okuma zamanı not edilir; yalnız eşzamanlı ve kararlı ise karşılaştırma yapılır.

**Araştırma soruları:**
- Yük açık Raw AC dağılımı yüksüz tabandan istatistiksel olarak ayrılıyor mu?
- Bias hareketi/dağılımı ölçüm varyansıyla birlikte değişiyor mu?
- Kabul edilmiş örnek sayısı ve tekrar kodlarının oranı sinyal genliğiyle nasıl değişiyor?
- Kalibre ADC gerilim basamağı/ölçek davranışı, ham ölçüm veya üretici dokümanıyla doğrulanabiliyor mu?
- Eski E00F 0.35 A filtresi ile güncel Modül 2 kodu birbirinden doğru ayrılmış mı?

Bu aşamada eşik, katsayı, pin veya algoritma değişikliği yapılmaz. Önce mevcut konfigürasyonla veri toplanır. Daha ileri dedup/RAW karşılaştırması ancak gözlemler somut bir belirsizliği işaret ederse ayrı ve kontrollü deney olarak planlanır.

**Kabul:** Yüksüz ve yük koşulları için pencere dağılımları ve örtüşme/ayrışma bulgusu, kullanılan gerçek konfigürasyonla birlikte raporlanır. Ölçülemeyen ya da ayrışmayan koşullar “bu düzenekte gösterilemedi” diye raporlanır; fiziksel imkânsızlık sonucu çıkarılmaz.

## 5. Çalışma kayıt standardı

Her anlamlı veri/deney kaydı en az şunları içerir:
- Deney/test kimliği, tarih, timezone
- Cihaz/ESPHome/firmware sürümü ve YAML hash'i
- SCT kanalı, GPIO, bias ve fiziksel bağlantı durumu
- Yük tipi ve açık/kapalı/kararlı/geçiş durumu
- Pencere zamanı; yoksa zaman bilgisinin bulunmadığı açıkça belirtilir
- Raw AC RMS (V), yayınlanan SCT akımı (A)
- Kabul edilmiş farklı örnek sayısı ve raporlanan SPS (gerçek ADC dönüşüm hızı diye adlandırılmaz)
- Bias ölçümü
- Varsa PZEM/pens değeri, kaynak entity/cihaz, birim ve okuma zamanı
- Hariç tutulan pencereler ve gerekçeleri
- Yorum, kanıt seviyesi ve sınırlamalar
- Gerçek calibration_id varsa değeri; yoksa uydurulmaz

“Veri doğru değilse kaydetmeye gerek yok” yaklaşımı kullanılmaz. Ham kaynak korunur; geçersiz, şüpheli veya eşleşmeyen kayıtlar silinmek yerine etiketlenir ve eğitimden ayrılır.

## 6. Bu planın dışladıkları

- Bu belge 0.4 A fiziksel alt sınır belirlemez.
- Eski E00F 0.35 A filtresinin güncel Modül 2'de bulunduğunu iddia etmez.
- Bölgesel katsayı/model seçimini önceden onaylamaz.
- Sürekli ham ADC/50 Hz dalga kaydını yeniden proje hedefi yapmaz.
- T010 tamamlanmadan T007/T008/T006'yı aktif görev sırasına almaz.
- Yeni firmware, YAML, kalibrasyon, OTA veya fiziksel test yapıldığını göstermez.

## 7. Kaynak kayıtlar

- [AGENTS.md](../../AGENTS.md)
- [ROADMAP.md](../../ROADMAP.md)
- [T010 — Modül 2](../../tasks/T010-module2-triple-sct-bringup.md)
- [T007/T008/T006 açık soruları](../open-questions.md)
- [Düşük akım teknik değerlendirmesi](../technical-reviews/2026-10-30-e00f-low-current-cumulative-review.md)
- [ct_clamp hipotez sicili](../research/ct-clamp/2026-10-31-hypothesis-register-and-next-experiments.md)
- [E10 protokolü](../../experiments/E10-ct-clamp-window-duration/README.md)
