# E00A sonuç kaydı

**Durum:** SCT bağlı olmayan bias-only Vmid alt adımı KAPATILDI (2026-10-30 log analizi). E00A bütünü AÇIK: 3.3 V bölücü koşulu ve ham CSV/zaman grafiği eksik.

| Koşul | Multimetre DC (V) | Hedef hız (S/s) | Kayıt süresi (s) | Örnek sayısı | Yaklaşık gerçek hız (S/s) | Ortalama ADC | Min | Max | Tepe-tepe | Std. sapma | Ham dosya |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Bias trafosu 3,3 V (ayrı 10k/10k ölçüm bölücüsü planı; ADC henüz bağlanmadı) | **3,31** | Henüz belirlenmedi | **30 (plan)** | — | — | — | — | — | — | — | data/raw/E00A/bias_trafo_3v3.csv |
| Bias Vmid (breadboard orta noktası; doğrudan ADC koşulu henüz yapılmadı) | **1,65** | Henüz belirlenmedi | **30 (plan)** | — | — | — | — | — | — | — | — | data/raw/E00A/bias_vmid.csv |

## Karşılaştırma
- ADC ham değerleri ve analogReadMilliVolts farkı:
- Multimetre ile ADC mV tahmini arasındaki fark:
- İki noktanın zaman içindeki değişimi:
- Örnek sayısı / gerçekleşen hız değerlendirmesi:
- Sonraki adım:

## HEDEF / LOG / SONUÇ

### HEDEF
Bias trafosunun L78L33 3,3 V çıkışını ve bias Vmid noktasını ayrı ayrı ADC ile okumak; ham değer, mV tahmini ve kısa dönem değişimi karşılaştırmak.

### LOG
- 2026-10-30 — Kullanıcı bildirimi: bias trafosunun L78L33 DC çıkışı multimetreyle 3,31 V ölçüldü. Kanıt türü: KULLANICI BİLDİRİMİ; multimetre marka/modeli, fotoğraf ve bağımsız tekrar bu kayıtta yok.
- 2026-10-30 — Kullanıcı bildirimi: bias breadboard üzerindeki Vmid/orta nokta multimetreyle 1,65 V okundu. Kanıt türü: KULLANICI BİLDİRİMİ; bu okuma breadboard üzerindeki bias orta noktasına aittir, ESP32 ADC ölçümü değildir.
- 30 saniye, her ADC koşulu için planlanan gözlem süresidir; henüz gerçekleştirilmedi.
- Gerçek ESP32 kart modeli ve GPIO:
- Bias trafosu fiziksel bileşen/bağlantı kontrolü:
- Ölçüm bölücüsünün direnç değerleri:
- Ortak GND bağlantısı:
- Firmware sürümü/commit:
- Her koşulun multimetre ölçümü, süresi, örnek sayısı, istatistikleri ve ham kayıt yolu: L78L33 çıkışı 3,31 V ve breadboard Vmid orta noktası 1,65 V (ikisi de kullanıcı multimetre bildirimi); ADC kayıtları henüz yok.
- Yapılmayan kontroller:

### SONUÇ
- İlk referanslar: L78L33 çıkışı 3,31 V; breadboard bias orta noktası 1,65 V olarak multimetreyle raporlandı. Bunlar iki ayrı DC noktasının kullanıcı tarafından bildirilen multimetre okumalarıdır; ESP32 ADC ölçümü değildir ve 30 saniyelik kararlılığı göstermez.
- Verinin desteklediği yorum:
- Ölçüm sınırlamaları:
- Sonraki adım:

Ölçüm yapılmadan sonuç veya kabul kararı yazılmaz. Ham CSV dosyaları varsayılan olarak Git'e eklenmez.


## 2026-10-30 — ESP32D2 ADC firmware ilk çalıştırma bildirimi

### HEDEF
GPIO34 ve GPIO35 üzerinden iki ayrı ESP32 ADC kanalını kullanarak aynı deney girişini iki farklı çıktı türüyle gözlemek: GPIO34 ham ADC sayısı, GPIO35 kalibrasyonlu voltaj tahmini.

### LOG
- Kullanıcı, ESPHome yapılandırmasının **derlendiğini ve çalıştığını** bildirdi (KULLANICI RAPORU).
- Tam yapılandırma depoya eklendi: [firmware/esp32d2-e00a-adc.yaml](firmware/esp32d2-e00a-adc.yaml).
- Cihaz adı: esp32d2; framework: ESP-IDF; GPIO34: ADC raw; GPIO35: ADC voltaj; attenuation: 12 dB; sensör güncelleme aralığı: 1 s.
- Bu kayıt anında derleme çıktısı/cihaz logu henüz paylaşılmadı; ADC sayısal değerleri, fiziksel pin bağlantıları, gözlem süresi ve ham CSV mevcut değil.
- 1 saniyelik sensör güncellemesi, 30 saniyelik ham ADC kaydı veya 2 kS/s edinim olarak yorumlanmaz.

### SONUÇ
- **Kod durumu:** Kullanıcı bildirimiyle derlendi ve çalıştı.
- **Ölçüm durumu:** Henüz yorumlanmadı. GPIO34 ham sayısı ile GPIO35 voltaj tahmininin gerçek değerleri ve kararlılığı log geldikten sonra değerlendirilecek.
- Bu bildirim tek başına ADC doğruluğunu, Vmid bağlantısını veya 30 saniyelik deney kabul ölçütlerini kanıtlamaz.
- **Sonraki adım:** Kullanıcı ESPHome/cihaz logunu ve Home Assistant'ta görülen iki sensörün değerlerini paylaşacak; değerlendirme sonrasında bu dosyaya eklenecek.


## 2026-10-30 — E00A-S01 GND referans testi

### HEDEF
SCT bağlı değilken GPIO34 ve GPIO35 girişlerini GND'ye referanslayıp uzun logda kararlılığı görmek; floating giriş davranışını ayırmak.

### LOG
- Kaynak: Kullanıcının paylaştığı `Yapıştırılan metin(8).txt`; ESPHome 2026.9.1, ESP32 rev3.1.
- Kullanıcı bildirimi: GPIO34 ve GPIO35 GND'ye bağlandı.
- GPIO34 raw: 14:49:11–14:52:24 arasında görünen her kayıtta 0 count.
- GPIO35 calibrated voltage: ilk bölümde 0.181–0.195 V, 14:49:24'te 2.405 V sıçrama, sonra düşüş; yaklaşık 14:49:29–14:52:24 arasında 0.142 V sabit.
- Kararlı bölüm yaklaşık 175 saniye; sensör bağlı değil.
- ADC Handle Init, Config, Calibration ve Overall Init her iki kanalda OK.
- Sensör güncelleme aralığı 1 s; bu yüksek hızlı ham örnekleme değildir.
- GPIO34 ve GPIO35 ayrı fiziksel ADC kanallarıdır; aynı analog örneğin count/volt karşılığı değildir.
- Ayrıntılı analiz: [E00A-S01 raporu](reports/E00A-S01-gnd-reference-stability.md).

### SONUÇ
GND'ye referanslama ile giriş kararlılığı gözlendi. Önceki açık giriş dalgalanması floating giriş teşhisini destekler. GPIO35'in GND'de 0.142 V göstermesi ADC voltaj tabanı/ofseti açısından açık sorudur; neden kesinleşmedi. Bu kayıt ADC'nin tam aralık doğruluğunu, 1.65 V davranışını veya SCT ölçümünü kanıtlamaz.

### Elektriksel karar adayı
Yazılımsal sıfırlama yerine ADC girişinin sensör yokken de tanımlı DC seviyede kalması hedeflenir. Jack/CT topolojisi doğrulandıktan sonra ADC düğümüne Vmid'e karşı 47–100 kΩ yüksek değerli bias direnci prototip olarak değerlendirilecek. Bu değer aralığı henüz doğrulanmış tasarım/BOM değildir. İlk sonraki test: tek kanalda Vmid bias, multimetreyle DC doğrulama, 60 saniye log.


## Düzeltme — GPIO34 bağlı değil; GPIO35 Vmid logu (2026-10-30)

Kullanıcı düzeltmesi: GPIO34 count kanalı bağlı değildir. GPIO34'ün 0 count değeri fiziksel GND testi kanıtı değildir; yorum dışıdır.

Yeni logda GPIO35 ADC voltajı 14:57:02'de 1.678 V ile başlıyor; ilk bölümde yaklaşık 1.651–1.744 V arasında değişiyor, ardından belirgin biçimde düşerek 14:57:26'da 0.699 V'a ulaşıyor. Kullanıcı Vmid'in multimetrede sabit yaklaşık 1.65 V DC olduğunu bildiriyor. ADC logu ile multimetre arasında uyuşmazlık vardır. Kök neden belirlenmedi; ADC arızası sonucu çıkarılamaz.

Sonraki ayırıcı test: GPIO34 yorum dışı. Yalnız GPIO35 bağlı olacak. Multimetre siyah probu ESP32 GND, kırmızı probu doğrudan GPIO35 pininde tutulurken aynı anda log alınacak; Vmid düğümü ayrıca ölçülecek. Kablo sürekliliği ve ortak GND doğrulanmadan direnç veya yazılım filtresi eklenmeyecek.



## 2026-10-30 — E00A Adım 2: GPIO35 voltaj sıfır noktası düzeltmesi

### HEDEF
GPIO35 ADC voltaj okumasında giriş GND seviyesindeyken yazılım çıktısını 0.000 V'a indirmek. Önceki GND referans logunda görülen kararlı 0.142 V tabanını geçici ofset olarak çıkarmak.

### LOG
- Firmware: `firmware/esp32d2-e00a-adc.yaml`; commit: `9eae26000a1dc460191bec68581cec0ac9ab9397`.
- GPIO34 ham ADC sayımı olarak korunmuştur.
- GPIO35 voltaj tahmini `raw: false` olarak korunmuş; filtrede `max(0, x - 0.142)` uygulanmıştır.
- Kullanıcı, güncellenen kodun derlendiğini bildirdi (KULLANICI RAPORU).
- Derleme sonrası cihaz logu ve GND girişinde yeni düzeltilmiş sensör değeri henüz paylaşılmadı.

### SONUÇ
Kod derleme aşaması kullanıcı bildirimiyle başarılıdır. Amaç, sıfır girişte yazılım çıktısını sıfırlamaktır; fiziksel sıfır okuması henüz doğrulanmamıştır. 0.142 V yalnız önceki gözlemden alınan geçici ofsettir; tam ADC kalibrasyonu veya farklı gerilimlerde doğruluk kanıtı değildir.

### Sonraki adım
GPIO35'i GND'ye bağlı tutarak güncel firmware logunu gözle; düzeltilmiş voltajın 0.000 V olup olmadığını kaydet. Ardından bilinen Vmid geriliminde (multimetreyle eşzamanlı) ofsetin ölçümü bozup bozmadığını değerlendir.



### LOG — Sifir noktasi kontrolu (2026-10-30, kullanici logu)

- Kaynak: Kullanıcının paylaştığı `Yapıştırılan metin(10).txt`; ESPHome 2026.9.1.
- Cihaz: ESP32 rev3.1; cihaz uygulama derleme zamanı logda 2026-10-30 15:09:22 +0300.
- GPIO35 düzeltilmiş voltaj: 15:13:08.379–15:13:56.381 arasında 49 kayıt; tüm kayıtlar `0.000 V`.
- Gözlenen süre: ilk ve son kayıt zamanları arasında yaklaşık 48 saniye.
- GPIO34: 48 kayıtta `0 count`; önceki kullanıcı düzeltmesine göre GPIO34 fiziksel olarak bağlı olmadığından bu kanalın değerleri deney sonucu olarak yorumlanmaz.
- Logda GPIO34 ve GPIO35 ADC başlatma/config/calibration durumları OK; iki sensörün güncelleme aralığı 1 saniye.
- Kullanıcı, bu aşamada sıfır voltaj hedefinin sağlandığını ve kodu değiştirmeden bias trafosuna enerji vererek aynı log oturumunda devam edeceğini bildirdi.

### SONUÇ
**Adım 2'nin yazılım sıfır gösterimi hedefi sağlandı (KULLANICI LOGU):** GPIO35 düzeltilmiş sensörü yaklaşık 48 saniye boyunca kesintisiz görünen 49 kaydın tamamında 0.000 V yayınladı. Bu, mevcut filtre ve mevcut GND test koşulunda hedeflenen sıfır çıktısını gösterir. GPIO34 verisi bağlı olmadığı için dışarıda bırakıldı.

**Açık devam:** Kod değiştirilmeden aynı log oturumunda bias trafosuna enerji verilecek. Sonraki log bölümünde GPIO35'in düzeltilmiş voltajı ve mümkünse eşzamanlı multimetre Vmid değeri kaydedilecek. Bu kayıt Adım 2'nin sıfır kontrolünden sonraki bias/Vmid kontrolüdür; henüz sonucu yoktur.


## 2026-10-30 — E00A Adım 2 bias açık logu ve sıfırlama kararının geri alınması

### HEDEF
GND koşulunda 0.142 V ofsetle 0.000 V çıktısı elde etme denemesinin, bias Vmid uygulandığında gerçek DC seviyeyi bozup bozmadığını değerlendirmek.

### LOG
- Kaynak: Kullanıcının paylaştığı `Yapıştırılan metin(20261030-121627).txt`; ESPHome 2026.9.1; ESP32 rev3.1.
- Cihaz logunda firmware derleme zamanı 2026-10-30 15:09:22 +0300; GPIO34 ve GPIO35 ADC init/config/calibration OK; güncelleme aralığı 1 s.
- Bias öncesi GPIO35, 15:13:08.379–15:14:47.400 arasında 0.000 V yayınladı. Bu, 0.142 V yazılım filtresinin çıktısıdır; ham ADC'nin sıfır olduğunu göstermez.
- Bias geçişi: 15:14:48.371'de GPIO35 1.158 V; 15:14:49.372'de 1.511 V.
- Kararlı bölüm: 15:14:50.392–15:16:14.378 arasında GPIO35 yaklaşık 1.509–1.544 V. Bu bölümde 85 örneğin ortalaması yaklaşık 1.525 V, standart sapması yaklaşık 0.0069 V olarak hesaplandı.
- GPIO34 sayımları bias geçişinden sonra yaklaşık 1840–1875 count görünür; kullanıcı GPIO34'ün bağlı olmadığını belirttiği için bu kanal yorum dışıdır.
- Kullanıcı multimetrede Vmid'i yaklaşık 1.65 V, daha net olarak 1.654 V bildirdi (KULLANICI BİLDİRİMİ).
- Hesap: filtre tarafından çıkarılan 0.142 V geri eklendiğinde tahmini filtresiz ortalama yaklaşık 1.667 V olur. Multimetre bildirimiyle fark yaklaşık +0.013 V'tur. Bu değer filtreli logdan türetilmiş hesaptır; doğrudan kaydedilmiş ham voltaj değildir.

### SONUÇ
- 0.142 V sabit ofset GND koşulunda ekranda 0.000 V elde etti; ancak bias Vmid koşulunda gerçek DC seviyeyi de 0.142 V azalttı.
- Sıfır gösterme hedefi, gerçek voltajı olduğu gibi okuma hedefiyle çelişti. Kullanıcının kararıyla yazılımsal sıfırlama kaldırılıyor.
- Bu deney noktasında filtresiz ADC voltaj tahmini yaklaşık 1.667 V hesaplanır ve kullanıcı multimetre bildirimi olan 1.654 V'a yaklaşık 13 mV farkla yakındır. Bu tek nokta tüm ADC aralığında doğruluk/lineerlik kanıtı değildir.
- GND'de görülen 0.142 V artık gizlenmeyecek; ölçüm olarak korunacak.
- Sonraki adım: ofsetsiz firmware'i derlemek/cihaza yüklemek ve aynı Vmid noktasında yeni log ile multimetre karşılaştırmasını tekrarlamak.


## 2026-10-30 — E00A bias-only / SCT bağlı değil: RAW ve voltaj ilk karşılaştırma logu

### HEDEF
SCT bağlamadan bias Vmid noktasını ESP32D2'nin GPIO34 RAW ve GPIO35 ADC voltaj kanallarında gözlemek; multimetre bildirimi olan 1.654 V ile karşılaştırmak. Sonraki uzun logda RAW ve voltaj serilerinin korelasyonunu incelemek için başlangıç gözlemi oluşturmak.

### LOG
- Kaynak: Kullanıcının paylaştığı `Yapıştırılan metin(20261030-123911).txt`; ESPHome 2026.9.1; ESP32 rev3.1; cihaz `esp32d2`; log bağlantısı 192.168.0.66.
- ADC GPIO34 (ADC1_CH6) ve GPIO35 (ADC1_CH7) başlatma, konfigürasyon ve kalibrasyon durumları OK; iki sensörün güncelleme aralığı 1 s.
- Kullanıcının multimetre bildirimi: Vmid = **1.654 V**. Bu değer kullanıcı raporudur; bu logda multimetre ölçümünün zaman damgası yoktur.
- İlk bölümde GPIO34 RAW = 0 count ve GPIO35 = 0.142 V görülüyor. Ardından GPIO34 yaklaşık 1837–1871 count bölgesine geçiyor; GPIO35 de yaklaşık 1.65–1.68 V bandına oturuyor.
- Kararlı görünen bölümde (yaklaşık 15:37:46–15:39:03): GPIO34 RAW gözlemi yaklaşık 1829–1871 count; RAW nominal voltaj tahmini yaklaşık 1.385–1.416 V; GPIO35 ADC voltajı yaklaşık 1.650–1.679 V; fark sensörü yaklaşık +0.250…+0.294 V.
- RAW nominal tahmini firmware formülüdür: `count × 3.1 / 4095`; kalibre edilmiş voltaj değildir.
- Logda iki kanalın yayınları aynı saniyede ve aynı anda gerçekleşmiyor; GPIO34 ve GPIO35 ayrı ADC kanallarıdır. Bu nedenle bu kısa kayıt tek başına örnek-örnek korelasyon katsayısı veya tam eşzamanlılık kanıtı değildir.
- Logda trafo enerjilendirme anı ayrıca işaretlenmediğinden, ilk geçişi belirli bir trafo ON/OFF zamanına atamıyoruz. Kullanıcının gözlemi: kondansatörlerle birlikte değerler belirgin biçimde oturuyor.

### SONUÇ
- Bias-only gözleminde GPIO35 voltaj okuması kararlı bölümde kullanıcının bildirdiği 1.654 V multimetre değerine yakındır (yaklaşık 1.650–1.679 V).
- Aynı kararlı bölümde GPIO34 RAW'dan nominal hesaplanan voltaj yaklaşık 1.4 V'tur ve GPIO35'ten yaklaşık 0.27 V düşüktür. Bu fark henüz nedenlendirilmemiştir; RAW dönüşüm katsayısı nominaldir ve iki kanal ayrı ADC okumalarıdır.
- Bu test SCT davranışını, akım ölçümünü veya bias devresinin SCT yükü altındaki davranışını göstermez. Yalnızca SCT'siz bias/ADC zincirinin ilk karşılaştırmasıdır.
- Kullanıcının sonraki adımı: daha uzun RAW + voltaj logu paylaşmak. O kayıtta zaman serilerini eşleştirip korelasyon (Pearson ve/veya Spearman), eğim/kesişim, fark ve kararlı/geçiş bölümlerini inceleyeceğiz. Ham logdaki örnekleme zamanları korunmalı; farklı zaman damgaları körlemesine satır satır eşleştirilmeyecek.
- E00A tamamlanmadı; bu kayıt ön gözlemdir.


## 2026-10-30 — SCT bağlı değil: bias-only ADC gözlemi kapatıldı

### HEDEF
SCT bağlı değilken bias Vmid noktasındaki ESP32 ADC ölçüm zincirinin taban davranışını gözlemek; GPIO34 RAW sayımı ile GPIO35 voltaj çıktısını uzun log üzerinden zaman damgalarıyla karşılaştırmak. Bu adımın kapanış ölçütü: logun analiz edilmesi, geçersiz RAW sıfırlarının eşleştirmeden çıkarılması, gözlenen dalgalanmanın sınırlarının belirlenmesi ve sonraki deney koşulunun açıkça tanımlanması.

### LOG
- Kaynak dosya: kullanıcının yüklediği `esp32d2-logs.txt` (ESPHome 2026.9.1; cihaz `esp32d2`; 2026-10-30).
- GPIO34 RAW, GPIO34 nominal voltaj tahmini, GPIO35 ADC voltajı ve fark sensörü için 618'er kayıt bulundu.
- Kullanıcı talimatı: **RAW sıfırları eşleme**. GPIO34'ün ilk 14 adet 0 count kaydı geçersiz/bağlantı oturmamış başlangıç verisi olarak eşleştirmeye alınmadı. İlk geçişteki 15:37:45.448 RAW=1837 kaydıyla aynı ana ait olmayan 15:37:45.187 tarihli 0.000 V nominal tahmin de stale/önceki güncelleme olduğundan çıkarıldı.
- Zaman damgası ile eşleştirilmiş geçerli çiftler: **603**; aralık 15:37:46.199–15:47:48.186. GPIO34 ve GPIO35 ayrı ADC kanallarıdır; yayınlar tam eşzamanlı değildir.
- GPIO34 RAW count: ortalama **1846.80**, std. sapma **6.97 count**, min **1813**, max **1871**.
- GPIO34 nominal voltaj tahmini: ortalama **1.398007 V**, std. sapma **5.303 mV**, min **1.372 V**, max **1.416 V**. Formül `count × 3.1 / 4095`; kalibre edilmiş voltaj değildir.
- GPIO35 ADC voltajı: ortalama **1.665138 V**, std. sapma **6.474 mV**, min **1.644 V**, max **1.683 V**.
- GPIO35 − RAW nominal tahmini farkı: ortalama **+0.267131 V**, std. sapma **8.444 mV**, min **+0.246 V**, max **+0.296 V**.
- Aynı zamanlı eşleştirilmiş nominal RAW tahmini ile GPIO35 arasında Pearson **r = −0.0201** (p≈0.623), Spearman **ρ = −0.0200** (p≈0.625); anlamlı birlikte değişim görülmedi. ±3 örnek gecikme taramasında da anlamlı ilişki ortaya çıkmadı.
- Kullanıcının multimetre Vmid bildirimi **1.654 V**'tur; bu ölçümün logla eşzamanlı zaman damgası yoktur.
- Bu kayıt bias-only koşuludur; SCT bağlı değildir. Logda trafonun enerjilendirme anı ayrıca işaretlenmedi. Kullanıcı kondansatörler takılıyken değerlerin oturduğunu gözlemlediğini bildirdi.

### SONUÇ
- **ÖLÇÜLDÜ (bu kurulum ve bu log için):** GPIO35 voltaj serisinin standart sapması yaklaşık **6.5 mV**; GPIO34 RAW sayımının standart sapması yaklaşık **7 count**. Bunlar SCT'siz bias/ADC ölçüm zincirinde gözlenen dalgalanma seviyeleridir.
- Bu değerler yalnız ADC'nin kendi taban gürültüsü olarak adlandırılamaz. ADC, bias beslemesi, kablolama, ortak toprak ve ölçüm zincirinin tüm etkileri ayrıştırılmadı. Bu nedenle sonuç **“SCT'siz ölçüm zincirinin gözlenen taban dalgalanması”** olarak kaydedilir; ADC'nin tek başına gürültü spesifikasyonu değildir.
- RAW nominal voltaj tahmini GPIO35'ten ortalama yaklaşık **267 mV** düşük kalmıştır. Formül kalibre değildir; kanallar ayrıdır ve örnekler tam eşzamanlı değildir. Farkın nedeni bu deneyde belirlenmedi.
- Yaklaşık sabit bias seviyesinde iki kanalın dalgalanmaları korelasyon göstermemiştir. Bu, SCT arızası veya ADC arızası kanıtı değildir; SCT zaten bağlı değildir ve sabit DC koşulundaki küçük değişimler kanal gürültüsü/ölçüm farkları tarafından baskılanabilir.
- **KAPANIŞ:** SCT bağlı olmayan bias-only gözlem ve bu logun ilk karşılaştırma/kararlılık analizi kapatıldı. Bu kapanış yalnız bu alt koşula aittir; E00A'nın tamamı kapatılmadı.
- **AÇIK KALAN E00A:** L78L33 3.3 V çıkışının ayrı 10k/10k ölçüm bölücüsüyle ADC gözlemi, ham yüksek hızlı ADC örneklerinin CSV olarak kaydı ve zaman grafiği bu logla sağlanmış değildir. E00A genel deneyi bu nedenle açık kalır.
- **SONRAKİ ADIM:** SCT bağlanmadan yapılan bu taban kaydı referans olarak korunacak. Sonraki ayrı koşul, SCT'nin ADC/bias girişine bağlanması ve ölçülen hatta akım yokken aynı ölçüm zincirinin gözlenmesidir. Bağlantı topolojisi ve pin güvenliği önceden kontrol edilecek; yazılımsal offset/filtre eklenmeyecek. Daha sonra SCT'li yüksüz sonuç bu tabanla karşılaştırılacaktır.

**Veri işleme kuralı:** Kullanıcının açık talimatı gereği, RAW count=0 başlangıç kayıtları eşleştirme/korelasyon analizine alınmaz; geçerli sıfır olayı olduğu ayrıca doğrulanmadıkça bu kayıtlar eksik/geçersiz başlangıç gözlemi sayılır.
