# ADR: Osiloskop Sinyal Görünürlüğü İçin Harici Yükselteç

- Tarih: 2026-11-21
- Durum: Öneri / ana BERO kapsamı dışında

## Bağlam

BERO'nun ana amacı SCT013 çıkışını kullanarak yük davranışını gözlemlemek ve SCT verisini PZEM ölçümleriyle kararlı pencerelerde eşleştirmektir. Osiloskop satın alma beklentisi, SCT'nin düşük seviyeli AC çıkışındaki milivolt değişimini doğrudan görerek yük açma/kapama farkını izlemekti.

Kullanılan FNIRSI 2D15P cihazında CH1 dikey ölçeğinin 1X probla en düşük kademesi 10 mV/div olarak gözlemlendi. Bu sınır, birkaç mV seviyesindeki SCT değişimlerini doğrudan ekranda rahatça ayırt etmeyi zorlaştırıyor.

## Karar

SCT sinyalini osiloskopta daha rahat gözlemlemek için harici bir analog yükselteç devresi değerlendirilmesi önerildi. MCP6002, mevcut malzeme envanterinden olası bir bileşen olarak incelenebilir.

Bu çalışma yalnızca osiloskop görüntülemesini kolaylaştırma amacı taşır. **Ana BERO ölçüm zincirine, veri toplama mimarisine veya eğitim verisine katkı sağladığı doğrulanmış değildir.** Bu nedenle ana BERO geliştirmesinin önceliği değildir ve şimdilik ertelenmiştir.

## Kapsam ve sınırlar

- Şu aşamada devre tasarımı, bağlantı şeması veya firmware değişikliği yapılmayacak.
- Yükselteç çıkışı yalnızca osiloskopta görüntüleme amacıyla kullanılacak şekilde ele alınacak.
- Yükselteç kazancı, giriş/çıkış aralığı, biaslama ve SCT'nin çıkış yüklenmesi hesaplanmadan bağlantı yapılmayacak.
- Yükselteçli ölçüm, SCT'nin ham çıkış gerilimi olarak kaydedilmeyecek; kazanç bilgisi olmadan mV karşılaştırmasına dahil edilmeyecek.
- Bu öneri başarılı deney sonucu değildir; henüz kurulmamış ve doğrulanmamıştır.

## Gerekçe

Mevcut osiloskopun dikey hassasiyet sınırı nedeniyle düşük seviyeli SCT sinyalini doğrudan görüntülemek güçleşiyor. Harici yükselteç, osiloskopun görüntüleme sınırını aşmak için yardımcı bir araç olabilir. Ancak bu çözümün ana BERO veri toplama sistemine değer kattığı gösterilmediğinden ayrı ve düşük öncelikli tutulur.

## Sonraki adım

Ana BERO çalışmasından bağımsız bir zamanda, güvenli ve hesaplanmış bir MCP6002 yükselteç devresi tasarlanıp yalnızca osiloskop gözlemi için denenebilir. Deney yapılmadan sonuç veya performans iddiası yazılmayacaktır.
