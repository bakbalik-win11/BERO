# E19 — ADS1115 ile düşük akım ölçüm alternatifi

- **Durum:** AÇIK — ADS1115 I2C ve diferansiyel okuma ilk logla gözlendi; 100 W ortak alan/katsayı aşaması PLANLANDI. Yeni YAML'ın derleme ve donanım doğrulaması bekliyor.
- **Öncelik:** Düşük akım ölçüm zinciri için sınırlı bütçeli alternatif araştırması.
- **Bütçe:** Kullanıcı bildirimi yaklaşık 250 TL.
- **Zamanlama:** Kullanıcının hedefi hafta sonu ilk denemeleri yapmak; kesin tarih teslimat ve hazırlığa bağlı.
- **Kapsam:** Mevcut BERO ölçüm mimarisini değiştirmeden, SCT-013 30A/1V ile ADS1115 kartını ayrı bir deney düzeneğinde değerlendirmek.

## Amaç

Mevcut SCT + bias orta noktası + ESP32 dahili ADC yoluna alternatif olarak ADS1115 kullanıldığında özellikle 0,5 A altındaki ölçümlerde gürültü, sıfıra yakın okuma davranışı, kararlılık ve PZEM referansına göre sapmanın iyileşip iyileşmediğini araştırmak.

İkincil hedef, ADS1115 kartının giriş yapısı uygunsa harici bias bölücü kullanmadan güvenli ve kararlı ölçüm yapılıp yapılamayacağını sınamaktır. Bias'sız çalışma önceden kabul edilmiş bir özellik değildir; deney sorusudur.

## Deney mimarileri

1. **Mevcut referans yol:** SCT-013 30A/1V → mevcut bias devresi → ESP32 ADC.
2. **Alternatif yol:** Aynı model SCT-013 30A/1V → ADS1115 → ESP32 I²C.
3. **Referans ölçüm:** PZEM-004T V3.0; PZEM mutlak ground truth değil, BERO'nun karşılaştırma/etiketleme referansıdır.

Mümkün olduğunda aynı fiziksel yük ve aynı hat koşulu kullanılacaktır. Aynı anda karşılaştırma yapılırsa iki ayrı CT kullanımı ve sensörler arası fark ayrıca kaydedilir. Tek CT ile ardışık karşılaştırmada yük ve PZEM kararlılığı doğrulanır; bağlantı değişiklikleri enerjisiz koşulda yapılır.

## Temel sınırlar

- Mevcut BERO bias + ESP32 ADC yolu korunur; bu deney onu değiştirmez.
- MCP3208 yeniden gündeme alınmayacak; E19'un konusu değildir.
- 0,5 A altı hedef bölgedir; testler gerektiğinde 0,5 A üstüne taşarak geçiş bölgesini de kapsar.
- ±%4 sapma hedefi bir kabul hedefidir; deney sonucu önceden varsayılmaz.
- ADS1115 PGA ayarı harici yükselteç gibi sensör sinyalini fiziksel olarak büyütmez; ADC ölçüm aralığını/kazanç kademesini değiştirir.
- Diferansiyel okuma ortak-mod gürültüsünü azaltabilir; tüm gürültüyü yok etmez.
- Diferansiyel mod, AIN pinlerinin GND–VDD çalışma sınırlarını kaldırmaz. Giriş ortak-mod seviyesi ve kart üzerindeki direnç/koruma/bias ağı incelenmeden SCT uçları doğrudan bağlanmayacaktır.
- Paylaşılan internetteki burden dirençli akım çıkışlı CT şeması, BERO'daki 1V çıkışlı SCT-013 için doğrudan kopyalanmayacaktır. 1V modelin dahili burden yapısı esas alınır; kart şeması/PCB'si ayrıca incelenir.

## Deney aşamaları

1. Kartın ön/arka yüzünü, pin etiketlerini, besleme gerilimini, I²C adresini ve olası pull-up seviyelerini kaydet.
2. ADS1115 breakout üzerinde girişe bağlı direnç, kondansatör, koruma ve olası bias/common-mode elemanlarını incele.
3. SCT model etiketini doğrula: SCT-013 30A/1V. 100A/1V ile karıştırma.
4. Güvenli besleme ve giriş sınırları doğrulandıktan sonra yüksüz/akımsız taban ölçümü yap.
5. İlk yük denemesinde mevcut tur sayısını koru; ilk karşılaştırmada 5 tur gibi yeni bir değişken ekleme.
6. Düşük yük basamaklarında ADS1115 ve mevcut ESP32 ADC yolunu PZEM ile karşılaştır.
7. Single-ended ve differential yöntemleri yalnızca elektriksel giriş koşulları uygunsa ayrı koşullar olarak dene.
8. PGA ve veri hızı seçeneklerini giriş tepe gerilimi/clipping kontrolüyle değerlendir.
9. 200 ms ve daha uzun RMS pencerelerini karşılaştır; 20 ms tek periyot penceresini varsayılan doğru yöntem kabul etme.
10. Sonuçları aynı deney kimliği altında ham kayıt, özet istatistik ve yorumla sakla.

## Güvenlik

- Şebeke tarafındaki kablo kesme/ekleme veya açık iletkenle çalışma yapılmaz.
- CT yalnızca yalıtılmış tek bir iletkeni çevreler; faz ve nötr aynı CT içinden birlikte geçirilmez.
- Akım çıkışlı CT'lerde primer akım varken sekonder açık bırakılmaz. Bu deneydeki 30A/1V modelin kendi tipine ait üretici bağlantı koşulları ayrıca doğrulanır.
- ADS1115 analog girişleri besleme raylarının dışına çıkarılmaz; 3,3 V ile çalışan ESP32'ye 5 V I²C pull-up uygulanmadığı doğrulanır.
- Giriş topolojisi ve common-mode seviyesi doğrulanmadan doğrudan bağlantı veya enerjili deneme yapılmaz.

## Çıktılar

- Kart fotoğrafları ve bağlantı incelemesi.
- Kullanılan firmware/kod sürümü ve gerçek derleme/çalışma logu.
- Yüksüz taban ve her yük basamağı için örnek sayısı, ortalama, RMS, standart sapma, CV, yüzdelikler, minimum/maksimum, clipping/dropout gözlemi.
- PZEM'e göre sapma ve iki ADC mimarisinin karşılaştırması.
- Bias'sız çalışmanın güvenli/kararlı olup olmadığına dair kanıt ve sınırları.
- Deney sonunda: düşük akım alternatifi olarak kabul, kısmi kabul veya reddetme kararı.

**Sonuç durumu:** Henüz ölçüm yok. Bu kayıt yalnızca sipariş ve deney planını belgeliyor.


## ESPHome ADS1115 + ct_clamp YAML incelemesi (2026-11-09)

ESPHome 2026.10.2 resmi dokümantasyonu ve C++ kaynak kodu incelendi. Mimari fikir **geçerli ve ESPHome tarafından destekleniyor**: ADS1115 sensör platformu, ct_clamp için gerilim örnekleme kaynağı olabilir; ADS1115 hub üzerinde `continuous_mode: true` özellikle ct_clamp kullanımı için önerilir.

Ancak paylaşılan YAML tek blok olarak doğru değil. Yapı iki sensör platformuna ayrılmalıdır:

1. `platform: ads1115` kaynak gerilim sensörü oluşturur; `id`, `ads1115_id`, `multiplexer`, `gain` ve `sample_rate` burada tanımlanır.
2. `platform: ct_clamp` kaynak sensörü `sensor: ads1115_diferansiyel_giris` ile kullanır. `sensor_id`, `ads1115_id`, `multiplexer` ve `gain` ct_clamp seçenekleri değildir.
3. ADS1115 hub'da `continuous_mode: true` açılır.
4. ESPHome dokümanına göre ADS1115 örnekleme hızı 860 SPS'ye kadar seçilebilir; gerçek alınan farklı örnek sayısı ct_clamp debug logundan doğrulanmalıdır.

### Düzeltilmiş bileşen yapısı — henüz donanımda test edilmedi

```yaml
ads1115:
  - id: ads1115_hub
    i2c_id: bus_a
    address: 0x48
    continuous_mode: true

sensor:
  # ADS1115 diferansiyel gerilim kaynağı
  - platform: ads1115
    id: ads1115_diferansiyel_giris
    ads1115_id: ads1115_hub
    multiplexer: 'A0_A1'
    gain: 0.256
    sample_rate: 860

  # CT RMS hesabı ve akım kalibrasyonu
  - platform: ct_clamp
    name: "BERO ADS1115 SCT Akım"
    sensor: ads1115_diferansiyel_giris
    sample_duration: 200ms
    update_interval: 2s
    filters:
      # Kalibrasyon noktaları PZEM karşılaştırmasıyla ölçülerek belirlenecek.
      # Örnek 0.1 -> 0.4 değerleri deneysel veri olmadan kullanılmayacak.
      - calibrate_linear:
          - 0.0 -> 0.0
          - 0.1 -> 0.4
```

Bu yalnızca bileşen bağlantı iskeletidir; I²C pinleri ve kart beslemesi gerçek ESP32 kartına göre ayrıca tanımlanmalıdır. 0.1 → 0.4 kalibrasyon çifti örnek olarak gösterilmiştir, gerçek katsayı değildir. Beş tur etkisi de otomatik olarak bu kalibrasyon noktasıyla giderilmiş sayılmaz; gerçek yükte ölçülen ham ct_clamp çıktısı ile PZEM referansına göre kalibrasyon yapılmalıdır.

### Mimari iddiaların teknik değerlendirmesi

- **İşlemci yükü:** ct_clamp, örnekleme sırasında yüksek frekanslı ESPHome loop'u kullanır ve her farklı örnekte toplam/kare toplamı biriktirip pencere sonunda RMS hesaplar. Bu, optimize edilmiş C++ uygulamasıdır; ancak işlemci yükünü sıfırlamaz veya hesabı ADC'nin içine taşımaz.
- **Diferansiyel/parazit:** A0_A1 diferansiyel ölçüm ortak-mod bileşenlerini reddetmeye yardımcı olabilir; her türlü EMI/paraziti sıfırlamaz. İki AIN pininin de GND–VDD aralığında kalması gerekir. Kartın gerçek giriş ağı görülmeden bias'sız bağlantı kabul edilmez.
- **Zaman davranışı:** `update_interval: 2s` sonuç yayınlama/ölçüm çevrim aralığıdır; `sample_duration: 200ms` ise her çevrimdeki örnek toplama penceresidir. Bu ayar 2 saniye boyunca kesintisiz dalga kaydı değildir; yaklaşık 200 ms ölçüm penceresi, ardından çevrim aralığına kadar bekleme söz konusudur. Kısa geçişleri kaçırma ihtimali deneyde incelenecek.
- **Örnekleme:** ADS1115 860 SPS ayarı ADC dönüşüm hızıdır; ct_clamp'in logladığı gerçek farklı örnek sayısı ve SPS değeri esas alınmalıdır. Aynı değerin tekrarları ct_clamp içinde atlanır.
- **Gain:** `gain: 0.256`, ±0.256 V tam ölçek aralığıdır; 16 kat analog yükseltme değildir. SCT çıkışının tepe değeri bu aralığı aşarsa kırpılma/taşma oluşabilir.

**Kaynaklar:** ESPHome ADS1115 dokümantasyonu; ESPHome CT Clamp dokümantasyonu; ESPHome 2026.10.2 ct_clamp ve ads1115 C++ kaynak kodu. Bu kayıt kaynak kod incelemesidir; gerçek kartta derleme/ölçüm doğrulaması değildir.

## 2026-11-09 — İkincil değerlendirme hedefi: yaklaşık 2 A bölgesi

Kullanıcı fikri: ADS1115 alternatifi düşük akım denemesinde işe yararsa, yalnızca 0,5 A altındaki bölge için değil, uygun ölçüm aralığı ve deneysel kalibrasyon katsayısıyla yaklaşık 2 A civarında da kullanılabilirliği değerlendirilecek.

- 2 A civarı ayrı bir doğrulama noktası/bölgesi olarak deneye eklenecek; mevcut düşük akım hedefinin yerine geçmez.
- Katsayı önceden seçilmeyecek veya teorik olarak atanmayacak. Gerçek SCT çıkışı, ADS1115 ham/ct_clamp çıktısı ve aynı kararlı yük koşulundaki PZEM referans ölçümleriyle belirlenecek.
- Farklı akım aralıklarında tek doğrusal katsayının yeterli olup olmadığı ayrıca kontrol edilecek. Gerekirse kalibrasyon aralığı ve doğrusal olmayan davranış raporlanacak.
- 2 A civarında kullanılabilirlik; girişte clipping olmaması, kararlılık/tekrar edilebilirlik ve PZEM'e göre sapma birlikte değerlendirilerek karara bağlanacak.
- **Durum:** Yalnızca deney hedefi olarak kaydedildi. ADS1115 kartı henüz fiziksel olarak test edilmedi; katsayı veya 2 A başarısı iddia edilmiyor.

## 2026-11-09 — Aynı ESP üzerinde çift ölçüm yolu ve yazılımsal aralık seçimi fikri

Kullanıcının tarif ettiği olası mimari:

- Mevcut ESP32 dahili ADC + bias ölçüm yolu normal ölçüm akışını izlemeye devam eder.
- Aynı ESP32'ye I²C üzerinden ADS1115 bağlanır; ADS1115 ikinci bir ölçüm yolu olarak aynı SCT kanalını ölçer.
- Akım yaklaşık 1 A eşiğinin altına indiğinde yayımlanan/tercih edilen ölçüm ADS1115 yolundan; eşik üstünde mevcut ESP32 ADC yolundan seçilir.
- Böylece ADS1115'in düşük akım bölgesinde, mevcut yolun ise daha yüksek akım bölgesinde kullanılması hedeflenir. Yaklaşık 2 A çevresi ayrıca doğrulanacak.

Bu fikir şu aşamada **yazılımsal ölçüm yolu seçimi** olarak ele alınır; analog sinyali fiziksel olarak anahtarlayan bir röle/multiplexer kararı verilmiş değildir. İlk geliştirme adımında iki yolun paralel ölçüm yapıp ham/işlenmiş sonuçlarının ayrı izlenmesi, seçimin ise yazılımda yapılması tercih edilebilir. Geçişte ani değer sıçramalarını önlemek için eşik çevresinde histerezis ve yol geçişi doğrulaması gerekecek; 1 A şimdilik kullanıcı tarafından önerilen başlangıç eşiğidir, deneyle sabitlenmiş değildir.

**Elektriksel ön koşul:** Aynı SCT sekonder çıkışını iki analog ön uca bağlamadan önce her iki giriş devresinin empedansı, bias/common-mode yapısı, koruma elemanları ve giriş sınırları birlikte incelenmelidir. Mevcut ESP32 bias ağı ile ADS1115 diferansiyel girişinin paralel bağlanmasının sinyali yüklemeyeceği veya iki devrenin birbirini etkilemeyeceği varsayılmayacaktır. Gerekirse tamponlama/ayırma veya kontrollü analog anahtarlama tasarlanır. Kart ve bağlantı şeması görülmeden paralel bağlantı yapılmaz.

**Durum:** Mimari fikir kaydedildi; eşik, histerezis, analog bağlantı ve yazılım seçimi henüz tasarım/deney aşamasında. Donanımda uygulanmış değildir.

## 2026-11-13 — İlk donanım bağlantısı ve iki aşamalı test planı

E19 fiziksel deneme aşamasına geçti. Çalışma iki soruya ayrıldı:

1. **Aşama 1 — ADS1115 bağlantı/okuma doğrulaması:** I2C adresi 0x48 bulundu. A0-A1 diferansiyel okuma yüksüz koşulda mikrovolt seviyesinde çıktı verdi. Yaklaşık 60 W yükte önceki düşük hızlı testte değerler yaklaşık -12.8 mV ile +13.1 mV arasında değişti. Bu aşama yalnız bağlantı ve sinyal tepkisi gözlemidir; RMS akım/katsayı doğrulaması değildir. [İlk log ve yorum](../../logs/ads1115/2026-11-13-E19-ads1115-first-bringup.md).
2. **Aşama 2 — 100 W ortak ölçüm alanı ve katsayı belirleme:** ESP32D1 mevcut ölçüm zinciri, ESP32D2 ADS1115 zinciri ve PZEM aynı 100 W sabit yük koşulunda karşılaştırılacaktır. Amaç, her iki SCT yolunun kararlı değer ürettiği ortak alanda ADS1115 katsayısını PZEM referansıyla belirlemektir. Test henüz yapılmadı.

### Aşama 2 test kararı

- Yük: 100 W akkor ampul, sürekli açık.
- Karşılaştırma: ESP32D1 mevcut SCT/ADC/ct_clamp yolu, ESP32D2 ADS1115/ct_clamp yolu ve PZEM-004T V3.0.
- Kayıt: Zaman damgalı kararlı değerler; gerilim, akım ve aktif güç; firmware ayarları ve bağlantı/tur sayısı.
- Kalibrasyon: YAML'daki nominal 30A/1V başlangıç doğrusu ölçüm sonucu değildir. Katsayı ADS1115 ham ct_clamp kararlı ortalaması ile PZEM kararlı akım referansından belirlenecek. Mevcut ESP32D1 K=24.22 değiştirilmeyecek.
- İki CT kullanılırsa konum ve tur sayısı kaydedilir. Tek CT ile ardışık ölçüm yapılırsa bağlantı değişiklikleri enerjisiz koşulda yapılır ve PZEM/yük kararlılığı yeniden doğrulanır.
- Kabul: Tekrarlı kararlı sonuç, clipping/taşma olmaması ve PZEM'e göre sapmanın raporlanması. ±%4 hedefi sonuç görülmeden başarı sayılmaz.

**Durum:** Aşama 1 LOG İLE DESTEKLENDİ. Aşama 2 PLANLANDI; 100 W ölçümü ve katsayı hesabı beklemede.


## 2026-11-13 — Üç modül ortak yük karşılaştırması

Üç cihaz logu ortak 17:48:27–17:51:13 (+03:00) penceresinde karşılaştırıldı. ADS1115 yayımlanan akım ortalaması 0.469881 A (n=84), PZEM 0.469882 A (n=34), ESP32D1 CH1-1T 0.434240 A (n=167) oldu. ESP32D1/PZEM farkı yaklaşık -7.59%; bu tek oturum gözlemidir ve katsayı kararı değildir.

ESP32D2 açılış logu ADS1115 Gain 2 / Sample rate 7 gösterirken depodaki E19 YAML Gain 2.048 / 860 bekler. Log esp32d2.yaml doğrulanmış cache'inden açıldığını bildirir; depodaki deney YAML'ının cihaza yüklendiğini kanıtlamaz. 860 SPS doğrulanmış değildir.

Modül 3 OFF komutlarında GPIO_OFF_READBACK_MISMATCH uyarıları ve OFF sonrası PZEM akımının sürmesi nedeniyle fiziksel yük kesilmesi doğrulanmadı. Olay akışı aktarımı çalıştı; ancak fiziksel ON/OFF etiketi sayılmayacak. Katsayılar değişmedi ve ±%4 başarısı ilan edilmedi.

Ayrıntı: [E19 üç modül karşılaştırma kaydı](../../logs/ads1115/2026-11-13-E19-three-module-100w-comparison.md).


## 2026-11-13 — 100 W ortak testinin yorum güncellemesi ve 150 W takip testi

100 W üç-modül logu artık yalnızca gözlemsel ortak-yük karşılaştırması olarak değerlendirilir. Ayrıntılı düzeltme [100 W karşılaştırma raporunun 8. bölümünde](../../logs/ads1115/2026-11-13-E19-three-module-100w-comparison.md) tutulur.

- 200 ms'de 174–177 farklı örnek, ADS1115 860 SPS seçimiyle uyumludur. Açılış logundaki `Sample rate: 7` değeri 7 SPS değildir; önceki hız uyuşmazlığı yorumu geri çekilmiştir.
- ADS1115 0.469881 A ve PZEM 0.469882 A ortalamaları bu yük/oturumda yakındır. Katsayı aynı 0.47 A noktasından türetildiyse bu bağımsız doğrulama değildir.
- Kullanıcı değerlendirmesinde 27.60 katsayısı geçse de depodaki E19 YAML halen 30.0 başlangıç doğrusu içerir. Çalışan binary/katsayı kaynağı henüz birebir eşleştirilmedi.
- `accuracy_decimals: 3` yayın çözünürlüğünü artırabilir; gerçek ölçüm doğruluğunu artırmaz. 150 W karşılaştırmasında mevcut 2 basamak korunacaktır.
- Gain 0.512 önerisi henüz uygulanmayacaktır. Dar ADC aralığı fiziksel sinyali büyütmez; clipping/headroom ve A0/A1 common-mode güvenliği önce doğrulanmalıdır.
- 0.05 A filtresi ve mevcut gain korunur. Yüksüz taban ölçümü olmadan eşik düşürülmez.
- SSR fiziksel OFF doğrulanmadığından 100 W kaydı SSR ON/OFF etiketli deney sayılmaz.

### Aşama 3 — 150 W sabit yük karşılaştırması açıldı

- **Durum:** PLANLANDI.
- **Hedef:** 100 W oturumundan sonra aynı ADS1115 ölçüm zincirinin daha yüksek ve güvenli ölçüm alanındaki davranışını görmek; 100 W ile karşılaştırılabilir kararlı kayıt üretmek.
- **Yük:** 150 W akkor lamba; yük sürekli bağlı ve fiziksel olarak devrede olduğu bağımsız biçimde kontrol edilecek.
- **Karşılaştırma:** ESP32D2 ADS1115/ct_clamp ve Modül 3 PZEM; Modül 2 CH1-1T logu varsa ek gözlem kanalı olarak saklanır, ana kabul ölçütü değildir.
- **Değişmeyecek ayarlar:** ADS1115 gain 2.048, sample_rate 860, continuous_mode true, A0_A1, ct_clamp sample_duration 200 ms, update_interval 2 s, accuracy_decimals 2, mevcut filtre ve depodaki YAML katsayı ayarı. Kayıt öncesi gerçek çalışan firmware/katsayı kaynağı ayrıca not edilecek.
- **Toplanacaklar:** cihaz logları ve ortak zaman aralığı; PZEM gerilim/akım/güç; ADS1115 yayımlanan akım; ct_clamp örnek sayısı/SPS; ortalama, SD, min-maks; I2C/timeout/clipping belirtileri; UDP gönderim/alım durumu.
- **Yorum sınırı:** 150 W tek başına çok noktalı kalibrasyon veya ±%4 başarısı değildir. 100 W ve 150 W birlikte iki yük noktasında gözlemsel karşılaştırma sağlar; bağımsız tekrar ve daha fazla yük noktası gerekir.
- **SSR:** Fiziksel anahtarlama doğrulanana kadar olaylar yük durumunu temsil etmez. Mümkünse test boyunca yük sürekli bağlı tutulur; SSR'ın mantıksal durumu veri etiketine dönüştürülmez.
- **Güvenlik ön koşulu:** A0/A1 girişlerinin bias/common-mode ve gerilim sınırları doğrulanmamışsa ADS1115 bağlantısı enerjili deneye alınmaz. Şebeke bağlantısı uygun muhafaza ve koruma altında yapılır.

**Bu kayıt yalnızca test planının açıldığını gösterir. 150 W ölçümü, log, derleme/OTA veya cihaz doğrulaması henüz yoktur.**


## 2026-11-13 — Aşama 3 sonucu: 150 W sabit yük

150 W sabit yük CSV analizi [ayrı karşılaştırma raporunda](../../logs/ads1115/2026-11-13-E19-150w-comparison.md) saklanır.

- Ortak kararlı pencere 18:16:30–18:24:30 (+03:00).
- PZEM ortalama 0.65472 A; ADS1115 0.66279 A (+%1.23); Modül 2 CH1-1T 0.60402 A (-%7.74).
- İlk yaklaşık iki dakikadaki lamba ısınma/oturma davranışı kalibrasyon penceresine dahil edilmedi.
- ADS1115 için K=27.60'ın çalışan binary'de kullanıldığı henüz kesin eşleştirilmedi. Bu varsayımla hesaplanan K≈27.26 yalnız koşullu hesaptır; katsayı değiştirilmedi.
- Ayarlar değiştirilmedi; 0.512 gain ve accuracy_decimals 3 uygulanmadı.

### Aşama 4 — 58 W sabit yük karşılaştırması açıldı

- **Durum:** PLANLANDI.
- 58 W nominal akkor yük sürekli bağlı olacak; ON/OFF geçiş deneyi yapılmayacak.
- İlk yaklaşık 3 dakika oturma süresi; ardından en az 5 dakika kararlı kayıt hedeflenir.
- İlk karşılaştırma için 150 W ile aynı gain 2.048, sample_rate 860, continuous_mode, 200 ms pencere, 2 s update, accuracy_decimals 2, 0.05 A filtre ve mevcut katsayı korunur.
- Gain 0.512 ve accuracy_decimals 3 önerileri bu testten önce uygulanmayacak; ayrı değişken deneyi olarak ertelenmiştir.
- PZEM aynı kararlı pencerede referans olacak; teorik yük akımı kalibrasyon girdisi değildir.
- A0/A1 bias/common-mode ve giriş gerilimi güvenliği fiziksel olarak doğrulanmadan enerjili teste başlanmaz.
- Protokol: [58 W test planı](../../logs/ads1115/2026-11-13-E19-58w-test-plan.md).


## 2026-11-13 — Aşama 4 düzeltmesi: 58 W yerine 57 W

Kullanıcı, sıradaki yükün **57 W** olduğunu ve testin **18:32 (+03:00)** saatinde açıldığını bildirdi. Önceki 58 W planı uygulanmadı; 57 W test kaydı esas alınır: [E19 57 W test kaydı](../../logs/ads1115/2026-11-13-E19-57w-test.md).

150 W deneyiminden sabit yük yöntemine eklenen not: ilk yaklaşık iki dakikada PZEM akım/güç yükselişi görüldüğü için yeni testlerde ilk 3 dakika geçici bölge kabul edilecek; kararlılık yalnız süreye göre değil, PZEM ve ADS/SCT zaman serilerinin gerçekten oturmasına göre belirlenecek. İlk karşılaştırmada mevcut ayarlar korunacak; gain 0.512 ve accuracy_decimals 3 ertelendi.

## 2026-11-13 — Deney amacı ve sıra düzeltmesi: önce çalışma sınırı, sonra katsayı

Önceki aşama metinlerinde 100 W testinden itibaren katsayı belirleme hedefi öne çıkarılmıştı. Kullanıcının son kararıyla E19'un mevcut çalışma aşamasının amacı netleştirilmiştir:

**Mevcut aşamanın hedefi kalibrasyon değildir.** ADS1115 + SCT zincirinin mevcut yapılandırma ve mevcut kaba/başlangıç katsayısıyla düşük akımda çalışma davranışını belirlemek; kararlılık, tekrarlanabilirlik, sıçrama/okuma kaybı ve kullanılabilir alt sınırı gözlemlemektir.

- Yükler kademeli olarak aşağı indirilecek.
- Her basamakta ADS1115 gain, sample rate, continuous mode, ct_clamp penceresi, güncelleme aralığı, filtre ve katsayı sabit tutulacak.
- PZEM aynı zaman aralığındaki karşılaştırma referansı olarak kullanılacak; bu aşamada PZEM'e göre fark raporlanır, katsayı bu farka göre ayarlanmaz.
- Bir basamakta kararlı görünmek tek başına alt sınırın kanıtı değildir; mümkün olduğunda yeterli süre ve tekrar gözlemi aranır.
- Sistem kararsızlaşmaya başladığında o nokta ve bir önceki kararlı basamak ayrı kaydedilecek. Alt çalışma sınırı, mevcut kurulum/ayarlar için deneysel gözlem olarak ifade edilecek.
- Katsayı belirleme ve kalibrasyon, bu çalışma sınırı deneyi bittikten sonra ayrı aşamadır. Tek noktaya göre katsayı ayarlanmayacak.

### İlk düşük akım gözlemi — 57 W

Kullanıcı bildirimi: PZEM 0,265 A, ADS1115 + SCT 0,270 A. Mevcut katsayı kaba/kalibre edilmemiştir. Fark +0,005 A ve PZEM'e göre yaklaşık +%1,89 (**HESAP**). Bu tek nokta, kalibrasyon başarısı, ±%4 genel kabulü veya alt sınır doğrulaması değildir. Tam zaman serisi/CSV ve ortak kararlı pencere istatistiği henüz bu kısa bildirime eşlik etmiyor.

### Eski sistemle karşılaştırma notu

İlk SCT + ESP32 dahili ADC yolu 100 W noktasında kısa kalibre edilmişti; buna rağmen düşük akım bölgesinde kararlılık/hassasiyet sorunu sürmüştü. Bu nedenle yeni ADS1115 yolunun 57 W'taki kararlı görünümü, henüz kalibre edilmemiş katsayıya rağmen ayrı ve anlamlı bir gözlemdir. İki mimariyi aynı sonuç dosyasında birleştirmeden, farklı ölçüm zincirleri olarak karşılaştır.

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
