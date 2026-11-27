# Home Assistant Community Deney Notu — ZMPT101B, ESP32 ADC ve ADS1115 Bağlamı

- Kayıt tarihi: 2026-11-22
- Kaynak: [Home Assistant Community — Measure mains voltage with ZMPT101B and ADS1115, mesaj #12](https://community.home-assistant.io/t/measure-mains-voltage-with-zmpt101b-and-ads1115/360162/12)
- Mesaj yazarı: NODeeJay (Alexander Weber)
- Mesaj tarihi: 24.05.2022
- Belge türü: Kullanıcı deneyimi, kod parçası ve ham log; üretici dokümanı veya kontrollü laboratuvar raporu değildir.

## 1. Mesajın kapsamı

Bu kayıt, başlığında ADS1115 geçmesine rağmen özellikle 12. mesajdaki kullanıcının **ADS1115'e geçmeden önce ZMPT101B modülünü ESP32'nin dahili ADC'siyle tek başına çalıştırma ve potansiyometreyi ayarlama girişimini** anlatır.

Kullanıcı ESP32 DOIT DevKit V1 (30 pin) kullanıyor. Önce GPIO25'i denemiş; ADC2'nin Wi-Fi ile çakışabileceğini okuduktan sonra ADC1 tarafındaki GPIO33'e geçmiş. ZMPT101B'yi ayrı bir güç kaynağıyla beslemiş; modülün D ve GND hatlarını ESP32'ye bağladığını bildiriyor.

Bu ayrıntı BERO için önemlidir: mesajdaki kararsızlık ADS1115'in performansına kanıt değildir; kullanıcı bu bölümde ESP32 dahili ADC'sini deniyor.

## 2. Kullanıcının denediği yöntem

Paylaşılan Arduino kodunun ana davranışı:
- GPIO33 analog giriş olarak seçiliyor.
- ADC attenuation 11 dB ayarlanıyor.
- ADC ham kodu 3.3/4095 ile çarpılarak gerilime çevriliyor.
- Her 100 ms'de bir hesaplanan değer seri porta yazdırılıyor.

Kullanıcı farklı kodlar ve gecikme değerleri denediğini, fakat AC bağlıyken kararlı ve tekrarlanabilir sonuç elde edemediğini bildiriyor. DC kaynak (örneğin 1,2 V şarjlı pil) ile yaptığı kontrolde değerlerin beklediğine yakın ve kararlı olduğunu; AC'de ise değerlerin düzensiz olduğunu söylüyor.

## 3. Mesajdaki log ve filtre denemesi

Kullanıcının ESPHome ADC logunda, şebeke bağlantısı yokken yaklaşık 0,075–0,185 V arasında değişen değerler görülüyor. Şebeke bağlandığında ilk okumalar yaklaşık 2,16–2,37 V aralığına çıkıyor; sonraki örneklerde 0,075 V ve 0,381 V gibi belirgin biçimde farklı değerler de oluşuyor. Şebeke bağlantısı kesilince yaklaşık 0,103 V seviyesine dönüyor.

Kullanıcı ayrıca şu işlem zincirini deniyor:
1. Boşta ölçülen ofseti çıkarma.
2. Örneklerin karesini alma.
3. 1250 örnekli kayan ortalama uygulama.
4. Kareköke dönme.
5. Sonucu 380 ile çarpma.

Bu zincirin amacı, RMS benzeri bir büyüklüğü uzun pencere ortalamasıyla hesaplayıp şebeke gerilimine ölçeklemek. Kullanıcı, D-G arasında şebeke bağlıyken 625–630 mVAC, şebeke ayrıyken 0,7 mVAC ölçtüğünü; 380 çarpanıyla yaklaşık 231 VAC sonucuna ulaştığını belirtiyor.

**Önemli ayrıntı:** Paylaşılan ESPHome filtresindeki `offset: 0` satırı, kullanıcının daha önce ölçtüğü boşta ofseti gerçekten çıkarmıyor; sıfır ofset uygular. Dolayısıyla yorum satırındaki “0V'da ölçülen değeri telafi et” açıklaması ile kodun gerçek parametresi arasında tutarsızlık var. Ayrıca ESPHome ADC sensörünün raporladığı tekil gerilim değerleri, dalga biçiminin tüm örneklerini ve zamanlamasını göstermez.

## 4. BERO açısından teknik değerlendirme

### 4.1. ADC2/Wi-Fi konusu ile ADC1 tercihi

Kullanıcı GPIO25'ten GPIO33'e geçiş gerekçesi olarak ESP32 ADC2 ile Wi-Fi çakışmasını gösteriyor. BERO'da Wi-Fi yalnızca bakım/yazılım güncelleme amacıyla kullanılacak olsa bile, ADC pin seçimi ve kablosuz haberleşme eşzamanlılığı açıkça test edilmelidir. Bu forum mesajı GPIO33 kullanımının BERO için otomatik olarak doğru pin olduğu anlamına gelmez; ESP32 kartının tam modeli ve pin eşlemesi esas alınmalıdır.

### 4.2. DC testinin başarılı olması AC ölçüm zincirini doğrulamaz

Kullanıcının 1,2 V DC kaynakla kararlı sonuç alması, ADC'nin statik DC seviyeyi okuyabildiğini gösteren sınırlı bir kontroldür. Bu, AC dalga biçiminin örnekleme hızını, RMS hesabını, ofset çıkarmayı veya faz doğruluğunu doğrulamaz.

### 4.3. Tekil ADC gerilimi RMS değildir

Bir ADC okumasının volt cinsinden dönüştürülmesi, AC gerilimin RMS değerini vermez. RMS için bir pencere boyunca örnekler alınmalı, DC bias/ortalama bileşeni doğru ele alınmalı, örneklerin karelerinin ortalaması ve karekökü hesaplanmalıdır. Örnekleme hızı ve pencere uzunluğu ölçülmeli; yalnızca yavaş güncellenen Home Assistant sensör değeri dalga biçimini değerlendirmek için kullanılmamalıdır.

### 4.4. Uzun kayan ortalama ve ölçek çarpanı

1250 örnekli pencere ve 380 katsayısı, kullanıcının kendi donanımı ve yazılımı için seçtiği deneysel ayarlardır. Bunlar BERO'ya aktarılmayacaktır. Uzun pencere rastgele değişimi yumuşatabilir; ancak örnekleme eksikliğini, aliasing'i, yanlış ofseti, kırpılmayı veya faz hatasını düzeltmez. Katsayı 380 de yalnızca o kullanıcının ölçüm zincirinde kalibre edilmiş olabilir.

### 4.5. Ayrı besleme ve ortak referans

Kullanıcı modülü ikinci bir kaynaktan beslediğini, D ve GND'yi ESP32'ye bağladığını belirtiyor. Ayrı besleme tek başına ölçüm kararlılığını garanti etmez. Analog OUT'un ESP ADC'si tarafından anlamlı okunabilmesi için sinyal referansı, ortak GND, besleme gürültüsü ve giriş aralığı devre bazında kontrol edilmelidir. Kartın tam şeması ve galvanik izolasyon yapısı bilinmeden forumdaki kablolama birebir kopyalanmayacaktır.

## 5. BERO deney planına eklenen kontroller

- [ ] ZMPT101B kartı geldiğinde önce osiloskopla DC ofset, AC genliği, simetri ve kırpılma kontrol edilecek.
- [ ] ESP32 dahili ADC denenecekse ADC1/ADC2 pin seçimi, kart modeli ve Wi-Fi etkinliği birlikte kaydedilecek.
- [ ] Modülün ayrı beslemesi ve ESP32 ortak GND bağlantısı kontrollü biçimde sınanacak; OUT geriliminin ADC giriş sınırlarında kaldığı doğrulanacak.
- [ ] DC kaynak testi yalnızca ADC'nin statik okuma kontrolü olarak etiketlenecek; AC RMS doğrulaması sayılmayacak.
- [ ] Ham AC örnekleri zaman bilgisiyle toplanacak; örnekleme hızı, örnek aralıklarının dağılımı ve pencere uzunluğu ölçülecek.
- [ ] Boşta ofset değeri gerçekten ölçülüp kaydedilecek; yazılımda kullanılan ofsetin bu ölçümle aynı olduğu kontrol edilecek.
- [ ] RMS hesabı ham örneklerden bağımsız çevrimdışı hesapla karşılaştırılacak.
- [ ] Kalibrasyon katsayısı, yalnızca birden fazla AC gerilim noktasında referans ölçümle doğrulandıktan sonra belirlenecek.
- [ ] ADS1115 kullanımı ayrı deney olarak ele alınacak; bu mesajın ESP32 dahili ADC denemeleri ADS1115 performansına kanıt gösterilmeyecek.

## 6. Güvenlik notu

Mesaj şebeke gerilimi ölçümünden söz ediyor. ESP32/USB bağlı osiloskop veya bilgisayarın toprak referansı, modülün şebeke tarafına gelişigüzel bağlanmamalıdır. İlk BERO testleri yalnızca güvenli, galvanik olarak izole düşük gerilimli AC kaynakla yapılacaktır. Ototransformatör tek başına izolasyon sağlamaz.

## 7. Sonuç

**BERO kararı:** Bu kaynak, ZMPT101B + ESP32 dahili ADC yolunda DC testinin AC doğruluğunu kanıtlamadığını; ham örnekleme, ofset, RMS hesabı ve kalibrasyonun ayrı ayrı doğrulanması gerektiğini gösteren bir deney uyarısı olarak saklanacaktır.

Mesajdaki 380 katsayısı, 625–630 mVAC gözlemi, yaklaşık 231 VAC sonucu ve ADC logları yalnızca forum kullanıcısının kurulumuna aittir. BERO için kalibrasyon değeri veya performans sonucu değildir.

## Durum

- Kaynak ve BERO teknik değerlendirmesi depoya kaydedildi.
- Mesaj #12'de anlatılan ESP32 dahili ADC denemesi ADS1115 testi değildir.
- BERO ZMPT101B kartında bu testler henüz yapılmadı.
