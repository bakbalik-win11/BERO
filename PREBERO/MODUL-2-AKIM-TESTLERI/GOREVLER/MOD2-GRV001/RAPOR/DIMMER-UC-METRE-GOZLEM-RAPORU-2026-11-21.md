# MOD2-GRV001 – Dimmer altında üçlü akım ölçümü gözlem raporu

**Tarih:** 2026-11-21  
**Deney:** SANEC 220 V dimmer ile tost makinesi yükünde akım ölçümlerinin karşılaştırılması  
**Ölçüm zincirleri:** Modül 3 PZEM, Modül 2 ESP32D2 + ADS1115 No.10 + SCT013 30A/1V, UNI-T UT200B+ pens ampermetre  
**Firmware:** V1.1 – katsayı 27.59 (deney boyunca değiştirilmedi)  
**Durum:** **KAPATILDI – dimmer ile katsayı alanı taraması sürdürülmeyecek.**

## 1. Amaç

Dimmer ayarı değiştikçe PZEM ile SCT/ADS1115 akım ölçümleri arasındaki farkın değişip değişmediğini gözlemek ve bağımsız üçüncü ölçüm olarak UNI-T UT200B+ pens ampermetreyi karşılaştırmaya dahil etmek.

Bu çalışma yeni katsayı belirleme veya kalibrasyon deneyi değildir. Dimmer altında elde edilen veriler, normal şebeke koşullarında alınan V1.1 kalibrasyon verileriyle birleştirilmez.

## 2. Deney koşulları

- Yük: Tost makinesi.
- Gerilim: Deney pencerelerinde yaklaşık 219–226 V.
- Yük kontrolü: SANEC AC 220 V dimmer.
- Akım sensörü: SCT013 30A/1V, ADS1115 No.10, ESP32D2.
- Karşılaştırma: Modül 3 PZEM.
- Bağımsız el ölçümü: UNI-T UT200B+.
- V1.1 firmware ve 27.59 katsayısı sabit tutuldu.
- Dimmer ayarı maksimumdan daha düşük seviyelere indirildi.

## 3. CSV'den çıkarılan kararlı gözlem pencereleri

Kaynak dosya: Home Assistant `history (5).csv`. Zamanlar Türkiye yerel saatidir. PZEM ve SCT ortalamaları aşağıdaki zaman pencerelerinde pozitif sayısal örneklerden hesaplandı. UT200B+ değerleri kullanıcı tarafından ilgili kademe için bildirilen pens okumalarıdır; CSV içinde pens sensörü kaydı bulunmamaktadır. Bu nedenle pens ölçümünün PZEM/SCT örnekleriyle milisaniye düzeyinde eşzamanlı olduğu iddia edilmemektedir.

| Kademe | Yerel zaman penceresi | PF | UT200B+ | PZEM ort. (n) | SCT ort. (n) |
|---|---|---:|---:|---:|---:|
| Maksimum | 18:01:06–18:02:11 | 1.00 | 7.69 A | 7.8621 A (14) | 8.0685 A (66) |
| Ara | 18:03:56–18:04:31 | 0.85 | 6.37 A | 6.6435 A (8) | 7.9016 A (36) |
| Düşük | 18:06:21–18:06:41 | 0.47 | 3.29 A | 3.6518 A (5) | 5.4844 A (21) |

### 3.1 Pens okumalarına göre farklar

Pens değeri karşılaştırma noktası olarak alınarak hesaplanan farklar:

| Kademe | PZEM – pens | SCT – pens | SCT – PZEM |
|---|---:|---:|---:|
| Maksimum | +%2.24 | +%4.92 | +%2.63 |
| Ara | +%4.29 | +%24.04 | +%18.94 |
| Düşük | +%11.00 | +%66.70 | +%50.18 |

Formül: `(ölçüm - karşılaştırma değeri) / karşılaştırma değeri × 100`.

Bu yüzdeler gözlem karşılaştırmasıdır. UT200B+ değerleri anlık kullanıcı okumaları, PZEM/SCT değerleri ise zaman penceresi ortalamaları olduğundan laboratuvar düzeyinde eşzamanlı doğruluk sonucu olarak yorumlanmamalıdır.

## 4. Gözlem ve değerlendirme

1. Maksimum dimmer konumunda üç ölçüm birbirine görece yakındır.
2. Dimmer daha düşük kademelere alındığında PZEM ile SCT/ADS1115 arasındaki fark belirgin biçimde büyümüştür.
3. Aynı kademelerde PZEM de pens değerinden uzaklaşmıştır; dolayısıyla PZEM kusursuz gerçek değer (ground truth) olarak kabul edilemez.
4. PF gözlemleri maksimum, ara ve düşük kademelerde sırasıyla 1.00, 0.85 ve 0.47'dir. PF düşüşü ile ölçüm farklarının artışı birlikte görülmüştür.
5. Bu veri, dimmerin oluşturduğu faz kesmeli/bozulmuş akım biçiminin ölçüm zincirlerinin sonuçlarını etkileyebileceği hipotezini destekler. Ancak PF tek başına neden olarak kanıtlanmamıştır.
6. UT200B+ için bu deneydeki faz kesmeli dalga biçiminde ölçüm doğruluğunu bağımsız olarak doğrulayan bir referans bulunmamaktadır. Pens okumaları da mutlak gerçek değer kabul edilmemelidir.

## 5. Deneyin neden kapatıldığı

Dimmer ayarı, yükün akımını düşürürken akım dalga biçimini de değiştirir. Bu nedenle gözlenen sapma yalnızca akım seviyesine bağlanamaz; PF ve dalga biçimi koşulları da aynı anda değişmektedir. Ayrıca pens okumaları zaman damgalı otomatik kayıt değildir.

Bu düzenekle katsayı alanı taramasına devam etmek, akım seviyesinin etkisi ile dalga biçimi etkisini birbirinden güvenilir biçimde ayırmayacaktır. Bu nedenle kullanıcı kararıyla dimmer deneyi sonlandırılmıştır: **“Dimmerla olmuyor bu iş.”**

## 6. Karar ve kapsam

- Dimmer ile katsayı alanı taraması kapatıldı.
- Dimmer verileri normal şebeke/saf sinüs kalibrasyon verilerine eklenmeyecek.
- V1.1 YAML değiştirilmedi.
- V1.1 katsayısı 27.59 olarak korunuyor.
- Bu deneyden yeni katsayı, katsayı geçiş noktası veya doğruluk iddiası çıkarılmayacak.
- Raporun sonucu, dimmer altında PZEM, SCT/ADS1115 ve pens ölçümlerinin farklılaştığına dair sınırlı gözlemdir.

## 7. Kaynak ve sınırlamalar

- Kaynak Home Assistant dosyası: `history (5).csv` (422 satır; bu raporda kullanılan PZEM akım, PF, gerilim, SCT akım ve olay kayıtları).
- Görsel kayıtlar: 2026-11-21 tarihli Home Assistant grafik ekran görüntüleri.
- UT200B+ pens okumaları: kullanıcı tarafından bildirilen 7.69 A, 6.37 A ve 3.29 A.
- Bu raporda pens okumalarının zaman damgası veya cihazdan otomatik alınmış ham kayıt bulunmamaktadır.
- Deney, elektriksel ölçüm laboratuvarı doğrulaması değildir.
