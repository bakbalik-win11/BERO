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
