# Modül 2 – Masaüstü 4 Kanal / Akım Testleri – Tarihçe

Bu dosya modülün görevleri boyunca edinilen tecrübeyi ve gelişim sürecini kronolojik olarak kaydeder.

## Kayıt standardı

Her kayıt aşağıdaki bilgileri içermelidir:

- **Tarih:**
- **Görev kimliği:**
- **Çalışma / deneme:**
- **Gözlenen sonuç:**
- **Edinilen tecrübe:**
- **Teknik karar:**
- **İlgili kayıtlar:** YAML sürümü, LOG ve RAPOR yolları

Başarısız, sonuçsuz veya henüz doğrulanmamış çalışmalar da kaydedilir. Sonuçlar olduğundan başarılı veya doğrulanmış gösterilmez. **Tarihçe, test loglarının veya raporların kopyası değildir.** Log ve raporların ne gösterdiğini, bunlardan ne öğrenildiğini ve hangi teknik sonuca/karara ulaşıldığını özetler. Ham loglar ve ayrıntılı raporlar kendi sürüm klasörlerinde korunur; tarihçe ilgili kayıtlara referans verir.

---

## Kronolojik kayıtlar

### 2026-11-21 – MOD2-GRV001 – Masaüstü donanım düzeninin tanımlanması

- **Çalışma / deneme:** ESP32-D geliştirme kartı ve ESP32 shield üzerine kurulu masaüstü düzenin donanım kapsamı netleştirildi. SCT013 30A/1V akım sensörü ve ADS1115 ara ADC sinyal zincirine dahil edildi.
- **Gözlenen sonuç:** Kullanıcının paylaştığı fotoğrafta ESP32-D kartının shield üzerine takılı olduğu ve ADS1115 modülünün kablolarla düzeneğe bağlandığı görülüyor. SCT013 sensör fotoğrafta görünmüyor.
- **Edinilen tecrübe:** Fiziksel yerleşim fotoğrafla belgelenebilir; ancak fotoğraf tek başına ADS1115 pin eşleşmelerini, besleme değerlerini, analog giriş bağlantısını veya sistemin çalıştığını doğrulamaz.
- **Teknik karar:** Sinyal zinciri SCT013 30A/1V → ADS1115 → ESP32-D olarak kaydedildi. Gerçek pin eşleşmeleri ve elektriksel bağlantılar ayrı ayrı doğrulanmadan şema veya çalışan sistem olarak ilan edilmeyecek.
- **İlgili kayıtlar:** `PREBERO/MODUL-2-AKIM-TESTLERI/IMALAT/IMALAT.md`; `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/GOREV.md`.


### 2026-11-21 – MOD2-GRV001 – Osiloskopla yüksüz biaslı SCT ölçümü

- **Çalışma / deneme:** Bias bağlı ve yük kapalı durumdayken osiloskop CH1 üzerinden altı ayrı Single yakalama alındı. Her yakalamanın Vrms değeri kaydedildi.
- **Gözlenen sonuç:** Vrms değerleri sırasıyla 1.60, 5.39, 5.01, 5.07, 1.05 ve 2.29 mV oldu. Altı ölçümün aritmetik ortalaması 3.4017 mV (yaklaşık 3.40 mV), aralık 1.05–5.39 mV olarak hesaplandı.
- **Edinilen tecrübe:** Yüksüz biaslı durumda altı Single yakalamasının Vrms değerleri belirgin saçılım gösterdi. 3.40 mV yalnızca bu altı yakalamanın ortalamasıdır; kalıcı gürültü tabanı veya sıfır düzeltme değeri olarak kabul edilmedi.
- **Teknik karar:** Aynı osiloskop ayarları ve bias bağlantısı korunarak yük kademelerinde de altışar Single ölçüm alınacak. PZEM akımı aynı yük koşulunda kaydedilecek. Akım hesabı, sıfır düzeltmesi veya katsayı kararı bu yüksüz veriyle tek başına verilmeyecek.
- **İlgili kayıtlar:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/TESTLER/OSILOSKOP-YUKSUZ-BIAS-2026-11-21.md`.


### 2026-11-21 – MOD2-GRV001 – Bias bağlı osiloskop yük kademeleri

- **Çalışma / deneme:** Bias bağlantısı korunarak 42 W, 57 W, 100 W ve 150 W yüklerinde altışar Single yakalama alındı. Yüksüz seri ayrı raporda tutuldu.
- **Gözlenen sonuç:** Vrms ortalamaları 42 W için 6.5417 mV, 57 W için 9.2983 mV, 100 W için 16.5700 mV ve 150 W için 22.8383 mV oldu. 100 W ve 150 W kademelerinin beş osiloskop parametresi de tek tek kaydedildi.
- **Edinilen tecrübe:** Vrms yükle düzenli artış gösterdi. 57 W serisinde 9.71 mV tekil okuma diğer beş değerden ayrıştı; ham veri korunmuştur. Nominal güç hesabı ile yapılan karşılaştırma yaklaşık bir ön kontroldür.
- **Teknik karar:** Osiloskop yük kademeleri tamamlandı. Bu sonuçlar ADS1115 başarısını kanıtlamaz ve PZEM ile doğrulanmış kalibrasyon değildir. Sıradaki deney aynı SCT/bias/yük koşullarında ADS1115 No. 1 A0-A1 ham diferansiyel gerilim okumasıdır; ilk aşamada RMS, akım katsayısı, sıfır düzeltmesi ve filtre uygulanmayacaktır.
- **İlgili kayıtlar:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/TESTLER/OSILOSKOP-YUK-KADEMELERI-BIAS-2026-11-21.md`; `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/GOREV.md`.


### 2026-11-21 – MOD2-GRV001 – ADS1115 biaslı/biassız ham okuma deneyi açıldı

- **Çalışma / deneme:** Aynı faz iletkenini aynı yönde ölçecek iki ayrı SCT013 30A/1V sensörüyle, tek ADS1115 No. 1 üzerinde biaslı ve biassız iki diferansiyel kolun ham okuma karşılaştırması için deney açıldı.
- **Gözlenen sonuç:** Henüz ölçüm yapılmadı. Bu kayıt yalnızca deney planının açıldığını gösterir.
- **Edinilen tecrübe:** Önceki konuşmada A2-A3 kolunun tek SCT ile biaslı bağlantı gibi yorumlanması yanlıştı. Depodaki görev tanımı ve güncel karar esas alınarak doğru deney düzeni netleştirildi: SCT No. 1 A0-A1 biaslı; SCT No. 2 A2-A3 biassız. Fark, yalnızca bir kolda SCT dönüş ucunun 1,65 V bias orta noktasına bağlanmasıdır.
- **Teknik karar:** Mevcut çalışan akım ölçüm kodu korunacak. İlk deneyde ham ADS1115 okumaları karşılaştırılacak; RMS/akım dönüşümü, katsayı, sıfır düzeltmesi ve filtre uygulanmayacak. A2/A3 mutlak giriş gerilimleri ve ADS1115 sınırları doğrulanmadan biassız kol bağlanmayacak.
- **İlgili kayıtlar:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/GOREV.md`; `PREBERO/DURUM.md`.


### 2026-11-21 – MOD2-GRV001 – ADS1115 iki kanal denemesi bağlantı sorunu nedeniyle geçersiz

- **Çalışma / deneme:** ADS1115 No.10 üzerinde A0-A1 ve A2-A3 kanallarını iki ayrı `ct_clamp` bileşeniyle okuyan deneme çalıştırıldı; kullanıcı bağlantı sorunu bildirdi.
- **Gözlenen sonuç:** A0-A1 yaklaşık 0.45–0.50 A civarında seyrederken A2-A3 yaklaşık 0.494 A'dan 1.357 A'ya yükseldi. 200 ms pencerede çoğunlukla kanal başına 25 örnek raporlandı.
- **Edinilen tecrübe:** Kayıt geçerli bias/biassız karşılaştırma veya kalibrasyon verisi değildir. Log kök nedeni tek başına açıklamaz.
- **Teknik karar:** Deney baştan kurulacak. Katsayı çıkarılmayacak. Çalışan tek kanallı V1.1 YAML korunacak. İki kanallı denemenin tam YAML kaynak dosyası logda bulunmadığından tahmin edilerek oluşturulmayacak.
- **Donanım kimliği:** Bu kurulum ADS1115 No.10 olarak kaydedilecek; görevdeki eski No.1 atıfları bu denemeye uygulanmayacak.
- **İlgili kayıt:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/ADS1115-IKILI-OKUMA-BAGLANTI-HATALI-2026-11-21.md`.


### 2026-11-21 – MOD2-GRV001 – Bias katkısını teyit için üçüncü çapraz deney açıldı

- **Çalışma / deneme:** İlk iki bias kanal çaprazlamasının ardından, biaslı kolun ölçüm ortalamasındaki farkı tekrar takip edip etmediğini sınamak üzere üçüncü deney planlandı.
- **Gözlenen sonuç:** Henüz fiziksel ölçüm yapılmadı. İlk iki deneyde biaslı kol sırasıyla A2–A3 ve A0–A1 olduğunda yüksek ortalama da ilgili biaslı kolda görüldü.
- **Edinilen tecrübe:** İki çapraz gözlem biasın ölçüm sonucunu etkilediği hipotezini destekliyor; üçüncü tekrar aynı örüntünün tekrarlanabilirliğini değerlendirecek. Gürültü azalması henüz tutarlı biçimde gösterilmiş değil.
- **Teknik karar:** Üçüncü deneyde A0–A1 biassız, A2–A3 biaslı olacak. Bias beslemesi Modül 1'de kalacak; ESP32'den besleme ayrı deney olacak. Aynı SCT'ler, konum/yön, yük, ESP32D2, ADS1115 No.10, YAML ve K=27.59 korunacak.
- **İlgili kayıtlar:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/BIAS-KANAL-TEKRAR-CAPRAZ-DENEY-2026-11-21.md`; önceki çapraz deney raporu `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/RAPOR/V1.1-BIAS-KANAL-CAPRAZ-2026-11-21.md`.


### 2026-11-21 – MOD2-GRV001 – Bias kanal tekrar çapraz deneyi (3. tekrar)

- **Çalışma / deneme:** İlk iki bias kanal çaprazlamasının ardından üçüncü tekrarın HA geçmiş verisi `history (10).csv` analiz edildi.
- **Gözlenen sonuç:** 199 A0–A1 örneğinin ortalaması 0.459638 A; 199 A2–A3 örneğinin ortalaması 0.472490 A; 15 PZEM akım örneğinin ortalaması 0.469267 A oldu. ±2 saniye zaman eşleştirmesinde MAPE A0–A1 için %2.508, A2–A3 için %1.819 bulundu.
- **Edinilen tecrübe:** Deney planındaki A0–A1 biassız / A2–A3 biaslı eşlemesi doğruysa üçüncü tekrar da biaslı kolda daha yüksek ortalama ve daha düşük PZEM MAPE örüntüsünü göstermektedir. Üç deney birlikte biasın yaklaşık 0.47 A bölgesindeki ölçüm ortalamasına pozitif katkı yaptığı hipotezini güçlendirir. PZEM ground truth değildir.
- **Gürültü yorumu:** Üçüncü deneyde CV A0–A1 için %1.871, A2–A3 için %2.138 oldu. Biaslı kol daha değişkendir; biasın gürültüyü azalttığı sonucu çıkarılamaz.
- **Teknik karar:** K=27.59 korunmuştur; yeni kalibrasyon katsayısı hesaplanmamıştır. Daha geniş akım aralığı için test gereklidir. Üçüncü deneyde fiziksel kablo eşlemesi ayrıca teyit edilmelidir.
- **Kaynak sınırı:** Ham HA CSV arşivlendi; ayrı ESPHome logu bu veri paketinde sunulmadı.
- **İlgili kayıtlar:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/LOG/V1.1-BIAS-KANAL-TEKRAR-HA-KAYNAK-2026-11-21.csv`; eşleştirme CSV'si `V1.1/LOG/V1.1-BIAS-KANAL-TEKRAR-PZEM-ESLESTIRME-2026-11-21.csv`; rapor `V1.1/RAPOR/V1.1-BIAS-KANAL-TEKRAR-2026-11-21.md`.


### 2026-11-21 – MOD2-GRV001 – Bias çapraz deney serisi nihai tespit

- **Çalışma / deneme:** Aynı iki SCT013 sensörü ve ADS1115 No.10 üzerinde bias A0–A1 ve A2–A3 kanalları arasında çaprazlanarak üç tekrar değerlendirildi.
- **Gözlenen sonuç:** Üç deneyin tamamında biaslı kanalın ortalaması daha yüksek, PZEM karşılaştırmasına göre MAPE değeri daha düşüktür. Biaslı/biassiz MAPE sırasıyla deney 1: %1.016/%3.262; deney 2: %1.275/%3.168; deney 3: %1.819/%2.508.
- **Edinilen tecrübe:** İlk iki çaprazlamada bias kanalı değiştiğinde yüksek ortalamanın biaslı kanalı takip etmesi, kanal etkisi ile bias etkisini ayırmaya yardımcı oldu. Üçüncü deneyde A0–A1 biassız / A2–A3 biaslı bağlantısı kullanıcı tarafından teyit edildi.
- **Teknik karar:** Yaklaşık 0.47 A çalışma noktasında biasın ölçüm sonucuna pozitif katkısı kabul edildi. PZEM ground truth değildir; mutlak doğruluk iddiası yoktur. Gürültü azalması gösterilmemiştir. K=27.59 korunmuştur.
- **Kapanış:** 100 W bias kanal çapraz deney serisi üç tekrar sonunda tamamlandı ve kapatıldı. ESP32'den bias besleme ve diğer akım bölgeleri ayrı araştırma konularıdır.
- **İlgili kayıtlar:** Üçüncü deney raporu PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/RAPOR/V1.1-BIAS-KANAL-TEKRAR-2026-11-21.md; çapraz deney kaydı PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/BIAS-KANAL-TEKRAR-CAPRAZ-DENEY-2026-11-21.md.


### 2026-11-21 – Biaslı kanal boşta spike gözlemi

- **Kaynak:** Home Assistant zaman grafiği ekran görüntüsü; 21:51–21:59.
- **Yük altında:** Yaklaşık 0.46–0.48 A ve yükün yeniden geldiği yaklaşık 0.19 A bölümünde iki ADS1115 kanalı PZEM'e yakın görünmektedir.
- **Yüksüz durumda:** PZEM sıfıra inerken A0–A1 biassız kanal sıfıra yakın ve daha sakin; A2–A3 biaslı kanalda pozitif spike'lar görülür.
- **Tecrübe:** Biasın yük altındaki olumlu ölçüm katkısı, boşta spike davranışından ayrı değerlendirilmelidir.
- **Sınır:** Görsel nitel kanıttır; ham CSV ile spike sayısı/genliği henüz hesaplanmamıştır.
- **Takip:** Uzun süreli boşta kayıtta spike sıklığı ve genliği iki kanalda karşılaştırılacaktır.

### 2026-11-21 – Kettle 1 / Kettle 2 ve bias kullanım kararı

Kettle 1 sıcaklık koruma modu ve Kettle 2 kaynatma modu ayrı sabit çalışma koşulları olarak değerlendirildi. Kullanıcı daha fazla kettle testine gerek olmadığına ve biasın gerekli olduğuna karar verdi. Biaslı kanalın PZEM'e yakınlığı lehine gözlemler korunurken boşta spike ve 15 W tekil spike bulguları da kararın sınırları olarak kaydedildi. Biasın gürültüyü azalttığı iddia edilmez. K=27.59, çalışan YAML ve 0.020 A eşiğinin uygulanmaması kararı korunur.

### 2026-11-21 – ESP32 kaynaklı bias ve ortak GND deneyi açıldı

Bias ESP32 3.3 V hattından sağlanacak; ESP32 GND, ADS1115 GND ve bias devresi GND ortaklanacak. Önceki Modül 1 bias deneylerinde bu ortak GND koşulu kullanılmamıştı. Bu nedenle yeni deneyde bias kaynağı ve ortak toprak referansı farkı birlikte not edilecek. Direnç değerleri, fiziksel bağlantı ve bias DC seviyesi henüz teyit edilmedi. K=27.59 ve çalışan YAML korunacak. Deney henüz ölçüm aşamasına geçmedi. Ayrıntı: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/ESP32-KAYNAKLI-BIAS-ORTAK-GND-2026-11-21.md`.

### 2026-11-22 – İki aşamalı katsayı çarpımı önerisi değerlendirildi ve kapatıldı

- **Çalışma / deneme:** Mevcut kalibrasyon katsayısını iki sabit katsayıya ayırıp çarpmanın bias yerine geçip geçemeyeceği matematiksel olarak değerlendirildi.
- **Gözlenen sonuç:** RMS(ADC) × K1 × K2, K1 × K2 = K ise RMS(ADC) × K ile aynıdır. Katsayının iki parçaya ayrılması tek başına yeni ölçüm bilgisi veya düzeltme sağlamaz.
- **Edinilen tecrübe:** Bias analog sinyalin ADC giriş referansını/çalışma noktasını etkiler; sabit katsayı çarpımı yalnızca sonucu ölçekler. İki katsayı ancak ayrı fiziksel veya kalibrasyon anlamları ve bağımsız belirleme yöntemleri varsa anlamlıdır.
- **Teknik karar:** Öneri, biasın yerine geçen yöntem olarak kabul edilmedi ve bu haliyle kapatıldı. K=27.59, YAML, firmware ve bias bağlantısı değiştirilmedi.
- **Kanıt sınırı:** Fiziksel test yapılmadı; yeni ölçüm, ham log veya kalibrasyon sonucu yoktur. Bu kayıt matematiksel yöntem değerlendirmesidir.
- **İlgili kayıt:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/KATSAYI-IKI-ASAMALI-CARPIM-DEGERLENDIRMESI-2026-11-22.md`.


### 2026-11-22 – İki bölgeli kalibrasyon ve bias kullanmama kararı

- **Çalışma / karar:** Kullanıcı, 1,5 A altı ve üstü için ayrı kalibrasyon katsayıları çalışılmasını; bias devresinin getirdiği zahmet nedeniyle yeni tasarımda bias tercih edilmemesini kararlaştırdı.
- **Gözlenen sonuç:** Bu aşamada yeni ölçüm yapılmadı. İki katsayının değeri henüz bilinmiyor.
- **Edinilen tecrübe:** Önceki bias deneylerinde bazı çalışma noktalarında ölçüm ortalamasına katkı gözlense de boşta spike ve değişkenlik sorunları da kaydedilmişti. Kullanıcı, bu katkıyı ek devre karmaşıklığına değer bulmadı.
- **Teknik karar:** Sade analog bağlantı ve iki bölgeli kalibrasyon yaklaşımı izlenecek. K=27.59, çalışan YAML ve firmware şimdilik korunacak. Yeni katsayılar yalnızca ölçümle belirlenecek.
- **Açık noktalar:** Tam 1,5 A sınırının hangi bölgeye dahil olacağı, bölge seçiminin nasıl yapılacağı ve geçişte çıktı sürekliliği testle/yazılım tasarımıyla belirlenecek.
- **Kanıt sınırı:** Bu bir tasarım kararıdır; biasın fiziksel olarak söküldüğü veya iki bölgeli kalibrasyonun doğrulandığı anlamına gelmez.
- **İlgili kayıt:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/IKI-BOLGELI-KALIBRASYON-VE-BIAS-KARARI-2026-11-22.md`.


### 2026-11-22 – MOD2-GRV001 – Birleşik 42/57/100/150 W kararlı kademe analizi

- **Çalışma / deneme:** Kullanıcının sağladığı `150-42-57-100.csv` dosyasında PZEM akımının sıfır olmadığı ve açılış/kapanış geçişleri dışında kalan dört kararlı pencere yeniden hesaplandı.
- **Gözlenen sonuç:** A0–A1 için K değerleri 42 W'da 33.58, 57 W'da 33.30, 100 W'da 30.65 ve 150 W'da 30.00 bulundu. 42/57 W ile 100/150 W grupları arasında belirgin katsayı ayrışması var.
- **Ek gözlem:** 100 W penceresi homojen değil. İlk yaklaşık 230 saniyede A0–A1 ortalaması 0.430886 A (K≈30.13), sonraki bölümde 0.418343 A (K≈30.97); PZEM iki bölümde de yaklaşık 0.470 A. Tüm pencerenin K=30.65 değeri iki alt seviyeyi birleştiriyor.
- **Edinilen tecrübe:** Kararlı PZEM akımı, A0–A1 ölçümünün pencere boyunca sabit kaldığını garanti etmiyor. 100 W içindeki seviye değişimi ayrıca açıklanmadan tek katsayı yorumuna dahil edilmemeli.
- **Teknik karar:** Katsayılar ön sonuç olarak tutuldu. Bias ve YAML sürümü birleşik CSV'den kesin doğrulanamadığı için seri biassız/aynı konfigürasyonla doğrulanmış ilan edilmedi. K=27.59 ve mevcut YAML değişmedi; tek ortak düşük bölge katsayısı seçilmedi.
- **İlgili kayıt:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/150-42-57-100-BIRLESIK-KADEME-ANALIZI-2026-11-22.md`; katsayı geçmişi `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/RAPORLAR/KATSAYI-RAPORU-ADS1115-NO10-SCT013.md`.


## 2026-11-22 – İleride PF etkisi araştırması: trimpotlu faz kaydırma düzeneği

Kullanıcı, mevcut akım kalibrasyonu ve negatif eğimli K fonksiyonu çalışmasından ayrı olarak, elindeki trimpotlu düzeneği ileride PF etkisini incelemek için kullanma fikrini kaydetti. Mevcut kalibrasyonun başarı ölçütü PZEM karşılaştırmasına göre ±%4 hata zarfıdır; PF düzeltmesi şimdilik fonksiyona eklenmeyecek. Ampul/birleşik ampul ve vantilatör doğrulamaları mevcut çalışma kapsamında kalacak; PF araştırması ayrı deney serisi olacaktır.

Trimpotun gerçek devre topolojisi, oluşturduğu faz kayması ve PF ayar aralığı henüz doğrulanmadı. Gelecekte şema/bağlantı incelenmeli, osiloskopla faz ilişkisi ve dalga şekli gözlenmeli; PZEM gerilim, akım, aktif güç ve PF değerleri SCT/ADS1115 ile birlikte kaydedilmelidir. Faz kaydırma devresi gerçek motorlu yük PF davranışıyla otomatik olarak eşdeğer sayılmayacaktır. Fiziksel deney yapılmadı; sonuç veya PF katsayısı üretilmedi.

Ayrıntılı plan: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/ILERIDE-PF-ETKISI-TRIMPOT-DENEY-PLANI.md`.

 
## 2026-11-22 – İki bölgeli/parçalı kalibrasyon yaklaşımı kapatıldı; V1.6 tek fonksiyon referans alındı

Önceki tasarım planında 1,5 A altı ve üstü için ayrı katsayılar ve arada bölge geçişi öngörülmüştü. Bu yaklaşım, V1.6 tam aralık testleri sonrasında **uygulama adayı olmaktan çıkarıldı ve kapatıldı**.

Yerine, aynı ölçüm zincirinde 0,065–17,52 A aralığındaki karma yük verileriyle geliştirilen tek fonksiyon kabul edildi:

`K(x) = 26.89 + 5.39 × exp(-x / 0.882)`

V1.6 YAML bu fonksiyonu parçalı bölge seçimi olmadan uygular; 30 mA ve altını Home Assistant'ta 0.000 A yayımlar. V1.6 doğrulama raporu, seçilmiş kademe sonuçları, 23 kademelik genel grafik ve 1:1 karşılaştırma grafiği için esas kayıttır:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.6/RAPOR/V1.6-TAM-ARALIK-TEK-FONKSIYON-DOGRULAMA-2026-11-22.md`.

**Kapanış kararı ve sınırlar**
- İki bölgeli katsayı yöntemi, V1.6 tek fonksiyon modeliyle ikame edildiği için kapatıldı; eski plan ve deney kayıtları silinmedi.
- 1,5 A bölge sınırı ve parçalı geçiş mantığı artık aktif tasarım gereksinimi değildir.
- V1.6, ADS1115 No.10 + SCT013 30A/1V + ESP32D2 + A0–A1 ölçüm zinciri için referans kalibrasyon modeli olarak korunur.
- Yaklaşık 15 W noktası SCT013'ün pratik alt ölçüm sınırına yakın kabul edilir; bu nokta için eğri yeniden şekillendirilmeyecektir.
- Yaklaşık 60 W noktasındaki -%4,89 sapmanın nedeni kanıtlanmış değildir; yük/çalışma koşulu kontrol edilerek ayrıca tekrar edilebilir. Bu istisna formülün yeniden açılması için tek başına gerekçe değildir.
- PF=0,76 olan 20,4 W noktası ayrı PF araştırma konusudur; V1.6'ya PF düzeltmesi eklenmez.
- PZEM karşılaştırma referansıdır, ground truth değildir.
- Bu kapanış MOD2-GRV001 görevinin tamamlandığı anlamına gelmez. Modülün diğer donanım, bağlantı, güvenilirlik ve gerçek yük gözlemleri ayrı iş olarak sürebilir.


## 2026-11-22 – Copilot incelemesi sonrası depo tutarlılığı düzeltmeleri

- Copilot incelemesinde işaret edilen tarih/güncel durum çelişkileri kaynak dosyalar üzerinden yeniden kontrol edildi.
- `DURUM.md` başındaki yetkili durum V1.6 tek fonksiyon kalibrasyon referansına hizalandı; eski iki bölgeli plan artık güncel sıradaki iş olarak görünmüyor.
- `GOREV.md` güncel çalışma kapsamını ve yetkili sürüm klasörlerini belirtiyor. Görev kökündeki `RAPOR/`, `RAPORLAR/` ve `KOD/` klasörleri tarihsel/ortak kayıt olarak ayrıştırıldı.
- Katsayı geçmişi raporunun başına iki bölgeli planın V1.6 ile kapandığı uyarısı eklendi; eski katsayılar tarihsel kayıt olarak bırakıldı.
- V1.6 raporunda 23 (ana kademeli zaman serisi), 21 (ideal K noktaları) ve 22 (1:1 karşılaştırma grafiği lejantı) sayımları ayrı analiz görünümleri olarak tanımlandı. Ham CSV yeniden eşleştirilmediği için bu sayımlar arasında birebir eşleme doğrulanmış değildir.
- Ham CSV ve PNG'lerin GitHub'a fiziksel dosya olarak eklenmesi hâlâ açık arşiv işidir; rapor bunların depoda olduğunu iddia etmez.
