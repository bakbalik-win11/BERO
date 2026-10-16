# PROJE BERO — ESP32-WR1-PZEM
## Günlük teknik inceleme raporu — 2026-10-16

### 1. Bu adımın amacı

ESP32-WR1-PZEM, iki veri kaynağını aynı test ortamında bir araya getiren alıcı düğüm olarak hazırlanıyor:

1. PZEM-004T üzerinden elektriksel ölçümler: gerilim, akım, güç, enerji, frekans ve güç faktörü.
2. ESP32-C3-SSR tarafından UDP ile yayımlanan ON/OFF olayları.

Bugünkü çalışma, bu iki yolun birlikte çalışıp çalışmadığını gözlemlemek. Bir sonraki veri işleme aşaması için SSR olayının zamanı/durumu ile PZEM ölçümlerini ilişkilendirebilecek bir temel oluşturmak amaçlanıyor. Bu ilişkilendirme henüz otomatik hesaplanmıyor ve CSV dosyasına yazılmıyor.

### 2. YAML ne yapıyor?

Kaydedilen `esphome-web-2a35cc.yaml` yapılandırması:

- ESPHome cihaz adı: `esphome-web-2a35cc`; görünen ad: `ESP32-WR1-PZEM`.
- ESP32, ESP-IDF çerçevesiyle yapılandırılmış.
- PZEM UART: TX GPIO17, RX GPIO16, 9600 baud, 1 stop bit.
- UART, Modbus bileşenine; Modbus da `pzemac` sensörüne bağlı.
- PZEM altı ölçümü 5 saniyelik aralıkla yayımlıyor.
- UDP alıcısı, 100 ms aralıkla çalışan bir lambda içinde UDP soketi açmayı ve 4210 portuna bağlanmayı deniyor.
- Soket oluşturma/bağlama başarısız olursa hata loglanıyor; soket açılamadıysa yeni deneme en az 5 saniye arayla yapılıyor.
- Soket bağlandıktan sonra bloklamayan moda alınması deneniyor.
- Her döngüde en fazla bir UDP datagramı okunuyor. Alınan içerik `UDP_EVENT_RECEIVED` olarak gönderen IP adresi ve ham mesajla loglanıyor.
- UDP içeriği ayrıştırılıp alanları doğrulanmıyor; olay kimliği/durum bellekte tutulmuyor ve CSV'ye yazılmıyor.

### 3. Logdan doğrudan doğrulananlar

#### Cihaz ve yazılım

- ESPHome log istemcisi `192.168.0.52` adresindeki cihaza bağlanmış.
- Cihaz, ESPHome 2026.9.1 ile derlenmiş bir firmware çalıştırıyor; logda derleme zamanı 2026-10-16 14:56:56 +0300.
- Çip ESP32 revizyon 3.1, iki çekirdek.
- Wi-Fi bağlantısı aktif; IP `192.168.0.52`, sinyal seviyesi yaklaşık -63 dB.
- Güvenli mod kaydı, 18:31:47 civarında açılışın başarılı kabul edildiğini gösteriyor.
- Derleme uyarıları minimum çip revizyonu ve SRAM1'in IRAM olarak kullanılması önerileriyle ilgili. Bu logda bunların çalışma hatasına dönüştüğüne dair kanıt yok.

#### PZEM ölçüm yolu

- UART ayarları logda GPIO17 TX, GPIO16 RX, 9600 baud olarak görünüyor.
- PZEMAC bileşeni ve altı ölçüm sensörü başlatılmış.
- Logda ölçümler tekrar tekrar alınmış; yaklaşık 226,1–226,9 V ve 50,0 Hz görülüyor.
- Akım/güç örnekleri yük durumuna göre değişiyor: örneğin 0,052 A / 7,80 W, 0,029 A / 4,00 W ve 0,000 A / 0,00 W.
- Enerji değeri log aralığında 10637 Wh'den 10638 Wh'ye ilerliyor.
- Bu, PZEM ölçüm değerlerinin cihaza ulaştığını gösterir; ölçüm doğruluğunun bağımsız kalibrasyonla doğrulandığı anlamına gelmez.

#### UDP olay yolu

Logda ESP32-C3-SSR cihazı `192.168.0.111` adresinden üç UDP olayı alındığı açıkça görülüyor:

| Alıcı zamanı | BOOT_ID | EVENT_ID | STATE |
|---|---|---:|---|
| 18:31:52.303 | D1A97EBE | 18 | OFF |
| 18:32:12.291 | D1A97EBE | 19 | ON |
| 18:32:52.188 | D1A97EBE | 20 | OFF |

Bu satırlar UDP datagramlarının ESP32-WR1-PZEM'e ulaşıp loglandığına doğrudan kanıttır. Bu oturumda yalnızca üç olay görünmektedir; olayların uzun süre boyunca kayıpsız alındığı veya kalıcı olarak saklandığı sonucu çıkarılamaz.

### 4. PZEM ile SSR olaylarının birlikte okunması

Log, iki veri yolunun aynı anda çalışabildiğini gösteriyor. Olayların yakınındaki PZEM örnekleri şöyle:

- EVENT_ID 18 / OFF, 18:31:52.303'te alınıyor. Yaklaşık 0,7 saniye sonra PZEM 0,029 A ve 4,00 W; sonraki örnekte 0,000 A ve 0,00 W gösteriyor.
- EVENT_ID 19 / ON, 18:32:12.291'de alınıyor. Yaklaşık 0,7 saniye sonra PZEM hâlâ 0,000 A / 0,00 W; yaklaşık 5,7 saniye sonra 0,052 A / 7,80 W görülüyor.
- EVENT_ID 20 / OFF, 18:32:52.188'de alınıyor. Yaklaşık 0,8 saniye sonraki PZEM örneği 0,052 A / 7,70 W gösteriyor.

Bu yakınlıklar, olay alındığı anda ölçümün aynı duruma geçmiş olmasının garanti olmadığını gösteriyor. PZEM güncellemesi 5 saniyede bir; UDP olayı ise kendi oluştuğu anda geliyor. Ayrıca SSR olayının yayınlanma zamanı, alıcıya ulaşma zamanı ve PZEM örnekleme zamanı farklı olabilir. Dolayısıyla tek bir komşu satıra bakarak SSR'nin fiziksel davranışının hatalı olduğu veya PZEM'in arızalı olduğu söylenemez.

Bir sonraki anlamlı adım, olayları zaman damgasıyla ve PZEM ölçümlerini zaman damgasıyla ayrı ayrı kaydetmek; sonra olaydan önceki/sonraki ölçümleri karşılaştırmaktır. Bu henüz bu YAML'da uygulanmış değildir.

### 5. YAML ile log arasındaki önemli durum farkı

YAML başındaki yorum, kodun henüz derlenip doğrulanmadığını söylüyor. Log ise cihazın 2026-10-16 tarihinde derlenmiş bir firmware çalıştırdığını ve ESPHome log istemcisinin cihaza bağlandığını gösteriyor.

Bununla birlikte log, “validated config cache” kullanıldığını ve doğrulamanın atlandığını belirtiyor. Bu nedenle yalnızca bu loga dayanarak GitHub'daki mevcut YAML dosyasının birebir aynı içerikle derlendiği ve ayrıca temiz bir yapılandırma doğrulamasından geçtiği iddia edilmemelidir. Kaydedilen YAML'ın mevcut yorum durumu daha sonra gerçek derleme/ doğrulama adımıyla güncellenebilir; bu rapor kodu değiştirmez.

### 6. Hedeflenen sistem ve bugünkü ilerleme

**Hedeflenen iş akışı:**

1. ESP32-C3-SSR, durum değişimlerini `BOOT_ID`, artan `EVENT_ID` ve `STATE` içeren UDP mesajlarıyla duyurur.
2. ESP32-WR1-PZEM bu olayları alır.
3. Aynı alıcı PZEM ölçümlerini okumaya devam eder.
4. Sonraki aşamada olaylar ve ölçümler zaman bilgileriyle kalıcı bir CSV kaydına dönüştürülür.
5. Python ile kayıtlar analiz edilerek SSR ON/OFF durumlarıyla akım/güç değişimleri karşılaştırılır.

**Bugün kanıtlanan bölüm:** PZEM ölçüm değerleri okunuyor ve ESP32-C3-SSR'den gönderilen UDP olayları alıcıda görünüyor.

**Henüz yapılmayan bölüm:** UDP mesajlarını alanlarına göre ayrıştırma, olayları ve PZEM değerlerini ortak zaman çizelgesinde CSV'ye yazma, uzun süreli kayıp/tekrar kontrolü ve Python analizi.

### 7. Açık işler / sonraki adım

1. Mevcut kodu değiştirmeden, temiz bir ESPHome yapılandırma doğrulaması/derlemesiyle GitHub'daki YAML ile çalışan firmware arasındaki eşleşmeyi teyit et.
2. Alınan UDP mesajının beklenen `BERO_EVT,BOOT_ID=...,EVENT_ID=...,STATE=ON|OFF` biçimine uyup uymadığını kontrol et; hatalı mesajı ayrı logla.
3. PZEM ölçüm örneklerine zaman bilgisi ekleyecek kayıt düzenini tasarla.
4. UDP olayları ve PZEM ölçümlerini tek CSV'ye veya ilişkilendirilebilir iki CSV'ye kaydetme aşamasını ayrı bir değişiklik olarak planla.
5. CSV oluştuğunda olay öncesi/sonrası akım ve güç değerlerini Python ile incele.
6. Daha uzun bir testte ardışık EVENT_ID'leri, beklenen ON/OFF sırasını ve alım kaybı olup olmadığını kontrol et.

### 8. Kayıt sınırı

Kaydedilmiş log, kullanıcı tarafından gönderildiği haliyle son satırda tek başına `S` karakteriyle bitiyor. Bu rapor, görünür içerik üzerinden hazırlanmıştır; eksik devamı tahmin edilmemiştir.

### Sonuç

16 Ekim 2026 çalışmasının somut sonucu, PZEM okuması ile UDP olay alımının aynı ESP32-WR1-PZEM üzerinde birlikte çalıştığının logla gösterilmesidir. Bu, olay ve ölçüm verilerini bir araya getirme hedefi için önemli bir ara adımdır; ancak henüz CSV tabanlı kayıt, zaman eşleştirme veya analiz tamamlanmış değildir. Kod bu rapor hazırlanırken değiştirilmemiştir.
