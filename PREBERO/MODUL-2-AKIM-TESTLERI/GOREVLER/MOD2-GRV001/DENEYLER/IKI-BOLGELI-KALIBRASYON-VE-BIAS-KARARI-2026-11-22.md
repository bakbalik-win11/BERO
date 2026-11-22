# İki bölgeli akım kalibrasyonu ve bias kararı – 2026-11-22

## Durum
**KAPATILDI – 2026-11-22.** Bu tarihsel iki bölgeli tasarım önerisi V1.6 tek fonksiyonlu tam aralık kalibrasyon modeliyle ikame edilmiştir. Ayrıntılı kapanış aşağıdadır.

## Kullanıcı kararı
Akım ölçümü iki çalışma bölgesinde ayrı kalibre edilecek:
- **Düşük akım bölgesi:** 1,5 A altı için ayrı katsayı.
- **Yüksek akım bölgesi:** 1,5 A üstü için ayrı katsayı.

Bias devresinin sağladığı katkı, ilave devre ve bağlantı zahmetine değmediği için yeni tasarım yaklaşımında bias tercih edilmeyecek. Kullanıcının tasarım ilkesi: daha basit ölçüm yolu tercih edilecek.

## Teknik yaklaşım
Mevcut tek katsayılı dönüşümün yerine, testlerle belirlenecek iki bölgesel katsayı değerlendirilecek:

\[
I_{hesaplanan} =
\begin{cases}
RMS(ADC) \times K_{düşük}, & I_{ön/ham\ tahmin} < 1.5\ A \\
RMS(ADC) \times K_{yüksek}, & I_{ön/ham\ tahmin} > 1.5\ A
\end{cases}
\]

Bu ifade yöntem taslağıdır; henüz uygulanabilir bir algoritma olarak doğrulanmamıştır. Özellikle hangi ölçüm büyüklüğünün bölge seçimini yapacağı, katsayı seçiminin kararlı olması ve 1,5 A geçişindeki davranış deney ve yazılım tasarımında netleştirilmelidir. Tam 1,5 A sınırındaki seçim kuralı henüz kararlaştırılmamıştır.

## Deney planı
1. Bias kullanılmayan sade analog bağlantı düzeni güvenli biçimde kurulup her ADS1115 girişinin mutlak gerilim sınırları doğrulanacak.
2. 1,5 A'nın belirgin altında birden fazla akım noktası ölçülecek.
3. 1,5 A'nın belirgin üstünde birden fazla akım noktası ölçülecek.
4. 1,5 A çevresinde alt ve üst bölgeyi ayırmak için ek ölçüm noktaları alınacak.
5. Her noktada yeterli sayıda PZEM akım örneği ve SCT/ADS1115 örneği toplanacak; yük ve zaman koşulları kaydedilecek.
6. PZEM ile karşılaştırma referans olarak kullanılacak; ground truth kabul edilmeyecek.
7. Her bölge için katsayı ayrı hesaplanacak ve aynı bölgedeki farklı yük noktalarında doğrulanacak.
8. İki katsayılı modelin tek katsayılı modele göre hata davranışı ve 1,5 A civarında olası sıçrama ayrıca değerlendirilecek.

## Koruma ve mevcut durum
- Mevcut K=27.59 değeri şimdilik korunur; yeni bölgesel katsayılar ölçüm olmadan atanmaz.
- Çalışan YAML ve firmware bu karar kaydıyla değiştirilmez.
- Biaslı deneylerin eski sonuçları tarihsel veri olarak korunur; yeni tasarım tercihi bu sonuçları silmez veya geçmiş deneyleri geçersiz kılmaz.
- Biasın fiziksel olarak devreden çıkarılması ve yeni bağlantının uygulanması, bağlantı şeması ve giriş gerilimleri doğrulandıktan sonra ayrı uygulama adımıdır.
- Bu karar henüz iki bölgeli kalibrasyonun başarılı olduğunu göstermez.

## Açık teknik noktalar
- 1,5 A sınırında hangi katsayının seçileceği.
- Bölge seçiminin hangi ölçümden ve hangi sırada yapılacağı.
- Geçiş çevresinde katsayı değişiminin ani çıktı sıçraması üretip üretmediği.
- Her iki bölgedeki katsayıların birden fazla yük noktasında tekrarlanabilirliği.

## Kapanış / sonraki adım
Biasın yeni tasarımda tercih edilmemesi ve iki bölgeli katsayı yaklaşımı **tasarım kararı olarak kaydedildi**. Kalibrasyon deneyi açık iş olarak kalır. Sonraki adım, bias kullanılmayan güvenli bağlantıyı doğrulamak ve düşük akım bölgesinden başlayarak ölçüm serisini oluşturmaktır.


## 2026-11-22 – İki bölgeli katsayı belirleme yöntemi: kullanıcı nihai kararı

Kullanıcı, iki katsayıyı pratik ev yükleriyle belirleme yöntemini kesinleştirdi. Mükemmel/laboratuvar düzeyinde kalibrasyon hedeflenmeyecek; seçilen yüklerle elde edilen yeterli ve tutarlı veri üzerinden katsayılar belirlenecek.

### Bölge 1 – 1,5 A altı
- 150 W'a kadar ampullerle ölçüm verisi toplanacak.
- Ampul yükleri düşük bölge katsayısını belirlemek için kullanılacak.
- Bu bölgedeki ölçüm noktaları ve gerçek akım değerleri deney sırasında kaydedilecek; nominal watt değeri tek başına akım ölçümü sayılmayacak.

### Bölge 2 – 1,5 A üstü
- Ütü, tost makinesi ve kettle'ın kaynatma modu kullanılacak.
- Bu yüklerle yüksek bölge katsayısı belirlenecek.
- Cihazların çalışma durumu ve ölçüm sırasındaki akım kararlılığı kaydedilecek.

### Ortak kurallar
- Bias kullanılmayan sade ölçüm yolu esas alınacak; fiziksel bağlantı değişikliği öncesinde ADS1115 girişlerinin mutlak gerilim sınırları doğrulanacak.
- PZEM karşılaştırma referansıdır; ground truth kabul edilmeyecek.
- K=27.59 yeni katsayılar hesaplanıp kontrol edilene kadar korunacak.
- Önceki biaslı deney verileri tarihsel kayıt olarak kalacak; yeni biassız kalibrasyon serisiyle karıştırılmayacak.
- Mükemmel doğruluk veya ±% belirli bir hedef şartı aranmayacak. Amaç, iki bölgede pratik kullanım için yeterli katsayı elde etmektir.
- 1,5 A sınırının tam seçimi ve yazılımda bölge belirleme yöntemi, iki katsayı elde edildikten sonra uygulama aşamasında ele alınacak; bu aşamada henüz çözülmüş kabul edilmeyecek.

**Sıradaki iş:** Biassız ölçüm bağlantısını güvenli şekilde doğrulamak ve önce 150 W'a kadar ampullerle düşük akım veri serisini toplamak. Düşük bölge katsayısı belirlendikten sonra ütü, tost makinesi ve kettle kaynatma moduyla yüksek bölgeye geçilecek.

 
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
