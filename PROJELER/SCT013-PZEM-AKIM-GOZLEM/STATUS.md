# Proje durumu

**Son güncelleme:** 2026-10-27  
**Aktif faz:** Faz 0 — hazırlık ve güvenlik  
**Aktif görev:** [T001 — Fiziksel donanım envanteri](tasks/T001-hardware-inventory.md)  
**Donanım referansları:** [SCT/PZEM referans kopyaları](hardware/references/README.md) proje klasörüne alındı; kaynak `DONANIM/` belgeleri korunuyor.  
**Deney durumu:** YAPILMADI  
**Çalışma protokolü:** SESSION_PROTOCOL.md ve [gün sonu kontrol listesi](GUN_SONU_KONTROLU.md) main dalında. PR #2 ve PR #3 birleştirildi; [otomatik kapanış kontrolü başarılı](https://github.com/bakbalik-win11/BERO/actions/runs/40234658507). İlk tarihli günlük girdisindeki 'PR #2 birleştirilmedi' cümlesi artık güncel değildir; en yeni günlük düzeltmesine bakın.

## Mevcut bilgi
- BERO'da [SCT013-100A-1V](../../DONANIM/SCT013-100A-1V/README.md), [SCT013-30A-1V](../../DONANIM/SCT013-30A-1V/README.md), [PZEM-004T V3.0](../../DONANIM/PZEM-004T/README.md), ESP32-WROOM-32D ve MCP3208 için önceden hazırlanmış donanım kayıtları vardır.
- SCT ve PZEM teknik Markdown belgelerinin kopyaları [hardware/references/](hardware/references/README.md) altında bulunur; genel teknik özellikler baştan yazılmayacaktır.
- Önceki kayıtlar tarihsel teknik açıklamalar ve test notlarıdır; yeni projedeki fiziksel konfigürasyonu, yeni deney veya kalibrasyon sonucunu tek başına doğrulamaz.
- Başlangıç ayarları: 2 kS/s, nominal 200 ms pencere, yaklaşık 1 s PZEM sorgusu.
- PZEM'in iç ölçüm penceresi ve bu modüldeki gecikmesi doğrulanmadı.

## Karar kapıları
- [ ] G1 — Faz 1 sonunda: SCT RMS kalibrasyonu önceden belirlenmiş hata hedefinde ve clipping yok.
- [ ] G2 — Faz 3 sonunda: PZEM okuma durumu izleniyor; geçersiz okumalar özetlerden dışlanıyor.
- [ ] G3 — Faz 6 sonunda: örnekleme hızı hedef yüklerde ölçülmüş metriklerle gerekçelendirilmiş.

## Sıradaki üç iş
1. [ ] [T001 — Donanım envanteri](tasks/T001-hardware-inventory.md): mevcut referans ve önceki kayıtları kullanarak seçilen SCT varyantını, PZEM 10 A/100 A varyantı ile CT'sini, mevcut MCU/ADC ve analog ön uç değerlerini proje için kaydet.
2. [ ] [T002 — Güvenlik kontrolü](tasks/T002-safety-checklist.md): şebeke bağlantısı öncesi yetkin kişi incelemesi.
3. [ ] [T003 — Referans ve hata hedefi](tasks/T003-reference-and-error-target.md): referans cihazı, en az üç yük seviyesi ve ölçüm öncesi kabul hedefi.

**Çalışma odağı:** Aynı anda yalnızca Aktif görev satırındaki görev üzerinde çalış. Yeni fikirler mevcut görevin kapsamını değiştirmesin.

## Açık engeller
- Bu projede hangi SCT varyantının kullanılacağı kayıtlı değil; iki modelin teknik kayıtları mevcuttur.
- PZEM için ortak V3.0 aile belgesi mevcuttur; bu projenin gerçek modülündeki 10 A/100 A varyantı ve CT modeli henüz kaydedilmedi.
- MCU/ADC, gerçek bias/VREF, burden/filtre ve kablolama ayrıntıları bu proje için doğrulanmadı.
- E01–E06 deneylerinin hiçbiri tamamlanmadı.

Firmware ve analiz uygulaması henüz eklenmedi. Deney/kalibrasyon sonuçları yapılmadı olarak kalır.
