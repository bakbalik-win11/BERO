# SSR — SAMM Market 5 V 2 Kanal Solid State Röle Kartı

## Ürün kimliği ve kaynak

- **Satın alma kaynağı (kullanıcı beyanı):** [SAMM Market — 5V 2 Kanal Solid State Röle Kartı](https://market.samm.com/5v-2-kanal-solid-state-role-karti)
- **Ürün adı:** 5V 2 Kanal Solid State Röle Kartı
- **Tedarikçi kodu:** İzmo9659
- **SAMM SKU:** MP02637
- **Kartta bildirilen SSR üreticisi:** OMRON
- **Kanal sayısı:** **2** (önceki kayıtlardaki “4 kanal” ifadesi hatalıydı; ürün sayfasıyla düzeltildi.)

Özellikler SAMM Market ürün sayfasından alınmıştır. Satın alınan fiziksel kart üzerinde parça kodu/markalama ayrıca okunarak eşleştirilmediği için tekil SSR entegresinin kesin model kodu (ör. G3MB-202P) doğrulanmış sayılmaz.

## Ürün sayfasında yayımlanan özellikler

- **Kart beslemesi:** 5 V DC; iki kanal da açıkken toplam 160 mA olarak belirtilmiş.
- **Kanal başına çıkış:** 75–264 V AC, 50/60 Hz.
- **Kanal başına bildirilen yük akımı:** 0,1–2 A.
- **Nominal çıkış yükü:** 100–240 V AC, 50/60 Hz.
- **Yük tipi:** Genel amaçlı AC.
- **DC yük anahtarlama:** Uygun değil; ürün sayfası yalnız AC yük için olduğunu belirtiyor.
- **İzolasyon:** Fototriyak.
- **Anahtarlama:** Zero-cross.
- **Giriş gerilimi açıklaması:** 0–0,5 V LOW (SSR kapalı), 0,5–2,5 V belirsiz bölge, 2,5–20 V HIGH (SSR açık).
- **Ek tetikleme notu:** Aynı ürün sayfasında “low level trigger” ifadesi de var. Bu açıklama, yukarıdaki LOW=kapalı/HIGH=açık gerilim açıklamasıyla çelişebildiğinden girişin gerçek aktif seviyesi masa üzerinde düşük gerilimle doğrulanmadan kabul edilmemeli.

## Bu projedeki durum

Kart proje donanım listesine dahil edildi; kullanılacak çıkış kanalları, yükler ve ESP32 GPIO'ları henüz belirlenmedi. Ürün sayfasındaki 2 A/kanal değeri, termal koşullar ve PCB yapısı doğrulanmadan sürekli akım garantisi gibi yorumlanmamalı.

Önceki BERO ESP32-C3 test kaydında GPIO6 geçer; bu tarihsel bilgi bu projedeki GPIO seçimi değildir.

## Güvenlik ve bağlantı öncesi kontrol

- ESP32 GPIO'su doğrudan 5 V seviyesine çekilmemeli. Kartın beslemesi ile kontrol girişinin elektriksel sınırlarını ayır; 5 V besleme, girişe mutlaka 5 V uygulanması gerektiği anlamına gelmez.
- Giriş tetik mantığı ve her kanala ait LED davranışı önce düşük gerilimli testle doğrulansın.
- Yalnız AC yük anahtarlanmalı; DC yük kullanımı bu modül için uygun değildir.
- Şebeke gerilimli çıkışlar MCU/USB/breadboard tarafından fiziksel olarak ayrılmalı; uygun sigorta, muhafaza, yalıtım aralıkları ve yetkin kişi kontrolü sağlanmalı.
- Kanal başına 2 A değeri, tüm kanalların aynı anda bu akımla sürekli çalışabileceğine dair bağımsız doğrulama değildir.
