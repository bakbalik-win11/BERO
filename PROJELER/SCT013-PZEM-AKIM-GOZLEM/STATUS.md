# Proje durumu

**Son güncelleme:** 2026-10-27  
**Aktif faz:** Faz 0 — hazırlık ve güvenlik  
**Aktif görev:** [T001 — Fiziksel donanım envanteri](tasks/T001-hardware-inventory.md) — DEVAM EDİYOR; stok ve hazır analog kart bilgileri işlendi, kalan teknik kabul maddeleri açık.  
**Öncelikli SCT:** SCT013-030 (30 A / 1 V)  
**PZEM:** Esas kaynak [DONANIM/PZEM-004T/README.md](../../DONANIM/PZEM-004T/README.md); CT modeli kullanıcı tarafından PZCT-02 (0–100 A) olarak belirtildi.  
**Bias üretim alt devresi:** TAMAMLANDI — kullanıcı onayı. RN130421 + KBU6M + 2200 µF / 35 V + L78L33; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) kondansatör. Bağımsız ölçüm raporu bu kayda eklenmedi.  
**SCT analog arayüz kartı:** Kullanıcı daha önce 8 kanallı, her kanalı ayrı bias ve direnç ağı bulunan bir kart hazırladı. SCT dişi jack ve breadboard bias devresi üzerinden ESP32 GPIO bacağından okunacak. İlk aşamada harici ADC yok; analog okuma ESP32'nin dahili ADC'si ile yapılacak. MCP3208 mevcut, ileriki aşama için ayrıldı. GPIO numarası henüz belirtilmedi.  
**SCT/PZEM etiketleme ve kalibrasyon hedefi:** [Hedef mimari notu](docs/architecture/sct-pzem-labeling-and-calibration.md) — zaman damgası/sabit süre odaklı değil, paket bağlamı ve PZEM/SCT kararlı alanlarını algoritma-istatistikle belirleyip etiketleme; Python'da etiketli SCT verisiyle sensör başına katsayı/`f(x)` modeli çıkarma; ardından modeli çok paketli ham akışta sınayıp gerekirse iyileştirme. Firmware, algoritma ve deneyler henüz yapılmadı.  
**SSR:** SAMM Market 5 V, 2 kanallı kart; tedarikçi kodu İzmo9659, SKU MP02637. Giriş mantığı ve kart üzerindeki SSR'nin tam kodu doğrulanmalı.  
**RTC:** DS3231 kullanılacak; gerçek breakout revizyonu, I²C pinleri, pull-up seviyesi ve yedek pil düzeni henüz doğrulanmadı.  
**Deney durumu:** YAPILMADI.

## Bildirilen stok

| Bileşen | Adet / özellik | Kaynak |
|---|---:|---|
| SCT013-030 (30 A / 1 V) | 7 | Kullanıcı bildirimi; jack çıkışlı |
| SCT013-100A-1V | 10 | Kullanıcı bildirimi; jack çıkışlı |
| SCT013 toplamı | 17 | Kullanıcı bildirimi |
| ESP32-C3 SuperMini | 1 | Kullanıcı bildirimi / önceki SSR düğümü |
| ESP32 ölçüm düğümü | 1 | Kullanıcı bildirimi / önceki PZEM düğümü |
| PZEM-004T | V3.0 | Kullanıcı bildirimi |
| Masaüstü güç kaynağı | 5 V / 1,8 A | Kullanıcı bildirimi |
| Test yükü | Lamba | Kullanıcı bildirimi |
| 8 kanallı analog arayüz | Kanal başına ayrı bias ve direnç ağı | Kullanıcı bildirimi; önceden hazırlanmış |
| Jack yuvaları ve bağlantı/ölçüm parçaları | Tam takım mevcut | Kullanıcı bildirimi |

## Mevcut bilgi
- Önceki BERO'daki SCT, PZEM, ESP32, MCP3208, SSR ve DS3231 teknik kaynakları proje referanslarına bağlandı.
- Bias üretim alt devresi, kullanıcının onayıyla tamamlandı sayılıyor; bağımsız voltaj ölçüm raporu eklenmedi.
- SCT013 sinyalinin jack üzerinden 8 kanallı, her kanalı ayrı bias/dirençli arayüze ve oradan ESP32 ADC'ye aktarılacağı kullanıcı tarafından belirtildi. MCP ADC opsiyonel; model seçimi doğrulanmadı.
- PZEM için mevcut BERO kaydı kullanılıyor; bağlı CT modeli PZCT-02 (0–100 A) olarak belirtildi.
- SSR kartının tam giriş tetik mantığı ve fiziksel SSR parça kodu doğrulanmalı.
- Deneyler ve kalibrasyon sonuçları henüz eklenmedi.

## Karar kapıları
- [ ] G1 — SCT RMS kalibrasyonu hata hedefinde ve clipping yok.
- [ ] G2 — PZEM okuma durumu izleniyor; geçersiz okumalar özetlerden dışlanıyor.
- [ ] G3 — örnekleme hızı hedef yüklerde ölçülmüş metriklerle gerekçelendirilmiş.

## Sıradaki işler
1. [ ] T001: SCT hızlı örnekleme amacı netleştirildi: 2 × ESP32-WROOM-32D ve 1 × ESP32-WROOM-32E ayrı kanallarda ham/anlık sensör gerilimlerini okuyacak; SSR-zamanlayıcı düğümünden gelen paket bilgisiyle birlikte yazdırılacak. Bu aşamada akım/RMS hesabı yapılmayacak. Dahili ADC GPIO'ları ve analog kuplaj ayrıntıları hâlâ doğrulanmalı.
2. [ ] [T002 — Güvenlik kontrolü](tasks/T002-safety-checklist.md): şebeke bağlantısı öncesi yetkin kişi incelemesi.
3. [ ] [T003 — Referans ve hata hedefi](tasks/T003-reference-and-error-target.md): referans cihazı, en az üç yük seviyesi ve ölçüm öncesi kabul hedefi.

## Açık engeller
- Üç SCT örnekleme kartının dahili ADC GPIO eşlemesi ve her girişin güvenli aralığı doğrulanmalı; genel NodeMCU kartının tam PCB revizyonu, kullanılacaksa kablolama öncesinde doğrulanmalı.
- SCT AC sinyalinin tamamlanmış 1,65 V bias noktasına kuplajı, kanal direnç/filtre değerleri ve güvenli ADC aralığı.
- DS3231 breakout revizyonu, I²C pinleri/pull-up gerilimi, yedek pil türü ve ilk saat ayarlama yöntemi.
- SSR'nin hangi iki AC yükü anahtarlayacağı, GPIO eşlemesi ve giriş mantığının düşük gerilimde doğrulanması.
- True-RMS referans cihazı, kontrollü yük kimlikleri ve E01–E06 deneyleri.

Firmware, deney ve kalibrasyon sonuçları henüz eklenmedi.
