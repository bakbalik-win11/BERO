# ADR-034 — Modül 4 bias karşılaştırması ve PREBERO besleme kararı sırası

- **Tarih:** 2026-11-20
- **Durum:** KABUL EDİLDİ — çalışma sırası; bias mimarisi kararı açık
- **Karar sahibi:** Kullanıcı

## Amaç

Modül 4'teki mevcut ESP32D2 + ADS1115 + SCT masaüstü ölçüm zincirinde bias kullanımının gerekliliğini deney ve osiloskop gözlemiyle belirlemek. PREBERO Modül 5, 6 ve 7'nin bias besleme/mimari seçimini bu sonuçtan sonraya bırakmak.

## Kabul edilen çalışma sırası

1. **Modül 4 biaslı/bias'sız karşılaştırma deneyi:** Aynı ölçüm zincirinde biaslı ve bias'sız koşullar karşılaştırılır. Deney koşulları, bağlantı farkları, ölçüm kayıtları ve sonuçlar ayrı ayrı kaydedilir.
2. **Osiloskopla sinyal incelemesi:** Biaslı ve bias'sız yapı birlikte incelenir. Sinyalin dalga biçimi, DC çalışma noktası/bias seviyesi ve ölçüm zincirindeki davranış gözlenir. Gerçek osiloskop görüntüleri ve ayarlar kanıt olarak saklanır.
3. **Bias gerekliliği kararı:** Deney ve osiloskop bulguları birlikte değerlendirilerek SCT + ADS1115 zincirinde bias gerekip gerekmediğine karar verilir. Bu karar önceden verilmiş değildir.
4. **PREBERO Modül 5/6/7 için bias besleme mimarisi değerlendirmesi:** Bias gerekliliği netleştikten sonra iki yaklaşım karşılaştırılır:
   - Bias devresini ESP'nin beslemesinden üretmek.
   - Modül 1'in ikiz bias devrelerini/kutularını üretmek.
   Seçim; ölçüm sonucu, besleme kapasitesi, elektriksel gürültü, izolasyon/güvenlik, fiziksel yerleşim ve modüllerin bağımsız çalışması dikkate alınarak yapılır.

## Kapsam ve sınırlar

- Modül 1 mevcut bias trafosu/güç kutusudur; korunur ve Modül 4 deneyinde kullanılabilir.
- Modül 4 mevcut masaüstü deney düzeneğidir; ilk aktif çalışma buradadır.
- Modül 5 çamaşır makinesi, Modül 6 bulaşık makinesi, Modül 7 ana hat + PZEM gözlem modülleridir. Üçü de PREBERO kapsamındadır.
- Modül 5/6/7 için bias besleme yöntemi henüz seçilmemiştir.
- Bias kullanımı, devre topolojisi veya ESP'den besleme güvenliği hakkında deney yapılmadan varsayım kurulmaz.
- Osiloskop incelemesi, ölçüm zincirinin gerçek davranışını anlamak içindir; tek başına nihai ölçüm doğruluğu kanıtı değildir.

## Kanıt ve tamamlanma

Her aşamada HEDEF / LOG / SONUÇ kaydı tutulur. Osiloskop ekran görüntüsü, cihaz ayarları, gerçek ölçüm logları ve yorumları depoya eklenir. Deney yapılmadan sonuç veya karar tamamlandı gösterilmez.

## İlgili kayıtlar

- [ADR-033 — Modül kimlikleri ve PREBERO](ADR-033-module-identities-desktop-and-prebero.md)
- [Modül 4 masaüstü düzenek ve deney kayıtları](../devices/README.md)
