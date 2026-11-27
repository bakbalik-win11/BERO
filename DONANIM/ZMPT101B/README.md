# ZMPT101B — AC gerilim algılama

## Amaç ve kayıt kapsamı

Bu sayfa ölçüm elemanını, BERO'da bulunan hazır kartı ve sensöre ait doğrulanmış/henüz doğrulanmamış bilgileri tutar. Tamamlanmış PF tasarımı veya imalat onayı değildir.

## Ölçüm elemanı

- **Model:** ZMPT101B, akım çıkışlı minyatür gerilim ölçüm transformatörü.
- **Üretici:** Qingxian Zeming Langxi Electronic Devices Co., Ltd. (ZEMING).
- **Sarım oranı:** 1000:1000 (1:1).
- **Üretici koşullu değerleri:** 2 mA nominal primer/sekonder akımı; 100 Ω örnekleme direnci ve 2 mA girişte faz hatası ≤20 yay-dakika; belirtilen aralıkta doğrusallık ≤0,2%; yalıtım gerilimi 4000 V.
- [Üretici ürün sayfası](https://www.micro-transformer.com/2ma-2ma-voltage-transformer-ZMPT101B.html) · [Üretici PDF veri sayfası](https://5nrorwxhmqqijik.leadongcdn.com/attachment/kjilKBmoioSRqlkqjoipSR7ww7fgzb73m/ZMPT101B-specification.pdf)

Bu değerler çıplak transformatör elemanına aittir; hazır kartın performansını veya kurulu devrenin güvenliğini tek başına doğrulamaz.

## BERO'daki hazır kart

Kullanıcının bildirdiği donanım, çıplak transformatör değil, potansiyometreli ZMPT101B AC Voltage Sensor Module kartıdır. Tipik kartlarda op-amp katı, trimpot, şebeke tarafında L/N ve düşük gerilim tarafında VCC/OUT/GND bulunabilir. Elimizdeki kartın üreticisi, revizyonu, op-amp modeli, pin sırası, besleme aralığı ve çıkış salınımı fiziksel incelemeyle doğrulanacaktır.

**Ön test hedefi:** Kartın trimpotuyla çıkış genliğini fiziksel olarak ayarlayıp ZMPT gerilim okumasını PZEM gerilim okumasına yaklaştırmak. Trimpot konumu ve her iki ölçüm aynı kararlı zaman aralığı için kaydedilir. Bu ayar faz düzeltmesi veya PF'ye bağlı akım düzeltmesi yerine geçmez; bunlar ayrı deney parametreleridir.

## BERO deney durumu

- BERO'ya ait önceki PF gözlemleri ve kanıt sınırları: [PF araştırma durumu ve saha verileri](PF-ARASTIRMA-GUNCEL-DURUM-2026-11-22.md).
- Genel PF metodolojisi, yapay zekâ sentezi ve dış kaynak notları: [isteğe bağlı PF araştırma başvurusu](REFERANS/PF-ARASTIRMA/README.md).
- MOD2-GRV002 kapsamında şebeke gerilimi okuma, SCT013 ile faz/PF denemesi ve sonraki akım düzeltme planı yürütülür.
- BERO'nun ZMPT tabanlı PF ölçümü henüz fiziksel olarak uygulanmış veya doğrulanmış değildir.

## Güvenlik ve açık noktalar

Şebeke primerinde ölümcül gerilim bulunabilir. 220–230 V ölçümüne geçmeden önce hazır kartın tam revizyonu, giriş devresi, yalıtım/mesafeler, terminal koruması ve kapalı-korumalı test düzeneği değerlendirilmelidir. Açık breadboard üzerinde şebeke deneyi yapılmaz. Osiloskop ground klipsi şebeke fazına veya nötrüne bağlanmaz. Bileşenin veri sayfasındaki yalıtım değeri tamamlanmış kart ve düzeneğin güvenli olduğunu kanıtlamaz.

## Kayıt durumu

- Üretici veri sayfası bulundu; hazır kartın detayları fiziksel doğrulama bekliyor.
- Trimpotla gerilim genliği ayarı, PZEM karşılaştırmalı ön test hedefidir; henüz yapılmış ölçüm değildir.
- ADC seçimi, örnekleme zamanlaması, faz düzeltmesi ve PF doğruluğu doğrulanmadı.
