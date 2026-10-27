# T001 — Fiziksel Donanım Envanteri

**Envanter durumu: KAYDEDİLDİ.** Kullanıcı tarafından bildirilen fiziksel stok, kart rolleri ve bias alt devresi kaydedildi. ADC/VREF seçimi ve SCT analog kuplaj doğrulaması T001 envanter görevinin kapsamı dışındadır; ilgili sonraki aşamada ele alınacaktır.

## 1. Kontrol ve ölçüm donanımı

| Bileşen | Özellik / adet | Durum |
|---|---|---|
| ESP32-C3 SuperMini | 1 | Mevcut; önceki SSR kontrol denemesinde kullanıldı |
| ESP32 ölçüm düğümü | 1 | Mevcut; önceki PZEM ölçüm denemesinde kullanıldı |
| SSR kartı | SAMM Market, 5 V, 2 kanal | Mevcut |
| RTC | DS3231 | Mevcut |
| PZEM-004T | V3.0 | Mevcut |
| Güç kaynağı | Masaüstü, 5 V / 1,8 A | Mevcut |
| Test yükü | Lamba | Mevcut |

## 2. SCT013 sensörleri

| Tür | Adet | Bağlantı |
|---|---:|---|
| SCT013 30 A / 1 V | 7 | Jack çıkışlı |
| SCT013 100 A / 1 V | 10 | Jack çıkışlı |
| **Toplam** | **17** | Jack yuvaları mevcut |

## 3. Önceden hazırlanmış analog arayüz kartı

Kullanıcı daha önce **8 kanallı, her kanalı ayrı bias ve direnç ağına sahip bir kart** hazırlamıştır. Bu, SCT013 ölçüm arayüzü için hazırlık bulunduğunu gösterir.

- Kanal sayısı: 8.
- Her kanalda ayrı bias ve direnç ağı.
- Jack yuvaları mevcut.
- Kullanıcının tarif ettiği okuma zinciri: **SCT013 → jack yuvası → ayrı bias/direnç ağı bulunan 8 kanallı kart → ESP32 ADC girişi**.
- İstenirse MCP serisi harici ADC bağlanabilir; MCP'nin bu projede seçildiği varsayılmıyor.
- Bağlantı ve ölçüm parçalarının tamamı kullanıcı beyanına göre mevcut.

## 4. Bilinmeyen bırakılan teknik ayrıntılar

Bu envanter konuşmasında aşağıdakiler belirtilmedi ve tahminle doldurulmadı:

- Gerçekte kullanılacak ADC modeli/revizyonu ve VREF kaynağı/değeri.
- SCT AC sinyalinin bias noktasına kuplaj yöntemi.
- Her kanalın direnç değerleri, filtre değerleri ve güvenli ADC giriş aralığı.
- MCP kullanılacaksa tam model ve bağlantı topolojisi.

Bunlar stok eksikliği değil; analog ön uç tasarımı/doğrulaması kapsamında kalan teknik kayıtlardır.

## 5. Kapanış notu

Kullanıcı, listelenen donanımların tamamının elinde olduğunu ve eksik parça olmadığını bildirmiştir. Bu sayfa fiziksel envanter beyanını kaydeder; tek başına elektriksel güvenlik veya analog ölçüm doğrulama kanıtı değildir.
