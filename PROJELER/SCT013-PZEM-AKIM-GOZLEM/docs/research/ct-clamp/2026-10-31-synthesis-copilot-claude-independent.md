# ESPHome ct_clamp — üç kaynaklı sentez

**Tarih:** 2026-10-31  
**Kaynaklar:** Kullanıcının sağladığı Claude raporu, GitHub Copilot raporu, önceki bağımsız kaynak kod/tarihçe incelemesi ve bu sentez sırasında GitHub PR kayıtları.  
**Amaç:** Aynı sorulara verilen yanıtları birleştirmek; doğrulanmış tarihsel olguları, kod davranışını, kaynak yorumlarını ve BERO'ya ilişkin çıkarımları ayırmak.

## Yönetici özeti

ESPHome `ct_clamp`, bir CT (current transformer) sensöründen alınan analog gerilim örneklerinden **AC akımın RMS değerini** üretmek üzere geliştirilmiş bir akım sensörü bileşenidir. Enerji sayacı, güç analizörü veya genel amaçlı AC gerilim RMS ölçeri değildir. Akım trafosunun analog sinyalini örnekler; CT devresindeki DC ofseti AC bileşenden ayırarak RMS hesabı yapar ve akım sensörü çıktısı üretir.

İlk bileşen 2019'da Jesse Hills'in PR'ı ile eklendi. Otto Winter mimari inceleme ve kod katkısı yaptı. 2021'de AC bileşeninin standart sapma üzerinden hesaplanması, çoklu CT örneklemesinin eşgüdümü, NaN/negatif karekök ve yinelenen örnekler gibi konularda bir dizi iyileştirme geldi. Dolayısıyla Copilot'un 2021 PR'larını tasarımın ilk kanıtı olarak göstermesi, ilk bileşen tarihçesini atladığı için eksiktir; ancak 2021 kayıtları algoritmanın ve sınır durumlarının nasıl olgunlaştırıldığını anlamak için önemlidir.

## 1. Kim geliştirdi, ne zaman eklendi?

- **İlk PR:** [#559 — Add CT Clamp component](https://github.com/esphome/esphome/pull/559), 26 Mayıs 2019.
- **İlk bileşen commit'i:** [3089ffa](https://github.com/esphome/esphome/commit/3089ffa8e73ee6daaa453704342a616ccef5c948), 29 Mayıs 2019.
- **Ana ilk kod katkısı:** Jesse Hills (@jesserockz).
- **Mimari katkı:** Otto Winter (@OttoWinter), PR incelemesinde doğrudan tasarım/kod önerileri sundu ve örnekleme mimarisinin ana döngüyü bloke etmemesi için değişiklik yaptı.

Copilot'un `sensor.py` içindeki güncel CODEOWNERS kaydından tek bir ilk yaratıcı çıkarılamayacağı uyarısı yerindedir: mevcut code owner bilgisi tarihsel ilk yazarlığı tek başına kanıtlamaz. Ancak PR #559 ve ilk commit, ilk katkının kimden geldiğini ayrıca gösterir. En doğru tanım: **Jesse Hills'in başlattığı, Otto Winter'ın önemli mimari katkı verdiği ESPHome bileşeni.**

## 2. Hangi ihtiyaca yönelikti?

İlk PR, CT clamp üzerinden akım sensörü eklemeyi hedefler. Jesse, kodun büyük bölümünü OpenEnergyMonitor EMonLib'den aldığını ve CTL-10-CLS pensiyle D1 Mini üzerinde evin tek fazlı hattını ölçerek akıllı sayaçla karşılaştırdığını belirtmiştir.

Bu nedenle:
- SCT013'e özel değildir; belirli bir CT modeline sabitlenmemiştir.
- Herhangi bir AC gerilim kaynağından RMS gerilim ölçen genel amaçlı bir bileşen değildir.
- CT pensi/akım trafosu sinyalinden AC akım üretmek üzere tasarlanmıştır.
- Kendi başına Wh/kWh, aktif güç, reaktif güç, PF, harmonik veya güç kalitesi analizi yapmaz.

**Terminoloji düzeltmesi:** “Genel AC RMS ölçüm bileşeni” ifadesi fazla geniştir. “CT sensörlü AC RMS akım sensörü” daha doğrudur.

## 3. AC bileşeni ve DC ofset hesabı

[PR #1906 — Calculating the AC only component of the samples](https://github.com/esphome/esphome/pull/1906), örneklerin AC bileşenini standart sapma formülüyle hesaplayarak offset kalibrasyonu ihtiyacını ortadan kaldırmayı hedeflediğini açıkça yazar. PR açıklaması bu değişikliği “standard-deviation” formülüyle ilişkilendirir.

Örnekler (x_i) ise kullanılan yaklaşımın özü:

[
V_{AC,RMS} = sqrt{E[x^2] - E[x]^2}
]

Bu, örneklerin standart sapmasıdır; sabit DC merkez/ofset bileşenini AC RMS hesabından ayırır. Akım çıktısı daha sonra sensör/kurulum katsayısıyla ölçeklenir.

Bu nedenle Copilot'un “DC ofseti çıkararak RMS hesaplar” özeti genel olarak doğrudur. Daha hassas tarihsel ifade şudur: bu hesap yaklaşımının açık PR açıklaması 2021 tarihli #1906'dır; ilk 2019 bileşeninin CT akımı ölçme amacı ise daha eskidir.

## 4. Önemli geliştirme adımları

| Kayıt | Belgelenmiş amaç / sorun | Sentez yorumu |
|---|---|---|
| [PR #559](https://github.com/esphome/esphome/pull/559), 2019 | CT clamp akım sensörünün eklenmesi; farklı voltage sampler kaynaklarını destekleme; örneklemenin ana döngüyü bloke etmemesi | İlk bileşen ve temel mimari |
| [PR #1906](https://github.com/esphome/esphome/pull/1906), 2021 | Standart sapma formülüyle AC-only örnek bileşenini hesaplamak; offset kalibrasyonu ihtiyacını kaldırmak | DC ofsetten bağımsız AC RMS yaklaşımının açıklaştırılması |
| [PR #1915](https://github.com/esphome/esphome/pull/1915) | Birden fazla ct_clamp aynı anda örneklemeye çalışınca ölçüm başına örnek sayısının azalması; örneklemeyi mutex ile sıraya koymak | Çoklu CT eşzamanlılığı sorunu; `last_value` filtresiyle karıştırılmamalı |
| [PR #1916](https://github.com/esphome/esphome/pull/1916) | AC hesabında negatif karekökten NaN oluşmasını önlemek | Sayısal sınır durumu düzeltmesi |
| [PR #2283](https://github.com/esphome/esphome/pull/2283), 2021 | Yinelenen örnekleri atarak doğruluğu iyileştirmek; ESPHome 1000 SPS isteyebilirken ADS1115'in nadiren 860 SPS üzerine çıkması | `last_value` filtresinin eklenmesi |
| [PR #4229](https://github.com/esphome/esphome/pull/4229) | Akım yokken sürekli sıfır örneklerinin NaN yerine 0 A olarak ele alınması | Sıfır akım semantiği |
| [PR #4236](https://github.com/esphome/esphome/pull/4236) | Sıfır akımda negatif karekökün NaN üretmesini önlemek | RMS sayısal güvenliği |

PR #1915'in çoklu CT örnekleme kilidi, #2283'teki yinelenen değer filtresiyle aynı problem değildir. Birincisi aynı anda çalışan birden fazla ct_clamp örnekleyicisinin birbirini etkilemesini; ikincisi ADC kaynağının talep edilenden daha düşük dönüşüm hızı nedeniyle aynı değeri tekrar döndürmesini ele alır.

## 5. sample_duration: neden 200 ms?

- İlk bileşende varsayılan pencere 200 ms'dir.
- Resmî dokümantasyon bu değeri 50 Hz'de 10 tam şebeke çevrimi olarak açıklar.
- 60 Hz'de 200 ms, 12 çevrime karşılık gelir.
- Daha uzun örnekleme penceresinin doğruluğu artırabileceği dokümantasyonda belirtilir.

Ancak ilk geliştiricinin neden özellikle 10 çevrimi seçtiğini açıklayan doğrudan bir PR/commit gerekçesi bulunmamıştır. “Kısa ama yeterli pencere”, “CPU ve doğruluk dengesi için seçildi” gibi ifadeler olası mühendislik yorumlarıdır; belgelenmiş tarihsel niyet değildir.

**Sonuç:** 200 ms'nin 50 Hz'de 10 çevrim olduğu doğrulanmıştır. 10 çevrimin neden tercih edildiği kesin olarak bilinmemektedir.

## 6. update_interval: neden 60 saniye?

İlk Python yapılandırmasında `cv.polling_component_schema('60s')` kullanılmıştır. Bu, ESPHome'un genel polling varsayılanıdır; ct_clamp'e özel ölçüm gerekçesi değildir. İlk PR test YAML'ında 5 s, PR içindeki başka bir örnekte 500 ms kullanılmıştır.

- `sample_duration`: bir RMS ölçüm penceresinin ne kadar süre örnekleneceğini belirler.
- `update_interval`: bir sonraki ölçüm penceresinin ne zaman başlatılacağını belirler.

60 saniyenin CPU, telemetri, Home Assistant kayıt yükü veya enerji tasarrufu dengesi için özel olarak seçildiğini gösteren geliştirici açıklaması bulunmamıştır. Copilot'un “60 saniyede bir yayınlamak için seçildi” yorumu, varsayılanın nasıl çalıştığını tarif eder; neden seçildiğini kanıtlamaz.

## 7. last_value filtresi: ne zaman ve neden eklendi?

[PR #2283](https://github.com/esphome/esphome/pull/2283) ile 2021'de eklendi. PR başlığı “Improves ct_clamp component accuracy”; açıklaması, ESPHome'un 1000 SPS'ye kadar örnek isteyebildiğini, ADS1115'in ise nadiren 860 SPS üzerinde örnek sağlayabildiğini belirtir. Kod yorumu da ADC'nin sağlayabileceğinden daha hızlı değer isteme varsayımına dayanır.

### Kodun yaptığı

Mevcut kaynakta sıra şöyledir:
1. `source_->sample()` çağrılarak ADC kaynağından değer istenir.
2. Değer NaN değilse önceki değerle karşılaştırılır.
3. Değer aynıysa fonksiyondan çıkılır; örnek sayaçlarına ve RMS toplamlarına eklenmez.
4. Değer farklıysa istatistiklere katılır.

Dolayısıyla filtre:
- **ADC okuma isteğini durdurmaz.** Örnek çağrısı karşılaştırmadan önce yapılır.
- **Bellek optimizasyonu olarak belgelenmemiştir.**
- **PR'de CPU/performance optimizasyonu olarak tanımlanmamıştır.** Belgelenmiş hedef doğruluk ve yinelenen örneklerin istatistiğe tekrar katılmamasıdır.
- **Aynı fiziksel ADC dönüşümünün tekrarlandığını kesin olarak teşhis etmez.** Aynı sayısal değer, daha yeni bir dönüşümün kuantalama sonucu da olabilir.

PR'nin test ortamı ESP8266 olarak işaretlenmiş, örnek yapılandırması ADS1115 kullanmıştır. Bu nedenle “filtre ESP32 için tasarlandı” denemez. Fakat buradan “ESP32 için gereksizdir” sonucu da çıkmaz; ESP32'nin dahili ADC'sinde eşit sayısal değerlerin nasıl oluştuğu ve filtreye etkisi ayrıca ölçülmelidir.

## 8. Üç kaynağın ortaklaştığı ve ayrıştığı noktalar

### Ortak ve güçlü bulgular
- Bileşen CT tabanlı AC akım ölçümü içindir; enerji ölçümü değildir.
- SCT013'e özel değildir.
- İlk geliştirici Jesse Hills'tir; Otto Winter mimari katkı sağlamıştır.
- 200 ms, 50 Hz'de 10 tam çevrimdir.
- 60 s genel polling varsayılanından gelir; özel tasarım gerekçesi bulunamamıştır.
- `last_value` filtresi sonradan eklenmiştir ve PR gerekçesi yinelenen örneklerin ölçüm istatistiğine tekrar katılmasını önlemektir.
- Filtre ADC okuma çağrısını azaltmaz.

### Düzeltilmesi gereken Copilot ifadeleri
- “İlk net tasarım kanıtı 2021” eksiktir: 2019 PR #559 ve commit #3089ffa ilk bileşeni kanıtlar. 2021 PR #1906, AC-only standart sapma hesabının açık gerekçesini belgeler.
- “60 s CPU/telemetri dengesi için seçildi” desteklenmiyor.
- “200 ms kısa ama yeterli seçildi” ifadesinin tarihsel gerekçesi bulunmuyor.
- `last_value` filtresinin CPU performansı için de tasarlandığı iddiası PR metninde yoktur.
- “Genel AC RMS bileşeni” yerine “CT sensöründen AC RMS akım bileşeni” denmelidir.

### Ek katkı
Copilot'un #1906, #1915, #1916, #4229 ve #4236 kayıtlarını işaret etmesi değerlidir. Bu PR'lar, bileşenin tek seferde tamamlanmış sabit bir algoritma olmadığını; AC bileşeni, çoklu sensör örneklemesi, NaN ve sıfır akım durumları üzerinden zamanla geliştirildiğini gösterir.

## 9. BERO için sonuç ve karar

1. ESPHome `ct_clamp` BERO'nun CT sinyalinden AC RMS akım gözlemi üretmesi için uygun sınıftadır; ancak ESPHome geliştiricilerinin amacı BERO'nun PZEM referanslı kararlı pencere etiketleme sistemi değildir.
2. 200 ms / 2 s / K=24.22 ayarları bu araştırma nedeniyle değiştirilmez.
3. E10 deneyi 200 ms → 500 ms → 1000 ms → 200 ms sırasıyla, aynı yük ve diğer sabitlerle yürütülür. Bu deney pencere süresinin etkisini gözler; tek başına kalibrasyon veya doğruluk testi değildir.
4. `last_value` filtresi şimdilik değiştirilmez. ESP32'de tekrar eden değerlerin kaynağı ve düşük akım bölgesindeki etkisi için ayrı, kontrollü bir karşılaştırma gerekir.
5. Loglardaki `num_samples`/SPS, ham ADC dönüşüm sayısı olarak adlandırılmaz; filtrelenmiş/kabul edilmiş örnek istatistiğidir.
6. Bu araştırmadan ESP32 ADC'sinin ADS1115 ile aynı hız sınırlamasına sahip olduğu veya filtrenin BERO'da yanlılık oluşturduğu sonucu çıkarılmaz.

## 10. Kaynaklar

- İlk PR: https://github.com/esphome/esphome/pull/559
- İlk bileşen commit'i: https://github.com/esphome/esphome/commit/3089ffa8e73ee6daaa453704342a616ccef5c948
- AC-only standart sapma: https://github.com/esphome/esphome/pull/1906
- Çoklu CT sampling mutex: https://github.com/esphome/esphome/pull/1915
- NaN / negatif karekök: https://github.com/esphome/esphome/pull/1916
- Yinelenen örnek filtresi: https://github.com/esphome/esphome/pull/2283
- Sıfır akım davranışı: https://github.com/esphome/esphome/pull/4229
- Negatif karekök düzeltmesi: https://github.com/esphome/esphome/pull/4236
- ADS1115 başlangıç/offset iyileştirmesi: https://github.com/esphome/esphome/pull/647
- ESPHome ct_clamp dokümantasyonu: https://beta.esphome.io/components/sensor/ct_clamp/
- ESPHome 2026.10.1 kaynak kodu: https://github.com/esphome/esphome/blob/4ea26ed/esphome/components/ct_clamp/ct_clamp_sensor.cpp

**Kanıt standardı:** PR açıklamaları geliştirici niyetini; ilk commit ve resmî dokümantasyon tarih/varsayılanları; güncel kaynak kodu çalışma sırasını destekler. Kaynaklarda açıklanmayan tercih nedenleri hipotez olarak kalır. BERO'ya ait yeni fiziksel ölçüm bu sentez sırasında yapılmamıştır.
