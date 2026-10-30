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
