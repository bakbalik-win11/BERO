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
| PY-01 | HA geçmişini PC'ye alma | AKTİF | T007 |
| PY-02 | PZEM/SCT kaynak akışlarını inceleme | BEKLEMEDE | T007 |
| PY-03 | Ayrı kararlılık pencereleri | BEKLEMEDE | T008 |
| PY-04 | Ortak pencere eşleştirme ve etiketleme | BEKLEMEDE | T008 |
| PY-05 | K=24.22 ve model değerlendirme | BEKLEMEDE | T006 |

## İlk teslimat

İlk olarak küçük bir gerçek HA export örneği PC'ye alınır. Python kodu bu dosyayı okur ve entity, satır, zaman aralığı, birim ve geçersiz değer özetini üretir. Kod, gerçek örnek çıktı/log ve yorum depoya eklenmeden T007 tamamlanmış sayılmaz.

Bu belge hedef mimariyi tanımlar; aktarımın veya Python uygulamasının hazır/çalışır olduğunu iddia etmez.
