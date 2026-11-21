# ADS1115 İkili Okuma – Yavaş Salınım Araştırması
**Tarih:** 2026-11-22  
**Görev:** MOD2-GRV001  
**Durum:** AÇILDI – TEST BEKLİYOR  
**Kod durumu:** Mevcut çalışan YAML değiştirilmeyecek

## 1. Amaç

Aynı ADS1115 üzerindeki iki diferansiyel SCT kanalında gözlenen, birbirleriyle aynı periyotta olmayan yavaş akım salınımlarının kaynağını araştırmak.

Araştırılacak temel soru: Salınım iki kanalın birlikte okunması, ADS1115 dönüşüm sırası veya ESPHome ölçüm zamanlaması nedeniyle mi oluşuyor; yoksa SCT ve analog giriş kollarının kendi davranışlarından mı kaynaklanıyor?

Bu deneyin amacı katsayı belirlemek, filtre ayarlamak veya ölçüm dalgalanmasını yazılımla gizlemek değildir.

## 2. Gözlemin dayanağı

Kullanıcının paylaştığı Home Assistant grafiği:
- Zaman aralığı: yaklaşık 00:18:00–00:22:15.
- Yük: Kettle 1 + 100 W ampul.
- PZEM akımı: yaklaşık 1.163 A seviyesinde düz/kararlı görünmektedir.
- A0–A1 (sarı): yaklaşık 0.98–1.21 A aralığında belirgin yavaş salınım.
- A2–A3 (kırmızı): yaklaşık 1.05–1.19 A aralığında, sarı kanalla aynı periyotta olmayan salınım.
- Görselden çıkarılan periyotlar yaklaşık 45–60 saniye mertebesindedir; kesin periyot ham CSV zaman serisinden hesaplanmalıdır.

Bu grafik nitel gözlemdir. Tek başına ADS1115, ESPHome veya gerçek yük kaynaklı bir neden kanıtlamaz. PZEM'in daha yavaş örneklemesi de göz önünde tutulacaktır.

## 3. Donanım ve mevcut yapı

- ESP: ESP32D2
- ADC: ADS1115, I²C adresi 0x48
- SDA: GPIO21
- SCL: GPIO22
- Besleme: 3.3 V
- Ortak GND: ESP32D2–ADS1115
- Kanal 1: A0–A1, SCT013
- Kanal 2: A2–A3, ikinci SCT013
- Ölçüm yaklaşımı: ADS1115 diferansiyel kanal okuması ve ESPHome ct_clamp
- Bilinen önceki ayarlar: ADS1115 continuous, 860 SPS, PGA 2.048 V; ct_clamp penceresi 200 ms, sensör güncellemesi 1 s. Test öncesi çalışan iki kanallı YAML'dan gerçek değerler teyit edilecektir.

**Önemli:** Depoda görülen KOD-0 YAML yalnızca A0–A1 tek kanalını tanımlar. Bu dosya iki kanallı salınımı açıklamak için yeterli değildir. Deneyden önce sahada çalışan iki kanallı YAML ayrıca alınmalı ve değiştirilmeden incelenmelidir.

## 4. Hipotezler

1. İki diferansiyel kanalın ADS1115 üzerinde ardışık dönüşümle okunması ve dönüşüm zamanlarının farklılığı.
2. İki ct_clamp örnekleme penceresinin başlangıç/bitiş zamanlarının veya güncelleme fazlarının farklı olması.
3. A0–A1 ve A2–A3 analog kollarında bias, SCT, bağlantı veya ortak-mod davranışı farkı.
4. ESP32/ADS1115 besleme veya referans hattında yavaş değişim.
5. Yükün gerçek akımında PZEM'in örnekleme/güncelleme hızı nedeniyle grafikte görünmeyen değişim.

Bunlar test edilecek hipotezlerdir; şu aşamada hiçbiri doğrulanmış neden değildir.

## 5. Deney protokolü

### A. Mevcut çift kanal düzeni – referans kaydı
- Çalışan iki kanallı YAML aynen korunacak; deney için kopyası alınacak.
- Kettle 1 + 100 W ampul yükü ve aynı SCT yerleşimi korunacak.
- PZEM, A0–A1 ve A2–A3 aynı oturumda kaydedilecek.
- En az 5 dakika kesintisiz veri alınacak.
- Açılış/kapanış geçişleri kararlı pencere analizine katılmayacak.
- Ham CSV saklanacak; grafik tek başına veri kaynağı sayılmayacak.

### B. Tek kanal karşılaştırması
Güvenli ve mevcut çalışan yapıdan ayrı bir test kopyası hazırlanması halinde:
1. Yalnız A0–A1 okunarak aynı yükte en az 3 dakika kayıt alınacak.
2. Yalnız A2–A3 okunarak aynı yükte en az 3 dakika kayıt alınacak.
3. Her aşamada PZEM kaydı devam edecek.
4. Tek kanal testleri arasında SCT konumu, yönü, yük ve kablolama değiştirilmemeye çalışılacak.

Bu aşama için YAML değişikliği ancak mevcut iki kanallı dosya incelendikten ve kullanıcı onayladıktan sonra yapılacaktır. Çalışan YAML üzerine yazılmayacaktır.

### C. Zaman serisi karşılaştırması
Her kanal için örnek sayısı, zaman damgaları ve örnek aralığı; ortalama, medyan, standart sapma, minimum ve maksimum; trend çıkarıldıktan sonra tepe-çukur genliği; tepe zamanları ve yaklaşık periyot; iki kanal arasındaki gecikme/faz ilişkisi; PZEM ile zaman eşleştirilmiş fark hesaplanacaktır.

İki ADS1115 kanalının ardışık dönüşümleri eşzamanlı örnek kabul edilmeyecektir. Zaman damgaları gerçek ölçüm anını göstermiyorsa bu sınırlama rapora yazılacaktır.

## 6. Kontrol edilecek YAML/firmware alanları
- ADS1115 continuous_mode
- Her kanalın multiplexer, gain, sample_rate tanımı
- Sensörlerin update_interval değerleri
- ct_clamp sample_duration değerleri
- filters zinciri ve filtre sırası
- Sensörlerin güncelleme/başlatılma sırası
- I²C frekansı ve hata/yeniden deneme logları

Örnekleme penceresi veya filtreler ilk referans kaydı alınmadan değiştirilmeyecektir.

## 7. Güvenlik ve değişiklik kontrolü
- ADS1115 A0, A1, A2 ve A3 pinlerinin her birinin GND'ye göre mutlak gerilimi ADS1115 besleme sınırları içinde kalmalıdır.
- Diferansiyel ölçüm seçimi pinlerin mutlak giriş sınırlarını değiştirmez.
- SCT yalnızca yalıtımı sağlam tek bir iletkeni kavramalıdır.
- Şebeke bağlantılı devrede ESP32 GND doğrudan şebekeye bağlanmayacaktır.
- Osiloskop kullanılacaksa prob toprak bağlantısının koruma toprağıyla ilişkisi önceden doğrulanmalıdır.
- Mevcut çalışan YAML ve K=27.59 korunacaktır. Bu deneyde kalibrasyon katsayısı veya filtre değişikliği yapılmayacaktır.

## 8. Başarı ölçütü

Deney, salınımın kaynağını kesin olarak bulmuş sayılmak için değil, olası kaynakları birbirinden ayıracak kanıt üretmek için açılmıştır.

Başarılı çıktı: çalışan iki kanallı YAML'ın incelenmiş kopyası; ham CSV ve test koşulları; her iki kanalın salınım periyodu/genliği/zaman ilişkisi; tek kanal ve çift kanal kayıtlarının karşılaştırması; bulguların kanıt sınırlarıyla birlikte teknik yorumu.

## 9. Mevcut karar
- Deney açıldı; fiziksel test henüz yapılmadı.
- YAML henüz değiştirilmedi.
- Filtre genişletme veya update_interval değiştirme kararı verilmedi.
- K=27.59 ve mevcut V1.1 çalışma kodu korunuyor.
- İlk sonraki adım: sahada çalışan iki kanallı YAML dosyasını incelemek.

## 10. Deneyde incelenecek mevcut V1.1 iki kanallı YAML

Kullanıcı tarafından 2026-11-22 tarihinde paylaşılan YAML, salınım araştırmasının referans kodu olarak bu deney kaydına eklenmiştir. Kod içeriği kullanıcı tarafından sağlandığı biçimiyle korunmuştur; bu ekleme kodun yeniden derlendiği, fiziksel cihaza yüklendiği veya doğrulandığı anlamına gelmez.

**Kodun deney açısından önemli zamanlama/ölçüm satırları:**
- ADS1115: `continuous_mode: true`
- Her iki ADS1115 kanalında: `sample_rate: 860`
- Her iki `ct_clamp` sensöründe: `sample_duration: 200ms`
- Her iki `ct_clamp` sensöründe: `update_interval: 1s`
- Her iki kanalda aynı kalibrasyon: K=27.59
- Her iki kanalda 5 mA altı sıfırlama filtresi

**İlk inceleme notu:** YAML iki ayrı ADS1115 multiplexer kaynağını ve iki ayrı `ct_clamp` sensörünü aynı ESPHome `sensor:` listesinde tanımlar. Ancak yalnızca YAML metninden ADS1115 dönüşümlerinin gerçek zaman çizelgesi, kanal dönüşüm sırası veya iki `ct_clamp` penceresinin tam başlangıç fazı kanıtlanamaz. Bunlar ESPHome bileşen davranışı ve çalışma loglarıyla ayrıca incelenecektir.

**Deney kuralı:** Bu YAML referans olarak eklendi; üzerinde henüz değişiklik yapılmayacak. Tek kanallı/çift kanallı karşılaştırma için gerekirse ayrı deney kopyası hazırlanacak. Mevcut V1.1 dosyasının üzerine yazılmayacaktır.

### Kullanıcının sağladığı YAML – aynen ek

```yaml
# ============================================================
# BERO – ESP32D2 / ADS1115 No.10 / SCT013 30A-1V
# MOD2-GRV001 – V1.1 – A0-A1 ve A2-A3 (Bias'lı Hat) Deneme Sürümü
# ============================================================
#
# AMAÇ:
# 1) SCT013 30A/1V sinyalini ADS1115 No.10 üzerinden A0-A1
#    diferansiyel girişte okuyup ct_clamp ile RMS akıma çevirmek.
# 2) İkinci hatta (bir hattında bias bulunan) SCT013 sinyalini
#    ADS1115 No.10 üzerinden A2-A3 diferansiyel girişte okuyup
#    ayrı ct_clamp sensörü olarak Home Assistant'a aktarmak.
#
# V1.1 DENEY AMACI:
# V1.0'da kullanılan 30.66 katsayısı ile yapılan yüksek yük
# ölçümlerinde SCT sonucu PZEM karşılaştırma değerinden yüksek
# bulundu. 2026-11-21 tarihli history (2).csv içindeki dört
# kararlı yüksek yük penceresinden 27.59 deney katsayısı elde
# edildi. V1.1 bu katsayının yeni ölçümlerdeki başarısını sınar
# ve A2-A3 (tek hatta bias bulunan) hattın okunabilirliğini test eder.
#
# DENEYSEL KATSAYI HESABI:
# K_yeni = K_mevcut × (I_PZEM / I_SCT)
# Dört kararlı pencere katsayısı yaklaşık:
# 27.68 / 27.57 / 27.30 / 27.81
# Aritmetik ortalama: yaklaşık 27.59
#
# Bu katsayı henüz doğrulanmış nihai kalibrasyon değildir.
# Yalnızca ADS1115 fiziksel modül No.10 için deneme değeridir.
# Başka ADS1115 modüllerine aktarılmayacaktır.
# A2-A3 hattı için bias/devre farkına göre ayrı kalibrasyon
# gerekebilir.
#
# DONANIM / BAĞLANTILAR:
# ESP32D2 GPIO21 -> ADS1115 SDA
# ESP32D2 GPIO22 -> ADS1115 SCL
# ESP32D2 3.3V   -> ADS1115 VDD
# ESP32D2 GND    -> ADS1115 GND
# ADS1115 ADDR   -> GND (I2C 0x48)
# Hat 1 SCT013   -> ADS1115 A0-A1 (diferansiyel)
# Hat 2 SCT013   -> ADS1115 A2-A3 (diferansiyel, bir hatta bias var)
#
# ÖLÇÜM AYARLARI:
# ADS1115 modu       : Continuous
# Multiplexer        : A0_A1 ve A2_A3
# PGA                : 2.048 V
# Sample rate        : 860 SPS
# ct_clamp penceresi : 200 ms
# HA güncelleme      : 1 saniye
#
# ALT EŞİK:
# Kalibre edilmiş akım 5 mA altındaysa 0 A yayınlanır.
#
# BEKLENEN ÇIKTI:
# Home Assistant entity:
# - BERO Akim Sensoru (A)       [A0-A1]
# - BERO Akim Sensoru A2-A3 (A) [A2-A3]
#
# SÜRÜM KORUMA:
# Kod 0 ve V1.0 dosyaları değiştirilmez.
# V1.1, V1.0'dan ayrı yeni deneme sürümüdür.
# V1.0 ile V1.1 arasındaki işlevsel fark kalibrasyon
# katsayısının 30.66'dan 27.59'a alınması ve A2-A3 kanalının
# eklenmesidir.
#
# DOĞRULAMA DURUMU:
# V1.1 YAML hazırlanmıştır; A0-A1 ve A2-A3 ölçümlerinden gelen
# log/CSV verisine göre gerekirse V1.2 revizyonuna geçilecektir.
#
# GÜVENLİK:
# ADS1115 A0, A1, A2 ve A3 pinlerinin her biri GND-0.3 V ile
# VDD+0.3 V sınırları içinde kalmalıdır. Diferansiyel ölçüm
# ve tek hatta uygulanan bias bu mutlak pin gerilimi sınırlarını
# değiştirmez.
# ============================================================

esphome:
  name: esp32d2
  friendly_name: ESP32D2
  min_version: 2026.4.0
  name_add_mac_suffix: false

esp32:
  variant: esp32
  framework:
    type: esp-idf

logger:
  level: DEBUG

api:

ota:
  - platform: esphome

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

i2c:
  sda: GPIO21
  scl: GPIO22
  scan: true
  frequency: 400kHz

ads1115:
  - address: 0x48
    continuous_mode: true

sensor:
  # --- Kanal 1: A0 - A1 (Diferansiyel) ---
  - platform: ads1115
    multiplexer: A0_A1
    gain: 2.048
    sample_rate: 860
    id: ads_sct_a0_a1_raw
    internal: true

  - platform: ct_clamp
    sensor: ads_sct_a0_a1_raw
    name: "BERO Akim Sensoru"
    id: bero_akim_a0_a1
    sample_duration: 200ms
    update_interval: 1s
    accuracy_decimals: 3
    filters:
      - calibrate_linear:
          - 0.0 -> 0.0
          - 1.0 -> 27.59
      - lambda: |-
          if (x < 0.005) return 0.0;
          return x;

  # --- Kanal 2: A2 - A3 (Diferansiyel, tek hatta bias) ---
  - platform: ads1115
    multiplexer: A2_A3
    gain: 2.048
    sample_rate: 860
    id: ads_sct_a2_a3_raw
    internal: true

  - platform: ct_clamp
    sensor: ads_sct_a2_a3_raw
    name: "BERO Akim Sensoru A2-A3"
    id: bero_akim_a2_a3
    sample_duration: 200ms
    update_interval: 1s
    accuracy_decimals: 3
    filters:
      - calibrate_linear:
          - 0.0 -> 0.0
          - 1.0 -> 27.59
      - lambda: |-
          if (x < 0.005) return 0.0;
          return x;
```


## 11. Uzatılmış grafik değerlendirmesi ve ek deney planı (2026-11-22)

Kullanıcının paylaştığı yaklaşık 00:18–00:26 UTC grafiği, önceki 00:18–00:22 kesitini uzatmaktadır. Görselde:
- PZEM yaklaşık 1.16 A çevresinde düz görünmektedir.
- A0–A1 yaklaşık 0.97–1.22 A aralığında hareket etmektedir.
- A2–A3 yaklaşık 1.03–1.20 A aralığında hareket etmektedir.
- İki SCT kanalının dalga biçimleri aynı değildir; bazı bölümlerde benzer yönde geniş hareketler, bazı bölümlerde farklılaşan kısa hareketler görülmektedir.

Gemini tarafından önerilen kısa (yaklaşık 15–25 s) ve uzun (yaklaşık 60–90 s) salınım bileşenlerinin birleşerek modüle bir zarf oluşturduğu yorumu, **test edilecek bir hipotez** olarak kaydedilmiştir. Bu süreler ekran görüntüsünden çıkarılmış yaklaşık tahminlerdir; kesin periyot veya frekans olarak kabul edilmez. Ham CSV üzerinde zaman serisi analizi yapılmalıdır.

PZEM çizgisinin düz görünmesi gerçek yük akımının kesinlikle sabit olduğunu kanıtlamaz; PZEM'in örnekleme ve güncelleme karakteristiği bu karşılaştırmada dikkate alınacaktır.

### 11.1 Yükleri birbirinden ayırma

Mevcut birleşik yük koşulu Kettle 1 + 100 W ampuldür. Yük bileşenlerinin etkisini ayırmak için, aynı SCT yerleşimi ve aynı ölçüm ayarları korunarak aşağıdaki kayıtlar alınacaktır:

1. **Yalnız Kettle 1:** En az 3–5 dakika.
2. **Yalnız 100 W ampul:** En az 3–5 dakika.
3. **Kettle 1 + 100 W ampul:** En az 5 dakika; önceki birleşik yük kaydının tekrarı.

Her kayıtta PZEM, A0–A1 ve A2–A3 birlikte kaydedilecektir. Açılış ve kapanış geçişleri kararlı pencere istatistiklerinden ayrı tutulacaktır. Yüklerin gerçek çalışma gücü/akımı her kayıt için PZEM verisinden raporlanacaktır.

Bu karşılaştırma, salınımın yük kombinasyonuna bağlı olup olmadığını araştırır; tek başına ölçüm zincirinin hatalı olduğunu kanıtlamaz.

### 11.2 Besleme ve bias gözlemi

Ölçüm zincirinin besleme/bias kaynaklı etkisini araştırmak için aşağıdaki noktalar kontrol edilecektir:
- ADS1115 VDD: nominal 3.3 V.
- ESP32D2 beslemesi.
- A2–A3 hattında kullanılan bias düğümü: nominal yaklaşık 1.66 V.
- ESP32D2 ve ADS1115 arasındaki ortak GND bağlantısı.
- SDA/SCL bağlantılarının fiziksel sağlamlığı.

Multimetreyle bir dakikalık gözlem, yalnızca yavaş ve belirgin gerilim değişimlerini gösterebilir; küçük veya hızlı dalgalanmaları dışlayamaz. Daha hassas dalgalanma incelemesi için uygun ve güvenli prob bağlantısıyla osiloskop kullanılabilir. ADS1115 girişlerinin her birinin GND'ye göre mutlak gerilim sınırları korunacaktır.

### 11.3 Filtre denemesinin yeri

10 saniye civarında hareketli ortalama veya EMA, yalnızca teşhis kayıtları tamamlandıktan sonra ayrı bir deney kopyasında değerlendirilebilir. İlk referans ve tek-kanal/yük ayrıştırma kayıtlarında filtre eklenmeyecektir.

Filtreli deneme yapılırsa:
- Orijinal ham ölçüm ve filtresiz kayıt korunacak.
- Filtreli sonuç ham verinin yerine geçirilmeyecek.
- Tepe-çukur genliği, ortalama hata ve gecikme birlikte raporlanacak.
- Dalgalanmanın azalması, kaynağın giderildiği şeklinde yorumlanmayacak.

### 11.4 Ek başarı ölçütleri

Yük ayrıştırma ve besleme gözlemleri sonrasında:
- Her yük koşulunda iki SCT kanalının salınım genliği ve periyodu karşılaştırılmalı.
- Kısa ve uzun zaman ölçekleri ham zaman serisinde ayrı ayrı doğrulanmalı veya reddedilmeli.
- Yük tekilleştirildiğinde salınımın sürüp sürmediği raporlanmalı.
- Besleme/bias değişimleri ile SCT salınımları arasında zaman ilişkisi aranmalı.
- Filtre uygulanmadan önce olası fiziksel ve zamanlama kaynakları değerlendirilmiş olmalı.

**Sıra kararı:** Önce yükleri ayırma (Kettle 1, 100 W ampul, birleşik yük); ardından besleme/bias gözlemi; sonra YAML/ADS1115 zamanlama analizi; en son gerekirse ayrı filtre denemesi. Mevcut V1.1 YAML ve kalibrasyon katsayısı değiştirilmez.


## 12. Sonuç, ESP32 reset gözlemi ve deney kapanışı (2026-11-22)

**Kapanış durumu: KAPATILDI – belirti reset sonrasında kayboldu; kök neden doğrulanmadı.**

Kullanıcı, ESP32D2'yi resetledikten sonra daha önce A0–A1 ve A2–A3 akım okumalarında gözlenen yavaş salınımın durduğunu bildirdi. Bu, deneyin en önemli saha gözlemidir.

### 12.1 Gözlem ve yorum sınırı

- Reset öncesinde iki SCT kanalında PZEM'e kıyasla belirgin, birbirleriyle aynı periyotta olmayan yavaş salınımlar gözlenmişti.
- Kullanıcının bildirimine göre ESP32 resetinden sonra salınım durdu.
- Bu durum, sorunun en azından o çalışma oturumunda ESP32/ADS1115/ESPHome çalışma durumuyla ilişkili olabileceğini düşündürür.
- Ancak reset tek başına kök nedeni kanıtlamaz. Yeniden başlatma; yazılım durumunu, ADS1115 yapılandırmasını, I²C haberleşmesini ve ölçüm zamanlamasını yeniden başlatır. Hangi unsurun salınımı durdurduğu bu deneyde ayrıştırılmadı.
- Bu nedenle sonuç **“reset salınımı durdurdu”** olarak kaydedilir; **“ADS1115 hatası”, “I²C kilitlenmesi” veya “yazılım hatası bulundu”** şeklinde kesin hüküm verilmez.

### 12.2 Karma 1 – history (25).csv kaydı

Dosya: `history (25).csv`  
Kayıt aralığı: 2026-11-21 21:35:00–21:37:59 UTC  
Toplam satır: 510  
Yük: Karma 1 (kullanıcının yük tanımı; bu dosyada yük bileşenlerinin fiziksel ayrıntısı ayrıca doğrulanmadı).

CSV'den yeniden hesaplanan tüm kayıt istatistikleri:
| Entity | n | Ortalama | Std. sapma | Min–Max |
|---|---:|---:|---:|---:|
| PZEM akım | 35 | 1.3205 A | 0.0872 A | 0.842–1.413 A |
| A0–A1 | 181 | 1.2731 A | 0.0698 A | 1.1337–1.3968 A |
| A2–A3 | 181 | 1.3502 A | 0.0562 A | 1.2244–1.4652 A |
| PZEM güç | 36 | 303.95 W | 19.95 W | 192.9–324.9 W |
| PZEM gerilim | 32 | 230.11 V | 0.32 V | 229.5–230.7 V |

Bu kayıt kısa ve PZEM akım/güç değerleri değişken olduğundan, sabit yükte kalibrasyon noktası olarak kullanılmaz. Önceki hızlı değerlendirmelerde verilen eşleştirilmiş MAPE/katsayı değerleri bu kapanış raporunda yeni ve bağımsız kalibrasyon sonucu olarak kabul edilmemiştir.

CSV'deki BERO_EVT satırlarında BOOT_ID `90841376C63EB630E4979C465881880E` görünür. Bu, dosyanın olay protokolünde görülen kimliktir; tek başına resetin tam zamanını veya reset öncesi/sonrası salınım genliğini kanıtlamaz. Reset sonrası durma bilgisi kullanıcının saha gözlemidir.

### 12.3 Deneyden çıkarılan kalıcı işletim dersi

1. İki SCT kanalında açıklanamayan yavaş salınım görüldüğünde ilk müdahale olarak filtre eklenmeyecek ve örnekleme ayarları değiştirilmeden önce mevcut durum kaydedilecek.
2. Zaman damgalı ham CSV, PZEM ve iki SCT kanalı birlikte saklanacak.
3. Mevcut durum kaydedildikten sonra ESP32D2 kontrollü biçimde yeniden başlatılabilir.
4. Reset sonrası salınımın kaybolup kaybolmadığı aynı yük ve aynı bağlantı koşullarında yeniden gözlenecek.
5. Reset sonrası düzelme, kök neden analizi yerine geçmez. Tekrarlanabilirlik için reset öncesi/sonrası karşılaştırmalı kayıt alınmalıdır.
6. V1.1 YAML, 860 SPS, 200 ms pencere, 1 s güncelleme, K=27.59 ve mevcut filtreler bu deney kapsamında değiştirilmedi.

### 12.4 Son karar

- Deney kapatıldı.
- Gözlenen salınım ESP32 reseti sonrasında kullanıcı tarafından durmuş olarak bildirildi.
- Kök neden belirlenmedi; yazılım/ADC/I²C/besleme/ölçüm zamanlaması hipotezleri kanıtlanmış sayılmıyor.
- Yükleri ayırma ve filtre denemeleri bu deneyin kapsamında yapılmadı; belirti resetle kaybolduğu için bu deneyde devam ettirilmeyecek.
- Aynı belirti yeniden oluşursa bu kayıt referans alınarak yeni bir tekrar/arıza incelemesi açılacak.
- Kalibrasyon katsayıları ve çalışan YAML değiştirilmedi.

**Deney sonucu:** Reset, salınımı durdurmak için işe yarayan saha müdahalesi olarak kaydedildi. Bu tecrübe BERO için işletim/teşhis notudur; teknik kök neden sonucu değildir.
