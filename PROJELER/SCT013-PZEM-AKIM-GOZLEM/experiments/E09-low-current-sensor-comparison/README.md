# E09 — ESP-2 düşük akım sensör karşılaştırması

## Amaç

Bir adet ACS712-5A ve bir adet ZMCT103C-5A modülünün, PZEM-004T V3.0 ile aynı ESP-2 düğümünde aşamalı olarak çalıştırılabilirliğini ve düşük akım koşullarındaki davranışlarını incelemek.

Bu deney, ESP-1'deki SCT013 ana ölçüm kolundan bağımsızdır. ESP-1'e bu deney kapsamında başka sensör veya PZEM görevi eklenmez.

## Mimari

| Düğüm | Donanım | Sınır |
|---|---|---|
| ESP-1 | SCT013-030 ana sensör | Yalnız SCT edinimi; hızlı örnekleme önceliği |
| ESP-2 | PZEM-004T V3.0 + ACS712-5A + ZMCT103C-5A | Sensörler aşamalı biçimde devreye alınır |
| Ayrı kontrol düğümü | Mevcut SSR/zamanlama donanımı | Bu deney planı bu düğümün firmware'ini değiştirmez |

Fiziksel ESP kart modelleri, GPIO'lar, analog ön uç ve haberleşme pinleri henüz bu planla atanmış değildir.

## Aşamalı test kapıları

| Sıra | Kurulum | Doğrulama | Sonraki aşama kapısı |
|---:|---|---|---|
| 1 | Yalnız PZEM | Haberleşme, geçerli alanlar, okuma sürekliliği ve hata durumları | PZEM verisi güvenilir biçimde okunuyor |
| 2 | Yalnız ACS712-5A | Besleme, yüksüz çıkış tabanı, güvenli ADC ölçekleme, kontrollü yük tepkisi | Çıkış ADC sınırları içinde ve tekrar edilebilir |
| 3 | Yalnız ZMCT103C-5A | Kart topolojisi/burden doğrulaması, yüksüz taban, kontrollü yük tepkisi | Analog çıkış güvenli ve okunabilir |
| 4 | PZEM + ACS712-5A | Birlikte çalışma, veri güncelleme ve zamanlama etkisi | Her iki veri akışı kesintisiz |
| 5 | PZEM + ZMCT103C-5A | Birlikte çalışma, veri güncelleme ve zamanlama etkisi | Her iki veri akışı kesintisiz |
| 6 | PZEM + ACS712-5A + ZMCT103C-5A | Kaynak, ADC, zamanlama ve veri akışı etkileşimi | Önceki kapıların tümü başarılı |

Her aşama ayrı firmware/configuration sürümü ve ayrı log ile kaydedilir. Önceki aşamanın başarılı olduğu doğrulanmadan yeni sensör eklenmez.

## Ölçüm yaklaşımı

- İlk amaç yüksüz taban ile yük altındaki sinyalin ayrışıp ayrışmadığını görmektir; ilk aşamada kesin akım doğruluğu iddiası yapılmaz.
- 50 mA, başlangıç araştırma hedefidir; doğrulanmış kabul eşiği değildir. Daha düşük seviyeler ancak ilk sonuçlar gerekçe oluşturursa incelenir.
- PZEM bu projede karşılaştırma/etiket referansıdır; bağımsız ve kusursuz ground-truth olarak tanımlanmaz.
- Yük koşulları, gerçek yük etiketi ve PZEM okumaları her test kaydında ayrı belirtilir.
- Ham verinin sürekli depolanması varsayılan değildir. İhtiyaç duyulan kısa teşhis kayıtları ve pencere özetleri saklanır.
- Sensörler farklı fiziksel prensiplere ve ölçeklere sahip olduğundan ham ADC sayıları doğrudan birbirleriyle karşılaştırılmaz; her kanalın kendi yüksüz tabanı ve dönüşüm zinciri belgelenir.

## Güvenlik ve bağlantı ön koşulları

- ACS712-5A modülünün 5 V beslemesi ve çıkış salınımı ölçülmeden ESP32 ADC pinine doğrudan bağlanmaz. Uygun ölçekleme/koruma tasarımı doğrulanır.
- ZMCT103C kartının gerçek burden direnci, çıkış tipi ve kart üzerindeki ek bileşenler incelenmeden bağlantı şeması kesinleştirilmez.
- Şebeke iletkeni üzerinden akım taşıyan modüller kapalı ve uygun yalıtımlı düzenekte kullanılmalıdır; açık breadboard şebeke akımı için kullanılmaz.
- GPIO, ADC attenuasyonu, örnekleme hızı, filtre ve ölçek katsayıları test öncesinde varsayılmaz; kullanılan gerçek konfigürasyon log/meta kaydına eklenir.

## Sonuç durumu

**PLANLANDI — henüz fiziksel test yapılmadı.** Bu dosyada ölçüm sonucu, derleme başarısı veya bağlantı doğrulaması iddiası yoktur.
