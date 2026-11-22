# YHDC SCT013-030 (30A/1V) üretici grafiği – BERO V1.6 K(x) karşılaştırması

- Tarih: 2026-11-22
- Kaynak: Kullanıcının paylaştığı YHDC SCT013 aile karakteristik grafiği; `SCT013(30A/1V)` panelindeki etiketli noktalar okunmuştur.
- Hesap tipi: Üretici grafiğindeki Vout değerlerine BERO V1.6 başlangıç ölçeği ve K(x) fonksiyonu uygulanarak teorik karşılaştırma.
- Durum: Matematiksel karşılaştırma; BERO donanımında yeni test yapılmadı.

## 1. Üretici grafiğinden okunan noktalar

| Üretici giriş akımı (A) | Üretici çıkışı (V) |
|---:|---:|
| 6 | 0.1994 |
| 12 | 0.3995 |
| 15 | 0.4997 |
| 18 | 0.5996 |
| 24 | 0.7997 |
| 30 | 0.9994 |
| 36 | 1.1993 |

Grafikte 30A/1V panelinin ilk işaretli noktası 6 A'dır. Bu, sensörün 6 A altında çalışmadığı anlamına gelmez; yalnızca bu üretici grafiğinde 6 A altı için karakteristik noktası gösterilmemiştir. 36 A noktası panelde çizilmiş olsa da 30 A nominal giriş sınırının dışındadır; karşılaştırma tablosunda gösterilir ama 6–30 A nominal aralık ortalamasına katılmaz.

## 2. BERO V1.6 fonksiyonuna uygulama yöntemi

V1.6 YAML zincirindeki başlangıç ölçeği `1.0 V → 27.59 A` olduğundan, üretici grafiğindeki her Vout için önce aynı taban ölçeği uygulanır:

`x = Vout × 27.59`

Sonra BERO'nun tek fonksiyonu hesaplanır:

`K(x) = 26.89 + 5.39 × exp(-x / 0.882)`

V1.6'nın düzeltilmiş akım çıktısı:

`I_BERO = x × K(x) / 27.59 = Vout × K(x)`

Üretici grafiğindeki giriş akımı `I_ref` kabul edilerek sapma:

`Sapma (%) = (I_BERO - I_ref) / I_ref × 100`

Bu sıralama önemlidir: K(x) girdisi üretici grafiğindeki gerçek giriş akımı değil, Vout'un V1.6 başlangıç ölçeği 27.59 ile hesaplanan ham taban akımıdır.

## 3. Hesap sonuçları

| Üretici giriş (A) | Vout (V) | V1.6 taban x (A) | K(x) | V1.6 akımı (A) | Sapma |
|---:|---:|---:|---:|---:|---:|
| 6 | 0.1994 | 5.5014 | 26.9005 | 5.3640 | -10.60% |
| 12 | 0.3995 | 11.0222 | 26.8900 | 10.7426 | -10.48% |
| 15 | 0.4997 | 13.7867 | 26.8900 | 13.4369 | -10.42% |
| 18 | 0.5996 | 16.5430 | 26.8900 | 16.1232 | -10.43% |
| 24 | 0.7997 | 22.0637 | 26.8900 | 21.5039 | -10.40% |
| 30 | 0.9994 | 27.5734 | 26.8900 | 26.8739 | -10.42% |
| 36* | 1.1993 | 33.0887 | 26.8900 | 32.2492 | -10.42% |

*36 A noktası 30 A nominal giriş aralığının dışındadır.*

**Nominal 6–30 A aralığı:**
- Ortalama bağıl sapma: **-10.46%**
- En küçük sapma: **-10.60%**
- En büyük sapma: **-10.40%**
- Üretici verilerinden hesaplanan gerekli katsayı `I_ref/Vout`: yaklaşık 30.01–30.09 A/V; ortalama yaklaşık 30.03 A/V.
- V1.6 fonksiyonunun bu noktalardaki etkin katsayısı: 6 A noktasında 26.9005; 12 A ve üzerindeki noktalarda yaklaşık 26.8900 A/V.

## 4. Grafiğin gösterdiği şey

Bu üretici veri setinde 6–30 A boyunca Vout / Iref oranı yaklaşık sabittir; üretici eğrisi bu gösterilen aralıkta doğrusaldır. V1.6 fonksiyonu ise ilk üretici noktası olan 6 A'da dahi taban x≈5.50 A değerine ulaşır ve etkin katsayısı 26.90 civarına iner; sonraki noktalarda yüksek akım asimptotu 26.89'a çok yakındır.

Bu nedenle üretici eğrisine V1.6 ölçeği uygulandığında yaklaşık -10.4% seviyesinde, neredeyse sabit bir ölçek farkı görülür. Bu sonuç **V1.6'nın kendi BERO ölçüm zincirinde aynı oranda hata yaptığı anlamına gelmez**. Üretici grafik eğrisi, üretici nominal 30A/1V hassasiyeti ve BERO V1.6'nın ampirik/kuruluma özgü kalibrasyon ölçeği doğrudan aynı şey değildir. V1.6, BERO'nun gerçek SCT013 örneği + ADS1115 No.10 + bağlantı/analog koşulları + yazılım zinciri ve PZEM referansıyla elde edilmiş deneysel modeldir.

Bu karşılaştırma, nominal 30 A/V üretici transferini V1.6'nın 27.59 taban ölçeği ve 26.89 yüksek akım katsayısı ile aynı kabul edemeyeceğimizi gösterir. Farkın olası kaynağı sensör örneği/parti hassasiyeti, analog aktarım/ölçek, veri sayfası grafik toleransı veya ölçüm zinciri olabilir; bu hesap bunlardan hangisinin neden olduğunu belirlemez.

## 5. Düşük akım hakkında ne söyler, ne söylemez?

- Bu üretici grafiği 30A/1V modeli için 6 A'dan başlar; 6 A altındaki karakteristik gösterilmediğinden düşük akım doğrusallığı hakkında bu grafikle karşılaştırma yapılamaz.
- İlk 6 A noktasının kendisi, sensörün 6 A altına inemeyeceği veya 6 A'nın kesin alt sınır olduğu anlamına gelmez.
- Dolayısıyla bu hesap, kullanıcının belirttiği düşük akımda üreticinin grafikle doğrulama göstermemesi konusunu destekler; düşük akım sapmasının boyutunu üretici verisinden hesaplamaz.
- 5A/1V paneli ayrı sensör modelidir ve grafikte ilk nokta 1 A'dır. Bu 30A/1V için 1 A alt sınırı olarak kullanılamaz.

## 6. Sonuç / proje kararı

1. Üretici grafiğindeki 30A/1V noktaları V1.6 fonksiyonuna matematiksel olarak uygulandı.
2. Nominal 6–30 A aralığında yaklaşık -10.46% sabit ölçek farkı çıktı.
3. Bu fark V1.6 katsayısını değiştirmek veya bölgesel kalibrasyona dönmek için kanıt değildir; üretici nominal eğrisi ile BERO'nun ampirik kalibrasyon ölçeğinin farklı olduğunu gösterir.
4. V1.6 kendi BERO donanım deneyleri ve PZEM karşılaştırması üzerinden kabul edilmiş referans olarak korunur.
5. PF araştırması ana hedef değildir; uzun vadeli isteğe bağlı araştırma konumunda kalır.
6. Bu hesap, gerçek donanımda ölçülmüş yeni bir sonuç olarak sunulmayacaktır.

Grafik: `YHDC-30A-1V-GRAFIGI-V1.6-KX-KARSILASTIRMA-2026-11-22.svg`

## 7. Ölçüm dayanakları ve bağımsız yüksek akım doğrulaması

Bu karşılaştırmada üç ayrı kanıt kaynağı birbirine karıştırılmamalıdır:

1. **YHDC üretici karakteristik grafiği:** Üreticinin kendi test koşullarında yayımladığı SCT013 30A/1V giriş-akım / çıkış-gerilimi karakteristiğidir. Bu grafik üretici laboratuvar verisidir; BERO donanımında yapılmış bir ölçüm değildir.
2. **BERO ADS1115 ölçüm zinciri:** V1.6'daki tek ve sürekli K(x) fonksiyonu, gerçek BERO kurulumunda ADS1115 diferansiyel ölçümünden elde edilen RMS verileri ve kalibrasyon deneyleri üzerinden geliştirilmiştir. Bu fonksiyon yalnızca SCT çekirdeğini değil, kullanılan sensör örneği, bağlantı/analog koşullar, ADS1115 ve yazılım zincirinin toplam ampirik davranışını temsil eder. Bu grafikte üretici eğrisindeki gerilim noktaları BERO ölçeği ve K(x) fonksiyonundan geçirilmiştir; bu işlem yeni bir fiziksel ADS1115 ölçümü değildir.
3. **PZEM ile saha karşılaştırması:** V1.6 deneylerinde BERO akım sonuçları PZEM ölçümleriyle karşılaştırılmış ve pratik çalışma aralığında fonksiyonun kabul edilmesini destekleyen sonuçlar elde edilmiştir. PZEM bu projede karşılaştırma referansıdır; izlenebilir bir laboratuvar akım standardı olduğu varsayılmamaktadır. Ayrıca mevcut V1.6 karşılaştırması yaklaşık 17.5 A seviyesine kadar veri içerir; bu sonuç tek başına 30 A tam ölçeğin tamamını doğrulamaz.

Bu nedenle üretici grafiğinde görülen yaklaşık -10.46% ölçek farkı, BERO'nun kendi ADS1115 ölçüm zincirindeki saha hatası olarak yorumlanamaz. PZEM karşılaştırması BERO'nun deneysel kalibrasyonunu destekler; ancak yüksek akım bölgesinde bağımsız bir pens ampermetre kontrolü ek kanıt sağlayabilir.

### Önerilen sonraki deney: yüksek akımda pens ampermetre kontrolü

**Amaç:** Üretici grafiği ile BERO'nun ampirik ADS1115/K(x) zinciri arasındaki ölçek farkını fiziksel sahada, PZEM'den bağımsız ikinci bir ölçüm cihazıyla kontrol etmek.

**Ölçüm düzeni:**
- Mümkünse AC True-RMS özellikli ve ölçüm aralığı/doğruluğu bilinen bir pens ampermetre kullanılmalıdır.
- Pens yalnızca tek bir iletkeni (faz veya nötrden biri) çevrelemelidir; faz ve nötr birlikte ölçülmemelidir.
- SCT013, pens ampermetre ve PZEM aynı yük akımını ve mümkün olduğunca aynı kararlı zaman aralığını gözlemlemelidir.
- Akımı yüksek ama devredeki priz, kablo, yük, SCT ve ölçü aletlerinin izin verilen sınırları içinde tutan kararlı bir yük kullanılmalıdır. Ölçüm için devre veya ekipman nominal sınırları aşılmamalıdır.
- Kararlı yük bölümünde BERO akımı, PZEM akımı ve pens ampermetre akımı aynı zaman aralığı için kaydedilmelidir. Tek bir anlık okumaya dayanmak yerine birkaç kararlı ölçüm tekrarı alınmalıdır.

**Kaydedilecek alanlar:**

| Alan | Birim | Açıklama |
|---|---|---|
| test_timestamp | tarih/saat | Ölçüm aralığının zamanı |
| load_description | metin | Kullanılan yük ve çalışma durumu |
| clamp_model | metin | Pens ampermetrenin marka/modeli |
| clamp_accuracy_range | metin | AC akım aralığı ve üretici doğruluk bilgisi |
| clamp_current_a | A | Pens ampermetrenin okuması |
| pzem_current_a | A | Aynı aralıktaki PZEM akımı |
| bero_current_a | A | V1.6 ADS1115/K(x) akımı |
| bero_raw_rms_v | V RMS | Elde edilebiliyorsa kalibrasyon öncesi ct_clamp RMS gerilimi |
| notes | metin | Yük kararlılığı, ölçüm koşulları ve gözlemler |

**Yorum yöntemi:**
- Öncelikle pens ampermetre ile PZEM'in birbirine ne kadar yakın olduğu incelenir.
- Ardından BERO sonucu pens ampermetreye göre değerlendirilir.
- Pens ile PZEM yakın, BERO farklıysa BERO ölçüm zinciri/kalibrasyon farkı araştırılır.
- Pens ile BERO yakın, PZEM farklıysa PZEM'in o çalışma noktasındaki ölçümü ayrıca incelenir.
- Üç cihaz da farklı sonuç verirse tek ölçümle katsayı değiştirilmez; bağlantı, ölçüm aralığı, True-RMS özelliği, yük kararlılığı ve zaman eşleşmesi kontrol edilerek deney tekrarlanır.

**Güvenlik:** Şebeke devresinde çalışma yalnızca uygun ekipman ve yetkinlikle yapılmalıdır. Pens ampermetre, yalıtımı sağlam ve güvenli biçimde erişilebilir tek iletken üzerinde kullanılmalı; açıkta canlı iletken oluşturulmamalı veya devre nominal sınırlarının üzerine çıkarılmamalıdır.

**Durum:** Pens ampermetre ile yüksek akım doğrulaması önerilmiştir; henüz yapılmış bir deney veya ölçüm sonucu değildir. Bu öneri V1.6 K(x) katsayılarını değiştirme kararı değildir.

## 8. MOD3 çamaşır makinesi ısıtma bloğunda pens doğrulaması – 2026-11-22 planı

MOD3-AKM001 uzun pamuklu program kaydındaki ısıtma bloğu, üretici grafiği karşılaştırmasını sahada kontrol etmek için uygun bir aday çalışma noktasıdır:

- Zaman aralığı: 17:24:12–17:38:56 (Europe/Istanbul).
- PZEM akımı: yaklaşık 8.28 A.
- BERO V1.6 akımı: PZEM farkı yaklaşık -0.109 A olduğundan yaklaşık 8.17 A (bu değer raporlanan ortalama farktan türetilmiş yaklaşık değerdir).
- Isıtma gücü: yaklaşık 1.81 kW.
- Yükün ısıtma bloğu boyunca görece kararlı olduğu raporlanmıştır.

### Üretici eğrisi için aynı noktadaki teorik çıkış

YHDC grafiğindeki 6 A (0.1994 V) ve 12 A (0.3995 V) noktaları arasında doğrusal ara değerleme yapılırsa 8.28 A için üretici eğrisinin yaklaşık çıkışı:

`Vout_üretici ≈ 0.2754 V RMS`

Bu, grafik değerlerinden ara değerlemedir; doğrudan üretici tarafından ayrıca listelenmiş bir 8.28 A ölçümü değildir.

BERO'nun aynı akım seviyesini V1.6 etkin katsayısı yaklaşık 26.89 A/V ile üretmesi için gereken gerilim yaklaşık 0.30 V RMS mertebesindedir. Kesin karşılaştırma, ham RMS sütunu aynı zaman aralığı için elde edilirse yapılmalıdır. Yalnızca kalibre edilmiş BERO akımından geriye hesaplanan gerilim, bağımsız ham ADC kaydının yerine geçmez.

### Deney düzeni ve karar mantığı

Aynı ısıtma bloğunda mümkün olduğunca eşzamanlı ve birkaç kararlı tekrar ile şu değerler alınmalıdır:
- PZEM akımı (mevcut kayıtla eşleştirilmiş),
- BERO V1.6 akımı ve mümkünse ct_clamp kalibrasyon öncesi RMS gerilimi,
- AC True-RMS pens ampermetre akımı (tek iletken üzerinden).

**Beklenen yorum:**
- Pens ≈ PZEM ≈ BERO ise, bu fiziksel SCT013/ADS1115/yazılım zincirinin bu yaklaşık 8 A çalışma noktasında gerçek akımı doğru izlediğini destekler. Buna rağmen üretici grafiğinden farklı çıkış gerilimi, kullanılan sensör örneğinin ve/veya analog ölçüm zincirinin üretici nominal transfer eğrisinden farklı etkin hassasiyette olduğunu düşündürür.
- Pens ≈ PZEM, BERO farklı ise BERO zincirinin bu noktadaki kalibrasyonu sorgulanır.
- Pens ≈ BERO, PZEM farklı ise PZEM okuması ve ölçüm koşulları incelenir.
- Pens/PZEM/BERO uyumu tek bir çalışma noktası için kanıttır; sensör ailesinin tüm toleransını, 0–30 A aralığını veya bütün dalga şekillerindeki doğruluğu ispatlamaz.

PZEM mevcut saha bazıdır; pens ampermetre bağımsız ikinci kontroldür. Pensin modeli, True-RMS özelliği, AC akım aralığı ve doğruluk sınıfı kayıt altına alınmalıdır. Pens sadece faz veya nötrden birini ölçmelidir.

**Durum:** MOD3-AKM001'in mevcut kaydı değişmeden korunur. Isıtma bloğu, ayrı/ek doğrulama için aday zaman aralığı olarak belirlenmiştir; bu ek pens ölçümü henüz yapılmış ve kaydedilmiş değildir. Bu plan MOD3-AKM001'i yeniden açmaz ve V1.6 K(x) katsayısını değiştirme kararı değildir.
