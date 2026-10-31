# T010 — Modül 2: ESP32D1 üçlü SCT okuma modülünü oluşturma

- **Durum:** AKTİF — tasarım ve donanım hazırlığı
- **Faz:** Faz 2 — Pratik yeniden kurulum ve sistem geliştirme
- **Modül:** BERO-SCT-OKUMA-TEST-002
- **Karar:** [ADR-015](../docs/decisions/ADR-015-module2-esp32d1-triple-sct.md)

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

## Hedef

Modül içine gömülü ESP32D1 ile üç bağımsız SCT sinyalini ve tek ortak bias noktasını okuyacak modülü oluşturmak. ESP harici 5 V ile beslenecek ve USB üzerinden PC'ye bağlanma imkânı korunacak.

## Kabul edilen işlevsel yapı

- 3 adet 3,5 mm dişi SCT girişi.
- Tek ortak bias devresi; kayıtlı bias yapısı mini breadboard üzerinde.
- Üç SCT için ayrı sinyal bağlantısı.
- Üç SCT'ye ortak dağıtılan bias noktasının tek ADC girişiyle izlenmesi.
- Toplam dört ADC giriş noktası: üç SCT sinyali + tek bias ölçümü.
- Modül içine gömülü ESP32 assembly: ESP32 kartı + GPIO shield.
- Harici 5 V DC besleme.
- ESP USB portundan PC bağlantısına erişim.
- Modül kutusunda şebeke, PZEM veya SSR bulunmaması.

## Bildirilen fiziksel eşleştirmeler

| SCT yuvası | Sinyal kablosu | Shield GPIO | Durum |
|---|---|---|---|
| 1. dişi yuva | Sarı | GPIO32 | Kullanıcı bildirdi |
| 2. dişi yuva | Yeşil | GPIO33 | Kullanıcı bildirdi |
| 3. dişi yuva | Mavi | GPIO34 | Kullanıcı bildirdi |
| Ortak bias ADC | Turuncu | GPIO35 | Kullanıcı bildirdi |

Dört eşleştirme de kullanıcı bildirimidir. Jakların tip/ring/sleeve pin diziliminin ve kabloların gerçek terminal güzergâhının tamamı fiziksel olarak doğrulanmış değildir.

## Kutu montajı ve 100 W kanal testi

**Kullanıcı bildirimi:** ESP32D1, üç SCT kanal bağlantısı ve Bias Trafosu modülü kapalı kutu içine gömüldü. Kutu harici 5 V DC ile beslenecek. Bu bilgi montaj beyanıdır; güç yolu/gerilim ölçümü veya çalışma testi anlamına gelmez.

| Test sırası | SCT kanalı | Kablo | GPIO | Test yükü | Sonuç |
|---:|---|---|---:|---|---|
| 1 | SCT-1 | Sarı | GPIO32 | 100 W akkor ampul | Bekliyor |
| 2 | SCT-2 | Yeşil | GPIO33 | 100 W akkor ampul | Bekliyor |
| 3 | SCT-3 | Mavi | GPIO34 | 100 W akkor ampul | Bekliyor |

Her testte aynı 100 W akkor ampul kullanılacak ve SCT kanalları sırayla, ayrı ayrı denenecek. GPIO35 ortak bias ADC kanalıdır; yük kanalı değildir ve her adımda izlenecektir. Yük kapalı başlangıç, açık kararlı bölüm ve kapatma sonrası değerleri ile GPIO35 bias değeri kaydedilecek. Test sonuçları henüz mevcut değildir.

**Güvenli test koşulu:** SCT, yalnız tek yalıtılmış iletkeni çevrelemelidir; faz ve nötr birlikte geçirilmez. CT bağlantısı/kanal değişimi yük enerjisizken yapılır. Şebeke tarafı kapalı ve korumalı lamba düzeneğinde tutulur; açıkta 230 V bağlantı veya breadboard kullanılmaz.

## Kod durumu

Başlangıç ESPHome iskeleti [esp32d1.yaml](../firmware/esp32d1.yaml) dosyasına kaydedildi. Cihaz kimliği esp32d1 / ESP32D1 olarak kullanıcı tarafından sağlandı.

İlk ADC giriş kontrolü YAML'ı eklendi: GPIO32/33/34 üzerinde üç SCT ADC gerilim sensörü ve GPIO35 üzerinde ortak bias ADC gerilim sensörü bulunur. Kod anlık gerilim yayınlar; RMS/akım hesabı içermez. Derleme ve cihaz testi yapılmadı.

## İş sırası

1. ESP32 kartı ve takılı GPIO shield'ın tam modelini/revizyonunu belirle.
2. ESP kartındaki USB konektörünü ve 5 V güç giriş yolunu doğrula. PC USB ve harici 5 V birlikte kullanılacaksa kartın güç yolu/geri besleme korumasını kontrol et.
3. Üç jack ve ortak bias mini breadboard bağlantılarını fiziksel olarak izle; tip/ring/sleeve pinout'unu doğrula.
4. Bildirilen dört eşleştirmeyi (GPIO32 sarı, GPIO33 yeşil, GPIO34 mavi, GPIO35 turuncu bias) fiziksel olarak teyit et.
5. Tek ortak bias bağlantısını üç SCT sinyal girişine nasıl dağıtacağını mevcut bias devresi üzerinde doğrula.
6. İlk sürümde dört ADC kanalı voltaj olarak tanımlandı; fiziksel bias gerilimi ölçülerek Home Assistant değeriyle karşılaştırılacak.
7. İlk ADC giriş kontrolü YAML'ını derle; derleme sonucunu kaydet.
8. Analog düğümlerin gerilimini multimetreyle doğrula; sonra düşük gerilim bağlantısı ve dört kanalın HA yayını testini yap.
9. Başarılı derleme/cihaz logu, gerçek sensör çıktısı ve yorumunu depoya ekle. SCT akım/RMS okuma yaklaşımı ancak bu temel aşama doğrulandıktan sonra seçilecek.

## Açık noktalar

- ESP32 kart model/revizyonu ve GPIO shield modeli.
- USB konektör tipi; harici 5 V ve PC USB'nin aynı anda kullanımı.
- Dört GPIO'nun gerçek ESP32 kartı ve shield terminaliyle birebir eşleştiğinin fiziksel teyidi.
- Üç jack'in tip/ring/sleeve pinout'u ve dört rengin gerçek terminal güzergâhının fiziksel teyidi.
- Bias devresinin elektrolitik kondansatör değeri/polaritesi ve Bias Trafosu modülünden besleme bağlantısı.
- Bias ADC'nin yazılım gösterimi (RAW count veya voltaj).
- SCT sinyalinden akım/RMS üretmek için sonraki aşamada seçilecek çalışan okuma yaklaşımı.

## Bağlantı ve güvenlik koşulları

- Harici 5 V yalnız kartın belgelenmiş girişine bağlanır; ADC/GPIO girişlerine verilmez.
- PC USB ile harici 5 V'un eşzamanlı bağlanması, kart güç devresi doğrulanmadan yapılmaz.
- ESP32 GND ve bias devresi GND ortaklanır; bağlantı noktaları devre görülerek doğrulanır.
- Analog giriş gerilimi ESP32 ADC giriş sınırları içinde olmalıdır.
- Jack pinout'u doğrulanmadan SCT kabloları bağlanmaz.
- Modül 2 yalnız düşük gerilim tarafıdır; 220–240 V bağlantı kutu kapsamı dışındadır.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Modül 2'nin elektriksel ve yazılımsal yapısını uygulanabilir hâle getirmek.
- **LOG:** Kullanıcının ESPHome temel ayarları, dört bağlantı bildirimi, kapalı kutu montajı, kutu içindeki Bias Trafosu modülü ve harici 5 V besleme planı kaydedildi.
- **SONUÇ:** GPIO eşleştirme tablosu ve 100 W akkor ampulle üç ayrı kanal test planı depoda. Üç test sonucu, derleme ve fiziksel çalışma doğrulaması beklemede. Modül tamamlanmış değildir.