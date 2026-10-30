# E00B — SCT bağlı, akımsız hat ADC gözlemi

## Neden yapıyoruz?
E00A bias-only alt deneyinde SCT bağlı değilken ölçüm zincirinin taban dalgalanması kaydedildi. E00B'de öncelikli SCT013-030 (30 A / 1 V), mevcut jack/bias ağına bağlanacak; SCT'nin izlediği iletkende akım yokken ADC girişlerinin davranışı gözlenecek. Amaç, SCT bağlandığında bias seviyesinin ve dalgalanmanın nasıl değiştiğini E00A tabanıyla karşılaştırmaktır.

Bu adım akım ölçümü, kalibrasyon veya yük altında performans testi değildir.

## GPIO planı

| İşlev | GPIO | ADC kanalı | Kullanım |
|---|---:|---|---|
| Bias RAW | GPIO34 | ADC1_CH6 | Mevcut E00A kanalı; bias Vmid gözlemi |
| Bias voltaj | GPIO35 | ADC1_CH7 | Mevcut E00A kanalı; bias Vmid voltajı |
| SCT RAW | GPIO32 | ADC1_CH4 | SCT analog düğümünün ham ADC sayımı |
| SCT voltaj | GPIO33 | ADC1_CH5 | Aynı SCT analog düğümünün ADC voltaj tahmini |

GPIO32/GPIO33 ataması ESP32-WROOM-32D için önerilen ADC1 pin planıdır. Gerçek geliştirme kartı üzerindeki pin etiketleri ve pinout fiziksel olarak doğrulanmadan kablo bağlanmayacaktır. GPIO34/35 ve GPIO32/33 aynı kartta kullanılacaktır; kart farklıysa pin planı yeniden kontrol edilir.

## Bağlantı yaklaşımı
- Bias ölçümü GPIO34/35'te E00A'daki mevcut bağlantı düzeniyle korunur.
- SCT013-030 dişi jack üzerinden mevcut breadboard bias ağına bağlanır.
- SCT sinyalinin bias uygulanmış analog düğümü GPIO32 ve GPIO33'e paralel gözlem için götürülür.
- ESP32 GND ile bias devresi GND ortak olmalıdır.
- Bu iki ADC pini aynı analog düğümü ayrı ADC kanallarıyla gözler; eşzamanlı tek ADC örneği oldukları varsayılmaz.
- SCT sekonderini üretici talimatı izin vermedikçe primerde akım varken açık devre bırakma. Bağlantıları enerji kesikken yap. Şebeke iletkeni üzerinde çalışma yalnız yetkin kişi tarafından, uygun izolasyon ve muhafaza ile yapılır.

## Deney koşulu
SCT bağlı olacak; SCT'nin izlediği iletkenden akım geçmeyecek. Yük kapalı/enerjisiz tutulur. İlk gözlemde yük çalıştırılmaz.

## Kaydedilecekler
- GPIO34 RAW ve GPIO35 voltajı (bias referansı)
- GPIO32 RAW ve GPIO33 voltajı (SCT düğümü)
- Her kanalın zaman damgaları, geçersiz/başlangıç RAW sıfırları ve log süresi
- Ortalama, min, max, peak-to-peak ve standart sapma
- E00A SCT'siz bias-only tabanıyla fark

## HEDEF / LOG / SONUÇ

### HEDEF
SCT bağlıyken akımsız koşulda ADC ölçüm zincirinin bias ve dalgalanma davranışını gözlemek; E00A SCT'siz tabanına göre değişimi belirlemek.

### LOG
- Planlanan kart: ESP32-WROOM-32D; gerçek kart/pinout doğrulaması bekliyor.
- Planlanan GPIO: bias 34/35; SCT 32/33.
- Öncelikli sensör: SCT013-030 (30 A / 1 V).
- Firmware, fiziksel bağlantı, derleme, cihaz logu ve ölçüm henüz yapılmadı.

### SONUÇ
Henüz ölçülmedi. Deney yalnız planlandı. GPIO32/33 fiziksel pinout doğrulaması ve firmware hazırlığı sonraki uygulama adımlarıdır.

Durum: PLANLANDI.
