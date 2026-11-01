# Python veri hattı mimarisi

**Faz:** Faz 2 — Bulunan kodu PZEM ile eğitmek  
**İlk görev:** [T007 — Home Assistant verisini PC'ye aktarma](../../tasks/T007-python-architecture.md)  
**Durum:** Taslak; gerçek HA dışa aktarımı görülünce somutlaştırılacak.

## Amaç

Home Assistant'ta kayıtlı PZEM-004T V3.0 referans akışı ile mevcut SCT ölçüm kodunun entity geçmişlerini PC'ye taşımak. Python tarafında önce kaynak veriyi koruyarak okumak; sonraki adımlarda PZEM ve SCT kararlı alanlarını ayrı bulmak, örtüşen alanları eşleştirmek ve PZEM akımıyla SCT kayıtlarını etiketlemek.

## Veri akışının hedef sırası

1. **Alma:** HA geçmişini dışa aktar; kaynak dosyayı değiştirmeden sakla.
2. **İnceleme:** Dosya biçimi, entity_id, birim, timestamp, boşluk, tekrar ve geçersiz state dağılımını raporla.
3. **Hazırlama:** PZEM ve SCT kayıtlarını ayrı veri akışları olarak ayır; zaman damgalarını ve kaynak kökenini koru.
4. **Kararlılık:** Her akışın kararlı pencerelerini kendi güncelleme hızına ve gözlenen dağılımına göre belirle.
5. **Eşleştirme:** Aynı olay içindeki örtüşen kararlı pencereleri bul.
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


## 2026-11-01 — Modül 2/3 olay akışı ve bağımsız kayıt kararı (ADR-019)

Modül 2 ve Modül 3 kayıtları ESP/HA katmanında ölçüm ve olay olarak ayrı tutulur. Python bunları sonradan zaman ve olay bilgisiyle ilişkilendirir.

### Modül 2 kaynakları
- **SCT ölçüm akışı:** Modül 2'nin mevcut SCT okuma sistemi.
- **UDP olay akışı:** Modül 3'ten gelen paket kimliği (varsa BOOT_ID/EVENT_ID), kaynak saat bilgisi ve SSR ON/OFF durumu.
- İki akış HA'ya ayrı kayıtlar olarak gider. UDP olayı SCT ölçümüne zorunlu biçimde bağlanmaz.

### Modül 3 kaynakları
- **UDP yayın akışı:** Paket/BOOT_ID/EVENT_ID, saat ve SSR ON/OFF olayları.
- **HA ölçüm akışı:** Modül 3'ün PZEM ölçümleri.
- **HA olay akışı:** Modül 3'ün yayınladığı/aldığı aradaki olay bilgileri.
- PZEM ve olay bilgileri HA'da ayrı kayıtlar olarak tutulur; UDP yayın düzeni bu kararla değiştirilmez.

### Python'ın kararlı alan eğitimindeki rolü
1. HA'dan SCT, PZEM ve olay kayıtlarını ayrı akışlar olarak alır.
2. Kaynak timestamp/timezone, entity_id, birim, ham state ve varsa BOOT_ID/EVENT_ID korunur.
3. Olay kayıtlarından ON/OFF ve geçiş zaman çizgisi oluşturulur.
4. PZEM ve SCT kararlılığı ayrı hesaplanır.
5. Olay/zaman bilgisi kararlı alanların sınırlarını ve yük durumunu yorumlamak için kullanılır.
6. Yalnız zaman bakımından örtüşen, kendi akışında kararlı PZEM/SCT pencereleri eşleştirilir; PZEM eşleşen SCT penceresine proje referans etiketi olur.

Bu tasarımda ölçüm ile olay arasında ESP/HA katmanında birebir eşleştirme şartı yoktur. Eşleştirme Python'da sonradan yapılır. Pencere süresi, kararlılık eşikleri ve zaman toleransı gerçek HA verisi incelenmeden sabitlenmez.

Ayrıntı: [ADR-019](../decisions/ADR-019-module2-module3-independent-event-streams.md).
