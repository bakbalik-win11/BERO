# T010 — Modül 2: ESP32D1 üçlü SCT okuma modülünü oluşturma

- **Durum:** AKTİF — tasarım ve donanım hazırlığı
- **Faz:** Faz 2 — Pratik yeniden kurulum ve sistem geliştirme
- **Modül:** BERO-SCT-OKUMA-TEST-002
- **Karar:** [ADR-015](../docs/decisions/ADR-015-module2-esp32d1-triple-sct.md)

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
| 3. dişi yuva | Açık | Açık | Bekliyor |
| Ortak bias ADC | Ortak bias hattı | Açık | Bekliyor |

Bu eşleştirmeler kullanıcı bildirimidir; jakın tip/ring/sleeve pin diziliminin tamamı fiziksel olarak doğrulanmış değildir.

## Kod durumu

Başlangıç ESPHome iskeleti [esp32d1.yaml](../firmware/esp32d1.yaml) dosyasına kaydedildi. Cihaz kimliği esp32d1 / ESP32D1 olarak kullanıcı tarafından sağlandı.

YAML henüz ADC/SCT/bias sensör bileşenleri içermez. GPIO32 ve GPIO33 için sensör kodu, kalan GPIO ataması, ct_clamp yapılandırması, entity adları ve katsayı/filtre kodu henüz eklenmedi. Derleme veya cihaz testi yapılmadı.

## İş sırası

1. ESP32 kartı ve takılı GPIO shield'ın tam modelini/revizyonunu belirle.
2. ESP kartındaki USB konektörünü ve 5 V güç giriş yolunu doğrula. PC USB ve harici 5 V birlikte kullanılacaksa kartın güç yolu/geri besleme korumasını kontrol et.
3. Üç jack ve ortak bias mini breadboard bağlantılarını fiziksel olarak izle; tip/ring/sleeve pinout'unu doğrula.
4. İlk iki bildirilen eşleştirmeyi (GPIO32 sarı, GPIO33 yeşil) fiziksel olarak teyit et; üçüncü SCT ve bias için GPIO seç.
5. Tek ortak bias bağlantısını üç SCT sinyal girişine nasıl dağıtacağını mevcut bias devresi üzerinde doğrula.
6. Bias ölçüm entity'sinin RAW count veya voltaj gösterimini kararlaştır; tek fiziksel bias ADC girişi kullan.
7. Üç kanallı SCT için çalışan ESPHome örneği bul; minimum uyarlamayla yapılandır.
8. Önce YAML derleme kontrolü, sonra uygun düşük gerilim bağlantısı ve gerçek donanım testi yap.
9. Başarılı YAML, gerçek cihaz logu/çıktısı ve yorumunu depoda sakla.

## Açık noktalar

- ESP32 kart model/revizyonu ve GPIO shield modeli.
- USB konektör tipi; harici 5 V ve PC USB'nin aynı anda kullanımı.
- Üçüncü SCT sinyal GPIO'su ve ortak bias ADC GPIO'su.
- Üç jack'in tip/ring/sleeve pinout'u ve diğer kabloların fiziksel eşlemesi.
- Bias devresinin elektrolitik kondansatör değeri/polaritesi ve Bias Trafosu modülünden besleme bağlantısı.
- Bias ADC'nin yazılım gösterimi (RAW count veya voltaj).
- Üç kanallı okuma için seçilecek çalışan ESPHome örneği.

## Bağlantı ve güvenlik koşulları

- Harici 5 V yalnız kartın belgelenmiş girişine bağlanır; ADC/GPIO girişlerine verilmez.
- PC USB ile harici 5 V'un eşzamanlı bağlanması, kart güç devresi doğrulanmadan yapılmaz.
- ESP32 GND ve bias devresi GND ortaklanır; bağlantı noktaları devre görülerek doğrulanır.
- Analog giriş gerilimi ESP32 ADC giriş sınırları içinde olmalıdır.
- Jack pinout'u doğrulanmadan SCT kabloları bağlanmaz.
- Modül 2 yalnız düşük gerilim tarafıdır; 220–240 V bağlantı kutu kapsamı dışındadır.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Modül 2'nin elektriksel ve yazılımsal yapısını uygulanabilir hâle getirmek.
- **LOG:** Kullanıcının esp32d1 ESPHome temel ayarları ve 1. yuva sarı/GPIO32 ile 2. yuva yeşil/GPIO33 bildirimleri kaydedildi.
- **SONUÇ:** Modül kapsamı ve iki sinyal eşlemesi kayıtlı. Üçüncü SCT/bias pinleri, kart doğrulaması, ADC/SCT kodu, derleme ve fiziksel test beklemede. Modül tamamlanmış değildir.