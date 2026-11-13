# E19 — Sonuç defteri

## Durum

**AÇIK — Aşama 1 loglandı; Aşama 2 (100 W ortak alan/katsayı) PLANLANDI.**

İlk donanım gözlemleri 2026-11-13 tarihli kayıt altında eklendi. Önceki sipariş bilgisi tarihsel nottur.

## Deney öncesi kayıt

- Sipariş: 1 adet ADS1115 kartı (kullanıcı bildirimi).
- Hedef kullanım: BERO'da düşük akım, özellikle 0,5 A altı için alternatif ölçüm yolu araştırması.
- Mevcut mimari korunacak: SCT-013 + bias + ESP32 ADC.
- Alternatif: SCT-013 30A/1V + ADS1115.
- Referans: PZEM-004T V3.0.
- Bias'sız bağlantı: araştırılacak; henüz doğrulanmadı.
- Kart fotoğrafı, pin/komponent incelemesi, kod, derleme ve ölçüm logu henüz yok.

## Ölçüm kayıtları

Henüz ölçüm yapılmadı. Her deney oturumu için tarih/saat, gerçek bağlantı, firmware/kod sürümü, ADS1115 gain/data rate, örnek sayısı, pencere süresi, PZEM değeri, ham ADC ve istatistikler eklenecek.

## Sonuç / yorum

Henüz sonuç yok. Sipariş verilmesi veya deney planının hazırlanması, donanımın çalıştığı ya da bias'sız ölçümün mümkün olduğu anlamına gelmez.

## 2026-11-09 — Yeni hedef notu: yaklaşık 2 A civarı

Kullanıcı, ADS1115 alternatifi işe yararsa uygun kalibrasyon katsayısıyla yaklaşık 2 A civarında da kullanılabileceğini değerlendirmeyi istedi. Bu hedef E19'a ikincil doğrulama bölgesi olarak eklendi.

Henüz ölçüm veya katsayı yoktur. Kartın giriş aralığı/gain ayarı, SCT çıkış tepe değeri, clipping, kararlılık ve PZEM referansına göre sapma ölçülecek. Düşük akım ve yaklaşık 2 A aralıklarında tek katsayının geçerli olduğu varsayılmayacak.

## 2026-11-09 — Çift yol / aralık seçimi fikri (henüz uygulanmadı)

Kullanıcının mimari tarifi: Aynı ESP üzerinde mevcut ESP32 ADC ölçüm yolu ve I²C ADS1115 ikinci ölçüm yolu birlikte bulunabilir. Yaklaşık 1 A altına inildiğinde kullanılacak ölçüm ADS1115 yolundan, eşik üstünde mevcut dahili ADC yolundan seçilecek. Hedef, iki yolun güçlü olduğu akım bölgelerini birleştirmek.

Bu henüz deney sonucu veya kesin mimari kararı değildir. İlk olarak aynı SCT sinyalinin iki ön uca güvenli biçimde verilip verilemeyeceği incelenecek. Bias/common-mode ve giriş yüklemesi doğrulanmadan paralel bağlantı yapılmayacak. Eşik 1 A başlangıç fikridir; histerezis ve geçiş davranışı ölçümle belirlenecek. Her iki yolun ham kayıtları ayrı tutulacak.

## 2026-11-13 — Aşama 1: ADS1115 ilk donanım okuma gözlemleri

Gerçek log özeti ve sınırları [ilk log kaydında](../../logs/ads1115/2026-11-13-E19-ads1115-first-bringup.md) tutulur.

- I2C taraması ADS1115'i 0x48 adresinde buldu.
- GPIO21 SDA, GPIO22 SCL, 3.3 V besleme, ADDR-GND; SCT uçları A0/A1 olarak bildirildi.
- Yüksüz diferansiyel ölçümde 8–39 µV aralığında değerler görüldü.
- Yaklaşık 60 W yükte PZEM 0.264 A / yaklaşık 60 W gösterirken önceki düşük hızlı ADS logu yaklaşık -12.8 mV ile +13.1 mV arasında değişti. 7 SPS ve yaklaşık 1 s yayın aralığı nedeniyle bu RMS akım/katsayı ölçümü değildir; aliasing olasılığı vardır.
- ESP32D1 logunda ham ct_clamp 0.13757–0.13954 A, K uygulanmış çıktı 3.332–3.380 A ve 6.700–6.920 SPS görüldü. Aynı zamanlı PZEM bu log kesitinde bulunmadığından 3.35 A gerçek akım kabul edilmedi.
- Yeni YAML: [esp32d2-ads1115-ct-clamp.yaml](../../firmware/experiments/esp32d2-ads1115-ct-clamp.yaml). Depoya eklenmesi derlendiği veya 100 W testinin yapıldığı anlamına gelmez.

**Aşama 1 yorumu:** I2C haberleşmesi ve diferansiyel sayısal okuma gözlendi. Yük değişiminde giriş çıktısının değiştiği logla destekleniyor. RMS ölçüm, 860 SPS gerçek örnek akışı, giriş common-mode güvenliği ve kalibrasyon doğrulanmadı.

## 2026-11-13 — Aşama 2: 100 W ortak ölçüm alanı testi açıldı

- **Durum:** PLANLANDI.
- **Hedef:** ADS1115/ct_clamp ölçüm yolunu mevcut ESP32D1 yolu ve PZEM ile ortak ölçüm alanında karşılaştırmak; ADS1115 katsayısını belirlemek.
- **Yük:** 100 W akkor ampul, sürekli açık.
- **Referans:** PZEM-004T V3.0; mutlak ground truth değil, BERO karşılaştırma referansı.
- **Karşılaştırma:** ESP32D1 mevcut SCT/ADC/ct_clamp; ESP32D2 ADS1115/ct_clamp; PZEM akım/gerilim/güç.
- **Sabitler:** İlk testte bağlantı/tur sayısı ve firmware ayarları sabit tutulacak. ESP32D1 K=24.22 değişmez. ADS1115 YAML'daki 30A/1V doğrusu yalnız başlangıç ayarıdır.
- **Toplanacak veri:** Zaman damgalı kararlı değerler, her iki SCT yolunun ham ct_clamp çıktısı, kalibre edilmiş akım, PZEM akımı/gücü/gerilimi, örnek sayısı/SPS, minimum/ortalama/maksimum ve standart sapma.
- **Katsayı:** Birimler ve dönüşüm doğrulandıktan sonra ADS1115 ham ct_clamp kararlı ortalaması PZEM kararlı ortalamasıyla karşılaştırılarak hesaplanacak.
- **Kabul:** Tekrarlı ölçümlerde kararlılık, girişte clipping olmaması ve PZEM'e göre sapmanın raporlanması. ±%4 hedefi henüz sonuç değildir.
- **Sonuç:** Ölçüm ve katsayı henüz yok.


## 2026-11-13 — Üç modül ortak yük logu ve ilk karşılaştırma

- **Ortak pencere:** 17:48:27–17:51:13 (+03:00).
- **ESP32D2 / ADS1115:** n=84, ortalama 0.469881 A, SD=0.001091 A, min–maks 0.46–0.47 A.
- **Modül 3 / PZEM:** n=34, ortalama 0.469882 A, SD=0.000537 A, min–maks 0.469–0.471 A.
- **Modül 2 / CH1-1T:** n=167, ortalama 0.434240 A, SD=0.013698 A, min–maks 0.410–0.498 A.
- ADS1115 sensör accuracy_decimals: 2 olduğundan yayın çözünürlüğü küçük sapma hesabını sınırlar. PZEM'e yakın ortalama, 860 SPS yapılandırmasının veya RMS doğruluğunun kanıtı değildir.
- ESP32D2 açılış logunda ADS1115 Gain 2 / Sample rate 7 görülür; depodaki E19 YAML Gain 2.048 / 860 bekler. Çalışan YAML/binary kaynağı doğrulanmadı.
- Modül 3 OFF readback mismatch uyarıları verdi; OFF sonrasında PZEM akımı yaklaşık 0.470 A sürdü. Fiziksel OFF doğrulanmadı; olay etiketi eğitimde yükün fiziksel durumu sayılmayacak.
- **Sonuç:** Üç cihaz ortak oturumda veri üretti. Bu kesitte ADS1115 ve PZEM ortalamaları örtüşüyor; ESP32D1 CH1-1T ortalaması PZEM'den yaklaşık %7.59 düşük. Katsayı değişikliği yapılmadı; ADS1115 katsayısı ve ±%4 kabul kararı beklemede.
- Ayrıntı: [üç modül karşılaştırma raporu](../../logs/ads1115/2026-11-13-E19-three-module-100w-comparison.md).


## 2026-11-13 — 100 W ortak test: ek yorum ve düzeltmeler

[Üç modül karşılaştırma raporunun 8. bölümü](../../logs/ads1115/2026-11-13-E19-three-module-100w-comparison.md) önceki teknik yorumları düzeltir.

- 200 ms'de 174–177 farklı örnek yaklaşık 870–885 SPS'tir ve ADS1115'in 860 SPS ayarıyla uyumludur. Açılış logundaki `Sample rate: 7`, enum/register kodudur; 7 SPS olarak okunması yanlıştır.
- ADS1115 ortalaması 0.469881 A (n=84), PZEM ortalaması 0.469882 A (n=34). Yakınlık bu oturuma ait gözlemdir; katsayı aynı çalışma noktasından türetildiyse bağımsız kalibrasyon kanıtı değildir.
- Depodaki E19 YAML'da katsayı doğrusu halen 1.0 -> 30.0 olarak kayıtlıdır. Log yorumunda geçen 27.60 ile çalışan binary eşleştirmesi açık kalır; firmware kaynağı doğrulanmadan hangi katsayının kullanıldığı kesinleştirilmez.
- `accuracy_decimals: 2` yayın çözünürlüğünü sınırlar. 3 basamaklı yayın daha fazla gösterim ayrıntısı verir, ölçüm doğruluğunu kendiliğinden artırmaz.
- Gain 0.512 daha dar tam ölçek aralığı sağlar; fiziksel sinyali yükseltmez ve clipping payını azaltır. Giriş tepe değeri ve common-mode doğrulanmadan uygulanmayacaktır.
- 0.05 A filtresi değiştirilmez; önce yüksüz taban kaydı gerekir.
- SSR OFF sonrası akım sürmesi fiziksel anahtarlamanın doğrulanmadığını gösterir. UDP olay akışı çalışmış olsa da olaylar fiziksel yük etiketi değildir.

## 2026-11-13 — Aşama 3: 150 W sabit yük testi

- **Durum:** PLANLANDI; ölçüm/log bekleniyor.
- **Yük:** 150 W akkor lamba, sürekli bağlı.
- **Amaç:** 100 W karşılaştırmasının devamı olarak ADS1115 ve PZEM'in 150 W kararlı yükteki davranışını gözlemek.
- **Sabitler:** Gain 2.048, sample_rate 860, continuous_mode true, A0_A1, 200 ms pencere, 2 s update, accuracy_decimals 2, mevcut filtre ve YAML'da kayıtlı katsayı. Firmware/binary kaynağı ve uygulanan K test loguyla eşleştirilecek.
- **Kayıt:** ADS1115, PZEM ve mevcutsa Modül 2 logları; ortak zaman aralığı, ortalama/SD/min-maks, örnek sayısı/SPS, gerilim/akım/güç, I2C uyarıları ve UDP olayları.
- **Kabul sınırı:** Bu tek nokta çok noktalı kalibrasyon veya ±%4 başarısı değildir. 100 W ile birlikte iki gözlem noktası sağlar.
- **Güvenlik:** A0/A1 giriş common-mode/bias ve gerilim sınırları doğrulanmadan enerjili ölçüme geçilmez; şebeke bağlantısı uygun koruma/muhafaza altında yapılır.



## 2026-11-13 — Aşama 4: 150 W sabit yük karşılaştırması (CSV sonucu)

Ayrıntılı rapor: [E19 150 W karşılaştırma raporu](../../logs/ads1115/2026-11-13-E19-150w-comparison.md).

- **Durum:** LOG İLE DESTEKLENDİ — sabit yük karşılaştırması yapıldı.
- Kaynak: `history (56).csv`; ortak kararlı pencere 18:16:30–18:24:30 (+03:00).
- PZEM: n=39, ortalama 0.65472 A, SD=0.00092 A; güç ortalaması 149.69 W, SD=0.45 W.
- ADS1115: n=241, ortalama 0.66279 A, SD=0.00172 A; PZEM'e göre +%1.23.
- Modül 2 CH1-1T: n=480, ortalama 0.60402 A, SD=0.01357 A; PZEM'e göre -%7.74.
- İlk yaklaşık iki dakikadaki PZEM akım/güç yükselişi lamba oturma bölümü olarak ayrıldı; kararlı karşılaştırma bu bölümden sonra yapıldı.
- K=27.60'ın çalışan firmware'de uygulandığı henüz depo YAML/binary eşleştirmesiyle doğrulanmadı. Bu K varsayımıyla 150 W noktasından hesaplanan düzeltme K≈27.26'dır; **uygulanmadı ve kabul edilmiş katsayı değildir**.
- Gain 2.048, 860 SPS, 200 ms, 2 s, accuracy_decimals 2 ve 0.05 A filtresi değişmedi. 0.512 gain ve 3 basamak yayın uygulanmadı.
- **Sonuç sınırı:** 100 W ve 150 W iki gözlemsel nokta sağlar; bağımsız doğrulama, tüm aralık doğrusallığı veya ±%4 genel kabulü değildir.
- Sonraki deney: 58 W sürekli sabit yük. Ayrıntı: [58 W test planı](../../logs/ads1115/2026-11-13-E19-58w-test-plan.md).


## 2026-11-13 — Aşama 5: 57 W sabit yük testi açıldı

- **Durum:** AÇILDI; başlangıç kullanıcı bildirimi, log/analiz bekleniyor.
- Önceki 58 W planı kullanıcı düzeltmesiyle 57 W olarak değiştirildi; 58 W planı tarihçe olarak korunur, uygulanmadı.
- Başlangıç saati: 18:32 (+03:00), kullanıcı bildirimi.
- Yük sürekli bağlı sabit 57 W nominal akkor ampul; aç/kapa geçiş deneyi değil.
- İlk 3 dakika geçici/ısınma bölgesi olarak ayrılacak; 18:35 otomatik kararlı başlangıç sayılmayacak. PZEM ve ADS/SCT eğrileri oturduktan sonra en az 5 dakikalık ortak kararlı pencere seçilecek.
- Gain 2.048, 860 SPS, continuous_mode, 200 ms, 2 s, accuracy_decimals 2, 0.05 A filtre ve çalışan katsayı korunacak. Gain 0.512 ve 3 basamak yayın uygulanmayacak.
- PZEM aynı kararlı pencerenin referansıdır; nominal 57 W'tan hesaplanan akım kalibrasyon girdisi değildir.
- A0/A1 bias/common-mode ve giriş gerilimi güvenliği doğrulanmadan enerjili teste devam edilmemeli.
- Ayrıntı: [57 W test kaydı](../../logs/ads1115/2026-11-13-E19-57w-test.md).

## 2026-11-13 — 57 W düşük akım ön gözlemi ve deney amacı düzeltmesi

**Deney amacı:** Bu aşamada katsayı belirlenmiyor. Mevcut ADS1115 + SCT ölçüm zincirinin ayar/katsayı değiştirilmeden düşük akımdaki kararlılığı ve alt çalışma sınırı araştırılıyor. Katsayı belirleme daha sonraki ayrı aşamadır.

### 57 W kullanıcı bildirimi
- Yük: 57 W nominal sabit akkor yük; sürekli bağlı, ON/OFF deneyi değil.
- PZEM akımı: **0,265 A**.
- ADS1115 + SCT akımı: **0,270 A**.
- Katsayı durumu: kaba/başlangıç katsayısı; henüz kalibrasyon yapılmadı.
- Fark: +0,005 A; PZEM'e göre yaklaşık +%1,89 (**HESAP**).
- Kullanıcı gözlemi: ADS1115 değeri kararlı görünüyor (**KULLANICI BİLDİRİMİ**).

### Yorum ve sınırlar
Bu, eski SCT + ESP32 dahili ADC yolunun düşük akım bölgesinde sorun yaşadığı aralıkta yeni yol için olumlu bir ilk gözlemdir. Eski sistemin 100 W noktasında kısa kalibre edilmiş olmasına rağmen düşük akımda kararlı/hassas sonuç vermediği bilgisi karşılaştırma bağlamı olarak korunur. İki ölçüm yolu farklı mimarilerdir.

Tek bir 57 W bildirimi, ortak zaman penceresi CSV analizi ve tekrar olmadan doğrulanmış kararlı alan değildir. +%1,89 fark kalibrasyon başarısı veya ±%4 genel doğrulaması olarak yorumlanamaz. Katsayıya dokunulmayacak; yük kademeli azaltılarak çalışma davranışı gözlenecek.

### Sonraki adım
Mevcut ayarları ve katsayıyı değiştirmeden bir alt yük basamağına geç; PZEM ve ADS/SCT ortak zaman kaydını al. Güvenlik ön koşulu olan ADS1115 A0/A1 giriş ortak-mod/bias ve ray sınırlarının fiziksel doğrulaması ayrıca açık kalır.

## 2026-11-13 — 57 W oturumu kapandı (18:40) ve CSV ön analizi

- Kullanıcı bildirimi: 57 W nominal akkor yük oturumu **18:40 (+03:00)** itibarıyla kapatıldı.
- Kaynak CSV: `history (57).csv`; SHA-256: `5945b3731a86408db84426f140c6b71869dd5e43b885514aa060e8d9a892a78b`; 5.441 satır, 3 sütun. CSV zamanları UTC'den Europe/Istanbul'a çevrilerek incelendi.
- İncelenen oturum aralığı: 18:32:00–18:40:00 (+03:00). Kullanıcı yükü 57 W nominal olarak tanımladı; CSV'deki PZEM aktif güç bu aralıkta yaklaşık 60,1–61,0 W (18:32–18:40 ortalama 60,58 W) gösteriyor. Nominal lamba etiketi ile PZEM'in ölçtüğü aktif güç birbirinden ayrıdır.
- 18:35:00–18:40:00 ortak gözlem kesiti: ADS1115 + SCT n=150, ortalama 0,266212 A, örnek SD=0,000985 A, min–maks 0,263838–0,269036 A. PZEM akım n=18, ortalama 0,264500 A, örnek SD=0,000514 A, min–maks 0,264–0,265 A. Ortalama fark +0,001712 A; PZEM'e göre yaklaşık +%0,647 (**HESAP**).
- 18:32:00–18:40:00 tam kesitinde ADS1115 n=239, ortalama 0,266547 A, SD=0,001108 A; PZEM n=23, ortalama 0,264783 A, SD=0,000795 A. Ortalama fark +0,001764 A; yaklaşık +%0,666 (**HESAP**).
- Aynı 18:35–18:40 aralığında eski ESP32D1 dahili ADC CH1-1T serisi n=300, ortalama 0,305881 A, SD=0,021954 A, min–maks 0,277557–0,439324 A. Bu seri ADS1115'ten belirgin biçimde daha geniş dağılım gösteriyor; farklı ölçüm mimarileri ayrı tutulur.
- CSV'nin son ADS1115 örneği 18:39:59.927, son PZEM akım örneği 18:39:57.857; kullanıcının 18:40'ta kapatma bildirimiyle uyumlu kayıt sonu.
- **Yorum sınırı:** 18:35–18:40 ADS1115 serisi bu oturumda dar dağılımlı/kararlı gözüküyor ve PZEM ortalamasına yakın. Bu, 100 W'ta yapılan kaba referans ayarından sonra düşük akımda çalışma davranışına ilişkin gözlemdir; bağımsız kalibrasyon, ±%4 genel doğrulaması veya alt çalışma sınırının kesin belirlenmesi değildir. Daha düşük basamaklar ve tekrarlar gerekir.
- Bu aşamanın yöntemi: her ölçüm yapısı PZEM'e karşı yaklaşık 100 W noktasında kaba kalibre edilir; ardından katsayı değiştirilmeden daha düşük akım basamaklarında davranışı tanınır. Düşük akım aşamasında amaç yeniden kalibrasyon değil, kararlılık ve kullanılabilir alt sınırı bulmaktır. Kullanıcı bu yöntemi her ölçüm yapısı için geçerli olarak netleştirdi.
- Güvenlik ön koşulu (ADS1115 A0/A1 ortak-mod/bias ve giriş ray sınırlarının fiziksel doğrulaması) ayrıca açık kalır.

## 2026-11-13 — 42 W sabit yük basamağı açıldı
- Kullanıcı bildirimi: 42 W nominal yük, başlangıç 18:44 (+03:00).
- 57 W basamağı 18:40'ta kapatıldı; 42 W bir sonraki düşük yük basamağıdır.
- Bu aşama çalışma sınırı karakterizasyonudur; katsayı/ayar değiştirilmez ve kalibrasyon yapılmaz.
- Kapanış, PZEM/ADS ortak CSV ve kararlı pencere analizi bekleniyor.
- Ayrıntı: [42 W test kaydı](../../logs/ads1115/2026-11-13-E19-42w-test.md).


## 2026-11-13 — Aşama 6: 42 W sabit yük testi kapandı ve CSV analizi

Ayrıntılı oturum kaydı: [E19 42 W test raporu](../../logs/ads1115/2026-11-13-E19-42w-test.md).

- **Durum:** LOG İLE DESTEKLENDİ — 42 W nominal basamak oturumu 18:44–18:50 (+03:00) arasında yürütüldü ve kullanıcı tarafından kapatıldı.
- Kaynak CSV: `history (58).csv`; 19.183 satır, SHA-256 `df278701f3dc4a317dd70716f0e192436c82cb334d6c1a6919f4a9e4af8811be`.
- Ortak analiz penceresi: 18:44:07–18:49:59 (+03:00).
- ADS1115 + SCT: n=176, ortalama 0.189236 A, örnek SD=0.001014 A, min–maks 0.186221–0.192013 A, CV=%0.536.
- PZEM: n=9, ortalama 0.189000 A, örnek SD=0.001000 A, min–maks 0.188–0.191 A, CV=%0.529.
- ADS1115 ortalaması PZEM ortalamasından +0.000236 A / yaklaşık +%0.125 yüksek (HESAP). Örnek sayıları belirgin biçimde farklıdır; bu fark doğruluk iddiası değildir.
- PZEM aktif güç: n=31, ortalama 43.452 W, SD=0.115 W, min–maks 43.3–43.8 W. 42 W nominal yük tanımı ile PZEM'in ölçtüğü aktif güç ayrı tutulur.
- Eski Modül 2 CH1-1T: n=352, ortalama 0.257694 A, SD=0.030760 A, min–maks 0.200736–0.418209 A, CV=%11.937. Bu yalnız aynı oturumdaki farklı ölçüm mimarisi karşılaştırmasıdır.
- Fiziksel düzen kullanıcı bildirimi: aynı SCT; ADS1115 ölçüm yolunda bias devresi yok ve harici transformatör yok.
- **Yorum:** ADS1115 + SCT yolu bu 42 W oturumunda dar dağılım ve PZEM'e yakın ortalama verdi. 57 W ile birlikte düşük akım davranışı açısından olumlu gözlemdir; kalibrasyon, bağımsız doğruluk, ±%4 genel kabulü veya alt sınır kanıtı değildir.
- Katsayı/ayar değiştirilmedi. ADS1115 A0/A1 ortak-mod ve giriş ray güvenliği doğrulanmış sayılmaz; güvenlik ön koşulu açık kalır.
- CSV yeniden sayımında ADS örnek sayısı 176'dır; önceki sohbet ön özetindeki 177 sayısı düzeltilmiştir.
