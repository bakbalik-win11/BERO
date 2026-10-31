# BERO Modül 2 — Üçlü SCT Okuma Modülü

**Modül kimliği:** BERO-SCT-OKUMA-TEST-002  
**ESPHome kimliği:** `esp32d1` / `ESP32D1`  
**Durum:** TASARIM / DONANIM HAZIRLIĞI — henüz imal ve test edilmedi  
**Görev:** [T010 — Modül 2 üçlü SCT devreye alma](../../tasks/T010-module2-triple-sct-bringup.md)  
**Karar:** [ADR-015](../decisions/ADR-015-module2-esp32d1-triple-sct.md)

## 1. Amaç

Üç SCT sensörünün ayrı analog sinyallerini modül içine gömülü ESP32D1 ile okumak ve üç girişin ortak kullandığı tek bias seviyesini dördüncü ADC girişinden izlemek.

Modül harici 5 V DC ile beslenecek. ESP'nin USB bağlantısı PC'ye erişim/servis bağlantısı için kullanılabilir durumda tutulacak.

## 2. Modül içeriği

- 3 adet 3,5 mm dişi SCT girişi.
- Modül içine gömülü ESP32 kartı + GPIO shield/terminal genişletme kartı (ESP32D1 assembly).
- Kayıtlı ortak bias yapısını taşıyan mini breadboard.
- ESP32 için kutu dışından gelen 5 V DC besleme.
- ESP USB portuna PC bağlantısı için fiziksel erişim.

**Kutu dışında:** 220–240 V AC giriş/çıkış, PZEM-004T, SSR ve kutu içi şebeke kaynaklı 5 V güç kaynağı.

## 3. Analog sinyal düzeni

Toplam dört ADC giriş noktası hedeflenir:

1. SCT-1 ayrı sinyal hattı.
2. SCT-2 ayrı sinyal hattı.
3. SCT-3 ayrı sinyal hattı.
4. Üç SCT'ye ortak dağıtılan tek bias/Vmid düğümünün bir kez ölçülmesi.

Tek bir bias devresi kullanılacaktır. Kayıtlı bias devresi mini breadboard üzerinde kurulacak ve Bias Trafosu modülünden beslenecektir. Ortak bias seviyesi üç SCT girişine dağıtılır; her SCT için ayrı bias kaynağı yapılmaz.

## 4. Bildirilen fiziksel GPIO eşleştirmeleri

| SCT yuvası | Sinyal kablosu | GPIO shield terminali | Kanıt durumu |
|---|---|---|---|
| 1. dişi yuva | Sarı | GPIO32 | Kullanıcı bildirimi |
| 2. dişi yuva | Yeşil | GPIO33 | Kullanıcı bildirimi |
| 3. dişi yuva | Henüz bildirilmedi | Henüz belirlenmedi | Açık |
| Ortak bias ölçümü | Ortak bias hattı | Henüz belirlenmedi | Açık |

Önceki kullanıcı bildiriminde kırmızı hattın ortak bias, mavi/yeşil/sarı hatların ayrı SCT sinyalleri olduğu belirtilmişti. Buradaki GPIO32 ve GPIO33 eşleştirmeleri sonradan verilen yuva bazlı bildirimlerdir.

Jack tip/ring/sleeve uçlarının tamamı henüz doğrulanmadı. Kablo rengi ve yuva sırası tek başına jak pinout'unun doğrulandığı anlamına gelmez.

## 5. ESPHome başlangıç dosyası

Dosya: [firmware/esp32d1.yaml](../../firmware/esp32d1.yaml).

Kullanıcının sağladığı başlangıç kimliği ve yapılandırma:
- `esphome.name: esp32d1`
- `friendly_name: ESP32D1`
- `variant: esp32`
- `framework: esp-idf`
- logger, API, OTA ve Wi-Fi.

YAML şimdilik yalnız temel ESPHome iskeletidir. Henüz ADC sensörleri, SCT okuma/ct_clamp bileşenleri, bias sensörü, kalan GPIO atamaları, katsayı veya filtre kodu yoktur. Derleme, OTA yüklemesi veya gerçek cihaz testi yapılmamıştır.

## 6. Açık bağlantı ve tasarım noktaları

- ESP32 kartının tam modeli ve revizyonu.
- GPIO shield modeli ve terminal/pin eşleşmesi.
- Üçüncü SCT sinyal GPIO'su ve ortak bias ADC GPIO'su.
- Üç jack'in tip/ring/sleeve pinout'u.
- Üçüncü girişin kablo rengi ve gerçek bağlantısı.
- Bias mini breadboard üzerindeki elektrolitik kondansatörün değeri, polaritesi ve kesin bağlantısı.
- Bias ADC'nin ESPHome'da RAW count mı, voltaj mı yayınlayacağı.
- USB konektör tipi ve 5 V güç yolu.
- Harici 5 V ile PC USB'nin aynı anda bağlanabilmesi için kartın güç yolu/geri besleme tasarımı.
- Üç kanallı SCT okumada kullanılacak çalışan ESPHome örneği ve minimum uyarlama.

## 7. Besleme ve bağlantı güvenliği

- ESP32 harici 5 V DC kaynaktan beslenecek; 5 V ADC/GPIO pinlerine uygulanmaz.
- USB üzerinden PC bağlantısı isteniyor. Harici 5 V ile PC USB aynı anda bağlı olacaksa kartın şeması/kılavuzundan güç yolu ve geri besleme koruması doğrulanmadan iki kaynak birlikte bağlanmaz.
- Bias devresi GND'si ve ESP32 GND ortak referans olmalıdır; kesin bağlantı fiziksel kart ve bias devresi görülerek çizilecektir.
- Bias/Vmid ve SCT analog düğümlerinin gerilimleri doğrulanmadan ESP32 ADC pinlerine bağlantı yapılmaz.
- Açık breadboard yalnız düşük gerilim bias devresi içindir; modül içinde şebeke gerilimi bulunmaz.
- CT sekonderinin açık bırakılması konusunda ilgili SCT modelinin üretici talimatı gözetilir.

## 8. Doğrulama durumu

Modülün kapsamı ve ESP32D1 kimliği kaydedildi. GPIO32 (1. yuva sarı) ve GPIO33 (2. yuva yeşil) kullanıcı bildirimi olarak kaydedildi. Diğer pinler, kablo eşleştirmeleri, kart modeli, besleme/USB güç yolu, sensör YAML kodu, derleme ve fiziksel test beklemededir.

**Durum özeti:** Tasarım açıldı; modül tamamlanmış veya çalışır olarak işaretlenmemiştir.