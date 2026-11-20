# GEMINI.md - Proje Özeti ve Rehberi

Bu dosya, Gemini CLI ajanları için projenin yapısını, donanım bileşenlerini ve çalışma prensiplerini özetleyen ana rehberdir.

## 🚀 Proje Genel Bakış
**Proje Adı:** BERO (Burak'ın Rumelikavağı Emeklilik Otomasyonu)
**Lokasyon:** Rumeli Kavağı, Sarıyer, İstanbul.
**Fazlar:** 
1. **PREBERO:** BERO'nun kurulacağı eve henüz taşınılamadığı, o evdeki kiracı çıkana kadar Sarıyer'deki mevcut evde yürütülen gözlem, deney ve veri toplama dönemi. Mevcut evdeki çamaşır makinesi, bulaşık makinesi ve ana hat izlenerek BERO'ya geçmeden önce ilerleme sağlanır.
2. **BERO (Nihai Sistem):** Taşınılacak/kurulacak evde devreye alınacak nihai sistem; PREBERO ile aynı şey değildir.

## 🏗 Altyapı ve Haberleşme Stratejisi
- **Haberleşme:** RS485 (Modbus) ana omurgadır. PREBERO fazında WiFi/HA geçici olarak kullanılır.
- **Uç Birim Zekası (Edge Intelligence):** Düğümler (ESP32), HA veya ekran bağlantısı kopsa dahi görevlerini bağımsız sürdürür ve yerel veri kaydı yapar.
- **Ekran Düğümleri:** ESP32-S3 tabanlı (4.3" / 7") merkezi ve bölgesel gösterim üniteleri.
- **Kablolama (Dual CAT Yapısı):**
    - **CAT-1 (Mavi/Standart):** Odalar için yüksek hızlı internet/WiFi.
    - **CAT-2 (Farklı Renk):** RS485 (A-B), Ekranlar için Ethernet ve **24V DC Dağıtımı** (Bölgesel olarak 5V'a düşürülür).
- **Yazılım Katmanları:** Uç birimlerde (ESP32) yerel işleyiş, merkezde (HA/Python) derin öğrenme ve analiz.

## 🛠 Donanım Bileşenleri
...

### İşlemciler
- **ESP32-D1 / D2:** Ana ölçüm düğümleri.
- **ESP32-C3:** SSR/Kontrol görevleri.
- **ESP32-WROOM:** Genişleme ve PZEM okuma.

### Sensörler ve ADC
- **ADS1115:** 16-bit hassas ADC (I2C üzerinden bağlanır). Ana ölçüm zincirinin kalbi.
- **SCT013-030 (30A / 1V):** Temel akım trafosu.
- **SCT013-100 (100A / 1V):** E22 kapsamında Modül 4 üzerinde ileride 30 A / 1 V ile karşılaştırılması düşünülen sensör; henüz bu deneyde kullanılmadı.
- **PZEM-004T V3.0:** Referans ölçüm cihazı (UART üzerinden bağlanır).

### Diğer Donanımlar
- **SSR (Solid State Relay):** Cihaz kontrolü ve test senaryoları için.
- **DS3231 RTC:** Hassas zaman damgası (zamanla bağımlılık azaltılmaktadır).
- **FNIRSI 2D15P Osiloskop:** Sinyal bütünlüğü ve gürültü analizi için (Kargoda/Yeni).

## 📂 Dosya Düzeni ve Klasör Rehberi

- `/firmware`: ESPHome YAML yapılandırmaları. `esp32d2.yaml` aktif referanstır.
- `/experiments`: Deney protokolleri ve sonuçları. (E19: Spike analizi, E21: Çamaşır makinesi).
- `/logs`: Ham veri kayıtları, analiz raporları ve istatistikler.
- `/docs/decisions`: ADR (Architectural Decision Records) - Mimari karar kayıtları.
- `/tasks`: T001-T010 arası tanımlanmış proje görevleri.
- `/hardware`: Şemalar, bias devreleri ve envanter bilgileri.
- `STATUS.md`: Projenin anlık "neyin üzerinde çalışıyoruz" özeti.
- `PROGRESS_TREE.md`: Görevlerin hiyerarşik başarı durumu.
- `MEMORY.md`: Gemini'nin oturumlar arası süreklilik hafızası.

## 📝 Çalışma Prensipleri

1. **Surgical Edits:** Dosya değişikliklerinde `replace` aracıyla minimum dokunuş yapılmalı.
2. **Empirical Verification:** Her kod değişikliği, derleme veya fiziksel log ile doğrulanmalıdır.
3. **Safety First:** ADS1115 giriş sınırları (GND-VDD) her zaman gözetilmeli, enerjili testlerden önce fiziksel doğrulama aranmalıdır.
4. **Documentation:** Yapılan her önemli analiz veya deney, ilgili klasöre `README.md` veya `report.md` olarak işlenmelidir.
5. **Context Efficiency:** Bilgi aramada `grep_search` ve `glob` araçları önceliklidir.

## Modül Kimlikleri — Güncel Kullanıcı Kararı

- **Modül 1:** Mevcut bias trafosu/güç kutusu; korunuyor ve Modül 4 masaüstü biaslı/bias'sız deneylerinde kullanılacak.
- **Modül 2:** Eski üç kanallı biaslı SCT fiziksel modülü imha edildi. ADS1115 ile istenen akım ölçüm sınırları sağlandığından eski fiziksel düzeneğe ihtiyaç kalmadı. Kod/log arşiv.
- **Modül 3:** Eski PZEM + SSR olay fiziksel modülü imha edildi. Kod/log arşiv.
- **Modül 4:** Günlük masaüstü ESP32D2 + ADS1115 + SCT deney düzeneği; biaslı/bias'sız karşılaştırmalar burada.
- **Modül 5 — PREBERO:** Sarıyer'deki mevcut evin çamaşır makinesini gözlemler.
- **Modül 6 — PREBERO:** Sarıyer'deki mevcut evin bulaşık makinesini gözlemler.
- **Modül 7 — PREBERO:** Sarıyer'deki mevcut evin ana hattını PZEM ile birlikte gözlemler.
- **PREBERO:** BERO'nun kurulacağı eve henüz taşınılamadığı ve o evdeki kiracı çıkana kadar mevcut Sarıyer evinde yürütülen saha gözlem/deney/veri toplama dönemidir. Modül 5, 6 ve 7'nin tamamı PREBERO'dur.
- **E22:** Modül değildir; Modül 4'te 30 A / 1 V ve 100 A / 1 V SCT karşılaştırma fikri. Henüz 100 A SCT ölçümü alınmadı.
- **E24:** Çoklu ADS1115 / çok kanallı SCT erişimi için ayrı deney/araştırma kaydıdır; modül numarası değildir.

## 🎯 Aktif Odak Alanları
1. **Modül 4:** Masaüstü ölçüm düzeneğini kullanmak; biaslı/bias'sız deneyleri Modül 1 bias trafosunu koruyarak yürütmek.
2. **PREBERO Modül 5/6:** Sarıyer'deki mevcut evde çamaşır ve bulaşık makinesi gözlem modüllerini imal edip veri toplamak.
3. **PREBERO Modül 7:** Aynı evin ana hattını PZEM ile birlikte izlemek ve veri toplamak.
4. **E22:** Modül 4 ölçüm zinciri kararlı olduktan sonra 30 A ve 100 A SCT karşılaştırma fikrini deney koşullarına dönüştürmek.
5. **E21:** Çamaşır makinesi tam program kayıtlarının zaman serisi analizi.
6. **Gürültü Analizi:** ADS1115 üzerindeki anlık sıçramaların (spikes) osiloskop ile incelenmesi.