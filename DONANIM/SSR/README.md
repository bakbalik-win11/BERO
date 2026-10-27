# SSR — Donanım Referansı

Bu kayıt, BERO'da bulunan dört kanallı SSR kartını tanımlar. Eski ESP32-C3 test düzeneğine ilişkin kontrolcü bilgileri tarihsel nottur; yeni proje için GPIO seçimi henüz yapılmadı.

## Modül ve elektriksel bilgiler

Aşağıdaki değerler kullanıcının verdiği modül bilgileri ve fotoğraf açıklamasıdır; bu oturumda bağımsız elektriksel test yapılmamıştır.

- **Kanal sayısı:** 4
- **Üretici işareti/beyanı:** OMRON
- **İzolasyon:** Fototriyak
- **Anahtarlama:** Zero-cross
- **Kontrol girişi — LOW:** 0–0,5 V (SSR kapalı)
- **Kontrol girişi — belirsiz bölge:** 0,5–2,5 V
- **Kontrol girişi — HIGH:** 2,5–20 V (SSR açık)
- **Çıkış yük gerilimi (kanal başına):** 75–264 V AC, 50/60 Hz
- **Nominal çıkış yükü:** 100–240 V AC, 50/60 Hz
- **Yük akımı (kanal başına, bildirilen):** 0,1–2 A
- **Yük tipi:** Genel amaçlı

Kart fotoğrafındaki SSR gövdelerinin tam model kodu güvenilir biçimde okunamadığından G3MB-202P gibi belirli bir model kesinleştirilmemiştir. Omron G3MB serisi veri sayfası şimdilik yalnızca olası karşılaştırma kaynağıdır; fiziksel modelle eşleştiği varsayılmamalıdır.

## Önceki BERO test düzeneği

- Önceki notlarda kontrolcü ESP32-C3 olarak geçer.
- Önceki notlarda SSR kontrol pini GPIO6 olarak belirtilmiştir.
- Bu tarihsel pin notu, yeni projede GPIO6 kullanılacağı veya SSR çıkışının çalıştığının kanıtı değildir.

## Kullanım ve güvenlik notları

- 0,5–2,5 V kontrol giriş aralığı belirtilen belirsiz bölgedir; girişin bu aralıkta kalmasına izin verilmemelidir.
- Bildirilen 2 A/kanal değeri, kart üzerindeki soğutma, PCB yolları, ortam sıcaklığı ve eşzamanlı kanal kullanımı değerlendirilmeden sürekli çalışma garantisi olarak yorumlanmamalıdır.
- Şebeke gerilimi bulunan çıkış tarafını MCU, USB, breadboard ve düşük gerilimli kablolardan fiziksel olarak ayır; uygun muhafaza, sigorta ve izolasyon düzeni kullan.
- Şebeke bağlantısı ve yük testleri yetkin kişi tarafından, enerji kesilerek ve uygun ölçüm/güvenlik ekipmanıyla yapılmalıdır.
- SSR'nin giriş akım gereksinimi, aktif seviyesi ve gerçek çıkış davranışı yük bağlanmadan önce kontrollü düşük gerilim testi ve ilgili model/veri sayfası ile doğrulanmalıdır.
