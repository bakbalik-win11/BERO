# SCT013-100 — 100 A / 1 V akım trafosu

## 1. Bu klasör ne için?

YHDC SCT013-100 (100 A / 1 V) gerilim çıkışlı akım trafosunun teknik bilgileri, bağlantısı, ADC koşulları ve BERO test notları burada tutulur.

**Model koduna dikkat:** SCT013-100 (100 A / 1 V) ile SCT013-000 (100 A / 50 mA) aynı elektriksel çıkışa sahip değildir. SCT013-100'de dahili burden/yük direnci bulunur ve nominal çıkışı gerilimdir. SCT013-000 ise akım çıkışlı modeldir; onun için tasarlanan yük direnci yaklaşımını bu sensöre doğrudan uygulama.

## 2. Hızlı teknik özet

| Özellik | Bilgi |
|---|---|
| Model | SCT013-100 |
| Nominal primer akımı | 100 A RMS AC |
| Nominal çıkış | 1 V RMS AC @ 100 A |
| Nominal hassasiyet | Yaklaşık 10 mV/A RMS |
| Maksimum giriş bilgisi | YHDC veri sayfası kopyalarında 120 A olarak listelenir; bu, 120 A'da doğruluk veya sürekli çalışma garantisi değildir |
| Çekirdek / yapı | Bölünebilir ferrit çekirdek, kelepçe tipi |
| Kablo / konnektör | Yaklaşık 1 m kablo, 3,5 mm üç kontaklı fiş |
| Frekans | Üretici dokümanlarında 50 Hz–1 kHz |
| Çalışma sıcaklığı | Üretici dokümanlarında -25 °C–+70 °C |
| Dahili yük direnci | Gerilim çıkışlı modelde vardır; ek burden direnci normalde eklenmez |

**Hesap:** 100 A girişte 1 V RMS ⇒ 1 V / 100 A = 0,01 V/A. İdeal nominal oranda 10 A ≈ 0,1 V RMS, 50 A ≈ 0,5 V RMS. Bunlar hesap değeridir; gerçek sensör kalibrasyonla doğrulanır.

## 3. Bağlantı ve yön

- Kelepçeyi yalnızca **tek bir iletkenin** etrafına kapat. Faz ve nötr birlikte kelepçelenirse akımlar birbirini götürür ve yaklaşık sıfır ölçülebilir.
- Çenelerin tam kapandığını ve temas yüzeylerinin temiz olduğunu kontrol et.
- Gövdedeki **IP oku**, primer akımın referans yönünü gösterir. Sadece RMS büyüklüğü için yön çoğu durumda sonucu değiştirmez; akım-gerilim faz ilişkisi veya aktif güç ölçümünde yön ve referans faz önemlidir.
- K/L uçları AC çıkış uçlarıdır; DC artı/eksi gibi değerlendirilmez. Uçları değiştirmek dalga biçiminin faz işaretini ters çevirebilir. Faz analizi yapılacaksa tüm kanallarda tutarlı bağlantı kullan.
- 3,5 mm fişin kontaklarını renk veya şekilden varsayma; üretici şemasını ve gerçek kablo sürekliliğini doğrula.

## 4. ESP32 / MCP3208 analog ön uç

Nominal 1 V RMS sinyalin sinüzoidal tepe değeri yaklaşık 1,414 V'tur. Tek beslemeli ADC'ye negatif gerilim uygulanmaması için sinyal, uygun bir DC bias çevresine oturtulmalıdır.

BERO'da daha önce ele alınan yaklaşık 1,67 V bias ve 3,12 V VREF ile teorik nominal aralık:
- Alt tepe: 1,67 − 1,414 ≈ 0,256 V
- Üst tepe: 1,67 + 1,414 ≈ 3,084 V

Bu, nominal 100 A'da bile 3,12 V ADC referansına yakın üst tepe demektir. Bias toleransı ve sinyal tepe değerleri için pay sınırlıdır. Gerçek dalga biçimini osiloskopla ölç; ADC pininin 0 V–VREF dışına çıkmadığını ve kırpılma olmadığını doğrula. 100 A üzerindeki akımlarda nominal çıkış aşılabilir.

- Bu modelde dahili burden direnci vardır; ilave burden direnci eklemek ölçüm oranını değiştirir ve gereksiz yük oluşturabilir.
- 3,12 V, geçmişte BERO testinde kaydedilmiş VREF değeridir; her kurulumda yeniden ölçülmelidir.
- Biasın gerçekten ADC pininde bulunduğunu, sensör bağlanmadan ve sensör bağlıyken ayrı ayrı kontrol et.
- ADC giriş koruması, filtre, empedans ve kablo düzeni devre şemasına göre doğrulanmalıdır.

## 5. RMS ve kalibrasyon

1. Akım yokken ADC bias ortalamasını ve gürültüyü kaydet.
2. Bilinen akımlarda True-RMS referans cihazıyla birkaç kalibrasyon noktası al.
3. Biası ham örneklerden çıkar; DC biası ölçülen akıma dahil etme.
4. Başlangıç ölçeği yaklaşık 10 mV/A RMS'tir; ADC kodu/A ölçeği ayrıca VREF, ADC çözünürlüğü, analog devre ve gerçek kalibrasyondan çıkarılmalıdır.
5. Tepe değerlerinde ADC alt/üst sınıra yaklaşma veya kırpılma olup olmadığını kontrol et.
6. Örnek zaman damgalarını ve RMS penceresini kaydet; düzensiz örnekleme aralıklarını eşit kabul etme.

## 6. BERO geçmişinden önemli test uyarıları

- Önceki MCP3204/MCP3208 denemelerinde sıfıra yakın veya tekrarlayan okumalar görüldü; bunun SCT013 sensöründen kaynaklandığı kanıtlanmış değil.
- ADC fiziksel olarak çıkarıldığında da benzer RX örüntüleri görüldüğünden SPI, CS, TX/RX baytları ve yazılım decode işlemi sensörden bağımsız olarak test edilmeli.
- SPI_ERROR_COUNT=0, ADC verisinin doğru olduğunu kanıtlamaz.
- Her denemede tam sensör modeli, ADC modeli, VREF, bias, SPI ayarları, ham baytlar ve referans akımını kaydet.

## 7. Güvenlik

Kelepçe, yalıtımı sağlam tek bir iletken etrafına takılır. Kurulum sırasında canlı iletkene veya çıplak bakıra dokunma. Yalıtım değeri, tüm sistemin güvenli kurulduğu anlamına gelmez. Sensör tek başına koruma cihazı veya sertifikalı enerji sayacı değildir.

## 8. Kaynaklar

- YHDC SCT013 üretici ürün sayfası ve veri sayfası bağlantıları: https://en.yhdc.com/product/SCT013-401.html
- SCT013-100-100A-1V PDF kopyası: https://cdn.webshopapp.com/shops/304271/files/444277299/sct013-100-100a-1v.pdf
- Seeed Studio'da barındırılan SCT013 veri sayfası PDF'si: https://files.seeedstudio.com/wiki/AC_Current_Sensor/Datasheet_of_SCT013.pdf
- OpenEnergyMonitor SCT-013 ailesi açıklaması: https://community.openenergymonitor.org/t/about-split-core-cts-sct-013-family/481

> Bazı çevrimiçi tablolar SCT013 modellerini ve yük dirençlerini karıştırabiliyor. Etiketteki tam model kodunu doğrulamadan 100 A / 50 mA modeliyle aynı bağlantı varsayımını kullanma.
