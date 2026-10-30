# E08 sonuçları

Durum: E08 Aşama 2 açıldı; önce mevcut E00B firmware'iyle düşük hızlı yük gözlemi yapılacak. Fiziksel ölçüm henüz yapılmadı.

Aşamalar: yüksüz uzun okuma; 100 W matrisi; 150 W ve 8,5 W LED matrisleri; aç-kapa testi.

Veri ve bulgular: henüz yok. Kararlılık eşiği ve gerekli pencere sayısı belirlenmedi.

## HEDEF / LOG / SONUÇ

### HEDEF
SCT sinyalini yüksüz, farklı yük/tur ve aç-kapa koşullarında karakterize etmek.

### LOG
- **Durum:** PLANLANDI / YAPILMADI; fiziksel ölçüm ve sonuç verisi yok.
- Gerçek donanım/yazılım ve uygulanan ayarlar: henüz kayıt yok.
- Veri yolu, süre, örnek sayısı ve gözlemler: henüz veri yok.
- Yapılmayan işlemler: fiziksel deney, firmware derlemesi ve ölçüm yapılmadı.

### SONUÇ
Henüz ölçülmedi; bu dosya deney başarısı veya fiziksel bulgu kanıtı değildir.

## 2026-10-30 — Aşama 2 yaklaşımı netleştirildi

Kullanıcı kararı: Yeni yüksek hızlı firmware'e şu aşamada geçilmeyecek. Mevcut E00B kodu değiştirilmeden 100 W akkor yük altındaki sensör yayınları gözlenecek. Bu kayıt, 1 saniyelik yayın aralığında sinyalin/yük davranışının farklı alanlarını görmeye yönelik düşük hızlı bir gözlem olarak değerlendirilecek. Daha sonra ayrı hızlandırma testlerine geçilecek. Bu aşama 1/2/2,5 kS/s örnekleme hedeflerinin gerçekleştirildiği anlamına gelmez. Gerçek veriler alındığında sonuç, sınırlamalar ve sonraki adım kanıta dayanarak yazılacaktır.


## 2026-10-30 — Aşama 2 / 100 W akkor testi açıldı

### HEDEF
SCT013-030 ve ESP32 dahili ADC zincirinin 100 W akkor yük altındaki davranışını gözlemek; 1/2/4 iletken turu ile 1.000/2.000/2.500 örnek/s hedeflerini karşılaştırmak. Her pencerenin aynı örneklerinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanacak.

### LOG
- Test kaydı açıldı; fiziksel ampul testi henüz yapılmadı.
- Yük: 100 W akkor ampul (kullanılacak ampulün etiketi/gerçek gücü uygulama sırasında kaydedilecek).
- SCT: öncelikli SCT013-030 (30 A / 1 V).
- Matris: 1, 2, 4 iletken turu × 1.000, 2.000, 2.500 örnek/s hedefleri.
- İlk kayıt/deneme koşulu: 1 tur × 1.000 örnek/s; sonraki matris koşulları bu ilk kayıt doğrulandıktan sonra yürütülecek.
- Mevcut E00B firmware'i 1 saniyelik sensör yayınları yapar; E08'in yüksek hızlı ham ADC edinimini gerçekleştirmez. E08 için ayrı yüksek hızlı edinim firmware'i hazırlanmalı ve gerçek örnekleme hızı ölçülmelidir.
- Gerçek kart/pinout, 100 W ampul ve CT'nin yalnız tek yalıtılmış iletkeni çevreleyecek şekilde yerleşimi, bağlantı öncesi fiziksel olarak doğrulanmalıdır. Şebeke bağlantısı yalnız yetkin kişi tarafından, uygun muhafaza/koruma ile yapılmalıdır.
- Gerçek örnekleme hızı, kayıt süresi, örnek sayısı, ADC pinleri ve veri dosyası henüz belirlenmedi; ölçümden sonra kaydedilecek.

### SONUÇ
Test planı açıldı; henüz fiziksel ölçüm, firmware derlemesi veya veri kaydı yok. Mevcut E00B YAML'ı kullanarak E08 örnekleme matrisi yapılmış sayılamaz. İlk teknik iş, E08 için yüksek hızlı ADC firmware'ini hazırlayıp derleme/gerçek hız doğrulamasını sağlamaktır. Kararlılık eşiği ve gerekli ardışık pencere sayısı önceden belirlenmeyecek.
