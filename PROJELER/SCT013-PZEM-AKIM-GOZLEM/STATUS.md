# Proje durumu

**Son güncelleme:** 2026-10-27  
**Aktif faz:** Faz 0 — hazırlık ve güvenlik  
**Aktif görev:** [T001 — Fiziksel donanım envanteri](tasks/T001-hardware-inventory.md)  
**SCT önceliği:** SCT013-030 (30 A / 1 V) — kullanıcı kararı.  
**Stok bildirimi:** 7 adet SCT013-030; 10 adet SCT013-100A-1V; 10 adet 100 nF / 50 V seramik kondansatör. **Adetler kullanıcı bildirimidir; bağımsız sayım yapılmadı.**  
**Donanım referansları:** [SCT/PZEM referans kopyaları](hardware/references/README.md) proje klasörüne alındı; kaynak `DONANIM/` belgeleri korunuyor.  
**Son oturum kaydı:** [HISTORY/SESSION_LOG.md](HISTORY/SESSION_LOG.md), PR #8 aktarımı ve başarılı kapanış kontrolüyle güncellendi.  
**Deney durumu:** YAPILMADI  
**Çalışma protokolü:** SESSION_PROTOCOL.md ve [gün sonu kontrol listesi](GUN_SONU_KONTROLU.md) main dalında. PR #2 ve PR #3 birleştirildi; [otomatik kapanış kontrolü başarılı](https://github.com/bakbalik-win11/BERO/actions/runs/40234658507). İlk tarihli günlük girdisindeki 'PR #2 birleştirilmedi' cümlesi artık güncel değildir; en yeni günlük düzeltmesine bakın.

## Mevcut bilgi
- BERO'da [SCT013-100A-1V](../../DONANIM/SCT013-100A-1V/README.md), [SCT013-30A-1V](../../DONANIM/SCT013-30A-1V/README.md), [PZEM-004T V3.0](../../DONANIM/PZEM-004T/README.md), ESP32-WROOM-32D ve MCP3208 için önceden hazırlanmış donanım kayıtları vardır.
- SCT ve PZEM teknik Markdown belgelerinin kopyaları [hardware/references/](hardware/references/README.md) altında bulunur; genel teknik özellikler baştan yazılmayacaktır.
- Bu proje için öncelikli SCT varyantı SCT013-030 (30 A / 1 V) olarak belirlendi. SCT013-100A-1V alternatif stokta kalır; adetler kullanıcı bildirimi olarak kaydedildi.
- 100 nF / 50 V seramik kondansatörden 10 adet bulunduğu bildirildi. Bu stok bilgisi kondansatörün belirli bir devre düğümünde kullanılacağını veya analog filtre tasarımının kesinleştiğini göstermez.
- Önceki kayıtlar tarihsel teknik açıklamalar ve test notlarıdır; yeni projedeki fiziksel konfigürasyonu, yeni deney veya kalibrasyon sonucunu tek başına doğrulamaz.
- Başlangıç ayarları: 2 kS/s, nominal 200 ms pencere, yaklaşık 1 s PZEM sorgusu.
- PZEM'in iç ölçüm penceresi ve bu modüldeki gecikmesi doğrulanmadı.

## Karar kapıları
- [ ] G1 — Faz 1 sonunda: SCT RMS kalibrasyonu önceden belirlenmiş hata hedefinde ve clipping yok.
- [ ] G2 — Faz 3 sonunda: PZEM okuma durumu izleniyor; geçersiz okumalar özetlerden dışlanıyor.
- [ ] G3 — Faz 6 sonunda: örnekleme hızı hedef yüklerde ölçülmüş metriklerle gerekçelendirilmiş.

## Sıradaki üç iş
1. [ ] [T001 — Donanım envanteri](tasks/T001-hardware-inventory.md): SCT013-030 önceliğini ve kullanıcı tarafından bildirilen stok adetlerini kaydet; ardından PZEM varyantı/CT, MCU/ADC, analog ön uç ve stok kanıtı gibi yalnızca proje-özel eksikleri tamamla.
2. [ ] [T002 — Güvenlik kontrolü](tasks/T002-safety-checklist.md): şebeke bağlantısı öncesi yetkin kişi incelemesi.
3. [ ] [T003 — Referans ve hata hedefi](tasks/T003-reference-and-error-target.md): referans cihazı, en az üç yük seviyesi ve ölçüm öncesi kabul hedefi.

**Çalışma odağı:** Aynı anda yalnızca Aktif görev satırındaki görev üzerinde çalış. Yeni fikirler mevcut görevin kapsamını değiştirmesin.

## Açık engeller
- SCT seçimi artık belirtilmiştir: bu projede öncelik SCT013-030 (30 A / 1 V). Gerçek parçanın fotoğrafı ve stok sayımı henüz depoda kalıcı kanıt olarak kayıtlı değil; adetler kullanıcı bildirimidir.
- PZEM için ortak V3.0 aile belgesi mevcuttur; bu projenin gerçek modülündeki 10 A/100 A varyantı ve CT modeli henüz kaydedilmedi.
- MCU/ADC, gerçek bias/VREF, analog ön uç ve kablolama ayrıntıları bu proje için doğrulanmadı.
- 100 nF / 50 V seramik kondansatörün devredeki görevi henüz belirlenmedi.
- E01–E06 deneylerinin hiçbiri tamamlanmadı.

Firmware ve analiz uygulaması henüz eklenmedi. Deney/kalibrasyon sonuçları yapılmadı olarak kalır.
