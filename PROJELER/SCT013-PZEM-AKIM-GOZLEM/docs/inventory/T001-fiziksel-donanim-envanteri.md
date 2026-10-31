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

## 6. BERO modülü: Bias Trafosu

Bu donanım bağımsız bir **BERO modülü** olarak tanımlanmıştır. Görevi ESP32D2'nin SCT013 ölçüm devresine bias beslemesi sağlamaktır. ESP32'nin ana beslemesi olarak tanımlanmamıştır.

- Modül kimliği: **BERO-BIAS-TRAFOSU-001**
- Modül içeriği: RN130421 izolasyon trafosu, KBU610 köprü doğrultucu, 2200 µF / 35 V filtre kondansatörü ve L78L33 TO-92 regülatör.
- Çıkış ölçümü: **3,31 V DC** (kullanıcının paylaştığı UNI-T UT33D+ fotoğrafı; ölçüm koşulu/yük durumu ayrıca doğrulanmadı).
- Modül bileşenlerinin stok dağılımı ve teknik ayrıntıları: [BERO Bias Trafosu modül belgesi](../modules/BIAS-TRAFOSU.md).

## 7. Konnektör ve bağlantı elemanları

| Bileşen | Model / özellik | Adet | Yerleşim |
|---|---|---:|---|
| 3.5 mm stereo jack dişi, PCB tipi | **PJ-324M** | **15** | Stok; hangi kutu/kartta kaç adet kullanılacağı henüz belirtilmedi |

**Kayıt dayanağı:** Kullanıcının ürün adı, modeli ve adet bildirimi ile paylaştığı ürün fotoğrafı. Fotoğraftaki parça PJ-324M tipi PCB montajlı 3.5 mm stereo dişi jack olarak envantere işlendi. Bu kayıt, 15 adedin tamamının akım trafosu kutusuna takılı olduğu anlamına gelmez.


### 2200 µF filtre kondansatörü — model ve stok ayrıntısı

- **Kapasite:** 2200 µF.
- **Anma gerilimi:** 35 V.
- **Boyut:** 16 × 25 mm.
- **Toplam adet:** 3.
- **Akım trafosu kutusundaki:** 1 adet.
- **Serbest stok:** 2 adet.
- **Kayıt dayanağı:** Kullanıcının model/özellik/adet ve yerleşim bildirimi.

**Not:** Kondansatörün kutudaki görevi filtreleme olarak kaydedilmiştir; devredeki gerçek bağlantı noktası ve polaritesi henüz fiziksel olarak izlenip doğrulanmadı.
