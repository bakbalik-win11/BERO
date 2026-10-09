# PZEM-004T-100A — AC güç ve enerji ölçüm modülü

## 1. Kapsam

Bu belge, Direnc.net üzerinden paylaşılan **PZEM-004T, TTL arayüzlü, 0–100 A / 80–260 V** ürün dokümanını temel alır. PZEM-004T-100A, akımı harici akım trafosu (CT) üzerinden ölçen ve ölçüm sonuçlarını UART-TTL üzerinden ileten bir AC ölçüm modülüdür.

Kaynakta ürünün donanım revizyonu açıkça belirtilmiyorsa, V3.0 kütüphanesiyle uyumlu olduğu varsayılmamalı; kartın etiketini ve üzerindeki sürümü kontrol et.

## 2. Kaynaklar

- [Kullanıcının verdiği Direnc.net PDF — PZEM-004T TTL 0–100A, 80–260V](https://pdf.direnc.net/upload/guc-volt-akim-test-modulu-pzem-004t-arduino-icin-ttl-0-100a-80-260v.pdf)
- [PZEM-004T V3.0 üretici kılavuzu kopyası (PDF)](https://mathieu.carbou.me/MycilaPZEM/PZEM-004T-V3.0-Datasheet-User-Manual.pdf)
- [PZEM-004T v3.0 Arduino kütüphanesi](https://github.com/mandulaj/PZEM-004T-v30)
- [ESPHome PZEM-004T enerji sensörü](https://esphome.io/components/sensor/pzemac/)

## 3. PZEM-004T-100A için temel özellikler

Aşağıdaki ölçüm özellikleri PZEM-004T V3.0 dokümanında listelenir; elindeki modülün sürümü farklıysa doğrulanmalıdır.

| Ölçüm | Belirtilen aralık | Çözünürlük / not |
|---|---:|---|
| AC gerilim | 80–260 V | 0,1 V |
| AC akım | 0–100 A | başlangıç akımı 0,02 A; 0,001 A çözünürlük olarak listelenir |
| Aktif güç | 0–23 kW | 0,1 W çözünürlük olarak listelenir |
| Frekans | 45–65 Hz | 0,1 Hz |
| Güç faktörü | 0,00–1,00 | 0,01 |
| Aktif enerji | 0–9999,99 kWh (kılavuz sürümüne göre gösterim değişebilir) | 1 Wh |
| Haberleşme | UART TTL + Modbus-RTU benzeri protokol | 9600 baud, 8N1 |
| Akım algılama | Harici CT | CT modeli/oranı ürünle birlikte doğrulanmalı |

Kılavuzda üretici tarafından verilen tipik doğruluk iddiası gerilim/akım/aktif güç/enerji için %0,5, frekans için %0,5 ve güç faktörü için %1 olarak listelenir. Bunlar bağımsız kalibrasyon sonucu değildir.

## 4. TTL bağlantısı

V3.0 kılavuzunda TTL tarafı için 5 V, RX, TX ve GND uçlarının tamamının bağlı olması gerektiği belirtilir.

| PZEM TTL | MCU tarafı | Not |
|---|---|---|
| 5V | Uygun 5 V besleme | Kılavuza göre haberleşme arayüzünün beslemesi |
| GND | MCU GND | Ortak lojik referans |
| TX | MCU UART RX | Çapraz bağlanır |
| RX | MCU UART TX | Çapraz bağlanır |

**ESP32 lojik seviyesi uyarısı:** PZEM'in TX çıkış seviyesi ve RX girişinin 3,3 V uyumluluğu elindeki kart revizyonu için doğrulanmalıdır. ESP32 GPIO'larına 5 V lojik uygulama. Gerekiyorsa uygun seviye dönüştürücü kullan. PZEM'in 5 V pinini ESP32'nin 3V3 pinine bağlama.

## 5. Yüksek gerilim ve akım güvenliği

- PZEM ölçüm terminalleri 80–260 V AC şebeke aralığıyla ilişkilidir. Şebeke gerilimi ölümcül olabilir.
- Primer akım yolu ve CT bağlantısı, ürün kılavuzundaki bağlantı şemasına göre yapılmalıdır. 100 A varyantında akımın doğrudan modül üzerindeki küçük sinyal pinlerinden geçirilmesi beklenmez; harici CT kullanılır.
- Modülün izolasyon/terminal mesafeleri ve muhafazası tek başına pano güvenliğini kanıtlamaz. Uygun sigorta, muhafaza, kablo kesiti, terminal sıkılığı ve çekme koruması gerekir.
- Enerji varken kablolama değiştirme. İlk testleri yetkin bir elektrikçi gözetiminde ve uygun korumalı düzenekte yap.
- TTL tarafını şebeke ölçüm bağlantılarından fiziksel olarak ayır; bilgisayar/USB bağlantısı üzerinden tehlikeli potansiyel taşınmadığını varsayma.

## 6. BERO için devreye alma sırası

1. Modülün tam modelini ve donanım sürümünü fotoğraf/etiketle kaydet.
2. Akım CT'sinin modelini, nominal akımını ve konektörünü doğrula.
3. Şebeke bağlantısını enerjisizken üretici şemasına göre kontrol ettir.
4. TTL tarafında 5V/GND/TX/RX pinlerini doğrula; MCU lojik seviyelerini ölç.
5. UART'ı 9600 baud, 8 data bit, no parity, 1 stop bit (9600 8N1) ile dene.
6. Önce gerilim ve frekans değerlerinin makul olup olmadığını kontrol et; ardından bilinen bir yükle akım, güç ve güç faktörünü karşılaştır.
7. Referans ölçümle farklı yüklerde test et; kütüphane veya sensör sürümü belirsizse bunu test kaydına ekle.

## 7. Sürüm uyumluluğu notu

“PZEM-004T” adı altında eski ve V3.0 varyantları bulunur. Mandulaj/PZEM-004T-v30 kütüphanesi özellikle V3.0 protokolünü hedefler; eski modüllerle uyumlu olduğu varsayılmamalıdır. ESPHome'daki `pzemac` bileşeni de desteklediği modül/sürüm açıklamasıyla karşılaştırılmalıdır.

**Durum:** Kaynak ve ilk devreye alma dokümanı hazırlandı. BERO'daki gerçek modülün sürümü, CT modeli ve ESP32 UART bağlantısı fiziksel olarak doğrulanmış değildir.