# Arduino Forum Deney Notu — ZMPT101B ile Düşük AC Gerilim Ölçümü

- Kayıt tarihi: 2026-11-22
- Kaynak: [Arduino Forum — ZMPT101B problem with measure AC voltage](https://forum.arduino.cc/t/zmpt101b-problem-with-measure-ac-voltage/1219148)
- Konu tarihi: 02–03.02.2024
- Donanım/yazılım: Arduino Uno, ZMPT101B modül, `ZMPT101B.h` kütüphanesi, 0–250 V AC ayarlı ototransformatör
- Belge türü: Kullanıcı deneyimi ve forum tartışması; üretici veri sayfası veya kontrollü laboratuvar raporu değildir.

## 1. Kullanıcının bildirdiği sorun

Konu sahibi, ayarlı ototransformatör çıkışını ZMPT101B modülüne bağladığında 5 V AC üzerindeki değerleri doğruya yakın okuduğunu; gerilimi düşürdüğünde yaklaşık 4,8 V civarında takılma yaşadığını bildiriyor. Sensörün AC giriş bağlantısı çıkarıldığında yazılım 0,0 V gösterirken, kablo yeniden bağlanıp ototransformatör açıldığında 4,8 V civarında değer oluştuğunu belirtiyor.

Paylaşılan kod:
- `ZMPT101B voltageSensor(A0, 50.0)`
- `SENSITIVITY 500.0f`
- `voltageSensor.getRmsVoltage()`
- Sonucu seri porta yazdırma ve 1 saniye bekleme.

Konu sahibi daha sonra hassasiyeti 500'den 250'ye indirdiğinde gösterimin 4,8 V'tan 2,4 V'a düştüğünü söylüyor. Bu, hassasiyet parametresinin yazılım sonucunu doğrudan ölçeklediğini gösteren kendi gözlemidir; sensörün fiziksel giriş-çıkış davranışını tek başına açıklamaz.

## 2. Forum yanıtlarından çıkan teknik noktalar

- Katılımcılar doğru kalibrasyon yapılıp yapılmadığını sorguluyor.
- Kullanılan kütüphanenin çok düşük AC gerilimleri ölçmeye uygun olup olmadığı soruluyor.
- Modülün kendisinin düşük gerilim aralığında yeterli çıkış üretip üretmediği ayrı bir olasılık olarak belirtiliyor.
- Arduino Uno ADC'sinin de kalibre edilmesi gerektiği ifade ediliyor.
- Kullanıcıya kütüphanenin talimatlarındaki kalibrasyon örneğini çalıştırıp çalıştırmadığı soruluyor; paylaşılan yazışmada bu kalibrasyonun gerçekten yapıldığına dair doğrulama yok.
- Bir katılımcı, ZMPT101B ile %0,04 doğruluk beklenmemesi gerektiğini söylüyor. Bu genel forum görüşüdür; BERO için ölçülmüş doğruluk sınırı değildir.

## 3. BERO açısından yorum

Bu tartışmanın asıl katkısı, düşük gerilimdeki ölçüm hatasını tek bir bileşene yüklemememiz gerektiğini hatırlatmasıdır. Ölçüm zincirini ayrı ayrı incelemeliyiz:

1. **Sensör ve analog ön uç:** Düşük giriş geriliminde transformatör ve op-amp çıkışı yeterli genlikte mi? Gürültü, ofset veya eşik benzeri davranış var mı?
2. **ADC:** ADC'nin giriş aralığı, çözünürlüğü, referans/ölçek doğruluğu ve düşük genlikteki gürültüsü sonucu sınırlıyor mu?
3. **Yazılım:** RMS hesabı, DC ofset çıkarımı, örnekleme penceresi ve hassasiyet katsayısı doğru mu?
4. **Kalibrasyon referansı:** Bağımsız AC voltmetre ile aynı noktada ve aynı anda karşılaştırma yapılıyor mu?

Konu sahibinin 4,8 V'ta sabitlenme gözlemi, BERO modülünün de 4,8 V altını ölçemeyeceği anlamına gelmez. Farklı PCB revizyonu, besleme, op-amp, pot ayarı, ADC ve yazılım aynı davranışı üretmeyebilir.

## 4. BERO için deney planına eklenen kontroller

- [ ] ZMPT101B kartı teslim alındığında önce PCB revizyonu, op-amp işareti, besleme ve pinler kaydedilecek.
- [ ] Düşük gerilim deneyi yalnızca güvenli, galvanik olarak izole AC kaynakla yapılacak.
- [ ] Gerilim birkaç kademede artırılıp azaltılacak; her kademede referans voltmetre değeri ve ADC ham örnekleri birlikte kaydedilecek.
- [ ] Aynı gerilim seviyesine hem yükselerek hem düşerek gelindiğinde sonuçlar karşılaştırılacak; histerezis veya kararsızlık olup olmadığı incelenecek.
- [ ] OUT sinyalinin DC ofseti ve AC genliği osiloskopla gözlenecek; düşük seviyede dalga biçimi gürültü tabanına yaklaşıyor mu kontrol edilecek.
- [ ] Yazılım RMS sonucu, ham örneklerden bağımsız çevrimdışı hesaplanan RMS ile karşılaştırılacak.
- [ ] Sensör/analog kat, ADC ve yazılım katsayısı ayrı ayrı kalibre edilecek; tek bir hassasiyet katsayısı bütün hataları gizlemek için kullanılmayacak.
- [ ] Düşük gerilimde hata büyüyorsa ölçüm aralığı ve kullanılabilir alt sınır deneysel olarak belirlenecek; forumdaki 4,8 V değeri BERO eşiği olarak kopyalanmayacak.

## 5. Kaynak sınırları ve güvenlik

Forum başlığında kullanıcı ototransformatör kullandığını söylüyor. Ototransformatör galvanik izolasyon sağlamaz. Bu nedenle forumdaki kurulum BERO için güvenli test yöntemi olarak örnek alınmayacaktır. Şebeke ile bağlantılı deneylerde osiloskop toprak klipsi ve prob izolasyonu ayrıca değerlendirilmeden bağlantı yapılmamalıdır. İlk testler güvenli, galvanik olarak izole düşük gerilimli AC kaynakla yürütülecektir.

Forum yazışması, 4,8 V altındaki davranışın nedenini kesinleştirmiyor. Kalibrasyonun tamamlandığı, Arduino ADC'sinin doğrulandığı veya modülün alt ölçüm sınırının ölçüldüğü gösterilmiyor.

## 6. Sonuç

**BERO kararı:** ZMPT101B kartının yalnızca 230 V civarındaki nominal kullanımını değil, düşük AC giriş seviyelerindeki davranışını da karakterize edeceğiz. Alt ölçüm sınırı; sensör çıkışı, ADC ham verisi, yazılım RMS hesabı ve bağımsız referans ölçüm birlikte incelenerek belirlenecek.

## Durum

- Kaynak ve teknik değerlendirme depoya kaydedildi.
- BERO kartı üzerinde düşük gerilim testi henüz yapılmadı.
- 4,8 V değeri yalnızca forum kullanıcısının sistemine ait gözlemdir; BERO için eşik veya spesifikasyon değildir.
