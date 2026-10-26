# SCT-013 + PZEM akım gözlem sistemi

## Amaç
SCT-013 benzeri akım trafosundan ADC örnekleri toplamak, pencere bazlı istatistikler üretmek ve bunları PZEM'in bildirdiği akım, gerilim ve PF değerleriyle zaman damgalı şekilde karşılaştırmak.

Bu çalışma enerji analizörü, güç kalitesi analizörü veya harmonik ölçüm sistemi geliştirme projesi değildir.

## BERO içindeki ilgili donanım kayıtları
- [SCT013-100A-1V](../../DONANIM/SCT013-100A-1V/README.md)
- [SCT013-30A-1V](../../DONANIM/SCT013-30A-1V/README.md)
- [PZEM-004T](../../DONANIM/PZEM-004T/README.md)
- [ESP32-WROOM-32D](../../DONANIM/ESP32-WROOM-32D/README.md)
- [MCP3208 ADC](../../DONANIM/MCP3208/README.md)

Bu kayıtlar BERO'nun donanım kaynaklarıdır. Bu projede kullanılacak fiziksel sensör, ADC, MCU, burden/bias yapısı ve PZEM varyantı envanterde doğrulanana kadar kesinleşmiş sayılmaz.

## Gün sonu kontrolü
Teknik ayrıntıları tek tek incelemek zorunda değilsiniz. [Gün sonu kontrol listesini](GUN_SONU_KONTROLU.md) izleyin; asistan her madde için doğrudan kanıt bağlantıları vermelidir.

## İlk okunacak dosyalar
1. [AGENTS.md](AGENTS.md) — çalışma protokolü.
2. [STATUS.md](STATUS.md) — mevcut durum ve sıradaki işler.
3. [ROADMAP.md](ROADMAP.md) — fazlar ve kabul ölçütleri.
4. [Görev kartları](tasks/README.md) — sıradaki tek işi, bağımlılıkları ve kabul ölçütlerini takip et.
5. [Açık sorular](docs/open-questions.md) — deneyle doğrulanacak konular.
6. [Kapsam](docs/00-scope.md) — hedefler ve kapsam dışı konular.

## Başlangıç tasarım değerleri
- SCT örnekleme hızı: 2 kS/s.
- SCT özet penceresi: nominal 200 ms (50 Hz'de nominal 10 çevrim).
- PZEM sorgusu: yaklaşık 1 s başlangıç aralığı.
- Yük geçişi etiketi: yaklaşık 3 s başlangıç süresi.

Bunlar bu donanımda doğrulanmış sonuçlar değil, deneylerle gözden geçirilecek tasarım başlangıçlarıdır.

## Deney durumu
Bu proje kapsamında fiziksel deney sonucu henüz üretilmedi. Deney tamamlanana kadar results.md dosyaları YAPILMADI durumunu koruyacaktır.
