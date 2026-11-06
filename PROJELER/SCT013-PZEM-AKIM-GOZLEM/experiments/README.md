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


- **[E14 — Modül 2 CH1-1T 2 Hz ölçüm denemesi](E14-module2-single-channel-2hz/README.md): KISA CİHAZ ÖN KONTROLÜ LOG İLE DESTEKLENDİ; E14 AÇIK.** 2026-11-06 cihaz logunda CH1 128 yayın / 0,500 s medyan aralık, CH2/CH3 yaklaşık 2 s tarama ve Modül 3 ON/OFF paketlerinin alımı görüldü. Uzun süreli kararlılık, tekrarlı olay çevrimi, fiziksel SSR ve PZEM eşleşmesi henüz doğrulanmadı.
