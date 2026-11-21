# MOD2-GRV001 – Akım davranışı ve katsayı çalışmaları

## Amaç

SCT013 30A/1V akım sensöründen gelen sinyali ADS1115 ara entegresi üzerinden okuyarak ESP32-D tabanlı masaüstü düzende akım davranışını incelemek ve ölçüm katsayılarını deneysel gözlemlerle belirlemek.

## Çalışma donanımı

- Ana kontrol kartı: ESP32-D geliştirme kartı.
- Taşıyıcı/bağlantı kartı: ESP32 shield.
- Akım sensörü: SCT013 30A/1V.
- Ara entegre / harici ADC: ADS1115.
- Sinyal zinciri: SCT013 30A/1V → ADS1115 → ESP32-D.
- Kullanıcının paylaştığı fiziksel fotoğrafta ESP32-D kartının shield üzerine takılı olduğu ve ADS1115 modülünün kablolarla düzeneğe bağlandığı görülmektedir.
- SCT013 30A/1V sensör fotoğrafta görünmemektedir; model kullanıcı tarafından bildirilmiştir.
- Fotoğraf fiziksel yerleşimi gösterir; kabloların pin eşleşmelerini, elektriksel değerleri veya sistemin çalıştığını kanıtlamaz.

## Çalışma kapsamı

1. ESP32-D ve shield masaüstü düzeneğini imal etmek.
2. ADS1115 modülü ile ESP32-D arasındaki mevcut kabloların pin eşleşmelerini doğrulamak.
3. ADS1115 ile ESP32-D arasındaki I²C haberleşmesini doğrulamak.
4. İki SCT013 30A/1V sensörünü aynı faz iletkenini ölçecek şekilde yerleştirip ayrı ADS1115 diferansiyel giriş çiftlerine bağlamak.
5. Bias, besleme ve ortak referans düzenini gerçek bağlantı üzerinden doğrulamak.
6. Üretilen/ölçülen sinyali osiloskopta gözlemlemek.
7. Test koşullarını ve ölçüm sonuçlarını kaydetmek.
8. Katsayıları ancak test sonuçları yeterli olduğunda belirlemek.
9. Her testin logunu ve yorumunu bu görev altında saklamak.

## Kullanıcı tarafından verilen pin yapısı ve ölçüm ayarları

Bu bölüm, kullanıcının sağladığı mevcut yapılandırma bilgisini kaydeder. Buradaki ayarlar deney sürümüne ait tanımdır; fiziksel bağlantı ve tüm elektriksel sınırlar ayrıca doğrulanmalıdır.

### Bağlantılar

| Kaynak | Hedef | İşlev |
|---|---|---|
| ESP32D2 GPIO21 | ADS1115 SDA | I²C veri |
| ESP32D2 GPIO22 | ADS1115 SCL | I²C saat |
| ESP32D2 3.3V | ADS1115 VDD | Besleme |
| ESP32D2 GND | ADS1115 GND | Ortak referans |
| ADS1115 ADDR | GND | I²C adresi 0x48 |
| SCT013 No. 1 çıkışı | ADS1115 A0–A1 | Biaslı diferansiyel ölçüm kolu |
| SCT013 No. 2 çıkışı | ADS1115 A2–A3 | Biassız diferansiyel ölçüm kolu |

### Ölçüm ve yazılım ayarları

| Parametre | Değer |
|---|---|
| ADS1115 ölçüm modu | Diferansiyel A0-A1 |
| PGA gain | 2.048 V |
| Örnekleme hızı | 860 SPS |
| Çalışma modu | Continuous |
| ct_clamp RMS penceresi | 200 ms |
| Sensör güncelleme aralığı | 1 saniye |
| Kalibrasyon katsayısı | 27.60 |
| Alt akım eşiği | 0.005 A (5 mA) |
| Alt eşik davranışı | 5 mA altındaki ölçüm sıfırlanır |

### Ölçüm amacı ve eşik gerekçesi

ADS1115 üzerinden SCT013 akım trafosunun diferansiyel çıkışı okunur; ct_clamp ile 200 ms RMS akım hesabı yapılır. Bu sürümde 5 mA altındaki ölçümler sıfırlanır. Amaç, yüksüz durumda gözlenen yaklaşık 1–2 mA taban değerlerinin Home Assistant'a gereksiz veri üretmesini önlemektir.

### Kod 0 – önceki ADS1115 ile akım okuma

- Kullanıcı, mevcut sadeleştirilmiş ESPHome koduyla akım okuması yapıldığını ve bu çalışmanın **Kod 0** olarak ayrıldığını bildirmiştir.
- Kod 0, ADS1115 No. 1 dışındaki önceki bir ADS1115 modülüyle çalıştırılmıştır.
- Kod 0'ın başarılı okuma geçmişi korunacaktır; bu kayıt ADS1115 No. 1'in katsayısını veya bias gerekliliğini doğrulamaz.
- ADS1115 modülü değiştiği için No. 1 üzerinde yeniden katsayı çalışması yapılacaktır. Önce biaslı/biassız karşılaştırma deneyi tamamlanacaktır.
- Kod 0'ın YAML ve gerçek çalışma logu, depoda mevcut dosya yolu ve kanıtı doğrulandığında kendi kayıt konumuyla ilişkilendirilecektir; burada yeni bir log veya dosya yolu varsayılmamıştır.

### ADS1115 birim kimliği ve kalibrasyon kuralı

- Kullanımdaki ADS1115 modülleri fiziksel olarak **1–10** şeklinde numaralandırılmıştır.
- Her ADS1115 kendi birim numarasıyla izlenir ve **her modül için ayrı kalibrasyon yapılır**.
- Bir ADS1115 için bulunan kalibrasyon katsayısı diğer ADS1115 modüllerine aktarılmaz; bütün ADS1115'ler için ortak katsayı kabul edilmez.
- Bu görevde yapılacak testlerde kullanılacak ADS1115: **No. 1**.
- Test kayıtlarında ADS1115 birim numarası açıkça yazılır; katsayı yalnızca o numaralı modülün kalibrasyon kaydına bağlanır.

### Önceki kalibrasyon gözlemi

- Önceki katsayı: 30.00
- ADS1115 gözlemi: yaklaşık 0.513 A
- PZEM gözlemi: yaklaşık 0.472 A
- Hesaplanan katsayı: 30.00 × (0.472 / 0.513) = 27.60

27.60 değeri önceki tek karşılaştırmadan elde edilmiş gözlem katsayısıdır; tüm ADS1115 modülleri için geçerli değildir. Bu değerin ADS1115 No. 1'e ait olduğu ayrıca doğrulanmadıkça No. 1'in kalibrasyon katsayısı olarak atanmaz. Her birim farklı akım seviyelerinde ayrıca kalibre edilip doğrulanmalıdır. PZEM karşılaştırma referansıdır, kusursuz ground truth olarak kabul edilmez.



## Bias, sıfır düzeltmesi ve katsayı gerekliliği deneyi – ADS1115 No. 1

### Deney amacı

Aynı akım koşulunda biaslı ve biassız SCT ölçümünü karşılaştırmak; yüksüz durumda sıfır düzeltmesine ihtiyaç olup olmadığını ve akım ölçümünde kalibrasyon katsayısının gerekliliğini deneysel olarak değerlendirmek.

### Deney donanımı ve kanal düzeni

- Tek ADC kullanılacaktır: **ADS1115 No. 1**.
- İki ayrı SCT013 30A/1V sensörü kullanılacaktır.
- Her iki SCT aynı faz iletkenini ölçecektir. Sensörler aynı tek iletkenin çevresine, birbirleriyle aynı yönde yerleştirilecektir.
- **SCT013 No. 1 → A0–A1:** bias uygulanmış ölçüm kolu.
- **SCT013 No. 2 → A2–A3:** bias uygulanmamış ölçüm kolu.
- İki SCT'nin elektriksel çıkışları birbirinden ayrı kalacaktır; tek bir SCT çıkışı iki ADC giriş çiftine paralel bağlanmayacaktır.
- İki ayrı ADS1115 kullanılmayacaktır.
- ADS1115 kanal dönüşümleri sırayla gerçekleştiğinden sonuçlar eşzamanlı örnekleme olarak tanımlanmayacaktır.

### Deney öncesi kontroller ve sıra

1. SCT'ler bağlı değilken bias hattının DC seviyesini multimetreyle ölç; osiloskopta çizgi kararlılığını ve gürültüyü gözle.
2. İki SCT'yi aynı faz iletkenine, aynı yönde yerleştir; her sensörün çıkışını yalnızca kendi diferansiyel giriş çiftine bağla.
3. Akım yokken iki sensörün çıkışlarını multimetre ve osiloskopla ayrı ayrı incele.
4. A0, A1, A2 ve A3 pinlerinin her birinin GND'ye göre mutlak gerilimlerini ölç. Diferansiyel gerilim tek başına yeterli güvenlik doğrulaması değildir.
5. Osiloskop probunun toprak bağlantısını ve ölçüm referansını doğrulamadan şebeke bağlantılı devreye bağlama. Masa tipi osiloskop toprak klipsi koruma toprağına bağlı olabilir.
6. İlk yüksüz ve akımlı karşılaştırmaları mümkün olduğunca **sıfır düzeltmesi ve kalibrasyon katsayısı uygulamadan** kaydet.
7. Kontrollü akım koşullarında iki kanal çiftinin ham ve işlenmiş okumalarını karşılaştır; kanal dönüşüm sırasını ve ölçüm zamanını kaydet.
8. Yüksüz okumaların dağılımına bakarak sıfır basma/alt eşik gerekliliğini değerlendir.
9. Katsayı uygulanmamış ölçümlerin karşılaştırma referansına göre davranışını inceleyerek kalibrasyon katsayısına ihtiyaç olup olmadığını değerlendir.
10. Osiloskop görüntülerini, multimetre değerlerini, ADS1115 ham okumalarını, test koşullarını ve yorumları kaydet.

### Değerlendirme ölçütleri

- Biaslı ve biassız durumda yüksüz DC seviye.
- Her SCT kanalının yüksüz gürültüsü ve dalgalanması.
- Aynı akım koşulunda iki sensörün ham ölçüm farkı.
- Akım uygulandığında sinyalin dalga şekli ve ölçüm kararlılığı.
- Akım kaldırıldığında sıfıra dönüş davranışı.
- Sıfır düzeltmesi veya alt eşik uygulanmasının gerekli olup olmadığı.
- Kalibrasyon katsayısı uygulanmadan ölçümün karşılaştırma referansına göre davranışı.
- Her AIN pininin mutlak gerilim sınırları.
- Aynı ADC üzerindeki ardışık kanal dönüşümlerinin karşılaştırmaya etkisi.

### Yorum sınırı

Bu deney henüz plan aşamasındadır; ölçüm sonucu veya bias, sıfırlama ve katsayı gerekliliği kararı verilmiş değildir. İki SCT aynı iletkeni ölçse de sensörlerin kendi hassasiyet farkları olabilir; bu fark sonuçlarda ayrı değerlendirilmelidir. ADS1115 girişleri GND − 0.3 V ile VDD + 0.3 V sınırlarında kalmalıdır. PGA ayarı bu mutlak giriş sınırlarını değiştirmez.

### Katsayı çalışmasına geçiş

Önce biaslı/biassız ve sıfır düzeltmeli/düzeltmesiz ham davranış incelenecektir. Sonuçlar uygun ölçüm yöntemini belirledikten sonra ADS1115 No. 1 ve ilgili SCT kanalları için katsayı ihtiyacı ayrıca değerlendirilecektir. Önceki ADS1115 ile elde edilmiş katsayı No. 1'e aktarılmayacaktır.

### Elektriksel sınır notu

ADS1115 girişleri GND − 0.3 V ile VDD + 0.3 V sınırları içinde kalmalıdır. PGA kazanç ayarı bu giriş sınırlarını değiştirmez. Diferansiyel okuma seçilmiş olması, her bir giriş pininin mutlak gerilim sınırlarını ortadan kaldırmaz.

### Doğrulama durumu

Bu bölüm mevcut tek-kanal Kod 0 bağlantı ve ayar tanımını kaydeder. İki SCT'li bias karşılaştırması ayrı bir deney düzenidir; henüz fiziksel olarak kurulmuş veya doğrulanmış sayılmaz.

## Çıktılar

- Her kod sürümünün YAML dosyası, logları ve raporları aynı görev klasörünün altındaki kendi sürüm klasöründe tutulur.
- Test verileri görev klasöründeki ortak `VERI/` alanında saklanır.
- Bir sürümün test kanıtları başka bir sürümün kayıtlarıyla karıştırılmaz.

## Tamamlanma ölçütü

Sinyal davranışı yeterince anlaşılmış, katsayılar ölçüm sonuçlarıyla gerekçelendirilmiş ve test çıktıları bu görev içinde kayıt altına alınmış olmalıdır.

Bu görev henüz tamamlanmış değildir.

## Kullanılan fiziksel ESP

- **Kart ailesi / çalışma tanımı:** ESP32-D.
- **Shield:** ESP32 shield.
- **Akım sensörü:** SCT013 30A/1V.
- **Ara entegre / harici ADC:** ADS1115.
- **Fiziksel kurulum kanıtı:** 2026-11-21 tarihli kullanıcı fotoğrafında ESP32-D + shield yerleşimi ve ADS1115 modülünün kabloları görülmektedir.
- **Fiziksel ESP envanter kimliği:** İlgili fiziksel kart envantere eşleştirildiğinde yazılacak.
- **ESPHome / Home Assistant cihaz adı:** Gerçek cihaz ve sabit ad doğrulandığında yazılacak.
- **Not:** Fotoğraf pinout veya çalışan sistem kanıtı değildir. Kimlik, pin ve elektriksel değer tahmin edilmeyecektir.

## Bu görevin sürümlü çıktı düzeni

YAML, LOG ve RAPOR her kod sürümü için tekrarlanan sürüm klasörlerinde birlikte tutulur:

```text
MOD2-GRV001/
├── GOREV.md
├── VERI/
├── V1.0/
│   ├── MOD2-GRV001_V1.0.yaml
│   ├── LOG/
│   │   └── [bu sürümün gerçek çalışma logları]
│   └── RAPOR/
│       └── [bu sürümün test sonucu ve teknik yorumu]
└── V1.1/
    ├── MOD2-GRV001_V1.1.yaml
    ├── LOG/
    └── RAPOR/
```

- Her yeni kod sürümü için görev klasörünün altında yeni bir sürüm klasörü açılır.
- YAML dosyası doğrudan sürüm klasöründe bulunur; LOG ve RAPOR alt klasörleri aynı sürüm klasörünün içindedir.
- `VERI/` görev genelindeki test verileri için ortak alandır.
- Önceki sürümün kodu, logları ve raporları değiştirilmeden korunur.
- Yeni sürümün test kayıtları yalnızca kendi sürüm klasörüne yazılır.


## 2026-11-21 – Osiloskop yük kademeleri tamamlandı / ADS1115 ham okuma sıradaki adım

Bias bağlı olarak yüksüz, 42 W, 57 W, 100 W ve 150 W kademelerinde altışar Single yakalama alındı. Yük kademelerinin Vrms ortalamaları sırasıyla 42 W: 6.5417 mV, 57 W: 9.2983 mV, 100 W: 16.5700 mV ve 150 W: 22.8383 mV oldu. 100 W ve 150 W için Vrms, Avg, Vp-p, Vmax ve Vmin değerleri ayrı ayrı raporlandı. 42 W ve 57 W için yapılandırılmış olarak yalnızca Vrms değerleri mevcuttur.

Ayrıntılı ham veriler ve nominal beklenti karşılaştırması:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/TESTLER/OSILOSKOP-YUK-KADEMELERI-BIAS-2026-11-21.md`

**Teknik yorum:** Ölçülen Vrms ortalamaları yükle düzenli artmıştır. 220 V ve PF=1 varsayımına dayanan nominal karşılaştırma yalnızca ilk değerlendirmedir; PZEM akımıyla doğrulanmış kalibrasyon sonucu değildir. Osiloskop testi ADS1115 performansını kanıtlamaz.

**Sıradaki çalışma:** ADS1115 No. 1 ile A0-A1 diferansiyel ham gerilim okuması. Aynı SCT, bias ve yük koşulları korunarak ADS1115 verisi osiloskop ölçümüyle karşılaştırılacaktır. İlk sürümde RMS, akım dönüşümü, katsayı, sıfır düzeltmesi ve filtre uygulanmayacaktır. I²C 0x48, GPIO21 SDA, GPIO22 SCL bağlantıları ve A0/A1 pinlerinin GND'ye göre mutlak gerilim sınırları test öncesinde doğrulanacaktır. ADS1115 ham örnekleri doğrudan osiloskop Vrms değeriyle eşdeğer sayılmayacak; uygun RMS işleme yöntemi ayrı değerlendirilecektir.

**Durum:** Osiloskop yük kademeleri tamamlandı. ADS1115 ham okuma/karşılaştırma bekliyor.


## 2026-11-21 – Çalışma hedefi güncellemesi: ADS1115 biaslı/biassız karşılaştırması

Kullanıcı kararıyla osiloskopla SCT sinyal genliği karşılaştırması şimdilik durdurulmuştur. Osiloskop mevcut testten sonra kaldırılacak; bu deneyin devamı için osiloskop kullanımı beklenmeyecektir.

### Güncel deney amacı

SCT013 sensörünün doğruluğunu, dalga biçimini veya akım katsayısını belirlemek bu deneyin hedefi değildir. Yalnızca ADS1115 No. 1 üzerinden biaslı ve biassız ölçüm kollarının ham okuma davranışı karşılaştırılacaktır.

### Korunacak mevcut yapı

- Mevcut çalışan akım ölçüm kodu korunacaktır; değiştirilmeyecek ve üzerine yazılmayacaktır.
- Yeni deney için gerektiğinde ayrı YAML sürümü hazırlanacaktır.
- Test ADS1115 No. 1 ile yürütülecektir.
- Planlanan kanal düzeni: SCT013 No. 1 → A0–A1 (biaslı); SCT013 No. 2 → A2–A3 (biassız).
- İki SCT aynı faz iletkenini aynı yönde ölçecek; sensör çıkışları birbirinden ayrı kalacaktır.
- İlk karşılaştırmada RMS/akım dönüşümü, kalibrasyon katsayısı, sıfır düzeltmesi ve filtre kullanılmayacaktır.
- Osiloskopla ölçülen 150 W Vrms değerleri bu deneyin kabul ölçütü olmayacaktır.

### Güvenlik ve doğrulama sınırı

Biassız kolun ADS1115 girişlerine bağlantısı, A2 ve A3 pinlerinin GND'ye göre mutlak gerilimleri ile ADS1115 besleme sınırları doğrulanmadan yapılmayacaktır. Diferansiyel ölçüm seçimi giriş pinlerinin mutlak gerilim sınırlarını ortadan kaldırmaz. Bağlantı topolojisi deney başlamadan önce ayrıca netleştirilecektir.

### Durum

Bu karar deney hedefini günceller; fiziksel bağlantının kurulduğu, yeni YAML'in hazırlandığı veya testin yapıldığı anlamına gelmez. Kullanıcı deneye hazır olduğunda bağlantı doğrulamasıyla devam edilecektir. Mevcut akım ölçüm kodu korunacaktır.


## 2026-11-21 – Deney açıldı: aynı yükte biaslı / biassız ADS1115 ham okuma karşılaştırması

**Durum: AÇILDI – fiziksel uygulama ve ölçüm bekliyor.** Kullanıcı yaklaşık iki saat ara verecek; kullanıcı döndüğünde bağlantı kontrolü ve deney yürütülecek. Bu kayıt deneyin açıldığını gösterir, testin yapıldığını göstermez.

### Deney sorusu
Aynı faz akımını izleyen iki ayrı SCT013 30A/1V sensöründen birinin dönüş ucuna 1,65 V bias referansı verildiğinde, ADS1115 ham diferansiyel okuması bias uygulanmayan kola göre nasıl değişiyor?

### Sabit deney düzeni
- Tek ADC: ADS1115 No. 1, I²C adresi 0x48.
- İki ayrı SCT013 30A/1V sensörü aynı faz iletkenini aynı yönde izleyecek.
- SCT No. 1 biaslı kol: A0–A1. SCT'nin bir ucu A0'a; dönüş ucu bias orta noktasına ve A1'e bağlanacak.
- SCT No. 2 biassız kol: A2–A3. SCT'nin iki ucu doğrudan A2 ve A3'e bağlanacak; bu kola bias bağlanmayacak.
- İki SCT'nin çıkışları birbirine veya ortak giriş çiftine paralellenmeyecek.
- I²C: ESP32D2 GPIO21 SDA, GPIO22 SCL. ADS1115 VDD 3,3 V, GND ortak.
- Mevcut bias kaynağı: 3,3 V üzerinden iki adet 10 kΩ ile yaklaşık 1,65 V orta nokta; 104 (100 nF) filtre kondansatörü. Deney öncesinde gerçek devre ve DC seviyesi ölçülecek.
- SCT013 30A/1V dahili burden'lı modeldir; harici 33 Ω burden eklenmeyecek.

### Tek değişken
İki ölçüm kolu arasındaki amaçlanan fark, **SCT'nin dönüş ucunun bias orta noktasına bağlanmasıdır**. Sensörler ayrı fiziksel SCT'ler olduğundan sensörler arası tolerans/yerleşim farkı olası karıştırıcı değişkendir; sensörler aynı iletken üzerinde aynı yönde ve mümkün olduğunca yakın yerleştirilecek, fiziksel konumları kaydedilecektir.

### Yazılım ve ölçüm sınırları
- Mevcut çalışan akım ölçüm kodu değiştirilmeyecek.
- Deney için ayrı ham okuma yapılandırması gerekirse yeni YAML sürümü hazırlanacak; mevcut kodun üzerine yazılmayacak.
- İlk karşılaştırmada RMS/akım dönüşümü, K katsayısı, sıfır düzeltmesi ve filtre uygulanmayacak.
- A0-A1 ve A2-A3 diferansiyel ham okumaları ardışık dönüşümlerdir; eşzamanlı örnekleme oldukları iddia edilmeyecek. Kanal sırası ve zaman bilgisi kaydedilecek.
- Sabit yükler mevcut testlerde kullanılan yüklerden seçilecek. Her yükte aynı kararlı zaman penceresi iki kanal için karşılaştırılacak.

### Deney öncesi güvenlik kapısı
Biassız kolu bağlamadan önce A2 ve A3 pinlerinin her birinin GND'ye göre mutlak gerilimi, ADS1115 beslemesi ve giriş sınırları doğrulanacak. Diferansiyel okuma ayarı bu mutlak giriş sınırlarını ortadan kaldırmaz. Ölçüm sırasında hiçbir giriş GND−0,3 V altına veya VDD+0,3 V üstüne taşmamalıdır. Bu kontrol yapılmadan biassız SCT kolu ADS1115'e bağlanmayacak. Şebeke tarafında kablo/CT konum değişikliği enerji kesilerek ve kapalı güvenli düzenekte yapılacak.

### Beklenen kayıt
- ADS1115 No. 1 kimliği ve yazılım yapılandırması.
- Bias orta noktasının ölçülen DC değeri.
- A0, A1, A2, A3 mutlak DC gerilimleri.
- Her yük için ham A0-A1 ve A2-A3 örnekleri, zaman damgaları ve örnek sayıları.
- Yük bilgisi ve PZEM akım/PF gözlemi (bağlam bilgisi; bu deneyin ana ölçüm hedefi değil).
- Kararlı pencere ortalaması, standart sapma ve biaslı/biassız farkı.
- Gerçek log ve sonuç yorumu.

**Başarı ölçütü:** Aynı yük koşullarında biaslı ve biassız kolların ham okuma seviyeleri/kararlılıkları karşılaştırılabilir biçimde kaydedilmiş olmalı. Bu deney tek başına katsayı veya PF düzeltmesi belirlemez.


---

## 2026-11-21 – ADS1115 iki kanal denemesi: bağlantı nedeniyle geçersiz / yeniden başlatılacak

**Durum: GEÇERSİZ DENEME – deney baştan kurulacak.**

Kullanıcı bu denemede bağlantı sorunu bulunduğunu bildirdi ve deneyi baştan başlatma kararı aldı. Bu log bias/biassız karşılaştırma sonucu veya kalibrasyon verisi değildir.

- ESP32D2, ESPHome 2026.11.0 ile çalıştı; ADS1115 I²C 0x48 bulundu.
- Logda A0-A1 ve A2-A3 için iki ayrı ADS1115 sensör tanımı ve iki ayrı `ct_clamp` bileşeni görülüyor.
- İlk açılışta 0.447 A ve 0.897 A yayınlandı. Sonraki kararlı pencerelerde A0-A1 yaklaşık 0.45–0.50 A çevresindeyken A2-A3 yükselerek 1.357 A'ya ulaştı.
- Her kanal için 200 ms pencerede çoğunlukla yaklaşık 25 örnek (125 SPS) raporlandı.
- Log kök nedeni kanıtlamıyor. Biasın tek başına hatalı olduğu veya iki `ct_clamp` bileşeninin kesin neden olduğu söylenemez.
- K=27.59 bu logla güncellenmeyecek; ölçümler kalibrasyon için kullanılmayacak.
- Mevcut çalışan tek kanallı V1.1 YAML korunmuştur.
- İki kanallı denemede kullanılan tam YAML kaynak dosyası bu logda bulunmuyor. Eksik bilgilerden kod yeniden oluşturulmadı; gerçek YAML temin edildiğinde ayrı sürüm olarak arşivlenecek.
- Bu fiziksel kurulumdaki ADC, kullanıcı bilgisine göre **ADS1115 No.10**'dur. Bu kayıt No.10 üzerinden izlenecektir.

Ayrıntılı log örnekleri ve yorum: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/ADS1115-IKILI-OKUMA-BAGLANTI-HATALI-2026-11-21.md`.


## 2026-11-21 – İki kanallı V1.1 kaynak kodu arşivlendi

Kullanıcı, bağlantı sorunu yaşanan denemede kullanılan gerçek iki kanallı YAML içeriğini sağladı. Kod, değiştirilmeden `V1.1/MOD2-GRV001_V1.1_IKI-KANAL-DENEY.yaml` adıyla kaydedildi. Önceden depoda bulunan tek kanallı `V1.1/MOD2-GRV001_V1.1.yaml` dosyası korunmuştur; üzerine yazılmamıştır. İki kanallı YAML henüz yeniden derlenmiş veya doğrulanmış değildir. Deney baştan kurulurken hangi YAML'in yükleneceği açıkça seçilecek ve yeni sürüm/test kaydı ayrı tutulacaktır.


---

## 2026-11-21 – Biaslı / biassız kanal karşılaştırması (ilk veri kaydı)

**Gerçek bağlantı eşlemesi – kullanıcı tarafından açıkça teyit edildi:**
- **A0–A1: bias yok**
- **A2–A3: bias var**

Bu eşleme, yukarıdaki eski plan metinlerinde geçen ters kanal açıklamalarını bu deney için geçersiz kılar. İki kanallı YAML'de A2–A3'ün biaslı hat olarak tanımlanmasıyla uyumludur.

### Kaynak ve veri
- Fiziksel ADC: ADS1115 No.10, I²C 0x48; ESP32D2.
- ESPHome logu: 109'ar yayın örneği, 21:27:48–21:29:36 yerel saat.
- HA CSV: A0–A1 183 kayıt, A2–A3 183 kayıt, PZEM akımı 13 kayıt.
- ESPHome logunda PZEM bulunmaz. PZEM karşılaştırması HA CSV zaman eşleştirmesinden yapılmıştır.
- Kaynakların zaman aralıkları birebir aynı değildir; ESPHome logu ile HA CSV tek bir eşzamanlı veri tablosu gibi birleştirilmemiştir.

### Özet sonuç
- ESPHome log ortalaması: A0–A1 0.45744 A; A2–A3 0.47101 A.
- HA CSV ortalaması: A0–A1 0.457052 A; A2–A3 0.472221 A; PZEM 0.467462 A.
- PZEM'e en yakın zamanlı 13 SCT örneğiyle eşleştirme: A0–A1 ortalaması 0.452213 A (PZEM'e göre -%3.262); A2–A3 ortalaması 0.464836 A (PZEM'e göre -%0.562).
- A2–A3 bu veri setinde PZEM'e daha yakındır. Bu sonuç PZEM'in ground truth olduğu anlamına gelmez.
- İki SCT kolunun değişim katsayıları yaklaşık %1.865 ve %1.863'tür; bu veri bias'ın gürültüyü azalttığını göstermemektedir.
- İki ayrı SCT kullanıldığından sensör toleransı ve fiziksel yerleşim farkı karıştırıcı değişkendir. Bias tek başına neden olarak kanıtlanmış değildir.
- Kalibrasyon katsayısı değiştirilmedi; bu deneyden yeni K türetilmedi.

### Arşiv
- Örnek akım verisi: `V1.1/LOG/V1.1-BIAS-KARSILASTIRMA-ESP32D2-2026-11-21.csv`
- PZEM eşleştirmesi: `V1.1/LOG/V1.1-BIAS-KARSILASTIRMA-PZEM-ESLESTIRME-2026-11-21.csv`
- Teknik rapor: `V1.1/RAPOR/V1.1-BIAS-KARSILASTIRMA-2026-11-21.md`

### Sonraki adım
Bias bağlantısı kanallar arasında değiştirilecek: ikinci deneyde A0–A1 biaslı, A2–A3 biassız olacak. Aynı iki SCT'nin fiziksel konumu ve yönü, yük, ADS1115 No.10 ve yazılım ayarları korunacak; yalnızca bias bağlantısının kanalı değişecek. Böylece farkın bias bağlantısını mı yoksa kanal/sensör yolunu mu izlediği sınanacak.

**Durum:** İlk karşılaştırma verisi arşivlendi. Çapraz deney bekliyor. MOD2-GRV001 tamamlanmadı.
