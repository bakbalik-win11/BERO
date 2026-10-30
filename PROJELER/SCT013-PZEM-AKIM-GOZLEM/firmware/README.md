# ESP32D2 / SCT013-030 — çalışan ct_clamp yapılandırması

## HEDEF

ESP32D2 üzerindeki SCT013-030 ölçümünü ESPHome'un hazır `ct_clamp` platformuyla almak; bir kez yapılan katsayı ayarından sonra farklı yüklerde davranışı gözlemlemek. Bu dosya, 2026-10-30 tarihinde kullanıcı tarafından cihaza yüklenip log çıktısı alınan yapılandırmanın depo kopyasıdır.

## KOD

- [esp32d2.yaml](esp32d2.yaml)
- Cihaz kimliği: `esp32d2` (değiştirilmedi).
- ESPHome: 2026.9.1 (cihaz logu).
- ESP32: klasik ESP32, ESP-IDF.
- SCT: SCT013-030, 30 A / 1 V.
- Bağlantı: SCT013-030 → mevcut yaklaşık 1.65 V bias devresi → GPIO33.
- ADC: GPIO33 / ADC1 / 12 dB.
- `ct_clamp`: 200 ms örnekleme penceresi, 2 s yayın aralığı.
- Katsayı: 24.22.
- Yayın eşiği: 0.35 A; altındaki değerler sıfırlanır.

## ÖNEMLİ KOD NOTU

Kullanıcının yapıştırdığı ilk açıklama bloğunda eşik 0.30 A yazıyordu; aynı YAML içindeki lambda gerçekte 0.35 A uyguluyordu. Depoya kaydedilen sürümde yalnızca açıklama metni, çalışan lambda ile tutarlı olması için 0.35 A olarak düzeltildi. Çalışan ölçüm mantığı, katsayı, pin ve cihaz adı değiştirilmedi.

## LOG VE GÖZLEM ÖZETİ — 2026-10-30

Aşağıdaki değerler kullanıcı tarafından paylaşılan cihaz logları ve pens ampermetre okumalarından derlenmiştir. Pens değerleri kullanıcı raporudur; burada bağımsız bir referans cihazı doğrulaması iddia edilmez.

| Koşul | Pens ampermetre | ESP32 çıktısı | Yorum |
|---|---:|---:|---|
| Yüksüz | 0 A varsayılan koşul | 6/6 yayın 0.000 A; ham AC 0.006–0.009 | Eşik, bu kısa yüksüz kesitte istenmeyen yayınları bastırdı. |
| 150 W akkor lamba | 0.616 A | yaklaşık 0.615 A ortalama | Yaklaşık −%0.2 fark; ±%4 hedefinin içinde. |
| Kettle, düşük/kararlı çalışma kesiti | 0.637 A civarı | yaklaşık 0.656 A ortalama (ilk 20 değer) | Yaklaşık +%3.0; ±%4 hedefinin içinde. |
| Kettle, kaynama | 6.39 A | yaklaşık 6.15 A ortalama (22 yayın) | Yaklaşık −%3.8; ±%4 hedefinin içinde. |
| 8.35 W LED | 0.041 A | çoğu yayın 0.000 A; ara sıra 0.508 A ve 0.372 A sıçramaları | 0.35 A eşiği 41 mA gerçek yükü gizliyor. Sıçramalar gerçek akım olarak kabul edilmedi. |

### Log kanıtları

- Kettle kaynama kesiti: [cihaz logu, 20:31:13–20:31:55](https://github.com/bakbalik-win11/BERO/blob/main/PROJELER/SCT013-PZEM-AKIM-GOZLEM/experiments/E08-sct-characterization/README.md) — konuşmada paylaşılan log satırları 275–318.
- LED açık/kapalı kesiti: konuşmada paylaşılan log satırları 73–184; LED açıkken pens değeri kullanıcı tarafından 0.041 A bildirildi.
- Ham dosyalar bu committe depoya yüklenmedi; yukarıdaki özet kullanıcı tarafından sağlanan sohbet loglarından çıkarılmıştır.

## SONUÇ

- 24.22 katsayısı ve 0.35 A eşiğiyle 150 W akkor ve kettle ölçümlerinde gözlenen sapmalar yaklaşık ±%4 hedefinin içinde kaldı.
- Bu, farklı yüklerde olumlu saha gözlemidir; bütün akım aralığında doğruluk garantisi değildir.
- 41 mA LED yükü mevcut eşik nedeniyle ölçüm çıktısında görünmüyor. Düşük akım davranışı açık konudur.
- Katsayı bu kayıt nedeniyle değiştirilmedi.
- Kodun depo kopyası kaydedildi; bu oturumda YAML derlemesi veya cihaza yeniden yükleme yapılmadı. Cihaz logları kullanıcının daha önce çalıştırdığı yapılandırmayı gösterir.

## SONRAKİ ADIM

Mevcut katsayıyı koruyarak, düşük akımın sıfırlanması ve ara sıra görülen sıçramalar konusunu ayrı ele almak. Çalışan `ct_clamp` paketini gereksiz yere yeniden yazmamak.
