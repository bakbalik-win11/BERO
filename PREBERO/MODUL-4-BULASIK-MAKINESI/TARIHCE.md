# Modül 4 – Bulaşık Makinesi – Tarihçe

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

Henüz bu PREBERO çalışma düzeninde kayda alınmış modül geçmişi bulunmuyor. Yeni çalışmalar tamamlandıkça kayıtlar buraya eklenecek.


## 2026-11-22 – Modül 3/4 ortak zaman pencereli sensör mimarisi taslak olarak kaydedildi

- **Çalışma:** Akım (SCT013), ses (MAX4466) ve titreşim (MPU6050) verilerini ortak 1 saniyelik zaman slotlarında birleştirme fikri değerlendirildi.
- **Teknik karar:** Sensörler kendi uygun örnekleme hızlarında çalışacak; pencere bazlı özetler ortak zaman damgası/tick ile tek veri kaydında birleştirilecek. Örnek özellikler akım RMS, ses RMS/peak/ZCR ve üç eksenli titreşim RMS değerleridir.
- **Durum:** Taslak mimari; örnekleme hızları, ADC/pin planı, kaynak yükü, veri şeması ve aktarım henüz kesin değil. Fikirler netleşmeden Modül 4 imalatına geçilmeyecek.
- **İlgili kayıt:** `PREBERO/ORTAK-MIMARI/MODUL-3-4-ORTAK-ZAMAN-PENCERELI-VERI-TOPLAMA-MIMARISI.md`.
