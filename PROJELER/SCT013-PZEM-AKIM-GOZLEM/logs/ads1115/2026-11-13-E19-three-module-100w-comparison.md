# E19 — Üç modül ortak 100 W yük gözlemi

Tarih: 2026-11-13  
Kaynak: Kullanıcının aynı oturumda sağladığı ESP32D2, Modül 3 WROOM ve Modül 2 ESP32D1 cihaz logları.  
Kanıt türü: **ÖLÇÜLDÜ / LOG İLE DESTEKLENDİ**; istatistikler ortak zaman penceresindeki yayınlardan hesaplandı.

## 1. Kayıt kapsamı

- ESP32D2 / ADS1115: 17:48:27–17:51:13
- Modül 3 / PZEM: 17:41:56–17:51:27
- Modül 2 / ESP32D1: 17:42:42–17:51:35
- Üç kaydın ortak kesişimi: **17:48:27–17:51:13 (+03:00)**.
- PZEM bu oturumda yaklaşık 107.2–107.7 W gösteriyor. Bu, nominal 100 W akkor yükün logdaki gerçek güç aralığıdır.

## 2. Ortak zaman aralığı istatistikleri

| Ölçüm yolu | Örnek sayısı | Ortalama akım | Örnek standart sapması | Min–maks |
|---|---:|---:|---:|---:|
| ESP32D2 / ADS1115 + ct_clamp | 84 | 0.469881 A | 0.001091 A | 0.46–0.47 A |
| Modül 3 / PZEM | 34 | 0.469882 A | 0.000537 A | 0.469–0.471 A |
| Modül 2 / ESP32D1 CH1-1T | 167 | 0.434240 A | 0.013698 A | 0.410–0.498 A |

- ESP32D2 sensörünün accuracy_decimals: 2 ayarı nedeniyle yayımlanan akım 0.01 A çözünürlükte görünür. Bu nedenle ADS1115'in 0.001 A seviyesinde kararlılığı kanıtlanmış sayılmaz; görünen standart sapma yayın çözünürlüğünden etkilenir.
- ADS1115 ct_clamp debug satırları çoğunlukla 173–177 farklı örnek / 200 ms pencere (865–885 SPS) bildirir. Bu, ADS1115'in gerçek ADC dönüşüm hızının 860 SPS olduğunu tek başına kanıtlamaz.
- PZEM ortalamasına göre ADS1115 yayımlanan akım ortalaması farkı yaklaşık -0.0003% (yuvarlanmış sensör yayınlarından hesaplanmıştır).
- PZEM ortalamasına göre ESP32D1 CH1 ortalaması farkı yaklaşık -7.59%. Bu yalnız bu oturum/kanal/yük penceresine ait gözlemsel farktır; genellenebilir kalibrasyon sonucu değildir.

## 3. ESP32D2 ADS1115 yapılandırma uyuşmazlığı

Açılış logu:
- I2C: GPIO21 SDA, GPIO22 SCL, 400 kHz; 0x48 bulundu.
- ADS1115: A0_A1 (Multiplexer 0), Gain 2, Sample rate 7.
- ct_clamp: sample duration 0.20 s, update interval 2.000 s.

Depodaki E19 YAML ise gain: 2.048 ve sample_rate: 860 bekliyor. Cihaz logunda "Loaded validated config cache for esp32d2.yaml" yazıyor; bu, depodaki firmware/experiments/esp32d2-ads1115-ct-clamp.yaml dosyasının derlenip cihaza yüklendiğini kanıtlamıyor.

Bu nedenle 860 SPS yapılandırma doğrulanmış değildir. ADS1115 açılış logundaki 7 SPS ile ct_clamp'in 865–885 SPS sayacı arasında açıklanması gereken örnek yenilenme uyumsuzluğu vardır. ADS ham gerilim yayınları bu kesitte yalnız iki kez görünür: -0.021375 V (17:49:22.115) ve -0.023312 V (17:50:22.116). Bunlar tek başına RMS veya kalibrasyon hesabına yeterli değildir. Bu logda I2C timeout uyarısı görülmedi; önceki ayrı oturumdaki timeout/106 ms uyarısı bu loga taşınmamıştır.

## 4. SSR olayları ve fiziksel yük durumu

Ortak zaman aralığında BOOT_ID ED9BD7889F614407255CB180A354D32F ile görülen olaylar:
- EVENT_ID 158 — OFF, 17:48:56
- EVENT_ID 159 — ON, 17:49:16
- EVENT_ID 160 — OFF, 17:49:56
- EVENT_ID 161 — ON, 17:50:16
- EVENT_ID 162 — OFF, 17:50:56

Modül 2 ve ESP32D2 bu olayları alıp HA text sensor'larına yayımlıyor. ESP32D2 logu 17:51:13'te bittiği için 17:51:16 EVENT_ID 163 bu dosyada yer almıyor.

Modül 3 logunda ON için GPIO_ON_CONFIRMED, OFF için tekrarlanan GPIO_OFF_READBACK_MISMATCH uyarıları var (tam Modül 3 logunda 9 OFF mismatch uyarısı). PZEM akımı OFF olaylarından sonra da yaklaşık 0.470 A seviyesinde kalıyor.

**Yorum:** Olay mesajı aktarımı logla destekleniyor; SSR OFF komutunun fiziksel yükü kestiği doğrulanmıyor. Bu nedenle olaylar doğrulanmış fiziksel ON/OFF yük etiketi olarak kullanılmamalıdır.

## 5. Sonuç

1. Üç cihaz aynı oturumda veri üretmiş ve ortak zaman aralığı oluşturulabilmiştir.
2. ADS1115 yayımlanan akım ortalaması PZEM ortalamasına çok yakındır; ancak açılış logunda 7 SPS görünür ve depodaki 860 SPS YAML ile çalışan yapılandırmanın eşleştiği kanıtlanmamıştır.
3. ESP32D1 CH1-1T ortalaması PZEM'den yaklaşık %7.59 düşüktür ve dağılımı daha geniştir. Bu sonuç tek oturuma aittir; katsayı değişikliği veya diğer SCT yapılarına genelleme gerekçesi değildir.
4. SSR olayları taşınmıştır; fiziksel OFF doğrulanmamıştır.
5. **Katsayı değiştirilmedi.** ESP32D1 K=24.22 korunur; ADS1115 için yeni katsayı belirlenmedi. ±%4 kabul başarısı ilan edilmedi.

## 6. Açık işler

- ESP32D2'nin hangi YAML dosyasından derlenip yüklendiğini doğrula.
- Gain ve sample rate açılış logunu hedeflenen YAML ile eşleştir; 860 SPS yapılandırmasını ayrı derleme/OTA/çalışma kanıtıyla doğrula.
- ADS1115 ham gerilim yenilenmesini ct_clamp farklı örnek sayacıyla açıklığa kavuştur.
- SSR GPIO OFF readback uyuşmazlığını ve fiziksel yük kesilmesini ayrı test et.
- Fiziksel ON/OFF doğrulanmış ve ölçüm yapılandırması sabitlenmiş kararlı yük oturumundan sonra katsayı değerlendir.

## 7. Temsilî ham log satırları

ESP32D2:
```text
[17:48:27.360][C][i2c:093]:   Frequency: 400000 Hz
[17:48:27.379][C][i2c:119]: Found device at address 0x48
[17:48:27.510][C][ads1115.sensor:023]:     Gain: 2
[17:48:27.510][C][ads1115.sensor:023]:     Sample rate: 7
[17:48:27.876][D][ct_clamp:040]: 'BERO Akim Sensoru' - Raw AC Value: 0.017A after 176 different samples (880 SPS)
[17:48:27.989][S][sensor]: 'BERO Akim Sensoru' >> 0.47 A
[17:49:22.115][D][ads1115.sensor:016]: 'ads_sct_raw': Got Voltage=-0.021375V
```

Modül 3 / SSR:
```text
[17:48:27.907][S][sensor]: 'BERO PZEM Akım' >> 0.470 A
[17:48:56.145][W][bero_ssr:394]: GPIO_OFF_READBACK_MISMATCH
[17:49:16.208][I][bero_ssr:413]: GPIO_ON_CONFIRMED
```

Modül 2:
```text
[17:48:27.876][D][ct_clamp:040]: 'BERO Mod2 CH1-1T Faz Akim' - Raw AC Value: 0.018A after 2891 different samples (14455 SPS)
[17:48:27.142][S][sensor]: 'BERO Mod2 CH1-1T Faz Akim' >> 0.437 A
```

Not: Temsilî satırlar kullanıcı tarafından sağlanan tam cihaz loglarından seçilmiştir. Tam ham log dosyaları ayrı Git dosyaları olarak saklanmadı; bu rapor istatistikleri, yapılandırma satırlarını, olayları ve yorumları saklar.


## 8. Sonradan yapılan teknik yorum ve düzeltme (2026-11-13)

Bu bölüm, yukarıdaki ilk rapor yorumunu silmeden düzeltir. Kullanıcı tarafından paylaşılan ek log değerlendirmesi ve kod incelemesi dikkate alınmıştır.

### Örnekleme hızı — önceki yorum düzeltildi
- Açılış logundaki `Sample rate: 7`, 7 SPS anlamına gelen fiziksel hız değeri olarak yorumlanmamalıdır. ESPHome ADS1115 yapılandırmasında bu değer veri-hızı enum/register kodudur; 7 (0b111) seçimi 860 SPS'e karşılık gelir.
- 200 ms pencerede 174–177 farklı örnek (yaklaşık 870–885 örnek/s) görülmesi 860 SPS ayarıyla uyumludur.
- Dolayısıyla önceki “7 SPS ile 860 SPS YAML uyuşmazlığı” ve “örnek akışı açıklanamıyor” sonuçları geri çekilmiştir. Bu log, 860 SPS sürekli modla uyumlu örnek akışını destekler. Ancak çalışan binary'nin depodaki deney YAML'ından üretildiğini tek başına kanıtlamaz.

### Akım uyumu ve katsayı sınırı
- Ortak pencerede ADS1115 0.469881 A (n=84), PZEM 0.469882 A (n=34) yayımlamıştır. Ortalamaların yakınlığı bu oturum için gözlemsel uyumdur.
- Kullanıcı değerlendirmesine göre yaklaşık 0.017 V ham RMS değeri × 27.60 ≈ 0.469 A'dır. Ancak katsayı 0.47 A civarındaki aynı noktadan türetildiyse bu uyum bağımsız kalibrasyon doğrulaması değildir; hesaplanan katsayının aynı noktayı geri üretmesidir.
- Önemli yapılandırma notu: Depodaki E19 YAML dosyasının mevcut sürümünde `calibrate_linear: 0.0 -> 0.0, 1.0 -> 30.0` yazmaktadır. Kullanıcının log değerlendirmesinde 27.60 katsayısı anılmaktadır. Çalışan firmware/cache kaynağı ve uygulanan katsayı, depodaki YAML ile birebir eşleştirilmeden 27.60'ın bu oturumda hangi binary'de kullanıldığı kesinleştirilmeyecektir.
- Tek nokta, çoklu akım aralığı doğrusallığını veya ±%4 kabulünü kanıtlamaz. Katsayı değişikliği yapılmamıştır.

### Yayın çözünürlüğü
- E19 YAML'daki `accuracy_decimals: 2`, yayınlanan akımı 0.01 A basamaklarla gösterir. `accuracy_decimals: 3` daha ince sayısal yayın sağlar; ADC'nin fiziksel doğruluğunu veya gürültü tabanını tek başına iyileştirmez.
- Kontrollü 150 W karşılaştırması için mevcut ayar korunacak; yayın hassasiyeti değişikliği ayrı bir yazılım değişkeni olarak ele alınacaktır.

### SSR ve UDP yorumu
- Olayların UDP ile alınıp ayrıştırılması haberleşme zincirini destekler; olay durumu fiziksel yük ON/OFF kanıtı değildir.
- OFF sonrasında PZEM akımının sürmesi ve GPIO readback mismatch uyarıları nedeniyle SSR'ın yükü fiziksel olarak kestiği doğrulanmamıştır. `gpio_get_level()` yalnızca GPIO seviyesine ilişkin kanıttır; SSR kontak/iletim durumunu kanıtlamaz.
- Bu nedenle 100 W kaydı sabit yükte ölçüm zinciri karşılaştırması olarak kullanılabilir; SSR anahtarlama deneyi veya doğrulanmış ON/OFF etiketli veri olarak kullanılamaz.

### ADS1115 gain ve giriş güvenliği
- `gain: 0.512`, `gain: 2.048` ayarına göre daha dar tam ölçek aralığı ve daha küçük nominal LSB sağlar; sensör sinyalini fiziksel olarak 4 kat büyütmez. Dar aralık clipping/headroom riskini azaltmaz, artırır.
- Bu nedenle gain değişikliği yapılmayacak. SCT sinyalinin tepe değeri, iki AIN pininin ortak-mod seviyesi ve giriş sınırları doğrulanmadan 0.512 V aralığına geçilmeyecek.
- A0/A1 bias/common-mode bağlantısı donanım üzerinden ayrıca doğrulanmalıdır. Mevcut YAML tek başına fiziksel bias devresini kanıtlamaz.

### Güncel sonuç
- Örnek akışı 860 SPS ile uyumludur; ADS1115/PZEM ortalama uyumu tek yük/tek oturum gözlemidir.
- Katsayı bağımsız doğrulanmamıştır; çalışan firmware'in katsayı kaynağı da ayrıca eşleştirilmelidir.
- ADS1115 bias/common-mode güvenliği ve SSR fiziksel anahtarlaması açık konudur.
- K, gain, filtre ve firmware değiştirilmemiştir. 100 W testi bu yorumla **gözlemsel karşılaştırma olarak işlendi**; çok noktalı kalibrasyon tamamlanmadı.
