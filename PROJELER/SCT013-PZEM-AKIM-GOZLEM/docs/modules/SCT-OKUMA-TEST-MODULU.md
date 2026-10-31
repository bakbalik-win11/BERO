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

## Şebeke girişi ve besleme dağıtımı

Modülde bir **220 V AC şebeke bağlantısı** bulunacaktır. Bu girişten iki besleme kolu planlanmıştır:

1. **PZEM bağlantısı:** PZEM-004T'nin AC ölçüm/gerilim referansı için gereken bağlantısı bu modülün şebeke girişinden beslenecektir.
2. **5 V güç kaynağı:** ESP'ye enerji sağlayacak 5 V güç kaynağı aynı modülün şebeke girişinden beslenecektir.

Bu kayıt işlevsel mimariyi tanımlar; şebeke dağıtımının kablolaması, koruma elemanları, klemensleri, sigorta değerleri ve muhafaza yerleşimi henüz tasarlanmış veya doğrulanmış değildir. PZEM'in akım ölçüm yolu ile gerilim bağlantısının kesin topolojisi de ayrıca belirlenecektir.

## SSR ve anahtarlanan yük çıkışı

Modülde SSR güç devresi için de **220 V AC girişi** bulunacaktır. SSR üzerinden anahtarlanan bir **220 V AC çıkış** modülün dışına alınacaktır; bu çıkış test yükünü (ör. lamba) beslemek için kullanılacaktır.

- SSR'nin güç tarafı, modülün şebeke girişinden beslenecek ve anahtarlanan 220 V AC çıkışı sağlayacaktır.
- SSR'nin kontrol girişi düşük gerilim tarafında ESP tarafından sürülecek şekilde planlanmaktadır.
- SSR'nin tam modeli, kontrol gerilimi/polaritesi, yük akımı, koruma elemanları ve bağlantı şeması henüz kesinleştirilmemiştir.
- PZEM'in akım ölçümünün SSR çıkışına bağlanan test yükünü doğru gözlemleyecek şekilde konumlandırılması ayrıca tasarlanacaktır.

## SCT bağlantıları

- Üç adet 3,5 mm dişi jack girişi vardır.
- Kullanıcı bildirimine göre kırmızı hat ortak bias hattıdır.
- Mavi, yeşil ve sarı hatlar üç ayrı SCT sinyal hattıdır.
- İlk aşamada tek kanal kullanılacaktır; diğer girişler mevcut kapasite olarak korunur.
- Jack uçlarının tip/ring/sleeve karşılıkları ve kesin pin dizilimi henüz doğrulanmamıştır.

## Güvenlik sınırı

Modülde 220 V AC girişleri ve SSR ile anahtarlanan 220 V AC yük çıkışı bulunacağından şebeke tarafı ile ESP/SCT düşük gerilim tarafı fiziksel ve elektriksel olarak ayrılmalıdır. Uygun sigorta/koruma, yalıtım mesafeleri, kablo sabitleme, dokunmaya karşı koruma ve kapalı muhafaza tasarlanmalıdır. Açık mini breadboard yalnızca düşük gerilim bias devresi için kullanılmalı; şebeke bağlantısı breadboard üzerinden taşınmamalıdır. Şebeke bağlantısı yetkin kişi tarafından uygun güvenlik koşullarında yapılmalıdır.

## Sınırlar ve açık noktalar

- PZEM bağlantısı, ESP'yi besleyecek 5 V güç kaynağı ve SSR güç devresi modülün 220 V AC girişinden beslenecek şekilde planlandı. SSR üzerinden anahtarlanan ayrı bir 220 V AC test yükü çıkışı bulunacak. ESP'nin kesin modeli ve RTC'nin modüle dahil olup olmayacağı henüz kararlaştırılmadı.
- Bias beslemesinin Bias Trafosu modülünden alınacağı tasarım kararıdır; bu modülün şebeke girişinden Bias Trafosu'na nasıl enerji aktarılacağı henüz netleştirilmedi. Bağlantı ve yük altında çalışma doğrulaması yapılmadı.
- Elektrolitik kondansatörün değeri, polaritesi ve devredeki kesin yeri doğrulanmadı.
- Devre şeması ve jack pin eşlemesi, fiziksel süreklilik/bağlantı kontrolü sonrasında eklenecektir.

**Kanıt ayrımı:** Modülün üç jack'i, kablo renkleri ve ortak bias niyeti kullanıcı bildirimidir. Genel bias elemanları kullanıcı fotoğrafıyla desteklenir. Fotoğraf tek başına devre bağlantılarını veya eleman değerlerini kanıtlamaz.
