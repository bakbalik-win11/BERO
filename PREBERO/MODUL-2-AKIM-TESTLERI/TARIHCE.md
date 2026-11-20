# Modül 2 – Masaüstü 4 Kanal / Akım Testleri – Tarihçe

Bu dosya modülün görevleri boyunca edinilen tecrübeyi ve gelişim sürecini kronolojik olarak kaydeder.

## Kayıt standardı

Her kayıt aşağıdaki bilgileri içermelidir:

- **Tarih:**
- **Görev kimliği:**
- **Çalışma / deneme:**
- **Gözlenen sonuç:**
- **Edinilen tecrübe:**
- **Teknik karar:**
- **İlgili kayıtlar:** YAML sürümü, LOG ve RAPOR yolları

Başarısız, sonuçsuz veya henüz doğrulanmamış çalışmalar da kaydedilir. Sonuçlar olduğundan başarılı veya doğrulanmış gösterilmez. **Tarihçe, test loglarının veya raporların kopyası değildir.** Log ve raporların ne gösterdiğini, bunlardan ne öğrenildiğini ve hangi teknik sonuca/karara ulaşıldığını özetler. Ham loglar ve ayrıntılı raporlar kendi sürüm klasörlerinde korunur; tarihçe ilgili kayıtlara referans verir.

---

## Kronolojik kayıtlar

### 2026-11-21 – MOD2-GRV001 – Masaüstü donanım düzeninin tanımlanması

- **Çalışma / deneme:** ESP32-D geliştirme kartı ve ESP32 shield üzerine kurulu masaüstü düzenin donanım kapsamı netleştirildi. SCT013 30A/1V akım sensörü ve ADS1115 ara ADC sinyal zincirine dahil edildi.
- **Gözlenen sonuç:** Kullanıcının paylaştığı fotoğrafta ESP32-D kartının shield üzerine takılı olduğu ve ADS1115 modülünün kablolarla düzeneğe bağlandığı görülüyor. SCT013 sensör fotoğrafta görünmüyor.
- **Edinilen tecrübe:** Fiziksel yerleşim fotoğrafla belgelenebilir; ancak fotoğraf tek başına ADS1115 pin eşleşmelerini, besleme değerlerini, analog giriş bağlantısını veya sistemin çalıştığını doğrulamaz.
- **Teknik karar:** Sinyal zinciri SCT013 30A/1V → ADS1115 → ESP32-D olarak kaydedildi. Gerçek pin eşleşmeleri ve elektriksel bağlantılar ayrı ayrı doğrulanmadan şema veya çalışan sistem olarak ilan edilmeyecek.
- **İlgili kayıtlar:** `PREBERO/MODUL-2-AKIM-TESTLERI/IMALAT/IMALAT.md`; `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/GOREV.md`.
