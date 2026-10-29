# Yol haritası

Bir fazın kabul ölçütü sağlanmadan sonraki faz tamamlandı sayılmaz. Kutular yalnız depoda kanıt olduğunda işaretlenir.

## Faz 0 — Hazırlık ve güvenlik
- [x] 0.1 Fiziksel envanter ve kullanıcı tarafından bildirilen hazır bias alt devresini kaydet. — [T001](tasks/T001-hardware-inventory.md)
  - **Mevcut kayıt:** Kullanıcı 7 adet SCT013 30 A / 1 V, 10 adet SCT013 100 A / 1 V, jack yuvaları, masaüstü 5 V / 1,8 A güç kaynağı, lamba yükü ve breadboard bias alt devresinin hazır olduğunu bildirdi. Ayrıntılar [envanterde](hardware/inventory.md) ve [T001 envanter notunda](docs/inventory/T001-fiziksel-donanim-envanteri.md).
  - **Kapanış:** kullanıcı tarafından bildirilen envanter ve bias alt devresi kaydedildi. Elektriksel kuplaj/ADC aralığı T004 kapsamındadır; bu T001'i açık tutmaz.
- [x] 0.2 220–240 V güvenlik kontrolleri. — [T002](tasks/T002-safety-checklist.md)
  - **Kapanış:** kullanıcı 2026-10-27 tarihinde listedeki tüm kontrolleri tamamladığını beyan etti. Kapanış kullanıcı beyanına dayanır; asistanın bağımsız fiziksel doğrulaması değildir.
- [x] 0.3 PZEM'e göre model kabul hata hedefini tanımla. — [T003](tasks/T003-reference-and-error-target.md) — [T003](tasks/T003-reference-and-error-target.md)
  - **Bitti sayılır:** PZEM'e göre ±%4 bağıl sapma hedefi ve Python `OK` karar kuralı tanımlanmış. Kullanılacak yükler ilgili test sırasında kullanıcı tarafından beyan edilir.

## Faz 1 — SCT analog ön uç
- [x] 1.1 Mevcut SCT jack bağlantısını, breadboard bias alt devresini ve ESP32 dahili ADC yaklaşımını hobi projesi kapsamında belgele. — [T004](tasks/T004-analog-frontend.md)
  - **Kapanış:** Kullanılan SCT modelleri ve jack çıkışı, 2 × 10 kΩ orta nokta, orta noktadan GND'ye 100 nF kondansatör, yaklaşık 1,65 V bias kabulü ve dahili ADC yaklaşımı kaydedildi. Laboratuvar düzeyinde bias/ADC aralığı/clipping ölçümü bu görevin şartı değil.
- [ ] 1.2 Hatta akım yokken ADC ofseti ve gürültü tabanını ölçüp zaman grafiğinde incele. — [T005](tasks/T005-noise-floor.md)
  - **Başlangıç:** Donanım henüz kurulmadı. PZEM ve ESP kartları ölçülen hattan beslenmiyor. 30 saniye asgari başlangıç referansı; kayıt daha uzun, gerekirse saatler sürebilir. Kesin süre deney sırasında belirlenecek.
- [ ] 1.3 En az üç seviyede kalibrasyon yap. — [T006](tasks/T006-calibration.md)
  - **Bitti sayılır:** önceden belirlenmiş hata hedefi sağlanmış; clipping yok; calibration_id kayıtlı.

## Faz 2 — SCT edinim
- [ ] 2.1 Gerçek örnekleme hızını ve sapmayı ölç.
- [ ] 2.2 2 kS/s ve nominal 200 ms penceresini dene.
- [ ] 2.3 RMS, ADC ortalaması, min/max, örnek sayısı ve clipping sayaçlarını üret.
  - **Bitti sayılır:** kararlı yükte pencere değişkenliği raporlanmış.

## Faz 3 — PZEM edinim
- [ ] 3.1 Yaklaşık 1 s sorgu başlangıcı; istek/yanıt zamanları ve read_status kaydı.
- [ ] 3.2 V/I/P/PF alanlarının değişim zamanlarını ayrı incele.
- [ ] 3.3 Sentinel, timeout ve parse hatalarını ayıkla.
  - **Bitti sayılır:** en az 10 dakikalık kayıt ve hata oranı var.

## Faz 4 — Zaman hizalama
- [ ] 4.1 Tek monotonik saat kaynağı kullan.
- [ ] 4.2 SCT RMS değişimiyle olay algıla.
- [ ] 4.3 Olay sonrası yaklaşık 3 s'yi başlangıç transition_or_settling etiketi yap.
  - **Bitti sayılır:** geçiş/kararlı kayıtlar ayrılmış; süre cihaz deneyine göre gözden geçirilmiş.

## Faz 5 — Kayıt şeması
- [ ] 5.1 Zorunlu ve önerilen alanları uygula, örnek kayıtları doğrula.
- [ ] 5.2 Olay tamponu prosedürünü belirle.
  - **Bitti sayılır:** bir saatlik örnek kayıt şema ile uyumlu; olay kesiti test edilmiş.

## Faz 6 — Deneyler
- [ ] 6.1 E03: dirençli yük aç/kapat, en az 5 tekrar.
- [ ] 6.2 E04: PZEM alanlarının değişim zamanı.
- [ ] 6.3 E05: aynı yükte 1 / 2 / 2,5 kS/s; opsiyonel 500 S/s.
- [ ] 6.4 E01, E02, E06: gürültü, kararlı yük ve farklı yük tipleri.
  - **Bitti sayılır:** her deneyin protokolü, metadata'sı, verisi ve sonucu mevcut.

## Faz 7 — Analiz ve karar
- [ ] 7.1 Kararlı aralıkta SCT–PZEM farkı, pencere değişkenliği, olay gecikmesi ve clipping.
- [ ] 7.2 Hızı, pencereyi, polling aralığını ve düşük akım sınırını ölçüme göre kararlaştır.
  - **Bitti sayılır:** her karar kendi veri setinden bir metrikle gerekçeli.

## Faz 8 — İşletme ve bakım
- [ ] 8.1 PZEM hata oranı, tekrar eden okumalar, ADC ofseti ve clipping izle.
- [ ] 8.2 Düzenli kalibrasyon yap; donanım değişikliğinde yeni calibration_id aç.
  - **Bitti sayılır:** kayıtlı bakım ve kalibrasyon geçmişi.

## Karar kapıları
- **G1:** SCT kalibrasyonu hata hedefinde ve clipping yok.
- **G2:** PZEM hata okumaları saptanıyor; geçersiz değerler hesaplardan dışlanıyor.
- **G3:** hız seçimi hedef yüklerde ölçülmüş sonuçlarla gerekçelendirilmiş.

## Tüm fazlar için — çalışma sürekliliği
- [ ] Her anlamlı depo oturumunda başlangıç/kapanış protokolünü uygula.
  - **Bitti sayılır:** oturum günlüğü ve STATUS güncellenmiş, ilgili testler çalıştırılmış, doğrulama kanıtı eklenmiş ve PR üzerindeki oturum kapanış kontrolü başarılı.
  - **Sınır:** CI yalnızca kayıt ve süreç alanlarını denetler; ölçüm doğruluğunu veya yeni sohbetin otomatik başlamasını garanti etmez.

## 2026-10-29 — Kaynak doküman incelemesi

SCT013-030 teknik raporu ve CT satürasyonu notu mevcut donanım referanslarına işlendi. Bu belge incelemesi deney/kalibrasyon sonucu değildir ve faz/karar kapısı durumlarını değiştirmez. Sonraki somut iş hâlâ T005/E01 yüksüz ofset ve gürültü tabanı ölçümüdür. E01 öncesi 10 µF orta nokta kondansatörü önerisi [ADR-007](docs/decisions/ADR-007-bias-midpoint-capacitor.md) ile kaydedildi; fiziksel uygulama ve ölçüm bekleniyor.
