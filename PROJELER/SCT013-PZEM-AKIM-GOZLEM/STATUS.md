# Proje durumu

**Son güncelleme:** 2026-10-27  
**Aktif faz:** Faz 0 — hazırlık ve güvenlik  
**Aktif görev:** [T001 — Fiziksel donanım envanteri](tasks/T001-hardware-inventory.md)  
**Öncelikli SCT:** SCT013-030 (30 A / 1 V)  
**PZEM:** Esas kaynak [DONANIM/PZEM-004T/README.md](../../DONANIM/PZEM-004T/README.md); CT modeli kullanıcı tarafından **PZCT-02 (0–100 A)** olarak belirtildi ve PZEM'e bağlı olduğu fotoğrafta gösterildi. Yapılandırma 100 A harici CT'li PZEM düzenidir.  
**Bias üretim alt devresi:** **TAMAMLANDI — kullanıcı onayı.** RN130421 6 V / 2,0 VA + KBU6M köprü + 2200 µF / 35 V filtre kondansatörü + L78L33; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) seramik kondansatör. Bağımsız ölçüm raporu bu kayda eklenmedi.  
**SSR:** SAMM Market'ten alınan 5 V, 2 kanallı OMRON SSR kartı (tedarikçi kodu İzmo9659, SKU MP02637) proje donanımına dahil edildi. Ürün sayfası: fototriyak, zero-cross, kanal başına 75–264 VAC ve 0,1–2 A. Giriş LOW/HIGH açıklamasıyla “low-level trigger” notu arasında tutarsızlık var; kontrol mantığı test edilmeli. Kart üzerindeki SSR'nin tam parça kodu okunmadı.  
**RTC:** DS3231 kullanılacak; teknik özellikler üretici veri sayfasıyla kontrol edildi ve [proje referansına](hardware/references/DS3231.md) kopyalandı. Gerçek breakout revizyonu, I²C pinleri, pull-up seviyesi ve yedek pil düzeni henüz doğrulanmadı.  
**Deney durumu:** YAPILMADI.

## Bildirilen stok

| Bileşen | Adet | Kaynak |
|---|---:|---|
| SCT013-030 (30 A / 1 V) | 7 | Kullanıcı bildirimi |
| SCT013-100A-1V | 10 | Kullanıcı bildirimi |
| 100 nF / 50 V seramik kondansatör | 10 başlangıç stoku | Kullanıcı bildirimi; 1 adedi bias bölücüsünde kullanılıyor |
| ESP32-WROOM-32D geliştirme kartı | 2 | Kullanıcı bildirimi ve görsel; bağımsız sayım yapılmadı |
| ESP32-WROOM-32E geliştirme kartı | 1 | Kullanıcı bildirimi ve görsel; bağımsız sayım yapılmadı |
| ESP-WROOM-32 tabanlı NodeMCU ESP32 Bluetooth kartı | 1 | Kullanıcı bildirimi ve görsel; tam PCB revizyonu okunmuyor |

**Not:** Stok miktarları bağımsız fiziksel sayım değildir. PZEM fotoğrafı mevcut donanım/CT bağlantısını göstermek içindi; kaynak kayıt zaten `DONANIM/PZEM-004T` altında bulunduğundan fotoğrafı ayrıca depoya kopyalamak gerekmiyor.

## Mevcut bilgi
- BERO'daki SCT, PZEM, ESP32-WROOM-32D, MCP3208, SSR ve DS3231 teknik kaynakları proje referanslarına bağlandı.
- Bias üretim alt devresi, kullanıcının tamamlandı onayıyla kapatıldı. SCT sinyalinin 1,65 V noktasına kuplajı ana analog ön uç bağlantısıdır; bu ayrı konudur.
- PZEM donanım kaydı mevcut BERO belgesinden kullanılıyor. Bağlı CT, kullanıcı tarafından PZCT-02 (0–100 A) olarak tanımlandı; bu proje 100 A harici CT düzeni olarak kaydedildi.
- İlk aşamada kullanılacak dört ESP32 geliştirme kartı belirlendi: 2× WROOM-32D, 1× WROOM-32E ve 1× genel ESP-WROOM-32 NodeMCU ESP32 Bluetooth. Genel kartın PCB revizyonu görselden kesinleşmedi.
- İki kanallı SSR için satıcı ürün sayfası ve elektriksel sınırlar kaydedildi; giriş tetik mantığı, giriş akımı, kanal eşzamanlı yük/termal sınırları ve fiziksel SSR parça kodu ayrıca doğrulanacak.
- DS3231 ölçüm/olay kayıtlarına takvim zamanı sağlamak için seçildi. BERO'da önceki RTC/NTP okuma örneği var; bu yeni projede pil yedeği veya kesinti testi yapılmış sayılmaz.
- Başlangıç tasarım değerleri: 2 kS/s, nominal 200 ms SCT penceresi ve yaklaşık 1 s PZEM sorgusu. Bunlar deneyle doğrulanmış sonuç değildir.

## Karar kapıları
- [ ] G1 — Faz 1 sonunda: SCT RMS kalibrasyonu önceden belirlenmiş hata hedefinde ve clipping yok.
- [ ] G2 — Faz 3 sonunda: PZEM okuma durumu izleniyor; geçersiz okumalar özetlerden dışlanıyor.
- [ ] G3 — Faz 6 sonunda: örnekleme hızı hedef yüklerde ölçülmüş metriklerle gerekçelendirilmiş.

## Sıradaki işler
1. [ ] [T001 — Donanım envanteri](tasks/T001-hardware-inventory.md): ADC/VREF'i, SCT'nin bias noktasına kuplajını ve analog ön uç değerlerini netleştir. İlk aşamadaki dört ESP32 kartı, PZEM/PZCT-02 ve bias üretim alt devresi kayıtlı.
2. [ ] [T002 — Güvenlik kontrolü](tasks/T002-safety-checklist.md): şebeke bağlantısı öncesi yetkin kişi incelemesi.
3. [ ] [T003 — Referans ve hata hedefi](tasks/T003-reference-and-error-target.md): referans cihazı, en az üç yük seviyesi ve ölçüm öncesi kabul hedefi.

## Açık engeller
- PZEM için mevcut BERO kaydı ve bağlı PZCT-02 (0–100 A) bilgisi kaydedildi. MCU bağlantısında UART lojik seviyesi ve izolasyon düzeni uygulama öncesinde doğrulanmalı.
- Fiziksel ADC modeli ve VREF kaynağı/değeri; genel NodeMCU kartının tam PCB revizyonu kablolama öncesinde görsel/üretici bilgisiyle doğrulanmalı.
- DS3231 breakout revizyonu, I²C pinleri/pull-up gerilimi, yedek pil türü ve ilk saat ayarlama yöntemi belirlenmeli.
- SCT AC sinyalinin tamamlanmış 1,65 V bias noktasına nasıl kuplaj yaptığı ve analog ön uç değerleri.
- SSR'nin hangi iki AC yükü anahtarlayacağı, kontrol GPIO'ları ve test öncesi giriş mantığının düşük gerilimde doğrulanması.
- True-RMS referans cihazı, kontrollü yük kimlikleri ve E01–E06 deneyleri.

Firmware, deney ve kalibrasyon sonuçları henüz eklenmedi.
