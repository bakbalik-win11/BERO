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
- Kullanıcı bildirimi olarak 7 adet SCT013-030, 10 adet SCT013-100A-1V ve 10 adet 100 nF / 50 V seramik kondansatör kaydedildi. İlk aşama planı dört ESP32 geliştirme kartıdır: 2× WROOM-32D, 1× WROOM-32E ve 1× genel ESP-WROOM-32 NodeMCU ESP32 Bluetooth; son kartın PCB revizyonu görselden kesinleşmedi.
- PZEM için mevcut BERO donanım kaydı esas alındı; bağlı CT modeli kullanıcı tarafından PZCT-02 (0–100 A) olarak belirtildi.
- **Temiz yaklaşık 1,65 V bias üretim alt devresi tamamlandı (kullanıcı onayı):** kutuda RN130421 + KBU6M + 2200 µF / 35 V + L78L33; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) kondansatör.
- Dört kanallı SSR kartı proje donanımına dahil edildi. Kullanıcı tarafından OMRON olarak tanımlandı; verilen giriş/çıkış sınırları kaydedildi. Tam röle model kodu ve giriş akımı henüz doğrulanmadı.

## Kalan işler
1. **Tamamlandı:** mevcut [DONANIM/PZEM-004T/README.md](../../../DONANIM/PZEM-004T/README.md) kaydı esas alındı; kullanıcı bağlı CT modelini PZCT-02 (0–100 A) olarak belirtti. Fotoğraf CT'nin bu PZEM'e bağlı olduğunu göstermek içindi. Bu bilgiyi yeniden sorma veya yeni PZEM donanım belgesi açma.
2. Kullanılacak ADC modelini/revizyonunu ve VREF kaynağını kaydet; MCP3208'in bu düzeneğe seçildiğini varsayma.
3. SCT sinyalinin tamamlanmış bias orta noktasına hangi bağlantıyla kuplaj yaptığını; burden/analog filtre değerlerini ve güvenli ADC aralığını kaydet.
4. True-RMS referans cihazı ve üç kontrollü yük düzeyini T003 görevine bağla.
5. SSR tam model kodunu mümkünse üst yüzey yazısından doğrula; kontrol GPIO'su ve test yüklerini belirle. Kullanıcı tarafından verilen elektriksel değerleri kesin model veri sayfası gibi sunma.

## Kabul ölçütü
Her satır ya bilinen kanıt/referansa bağlanmış olmalı ya da yalnız gerçekten karara bağlanmamış proje-özel bir konu olarak kalmalı. Bildirilen stok miktarları fiziksel sayım gibi sunulmaz; tamamlandı denilen bias kurulumuna tekrar bileşen soruları yöneltilmez.

## Çıktılar
- `hardware/inventory.md`
- Gerekiyorsa `hardware/photos/`
- `docs/open-questions.md`

## Güvenlik
Bu görev dokümantasyon ve görsel incelemedir. Şebeke bağlantısını sökme, kabloyu ayırma veya sisteme enerji verme.
