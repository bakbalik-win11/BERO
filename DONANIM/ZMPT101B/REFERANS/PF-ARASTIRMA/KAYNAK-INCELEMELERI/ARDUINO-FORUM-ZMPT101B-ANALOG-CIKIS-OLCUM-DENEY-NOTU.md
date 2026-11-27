# Arduino Forum Deney Notu — ZMPT101B Analog Çıkışını Okuma

- Kayıt tarihi: 2026-11-22
- Kaynak: [Arduino Forum — Problem with translate the values of voltage sensor ZMPT101B](https://forum.arduino.cc/t/problem-with-translate-the-values-of-voltage-sensor-zmpt101b/491534)
- Konu tarihi: 15–16.11.2017; sonradan eklenen yorum: 29.01.2019
- Belge türü: Kullanıcı deneyimi ve forum teknik tartışması. Üretici dokümanı veya kontrollü laboratuvar raporu değildir.

## 1. Konunun özeti

Konu sahibi, potansiyometreli ZMPT101B modülünü Arduino Uno ile kullanarak 220 V AC şebekenin tepe-tepe değerini elde etmeye çalışıyor. Seri monitördeki değerlerin beklediği gibi ilerlememesi üzerine kodunu ve osiloskop görüntülerini paylaşıyor.

Tartışma, BERO'nun kartı teslim aldığında yapacağı ilk analog çıkış kontrolleri açısından yararlı dört konu ortaya çıkarıyor:
- Analog çıkışın DC ofsetinin görünür olması için osiloskopta DC coupling kullanılması.
- Potansiyometrenin çıkış genliğini değiştirmesi ve aşırı ayarda kırpılma/flat-top oluşabilmesi.
- Örneklerin zaman bilgisi olmadan seri monitörden izlenmesinin dalga biçimini değerlendirmek için yeterli olmaması.
- Kodda maksimum/minimum takibinin ve örnekleme zamanlamasının doğru kurulması.

## 2. Kod incelemesinden çıkan somut hatalar

### 2.1. `max()` fonksiyonu geçmiş örneklerin maksimumunu bulmaz

Konu sahibinin ilk kodundaki:

```cpp
sensmax = max(sensorvalue, 600);
sensmin = max(sensorvalue, 50);
```

satırları, mevcut `sensorvalue` ile sabit 600 veya 50 değerini karşılaştırır. Önceki örnekleri saklayıp bir ölçüm penceresinin maksimum/minimum değerini takip etmez. Ayrıca ikinci satırda minimum aramak için `max()` kullanılması da mantıksal olarak yanlıştır.

Pencere içinde tepe-tepe ölçümü yapılacaksa başlangıçta pencere maksimumu düşük, minimumu yüksek bir başlangıç değeriyle kurulmalı; her yeni örnekte ayrı ayrı güncellenmeli ve pencere sonunda `Vpp = max - min` hesaplanmalıdır. Bu yaklaşım yalnızca tepe-tepe genlik gözlemidir; RMS veya gerçek güç faktörü hesabının yerine geçmez.

### 2.2. `delay(0.000001)` mikro saniyelik bekleme sağlamaz

Arduino `delay()` fonksiyonunun parametresi milisaniye cinsinden tamsayıdır. Ondalıklı `0.000001` değeri tamsayıya dönüştüğünde sıfır olur; yani kod fiilen `delay(0)` çağırır. Mikro saniye düzeyinde bekleme gerekiyorsa farklı bir zamanlama mekanizması gerekir; fakat BERO örnekleme tasarımında sabit bekleme varsaymak yerine gerçek örnek zaman damgaları ölçülmelidir.

### 2.3. Seri monitör ölçüm zamanlamasını bozabilir

Forum katılımcısı, 9600 baud seri iletişim ve her örneği yazdırma yükü nedeniyle örneklerin seyrekleşebileceğini; kendi değerlendirmesinde bu kod düzeninin yaklaşık 200 ölçüm/saniyeyi aşamayacağını belirtir. Bu sayı Arduino Uno, seri yazdırma biçimi ve o test koduna ait bir forum değerlendirmesidir; BERO veya ESP32 için genel hız sınırı değildir.

Önemli ders: seri porta her örneği yazdırarak örnekleme hızını ölçmemeliyiz. Önce örnekleri bellekte veya tamponda zaman damgasıyla toplamak, ölçüm penceresi sonunda özet/hız bilgisini yazdırmak daha doğru olacaktır.

## 3. Analog çıkış ve osiloskop gözlemi

Forumdaki kart için verilen açıklamaya göre:
- AC giriş yokken çıkış yaklaşık VCC/2 DC seviyesinde olabilir.
- AC uygulandığında sinyal bu DC ofsetin çevresinde salınır.
- Potansiyometre AC salınımın genliğini değiştirir.
- Osiloskop AC coupling konumunda DC bileşeni kaldırır; bu nedenle sinyalin gerçek DC ofsetini görmek için DC coupling kullanılmalıdır.

Bu açıklama yaygın modül topolojisine ilişkin forum katılımcısı gözlemidir. BERO'nun satın aldığı kartın aynı devreye sahip olduğu henüz fiziksel olarak doğrulanmadı. Kart revizyonu ve ölçüm sonucu esas alınacaktır.

### Kırpılma / flat-top

Forumda bir osiloskop görüntüsünde dalga tepesinin düzleşmesi, potansiyometre ayarının fazla yüksek olabileceği veya analog katın/trafo girişinin sınırlarına ulaşması ihtimalleriyle tartışılmıştır. Bu yorumlar kesin teşhis değildir.

BERO kontrolünde:
1. Potansiyometre en düşük genlik konumundan başlanarak küçük adımlarla artırılmalı.
2. Dalga biçiminin iki tepesi ve tabanı gözlenmeli.
3. Düzleşme, asimetri veya ani bozulma görülürse ayar geri alınmalı.
4. ADC besleme ve giriş sınırları aşılmamalı; ADC girişinde kırpılma ayrıca kontrol edilmeli.

## 4. BERO için uygulanabilir deney kontrol listesi

- [ ] Kartın PCB ön/arka yüzü, üzerindeki entegre işareti, pin sırası ve bağlantı etiketleri fotoğraflanacak.
- [ ] İlk test, şebekeden galvanik olarak izole edilmiş ve düşük gerilimli AC kaynakla yapılacak.
- [ ] Osiloskop DC coupling konumunda kullanılacak; önce kart GND referansı ve prob bağlantısı düşük gerilimli test düzeninde doğrulanacak.
- [ ] AC giriş yokken OUT–GND DC seviyesi ölçülerek VCC/2 varsayımı sınanacak.
- [ ] AC giriş varken OUT dalgasının ofseti, tepe-tepe genliği, simetrisi ve frekansı kaydedilecek.
- [ ] Potansiyometre ayarı boyunca kırpılma/flat-top başlangıcı gözlenecek; ADC için güvenli genlik payı bırakılacak.
- [ ] ADC örnekleri seri porta tek tek yazdırılmadan zaman damgasıyla toplanacak; gerçek örnekleme hızı ölçülecek.
- [ ] Ham veri üzerinde ortalama/DC ofset, RMS ve gerekiyorsa tepe-tepe değer ayrı ayrı hesaplanacak.
- [ ] PZEM ile yapılacak RMS karşılaştırması yalnızca genlik ölçeği kontrolü olarak kullanılacak; faz gecikmesi bu karşılaştırmayla doğrulanmış sayılmayacak.

## 5. Güvenlik ve kaynak sınırları

Bu forumdaki osiloskop bağlantı tarifleri, BERO'nun şebeke testinde doğrudan uygulanacak bağlantı talimatı değildir. 230 V şebeke ölümcül tehlike taşır. Osiloskop probunun toprak klipsi, cihazın koruma toprağı ve modülün şebeke tarafı arasındaki ilişki bilinmeden şebekeye bağlanmamalıdır. İlk inceleme yalnızca güvenli, galvanik olarak izole düşük gerilimli kaynakla yapılmalıdır.

Konu içindeki bir katılımcı, tek beslemeli op-amp devresinin negatif yarım dalgayı kırpabileceğine ilişkin farklı bir devre yorumu da sunar. Bu yorum forumdaki şemaya ve katılımcının varsayımına dayanır; tüm ZMPT101B kartları için geçerli kabul edilemez. BERO kartında bu ihtimal dalga biçimi gözlemi ve kart devresi incelenerek sınanacaktır.

Forumda geçen 220 V RMS ile tepe-tepe dönüşüm önerisi de yalnızca ideal sinüs varsayımında anlamlıdır. BERO'da kalibrasyon sabiti olarak doğrudan kullanılmayacak; gerçek modül çıkışı ve ölçüm zinciri deneyle kalibre edilecektir.

## 6. Sonuç ve BERO kararı

Bu kaynak, ZMPT101B modülünü ADC'ye bağlamadan önce analog çıkışın DC ofsetini ve kırpılma durumunu osiloskopla görmenin önemini destekliyor. Ayrıca yazılım örnekleme hızının seri monitör çıktısından çıkarılamayacağını gösteriyor.

**Karar:** ZMPT101B kartı geldiğinde ilk deney; düşük gerilimli izole AC kaynak, osiloskop DC coupling ve potansiyometre boyunca dalga biçimi gözlemi olacaktır. Bu aşama tamamlanmadan ADS1115 ile RMS/PF yazılımına geçilmeyecek.

## Durum

- Kaynak ve teknik değerlendirme depoya kaydedildi.
- BERO kartı üzerinde bu nottaki deneyler henüz yapılmadı.
- Bu nottaki forum gözlemleri BERO ölçüm sonucu veya kart performans garantisi değildir.
