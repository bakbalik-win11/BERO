# SSR — Ürün sayfası ve veri sayfası eşleştirmesi

## Satın alınan kart

Kullanıcının verdiği satın alma kaynağı: [SAMM Market — 5V 2 Kanal Solid State Röle Kartı](https://market.samm.com/5v-2-kanal-solid-state-role-karti).

- Tedarikçi kodu: İzmo9659
- SAMM SKU: MP02637
- Kart: 5 V DC, 2 kanal
- Ürün sayfasında belirtilen çıkış: kanal başına 75–264 V AC, 0,1–2 A; nominal 100–240 V AC
- OMRON, fototriyak izolasyon ve zero-cross nitelikleri ürün sayfasında verilir.

**Kanal sayısı düzeltmesi:** Önceki proje belgelerinde kullanılan “4 kanallı SSR” ifadesi yanlıştı. Satın alınan ürün 2 kanallıdır.

## Tam SSR parça kodu

SAMM ürün sayfası kart üzerindeki SSR entegresinin tam model numarasını belirtmiyor. Fotoğraftaki yazı da güvenilir eşleştirme için yeterince net değil. Bu yüzden aşağıdaki üretici ailesi yalnız karşılaştırma amacı taşır.

[Omron G3MB serisi veri sayfası (PDF)](https://www.omronkft.hu/pdf_en/g3mb.pdf)

G3MB-202P'nin 5 V kontrol girişli, zero-cross ve 2 A / 100–240 V AC sınıfı olması özellikler bakımından benzerlik gösterir; ancak fiziksel karttaki parçanın kesin olarak G3MB-202P olduğu henüz kanıtlanmamıştır.

## Kontrol girişindeki belirsizlik

Ürün sayfasında LOW/HIGH gerilim eşikleri verilirken ayrıca “low level trigger” ifadesi bulunur. Kontrol girişinin gerçek mantığı önce şebekeden tamamen bağımsız, düşük gerilimli masa testinde doğrulanmalıdır. Kartın 5 V beslemesi, ESP32 GPIO'sunun 5 V toleranslı olduğu anlamına gelmez.
