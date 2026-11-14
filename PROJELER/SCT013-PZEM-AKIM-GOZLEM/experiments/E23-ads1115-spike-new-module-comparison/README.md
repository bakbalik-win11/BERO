# E23 — ADS1115 yüksüz sıçrama araştırması: yeni modül karşılaştırması

## HEDEF
Önceki ADS1115 enerjili-hat / ölçülen iletkende yüksüz gözleminde görülen yüksek akım sıçramalarının, aç/kapa mekanizması ve kodları aktif düzenden çıkarıldıktan ve yeni modül yapısı kurulduktan sonra devam edip etmediğini araştırmak. Yeni uzun kayıt, 2026-11-14 tarihli E19 istatistiksel kayıtla karşılaştırılacaktır.

## ARAŞTIRMA SORUSU
Ölçülen hatta aç/kapa yapılmadığı ve rölenin bu hatta bağlı olmadığı koşulda görülen ADS1115 sıçramaları, aç/kapa mekanizması/kodları kaldırılmış yeni modül yapısında da görülüyor mu?

Kullanıcı bildirimi:
- Önceki gözlem hattında aç/kapa yapılmıyor.
- Röle bu hatta bağlı değil.
- Aç/kapa başka bir ESP üzerinden yapılıyor; ADS1115'in bulunduğu ESP ile aynı cihaz değil.
- Kullanıcı aç/kapa sesini duyduğunu ve parazit olasılığından şüphelendiğini belirtti.
Bu açıklamalar test bağlamı olarak kullanıcı bildirimidir; parazitin fiziksel mekanizmasını tek başına kanıtlamaz.

## ÖNCEKİ KAYIT — KARŞILAŞTIRMA BASELINE'I
Kaynak rapor: [E19 2026-11-14 istatistiksel raporu](../../logs/ads1115/2026-11-14-E19-energized-no-load-statistical-report.md).
Ek yorum: [E19 sıçrama nedeni yeniden değerlendirmesi](../../logs/ads1115/2026-11-14-E19-spike-cause-reassessment.md).

- ADS1115 sayısal kayıt: n=1.669.
- 0,005 A ve altı: n=1.592 (%95,39), ortalama 0,00122955 A, medyan 0,00128425 A, örnek SD 0,00028426 A.
- 0,040 A ve üzeri: 72 kayıt (%4,31), medyan 0,046599 A, ortalama 0,051456 A.
- Maksimum: 0,353055 A.
- Eski CSV'deki HA switch state geçişleriyle zamansal yakınlık, nedensellik kanıtı değildir. Kullanıcının yeni fiziksel açıklaması nedeniyle bu ilişki rölenin ölçülen hattı anahtarlaması şeklinde yorumlanmayacaktır.

## YENİ MODÜL DÜZENİ — PLAN
Kullanıcı kararı/bildirimi:
- Aç/kapa mekanizması ve ilgili kodlar mevcut düzenden çıkarılacak.
- Kodlar yenilenecek ve yeni modül yapısı oluşturulacak.
- Yeni modülle akşam uzun süreli kayıt alınacak.
- Yeni kayıt önceki E19 baseline'ıyla karşılaştırılacak.

Yeni modülün kesin ESP modeli, SCT modeli, ADS1115 gain/rate, bağlantılar, besleme/toprak düzeni, firmware sürümü ve YAML kimliği henüz bu protokolde belirlenmiş değildir. Fiziksel kurulum görüldüğünde gerçek değerler kaydedilecektir. Eski modülün ayrıntıları yeni modüle varsayımla aktarılmayacaktır.

## TEST KOŞULLARI
- Ölçülen iletken yüksüz olacak.
- Ölçülen hatta aç/kapa yapılmayacak; röle bu hatta bağlı olmayacak.
- Aç/kapa mekanizması yeni modülün aktif kodunda bulunmayacak.
- Gözlem süresi ve kayıt aralığı gerçek kayıt üzerinden yazılacak.
- CSV'nin state-change kaydı mı, düzenli örnek kaydı mı olduğu doğrulanacak.
- Ham CSV, firmware/YAML kimliği, cihaz logu ve zaman aralığı korunacak.
- ADS1115 giriş ortak-mod ve GND–VDD sınırları ile SCT sekonder bağlantı güvenliği doğrulanmadan enerjili ölçüm başlatılmayacak.

## KARŞILAŞTIRMA YÖNTEMİ
Yeni CSV'de, önceki raporla aynı metrikler hesaplanacak:
1. Sayısal kayıt sayısı, unavailable sayısı, süre ve timestamp boşlukları.
2. Ortalama, medyan, örnek SD, min, max, P95, P97.5 ve P99.
3. 0,005 A ve altındaki taban grubunun n, oran, ortalama, medyan ve SD'si.
4. 0,005 A üzerindeki örnekler ve 0,040 A üzerindeki sapmaların sayısı/oranı/dağılımı.
5. En yüksek sıçramalar ve mümkünse olay süresi/genliği.
6. Önceki ve yeni modülün donanım, firmware, ADS ayarı, ölçüm penceresi, yayın aralığı ve kablolama farkları.

Önceki E19 verisi ile yeni kayıt donanım/yazılım koşulları farklıysa doğrudan eşdeğer ölçüm gibi yorumlanmayacak; farklar açıkça belirtilecek. Home Assistant state-change CSV'si tek başına darbe genişliği veya gerçek darbe süresi vermeyebilir.

## DEĞERLENDİRME SINIRLARI
- Sıçramaların azalması/kaybolması yeni modül düzeniyle ilişkili farkı destekler; tek başına fiziksel nedeni kanıtlamaz.
- Sıçramaların sürmesi, ortak çevre/tesisat, besleme, toprak referansı, kablolama, analog giriş veya başka kuplaj olasılıklarının ayrı kontrollü testlerle incelenmesini gerektirir.
- Bu deneyde eşik, filtre veya ortalama ile sıçramalar gizlenmeyecek. Ölçüm zinciri değişiklikleri ayrı kaydedilecek.
- Sonuç görülmeden parazit kaynağı, donanım arızası veya yazılım hatası ilan edilmeyecek.

## DURUM
**PLANLANDI — araştırma yeni modül yapısıyla devam ediyor.** Önceki E19 uzun gözlem/istatistik oturumu kapalıdır; E23 yeni karşılaştırmalı araştırma kaydıdır. Yeni modülün fiziksel kurulumu, uzun kayıt, analiz ve sonuç henüz yapılmış değildir.

