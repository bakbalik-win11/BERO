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
