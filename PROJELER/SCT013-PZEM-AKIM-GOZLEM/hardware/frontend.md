# SCT analog ön uç kontrolü

**Durum: Ölçüm yapılmadı.** BERO'nun SCT013-100A-1V notlarında nominal 100 A için 1 V RMS çıkış ve bir tarihsel kurulumda yaklaşık 1,67 V bias / 3,12 V VREF yer alır. Bunlar bu deney düzeneğinin doğrulanmış parametreleri sayılmaz.

Kaydedilecekler:
- SCT model kodu ve dönüşüm oranı.
- Dahili burden olup olmadığı; ek burden varsa değeri ve gücü.
- Bias şeması ve ADC pininde ölçülen DC seviyesi.
- ADC modeli, çözünürlük, VREF ve örnekleme davranışı.
- Analog filtre ve kaynak empedansı.
- Yüksüz ADC ortalaması, min/max ve gürültü RMS'i.
- En yüksek planlanan akımda clipping durumu.

SCT013-100 (100 A / 1 V) gerilim çıkışlı varyant ile SCT013-000 akım çıkışlı varyant aynı değildir. Analog ön uç gerçek sensöre göre kurulmalı ve ölçülerek doğrulanmalı.
