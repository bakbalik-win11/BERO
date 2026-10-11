# GRV-005-05 — MATH SELF TEST v01 sonuç kaydı

- Tarih: 2026-10-11
- Derleme: **PASS** (kullanıcı bildirimi)
- Boot: **PASS** (paylaşılan ESP32D1OTA logunda normal açılış ve Safe Mode başarılı mesajı görülüyor)
- Self-test logları: **NOT OBSERVED**
- Matematik doğrulaması: **NOT VERIFIED**
- Cihaza yükleme: Kullanıcının önceki beyanına göre self-test yüklenmedi; paylaşılan logda self-test sürümünün yüklendiğini kanıtlayan bilgi yok.

## Beklenen fakat görülmeyen çıktı

```text
===== MATH SELF TEST =====
sample_count=4
adc_mean=...
adc_std=...
adc_rms_raw=...
adc_rms_ac=...
RESULT=PASS
```

Beklenen `[I][grv005_math]:` bloğu paylaşılan logda görünmüyor.

## Kanıtın sınırları

Paylaşılan ESP32D1OTA kaydı mevcut cihaz yazılımının başlatıldığını, Wi-Fi ve API bağlantılarının kurulduğunu, Safe Mode'un başarılı açılışı kaydettiğini ve daha sonra Wi-Fi roam scan başladığını gösteriyor. Bu kayıt, matematik self-test fonksiyonunun çalıştığını veya çalışmadığını tek başına kanıtlamaz.

Olasılıklar:
1. Self-test çalışmış, ancak log satırları bağlantı kurulmadan önce oluştuğu için gözlenmemiş olabilir.
2. Self-test çağrısı gerçekleşmemiş olabilir.
3. Matematik işlemlerinde beklenmeyen durum olabilir; mevcut logda bunu doğrulayan bir hata yoktur.

Bunlar henüz ayrıştırılmamıştır. `sqrtf`, `fabsf` veya `NAN` kaynaklı hata olduğu sonucuna varılmamıştır.

## Sonraki adım

Matematik formüllerini değiştirmeden önce self-test çıktısının görünürlüğünü ve çağrılma durumunu doğrula. Sonraki testte:
- `grv005_math` için log seviyesinin INFO veya daha ayrıntılı olduğundan emin ol.
- Self-test çalıştığında belirgin başlangıç ve bitiş kayıtları üret.
- Çıktıyı boot sonrasında tekrarlanabilir biçimde gözleyebilecek bir tetikleme veya gecikmeli test düzeni kullan.
- Test çıktısı görülmeden matematik doğrulamasını PASS sayma.

## Geçmişi koruma

Bu kayıt yalnızca mevcut kanıt durumunu belgelendirir. Önceki deneyler, yapılandırmalar ve kodlar değiştirilmez.
