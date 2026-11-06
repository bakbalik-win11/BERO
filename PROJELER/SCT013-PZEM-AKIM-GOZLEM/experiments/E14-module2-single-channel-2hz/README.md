# E14 — Modül 2 CH1-1T 2 Hz ölçüm denemesi

**Durum:** İLK CİHAZ LOGU DEĞERLENDİRİLDİ; ÜÇ HIZLI KARŞILAŞTIRMA REVİZYONU DERLENECEK; E14 AÇIK  
**İlk cihaz kaydı:** 2026-11-06 10:55:37–10:56:41 (+03:00)  
**Faz:** Faz 2  
**İlişkili işler:** T010 Modül 2, E13 örnekleme hızı ve yüksüz veri gözlemi

## Amaç

Modül 2 üzerinde CH1-1T kanalının yaklaşık 500 ms'de bir yeni ölçüm üretmesini (nominal 2 Hz) gerçek cihaz loguyla doğrulamak. CH2 ve CH3 kanallarını daha düşük hızda çalışır durumda tutarak üç kanalın aynı firmware içinde birlikte yürüyüp yürümediğini ve Modül 3 olay alımının etkilenip etkilenmediğini görmek.

Bu, kısa bir fizibilite/çalışma kontrolüdür; uzun süreli kararlılık, kalibrasyon veya nihai canlı mimari kabulü değildir.

## Gerçek uygulama ve bağlantılar

| Kanal | Fiziksel bağlantı | Deney davranışı |
|---|---|---|
| CH1-1T | Sarı, GPIO32, 1 geçiş | 500 ms hedef; nominal 2 Hz |
| CH2-1T | Yeşil, GPIO33, 1 geçiş | 1 saniyede bir (1 Hz) |
| CH3-1T | Mavi, GPIO34, 1 geçiş | 2 saniyede bir (0,5 Hz) |
| Ortak bias | Turuncu, GPIO35 | Ortak bias ölçümü |

- K=24.22, tüm kanallarda sabit.
- Gerçek uygulamada üç kanalın `sample_duration` değeri 100 ms'dir.
- CH1 bağımsız 500 ms aralıklı tetiklenir.
- CH2 her 1 saniyede bir okunur; her ikinci çevrimde CH3 ve ortak bias da okunur (2 saniye).
- Modül 3'ün UDP 4210 ON/OFF olay alıcısı korunmuştur.
- Olay eşleştirme anahtarı `BOOT_ID + EVENT_ID`; paket formatında TIME alanı yoktur.

**Plan değişikliği:** İlk E14 taslağında 200 ms sample_duration ve yalnız SCT1'in aktif olması yazılmıştı. Kullanıcının son uygulama kararıyla CH2/CH3 yavaş taramada tutuldu ve üç kanalın sample_duration değeri 100 ms oldu. Bu deney raporu gerçek uygulamayı esas alır; ilk taslak tarihsel plandır.

## Kod ve kanıt

- Deney dalı: `exp/modul2-ch1-2hz-20261106`
- Firmware: [bero-modul2-esp32d1.yaml](../../firmware/bero-modul2-esp32d1.yaml)
- İlk cihaz logunun kaynak YAML SHA: `afe5a689832b4d78b78c1bd1a0d8971301d2caaf`. Üç hızlı yeni deney revizyonunun güncel SHA, YAML geri okunup doğrulandıktan sonra eklenecek.
- Ham cihaz logu: [2026-11-06 cihaz logu](../../logs/module2/2026-11-06-module2-ch1-2hz-device-log.txt)
- Ön analiz: [2026-11-06 log analizi](../../logs/module2/2026-11-06-module2-ch1-2hz-log-analysis.md)

Log ESPHome 2026.10.2 ile 2026-11-06 10:54:01 +0300 tarihinde derlenmiş cihaz yazılımını gösterir. Cihaz API bağlantısı kurmuş ve ADC başlangıçları OK olmuştur. Logda binary hash bulunmadığı için çalışan binary ile YAML'ın byte-byte aynı olduğu iddia edilmez.

## İlk cihaz logu — 2026-11-06

- 910 satır / 71.312 bayt kaynak log; SHA-256: `b2f0e86f0053eb24c3455a7ee279cbdc1805c72dae5e7b4f8dbacc130a4d562d`.
- CH1-1T: 128 yayın; medyan yayın aralığı 0,500 s; gözlenen aralık 0,335–0,669 s. Kısa logda nominal 2 Hz desteklendi.
- CH2-1T: 32 yayın; medyan aralık 2,000 s.
- CH3-1T: 32 yayın; medyan aralık 2,001 s.
- Bias: 32 yayın; 1,652–1,669 V; ortalama 1,6621 V.
- Modül 3 EVENT_ID=1897 ON ve EVENT_ID=1898 OFF paketleri aynı BOOT_ID ile alındı ve HA entity'lerine yayınlandı.
- Logda ERROR/[E]/FAILED yok; bir safe_mode uzun işlem uyarısı (69 ms) ve üç ESP32 optimizasyon önerisi var.

Kullanıcı, kayıt boyunca hatta fiziksel olarak yük olmadığını ve bunu cihazın başında gözlemlediğini doğruladı. Modül 3 ON/OFF UDP mesajları fiziksel yük açma/kapama değildir; yalnızca mantıksal olay işaretleridir. Bu nedenle ON öncesi / ON aralığı / OFF sonrası medyan farkları yük geçişi olarak yorumlanmaz. OFF'tan yaklaşık 3 saniye sonra CH1'de 0,491 A tekil tepe görülmüştür; bu yüksüz koşuldaki bir ölçüm gözlemidir, nedeni bilinmemektedir. PZEM kaydı yoktur; kalibrasyon veya ±%4 sonucu çıkarılmaz.

## Değerlendirme

**Kısa cihaz ön kontrolü LOG İLE DESTEKLENDİ.** CH1 nominal 2 Hz, CH2/CH3 yavaş tarama ve Modül 3 ON/OFF paket alımı birlikte gözlenmiştir.

**E14 TAMAMLANMADI.** 64 saniyelik kayıt uzun süreli örnekleme kararlılığını, HA Recorder kalıcılığını, olay kayıpsızlığını veya fiziksel SSR anahtarlamasını kanıtlamaz. PZEM ile eşleşme yapılmamıştır.

## Açık işler

- [x] Deney firmware'ini ayrı dalda koru.
- [x] ESP32D1 cihaz logunda CH1 yaklaşık 500 ms yayın aralığını incele.
- [x] CH2/CH3 yavaş taramasının sürdüğünü incele.
- [x] Modül 3 ON/OFF paketlerinin Modül 2'ye ulaştığını incele.
- [ ] Daha uzun süreli log/HA History ile CH1 2 Hz devamlılığını ölç.
- [ ] Birden fazla ON/OFF çevrimini karşılaştır.
- [ ] Yüksüz koşulda ON ile görülen kanal artışının tekrarlanabilirliğini araştır.
- [ ] PZEM ve HA History zaman aralığıyla çapraz kontrol yap.
- [ ] Uzun kayıt sonrasında CPU/safe_mode uyarılarının tekrarını kontrol et.

## 2026-11-06 — Üç örnekleme hızı karşılaştırması revizyonu

Kullanıcı fiziksel olarak hattın yüksüz olduğunu doğruladı; 100 W akkor ampul yalnızca kullanıcıya "aç" denildiğinde fiziksel olarak devreye alınacak. Modül 3 ON/OFF mesajı fiziksel yükün açık/kapalı olduğunun kanıtı sayılmayacak; yalnızca olay işaretidir.

Yeni deney düzeni:
- CH1-1T: 500 ms (2 Hz).
- CH2-1T: 1 saniye (1 Hz).
- CH3-1T: 2 saniye (0,5 Hz).
- Üç kanal sample_duration: 100 ms.
- K: 24.22.
- CH2 her saniyelik script çevriminde okunur; her ikinci çevrimde CH3 ve ortak bias da okunur. CH1 bağımsız 500 ms döngüsünde kalır.

Bu değişiklik yalnızca deney dalındaki YAML'a işlendi; henüz ESPHome Validate/Compile, OTA veya fiziksel cihaz testi yapılmadı. Yeni firmware doğrulanmadan ampul testi başlatılmayacak.

## Sonraki adım

Önce yeni YAML'ı ESPHome Validate ve Compile ile doğrula. Cihaza yüklendikten sonra yüksüz baz çizgiyi kaydet; ardından kullanıcı ampulü fiziksel olarak açtığında 100 W akkor yük aşamasını başlat. Kararlı bölüm boyunca veri topla, sonra ampulü kapatıp kapanış davranışını kaydet.

## Genişletilmiş yüksüz kayıt — 2026-11-06

Kullanıcı fiziksel olarak bu 5 dakika 37 saniyelik kayıt boyunca hatta yük bağlı olmadığını doğruladı. Modül 3 ON/OFF mesajları fiziksel yük durumunu değiştirmedi; yalnızca olay işaretidir.

- [Genişletilmiş ham log](../../logs/module2/2026-11-06-module2-idle-extended-source.txt), 4.104 satır.
- CH1: 674 yayın; medyan aralık 0,500 s. Tekil aralıklar 0,004–1,158 s; dağılımda düzensiz örnek aralıkları var.
- CH2: 169 yayın; medyan 2,000 s. CH3: 168 yayın; medyan 2,000 s. Bu log yeni CH2=1 Hz revizyonundan önceki firmware ile alındı.
- Yüksüz gösterge medyanları CH1 0,2725 A; CH2 0,216 A; CH3 0,252 A. Bunlar fiziksel akım değil, yüksüz ölçüm zinciri göstergeleridir.
- Bias 168 yayın; 1,615–1,675 V; ortalama 1,6617 V.
- 6 ON / 5 OFF UDP olayı alındı; fiziksel yük geçişi olarak yorumlanmayacak.

Bu kayıt, yeni üç hız revizyonunun öncesindeki yüksüz baz çizgi kanıtıdır. Yeni YAML doğrulandıktan sonra aynı fiziksel koşulda yeni baz çizgi alınacak; ardından kullanıcı 100 W akkor ampulü açarak yük aşamasını başlatacak.

## 2026-11-06 — Üç adımlı karşılaştırmanın ikinci ve üçüncü gözlemleri

### 2. Farklı örnekleme hızlarının karşılaştırılması

- Üç kanal aynı deney düzeninde farklı yayın hızlarında çalıştırıldı: CH1 2 Hz, CH2 1 Hz, CH3 0,5 Hz hedefi.
- **KULLANICI GÖZLEMİ:** İlk karşılaştırmada CH2'nin sapması diğer kanallara göre daha az gözlendi.
- Bu, şu aşamada nitel bir gözlemdir. Hangi referansa göre sapma, sayısal fark ve dağılım ölçüleri yeni kayıt üzerinden ayrıca hesaplanmalıdır. Bu nedenle CH2'nin kesin olarak daha doğru olduğu veya 1 Hz'in en iyi hız olduğu sonucu çıkarılmaz.

### 3. Fiziksel SCT kanallarının yer değiştirmesi

- Kullanıcı fiziksel sensör/kanal bağlantılarını değiştirdi; yeni eşleştirme kaydı 2026-11-06 12:01 (+03:00) itibarıyla başlatıldı.
- Yeni eşleştirme: CH1 ← önceki fiziksel SCT3; CH2 ← önceki fiziksel SCT1; CH3 ← önceki fiziksel SCT2.
- Amaç, ölçüm farklarının ESP/ADC kanalına mı yoksa fiziksel SCT sensörüne/yerleşimine mi bağlı olduğunu ayırmaya yardımcı olmaktır.
- Yeni HA History CSV gelmeden donanım etkisi hakkında sonuç verilmeyecek. Önceki ve yeni kayıt aynı yük/koşul ve karşılaştırılabilir zaman aralıkları üzerinden incelenecek.

### Üç adımın mevcut sırası

1. PZEM History geçişlerinde paket ortalaması/önceki örneklerin etkisi gözlemi; geçiş değerleri anlık akım kabul edilmeyecek.
2. Üç farklı SCT yayın hızının karşılaştırılması; ilk kullanıcı gözleminde CH2 daha az sapıyor, sayısal doğrulama bekliyor.
3. Fiziksel SCT kanallarının yer değiştirilmesi; donanım etkisini ayırmak için yeni kayıt bekleniyor.

## 2026-11-06 — E14 üçüncü adım: örnekleme profilinin kod kanalları arasında kaydırılması

### Deney zinciri
1. **PZEM History:** Geçiş kenarındaki ara değerler anlık akım veya kararlı pencere istatistiği olarak kullanılmayacak. İç ortalama algoritması kaynak koddan doğrulanmış değildir; kayıt kullanıcı gözlemi ve yorumudur.
2. **Fiziksel sensör değişimi:** Kod/GPIO eşlemesi ve hızlar sabitken sensörler değiştirildi. İlk değişim SCT1→CH3, SCT2→CH1, SCT3→CH2; 12:15 ikinci değişim SCT1→CH2, SCT2→CH3, SCT3→CH1. Kullanıcı, ikinci yerleşimde de CH2'nin daha kararlı göründüğünü bildirdi. Takma/çıkarma sıçramaları ham veride korunur, kararlı pencere istatistiğine alınmaz.
3. **Kodda örnekleme profili değişimi:** Son fiziksel sensör yerleşimi sabit kalır; yalnız örnekleme profilleri kaydırılır. Beklenti, önceki CH2 avantajının 1 Hz profilini izleyerek CH1'e taşınmasıdır.

### Yeni kod düzeni
| Kanal | Önceki | Yeni |
|---|---:|---:|
| CH1-1T / GPIO32 | 2 Hz | **1 Hz** |
| CH2-1T / GPIO33 | 1 Hz | **0,5 Hz** |
| CH3-1T / GPIO34 | 0,5 Hz | **2 Hz** |
- sample_duration=100ms ve K=24.22 sabit.
- Son fiziksel eşleme: CH1←SCT3, CH2←SCT1, CH3←SCT2.
- CH1 her 1 saniyede; CH2 her ikinci çevrimde (2 saniyede); CH3 bağımsız 500 ms aralıkla okunur.
- Ortak bias, CH2'nin okunduğu 2 saniyelik çevrimde okunur.
- Aynı kararlı pencere değerlendirme yöntemi korunur; PZEM üç SCT hızının sıralamasında ölçüt değildir.

### Beklenti ve doğrulama sınırı
- Kararlılık avantajı CH1'e taşınırsa 1 Hz profil hipotezi desteklenir.
- Avantaj CH2'de kalırsa GPIO/ADC veya kanala özgü etki olasılığı güçlenir.
- Sonuçlar yakınsa örnekleme hızı tek başına belirleyici olmayabilir.
- YAML kaynak değişikliği depoya yazıldı. Validate, Compile, OTA ve fiziksel cihaz testi henüz yapılmadı.

## 2026-11-06 — 12:30 sonrası uzun kayıt ve örnekleme profilinin CH3'e taşınması

### Uzun kayıt değerlendirmesi
Kullanıcının sağladığı 12:30 sonrası HA History CSV'si 12:30:00–12:47:15 aralığını kapsıyor. Kayıtta CH1 1.036, CH2 518, CH3 2.072 ve PZEM 105 akım kaydı bulunuyor.

PZEM'in yaklaşık 0,46–0,48 A kararlı bölümleri incelenirken geçişlerin başı ve sonundan ikişer saniye dışlandı. Bu seçilmiş bölümlerde gözlenen standart sapmalar:
- CH1 (1 Hz): 0,0212 A
- CH2 (0,5 Hz): 0,0340 A
- CH3 (2 Hz): 0,0191 A

Bu kayıt içinde en düşük sapma CH3'te; CH1 çok yakındır. Bu sonuç örnekleme hızının tek başına nedensel etkisini kanıtlamaz. Önceki kısa kayıtta CH1 lehine görülen fark uzun kayıtta aynı biçimde sürmemiştir. PZEM burada kararlı bölgeyi seçmeye yardımcı olmuştur; SCT kanallarının sıralamasında mutlak doğruluk ölçütü değildir.

### Kullanıcı kararı ve yeni kod düzeni
Kullanıcı, uzun kayıt karşılaştırmasından sonra 1 Hz profilini CH1'den CH3'e taşımayı onayladı. CH1, eski CH3'ün 2 Hz profilini devralır; CH2'nin 0,5 Hz profili korunur:
| Kanal | Önceki profil | Yeni profil |
|---|---:|---:|
| CH1-1T / GPIO32 | 1 Hz | 2 Hz |
| CH2-1T / GPIO33 | 0,5 Hz | 0,5 Hz |
| CH3-1T / GPIO34 | 2 Hz | 1 Hz |

- CH1 bağımsız 500 ms interval ile okunur.
- CH3 bağımsız 1 s interval ile okunur.
- CH2 ve GPIO35 ortak bias aynı 2 s yavaş tarama script'inde okunur.
- Üç kanalda sample_duration=100ms ve K=24.22 korunur.
- GPIO/entity eşlemesi ve fiziksel sensör yerleşimi değiştirilmez.
- UDP 4210 olay alıcısı korunur.

**Doğrulama durumu:** YAML deney dalına yazıldı. ESPHome Validate/Compile, OTA ve fiziksel cihaz testi henüz yapılmadı. Yeni profilin çalıştığı veya ölçüm avantajı sağladığı iddia edilmez; bunlar sonraki doğrulama adımlarıdır.


## 2026-11-06 — 12:52 yeni kodla kayıt başlangıcı

- **KULLANICI BİLDİRİMİ:** Yeni örnekleme profiline ait kodla kayıt başlangıcı 12:52 (+03:00) olarak bildirildi.
- Başlangıç profili: CH1-1T / GPIO32 = 2 Hz (500 ms); CH2-1T / GPIO33 = 0,5 Hz (2 s); CH3-1T / GPIO34 = 1 Hz (1 s).
- Her üç kanalda sample_duration=100 ms ve K=24.22 korunmuştur. Ortak bias, CH2 ile aynı 2 saniyelik taramada okunur.
- Deney hedefi tek bir kanalı kazanan seçmek değildir. Üç kanalın da aynı koşullarda tutarlı, tekrarlanabilir ve düşük saçılımlı ölçüm üretmesi hedeflenir.
- Bu saat, kullanıcı tarafından bildirilen kayıt başlangıcıdır; cihaz logu/HA CSV henüz bu kayda eklenmedi. Fiziksel yük durumu bu başlangıç notunda belirtilmemiştir; UDP ON/OFF mesajları fiziksel yük durumunun kanıtı sayılmayacaktır.
- Sonraki analizde yeni profilin gerçekten çalıştığı yayın timestamp aralıklarından kontrol edilecek; karşılaştırma aynı fiziksel koşul ve kararlı pencereler üzerinden yapılacaktır.


## 2026-11-06 — 12:52 sonrası yeni profil HA History ilk analizi

### Kaynak ve kapsam
- **KAYNAK: KULLANICININ SAĞLADIĞI HA HISTORY CSV** `history (41).csv`; toplam 57.116 satır, 3 sütun. Dosyanın tamamı yerel saatle 11:00:00–12:59:09 (+03:00) aralığını kapsıyor.
- Bu analiz yalnız yeni kod başlangıcı olan 12:52:00 sonrasını kapsar: 12:52:04–12:59:09. Eski firmware verileri yeni profil karşılaştırmasına karıştırılmadı.
- Yeni profil aralıkları HA timestamp'lerinden doğrulandı: CH1 852 kayıt / medyan 0,500 s; CH2 214 kayıt / medyan 2,000 s; CH3 426 kayıt / medyan 1,000 s. Hedefler sırasıyla 2 Hz, 0,5 Hz ve 1 Hz. Bu, yayın ritminin HA tarafındaki doğrulamasıdır; ölçüm doğruluğu kanıtı değildir.
- Ortak bias 200 kayıt, medyan 2,000 s; gözlenen aralık 1,646–1,680 V.

### PZEM ve olay gözlemi
- PZEM akımında 0,470–0,473 A yüksek seviyeleri ve 0 A düşük seviyeleri gözlendi; yüksek seviyelerde 26 örneğin ortalaması 0,4715 A, standart sapması 0,00086 A. PZEM aktif güç yüksek örneklerde yaklaşık 91,2–110,4 W aralığındadır.
- Modül 3 ve Modül 2 olay kayıtları aynı BOOT_ID ile 206–219 EVENT_ID aralığında ON/OFF işaretlerini gösteriyor. Olay işaretleri tek başına fiziksel yük durumu kanıtı değildir; PZEM akım/güç değişimleri elektriksel yük çevrimleriyle uyumlu ek gözlemdir.

### İlk altı ON kararlı alanı
Olay ON başlangıcından 8 saniye sonrası ile eşleşen OFF işaretinden 5 saniye öncesi arasındaki örnekler alındı. Böylece geçiş kenarları ana istatistik dışında bırakıldı. Altı tam ON çevrimi kullanıldı:

| Kanal | Örnek | Ortalama (A) | Std. sapma (A) | Medyan (A) |
|---|---:|---:|---:|---:|
| CH1-1T / 2 Hz | 324 | 0,4758 | 0,0274 | 0,4701 |
| CH2-1T / 0,5 Hz | 78 | 0,4737 | 0,0261 | 0,4713 |
| CH3-1T / 1 Hz | 162 | 0,4699 | 0,0226 | 0,4653 |

- Aynı seçilmiş alanlardaki PZEM yüksek akım örnekleri 0,470–0,473 A bandında, ortalama 0,4715 A'dır.
- Bu ilk altı çevrimde CH3'ün standart sapması en düşüktür. Bununla birlikte üç kanalın medyanları PZEM yüksek seviye ortalamasına yakındır; çevrim bazında kanal ortalamaları da değişmektedir.
- **YORUM / SINIR:** Bu sonuç tek bir kısa kayıt ve altı çevrime dayanır. Örnekleme hızının nedensel etkisini, kanal üstünlüğünü veya uzun dönem tekrarlanabilirliği kanıtlamaz. Kullanıcının hedefi tek kazanan kanal seçmek değil, üç kanalın da tutarlı ve tekrarlanabilir veri üretmesidir. Bu nedenle profil değiştirme veya kanal eleme kararı çıkarılmadı.
- Kayıt fiziksel yükün kim tarafından/neyin anahtarladığına ilişkin ayrıca bir kullanıcı teyidi içermiyor; fiziksel yük kimliği varsayılmadı.

### Sonraki değerlendirme
- Daha uzun yeni profil kaydı alınmalı; aynı kararlı pencere seçim yöntemi ve fiziksel koşul korunmalı.
- Üç kanalın çevrimler arası ortalama değişimi, saçılımı, aykırı örnekleri ve PZEM'e göre farkı birlikte incelenmeli. PZEM referans kaydıdır; mutlak ground truth değildir.
- Ham CSV bu commit'e eklenmedi; kaynak kullanıcı tarafından bu konuşmada sağlanan dosyadır. Yukarıdaki sayımlar ve istatistikler bu dosyadan hesaplanmıştır.
