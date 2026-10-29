# Fiziksel donanım envanteri

**Durum: KISMEN HAZIR.** Kullanıcı tarafından bildirilen fiziksel stok, ESP32 kart/modül çeşitleri, güç kaynağı, test yükü ve breadboard bias alt devresi kaydedildi. T001 kart dağılımında kullanıcı beyanı esas alınır. Kullanıcının sağladığı fotoğraflarda ESP32-WROOM-32D metal kalkanlı geliştirme kartı ve ESP32-C3 Super Mini kartının arka yüzü görsel olarak tanımlandı. Fotoğraflar bu kayda işlendi; tekrar istenmeyecek.

## Stok ve seçimler

| Kalem | Kaydedilen bilgi | Kaynak / durum |
|---|---|---|
| SCT013-030 stok | 7 adet, 30 A / 1 V, jack çıkışlı | Kullanıcı bildirimi |
| SCT013-100A-1V stok | 10 adet, 100 A / 1 V, jack çıkışlı | Kullanıcı bildirimi |
| Jack yuvaları | Mevcut | Kullanıcı bildirimi |
| ESP32-C3 SuperMini | 1 adet | Kullanıcının bu turda paylaştığı fotoğraf kartı ESP32-C3 SuperMini olarak tanımlıyor; kullanıcı SSR kontrolü ve zamanlama kodunun bu karta ait olduğunu belirtti |
| ESP32-WROOM-32D tabanlı kart/modül | 2 adet | Kullanıcı fotoğrafında ESP32-WROOM-32D metal kalkanlı kart görsel olarak eşleştirildi; kullanıcı bu iki kartı SCT013 ölçümünde kullanacağını belirtti |
| ESP32-WROOM-32E tabanlı kart/modül | 1 adet | Kullanıcı bu kartı da SCT013 ölçümünde kullanacağını belirtti |
| Genel ESP-WROOM-32 tabanlı NodeMCU ESP32 kartı | 1 adet | BERO envanter kaydı; kart üreticisi/revizyonu ve fotoğrafla eşleşmesi proje kaydında net değil |
| ESP32 ölçüm düğümü | 1 adet | Önceki PZEM ölçüm düğümünde kullanıldı; fiziksel kart modeli yukarıdaki stoktan kesin eşleştirilmedi |
| PZEM-004T | V3.0 | Kullanıcı bildirimi; ayrıntı için [mevcut BERO kaydı](../../../DONANIM/PZEM-004T/README.md) |
| SSR kartı | SAMM Market 5 V, 2 kanal | Tedarikçi kodu İzmo9659, SKU MP02637; kart üzerindeki SSR'nin tam kodu ayrıca doğrulanmalı |
| RTC | 2 × DS3231 modülü; her birinde 2032 tipi pil | Kullanıcı beyanı: kod çalıştı; güç kesilip yeniden verildikten sonra saat korundu |
| Güç kaynağı | Masaüstü 5 V / 1,8 A | Kullanıcı bildirimi |
| Test yükleri | 100 W ve 150 W ampuller (ana deney yükleri); 5 W LED ampul (farklı PF karakteristiğini sınamak için) | Kullanıcı bildirimi; etiket gücü kaydedildi, gerçek güç/akım/PF ölçümle doğrulanacak |
| Bağlantı ve ölçüm parçaları | Tam takım mevcut | Kullanıcı bildirimi |

**Toplam SCT013: 17 adet.** Bu adetler kullanıcı bildirimi olup bağımsız fiziksel sayım değildir.

## Hazır analog arayüz kartı

Breadboard bias alt devresi kullanıcı beyanına göre 2 × 10 kΩ dirençle orta nokta oluşturur ve orta noktadan GND'ye 104 (100 nF) kondansatör bağlanmıştır.

**Bağlantı tarifi (kullanıcı bildirimi):** SCT013 jack üzerinden breadboard bias devresine bağlanır; okuma ESP32'nin dahili ADC'siyle yapılır. 8 kanallı analog arayüz kartı mevcut değildir. Harici ADC kullanılmayacak; MCP3208 sonraki aşamaya ayrılmıştır.
## SCT ölçüm kartı ve test düzeni

Kullanıcı kararı ve hedef mimari:

- **Zamanlayıcı/olay üreticisi:** ESP32-C3 SuperMini, SSR yükünü açıp kapatır ve her geçiş için olay/paket bilgisi üretir. Mevcut ADR-006 tasarım kaydında 40 s ON / 20 s OFF, UDP broadcast port 4210 ve `BERO_EVT,BOOT_ID=XXXXXXXX,EVENT_ID=N,STATE=ON|OFF` biçimi tanımlıdır.
- **Üç hızlı örnekleme düğümü:** 2 × ESP32-WROOM-32D + 1 × ESP32-WROOM-32E. Her biri SCT013 sensöründen ham/anlık gerilim örneklerini hızlı biçimde alır; bu aşamada akım veya RMS hesabı yapmaz.
- **Çıktı hedefi:** Her örnekleme düğümü sensör gerilim örneklerini zamanlayıcıdan gelen olay/paket bilgisiyle birlikte yazdırır; böylece örnekler SSR'nin ON/OFF olayına bağlanabilir. Paket alımı/teslimi ve örnekleme zamanlaması testle doğrulanmalıdır.
- **Sarım testleri:** Aynı hatta iletkenin SCT içinden 1, 2 ve 4 sarım geçirilmesi ayrı ayrı denenir.

Bu, hedef mimari ve test planıdır; henüz ölçüm sonucu veya GPIO eşlemesi değildir.

## Önceden hazırlanmış bias üretim alt devresi

**Durum: TAMAMLANDI — kullanıcı onayı.** Mevcut BERO kaydına göre kutu içinde RN130421 6 V AC / 2,0 VA trafo, KBU6M köprü doğrultucu, 2200 µF / 35 V filtre kondansatörü ve L78L33 regülatör; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) kondansatör bulunuyor. Bu, bias üretim alt devresinin hazır olduğu bilgisidir; SCT AC sinyalinin bias noktasına kuplajı ayrıca tanımlanmalıdır. Bağımsız ölçüm raporu bu kayda eklenmemiştir.

## Donanım konfigürasyonu ve açık teknik maddeler

| Öğe | Mevcut durum | Kalan adım |
|---|---|---|
| SCT | 30 A / 1 V öncelikli; 100 A / 1 V alternatif stok | Kullanılacak kanal/sensör eşlemesini belirle |
| MCU | SCT ölçümü için 2 × ESP32-WROOM-32D ve 1 × ESP32-WROOM-32E; SSR kontrolü/zamanlama için ayrı ESP32-C3 SuperMini | ADC destekli GPIO ve pin eşlemesi firmware/pin planlama aşamasında, seçilen fiziksel kart ve teknik belgeyle doğrulanacak; T001’de pin numarası şartı değil |
| ADC | Bu aşamada ayrı/harici ADC kullanılmayacak; sinyal ESP32 kartına gider | MCP3208 mevcut olsa da sonraki aşamaya ayrılmıştır; bu görevde harici ADC modeli/revizyonu veya harici VREF seçimi yapılmayacak |
| Harici ADC | MCP3208 mevcut, ileriki aşamaya ayrıldı | İlk aşamada kullanılmayacak |
| Analog ön uç | Breadboard bias alt devresi; SCT sinyali ESP32 dahili ADC'sine aktarılacak | Sensör dönüşünün jack üzerinden analog karta ve oradan ESP32 kartına gittiği bağlantı yolu kullanıcı tarafından açıklandı; bu aşamada ayrı/harici ADC yok. Elektriksel bias kuplaj topolojisi (hangi hat/noktanın bias orta noktasına bağlandığı), direnç/filtre değerleri ve güvenli ADC aralığı ayrıca devre izi/şema/ölçüm kanıtıyla kaydedilmeli |
| PZEM ve CT | PZEM-004T için [mevcut BERO donanım kaydı](../../../DONANIM/PZEM-004T/README.md) esas alınır; bağlı CT modeli kullanıcı beyanıyla PZCT-02 (0–100 A) | Bu projede yeniden donanım belgesi açma veya CT modelini tekrar sorma; entegrasyon sırasında UART lojik seviyesi ve izolasyon gereksinimlerini kontrol et |
| DS3231 | İki modülde 2032 tipi pil; güç kesintisi sonrası saat koruma testi kullanıcı beyanına göre başarılı | Bu proje aşamasında ek iş yok; proje bağlantısı gerektiğinde pin planı ayrı ele alınır |
| SSR | SAMM Market 5 V, 2 kanal, İzmo9659 / MP02637 | İki AC yük, GPIO eşlemesi, tetik mantığı ve termal sınırlar güvenli biçimde doğrulanmalı |
| Yükler | Kullanıcı testte kullanılacak ampulü/koşulu test kaydında beyan edecek | Önceden yük seviyesi belirleme şartı yok |

## Kayıt kuralları
- Önceki BERO teknik belgelerindeki ürün bilgilerini tekrar yazmak yerine ilgili referansa bağlan.
- Önceki test notları yalnız kendi kayıt kapsamları için kanıttır; yeni deney veya kalibrasyon sonucu gibi sunulmaz.
- Kullanıcı tarafından bildirilen stokları kullanıcı bildirimi olarak etiketle.
- Bu projede ölçülmemiş değerleri ölçülmüş gibi yazma.
- Kullanıcının sağladığı fotoğraflar: ESP32-WROOM-32D metal kalkanlı geliştirme kartı ve ESP32-C3 Super Mini kartının arka yüzü. Görseller metin envanterinde referans olarak kaydedildi; dosyaların kendisi GitHub'a resim dosyası olarak yüklenmedi.


### ESP32 üretici veri sayfaları
- [ESP32-WROOM-32D/32U datasheet — Espressif](https://documentation.espressif.com/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.html)
- [ESP32-WROOM-32E/32UE datasheet — Espressif](https://documentation.espressif.com/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.html)
- [ESP32-WROOM-32 datasheet — Espressif](https://documentation.espressif.com/esp32-wroom-32_datasheet_en.html)
- [ESP32-C3-MINI-1/1U module datasheet — Espressif](https://documentation.espressif.com/esp32-c3-mini-1_mini-1u_datasheet_en.html)

Pin planı notu: Modül datasheet'i, geliştirme kartındaki başlık/pad etiketleriyle aynı şey değildir. Kodlama öncesinde her kartın pinout/şeması ayrı doğrulanacak; yalnızca benzer görünen kartlara bakarak GPIO eşlemesi kopyalanmayacak.

## 2026-10-29 — SCT013-030 kaynak raporundan eklenen notlar

- **Nominal oran:** SCT013-030, 30 A AC RMS girişte yaklaşık 1 V AC RMS çıkış verir; nominal ölçek 30 A/V (33,33 mV/A). **Kaynak etiketi:** teknik rapor/nominal hesap; BERO'da ölçülmüş kalibrasyon değildir.
- **Çıkış tipi:** Gerilim çıkışlı; dahili burden direnci bulunur. Ek burden direnci mevcut tasarımın varsayılan parçası değildir.
- **Satürasyon:** CT satürasyonu genel teknik risk olarak kayda alındı. BERO'da satürasyon ölçülmüş değildir.
- **Belge ayrımı:** ESP32 ADC, RMS, kalibrasyon ve örnek kodları genel kaynak bilgisidir. BERO'nun dahili ADC/T005 planı bu rapordaki kodlarla değiştirilmedi.
- **Kondansatör:** Mevcut fiziksel devre kaydı orta noktadan GND'ye bağlı 104 (100 nF) kondansatördür. E01 öncesi, 10 µF ile değiştirilmesi [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md) kapsamında önerildi; fiziksel değişiklik yapılmış sayılmaz.

## Bias orta noktası — sonraki kurulum notu

Mevcut envanter bildirimi, iki 10 kΩ direnç orta noktasından GND'ye bağlı 104 (100 nF) kondansatör içeriyor. E01 kurulumu öncesi, [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md) uyarınca bunun 10 µF ile değiştirilmesi planlanmıştır. Envanter, değişiklik fiziksel olarak yapılana kadar mevcut parçayı 100 nF olarak tutar. ADC pinine ikinci bir kondansatör eklenmesi şu an kararlaştırılmamıştır.
