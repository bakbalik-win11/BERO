# Proje durumu

**Son güncelleme:** 2026-10-26  
**Aktif faz:** Faz 0 — hazırlık ve güvenlik  
**Aktif görev:** [T001 — Fiziksel donanım envanteri](tasks/T001-hardware-inventory.md)  
**Deney durumu:** YAPILMADI  
**Çalışma protokolü:** SESSION_PROTOCOL.md ve [gün sonu kontrol listesi](GUN_SONU_KONTROLU.md) main dalında. PR #2 ve PR #3 birleştirildi; [otomatik kapanış kontrolü başarılı](https://github.com/bakbalik-win11/BERO/actions/runs/40234658507). İlk tarihli günlük girdisindeki 'PR #2 birleştirilmedi' cümlesi artık güncel değildir; en yeni günlük düzeltmesine bakın.

## Mevcut bilgi
- BERO içinde SCT013-100A-1V, SCT013-30A-1V, PZEM-004T, ESP32-WROOM-32D ve MCP3208 bileşen kayıtları var.
- Bu kayıtlar bu projede fiziksel olarak kullanılan tam konfigürasyonu tek başına doğrulamaz.
- Başlangıç ayarları: 2 kS/s, nominal 200 ms pencere, yaklaşık 1 s PZEM sorgusu.
- PZEM'in iç ölçüm penceresi ve bu modüldeki gecikmesi doğrulanmadı.

## Karar kapıları
- [ ] G1 — Faz 1 sonunda: SCT RMS kalibrasyonu önceden belirlenmiş hata hedefinde ve clipping yok.
- [ ] G2 — Faz 3 sonunda: PZEM okuma durumu izleniyor; geçersiz okumalar özetlerden dışlanıyor.
- [ ] G3 — Faz 6 sonunda: örnekleme hızı hedef yüklerde ölçülmüş metriklerle gerekçelendirilmiş.

## Sıradaki üç iş
1. [ ] [T001 — Donanım envanteri](tasks/T001-hardware-inventory.md): fiziksel SCT, PZEM, MCU, ADC, burden/bias, VREF.
2. [ ] [T002 — Güvenlik kontrolü](tasks/T002-safety-checklist.md): şebeke bağlantısı öncesi yetkin kişi incelemesi.
3. [ ] [T003 — Referans ve hata hedefi](tasks/T003-reference-and-error-target.md): referans cihazı, en az üç yük seviyesi ve ölçüm öncesi kabul hedefi.

**Çalışma odağı:** Aynı anda yalnızca Aktif görev satırındaki görev üzerinde çalış. Yeni fikirler mevcut görevin kapsamını değiştirmesin.

## Açık engeller
- Kullanılacak SCT ve PZEM varyantları/etiketleri bu proje için doğrulanmadı.
- Analog ön uç ve ADC ayarları fiziksel olarak doğrulanmadı.
- E01–E06 deneylerinin hiçbiri tamamlanmadı.

Firmware ve analiz uygulaması henüz eklenmedi. Deney/kalibrasyon sonuçları yapılmadı olarak kalır.
