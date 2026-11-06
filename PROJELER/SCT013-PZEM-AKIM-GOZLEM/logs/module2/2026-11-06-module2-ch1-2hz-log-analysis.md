# 2026-11-06 — Modül 2 CH1-1T 2 Hz ilk cihaz logu / ön analiz

## HEDEF

E14 kapsamında Modül 2'nin yeni firmware'inin gerçek ESP32D1 üzerinde çalıştığını, CH1-1T'nin yaklaşık 500 ms aralıkla yeni sonuç ürettiğini, CH2/CH3 yavaş taramasının sürdüğünü ve Modül 3 ON/OFF UDP olaylarının alındığını ilk cihaz loguyla kontrol etmek.

## KAYNAK VE KOD

- Kaynak log: [2026-11-06 Modül 2 cihaz logu](2026-11-06-module2-ch1-2hz-device-log.txt)
- Kullanıcı tarafından yüklenen kaynak: 910 satır, 71.312 bayt.
- Kaynak dosya SHA-256: `b2f0e86f0053eb24c3455a7ee279cbdc1805c72dae5e7b4f8dbacc130a4d562d`
- Çalışma dalı: `exp/modul2-ch1-2hz-20261106`
- Firmware: [bero-modul2-esp32d1.yaml](../../firmware/bero-modul2-esp32d1.yaml)
- YAML blob SHA: `afe5a689832b4d78b78c1bd1a0d8971301d2caaf`
- Logda görünen derleme: ESPHome 2026.10.2, 2026-11-06 10:54:01 +0300.
- Cihaz: `esp32d1`, IP `192.168.0.35`.

**Kod/ikili ilişki sınırı:** Log gerçek cihazda çalışan firmware davranışını kanıtlar ve ayarları deney YAML'ıyla uyumludur. Ancak logda binary hash bulunmadığından çalışan binary'nin YAML kaynak dosyasıyla byte-byte aynı olduğu iddia edilmez.

## GERÇEK ÇALIŞMA AYARLARI

- CH1-1T: GPIO32, 1 fiziksel geçiş, `sample_duration: 100ms`, hedef `interval: 500ms`.
- CH2-1T: GPIO33, 1 fiziksel geçiş, 2 saniyelik yavaş tarama.
- CH3-1T: GPIO34, 1 fiziksel geçiş, 2 saniyelik yavaş tarama.
- Ortak bias: GPIO35.
- Üç kanalın katsayısı: K=24.22.
- Üç kanalın ct_clamp penceresi: 100 ms.
- Modül 3 olay alıcısı: UDP 4210.

E14 ilk planındaki 200 ms pencere bu uygulamada 100 ms olarak değiştirilmiştir. Dolayısıyla bu kayıt 200 ms pencere testi değildir; yalnız çağrı aralığı ve cihaz çalışma davranışının kısa ön kontrolüdür.

## LOG İLE DESTEKLENEN SONUÇLAR

### 1. Derleme, bağlantı ve ADC başlangıcı

- Cihaz API üzerinden bağlandı; Wi-Fi bağlantısı YES, sinyal yaklaşık -59 dB.
- GPIO32/33/34/35 ADC birimlerinin Handle Init, Config, Calibration ve Overall Init sonuçları OK.
- Üç ct_clamp bileşeninde Sample Duration 0.10 s ve Update Interval never görünüyor; ölçümler script/interval çağrılarıyla tetikleniyor.
- Logda `[E]`, ERROR veya FAILED kaydı yok.

### 2. Ölçüm yayın sıklığı

| Kanal | Yayın sayısı | Medyan aralık | Gözlenen aralık | Değerlendirme |
|---|---:|---:|---:|---|
| CH1-1T | 128 | 0,500 s | 0,335–0,669 s | Kısa logda nominal 2 Hz desteklendi |
| CH2-1T | 32 | 2,000 s | 1,941–2,047 s | Yaklaşık 0,5 Hz |
| CH3-1T | 32 | 2,001 s | 1,894–2,069 s | Yaklaşık 0,5 Hz |

CH1'in medyan aralığı 500 ms'dir. Ancak tek tek aralıklar tam 500 ms değildir; 335–669 ms aralığı görülmüştür. Bu nedenle sonuç "kısa logda nominal 2 Hz çıktı hızı gözlendi" şeklinde yazılır; uzun süreli kesintisiz 2 Hz garantisi değildir.

CH2 ve CH3 yavaş taraması devam etmiş; logda sırasıyla CH2 başlangıcı, CH3 başlangıcı, ortak bias okuması ve tarama tamamlandı mesajları tekrarlanmıştır. CH1 akışı ile yavaş taramanın birlikte çalıştığı görülmüştür.

### 3. Bias

32 bias yayını:
- Minimum: 1,652 V
- Maksimum: 1,669 V
- Ortalama: 1,6621 V

Bu kısa kayıtta ortak bias seviyesi dar bir aralıkta kalmıştır.

### 4. Modül 3 ON/OFF olayları

Aynı BOOT_ID ile iki olay da alındı ve HA entity'lerine yayınlandı:

| Yerel zaman | EVENT_ID | STATE | Sonuç |
|---|---:|---|---|
| 10:55:50.846 | 1897 | ON | UDP_EVENT_RECEIVED ve HA_EVENT_PUBLISHED |
| 10:56:30.948 | 1898 | OFF | UDP_EVENT_RECEIVED ve HA_EVENT_PUBLISHED |

BOOT_ID: `8E809736A273DDC25CF41462945DEE69`

İki olayın EVENT_ID değerleri ardışık; bu log kesitinde ON/OFF paketlerinden biri eksik görünmüyor. Bu yalnızca bu iki paketin Modül 2'ye ulaşıp HA entity yayınlarına aktarıldığını gösterir. Fiziksel SSR anahtarlaması veya uzun dönem kayıpsızlık kanıtı değildir.

## YÜKSÜZ KOŞULDA ÖN GÖZLEM

Kullanıcının bu kaydı sistem boşta/yüksüz koşul olarak tanımlamasına göre aşağıdaki değerler ölçüm tabanı gözlemidir. Fiziksel sıfır koşulunun bağımsız elektriksel doğrulaması bu logun içinde yer almaz.

ON olayından önceki, olay aralığındaki ve OFF sonrasındaki yayınlar ayrı incelendi:

| Kanal | ON öncesi medyan (n) | ON aralığı medyan (n) | OFF sonrası medyan (n) |
|---|---:|---:|---:|
| CH1-1T | 0,172 A (26) | 0,317 A (80) | 0,193 A (22) |
| CH2-1T | 0,150 A (7) | 0,248 A (20) | 0,155 A (5) |
| CH3-1T | 0,169 A (7) | 0,278 A (20) | 0,164 A (5) |

Önemli bağlam düzeltmesi (kullanıcının fiziksel gözlemi):
- Kullanıcı, bu kayıt boyunca hatta fiziksel olarak hiçbir yük bulunmadığını ve bunu cihazın başında gözlemlediğini açıkça doğruladı.
- Modül 3'ün ON/OFF UDP mesajları bu kayıtta fiziksel yükün açılıp kapanması değildir; yalnızca mantıksal deney olay işaretleridir.
- Bu nedenle ON öncesi / ON aralığı / OFF sonrası medyan farkları bir yük geçişi olarak yorumlanamaz. Bu bölümler fiziksel olarak yüksüz koşulun farklı olay-zaman dilimleridir.
- OFF olayından yaklaşık 3 saniye sonra CH1'de 0,491 A tekil tepe görülmüştür (10:56:33.986). Bu, yüksüz kayıttaki tekil ölçüm gözlemidir; nedeni bilinmemektedir.
- Üç kanalda olay-zaman dilimleri arasında görülen farklar gürültü, ölçüm zinciri davranışı, besleme/ortam etkisi veya başka bir etkenden kaynaklanabilir; bu log tek başına ayrıştırmaz.

Dolayısıyla bu log, fiziksel yüksüz baz çizgi kaydıdır. Modül 3 olay işaretleri yalnızca zaman bölümlendirme için kullanılabilir; fiziksel yük durumu kullanıcının gözlemine göre etiketlenir. Ham veri korunur; eşik veya filtre bu logdan seçilmez.

## UYARILAR VE SINIRLAR

- Üç açılış uyarısı ESP32 flash/IRAM optimizasyon önerileridir; derlemeyi veya cihaz bağlantısını engellememiştir.
- 10:56:32.206'da safe_mode işlemi 69 ms sürmüş ve 50 ms sınırını aşan tek bir uyarı üretmiştir. Tek örnekle ölçüm akışını etkilediği söylenemez; uzun kayıtta tekrar edip etmediği izlenmelidir.
- Log yaklaşık 64 saniyelik kısa gözlemdir.
- PZEM verisi bu logda bulunmadığından kalibrasyon, ±%4 doğruluk veya SCT/PZEM eşleşmesi değerlendirilmemiştir.
- Uzun süreli 2 Hz sürdürülebilirliği, HA Recorder kalıcılığı ve olay kayıpsızlığı bu kayıtla doğrulanmaz.

## SONUÇ

**E14 kısa cihaz ön kontrolü: LOG İLE DESTEKLENDİ.**

1. Yeni firmware ESP32D1 üzerinde çalışıyor; ADC kanalları başlatılmış ve sensör yayınları görülmüştür.
2. CH1-1T için yayın aralığı medyanı 500 ms'dir; kısa kayıtta nominal 2 Hz hedefi desteklenmiştir.
3. CH2/CH3 yaklaşık 2 saniyelik taramayı sürdürmüştür.
4. Modül 3'ün bir ON ve bir OFF paketi Modül 2 tarafından alınmış ve HA entity'lerine yayınlanmıştır.
5. Yüksüz diye tanımlanan koşulda ON/OFF aralığı ile üç kanalın görünen akım seviyeleri arasında zamansal değişim vardır; neden henüz bilinmemektedir.

**Durum:** Kısa cihaz çalışma doğrulaması var; E14 tamamlanmadı. Uzun süreli örnekleme kararlılığı, tekrarlı ON/OFF çevrimleri, fiziksel koşul teyidi ve PZEM/HA History karşılaştırması açık.

## SONRAKİ ADIM

- Aynı fiziksel yüksüz koşulda daha uzun log/HA History kaydı al.
- Modül 3'ün birden fazla ON/OFF çevrimini yakala; olay ID sırası ve akım değişiminin tekrar edip etmediğini incele.
- CH1 timestamp aralıklarının 500 ms çevresindeki dağılımını daha uzun kayıtla değerlendir.
- Bu aşamada K, sample_duration veya filtre eşiğini değiştirme.

## Genişletilmiş yüksüz log — 2026-11-06 10:55:37–11:01:14

Kullanıcının fiziksel gözlemine göre bu 5 dakika 37 saniyelik kaydın tamamında hatta yük bağlı değildir. Modül 3 ON/OFF olayları yalnızca mantıksal olay işaretleridir.

- Kaynak: [genişletilmiş yüksüz cihaz logu](2026-11-06-module2-idle-extended-source.txt)
- 4.104 satır; 335.541 karakter (depo arşiv kopyası).
- CH1-1T: 674 akım yayını; medyan yayın aralığı 0,500 s. Tekil aralıklar 0,004–1,158 s aralığına yayıldı; bu nedenle medyan 2 Hz görünse de aralık dağılımında kümelenme/uzama örnekleri ayrıca izlenmelidir.
- CH2-1T: 169 yayın; medyan aralık 2,000 s.
- CH3-1T: 168 yayın; medyan aralık 2,000 s.
- Yüksüz gösterge değerleri: CH1 medyan 0,2725 A (min 0,120 / max 0,910); CH2 medyan 0,216 A (min 0,106 / max 0,406); CH3 medyan 0,252 A (min 0,139 / max 0,443). Bunlar fiziksel yük akımı değildir; yüksüz koşulda sensör zincirinin gösterdiği değerlerdir.
- Bias: 168 yayın; 1,615–1,675 V; ortalama 1,6617 V.
- UDP olayları: 6 ON, 5 OFF alındı. Bu olaylar fiziksel yük durumunu değiştirmemiştir.
- Bu log mevcut eski firmware ile alındı: CH1 yaklaşık 2 Hz, CH2 ve CH3 yaklaşık 0,5 Hz. CH2=1 Hz / CH3=0,5 Hz yeni firmware revizyonu henüz bu logda denenmedi.

Bu uzun kayıt yüksüz baz çizgi için daha fazla veri sağlar. CH1'de medyan 500 ms olumlu olmakla birlikte 4 ms gibi kısa aralıklar ve 1,158 s gibi uzun aralıklar bulunduğundan yalnız medyanla kesintisiz 2 Hz garantisi verilmez.