# GEMINI.md - Proje Özeti ve Rehberi

Bu dosya, Gemini CLI ajanları için projenin yapısını, donanım bileşenlerini ve çalışma prensiplerini özetleyen ana rehberdir.

## 🚀 Proje Genel Bakış
**Proje Adı:** BERO (Burak'ın Rumelikavağı Emeklilik Otomasyonu)
**Lokasyon:** Rumeli Kavağı, Sarıyer, İstanbul.
**Fazlar:** 
1. **PREBERO (Saha Deney & Veri):** WiFi/HA üzerinden hızlı veri toplama, cihaz karakterizasyonu ve masaüstü laboratuvar testleri.
2. **BERO (Nihai Sistem):** Tam bağımsız RS485 omurgalı dağıtık zeka mimarisi.

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

- **Modül 4:** Günlük kullanılan mevcut masaüstü ESP32D2 + ADS1115 + SCT ölçüm düzeneği.
- **Modül 5:** İmal edilecek çamaşır makinesi gözlem modülü.
- **Modül 6:** İmal edilecek bulaşık makinesi gözlem modülü.
- **Modül 7 / PreBERO:** Ana hattı PZEM ile birlikte okumaya yönelik hedef düzenek; tasarım ve test bekliyor.
- **E22:** Modül değildir. Modül 4'ün ölçüm zinciri kararlı çalıştıktan sonra bir kanalda 30 A / 1 V, diğerinde 100 A / 1 V SCT karşılaştırması yapılması fikridir. Henüz ölçüm alınmadı.
- **E24:** Çoklu ADS1115 / çok kanallı SCT erişimi için ayrı deney/araştırma kaydıdır; modül numarası değildir.

## 🎯 Aktif Odak Alanları
1. **Modül 4:** Mevcut günlük masaüstü ölçüm zincirini korumak ve çalışmasını sürdürmek.
2. **Modül 5/6:** Çamaşır ve bulaşık gözlem modüllerinin imalat hazırlığı.
3. **E22:** Modül 4 başarılı/kararlı olduktan sonra 30 A ve 100 A SCT karşılaştırma fikrini deney koşullarına dönüştürmek.
4. **Modül 7 / PreBERO:** Ana hat + PZEM gözlem hedefini daha sonra tasarlamak.
5. **E21:** Çamaşır makinesi tam program kayıtlarının zaman serisi analizi.
6. **Gürültü Analizi:** ADS1115 üzerindeki anlık sıçramaların (spikes) osiloskop ile incelenmesi.
