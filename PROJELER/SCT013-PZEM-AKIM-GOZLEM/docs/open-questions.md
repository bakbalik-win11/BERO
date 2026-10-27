# Açık sorular

Aşağıdaki sorular yalnız bu projede hâlâ cevaplanmamış proje-özel konulardır. Genel donanım bilgileri [referans klasöründe](../hardware/references/README.md) ve ana BERO `DONANIM/` belgelerinde mevcuttur.

1. İlk aşamada kullanılacak ESP32 kartında SCT sinyalinin okunacağı ADC destekli GPIO numarası nedir? Harici ADC kullanılmayacak; analog örnekleme ESP32'nin dahili ADC işleviyle yapılacak. Seçilen kartın pin yeteneği ve güvenli giriş aralığı doğrulanmalı.
2. SCT013-030 AC sinyali tamamlanmış yaklaşık 1,65 V bias orta noktasına hangi bağlantı/kuplaj elemanıyla eklenecek?
3. 8 kanallı hazır karttaki kanal başına direnç/bias ağı ve analog filtre değerleri ile ADC girişinin güvenli maksimum aralığı nedir? Nihai bağlantı kanıtı kaydı eksik.
4. SAMM Market 5 V 2 kanallı SSR kartının hangi iki AC yükü anahtarlayacağı ve hangi ESP32 GPIO'larının kullanılacağı nedir? Ürün sayfasındaki LOW/HIGH eşikleri ile “low-level trigger” notu tutarsız olabildiğinden kontrol mantığı düşük gerilimde doğrulanmalı; giriş akımı ve kanal başına termal/sürekli yük sınırları ayrıca teyit edilmeli.
7. PZEM'in iç ölçüm/ortalama penceresi nedir; V, I, P ve PF aynı anda mı yenileniyor? Bunlar deneyle ölçülecek.
8. Hangi akımın altında PZEM, bağımsız referansa göre kabul edilemez sapma/kararsızlık gösteriyor?
9. 1 kS/s, 2 kS/s ve 2,5 kS/s seçenekleri arasında hedef yüklerde anlamlı performans farkı var mı?
10. 200 ms pencere kararlı yükte tekrarlanabilir mi; çevrime senkron pencere gerekli mi?

**Karara bağlandı; yeniden sorulmayacak:**
- Eğitim/etiket referansı PZEM-004T V3.0'dır. Açık kalan konu, SCT modelinin PZEM okumalarını değerlendirmek için kullanılacak hata ölçütleri ve kararlı alan koşullarıdır.
- DS3231: kullanıcı beyanı — RTC kodu çalıştı, güç kesilip yeniden verildikten sonra saat korundu; iki modülde de 2032 tipi pil var. Bu test ve pil bilgisi tekrar istenmeyecek.
- Deney yükleri önceden sabitlenmeyecek; kullanıcı her testte kullandığı yükü ve koşulları beyan edecek.
- Öncelikli sensör: SCT013-030 (30 A / 1 V).
- Kullanıcı stok bildirimi: 7 adet SCT013 30 A / 1 V ve 10 adet SCT013 100 A / 1 V; ikisi de jack çıkışlı. Jack yuvaları mevcut.
- Kullanıcı daha önce **8 kanallı, her kanalında ayrı bias ve direnç ağı bulunan bir analog arayüz kartı** hazırladı. Bu ilk aşamada harici ADC kullanılmayacak; SCT sinyali jack yuvası ve breadboard üzerindeki bias devresi üzerinden ESP32'nin ADC destekli GPIO girişinden okunacak. Bu, ESP32'nin dahili ADC'sinin kullanılması demektir. MCP3208 fiziksel olarak mevcut; ileriki aşama için ayrıldı. İlk aşamada kullanılmayacak. Kartın kanal şeması veya elektriksel değerleri doğrulanmış sayılmaz.
- PZEM kaydı: mevcut [DONANIM/PZEM-004T/README.md](../../../DONANIM/PZEM-004T/README.md) esas alınır.
- Bağlı CT: PZCT-02, 0–100 A; kullanıcı tarafından model olarak belirtildi ve PZEM'e bağlı olduğu fotoğrafta gösterildi. Bu, 100 A harici CT'li yapılandırmadır.
- İlk aşamada kullanılacak ESP32 kartları: 2× WROOM-32D, 1× WROOM-32E ve 1× genel ESP-WROOM-32 NodeMCU ESP32 Bluetooth.
- Masaüstü güç kaynağı: 5 V / 1,8 A; test yükü: lamba. Kullanıcı bağlantı ve ölçüm parçalarının tamamının mevcut olduğunu bildirdi.
- 5 V, 2 kanallı SAMM Market SSR kartı proje donanımına dahil edildi (tedarikçi kodu İzmo9659, SKU MP02637). Ürün sayfası OMRON, fototriyak izolasyon, zero-cross; kanal başına 75–264 VAC ve 0,1–2 A; kart beslemesi tüm kanallar açıkken 160 mA bildiriyor. Tam SSR parça kodu, gerçek giriş tetik mantığı ve yük ataması ayrıca doğrulanacak.
- DS3231 RTC, ölçüm/olay kayıtlarına takvim zamanı sağlamak için projede kullanılacak. Önceki BERO bağlantı pinleri ve NTP örneği referanstır; bu proje için pin/başlatma kararı değildir.
- Temiz yaklaşık 1,65 V bias üretim alt devresi kullanıcı onayıyla tamamlandı: RN130421 6 V / 2 VA → KBU6M köprü → 2200 µF / 35 V → L78L33; ayrı breadboardda 2×10 kΩ ve orta noktadan GND'ye 104 kodlu 100 nF seramik. Bağımsız ölçüm raporu yoksa 1,650 V'nin cihazla ölçüldüğü iddia edilmeyecek.

Bu soruların açık kalması, fiziksel parçaların eksik olduğu anlamına gelmez; envanter/analog ön uç için proje-özel teknik karar veya ölçüm kanıtı beklendiğini belirtir.
