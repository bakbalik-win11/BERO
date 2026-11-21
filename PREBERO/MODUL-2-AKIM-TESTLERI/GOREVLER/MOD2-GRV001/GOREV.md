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


## 2026-11-21 – Yeni deney açıldı: bias kanal çapraz deneyi

İlk karşılaştırmadan sonra kullanıcı kanal bağlantılarını çaprazladı. Yeni deneyde **A0–A1 biaslı**, **A2–A3 biassız** olarak kullanılacaktır. Önceki deneydeki eşleme A0–A1 biassız, A2–A3 biaslıydı.

- Fiziksel ADC: ADS1115 No.10, I²C 0x48; kontrol kartı ESP32D2.
- Aynı iki SCT013 sensörü, aynı faz iletkeni, aynı yön ve konum korunacaktır.
- Mevcut iki kanallı YAML kullanılacak; bu deney için YAML/firmware değiştirilmedi. Tek kanallı çalışan V1.1 korunur.
- Yeni deney dosyası: `DENEYLER/BIAS-KANAL-CAPRAZ-DENEY-2026-11-21.md`.
- Deney açılmıştır; bağlantı kontrolü ve yeni ölçüm henüz yapılmamıştır. Sonuç veya kalibrasyon kararı yoktur.

## 2026-11-21 – Bias kanal çapraz deneyi PZEM verisiyle analiz edildi

- Fiziksel bağlantı: A0–A1 biaslı, A2–A3 biassız; bias beslemesi Modül 1.
- Yazılım: Mevcut iki kanallı V1.1 YAML aynen kullanıldı; kod değişmedi.
- HA CSV: 356 A0–A1, 355 A2–A3 ve 27 PZEM akım örneği.
- Tüm kayıt ortalamaları: A0–A1 0.470006 A; A2–A3 0.457269 A; PZEM 0.469667 A.
- PZEM'e ±2 saniye eşleştirilmiş MAPE: biaslı A0–A1 %1.275; biassız A2–A3 %3.168.
- İlk deneyde bias A2–A3'teyken yüksek okuma A2–A3'teydi; çapraz deneyde bias A0–A1'e taşındığında yüksek okuma A0–A1'e geçti. Ortalama fark bias bağlantısını takip ediyor görünmektedir.
- Gürültü/kararlılık konusunda kesin karar yok: yeni deneyde biaslı CV %1.666, biassız %1.942; ilk deneyde CV'ler yaklaşık %1.86 ile eşitti.
- Bu veri yalnızca yaklaşık 0.47 A / 108 W çalışma bölgesini kapsar. Çoklu akım seviyesinde tek katsayı yeterliliği henüz sınanmadı.
- K=27.59 değiştirilmedi. PZEM yalnızca karşılaştırma referansıdır.
- Kaynak dosya: kullanıcı ekindeki `history (9).csv`; türetilmiş eşleştirme ve rapor V1.1 altında arşivlendi.

**Sıradaki deney:** Bias beslemesini Modül 1 yerine ESP kartından sağlamak; sonra birden fazla akım seviyesinde aynı karşılaştırmayı tekrarlamak. Görev açık kalır.



## 2026-11-21 – Bias katkısını teyit için üçüncü çapraz deney açıldı

**Durum: KAPATILDI – üçüncü 100 W çapraz test verisi analiz edildi.**

İlk deneyde A0–A1 biassız / A2–A3 biaslı iken yüksek ortalama A2–A3'te; ikinci deneyde A0–A1 biaslı / A2–A3 biassız iken yüksek ortalama A0–A1'de görüldü. Bu iki sonuç ortalama farkın bias bağlantısını takip ettiği yönünde bulgudur.

Üçüncü deneyde ilk deneyin fiziksel eşlemesi tekrar edilecek:
- A0–A1: bias yok.
- A2–A3: bias var.
- Bias beslemesi yine Modül 1 olacak.
- Aynı iki SCT, aynı faz iletkeni, aynı yön ve fiziksel konum korunacak.
- Aynı ESP32D2, ADS1115 No.10 ve mevcut iki kanallı YAML kullanılacak.
- Kod, K=27.59 ve diğer yazılım ayarları değiştirilmeyecek.
- Bu deneyde bias kaynağı ESP32'ye çevrilmeyecek; besleme kaynağı değişimi ayrı deney olarak tutulacak.

Amaç, biaslı kolun tekrar daha yüksek ölçüm vermesini ve PZEM karşılaştırmasında daha yakın sonuç üretmesini gözleyerek biasın pozitif katkısı hipotezini teyit etmeye çalışmaktır. Yalnızca yüksek ortalama pozitif doğruluk kanıtı sayılmayacak; PZEM karşılaştırması ve kanal istatistikleri birlikte değerlendirilecektir. PZEM referanstır, ground truth değildir.

Deney planı:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/BIAS-KANAL-TEKRAR-CAPRAZ-DENEY-2026-11-21.md`

**Kapanış:** Üçüncü 100 W tekrarın HA verisi analiz edildi. Üç çapraz deneyin tamamında biaslı kanal başarılı bulundu; biaslı kolun ortalaması daha yüksek ve PZEM'e göre MAPE değeri daha düşüktür. Bu çalışma noktası için bias katkısı tespit olarak kaydedildi. Gürültü azalması veya tüm akım aralığı için genelleme yapılmadı.


## 2026-11-21 – Bias katkısı üçüncü çapraz tekrar: HA verisi analiz edildi

- **Kaynak:** Kullanıcı tarafından yüklenen `history (10).csv`; 509 satır. 199 A0–A1 akım, 199 A2–A3 akım ve 15 PZEM akım kaydı.
- **Zaman:** 21:51:00–21:54:17 Türkiye saati.
- **Bağlantı etiketleri:** Deney planındaki eşleme A0–A1 biassız, A2–A3 biaslıdır. Kullanıcı üç deneyin tamamında biaslı kanalın başarılı olduğunu teyit ederek test serisini kapattı.
- **Ortalama:** A0–A1 0.459638 A; A2–A3 0.472490 A; PZEM 0.469267 A.
- **±2 saniye PZEM eşleştirme MAPE:** A0–A1 %2.508; A2–A3 %1.819. 15 PZEM örneğinin tamamı iki kanalla da eşleştirildi.
- **Kararlılık:** CV A0–A1 %1.871; A2–A3 %2.138. Üçüncü deney biasın gürültüyü azalttığını göstermiyor.
- **Üç deneyin ortak örüntüsü:** Biaslı kolun ortalaması her üç deneyde de biassız koldan yüksek. İlk iki çaprazlamada kanal bağlantısı değiştiğinde yüksek ortalama biaslı kolu takip etti; üçüncü sonuç da planlanan bağlantı eşlemesi doğruysa aynı örüntüyü tekrar ediyor.
- **Yorum:** Biasın yaklaşık 0.47 A bölgesinde ölçüm ortalamasına pozitif yönde etki ettiği ve PZEM referansına göre MAPE'yi düşürdüğü hipotezi güçlenmiştir. PZEM ground truth değildir; iki ayrı SCT'nin tolerans ve konum farkları olası karıştırıcıdır. Mutlak doğruluk veya tüm akım aralığı için sonuç çıkarılamaz.
- **Kalibrasyon:** K=27.59 korundu; yeni katsayı hesaplanmadı.
- **Kaynak ESPHome logu:** Bu veri paketinde ayrıca sunulmadı; rapor HA CSV'ye dayanır.
- **Arşiv:** Ham CSV `V1.1/LOG/V1.1-BIAS-KANAL-TEKRAR-HA-KAYNAK-2026-11-21.csv`; eşleştirme `V1.1/LOG/V1.1-BIAS-KANAL-TEKRAR-PZEM-ESLESTIRME-2026-11-21.csv`; rapor `V1.1/RAPOR/V1.1-BIAS-KANAL-TEKRAR-2026-11-21.md`.
- **Durum:** Üçüncü 100 W çapraz deneyin HA verisi arşivlendi ve analiz edildi. Kullanıcı üç testte biaslı kanalın başarılı olduğunu teyit etti; bias çapraz deney serisi kapatıldı. MOD2-GRV001'in diğer çalışmaları açık.


## 2026-11-21 – Bias çapraz deneyi nihai kararı ve kapanış

**Durum: Bias katkısı çapraz deney serisi KAPATILDI.**

Üç deneyin bağlantı eşlemesi ve sonuçları birlikte değerlendirildi. Üç durumda da biaslı kanal:
- Daha yüksek ortalama akım gösterdi.
- PZEM karşılaştırmasında daha düşük MAPE verdi.

| Deney | Biaslı kanal | Biassiz kanal | Biaslı kolun ortalama avantajı | MAPE biaslı / biassiz |
|---|---|---|---:|---:|
| 1 | A2–A3 | A0–A1 | +0.015169 A | 1.016% / 3.262% |
| 2 | A0–A1 | A2–A3 | +0.012737 A | 1.275% / 3.168% |
| 3 | A2–A3 | A0–A1 | +0.012852 A | 1.819% / 2.508% |

Kullanıcı üç deneyin tamamında biaslı kanalın başarılı olduğunu teyit etti. Üç deneyde biaslı kanalın MAPE değeri daha düşüktür. Bu sonuç yaklaşık 0.47 A çalışma bölgesinde biasın ölçüm sonucuna pozitif katkısını destekleyen tekrarlı deneysel bulgu olarak kaydedildi.

**Sınırlar:** PZEM ground truth değildir. Mutlak doğruluk iddiası yoktur. CV sonuçları biasın gürültüyü azalttığını göstermemiştir. Tüm akım aralığına genelleme yapılmayacaktır. K=27.59 korunmuştur.

**100 W üçüncü çapraz testi:** Üçüncü tekrarın verisi değerlendirildi; biaslı kanalın üç testte de başarılı olması nedeniyle test serisi kapatıldı.

Bias çapraz deneyi serisi tamamlandı. Bu kapanış, MOD2-GRV001 görevinin tamamının kapandığı anlamına gelmez; görev kapsamındaki diğer donanım/ölçüm çalışmaları ayrı olarak devam edebilir.


## 15 W bias karşılaştırma deneyi – KAPATILDI (2026-11-21)

Tek nominal 15 W ampul ile A0–A1 biassız ve A2–A3 biaslı kanallar karşılaştırıldı. Biaslı kanalın medyanı 0.060014 A, biassız kanalın medyanı 0.058814 A; PZEM'in tek akım örneği 0.065 A'dır. Biaslı kanal PZEM örneğine daha yakın görünmektedir. Ancak biaslı kanalda 0.516451 A tekil spike ve yüksek standart sapma gözlenmiştir. Bu nedenle ölçüm seviyesi lehine bulgu kaydedilmiş, kararlılık/gürültü avantajı iddia edilmemiştir. PZEM güç ortalaması 14.839 W'tır; PZEM akım örneği tek olduğundan MAPE hesaplanmamıştır. PZEM ground truth değildir. K=27.59 ve YAML korunmuştur. Deney kapatıldı; MOD2-GRV001 görevinin tamamı açık kalır.

Ayrıntılı rapor: `V1.1/RAPOR/V1.1-15W-BIAS-KANAL-TESTI-2026-11-21.md`.

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

## 2026-11-21 – ESP32 kaynaklı bias + ortak GND deneyi AÇILDI

Yeni deneyde bias ESP32 kartının 3.3 V hattından sağlanacak; ESP32 GND, ADS1115 GND ve bias devresi GND ortaklanacak. Önceki Modül 1 bias deneylerinde bu ortak GND koşulu kullanılmamıştı; dolayısıyla bu yeni deneyde besleme kaynağı ve toprak referansı farkı birlikte değerlendirilecek.

Fiziksel bağlantı, direnç değerleri ve bias DC seviyesi henüz teyit edilmedi. Enerji verilmeden önce bağlantı ve ADS1115 mutlak giriş gerilimleri kontrol edilecek. K=27.59 ve çalışan YAML korunacak. Deney açık; henüz ölçüm sonucu yoktur.

Deney kaydı: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/ESP32-KAYNAKLI-BIAS-ORTAK-GND-2026-11-21.md`.

## 2026-11-21 – ESP32 bias + ortak GND / Kettle 2

Kettle 2 (kaynatma modu) ESP32 3.3 V kaynaklı yaklaşık 1.66 V bias ve ortak GND düzeniyle test edildi. Analiz aralığı 23:03:15–23:05:21.486 Türkiye saati; 127 örnek/kanal ve 24 PZEM akım örneği kullanıldı.

- ESP32 akım sensörü ortalaması: 6.71357 A; CV %2.898; PZEM eşleştirmeli MAPE %2.801.
- A2–A3 ortalaması: 6.83096 A; CV %2.768; PZEM eşleştirmeli MAPE %2.550.
- PZEM ortalaması: 6.80079 A.
- İki SCT kanalında da belirgin dalgalanma görüldü. Kaynağı belirlenmedi; biasın gürültüyü azalttığı sonucu çıkarılmadı.
- Kullanıcı kararıyla ESP32 bias + ortak GND Kettle 2 deneyi kapatıldı. Bu çalışma noktasında ESP32 bias yapısı işe yarar sonuç verdi; genel nihai karar için 100 W ve 15 W deneyleri yapılacak.
- K=27.59 ve firmware/YAML korunmuştur. PZEM ground truth değildir.

Rapor: `V1.1/RAPOR/V1.1-ESP32-BIAS-KETTLE2-2026-11-21.md`  
Özet CSV: `V1.1/LOG/V1.1-ESP32-BIAS-KETTLE2-OZET-2026-11-21.csv`


## 2026-11-21 – ESP32 bias / trafolu bias Kettle 2 karşılaştırması ve 100 W değerlendirmesi

Kullanıcının sağladığı Kettle 2 karşılaştırmasına göre A2–A3 PZEM sapması trafolu 1,65 V bias ile -%0,18, ESP32 kaynaklı 1,66 V bias ile +%0,31'dir. Ortalama ölçüm yakınlığı korunmuştur; ESP32 bias geçişinin bu yükte doğruluk açısından olumsuz etkisi görülmemiştir.

Bununla birlikte A2–A3 standart sapması 0,1323 A'dan 0,1906 A'ya yükselmiştir. Kanal farkı büyümüş, kanal farkı standart sapması düşmüştür. Boşta pik aralıkları da benzer kalmıştır. Dolayısıyla ortalama doğruluk korunurken dalgalanma karakteri değişmiştir; biasın gürültüyü azalttığı söylenemez.

100 W sınıfı ESP32 bias testinde A2–A3 MAPE %5,184, diğer SCT kolu %9,597 bulunmuştur. ESP32 biaslı kol PZEM'e daha yakındır; ancak bu 100 W testinde aynı yükte trafolu bias karşılaştırması yapılmadığından bias kaynağının değişim etkisi izole edilmemiştir.

**Sonuç:** Kettle 2 ve 100 W verileri ESP32 biasın bu çalışma noktalarında kullanılabilir olduğunu ve ortalama ölçüm doğruluğunda belirgin olumsuz etki göstermediğini destekler. Anlık dalgalanma ve boşta pik davranışı açık konudur. PZEM ground truth değildir. K=27.59 ve çalışan YAML/firmware korunmuştur.

Ayrıntılı rapor: `V1.1/RAPOR/V1.1-ESP32-BIAS-KETTLE2-TRAFOLU-KARSILASTIRMA-VE-100W-DEGERLENDIRME-2026-11-21.md`.


## 2026-11-21 – ESP32 bias 15 W deneyi sonucu

`history (19)(1).csv` analiz edildi. İlk 3 saniye çıkarıldıktan sonra A2–A3 ESP32 bias kanalının ortalaması 0.060924 A, medyanı 0.060054 A, CV değeri %6.276'dır. Diğer SCT kanalının ortalaması 0.058321 A, medyanı 0.058056 A, CV değeri %3.611'dir.

PZEM akımında yalnızca 3 örnek (ortalama 0.064333 A) bulundu. ±2 saniye eşleştirmeli MAPE A2–A3 için %8.157, diğer kanal için %8.900'dür; örnek sayısı düşük olduğundan bu fark kesin doğruluk kanıtı değildir.

Önceki 15 W deneyindeki A2–A3 medyanı 0.060014 A iken yeni oturumda 0.060054 A bulunmuştur. Önceki 0.516451 A spike tekrarlanmamış; yeni maksimum 0.080796 A olmuştur. Buna rağmen A2–A3 CV değeri diğer kanaldan yüksektir.

Ortalama bazlı kaba katsayı 29.13 hesaplanabilse de PZEM akım örneği yalnızca üç olduğu için kabul edilmemiştir. **K=27.59, firmware ve YAML korunmuştur.** Biaslı kanalın ölçüm seviyesi tekrarlanmış; kararlılık iyileşmesi gösterilmemiştir.

Rapor: `V1.1/RAPOR/V1.1-ESP32-BIAS-15W-2026-11-21.md`  
Özet: `V1.1/LOG/V1.1-ESP32-BIAS-15W-OZET-2026-11-21.csv`

## 2026-11-22 – ADS1115 ikili okuma yavaş salınım araştırması KAPATILDI

A0–A1 ve A2–A3 kanallarında gözlenen, PZEM çizgisine kıyasla belirgin yavaş salınım için ayrı deney açıldı. Kullanıcının saha bildirimine göre ESP32D2 resetlendikten sonra salınım durdu.

**Sonuç ve sınır:** Reset sonrasında belirtinin kaybolması kaydedildi; bu durum ESP32/ADS1115/ESPHome çalışma oturumuyla ilişkili olasılığı güçlendirir, ancak kök nedeni kanıtlamaz. I²C, ADS1115 dönüşüm sırası, yazılım zamanlaması veya besleme kaynaklarından hiçbiri doğrulanmış neden olarak ilan edilmedi. Filtre veya örnekleme ayarı değiştirilmedi; K=27.59 ve V1.1 YAML korundu.

history (25).csv kısa Karma 1 kaydı deney raporuna eklendi. PZEM akımı ve gücü kayıt boyunca değişken olduğundan kalibrasyon noktası olarak kullanılmadı.

**Kalıcı işletim dersi:** Açıklanamayan çok kanallı salınımda önce ham veri/log ve mevcut ayarlar korunur; sonra kontrollü ESP32 reseti uygulanabilir. Reset sonrası belirti kaybolursa bu müdahale ve gözlem kaydedilir; kök neden bulunduğu iddia edilmez. Belirti tekrarlarsa reset öncesi/sonrası karşılaştırmalı yeni inceleme açılır.

Deney raporu: PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/ADS1115-IKILI-OKUMA-YAVAS-SALINIM-ARASTIRMASI-2026-11-22.md.

Bu deney kapatılmıştır; MOD2-GRV001 görevinin tamamı kapatılmamıştır.

## 2026-11-22 – 150 W sabit yük / iki kanallı referans kaydı

Kullanıcının sağladığı `history (27).csv` analiz edildi ve 150 W sabit yük deneyi referans kaydı olarak arşivlendi. Kayıt 00:55:00–00:58:54 Türkiye saati aralığındadır; PZEM sıfır/geçiş örnekleri karşılaştırma istatistiklerinden çıkarılmıştır.

- PZEM güç: 150.981 W ortalama (36 sıfır dışı örnek).
- PZEM akım: 0.64913 A ortalama (15 sıfır dışı örnek).
- A0–A1: 0.59877 A ortalama, CV %1.462 (236 örnek).
- A2–A3: 0.60157 A ortalama, CV %0.936 (235 örnek).
- Kanalların ortalama farkı: 0.00280 A.
- PZEM'e ±2 saniye en yakın örnek eşleştirmesinde 15 eşleşme: A0–A1 MAPE %8.061; A2–A3 MAPE %7.065.

**Yorum sınırı:** İki kanal aynı oturumda aktifti. Bu kayıt çift kanal referansıdır; tek kanal okuma hipotezini sınamaz. A2–A3 CV değeri bu oturumda daha düşük görünse de tek kayıt kalıcı üstünlük kanıtı değildir. PZEM ground truth değildir. K=27.59, firmware ve YAML değiştirilmedi.

**Sonraki adım:** Aynı sabit yükte yalnız A0–A1, ardından yalnız A2–A3 aktif olacak şekilde ayrı deney kopyalarıyla en az 3'er dakikalık kayıt alınması. Mevcut çalışan iki kanallı YAML korunacak.

Rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/150W-SABIT-YUK-IKILI-KANAL-REFERANS-2026-11-22.md`  
Özet CSV: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/LOG/150W-SABIT-YUK-IKILI-KANAL-OZET-2026-11-22.csv`  
Ham kaynak `history (27).csv` bu konuşmadaki ek dosya olarak korunmaktadır; GitHub'a birebir kopyalanmamıştır.


## 2026-11-22 – 150 W tek kanal A0–A1 deneyi analiz edildi

Kullanıcının sağladığı `history (28).csv` kaydı analiz edildi. ESP32D2 A0–A1 akım sensöründe 197 örnek, PZEM güçte 31 örnek ve PZEM akımda 11 örnek vardır. Kayıt 195.26 saniyedir. İlk 10 saniye çıkarıldıktan sonra A0–A1 ortalaması 0.583896 A, standart sapması 0.005455 A, CV %0.9343, min–max 0.574581–0.598334 A'dır. PZEM güç ortalaması 149.552 W; PZEM akım ortalaması 0.647182 A'dır. ±2 saniye zaman eşleştirmesinde 40 çift ve MAPE %9.54 elde edilmiştir.

Önceki 150 W çift kanal referansında A0–A1 ortalaması 0.598765 A ve CV %1.462 idi. Tek kanal oturumunda ortalama daha düşük, CV daha küçüktür. Farkın nedeni belirlenmemiştir; bu iki ayrı oturum tek başına çift kanal zamanlamasını kök neden olarak kanıtlamaz.

Kaynak CSV'de Modül 3 SSR durum geçişleri ve BERO_EVT kayıtları da bulunur. SSR ON/OFF geçişleri kayıt süresince tekrarlanmıştır. PZEM güç 148.3–150.5 W aralığında kalmıştır; SSR'nin bu deney yükünü kontrol edip etmediği CSV'den kesin olarak çıkarılamaz. Bu nedenle yükün kesintisiz sabit kaldığı varsayılmamıştır.

K=27.59, 860 SPS, 200 ms pencere ve 1 s güncelleme korunmuştur. Filtre veya firmware ayarı değiştirilmedi. Rapor ve A0–A1 tek kanal deney YAML kopyası depoya kaydedildi. Özet CSV de kaydedildi; orijinal 311 satırlık `history (28).csv` konuşma eki olarak korunmaktadır. Depoya orijinal dosyanın birebir kopyası değil, seçilmiş ölçüm/olay alt kümesi ayrıca kaydedilmesi planlanmıştır.

Rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/150W-TEK-KANAL-A0A1-2026-11-22.md`  
YAML: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/V1.1-TEST-A0A1.yaml`  
Özet CSV: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/LOG/150W-TEK-KANAL-A0A1-OZET-2026-11-22.csv`


## 2026-11-22 – 150 W tek kanal A2–A3 deney YAML'ı hazırlandı

A0–A1 tek kanal testinden sonra aynı ölçüm ayarlarıyla A2–A3'ü tek başına çalıştırmak üzere ayrı YAML kopyası oluşturuldu.

- Multiplexer: A2_A3
- PGA: 2.048 V
- Sample rate: 860 SPS
- ct_clamp penceresi: 200 ms
- Güncelleme: 1 s
- K: 27.59
- A0–A1 bu YAML içinde tanımlı değildir.
- A2–A3 bias devresi ve fiziksel bağlantısı değiştirilmez.

Bu dosya yalnızca hazırlanıp depoya kaydedilmiştir; derleme, cihaza yükleme ve ölçüm henüz doğrulanmamıştır. A0–A1 deneyiyle karşılaştırmada aynı yük, sensör konumu, bias bağlantısı ve kayıt süresi korunmalıdır.

YAML: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/V1.1-TEST-A2A3.yaml`


## 2026-11-22 – 150 W tek kanal A2–A3 deneyi analiz edildi

Kullanıcının sağladığı `history (30).csv` (315 satır) analiz edildi. Kayıt 01:11:00–01:14:11.709 Türkiye saati aralığındadır. İlk 10 saniye çıkarıldıktan sonra A2–A3 için 182 örnek kaldı: ortalama 0.589707 A, medyan 0.589793 A, standart sapma 0.006573 A, CV %1.1146, min–max 0.571915–0.602744 A.

PZEM güç: 32 örnekte ortalama 147.403 W; PZEM akım: 13 örnekte ortalama 0.643615 A; PZEM gerilim: 31 örnekte ortalama 229.010 V. A2–A3/PZEM akım ±2 saniye en yakın zaman eşleştirmesinde 52 çift, MAPE %8.510 ve ortalama fark −0.05477 A bulundu. PZEM ground truth değildir.

CSV'de SSR ve BERO_EVT geçişleri 01:11:00 ON, 01:11:22 OFF, 01:11:42 ON, 01:12:22 OFF, 01:12:42 ON, 01:13:22 OFF, 01:13:42 ON olarak kaydedilmiştir. SSR'nin deney yükünü kontrol edip etmediği dosyadan kesinleşmediğinden yükün kesintisiz sabit kaldığı varsayılmadı.

A0–A1 tek kanal kaydının CV'si %0.9343; bu A2–A3 tek kanal kaydının CV'si %1.1146'dır. Ayrı oturumlar arasında A0–A1 daha az değişken görünmüştür; bu fark kök neden veya genel kanal üstünlüğü kanıtı değildir. Önceki çift kanal A2–A3 referansındaki CV %0.936 idi; bu tek kanal oturumunda daha yüksek CV gözlenmiştir.

K=27.59, 860 SPS, 200 ms pencere ve 1 s güncelleme korunmuştur. Filtre veya firmware değişikliği yapılmadı.

Rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/150W-TEK-KANAL-A2A3-2026-11-22.md`  
Özet CSV: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/LOG/150W-TEK-KANAL-A2A3-OZET-2026-11-22.csv`  
Orijinal `history (30).csv` konuşma eki olarak korunur; bu işlemde GitHub'a birebir kopyalanmamıştır.


## 2026-11-22 – İki aşamalı katsayı çarpımı değerlendirmesi KAPATILDI

Kullanıcının önerisi, bias devresiyle uğraşmak yerine mevcut katsayının iki parçaya ayrılarak ardışık çarpılmasıydı. Değerlendirme sonucunda, K1 ve K2 sabit çarpanlar olup yalnızca K1 × K2 = K koşulunu sağlıyorsa RMS(ADC) × K1 × K2 ifadesinin mevcut RMS(ADC) × K hesabıyla matematiksel olarak aynı olduğu belirlendi. Bu işlem tek başına ölçüm hatasını, gürültüyü veya bias ihtiyacını değiştirmez.

Bias analog sinyalin ADC giriş referans/çalışma noktasını etkiler; sabit çarpanlar ise ölçüm sonucunu ölçekler. Dolayısıyla iki sabit katsayı biasın yerine geçen çözüm olarak kabul edilmedi. İki katsayılı yapı ancak her katsayının ayrı ve ölçülebilir bir fiziksel/kalibrasyon anlamı tanımlanırsa ileride değerlendirilebilir.

**Karar:** Bu önerinin matematiksel değerlendirmesi kapatıldı. Fiziksel deney yapılmadı ve yeni ölçüm/log üretilmedi. K=27.59, çalışan YAML, firmware ve mevcut bias bağlantısı değiştirilmedi. Bu kapanış MOD2-GRV001 görevinin tamamlandığı anlamına gelmez.

Rapor: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/KATSAYI-IKI-ASAMALI-CARPIM-DEGERLENDIRMESI-2026-11-22.md`.


## 2026-11-22 – İki bölgeli katsayı ve bias kullanmama kararı

Kullanıcı kararıyla kalibrasyon çalışması iki akım bölgesine ayrılacaktır: 1,5 A altı için ayrı katsayı, 1,5 A üstü için ayrı katsayı belirlenecektir. Bias devresinin sağladığı katkı, getirdiği donanım/bağlantı zahmetine değmediğinden yeni tasarım yaklaşımında bias tercih edilmeyecektir; daha basit analog ölçüm yolu esas alınacaktır.

**Durum:** Bu bir tasarım kararıdır; katsayı deneyleri henüz yapılmamıştır. K=27.59 şimdilik korunur. Ölçüm verisi olmadan düşük/yüksek bölge katsayıları atanmayacak, çalışan YAML ve firmware değiştirilmeyecektir. Önce bias kullanılmayan bağlantının güvenliği ve ADS1115 girişlerinin mutlak gerilim sınırları doğrulanmalıdır.

**Deney planı:** 1,5 A altı ve üstünde birden fazla yük noktası ölçülecek; 1,5 A çevresi ayrıca incelenecek. Her iki katsayı PZEM karşılaştırma referansıyla hesaplanıp farklı yük noktalarında doğrulanacaktır. PZEM ground truth değildir. Tam 1,5 A sınırında katsayı seçimi, bölge seçimini yapacak ölçüm ve geçişte çıktı sürekliliği henüz kararlaştırılmamıştır.

Eski bias deneyleri tarihsel kanıt olarak korunur; yeni tasarım tercihi geçmiş sonuçları silmez. Bu karar MOD2-GRV001 görevinin tamamlandığı anlamına gelmez.

Ayrıntılı karar ve deney planı: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/IKI-BOLGELI-KALIBRASYON-VE-BIAS-KARARI-2026-11-22.md`.
