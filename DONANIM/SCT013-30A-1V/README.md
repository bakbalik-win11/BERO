# SCT013-030 — 30 A / 1 V akım trafosu

## 1. Bu klasör ne için?

YHDC SCT013-030 (30 A / 1 V) sensörünün teknik referansı, bağlantısı, analog ölçüm şartları ve BERO projesindeki test notları burada tutulur. Bu model, çıkışında **gerilim veren** SCT013 çeşididir; 100 A / 50 mA olan SCT013-000 ile karıştırılmamalıdır.

## 2. Hızlı teknik özet

| Özellik | Bilgi |
|---|---|
| Model | SCT013-030 |
| Nominal primer akımı | 30 A RMS AC |
| Nominal çıkış | 1 V RMS AC @ 30 A |
| Nominal hassasiyet | Yaklaşık 33,33 mV/A RMS |
| Maksimum giriş bilgisi | Bazı YHDC veri sayfası kopyalarında 60 A olarak listelenir; bu, 60 A'da doğruluk/uzun süreli çalışma garantisi değildir |
| Çekirdek / yapı | Bölünebilir ferrit çekirdek, kelepçe tipi |
| Kablo / konnektör | Yaklaşık 1 m kablo, 3,5 mm üç kontaklı fiş |
| Frekans | Üretici dokümanlarında 50 Hz–1 kHz |
| Çalışma sıcaklığı | Üretici dokümanlarında -25 °C–+70 °C |
| Dahili yük direnci | Gerilim çıkışlı modelde vardır; ek burden direnci normalde eklenmez |

**Hesap:** 30 A girişte 1 V RMS ⇒ 1 V / 30 A ≈ 0,03333 V/A. Örneğin ideal nominal oranda 3 A ≈ 0,1 V RMS, 15 A ≈ 0,5 V RMS. Bunlar hesap değeridir; gerçek sensör kalibrasyonla doğrulanır.

## 3. Bağlantı ve yön

- Kelepçeyi yalnızca **tek bir iletkenin** etrafına kapat. Faz ve nötrü birlikte kelepçelemek, akımlar birbirini götürdüğü için yaklaşık sıfır okuma oluşturabilir.
- Çeneler tamamen kapanmalı; temas yüzeyleri temiz olmalı.
- Gövdedeki **IP oku**, üreticinin primer akım referans yönünü belirtir. Yön, özellikle gerilim-akım faz ilişkisi ve aktif güç hesabında önemlidir. Yalnızca RMS büyüklüğü ölçülüyorsa akım yönünü ters çevirmek ideal olarak RMS değerini değiştirmez.
- Çıkış uçları K/L olarak işaretlenmiş olabilir. Bu bir DC besleme girişi değildir; sensör AC gerilim üretir. Uçları değiştirmek dalga biçiminin faz işaretini ters çevirebilir. Faz ölçümü yapılacaksa aynı yön ve kablolama standardını bütün kanallarda koru.
- Fişin tip/ring/sleeve bağlantısını yalnızca görünüşten varsayma. Üretici çizimini ve elindeki fiş/kabloyu süreklilik ölçümüyle doğrula; bazı fiş şemalarında bir kontak NC gösterilir.

## 4. ESP32 / MCP3208 analog ön uç

SCT013-030'un 1 V RMS çıkışı sinüzoidal kabul edilirse tepe değeri yaklaşık 1,414 V'tur. ESP32/MCP3208 tek beslemeli ADC girişine negatif AC doğrudan uygulanamaz; sinyal uygun bir DC bias çevresinde tutulmalıdır.

BERO testlerinde konuşulan yaklaşık 1,67 V bias ve 3,12 V ADC referansı için teorik nominal sinyal aralığı:
- Alt tepe: 1,67 − 1,414 ≈ 0,256 V
- Üst tepe: 1,67 + 1,414 ≈ 3,084 V

Üst tepe 3,12 V referansa çok yakındır. Bias toleransı, gerçek RMS çıkış, şebeke bozulması ve geçici darbeler için pay azdır. ADC girişinin **0 V ile VREF arasında** kaldığını osiloskopla kontrol et; VREF'i aşma. 30 A üzerindeki akımda çıkış 1 V RMS'i aşabileceği için kırpılma riski artar. Bu hesap ideal sinüs varsayımıdır, güvenlik garantisi değildir.

- Gerilim çıkışlı SCT013 için sırf akım trafosu olduğu için harici burden direnci ekleme; dahili direnç bulunur. Ek yük, oranı ve ölçümü değiştirir.
- Bias, ADC giriş empedansı, koruma elemanları ve RC filtre gerçek devre şemasına göre değerlendirilmelidir.
- Ölçüm sırasında sensörün çıkışını ve ADC pinini aynı anda gözlemek, bias ve kırpılmayı ayırmaya yardımcı olur.
- Sensörün sekonder devresini, özellikle model kimliği belirsizken, açık devre bırakmanın güvenli olduğunu varsayma.

## 5. RMS ve kalibrasyon

1. Akım olmayan durumda bias merkezini ve ADC gürültüsünü kaydet.
2. Bilinen bir referans akımla, tercihen True-RMS ölçerle, birden çok noktada test et.
3. Ham ADC sayımlarından bias ortalamasını çıkar; RMS hesabında sinyalin DC biasını akım olarak sayma.
4. Sensör oranını gerçek referansla kalibre et. Nominal başlangıç ölçeği yaklaşık 33,33 mV/A RMS'tir; gerçek ADC kodu dönüşümü ayrıca VREF, ADC çözünürlüğü ve analog kazanca bağlıdır.
5. Dalga biçiminde tepe noktalarının ADC alt/üst sınırına yapışmadığını doğrula.
6. RMS penceresi ve örnek zaman damgalarını kaydet. Düzensiz örnekleme aralıklarını eşit aralıklıymış gibi kabul etmek RMS sonucunu bozabilir.

## 6. BERO geçmişinden önemli test uyarıları

- MCP3204/MCP3208 ile sıfıra yakın veya sabit/tekrarlayan okumalar görülmesi tek başına sensör arızasını kanıtlamaz.
- Daha önce ADC fiziksel olarak çıkarıldığında da benzer RX örüntüleri görüldüğü için SPI aktarımı, CS zamanlaması, TX/RX baytları ve okuma kodu ayrıca doğrulanmalıdır.
- SPI hata sayacının sıfır olması, alınan verinin doğru kanalı ve doğru sayısal değeri temsil ettiğini kanıtlamaz.
- Her testte sensör modeli, ADC modeli, VREF, bias, SPI pinleri/hızı/modu, ham RX baytları ve gerçek referans akımını birlikte kaydet.

## 7. Sınırlar ve güvenlik

Bu sensör şebeke iletkeninin etrafına takılır; kelepçeyi açıp kapatırken canlı iletkene veya çıplak bakıra dokunma. Sensörün yalıtım beyanı tüm montajı otomatik olarak güvenli yapmaz. Şebeke tarafındaki işler uygun yetkinlikle yapılmalıdır. Sensör, tek başına elektrik çarpmasına karşı koruma veya sertifikalı enerji sayacı değildir.

## 8. Kaynaklar

- YHDC SCT013 ürün ailesi / üretici sayfası ve veri sayfası bağlantıları: https://en.yhdc.com/product/SCT013-401.html
- SCT013-030 PDF kopyası (YHDC dokümanının dağıtılmış kopyası): https://naylampmechatronics.com/img/cms/000154/SCT013-030-0-30A-0-1V.pdf
- Seeed Studio'da barındırılan SCT013 veri sayfası PDF'si: https://files.seeedstudio.com/wiki/AC_Current_Sensor/Datasheet_of_SCT013.pdf
- OpenEnergyMonitor SCT-013 ailesi açıklaması: https://community.openenergymonitor.org/t/about-split-core-cts-sct-013-family/481

> Üretici dokümanlarının bazı kopyalarında tablo alanları eksik veya çeviri hatalı olabilir. Fiziksel sensörün etiketi ve tam model kodu birincil doğrulamadır.
