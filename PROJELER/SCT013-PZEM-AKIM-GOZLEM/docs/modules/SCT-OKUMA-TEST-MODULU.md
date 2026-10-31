# BERO Modülü 2 — SCT Okuma Test Modülü

**Modül kimliği:** BERO-SCT-OKUMA-TEST-002  
**Adı:** SCT Okuma Test Modülü  
**Durum:** Taslak / donanım tanımı sürüyor

## Amaç

SCT sensörlerini geçici ve taşınabilir bir düzenekte bağlayarak okuma/test çalışmalarında kullanmak. Modülde üç adet 3,5 mm dişi SCT bağlantısı bulunur. İlk çalışma tek SCT kanalıyla başlayacaktır; üç giriş kapasitesi korunur.

## Ortak bias yapısı

Modülde mini breadboard üzerinde ortak bir bias devresi bulunacaktır. Bu bias devresi, ayrı **BERO-BIAS-TRAFOSU-001 (Bias Trafosu)** modülünden beslenecektir.

Kullanıcının paylaştığı genel bias yapısında görülen/bildirilen elemanlar:
- 2 direnç,
- 1 seramik kondansatör,
- 1 elektrolitik kondansatör.

Envanterde daha önce belirtilen breadboard bias bileşenleri: 2 × 10 kΩ, 1/4 W metal film direnç ve 104 kodlu (100 nF) seramik kondansatör. Fotoğraftaki elektrolitik kondansatörün değeri henüz belirlenmedi. Kesin bağlantı şeması ve elemanların bağlantı noktaları doğrulanmış değildir.

## SCT bağlantıları

- Üç adet 3,5 mm dişi jack girişi vardır.
- Kullanıcı bildirimine göre kırmızı hat ortak bias hattıdır.
- Mavi, yeşil ve sarı hatlar üç ayrı SCT sinyal hattıdır.
- İlk aşamada tek kanal kullanılacaktır; diğer girişler mevcut kapasite olarak korunur.
- Jack uçlarının tip/ring/sleeve karşılıkları ve kesin pin dizilimi henüz doğrulanmamıştır.

## Sınırlar ve açık noktalar

- Bu modülün PZEM, SSR, RTC veya ESP içereceği henüz kararlaştırılmadı.
- Bias beslemesinin Bias Trafosu modülünden alınacağı tasarım kararıdır; bağlantı ve yük altında çalışma doğrulaması yapılmadı.
- Elektrolitik kondansatörün değeri, polaritesi ve devredeki kesin yeri doğrulanmadı.
- Devre şeması ve jack pin eşlemesi, fiziksel süreklilik/bağlantı kontrolü sonrasında eklenecektir.

**Kanıt ayrımı:** Modülün üç jack'i, kablo renkleri ve ortak bias niyeti kullanıcı bildirimidir. Genel bias elemanları kullanıcı fotoğrafıyla desteklenir. Fotoğraf tek başına devre bağlantılarını veya eleman değerlerini kanıtlamaz.
