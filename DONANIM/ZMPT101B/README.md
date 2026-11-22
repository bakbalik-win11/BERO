# ZMPT101B – AC Gerilim Algılama

## Amaç
BERO kapsamında şebeke geriliminin anlık dalga şeklini güvenli bir ölçüm zinciri üzerinden örneklemek; SCT013 akım dalga şekliyle zaman hizalı veriler elde ederek aktif güç (P), görünür güç (S) ve gerçek güç faktörü (PF) araştırmasına veri sağlamak.

Bu donanım kaydı bir imalat/onay belgesi değildir. Önce sensör, analog ön uç, ADC ve zamanlama deneyleri doğrulanacaktır.

## Parça kimliği
- Model: ZMPT101B
- Üretici: Qingxian Zeming Langxi Electronic Devices Co., Ltd. (ZEMING)
- Tip: Akım çıkışlı minyatür gerilim ölçü trafosu
- Sarım oranı: 1000:1000 (1:1)
- Nominal primer akımı: 2 mA
- Nominal sekonder akımı: 2 mA
- Üretici sayfasında belirtilen faz açısı hatası: 100 Ω örnekleme direnci ve 2 mA giriş koşulunda ≤20 yay-dakika
- Doğrusallık: ≤0,2% (belirtilen çalışma aralığında)
- İzolasyon gerilimi: 4000 V (üretici veri sayfası değeri; tamamlanmış devrenin güvenlik onayı değildir)
- Çalışma sıcaklığı: -40 °C … +60 °C

## Üretici belgeleri
- [Üretici ürün sayfası](https://www.micro-transformer.com/2ma-2ma-voltage-transformer-ZMPT101B.html)
- [Üretici sunucusundaki orijinal ZMPT101B PDF veri sayfası](https://5nrorwxhmqqijik.leadongcdn.com/attachment/kjilKBmoioSRqlkqjoipSR7ww7fgzb73m/ZMPT101B-specification.pdf)

## Bağlantı ve analog ön uç – henüz tasarım kararı değil
ZMPT101B çıplak transformatör elemanıdır. Primerde akım sınırlama direnci, sekonderde uygun örnekleme direnci ve ADC girişine uygun analog koşullandırma gerekir. Yaygın potansiyometreli ZMPT101B modülü ile çıplak transformatör aynı donanım değildir; kart üzerindeki op-amp ve ayar devresi ayrıca değerlendirilmelidir.

ESP32/ADC girişine uygulanacak sinyal, ADC'nin izin verilen aralığında kalmalı ve negatif gerilim içermemelidir. Bunun için uygun AC kuplaj/bias ve gerekiyorsa koruma/filtreleme tasarlanmalıdır. Direnç değerleri, şebeke gerilimi ve kullanılacak tam devre doğrulanmadan bağlantı yapılmayacaktır.

## BERO'daki kullanım yaklaşımı
- SCT013 akım dalga şekli ile ZMPT101B gerilim dalga şekli aynı zaman tabanında örneklenmelidir.
- Her örnek için eşleşmiş v[n] ve i[n] değerleri kullanılmalıdır.
- P = mean(v[n] × i[n])
- Vrms = sqrt(mean(v[n]²))
- Irms = sqrt(mean(i[n]²))
- S = Vrms × Irms
- Gerçek PF = P / S

Sinüzoidal olmayan yüklerde yalnızca faz açısı üzerinden cos(phi) hesaplamak gerçek PF değildir. Gerçek PF, aktif gücün görünür güce oranıdır ve dalga şekli bozulmasını da kapsar.

## Önemli ölçüm kısıtı
ADS1115'in 860 SPS azami dönüşüm hızı iki kanala bölündüğünde kanal başına yaklaşık 430 örnek/saniye düzeyine iner; 50 Hz için bu yaklaşık 8,6 örnek/döngüdür. Ayrıca ADS1115 kanalları eşzamanlı örneklemez. Bu nedenle ADS1115, faz ve gerçek PF ölçümü için ilk tercih olarak kabul edilmeyecektir. Daha hızlı ve zaman hizalı iki kanal örneklemesi sağlayan ADC/örnekleme mimarisi araştırılacaktır.

## Güvenlik
Bu eleman şebeke gerilimi ölçümünde kullanılacaktır. Primer tarafında ölümcül gerilim bulunabilir. Açık breadboard üzerinde şebeke bağlantısı yapılmayacaktır. Uygun izolasyon mesafeleri, muhafaza, sigorta/akım sınırlama, terminal koruması ve ölçüm ekipmanı güvenliği tasarımın zorunlu parçalarıdır. 4000 V izolasyon değeri tek başına kurulmuş devrenin güvenli olduğunu göstermez.

## Durum
- Veri sayfası bulundu.
- Donanım klasörü açıldı.
- Elektriksel bağlantı ve ADC seçimi: araştırma aşamasında.
- PF ölçümü: henüz uygulanmadı ve doğrulanmadı.


## BERO envanter notu – satın alınan donanım
Kullanıcının doğruladığı satın alınan parça, çıplak transformatör değil; ZMPT101B AC Voltage Sensor Module (potansiyometreli PCB modülü) kartıdır.

Kart tipik olarak şu bölümleri içerir:
- ZMPT101B ölçüm transformatörü
- LM358 veya kart revizyonuna göre farklı olabilen op-amp sinyal koşullandırma katı
- Çıkış genliğini ayarlayan trimpot
- Şebeke tarafı L/N klemensi
- Düşük gerilim tarafı VCC, OUT ve GND bağlantıları

Tipik kartlarda 5V besleme, VCC/2 civarında DC ofsetli analog OUT sinyali ve ayarlanabilir AC genliği bulunur. Ancak üretici/PCB revizyonları farklı olabildiğinden pin sırası, op-amp modeli, besleme aralığı ve çıkış salınımı satın alınan kartın üzerindeki baskı ve ölçümle doğrulanmadan kesin kabul edilmeyecektir.

Çıplak ZMPT101B transformatör datasheet'i yalnızca kart üzerindeki transformatör elemanını tanımlar; komple PCB modülünün şeması veya performans garantisi değildir.

## PF araştırması için özel not
Kartın op-amp ve filtreleme katı, gerilim dalgasına frekansa bağlı genlik/faz etkisi ve distorsiyon ekleyebilir. Bu nedenle SCT013 akım dalgasıyla PF hesabına geçmeden önce:
1. Kart çıkışının DC ofseti ve kırpılma payı ölçülecek.
2. Gerilim dalgası bilinen, güvenli ve izole bir AC kaynakla gözlenecek.
3. Modülün 50 Hz faz gecikmesi ölçülerek yazılımda düzeltme gerekip gerekmediği değerlendirilecek.
4. Akım ve gerilim kanallarının örnekleme zaman farkı ayrıca ölçülecek.

Modülün analog çıkışı tek başına PF vermez. Gerçek PF için aynı zaman tabanında örneklenmiş gerilim ve akım dalgaları gerekir.


## Ek belge – ZMPT101B/ZMPT107 kullanım kılavuzu
Kullanıcının sağladığı 4 sayfalık `ZMPT101B.PDF` işletim kılavuzu incelendi. Aktif/pasif çıkış şemaları, ADC maksimum RMS sınırları, primer akım sınırlama direnci ve sekonder örnekleme direnci seçim açıklamaları ile PF araştırmasına etkileri şu kayda işlendi:
- [ZMPT101B/ZMPT107 Kullanım Kılavuzu İnceleme Kaydı](datasheets/ZMPT101B-ZMPT107-KULLANIM-KILAVUZU-INCELEME.md)

Kılavuzun aktif çıkış için küçük faz hatası, pasif çıkış için yük direnci arttıkça faz farkı artışı yönündeki nitel açıklamaları hazır PCB modülünün doğrulanmış performansı sayılmaz. Kartın gerçek faz gecikmesi ve çıkış genliği fiziksel ölçümle belirlenecektir. Orijinal PDF ikili dosyası henüz GitHub'a eklenmemiştir.


## Hazır modül kartı için ek teknik kaynak
- [DataCaptureControl – ZMPT101B AC Voltage Transformer Sensor Module](https://datacapturecontrol.com/articles/io-components/sensors/voltage/zmpt101b-ac-voltage-transformer-sensor-module)

Bu kaynak LM358'li hazır kartın blok yapısını, L/N ve VCC/OUT/GND pinlerini ve ADC üzerinden RMS kalibrasyon yaklaşımını açıklar. Kaynak incelemesi, [kullanım kılavuzu inceleme kaydına](datasheets/ZMPT101B-ZMPT107-KULLANIM-KILAVUZU-INCELEME.md) eklendi. Hazır kartın faz gecikmesi ve PF doğruluğu ölçülmüş kabul edilmemektedir.


## Ek teknik kaynak – Arduino Forum / ADS1115
- [Arduino Forum – Using ZMPT101B with ADS1115](https://forum.arduino.cc/t/using-zmpt101b-with-ads1115/1434976)
- Konu, eski ZMPT101B kütüphanesinin `analogRead()`/GPIO pin arayüzünün ADS1115 ile doğrudan uyumlu olmadığını; ham ADS1115 örnekleriyle ayrı RMS hesabı yapılabileceğini tartışır.
- ADS1115 örnekleme hızı, çoklu kanal taraması, kanal zaman farkı ve ZMPT101B faz kayması hakkındaki kullanıcı gözlemleri üretici garantisi veya BERO ölçümü değildir.
- BERO için kaynak incelemesi ve deney planı: [Arduino Forum ZMPT101B + ADS1115 Deney Notu](datasheets/ARDUINO-FORUM-ZMPT101B-ADS1115-DENEY-NOTU.md)


## Ek teknik kaynak – Arduino Forum / analog çıkış ve osiloskop
- [Arduino Forum – Problem with translate the values of voltage sensor ZMPT101B](https://forum.arduino.cc/t/problem-with-translate-the-values-of-voltage-sensor-zmpt101b/491534)
- Kaynaktaki kod hataları, DC ofsetin osiloskopta görülmesi, potansiyometreyle genlik ayarı, kırpılma ve örnekleme zamanlaması değerlendirmesi: [Arduino Forum ZMPT101B Analog Çıkış Ölçüm Deney Notu](datasheets/ARDUINO-FORUM-ZMPT101B-ANALOG-CIKIS-OLCUM-DENEY-NOTU.md)
- Forumdaki ölçümler ve devre yorumları BERO kartında doğrulanmış sonuç değildir. İlk test güvenli, galvanik olarak izole düşük gerilimli AC kaynakla yapılacaktır.


## Ek teknik kaynak – Arduino Forum / düşük AC gerilim ölçümü
- [Arduino Forum – ZMPT101B problem with measure AC voltage](https://forum.arduino.cc/t/zmpt101b-problem-with-measure-ac-voltage/1219148)
- 4,8 V civarında takılma bildiren kullanıcı deneyimi, kalibrasyon ve ADC ayrımı, düşük gerilim test planı: [Arduino Forum ZMPT101B Düşük Gerilim Ölçüm Deney Notu](datasheets/ARDUINO-FORUM-ZMPT101B-DUSUK-GERILIM-OLCUM-DENEY-NOTU.md)
- 4,8 V değeri BERO için ölçülmüş alt sınır değildir; yalnızca forum kullanıcısının sistemine ait gözlemdir.


## Ek teknik kaynak – Home Assistant Community / ESP32 ADC
- [Home Assistant Community – Measure mains voltage with ZMPT101B and ADS1115, mesaj #12](https://community.home-assistant.io/t/measure-mains-voltage-with-zmpt101b-and-ads1115/360162/12)
- Mesaj #12'deki ESP32 dahili ADC denemesi, ADC1/ADC2 pin seçimi, kararsız AC okumaları, DC testinin sınırı, RMS/ofset ve kalibrasyon değerlendirmesi: [Home Assistant Community ZMPT101B ESP32 ADC Deney Notu](datasheets/HOME-ASSISTANT-COMMUNITY-ZMPT101B-ESP32-ADC-DENEY-NOTU.md)
- Mesaj başlığı ADS1115 olsa da #12'deki bu kullanıcı denemesi ESP32 dahili ADC'siyle yapılmıştır; ADS1115 performans kanıtı değildir.


## Sayısal PF hesaplama ve istatistik metodolojisi
PF araştırmasının amacı dalgayı yalnızca çizmek değil, SCT013 akım ve ZMPT101B gerilim örneklerinden sayısal olarak P, Vrms, Irms, S ve gerçek PF hesaplamak; pencere bazında istatistiksel dağılımı incelemektir.
- [PF Sayısal Hesaplama ve İstatistik Metodolojisi](PF-SAYISAL-HESAPLAMA-VE-ISTATISTIK-METODOLOJISI.md)
- Bu metodoloji deney planıdır; ADS1115'in yeterliliği, kanal zaman hizası, sensör faz gecikmesi ve PF doğruluğu henüz doğrulanmamıştır.

## Beş AI teknik değerlendirme yanıtının karşılaştırması
Copilot, Google, Gemini ve Claude'un PF araştırması hakkındaki teknik yanıtları karşılaştırıldı; tahminler, teknik düzeltmeler, güvenlik notları ve birleştirilmiş ilk deney sırası:
- [Dört AI Teknik Değerlendirmesi – Karşılaştırmalı BERO Notu](AI-TEKNIK-DEGERLENDIRME-KARSILASTIRMASI-2026-11-22.md)

## Faz 1 – Claude yakalama/analiz kodu incelemesi
Claude'un ESP32 yakalama sketch'i ve Python analiz betiği, Gemini'nin son uygulama senteziyle birlikte incelendi. Kodların mevcut durumu, sentetik test bulguları, donanım öncesi düzeltmeler ve güvenli deney sırası:
- [Faz 1 Claude Kodu ve Gemini Sentezi İncelemesi](FAZ1/FAZ1-CLAUDE-KODU-GEMINI-INCELEMESI-2026-11-22.md)

Bu taslaklar henüz Arduino derlemesinden veya gerçek ADS1115 donanım testinden geçmedi. Başarılı/kararlı firmware olarak kullanılmamalıdır.

### Faz 1 sentetik test kaydı
Claude'un Python analiz betiği sözdizimi kontrolünden ve sentetik g/h çalıştırmasından geçti. Bu kayıt gerçek ADS1115 donanım testi değildir; komut çıktıları ve yorumları:
- [Faz 1 sentetik test logu](FAZ1/LOGS/SENTETIK-FAZ1-TEST-G-H-2026-11-22.txt)
- [Faz 1 kod inceleme ve deney kararı](FAZ1/FAZ1-CLAUDE-KODU-GEMINI-INCELEMESI-2026-11-22.md)

Arduino derlemesi, ESP32D2 yüklemesi ve ADS1115 fiziksel ölçümü henüz yapılmamıştır.


## 2026-11-22 – PF araştırma durumu ve bugünkü V1.6 grafiği

Bugün depoya eklenen [V1.6 kalibrasyon ve doğrusallık grafiği](../../PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/VERI/V1.6/v1.6-kalibrasyon-ve-dogrusallik.jpg), PF ≥0.90 ideal PF kalibrasyon noktaları ile PF=0.76 / 20.4 W düşük PF noktasını ayrı gösterir. Bu görsel PF düzeltme modeli değildir; düşük PF noktasının normal kalibrasyon grubundan ayrı tutulması gerektiğini gösteren deney görselleştirmesidir.

Çamaşır makinesi uzun pamuklu saha kaydında PZEM PF, ısıtma bloğunda yaklaşık 1.00; düşük/orta akım motor/yıkama bölümlerinde yaklaşık 0.53–0.73 bandında gözlendi. Bu saha kaydı PF araştırması için anlamlı farklı çalışma durumları sunar, ancak PZEM PF değerleri ZMPT101B tabanlı gerçek PF ölçümü değildir ve SCT sapmasının nedenini tek başına kanıtlamaz.

Ayrıca tek 8.5 W LED düşük PF tekrar deneyinde PZEM PF yaklaşık 0.66–0.67 ve SCT/PZEM oranı yaklaşık 1.81–1.83 bulundu; bu tek yük/PF çalışma noktası genel model için yeterli değildir. 100 W dimmer deneyinde PF düşerken SCT/PZEM farkı artmıştır, ancak dimmer dalga biçimini ve akım seviyesini de birlikte değiştirmiştir.

Bütün saha bulguları ve ayrı deney kapsamları:
[PF Araştırması – Güncel Durum ve Saha Verileri](PF-ARASTIRMA-GUNCEL-DURUM-2026-11-22.md)

Teknik hedef değişmemiştir: PZEM PF'ye göre katsayı uydurmak değil, ZMPT101B gerilim ve SCT013 akım dalga biçimlerini güvenli ve zaman hizalı toplayıp P, Vrms, Irms, S ve gerçek PF hesaplamaktır. ADS1115'in örnekleme/zamanlama yeterliliği henüz onaylanmadı.
