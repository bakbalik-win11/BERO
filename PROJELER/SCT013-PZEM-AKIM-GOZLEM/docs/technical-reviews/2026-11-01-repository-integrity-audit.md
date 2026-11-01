# 2026-11-01 — BERO SCT013/PZEM depo bütünlük denetimi

## Denetim kapsamı

- GitHub deposu: bakbalik-win11/BERO, varsayılan dal: main.
- Denetlenen proje kökü: PROJELER/SCT013-PZEM-AKIM-GOZLEM.
- İlk envanter: 264 dosya. Bu oturumda iki olay kanıt dosyası ve bir bütünlük denetimi raporu eklendi; güncel ağaçta 267 dosya var.
- Ağaç envanteri çıkarıldı; proje README/AGENTS/STATUS/ROADMAP/PROGRESS_TREE, firmware README, Modül 2/3 YAML kaynakları, T009/T010/T007/T008, ADR-019/022/023, Python mimari belgeleri ve ilgili deney/olay analizleri incelendi.
- 266 dosyanın tüm ham logları ve tarihsel arşivleri satır satır yeniden analiz edilmiş değildir. Büyük deney/log arşivleri tarihsel kayıt olarak bırakıldı; aktif mimari ve güncel kod bağlantıları öncelikli denetlendi.

## Düzeltilen bütünlük sorunları

1. Ana README'de eski ADR-019 yaklaşımından kalan timestamp kesişimiyle eğitim eşleştirme açıklaması, ADR-022 paket kimliği yaklaşımıyla değiştirildi.
2. Ana README'deki olay alanları paket/zaman/SSR ifadesinden TIME'sız BERO_EVT/BOOT_ID/EVENT_ID/STATE protokolüne hizalandı.
3. Python mimari belgesinde ADR-019 timestamp-kesişim bölümü ADR-022/023 geçerli kurallarıyla değiştirildi; eski ADR-019 bölümü tarihsel ve geçersiz olarak işaretlendi.
4. Eğitim/dinamik gözlem belgesinin eski sürekli ham ADC ve timestamp hizalama önerileri güncel politika değildir; belge başına açık tarihsel/superseded notu eklendi.
5. T009 çalışma sırasındaki TIME alanı gerekliliği kaldırıldı; güncel olay kimliği ve TIME'sız protokolle hizalandı.
6. Modül 2 YAML başlığı, eski LOAD-15W-003 UNIT kıyas deneyinden güncel üç-SCT + UDP 4210 olay alıcısı işlevine göre düzeltildi. YAML çalışma mantığı değiştirilmedi.
7. Modül 3 YAML başlığındaki henüz derlenmedi/yüklenmedi ifadesi gerçek cihaz loglarıyla uyumlu hâle getirildi; fiziksel SSR anahtarlaması doğrulanmış gibi sunulmadı.
8. Firmware README'ye güncel Modül 2/Modül 3 düğüm rolleri, pinler, olay protokolü ve doğrulama sınırları eklendi.
9. ADR-023'e gerçek Modül 2 olay alımı ve HA History ekran görüntüsü kanıtı eklendi.
10. STATUS, PROGRESS_TREE, ROADMAP ve HISTORY/SESSION_LOG yeni kanıt ve açık sınırlarla güncellendi.

## Güncel protokol

- Mesaj: BERO_EVT,BOOT_ID=<32 HEX>,EVENT_ID=N,STATE=ON|OFF
- BOOT_ID: Modül 3 tarafından her boot'ta üretilen 128-bit kimlik; o boot boyunca sabit.
- EVENT_ID: Modül 3'te her SSR durum geçişinde artan uint32 sayaç.
- Eşleştirme anahtarı: BOOT_ID + EVENT_ID.
- TIME olay protokolünde yoktur.
- Modül 3 aynı olay metnini kendi HA olay entity'sine ve UDP 4210 broadcast'e yollar.
- Modül 2 aldığı olay metnini kendi HA olay entity'lerine aktarır; kimliği yeniden üretmez.
- SCT ve PZEM ölçüm akışları ayrı kalır. Python paketleri BOOT_ID + EVENT_ID ile eşleştirir; her ölçüm akışının kararlılığını kendi verisinden bağımsız belirler. Timestamp iki sensörün örneklerini eşleştirme anahtarı değildir.

## Son olay kanıtı

- Modül 2 uzun logu: 1.809 satır / 145.178 bayt; SHA-256 e125e3d471a70abb63407d1ee9c6db82336780fbd93bc26e6f9481681e24dece.
- Aynı BOOT_ID altında 59 ON, 61 ON, 62 OFF ve 64 OFF paketleri UDP alındı ve HA yayın çağrısı yapıldı.
- 60 ve 63 bu alıcı logunda görünmüyor. Tüm olayların kayıpsız teslimi doğrulanmış değildir.
- Ayrı HA History ekran görüntüsünde 70 OFF ve 71 ON olayları iki modülün olay kayıtlarında; Modül 2 STATE entity'leri ve SSR entity'sinin mantıksal Kapalı/Açık durumları görünüyor.
- 69 numarası görüntüde var, fakat STATE/ham paket satırı görünmediği için durumu kaydedilmedi.
- Fiziksel SSR kontak/yük anahtarlaması ve Recorder DB'nin yeniden başlatma sonrası kalıcılığı bu kanıtlarla doğrulanmış değildir.

Ayrıntı: [uzun ON/OFF log analizi](../logs/module2/2026-11-01-module2-on-off-extended-analysis.md) ve [seçilmiş kanıt](../logs/module2/2026-11-01-module2-on-off-extended-evidence.log).

## Bulunan tarihsel çakışmalar

- ADR-017 numarası iki dosyada, ADR-018 numarası iki dosyada kullanılmıştır. Mevcut dosya slug'ları ve bağlantılar bozulmaması için yeniden adlandırılmadı. Bu durum karar indeksinde açıkça kaydedildi; yeni ADR numaraları 024'ten devam etmelidir.
- ADR-019 tarihsel olarak korunur; timestamp kesişimiyle sensör örneği eşleştirme yaklaşımı ADR-022 ile geçersizdir.
- ADR-022 içindeki TIME alanı açıklaması ve örnek mesaj ADR-023 ile geçersizdir.
- Eski STATUS/HISTORY girdileri silinmedi. En yeni kayıtlar dosyaların başına eklenerek önceki durumların tarihsel olduğu açıklandı.

## Açık kalan doğrulama işleri

| Konu | Durum |
|---|---|
| Modül 2 UDP ON/OFF alımı | Çoklu olaylar için log ile doğrulandı; 60/63 eksik |
| Modül 2 HA event publish | Alınan dört olay için log ile doğrulandı |
| Modül 2/3 HA History | 70 OFF / 71 ON ekran görüntüsüyle desteklendi |
| Bütün UDP olaylarının kayıpsızlığı | Doğrulanmadı |
| Fiziksel SSR anahtarlaması | Doğrulanmadı |
| HA Recorder DB kalıcılığı / yeniden başlatma sonrası kontrol | Doğrulanmadı |
| Güncel YAML ile çalışan binary'nin byte-byte eşitliği | Doğrulanmadı |
| Güncel Modül 2/3 YAML bağımsız ESPHome config check/derleme | Bu denetimde yapılmadı |
| Python T007 HA export | Beklemede |
| Python T008 paketleme/kararlılık/etiketleme | Beklemede |
| T006 K=24.22/model değerlendirmesi | T007/T008 verisi bekleniyor |

## Değişiklik sınırı

Bu denetimde firmware mantığı veya pin/katsayı/örnekleme ayarları değiştirilmedi. Modül 2 YAML'da yalnız açıklama başlığı düzeltildi. Modül 3 YAML'da yalnız test durumunu anlatan yorum güncellendi. Yeni derleme, OTA veya fiziksel deney yapılmadı.

## Sonuç

Aktif mimari belgeleri ve güncel firmware açıklamaları TIME'sız BOOT_ID + EVENT_ID protokolüne göre hizalandı. Olay alımının çoklu ON/OFF kanıtı depoya işlendi. Depoda bilinen tarihsel ADR numara tekrarları açıkça belgelendi. Python veri hattı, kayıpsız UDP teslimi ve fiziksel SSR doğrulaması tamamlanmış değildir; bu nedenle proje bütünüyle tamamlandı olarak işaretlenmemiştir.
