# BERO Modül 2 — Üçlü SCT Okuma Modülü

**Modül kimliği:** BERO-SCT-OKUMA-TEST-002  
**ESPHome kimliği:** `esp32d1` / `ESP32D1`  
**Durum:** FIRMWARE AÇILDI, DÖRT ADC BAŞLATMASI LOG İLE DESTEKLENDİ — SCT/100 W kanal testleri bekliyor  
**Görev:** [T010 — Modül 2 üçlü SCT devreye alma](../../tasks/T010-module2-triple-sct-bringup.md)  
**Karar:** [ADR-015](../decisions/ADR-015-module2-esp32d1-triple-sct.md)

## 2026-10-31 — Modül 2 ilk firmware açılışı / bağlantısız ADC kontrol logu

- **KANIT:** Kullanıcının paylaştığı ESPHome logu depoya ham kayıt olarak eklendi: [ilk açılış log kanıt dökümü](logs/module2/2026-10-31-first-boot-no-load.txt).
- **KOD:** [firmware/esp32d1.yaml](firmware/esp32d1.yaml) mevcut depodaki dört ADC sensörlü sürüm; GPIO32/33/34 SCT kanalları ve GPIO35 ortak bias. Log, ESPHome 2026.10.1 ile 2026-10-31 15:19:21 +0300 derlenmiş firmware'in cihazda açıldığını gösteriyor.
- **BAŞLATMA KANITI:** Dört ADC için Handle Init, Config, Calibration ve Overall Init durumları OK. GPIO32/33/34/35, ADC1_CH4/5/6/7 olarak listelenmiş; 12 dB attenuation ve 1.000 s güncelleme aralığı görülüyor.
- **BAĞLANTI DURUMU:** Kullanıcı beyanına göre bu açılış sırasında SCT ve 220 V ampul bağlantısı henüz yapılmamıştı. Bu nedenle üç SCT ADC değerleri sensör/yük ölçüm sonucu değildir; açıkta/bağlantısız analog girişlerin o andaki okumalarıdır.
- **LOG ÖZETİ:** 15:26:05–15:26:14 bölümünde 10'ar örnek: GPIO32 0.333–0.858 V (ortalama 0.634 V); GPIO33 0.142–0.468 V (ortalama 0.259 V); GPIO34 0.442–0.806 V (ortalama 0.588 V); ortak bias GPIO35 1.643–1.668 V (ortalama 1.657 V). Örnek sayısı kısa olduğundan bu aralıklar istatistiksel kararlılık iddiası değildir.
- **AĞ:** Wi-Fi Connected YES, IP 192.168.0.31; ESPHome API handshake başarılı.
- **BROWNOUT AYRIMI:** Önceki ayrı logda OTA rollback/brownout uyarısı vardı. Bu ilk bağlantısız ADC logunda brownout mesajı görünmüyor; bu kayıt önceki olayın nedenini açıklamaz.
- **SONUÇ:** Firmware'in cihazda çalıştığı ve dört ADC kanalının başlatıldığı LOG İLE DESTEKLENDİ. SCT okuma performansı, 100 W ampul tepkisi ve gerçek bağlantı doğrulanmadı. T010 AKTİF kalır; üç ayrı 100 W kanal testi bekliyor.
- **KAYNAK DOSYA ÖZETİ:** Kullanıcı ekindeki özgün log: 203 satır, 11,363 bayt; SHA-256 `88f897b2603815233b0c44e497261169be2e6bff73368b435ae04e38ebb312b3`. Depodaki kayıt dosyası önemli kurulum ve örnek satırlarını korur; özgün tam metin kullanıcı ekinde kalır ve SHA-256 özetiyle tanımlanır.

## 1. Amaç

Üç SCT sensörünün ayrı analog sinyallerini modül içine gömülü ESP32D1 ile okumak ve üç girişin ortak kullandığı tek bias seviyesini dördüncü ADC girişinden izlemek.

Modül harici 5 V DC ile beslenecek. ESP'nin USB bağlantısı PC'ye erişim/servis bağlantısı için kullanılabilir durumda tutulacak.

## 2. Modül içeriği

- 3 adet 3,5 mm dişi SCT girişi.
- Modül içine gömülü ESP32 kartı + GPIO shield/terminal genişletme kartı (ESP32D1 assembly).
- Kutu içine gömülü Bias Trafosu modülü ve ortak bias devresi.
- Kapalı kutu içinde ESP32D1, GPIO shield, üç SCT giriş bağlantısı ve bias devresi.
- Kutu dışından gelen harici 5 V DC besleme.
- ESP32 USB portuna PC bağlantısı/servis erişimi.

**Kutu dışında:** 220–240 V AC giriş/çıkış, PZEM-004T, SSR ve kutu içi şebeke kaynaklı 5 V güç kaynağı.

## 3. Modül 2 bağlantı şeması

Aşağıdaki çizim, şu ana kadar bildirilen işlevsel bağlantı planıdır. GPIO/kablo eşleştirmeleri kullanıcı bildirimidir. Jack tip/ring/sleeve uçları, bias devresinin kesin düğümleri ve shield üzerindeki fiziksel terminaller henüz ölçülerek doğrulanmadı. Bu nedenle çizim, jack iç bağlantı pinout'u veya üretime hazır elektrik şeması değildir.

```text
                 KAPALI MODUL KUTUSU
+-----------------------------------------------------------+
|                                                           |
|  BIAS TRAFOSU MODULU                                      |
|       |                                                   |
|       v                                                   |
|  ORTAK BIAS DEVRESI                                       |
|       |---------------------> SCT-1 bias noktasi          |
|       |---------------------> SCT-2 bias noktasi          |
|       |---------------------> SCT-3 bias noktasi          |
|       |                                                   |
|       +---- TURUNCU --------------------> GPIO35 / ADC1   |
|       +---- GND ------------------------> ESP32 GND       |
|                                                           |
|  SCT-1 sinyal -- SARI ------------------> GPIO32 / ADC1   |
|  SCT-2 sinyal -- YESIL -----------------> GPIO33 / ADC1   |
|  SCT-3 sinyal -- MAVI ------------------> GPIO34 / ADC1   |
|                                                           |
|  +----------------------+                                 |
|  | ESP32D1 + GPIO SHIELD|                                 |
|  +----------------------+                                 |
|                                                           |
+-----------------------------------------------------------+
       ^                              ^
       |                              |
HARICI 5 V DC                  USB -> PC / SERVIS
(kutu disindan)
```

`*` İşaretleri ortak bias düğümünün üç kanala dağıtılması fikrini gösterir; gerçek direnç/kondansatör bağlantı noktalarını veya jack kontaklarını tarif etmez. Bu noktalar bias devresi ve kablo süreklilik ölçümüyle netleştirilecektir.

### 3.1 Kanal bağlantı tablosu

| Kanal | SCT yuvası / işlev | Kablo rengi | GPIO | ESP32 klasik pin işlevi |
|---:|---|---|---:|---|
| 1 | SCT-1 sinyal girişi | Sarı | GPIO32 | ADC1_CH4 |
| 2 | SCT-2 sinyal girişi | Yeşil | GPIO33 | ADC1_CH5 |
| 3 | SCT-3 sinyal girişi | Mavi | GPIO34 | ADC1_CH6 |
| 4 | Ortak bias ölçümü | Turuncu | GPIO35 | ADC1_CH7 |

GPIO işlev adları klasik ESP32 varyantı içindir; kartın tam modeli/revizyonu ve ESPHome pin desteği ayrıca doğrulanacaktır.

### 3.2 100 W akkor ampul ile kanal bazlı test planı

Üç SCT kanalı aynı 100 W akkor ampul/yük koşulunda **tek tek** denenecek. Bir test adımında yalnız test edilen SCT kanalı yük akımını görecek; diğer iki SCT kanalı test dışı/boşta kalacak. Dördüncü kanal GPIO35 ortak bias seviyesini izler; 100 W yük kanalı değildir ve her test boyunca ayrıca gözlenecektir.

| Test sırası | Test edilen SCT kanalı | Kablo | GPIO | Yük | Sonuç |
|---:|---|---|---:|---|---|
| 1 | SCT-1 | Sarı | GPIO32 | 100 W akkor ampul | Bekliyor |
| 2 | SCT-2 | Yeşil | GPIO33 | 100 W akkor ampul | Bekliyor |
| 3 | SCT-3 | Mavi | GPIO34 | 100 W akkor ampul | Bekliyor |

**Her kanal için kayıt:** Yük kapalı başlangıç değeri, ampul açık kararlı bölümdeki ADC gerilimi, ampul kapatıldıktan sonraki değer, GPIO35 bias değeri, Home Assistant zaman aralığı ve varsa ESPHome logu. Henüz hiçbir test sonucu girilmemiştir.

**Test yöntemi:** Aynı ampul ve aynı test düzeneği korunur; kanallar sırayla test edilir. SCT, yalnız tek bir yalıtılmış iletkeni çevrelemelidir; faz ve nötr birlikte SCT içinden geçirilmez. CT'nin yerini/kanalını değiştirirken ampul devresi enerjisiz bırakılır. Şebeke bağlantıları kapalı/korumalı hazır lamba düzeneğinde yapılmalı; açıkta 230 V iletken veya breadboard bağlantısı bulunmamalıdır. Bu işlem şebeke tarafı içerdiğinden, güvenli ve yalıtılmış test düzeneği yoksa test yapılmaz.

## 4. Analog sinyal düzeni

Toplam dört ADC giriş noktası hedeflenir:

1. SCT-1 ayrı sinyal hattı.
2. SCT-2 ayrı sinyal hattı.
3. SCT-3 ayrı sinyal hattı.
4. Üç SCT'ye ortak dağıtılan tek bias/Vmid düğümünün bir kez ölçülmesi.

Tek bir ortak bias devresi kullanılacaktır. Bias Trafosu modülü ve ortak bias devresi kapalı kutu içine gömülüdür. Ortak bias seviyesi üç SCT girişine dağıtılır; her SCT için ayrı bias kaynağı yapılmaz. Ortak bias seviyesi üç SCT girişine dağıtılır; her SCT için ayrı bias kaynağı yapılmaz.

## 5. Bildirilen fiziksel GPIO eşleştirmeleri

| SCT yuvası | Sinyal kablosu | GPIO shield terminali | Kanıt durumu |
|---|---|---|---|
| 1. dişi yuva | Sarı | GPIO32 | Kullanıcı bildirimi |
| 2. dişi yuva | Yeşil | GPIO33 | Kullanıcı bildirimi |
| 3. dişi yuva | Mavi | GPIO34 | Kullanıcı bildirimi |
| Ortak bias ölçümü | Turuncu | GPIO35 | Kullanıcı bildirimi |

Güncel yuva bazlı kullanıcı bildirimleri: 1. yuva sarı → GPIO32; 2. yuva yeşil → GPIO33; 3. yuva mavi → GPIO34; ortak bias ölçüm kablosu turuncu → GPIO35. Önceki genel kablo rengi notunda kırmızı hattın ortak bias olduğu belirtilmişti; yeni bağlantı tarifinde bias ölçüm kablosu turuncu olarak bildirildiğinden, fiziksel kablo güzergâhı/renk teyidi montaj sırasında yapılmalıdır.

Jack tip/ring/sleeve uçlarının tamamı henüz doğrulanmadı. Kablo rengi ve yuva sırası tek başına jak pinout'unun doğrulandığı anlamına gelmez.

## 6. ESPHome başlangıç dosyası

Dosya: [firmware/esp32d1.yaml](../../firmware/esp32d1.yaml).

Kullanıcının sağladığı başlangıç kimliği ve yapılandırma:
- `esphome.name: esp32d1`
- `friendly_name: ESP32D1`
- `variant: esp32`
- `framework: esp-idf`
- logger, API, OTA ve Wi-Fi.

YAML, kullanıcının sağladığı temel ESPHome yapılandırması korunarak ilk ADC giriş kontrolü seviyesine genişletildi. GPIO32/33/34 için üç ayrı SCT ADC gerilim sensörü ve GPIO35 için ortak bias ADC gerilim sensörü tanımlıdır. Dört sensör 1 saniye aralıkla voltaj örneği yayınlar. Bu okumalar anlık ADC gerilimidir; RMS/akım hesabı, ct_clamp, katsayı veya filtre içermez. Kodun derlenmesi, OTA yüklemesi ve gerçek cihaz testi henüz yapılmamıştır.

## 7. Açık bağlantı ve tasarım noktaları

- ESP32 kartının tam modeli ve revizyonu.
- GPIO shield modeli ve terminal/pin eşleşmesi.
- Üç jack'in tip/ring/sleeve pinout'u.
- Bias mini breadboard üzerindeki elektrolitik kondansatörün değeri, polaritesi ve kesin bağlantısı.
- Bias ADC'nin ESPHome'da RAW count mı, voltaj mı yayınlayacağı.
- USB konektör tipi ve 5 V güç yolu.
- Harici 5 V ile PC USB'nin aynı anda bağlanabilmesi için kartın güç yolu/geri besleme tasarımı.
- Üç kanallı SCT okumada kullanılacak çalışan ESPHome örneği ve minimum uyarlama.

## 8. Besleme ve bağlantı güvenliği

- ESP32 ve kutu içi Bias Trafosu modülü, tasarlanan besleme düzenine göre harici 5 V DC kaynaktan beslenecek; 5 V ADC/GPIO pinlerine uygulanmaz. Bias modülünün besleme gereksinimi/çıkışı ölçülerek doğrulanmalıdır.
- USB üzerinden PC bağlantısı isteniyor. Harici 5 V ile PC USB aynı anda bağlı olacaksa kartın şeması/kılavuzundan güç yolu ve geri besleme koruması doğrulanmadan iki kaynak birlikte bağlanmaz.
- Bias devresi GND'si ve ESP32 GND ortak referans olmalıdır; kesin bağlantı noktaları fiziksel kart ve bias devresi görülerek teyit edilir.
- Bias/Vmid ve SCT analog düğümlerinin gerilimleri doğrulanmadan ESP32 ADC pinlerine bağlantı yapılmaz.
- Açık breadboard yalnız düşük gerilim bias devresi içindir; modül içinde şebeke gerilimi bulunmaz.
- CT sekonderinin açık bırakılması konusunda ilgili SCT modelinin üretici talimatı gözetilir.

## 9. Doğrulama durumu

Modülün kapalı kutu içinde toplandığı, ESP32D1 ve Bias Trafosu modülünün kutuya gömüldüğü, üç SCT kanalı bulunduğu ve kutunun harici 5 V DC ile besleneceği kullanıcı tarafından bildirildi. Dört GPIO eşlemesi: GPIO32 (1. yuva sarı), GPIO33 (2. yuva yeşil), GPIO34 (3. yuva mavi), GPIO35 (ortak bias turuncu). Kanal tablosu ve 100 W akkor ampulle üç ayrı kanal testi depoya eklendi. Derleme, GPIO/jack fiziksel teyidi, analog düğüm gerilimleri, besleme/USB güç yolu ve üç kanalın gerçek test sonuçları beklemededir.

**Durum özeti:** Kapalı kutu montajı kullanıcı beyanıyla kaydedildi. İlk dört kanallı ADC YAML kodu depoda. Kod derlenmedi; üç SCT kanalının 100 W ampulle ayrı ayrı testi yapılmadı. Modül çalışır/tamamlandı olarak işaretlenmemiştir.
