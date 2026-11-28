# BERO Ölçüm Altyapısı ve Sensör Doğrulama Stratejisi — V1.0

- **Tarih:** 2026-11-28
- **Durum:** STRATEJİ KABUL EDİLDİ; ilk fiziksel testler bekliyor.
- **Amaç:** Sensör, ölçü aleti, analog ön uç, ADC, haberleşme ve yazılım kaynaklı hataları birbirinden ayırmak; ölçüm altyapısı belirsizliği nedeniyle geliştirme süresini tekrar tekrar kaybetmemek.
- **Kapsam:** PREBERO / Modül 2 ve BERO'daki analog sensörlerin masaüstü karakterizasyonu.

## 1. Ana karar — sensörden yazılıma doğru ölçüm

BERO'da ölçüm geliştirme sırası:

**Fiziksel sensör → sensörün ham elektriksel çıkışı → bağımsız ölçü aleti → dalga biçimi kontrolü → analog ön uç → ADC ham kodu → yazılım hesabı → kalibrasyon modeli.**

Bir aşama, kendisinden önceki katmanın davranışı yeterince anlaşılmadan kalibre edilmiş/başarılı kabul edilmez. Sensörün kendi çıkışı görülmeden ADS1115, MCP3208 veya ESP32 ADC sayısına bakarak sensör hakkında kesin karar verilmez.

## 2. Tezgâh cihazlarının sabit görev dağılımı

| Cihaz | Ana görev | Kullanım sınırı |
|---|---|---|
| **FNIRSI 2D15P** | Analog dalga biçimi, genlik, frekans, zamanlama ve kanal karşılaştırması; dahili DDS ile test sinyali üretimi; temel DMM işlevi | DMM düşük AC mV doğruluğu üretici tablosunda açıkça garanti edilmemiştir. DDS çıkışı kalibrasyon standardı değildir. DDS ve DMM modlarının eşzamanlı çalıştığı varsayılmaz. |
| **UNI-T UT61E+** | **Satın alınacak tek yeni ölçüm cihazı.** Bağımsız analog sensör DMM'si: AC/DC gerilim, düşük AC mV, DC/AC akım, direnç ve frekans | Satın alma/teslim durumu doğrulanana kadar mevcut envanter cihazı sayılmaz. Üretici spesifikasyonlu DMM'dir; kalibrasyon sertifikalı referans standardı olduğu varsayılmaz. 220 mV AC kademesinde 40 Hz–1 kHz doğruluk garantisi yaklaşık 2,2 mV'den başlar; 1,67 mV yalnız görünürlük/kararlılık testidir. |
| **UNI-T UT200B+** | Tek yalıtılmış iletken üzerinde pensle primer/yük akımını yardımcı olarak kontrol etmek | Düşük akımda ve bozulmuş dalga biçimlerinde kesin referans değildir. LoZ özelliği fiziksel model kılavuzundan teyit edilmeden rolüne eklenmez. |
| **UNI-T UT33D+** | Günlük süreklilik, kablo/hat ve temel DC/AC kontrolü | Hassas analog mV referansı olarak kullanılmaz. |
| **FNIRSI SG-002** | Kontrollü DC gerilim (0–10 V sınıfı) ve DC akım döngüsü (4–20 mA dahil) simülasyonu | AC 50 Hz sinüs kaynağı değildir. Kılavuzdaki 50HZ ifadesi ekran gösterim seçeneğidir. Fiziksel cihaz menüsü/terminali teyit edilir. |
| **SANEC USB lojik analizör** | Düşük gerilimli UART, I²C ve SPI zamanlama/protokol yakalama | Dijital analizördür; analog mV ölçmez. RS485 A/B diferansiyel saha hattına doğrudan bağlanmaz; uygun transceiver'ın lojik tarafı veya uygun izole arayüz kullanılır. |
| **SANEC sinyal jeneratörü** | Düşük gerilimli test sinyali üretimi | Envanterde mevcut; tam model/çıkış aralığı doğrulanmadan kritik deney bağımlılığı yapılmaz. |
| **AD9833 / AD9850 gibi DDS modülleri** | İleride ESP/SPI ile otomatik frekans taraması ve tekrarlı uyarım üretimi | BERO'nun ilk sensör karakterizasyonu için satın alma gereksinimi değildir. Fiziksel modülün varlığı, çıkış aralığı ve revizyonu teyit edilmeden ölçüm kaynağı olarak kabul edilmez. |
| **FYE050 / XR2206 gibi jeneratörler** | Alternatif manuel/bağımsız test kaynağı | Şimdilik satın alınmayacak; mevcut 2D15P ve SANEC kaynaklarıyla karşılanamayan somut test ihtiyacı ortaya çıkarsa yeniden değerlendirilir. |

### Satın alma kararı

- Mevcut altyapı: FNIRSI 2D15P, FNIRSI SG-002, SANEC lojik analizör, envanterdeki SANEC sinyal jeneratörü, UNI-T UT200B+ ve UT33D+.
- **Tek planlanan satın alma: UNI-T UT61E+.**
- AD9833, AD9850, FYE050 veya XR2206 için şu aşamada satın alma yapılmaz.
- Yeni cihaz talebi, mevcut cihazlarla gerçekleştirilemeyen somut bir deney ve ölçüm gereksinimi gösterilmeden açılmaz.

## 3. Ölçüm referansı ve kanıt sınıfları

1. **Kaynak ayarı:** DDS/SG-002 ekranına girilen nominal değer. Tek başına gerçek çıkış değeri değildir.
2. **Bağımsız elektriksel ölçüm:** Uygun aralıkta multimetreyle ölçülen RMS/DC/akım/direnç değeri.
3. **Dalga biçimi kanıtı:** 2D15P ile görülen frekans, genlik, şekil, ripple, gürültü ve zaman davranışı.
4. **ADC kanıtı:** ADS1115/MCP3208/ESP ADC ham kodu, gerçek örnekleme hızı, kazanç, ofset ve RMS hesabı.
5. **Karşılaştırma referansı:** PZEM/UT200B+ gibi cihazlardan gelen karşılaştırmalı değer. Bunlar izlenebilir kalibrasyon standardı olarak sunulmaz.

UT61E+ alınsa dahi bu ayrım korunur. Ölçü aletinin ekranda değer göstermesi doğruluk kanıtı değildir.

## 4. Ana test sırası — ölçüm nedeniyle tekrar kaybetmemek için

### Aşama 0 — Cihaz ve bağlantı teyidi
- Fiziksel model, PCB revizyonu, terminal isimleri ve ölçüm kablo bağlantısı kaydedilir.
- DMM probları/kabloları, giriş soketleri ve seçilen kademe kontrol edilir.
- Her cihazın görevi ve sınırı yukarıdaki tabloya göre sabitlenir.
- Doğrulanmamış cihaz özelliği deney şartı olarak kabul edilmez.

### Aşama 1 — Bağımsız ölçü aleti ve kaynak kontrolü

**AC düşük mV kontrolü**
- FNIRSI 2D15P DDS ile 50 Hz sinüs üretilir.
- Kaynağın dalga biçimi 2D15P osiloskop ekranında kontrol edilir.
- 2D15P'nin minimum 0,1 Vpp çıkışı, 20 kΩ seri + 1 kΩ şönt dirençle nominal 1/21 oranında zayıflatma seçeneğiyle düşük mV seviyelerine indirilebilir.
- Yaklaşık seviyeler: 1,68 mV RMS (yalnız görünürlük/taban ayrımı), 3,37 mV, 8,42 mV ve 16,84 mV RMS.
- Kaynak çıkış empedansı, direnç toleransı ve DMM yüklemesi hesaba katılır. Bölücü fiziksel olarak doğrulanmadan kalibrasyon standardı sayılmaz.
- 2D15P'nin DDS ve DMM işlevlerinin eşzamanlı çalıştığı varsayılmaz.
- UT61E+ geldikten sonra aynı kaynak ve bağlantı noktalarında DMM ölçümleri tekrarlanır. 1,68 mV noktası yalnız görünürlük/kararlılık; 3,37 mV ve üstü UT61E+ 220 mV AC kademesinin 40 Hz–1 kHz üretici doğruluk şartları içinde değerlendirilir.

**DC gerilim / akım döngüsü kontrolü**
- FNIRSI SG-002 ile cihazın fiziksel menüsünde desteklenen DC gerilim setpoint'leri ve 4–20 mA akım döngüsü noktaları uygulanır.
- UT61E+ ile gerilim veya seri akım / uygun algılama direnci üzerinden ölçüm yapılır.
- SG-002'nin ayar ekranı mutlak referans kabul edilmez; gerçek çıkış ayrıca ölçülür.
- SG-002 AC sinüs kaynağı olarak kullanılmaz.

### Aşama 2 — Sensörün kendisini bağımsız tanıma
- Sensörün tam model/çıkış türü/bağlantısı doğrulanır.
- Beslemeli sensörlerde doğru besleme, referans GND ve çıkış bağlantısı kontrol edilir.
- Çıkış tipi ne gerektiriyorsa doğru fiziksel birimle ölçülür: AC mV, DC V/mV, akım, direnç veya frekans.
- Yüksüz/sıfır noktası, düşük-orta-yüksek birkaç kararlı nokta, tekrarlanabilirlik ve yük değişimine tepki kaydedilir.
- Akım çıkışlı CT sekonderi uygun burden ile kapalı tutulur; gerilim çıkışlı SCT013-030'a harici burden eklenmez.
- Her sensör için ham değer, ölçü aleti kademesi, yük/uyartım, zaman ve gözlem notu saklanır.

### Aşama 3 — Dalga biçimi ve gürültü karakterizasyonu
- Aynı sensör çıkışı uygun düşük gerilimli koşullarda 2D15P ile gözlenir.
- Sinüs/bozulma, frekans, tepe/RMS ilişkisi, ripple, gürültü, faz/zaman farkı ve geçici olaylar ayrı ayrı kaydedilir.
- Osiloskop ekranında görülen gürültü otomatik olarak sensör gürültüsü sayılmaz; prob, toprak, bant genişliği, dikey kademe ve ölçüm düzeni de kontrol edilir.

### Aşama 4 — ADC/analog ön uç karakterizasyonu
- Sensör çıkışının bağımsız DMM ve osiloskopla karakteri anlaşıldıktan sonra ADC bağlanır.
- ADS1115/MCP3208/ESP32 ADC'nin ham kodu, PGA/attenuation, referans, örnekleme hızı, örnekleme penceresi ve kanal sıralaması kaydedilir.
- Aynı fiziksel girişte sensör çıkışı ile ADC kodu eşleştirilir. ADC'nin ölçüm hatası sensör hatası olarak etiketlenmez.
- Bias, yükselteç, burden, filtre veya başka şartlandırma bileşenleri yalnızca gerekçesi ve ölçüm etkisi ayrı deneyle gösterilirse eklenir.

### Aşama 5 — Hesap, kalibrasyon ve yazılım
- Önce ham elektriksel dönüşüm ve ADC ölçeği belirlenir.
- Kalibrasyon katsayısı ancak yeterli noktada, tekrar ve mümkünse bağımsız doğrulama verisiyle hesaplanır.
- PZEM karşılaştırma referansıdır; mutlak ground truth diye adlandırılmaz.
- Mevcut kabul edilmiş YAML/model sürümlerinin üzerine yazılmaz; yeni sürüm ve rapor açılır.

## 5. İlk uygulanacak deneyler

1. **2D15P DMM + SCT013-030 doğrudan çıkış deneyi:** 0,05 A karşılığı yaklaşık 1,67 mV RMS sinyalin yüksüz tabandan ayırt edilebilirliğini gözle. Bu nokta gürültü nedeniyle doğruluk hedefi değildir; yalnız görünürlük/tekrarlanabilirlik denemesidir. Asıl karakterizasyon daha güvenilir akım bölgesinde yapılır.
2. **2D15P DDS + pasif bölücü testi:** UT61E+ geldiğinde 50 Hz düşük mV seviyelerinde gösterim kararlılığı ve yaklaşık seviye tepkisini incele. Kaynak kalibrasyon standardı değildir.
3. **SG-002 DC testi:** UT61E+ ile 0–10 V sınıfı DC gerilim ve 4–20 mA simülasyonunu karşılaştır.
4. **SCT013 sensör karakterizasyonu:** UT61E+ ile 0,5 A ve üzerindeki kararlı çalışma noktalarında AC mV davranışını incele; 2D15P ile dalga şeklini eş zamanlı/uygun şekilde gözle.
5. **ADC karşılaştırması:** Yukarıdaki ham sensör davranışı görüldükten sonra ADS1115/MCP3208/ESP ADC ile aynı noktalar karşılaştırılır.

Ayrıntılı deney dosyaları MOD2-GRV002 görev klasöründe tutulur.

## 6. Başarı kapıları

- **G0 – Kaynak/ölçü aleti:** Seçilen kaynak, çıkış türü ve ölçü aleti kademesi doğru; gerçek çıkış seviyesi bağımsız ölçümle teyit edilmiş.
- **G1 – Sensör:** Sensörün yüksüz çıkışı, tepki yönü, pratik alt aralığı ve tekrar davranışı anlaşılmış.
- **G2 – Analog dalga:** Dalga şekli ve gürültünün sensörden mi, prob/bağlantı/ölçüm cihazından mı geldiği ayrıştırılmış.
- **G3 – ADC:** Ham ADC kodu ile bağımsız elektriksel ölçüm arasındaki dönüşüm ve sapma belirlenmiş.
- **G4 – Yazılım:** RMS/filtre/kalibrasyon modeli ham veride doğrulanmış ve ayrı sürüm olarak saklanmış.

Önceki kapıdan kanıt olmadan sonraki kapı “tamamlandı” olarak işaretlenmez. Başarısız ve kararsız deneyler de arşivlenir.

## 7. Güvenlik sınırları

- DMM voltaj girişi ile akım girişi birbirine karıştırılmaz. Akım ölçümü seri bağlantı gerektirir.
- Akım çıkışlı CT sekonderi primer akım varken açık bırakılmaz; uygun burden/topoloji üretici bilgisinden doğrulanır.
- SCT013-030 30 A / 1 V gerilim çıkış modelinde dahili burden olduğu kabul edilir; harici burden eklenmez.
- Osiloskopun pille çalışması girişlerinin şebekeden izole olduğunu kanıtlamaz. Ground klipsi doğrudan şebeke fazına/nötrüne bağlanmaz.
- ZMPT101B modülünün şebeke tarafı, izolasyon mesafesi, terminal koruması ve kapalı test düzeneği incelenmeden şebeke bağlantısı yapılmaz.
- İlk sinyal jeneratörü/bölücü testleri düşük gerilimli ve akım sınırlı düzende yapılır.

## 8. Satın alma ve kapsam kontrolü

- Tek planlı yeni cihaz UT61E+'tır.
- AD9833/AD9850 gibi programlanabilir DDS modülleri ve FYE050/XR2206 jeneratörleri mevcut testler yürütülmeden satın alma listesine alınmaz.
- Yeni bir cihaz ancak mevcut cihazlarla karşılanamayan belgeli bir test gereksinimi varsa değerlendirilir.
- Bu strateji cihaz satın almayı değil, sensör doğrulama sırasını ve kanıt standardını sabitler.

## 9. Sonuç / revizyon kaydı

V1.0, kullanıcıyla 2026-11-28 tarihinde belirlenen çalışma yaklaşımını kaydeder. Buradaki deneylerin fiziksel olarak tamamlandığı, cihazların kalibre edildiği veya tüm sensörlerin doğrulandığı anlamına gelmez. Sonuçlar deney dosyalarında kanıtlarıyla saklandıkça bu stratejinin revizyonu yapılabilir.
