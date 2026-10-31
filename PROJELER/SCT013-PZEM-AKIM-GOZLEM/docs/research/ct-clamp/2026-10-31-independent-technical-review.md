# ESPHome ct_clamp — Bağımsız teknik inceleme

**Proje:** BERO / SCT-013 akım gözlem sistemi  
**Tarih:** 2026-10-31  
**İncelenen yazılım:** ESPHome 2026.10.1, kaynak commit `4ea26ed`  
**İncelenen BERO kaydı:** Modül 2 / ESP32D1 / SCT-1 / Log 63  
**Rapor türü:** Kaynak kod + üretici dokümanı + BERO log analizi. Bu rapor yeni bir donanım testi değildir.

## 1. Yönetici özeti

ESPHome `ct_clamp`, belirli bir süre boyunca ADC kaynağından gerilim örnekleri toplayıp bu örneklerin DC ortalamasını çıkararak AC bileşenin RMS değerini hesaplar. BERO'da bu gerilim RMS değeri, mevcut yapılandırmadaki 24,22 ölçek katsayısıyla akım göstergesine dönüştürülmektedir.

En önemli teknik bulgu, kaynak kodunun ardışık olarak aynı gerilim değerini tekrar gördüğünde o örneği toplamaya katmamasıdır. Böylece RMS hesabındaki örnekler eşit zaman aralıklı bir örnek dizisi olmaktan çıkar. Bu davranışın etkisi özellikle küçük genliklerde ve ADC kuantizasyonunun aynı kodu birden fazla döngüde üretmesi halinde önem kazanabilir. Etkinin BERO'daki gerçek büyüklüğü henüz ölçülmemiştir.

İkinci önemli nokta, `sample_duration: 200ms` ve `update_interval: 2s` ayarında `ct_clamp` örneklemeyi sürekli yapmaz: yaklaşık her iki saniyede bir 200 ms'lik pencere açar. Pencere dışındaki yaklaşık 1,8 saniyede bu bileşen kendi örnek toplama döngüsünü çalıştırmaz. Bu nedenle yayın, iki saniyelik sürekli ölçüm ortalaması değil, kısa pencere gözlemidir.

Log 63'te, ilk açılış örneği ayrıldıktan sonra 50 yayının ortalama akım göstergesi 3,09636 A; ortalama Raw AC gerilimi 0,127843 V'tur. Çarpım:
`0,127843 V × 24,22 A/V = 3,09636 A`.
Bu, raporlanan ölçekleme aritmetiğinin tutarlı olduğunu gösterir; mutlak doğruluğu veya PZEM ile eşleşmeyi kanıtlamaz. UNIT 3,30 A kullanıcı bildirimidir, PZEM değildir ve aynı zaman penceresine ait olduğu belgelenmemiştir.

**Karar:** Mevcut firmware, K=24,22, 200 ms pencere ve 2 s yayın aralığı bu araştırma nedeniyle değiştirilmemelidir. Önce örnek tekrar eleme davranışı ve düşük akım tabanı ölçülebilir bir deneyle incelenmelidir.

## 2. Ölçüm zinciri

BERO'nun incelenen ölçüm yolu kavramsal olarak şöyledir:

1. **SCT013-030:** Primer akım, CT sekonderinde AC gerilim üretir. İncelenen 30 A / 1 V gerilim çıkışlı varyantta burden direnci sensör gövdesindedir; normalde harici burden eklenmez.
2. **Bias devresi:** AC sinyal yaklaşık 1,65 V DC orta nokta çevresine taşınır. Böylece ESP32 ADC girişinde negatif gerilim oluşmadan AC dalga gözlenebilir.
3. **ESP32 ADC:** SCT-1 sinyali BERO Log 63 kurulumunda GPIO32 / ADC1_CH4 üzerinden okunmuştur. Ortak bias ayrıca GPIO35 / ADC1_CH7 üzerinden izlenmiştir.
4. **ESPHome ADC bileşeni:** ADC kaynağı örnekleme çağrısında gerilimi volt cinsinden döndürür. Kalibrasyon yolu kullanıldığında ADC ham sayısı kalibrasyon fonksiyonundan geçirilip mV tam sayı çözünürlüğünde volt değerine dönüştürülebilir.
5. **ESPHome ct_clamp:** Aktif pencere boyunca ADC kaynağını tekrar tekrar çağırır, geçerli ve önceki örnekten farklı değerleri toplar, AC RMS gerilimini hesaplar ve sensör durumunu yayımlar.
6. **Ölçekleme:** BERO yapılandırmasında kullanılan 24,22 katsayısı gerilim RMS değerini akım göstergesine çevirir. Bu katsayı, yalnızca SCT etiketinden çıkarılan evrensel bir oran değil, mevcut sistemin ampirik ölçek katsayısı olarak ele alınmalıdır.

GPIO35 bias izleme kanalı, GPIO32'den alınan ct_clamp örneklerinin parçası değildir. Bias'ın sabit DC bileşeni, ct_clamp'in aynı pencere içindeki ortalamayı çıkarma işlemiyle matematiksel olarak etkisizleşir. Ancak bias pencere içinde değişirse bu değişim AC varyansına katkıda bulunabilir.

## 3. Kaynak kod davranışı

ESPHome 2026.10.1 kaynak kodunda ct_clamp'in temel akışı şöyledir:

- `update()` örnekleme fazını başlatır, yüksek frekanslı döngü modunu etkinleştirir, pencere bitiş zamanlayıcısını kurar, örnek sayaçlarını ve toplamları sıfırlar.
- Pencere açıkken `loop()` ADC kaynağının `sample()` fonksiyonunu çağırır.
- NaN değerler hesaba alınmaz.
- Önceki kabul edilen örnekle aynı olan ardışık değer atlanır.
- Kabul edilen her örnek için örnek sayısı, örneklerin toplamı ve kareleri toplamı güncellenir.
- Süre dolduğunda örnekleme durdurulur ve RMS hesaplanıp `publish_state()` ile yayımlanır.

Kaynakta kullanılan matematik:

`mean = Σvᵢ / N`

`mean_square = Σ(vᵢ²) / N`

`AC_RMS = √(mean_square − mean²)`

Negatif yuvarlama sonucu oluşursa kaynak kod negatif karekök almamak için sonucu sıfıra sınırlar. Bu işlem örneklerin mutlak değerlerinin ortalaması değildir; DC ortalamayı varyans özdeşliğiyle ayıran RMS hesabıdır.

**Önemli ayrıntı — tekrar eden örneklerin elenmesi:** Kaynakta `last_value_ == value` koşuluyla ardışık eşit örnekler atlanır. Her kabul edilen örneğe eşit ağırlık verilir, ancak kabul edilen örneklerin zaman aralıkları eşit değildir. Bu nedenle hesap, klasik sabit hızlı örnekleme ile alınmış zaman-ağırlıklı RMS'e eşdeğer olmak zorunda değildir.

İdealize edilmiş bir sınır durumunda, sinüs dalgasının her genlik kodu yükselen ve alçalan kolda birer kez tutulursa kabul edilen genlikler zaman boyunca eşit dağılmak yerine genlik ekseninde daha eşit dağılabilir. Bu ideal modelde RMS oranı `√(2/3) ≈ 0,8165` seviyesine, yani sinüsün zaman-ağırlıklı RMS değerinden yaklaşık %18,35 aşağıya gidebilir. **Bu teorik sınır senaryosudur; BERO'da ölçülmüş bir hata değildir.** Gerçek etki ADC çözünürlüğü, gürültü, döngü hızı, örnek sayısı ve sinyal genliğine bağlıdır.

Loglarda görülen SPS alanı, kaynak kodun kabul ettiği farklı örneklerin pencereye oranıysa, gerçek ADC dönüşüm sayısıyla aynı şey değildir. Bu iki hız birbirinden ayrılmalıdır.

## 4. Örnekleme penceresi ve yayın aralığı

50 Hz şebekede bir periyot 20 ms'dir:

| sample_duration | 50 Hz periyot sayısı |
|---:|---:|
| 100 ms | 5 |
| 200 ms | 10 |
| 500 ms | 25 |
| 1 s | 50 |

200 ms, nominal 50 Hz'de 10 periyot kapsar. Kararlı yük gözlemi için makul bir başlangıç penceresidir. Daha uzun pencere daha fazla çevrim kapsar; fakat termostat, motor veya yük anahtarlaması gibi durum değişikliklerini tek ölçüm içine karıştırabilir.

`update_interval: 2s` ise pencere süresiyle aynı kavram değildir. 200 ms örnekleme penceresi her 2 saniyede bir başlatılıyorsa yaklaşık 1,8 saniye pencere dışı kalır. Pencere dışındaki dönemde ct_clamp'in kendi `loop()` örnek toplama bölümü etkin değildir.

ESPHome ADC sensörünün kendi 1 saniyelik `update_interval` ayarı farklı bir yayın/okuma yoludur. ct_clamp, aktif penceresinde ADC kaynak nesnesinin `sample()` fonksiyonunu doğrudan çağırır; ADC sensörünün Home Assistant'a yayımladığı tekil 1 saniyelik durum değerlerini RMS girdisi olarak kullanmaz.

Bu yapı kısa olayları kaçırabilir. BERO'nun PZEM ile eşleştirme yaklaşımında yalnız kararlı ve zaman bakımından örtüşen pencerelerin kullanılmasının nedeni budur.

## 5. ESP32 ADC ve sayısal çözünürlük

BERO'da kullanılan ESP32D1 kartının klasik ESP32 tabanlı olduğu ve Log 63'te GPIO32'nin ADC1_CH4 olarak kullanıldığı kaydedilmiştir. Klasik ESP32 ADC 12 bit sınıfındadır; ancak 12 bit çözünürlük, 12 bit mutlak doğruluk anlamına gelmez.

Espressif dokümanları ADC referans gerilimi ve doğrusal olmayanlık nedeniyle kalibrasyon kullanılmasını önerir. Orijinal ESP32 için 11 dB attenuation koşulunda önerilen doğruluk aralığı yaklaşık 150–2450 mV'dir. Bu aralık, ADC'nin fiziksel olarak ölçebildiği mutlak üst sınırla karıştırılmamalıdır. BERO'nun yaklaşık 1,66 V bias noktası bu önerilen aralık içindedir.

ESPHome'un ESP32 ADC uygulamasında kalibrasyon destekleniyorsa ham ADC sayısı kalibrasyon karakteristiğiyle gerilime çevrilir. Bu yolun çıkışı mV tam sayı basamaklarına yuvarlanabildiği için uygulamaya ulaşan gerilim örnekleri 1 mV adımlı olabilir. Kalibrasyon başlatılamazsa kaynak kodun yedek dönüşümü farklı hata karakteristiğine sahip olabilir. Bu nedenle gerçek derleme/logda kalibrasyon yolunun başarıyla başlatıldığı doğrulanmalıdır.

ADC attenuation ayarının ESPHome YAML'ındaki adı ile ESP-IDF sürümündeki enum/gerçek donanım seviyesi birebir aynı adlandırılmayabilir. BERO kaydındaki “12 dB” ifadesi, kullanılan ESPHome/ESP-IDF sürüm bağlamıyla okunmalıdır.

## 6. Düşük akım bölgesi — hesap ve riskler

K=24,22 A/V varsayımıyla gerilim karşılıkları:

| Akım göstergesi | AC RMS gerilim | Sinüs tepe değeri |
|---:|---:|---:|
| 0,1 A | 4,13 mV | 5,84 mV |
| 0,3 A | 12,39 mV | 17,52 mV |
| 0,5 A | 20,64 mV | 29,19 mV |
| 1,0 A | 41,29 mV | 58,39 mV |

Bunlar K katsayısından türetilmiş hesap değerleridir; gerçek sensör ölçümü değildir.

Düşük akımda başlıca riskler:

- **ADC mV basamağı:** 0,1 A karşılığı yaklaşık 4,13 mV RMS olduğundan 1 mV çıkış basamağı küçük sinyalin anlamlı bir bölümüdür.
- **Analog gürültü:** Gürültü, gerçek AC sinyal varyansına eklenebilir. ct_clamp kodunda otomatik boşta gürültü tabanı çıkarımı veya sıfır eşiği yoktur.
- **Tekrar örnek eleme:** Düşük genlikte aynı ADC kodunun ardışık tekrarları daha sık görülebilir; kabul edilen örnek sayısı ve genlik dağılımı değişebilir.
- **Bias hareketi:** Sabit bias ortalama çıkarma ile yok olur; pencere içinde değişen bias, RMS hesabına ek varyans olarak girebilir.
- **Sayısal iptal:** `mean_square − mean²` işlemi, büyük DC ofset üzerindeki küçük AC varyansını elde eder. Bu tür çıkarma sayısal hassasiyete duyarlıdır. Ancak BERO'daki etkisinin büyüklüğü mevcut logla ölçülmüş değildir.

Bu nedenle 0,1–0,3 A alanında tek katsayıyla güvenilirlik ilan edilmemelidir. BERO'nun güncel proje deney kararı gereği 0,30 A altı gözlem alanında ±%4 kabul/ret uygulanmaz. Bu eşik üretici minimum akım spesifikasyonu değildir.

## 7. Yüksek akım bölgesi — hesap ve headroom

Aynı K=24,22 A/V varsayımıyla:

| Akım göstergesi | AC RMS gerilim | Bias 1,66 V varsayımıyla pozitif tepe |
|---:|---:|---:|
| 3 A | 0,124 V | 1,835 V |
| 8 A | 0,330 V | 2,127 V |
| 10 A | 0,413 V | 2,244 V |

Bu hesapta 10 A düzeyinde pozitif tepe yaklaşık 2,244 V'tur; orijinal ESP32 için kaynak dokümanında verilen yaklaşık 2,45 V önerilen doğruluk üst sınırının altındadır. Aynı basit modelde bu sınıra yaklaşık 13,5 A civarında yaklaşılır.

Bu bir ADC doygunluk testi değildir. Gerçek tepe, bias seviyesi, SCT dönüşümü, analog devre, ADC kalibrasyonu ve dalga biçimine bağlıdır. Kodda doygunluk düzeltmesi veya kırpılmış örnekleri telafi eden bir algoritma yoktur. ADC kırpılırsa RMS ve dolayısıyla akım göstergesi düşük kalabilir.

SCT013-030 için üretici/dağıtıcı veri sayfasında 30 A → 1 V nominal çıkış ve dahili burden bilgisi verilir. K=24,22 A/V ise tersine 30 A için yaklaşık 1,239 V RMS bekletir. Bu fark, katsayının sensörün nominal oranıyla aynı olmadığını gösterir. K, mevcut tüm zincirin ampirik katsayısı olarak tutulmalı; sensör etiketiyle birebir oran gibi sunulmamalıdır.

## 8. BERO Log 63 — gerçek kayıtla sınırlı değerlendirme

**Kaynak:** 2026-10-31 BREAD-TOASTER-001 / ESP32D1 Log 63.

- ESPHome 2026.10.1.
- SCT-1: GPIO32 / ADC1_CH4.
- Ortak bias izleme: GPIO35 / ADC1_CH7.
- ADC sensör güncellemesi: 1 s.
- ct_clamp penceresi: 200 ms.
- ct_clamp yayın aralığı: 2 s.
- K: 24,22; firmware değiştirilmedi.
- İlk açılış yayını 3,027 A; 186 örnek / 930 SPS olduğu için kararlı istatistik dışında tutuldu.
- Kalan 50 yayın: ortalama 3,09636 A; medyan 3,094 A; min–maks 3,071–3,144 A; örnek SD 0,01340 A; CV %0,433.
- Kararlı Raw AC ortalaması: 0,127843 V.
- Kabul edilen örnek hızı ortalaması: yaklaşık 18.117 SPS.
- GPIO35 bias medyanı: 1,664 V; ortalaması 1,66203 V. Tekil 1,565 V örneği vardır; nedeni bu logla belirlenmemiştir.

Aritmetik kontrol: 0,127843 × 24,22 = 3,09636. Logdaki ölçekleme bu çarpımla tutarlıdır.

UNIT 3,30 A kullanıcı bildirimidir. SCT ortalamasına göre aritmetik fark yaklaşık −0,20364 A / −%6,17'dir. Ancak bu değer PZEM değildir ve aynı zaman damgasına ait kararlı pencere eşleşmesi belgelenmemiştir. Dolayısıyla bu fark doğruluk veya kalibrasyon sonucu değildir.

## 9. Yüklenen kullanıcı raporuyla ayrım ve değerlendirme

Aynı klasörde ayrıca kullanıcının sağladığı “ESPHome ct_clamp iç çalışma raporu” özgün DOCX biçiminde korunmuştur. O raporun simülasyon tabloları, LSB/gürültü varsayımları ve bazı sonuçları kullanıcı belgesine ait bulgulardır; bu bağımsız incelemenin BERO'da yeniden ürettiği ölçümler olarak sunulmamıştır.

Özellikle:

- Kullanıcı raporunun başlığı GPIO33 der; BERO Log 63 ve güncel Modül 2 kaydı SCT-1 için GPIO32'yi gösterir. Bu pin farkı tarihsel belge üzerinde değiştirilmemiştir.
- Kullanıcı raporundaki 0,1–0,5 A simülasyon tablosu, float32 ve dedup yüzdeleri sandbox simülasyonu olarak işaretlenmiştir. Bunlar gerçek BERO ölçüm sonucu değildir.
- Kullanıcı raporunun `sample_duration` için verdiği kesirli periyot hata yaklaşımı, raporun kendi türetimidir; kaynak kod veya BERO testiyle doğrulanmış bir hata garantisi değildir.
- Bu bağımsız inceleme, tekrar örnek eleme davranışının örnekleri zaman bakımından eşit ağırlıklı olmaktan çıkardığını kaynak kod üzerinden doğrular; ancak gerçek sapma yüzdesini ölçülmüş kabul etmez.
- İki rapor da sabit bias ortalamasının çıkarılabildiği konusunda aynı matematiksel sonuca gelir. Pencere içi bias değişimi ise ayrıca değerlendirilmelidir.

## 10. Mühendislik kararı ve önerilen doğrulama sırası

**Mevcut ayarları şimdilik koru.** Yalnızca teorik dedup etkisine dayanarak firmware değiştirmek doğru değildir. Önce etkisini gözlenebilir hale getir:

1. **Yüksüz kayıt:** Raw AC, bias, örnek sayısı ve SPS aynı pencere için birlikte kaydedilsin. N arttıkça Raw AC tabanı sistematik değişiyor mu bakılsın.
2. **Tekrar örnek tanısı:** Toplam ADC sample çağrısı, aynı değere denk gelen tekrar sayısı ve kabul edilen farklı örnek sayısı ayrı sayaçlarla izlenebilsin. Bu tanı kodu ölçüm algoritmasını değiştirmeden çalışmalı.
3. **Düşük akım taraması:** 0,1 / 0,3 / 0,5 / 1 A civarı koşullar, güvenli ve kararlı yüklerle tekrarlansın. 0,30 A altı gözlem olarak raporlansın; ±%4 kabul/ret uygulanmasın.
4. **Kararlı orta/yüksek akım:** 3 A, 7 A ve mümkünse 8–10 A çevresinde aynı yükte tekrarlı pencereler alınsın. ADC tepe payı ve kararlılık izlenmeli.
5. **Referans eşleştirmesi:** PZEM akımı ve SCT penceresi aynı zaman aralığında kararlı olmalı. UNIT/PENS bildirimleri PZEM gibi etiketlenmemeli.
6. **Son karar:** Dedup kaynaklı sapma gerçek ölçümle gösterilirse alternatif zaman-ağırlıklı örnekleme değerlendirilir. O zamana kadar çalışan yapı korunur.

Şebeke tarafındaki bağlantı ve yük deneyleri yalnız uygun muhafaza/koruma ve yetkin uygulama ile yapılmalıdır. CT sekonderi üretici talimatı aksini söylemedikçe primer akım geçerken açık bırakılmamalıdır.

## 11. Sonuç

ct_clamp, BERO'nun kararlı yük davranışını izleme ve PZEM kararlı pencereleriyle eşleştirme hedefi için kullanılabilir bir başlangıç katmanıdır. Ancak kaynak kodundaki tekrar örnek eleme davranışı, ölçümün klasik zaman-ağırlıklı RMS ile aynı olmasını garanti etmez. 200 ms / 2 s ayarı sürekli dalga kaydı değil, seyrek aralıklı kısa pencerelerdir.

Log 63, 3,1 A civarında kısa pencere çıktısının kendi içinde düşük dağılım gösterdiğini ve 24,22 ölçek çarpımının tutarlı olduğunu kanıtlar. Tek başına sensör doğruluğunu, düşük akım performansını, 10 A üstünü veya enerji ölçüm yeterliliğini kanıtlamaz.

Bu sistem enerji analizörü değildir; gerilim, faz, aktif güç ve enerji ölçüm zincirini tamamlamaz. Mevcut proje kapsamı içinde doğru kullanım, SCT gerilim davranışını gözlemek ve eşleşmiş PZEM kararlı pencereleriyle etiketlemektir.

## 12. Kaynaklar

### ESPHome 2026.10.1 — sabit commit

- [ct_clamp_sensor.cpp](https://github.com/esphome/esphome/blob/4ea26ed/esphome/components/ct_clamp/ct_clamp_sensor.cpp)
- [ct_clamp_sensor.h](https://github.com/esphome/esphome/blob/4ea26ed/esphome/components/ct_clamp/ct_clamp_sensor.h)
- [ct_clamp sensor schema](https://github.com/esphome/esphome/blob/4ea26ed/esphome/components/ct_clamp/sensor.py)
- [ESP32 ADC implementation](https://github.com/esphome/esphome/blob/4ea26ed/esphome/components/adc/adc_sensor_esp32.cpp)
- [ESPHome ct_clamp documentation](https://esphome.io/components/sensor/ct_clamp/)

### Üretici / donanım referansları

- [Espressif ESP32 datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)
- [ESP-IDF ADC calibration documentation](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/adc/adc_calibration.html)
- [SCT-013-030 30 A / 1 V datasheet copy](https://learn.openenergymonitor.org/electricity-monitoring/ct-sensors/files/YHDC-SCT-013-030V.pdf)

### BERO kanıtları

- [BREAD-TOASTER-001 test kaydı](../../../test-loads/bread-toaster/README.md)
- [Log 63 teknik analiz](../../../logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-analysis.md)
- [Log 63 tam ham kayıt](../../logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-full.txt)

---

**Kanıt sınıflandırması:** Kaynak kod davranışı = kaynak kod incelemesi; ADC aralığı ve SCT nominal bilgileri = üretici/doküman; Log 63 istatistikleri = paylaşılan gerçek log; 0,1–10 A gerilim tabloları ve 13,5 A yaklaşımı = belirtilen K ve bias varsayımıyla hesap; √(2/3) dedup sonucu = idealize teorik senaryo; simülasyon yüzdeleri = bu raporda yeniden doğrulanmadı.
