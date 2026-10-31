# BERO — Ölçüm İmkânları Kataloğu

**Amaç:** BERO çalışmaları sırasında fiziksel kontrol gerektiğinde, kullanıcıya hangi ölçü aletini hangi fonksiyonda/kademede kullanacağı, probları veya pensi nereye uygulayacağı ve hangi sonucu beklediğimiz açıkça söylenebilsin.

Bu katalog yalnız cihaz listesi değildir. Her ölçüm talimatı; cihaz + mod/fonksiyon + kademe + ölçüm noktası/bağlantı + beklenen değer/aralık + yorum ölçütü içerir.

## 1. Cihaz ve ölçüm imkânları

### UNI-T UT33D+ — dijital multimetre

| Fonksiyon | Kullanılabilir mod/kademe | BERO'daki olası kontrol | Beklenen sonuç nasıl tanımlanır? |
|---|---|---|---|
| DC gerilim | DC V; 200 mV, 2 V, 20 V, 200 V, 600 V | Bias regülatör çıkışı, bias orta noktası, düşük gerilim beslemeleri | Devre şeması/hedef gerilime göre sayısal değer veya tolerans aralığı |
| AC gerilim | AC V; 200 V, 600 V | Yalnız uygun ve güvenli koşullarda AC gerilim kontrolü | Kaynak gerilimi ve ölçüm noktası belirtilerek |
| DC akım | DC A; 2 mA, 20 mA, 200 mA, 10 A kademeleri | Düşük gerilim devresinin DC akım tüketimi; seri bağlantı gerektirir | Devre beklenen tüketimi biliniyorsa değer/aralık |
| Direnç | Ω kademeleri; 200 Ω'dan 200 MΩ'a | Enerjisiz devrede direnç, direnç ağı ve süreklilik ön kontrolü | Şema/renk kodu/parça toleransından hesaplanan değer |
| Diyot | Diyot test modu | Diyot ve köprü doğrultucu elemanlarının enerjisiz ön kontrolü | İlgili yarı iletkenin beklenen ileri yön düşümü; parça/veri sayfasına göre |
| Süreklilik | Buzzer | Enerjisiz kablo, hat ve bağlantı sürekliliği | İletişim/süreklilik var-yok; buzzer eşik değeri cihaz kılavuzuna bağlı |
| NCV | Temassız gerilim algılama | Yalnız ön tarama | Kesin gerilim yokluğu kanıtı değildir |

**Sınırlar:** UT33D+ AC akım ölçmez. Direnç, diyot ve süreklilik ölçümleri devre enerjisizken ve kondansatörler güvenli biçimde boşaltıldıktan sonra yapılır. Akım ölçümü devreye seri bağlanmayı gerektirir; yanlış soket/mod kullanımı kısa devre ve cihaz hasarı riski taşır. Şebeke tarafında ölçüm talimatı ayrıca güvenlik değerlendirmesi olmadan verilmez.

### UNI-T UT200B+ — pens ampermetre

| Fonksiyon | Kullanılabilir mod/kademe | BERO'daki olası kontrol | Beklenen sonuç nasıl tanımlanır? |
|---|---|---|---|
| AC akım | AC A; kullanıcının belirttiği 3 A kademesi ve cihazın diğer uygun kademeleri | PZEM/SCT akımını bağımsız fiziksel ölçümle karşılaştırma | Aynı yük ve zaman aralığında PZEM/SCT ile karşılaştırılacak A değeri/aralığı |

**Uygulama notu:** Pens yalnız tek bir akım taşıyan iletkeni çevrelemeli; faz ve nötr birlikte pens içine alınmamalıdır. Düşük akım ölçümünde 3 A kademesi, cihazın kılavuzundaki aralık ve doğruluk koşulları kontrol edilerek seçilir. Pensin iletken çevresindeki konumu ve ölçüm kararlılığı not edilir.

**Kayıt sınırı:** 3 A kademesi kullanıcı tarafından bildirildi. Bu katalogda henüz BERO'ya ait UT200B+ ile alınmış sayısal bir ölçüm sonucu yoktur.


### SANEC USB Lojik Analizör — 24 MHz / 8 kanal

**Sınıf:** Bağımsız ölçüm ekipmanı → Dijital sinyal ve haberleşme analizörleri → USB lojik analizör.

**Cihaz kimliği / kanıt sınırı:** Kullanıcının bildirdiği model adı SANEC USB Lojik Analizör, 24 MHz, 8 kanal. Erişilebilen SANEC ürün ilanı 8 kanal ve 24 MHz bilgisini veriyor; SANEC'e ait ayrıntılı üretici veri sayfası veya bu cihazın kart revizyonunu kesinleştiren belge bulunamadı. Aşağıdaki elektriksel giriş eşikleri, aynı sınıftaki SparkFun 24 MHz/8 kanal cihazın üretici dokümanı ve benzer ürün teknik listelerinden alınmış **referans değerleridir**; SANEC cihazına ait doğrulanmış garanti değerleri değildir.

| Özellik | Kayıt | Kanıt / sınır |
|---|---|---|
| Kanal sayısı | 8 dijital giriş | Kullanıcının bildirdiği model tanımı ve SANEC ürün ilanı |
| Azami örnekleme | 24 MHz (24 MS/s olarak listeleniyor) | Ürün ilanı ve benzer model dokümanları; SANEC donanımında bağımsız test yapılmadı |
| Sinyal türü | Dijital lojik 0/1 | Lojik analizörün çalışma türü |
| Tipik protokol çözümleme | UART, I²C, SPI, 1-Wire; CAN desteği yazılım/cihaz uyumuna bağlı | Sigrok/PulseView ve benzer ürün kaynakları; SANEC uyumluluğu henüz test edilmedi |
| PC bağlantısı | USB | Ürün tanımı |
| Yazılım adayı | PulseView / sigrok | Benzer 24 MHz analizörlerin desteklediği açık kaynaklı yazılım; SANEC cihazında henüz doğrulanmadı |
| Lojik seviye / giriş sınırı | Benzer modelde 5,25 V azami giriş; lojik HIGH en az 2,0 V, LOW en çok 0,8 V | SparkFun referans dokümanı; SANEC için kesin sınır kabul edilmez |
| Analog ölçüm | Yapmaz | Analog gerilim dalga şeklini veya akımı ölçen osiloskop/pens yerine geçmez |

**BERO'da kullanım alanları:**
- ESP32-WR1-PZEM ile PZEM arasındaki UART TX/RX trafiğini gözlemek; baud hızı, paket zamanlaması ve veri alışverişini incelemek.
- ESP32-C3 ile DS3231 arasındaki I²C SDA/SCL trafiğini incelemek.
- ESP32-C3 SSR kontrol GPIO'sunun açma/kapama zamanlamasını ve dijital durum geçişlerini gözlemek.
- Gerekirse ESP32 düğümleri arasındaki diğer kablolu dijital sinyalleri eşzamanlı olarak kaydetmek (kanal ve bağlantı uygunluğuna göre).

**Sınırlar ve güvenlik:**
- Bu cihaz analog SCT sinyalinin genliğini, 50 Hz akım dalga şeklini, RMS değerini veya bias voltajını ölçmez. Bu işler için uygun multimetre/osiloskop/akım ölçüm aracı gerekir.
- 24 MHz örnekleme, her türlü 24 MHz dijital sinyali hatasız çözebileceği anlamına gelmez; sinyal frekansı, kenar süreleri, örnekleme ayarı, tampon kapasitesi ve yazılım dekoderi sonucu etkiler.
- Giriş gerilim sınırı SANEC'e ait belgeyle doğrulanana kadar 5 V toleranslı olduğu varsayılmayacak. İlk kullanımda yalnız 3,3 V lojik hatlarda ve düşük gerilimli, ortak referansı bilinen devrelerde kullanılacak.
- GND referansı doğru kurulmalı; USB üzerinden bilgisayara bağlı cihazın toprak bağlantısı ölçülen devreyi bilgisayar toprağına bağlayabilir. Şebeke gerilimi veya izolasyonu belirsiz/floating devrelerde kullanılmaz.
- Girişlere 220–240 V şebeke, PZEM'in şebeke tarafı veya herhangi bir yüksek gerilim hattı kesinlikle bağlanmaz. Lojik analizör galvanik izolasyon veya yüksek gerilim probu değildir.
- SANEC cihazının gerçek giriş eşikleri, pin sıralaması, koruma devresi, kanal tamponu ve yazılım uyumluluğu; kart üzerindeki entegre/PCB revizyonu veya üretici belgesi görülmeden kesinleştirilmiş sayılmaz.

**İlk kullanım kontrolü — henüz yapılmadı:**
1. Cihazın kart fotoğrafı, USB konnektörü ve kanal/GND pin etiketleri kaydedilir.
2. Bilgisayarda PulseView/sigrok cihazı tanıyorsa model/driver bilgisi not edilir; tanınmıyorsa uyumlu sürücü varsayılmaz.
3. İlk bağlantı yalnız ESP32'nin 3,3 V UART veya I²C hattında, GND ortaklığı ve pin eşlemesi doğrulandıktan sonra yapılır.
4. İlk yakalamada örnekleme ayarı, aktif kanal, dekoder ayarları ve gerçek ekran/log çıktısı saklanır.

**Katalog kaydı:** Cihaz envantere ölçüm imkânı olarak eklendi; SANEC'e özgü elektriksel limitler ve BERO üzerinde çalışması henüz doğrulanmadı. Bu kayıt fiziksel test yapıldığı anlamına gelmez.


### MCP3208 — harici 12 bit ADC / analog ölçüm teşhis modülü

**Sınıf:** Bağımsız ölçüm ve teşhis ekipmanı → Harici ADC / analog veri toplama.

**BERO'daki edinim amacı (KULLANICI BİLDİRİMİ):** MCP3208 özellikle SCT ölçüm zincirinde veya ESP32 dahili ADC okumalarında ortaya çıkabilecek sorunları araştırmak, analog sinyali bağımsız bir ADC üzerinden karşılaştırmak ve gerektiğinde alternatif analog veri toplama yolunu sınamak amacıyla edinildi. Bu cihaz şu anda BERO'nun çalışan baseline'ı değildir; envanterde bulunması kullanıldığı veya devreye alındığı anlamına gelmez.

**Üretici teknik özellikleri — Microchip MCP3208:**

| Özellik | Değer | Kaynak |
|---|---|---|
| ADC mimarisi | 12 bit SAR, dahili sample-and-hold | Microchip MCP3204/3208 veri sayfası |
| Kanal | 8 tek uçlu kanal veya 4 pseudo-differential çift | Microchip veri sayfası |
| Haberleşme | SPI; Mode 0,0 ve 1,1 | Microchip veri sayfası |
| Besleme | 2,7–5,5 V | Microchip veri sayfası |
| Azami dönüşüm hızı | VDD=5 V iken 100 ksps; VDD=2,7 V iken 50 ksps | Microchip veri sayfası |
| Analog giriş aralığı | Single-ended kullanımda VSS ile VREF arası | Microchip veri sayfası |
| Referans | Harici VREF girişi | Microchip veri sayfası |
| Doğrusallık | B sürümünde INL ±1 LSB; C sürümünde ±2 LSB; DNL ±1 LSB | Tam parça son eki önemlidir |

Kaynak: [Microchip MCP3204/3208 resmi veri sayfası](https://ww1.microchip.com/downloads/aemDocuments/documents/APID/ProductDocuments/DataSheets/21298e.pdf). Bu değerler entegre içindir; kullanıcının elindeki breakout/modül üzerindeki regülatör, referans kaynağı, filtre ve bağlantı kalitesi ayrıca doğrulanmalıdır.

**BERO'da teşhis amacıyla kullanılabilecek kontroller:**
- Aynı düşük gerilim analog noktasını ESP32 dahili ADC ve MCP3208 ile karşılaştırarak ADC kaynaklı sapma, gürültü veya kararsızlık olup olmadığını araştırmak.
- SCT analog çıkışının bias çevresindeki davranışını, kanal bazında sayısal örnekler alarak incelemek.
- MCP3208 kanalları arasında çapraz etki, kanal değiştirme sonrası yerleşme ve örnekleme kararlılığını araştırmak.
- SPI haberleşme/okuma kodunu ve seçilen örnekleme hızında veri kaybı olup olmadığını test etmek.
- Gerektiğinde MCP3208'i üç SCT sinyali ve bias voltajı için alternatif çok kanallı ADC adayı olarak değerlendirmek; bu kullanım henüz tasarım kararı değildir.

**Önemli yorum sınırları:**
- 12 bit çözünürlük, otomatik olarak 12 bit etkin doğruluk veya ESP32 ADC'den her koşulda daha iyi sonuç anlamına gelmez. Referans gerilimi, analog kaynak empedansı, topraklama, besleme gürültüsü, PCB/modül tasarımı ve SPI zamanlaması sonucu etkiler.
- 100 ksps toplam ADC dönüşüm kapasitesi olarak ele alınmalı; sekiz kanalın her birinde aynı anda 100 ksps garantisi değildir. Kanallar çoklanarak okunur.
- MCP3208'in 100 ksps değeri, BERO'nun şu anki kararlı pencere/etiketleme hedefi için zorunlu gereksinim olarak kabul edilmez.
- MCP3208 analog girişine VREF/VDD sınırlarını aşan veya negatif gerilim uygulanmaz. SCT devresinin bias'lı sinyali, ortak GND ve giriş aralığı ölçülmeden doğrudan bağlanmaz.
- Bu modülün satın alınmış olması, MCP3208'in mevcut ESP32D2 YAML'ına eklendiği veya firmware'de kullanıldığı anlamına gelmez. Firmware/pin planı değişikliği ancak ayrı test ve karar kaydıyla yapılır.

**İlk teşhis yaklaşımı — henüz uygulanmadı:** Önce tam MCP3208 kartının fotoğrafı ve pin etiketleri, entegre parça son eki, VREF bağlantısı ve kart üzerindeki ek devreler belirlenir. Ardından aynı güvenli düşük gerilim analog nokta iki ADC ile aynı koşulda ölçülür; örnek sayısı, örnekleme hızı, ortalama/medyan, standart sapma ve uç değerler karşılaştırılır. Sonuçlar gerçek logla kaydedilmeden ADC üstünlüğü veya arızası ilan edilmez.

## 2. Ölçüm talimatı standardı

Kullanıcıdan ölçüm istenirken aşağıdaki sırayla açık talimat ver:

1. **Amaç:** Hangi arıza/hipotez/özelliği kontrol ediyoruz?
2. **Cihaz:** Tam model.
3. **Mod ve kademe:** Örn. UT33D+ → direnç (Ω) → uygun kademe.
4. **Bağlantı:** Probların iki ucu veya pensin çevreleyeceği tek iletken. Gerekirse enerjisiz bırakma koşulu.
5. **Beklenen:** Sayısal hedef, tolerans aralığı veya yalnız karşılaştırma beklentisi. Değer bilinmiyorsa uydurma; önce şema, parça kodu veya üretici belgesinden çıkar.
6. **Kullanıcıdan istenecek çıktı:** Ekran değeri, birim, seçili kademe ve ölçüm koşulu.
7. **Yorum:** Sonucun hangi aralıkta normal, şüpheli veya geçersiz sayılacağı; eşik kaynağı.

### Örnek talimat biçimi — henüz yapılmış test değildir

> **Kontrol:** Bias trafosu regülatör çıkışını doğrula.  
> **Cihaz/mod:** UT33D+ — DC V — 20 V kademesi.  
> **Bağlantı:** Siyah prob devre GND, kırmızı prob L78L33 çıkışı. Yalnız düşük gerilim DC tarafında ölç.  
> **Beklenti:** Kullanıcının daha önce bildirdiği ölçüm 3,31 V DC. Bu önceki gözlemi tekrar kontrol edeceğiz; kabul toleransı devre gereksinimi ve regülatör toleransı doğrulanmadan belirlenmiş sayılmaz.  
> **Bildir:** Ekran değeri, kademe ve ölçüm anındaki yük durumu.

> **Kontrol:** Bilinen direnç değerini doğrula.  
> **Cihaz/mod:** UT33D+ — Ω — ölçülen nominal değere uygun kademe.  
> **Bağlantı:** Devre enerjisiz; mümkünse direncin en az bir bacağı devreden ayrılmış; problar direncin iki ucunda.  
> **Beklenti:** Nominal direnç ve parça toleransından hesaplanır. Örneğin 10 kΩ ±%5 parça için 9,5–10,5 kΩ aralığı; bu yalnız örnek tolerans hesabıdır, BERO'da teyit edilmiş bir parça değeri değildir.

> **Kontrol:** Yük akımını bağımsız gözle.  
> **Cihaz/mod:** UT200B+ — AC A — uygun aralık; kullanıcı tarafından belirtilen 3 A kademesi düşük akım koşulunda değerlendirilebilir.  
> **Bağlantı:** Pens yalnız faz gibi tek akım taşıyan iletkeni çevreler.  
> **Beklenti:** Test yükü ve eşzamanlı PZEM ölçümü bilindikten sonra belirlenir; örnek bir yükün akımı varsayılarak ölçüm sonucu uydurulmaz.

## 3. Sonuç kaydı şablonu

Her gerçek ölçümden sonra şu alanları doldur:

- Tarih/saat ve saat dilimi:
- Kontrol edilen modül/devre:
- Kontrol amacı:
- Ölçü aleti/model:
- Fonksiyon/mod ve kademe:
- Ölçüm noktası veya pens konumu:
- Devre/yük koşulu:
- Beklenen değer ve dayanağı:
- Gerçek okuma ve birim:
- Tekrar sayısı/kararlılık:
- Sonuç: UYGUN / ŞÜPHELİ / UYGUN DEĞİL / SONUÇSUZ
- Kanıt sınıfı: ÖLÇÜLDÜ / ÜRETİCİ BELGESİ / HESAP / HİPOTEZ / KULLANICI BİLDİRİMİ
- Log/fotoğraf referansı ve yorum:

## 4. Katalog kapsamı ve güncelleme

Yeni ölçü aleti kullanıcı tarafından bildirildiğinde önce model ve fonksiyonları doğrulanır, sonra bu kataloğa eklenir. Yeni ölçüm imkânı ortaya çıktığında ilgili mod/kademe, güvenli bağlantı biçimi ve beklenen değer belirleme yöntemi eklenir.

**Önemli:** Katalogdaki örnek talimatlar geçmişte yapılmış testleri göstermez. Beklenen değer, gerçek devre ve ölçüm koşulu bilinmeden kesinleştirilmez. Ölçüm cihazı kapasitesi ile BERO'da fiilen ölçülmüş sonuç ayrı tutulur.
