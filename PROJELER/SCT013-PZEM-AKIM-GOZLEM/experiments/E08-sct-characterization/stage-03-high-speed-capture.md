# Aşama 3 — Yüksek hızlı ham ADC edinimi hazırlığı

**Durum: PLANLANDI — firmware henüz yazılmadı.**

## HEDEF

Kullanıcının onayladığı zaman grafiğinde 50 Hz yük sinyalinin daha sık örneklerle oluşturduğu salınımları görmek. 1 saniyelik ESPHome yayınlarının yerine kısa, zaman damgalı ham ADC pencereleri edinmek.

Bu aşamanın ilk hedefi dalga şeklini gözlemlemektir. Akım hesabı, PF, FFT/THD veya güç kalitesi analizi bu aşamanın kapsamı değildir.

## Görsel çıktı standardı

- X ekseni: örneklerin gerçek zaman damgası.
- Y ekseni: ADC RAW count.
- Mavi: GPIO34 Bias RAW.
- Kırmızı: GPIO32 SCT RAW.
- Yeşil kesikli dikey çizgi: açıkça kaydedilmiş yük açılma olayı; olay zamanı yoksa tahminî olduğu yazılır.
- Ham örnekler arasında interpolasyonla yeni veri üretilmez.
- Başlık/alt yazıda hedef ve gerçekleşen kanal başı örnekleme hızı, pencere süresi ve örnek sayısı gösterilir.

## Donanım ve değişmez bağlantılar

- Cihaz kimliği: mevcut ESP32D2; ESPHome name/hostname kimliği kullanıcı onayı olmadan değiştirilemez.
- Kart/variant/framework ve başlangıçta verilen donanım tanımları korunur.
- Bias referansı: mevcut GPIO34 / ADC1_CH6.
- SCT sinyal düğümü: mevcut GPIO32 / ADC1_CH4.
- İlk yüksek hızlı görünüm için bu iki RAW kanal örneklenir. GPIO35 ve GPIO33'ün mevcut yavaş voltaj kanalları, aynı analog düğümlerin ikinci ölçüm yollarıdır; ilk yüksek hızlı edinim için zorunlu değildir. Bunların fiziksel bağlantısı değiştirilmez.
- Yeni ADC, MCP3208 veya başka donanım eklenmesi bu aşamada planlanmıyor.

## Edinim yaklaşımı

ESP-IDF ADC Continuous (DMA) sürücüsü araştırma adayıdır. Sürücü, ADC dönüşümlerini sürekli alıp DMA çerçeveleri halinde belleğe aktarır. Resmî belge:
https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/adc_continuous.html

İlk prototip hedefi:
- Kanal: GPIO34 ve GPIO32 (ADC1).
- Hedef: kanal başına 1.000 örnek/s.
- İki kanal tarandığında başlangıç yapılandırma hedefi yaklaşık 2.000 ADC dönüşümü/s olacaktır. Gerçek kanal başına hız varsayılmayacak; zaman damgası ve örnek sayısından hesaplanıp doğrulanacaktır.
- Pencere: başlangıçta 200 ms; kanal başına yaklaşık 200 örnek hedeflenir. Bu pencere nihai/optimum kabul edilmez.
- Ham veri: kısa pencere/buffer olarak alınır ve PC'ye aktarılır. Sürekli ham ADC arşivi tutulmaz.
- İlk aktarım yolu ve tampon boyutu, firmware tasarımında ayrıca seçilip derleme öncesi açıklanır.

## Kritik sürücü kısıtları

- ESP-IDF belgesine göre aynı ADC birimi aynı anda continuous ve one-shot modlarında çalıştırılamaz. Bu nedenle GPIO34/32'yi kullanan mevcut ESPHome ADC sensörleri, continuous sürücüyle aynı firmware içinde eşzamanlı çalışır durumda bırakılmayacaktır.
- Mevcut ESPHome ADC sensörleri ve yeni continuous sürücü arasında kaynak/ADC sahipliği çakışması tasarım aşamasında giderilmelidir.
- Eski E00F ct_clamp / ADC One-shot ve yeni ADC Continuous edinimi aynı ADC1 biriminde eşzamanlı karşılaştırılamaz. Modlar arası karşılaştırma gerekiyorsa aynı yük, CT tur sayısı, bias/bağlantı ve kararlı koşul korunarak sıralı iki ayrı kayıt alınır; her kayıt öncesi yük koşulu yeniden teyit edilir.
- Continuous sürücü DMA/I2S0 kaynaklarını kullanır; I2S0 kullanan başka bir bileşen varsa kaynak çakışması kontrol edilmelidir.
- Örnek başına Home Assistant API yayını yapılmayacaktır. Kısa örnek pencereleri tamponlanıp toplu aktarılacaktır.
- Hedef örnekleme hızı ile ölçülen gerçekleşen hız ayrı kaydedilecektir. Buffer taşması/kayıp örnek sayısı varsa raporlanacaktır.

## Deney sırası

1. Firmware tasarımını ve PC'ye aktarım biçimini belirle; ESP32D2 kimliği, board/variant/framework ve GPIO34/32 eşleşmesini kaynak YAML ile diff üzerinden doğrula.
2. Yalnız 1 kS/s/kanal hedefli ilk firmware'i hazırla; derleme doğrulaması yap. Derleme, fiziksel çalışmayı kanıtlamaz.
3. Kısa test penceresinde örnek sayısı ve süreyle gerçekleşen hızı ölç; kayıp/taşma kontrolü yap.
4. 100 W akkor yükte yüksüz başlangıç ve yük açık pencerelerini kaydet; gerçek açılma zamanını ayrıca olay kaydına yaz.
5. İstenen grafik standardında ham örnekleri çiz.
6. İlk hız kararlı ve doğrulanmışsa aynı mimariyle 2 kS/s/kanal, ardından 2.5 kS/s/kanal hedeflerini ayrı koşullarda dene.

## Kabul ölçütleri

- Cihaz kimliği ve mevcut pin eşlemeleri değişmemiş olmalı.
- İki kanalın gerçek örnekleme hızları ayrı ayrı ölçülmüş olmalı.
- İstenen/gerçekleşen hız, örnek sayısı, pencere süresi ve olası kayıp örnekler kaydedilmiş olmalı.
- 200 ms pencerede iki kanalın zaman grafiği ham örneklerden üretilebilmeli.
- Derleme, cihaza yükleme ve fiziksel test durumları birbirinden ayrı raporlanmalı.

## LOG / SONUÇ

- **LOG:** 2026-10-30 tarihinde kullanıcı daha hızlı salınım görünümü istedi. ESP-IDF ADC Continuous/DMA resmî dokümantasyonu incelendi. Mevcut E00B YAML değiştirilmedi.
- **SONUÇ:** Yüksek hızlı edinim PLANLANDI. Kod, derleme, flash ve fiziksel ölçüm henüz yapılmadı.
