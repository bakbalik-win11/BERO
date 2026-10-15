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

### B. Yük kontrolü ve referans ölçüm grubu
Ayrı bir ESP üzerinde:
- PZEM ölçümü
- Bir kanallı Solid State Relay (SSR) kontrolü
- Yük zamanlaması: **55 saniye açık, 5 saniye kapalı**, tekrarlı döngü

PZEM modeli/bağlantısı, SSR tipi, kontrol pini, yükün elektriksel özellikleri, zamanlama başlangıcı ve ölçüm kayıtlarının nasıl ilişkilendirileceği daha sonra netleştirilecek.

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
- [ ] ESP32D2 ve ESP32E1'in aynı şekilde tanıtılması ve durumlarının kaydedilmesi.
- [ ] PZEM + SSR için kullanılacak ayrı ESP'nin tanıtılması.
- **Sınır:** Bu alt görev yalnızca cihazların sisteme tanıtılmasını kapsar; sensör okuması veya deney kabulü değildir.

### Sonraki kurulum adımları

1. Kullanılacak tüm ESP'leri ve ilgili donanımı envantere kaydet.
2. Üç ESP'li akım ölçüm grubunun 1T/2T/4T ve BIAS bağlantılarını kullanıcı tarafından verilecek ayrıntılara göre kur.
3. PZEM + tek kanallı SSR grubunu ayrı ESP üzerinde kur.
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
- [ ] Ayrı PZEM + SSR ESP'si ve 55 s açık / 5 s kapalı döngüsü belgelenmiş.
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
