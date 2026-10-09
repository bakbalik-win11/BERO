# PZEM-004T — AC gerilim, akım, güç ve enerji ölçüm modülü

## Amaç ve model

Bu klasör, paylaşılan **PZEM-004T TTL, 0–100 A, 80–260 V** PDF'sini ve PZEM-004T V3.0 ailesine ait teknik kaynakları toplar.

- [Direnc.net ürün PDF'si](https://pdf.direnc.net/upload/guc-volt-akim-test-modulu-pzem-004t-arduino-icin-ttl-0-100a-80-260v.pdf)
- [PZEM-004T V3.0 kullanım kılavuzu / veri sayfası](https://eshop.tdmetal.cz/user/documents/upload/PZEM-004T-V3.0-Datasheet-User-Manual.pdf)
- [mandulaj PZEM-004T v3.0 Arduino kütüphanesi](https://github.com/mandulaj/PZEM-004T-v30)

PZEM-004T ailesinde 10 A dahili şöntlü ve 100 A harici akım trafolu varyantlar bulunur. V1/V2/V3 sürümleri haberleşme ve kütüphane uyumluluğu bakımından birbirinin yerine varsayılmamalıdır. Kart etiketinden tam sürümü doğrula.

## Ölçüm ve arayüz

PZEM-004T V3.0 gerilim, akım, aktif güç, aktif enerji, frekans ve güç faktörü ölçer. Ölçüm sonuçları UART-TTL üzerinden sayısal okunur; V3.0 protokolü Modbus-RTU benzeri çerçeve kullanır.

| Parametre | Yayınlanan değer | Not |
|---|---|---|
| Gerilim | 80–260 V AC, 0,1 V çözünürlük | Şebeke tarafı tehlikelidir |
| Akım | 10 A veya 100 A varyantı | 100 A model harici CT kullanır |
| Başlangıç ölçüm akımı | Yaklaşık 0,01/0,02 A, varyanta bağlı | Sürüme göre kontrol et |
| Aktif güç | Yaklaşık 2,3 kW (10 A) / 23 kW (100 A) | Ürün sınıfı değeri |
| Frekans | 45–65 Hz | V3.0 kaynakları |
| Güç faktörü | 0,00–1,00 | V3.0 kaynakları |
| Seri ayarı | 9600 baud, 8N1 | V3.0 dokümanına göre |

Bazı kaynaklar yaklaşık %0,5 gerilim/akım/güç doğruluğu ve %1 PF doğruluğu bildirir. Bunlar BERO'da doğrulanmış kalibrasyon sonucu değildir.

## 100 A varyantı ve CT

100 A varyantı harici akım trafosu (CT), 10 A varyantı genellikle dahili şönt kullanır. CT türü ve bağlantısı ürünle gelen çizime uygun olmalıdır. CT sekonderini üreticinin tarif ettiği yük dışında açık devre bırakma. Faz ve nötrü CT içinden birlikte geçirmek ölçümü iptal ettirebilir.

## ESP32 UART bağlantısı

- PZEM TX → ESP32 UART RX
- PZEM RX → ESP32 UART TX
- GND → GND
- VCC/5V → ürün revizyonunun besleme gereksinimine göre

UART-TTL portu RS-485 A/B değildir. TX/RX çapraz bağlanır. 5 V pininin bulunması UART pinlerinin 5 V toleranslı olduğunu garanti etmez; lojik seviyeleri doğrula.

## Elektrik güvenliği

PZEM 80–260 V AC ölçüm modülüdür; şebeke terminalleri ölümcül gerilim taşır. Enerjiyi keserek bağla; uygun sigorta, muhafaza, izolasyon aralığı ve klemens kullan. Açıkta şebeke terminali bırakma, breadboard/jumper kabloyla 230 V taşıma. USB/ESP32 bağlıyken şebeke tarafına dokunma. Şebeke bağlantısını yetkin kişi yapmalıdır.

## BERO test sırası

1. Kart sürümünü ve CT tipini kaydet.
2. UART pinlerini ve beslemeyi kılavuzdan doğrula.
3. UART 9600 8N1 ve TX/RX bağlantısını kontrol et.
4. Gerilim, akım, güç, enerji, frekans ve PF değerlerini oku.
5. Geçersiz veri ve bağlantı kopması davranışını test et.
6. Gerilim, akım ve gücü uygun referans ölçüm cihazlarıyla karşılaştır.
7. Home Assistant aktarımından önce veri yenileme ve haberleşme hatalarını kontrol et.

## Kaynaklar

- [Direnc.net PZEM-004T PDF](https://pdf.direnc.net/upload/guc-volt-akim-test-modulu-pzem-004t-arduino-icin-ttl-0-100a-80-260v.pdf)
- [PZEM-004T V3.0 User Manual](https://eshop.tdmetal.cz/user/documents/upload/PZEM-004T-V3.0-Datasheet-User-Manual.pdf)
- [mandulaj/PZEM-004T-v30](https://github.com/mandulaj/PZEM-004T-v30)
- [PlatformIO Library Registry](https://registry.platformio.org/libraries/mandulaj/PZEM-004T-v30)

**Durum:** Dokümantasyon hazırlandı. BERO'daki fiziksel modülün sürümü, CT bağlantısı ve ölçüm doğruluğu henüz fiziksel testle doğrulanmadı.