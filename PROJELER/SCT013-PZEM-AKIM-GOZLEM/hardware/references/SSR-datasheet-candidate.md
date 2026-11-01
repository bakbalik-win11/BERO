# SSR — Ürün sayfası ve veri sayfası eşleştirmesi

> **Proje referans kopyası.** Asıl kayıt: [`DONANIM/SSR/datasheets/README.md`](../../../../DONANIM/SSR/datasheets/README.md).

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

## Besleme ve tetik gerilimi — önemli ayrım

**Kartın 5 V beslemesi ile tetik girişindeki lojik sinyal aynı bağlantı/aynı işlev değildir.**

- **VCC / kart beslemesi:** Kartın elektronik devresini beslemek için 5 V DC.
- **IN1 / IN2 tetik girişleri:** ESP32'nin GPIO çıkışlarından gelen kontrol sinyalleri. ESP32 GPIO lojik seviyesi 3,3 V'tur; bu hatlara kartın 5 V beslemesi doğrudan bağlanmaz.
- **AC yük tarafı:** Anahtarlanan şebeke/yük bağlantısıdır; 5 V kontrol beslemesinden ve ESP32 GPIO sinyalinden ayrı tutulur.
- Ürün sayfasında giriş için 0–0,5 V LOW, 0,5–2,5 V belirsiz ve 2,5–20 V HIGH değerleri verilir. Bu değerlere göre 3,3 V, HIGH aralığındadır; ancak aynı sayfadaki “low level trigger” ifadesiyle mantık çelişkisi bulunduğundan gerçek aktif seviye henüz doğrulanmış değildir.
- Bu nedenle 5 V VCC verilecek olması, tetik girişine de 5 V verilmesi gerektiği anlamına gelmez. ESP32 GPIO'su 5 V'a çekilmez. IN girişinin 3,3 V ile güvenilir ve doğru yönde tetiklenmesi, şebeke bağlantısı yapılmadan önce düşük gerilimli masa testinde doğrulanır.

**Mevcut karar:** Kart beslemesi 5 V DC; kontrol sinyali ESP32'den 3,3 V lojik seviyesinde gelir. Tetik polaritesi/aktif seviyesi ve giriş akımı fiziksel kart üzerinde test edilene kadar kesinleşmiş sayılmaz. Bu not bir bağlantı/test sonucu değil, ürün sayfası bilgisi ve güvenli tasarım ayrımıdır.
