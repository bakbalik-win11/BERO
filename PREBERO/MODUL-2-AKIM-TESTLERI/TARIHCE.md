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
