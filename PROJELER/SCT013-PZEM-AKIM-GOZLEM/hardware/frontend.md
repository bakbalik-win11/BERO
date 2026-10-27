# SCT analog ön uç kontrolü

**Durum: Ölçüm yapılmadı; fiziksel arayüz kartı kullanıcı beyanıyla mevcut.** Kullanıcı daha önce 8 kanallı, her kanalı ayrı bias ve direnç ağı bulunan bir kart hazırladığını bildirdi. SCT013 sensörleri jack yuvaları üzerinden bağlanıyor; sinyal bias uygulanmış olarak ESP32 ADC girişinden okunuyor. İstenirse MCP serisi harici ADC bağlanabilir, ancak bu projede belirli MCP modeli seçilmiş değildir.

Bu bilgi kartın hazırlandığını belirtir; şema, kanal değerleri veya elektriksel davranışın doğrulandığını göstermez.

BERO'nun SCT013-100A-1V notlarında nominal 100 A için 1 V RMS çıkış ve tarihsel bir kurulumda yaklaşık 1,67 V bias / 3,12 V VREF yer alır. Bunlar bu deney düzeneğinin doğrulanmış parametreleri sayılmaz.

Kaydedilecekler:
- Kullanılacak SCT model kodu ve dönüşüm oranı.
- Dahili burden var/yok; ek burden varsa değeri ve gücü.
- Hazır 8 kanallı kartın şeması veya net bağlantı listesi; kanal başına direnç ve filtre değerleri.
- Bias şeması, bias noktasına SCT AC sinyalinin kuplaj yöntemi ve ADC pininde ölçülen DC seviyesi.
- Gerçekte kullanılacak ADC modeli/revizyonu, çözünürlük, VREF kaynağı/değeri ve örnekleme davranışı.
- Analog filtre ve kaynak empedansı.
- Yüksüz ADC ortalaması, min/max ve gürültü RMS'i.
- En yüksek planlanan akımda clipping durumu.

SCT013-100 (100 A / 1 V) gerilim çıkışlı varyant ile SCT013-000 akım çıkışlı varyant aynı değildir. Analog ön uç gerçek sensöre göre kurulmalı ve ölçülerek doğrulanmalı.
