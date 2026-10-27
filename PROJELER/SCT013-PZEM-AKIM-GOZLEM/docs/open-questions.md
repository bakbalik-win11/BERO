# Açık sorular

Aşağıdaki sorular yalnız bu projede hâlâ cevaplanmamış proje-özel konulardır. Genel donanım bilgileri [referans klasöründe](../hardware/references/README.md) ve ana BERO `DONANIM/` belgelerinde mevcuttur.

1. İlk aşamada kullanılacak ESP32 kartında SCT sinyalinin okunacağı ADC destekli GPIO numarası nedir? Harici ADC kullanılmayacak; dahili ADC pin eşlemesi firmware/pin planlama aşamasında seçilecek.
2. SAMM Market 5 V 2 kanallı SSR kartının hangi iki AC yükü anahtarlayacağı ve hangi ESP32 GPIO'larının kullanılacağı nedir? Ürün sayfasındaki LOW/HIGH eşikleri ile “low-level trigger” notu tutarsız olabildiğinden kontrol mantığı düşük gerilimde doğrulanmalı; giriş akımı ve kanal başına termal/sürekli yük sınırları ayrıca teyit edilmeli.
3. PZEM'in iç ölçüm/ortalama penceresi nedir; V, I, P ve PF aynı anda mı yenileniyor? Bunlar deneyle ölçülecek.
4. Hangi akımın altında PZEM, bağımsız referansa göre kabul edilemez sapma/kararsızlık gösteriyor?
5. 1 kS/s, 2 kS/s ve 2,5 kS/s seçenekleri arasında hedef yüklerde anlamlı performans farkı var mı?
6. 200 ms pencere kararlı yükte tekrarlanabilir mi; çevrime senkron pencere gerekli mi?

**Karara bağlandı; yeniden sorulmayacak:**
- Eğitim/etiket referansı PZEM-004T V3.0'dır. Modelin geçerli PZEM akım okumasına göre ±%4 bağıl sapma içinde olması Python'da `OK` sayılır. Kararlı alan gözlemi ve SCT istatistikleri ayrı görev/deney konusudur.
- DS3231: kullanıcı beyanı — RTC kodu çalıştı, güç kesilip yeniden verildikten sonra saat korundu; iki modülde de 2032 tipi pil var. Bu test ve pil bilgisi tekrar istenmeyecek.
- Deney yükleri önceden sabitlenmeyecek; kullanıcı her testte kullandığı yükü ve koşulları beyan edecek.
- Öncelikli sensör: SCT013-030 (30 A / 1 V).
- Kullanıcı stok bildirimi: 7 adet SCT013 30 A / 1 V ve 10 adet SCT013 100 A / 1 V; ikisi de jack çıkışlı. Jack yuvaları mevcut.
- Kullanıcı SCT'nin dişi jack üzerinden breadboard bias devresine bağlandığını tarif etti: 2 × 10 kΩ dirençle orta nokta ve orta noktadan GND'ye 104 (100 nF) kondansatör. Bu bağlantı bilgisi tekrar sorulmayacak. ESP32'nin dahili ADC'si kullanılacak; MCP3208 sonraki aşamaya ayrılmıştır. T004 hobi kapsamındaki belgeleme olarak tamamlandı; laboratuvar düzeyinde ADC aralığı/clipping ölçümü kapanış şartı değildir.
- PZEM kaydı: mevcut [DONANIM/PZEM-004T/README.md](../../../DONANIM/PZEM-004T/README.md) esas alınır.
- Bağlı CT: PZCT-02, 0–100 A; kullanıcı tarafından model olarak belirtildi ve PZEM'e bağlı olduğu fotoğrafta gösterildi. Bu, 100 A harici CT'li yapılandırmadır.
- İlk aşamada kullanılacak ESP32 kartları: 2× WROOM-32D, 1× WROOM-32E ve 1× genel ESP-WROOM-32 NodeMCU ESP32 Bluetooth.
- Masaüstü güç kaynağı: 5 V / 1,8 A; test yükü: lamba. Kullanıcı bağlantı ve ölçüm parçalarının tamamının mevcut olduğunu bildirdi.
- 5 V, 2 kanallı SAMM Market SSR kartı proje donanımına dahil edildi (tedarikçi kodu İzmo9659, SKU MP02637). Ürün sayfası OMRON, fototriyak izolasyon, zero-cross; kanal başına 75–264 VAC ve 0,1–2 A; kart beslemesi tüm kanallar açıkken 160 mA bildiriyor. Tam SSR parça kodu, gerçek giriş tetik mantığı ve yük ataması ayrıca doğrulanacak.
- DS3231 RTC, ölçüm/olay kayıtlarına takvim zamanı sağlamak için projede kullanılacak. Önceki BERO bağlantı pinleri ve NTP örneği referanstır; bu proje için pin/başlatma kararı değildir.
- Temiz yaklaşık 1,65 V bias üretim alt devresi kullanıcı onayıyla tamamlandı: RN130421 6 V / 2 VA → KBU6M köprü → 2200 µF / 35 V → L78L33; ayrı breadboardda 2×10 kΩ ve orta noktadan GND'ye 104 kodlu 100 nF seramik. Bağımsız ölçüm raporu yoksa 1,650 V'nin cihazla ölçüldüğü iddia edilmeyecek.

Açık kalan pin/SSR/ölçüm soruları, fiziksel parçaların eksik olduğu anlamına gelmez; sonraki pin planlama ve deney aşamalarında ele alınacak proje-özel kararlardır.
