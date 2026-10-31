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

## Modül 2 — SCT Okuma Test Modülü

- **Kutu içeriği:** 3 adet SCT jack girişi, ESP32D2 assembly (ESP32 kartı + GPIO shield) ve bias mini breadboard.
- **Kutu dışında:** 220 V AC giriş/çıkış, PZEM, SSR ve kutu içi 5 V güç kaynağı.
- **Besleme:** Bias ayrı Bias Trafosu modülünden; ESP32 harici 5 V kaynaktan beslenecek. ESP kart modeli ve USB konektör tipi henüz kesinleştirilmedi.
- **Sinyal düzeni:** Kullanıcı bildirimine göre kırmızı ortak bias hattı; mavi, yeşil ve sarı ayrı SCT sinyal hatları. Jack tip/ring/sleeve eşlemesi fiziksel olarak doğrulanmadı.
- **ADC hedefi:** Tasarım adayı 3 bağımsız SCT sinyali + 1 ortak bias/Vmid izleme noktasıdır. Kesin GPIO/pin planı ve RAW/voltaj sensör tercihi Faz 2 uygulamasında netleştirilecektir.
- **Durum:** Taslak; bağlantı ve firmware uygulanmadı/doğrulanmadı.
- **Kararlar:** [ADR-012](docs/decisions/ADR-012-sct-test-module-scope.md), [ADR-013](docs/decisions/ADR-013-bias-adc-channel-selection.md).

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
