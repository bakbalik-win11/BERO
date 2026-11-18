# GEMINI.md - Proje Özeti ve Rehberi

Bu dosya, Gemini CLI ajanları için projenin yapısını, donanım bileşenlerini ve çalışma prensiplerini özetleyen ana rehberdir.

## 🚀 Proje Genel Bakış
**Proje Adı:** BERO (Burak'ın Rumelikavağı Emeklilik Otomasyonu)
**Lokasyon:** Rumeli Kavağı, Sarıyer, İstanbul.
**Temel Hedef:** Tam bağımsız, öğrenen ve gelişen bir ev otomasyonu ekosistemi.
**Felsefe:** Ticari kapalı ekosistemlerden (Apple/Aqara vb.) bağımsız, tamiri ve geliştirilmesi gelecekte (ör. aile bireyleri veya teknik personel) dökümantasyonla mümkün olan evrensel bir yapı.

## 🏗 Altyapı ve Haberleşme Stratejisi
- **Haberleşme Önceliği:** RS485 (Modbus) ana omurgadır. WiFi sadece OTA (güncelleme) için RS485 üzerinden gelen komutla geçici olarak açılır.
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
- **SCT013-100 (100A / 1V):** Ana hat veya yüksek akım izleme için yedek stok.
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

## 🎯 Aktif Odak Alanları
1. **Modül 4 Kurulumu:** Tek ESP32 + 3 ADS1115 + 6 SCT hedefi (E24).
2. **Yük Karakterizasyonu:** Çamaşır makinesi tam program analizi (E21).
3. **Gürültü Analizi:** ADS1115 üzerindeki anlık sıçramaların (spikes) osiloskop ile incelenmesi.
