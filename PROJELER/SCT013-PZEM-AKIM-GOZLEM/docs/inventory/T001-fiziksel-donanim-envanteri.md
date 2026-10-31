# T001 — Fiziksel Donanım Envanteri

**Envanter durumu: KAYDEDİLDİ.** Kullanıcı tarafından bildirilen fiziksel stok, kart rolleri ve bias alt devresi kaydedildi. Harici ADC/VREF seçimi ve SCT analog kuplaj doğrulaması T001 envanter görevinin kapsamı dışındadır; bu aşamada ESP32'nin dahili ADC'si kullanılacaktır.

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

## 3. Breadboard bias alt devresi

Kullanıcının bildirdiği mevcut devre breadboard üzerinde hazırlanmış bias alt devresidir:
- 2 adet 10 kΩ, 1/4 W metal film dirençle orta nokta oluşturulur.
- Orta nokta ile GND arasına “104” kodlu 100 nF kondansatör bağlanmıştır.
- SCT013 jack üzerinden bu devreye bağlanacaktır.
- Bu aşamada harici ADC kullanılmayacak; ESP32'nin dahili ADC işlevi kullanılacaktır. MCP3208 sonraki aşamaya ayrılmıştır.

8 kanallı analog arayüz kartı mevcut değildir.

## 4. Bilinmeyen bırakılan teknik ayrıntılar

Bu envanter konuşmasında aşağıdakiler belirtilmedi ve tahminle doldurulmadı:

- Gerçekte kullanılacak ADC modeli/revizyonu ve VREF kaynağı/değeri.
- SCT AC sinyalinin bias noktasına kuplaj yöntemi.
- Her kanalın direnç değerleri, filtre değerleri ve güvenli ADC giriş aralığı.
- MCP kullanılacaksa tam model ve bağlantı topolojisi.

Bunlar stok eksikliği değil; analog ön uç tasarımı/doğrulaması kapsamında kalan teknik kayıtlardır.

## 5. Kapanış notu

Kullanıcı, listelenen donanımların tamamının elinde olduğunu ve eksik parça olmadığını bildirmiştir. Bu sayfa fiziksel envanter beyanını kaydeder; tek başına elektriksel güvenlik veya analog ölçüm doğrulama kanıtı değildir.

## 6. Akım trafosu modülü — kutu içindeki mevcut parçalar

**Yerleşim:** Bu parçalar, kullanıcının SCT013 sinyalinin ESP32D2'ye bağlandığını belirttiği mevcut akım trafosu kutusunun içindedir. Ayrı bir stok kalemi olarak değil, **akım trafosu modülünün mevcut iç bileşenleri** olarak kaydedilmiştir.

| Bileşen | Özellik / model | Kayıt dayanağı |
|---|---|---|
| İzolasyon trafosu | **RN130421**, 230 V AC / 6 V AC, 2.0 VA, EI 30/15.5, PCB tipi | Kullanıcının paylaştığı üretici teknik dokümanı |
| Köprü doğrultucu | **KBU610** | Kullanıcı bildirimi |
| Filtre kondansatörleri | Mevcut; adet ve değerleri henüz belirlenmedi | Kullanıcı bildirimi |
| 3.3 V regülatör entegresi | Mevcut; parça/model numarası henüz belirlenmedi | Kullanıcı bildirimi |

### RN130421 üretici dokümanı bilgileri

- Primer: 230 V AC, 50–60 Hz.
- Sekonder: 6 V AC.
- Nominal çıkış gücü: 2.0 VA.
- Nominal sekonder akımı: 0.333 A.
- Yüksüz çıkış gerilimi: 9.30 V.
- İzolasyon test gerilimi: 4000 V / 50 Hz.
- Güvenlik sınıfı: II; kısa devre dayanımlı (dokümandaki “Short-Circuit Proof” ifadesi).
- Maksimum ortam sıcaklığı: 60 °C.
- Yapı: vakum altında kapsüllenmiş, bölünmüş bobin (split-bobbin), PCB pinli EI 30/15.5.

**İşlevsel zincir — henüz bağlantı ölçümüyle doğrulanmadı:** 230 V AC → RN130421 → KBU610 köprü doğrultucu → filtre kondansatörleri → 3.3 V regülatör. Bu sıra, bildirilen bileşenlerden çıkarılan teknik yerleşim yorumudur; kart üzerindeki izler ve pin bağlantıları henüz takip edilmedi.

**Kayıt sınırı:** 3.3 V çıkışın varlığı kullanıcı tarafından bildirildi. Regülatörün tam modeli, kondansatör değerleri, doğrultucu çıkış gerilimi ve 3.3 V hattının ESP32D2'ye hangi pin/bağlantı üzerinden gittiği henüz doğrulanmadı. Şebeke tarafı bağlantılar enerjiliyken incelenmeyecek.

