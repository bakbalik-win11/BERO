# Proje durumu

**Son güncelleme:** 2026-10-27  
**Aktif faz:** Faz 0 — hazırlık ve güvenlik  
**Aktif görev:** [T001 — Fiziksel donanım envanteri](tasks/T001-hardware-inventory.md)  
**Öncelikli SCT:** SCT013-030 (30 A / 1 V)  
**PZEM:** Kullanıcının paylaştığı görseldeki modül PZEM-004T V3.0 olarak kaydedildi; 10 A / 100 A varyantı ve CT modeli henüz net değil.  
**Bias üretim alt devresi:** **TAMAMLANDI — kullanıcı onayı.** RN130421 6 V / 2,0 VA + KBU6M köprü + 2200 µF / 35 V filtre kondansatörü + L78L33; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) seramik kondansatör. Bağımsız ölçüm raporu bu kayda eklenmedi.  
**SSR:** Mevcut BERO SSR referansı projeye kopyalandı; fiziksel model kaynak kayıtta da doğrulanmamış.  
**Deney durumu:** YAPILMADI.

## Bildirilen stok

| Bileşen | Adet | Kaynak |
|---|---:|---|
| SCT013-030 (30 A / 1 V) | 7 | Kullanıcı bildirimi |
| SCT013-100A-1V | 10 | Kullanıcı bildirimi |
| 100 nF / 50 V seramik kondansatör | 10 başlangıç stoku | Kullanıcı bildirimi; 1 adedi bias bölücüsünde kullanılıyor |
| ESP32-WROOM-32D | 2 | Kullanıcı bildirimi |
| ESP32-WROOM-32E | 1 | Kullanıcı bildirimi |
| ESP32-WROOM-32S | 1 | Kullanıcı bildirimi |

**Not:** Stok miktarları bağımsız fiziksel sayım değildir. PZEM fotoğrafı bu sohbette paylaşılmıştır; görsel dosyası henüz depodaki `hardware/photos/` klasörüne alınmadı.

## Mevcut bilgi
- BERO'daki SCT, PZEM, ESP32-WROOM-32D, MCP3208 ve SSR teknik kaynakları proje referanslarına bağlandı.
- Bias üretim alt devresi, kullanıcının tamamlandı onayıyla kapatıldı. SCT sinyalinin 1,65 V noktasına kuplajı ana analog ön uç bağlantısıdır; bu ayrı konudur.
- PZEM-004T V3.0 ailesi belirlendi; bu modülün 10 A dahili şönt / 100 A harici CT varyantı ve CT'si henüz belirlenmedi.
- Kullanılabilir ESP32 modül stokları kaydedildi; bu projede kullanılacak gerçek modül/kart henüz seçilmedi.
- SSR kaynak klasörü var ve proje kopyası eklendi; gerçek SSR modeli, giriş/çıkış türü ve yük kapasitesi doğrulanmadı.
- Başlangıç tasarım değerleri: 2 kS/s, nominal 200 ms SCT penceresi ve yaklaşık 1 s PZEM sorgusu. Bunlar deneyle doğrulanmış sonuç değildir.

## Karar kapıları
- [ ] G1 — Faz 1 sonunda: SCT RMS kalibrasyonu önceden belirlenmiş hata hedefinde ve clipping yok.
- [ ] G2 — Faz 3 sonunda: PZEM okuma durumu izleniyor; geçersiz okumalar özetlerden dışlanıyor.
- [ ] G3 — Faz 6 sonunda: örnekleme hızı hedef yüklerde ölçülmüş metriklerle gerekçelendirilmiş.

## Sıradaki işler
1. [ ] [T001 — Donanım envanteri](tasks/T001-hardware-inventory.md): PZEM varyantı/CT, gerçek MCU/ADC ve kalan analog ön uç bağlantılarını netleştir. Bias üretim alt devresi tamamlandı.
2. [ ] [T002 — Güvenlik kontrolü](tasks/T002-safety-checklist.md): şebeke bağlantısı öncesi yetkin kişi incelemesi.
3. [ ] [T003 — Referans ve hata hedefi](tasks/T003-reference-and-error-target.md): referans cihazı, en az üç yük seviyesi ve ölçüm öncesi kabul hedefi.

## Açık engeller
- PZEM'in 10 A / 100 A fiziksel varyantı ve CT'si.
- Projede kullanılacak ESP32 varyantı/kartı, gerçek ADC ve VREF.
- SCT AC sinyalinin tamamlanmış 1,65 V bias noktasına nasıl kuplaj yaptığı ve analog ön uç değerleri.
- SSR projede kullanılacaksa tam model, giriş/çıkış türü ve yük kapasitesi.
- True-RMS referans cihazı, kontrollü yük kimlikleri ve E01–E06 deneyleri.

Firmware, deney ve kalibrasyon sonuçları henüz eklenmedi.
