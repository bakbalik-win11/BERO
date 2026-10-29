# SCT-013 + PZEM akım gözlem sistemi

## Amaç
SCT-013 akım trafosundan ADC örnekleri toplamak, pencere bazlı akım istatistikleri üretmek ve bunları PZEM'in bildirdiği ölçümlerle zaman damgalı şekilde karşılaştırmak.

Bu çalışma enerji analizörü, güç kalitesi analizörü veya harmonik ölçüm sistemi geliştirme projesi değildir.

## Bu projede seçilen / tanımlanan donanım
- **Öncelikli SCT:** [SCT013-030 — 30 A / 1 V](hardware/references/SCT013-30A-1V.md). Kullanıcı stok bildirimi: 7 adet 30 A / 1 V ve 10 adet 100 A / 1 V; ikisi de jack çıkışlı.
- **SCT/bias devresi:** Mevcut devre breadboard üzerinde hazırlanmış bias alt devresidir (2 × 10 kΩ, orta nokta ve orta noktadan GND'ye 104/100 nF kondansatör). SCT013 jack üzerinden bu devreye bağlanıp ESP32'nin dahili ADC'siyle okunacak. 8 kanallı analog arayüz kartı mevcut değildir; MCP3208 sonraki aşamaya ayrılmıştır. Ayrıntılar [analog ön uç kaydında](hardware/frontend.md) ve [envanterde](hardware/inventory.md).
- **PZEM:** Esas kaynak [DONANIM/PZEM-004T/README.md](../../DONANIM/PZEM-004T/README.md); proje içi teknik kopyası [PZEM-004T V3.0](hardware/references/PZEM-004T-V3.0.md). Kullanıcı CT modelini **PZCT-02 (0–100 A)** olarak belirtti ve görüntü, bu CT'nin PZEM'e bağlı olduğunu göstermek içindi. Bu, 100 A harici CT'li PZEM düzenidir; fotoğraf yeni bir donanım referansı oluşturmak için paylaşılmadı.
- **Bias üretim alt devresi:** Kullanıcı onayıyla tamamlandı sayılıyor. Ayrıntılar [donanım envanterinde](hardware/inventory.md) yer alır.
- **SSR:** [SAMM Market 5 V 2 Kanal SSR kartı](https://market.samm.com/5v-2-kanal-solid-state-role-karti) (tedarikçi kodu İzmo9659, SKU MP02637) proje donanımına dahil edildi. OMRON, fototriyak izolasyon ve zero-cross; kanal başına 75–264 VAC ve 0,1–2 A (ürün sayfası değerleri). Kart üzerindeki SSR'nin tekil parça kodu doğrulanmadı. Girişin LOW/HIGH açıklamasıyla “low-level trigger” notu çelişebildiğinden gerçek kontrol mantığı düşük gerilim testiyle doğrulanmalı. Ayrıntılar [SSR referansında](hardware/references/SSR.md).
- **RTC:** DS3231, ölçüm ve olay kayıtlarına takvim/saat zaman damgası eklemek için kullanılacak. [Proje içi DS3231 referansı](hardware/references/DS3231.md); resmî veri sayfası bağlantısı [burada](hardware/references/DS3231-datasheet.md).
- **Güç ve test:** Kullanıcı masaüstü 5 V / 1,8 A güç kaynağı, lamba test yükü ve bağlantı/ölçüm parçalarının mevcut olduğunu bildirdi.
- **Güvenlik kontrolü:** T002 kontrol listesi kullanıcı beyanına göre tamamlandı ve depoya işlendi; bu kayıt asistanın bağımsız fiziksel güvenlik doğrulaması değildir. [Kontrol listesi](hardware/safety-checklist.md).

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
Teknik açıklamaları yeniden yazmamak için ilgili Markdown dosyaları [hardware/references/](hardware/references/README.md) altında bulunur. DS3231 kaydı da önceki BERO donanım belgesinden kopyalandı ve üreticinin resmî veri sayfasıyla desteklendi. Kaynak `DONANIM/` dosyaları asıl kayıttır; kopyaların varlığı yeni deney veya kalibrasyon yapıldığı anlamına gelmez.

## İlk okunacak dosyalar
1. [AGENTS.md](AGENTS.md) — çalışma protokolü.
2. [STATUS.md](STATUS.md) — güncel durum ve sıradaki işler.
3. [ROADMAP.md](ROADMAP.md) — fazlar ve kabul ölçütleri.
4. [Görev kartları](tasks/README.md) — aktif iş ve bağımlılıklar.
5. [Açık sorular](docs/open-questions.md) — gerçekten cevap bekleyen konular.
6. [Fiziksel donanım envanteri](hardware/inventory.md) — seçilen modüller ve bias alt devresi.
7. [T001 kullanıcı envanter özeti](docs/inventory/T001-fiziksel-donanim-envanteri.md) — bildirilen stoklar ve breadboard bias alt devresi.

## Başlangıç tasarım değerleri
- SCT örnekleme hızı: 2 kS/s.
- SCT özet penceresi: nominal 200 ms (50 Hz'de nominal 10 çevrim).
- PZEM sorgusu: yaklaşık 1 s başlangıç aralığı.
- Yük geçişi etiketi: yaklaşık 3 s başlangıç süresi.

Bunlar deneylerle gözden geçirilecek başlangıç değerleridir; doğrulanmış sonuç değildir.

## Deney durumu
Fiziksel deney veya kalibrasyon sonucu henüz üretilmedi. E00/E01 temel ADC ve yüksüz gürültü hazırlığı aktif görev sırasındadır. Sonraki kapsamlı SCT karakterizasyon planı [E08](experiments/E08-sct-characterization/README.md) içinde belgelenmiştir: yüksüz uzun okuma, 100 W akkor matrisi, 150 W akkor ve 8,5 W LED karşılaştırması, ardından aç-kapa testi. [E07](experiments/E07-sct-stability-step-tests/protocol.md) önceki uygulanmamış plan olarak korunur; E08 güncel planı açıklar. E08 kapsamında PZEM/başka ESP ortalama akımı yalnız genel bağlamdır, zaman eşleştirmesi yapılmaz. Tüm sonuç kayıtları gerçek ölçüm yapılana kadar YAPILMADI durumunda kalır.
