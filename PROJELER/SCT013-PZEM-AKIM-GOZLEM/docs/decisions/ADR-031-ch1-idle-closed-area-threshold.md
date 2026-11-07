# ADR-031 — CH1 yüksüz kapalı alan eşiği

- **Durum:** KABUL EDİLDİ
- **Tarih:** 2026-11-07
- **Bağlam:** Fiziksel olarak akım bulunmayan hatta CH1'in yüksüz SCT çıktısından kapalı alan sınırı seçilmesi.
- **Karar sahibi:** Kullanıcı

## Karar

CH1 için kapalı alan üst sınırı **0,24 A** olarak seçilir. Bu sınır, K=24.22 uygulanmış CH1 akım entity'si üzerinden ifade edilir. Aynı eşik ham SCT göstergesiyle yaklaşık **0,00991** değerine karşılık gelir (0,24 / 24,22).

- **0–0,24 A:** Kapalı alan.
- **0,24 A ile ilk güvenilir akım okuması arasındaki bölge:** Hesaplanmadı alanı.
- **İlk güvenilir akım okuması ve üzeri:** Hesaplanacak alan.

İlk güvenilir akım okumasının sayısal sınırı henüz belirlenmemiştir. Bu aralık yeni kontrollü yük deneyleriyle belirlenecektir. 0,24 A tek başına ilk güvenilir okuma veya ölçüm doğruluğu garantisi değildir.

## İstatistiksel dayanak

Kullanıcının sağladığı Home Assistant History kaydında, fiziksel hatta enerji/yük akımı bulunmayan koşulda CH1 için 10 saatlik kesintisiz kayıt incelendi.

- CH1 akım entity örnek sayısı: **36.002**
- CH1 ham SCT entity örnek sayısı: **36.002**
- K: **24.22**
- K uygulanmış akımın P95 değeri: **0,23587365 A**
- Ham SCT değerinin P95 değeri: **0,00973880**
- K uygulanmış akımda **%96,33** ölçüm 0,24 A veya altında; yaklaşık **%3,67** ölçüm 0,24 A üzerindedir.
- K uygulanmış akımın P99 değeri: 0,27521688 A; maksimumu 0,96086776 A'dır. Tekil yüksek sıçramalar kapalı alan sınırını belirlemek için belirleyici kabul edilmemiştir.

P95'in biraz üzerinde, yuvarlak ve uygulanabilir eşik olarak 0,24 A seçilmiştir. Bu karar, bu 10 saatlik CH1 yüksüz kaydının istatistiğine dayanır; tüm kanallara veya farklı donanım/kurulumlara otomatik genellenmez.

## Kapsam ve sınırlar

- Ham CSV, kullanıcının isteğiyle depoya eklenmemiştir. Yalnızca karar için gerekli istatistiksel özet saklanır.
- Bu karar ON kalibrasyonu, PZEM–SCT eşleştirmesi, katsayı eğitimi veya kararlılık algoritması tanımlamaz.
- Sıçrama filtreleme bu kararın kapsamında değildir.
- E16'daki ON/OFF gözlem konusu ayrıdır; bu 10 saatlik yüksüz kayıt E16 ON/OFF davranışını doğrulamaz.
- I007 çoklu oturum gürültü karakterizasyonu ileride ek bilgi sağlayabilir; ancak CH1 için bu ilk 0,24 A kapalı alan kararının ön koşulu değildir.

## Sonraki iş

0,24 A üzerindeki bölgede, ilk güvenilir akım okumasının hangi seviyede başladığını kontrollü yüklerle belirle. Bu seviyeye kadar olan aralık hesaplanmadı olarak kalacaktır.
