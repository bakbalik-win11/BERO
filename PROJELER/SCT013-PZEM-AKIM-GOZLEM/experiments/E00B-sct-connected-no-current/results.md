# E00B sonuç kaydı

## 2026-10-30 — Deney açılışı

### HEDEF
SCT013-030 bağlandıktan sonra, izlenen iletkende akım yokken SCT analog düğümünün bias ve ADC dalgalanmasını E00A SCT'siz bias-only tabanıyla karşılaştırmak.

### LOG
- Deney kimliği: E00B.
- Bias kanalları: GPIO34 RAW (ADC1_CH6), GPIO35 ADC voltajı (ADC1_CH7).
- SCT kanalları önerisi: GPIO32 RAW (ADC1_CH4), GPIO33 ADC voltajı (ADC1_CH5).
- Kart adayı: ESP32-WROOM-32D; gerçek geliştirme kartı pinout'u doğrulanmadı.
- Öncelikli sensör: SCT013-030 (30 A / 1 V).
- Fiziksel bağlantı, firmware, derleme ve cihaz logu henüz yok.

### SONUÇ
Deney açıldı ve pin planı önerildi. GPIO32/33 fiziksel pinout doğrulaması beklediğinden bağlantı yapılmamalıdır. Henüz ölçüm sonucu yoktur. İlk ölçüm koşulu SCT bağlı, primer akım sıfır ve yük kapalı/enerjisiz durumudur.

## 2026-10-30 — E00B firmware derleme bildirimi

### HEDEF
E00B icin bias referans kanallari GPIO34/35 ile SCT dugumu kanallari GPIO32/33'u birlikte gozleyen tam ESPHome firmware'ini olusturmak ve derleme durumunu deney kaydina baglamak.

### LOG
- Firmware: [firmware/esp32d2-e00b-sct-no-current.yaml](firmware/esp32d2-e00b-sct-no-current.yaml)
- GitHub firmware commit'i: `20fbe9b4a99d057ef579d882bfd83d23f4ef199e`.
- Kullanici 2026-10-30 tarihinde kodun derlendigini bildirdi (KULLANICI RAPORU).
- Kodda GPIO34 bias RAW, GPIO35 bias ADC voltaji, GPIO32 SCT RAW, GPIO33 SCT ADC voltaji bulunur.
- Sensor yayin araligi 1 saniyedir. Bu, E08 icin planlanan 1000/2000/2500 SPS ham ornekleme hizlarinin uygulandigi anlamina gelmez.
- Derleme cikti logu bu kayda eklenmedi. Cihaza yukleme, pinout/fiziksel baglanti dogrulamasi ve olcum henuz bildirilmedi.

### SONUC
E00B firmware'i hazir ve kullanici tarafindan basarili derlendigi bildirildi. Deneyin fiziksel olcum asamasi henuz baslamis/kanıtlanmis degildir. E00B durumu PLANLANDI'dan firmware derlendi asamasina ilerledi; fiziksel deney tamamlanmadi.

### SONRAKI ADIM
Gercek gelistirme karti ve GPIO32/33 pinout'unu dogrula; guvenli baglantidan sonra cihaza yukle ve SCT bagli/primer akimsiz kosulun cihaz logunu kaydet.


---

## 2026-10-30 — İlk ESP32D2 saha logu

### HEDEF
E00B firmware'inin cihaza yüklendikten sonra dört ADC kanalını çalıştırdığını doğrulamak; açılış geçişini ayırarak bias ve SCT analog düğümünün akımsız koşuldaki kararlı okumalarını incelemek.

### LOG
- Kaynak dosya: [2026-10-30-e00b-esp32d2-startup-and-observation.log](logs/2026-10-30-e00b-esp32d2-startup-and-observation.log)
- Cihaz: ESP32 rev3.1, 2 çekirdek; ESPHome 2026.9.1.
- Derleme zamanı: 2026-10-30 16:17:02 +0300.
- Log bağlantısı: 192.168.0.66 üzerinden ESPHome API; başarılı çözümleme, bağlantı ve handshake.
- Wi-Fi bağlantısı başarılı; IP 192.168.0.66, RSSI -69 dB.
- Dört ADC kanalı da ADC1 üzerinde, 12 dB attenuation, 1 sample ve 1 saniye update interval ile başlatılmış. Her kanal için Handle Init, Config, Calibration ve Overall Init = OK.
- Log zaman aralığı yaklaşık 16:20:32–16:22:30.
- Açılışın ilk yaklaşık 9 saniyesinde RAW kanalları 0 count ve voltaj kanalları 0.142 V gösterdi. Bu bölüm kararlı ölçüm kabul edilmedi; RAW sıfırları kullanıcı kuralı gereği ölçüm eşlemesine alınmadı.
- Kararlı bölüm için 16:20:41 sonrasındaki 110 örnek/kanal kullanıldı. İstatistikler logda yayınlanan değerlerden hesaplandı; örnekler 1 saniyelik periyodik yayınlar olup yüksek hızlı ham ADC örneklemesi değildir.

| Kanal | n | Ortalama | Std. sapma | Min | Maks |
|---|---:|---:|---:|---:|---:|
| Bias GPIO34 RAW | 110 | 1854.14 count | 9.64 | 1834 | 1874 |
| SCT GPIO32 RAW | 110 | 1853.45 count | 8.22 | 1831 | 1865 |
| Bias GPIO35 ADC | 110 | 1.6651 V | 0.0079 V | 1.635 V | 1.679 V |
| SCT GPIO33 ADC | 110 | 1.6639 V | 0.0063 V | 1.650 V | 1.674 V |

- Kararlı bölümde Bias GPIO34 RAW ile SCT GPIO32 RAW ortalamaları birbirine yakındır (fark yaklaşık 0.68 count).
- Bias GPIO35 ve SCT GPIO33 ADC voltaj ortalamaları arasındaki fark yaklaşık 1.2 mV'dur.
- Ham count değerinden hesaplanan nominal voltaj (count × 3.1 / 4095) yaklaşık 1.404 V seviyesindedir; doğrudan ADC voltajı yaklaşık 1.664 V seviyesindedir. Firmware'deki "Voltage Difference" sensörlerinin yaklaşık 0.25–0.27 V göstermesi bu iki farklı gösterim yönteminin sistematik farkıdır; fiziksel devrede gerçek bir 0.25 V düşüm olarak yorumlanmamalıdır.
- E00A SCT'siz bias-only kaydındaki GPIO34 RAW ortalaması 1846.80 count idi. E00B bias RAW ortalaması 1854.14 count; fark +7.34 count. E00A ve E00B kayıtlarının aynı koşulda ve eşzamanlı alınmış kontrollü tekrarlar olduğu gösterilmediğinden bu fark yalnızca betimleyici karşılaştırmadır.
- Kullanıcı log açıklamasında SCT bağlı/primer akımsız deney bağlamını belirtti; logun kendi satırları primer akımın sıfır olduğunu veya fiziksel bağlantı şemasını bağımsız olarak doğrulamıyor.

### SONUÇ
- Firmware cihazda çalışıyor; ESPHome API bağlantısı ve dört ADC kanalının başlatılması logla doğrulandı.
- Açılışta geçici 0 count / 0.142 V okumaları var. Bunlar geçerli kararlı ölçüm olarak kullanılmamalı.
- Açılış geçişinden sonra bias ve SCT ADC voltaj kanalları yaklaşık 1.664–1.665 V ortalamalarında ve bu log kesitinde düşük saçılma gösteriyor.
- RAW kanalları yaklaşık 1853–1854 count ortalamasında. Bu kesitte SCT kanalının bias kanalından belirgin biçimde ayrıldığına dair bulgu yok.
- Bu kayıt E00B'nin cihaz/log doğrulamasıdır; kontrollü fiziksel deneyin tüm koşullarını (primer akımın gerçekten sıfır olması, CT'nin iletkene/konuma montajı, kart pinout doğrulaması ve ölçüm bağlantısı) tek başına kanıtlamaz.
- ESPHome logunda iki ayrı ADC pininin örnekleri farklı zamanlarda yayınlanıyor; bunlar eşzamanlı örnek çifti değildir.
- ESPHome'un chip revision ve SRAM1-as-IRAM uyarıları bilgilendiricidir; bu logda ADC başlatma hatası görülmedi.

### SONRAKİ ADIM
Fiziksel koşulu (SCT'nin hangi iletken üzerinde ve primer akımın nasıl sıfırlandığını) deney notuna açıkça kaydet; aynı düzenekte daha uzun kararlı kayıt al. Sonraki değerlendirmede ilk açılış geçişini ayrı tut ve RAW sıfırlarını eşleştirme. E00A ile nicel kıyas için aynı bağlantı, aynı besleme ve aynı kayıt yöntemiyle tekrarlı A/B kayıtları gerekir.


---

## 2026-10-30 — Uzun E00B logu ve yüksüz karşılaştırma

### HEDEF
İlk cihaz logundaki kısa kararlı pencereyi daha uzun kayıtla tekrar değerlendirmek; SCT bağlı analog düğümün yüksüz durumda bias referansıyla aynı seviyeyi koruyup korumadığını görmek.

### LOG
- Ham kaynak: [2026-10-30-e00b-esp32d2-long-observation.log](logs/2026-10-30-e00b-esp32d2-long-observation.log) (222,578 bayt).
- Açılış geçişi ve başlangıç RAW=0 / 0.142 V okumaları dışarıda bırakıldı; her kanal için 351 geçerli yayın değeri kullanıldı.
- Bias GPIO34 RAW: ortalama **1852.56 count**, std **8.97**, medyan 1854, min 1834, max 1874.
- SCT GPIO32 RAW: ortalama **1853.37 count**, std **9.33**, medyan 1856, min 1831, max 1941.
- RAW ortalama farkı (SCT − Bias): **+0.82 count**; medyan fark **+2 count**.
- Bias GPIO35 ADC voltajı: ortalama **1.6646 V**, std **0.0068 V**, medyan 1.666 V, min 1.635 V, max 1.680 V.
- SCT GPIO33 ADC voltajı: ortalama **1.6632 V**, std **0.0070 V**, medyan 1.666 V, min 1.649 V, max 1.705 V.
- ADC voltaj ortalama farkı (SCT − Bias): **−0.00136 V (−1.4 mV)**; medyanlar eşit: 1.666 V.
- Dört kanalın her birinde n=351. Ayrı ADC girişlerinin yayınları eşzamanlı değildir; farklar yaklaşık yayın sırası üzerinden betimleyicidir.
- Firmware sensör yayın aralığı 1 saniyedir; bu yüksek hızlı ham ADC örneklemesi değildir.

### SONUÇ
- **Deney sonucu olumlu:** uzun logun geçerli penceresinde SCT bağlı hat, yüksüz durumda bias referansıyla pratik olarak aynı seviyeyi göstermiştir.
- RAW ortalama farkı 1 count'un altındadır; ADC voltaj ortalama farkı yaklaşık 1.4 mV'dur. Bu kayıtta SCT bağlantısının bias seviyesini anlamlı ölçüde kaydırdığına dair bulgu yoktur.
- SCT RAW maksimumunda 1941 count görülmüştür; üst uçtaki bu değerin nedeni doğrulanmamıştır ve sonraki yük kayıtlarında izlenecektir.
- Sonuç yalnız yüksüz koşula aittir. Fiziksel primer akımın sıfır olması ve CT montajı log satırlarından bağımsız doğrulanmış değildir.

### SONRAKİ ADIM
Aynı dört kanalı izleyen E00B firmware'i değiştirmeden koru. Sonraki yük koşulunu ayrı deney/log olarak kaydet; yük tipi ve gücü kesinleştirildikten sonra koşul başlığı aç.
