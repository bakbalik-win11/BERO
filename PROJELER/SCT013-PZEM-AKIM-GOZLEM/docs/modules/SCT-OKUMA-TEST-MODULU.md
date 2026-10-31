# BERO Modülü 2 — SCT Okuma Test Modülü

**Modül kimliği:** BERO-SCT-OKUMA-TEST-002  
**Adı:** SCT Okuma Test Modülü  
**Durum:** Taslak / donanım tanımı sürüyor

## Amaç

SCT sensörlerini taşınabilir bir düzenekte ESP32D2 ile okumak ve test etmek. Bu kutu yalnızca SCT girişleri, ESP32D2 ve ortak bias devresini barındıracaktır.

## Kutu içeriği

- 3 adet 3,5 mm dişi SCT girişi.
- ESP32D2 kartı.
- Ortak bias devresi için mini breadboard.

Üç SCT girişi fiziksel kapasite olarak korunur. İlk testlerin kaç kanal ile ve eşzamanlı yürütüleceği ayrıca belirlenecektir.

## Ortak bias yapısı

Mini breadboard üzerinde ortak bias devresi bulunur. Bias beslemesi ayrı **BERO-BIAS-TRAFOSU-001 (Bias Trafosu)** modülünden sağlanacaktır.

Kullanıcının paylaştığı genel bias yapısında görülen/bildirilen elemanlar:
- 2 direnç,
- 1 seramik kondansatör,
- 1 elektrolitik kondansatör.

Envanterde daha önce belirtilen bileşenler: 2 × 10 kΩ, 1/4 W metal film direnç ve 104 kodlu (100 nF) seramik kondansatör. Elektrolitik kondansatörün değeri henüz belirlenmedi. Kesin devre bağlantısı ve elemanların bağlantı noktaları doğrulanmış değildir.

## SCT bağlantıları

- Üç adet 3,5 mm dişi jack girişi bulunur.
- Kullanıcı bildirimine göre kırmızı hat ortak bias hattıdır.
- Mavi, yeşil ve sarı hatlar ayrı SCT sinyal hatlarıdır.
- Jack uçlarının tip/ring/sleeve karşılıkları ve kesin pin dizilimi henüz doğrulanmamıştır.

## Kutu dışında bırakılanlar

Bu kutuda aşağıdaki donanımlar bulunmayacaktır:
- 220 V AC şebeke girişi veya 220 V AC çıkışı.
- PZEM-004T.
- SSR ve SSR kontrol/güç devresi.
- ESP için kutu içi 220 V → 5 V güç kaynağı.

PZEM ve SSR, BERO sisteminin diğer bölümlerinde ayrı ele alınacaktır; bu kutunun kapsamına dahil değildir.

## Besleme ve güvenlik sınırı

ESP32D2'nin besleme yöntemi ve kutu dışından sağlanacak düşük gerilim bağlantısı henüz bu modül kaydında tanımlanmamıştır. Bias devresi ayrı Bias Trafosu modülünden beslenecektir. Kutu içinde şebeke gerilimi planlanmamaktadır. Mini breadboard yalnızca düşük gerilim bias devresi içindir.

## Açık noktalar

- ESP32D2'nin güç bağlantısının nasıl sağlanacağı.
- Bias Trafosu ile mini breadboard arasındaki kablo/konnektör düzeni.
- Üç SCT jack'inin kesin pin eşlemesi.
- Elektrolitik kondansatörün değeri, polaritesi ve devredeki kesin yeri.
- Üç girişin kullanım/test sırası.

**Kanıt ayrımı:** Kutu içeriği ve kapsam, kullanıcının bu oturumdaki tasarım kararıdır. Jack renkleri ve bias elemanları önceki kullanıcı bildirim/fotoğrafına dayanır. Devre bağlantıları henüz fiziksel olarak doğrulanmamıştır.
