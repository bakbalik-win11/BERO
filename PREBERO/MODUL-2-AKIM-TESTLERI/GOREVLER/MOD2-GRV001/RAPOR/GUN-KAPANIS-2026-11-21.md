# BERO – 2026-11-21 Gün Kapanışı

**Proje:** BERO / MOD2-GRV001  
**Çalışma alanı:** ADS1115 No.10 + SCT013 30A/1V, Modül 2; PZEM karşılaştırması Modül 3  
**Firmware:** V1.1 – K=27.59  
**Gün durumu:** KAPATILDI

## 1. Günün teknik tespitleri

### Tespit 1 – PF ile SCT/PZEM ölçüm farkı birlikte değişiyor

100 W akkor ampul ile dimmer deneyinde PZEM PF düştükçe SCT/PZEM oranı belirgin biçimde yükseldi:

| PF | PZEM ort. (A) | SCT ort. (A) | SCT/PZEM | SCT sapması |
|---:|---:|---:|---:|---:|
| 1.00 | 0.46325 | 0.42657 | 0.921 | -7.92% |
| 0.89 | 0.42800 | 0.44343 | 1.036 | +3.61% |
| 0.73 | 0.37656 | 0.44861 | 1.191 | +19.14% |
| 0.61 | 0.33750 | 0.50866 | 1.507 | +50.71% |

Bu deneyde PF ile ölçüm farkı arasında güçlü, monoton yönlü bir deneysel ilişki gözlendi. Ancak dimmer akım seviyesini ve dalga biçimini birlikte değiştirdiğinden, PF'nin tek başına nedensel etkisi izole edilmiş değildir. Bulguyu "PF tek başına SCT'yi bozar" şeklinde değil, "PF ile birlikte değişen dimmerli çalışma/dalga biçimi koşulunda SCT ve PZEM ilişkisi değişiyor" şeklinde ifade etmek gerekir.

**Deney kararı:** Dimmerle kalibrasyon/katsayı taraması kapatıldı. Dimmer verileri normal kalibrasyon grubuna karıştırılmayacak.

Ayrıntılı rapor: `DIMMER-100W-PF-ETKISI-2026-11-21.md`.

### Tespit 2 – Mevcut K=27.59 düşük akım bölgesinde sapıyor

V1.1 katsayısı yüksek akım testlerinde iyi sonuç vermiş olsa da düşük akım ölçümlerinde SCT/PZEM farkı büyüyor. Bugünkü 8.5 W LED deneyi bu alan için yeni bir doğal düşük PF gözlemi sağladı.

| LED çevrimi | PZEM akım (A) | SCT akım (A) | PF | SCT/PZEM |
|---|---:|---:|---:|---:|
| 1 | 0.052 | 0.095 | 0.67 | 1.827 |
| 2 | 0.053 | 0.096 | 0.66 | 1.811 |

İki çevrimde SCT/PZEM oranı yaklaşık %0.9 farkla tekrarlandı. Bu, PF 0.66–0.67 ve yaklaşık 0.052–0.053 A PZEM akımı çevresinde ilk tekrar edilebilirlik işaretidir.

İlk çevrimde kullanıcı UT200B+ pens ölçümünü 0.044 A olarak bildirdi. Düşük akımda pens cihazı bağımsız kesin referans sayılmadığından PZEM/SCT analizinin temeli yapılmadı.

İkinci çevrim ekranında PZEM akımı kısa bir bölümde sıfıra düştü; bu veri kesintisi/geçersiz alan kararlı pencere ortalamasına katılmadı.

**Sınırlama:** 8.5 W LED protokolünde üç çevrim hedeflenmişti; gün sonunda iki çevrim kaydedildi. Kaynak tam CSV yerine ekran görüntüleridir. Dolayısıyla bu rapordaki akım değerleri grafik gösterge okumalarıdır; tam pencere ortalaması, standart sapma veya örnek sayısı olarak yorumlanmamalıdır.

Ayrıntılı deney kaydı: `../DENEYLER/8_5W-LED-DUSUK-PF-TEKRAR-2026-11-21.md`.

### Tespit 3 – Tek katsayı tüm çalışma alanı için yeterli olmayabilir

Bugünkü yüksek/düşük akım ve farklı PF koşullarındaki gözlemler, tek K katsayısının bütün çalışma alanında aynı sapmayı sağlamayabileceğini gösteriyor.

Birden fazla katsayı veya koşula bağlı düzeltme yaklaşımı araştırılabilir. Ancak:
- Akım dilimlerinin alt/üst sınırları henüz belirlenmedi.
- Gerekli katsayıların sayısı belirlenmedi.
- PF etkisi ile akım seviyesi etkisi henüz tam ayrıştırılmadı.
- PF'ye bağlı düzeltme fonksiyonu doğrulanmadı.
- Yeni katsayı firmware'e uygulanmayacak.

Katsayı dilimleri ancak ara akım bölgelerinde ve farklı doğal PF koşullarında tekrarlı, karşılaştırılabilir veriler toplandıktan sonra tanımlanmalıdır.

## 2. Günün yöntemsel tecrübeleri

1. **Dimmer kalibrasyon aracı olarak uygun değil:** Dimmer akımı düşürürken dalga biçimini de değiştiriyor. Bu nedenle normal yük kalibrasyonundan ayrı tutulmalı.
2. **Üçüncü ölçümün geometrisi önemli:** UT200B+ ile faz ve nötr birlikte/çok yakın kavrandığında alınan önceki pens okumaları geçersiz kabul edildi. Pens yalnızca tek iletkeni kavramalı. Kablo ayrıldıktan sonraki okumalar dahi düşük akımda cihazın doğruluğu ve eşzamanlılık sınırları gözetilerek kullanılmalı.
3. **PF zaman eşleştirmesi gerekli:** PZEM PF ve akım örnekleri SCT verisiyle aynı kararlı zaman penceresinde eşleştirilmeden korelasyon hesabı yapılmamalı.
4. **Tekrar sayısı ve ham veri korunmalı:** Ekran görüntüsü ön gözlem sağlar; nicel analiz için zaman damgalı tam CSV, geçerli örnek sayıları ve kararlı pencere sınırları gerekir.
5. **PZEM referanstır, mutlak gerçek değer değildir:** PZEM karşılaştırma/etiketleme referansı olarak kullanılmaya devam eder; ölçüm belirsizliği göz ardı edilmez.
6. **Kod sabit tutuldu:** Deneyler boyunca V1.1 ve K=27.59 değiştirilmedi. Böylece değişen sonuçlar firmware değişikliğiyle karıştırılmadı.

## 3. Sonraki deney önerisi – ADS1115 biaslı / bias'sız karşılaştırması

Bir sonraki deneyin konusu:

**Mevcut sabit yüklerle ADS1115 girişinde biaslı ve bias'sız okuma davranışını karşılaştırmak.**

Amaç, aynı yük ve aynı ölçüm koşullarında bias devresinin SCT/ADS1115 okumasına etkisini ayırmak.

Önerilen yöntem:
- Mevcut sabit yükler kullanılacak; yeni bir değişken olarak dimmer eklenmeyecek.
- Her yükte önce mevcut biaslı düzenek, sonra güvenli ve teknik olarak tanımlanmış bias'sız düzenek ölçülecek.
- V1.1 yazılım/ölçekleme ve diğer ADC ayarları mümkün olduğunca sabit tutulacak; bias'sız bağlantı için girişin ortak-mod ve ADC mutlak giriş sınırları ayrıca doğrulanmadan bağlantı değiştirilmemeli.
- Aynı yük, aynı iletken, aynı SCT yönü/konumu, aynı kayıt penceresi ve aynı PZEM koşulları korunacak.
- Ham ADS1115 verisi, hesaplanan akım, PZEM akım/PF, örnek sayısı ve kararlı pencere istatistikleri kaydedilecek.
- Bias'sız koşulda girişin güvenli çalışma aralığı ve ADC giriş sınırları doğrulanmadan donanım bağlantısı uygulanmayacak.
- Sonuçlar bias devresinin offset kaldırma, sinyal salınımını ADC aralığında tutma ve ölçüm kararlılığına katkısı açısından yorumlanacak.

Bu deney yeni bir görev olarak açılacak; bugünkü üç tespit ve mevcut katsayı kararları değiştirilmeden korunacak.

## 4. Gün sonu kararları

- Dimmer deneyi: **KAPALI**.
- 8.5 W LED düşük PF oturumu: **BUGÜN İÇİN KAPALI; iki çevrim kayıtlı, üçüncü çevrim eksik**.
- V1.1 YAML: **DEĞİŞMEDİ**.
- Katsayı K=27.59: **KORUNDU**.
- Akım dilimleri ve çoklu katsayı yapısı: **ARAŞTIRMA KONUSU; henüz karara bağlanmadı**.
- Sonraki çalışma: **ADS1115 biaslı/bias'sız okuma karşılaştırması**.
- Bu rapor, günün deneysel bulgularını ve yöntemsel tecrübelerini kaydeder; laboratuvar doğrulaması veya nihai kalibrasyon iddiası değildir.

## 5. Kaynak dosyalar

- Dimmer PF raporu: `DIMMER-100W-PF-ETKISI-2026-11-21.md`
- 8.5 W LED deney kaydı: `../DENEYLER/8_5W-LED-DUSUK-PF-TEKRAR-2026-11-21.md`
- Önceki V1.1 düşük akım raporu: `../V1.1/RAPOR/V1.1-KATSAYI-DOGRULAMA-VE-DUSUK-AKIM-ANALIZI-2026-11-21.md`


## 6. Günün dördüncü teknik tespiti – Bias, yaklaşık 0.47 A çalışma noktasında faydalı

Üç ayrı bias kanal çapraz deneyinin ortak sonucu değerlendirildi. Her üç deneyde de biaslı kanalın ortalama akımı daha yüksek ve PZEM karşılaştırmasına göre MAPE değeri daha düşük çıktı.

| Deney | Biaslı kanal | Biassiz kanal | Biaslı kol ortalama avantajı | MAPE biaslı / biassiz |
|---|---|---|---:|---:|
| 1 | A2–A3 | A0–A1 | +0.015169 A | %1.016 / %3.262 |
| 2 | A0–A1 | A2–A3 | +0.012737 A | %1.275 / %3.168 |
| 3 | A2–A3 | A0–A1 | +0.012852 A | %1.819 / %2.508 |

İlk iki deneyde bias kanalı değiştirildiğinde yüksek ortalamanın biaslı kanalı takip etmesi, kanal etkisi yerine bias katkısı yorumunu destekler. Kullanıcı, üç deneyin tamamında biaslı kanalın başarılı olduğunu teyit ederek test serisini kapatmıştır.

**Günün tespiti:** Yaklaşık 0.47 A / 107–108 W çalışma bölgesinde biasın ölçüm sonucuna pozitif katkısı olduğu kabul edildi. Bu, PZEM karşılaştırma referansına göre daha yakın sonuç örüntüsüdür; PZEM ground truth değildir ve mutlak doğruluk iddiası yapılmamaktadır.

**Sınırlar:** Biasın gürültüyü azalttığı gösterilmedi; tüm akım aralığına genelleme yapılmayacak. K=27.59 korundu. 100 W bias kanal çapraz deney serisi (üç tekrar) kapatıldı.

İlgili ayrıntılı kayıt: ../DENEYLER/BIAS-KANAL-TEKRAR-CAPRAZ-DENEY-2026-11-21.md ve ../V1.1/RAPOR/V1.1-BIAS-KANAL-TEKRAR-2026-11-21.md.


## 7. Ek tespit – Biaslı ADS1115 kanalında yük altı uyum ve boşta spike gözlemi

Kullanıcının paylaştığı Home Assistant zaman grafiği (21:51–21:59, 2026-11-21) nitel olarak incelendi. Grafikte PZEM akımı mavi, ESP32D2 A0–A1 akımı sarı, A2–A3 akımı kırmızı izdir. Bu oturumun bağlantı düzeninde A0–A1 biassız, A2–A3 biaslıdır.

- **Yük altında ilk bölüm (~0.46–0.48 A):** İki ADS1115 kanalının akım izleri PZEM çevresinde birbirine yakın seyrediyor.
- **Yük kesildiğinde (~21:56–21:59):** PZEM sıfıra iner. A0–A1 biassız iz sıfıra yakın ve daha sakin görünürken A2–A3 biaslı izde tekil ve tekrarlayan pozitif spike'lar görülür.
- **Yük yeniden geldiğinde (~0.19 A):** İki ADS1115 kanalının son değerleri yaklaşık 0.189–0.190 A, PZEM yaklaşık 0.188 A olarak grafikte gösterilmektedir.

**Yeni teknik tespit:** Biaslı ADS1115 kanalı yük altında PZEM karşılaştırmasına yakın sonuç verirken sistem boşta daha fazla spike üretebilmektedir. Bu iki davranış birlikte değerlendirilmelidir; biasın ölçüm katkısı boşta gürültü/spike davranışını ortadan kaldırmamaktadır.

**Kanıt sınırı:** Bu kayıt grafik ekran görüntüsüne dayalı nitel gözlemdir; ham zaman serisi CSV'si ve spike sayısı/genliği istatistiği bu ekle birlikte sunulmamıştır. Bu nedenle boşta spike farkı henüz nicel olarak ölçülmüş kabul edilmez. Yeni bir test sonucu veya kalibrasyon değişikliği değildir.

**Takip önerisi:** Boşta uzun süreli iki kanal kaydı alınıp spike sayısı, tepe genliği, medyan, standart sapma ve eşik üstü olay sıklığı karşılaştırılmalıdır. Yük altı karşılaştırması ve boşta davranış ayrı metrikler olarak raporlanmalıdır.

## 8. 15 W tek ampul bias karşılaştırma deneyi – KAPATILDI

**Kaynak:** Kullanıcının paylaştığı `history (12).csv`; 559 satır; 22:16:00–22:19:45 Türkiye saati. Tek nominal 15 W ampul bağlıdır. Kanal eşlemesi A0–A1 biassız, A2–A3 biaslıdır.

| Ölçüm | A0–A1 biassız | A2–A3 biaslı |
|---|---:|---:|
| Örnek | 225 | 227 |
| Ortalama | 0.058746 A | 0.063017 A |
| Medyan | 0.058814 A | 0.060014 A |
| Standart sapma | 0.002175 A | 0.030700 A |
| Maksimum | 0.066375 A | 0.516451 A |

- PZEM güç ortalaması 14.839 W; nominal 15 W yükle uyumludur.
- PZEM akımında yalnızca tek örnek vardır: 0.065 A. Bu nedenle akım MAPE/hata hesabı yapılmamıştır.
- A2–A3 biaslı kanalda 0.516451 A tekil spike görülmüştür. Spike hariç A2–A3 ortalaması yaklaşık 0.061011 A'dır.
- **Yorum:** Biaslı kanalın medyanı ve genel ölçüm seviyesi PZEM'in tek akım örneğine biassız kanaldan daha yakındır. Kullanıcının gözlemi doğrultusunda biaslı kanalın ölçüm seviyesi bakımından daha yakın olduğu tespiti kaydedildi. Bununla birlikte spike belirgindir ve standart sapma yüksektir; biasın kararlılığı artırdığı söylenemez.
- **Karar:** 15 W oturumu kapatıldı. Sonuç düşük akım bölgesinde bias lehine ek gözlemdir; tek deneyden genelleme yapılmaz.
- K=27.59 ve YAML korunmuştur. PZEM ground truth değildir. SSR fiziksel bağlı değildir; switch olayları fiziksel yük kontrolü sayılmamıştır.
- Ayrıntılı rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/RAPOR/V1.1-15W-BIAS-KANAL-TESTI-2026-11-21.md`.
- Ham CSV konuşma ekinde incelendi; GitHub'a ham CSV yüklenmedi.


## 9. Kettle testleri – kapanış ve bias kararı

## 2026-11-21 – Kettle testleri ve bias kararı

Kettle 1 (sıcaklık koruma modu) ve Kettle 2 (kaynatma modu) ayrı sabit çalışma koşulları olarak değerlendirildi. Kullanıcının kararıyla ek kettle testine devam edilmeyecek.

**Karar:** Mevcut deney dizisi kapsamında ADS1115 ölçüm yolunda bias gerekli kabul edildi. Kettle karşılaştırmalarında biaslı A2–A3 kanalının PZEM akım ortalamasına daha yakın sonuç verdiği değerlendirildi. Bu karar, biasın tüm çalışma koşullarında gürültüyü azalttığı anlamına gelmez.

**Sınırlar ve açık bulgular:**
- Boşta alınan CSV'de biaslı kanalda 0.030 A üzeri 128 örnek ve 0.10114 A maksimum görülmüştür; biassız kanalda 0.030 A üzeri örnek görülmemiştir.
- 15 W deneyinde biaslı kanalda 0.516451 A tekil spike kaydedilmiştir.
- Kettle sonuçlarında ölçüm yakınlığı bias lehine değerlendirilmiş olsa da değişkenlik/kararlılık her deneyde aynı yönde değildir.
- PZEM karşılaştırma referansıdır, ground truth değildir.
- 0.020 A altını sıfırlama yalnızca ileride tartışılacak aday eşiktir; uygulanmadı.
- K=27.59 ve çalışan YAML değiştirilmedi.
- Bu karar mevcut deneylerin kapsamındadır; tüm akım aralığı için mutlak doğruluk veya nihai devre tasarımı iddiası değildir.

**Kullanıcı kararı:** Daha fazla kettle testi gerekmiyor; bias kullanılmalı.

Kettle 1 ve Kettle 2 oturumları için açılış geçişleri değerlendirme dışı tutuldu; PZEM'in kararlı çalışma alanları esas alındı. Kettle 1 sıcaklık koruma, Kettle 2 kaynatma modudur. Kullanıcı ek teste devam etmeme kararı verdi.

## 10. 2026-11-21 – Alt/üst akım bandı katsayı dağılımı: ilk değerlendirme

Bugünkü farklı yüklerde elde edilmiş mevcut ölçüm noktaları, K=27.59 baz alınarak birlikte değerlendirildi. Amaç yeni bir deney açmak değil; gün içinde oluşan katsayı dağılımı gözlemini ve sonraki çalışma yönünü günlük kayda eklemektir.

### Mevcut veri dağılımı

| Test yükü | PZEM referans akımı | A2–A3 mevcut (K=27.59) | PZEM'i tutturan ideal K | Geçici rejim sınıfı |
|---|---:|---:|---:|---|
| 15 W | 0.0643 A | 0.0609 A (-%5.33) | 29.14 | Alt bant adayı |
| 108 W | 0.4699 A | 0.4429 A (-%5.75) | 29.27 | Alt bant adayı |
| Kettle 1, yaklaşık 157 W | 0.6849 A | 0.6373 A (-%6.95) | 29.65 | Alt bant adayı |
| Kettle 2, yaklaşık 1524 W | 6.8028 A | 6.8237 A (+%0.31) | 27.51 | Üst bant adayı |
| Ütü, yaklaşık 2317 W | 10.5467 A | 10.5546 A (+%0.07) | 27.57 | Üst bant adayı |

Alt banttaki üç ideal katsayının aritmetik ortalaması yaklaşık **29.35**'tir. Üst banttaki iki nokta mevcut **K=27.59** ile uyumludur.

### Geçici iki bant hipotezi

- **Alt bant adayı:** 1.5 A altı için K_alt ≈ 29.35.
- **Üst bant adayı:** 1.5 A ve üzeri için K_üst = 27.59.
- Bu dağılım mevcut beş çalışma noktasına dayalı bir hipotezdir; kalibrasyon kararı veya firmware uygulaması değildir.
- K_alt=29.35 kullanıldığında tablodaki alt bant noktalarının teorik sapmaları yaklaşık +%0.7, +%0.3 ve -%1.0 olur. Bu hesap, ideal K değerlerinden türetilmiştir; yeni ölçüm sonucu değildir.
- Üst bantta K=27.59 ile mevcut sapmalar yaklaşık +%0.31 ve +%0.07 düzeyindedir.

### Açık kalan eşik sorusu

1.5 A geçiş eşiği henüz deneysel olarak doğrulanmamıştır. Mevcut veri 0.6849 A ile 6.8028 A arasında geniş bir boşluk bırakmaktadır. Bu nedenle 1.5 A yalnızca başlangıç eşiği önerisidir; kesin sınır olarak kabul edilmeyecektir.

**Devam yönü:** Orta akım bölgesinde, tercihen yaklaşık 1.3–4.5 A (kabaca 300–1000 W koşullarında) ölçüm alınarak K=27.59 ve K_alt=29.35 sonuçları karşılaştırılacak. Ölçüm sonuçlarına göre alt/üst bant sınırı aranacak; gerekirse 1.5 A yerine daha yüksek bir geçiş noktası değerlendirilecek. Tek bir orta-yük ölçümü tek başına kesin eşik ilan etmek için yeterli sayılmayacak.

### Günlük karar ve koruma

- K=27.59 çalışan katsayı olarak korunuyor.
- K_alt=29.35 yalnızca aday katsayıdır; kabul edilmedi.
- 1.5 A eşiği kesinleşmedi; aranmaya devam edilecek.
- Firmware, ESPHome YAML ve çalışan ölçüm zincirinde değişiklik yapılmadı.
- PZEM karşılaştırma referansıdır; ground truth değildir.
- Bu kayıt günlük değerlendirmedir; ayrı bir deney dosyası veya deney kapanışı değildir.
