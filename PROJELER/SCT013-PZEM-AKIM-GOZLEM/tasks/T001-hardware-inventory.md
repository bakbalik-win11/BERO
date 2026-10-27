# T001 — Fiziksel donanım envanteri

- **Durum:** DEVAM EDİYOR
- **Faz:** 0.1
- **Bağımlılık:** Yok
- **Hedef:** Önceki BERO kayıtlarını yeniden toplatmadan kullanmak; seçilmiş donanımı, kullanıcı tarafından bildirilen stokları ve yalnızca kalan proje-özel bilgileri kaydetmek.

## Önceden mevcut referanslar
- [SCT013-100A-1V](../hardware/references/SCT013-100A-1V.md)
- [SCT013-30A-1V](../hardware/references/SCT013-30A-1V.md)
- [PZEM-004T V3.0](../hardware/references/PZEM-004T-V3.0.md)
- [SSR donanım referansı](../hardware/references/SSR.md)
- [SSR aday veri sayfası notu](../hardware/references/SSR-datasheet-candidate.md)
- [Referans indeksi](../hardware/references/README.md)

Genel teknik özellikleri tekrar yazma. Önceden var olan kaynaklardan yararlan; proje için verilmiş kararları yeniden sorma.

## Yapılan / tamamlanan
- SCT013-030 (30 A / 1 V) bu projede öncelikli seçim.
- Kullanıcı bildirimi olarak 7 adet SCT013-030, 10 adet SCT013-100A-1V, 10 adet 100 nF / 50 V seramik kondansatör, 2 adet ESP32-WROOM-32D, 1 adet ESP32-WROOM-32E ve 1 adet ESP32-WROOM-32S kaydedildi.
- PZEM için mevcut BERO donanım kaydı esas alındı; bağlı CT modeli kullanıcı tarafından PZCT-02 (0–100 A) olarak belirtildi.
- **Temiz yaklaşık 1,65 V bias üretim alt devresi tamamlandı (kullanıcı onayı):** kutuda RN130421 + KBU6M + 2200 µF / 35 V + L78L33; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) kondansatör.
- SSR donanım referansı proje referans klasörüne kopyalandı. Fiziksel model doğrulanmadı; projede kullanılması henüz kararlaştırılmadı.

## Kalan işler
1. **Tamamlandı:** mevcut [DONANIM/PZEM-004T/README.md](../../../DONANIM/PZEM-004T/README.md) kaydı esas alındı; kullanıcı bağlı CT modelini PZCT-02 (0–100 A) olarak belirtti. Fotoğraf CT'nin bu PZEM'e bağlı olduğunu göstermek içindi. Bu bilgiyi yeniden sorma veya yeni PZEM donanım belgesi açma.
2. Bu projede kullanılacak ESP32 modülünü ve geliştirme kartı/revizyonunu belirle; 2×D, 1×E, 1×S stok bilgisini yeniden sorma.
3. Kullanılacak ADC modelini/revizyonunu ve VREF kaynağını kaydet.
4. SCT sinyalinin tamamlanmış bias orta noktasına hangi bağlantıyla kuplaj yaptığını; burden/analog filtre değerlerini ve güvenli ADC aralığını kaydet.
5. True-RMS referans cihazı ve üç kontrollü yük düzeyini T003 görevine bağla.
6. SSR bu projede kullanılacaksa model etiketini doğrula; kullanılmayacaksa yalnız mevcut BERO referansı olarak bırak.

## Kabul ölçütü
Her satır ya bilinen kanıt/referansa bağlanmış olmalı ya da yalnız gerçekten karara bağlanmamış proje-özel bir konu olarak kalmalı. Bildirilen stok miktarları fiziksel sayım gibi sunulmaz; tamamlandı denilen bias kurulumuna tekrar bileşen soruları yöneltilmez.

## Çıktılar
- `hardware/inventory.md`
- Gerekiyorsa `hardware/photos/`
- `docs/open-questions.md`

## Güvenlik
Bu görev dokümantasyon ve görsel incelemedir. Şebeke bağlantısını sökme, kabloyu ayırma veya sisteme enerji verme.
