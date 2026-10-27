# SCT-013 + PZEM akım gözlem sistemi

## Amaç
SCT-013 akım trafosundan ADC örnekleri toplamak, pencere bazlı akım istatistikleri üretmek ve bunları PZEM'in bildirdiği ölçümlerle zaman damgalı şekilde karşılaştırmak.

Bu çalışma enerji analizörü, güç kalitesi analizörü veya harmonik ölçüm sistemi geliştirme projesi değildir.

## Bu projede seçilen / tanımlanan donanım
- **Öncelikli SCT:** [SCT013-030 — 30 A / 1 V](hardware/references/SCT013-30A-1V.md).
- **PZEM:** Esas kaynak [DONANIM/PZEM-004T/README.md](../../DONANIM/PZEM-004T/README.md); proje içi teknik kopyası [PZEM-004T V3.0](hardware/references/PZEM-004T-V3.0.md). Kullanıcı CT modelini **PZCT-02 (0–100 A)** olarak belirtti ve görüntü, bu CT'nin PZEM'e bağlı olduğunu göstermek içindi. Bu, 100 A harici CT'li PZEM düzenidir; fotoğraf yeni bir donanım referansı oluşturmak için paylaşılmadı.
- **Bias üretim alt devresi:** Kullanıcı onayıyla tamamlandı sayılıyor. Ayrıntılar [donanım envanterinde](hardware/inventory.md) yer alır.
- **SSR:** [Mevcut BERO SSR donanım kaydı](hardware/references/SSR.md) ve [aday veri sayfası notu](hardware/references/SSR-datasheet-candidate.md) aktarıldı. Fiziksel SSR'nin tam modeli doğrulanmış değil; bu kayıt projede kullanım kararı değildir.

## İlk aşamada kullanılacak ESP32 kartları
- **2 adet ESP32-WROOM-32D geliştirme kartı**
- **1 adet ESP32-WROOM-32E geliştirme kartı**
- **1 adet ESP-WROOM-32 tabanlı NodeMCU ESP32 Bluetooth geliştirme kartı** (fotoğrafta bu adla tanımlanıyor; kart üreticisi/PCB revizyonu henüz okunmuyor)

**İlk aşama toplamı: 4 ESP32 geliştirme kartı.** Bu dağılım kullanıcı tarafından belirtildi ve görsellerle desteklendi; bağımsız fiziksel sayım yapılmadı. Önceki `ESP32-WROOM-32S × 1` satırı, kullanıcının son düzeltmesi doğrultusunda genel ESP-WROOM-32 NodeMCU kartı olarak değiştirildi. Mevcut [ESP32-WROOM-32D teknik kaydı](../../DONANIM/ESP32-WROOM-32D/README.md) referans olarak korunur. Dört kartın ilk aşamadaki rolleri ve ortak ADC arayüzü yazılım/bağlantı planında ayrıştırılacak.

## Önceki BERO donanım kayıtları
- [SCT013-100A-1V](../../DONANIM/SCT013-100A-1V/README.md)
- [SCT013-30A-1V](../../DONANIM/SCT013-30A-1V/README.md)
- [PZEM-004T](../../DONANIM/PZEM-004T/README.md)
- [ESP32-WROOM-32D](../../DONANIM/ESP32-WROOM-32D/README.md)
- [MCP3208 ADC](../../DONANIM/MCP3208/README.md)
- [SSR](../../DONANIM/SSR/README.md)

## Projeye kopyalanan referanslar
Teknik açıklamaları yeniden yazmamak için ilgili Markdown dosyaları [hardware/references/](hardware/references/README.md) altında bulunur. Kaynak `DONANIM/` dosyaları asıl kayıttır; kopyaların varlığı yeni deney veya kalibrasyon yapıldığı anlamına gelmez.

## İlk okunacak dosyalar
1. [AGENTS.md](AGENTS.md) — çalışma protokolü.
2. [STATUS.md](STATUS.md) — güncel durum ve sıradaki işler.
3. [ROADMAP.md](ROADMAP.md) — fazlar ve kabul ölçütleri.
4. [Görev kartları](tasks/README.md) — aktif iş ve bağımlılıklar.
5. [Açık sorular](docs/open-questions.md) — gerçekten cevap bekleyen konular.
6. [Fiziksel donanım envanteri](hardware/inventory.md) — seçilen modüller ve bias alt devresi.

## Başlangıç tasarım değerleri
- SCT örnekleme hızı: 2 kS/s.
- SCT özet penceresi: nominal 200 ms (50 Hz'de nominal 10 çevrim).
- PZEM sorgusu: yaklaşık 1 s başlangıç aralığı.
- Yük geçişi etiketi: yaklaşık 3 s başlangıç süresi.

Bunlar deneylerle gözden geçirilecek başlangıç değerleridir; doğrulanmış sonuç değildir.

## Deney durumu
Bu projede henüz E01–E06 deney sonucu veya kalibrasyon sonucu üretilmedi. Deney tamamlanana kadar sonuç kayıtları YAPILMADI durumunu korur.
