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

## Besleme ve tetik gerilimi — önemli ayrım

**Kartın 5 V beslemesi ile tetik girişindeki lojik sinyal aynı bağlantı/aynı işlev değildir.**

- **VCC / kart beslemesi:** Kartın elektronik devresini beslemek için 5 V DC.
- **IN1 / IN2 tetik girişleri:** ESP32'nin GPIO çıkışlarından gelen kontrol sinyalleri. ESP32 GPIO lojik seviyesi 3,3 V'tur; bu hatlara kartın 5 V beslemesi doğrudan bağlanmaz.
- **AC yük tarafı:** Anahtarlanan şebeke/yük bağlantısıdır; 5 V kontrol beslemesinden ve ESP32 GPIO sinyalinden ayrı tutulur.
- Ürün sayfasında giriş için 0–0,5 V LOW, 0,5–2,5 V belirsiz ve 2,5–20 V HIGH değerleri verilir. Bu değerlere göre 3,3 V, HIGH aralığındadır; ancak aynı sayfadaki “low level trigger” ifadesiyle mantık çelişkisi bulunduğundan gerçek aktif seviye henüz doğrulanmış değildir.
- Bu nedenle 5 V VCC verilecek olması, tetik girişine de 5 V verilmesi gerektiği anlamına gelmez. ESP32 GPIO'su 5 V'a çekilmez. IN girişinin 3,3 V ile güvenilir ve doğru yönde tetiklenmesi, şebeke bağlantısı yapılmadan önce düşük gerilimli masa testinde doğrulanır.

**Mevcut karar:** Kart beslemesi 5 V DC; kontrol sinyali ESP32'den 3,3 V lojik seviyesinde gelir. Tetik polaritesi/aktif seviyesi ve giriş akımı fiziksel kart üzerinde test edilene kadar kesinleşmiş sayılmaz. Bu not bir bağlantı/test sonucu değil, ürün sayfası bilgisi ve güvenli tasarım ayrımıdır.

## Önceki denemeden kullanıcı hatırlatması — testte doğrulanacak

Kullanıcı, önceki SSR denemelerinde kart beslemesi ile tetik girişinin aynı gerilim seviyesinde olmaması durumunda rölenin açılıp kapanmadığını hatırlıyor. Bu, **kullanıcı hatırlatmasıdır; mevcut kayıtlarda bunu kanıtlayan ölçüm veya test logu bulunmuyor.** Dolayısıyla “VCC ile IN mutlaka aynı gerilim olmalı” şeklinde kesin bir elektriksel gereksinim olarak kabul edilmeyecek; ancak yeni testte özellikle araştırılacak.

Testte ayrı ayrı kaydedilecek durumlar:

1. Kart VCC=5 V iken IN girişine 3,3 V lojik HIGH uygulandığında kanalın davranışı.
2. Aynı besleme koşulunda IN=LOW uygulandığında kanalın davranışı.
3. Üretici/ürün belgesinde destekleniyorsa, IN girişinin gerekli tetik akımı ve giriş devresi; yalnızca gerilim seviyesi karşılaştırılmayacak.
4. Kartın giriş mantığının aktif-HIGH mı aktif-LOW mu olduğu ve kanal LED'i/çıkış davranışı.

**Güvenlik sınırı:** ESP32 GPIO'su 5 V'a doğrudan bağlanmayacak. 5 V tetik seviyesi gerçekten gerekiyorsa, uygun transistor veya seviye dönüştürücü arayüzü ayrıca tasarlanacak. Şebeke yükü bağlanmadan önce düşük gerilimli, izole masa testi yapılacak.

Test sonucu alınana kadar VCC=5 V ve GPIO=3,3 V kombinasyonunun çalıştığı veya çalışmadığı iddia edilmeyecek. Bu kayıt geçmişte yaşandığı hatırlanan sorunu kaybetmemek ve kontrollü biçimde yeniden sınamak içindir.
