

## Yeni hedef — E21 Çamaşır makinesi program davranışı analizi

- **[E21 — Çamaşır makinesi program davranışı analizi](E21-washing-machine-program-analysis/README.md): AKTİF / PLANLANDI.** Bir tam programın SCT-013 + ADS1115 akım zaman serisi kaydedilecek; gözlenen evre adayları, süreleri, geçişleri ve tekrar eden örüntüleri çıkarılacak. Program adı/ayar/yük bilgileri kullanıcıdan alınacak; yalnız akım grafiğinden makine içi durum kesin varsayılmayacak.
- PZEM kararlı-alan eşleştirmesiyle eğitim/kalibrasyon iş akışı kullanıcı kararıyla kapatıldı. E20 aç/kapa deneyi plan aşamasında kaldığı için yapılmadan kapatıldı. Eski protokoller ve sonuçlar tarihsel arşiv olarak korunur.
- Karar: [ADR-026](../docs/decisions/ADR-026-close-stable-window-training-open-washer-analysis.md).
# Deney arşivi

Bu klasör Faz 1'deki tarihsel deney ve gözlem kayıtlarını korur. **Faz 1 kapalıdır.** Aşağıdaki kayıtlar yeni aktif deney planı değildir; yapılmış çalışmaların logları ve sonuçları ile hedefe ulaşıldığı için yapılmadan kapatılan planlar aynı tarihçe altında korunur.

## Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak (KAPATILDI)

Eski kayıtlar:
- [E00A — Bias/DC ve ADC gözlemleri](E00A-raw-waveform-observation/README.md)
- [E00B — SCT bağlı, akımsız hat gözlemi](E00B-sct-connected-no-current/README.md)
- [E00 — Bias ADC baseline](E00-bias-adc-baseline/protocol.md)
- E01 — Yüksüz ofset/gürültü tabanı
- E02 — Kararlı rezistif yük
- E03 — PZEM adım yanıtı/yerleşme
- E04 — PZEM alan değişim zamanları
- E05 — Örnekleme hızı karşılaştırması
- E06 — Yük senaryoları
- [E07 — SCT kararlılık basamak planı](E07-sct-stability-step-tests/protocol.md)
- [E08 — SCT sinyal karakterizasyonu](E08-sct-characterization/README.md)
- [E00F-N02/N03 — ESP32D2 gözlem logları](E00F-unthresholded-overnight-log/E00F-N02-first-device-log.md)

**Kapanış anlamı:** Faz 1 hedefi dış kaynaklı çalışan kodla ±%4 sapma olarak sağlandığı için Faz 1 kapsamında kalan yapılmamış deneyler ve işler KAPATILDI — HEDEFE ULAŞILDI. Bu deneylerin fiziksel olarak yapıldığı veya sonuç ürettiği anlamına gelmez. Gerçekten yapılmış alt deneylerin sonuçları kendi dosyalarında kalır. Eski planlar Faz 2'nin ön koşulu değildir ve yeniden açılmaz.

## Faz 1 başarı karşılaştırmaları

| Yük | Referans | Kod sonucu | Sapma |
|---|---:|---:|---:|
| 100 W akkor | 0,446–0,447 A | 0,4471 A | yaklaşık %0 |
| 150 W akkor | 0,616 A | 0,615 A | −%0,2 |
| Kettle düşük/kararlı | 0,637 A | 0,656 A | +%3,0 |
| Kettle kaynama | 6,39 A | 6,15 A | −%3,8 |

Dört koşulun tamamı ±%4 sınırındadır. Sonuç ve kapanış kararı [ADR-009](../docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md) içinde kayıtlıdır.

## Test yükleri ve karşılaştırmalı ölçüm kayıtları

Aynı fiziksel yükte farklı ESP/modül/kod düzenekleriyle alınan sonuçlar, deney numaralarından ayrı olarak yük bazında izlenir. Her yükün ana tablosu kod, log, tarih/saat aralığı, referans, sonuç ve ±%4 değerlendirmesini birbirine bağlar. İlk kayıt: [100 W akkor ampul karşılaştırma tablosu](../test-loads/100w-incandescent/README.md). Genel kayıt standardı: [Test yükleri bölümü](../test-loads/README.md).

## Faz 2 — Yeni deneyler

- **[E10 — ESPHome ct_clamp örnekleme penceresi süresi gözlemi](E10-ct-clamp-window-duration/README.md): PLANLANDI.** T010 / Modül 2 SCT-1 altında 200 → 500 → 1000 → 200 ms geri dönüş karşılaştırması. Yalnızca sample_duration değişecek; update_interval: 2s ve K=24.22 sabit. Bu deney kalibrasyon değildir. [Sonuç defteri](E10-ct-clamp-window-duration/results.md).
- E09 — PF koşulu ile SCT/PZEM akım karşılaştırması ayrı uzun vadeli plandır; E10 ile birleştirilmez.

Faz 2 görev sırası T010 → T007 → T008 → T006 olarak kalır. E10, T010 altındaki somut ölçüm sorusudur; görev sırasını değiştirmez.

## Kayıt standardı

Her yeni deney için amaç/HEDEF, gerçek bağlantı ve ayarlar, LOG, SONUÇ, kaynak veri/hash, kod sürümü ve yorum birlikte saklanır. Yapılmayan adım yapılmış gibi gösterilmez. Ham veri varsayılan olarak Git'e eklenmez; gerekli küçük örnekler ve özetler saklanır.


## Faz 2 — Yeni deneyler ve güncel öncelik

- **[E11 — Modül 2/3 birlikte yüksüz hat uzun süreli gözlem ve olay aktarımı](E11-idle-dual-module-observation/README.md): PLANLANDI / ilk ortak deney önceliği.** İki modül birlikte çalışır; ölçülen hatta yük bağlanmaz; Modül 3'ün 40 s ON / 20 s OFF olay döngüsü sürer. PZEM ve üç SCT kanalının yüksüz davranışı ile Modül 3 olay gönderimi/Modül 2 olay alımı karşılaştırılır.
- Deney sırası sabit değildir; ihtiyaca ve donanım hazır oluşuna göre değişebilir. Bu, Faz 2 görev bağımlılıklarını değiştirmez.
- E10 (ct_clamp pencere süresi) planlı deney olarak korunur; E11 nedeniyle iptal edilmez veya tamamlandı sayılmaz.


- **[E12 — SCT kararlı alan tespiti, PZEM örtüşmesi ve tepki süresi](E12-sct-stability-window-and-response/README.md): PLANLANDI / ilk gözlem oturumu 2026-11-05.** Üç inceleme: SCT istatistiksel kararlılık algoritması; bağımsız SCT/PZEM kararlı alanlarının zaman örtüşmesi; SCT tepki süresi ve daha kısa sample_duration olasılığı. 20:07–20:37 100 W oturumu ilk gözlem adayı; 20:12 kablo değişikliği öncesi/sonrası ayrı incelenecek. Tam log ve sonuç analizi bekleniyor.

**Deney sırası ilkesi:** Deney numaraları tarihsel kimliktir; zorunlu çalışma sırası değildir. Kullanıcı ve asistan, ihtiyaca ve donanım hazır oluşuna göre bir deneyi diğerinin önüne alabilir. Bu esneklik Faz 2 görev bağımlılıklarını veya mimari kabul kurallarını kendiliğinden değiştirmez.


- **[E13 — Yüksüz gürültü filtresi ve SCT örnekleme hızı](E13-idle-noise-filter-and-sampling-rate/README.md): PLANLANDI.** I007 ham yüksüz kayıtlarından ayrı filtrelenmiş türev akış oluşturma ve SCT için kullanıcı tarafından önerilen 2 Hz (500 ms) çıktı hedefinin tek kanal/üç kanal koşullarında fizibilitesini ölçme. Ham veri korunur; filtre parametreleri ve firmware değişikliği henüz yoktur.


- **[E14 — Modül 2 tek SCT kanalında 2 Hz ölçüm denemesi](E14-module2-single-channel-2hz/README.md): PLANLANDI / 2026-11-06 akşamı kısa oturum adayı.

- **[E15 — Eğitim işaretli kanal adlarının Home Assistant History doğrulaması](E15-training-channel-history-naming/README.md): PLANLANDI.** Genel deney adları CH1/CH2/CH3 olarak kalır; eğitim kaydı alınacağı zaman kodda yalnız adlandırma değiştirilerek CH1-E/CH2-E/CH3-E akışları yayınlanır. Deney, koddan HA History'ye görünen ad ve gerçek entity_id geçişini ve CSV dışa aktarımını doğrular. Ölçüm hesabı/ayarları değiştirilmez.** Modül 2 deney alanı olarak kullanılacak; yalnız SCT1 (sarı/GPIO32, fiziksel 1 geçiş) okunacak. İlk denemede K=24.22 ve sample_duration=200 ms sabit tutularak yaklaşık 500 ms çağrı aralığı denenecek. Gerçek 2 Hz başarısı timestamp'lerle doğrulanacak. Deney firmware'i çalışan üç kanallı YAML'ın üzerine yazılmayacak; ayrı sürüm korunacak. E14, E13'ün genel 2 Hz/filtre planını somut kısa oturumla sınar; filtre algoritması veya nihai canlı mimari kararı değildir. Deney önceliği Cumartesi uzun çalışmasını engellemez ve kullanıcıyla esnek belirlenir.


- **[E16 — Yüksüz/düşük akım koşulunda SCT'nin ON/OFF davranışını gözlemleme](E16-sct-on-off-response-idle-low-current/README.md): PLANLANDI — 2026-11-06 gece kaydı.** PZEM sıfır/sıfıra yakın akım gösterirken SCT CH1'in ON/OFF olaylarıyla değişip değişmediği ve tekrarlanabilir seviyelere yerleşip yerleşmediği incelenecek. Kullanıcının 18 W gözlemi ayrı doğrulanmamış hipotez olarak tutulur; gece yüksüz kaydıyla karıştırılmaz. HA History CSV ve iki modülün olay kayıtları sabah analiz edilecek. Eğitim etiketi/katsayı üretimi bu deneyin kapsamında değildir.


- **[E17 — CH1 düşük akım bölgesi: sürekli küçük yük gözlemleri](E17-low-current-continuous-load-observation/README.md): AÇIK — E17-A 18 W sürekli açık kayıt (2026-11-07 10:21).** Röle devrede değil; ilk ekranda PZEM 227,1 V / 0,078 A, CH1 yaklaşık 0,28–0,30 A. 0,24–0,41 A hesaplanmadı alanında sayısal akım değeri kabul edilmeyecek. CSV analizi bekleniyor. Sonraki ayrı kayıt adayı 15 W mini buzdolabı ampulü.


- **[E18 — CH1 SCT çıkarılmış, bias hattı üzerinden uzun süreli kontrol](E18-ch1-bias-line-control/README.md): PLANLANDI.** CH1 SCT sensörü çıkarılacak; CH1 ölçüm girişi ortak bias okuyan hatta bağlanarak uzun HA History kaydı alınacak. Amaç, SCT sinyali olmadan ölçüm zincirinde sıçrama görülüp görülmediğini incelemek. Fiziksel bağlantı, kayıt ve analiz henüz yapılmadı.


- **[E19 — ADS1115 ile düşük akım ölçüm alternatifi](E19-ads1115-low-current-alternative/README.md): AÇIK.** Aşama 1'de ADS1115 I2C 0x48 ve A0-A1 diferansiyel okumaları logla desteklendi; önceki 7 SPS kayıtları RMS/katsayı doğrulaması değildir. Aşama 2 olarak 100 W akkor sabit yükte ESP32D1 + ESP32D2 ADS1115 + PZEM ortak kararlı alan karşılaştırması ve ADS1115 katsayı testi açıldı. Ölçüm/katsayı beklemede. [Protokol](E19-ads1115-low-current-alternative/protocol.md) · [Sonuç](E19-ads1115-low-current-alternative/results.md) · [ilk log](../logs/ads1115/2026-11-13-E19-ads1115-first-bringup.md) · [YAML](../firmware/experiments/esp32d2-ads1115-ct-clamp.yaml).
