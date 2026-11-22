# Modül 3 – Çamaşır Makinesi – Tarihçe

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

### 2026-11-22 – Modül 3 PZEM-only ESPHome kodu arşivlendi

- **Görev kimliği:** Henüz atanmadı.
- **Çalışma / deneme:** Sökülecek Modül 3'te kullanılan ESP32-WROOM + PZEM-004T V3.0 yapılandırması, kullanıcı tarafından sağlanan haliyle donanım arşivine kaydedildi.
- **Gözlenen sonuç:** Kodda PZEM ölçümlerini 5 saniye aralıkla Home Assistant'a yayınlayan altı sensör tanımı bulunuyor: gerilim, akım, güç, enerji, frekans ve güç faktörü. Aç/kapa kontrolü bulunmuyor.
- **Edinilen tecrübe:** PZEM ölçüm/yayın yapılandırması, modül söküldükten sonra da yeniden kullanılabilmesi için modül görev klasöründen bağımsız donanım kaydında tutulmalı.
- **Teknik karar:** Kod, aktif firmware değil eski modülden kalan arşiv örneği olarak saklanacak. Derleme ve fiziksel test başarısı bu kayıtla iddia edilmiyor.
- **İlgili kayıtlar:** `DONANIM/PZEM-004T/KOD/BERO-MODUL3-WROOM-PZEM-ONLY-ARSIV.yaml`; donanım açıklaması `DONANIM/PZEM-004T/README.md`.
