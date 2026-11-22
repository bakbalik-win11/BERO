# ZMPT101B – Bileşen Veri Sayfası

Aranan parça, potansiyometreli ZMPT101B Arduino modülü değil; dört bacaklı çıplak ZMPT101B gerilim ölçüm transformatörüdür.

Üretici: Qingxian Zeming Langxi Electronic Devices Co., Ltd. (ZEMING)

- [ZMPT101B – üretici sunucusundaki orijinal PDF datasheet](https://5nrorwxhmqqijik.leadongcdn.com/attachment/kjilKBmoioSRqlkqjoipSR7ww7fgzb73m/ZMPT101B-specification.pdf)
- [Üreticinin ZMPT101B ürün sayfası](https://www.micro-transformer.com/2ma-2ma-voltage-transformer-ZMPT101B.html)

Bu PDF bileşenin mekanik ölçülerini, dört pin bağlantısını/polaritesini ve elektriksel karakteristiklerini içerir. Kart/modül şeması değildir.


## Ek kullanım kılavuzu
Kullanıcı tarafından sağlanan `ZMPT101B.PDF` dosyası, **ZMPT101B (ZMPT107) voltage transformer operating guide** başlıklı 4 sayfalık belgedir. Çıplak transformatör/ön uç bağlantı yaklaşımlarını, ADC çıkış sınırlarını ve direnç seçim yöntemlerini açıklar. Bu belge hazır potansiyometreli PCB modülünün tam şeması değildir.

- İnceleme ve BERO deney notları: [ZMPT101B-ZMPT107-KULLANIM-KILAVUZU-INCELEME.md](ZMPT101B-ZMPT107-KULLANIM-KILAVUZU-INCELEME.md)
- Orijinal kullanıcı PDF'si bu commit işleminde ikili dosya olarak depoya yüklenmemiştir; teknik içeriği ve kaynak kapsamı inceleme kaydına aktarılmıştır.


## Hazır modül kartı teknik makalesi
- [DataCaptureControl – ZMPT101B AC Voltage Transformer Sensor Module](https://datacapturecontrol.com/articles/io-components/sensors/voltage/zmpt101b-ac-voltage-transformer-sensor-module)
- Makale, LM358'li hazır modülün pinlerini, kart devresini ve RMS kalibrasyon yöntemini açıklar.
- Teknik değerlendirme: [ZMPT101B-ZMPT107-KULLANIM-KILAVUZU-INCELEME.md](ZMPT101B-ZMPT107-KULLANIM-KILAVUZU-INCELEME.md)


## Arduino Forum – ZMPT101B + ADS1115 deney tartışması
- [Kaynak başlık](https://forum.arduino.cc/t/using-zmpt101b-with-ads1115/1434976)
- Kütüphane arayüzü, ham ADS1115 örnekleme, örnekleme hızı ve faz kayması tartışmasının BERO açısından özeti: [ARDUINO-FORUM-ZMPT101B-ADS1115-DENEY-NOTU.md](ARDUINO-FORUM-ZMPT101B-ADS1115-DENEY-NOTU.md)
- Forum mesajlarındaki test sonuçları ve teknik yorumlar kullanıcıya/kuruluma özgüdür; BERO donanımında doğrulanmış sonuç olarak kabul edilmez.
