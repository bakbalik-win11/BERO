# 13 Kasım 2026 — FNIRSI 2D15P Osiloskop Öğrenme Başlığı

## Amaç

BERO çalışmalarında ve genel hobi elektroniğinde kullanılmak üzere satın alınan **FNIRSI 2D15P** osiloskobun kullanımını adım adım öğrenmek; analog sinyalleri doğrudan gözlemlemek ve ESP32/ADC yazılımının ürettiği istatistiklerle bağımsız bir ölçüm yolundan karşılaştırmak.

Bu başlık, BERO'nun ana veri toplama ve etiketleme mimarisinden ayrı bir öğrenme/ölçüm konusu olarak tutulur. Osiloskop BERO'nun çalışması için zorunlu bir bileşen değildir; fiziksel sinyal davranışını incelemek ve hata ayıklamak için yardımcı ölçüm cihazıdır.

## Satın alma kaydı

- **Cihaz:** FNIRSI 2D15P, 2 kanallı taşınabilir osiloskop / multimetre / sinyal jeneratörü.
- **Karar ve sipariş tarihi:** 2026-11-13.
- **Kullanıcının bildirdiği ödeme:** 11.152 TL, 6 taksit; aylık yaklaşık 1.858,67 TL.
- **Satıcı / garanti / kutu içeriği:** Sipariş belgesi ve ürün tesliminde doğrulanacak.
- **Durum:** Sipariş verildi; cihaz henüz teslim alınmadı ve fiziksel test yapılmadı.

Satış ilanlarında belirtilen özellikler cihazın ölçüm performansının doğrulandığı anlamına gelmez. Gerçek cihaz, prob ve ölçüm sonuçları teslimattan sonra kontrol edilecektir.

## BERO içindeki rolü

Osiloskopun temel görevi analog gerilim-zaman dalga biçimini göstermektir. SANEC 24 MHz / 8 kanal lojik analizör dijital lojik seviyelerini ve protokol zamanlamasını inceler; analog osiloskopun yerine geçmez.

| Ekipman | BERO'daki rol |
|---|---|
| FNIRSI 2D15P | Analog dalga biçimi, gerilim seviyesi, zamanlama ve gürültü gözlemi |
| SANEC 24 MHz / 8 kanal | Dijital sinyaller ve UART / I²C / SPI protokol incelemesi |
| ADS1115 | Analog sinyalin sayısal örneklenmesi |
| ESP32 | Örnekleme, veri işleme ve istatistik üretimi |
| Python | Kayıtların analizi ve görselleştirilmesi |

Osiloskop ölçümü ile ESP32 istatistikleri karşılaştırıldığında amaç laboratuvar kalibrasyonu veya mutlak doğruluk iddiası değildir. Amaç, aynı fiziksel sinyalin iki ayrı ölçüm yolunda tutarlı davranıp davranmadığını incelemek ve olası sensör, analog ön uç, ADC veya yazılım sorunlarını ayırmaya yardımcı olmaktır.

## Öğrenme planı

Eğitim cihaz teslim alındıktan sonra uygulamalı ve küçük adımlarla yürütülecek. Her aşamada önce kavram ve bağlantı açıklanacak, ardından düşük gerilimli bir deney yapılacak.

1. **Cihazı tanıma**
   - Kanal girişleri, ekran, fiziksel tuşlar ve döner kontroller.
   - Menü yapısı, kanal etkinleştirme ve ölçüm ekranı.
   - Volt/div, Time/div, trigger, Run/Stop ve otomatik ayar kavramları.

2. **Prob ve güvenli bağlantı**
   - Osiloskop probunun 1X / 10X seçimi ve cihaz menüsündeki prob oranının eşleştirilmesi.
   - Prob kompanzasyonu ve ilk kontrol.
   - Prob toprak klipsinin işlevi ve ortak referansın etkisi.
   - Ölçüm öncesi bağlantı ve gerilim sınırlarının kontrolü.

3. **İlk dalga biçimi**
   - Cihazın sinyal jeneratöründen düşük gerilimli sinüs ve kare dalga üretme.
   - Genlik, frekans, periyot ve tepeden tepeye gerilim (Vpp) kavramları.
   - Volt/div ve Time/div ayarlarının etkisi.

4. **İki kanal kullanımı**
   - CH1 ve CH2 dalga biçimlerini aynı anda görüntüleme.
   - Kanal ölçekleri, zaman tabanı ve tetikleme ilişkisi.
   - Aynı sinyalin iki noktada veya iki sensör çıkışında karşılaştırılması.

5. **BERO analog zincirini inceleme**
   - SCT013 30A/1V çıkışını düşük gerilimli ve uygun bağlantı düzeninde gözlemleme.
   - Teslim edilirse SCT013 5A/1V ile aynı yük koşullarında karşılaştırma.
   - Bias seviyesini, dalga merkezini, olası kırpılmayı ve gürültüyü inceleme.
   - Gerekirse ADS1115 girişindeki sinyali ayrıca gözlemleme.

6. **ESP32 istatistikleriyle çapraz kontrol**
   - Aynı fiziksel sinyal ve mümkün olduğunca aynı zaman penceresi için osiloskop ve ESP32 sonuçlarını karşılaştırma.
   - RMS, tepe, Vpp, frekans ve kararlılık gibi ortak parametreleri değerlendirme.
   - Osiloskopun kendi ölçüm toleransı, prob oranı, örnekleme ve bant genişliği sınırlarını dikkate alma.
   - Fark görüldüğünde sensör, bias/analog ön uç, ADC ve yazılım olasılıklarını ayrı ayrı inceleme.

7. **Genel elektronik hobi uygulamaları**
   - Düşük gerilimli devrelerde sinyal takibi.
   - Uygun koşullarda MCP6002 gibi analog devrelerin giriş/çıkış karşılaştırması.
   - Sinyal jeneratörü ile basit devre tepkilerinin incelenmesi.

## İlk kullanım için güvenlik kuralları

- İlk öğrenme ve denemeler yalnızca düşük gerilimli, güvenli ve akım sınırlaması uygun deney devrelerinde yapılacak.
- **Osiloskop probunun toprak klipsi koruyucu toprakla ilişkili olabilir. Toprak klipsi doğrudan şebeke fazına, nötre veya izolasyonu doğrulanmamış devre noktasına bağlanmayacak.**
- 230 V şebeke üzerinde doğrudan ölçüm yapılmayacak. Şebeke tarafındaki inceleme ancak uygun kategoride diferansiyel/izole ölçüm düzeni ve yetkin güvenlik prosedürü varsa ayrıca ele alınabilir.
- SCT sekonder/çıkış bağlantısı ve ölçüm devresi modelin özellikleri doğrulanmadan açık devre veya gelişigüzel bağlantı durumunda bırakılmayacak.
- Probun 1X/10X oranı, osiloskop menüsündeki prob ayarı ve beklenen gerilim seviyesi her ölçümden önce kontrol edilecek.
- Osiloskop ekranındaki otomatik ölçüm değerleri tek başına doğruluk kanıtı sayılmayacak.

## Deney kayıt standardı

Her anlamlı deney için aşağıdakiler kaydedilecek:

- Tarih ve deney amacı.
- Osiloskop modeli, kanal ve prob oranı (1X / 10X).
- Volt/div, Time/div, trigger ayarı ve varsa bant genişliği sınırlaması.
- Ölçüm noktası, bağlantı şeması ve ortak GND bilgisi.
- Sensör modeli, yük koşulu ve PZEM referans ölçümü varsa değeri.
- Osiloskop ekran görüntüsü veya dışa aktarılan dalga verisi.
- ESP32 / ADS1115 ham veya özet ölçüm kaydı.
- Gözlem, hesaplama, yorum ve belirsizlikler.
- Sonuç durumu: gözlendi, tekrarlandı, doğrulandı veya sonuçsuz.

Başarılı deneyler ve örnek loglar, çıktının yorumu ile birlikte bu başlık altında veya ilgili donanım klasöründe saklanacak. Henüz yapılmamış deneyler başarılı/ doğrulanmış olarak işaretlenmeyecek.

## Mevcut durum

- [x] FNIRSI 2D15P model tercihi yapıldı.
- [x] 2026-11-13 tarihinde sipariş verildi (kullanıcı bildirimi).
- [ ] Cihaz teslim alındı.
- [ ] Kutu içeriği ve aksesuarlar kontrol edildi.
- [ ] Prob 1X / 10X ayarı ve kompanzasyonu öğrenildi.
- [ ] İlk düşük gerilimli sinyal ölçümü yapıldı.
- [ ] İki kanal karşılaştırması yapıldı.
- [ ] SCT013 30A/1V dalga biçimi kaydedildi.
- [ ] SCT013 5A/1V temin edilirse karşılaştırmalı deney yapıldı.
- [ ] Osiloskop ve ESP32 / ADS1115 ölçümleri karşılaştırıldı.

## Kapsam dışı

Bu öğrenme başlığı BERO'yu güç kalitesi analizörüne dönüştürme amacı taşımaz. Harmonik, FFT/THD, şebeke kalite sınıflandırması veya laboratuvar kalibrasyonu bu çalışmanın hedefi değildir. Ana BERO hedefi, SCT ham/özet ölçümlerini PZEM referanslı kararlı pencerelerle incelemeye devam etmektir.

---

**İlke:** Önce güvenli bağlantı, sonra doğru dalga biçimi, ardından ölçüm ve yorum. Cihazı öğrenmek de BERO'nun öğrenme günlüğünün bir parçasıdır.
