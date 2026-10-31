# ADR-015 — Modül 2: ESP32D1 gömülü üçlü SCT okuma modülü

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ — modül kapsamı ve bildirilen bağlantılar
- **Karar sahibi:** Kullanıcı
- **İlişkili kararlar:** ADR-012, ADR-013, ADR-014
- **Kapsam notu:** Bu ADR, ADR-012'nin Modül 2 kutu kapsamını korur; ESP32D2 kimliği/yerleşimi ve ESP besleme yöntemiyle ilgili eski varsayımları günceller. ADR-013'ün tek bias ölçüm noktası kararını korur; bias ADC yazılım gösterim biçimini RAW veya voltaj olarak henüz kesinleştirmez.

## Amaç

Üç SCT sensörünün sinyallerini aynı modül içindeki ESP32 ile okumak ve ortak bias seviyesini tek ADC girişi üzerinden izlemek. Modül harici 5 V DC ile beslenecek; ESP'nin USB bağlantısı üzerinden PC'ye bağlanma imkânı bulunacak.

## Kabul edilen donanım kapsamı

1. Üç adet 3,5 mm dişi SCT girişi.
2. Modül içine yerleştirilmiş ESP32 kartı ve GPIO shield/terminal genişletme kartı (ESP32D1 assembly).
3. Kayıtlı ortak bias devresini taşıyan mini breadboard.
4. ESP32 için modül dışından sağlanan 5 V DC besleme.
5. ESP'nin USB bağlantısıyla PC'ye bağlanma imkânı.

Modül içinde 220–240 V şebeke girişi/çıkışı, PZEM, SSR veya kutu içi şebeke beslemesi bulunmaz.

## İşlevsel analog kanal düzeni

- SCT kanal 1: birinci SCT girişinin ayrı sinyal hattı.
- SCT kanal 2: ikinci SCT girişinin ayrı sinyal hattı.
- SCT kanal 3: üçüncü SCT girişinin ayrı sinyal hattı.
- Bias kanalı: üç SCT girişinde ortak kullanılan tek Vmid/bias noktasının tek ADC girişiyle izlenmesi.

Toplam hedef: **3 bağımsız SCT sinyal okuması + 1 ortak bias okuması = 4 ADC giriş noktası.**

Tek bir bias devresi kullanılacak ve ortak bias seviyesi üç girişe dağıtılacak. Bias seviyesi tek noktadan bir kez ADC ile izlenecek; her SCT için ayrı bias üretimi veya ayrı bias ölçüm girişi planlanmıyor.

## Bildirilen fiziksel bağlantılar

| SCT yuvası | Kablo rengi | Shield terminali | Kanıt durumu |
|---|---|---|---|
| 1. dişi yuva | Sarı | GPIO32 | Kullanıcı bildirimi |
| 2. dişi yuva | Yeşil | GPIO33 | Kullanıcı bildirimi |
| 3. dişi yuva | Henüz bildirilmedi | Henüz belirlenmedi | Açık |
| Ortak bias ölçümü | Ortak bias hattı | Henüz belirlenmedi | Açık |

Önceki kullanıcı bildiriminde kırmızı hat ortak bias hattı, mavi/yeşil/sarı hatlar ayrı SCT sinyal hatları olarak tarif edilmişti. Bu kayıt, 1. ve 2. yuva için sonradan verilen kesin GPIO eşlemesini yansıtır. Jack tip/ring/sleeve pinlerinin tamamı henüz doğrulanmamıştır.

## ESPHome başlangıç yapılandırması

Kullanıcının sağladığı cihaz kimliği ve temel ayarlar:
- esphome.name: esp32d1
- friendly_name: ESP32D1
- ESP32 / ESP-IDF
- logger, Home Assistant API, OTA ve Wi-Fi

Başlangıç dosyası: [firmware/esp32d1.yaml](../../firmware/esp32d1.yaml).

Bu dosya yalnız ESPHome temel iskeletidir. Henüz ADC sensörü, SCT okuma bileşeni, bias sensörü, kalan GPIO eşlemesi veya filtre/katsayı kodu içermez. Derleme, yükleme ve fiziksel çalışma testi yapılmış değildir.

## Henüz kararlaştırılmayan / doğrulanması gerekenler

- ESP32 kartının tam modeli ve revizyonu.
- Shield üzerindeki GPIO pin etiketleri ve ESP32 pinlerine gerçek bağlantısı.
- 3. SCT girişinin sinyal GPIO'su ve kablo rengi.
- Ortak bias ölçümü için kullanılacak ADC GPIO'su.
- ESP'nin 5 V giriş yolunun kart üzerindeki gerçek adı/konumu ve USB konektör tipi.
- Harici 5 V kaynağı ile PC USB bağlantısının aynı anda kullanımına ilişkin kartın güç yolu/geri besleme özelliği.
- Üç adet 3,5 mm jack'in tip/ring/sleeve eşlemesi ve CT kablo renklerinin fiziksel teyidi.
- Bias mini breadboard'daki elektrolitik kondansatörün değeri, polaritesi ve kesin bağlantı yeri.
- Bias ADC entity'sinin RAW count mı yoksa voltaj mı yayınlayacağı.
- SCT kanalları için kullanılacak çalışan ESPHome kod örneği ve minimum uyarlaması.
- Üç SCT kanalının örnekleme/yayınlama yapılandırması ve Home Assistant entity adları.

## Bağlantı ve güvenlik ilkeleri

- Bias devresinin düşük gerilim GND'si ile ESP32 GND ortak referans olmalıdır; kesin bağlantı, gerçek bias ve ESP kartı görülerek çizilecektir.
- Harici 5 V yalnız ESP kartının belgelenmiş 5 V/VIN/USB güç yoluna uygulanır. GPIO veya ADC girişine 5 V verilmez.
- ESP kartının USB'si hem harici besleme hem PC bağlantısı için kullanılacaksa çift beslemenin izin verilip verilmediği kart şeması/kılavuzundan doğrulanmalıdır. Aynı anda iki kaynaktan besleme güvenli varsayılmaz.
- ADC girişleri ESP32'nin izin verilen analog gerilim aralığını aşmamalıdır. Bias ve SCT analog düğümleri ölçülmeden GPIO'lara bağlanmaz.
- Jack pinout'u fiziksel teyit olmadan kablo rengine veya jak geometrisine göre varsayılmaz.
- Kutu içinde şebeke gerilimi bulunmaz; açık breadboard yalnız düşük gerilim bias devresinde kullanılır.
- CT sekonderinin açık bırakılmasına ilişkin SCT modelinin üretici talimatı gözetilir.

## Doğrulama durumu

Bu ADR modülün amaç ve işlevsel kapsamını ve kullanıcı tarafından bildirilen iki bağlantıyı kaydeder. Kutu imalatı, diğer kablo bağlantıları, pin eşlemesi, YAML sensör kodu, derleme, OTA ve gerçek donanım testi henüz yapılmamıştır.

**Sonuç:** Modül 2'nin hedefi ESP32D1 gömülü, harici 5 V beslemeli, PC USB bağlantısına erişilebilir; üç SCT sinyali ve bir ortak bias ölçümü olan düşük gerilim SCT okuma modülüdür.