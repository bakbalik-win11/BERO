# E24 — Çoklu ADS1115 / bağımsız I²C hatları ve 12 SCT düğüm mimarisi

## DURUM
**PLANLANDI — ilk donanım testi bekleniyor.** Bu belge mimari öneriyi ve test sırasını kaydeder. Üç ADS1115'in tek ESP32 üzerinde üç ayrı SDA/SCL çiftiyle çalıştığı henüz doğrulanmamıştır. Kod, bağlantı şeması, derleme, cihaz testi veya performans sonucu mevcut değildir.

## HEDEF

**Nihai tek düğüm hedefi:** tek ESP32 ile 6 SCT kanalını okumak. Simetrik toplam sistem hedefi iki aynı düğümle 12 SCT kanalına ulaşmaktır.

### Aşamalı doğrulama
1. **İlk aşama:** 1 ESP32 + eldeki 2 ADS1115 + 4 SCT kanalı. İki ADC'nin birlikte çalışması, dört kanalın okuma zamanlaması, gecikme ve hata davranışı doğrulanır.
2. **Nihai tek düğüm:** 1 ESP32 + 3 ADS1115 + 6 SCT kanalı. Üçüncü ADS için bağımsız I²C hattı veya alternatif topoloji ayrıca doğrulanır. Altı kanallı modül şu anda fiziksel olarak kurulmuş değildir.
3. **Sistem genişlemesi:** aynı altı kanallı düğümden ikinci adet kurularak 2 ESP32 + 6 ADS1115 + 12 SCT hedeflenir.

Dört SCT'li ilk aşama nihai mimari değildir; altı SCT'li tek ESP32 düğümüne geçiş öncesi test basamağıdır.

12 SCT girişli simetrik bir sistem için iki aynı ölçüm düğümü tasarımını incelemek:
- Ölçüm düğümü A: 1 ESP32 + 3 ADS1115 + 6 SCT kanalı.
- Ölçüm düğümü B: 1 ESP32 + 3 ADS1115 + 6 SCT kanalı.
- Her ADS1115 için ayrı SDA/SCL çifti kullanılması hedefleniyor.
- Her ölçüm ESP düğümünde bir RS485 dönüştürücü bulunması planlanıyor; iki düğüm ortak RS485 hattıyla merkez veri toplayıcıya bağlanacak.
- Toplam hedef: 2 ESP32 + 6 ADS1115 + 12 SCT kanalı + 2 saha RS485 dönüştürücü. Merkez RS485 arayüzü bu sayıya dahil değildir; merkez donanımına göre ayrıca belirlenecektir.

## MEVCUT DONANIM / KULLANICI BİLDİRİMİ
- Kullanıcının elinde şu anda 2 adet ADS1115 modülü bulunuyor.
- Kullanıcı, altı SCT kanallı tek ESP32 modülünün henüz fiziksel olarak hazır olmadığını belirtti; ilk adım dört kanallı doğrulama testidir.
- Bu iki modülden biri önceki denemede çalışmamış olabilir; kullanıcı ilk testte bu modülü özellikle yeniden kontrol edecek. Arızalı olduğu kesinleşmiş değildir.
- Kullanıcı, ilk yeni modül imalatından önce eldeki iki ADS1115 ile deneme yapılmasını istedi.
- Kullanıcı, ilk test başarılı olursa tedarik güçlüğü ve gümrük gecikmelerine karşı 10 adet ADS1115'i yedek stok olarak sipariş etmeyi planlıyor. Sipariş henüz verilmedi.
- Sensörlerin ilk genişleme hedefindeki envanteri 8 adet SCT 30 A / 1 V ve 2 adet SCT 100 A / 1 V olarak bildirilmiştir. 12 kanallı simetrik tasarım, iki ek kanal için gelecekteki genişleme payı içerir; ek SCT stoğu teyit edilmemiştir.

## ÖNEMLİ DONANIM SINIRI — ESP32 I²C KONTROLCÜLERİ
Espressif ESP32 teknik belgelerine göre klasik ESP32'de iki donanımsal I²C kontrolcüsü bulunur. Bu nedenle tek ESP32 üzerinde üç ayrı donanımsal I²C bus bulunduğu varsayılamaz.

Bu sınır nedeniyle:
- İki ADS1115 ile iki ayrı donanımsal SDA/SCL hattı testi, uygun ESP32 kartında yapılabilir.
- Üç ADS1115'in her birine ayrı SDA/SCL çifti verme hedefi için üçüncü hattın nasıl sağlanacağı çözülmelidir.
- Olası yollar: üçüncü hat için yazılımsal I²C desteğini doğrulamak; I²C çoklayıcı (ör. TCA9548A) kullanmak; veya üç ADS1115'i adresleri farklı olacak şekilde ortak I²C bus üzerinde çalıştırmayı ayrı seçenek olarak değerlendirmek.
- Kullanıcı şimdilik ADS1115'leri ayrı SDA/SCL çiftleriyle bağlama fikrini test etmek istiyor. Bu istek korunur; donanım sınırı test sonucundan önce gizlenmez.
- Kullanılacak ESP32'nin tam modeli ve framework/ESPHome desteği doğrulanmadan üç bağımsız bus uygulanabilir kabul edilmeyecektir.

## İLK TEST — 1 ESP32 ÜZERİNDE 2 ADS1115 İLE 4 SCT KANALI
### Test sırası
1. Eldeki iki ADS1115 modülünü tek tek kontrol et; I²C taraması ve güvenli giriş koşulunda bilinen bir analog seviye ile yanıtlarını doğrula.
2. Daha önce çalışmadığı düşünülen modülü ayrıca test et; sonucu **çalışıyor / yanıt vermiyor / kararsız / test edilemedi** olarak kanıtla.
3. İki ADS1115'i aynı ESP32'ye, iki ayrı donanımsal I²C kontrolcüsü/SDA-SCL çifti üzerinden bağla.
4. Her ADS1115'e ikişer SCT bağlayarak toplam dört SCT kanalını aynı ESP32 ile oku.
5. Dört kanalın okuma çevrimi, kanal başına güncelleme hızı, zaman damgaları, gecikme, timeout/hata ve veri kaybını kaydet.
6. İki ADC dönüşümünü mümkünse yakın/eş zamanlı başlatıp sonuçları sırayla oku; ESP32 ölçüm döngüsünün bloke olup olmadığını incele.
7. Önce ADC girişleri güvenli, bilinen DC test seviyeleriyle denenir. SCT/şebeke ölçümüne geçiş, analog giriş ortak-mod ve mutlak gerilim sınırları ile SCT sekonder bağlantı güvenliği ayrıca doğrulandıktan sonra yapılır.

### İlk testin kabul koşulları
- İki ADS1115 ayrı ayrı kararlı biçimde bulunmalı ve okunmalı.
- Her modülün kimliği/bus eşlemesi karışmamalı.
- Tek ESP32'nin iki bus'ı aynı test oturumunda yönetebilmesi gösterilmeli.
- Ölçüm başlatma/okuma çevrim süreleri ve hata sayıları loglanmalı.
- Daha önce çalışmayan modülün durumu belirsiz bırakılmamalı; kanıtla sınıflandırılmalı.

## İKİNCİ AŞAMA — TEK ESP32 ÜZERİNDE 3 ADS1115 / 6 SCT HEDEFİ
Dört SCT'li ilk test başarılı olduktan sonra tek ESP32'de altı SCT hedefine geçmek için üçüncü ADS bağlantı yöntemi seçilecek:
1. ESP32 üzerinde üçüncü yazılımsal I²C hattı (kullanılan framework ve ESPHome desteği gerçek derleme ile doğrulanmalı).
2. TCA9548A gibi I²C çoklayıcı; kanal başına ayrı SDA/SCL segmenti, ancak ESP tarafında tek ana I²C bus.
3. Üç ADS1115'i tek I²C bus üzerinde farklı ADS1115 adresleriyle kullanmak. ADS1115'in ADDR seçimiyle dört adres olanağı olduğu için bu seçenek teknik olarak değerlendirilebilir; kullanıcı tarafından tercih edilen fiziksel bağımsız hat tasarımıyla aynı şey değildir.
4. Gerekirse ESP32 başına ADS sayısını veya düğüm sayısını değiştirmek.

Bu seçeneklerden biri gerçek donanım ve yazılım testiyle doğrulanmadan tek ESP32 + 3 ADS1115 + 6 SCT düğümü doğrulanmış sayılmayacaktır. Aynı altı kanallı düğümün ikinci kopyası ancak ilk düğüm doğrulandıktan sonra kurulacaktır.

## RS485 / VERİ TOPLAMA
- İlk dört/altı kanal ADC doğrulama testinde RS485 zorunlu değildir; RS485, iki doğrulanmış ölçüm düğümünü merkezde birleştirme aşamasında eklenir.
- İki ölçüm ESP'si aynı RS485 A/B omurgasına bağlanacak şekilde tasarlanır.
- Her ESP'nin sabit düğüm kimliği ve her SCT kanalının sabit kanal kimliği olmalıdır.
- Paketlerde en az düğüm kimliği, kanal kimliği, sıra numarası, ölçüm zamanı, değer ve hata/kalite durumu düşünülmelidir.
- RS485 veri hızı, paket biçimi, sorgulama/çakışma yönetimi ve merkez arayüzü ilk ölçüm testi sonrasında belirlenir.
- RS485'in varlığı tek başına kayıpsız aktarım garantisi değildir; sıra numarası, hata kontrolü, timeout ve gerekiyorsa yeniden isteme/tamponlama davranışı tasarlanıp test edilmelidir.

## TEDARİK PLANI
- İlk önce mevcut iki ADS1115 ile test yapılır.
- Test sonucu uygun bulunursa kullanıcı 10 adet ADS1115'i yedek stok için sipariş etmeyi planlamaktadır.
- Bu 10 adet sipariş henüz verilmiş veya teslim alınmış değildir. Stok kaydı ancak fiziksel teslim ve adet kontrolünden sonra güncellenir.
- Gerekçe: gümrük/tedarik gecikmeleri ve ileride aynı modülü tekrar tekrar değiştirmek zorunda kalmamak.

## AÇIK KONULAR
- ESP32 kartının tam modeli ve kullanılabilir pinleri.
- ESPHome/ESP-IDF/Arduino tarafında üçüncü bağımsız I²C hattının uygulanabilirliği.
- ADS1115 modüllerinin pull-up dirençleri ve toplam bus elektriksel yükü.
- ADC gain, data rate, SCT analog bağlantı/bias, giriş koruması ve RMS örnekleme stratejisi.
- RS485 merkez arayüzü ve protokolü.
- 12 SCT'nin fiziksel yerleşimi ve 100 A / 1 V sensörlerin kanal dağılımı.

## KAYNAKLAR
- Espressif ESP-IDF I²C belgesi: ESP32'de iki I²C kontrolcüsü bulunduğunu belirtir: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/i2c.html
- ESPHome I²C belgesi: birden fazla I²C bus tanımlama ve cihazın birden fazla bus desteklemesi koşulunu açıklar: https://esphome.io/components/i2c/
- Bu E24 kaydı, 2026-11-14 tarihli kullanıcı mimari/test/tedarik kararlarını ve resmi dokümanlardan doğrulanan I²C kontrolcü sınırını bir arada tutar.
