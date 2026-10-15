# HDF2-GRV-001 — Hedef 2 Test Donanımının Kurulması

**Amaç:** Hedef 2 test donanımını fiziksel olarak kurmak, bağlantıları doğrulamak ve veri toplama deneylerine hazır hâle getirmek.

**Durum:** Açık — donanım ayrıntıları kullanıcı tarafından aşamalı olarak verilecek.  
**Alt Görev 1:** ✅ Tamamlandı — ESP32 cihazlarının Home Assistant/ESPHome tarafına tanıtılması.  
**Kanıt:** 2026-10-15 tarihinde paylaşılan Home Assistant/ESPHome cihaz bilgisi ekran görüntüsünde `ESP32D1` çevrimiçi (`Device Online`) görünüyor. Cihaz bilgileri aşağıda kaydedilmiştir. Bu kanıt ağ üzerinden erişilebilirliği gösterir; ölçüm kanalları, BIAS, örnekleme ve veri doğruluğu henüz doğrulanmış sayılmaz.  
**Kanıt durumu:** Alt Görev 1 tamamlandı. Fiziksel test donanımının bütünü, ölçüm bağlantıları, derleme ve veri testleri henüz tamamlanmış/PASS olarak kaydedilmedi.

## 1. Geçici donanım planı

### A. Akım ölçüm grubu
Ölçüm donanımında şu üç ESP kullanılacak:
- ESP32D1
- ESP32D2
- ESP32E1

Bu ESP'lerle **1T, 2T ve 4T olarak adlandırılan üç kanalda ölçüm** ve **BIAS okuması** yapılacak. Kanal dağılımı, sensör bağlantıları, pinler, örnekleme düzeni ve görev paylaşımı kullanıcı ayrıntıları verdikçe netleştirilecek. Bu aşamada bu konularda varsayım yapılmayacak.

### B. Referans ölçüm grubu
- Ayrı ESP: `ESP32-WR1-PZEM` — PZEM Modbus ölçümü ve referans akım/PF verisi.

### C. Yük kontrolü ve tetikleme grubu
- Ayrı ESP: `ESP32-C3-SSR` — iki kanallı SSR modülünün kontrolü; zaman dalgası/ortak tetikleme sonraki aşamada ele alınacak.
- **55 saniye açık / 5 saniye kapalı** döngü önceki taslakta yer almıştı; SSR testi sırasında kullanıcıyla doğrulanmadan uygulanmış kabul edilmeyecek.

PZEM ve SSR işlevleri ayrı ESP'lerde tutulur. SSR'nin kesin modeli, GPIO/polarite, yük sınırları ve zamanlama davranışı henüz doğrulanmadı.

## 2. Alt görevler ve kurulum aşamaları

### Alt Görev 1 — ESP'leri Home Assistant'a tanıtma

#### ESP32D1 — cihaz bilgileri (2026-10-15)

| Alan | Ekranda görülen değer |
|---|---|
| Cihaz adı | `ESP32D1` |
| Yapılandırma dosyası | `esp32d1.yaml` |
| Durum | `Device Online` |
| Hostname | `esp32d1.local` |
| IP adresi | `192.168.0.13` |
| MAC adresi | `70:4B:CA:48:0B:9C` |
| Platform | `esp32` |
| Build Size | `171.4 MB` (arayüzde gösterildiği şekliyle; doğrulanmadı) |
| API şifrelemesi | `Not encrypted` |

**Depo kontrolü:** ESP32D1 için temel ESPHome yapılandırması `GOREVLER/HDF1/HDF1-GRV-001/KOD/ESP32D1.yaml` konumunda mevcut. Önceki deneylere ait ayrı YAML dosyaları ve loglar da HDF1 görevlerinde bulunuyor. Bunlar farklı deney yapılandırmalarıdır; bu kayıt, hangisinin şu anda cihaza yüklü olduğunu kanıtlamaz.

- [x] ESP32D1 Home Assistant/ESPHome arayüzünde çevrimiçi görünüyor.
- [x] ESP32D2 Home Assistant/ESPHome arayüzünde çevrimiçi; cihaz bilgileri Alt Görev 2 altında kaydedildi.
- [x] ESP32E1 Home Assistant/ESPHome arayüzünde çevrimiçi görünüyor; cihaz bilgileri Alt Görev 3 altında kaydedildi.
- [x] ESP32-WR1-PZEM Home Assistant/ESPHome arayüzünde çevrimiçi görünüyor; cihaz bilgileri Alt Görev 4 altında kaydedildi.
- [x] ESP32-C3-SSR Home Assistant/ESPHome arayüzünde çevrimiçi görünüyor; cihaz bilgileri Alt Görev 5 altında kaydedildi.
- **Sınır:** Bu alt görev yalnızca cihazların sisteme tanıtılmasını kapsar; sensör okuması veya deney kabulü değildir.

### Alt Görev 2 — ESP32D2'yi Home Assistant'a tanıtma

#### ESP32D2 — cihaz bilgileri (2026-10-15)

| Alan | Ekranda görülen değer |
|---|---|
| Cihaz adı | `ESP32D2` |
| Yapılandırma dosyası | `esphome-web-5cf4e4.yaml` |
| Durum | `Device Online` |
| Ek durum | `Modified` |
| Hostname | `esphome-web-5cf4e4.local` |
| IP adresi | `192.168.0.50` |
| MAC adresi | `E0:8C:FE:5C:F4:E4` |
| Platform | `esp32` |
| API şifrelemesi | `Not encrypted` |

**İlk kurulum notu:** ESP32D2 çevrimiçi görünse de `Modified` etiketi var ve yapılandırma dosyası genel `esphome-web` adı taşıyor. Bu nedenle cihazın Home Assistant/ESPHome arayüzünde görünmesi kaydedildi; BERO'ya özel YAML'ın yüklü olduğu veya ölçüm yazılımının çalıştığı sonucuna varılmadı. Önceki paylaşılan logda ESPHome API bağlantısı başarılıydı; bu da yalnızca ağ/API erişimini doğrular. ESP32D2'nin sorunlu olduğuna ilişkin teşhis bu ekranla konulamaz.


### Alt Görev 3 — ESP32E1'i Home Assistant'a tanıtma

#### ESP32E1 — cihaz bilgileri (2026-10-15)

| Alan | Ekranda görülen değer |
|---|---|
| Cihaz adı | `ESP32E1` |
| Yapılandırma dosyası | `esphome-web-9e07c4.yaml` |
| Durum | `Device Online` |
| Hostname | `esphome-web-9e07c4.local` |
| IP adresi | `192.168.0.56` |
| MAC adresi | `68:09:47:9E:07:C4` |
| Platform | `esp32` |
| Build Size | `137.8 MB` (arayüzde gösterildiği şekliyle; doğrulanmadı) |
| API şifrelemesi | `Not encrypted` |

**Sınır:** Bu kayıt yalnızca cihazın çevrimiçi görünmesini belgeler; BERO'ya özel yazılım, ölçüm veya veri doğrulaması anlamına gelmez.

### Alt Görev 4 — ESP32-WR1-PZEM'i Home Assistant'a tanıtma

#### ESP32-WR1-PZEM — cihaz bilgileri (2026-10-15)

| Alan | Ekranda görülen değer |
|---|---|
| Cihaz adı | `ESP32-WR1-PZEM` |
| Yapılandırma dosyası | `esphome-web-2a35cc.yaml` |
| Durum | `Device Online` |
| Hostname | `esphome-web-2a35cc.local` |
| IP adresi | `192.168.0.52` |
| MAC adresi | `20:50:0D:2A:35:CC` |
| Platform | `esp32` |
| Build Size | `137.8 MB` (arayüzde gösterildiği şekliyle; doğrulanmadı) |
| API şifrelemesi | `Not encrypted` |

**Planlanan rol:** PZEM ölçümünü Home Assistant'a aktarmak. Önceki görev taslağında PZEM ile tek kanallı SSR kontrolünün aynı ayrı ESP üzerinde olması düşünülmüştü; kullanıcı görev dağılımını netleştirene kadar SSR ve ortak zaman tetikleyicisinin bu cihaza atanmış olduğu varsayılmayacak.

**Sınır:** Cihazın çevrimiçi görünmesi PZEM bağlantısının, ölçüm değerlerinin veya Home Assistant sensörlerinin çalıştığını kanıtlamaz.


### Alt Görev 5 — ESP32-C3-SSR'yi Home Assistant'a tanıtma

#### ESP32-C3-SSR — cihaz bilgileri (2026-10-15)

| Alan | Ekranda görülen değer |
|---|---|
| Cihaz adı | `ESP32-C3-SSR` |
| Yapılandırma dosyası | `esp32-c3-ssr.yaml` |
| Durum | `Device Online` |
| Hostname | `esp32-c3-ssr.local` |
| IP adresi | `192.168.0.88` |
| MAC adresi | `90:64:9B:E8:6C:04` |
| Platform | `esp32` |
| Build Size | `177.4 MB` (arayüzde gösterildiği şekliyle; doğrulanmış firmware boyutu olarak kabul edilmez) |
| API şifrelemesi | `Not encrypted` |

**Planlanan rol:** SSR röle kontrolü; sonraki aşamada zaman dalgası/ortak tetikleme işlevi değerlendirilmesi.

**Donanım notu:** Kullanıcının paylaştığı fotoğrafta iki kanallı SSR modülü ve `VCC`, `DC-`, `CH1`, `CH2` kontrol işaretleri görülüyor. Modülün tam modeli, giriş polaritesi/aktif seviyesi, ESP GPIO eşlemesi ve yük tarafı değerleri henüz doğrulanmadı.

**Durum sınırı:** ESPHome ekranı yalnızca cihazın çevrimiçi olduğunu doğrular. Bu kayıt SSR'nin açılıp kapandığını, yükü anahtarladığını veya zamanlamanın çalıştığını kanıtlamaz.

- [x] ESP32-C3-SSR cihaz tanıtımı ve ağ bilgileri kaydedildi.
- [ ] Mevcut `esp32-c3-ssr.yaml` incelenecek; cihaz adı değiştirilmeden mevcut GPIO/kod yapısı belirlenecek.
- [ ] SSR kontrol çıkışı, yük tarafı enerjilendirilmeden uygun kontrol koşullarında doğrulanacak.
- [ ] Röle kontrolü doğrulandıktan sonra zaman dalgası/ortak tetikleme ayrı adım olarak ele alınacak.

### Sonraki kurulum adımları

1. Kullanılacak tüm ESP'leri ve ilgili donanımı envantere kaydet.
2. Üç ESP'li akım ölçüm grubunun 1T/2T/4T ve BIAS bağlantılarını kullanıcı tarafından verilecek ayrıntılara göre kur.
3. PZEM referans ölçüm ESP'sini ve SSR kontrol ESP'sini ayrı ayrı doğrula.
4. Besleme, GND/referans, sinyal kabloları, seri bağlantı ve gerekiyorsa izolasyon gereksinimlerini kontrol et.
5. Bağlantı şeması/fotoğrafı ve ilk kontrolleri RAPOR/LOG altında kaydet.
6. Her ESP'yi ayrı ayrı doğrula; bir ESP'nin sonucu diğer ESP'nin doğrulaması sayılmayacak.
7. Kurulum tamamlanınca yazılım derleme ve kontrollü test adımlarını ayrı kabul ölçütleriyle yürüt.

## 3. Güvenli çalışma ve sınırlar

- Bu kayıt bir **donanım kurulum planıdır**; test yapılmış veya kod hazır anlamına gelmez.
- Kullanıcı ayrıntıları gelmeden GPIO, ADC kanalı, örnekleme frekansı, sensör tipi, PZEM modeli veya SSR kontrol devresi belirlenmiş sayılmayacak.
- Şebeke/yük tarafı bağlantıları, SSR'nin yük ve gerilim sınıfı ile uygun izolasyon/koruma doğrulanmadan enerjilendirilmeyecek.
- GRV-Freeze-1 çalışma kısıtı korunacak: önce donanım ve mevcut test hattı; gereksiz yeni kod/mimari tasarımı yok.
- Ham kayıtlar korunacak; eski deneylerin üzerine yazılmayacak.
- Kurulum, derleme, yükleme ve veri testi ayrı aşamalar olarak raporlanacak.

## 4. Kabul ölçütleri

- [ ] ESP32D1, ESP32D2 ve ESP32E1 donanımları tanımlanmış.
- [ ] 1T, 2T, 4T ve BIAS bağlantıları kullanıcı ayrıntılarıyla netleştirilip kaydedilmiş.
- [ ] Ayrı PZEM referans ESP'si ve SSR kontrol ESP'si belgelenmiş; zamanlama döngüsü ayrıca doğrulanmış.
- [ ] Besleme, referans/GND, sinyal bağlantıları ve yük tarafı güvenlik kontrolleri kaydedilmiş.
- [ ] Kurulum fotoğrafı veya eşdeğer bağlantı kaydı eklenmiş.
- [ ] Her ESP için bağımsız doğrulama planı hazırlanmış.
- [ ] Açık kalan noktalar ve sonraki adım raporlanmış.

## 5. Klasörler

- `KOD/` — bu görevin yazılım referansları ve ileride doğrulanmış kodlar
- `RAPOR/` — donanım planı, bağlantı şemaları ve kontrol raporları
- `LOG/` — ham cihaz kayıtları ve gerçek test çıktıları

## 6. Sonraki adım

Kullanıcı 1T/2T/4T, BIAS ve PZEM/SSR donanımının ayrıntılarını verecek. Bu ayrıntılar gelene kadar pin veya devre varsayımı yapılmayacak; görev donanım kurulumuna odaklı kalacak.
