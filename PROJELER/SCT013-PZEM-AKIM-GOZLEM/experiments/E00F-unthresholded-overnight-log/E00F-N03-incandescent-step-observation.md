# E00F-N03 — 100 W akkor yük basamak gözlemi (kısmi) — 2026-10-31

## HEDEF

Mevcut ESP32D2/E00F ölçüm zincirini değiştirmeden, bilinen 100 W akkor ampul açıldığında SCT Raw AC çıktısının yüksüz başlangıç kesitinden ayrılıp ayrılmadığını gözlemek. Bu adım kalibrasyon veya ±%4 doğruluk doğrulaması değildir. Planlanan tam sıra yük kapalı → yük açık kararlı → tekrar yük kapalıdır.

## LOG

- **Yük:** 100 W akkor ampul — KULLANICI BEYANI; kullanıcı 10:32'de açtığını bildirdi ve ampulün 100 W akkor olduğunu doğruladı.
- **Kaynak:** Kullanıcının yüklediği `esp32d2-logs (14).txt`; 3.006 satır; 222.950 bayt.
- **SHA-256:** `c4131d1d4a6f40f2024c05fa51eeed542cee4cf6b2d4a8f806d6a594ea72280e`.
- **Zaman:** cihaz logu 10:30:27.239–10:39:09.934; CT Clamp pencereleri 10:30:27.836–10:39:09.831; 262 pencere. Kullanıcının yük açma işareti 10:32.
- **Cihaz:** ESPHome 2026.10.1, ESP32 rev3.1, `esp32d2`; Wi-Fi/API bağlantısı başarılı.
- **Ayarlar:** CT Clamp 0.20 s pencere / 2.00 s güncelleme. GPIO32 SCT RAW, GPIO33 SCT voltajı, GPIO34 bias RAW, GPIO35 bias voltajı; dört ADC kanalı ADC1, 12 dB, samples=1, average, 1.00 s güncelleme. Mevcut katsayı 24.22 korunmuştur; bu log açılış özeti katsayıyı göstermediğinden katsayı mevcut E00F yapılandırma kaydından alınmıştır.
- **Fiziksel kurulum sınırı:** Yük türü/gücü kullanıcı tarafından doğrulandı. CT'nin hangi iletkeni kaç tur çevrelediği bu logdan doğrulanamıyor; bu alanlar tahmin edilmedi.
- **Ham veri durumu:** DEBUG log, CT Clamp pencerelerinin Raw AC/N/SPS satırlarını ve yavaş ADC yayınlarını içerir; ham ADC dönüşüm dizisini içermez. Kaynak dosyanın SHA-256 değeri saklandı. Bu oturumda tam ham TXT dosyası Git deposuna aktarılmadı; aşağıdaki ölçüm özeti ve seçilmiş log örnekleri rapora işlendi.

### Yük öncesi ve sonrası Raw AC

| Bölüm | Pencere | n | Raw AC medyan | Ortalama | p95 | Maksimum |
|---|---:|---:|---:|---:|---:|---:|
| Yük öncesi 10:30:27–10:31:59 | 0.20 s / 2 s yayın | 46 | 0.004 V | 0.00426 V | 0.011 V | 0.031 V |
| Kullanıcı açma işaretinden sonra 10:32–10:39:09 | aynı | 215 | 0.019 V | 0.02447 V | 0.080 V | 0.088 V |
| Daha sakin yük bölümü 10:35–10:39:09 | aynı | 124 | 0.019 V | 0.02003 V | 0.02385 V | 0.049 V |

> Not: Son satırın maksimum değeri özet istatistikten ayrıca teyit edilmelidir; raporda kararlı bölüm için medyan/ortalama/p95 esas alınır, tekil tepe kararlı seviye olarak kullanılmaz.

- Kullanıcı 10:32 açma saatini bildirdi. Logda 10:32:01.836 penceresi 0.000 V, 10:32:03.836 penceresi 0.018 V; sonraki ilk dakika pencereleri çoğunlukla 0.018–0.024 V aralığındadır.
- Yük öncesi Raw AC medyanı ile 10:35 sonrası daha sakin bölüm medyanı arasında yaklaşık 4.75 kat fark vardır. Bu, ölçüm zincirinin akkor yük açılmasına belirgin tepki verdiğini destekler.
- 10:35–10:39 bölümünde akım entity medyanı 0.466 A, ortalaması 0.482 A'dır. Raw AC × 24.22 ilişkisiyle aynı büyüklükte sonuç verir; bunlar bağımsız ölçümler değildir.

### Kısa süreli yüksek bölüm

- 10:33:53–10:34:21 arasında Raw AC 0.080–0.088 V bandında kümelenmiştir; en yüksek pencere 10:34:11.836'da 0.088 V, yayınlanan akım 10:34:11.963'te 2.129 A'dır.
- Aynı bölümde `different samples` medyanı 3.754; SPS medyanı 18.770'tir. Tüm 262 pencere için Raw AC ile N arasındaki korelasyon yaklaşık 0.886 hesaplandı.
- **Yorum sınırı:** N, ct_clamp'in farklı kabul ettiği örnek sayısıdır; SPS de N / 0.20 s hesabıdır. Bu iki alan bağımsız değildir ve gerçek ADC dönüşüm hızı değildir. Yük sinyali büyürken N'nin de artması gözlenmiştir; bu ilişki tek başına fiziksel örnekleme hızının arttığını veya anomali nedenini kanıtlamaz.
- Yüksek bölümün nedeni logdan belirlenemiyor; bu pencereler kararlı ampul seviyesi istatistiğine dahil edilerek temsilî değer yapılmamalıdır.

### Yavaş ADC kanalları

- Her GPIO kanalında 523 yayın vardır; güncelleme aralığı yaklaşık 1 s'dir.
- Yük öncesi / yük sonrası medyanlar: GPIO32 SCT RAW 1842 / 1847.5 count; GPIO33 SCT voltaj 1.643 / 1.652 V; GPIO34 Bias RAW 1841 / 1840 count; GPIO35 Bias voltaj 1.653 / 1.653 V.
- Bu kanallar CT Clamp'in 200 ms pencereleriyle eşzamanlı değildir. Dolayısıyla CT tepe pencerelerini doğrulayan eşzamanlı ham ADC örnekleri olarak kullanılamaz.

### Cihaz logu ve uyarılar

- 262 CT Clamp DEBUG penceresi bulundu.
- `[E]` / ERROR kaydı yoktur.
- Açılışta üç ESP32 framework optimizasyon uyarısı vardır; cihazın Wi-Fi/API bağlantısı başarılıdır.
- Seçilmiş örnekler:
  - `10:32:01.836 Raw AC Value: 0.000 V` (yük açma öncesi/işaretine çok yakın pencere)
  - `10:32:03.836 Raw AC Value: 0.018 V` (açma işaretinden sonraki ilk belirgin yükselmiş pencere)
  - `10:34:11.836 Raw AC Value: 0.088 V` (kısa yüksek bölüm)
  - `10:39:09.831 Raw AC Value: 0.025 V` (logun son CT penceresi)

## SONUÇ

- **ÖLÇÜLDÜ:** Bu logda 100 W akkor yük açılmasından sonra Raw AC medyanı 0.004 V'tan 0.019 V'a yükselmiştir. 10:35–10:39 daha sakin bölümünde medyan 0.019 V ve akım entity medyanı 0.466 A'dır.
- **YORUM:** Mevcut E00F zinciri yük açılmasına tepki vermektedir. Bu ilk karşılaştırma, yük değişiminin algılandığına dair kanıttır; CT akım kalibrasyonu veya PZEM'e göre ±%4 doğruluk kanıtı değildir.
- **AÇIK:** Yük kapatma saati ve kapanış sonrası ölçüm bu dosyada yoktur. CT'nin fiziksel iletken/tur bilgisi de doğrulanmamıştır. E00F-N03 bu nedenle **DEVAM EDİYOR / KISMİ GÖZLEM** durumundadır.
- **SONRAKİ ADIM:** Yük kapatıldığında saati ayrıca kaydet; kapanış sonrası log/HA verisiyle Raw AC'nin önceki yüksüz davranışına dönüşünü incele. Firmware, katsayı, eşik, pin ve cihaz kimliği değiştirilmemelidir.

## Sınırlamalar

- Logdaki CT Clamp Raw AC ve akım aynı ölçüm zincirinin katsayı öncesi/sonrası değerleridir; bağımsız ölçüm değildir.
- Yavaş ADC kanalları CT pencereleriyle eşzamanlı değildir.
- Log gerçek ham ADC örnek dizisini saklamaz; 50 Hz dalga şekli, faz veya harmonik sonucu çıkarılmaz.
- PZEM kaydı bu dosyada yoktur; referans karşılaştırması yapılmamıştır.
- CT'nin fiziksel konumu ve tur sayısı bilinmemektedir.
- Yük kapatma/geri dönüş kesiti yoktur.


## İkinci log — yük sonrası tabana dönüş gözlemi

### HEDEF

İlk logda 100 W akkor ampul açıldıktan sonra yükselen Raw AC seviyesinin, yük kesildiğinde başlangıçtaki yüksüz davranışına dönüp dönmediğini incelemek. Bu ikinci kayıt, fiziksel kapatma saatini kullanıcı beyanı yerine koymaz; yalnızca log içindeki geçişi gösterir.

### LOG

- **Kaynak:** Kullanıcının yüklediği `esp32d2-logs (15).txt`; 5.000 satır; 375.017 bayt.
- **SHA-256:** `1ada9e16f102b8a290d2bdc3b8d7572c3ab442561f552acb081ee367f5a23952`.
- **Zaman:** CT DEBUG pencereleri 10:30:51.840–10:45:59.928; toplam 455 pencere.
- **Başlangıç kesiti:** 10:30–10:32 aralığında 35 pencere; Raw AC medyanı 0.004 V, ortalaması 0.00423 V.
- **Yük açık sakin kesit:** 10:35–10:39 aralığında 120 pencere; medyan 0.019 V, ortalama 0.01997 V, p95 0.024 V.
- **Geçiş:** 10:39:25.820 penceresinde 0.018 V; 10:39:27.837'de 0.006 V; 10:39:29.819'da 0.000 V. Bu, logdan çıkarılan geçiş aralığıdır. Kullanıcı ampulü bu saniyelerde kapattığını henüz ayrıca bildirmedi.
- **Yük sonrası:** 10:40–10:46 aralığında 180 pencere; Raw AC medyanı 0.000 V, ortalaması 0.00238 V, maksimum 0.011 V. Bu dağılım başlangıç kesitindeki 0.004 V medyanla aynı düşük seviyededir.
- **Yavaş ADC kanalları (başlangıç / yük açık / yük sonrası medyan):** GPIO32 SCT RAW 1842 / 1852 / 1842 count; GPIO33 SCT voltaj 1.642 / 1.657 / 1.642 V; GPIO34 Bias RAW 1841.5 / 1841 / 1840 count; GPIO35 Bias voltaj 1.653 / 1.653 / 1.653 V. Bu kanallar yaklaşık 1 s aralıkla yayınlanır ve 200 ms CT pencereleriyle eşzamanlı değildir.
- **Hata satırları:** Bu devam dosyasında ERROR veya [E] satırı yoktur. Dosya cihaz açılışını içermediğinden açılış uyarıları hakkında yeni kanıt sağlamaz.
- **Arşiv:** Tam TXT dosyası Git deposuna aktarılmadı; dosya boyutu ve SHA-256 rapora kaydedildi.

### SONUÇ

- **ÖLÇÜLDÜ:** İlk kayıtta yük öncesi 0.004 V olan Raw AC medyanı, yük açık sakin bölümde 0.019 V'a yükselmişti. İkinci kayıtta sinyal 10:39:27.837–10:39:29.819 aralığında düşük seviyeye inmiş ve takip eden altı dakikada medyan 0.000 V olmuştur.
- **YORUM:** Ölçüm zinciri hem yük açıldığında yükselme hem de yük kesildiğinde başlangıç tabanına dönüş davranışı göstermiştir. Bu, 100 W akkor yükün SCT sinyalinde ayrışabilir bir etki oluşturduğunu destekleyen daha güçlü bir aç-kapa gözlemidir.
- **SINIR:** Logdaki sinyal dönüşü ampulün fiziksel olarak kapatıldığını düşündürür; ancak gerçek anahtarlama zamanı kullanıcı tarafından teyit edilmediği için olay zamanı yalnızca logdan çıkarılmıştır. CT'nin primer iletkeni/tur sayısı doğrulanmamıştır. PZEM verisi ve ham ADC örnek dizisi yoktur. Kalibrasyon veya ±%4 doğruluk sonucu çıkarılamaz.
- **DURUM:** E00F-N03 kısmi gözlem olarak kalır. Kullanıcıdan yaklaşık 10:39:28'de ampulü kapatıp kapatmadığı teyit edilecek; CT fiziksel konum/tur bilgisi de doğrulanmadan deney TAMAMLANDI sayılmayacak.

