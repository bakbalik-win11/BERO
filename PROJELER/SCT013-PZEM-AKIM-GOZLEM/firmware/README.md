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
| Kettle, düşük/kararlı çalışma kesiti | 0.637 A (kullanıcı pens bildirimi) | İlk 20 yayın ortalaması yaklaşık 0.656 A | Yaklaşık +%3.0; ±%4 hedefinin içinde. |
| Kettle, kaynama kesiti | 6.39 A (kullanıcı pens bildirimi) | 22 yayın ortalaması yaklaşık 6.15 A | Yaklaşık −%3.8; ±%4 hedefinin içinde. |
| Sonraki log kesiti; yük adı/koşulu teyitsiz | 0.437 A (kullanıcı bildirimi) | 74 yayın ortalaması 0.664 A; son değer 0.910 A; son sıçrama hariç ortalama 0.660 A | Referansla fark yaklaşık +%52. Bu kesit kettle sonucu olarak etiketlenmedi; koşul ve eşzamanlı pens okuması teyit edilmeden katsayıya müdahale edilmez. |
| 8.35 W LED | 0.041 A | çoğu yayın 0.000 A; ara sıra 0.508 A ve 0.372 A sıçramaları | 0.35 A eşiği 41 mA gerçek yükü gizliyor. Sıçramalar gerçek akım olarak kabul edilmedi. |


### Kettle karşılaştırmasının ayrıntısı

- **Düşük/kararlı kettle kesiti:** Pens 0.637 A; ESP32'nin ilk 20 yayını ortalama yaklaşık 0.656 A. Fark yaklaşık +0.019 A / +%3.0. Kullanıcının ±%4 kabul sınırının içinde.
- **Kaynama kesiti:** Pens 6.39 A; ESP32 tarafında 22 yayının ortalaması yaklaşık 6.15 A. Fark yaklaşık −0.24 A / −%3.8. Yuvarlama ve pens okumasının kullanıcı tarafından bildirilmiş olması dikkate alınmalıdır; sonuç sınırın içinde fakat sınıra yakındır.
- **Daha sonraki 0.437 A pens bildirimi:** Bu değere ait paylaşılan 74 yayınlık logun ortalaması 0.664 A, son 0.910 A sıçraması çıkarıldığında 0.660 A'dır. Bu kayıt kettle olarak doğrulanmadığından kettle satırlarına karıştırılmadı. İki ölçüm aynı yükte ve aynı zaman aralığında alınmış mı, henüz belli değil. Bu nedenle uyum sonucu çıkarılamaz ve katsayı değiştirilmez.

### Log kanıtları

- Kettle kaynama kesiti: konuşmada paylaşılan cihaz logu, 20:31:13–20:31:55, satırlar 275–318 (ham log henüz depoya eklenmedi).
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
