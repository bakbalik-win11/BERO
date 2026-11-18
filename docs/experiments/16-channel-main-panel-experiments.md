# BERO — 16 Kanallı Ana Pano İçin Ön Araştırma Deneyleri

Bu kayıt, 16 kanallı ana pano mimarisine karar vermek için planlanan iki deneyin amaçlarını, düzeneklerini ve karar ölçütlerini tanımlar. Deneyler henüz yapılmış değildir; sonuç veya doğrulanmış tasarım kararı içermez.

## Deney 1 — Aynı SCT hattında biaslı / biassız ölçüm karşılaştırması

### Amaç
Özellikle yüksek akım seviyelerinde ölçüm problemi yaşamamak. Bias uygulamasının mevcut ölçüm yöntemine göre ölçüm davranışını iyileştirip iyileştirmediğini aynı sensör ve aynı yük üzerinde karşılaştırmalı olarak incelemek. Sonuçlar, 16 kanallı ana pano analog giriş mimarisine karar vermek için kullanılacaktır.

### Deney düzeni
- Aynı SCT sensörü ve aynı akım hattı kullanılacak.
- ADS1115'in A0–A1 diferansiyel çifti: mevcut biassız ölçüm.
- ADS1115'in A2–A3 diferansiyel çifti: biaslı ölçüm.
- Bias, BERO kapsamında imal edilmiş Modül 1 bias devresinden sağlanacak.
- İki ölçüm aynı yük koşullarında karşılaştırılacak.

### Karşılaştırılacak gözlemler
- Okunan akım ve iki ölçüm arasındaki fark
- Gürültü ve dalgalanma
- Kararlı ölçüm davranışı
- Yüksek akım seviyelerinde ölçüm sınırları, bozulma veya clipping belirtileri
- Ölçüm aralığı ve kullanılabilirlik

### Beklenen karar çıktısı
Biasın yüksek akım bölgesindeki davranışa etkisi deneyle belirlenecek. 16 kanallı ana panoda bias kullanımı, bias bağlantı biçimi ve analog giriş yapısı ölçüm sonuçlarına göre kararlaştırılacak.

### Güvenlik / teknik kontrol
Deney bağlantısı kurulmadan önce ADS1115 girişlerinin mutlak ve diferansiyel gerilim sınırları, bias devresinin çıkışı ve SCT sinyalinin ADC girişlerinde oluşturacağı gerilim aralığı doğrulanmalıdır. PDF'deki bağlantı şeması doğrudan kabul edilmiş tasarım değildir.

---

## Deney 2 — TCA9548A ile çoklu ADS1115 okuma ve veri toplama mimarisi

### Amaç
16 kanallı ana pano için mümkün olan en hızlı, en kaliteli ve en kararlı çoklu okuma mimarisini bulmak. Çoklu ADC'lerin tarama/okuma yapısı, mümkün olan eş zamanlı veya zaman örtüşmeli dönüşüm yaklaşımları, ESP32 işlem yükü ve Home Assistant'a veri aktarımı birlikte değerlendirilir.

### Araştırma kapsamı
- TCA9548A üzerinden birden fazla ADS1115'i yönetmek.
- I²C kanal seçimi ve ADC okuma sırasının toplam tarama süresine etkisi.
- ADS1115 dönüşümlerini sırayla başlatma/okuma ve dönüşümleri zaman örtüşmeli yürütme (pipelining) olasılığını incelemek.
- Gerçek eş zamanlı ölçüm ile hızlı ardışık taramayı ayırt etmek; eş zamanlılık iddiasını ölçmeden kullanmamak.
- Ölçüm/işleme döngüsünü Home Assistant haberleşmesinden mümkün olduğunca ayırmak.
- ESP32 üzerinden ölçüm verisini Home Assistant'a iletmek ve haberleşmenin ölçüm döngüsüne etkisini test etmek.

### Ölçülecek performans
- Tüm kanallar için toplam tarama süresi
- Kanal başına örnekleme hızı
- Kanallar arası zaman farkı / gecikme
- Okuma kararlılığı ve veri kaybı
- ESP32 işlem yükü
- Wi-Fi ve Home Assistant gönderim gecikmesinin ölçüm döngüsüne etkisi
- Hız artarken ölçüm kalitesinin korunup korunmadığı

### Beklenen karar çıktısı
Ana pano için kanal sayısı, ADC ve multiplexer kullanımı, tarama/okuma zamanlaması, veri işleme ve Home Assistant'a yayın mimarisi deney sonuçlarına göre seçilecek.

### TCA9548A'nın potansiyel katkısı
TCA9548A, aynı I²C adresinde çalışan birden fazla ADS1115'in kanal seçimiyle yönetilmesini sağlayarak ana pano kablolamasını ve adres yönetimini sadeleştirebilir. Bu sadeleşme ve performans avantajı henüz bir hipotezdir; prototip üzerinde doğrulanacaktır.

---

## Ana pano tasarım kararı

İki deney birbirini tamamlar:
- Deney 1, tek kanalın analog ölçüm yaklaşımını (biaslı veya biassız) belirlemeye yardım eder.
- Deney 2, çok kanallı ölçüm, tarama, zamanlama ve Home Assistant veri aktarım mimarisini belirlemeye yardım eder.

Bu deneyler tamamlanmadan 16 kanallı ana pano için nihai imalat kararı verilmez. Son karar; deney kayıtları, ölçüm kalitesi, zaman çözünürlüğü, kararlılık ve uygulama kolaylığı üzerinden verilecektir.


## Ana pano için alternatif mimari fikirler

Bu bölüm, TCA9548A araştırmasıyla ortaya çıkan alternatif yapıları final imalat kararı öncesinde karşılaştırmak üzere eklenmiştir. Bunlar aday mimarilerdir; henüz doğrulanmış tasarım veya imalat kararı değildir.

### Alternatif A — Önceden düşünülen dağıtık yapı: 2 ESP × 3 ADS1115 = 12 SCT

- 2 ESP32 kullanılır.
- Her ESP 3 ADS1115 yönetir.
- Her ADS1115'in iki diferansiyel ölçüm çiftiyle 2 SCT ölçülmesi hedeflenir.
- Toplam: 6 ADS1115 ve 12 SCT ölçüm kanalı.
- Ölçüm ve haberleşme yükü iki ESP'ye dağıtılır.

**Değerlendirme:** Dağıtık işlem ve olası yük paylaşımı avantajı; iki ayrı ESP, Wi-Fi bağlantısı, firmware ve cihaz yönetimi gerektirir.

### Alternatif B — Tek ESP + TCA9548A + 6 ADS1115 = 12 SCT

- Tek ESP32 kullanılır.
- Bir TCA9548A üzerinden 6 ADS1115, ayrı mux kanallarına yerleştirilerek yönetilir.
- Her ADS1115 ile 2 SCT ölçümü hedeflenir.
- Toplam: 6 ADS1115 ve 12 SCT ölçüm kanalı.
- Tek firmware, tek Wi-Fi bağlantısı ve tek Home Assistant bağlantısı.

**Değerlendirme:** Dağıtık yapıdaki iki ESP'yi tek kontrolcüde birleştirerek cihaz, kablolama ve yönetim düzenini sadeleştirme potansiyeli taşır. Toplam tarama süresi, kanal başına hız ve ölçüm kalitesi deneyle doğrulanmalıdır.

### Alternatif C — Tek ESP + TCA9548A + 8 ADS1115 = 16 SCT

- Tek ESP32 ve bir TCA9548A kullanılır.
- TCA'nın 8 kanalına 8 ADS1115 yerleştirilmesi planlanır.
- Her ADS1115 ile 2 SCT ölçümü hedeflenir.
- Teorik toplam: 16 SCT ölçüm kanalı.

**Değerlendirme:** En az ESP sayısıyla 16 kanala ulaşma olasılığı sunar. Ancak tarama süresi, kanal başına örnekleme hızı, I²C ve ADC zamanlaması, ESP32 yükü, Wi-Fi/HA aktarımı ve ölçüm kalitesi prototip üzerinde test edilmeden uygulanabilir final tasarım olarak kabul edilmez.

### Alternatiflerin karşılaştırmalı karar ölçütleri

| Ölçüt | A: 2 ESP / 12 kanal | B: 1 ESP / 12 kanal | C: 1 ESP / 16 kanal |
|---|---|---|---|
| ESP sayısı | 2 | 1 | 1 |
| ADS1115 sayısı | 6 | 6 | 8 |
| TCA9548A | Yok (ilk tasarım) | 1 | 1 |
| SCT kanalı | 12 | 12 | 16 |
| Kontrol ve HA bağlantısı | 2 cihaz | 1 cihaz | 1 cihaz |
| Mimari karmaşıklık | Dağıtık | Merkezi | Merkezi, daha fazla kanal |
| Ölçüm hızı/kalitesi | Test edilecek | Test edilecek | Test edilecek |
| Final kararı | Deney sonrası | Deney sonrası | Deney sonrası |

### TCA9548A ile sadeleşme hipotezi

TCA9548A, aynı I²C adresindeki ADS1115'leri mux kanallarında ayırarak adres yönetimini kolaylaştırabilir ve ana pano bağlantılarını daha düzenli hale getirebilir. Bu nedenle yalnızca kanal çoğaltma komponenti olarak değil, modülün kablolama, montaj, firmware ve bakım düzenini sadeleştirme adayı olarak değerlendirilecektir.

### Karar ilkesi

Ana pano final imalatı; kanal sayısı tek başına esas alınarak seçilmeyecektir. Üç aday yapı, deneylerden elde edilen gerçek tarama hızı, zaman çözünürlüğü, ölçüm kararlılığı, haberleşme etkisi, kablolama/kurulum kolaylığı ve bakım edilebilirlik birlikte değerlendirilerek karşılaştırılacaktır. Tek ESP'li 12 kanal yapısı, TCA9548A ile sadeleşme sağlayıp performans hedeflerini karşılayabiliyorsa güçlü bir adaydır.
