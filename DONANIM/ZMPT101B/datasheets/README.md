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


## Arduino Forum – ZMPT101B analog çıkış ve osiloskop
- [Kaynak başlık](https://forum.arduino.cc/t/problem-with-translate-the-values-of-voltage-sensor-zmpt101b/491534)
- Kodda maksimum/minimum takibi, `delay()` parametresi, seri portun örnekleme zamanlamasına etkisi, DC coupling ile ofseti görme ve potansiyometre kaynaklı kırpılma konularının BERO değerlendirmesi: [ARDUINO-FORUM-ZMPT101B-ANALOG-CIKIS-OLCUM-DENEY-NOTU.md](ARDUINO-FORUM-ZMPT101B-ANALOG-CIKIS-OLCUM-DENEY-NOTU.md)
- Forumdaki kart şeması ve ölçüm gözlemleri satın alınan BERO kartının doğrulanmış özellikleri değildir.


## Arduino Forum – ZMPT101B düşük AC gerilim ölçümü
- [Kaynak başlık](https://forum.arduino.cc/t/zmpt101b-problem-with-measure-ac-voltage/1219148)
- Düşük girişte 4,8 V civarında takılma, hassasiyet katsayısı, kütüphane kalibrasyonu ve Arduino ADC kalibrasyonu ayrımı: [ARDUINO-FORUM-ZMPT101B-DUSUK-GERILIM-OLCUM-DENEY-NOTU.md](ARDUINO-FORUM-ZMPT101B-DUSUK-GERILIM-OLCUM-DENEY-NOTU.md)
- Forum sonucu BERO kartının alt ölçüm sınırı değildir; düşük gerilim davranışı deneyle belirlenecektir.


## Home Assistant Community – ZMPT101B, ESP32 ADC ve ADS1115 bağlamı
- [Kaynak mesaj #12](https://community.home-assistant.io/t/measure-mains-voltage-with-zmpt101b-and-ads1115/360162/12)
- ESP32 GPIO33/ADC1 denemesi, ADC2/Wi-Fi gerekçesi, AC'de kararsız ham okumalar, DC testinin sınırlılığı, RMS filtresi ve kalibrasyon katsayısının BERO açısından değerlendirmesi: [HOME-ASSISTANT-COMMUNITY-ZMPT101B-ESP32-ADC-DENEY-NOTU.md](HOME-ASSISTANT-COMMUNITY-ZMPT101B-ESP32-ADC-DENEY-NOTU.md)
- Bu mesajdaki deney ADS1115 ile yapılmamıştır; kullanıcı ESP32 dahili ADC'sini denemektedir.
