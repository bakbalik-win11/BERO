# I007 / 15 W — Yüksüz taban ile düşük yük ayrışma deneyi

## Amaç

2026-11-06 CH1-1T uzun OFF oturumunda ölçülen yüksüz SCT dağılımının, aynı ölçüm zincirinde 15 W fiziksel yük çalışırken oluşan dağılımdan ayrışıp ayrışmadığını incelemek.

Bu deney K katsayısı eğitimi değildir. Amaç, fiziksel 0 A tabanı ile düşük akım koşulunun istatistiksel olarak ayırt edilebilirliğini değerlendirmektir.

## Referans OFF oturumu

- Oturum: [I007-2026-11-06-02](../../data/off-noise/sessions/2026-11-06-session-02-ch1-1t-off.md)
- CH1-1T katsayısız SCT medyanı: 0.009918 A
- MAD: 0.001950 A
- P95: 0.013439 A
- P99: 0.015288 A
- n=1,260; yaklaşık 21 dakika.
- Kaynak CSV SHA-256: `235ad89116f3d0a36205acafbe4eec1f29baa9043567e59f71b3d12835c45e74`.

Bu sayılar yalnız referans oturumun özetidir; cutoff eşiği değildir.

## Deney koşulları

- Fiziksel yük: 15 W lamba. Lambanın türü/etiket gücü ve bağlantı şekli oturum başında kaydedilecek.
- Ölçüm kanalı: CH1-1T, SCT013 30A/1V, GPIO32 / ADC1_CH4.
- Firmware, `sample_duration`, SCT yayın aralığı, K, ADC attenuation ve fiziksel CT yerleşimi OFF referansıyla aynı tutulacak.
- Deney sırasında firmware veya donanım parametresi değiştirilmez.
- Kullanıcı fiziksel yükü ON/OFF yaptığında gerçek zaman not edilir. UDP/SSR STATE tek başına fiziksel yük durumu kanıtı değildir.
- PZEM akım entity'sinin yeni timestamp'lerle güncellendiği ve güncel değer ürettiği deney başlamadan kontrol edilir. 2026-11-06 OFF CSV'sinde PZEM akım kaydı 16:13:12.898'de kesildiğinden, eski 0.000 A değeri bu testte referans kabul edilemez.

## Kayıt süresi ve akış

1. Ölçüm zinciri ve PZEM canlı güncellemesi kontrol edilir.
2. 15 W fiziksel yük açılır; gerçek ON zamanı not edilir.
3. SCT katsayısız CH1-1T çıktısı, PZEM akımı, PZEM gücü, gerilim, olay kaydı ve timestamp'ler birlikte kaydedilir.
4. Hedef kayıt süresi 30 dakikadır. En az 21 dakika kesintisiz kayıt, OFF referansıyla süre karşılaştırması için asgari hedeftir.
5. Yük kapatılır ve OFF sonrası geçiş de ham kayıtta tutulur.
6. Ham kayıt silinmez veya filtrelenerek üzerine yazılmaz.

## Analiz planı

OFF ve 15 W verileri ayrı gruplar olarak raporlanır. Her iki grupta:

- n, gerçek timestamp aralığı ve eksik kayıt sayısı;
- medyan ve MAD (ana sağlam merkez/yayılım);
- 1.4826×MAD;
- P05, P25, P75, P95, P99;
- minimum/maksimum;
- dakika veya sabit zaman dilimi bazında medyan ve MAD;
- 0.015 A üzerindeki örnek oranı (yalnız karşılaştırma metriği; eşik olarak değil);
- dağılım örtüşmesi ve OFF/15 W ayrışması.

Ortalama ve standart sapma yalnız betimleyici yardımcı istatistiklerdir; medyanın yerine eğitim merkezi olarak kullanılmaz. Uç değerler ham veriden silinmez.

## Önceden belirlenmiş yorum sınırları

- 15 W medyanının OFF medyanından büyük olması tek başına ayrışma kanıtı değildir.
- 15 W dağılımının OFF dağılımıyla örtüşme miktarı ve zaman içindeki kararlılığı birlikte değerlendirilir.
- Ayrışma zayıfsa bu sonuç saklanır; eşik zorlanarak seçilmez.
- Bu tek 15 W oturumu, farklı gün/tekrar koşullarında doğrulama yapılmadan genellenmez.
- Bu deneyden doğrudan K= PZEM/SCT eğitim katsayısı çıkarılmaz; katsayı eğitimi kendi sabit yük ON penceresi protokolünü izler.

## Durum

**PLANLANDI — henüz çalıştırılmadı.** 15 W deneyinin sonucu veya kabul eşiği önceden varsayılmamıştır.
