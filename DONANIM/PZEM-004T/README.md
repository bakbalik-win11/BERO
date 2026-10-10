# PZEM-004T V3.0 — AC gerilim, akım, güç ve enerji ölçüm modülü

## Amaç ve model

Bu klasör, BERO'daki PZEM-004T ailesi için ortak donanım kaydıdır. TTL arayüzlü 10 A dahili şöntlü ve 100 A harici akım trafolu varyantları kapsar. Ürün dokümanında donanım revizyonu açıkça belirtilmiyorsa V3.0 uyumluluğu varsayılmamalı; kart etiketi ve sürümü doğrulanmalıdır.

- [Direnc.net ürün PDF'si — PZEM-004T TTL 0–100 A, 80–260 V](https://pdf.direnc.net/upload/guc-volt-akim-test-modulu-pzem-004t-arduino-icin-ttl-0-100a-80-260v.pdf)
- [PZEM-004T V3.0 kullanım kılavuzu / veri sayfası](https://eshop.tdmetal.cz/user/documents/upload/PZEM-004T-V3.0-Datasheet-User-Manual.pdf)
- [Alternatif PZEM-004T V3.0 kılavuz kopyası](https://mathieu.carbou.me/MycilaPZEM/PZEM-004T-V3.0-Datasheet-User-Manual.pdf)
- [mandulaj PZEM-004T v3.0 Arduino kütüphanesi](https://github.com/mandulaj/PZEM-004T-v30)
- [PlatformIO Library Registry](https://registry.platformio.org/libraries/mandulaj/PZEM-004T-v30)
- [ESPHome PZEM-004T enerji sensörü](https://esphome.io/components/sensor/pzemac/)

## Ölçüm ve arayüz

PZEM-004T V3.0; AC gerilim, akım, aktif güç, aktif enerji, frekans ve güç faktörü ölçer. Sonuçlar UART-TTL üzerinden, Modbus-RTU benzeri protokolle okunur.

| Parametre | Yayınlanan değer | Not |
|---|---|---|
| AC gerilim | 80–260 V AC | 0,1 V çözünürlük |
| Akım | 10 A veya 100 A varyantı | 100 A model harici CT kullanır |
| Başlangıç ölçüm akımı | Yaklaşık 0,01–0,02 A | Varyanta/kılavuza bağlı |
| Aktif güç | Yaklaşık 2,3 kW (10 A) / 23 kW (100 A) | Ürün sınıfı değeri |
| Frekans | 45–65 Hz | 0,1 Hz |
| Güç faktörü | 0,00–1,00 | 0,01 |
| Aktif enerji | Kılavuz sürümüne göre gösterim değişebilir | 1 Wh olarak listelenir |
| Seri haberleşme | UART-TTL | 9600 baud, 8N1 |

Üretici/kılavuz kaynaklarında yaklaşık %0,5 gerilim, akım, güç ve enerji; %1 güç faktörü doğruluğu bildirilebilir. Bunlar BERO'da doğrulanmış kalibrasyon sonucu değildir.

## Varyant ve akım trafosu

- 10 A varyantı genellikle dahili şönt kullanır.
- 100 A varyantı harici akım trafosu (CT) kullanır.
- CT modeli, oranı ve bağlantısı ürünle gelen şemaya göre doğrulanmalıdır.
- CT sekonderini üreticinin tarif ettiği yük dışında açık devre bırakma.
- Faz ve nötrü CT içinden birlikte geçirmek ölçümü iptal ettirebilir.

## UART-TTL bağlantısı

| PZEM TTL | MCU tarafı | Not |
|---|---|---|
| TX | MCU UART RX | Çapraz bağlanır |
| RX | MCU UART TX | Çapraz bağlanır |
| GND | MCU GND | Yalnızca izolasyon ve arayüz düzeni doğrulandıktan sonra |
| 5V/VCC | Uygun 5 V besleme | Ürün revizyonunun gereksinimini kontrol et |

UART-TTL portu RS-485 A/B değildir. PZEM'in 5 V pininin bulunması UART pinlerinin 5 V toleranslı olduğunu garanti etmez. ESP32 GPIO'larına 5 V lojik uygulama; TX çıkış seviyesini ve RX giriş uyumluluğunu doğrula, gerekiyorsa uygun seviye dönüştürücü kullan. PZEM'in 5 V pinini ESP32'nin 3V3 pinine bağlama.

## Elektrik güvenliği

PZEM 80–260 V AC şebeke ölçümü yapar; şebeke terminalleri ölümcül gerilim taşıyabilir.

- Enerjiyi tamamen kesmeden kablolama yapma.
- Uygun sigorta, muhafaza, izolasyon aralığı, kablo kesiti ve korumalı klemens kullan.
- Açıkta şebeke terminali bırakma; breadboard/jumper kabloyla 230 V taşıma.
- TTL tarafını şebeke terminallerinden fiziksel olarak ayır.
- USB/ESP32 bağlantısının güvenli izolasyon sağladığını varsayma.
- Şebeke bağlantısını yetkin kişi yapmalıdır.

## BERO devreye alma ve test sırası

1. Kart üzerindeki tam model/sürümü ve CT tipini kaydet.
2. UART pinlerini, besleme gereksinimini ve lojik seviyeleri doğrula.
3. UART'ı 9600 baud, 8N1 ile dene.
4. Gerilim, akım, güç, enerji, frekans ve güç faktörünü oku.
5. Geçersiz veri ve haberleşme kopması davranışını kontrol et.
6. Bilinen bir yükle değerleri uygun referans ölçüm cihazlarıyla karşılaştır.
7. Home Assistant aktarımından önce veri yenileme ve haberleşme hatalarını kontrol et.

## BERO test kaydı

ESP32D1 üzerinde ESPHome `pzemac` bileşeniyle başarılı okuma logu alınmıştır. Örnek ölçüm: 230,2 V, 0,028 A, 1,50 W, 10386 Wh, 50,0 Hz ve güç faktörü 0,23. Sonraki örneklerde de değerler tekrar okunmuştur. Bu, UART/Modbus haberleşmesinin çalıştığını gösterir; ölçüm doğruluğu bağımsız referansla henüz kalibre edilmiş değildir.

**Durum:** Ortak PZEM-004T kaydı. BERO'daki fiziksel modülün kesin varyantı/CT modeli ve ölçüm doğruluğu ayrıca doğrulanmalıdır.
