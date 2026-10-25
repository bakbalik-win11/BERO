# Proje durumu

**Son güncelleme:** 2026-10-26  
**Aktif faz:** Faz 0 — hazırlık ve güvenlik  
**Deney durumu:** YAPILMADI  
**Yönetim protokolü:** SESSION_PROTOCOL.md ve HISTORY/SESSION_LOG.md bu PR ile ekleniyor; GitHub kontrolü birleştirme ve ilk başarılı Action çalışmasından sonra teyit edilecek.

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
1. [ ] [Donanım envanterini doldur](hardware/inventory.md): fiziksel SCT, PZEM, MCU, ADC, burden/bias, VREF.
2. [ ] [Güvenlik kontrol listesini](hardware/safety-checklist.md) tamamlat; şebeke bağlantısı öncesinde yetkin inceleme al.
3. [ ] Kalibrasyon için referans True-RMS ampermetre ve en az üç rezistif yük seviyesi belirle.

## Açık engeller
- Kullanılacak SCT ve PZEM varyantları/etiketleri bu proje için doğrulanmadı.
- Analog ön uç ve ADC ayarları fiziksel olarak doğrulanmadı.
- E01–E06 deneylerinin hiçbiri tamamlanmadı.
- Yeni oturum protokolünün CI denetimi henüz bu PR üzerinde çalıştırılıp doğrulanmadı.

Firmware ve analiz uygulaması henüz eklenmedi. Deney/kalibrasyon sonuçları yapılmadı olarak kalır.
