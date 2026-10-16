# SSR Test Logları

Bu klasör, ESP32-C3 SSR kontrolüyle ilgili log ve doğrulama kayıtları içindir.

Kayıtlarda şu aşamalar birbirinden ayrı tutulmalıdır:
1. Komut gönderildi.
2. GPIO6 yazılım durumu değişti.
3. SSR çıkışı ölçümle doğrulandı.
4. Bağlı yükün durumu bağımsız olarak doğrulandı.

Mevcut ESPHome/DS3231 logu SSR'nin fiziksel çıkışını veya bağlı yükün açılıp kapandığını kanıtlamaz. Doğrulanmış bir SSR anahtarlama logu elde edildiğinde tarihli dosya olarak buraya eklenmelidir.
