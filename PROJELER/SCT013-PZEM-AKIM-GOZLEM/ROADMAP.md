# Yol haritası

Bir fazın kabul ölçütü sağlanmadan sonraki faz tamamlandı sayılmaz. Kutular yalnız depoda kanıt olduğunda işaretlenir.

## Faz 0 — Hazırlık ve güvenlik
- [x] 0.1 Fiziksel envanter ve kullanıcı tarafından bildirilen hazır bias alt devresini kaydet. — [T001](tasks/T001-hardware-inventory.md)
  - **Mevcut kayıt:** Kullanıcı 7 adet SCT013 30 A / 1 V, 10 adet SCT013 100 A / 1 V, jack yuvaları, masaüstü 5 V / 1,8 A güç kaynağı, lamba yükü ve breadboard bias alt devresinin hazır olduğunu bildirdi. Ayrıntılar [envanterde](hardware/inventory.md) ve [T001 envanter notunda](docs/inventory/T001-fiziksel-donanim-envanteri.md).
  - **Kapanış:** kullanıcı tarafından bildirilen envanter ve bias alt devresi kaydedildi. Elektriksel kuplaj/ADC aralığı T004 kapsamındadır; bu T001'i açık tutmaz.
- [x] 0.2 220–240 V güvenlik kontrolleri. — [T002](tasks/T002-safety-checklist.md)
  - **Kapanış:** kullanıcı 2026-10-27 tarihinde listedeki tüm kontrolleri tamamladığını beyan etti. Kapanış kullanıcı beyanına dayanır; asistanın bağımsız fiziksel doğrulaması değildir.
- [x] 0.3 PZEM'e göre model kabul hata hedefini tanımla. — [T003](tasks/T003-reference-and-error-target.md)
  - **Bitti sayılır:** PZEM'e göre ±%4 bağıl sapma hedefi ve Python `OK` karar kuralı tanımlanmış. Kullanılacak yükler ilgili test sırasında kullanıcı tarafından beyan edilir.

## Faz 1 — SCT analog ön uç
- [x] 1.1 Mevcut SCT jack bağlantısını, breadboard bias alt devresini ve ESP32 dahili ADC yaklaşımını hobi projesi kapsamında belgele. — [T004](tasks/T004-analog-frontend.md)
  - **Kapanış:** Kullanılan SCT modelleri ve jack çıkışı, 2 × 10 kΩ orta nokta, orta noktadan GND'ye 100 nF kondansatör, yaklaşık 1,65 V bias kabulü ve dahili ADC yaklaşımı kaydedildi. Laboratuvar düzeyinde bias/ADC aralığı/clipping ölçümü bu görevin şartı değil.
- [ ] Ön adım E00A — ham ADC örneklerini kaydet ve bilgisayarda görselleştir: bias-only → SCT yüksüz → 100 W ampul; tek ESP32, ilk geçişte 2 kS/s hedefi, her koşul için yaklaşık 1 saniyelik kayıt. ADC-değer/zaman grafiği temel inceleme çıktısıdır; ortalama, min/max, tepe-tepe aralığı, standart sapma, örnek sayısı ve gerçekleşen hız grafiği tamamlayan özetlerdir. [E00A protokolü](experiments/E00A-raw-waveform-observation/protocol.md). Bu adım E00/E01 ve aktarım mimarisi kararından önce gelir. Daha fazla hız veya çoklu ESP32 ancak sonuçlar gerektirirse ele alınır.
- [ ] 1.2a SCT bağlı değilken bias noktasını ADC ile oku; `analogRead()` ham sayısı ve `analogReadMilliVolts()` çıktısını voltmetreyle karşılaştır. — [E00 protokolü](experiments/E00-bias-adc-baseline/protocol.md)
- [ ] 1.2b SCT bağlıyken ve ölçülen hatta akım yokken aynı iki ADC okumasını karşılaştır.
- [ ] 1.2c Uzun yüksüz ADC kaydı, zaman grafiği ve gürültü özeti. — [T005](tasks/T005-noise-floor.md)
  - **Başlangıç:** Donanım henüz kurulmadı. PZEM ve ESP kartları ölçülen hattan beslenmiyor. 30 saniye asgari başlangıç referansı; kayıt daha uzun, gerekirse saatler sürebilir. Kesin süre deney sırasında belirlenecek.
- [ ] 1.3 PZEM referans akışını kullanarak farklı akım/yük seviyelerinde SCT modelini değerlendir; veri kapsamı deneylerle belirlenecek. — [T006](tasks/T006-calibration.md)
  - **Bitti sayılır:** eğitim ve değerlendirme verileri ayrılmış; PZEM'e göre ±%4 hedefi, clipping durumu ve sınırlamalar raporlanmış; calibration_id kayıtlı. Üç seviye bağımsız referans cihazıyla ölçüm zorunluluğu değildir.

## Faz 2 — SCT edinim
- [ ] 2.1 Gerçek örnekleme hızını ve sapmayı ölç.
- [ ] 2.2 2 kS/s ve nominal 200 ms penceresini dene.
- [ ] 2.3 RMS, ADC ortalaması, min/max, örnek sayısı ve clipping sayaçlarını üret.
- [ ] E08 için aynı pencereden bias çıkarılmış RMS, mutlak Peak, Peak-to-Peak ve yardımcı istatistikleri üret; hedef örnekleme hızı ile ölçülen gerçek hızı ayrı kaydet.
  - **Bitti sayılır:** yüksüz ve yük altındaki pencere değişkenliği raporlanmış; hız ve kablo turu etkileri karşılaştırılmış; sonraki karar eldeki veriyle gerekçelendirilmiş.

## Faz 3 — PZEM edinim
- [ ] 3.1 Yaklaşık 1 s sorgu başlangıcı; istek/yanıt zamanları ve read_status kaydı.
- [ ] 3.2 V/I/P/PF alanlarının değişim zamanlarını ayrı incele.
- [ ] 3.3 Sentinel, timeout ve parse hatalarını ayıkla.
  - **Bitti sayılır:** en az 10 dakikalık kayıt ve hata oranı var.

## Faz 4 — Zaman hizalama
- [ ] 4.1 Tek monotonik saat kaynağı kullan.
- [ ] 4.2 SCT RMS değişimiyle olay algıla.
- [ ] 4.3 PZEM ve SCT verilerinde kararlı/geçiş alanlarını deney verisi ve geliştirilecek istatistiksel ölçütlerle belirle; sabit süreyi nihai etiket kuralı olarak varsayma.
  - **Bitti sayılır:** geçiş/kararlı alanların seçim yöntemi belgelenmiş, veride sınanmış ve sınırlamaları raporlanmış. Yaklaşık 3 s yalnız geçmişteki bir hipotez olarak kalır; otomatik etiket kuralı değildir.

## Faz 5 — Kayıt şeması
- [ ] 5.1 Zorunlu ve önerilen alanları uygula, örnek kayıtları doğrula.
- [ ] 5.2 Olay tamponu prosedürünü belirle.
  - **Bitti sayılır:** bir saatlik örnek kayıt şema ile uyumlu; olay kesiti test edilmiş.

## Faz 6 — Deneyler
- [ ] 6.1 E03: dirençli yük aç/kapat, en az 5 tekrar.
- [ ] 6.2 E04: PZEM alanlarının değişim zamanı.
- [ ] 6.3 E05: aynı yükte 1 / 2 / 2,5 kS/s; opsiyonel 500 S/s.
- [ ] 6.4 E01, E02, E06: gürültü, kararlı yük ve farklı yük tipleri.
- [ ] E07: önceki, henüz uygulanmamış SCT gözlem planı; güncel uygulama planı olarak kullanılmayacak. Ayrıntı için E07 protokolündeki E08 bağlantısına bak.
- [ ] E08: yüksüz uzun okuma → 100 W akkor tam matris → 150 W akkor ve 8,5 W LED aynı matris → aç-kapa testi. [E08 genel açıklaması](experiments/E08-sct-characterization/README.md) ve aşama belgeleri esas alınır.
  - **Bitti sayılır:** her aşamanın amacı ve koşulları kaydedilmiş; gerçek hız, pencere istatistikleri ve kablo turu belirtilmiş; sonuçlar ve açık kalan sorular raporlanmış. Fiziksel deney henüz yapılmadı.

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

## 2026-10-29 — E00A kapsamı sadeleştirildi

E00A'nın amacı korunarak ilk geçiş sadeleştirildi. Öncelik canlı/akıcı grafik değil, üç donanım koşulundan alınan ham kayıtların temel istatistiklerini karşılaştırmaktır. İlk geçişte tek ESP32, 2 kS/s başlangıç hedefi ve yaklaşık 1 saniyelik kayıt kullanılır. Grafik yardımcı tanı çıktısıdır. 1/2,5 kS/s tam matrisi, yavaş oynatma ve üç ESP32 eşzamanlaması ilk aşamanın kabul koşulundan çıkarıldı; istatistikler yeni bir soru doğurursa sonraki deney seçilir.

## 2026-10-29 — Kaynak doküman incelemesi

SCT013-030 teknik raporu ve CT satürasyonu notu mevcut donanım referanslarına işlendi. Bu belge incelemesi deney/kalibrasyon sonucu değildir ve faz/karar kapısı durumlarını değiştirmez. Sonraki somut teknik adım E00A ham sinyal gözlemidir; ardından E00/T005/E01 temel okumaları gelir. İlk notta 10 µF ekleme E01 öncesi olarak yazılmıştı; sonraki tutarlılık denetiminde, ilk SCT bağlantılı kayıt E00A olduğu için uygulama planı E00A öncesine alındı. Ayrıntı [ADR-007](docs/decisions/ADR-007-bias-midpoint-capacitor.md) içinde; fiziksel uygulama ve ölçüm bekleniyor.


## 2026-10-29 — E07 SCT kararlılık basamak testi planı

E07, yalnız SCT sinyalinden kararlı bölgeleri belirleme yaklaşımını incelemek için eklendi; PZEM alan eşleştirmesi bu deneyin amacı değildir. Üç turla sınırlandı. Her turda boşta, 100 W akkor, 150 W akkor ve 8,5 W LED basamakları uygulanacak; hedef örnekleme hızı turlar arasında 1, 2 ve 2,5 kS/s olarak değişecek. İlk pencere varsayımı 200 ms'dir. Aynı örneklerden RMS, Peak, Peak-to-Peak ve yardımcı dalga istatistikleri çıkarılıp Python'da analiz edilecek.

**Kararlılık ilkesi:** “Henüz kararlılık eşiği veya gereken pencere sayısı belirlemeyelim. Bunlar deney sonuçlarından çıkarmamız gereken kararlar; baştan varsaymamız gereken değerler değil.” Bu deney için eşik veya ardışık pencere sayısı önceden belirlenmeyecek. Üç tur sonunda mevcut verinin yeterliliği değerlendirilecek; sırf daha fazla test mümkün diye yeni tur eklenmeyecek.

E07 protokolü: [protocol.md](experiments/E07-sct-stability-step-tests/protocol.md). Donanım kurulumu ve ölçüm yapılmadı.


## 2026-10-29 — E08 SCT karakterizasyonu

E08, önceki E07 tasarımından daha kapsamlı güncel karakterizasyon planıdır. E07 tarihsel/uygulanmamış protokol olarak korunur; uygulama sırası için E08 esas alınır. E08 hız, hesaplama yöntemi ve iletken tur sayısının etkilerini aynı karşılaştırma düzeninde incelemek için planlandı. Aşamalar ve her aşamanın gerekçesi [E08 açıklamasında](experiments/E08-sct-characterization/README.md) ve aşama notlarında bulunur. Sıra: yüksüz uzun okuma → 100 W akkor tam matris → 150 W akkor ve 8,5 W LED aynı matris → aç-kapa testi. Hız hedefleri 1/2/2,5 kS/s; kablo turları 1/2/4; hesaplamalar bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak. Dış cihaz ortalama akımı yalnız genel not olabilir; zaman eşleştirmesi yapılmaz. Kararlılık eşiği ve pencere sayısı sonuçlardan çıkarılacak. E08 planlandı; ölçüm yapılmadı. T005/E00-E01 hazırlığı hâlâ önce gelir.
