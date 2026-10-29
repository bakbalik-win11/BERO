# Proje durumu

**Son güncelleme:** 2026-10-29  
**Aktif faz:** Faz 1 — SCT analog ön uç ve yüksüz ölçüm hazırlığı  
**Sıradaki iş:** Önce [E00A — Ham sinyal gözlemi ve örnekleme hızı](experiments/E00A-raw-waveform-observation/README.md) (PLANLANDI); ardından [E00 — Bias ADC karşılaştırması](experiments/E00-bias-adc-baseline/protocol.md) ve [T005 — ADC temel okumaları ve E01 gürültü tabanı](tasks/T005-noise-floor.md). E00A, paketleme kararından önce ham dalgayı farklı hızlarda görme ve temel istatistikleri karşılaştırma adımıdır. T005 — PLANLANDI. İlk önce SCT bağlamadan bias noktasında `analogRead()` ham sayısı ile `analogReadMilliVolts()` karşılaştırılacak; sonra SCT bağlıyken akım yok durumunda aynı iki okuma yapılacak; uzun E01 gürültü kaydı daha sonraya bırakıldı. T003, PZEM'e göre ±%4 bağıl sapma ve Python `OK` karar kuralı belirlenerek kapatıldı. T001 envanter ve T002 güvenlik kontrolü, kullanıcının tamamladığını bildirdiği bilgiler esas alınarak kaydedilip kapatıldı.  
**Öncelikli SCT:** SCT013-030 (30 A / 1 V)  
**PZEM:** Esas kaynak [DONANIM/PZEM-004T/README.md](../../DONANIM/PZEM-004T/README.md); CT modeli kullanıcı tarafından PZCT-02 (0–100 A) olarak belirtildi.  
**Bias üretim alt devresi:** TAMAMLANDI — kullanıcı onayı. RN130421 + KBU6M + 2200 µF / 35 V + L78L33; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) kondansatör. Bağımsız ölçüm raporu bu kayda eklenmedi.  
**SCT/bias devresi:** Kullanıcı tarafından tarif edilen bağlantıda SCT dişi jack üzerinden breadboard bias alt devresine bağlanır; alt devrede 2 × 10 kΩ dirençle orta nokta ve orta noktadan GND'ye 104 (100 nF) kondansatör vardır. Bias yaklaşık 1,65 V kabul edilir; bu aşamada ayrıca ölçülmesi şart değildir. Harici ADC kullanılmayacak; ESP32 dahili ADC kullanılacak, MCP3208 sonraya bırakıldı. Bias'ın ayrı kayıt alanı olması yazılım/veri kaydı aşamasında ele alınacak. ADC GPIO/pin planı firmware aşamasına aittir. T004 hobi düzeyi belgeleme kapsamıyla tamamlandı; laboratuvar düzeyinde ADC aralığı/clipping hesabı T004 kapanış şartı değildir.  
**SCT/PZEM etiketleme ve kalibrasyon hedefi:** [Hedef mimari notu](docs/architecture/sct-pzem-labeling-and-calibration.md) — zaman damgası/sabit süre odaklı değil, paket bağlamı ve PZEM/SCT kararlı alanlarını algoritma-istatistikle belirleyip etiketleme; Python'da etiketli SCT verisiyle sensör başına katsayı/`f(x)` modeli çıkarma; ardından modeli çok paketli ham akışta sınayıp gerekirse iyileştirme. Firmware, algoritma ve deneyler henüz yapılmadı.  
**SSR:** SAMM Market 5 V, 2 kanallı kart; tedarikçi kodu İzmo9659, SKU MP02637. Giriş mantığı ve kart üzerindeki SSR'nin tam kodu doğrulanmalı.  
**RTC:** İki DS3231 modülünde de 2032 tipi pil bulunuyor. RTC kodunun çalıştığı ve güç kesilip yeniden verildikten sonra saatin korunduğu daha önce test edildi; bu bilgi esas alınır ve test tekrar istenmeyecek. Yüksek hızlı örnekleme zamanlaması ESP32 monoton zamanlayıcısına aittir.  
**Deney durumu:** Donanım henüz kurulmadı; E00 bias-only ADC karşılaştırması, E01 yüksüz gürültü kaydı, E07 eski planı, E08 yeni karakterizasyon planı ve kalibrasyon YAPILMADI. Güncel SCT karakterizasyon sırası [E08](experiments/E08-sct-characterization/README.md): (1) yüksüz uzun okuma, (2) 100 W akkorla 1/2/4 kablo turu × 1/2/2,5 kS/s matrisi, (3) aynı matrisin 150 W akkor ve 8,5 W LED'de tekrarı, (4) sonuçlardan sonra aç-kapa davranışı. Aynı pencere örneklerinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanacak; yardımcı istatistikler ve gerçekleşen örnekleme hızı kaydedilecek. PZEM veya başka ESP'nin ortalama akımı yalnız genel deney notudur; SCT pencereleriyle zaman eşleştirmesi yapılmaz. Kararlılık eşiği, pencere sayısı ve kesin kayıt süresi önceden sabitlenmez. Önceki [E07 protokolü](experiments/E07-sct-stability-step-tests/protocol.md) fiziksel olarak uygulanmadı; güncel plan için E08 esas alınır. T005/E00-E01 hazırlığı hâlâ aktif sıradaki iştir. 30 saniye asgari başlangıç referansıdır, üst sınır değildir; kesin süre belirlenmedi. PZEM ve diğer ESP kartları ölçülen hattan beslenmez; beslemeleri ayrıdır.

## Oturum sürekliliği
- Yeni oturumda başlangıç protokolü uygulanır: güncel main/son commit kontrol edilir; AGENTS, STATUS, ROADMAP, open-questions, ilgili görev/deney ve son günlük kaydı okunup karşılaştırılır.
- Başlangıç raporunda okunan kaynaklar, mevcut durum, hedef ve kabul koşulları kısaca belirtilir. Önceden kaydedilmiş bilgiler depoda aranıp kontrol edilmeden kullanıcıdan tekrar istenmez.
- Kullanıcı beyanı, üretici belgesi, hipotez, hesap ve ölçüm sonucu ayrı tutulur; commit sonrası dosyalar yeniden okunur, test/CI çalışmadıysa açıkça yazılır.

## Bildirilen stok

| Bileşen | Adet / özellik | Kaynak |
|---|---:|---|
| SCT013-030 (30 A / 1 V) | 7 | Kullanıcının verdiği envanter bilgisi; jack çıkışlı |
| SCT013-100A-1V | 10 | Kullanıcı bildirimi; jack çıkışlı |
| SCT013 toplamı | 17 | Kullanıcının verdiği envanter bilgisi |
| ESP32-C3 SuperMini | 1 | Envanter kaydı / önceki SSR düğümü |
| ESP32 ölçüm düğümü | 1 | Envanter kaydı / önceki PZEM düğümü |
| PZEM-004T | V3.0 | Kullanıcı bildirimi |
| Masaüstü güç kaynağı | 5 V / 1,8 A | Kullanıcı bildirimi |
| Test yükleri | 100 W ve 150 W ampuller ana deney yükleri; 5 W LED ampul farklı PF için | Planlanan test yükleri; gerçek güç, akım ve PF ilgili testte ölçülecek |
| Breadboard bias alt devresi | Mevcut kayıt: 2 × 10 kΩ, orta nokta ve GND'ye 104 (100 nF); E01 öncesi 10 µF önerisi ADR-007'de | Mevcut durum kullanıcı bildirimi; değişiklik bekliyor |
| Jack yuvaları ve bağlantı/ölçüm parçaları | Tam takım mevcut | Kullanıcı bildirimi |

## Mevcut bilgi
- Önceki BERO'daki SCT, PZEM, ESP32, MCP3208, SSR ve DS3231 teknik kaynakları proje referanslarına bağlandı.
- Bias üretim alt devresi, kullanıcının onayıyla tamamlandı sayılıyor; bağımsız voltaj ölçüm raporu eklenmedi.
- SCT013 sinyalinin breadboard bias devresi üzerinden ESP32'nin dahili ADC'sine alınması planlanıyor. 8 kanallı analog arayüz kartı mevcut değildir. MCP3208 sonraki aşamaya ayrılmıştır.
- PZEM için mevcut BERO kaydı kullanılıyor; bağlı CT modeli PZCT-02 (0–100 A) olarak belirtildi.
- SSR kartının tam giriş tetik mantığı ve fiziksel SSR parça kodu doğrulanmalı.
- Deneyler ve kalibrasyon sonuçları henüz eklenmedi.

## Karar kapıları
- [ ] G1 — SCT RMS kalibrasyonu hata hedefinde ve clipping yok.
- [ ] G2 — PZEM okuma durumu izleniyor; geçersiz okumalar özetlerden dışlanıyor.
- [ ] G3 — örnekleme hızı hedef yüklerde ölçülmüş metriklerle gerekçelendirilmiş.

## Sıradaki işler
1. [x] [T003 — PZEM tabanlı model hata hedefi](tasks/T003-reference-and-error-target.md): ±%4 bağıl sapma; Python geçerli örneklerde `OK` kararı verir.
2. [x] [T004 — Analog ön uç](tasks/T004-analog-frontend.md): mevcut jack/bias bağlantısı, SCT modelleri ve ESP32 dahili ADC yaklaşımı belgelendi.
3. [ ] [T005 — E01 gürültü tabanı](tasks/T005-noise-floor.md): donanım kurulduktan sonra yüksüz ADC verisini toplama ve grafikleme.
4. E00/E01 ve edinim temeli sonrası [E07 SCT kararlılık basamak testi](experiments/E07-sct-stability-step-tests/protocol.md): üç turda dört durum; her turda farklı hedef örnekleme hızı.

## Açık engeller
- Donanım henüz kurulmadı. Gerçek bağlantı kurulurken SCT jack–breadboard bias bağlantısı ve ESP32 ADC pini uygulanacak donanımla eşleştirilecek; firmware/pin planlama aşamasında GPIO seçimi yapılacak. T004 kapsamında laboratuvar düzeyinde ADC aralığı/clipping hesabı istenmiyor.
- T005 için gerçek donanım kurulumundan sonra yüksüz veri toplama, süreyi belirleme ve grafik üretme bekleniyor.
- SSR'nin hangi iki AC yükü anahtarlayacağı, GPIO eşlemesi ve giriş mantığının düşük gerilimde doğrulanması.
- T003 TAMAMLANDI: model tahmini geçerli PZEM akımından ±%4 bağıl sapma içindeyse Python sonucu `OK` işaretler. Kararlı alan gözlemi ve SCT istatistikleri ayrı görev/deneylerde ele alınır. Test yükleri ilgili test kaydında beyan edilecek.

Firmware, deney ve kalibrasyon sonuçları henüz eklenmedi. E07 protokolü eklendi; kararlılık eşiği/pencere sayısı henüz belirlenmedi ve fiziksel test yapılmadı.

## İlk test sıralaması — 2026-10-29

1. E00: SCT bağlı değil; bias orta noktası → ADC GPIO. `analogRead()` ham sayısı ve `analogReadMilliVolts()` aynı döngüde okunup voltmetreyle karşılaştırılacak.
2. SCT bağlı, ölçülen hatta akım yok: aynı iki okuma tekrar edilecek.
3. Ardından E01'in uzun yüksüz kayıt/grafik ve gürültü özeti yapılacak.

E00 protokolü: [Bias-only ADC baseline](experiments/E00-bias-adc-baseline/protocol.md). Henüz fiziksel ölçüm yapılmadı.

## 2026-10-29 belge incelemesi

- Kullanıcının sağladığı SCT013_30A_1V_ESP32_Raporu.docx ve ct-akım-trafosu-satürasyonu.txt okundu.
- SCT013-030 nominal oranı, gerilim çıkışlı modelde dahili burden bilgisi ve genel satürasyon riskleri donanım referanslarına eklendi.
- [ADR-007](docs/decisions/ADR-007-bias-midpoint-capacitor.md) kapsamında, E01 öncesi bias orta noktasındaki mevcut 100 nF kondansatöre paralel 10 µF elektrolitik kondansatör eklenmesi önerildi. Fiziksel değişiklik ve sonuç ölçümü henüz yapılmadı; ADC GPIO'suna ek 100 nF kararı verilmedi.
- Rapordaki genel ESP32/ADS1115/RMS örnek kodları BERO firmware'i olarak alınmadı.
- Fiziksel ölçüm, ADC okuması, firmware testi ve kalibrasyon yapılmadı.


## Bias kondansatörü — aktif donanım notu

- Mevcut kayıtlı devrede bias orta noktasından GND'ye 104 (100 nF) bulunur.
- [ADR-007](docs/decisions/ADR-007-bias-midpoint-capacitor.md) 10 kΩ + 10 kΩ bölücü ve 50 Hz SCT sinyali için orta noktadaki mevcut 100 nF'ye paralel 10 µF eklenmesini önerir. Değişiklik E01 öncesinde uygulanmalı ve fiziksel olarak yapılana kadar tamamlandı sayılmamalıdır.
- ADC pinine ayrıca 100 nF eklenmesi opsiyoneldir; ilk E01 ölçümünde aynı anda ikinci değişken eklememek için şimdilik planlanmadı.


## 2026-10-29 — E08 SCT karakterizasyon planı

Kullanıcıyla mutabık kalınan sıra E08 olarak kaydedildi: (1) SCT yüksüz uzun okuma ile temel gürültü/bias davranışı, (2) 100 W akkor ile 1/2/4 kablo turu × 1/2/2,5 kS/s matrisi, (3) aynı matrisin 150 W akkor ve 8,5 W LED'de tekrarı, (4) sonuçlar görüldükten sonra aç-kapa ve kararlı görünen bölgelerin incelenmesi. Her pencerenin aynı örneklerinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanır; yardımcı istatistikler ve gerçekleşen örnekleme hızı kaydedilir. PZEM/başka ESP ortalama akımı varsa genel koşul notudur; SCT ile zaman eşleştirmesi yapılmaz. Kararlılık eşiği, pencere sayısı ve kesin kayıt süresi önceden belirlenmez.

[E08 açıklaması](experiments/E08-sct-characterization/README.md) · [Protokol](experiments/E08-sct-characterization/protocol.md). E08 planlandı; fiziksel ölçüm yapılmadı. Aktif sıradaki iş hâlâ T005/E00-E01 yüksüz temel ölçüm hazırlığıdır; E08 bunun ardından uygulanacak.
