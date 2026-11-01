# Python veri hattı mimarisi

**Faz:** Faz 2 — Bulunan kodu PZEM ile eğitmek  
**İlk görev:** [T007 — Home Assistant verisini PC'ye aktarma](../../tasks/T007-python-architecture.md)  
**Durum:** Taslak; gerçek HA dışa aktarımı görülünce somutlaştırılacak.

## Amaç

Home Assistant'ta kayıtlı PZEM-004T V3.0 referans akışı ile mevcut SCT ölçüm kodunun entity geçmişlerini PC'ye taşımak. Python tarafında önce kaynak veriyi koruyarak okumak; sonraki adımlarda PZEM ve SCT akışlarını BOOT_ID + EVENT_ID ile paketlemek, kararlılıklarını kendi ölçümlerinden bağımsız belirlemek ve eşleşen paket aralığında PZEM akımıyla SCT verisini etiketlemek.

## Veri akışının hedef sırası

1. **Alma:** HA geçmişini dışa aktar; kaynak dosyayı değiştirmeden sakla.
2. **İnceleme:** Dosya biçimi, entity_id, birim, timestamp, boşluk, tekrar ve geçersiz state dağılımını raporla.
3. **Hazırlama:** PZEM ve SCT kayıtlarını ayrı veri akışları olarak ayır; zaman damgalarını ve kaynak kökenini koru.
4. **Kararlılık:** Her akışın kararlı pencerelerini kendi güncelleme hızına ve gözlenen dağılımına göre belirle.
5. **Eşleştirme:** Aynı BOOT_ID + EVENT_ID paket aralığında iki tarafta da geçerli/kararlı bölge olup olmadığını değerlendir; timestamp kesişimi eşleştirme şartı değildir.
6. **Etiketleme:** Geçerli PZEM akımını eşleşen SCT penceresine referans etiketi olarak ekle.
7. **Öğrenme:** Önce K=24.22'yi değerlendir; veri desteklerse yeni katsayı/model sürümü üret.


## Kararlılık ve eşleştirme kuralı (ADR-022 / ADR-023 — geçerli)

**Önce paket kimliği, sonra bağımsız kararlılık analizi.** ADR-019 tarihsel kararındaki timestamp kesişimiyle iki sensör örneğini eşleştirme yaklaşımı ADR-022 ile geçersiz kılınmıştır. TIME alanı da ADR-023 ile olay protokolünden çıkarılmıştır.

1. Modül 3 PZEM akışı, kendi olay kayıtlarıyla; Modül 2 SCT akışı, aldığı aynı olay kayıtlarıyla kendi içinde sıralanır.
2. Her iki akış olay işaretleri arasındaki paket aralıklarına ayrılır.
3. Paket aralıkları yalnız BOOT_ID + EVENT_ID ile eşleştirilir. EVENT_ID tek başına benzersiz değildir.
4. PZEM kararlılığı yalnız PZEM değerlerinden; SCT kararlılığı yalnız SCT değerlerinden bağımsız tespit edilir.
5. Her iki tarafta geçerli ve karşılaştırılabilir kararlı bölge bulunmayan paket eğitim örneği üretmez. Geçiş/yerleşme bölümleri kararlı kabul edilmez.
6. İki modülün ölçüm örnekleri timestamp ile birebir eşleştirilmez; kararlı pencere başlangıç/bitiş timestamp kesişimi de paket eşleştirme şartı değildir.
7. Timestamp/timezone yalnızca aynı modül içindeki ölçüm ve olay kayıtlarının yerel sırasını kurmak, paket sınırlarını belirlemek ve kaynak izini korumak için kullanılır.
8. PZEM akımı geçerli paket aralığındaki SCT kararlı bölgesine proje referans etiketi olur; mutlak ground truth değildir.

Güncel olay biçimi: `BERO_EVT,BOOT_ID=<32 HEX>,EVENT_ID=N,STATE=ON|OFF`. TIME alanı yoktur. Ayrıntı: [ADR-022](../decisions/ADR-022-packet-marker-segmented-training-streams.md) ve [ADR-023](../decisions/ADR-023-event-identity-without-time.md).

## Şimdilik kesinleştirilmeyenler

- HA'dan PC'ye aktarım yöntemi (API, geçmiş dışa aktarımı veya dosya aktarımı).
- Gerçek entity_id listesi ve kullanılacak PZEM/SCT alanları.
- Kaynak export biçimi ve kayıt boyutu.
- Python dosya/modül sayısı ve çalıştırma biçimi.
- Kararlılık eşikleri, pencere süresi ve eşleştirme toleransı.
- Eğitim/ayrı doğrulama veri bölme yöntemi.

Bu kararlar gerçek HA örnek verisi görülmeden varsayılmayacak.

## Veri koruma kuralları

- Kaynak timestamp, timezone/offset, entity_id, state ve unit korunur.
- PZEM ve SCT güncelleme hızları aynı kabul edilmez; yapay zaman yuvarlama/senkronizasyon yapılmaz.
- -1.0, NaN, timeout ve parse hataları etiketlemeden çıkarılır; ham kaynak kayıt silinmez.
- Sıfır değerler doğrulanmadan otomatik silinmez.
- Her etiketli SCT pencere kaydında gerçek calibration_id bulunur; yoksa uydurulmaz.
- Kaynak dosya hash'i, analiz kodu sürümü ve dışlama özeti sonuçla birlikte saklanır.

## Parçalar ve ilerleme

| ID | Parça | Durum | Görev |
|---|---|---|---|
| PY-01 | HA geçmişini PC'ye alma | BEKLEMEDE | T007 |
| PY-02 | PZEM/SCT kaynak akışlarını inceleme | BEKLEMEDE | T007 |
| PY-03 | Ayrı kararlılık pencereleri | BEKLEMEDE | T008 |
| PY-04 | Ortak pencere eşleştirme ve etiketleme | BEKLEMEDE | T008 |
| PY-05 | K=24.22 ve model değerlendirme | BEKLEMEDE | T006 |

## İlk teslimat

İlk olarak küçük bir gerçek HA export örneği PC'ye alınır. Python kodu bu dosyayı okur ve entity, satır, zaman aralığı, birim ve geçersiz değer özetini üretir. Kod, gerçek örnek çıktı/log ve yorum depoya eklenmeden T007 tamamlanmış sayılmaz.

Bu belge hedef mimariyi tanımlar; aktarımın veya Python uygulamasının hazır/çalışır olduğunu iddia etmez.


## Tarihsel ADR-019 notu — güncel uygulamada geçerli değildir

ADR-019 ilk tasarım aşamasında iki akışın timestamp bakımından örtüşen kararlı pencerelerini eşleştirmeyi tarif ediyordu. Bu yaklaşım [ADR-022](../decisions/ADR-022-packet-marker-segmented-training-streams.md) ile paket kimliği önceliğine dönüştürüldü; olay mesajındaki TIME alanı da [ADR-023](../decisions/ADR-023-event-identity-without-time.md) ile kaldırıldı.

Bu nedenle bu mimari belgede geçerli tek yöntem yukarıdaki ADR-022/023 bölümüdür: önce akışları BOOT_ID + EVENT_ID ile paketle, sonra her akışta kararlılığı bağımsız belirle. Timestamp iki modülün örneklerini eşleştirmez. ADR-019 yalnız karar tarihçesi olarak korunur.


## Paket bütünlüğü ve eksik ON/OFF işaretleri (ADR-024 — geçerli karar)

Paketleme her ölçüm akışında bağımsız yapılır:

- Modül 3 PZEM akışı yalnız Modül 3'ün kendi olay kayıtlarıyla; Modül 2 SCT akışı yalnız Modül 2'nin aldığı olay kayıtlarıyla bölümlenir.
- Her akışta ON başlangıcı ve onu izleyen OFF bitişi bulunan aralık tamamlanmış paket adayıdır. Eksik başlangıç/bitiş veya tutarsız olay kimliği/sırası varsa aralık tamamlanmış kabul edilmez.
- Yeni ON, önceki paket kapanmadan gelirse önceki açık aralık eksik/bozuk olarak işaretlenir; yeni ON yeni paket adayı başlatır. BOOT_ID değişiminde açık kalan önceki boot aralığı tamamlanmamış kapatılır.
- EVENT_ID boşlukları, tekrarlar ve beklenmeyen STATE sırası ayrıca raporlanır. Tanı kodları: INCOMPLETE_EVENT, MISSING_ON, MISSING_OFF, EVENT_ID_GAP, DUPLICATE_EVENT, STATE_ORDER_ERROR, BOOT_CHANGED_WITH_OPEN_PACKET.
- İki akışın paketleri yalnız BOOT_ID + EVENT_ID ile eşleştirilir. Her iki tarafta aynı paket aralığı doğrulanmadan eğitim örneği oluşturulmaz. Tek taraftaki tam paket, diğer taraftaki eksik aralığı geçerli yapmaz.
- ON/OFF sınırlarının varlığı kararlılık kanıtı değildir; PZEM ve SCT kararlılığı kendi ölçüm değerlerinden bağımsız belirlenir.

Mevcut Modül 3 → UDP 4210 → Modül 2 aktarımı korunur. Bu karar UDP'yi kaldırmaz, yeni HA helper/merkezi HA mimarisi kurmaz ve olay mesajına TIME alanı eklemez. Güncel protokol ADR-023'teki TIME'sız biçimdir.

**Uygulama durumu:** Bu bölüm kabul kuralıdır. Python kodu, gerçek HA export testi ve örnek çıktı henüz mevcut değildir. Ayrıntı: [ADR-024](../decisions/ADR-024-python-packet-completeness-validation.md).


## Tam ham kayıtta öğrenilmiş SCT modelinin değerlendirilmesi (ADR-025)

Eğitim için PZEM ve SCT akışlarının kendi içlerinde kararlı bulunan uygun alanları eşleştirilir; PZEM bu aşamada proje referansıdır. Eğitim alanları seçilse bile deneyin ham kaydının tamamı korunur. Açılma, kapanma ve geçiş bölgeleri de öğrenilmiş katsayı/model ile ayrıca incelenir.

Tam kayıt değerlendirmesinde Python'a deneyin bilinen ON/OFF koşulu ve yük aralığı verilir (örneğin OFF=0 A, ON yaklaşık 1 A). SCT'nin OFF tabanı, ON seviyesi, geçiş davranışı ve bilinen aralıkla tutarlılığı değerlendirilir. PZEM'in geçişteki ardışık okumaları SCT'nin her örneği için noktasal doğruluk referansı yapılmaz; bu değerlerle tam kayıt üzerinde hata puanı üretilmez. Bilinmeyen ara geçiş akımları uydurulmaz. Sonuç, bilinen deney koşullarına göre SCT davranış/tutarlılık değerlendirmesidir; bağımsız örnek referansı olmadan mutlak doğruluk testi değildir.

Tek katsayı veya Python'ın veriden seçeceği alan bazlı katsayılar ve alan sınırları henüz belirlenmemiştir. Algoritma, en küçük kareler yöntemi ve kabul eşiği bu ADR ile seçilmez. Ayrı SCT üzerinde eğitilmiş modeli çalıştıracak olası Modül 4 fikri ayrı bir gelecek önerisidir.

Ayrıntı: [ADR-025](../decisions/ADR-025-raw-data-sct-model-behavior-validation.md). Python uygulaması ve gerçek ham kayıt çıktısı henüz yoktur.
