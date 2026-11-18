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
