# T009 — Faz 2 pratik sistem başlangıcı: modülleri ve ESP düğümlerini devreye alma

- **Durum:** AKTİF — Faz 2'nin ilk çalışma görevi
- **Faz:** Faz 2 — Pratik yeniden kurulum ve sistem geliştirme
- **Karar:** [ADR-014](../docs/decisions/ADR-014-phase2-practical-restart.md)

## Hedef

BERO donanımını ve ESP düğümlerini kayıtlı kodlardan ve çalışan örneklerden yararlanarak modül modül yeniden devreye almak. İlk başarı ölçütü, seçilen modülün temel işlevinin gerçek donanımda çalıştığını görmek ve bunu gerçek log/çıktıyla kanıtlamaktır.

## Çalışma yöntemi

1. O modülün amacı, kutu kapsamı ve fiziksel parçaları belirlenir.
2. Gerçek kart modeli, pin etiketleri, konektörler ve bağlantılar doğrulanır; bilinmeyenler tahmin edilmez.
3. Aynı işi yapan çalışan örnek kod/kütüphane araştırılır. Depodaki YAML ve geçmiş kodlar başlangıç referansı olarak okunur.
4. En az uyarlamayla bir ilk yapılandırma hazırlanır. Gereksiz mimari değişiklik yapılmaz.
5. Önce yapılandırma/derleme kontrol edilir; sonra yalnız uygun düşük gerilim tarafında bağlantı ve fiziksel işlev testi yapılır.
6. Gerçek cihaz çıktısı, log, test koşulu ve yorum kaydedilir.
7. Bir modülün temel işlevi doğrulanmadan diğer modüllerle entegrasyona geçilmez.

## Öncelik ilkeleri

- İlk soru "Bunu çalışan örnekle nasıl ayağa kaldırırız?" olur.
- Manyetik teori, ESP32 ADC iç mimarisi, MCP3208/SPI gibi konular yalnız somut bir uygulama engeli, tekrarlanabilir arıza veya açık teknik karar gerektiğinde derinleştirilir.
- Gereken güvenlik ve elektriksel sınırlar atlanmaz.
- Kullanıcı belirlemeden modül sırası, pin eşlemesi, ESP kartı veya firmware mimarisi kesinleştirilmez.
- Mevcut kod kayıtları korunur; yeni yapılandırma ile eski baseline arasındaki fark açıklanır.

## Kapsam

- SCT Okuma Test Modülü (3 SCT girişi + ortak bias + ESP32D2 assembly).
- PZEM düğümü (ESP32-WR1-PZEM ve PZEM-004T V3).
- SSR/zamanlama düğümü (ESP32-C3, SSR kontrolü, DS3231 ve olay bildirimi).
- Gerekli diğer modüller ve ortak haberleşme/HA entegrasyonu.

Bu liste donanımların mevcut durumda bağlı veya çalışır olduğu anlamına gelmez. Modül sırası kullanıcıyla belirlenir.

## Bu görevde yapılmayacaklar

- Sırf teorik kapsamı genişletmek için manyetik/ADC mimarisi araştırmasını derinleştirmek.
- Somut ihtiyaç doğmadan MCP3208'i mevcut firmware'e eklemek.
- Faz 1 deneylerini yeniden açmak.
- Sürekli ham ADC/50 Hz dalga kaydını yeniden zorunlu hâle getirmek.
- Derlenmemiş veya fiziksel olarak test edilmemiş kodu çalışır kabul etmek.

## Kabul ölçütleri

Her modül için ayrı ayrı:
- Gerçek kart/modül ve pin eşlemesi kaydedilmiş olmalı.
- Seçilen kodun kaynağı/sürümü veya depodaki referansı belirtilmeli.
- Yapılandırma derleme/konfigürasyon kontrolünden geçmiş olmalı.
- Uygun güvenli koşullarda gerçek donanım testi yapılmalı.
- Gerçek log/çıktı ve kısa teknik yorum depoda saklanmalı.

T009, yalnız tasarım belgesi yazıldığı için tamamlanmış sayılmaz. Her modülün durumu kanıtına göre ayrı tutulur.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Faz 2'yi pratik yeniden kurulum ve geliştirme süreci olarak başlatmak.
- **LOG:** Bu görev açılırken yeni firmware derleme, yükleme veya fiziksel test yapılmadı.
- **SONUÇ:** T009 AKTİF. İlk modül ve bağlantı ayrıntıları kullanıcıyla belirlenecek.
