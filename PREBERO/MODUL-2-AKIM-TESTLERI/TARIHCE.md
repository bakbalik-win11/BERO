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


### 2026-11-22 – MOD2-GRV001 masaüstü prototip görevi kapatıldı

- **Çalışma / deneme:** ESP32D2 + ADS1115 No.10 + SCT013 30A/1V masaüstü prototipinde geniş akım aralığında farklı ev yükleri ve yük kombinasyonları denendi; V1.6 tek fonksiyon kalibrasyon modeli referans olarak kabul edildi.
- **Gözlenen sonuç:** Masaüstü prototip, akım ölçüm zincirinin geliştirilmesi ve gerçek cihaz modüllerine aktarılması için belirlenen amacını yerine getirdi.
- **Edinilen tecrübe:** Yükleri masaüstünde kontrollü ve kombinasyonlu biçimde denemek, gerçek cihazlarda izleme mantığına geçmeden önce ölçüm zinciri ve kalibrasyon yaklaşımını hazırladı.
- **Teknik karar:** MOD2-GRV001 kapatıldı. 60 W tekrar testi, yeni yük kombinasyonu ve uzun süreli masaüstü gerçek kullanım gözlemi iptal edildi.
- **Sonraki aşama:** Gerçek kullanım denemeleri Modül 3 çamaşır makinesi ve Modül 4 bulaşık makinesi görevlerinde yapılacak. Bunlar Modül 2'nin açık işleri değildir.
- **İlgili kayıtlar:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/GOREV.md`; V1.6 YAML ve doğrulama raporu kendi sürüm klasöründedir.


### 2026-11-22 – Modül 2'nin ileri araştırma rolü: dalga biçimi ve PF etkisi

- **Çalışma / karar:** Kullanıcı, Modül 2'nin akım ölçümünden sonra dalga biçimini anlamaya ve PF etkisini araştırmaya odaklanmasını netleştirdi.
- **Araştırma yönü:** SCT013 akım dalga biçimi ve ZMPT101B gerilim dalga biçimi üzerinden dalga istatistikleri çıkarılması; farklı PF koşullarında akım ölçüm sapmasının incelenmesi.
- **Modül 3/4 ile ilişki:** Çamaşır ve bulaşık makinesi tasarım/saha deneyleri, farklı çalışma evreleri ve PF koşullarına ilişkin veriler sağlayarak Modül 2 araştırmasına katkıda bulunabilir.
- **Teknik sınır:** PF etkisi henüz kanıtlanmış değildir. ZMPT101B tek başına PF ölçmez; gerilim ve akım dalga biçimlerinin uygun zaman eşlemeli örneklenmesi gerekir. V1.6 kalibrasyonuna doğrulama olmadan PF düzeltmesi eklenmeyecektir.
- **Görev sınırı:** MOD2-GRV001 kapalı kalır. PF/dalga biçimi çalışması ayrı araştırma görevi olarak açılacaktır; mevcut kapanış ve referans YAML değiştirilmeyecektir.


## 2026-11-24 – MOD2-GRV002 açıldı: BERO'ya özel bağımsız PF ve akım ölçümü

- **Çalışma / karar:** Kullanıcı, PF araştırmasının hedefini pratik BERO ölçüm sistemi olarak netleştirdi. Her hatta PZEM kullanmadan, SCT013 tabanlı hızlı tepki veren, akım değerinde PZEM referansına yaklaşan ve kendi PF'sini hesaplayan bir yapı hedefleniyor.
- **Yöntem:** İlk adımda PZEM'in akım ve PF yayınları eğitim/karşılaştırma referansı olacak. EXP akımıyla aynı zaman pencerelerinde karşılaştırılacak; hata ve oran grafiklerinden EXP formülünün geliştirilmesindeki gibi basit fonksiyon aranacak. PF düştükçe akımı küçültme hipotezi henüz doğrulanmadı.
- **İkinci aşama:** ZMPT101B gerilim ve SCT013 akım dalgaları ortak zaman tabanında örneklenerek BERO'nun kendi gerçek PF hesabı geliştirilecek. PZEM normal çalışma sırasında zorunlu sensör olmayacak.
- **Korunan karar:** MOD2-GRV001 V1.6 ve EXP/K(x) modeli değiştirilmez. Yeni düzeltme ayrı görev/model olarak geliştirilir. PZEM referanstır, mutlak ground truth değildir.
- **İlk iş:** Mevcut çamaşır makinesi ve düşük PF kayıtlarını grafiklemek. Sonraki adımlar zaman hizalı yeni kayıt, grafiklerden fonksiyon adayı, bağımsız doğrulama, ZMPT101B analog/zamanlama testleri ve BERO PF hesabıdır.
- **Durum:** Görev ve deney planı açıldı; yeni fiziksel deney yapılmadı, yeni fonksiyon bulunmadı, firmware doğrulanmadı.
- **Görev kaydı:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md`.


### 2026-11-27 — MOD2-GRV002 pratik PF yöntemi seçildi

- **Kullanıcı kararı:** İlk yöntem, ZMPT101B hazır kartını tanıyıp güvenli ön testlerden sonra trimpotla gerilim okumasını PZEM'e yaklaştırmaktır; ardından SCT013 ile faz/PF ilişkisi pratik şekilde ölçülecektir.
- **Deney yaklaşımı:** Sabit ampul yükü, kullanıcının sağladığı dimmerin farklı ayarlarında denenir. Her ayardaki PZEM V/I/P/PF değeri BERO ham ve hesaplanan değerleriyle aynı kararlı pencerede karşılaştırılır.
- **Model kararı:** Gerilim genlik ayarı, PHASE_CORRECTION ve PF'ye bağlı akım düzeltmesi ayrı tutulur. V1.6 korunur; yeni PF etkili model MOD2-GRV002 altında çıkarılır.
- **Araştırma notlarının rolü:** Diğer yapay zekâların sentezi, genel metodoloji ve dış kaynak notları içeriği korunarak isteğe bağlı başvuruya ayrılır; güncel uygulamayı zorunlu kılmaz.
- **Güvenlik/kanıt sınırı:** Kart ve korumalı test düzeni gözden geçirilmeden şebeke bağlantısı yapılmaz. Bu kayıt plan kararını gösterir; henüz fiziksel test veya katsayı yoktur.
- **Ayrıntılı plan:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md`.


### 2026-11-28 – MOD2-GRV002 – SCT013-030 çıkışını FNIRSI 2D15P DMM ile doğrudan gözlemleme deneyi planlandı

- **Çalışma / karar:** Kullanıcı, sensörleri ADC/ESP32/ADS1115/MCP3208 katmanlarından bağımsız tanımak için sensörün kendi elektriksel çıkışını doğrudan ölçme yaklaşımını seçti. İlk kısa deney, FNIRSI 2D15P'nin DMM moduyla SCT013-030'un düşük AC mV çıkışını okumaktır.
- **Hedef:** SCT013-030 (30 A / 1 V) nominal oranında 0,05 A RMS primer akımına karşılık gelen yaklaşık 1,67 mV RMS AC çıkışın DMM'de yüksüz tabandan ayırt edilip edilemediğini ve tekrarlandığında kararlı olup olmadığını görmek.
- **Teknik hesap:** 1 V / 30 A = 33,333 mV/A; 0,05 A × 33,333 mV/A ≈ 1,667 mV RMS.
- **Ölçü aleti bilgisi:** FNIRSI üretici ürün sayfasında DMM için 19.999 count ve en düşük 1,9999 V ACV kademesi belirtilir; teorik ekran basamağı 0,1 mV'dir. Düşük AC mV bölgesinde doğruluk/minimum güvenilir giriş seviyesi açık teknik tabloda belirtilmediğinden, ekranda değer görünmesi doğruluk kanıtı sayılmayacaktır.
- **Edinilen yaklaşım:** İlk karakterizasyon doğrudan sensör çıkışında yapılır. Bu ilk deneyde ADC, ESP, bias, harici burden ve yükselteç eklenmez. Sonraki aşamada ADC zincirinin sensörü ne kadar iyi okuduğu ayrıca kıyaslanır.
- **Kanıt durumu:** Fiziksel deney henüz yapılmadı. Ölçüm, log, ekran görüntüsü veya başarılı/başarısız sonuç yoktur. 0,05 A akım bağımsız ve güvenilir biçimde doğrulanamazsa deney yaklaşık yük gözlemi olarak etiketlenecektir.
- **Teknik karar:** Deney, MOD2-GRV002'de ZMPT101B/PF adımlarından önce yapılacak ilk kısa kontrol olarak sıralandı. Bu karar MOD2-GRV001 V1.6 modelini veya YAML'ini değiştirmez.
- **İlgili kayıt:** `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/DENEYLER/FNIRSI-2D15P-DMM-SCT013-030-005A-2026-11-28.md`; görev `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md`.
- **Üretici teknik sayfası:** https://www.fnirsi.com/products/2d15p


### 2026-11-28 – MOD2-GRV002 – Mevcut jeneratörlerle analog ölçü aleti ön testi planlandı

- **Çalışma / karar:** Kullanıcının mevcut FNIRSI SG-002 ve FNIRSI 2D15P cihazları bulunduğu teyit edildi. Küçük FYE050/AD9833/XR2206 jeneratörü satın almadan önce mevcut kaynaklarla deney yapma kararı alındı.
- **Kaynak ayrımı:** SG-002 DC gerilim ve DC akım simülatörüdür; kılavuzdaki “50HZ” ibaresi ekran gösterim seçeneği olup AC sinüs çıkışı değildir. 2D15P DDS 0,1–3,0 Vpp aralığında AC dalga şekli üretebilir; minimum 0,1 Vpp seviyesi 20 kΩ seri / 1 kΩ şönt bölücüyle yaklaşık 1,68 mV RMS'e indirilebilir.
- **Deney amacı:** UT61E+ gibi bağımsız DMM'nin düşük AC mV seviyesindeki görünürlük, tepki ve yaklaşık seviye doğrusallığını incelemek. 1,68 mV noktası doğruluk garantisi dışında olduğundan yalnızca görünürlük/kararlılık noktasıdır; 3,37 mV ve üzeri noktalar UT61E+ 220 mV AC kademesinin üretici doğruluk başlangıcının üzerindedir.
- **Sınırlar:** 2D15P'nin DDS ve DMM modlarının eşzamanlı çalıştığı doğrulanmamıştır. Aynı cihazın kaynağıyla kendi DMM girişinin eşzamanlı ölçüm yapabildiği varsayılmaz. 2D15P DDS + bölücü kalibrasyon standardı değildir ve SCT'nin manyetik/primer akım davranışını simüle etmez.
- **Alternatifler:** FYE050 yüksek minimum çıkış nedeniyle yine zayıflatıcı ister; AD9833 ESP32/SPI otomasyonu için değerlidir ancak modül çıkış genliği devreye bağlıdır; XR2206 kitlerinin özellikleri kart revizyonuna göre değişir. Bunlardan hiçbiri şimdilik satın alınmayacaktır.
- **İlgili kayıtlar:** [2D15P DMM/SCT/DDS deney planı](GOREVLER/MOD2-GRV002/DENEYLER/FNIRSI-2D15P-DMM-SCT013-030-005A-2026-11-28.md); [SG-002 DC deney planı](GOREVLER/MOD2-GRV002/DENEYLER/FNIRSI-SG002-DC-ANALOG-SIMULATOR-TESTI-2026-11-28.md); görev kaydı `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md`.
- **Kanıt durumu:** Yalnızca deney planı ve teknik ayrım kaydedildi; fiziksel test, log veya doğrulanmış ölçüm sonucu yoktur.


### 2026-11-28 – BERO ölçüm altyapısı hedefleri sabitlendi — Ölçüm Stratejisi V1.0

- **Çalışma / karar:** Kullanıcı, BERO'da ölçüm kaynaklı gecikmeleri önlemek için tezgâh cihazlarının görevlerinin ve sensör doğrulama sırasının sabitlenmesini istedi.
- **Ana yaklaşım:** Önce sensörün ham elektriksel çıkışı bağımsız ölçülür; sonra dalga biçimi 2D15P ile incelenir; ardından analog ön uç/ADC ham kodu ve en son yazılım/kalibrasyon doğrulanır. ADC sayısı sensörün ham çıkışı yerine kullanılmaz.
- **Cihaz görevleri:** SANEC lojik analizör dijital protokol/zamanlama; FNIRSI 2D15P analog dalga biçimi ve DDS; FNIRSI SG-002 DC gerilim/akım simülasyonu; UT200B+ yardımcı pens akımı; UT33D+ günlük süreklilik/temel kontroller; planlanan UT61E+ bağımsız analog sensör DMM'si.
- **Satın alma kararı:** Yalnızca UNI-T UT61E+ planlanan yeni ölçüm cihazıdır. AD9833/AD9850 DDS modülleri, FYE050 veya XR2206 yeni satın alma gereksinimi olarak açılmayacaktır; mevcut cihazlarla karşılanamayan somut deney ihtiyacı gösterilirse tekrar değerlendirilir.
- **Kaynak sınırı:** FNIRSI SG-002 DC V/DC mA simülatörüdür; AC sinüs jeneratörü olarak kullanılmaz. FNIRSI 2D15P DDS, zayıflatıcıyla düşük mV yardımcı test seviyesi oluşturabilir; kaynak kalibrasyon standardı değildir. DDS ve DMM işlevlerinin aynı anda çalıştığı varsayılmaz.
- **Kanıt/sonuç durumu:** Ölçüm altyapısı stratejisi ve test sırası dokümante edildi. Bu karar cihazların kalibrasyonunu veya deneylerin fiziksel olarak tamamlandığını göstermez.
- **İlgili kayıt:** `PREBERO/OLCUM-ALTYAPISI/OLCUM-STRATEJISI-V1.0.md`; güncel durum `PREBERO/DURUM.md`; planlanan cihaz envanteri `ENVANTER/README.md`.


### 2026-11-28 – MOD2-GRV002 – SCT akım genlik hatası ile PF hesabının ayrılması

- **Çalışma / karar:** Kullanıcı, PF≈1 koşulunda SCT013 akım kalibrasyonunun daha önce başarıldığını teyit etti. Bu kalibrasyon ve MOD2-GRV001 V1.6 korunacak; PF<1 deneyi için SCT amper katsayısı baştan ayarlanmayacak.
- **Gerilim/PF ayar ayrımı:** ZMPT101B trimpotu yalnızca BERO gerilim RMS ölçeğini PZEM gerilimine yaklaştırır. PF≈0,50 gibi deney noktası dimmerle oluşturulur; dimmer konumu ve PZEM PF değeri kaydedilerek sabitlenir. Trimpot PF ayar elemanı değildir.
- **Matematiksel sonuç:** PF yalnızca (V_{RMS}) ve (I_{RMS}) üzerinden bulunamaz. Zaman eşlemeli örneklerden (P=\operatorname{mean}(v[n]i[n])) ve (PF=P/(V_{RMS}I_{RMS})) hesaplanmalıdır. SCT akım örnekleri gerçek dalganın yalnızca sabit doğrusal bir kazançla çarpılmış hali ise akımdaki genlik katsayısı hem P hem (I_{RMS}) içinde bulunduğundan PF oranında sadeleşir. Bu nedenle amper ölçeği henüz PZEM'le eşleşmese bile, dalga biçimi ve zaman ilişkisi korunuyorsa PF hesaplanabilir.
- **Sınırlar:** Faz/frekans cevabı hatası, dalga biçimi bozulması, doyum/kırpılma, doğrusal olmayanlık, ofset/gürültü ve ADC kanalları arasındaki örnek zaman farkı PF sonucunu bozabilir. Sadece RMS gerilim ve RMS akım okumak PF için yeterli değildir.
- **Deney sırası:** Önce ZMPT gerilim RMS ölçeğini PZEM'e yaklaştır; dimmerle sabit PF noktası oluştur; daha önce elde edilen SCT PF≈1 akım kalibrasyonuna dokunmadan iki kanaldan aynı pencereye ait örnek al; BERO PF ve akımını PZEM ile karşılaştır; tekrarlanabilir veri oluşursa ayrı PF'ye bağlı akım düzeltme fonksiyonu araştır.
- **Koruma:** MOD2-GRV001 V1.6 değiştirilmez. ZMPT gerilim ayarı, SCT akım ölçeği, PF hesabı ve PF'ye bağlı akım düzeltmesi ayrı kavramlar olarak tutulur.
- **Kanıt durumu:** Matematiksel gerekçe ve deney kararı kaydedildi; fiziksel ZMPT/PF deneyi, zaman eşlemeli ADC doğrulaması veya yeni fonksiyon henüz yoktur.
- **Ayrıntılı kayıt:** [MOD2-GRV002 görev kaydı, §16](GOREVLER/MOD2-GRV002/GOREV.md).


### 2026-11-28 – MOD2-GRV002 – PF için çok değişkenli deney ve zaman penceresi tasarımı

- **Kullanıcı önerisi:** Aynı PF değerinin dimmerli akkor, düşük akım LED ve motor gibi farklı fiziksel yüklerde farklı akım dalga biçimleriyle oluşabileceği; bu nedenle düzeltmenin yalnız PF sütununa göre kurulamayacağı belirtildi.
- **Deney değişkenleri:** PF, I_RMS, mümkünse I_peak/crest factor, yük etiketi/türü, dimmer konumu, dalga biçimi gözlemi ve ADC örnekleme kimliği ayrı alanlar olarak kaydedilecek.
- **Tarihsel kanıt – dimmerli 100 W akkor:** 2026-11-21 kaydında PF 1,00'dan 0,61'e inerken SCT/PZEM oranı 0,921'den 1,507'ye çıktı. Aynı pencerelerde PZEM akımı da 0,463 A'dan 0,338 A'ya değişti; ham dalga/harmonik verisi bulunmadığından PF tek başına neden sayılamaz. Kaynak: PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/RAPOR/DIMMER-100W-PF-ETKISI-2026-11-21.md.
- **Tarihsel kanıt – 8,5 W LED:** İki çevrimde PF 0,66–0,67, PZEM akımı 0,052–0,053 A ve SCT akımı 0,095–0,096 A görüldü. Bu nokta düşük akım, LED yükü ve düşük PF'yi birlikte içerir; nüve nonlineerliği tek başına kanıtlanmamıştır. Kaynak: PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/8_5W-LED-DUSUK-PF-TEKRAR-2026-11-21.md.
- **Katsayı ayrımı:** K=27.59 eski V1.1 zincirinin baz katsayısıdır; güncel V1.6 modelinin yerine geçen veya tek başına “alt bant katsayısı” olan bir değer gibi kullanılmayacaktır. V1.6 K(x)=26.89+5.39e^(-x/0.882) modeli korunur.
- **PZEM zamanlaması:** PZEM-REF-WROOM-01 değerleri 5 saniyede bir yayımlar. Her yük/dimmer değişiminden sonra geçiş verisi dışlanacak; ardışık PZEM yayınlarında kararlılık görülünce ortak zaman sınırları olan kararlı pencere açılacaktır. Seyrek PZEM örnekleri interpolasyonla yapay biçimde çoğaltılmayacak.
- **ADS1115 sınırı:** Mevcut YAML'de ADS1115 860 SPS, ct_clamp 200 ms RMS penceresi ve 1 s yayın vardır; bu Home Assistant akım varlığı ham gerilim-akım örnek dizisi değildir. ADS1115 MUX kanalları eşzamanlı değildir. İki kanalın 860 SPS toplam hızda dönüşümlü okunması halinde kanal başına teorik üst sınır yaklaşık 430 SPS (50 Hz'de 8,6 örnek/periyot) olur; gerçek hız ve Δt ölçülmelidir. Enterpolasyon zaman farkını azaltabilir, fakat kayıp harmonikleri/aliasing'i geri getiremez.
- **Model kapsamı:** Ampirik düzeltme yalnız test edilen PF, akım, dalga biçimi ve yük aralığında adaydır. Yeni yük tipi veya motor/çamaşır makinesi geçişi ayrı doğrulama gerektirir.
- **Kanıt durumu:** Bu kayıt deney tasarımı ve tarihsel verinin yorumudur; yeni fiziksel ölçüm, harmonik analizi, ham ADS örnek kaydı veya doğrulanmış yeni fonksiyon değildir.
- **Ayrıntılı kayıt:** MOD2-GRV002 görev kaydı, Bölüm 17.


### 2026-11-28 – MOD2-GRV002 – Deney logunda settling/steady ve örnekleme penceresi ayrımı

- **Kullanıcı önerisi:** Yük/dimmer geçişlerinde PZEM'in 5 saniyelik yayın ritmi dikkate alınarak `settling` ve `steady` etiketleri kullanılması; örnek sayısı ve Δt yanında gerçek ölçüm penceresi süresi veya ESPHome 200 ms pencere bilgisinin tutulması önerildi.
- **Teknik doğrulama:** ESPHome ct_clamp belgeleri `sample_duration` değerini her ölçümde örnekleme süresi, `update_interval` değerini sensörün ölçüm kontrol/yeni örnekleme aralığı olarak tanımlar. Kaynak kodunda update çağrısı örnekleme fazını başlatır; sample_duration zaman aşımında faz sona erer, örnek sayısı üzerinden RMS hesaplanıp yayımlanır. Dolayısıyla 200 ms + 1 s ayarı, saniyede beş adet 200 ms pencerenin birleştirilmesi demek değildir.
- **Kayıt kararı:** `settling/steady/invalid` etiketi; yük değişim zamanı; PZEM yayın zamanı; gerçek BERO pencere başlangıç/bitişi ve süresi; yapılandırılmış 200 ms sample_duration; 1000 ms update_interval; logdan elde edilen gerçek kaynak örnek sayısı ve efektif SPS ayrı alanlarda tutulacak.
- **PZEM kararlılığı:** Ayar değişiminden sonra en az bir tam 5 saniyelik yayın aralığı geçecek; ardından kararlılık, önceden belirlenmiş tolerans ve ardışık yayın şartlarıyla değerlendirilecek. 5 saniyelik yayın ritmi PZEM'in iç örnekleme penceresinin kesin süresi diye yorumlanmayacak.
- **Kanıt sınırı:** Mevcut HA ct_clamp RMS varlığı ham örnek zaman damgalarını ve gerçek kaynak örnek sayısını tek başına taşımaz. Bu alanlar debug veya ayrı ham veri kaydıyla elde edilmedikçe boş bırakılacak; tahmin edilmeyecek.
- **Ayrıntılı kayıt:** MOD2-GRV002 görev kaydı, Bölüm 17.6.


### 2026-11-28 – MOD2-GRV002 – Veri şemasının kanıt zinciri ve ham veri/analiz ayrımı

- **Kullanıcı açıklaması:** `window_status` etiketlerinin geçiş, kararlı ve bozuk kayıtları ayırdığı; zaman damgalarının PZEM yayını ile BERO'nun gerçek 200 ms penceresini karşılaştırmayı sağladığı; gerçek örnek sayısı/hızının tahmin edilmemesi gerektiği ve ham verinin yorumdan ayrı tutulmasının yeniden analize imkân verdiği vurgulandı.
- **Teknik sınır:** Zaman damgaları PZEM yayın anı ile BERO pencere başlangıç/bitişini karşılaştırır; PZEM'in iç ölçüm/ortalama penceresinin süresini tek başına göstermez. Bu bilgi ayrıca doğrulanmadıkça varsayılmaz.
- **Kayıt ilkesi:** Ham ADS1115 ve PZEM verileri değişmeden saklanır. Kararlı pencere seçimi, settling/invalid dışlamaları, filtreleme, kalibrasyon hesabı ve grafikler ayrı analiz çıktısı olarak üretilir ve kaynak ham dosya ile yöntem/sürüm bilgisine bağlanır.
- **Yeniden analiz:** Aynı ham kayıtlar daha sonra farklı PF, dalga biçimi veya kalibrasyon hipotezleriyle yeniden analiz edilebilir. Bu işlem V1.6'yı otomatik değiştirmez; (K(x)=26.89+5.39e^{-x/0.882}) referansı korunur, yeni PF modeli ayrı sürüm ve bağımsız doğrulama gerektirir.
- **Kanıt durumu:** Veri yönetimi ve deney yöntemi kararıdır; gerçek pencere çakışması, örnek sayısı ve ham çift kanal kaydı fiziksel deneyle doğrulanmayı bekler.
- **Ayrıntılı kayıt:** MOD2-GRV002 görev kaydı, Bölüm 17.7.


### 2026-11-28 – MOD2-GRV002 – Gerçek hayat PF yükleri ve üç LED ile akım basamaklama

- **Kullanıcı bildirimi:** Kullanıcının elinde üç adede kadar LED ampul bulunduğu belirtildi. İlk gerçek hayat yük serisi, LED ampulleri tek tek, ikili ve üçlü kombinasyonla çalıştırarak aynı yük ailesinde toplam akımı basamaklandırmak olarak belirlendi.
- **Deney amacı:** LED sürücüsü karakteri altında toplam akım değişirken PZEM PF ve SCT/PZEM akım farkının nasıl değiştiğini görmek. Her kombinasyonda PZEM V/I/P/PF yeniden kaydedilecek; PF'nin sabit kalacağı varsayılmayacak.
- **Yük kimliği:** Ampuller aynı marka/model/watt ise aynı seri içinde bir/iki/üç ampul basamağı olarak karşılaştırılabilir. Farklılarsa her ampulün marka/model/watt bilgisi ve kullanılan kombinasyon açıkça etiketlenecek; aynı yük tipi varsayılmayacak.
- **Diğer gerçek hayat yükleri:** Vantilatör sabit hız kademeleriyle motorlu yük grubu; telefon şarjı ise kısa kararlı aralıklar yakalanabilirse steady pencere, aksi halde dynamic zaman serisi olarak incelenecek. Dimmerli akkor ayrı kontrollü dalga biçimi deneyidir.
- **Durum etiketleri:** settling geçişi, steady kararlı platoyu, dynamic geçerli fakat zamanla değişen yükü, invalid bozuk/eksik veriyi belirtir. Dynamic kayıt geçersiz sayılıp silinmez.
- **Kanıt durumu:** Yükler ve deney sırası planlandı; LED ampul, vantilatör veya telefon şarjıyla bu yeni seri henüz ölçülmedi.
- **Ayrıntılı kayıt:** MOD2-GRV002 görev kaydı, Bölüm 17.8.
