# E19 — ADS1115 ile düşük akım ölçüm alternatifi

- **Durum:** PLANLANDI — ADS1115 kartı kullanıcı tarafından sipariş edildi; fiziksel teslimat ve deney henüz yapılmadı.
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
