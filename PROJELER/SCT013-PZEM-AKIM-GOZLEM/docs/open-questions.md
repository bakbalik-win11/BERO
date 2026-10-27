# Açık sorular

Aşağıdaki sorular yalnız bu projede hâlâ cevaplanmamış proje-özel konulardır. Genel donanım bilgileri [referans klasöründe](../hardware/references/README.md) ve ana BERO `DONANIM/` belgelerinde mevcuttur.

1. Bu projede kullanılacak ADC hangisi ve VREF kaynağı/değeri nedir? BERO'da MCP3208 referansı var, ancak bu projedeki fiziksel düzeneğe seçildiği henüz doğrulanmadı.
2. SCT013-030 AC sinyali tamamlanmış yaklaşık 1,65 V bias orta noktasına hangi bağlantı/kuplaj elemanıyla eklenecek?
3. Burden/analog filtre değerleri ile ADC girişinin güvenli maksimum aralığı nedir? Nihai bağlantı kanıtı kaydı eksik.
4. SAMM Market 5 V 2 kanallı SSR kartının hangi iki AC yükü anahtarlayacağı ve hangi ESP32 GPIO'larının kullanılacağı nedir? Ürün sayfasındaki LOW/HIGH eşikleri ile “low-level trigger” notu tutarsız olabildiğinden kontrol mantığı düşük gerilimde doğrulanmalı; giriş akımı ve kanal başına termal/sürekli yük sınırları ayrıca teyit edilmeli.
5. DS3231 breakout kartının gerçek modeli/revizyonu nedir; SDA/SCL pinleri ve I²C pull-up gerilimi nedir? Yedek pil türü ve kartta şarj devresi olup olmadığı da doğrulanmalı.
6. DS3231'in saati ilk kurulumda nasıl ayarlanacak: manuel başlangıç mı, ağ erişimi varsa NTP eşitlemesi mi? Saat dilimi ve UTC/yerel zamanın kayıtlarda nasıl temsil edileceği belirlenmeli.
7. PZEM'in iç ölçüm/ortalama penceresi nedir; V, I, P ve PF aynı anda mı yenileniyor? Bunlar deneyle ölçülecek.
8. Hangi akımın altında PZEM, bağımsız referansa göre kabul edilemez sapma/kararsızlık gösteriyor?
9. 1 kS/s, 2 kS/s ve 2,5 kS/s seçenekleri arasında hedef yüklerde anlamlı performans farkı var mı?
10. 200 ms pencere kararlı yükte tekrarlanabilir mi; çevrime senkron pencere gerekli mi?
11. True-RMS referans cihazı nedir ve en az üç kontrollü yük seviyesi hangi yüklerle sağlanacak?

**Karara bağlandı; yeniden sorulmayacak:**
- Öncelikli sensör: SCT013-030 (30 A / 1 V).
- PZEM kaydı: mevcut [DONANIM/PZEM-004T/README.md](../../../DONANIM/PZEM-004T/README.md) esas alınır.
- Bağlı CT: PZCT-02, 0–100 A; kullanıcı tarafından model olarak belirtildi ve PZEM'e bağlı olduğu fotoğrafta gösterildi. Bu, 100 A harici CT'li yapılandırmadır.
- İlk aşamada kullanılacak ESP32 kartları: 2× WROOM-32D, 1× WROOM-32E ve 1× genel ESP-WROOM-32 NodeMCU ESP32 Bluetooth.
- 5 V, 2 kanallı SAMM Market SSR kartı proje donanımına dahil edildi (tedarikçi kodu İzmo9659, SKU MP02637). Ürün sayfası OMRON, fototriyak izolasyon, zero-cross; kanal başına 75–264 VAC ve 0,1–2 A; kart beslemesi tüm kanallar açıkken 160 mA bildiriyor. Tam SSR parça kodu, gerçek giriş tetik mantığı ve yük ataması ayrıca doğrulanacak.
- DS3231 RTC, ölçüm/olay kayıtlarına takvim zamanı sağlamak için projede kullanılacak. Önceki BERO bağlantı pinleri ve NTP örneği referanstır; bu proje için pin/başlatma kararı değildir.
- Temiz yaklaşık 1,65 V bias üretim alt devresi kullanıcı onayıyla tamamlandı: RN130421 6 V / 2 VA → KBU6M köprü → 2200 µF / 35 V → L78L33; ayrı breadboardda 2×10 kΩ ve orta noktadan GND'ye 104 kodlu 100 nF seramik. Bağımsız ölçüm raporu yoksa 1,650 V'nin cihazla ölçüldüğü iddia edilmeyecek.
