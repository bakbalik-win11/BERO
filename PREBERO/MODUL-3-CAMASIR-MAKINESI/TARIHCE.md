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


## 2026-11-22 – MOD3-AKM001: V1.6 uzun pamuklu program saha testi kapatıldı

- **Çalışma:** ESP32D2/SCT013 V1.6 koduyla çamaşır makinesinin uzun pamuklu programı baştan sona kaydedildi; yaklaşık 78 dakikalık CSV elde edildi.
- **Gözlenen sonuç:** Isıtma bloğunda PZEM akımıyla yakın takip; ısıtma sonrası düşük akım/motor çalışma bölümlerinde ESP32D2'nin daha yüksek okuma eğilimi görüldü. Ara sıkma rampaları ve final sıkma izi kayıtta seçilebildi.
- **Edinilen tecrübe:** V1.6 gerçek cihazda uzun program boyunca çalıştı. Çalışma koşuluna göre PZEM ile farkın yönü değişebiliyor; bu deney farkın PF kaynaklı olduğunu kanıtlamıyor.
- **Teknik karar:** Ana hedef yeni kodu gerçek makinede test etmekti; hedef yerine geldiği için MOD3-AKM001 kapatıldı. V1.6 değiştirilmedi. PF/ZMPT101B araştırması ayrı ve geleceğe dönük; bu testin kapsamı değil. Ses/titreşim kanalları kullanılmadı.
- **İlgili kayıt:** `GOREVLER/MOD3-AKM001/RAPOR/MOD3-AKM001-V1.6-UZUN-PAMUKLU-SAHA-TESTI-2026-11-22.md`.


## 2026-11-22 – Modül 3/4 ortak zaman pencereli sensör mimarisi taslak olarak kaydedildi

- **Çalışma:** Akım (SCT013), ses (MAX4466) ve titreşim (MPU6050) verilerini ortak 1 saniyelik zaman slotlarında birleştirme fikri değerlendirildi.
- **Teknik karar:** Sensörler kendi uygun örnekleme hızlarında çalışacak; pencere bazlı özetler ortak zaman damgası/tick ile tek veri kaydında birleştirilecek. Örnek özellikler akım RMS, ses RMS/peak/ZCR ve üç eksenli titreşim RMS değerleridir.
- **Durum:** Taslak mimari; örnekleme hızları, ADC/pin planı, kaynak yükü, veri şeması ve aktarım henüz kesin değil. Fikirler netleşmeden Modül 3 imalatına geçilmeyecek.
- **İlgili kayıt:** `PREBERO/ORTAK-MIMARI/MODUL-3-4-ORTAK-ZAMAN-PENCERELI-VERI-TOPLAMA-MIMARISI.md`.
