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
  1. **T009 — Modülleri/ESP düğümlerini yeniden devreye alma:** AKTİF.
  2. **T007 — HA → PC veri aktarımı:** T009 sonrasında, PZEM/SCT entity'leri çalışınca.
  3. **T008 — PZEM/SCT kararlı alan eşleştirme/etiketleme:** T007 sonrasında.
  4. **T006 — K=24.22 katsayı/model değerlendirmesi:** T008 sonrasında.

## Faz 2 geliştirme ilkesi

Önce çalışan kod/örnek bulunur, donanım doğrulanır ve tek modül tek işlev şeklinde devreye alınır. Teori ve iç mimari araştırması yalnız somut arıza, uygulama engeli veya karar ihtiyacı varsa derinleştirilir. Başarılı kod ile gerçek log/çıktı ve yorum depoda saklanır. Eski YAML ve araştırmalar tarihsel referans olarak korunur; yeni donanımda test edilmiş sayılmaz.

## Korunan referans

- E00F ESP32D2 YAML ve eski ESP yapılandırmaları kayıtlıdır; yeni kurulumun değiştirilemez şablonu değildir.
- 200 ms pencere, 2 s yayın ve K=24.22 önceki çalışan ölçüm yolunun tarihsel değerleridir.
- Yeni üç SCT + bias Modül 2 bağlantısı ve yeni ESP pin eşlemesi henüz doğrulanmadı.

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

## Modül 2 — SCT Okuma Test Modülü

- **Kutu içeriği:** 3 SCT jack girişi, ESP32D2, bias mini breadboard.
- **Kutu dışında:** 220 V AC giriş/çıkış, PZEM, SSR ve kutu içi 5 V güç kaynağı.
- **Besleme:** Bias ayrı Bias Trafosu modülünden; ESP32D2 besleme yöntemi henüz belirlenmedi.
- **Durum:** Taslak; fiziksel bağlantılar ve jack pin eşlemesi doğrulanmadı.
- **Karar:** [ADR-012](docs/decisions/ADR-012-sct-test-module-scope.md).

# BERO — İlerleme Ağacı

## Güncel konum

**FAZ 2 AKTİF.** Faz 1 tamamlandı: dış kaynaklı çalışan kodla ±%4 sapma hedefi sağlandı. 100 W akkor, 150 W akkor ve kettle'ın iki koşulundaki karşılaştırmaların tamamı sınır içindedir. Faz 1 kapsamında kalan yapılmamış işler hedefe ulaşıldığı için kapatıldı. Eski deneyler tarihsel kayıt olarak korunur.

## İki fazlı proje ağacı

- **FAZ 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak: TAMAMLANDI**
  - Dış kaynaklı ESPHome ct_clamp kodu kullanıldı.
  - 100 W akkor: yaklaşık %0 sapma.
  - 150 W akkor: −%0,2.
  - Kettle düşük/kararlı: +%3,0.
  - Kettle kaynama: −%3,8.
  - ±%4 hedefi sağlandı.
  - Faz 1 kapsamındaki yapılmamış deneyler kapatıldı; eski kayıtlar arşivde.

- **FAZ 2 — Bulunan kodu PZEM ile eğitmek: AKTİF**
  1. **T007 — HA geçmişini PC'ye aktarma:** AKTİF / ilk iş.
  2. **T008 — PZEM/SCT kararlı alan eşleştirme ve etiketleme:** BEKLEMEDE.
  3. **T006 — K=24.22 katsayı/model değerlendirmesi:** BEKLEMEDE.
  4. Yeni veriler geldikçe öğrenme döngüsü tekrarlanır.

## Faz 2 veri akışı

Home Assistant geçmişi → T007 PC aktarımı → Python'da PZEM/SCT akışlarını ayrı inceleme → T008 kararlılık tespiti → örtüşen alanları eşleştirme → PZEM ile etiketleme → T006 katsayı/model değerlendirmesi → yeni calibration_id ve yeni veriyle tekrar.

## Korunan baseline

- ESP32D2 E00F ve mevcut ESPHome ct_clamp yolu.
- 200 ms ölçüm penceresi, 2 s yayın aralığı, K=24.22.
- İlk eşleşmiş veri görülmeden ct_clamp veya firmware değişikliği yok.

## Dosya navigasyonu

| Bilgi | Dosya |
|---|---|
| Güncel aktif iş | [STATUS.md](STATUS.md) |
| İki faz ve karar kapıları | [ROADMAP.md](ROADMAP.md) |
| Görev sırası | [tasks/README.md](tasks/README.md) |
| İlk iş: HA → PC | [T007](tasks/T007-python-architecture.md) |
| Kararlı alan eşleştirme | [T008](tasks/T008-pzem-sct-stable-window-labeling.md) |
| Katsayı/model değerlendirme | [T006](tasks/T006-calibration.md) |
| Python veri hattı | [Mimari](docs/architecture/python-program-architecture.md) |
| Faz 1 deney geçmişi | [Deney arşivi](experiments/README.md) |
| Karar geçmişi | [ADR kayıtları](docs/decisions/) |

## HEDEF / LOG / SONUÇ

- **HEDEF:** Projenin yalnız iki ana fazını görünür kılmak ve Faz 2'nin ilk işini belirlemek.
- **LOG:** Yol haritası, görev listesi, mimari ve deney indeksi iki fazlı yapıya göre düzenlenmiştir.
- **SONUÇ:** Faz 1 kapalı; Faz 2 aktif; T007 ilk görevdir. Python aktarımının uygulandığı anlamına gelmez.
