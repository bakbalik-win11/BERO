## 2026-10-31 — ANA YOL HARİTASI: PZEM–SCT KARARLI ALAN ÖĞRENME DÖNGÜSÜ

> Bu bölüm güncel ve bağlayıcı çalışma sırasıdır. Aşağıdaki eski faz açıklamalarındaki ham ADC/2 kS/s edinim adımları tarihsel plandır; ADR-009 ile kapatılan işleri yeniden açmaz. Çelişki varsa bu bölüm ve STATUS.md esas alınır.

### Proje hedefi
Çalışan E00F ölçüm yolunu koruyarak SCT çıktısını PZEM-004T V3.0 referans akışıyla aynı yük koşullarında karşılaştırmak; iki tarafta kararlı alanları ayrı tespit etmek; örtüşen alanları eşleştirip PZEM ile etiketlemek; veri biriktikçe SCT katsayısını/modelini iyileştirmek. Bu öğrenme döngüsü BERO boyunca sürecektir. PZEM referanstır; mutlak ve yanılmaz ground truth değildir.

### Aktif iş sırası
1. **T008 — PZEM ve E00F eşzamanlı gözlem kaydı.**
   - Kullanıcının paylaştığı çalışan E00F YAML baseline kabul edilir; pinler, 200 ms pencere, 2 s yayın aralığı ve 24.22 katsayısı gerekçe olmadan değiştirilmez.
   - Aynı yük/olay koşulunda PZEM alanları ile SCT Raw AC ve akım entity'leri kaydedilir.
   - Zaman damgası, saat dilimi, yük, olay/tekrar, sensör/firmware ve calibration_id bilgisi korunur.
   - PZEM -1, NaN, timeout ve parse hataları etiketlemeden çıkarılır; dışlama sayıları ayrıca raporlanır.
2. **Kararlılık ölçütlerini veriden çıkar.**
   - PZEM ve SCT kararlılığı ayrı hesaplanır; örnekleme/güncelleme hızları aynı varsayılmaz.
   - Aday ölçütler: pencere içi yayılım, min-max aralığı, eğim ve ardışık pencere tutarlılığı.
   - Sabit 3 saniye gecikme veya sabit maske önceden kabul edilmez.
3. **Ortak kararlı alanları eşleştir ve etiketle.**
   - Aynı fiziksel yük/SSR olayı içindeki örtüşen PZEM/SCT kararlı alanları seçilir.
   - Geçerli PZEM akımı etiket/referans alanıdır; eşleşme kalitesi ve zaman belirsizliği kaydedilir.
   - Geçiş/yerleşme verisi kararlı etiketlerden ayrı tutulur.
4. **Katsayı/model iyileştirme.**
   - İlk olarak mevcut 24.22 katsayısının yeni etiketli alanlardaki sapması ölçülür.
   - Sistematik ve tekrarlanabilir hata gösterilirse katsayı/model güncellenir; veri gerekçelendirmedikçe karmaşık model eklenmez.
   - Her sürüm yeni calibration_id ile kaydedilir; önceki sürümler korunur.
   - Eğitim verisi içi uyum ile ayrı deney/genelleme doğrulaması ayrılır.
5. **Sürekli öğrenme ve bakım.**
   - Yeni yük, akım seviyesi, sensör veya kurulum koşulunda döngü tekrarlanır.
   - Model performansı, artıklar, düşük akım davranışı ve koşul dışı örnekler izlenir.
   - Değişiklik ancak karşılaştırmalı kanıtla kabul edilir; çalışan baseline geri dönüş noktasıdır.

### ct_clamp inceleme kararı
ESPHome ct_clamp bileşenini şu aşamada değiştirmek, yeniden yazmak veya alternatif RMS algoritması geliştirmek aktif iş değildir. Önce mevcut bileşenin PZEM ile eşleştirilmiş kararlı alanlardaki davranışı ölçülür. Tekrarlanabilir sapma, kararlılık sorunu veya açıklanamayan anomali görülürse hedefli kaynak kod incelemesi açılır. Salt merak veya varsayımla firmware değiştirilmez. Önceki teknik notlar ölçüm kanıtı değil, kaynak kod gözlemi/hipotez olarak korunur.

### Kapatılan / park edilen işler
- PC'ye sürekli ham 50 Hz dalga aktarımı, örnek başına timestamp ve DMA/ADC Continuous: **KAPATILDI / GEREKSİZ** (ADR-009).
- Eski T005/E00A/E01 ham ADC ve gürültü tabanı planı: PZEM etiketlemenin zorunlu ön koşulu olmaktan çıkarıldı; **PARK EDİLDİ**.
- ct_clamp algoritmasını değiştirme/yeniden yazma: şimdilik yapılmayacak.
- Eski deneyler otomatik tamamlanmış sayılmaz; yalnız ana hedefe doğrudan katkı sağlayan yük koşulları gerektiğinde yeniden kullanılır.

### Karar kapıları
- **G1 Veri:** PZEM ve SCT aynı olay/yük koşulunda yeterli kayıt üretmiş; zaman ve kaynak bilgisi korunmuş.
- **G2 Kararlılık:** İki kanal için ayrı, veride sınanmış kararlılık ölçütleri tanımlanmış.
- **G3 Etiket:** Ortak alanlar, dışlanan okumalar ve eşleşme belirsizliği raporlanmış.
- **G4 Model:** Mevcut katsayı ve varsa yeni model karşılaştırılmış; eğitim içi ve ayrı doğrulama sonuçları ayrılmış.
- **G5 Süreklilik:** Yeni calibration_id, veri kökeni ve geri dönüş kaydı mevcut.

---

## 2026-10-31 — Kapsam revizyonu: ±%4 hedefi sağlandı

±%4 sapma hedefinin yeni/harici kodla sağlandığı kullanıcı tarafından bildirildi. Dünkü dört karşılaştırma (100 W akkor, 150 W akkor, kettle düşük/kararlı, kettle kaynama) ±%4 içindedir; ayrıntı [ADR-009](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md).

Aşağıdaki ara işler artık hedef değildir ve kapatılmıştır:
- 50 Hz ham dalga şeklini bilgisayara aktarma.
- Her ADC örneğini ayrı zaman damgasıyla saklama.
- Bu edinim için ESP-IDF ADC Continuous/DMA firmware'i geliştirme.

Bu karar E00F'nin çalışan ölçüm yolunu değiştirmez. E08 yüksek hızlı ham edinim hazırlığı KAPATILDI — GEREKSİZ olarak arşivlenir. E08'in 100/150 W/LED yük karakterizasyon belgeleri otomatik olarak tamamlanmış sayılmaz; yalnızca kullanıcı tarafından sunulmuş dört karşılaştırma kaydı ±%4 sonucunu destekler. BERO içindeki Python model/eğitim hattı ve bağımsız genelleme doğrulaması da tamamlanmış sayılmaz.

# Yol haritas

## Paralel düşük akım sensör karşılaştırma hattı — E09 (2026-10-30)

- [ ] ESP-1'i yalnız SCT013 hızlı örnekleme düğümü olarak koru; PZEM ve yardımcı sensörleri bu düğüme ekleme.
- [ ] ESP-2'de PZEM, ACS712-5A ve ZMCT103C-5A'yı E09 sırasıyla tekil → ikili → üçlü aşamalarda doğrula.
- [ ] Her aşama için bağlantı, gerçek kart/pin eşleşmesi, derleme/çalışma logu ve sonuç yorumunu kaydetmeden sonraki aşamaya geçme.
- Bu hat mimari/test planı olarak kabul edildi; Faz 1 SCT aktif işlerinin tamamlandığı veya fiziksel testlerin yapıldığı anlamına gelmez. Ayrıntı: [ADR-008](docs/decisions/ADR-008-two-node-staged-sensor-tests.md), [E09](experiments/E09-low-current-sensor-comparison/README.md).


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
- [ ] Ön adım E00A — bias trafosunun DC noktalarını SCT bağlamadan gözle: (A) L78L33 3,3 V çıkışı harici 10k/10k ölçüm bölücüsü üzerinden ADC'ye; (B) yaklaşık 1,65 V Vmid doğrudan ADC'ye. Tek ESP32, ilk geçişte 2 kS/s hedefi, koşul başına yaklaşık 1 saniye; ham ADC ve analogReadMilliVolts, multimetre karşılaştırması, zaman içi istatistik ve grafik. İlk ESP32D2 firmware'i depoda: GPIO34 (ADC1_CH6) ham ADC, GPIO35 (ADC1_CH7) voltaj; ESP-IDF. Kullanıcı derlendiğini/çalıştığını bildirdi; log ve fiziksel ölçüm sonuçları bekleniyor. [E00A protokolü](experiments/E00A-raw-waveform-observation/protocol.md). SCT bağlantısı ve yük testi bu E00A kapsamına dahil değil. ham ADC örneklerini kaydet ve bilgisayarda görselleştir: bias-only → SCT yüksüz → 100 W ampul; tek ESP32, her koşul için 30 saniyelik gözlem; örnekleme hızı firmware aşamasında belirlenecek. ADC-değer/zaman grafiği temel inceleme çıktısıdır; ortalama, min/max, tepe-tepe aralığı, standart sapma, örnek sayısı ve gerçekleşen hız grafiği tamamlayan özetlerdir. [E00A protokolü](experiments/E00A-raw-waveform-observation/protocol.md). Bu adım E00/E01 ve aktarım mimarisi kararından önce gelir. Daha fazla hız veya çoklu ESP32 ancak sonuçlar gerektirirse ele alınır.
- [ ] 1.2a SCT bağlı değilken bias noktasını ADC ile oku; `analogRead()` ham sayısı ve `analogReadMilliVolts()` çıktısını voltmetreyle karşılaştır. — [E00 protokolü](experiments/E00-bias-adc-baseline/protocol.md)
- [ ] 1.2b SCT bağlıyken ve ölçülen hatta akım yokken aynı iki ADC okumasını karşılaştır.
- [ ] 1.2c Uzun yüksüz ADC kaydı, zaman grafiği ve gürültü özeti. — [T005](tasks/T005-noise-floor.md)
  - **Başlangıç:** Donanım henüz kurulmadı. PZEM ve ESP kartları ölçülen hattan beslenmiyor. 30 saniye asgari başlangıç referansı; kayıt daha uzun, gerekirse saatler sürebilir. Kesin süre deney sırasında belirlenecek.
- [ ] 1.3 PZEM referans akışını kullanarak ortak kararlı alanlardan SCT modelini eğit ve ilk uyum raporunu oluştur; aynı aç-kapa olayının tam ham akışını ayrıca gözlemle. — [T006](tasks/T006-calibration.md)
  - **Bitti sayılır:** ortak kararlı alan etiketleme yöntemi ve veri kimlikleri kayıtlı; modelin aynı etiketli eğitim verisindeki ±%4 uyumu raporlanmış; aynı olayın ham SCT tahmini/PZEM zaman grafiği ile tepki ve gecikme gözlemleri ayrı raporlanmış; clipping ve sınırlamalar yazılmış. Bu ilk aşama bağımsız genelleme testi değildir.

## Faz 2 — SCT edinim
- [x] 2.1–2.3 Ham örnek edinimi, örnekleme hızı matrisi ve örnek-bazlı kayıt — KAPATILDI / GEREKSİZ (2026-10-31). ±%4 hedefi yeni/harici kodla sağlandığı için PC'ye ham 50 Hz dalga aktarımı, her örneğe zaman damgası ve bu amaçla DMA/ADC Continuous geliştirmesi yapılmayacak. [ADR-009](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md).
- [x] E08 ham dalga/örnekleme hızı karakterizasyonu — KAPATILDI / GEREKSİZ (2026-10-31). Ayrı yüksek hızlı ham edinim artık hedef değildir; E08'in yük karşılaştırma raporları kendi kanıt durumuna göre korunur. [Aşama 3 kapanış kaydı](experiments/E08-sct-characterization/stage-03-high-speed-capture.md).

## Faz 3 — PZEM edinim
- [ ] 3.1 Yaklaşık 1 s sorgu başlangıcı; istek/yanıt zamanları ve read_status kaydı.
- [ ] 3.2 V/I/P/PF alanlarının değişim zamanlarını ayrı incele.
- [ ] 3.3 Sentinel, timeout ve parse hatalarını ayıkla.
  - **Bitti sayılır:** en az 10 dakikalık kayıt ve hata oranı var.

## Faz 4 — Zaman ilişkisi ve olay davranışı
- [ ] 4.1 SSR, SCT ve PZEM kayıtları için ortak monotonik zaman ilişkisini kur; istek/yanıt zamanlarını koru.
- [ ] 4.2 SCT ve PZEM kararlılık/geçiş alanlarını ayrı ayrı deney verisi ve istatistiksel ölçütlerle belirle.
- [ ] 4.3 Aynı SSR olayı içindeki örtüşen ortak kararlı alanları etiketleme için seç; tam ham olay akışını dinamik grafik için koru.
- [ ] 4.4 PZEM güncelleme davranışı, okuma süresi, SCT tepki/yerleşme ve gözlenen zaman farklarını ayrı incele. Sabit süreyi nihai etiket kuralı varsayma.
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

## 2026-10-30 — E00A açıldı; ilk multimetre referansı kaydedildi

Kullanıcı L78L33 DC çıkışını multimetreyle 3,31 V ölçtüğünü bildirdi; bu değer E00A sonuç kaydına KULLANICI BİLDİRİMİ olarak eklendi. Bu, ADC ölçümü değildir. Her koşul için 30 saniyelik gözlem planlandı. 3,3 V için ayrı/geçici 10k/10k ölçüm bölücüsü bias trafosunun parçası değildir; fiziksel olarak kurulmuş sayılmaz. ADC sınırları ve gerçek kart/pinout doğrulanmadan bağlantı yapılmayacak. E00A belgeleri güncellendi. Firmware, ADC kaydı ve Vmid ölçümü henüz yok.

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


## 2026-10-30 — E00A firmware uygulama notu

E00A için [ESP32D2 firmware'i](experiments/E00A-raw-waveform-observation/firmware/esp32d2-e00a-adc.yaml) depoya eklendi. GPIO34 ham ADC, GPIO35 voltaj sensörü olarak iki ayrı ADC kanalı kullanılır; ESP-IDF framework ve 1 saniyelik sensör güncellemesi tanımlıdır. Kullanıcı derleme ve çalışmayı bildirdi (KULLANICI RAPORU). Bu, E00A'nın 30 saniyelik ham kayıt, grafik ve iki fiziksel koşul kabul ölçütlerini tamamlamaz. Sonuç logu bekleniyor.


## 2026-10-30 — E00A-S01 GND referans testi

E00A kapsamında S01 alt adımı kaydedildi: sensör yokken GPIO34/GPIO35 GND referansında uzun log gözlendi. GPIO34 0 count; GPIO35 yaklaşık 175 saniyelik kararlı bölümde 0.142 V. Önceki açık giriş dalgalanması floating giriş teşhisini destekliyor. Elektriksel çözüm adayı, jack/CT bağlantısı doğrulandıktan sonra ADC düğümünü Vmid'e yüksek değerli pasif dirençle biaslamak. Sonraki test tek ADC kanalında Vmid bias ve 60 saniyelik gözlem. E00A henüz tamamlanmadı. Ayrıntı: [E00A-S01 raporu](experiments/E00A-raw-waveform-observation/reports/E00A-S01-gnd-reference-stability.md).


## 2026-10-30 — E00A SCT'siz bias-only alt adım sonucu

SCT bağlı değilken Vmid bias koşuluna ait uzun ESP32D2 logu analiz edildi; bu alt koşul kapatıldı. 603 geçerli zaman eşleşmesinde GPIO35 std. sapma 6.474 mV, GPIO34 RAW std. sapma 6.97 count. RAW sıfır başlangıç kayıtları eşleştirme dışı bırakıldı. Bu, tüm SCT'siz bias/ADC ölçüm zincirinin gözlenen dalgalanmasıdır; ADC'nin tek başına gürültüsü değildir. E00A bütünü açık kalır: L78L33 3.3 V ayrı bölücü koşulu ile ham CSV ve zaman grafiği tamamlanmadı. Sonraki deney koşulu SCT bağlı fakat ölçülen hatta akım yok durumudur. Ayrıntı [E00A sonuç kaydı](experiments/E00A-raw-waveform-observation/results.md).


## 2026-10-30 — E00B yeni deney adımı

E00A SCT'siz bias-only alt koşulu kapandıktan sonra SCT bağlı fakat primer akımı olmayan koşul E00B olarak açıldı. Bias GPIO34/35 korunur; SCT RAW GPIO32 (ADC1_CH4), SCT voltaj GPIO33 (ADC1_CH5) önerildi. ESP32-WROOM-32D geliştirme kartının gerçek pinout'u doğrulanmadan bağlantı yapılmaz. E00B firmware'i depoya eklendi ve kullanıcı tarafından derlendiği bildirildi (KULLANICI RAPORU); fiziksel bağlantı/ölçüm henüz yok. GPIO32/33 gerçek pinout doğrulaması bekliyor. Ayrıntı [E00B](experiments/E00B-sct-connected-no-current/README.md).


## 2026-10-30 — E08 Aşama 2 / 100 W akkor testi açıldı

- [ ] E08 Aşama 2 — 100 W akkor matrisi. Durum: HAZIRLIK.
  - İlk koşul: 1 iletken turu × 1.000 örnek/s hedefi.
  - Tam matris: 1/2/4 tur × 1.000/2.000/2.500 örnek/s.
  - Mevcut E00B 1 saniyelik yayın firmware'i yeterli değildir; E08 yüksek hızlı ADC edinim firmware'i hazırlanacak.
  - Ölçüm, gerçek örnekleme hızı, veri kaydı ve sonuç henüz yok.
  - [Aşama protokolü](experiments/E08-sct-characterization/stage-02-100w-matrix.md).
