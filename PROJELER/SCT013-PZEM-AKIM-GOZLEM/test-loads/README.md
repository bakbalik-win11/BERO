# Test Yükleri ve Karşılaştırmalı Ölçüm Kayıtları

Bu bölüm, aynı fiziksel test yüküyle farklı ESP kartı, modül, SCT kanalı, firmware ve ölçüm yöntemi kullanılarak alınan sonuçları bir arada izlemek için açılmıştır.

## Kayıt düzeni

- Her fiziksel yük/senaryo için ayrı klasör ve ana kayıt dosyası oluşturulur.
- Her test oturumu için kullanılan firmware'in tam sürümü, kod bağlantısı ve mümkünse commit SHA'sı kaydedilir.
- Log, test tarih/saat aralığı, zaman dilimi, ilgili satırlar veya kayıt dosyası bağlantısı ile birlikte tutulur.
- Aynı yük için farklı donanım veya kodla yapılan her ölçüm ana yük tablosuna yeni satır olarak eklenir; eski satırlar değiştirilmez.
- Referans cihaz, referans değeri ve kaynak türü (log, fotoğraf, kullanıcı bildirimi) açıkça yazılır.
- Sapma yalnız eşleşen yük ve zaman pencereleri için hesaplanır. Referans değeri yoksa sapma hesaplanmaz.
- ±%4 kabulü bir test sonucu olarak işaretlenir; yalnızca gerçek ve karşılaştırılabilir referans verisi varsa değerlendirilir.
- Kod, log veya zaman aralığı mevcut değilse hücreye “mevcut değil / doğrulanmadı” yazılır; tahmin üretilmez.

## Yük kayıtları

| Test yükü | Ana kayıt |
|---|---|
| 100 W akkor ampul | [100 W akkor — karşılaştırmalı ölçüm tablosu](100w-incandescent/README.md) |
| 150 W akkor ampul | [150 W akkor — karşılaştırmalı ölçüm tablosu](150w-incandescent/README.md) |

## Her ölçüm satırında tutulacak alanlar

1. Test ID ve tarih.
2. Başlangıç/bitiş saati ve log içindeki gerçek ölçüm aralığı.
3. Test yükü ve fiziksel koşul.
4. ESP/kart/modül ve SCT kanalı/GPIO.
5. Firmware dosyası, sürüm/commit ve kod bağlantısı.
6. Log dosyası bağlantısı ve log kaynağının niteliği.
7. Referans cihaz/değer ve kaynak türü.
8. Kodun kararlı bölüm sonucu (ör. ortalama, aralık, örnek sayısı).
9. Mutlak fark ve yüzde sapma.
10. ±%4 değerlendirmesi, teknik yorum ve açık kanıt eksikleri.

## Kanıt sınıfları

- **LOG:** Paylaşılan cihaz logundan doğrudan çıkarılmış veri.
- **KULLANICI BİLDİRİMİ:** Kullanıcının bildirdiği referans veya fiziksel test koşulu.
- **KOD KAYDI:** Depodaki firmware dosyası; tek başına çalıştığını kanıtlamaz.
- **HESAP:** Kaydedilmiş sayısal verilerden hesaplanan sonuç.
- **EKSİK KANIT:** İlgili ham log, zaman aralığı veya tam firmware sürümü mevcut değil.


## 2026-10-31 — LOAD-150W-001 sonucu

- 150 W akkor / ESP32D1 Modül 2 / SCT-1 GPIO32 / harici masaüstü besleme oturumu analiz edildi.
- UNIT kullanıcı bildirimleri 0,598 A ve 0,599 A; geçici ortalama 0,5985 A. ±%4 bandı 0,57456–0,62244 A.
- Uzun log 391 akım yayını içeriyor: ortalama 0,60821 A, medyan 0,608 A; ortalama sapma +%1,62; 388/391 (%99,23) yayın UNIT ±%4 bandında.
- PZEM bu logda yoktur; UNIT karşılaştırması PZEM doğrulaması olarak sunulmaz. K=24.22 değiştirilmedi.
- [150 W karşılaştırma kaydı](150w-incandescent/README.md); [uzun log analizi](../logs/module2/2026-10-31-load-150w-001-sct1-long-analysis.md).
- Ham kaynak dosya adı/boyutu/SHA-256 analizde tanımlandı; ham metnin GitHub'a tam aktarımı açık arşiv işidir.

## Test referans sırası kararı

Her test yükü için önce o yüke ait UNIT ölçümü alınır ve SCT sonucu bu UNIT değeriyle karşılaştırılır. PZEM sonraki aşamada eklenir. UNIT ve PZEM değerleri birbirinin yerine yazılmaz.
