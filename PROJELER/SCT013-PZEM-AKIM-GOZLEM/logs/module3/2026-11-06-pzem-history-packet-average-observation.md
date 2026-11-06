# 2026-11-06 — PZEM History geçiş davranışı: paket ortalaması gözlemi

## HEDEF
PZEM'in yük açma/kapama geçişlerinde görünen akım değerlerinin anlık fiziksel akımı temsil edip etmediğini ayırt etmek; kararlı alanların neden geçiş alanlarından ayrı ele alınması gerektiğini kaydetmek.

## GÖZLEM
Kullanıcı, Home Assistant geçmiş grafiğindeki PZEM akımının geçiş sırasında tek bir anlık ölçüm gibi okunmaması gerektiğini belirtti. Kullanıcının tarif ettiği beş örnekli davranışta:
- `1, 1, 1, 1, 1` → ortalama `1,0`
- `1, 1, 1, 1, 0` → ortalama `0,8`

Bu örnek, önceki durumdan kalan örneklerin geçiş sonrasında gösterilen değere katkı vermesiyle uyumlu bir paket/beşli ortalama davranışını anlatır. Bu nedenle PZEM grafiğinde açma-kapama kenarlarında görülen ara değerler, fiziksel akımın o andaki gerçek seviyesi olarak doğrudan yorumlanmamalıdır.

## SONUÇ
- **KULLANICI GÖZLEMİ:** PZEM History geçiş değerleri paket ortalaması/önceki örneklerin etkisini taşıyan bir gösterim olarak değerlendirilmelidir.
- **HESAP:** Yukarıdaki beşli örneklerin aritmetik ortalamaları sırasıyla 1,0 ve 0,8'dir.
- PZEM'in bu geçiş davranışı, kararlı yük alanlarındaki değerlerin geçerli olmadığı anlamına gelmez. Kullanıcının mevcut deney yaklaşımında PZEM'in kararlı açık/kapalı alanları durum ve zaman aralığı belirlemek için kullanılabilir; geçiş kenarları ise kararlı alan istatistiklerine katılmaz.
- Bu gözlem, PZEM'i her zaman ve her örnek için anlık ground truth kabul etmemek gerektiğini destekler. PZEM proje içindeki yardımcı referans rolünü korur; mutlak ground truth olarak tanımlanmaz.
- SCT örnekleme hızı/kanal kararlılığı karşılaştırmasında PZEM değeri ölçüt değildir. Üç SCT kanalı kendi kararlı ON alanlarında ve ortak yük davranışı üzerinden ayrı değerlendirilir.

## KANIT SINIRI
Bu kayıt, kullanıcının Home Assistant grafiği ve tarif ettiği beşli örnek üzerinden yapılan gözlemi belgeler. PZEM firmware/Modbus içindeki filtre veya ortalama algoritmasının kaynak kodu incelenmiş değildir. Dolayısıyla iç uygulamanın kesin teknik algoritması kanıtlanmış sayılmaz; burada belgelenen sonuç, gözlenen History davranışının yorumudur.

## SONRAKİ ADIM
12:01 sonrasında başlatılan yeni kanal eşleştirme deneyi ayrı veri seti olarak korunacak. Yeni eşleştirme:
- CH1 ← önceki fiziksel SCT3
- CH2 ← önceki fiziksel SCT1
- CH3 ← önceki fiziksel SCT2

Bu yeni kaydın başlangıcı 2026-11-06 12:01:00 (+03:00) olarak kullanıcı tarafından belirlendi. Yeni CSV geldiğinde aynı SCT-kendi-içinde kararlılık istatistikleri uygulanacak; PZEM geçiş değerleri bu hesaplara dahil edilmeyecek.
