# Yüksüz ofset ve gürültü tabanı

## Amaç
Hatta akım yokken SCT/analog ön uç ve ESP32 ADC verisinin ofsetini, gürültüsünü ve zaman içindeki değişimini gözlemlemek. Veriler grafiklenerek yüksüz durumdaki davranış incelenecek.

## Sistem beslemesi
PZEM ve ölçüm/kontrol ESP kartları ölçülen hattan beslenmez; kendi beslemeleri ayrıdır. Deney kurulumu yapılırken bu özellik korunur ve gerçek bağlantı düzeni deney metadata kaydına işlenir.

## Başlangıç hipotezi
HİPOTEZ — bu projede deneyle doğrulanmadı; sonuç gibi raporlanamaz.

## Prosedür
1. Donanım kurulumu henüz tamamlanmadığından, fiziksel ölçüm ancak kurulumdan sonra yapılır. Güvenlik ve bağlantılar kontrol edilir.
2. Ölçülen hatta akım olmadığı durum doğrulanır ve bu durum deney kaydına yazılır.
3. Sabit yapılandırmayla ADC verisi alınır. **30 saniye asgari başlangıç referansıdır, üst sınır değildir.** Daha uzun kayıt; gerekirse saatler süren kayıt, deney sırasında kararlaştırılabilir. Kesin süre şimdiden belirlenmiş değildir.
4. Ham veri saklanır ve zaman ekseninde grafiklenir. sample_count, ortalama, min/max ve ofset çıkarılmış gürültü RMS'i hesaplanır; mümkünse zaman içindeki değişim de incelenir.
5. Kullanılan firmware/donanım kimlikleri, örnekleme ayarları, gerçek kayıt süresi ve veri yolu metadata ile sonuç dosyasına bağlanır.

## Güvenlik
hardware/safety-checklist.md tamamlanmadan şebeke deneyi yapılmaz. Bağlantı değişiklikleri enerji kesikken yapılır.

## Kabul ölçütü
Donanım ve yazılım kimlikleri, gerçek ölçüm süresi, ham veri ve grafik/özet sonuç birbiriyle ilişkilendirilebilir olmalıdır. Ölçülmeyen sonuç yazılmaz. Tek bir yüksüz kayıt, tüm koşullar için kesin gürültü veya düşük akım sınırı kanıtı sayılmaz.
