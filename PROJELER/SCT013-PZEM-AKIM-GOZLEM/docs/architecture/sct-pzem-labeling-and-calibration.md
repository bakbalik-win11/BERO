# SCT–PZEM Kararlılık Etiketleme ve Kalibrasyon Hedefi

**Durum:** Hedef mimari notu — uygulama/firmware henüz tamamlanmadı.  
**Kapsam:** T001 sırasında kullanıcının açıkladığı proje hedefini ve ileride geliştirilecek veri işleme akışını kaydeder. Bu belge bir deney sonucu veya uygulanmış yazılım iddiası değildir.

## Amaç

Üç ayrı SCT örnekleme düğümünden mümkün olduğunca az kayıpla ham/anlık gerilim örnekleri toplamak; SSR olay paketleri ve PZEM/SCT kararlılık bilgileri üzerinden bu verileri etiketlemek; Python ile etiketlenmiş veri kümesi oluşturup her SCT için kalibrasyon katsayısı ve (f(x)) modelini geliştirmek.

## Hedef iş bölümü

- **ESP32-C3 SuperMini:** SSR anahtarlama ve zamanlama düğümü; ON/OFF olaylarını paket bilgisiyle yayımlar. Mevcut paket biçimi: `BERO_EVT,BOOT_ID=XXXXXXXX,EVENT_ID=N,STATE=ON|OFF`.
- **SCT örnekleme düğümleri:** 2 × ESP32-WROOM-32D ve 1 × ESP32-WROOM-32E. Her düğüm SCT sinyalinin ham/anlık gerilim örneklerini hızlı ve düşük kayıpla toplar ve veriyi Home Assistant'a aktarır. Bu düğümlerde ilk aşamada akım/RMS hesabı yapılması hedeflenmiyor.
- **PZEM düğümü:** PZEM ölçüm bilgisi ve ilgili paket/olay bağlamı, PZEM'in kararlı olduğu anları belirleme sürecinde kullanılacak.
- **Python (Mac Mini/PC):** Ham SCT verilerini, olay paketlerini ve kararlılık etiketlerini bir araya getirme; istatistiksel analiz ve algoritma geliştirme; kalibrasyon katsayıları ve SCT başına (f(x)) modelini çıkarma.
- **Home Assistant:** ESP düğümlerinden gelen verilerin aktarılacağı hedef sistemdir; temel hesaplama ve modelleme burada değil Python tarafında yapılır.

## Etiketleme yaklaşımı

- Zaman damgasına dayalı eşleştirme, hedef yaklaşımın ana yöntemi olarak tarif edilmedi. Kullanıcı, **paket bilgisinin** kullanılacağını ve PZEM'in kararlı olduğu anlar ile SCT'nin kararlı olduğu anların etiketleneceğini belirtti.
- Kararlılık tanımı, algoritması ve istatistiksel eşikleri henüz tasarlanacak; bunlar şimdiden belirlenmiş değildir.
- Paket bilgisi olayın/çalışma durumunun bağlamını sağlar. Bir ölçümün kararlı sayılması, geliştirilecek algoritma ve istatistiksel ölçütlerle kararlaştırılacaktır.
- Python tarafında kararlılık etiketleriyle işaretlenmiş SCT ham verisi oluşturulacaktır.

## Kalibrasyon deneyleri

Aynı iletkenin SCT içinden geçirilme sayısı ayrı deneylerde 1 sarım, 2 sarım ve 4 sarım olarak değiştirilecektir. Bu deneylerden gelen etiketli örnekler, SCT ölçüm davranışını modellemek ve her sensör için katsayı/(f(x)) ilişkisini geliştirmek amacıyla kullanılacaktır. Henüz deney verisi veya doğrulanmış model yoktur.

## Açık kalanlar

1. Paket bilgisinin SCT örnekleme düğümlerine nasıl ulaştırılacağı ve örneklerle nasıl ilişkilendirileceği kesinleştirilecek.
2. Mevcut ADR-006'da yer alan ilk aşamada SCT ESP'lerinin UDP olaylarını dinlememesi ve Python'da sonradan ilişkilendirme yaklaşımı bu hedef notuyla birlikte gözden geçirilecek; bu not tek başına ADR-006'yı değiştirmez.
3. PZEM ve SCT kararlılığının algoritmik/istatistiksel tanımları geliştirilecek.
4. Home Assistant'a aktarılacak veri şeması, örnekleme hızı, tamponlama ve kayıp ölçüm yöntemi belirlenecek.
5. Kalibrasyon için referans ölçüm, model biçimi, hata ölçütü ve doğrulama prosedürü daha sonra tanımlanacak.

## Kayıt ilkesi

Bu belge kullanıcının açıkladığı hedef mimariyi kaydeder. Henüz yazılmamış SCT firmware'ini, yapılmamış deneyleri, belirlenmemiş algoritmaları veya doğrulanmamış kalibrasyon sonuçlarını mevcutmuş gibi göstermez.
