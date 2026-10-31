# ADR-013 — Modül 2 bias ADC kanal seçimi

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ
- **Karar sahibi:** Kullanıcı adına teknik karar asistan tarafından verildi; kullanıcı “sen karar ver” talimatı verdi.
- **Karar:** Yeni Modül 2 tasarımında üç ayrı SCT sinyali ve tek bias/Vmid ölçümü için dört bağımsız ADC girişi kullanılacak. Bias ADC kanalı voltaj olarak (`raw: false`) okunacak. Bias için ayrı bir RAW GPIO ayrılmayacak.

## Bağlam

Mevcut E00F firmware'inde:
- GPIO32: SCT analog düğümü, RAW count.
- GPIO33: aynı SCT analog düğümü, ADC voltajı ve ct_clamp kaynağı.
- GPIO34: bias/Vmid düğümü, RAW count.
- GPIO35: aynı bias/Vmid düğümü, ADC voltajı.

Dolayısıyla dört GPIO tanımlı olsa da mevcut düzen dört bağımsız fiziksel sinyal ölçmüyor; iki analog düğümün ikişer gösterimini ölçüyor. Yeni kutu ise üç ayrı SCT girişi ve bir ortak bias ölçümü gerektiriyor.

## Kanıt

**ÖLÇÜLDÜ / HA geçmişi ile desteklendi:** Kullanıcının 2026-10-30 23:15:00–2026-10-31 10:07:48.897 Türkiye saati aralığındaki gece kaydı 10 saat 52 dakika 48.897 saniye sürmüş ve 177,370 kayıt içermiştir.

Bias kanallarının özetleri:
- GPIO35 bias voltajı: medyan 1.653 V; ortalama 1.6516 V; SD 7.94 mV; p5–p95 1.637–1.662 V; min/max 1.503/1.779 V.
- GPIO34 bias RAW: medyan 1,840 count; ortalama 1,839.01 count; SD 9.77 count; p5–p95 1,821–1,851; min/max 1,535/2,011.
- Voltajın saatlik medyanlarında yaklaşık 5 mV yükselme gözlenmiştir; tekil uç değerler kayıt içinde tutulmuştur.

Bu ölçümler bias noktasının uzun süreli izlenebildiğini gösterir. İki sensör aynı fiziksel bias noktasını farklı birimlerde gösterdiğinden, yeni kutuda her iki gösterim için iki ayrı fiziksel ADC girişi ayırmak gerekli değildir. Voltaj, hedeflenen yaklaşık 1.65 V bias seviyesini doğrudan ve okunabilir birimle izlediği için tercih edilmiştir.

## Sonuç / uygulama sınırı

1. Yeni modül ADC kaynakları: SCT-1, SCT-2, SCT-3 ve bias voltajı.
2. Bias RAW için ikinci fiziksel ADC kanalı ayrılmayacak.
3. Mevcut `firmware/esp32d2.yaml` ve çalışan E00F baseline bu ADR ile değiştirilmez.
4. GPIO yeniden ataması, kart pinout doğrulaması ve çoklu SCT firmware tasarımı ayrı uygulama işi olarak kalır.
5. USB üzerinden harici 5 V besleme / Mac veri bağlantısı konusu bu ADR'nin kapsamı dışındadır; bağlantı tipi ve kart üzerindeki gerçek USB portu ayrıca doğrulanmalıdır.

## Doğrulama durumu

Bu bir donanım mimarisi kararıdır. Yeni üç SCT + bir bias bağlantısı henüz kurulmadı; yeni firmware yazılmadı, derlenmedi veya cihaza yüklenmedi.
