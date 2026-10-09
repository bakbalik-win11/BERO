# HDF-001 — Akımı Okuma

## Hedef

Proje BERO kapsamında akımın ölçüm zinciri üzerinden okunmasını, davranışının ölçümlerle doğrulanmasını ve elde edilen yöntemin sınırlarıyla birlikte tekrarlanabilir biçimde belgelenmesini sağlamak.

Bu ana hedef, tek bir kod denemesinden ibaret değildir. Sonuca ulaşmak için gereken görevler sırayla yürütülür; görev sırası, önceki görevlerden elde edilen ölçüm ve bulgulara göre netleştirilebilir. Her görev kendi kimliği ve kayıt alanıyla yürütülür; kapanmış görevlerin geçmişi korunur.

## Görev silsilesi

| Görev | Amaç | Durum |
|---|---|---|
| [GRV-001 — ESP32-D ile SCT-013 Akım Okuması](../../GOREVLER/GRV-001/RAPOR/README.md) | ESP32-D ve SCT-013 ile okuma zincirinin davranışını incelemek ve ölçüm sonuçlarını kaydetmek | Başlangıç / sonuç bekleniyor |

Yeni görevler, önceki görevdeki bulgulara göre bu tabloya yeni satır olarak eklenir. Eski görevlerin kayıtları yeni görev için yeniden yazılmaz.

GRV-001'in odağı ESP32-D ve SCT-013 ile akım okuma zincirini incelemek ve ölçüm davranışını kaydetmektir. MCP3208/SPI zamanlama doğrulaması bu görevin kapsamına dahil değildir; gerekirse ayrı bir görev olarak tanımlanır.

## Tamamlanma yaklaşımı

Ana hedefin tamamlandığı ancak sonuçlar ve kanıtlar değerlendirildikten sonra ilan edilir. Sonuç değerlendirmesi en az şunları kapsar:

- Hedeflenen ve fiilen elde edilen sonuç
- Kullanılan donanım, bağlantı ve test koşulları
- Ölçüm kayıtları ve bunların desteklediği bulgular
- Derlendiği ve test edildiği doğrulanmış kod sürümü ile bağlantısı
- Doğrulanmış noktalar, belirsizlikler ve sınırlar
- Öğrenilenler ve açık kalan işler

Test edilmemiş veya ölçümle doğrulanmamış noktalar başarılı sonuç olarak sunulmaz. Sonuç raporu hedef tamamlanırken hazırlanır; henüz sonuçlanmamış bir hedef için başarı iddiası oluşturulmaz.

## Süreklilik kuralı

Bu hedefe ait rapor, ölçüm ve kod geçmişi sessizce üzerine yazılarak değiştirilmez. Yeni bulgu yeni görev, yeni kod sürümü veya ek kayıt olarak tutulur. Ayrıntı: [Kayıt, Sürümleme ve Süreklilik Politikası](../../KAYIT_VE_SUREKLILIK.md).

## Durum

**Devam ediyor —** görev sonuçları henüz toplanmadı; ana hedef tamamlanmış sayılmıyor.
