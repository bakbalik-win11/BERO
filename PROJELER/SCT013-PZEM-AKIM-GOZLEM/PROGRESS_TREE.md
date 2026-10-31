# BERO — İlerleme Ağacı

## Güncel konum

**FAZ 2 AKTİF — pratik yeniden kurulum ve sistem geliştirme.** Faz 1'de çalışan akım okuma kod yolu bulundu ve kullanıcının dört karşılaştırmasında ±%4 hedefi sağlandı. Faz 2'de sistem modül modül yeniden devreye alınacak; PZEM referanslı veri işleme daha sonraki alt aşamadır.

## İki fazlı proje ağacı

- **FAZ 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak: TAMAMLANDI**
  - Dış kaynaklı ESPHome ct_clamp kodu kullanıldı.
  - 100 W akkor: yaklaşık %0 sapma.
  - 150 W akkor: −%0,2.
  - Kettle düşük/kararlı: +%3,0.
  - Kettle kaynama: −%3,8.
  - Yapılmamış Faz 1 işleri hedefe ulaşıldığı için kapatıldı; kayıtlar arşivde.

- **FAZ 2 — Pratik yeniden kurulum ve sistem geliştirme: AKTİF**
  1. **T009 — Modül/ESP devreye alma üst görevi:** DEVAM EDİYOR.
  2. **T010 — Modül 2 ESP32D1 üçlü SCT + tek ortak bias modülü:** AKTİF.
  3. **T007 — HA → PC veri aktarımı:** PZEM/SCT entity'leri çalışınca.
  4. **T008 — PZEM/SCT kararlı alan eşleştirme/etiketleme:** T007 sonrasında.
  5. **T006 — K=24.22 katsayı/model değerlendirmesi:** T008 sonrasında.

## Faz 2 geliştirme ilkesi

Önce çalışan kod/örnek bulunur, donanım doğrulanır ve tek modül tek işlev şeklinde devreye alınır. Teori ve iç mimari araştırması yalnız somut arıza, uygulama engeli veya karar ihtiyacı varsa derinleştirilir. Başarılı kod ile gerçek log/çıktı ve yorum depoda saklanır. Eski YAML ve araştırmalar tarihsel referans olarak korunur; yeni donanımda test edilmiş sayılmaz.

## Korunan referans

- E00F ESP32D2 YAML ve eski ESP yapılandırmaları kayıtlıdır; yeni kurulumun değiştirilemez şablonu değildir.
- 200 ms pencere, 2 s yayın ve K=24.22 önceki çalışan ölçüm yolunun tarihsel değerleridir.
- Yeni üç SCT + bias Modül 2 bağlantısı ve yeni ESP pin eşlemesi henüz doğrulanmadı.

### 2026-10-31 ilk firmware açılışı

- Dört ADC sensörü (GPIO32/33/34/35) logda başlatıldı; tüm ADC setup durumları OK.
- ESPHome 2026.10.1 firmware'i açıldı; Wi-Fi/API bağlantısı başarılı.
- GPIO35 ortak bias örnekleri 1.643–1.668 V.
- SCT/ampul bağlantısı yoktu; üç SCT kanalı için 100 W test sonucu değildir.
- [İlk açılış log kanıt dökümü](logs/module2/2026-10-31-first-boot-no-load.txt).
- **T010:** Firmware açılışı ve ADC başlatma LOG İLE DESTEKLENDİ; 100 W kanal testleri bekliyor.

## Modül 2 — Üçlü SCT Okuma Modülü

- **ESPHome kimliği:** `esp32d1` / `ESP32D1`; temel başlangıç YAML'ı eklendi.
- **Kutu içeriği:** 3 SCT jack girişi, gömülü ESP32 kartı + GPIO shield, ortak bias mini breadboard.
- **Besleme:** ESP32 harici 5 V DC ile beslenecek; USB portundan PC bağlantısına erişim bulunacak.
- **Bias:** Tek kayıtlı bias devresi; tek ortak bias beslemesi üç SCT girişine dağıtılacak. Ortak bias düğümü tek ADC noktasından izlenecek.
- **ADC hedefi:** 3 bağımsız SCT sinyali + 1 ortak bias izleme = 4 ADC giriş noktası.
- **Bildirilen eşleştirmeler:** 1. dişi yuva sarı → GPIO32; 2. dişi yuva yeşil → GPIO33; 3. dişi yuva mavi → GPIO34; ortak bias turuncu → GPIO35.
- **Açık noktalar:** ESP32 kart/shield modeli, jack tip/ring/sleeve pinout'unun fiziksel teyidi, USB ile harici 5 V'un birlikte kullanım koşulları, bias ADC RAW/voltaj gösterimi.
- **Durum:** Tasarım tanımlandı; fiziksel bağlantı, YAML sensörleri, derleme ve donanım testi yapılmadı.
- **Görev:** [T010](tasks/T010-module2-triple-sct-bringup.md).
- **Karar:** [ADR-015](docs/decisions/ADR-015-module2-esp32d1-triple-sct.md).

## Dosya navigasyonu

| Bilgi | Dosya |
|---|---|
| Güncel durum | [STATUS.md](STATUS.md) |
| Yol haritası | [ROADMAP.md](ROADMAP.md) |
| Görev sırası | [tasks/README.md](tasks/README.md) |
| İlk aktif görev | [T009](tasks/T009-practical-system-bringup.md) |
| HA → PC aktarımı | [T007](tasks/T007-python-architecture.md) |
| Kararlı alan eşleştirme | [T008](tasks/T008-pzem-sct-stable-window-labeling.md) |
| Katsayı/model değerlendirmesi | [T006](tasks/T006-calibration.md) |
| Faz 1 deney geçmişi | [Deney arşivi](experiments/README.md) |
| Yeni Faz 2 kararı | [ADR-014](docs/decisions/ADR-014-phase2-practical-restart.md) |

## HEDEF / LOG / SONUÇ

- **HEDEF:** Faz 2'nin pratik başlangıç yaklaşımını, görev sırasını ve Modül 2'nin mevcut tasarım durumunu tek görünümde göstermek.
- **LOG:** ADR-014, T009 ve ana proje yönergeleri oluşturuldu/güncellendi.
- **SONUÇ:** Faz 1 tamamlandı; Faz 2 pratik yeniden kurulum ve geliştirme olarak aktif. T009 ilk görev. Bu belge donanımın çalıştığına veya firmware'in test edildiğine kanıt değildir.
