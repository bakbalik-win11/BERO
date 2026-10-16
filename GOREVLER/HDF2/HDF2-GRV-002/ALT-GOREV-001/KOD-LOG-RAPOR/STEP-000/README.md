# STEP-000 — Görev ve kayıt yapısı

**Durum:** TAMAMLANDI

Bu step, Alt Görev 1'in kayıt klasörlerinin ve ilerleme raporu yapısının oluşturulmasını kapsar.

- `KOD/` — firmware ve Python kodları
- `LOG/` — derleme ve fiziksel test logları
- `RAPOR/` — step raporları ve ana ilerleme raporu

Kanıt: Alt görev klasörü ve kayıt dizini GitHub'da oluşturuldu.


# STEP-000 — Görev ve kayıt yapısı

**Durum:** TAMAMLANDI

## Amaç
Alt görev için step bazlı klasörleri ve ilerleme raporu bağlantılarını oluşturmak.

## Planlanan işler
1. KOD, LOG ve RAPOR kayıt düzenini belirle.
2. Step klasörlerini ve görev tanımlarını aç.
3. İlerleme raporunu step klasörlerine bağla.

## Tamamlanan işler
- [x] Step klasörleri oluşturuldu.
- [x] İlerleme raporu bağlantıları eklendi.

## Kapanış ölçütü
Kayıt düzeni ve step dizini mevcut.

## Çalışma kaydı
Her tamamlanan işin tarihi, kullanılan kod sürümü, test sonucu ve kanıt bağlantısı aşağıya alt alta eklenecek. Step ancak kapanış ölçütü kanıtlandığında kapatılacak.

## 2026-10-16 — PZEM / SSR / Home Assistant kayıtlarının doğrulanması

Öncelik, yüksek hızlı USB/ham veri testlerine geçmeden önce mevcut çalışan PZEM–SSR–Home Assistant zincirinin gerçek durumunu kanıtlamaktır. Kullanıcının sağlayacağı mevcut ESPHome YAML dosyaları ve loglar esas alınarak (1) PZEM ölçümlerinin Home Assistant'a ulaşıp güncellendiği, (2) SSR açma/kapama olaylarının nerede üretildiği ve nasıl kaydedildiği, (3) bu iki veri akışının ayrı ayrı zaman damgasıyla tutulup tutulmadığı, (4) SSR olayları ile PZEM ölçümlerinin aynı deney/olay kimliğiyle ilişkilendirilmeye uygunluğu ve (5) mevcut kayıtların kanıt olarak saklanması incelenecektir. Eksik kanıtlar varsayımla tamamlanmayacak; çalışan kodlar görülmeden değiştirilmeyecek. Gerekirse yalnızca doğrulanan eksik için kod değişikliği yapılacak; ilgili YAML/kod sürümü, test logu ve sonuç raporu STEP-000 altında saklanacaktır. Şu anki durum: YAML ve loglar kullanıcı tarafından henüz bu inceleme için sunulmadı; doğrulama yapılmış veya PASS alınmış sayılmaz.

## 2026-10-16 — ESP32-C3-SSR YAML ve log incelemesi

Kullanıcının verdiği YAML ve ESPHome logu STEP-000 altında ESP adıyla arşivlendi; kod ve loga dayalı test raporu eklendi.

- Klasör: [ESP32-C3-SSR](./ESP32-C3-SSR/)
- YAML: [esphome-web-0424f4.yaml](./ESP32-C3-SSR/esphome-web-0424f4.yaml)
- Log: [ESP32-C3-SSR-LOG-2026-10-16.txt](./ESP32-C3-SSR/ESP32-C3-SSR-LOG-2026-10-16.txt)
- Rapor: [ESP32-C3-SSR-TEST-RAPORU-2026-10-16.md](./ESP32-C3-SSR/ESP32-C3-SSR-TEST-RAPORU-2026-10-16.md)

**Sonuç:** Kullanıcı fiziksel ON/OFF uyumunu gözle gördüğünü bildirdi. Logda zaman damgalı ON/OFF olayları ve UDP gönderim kayıtları mevcut. DS3231 iletişim/yazma hatası ile ON sırasındaki GPIO geri okuma uyuşmazlığı raporlandı; kullanıcı kararıyla şimdilik beklemede. UDP alıcı teyidi ve Home Assistant geçmişinde kalıcı kayıt henüz bu logla kanıtlanmış değil. YAML değiştirilmedi; bu rapor bir PASS/derleme beyanı değildir.


## 2026-10-16 — İki ESP'nin Home Assistant'a ayrı bağlanması

- Plan ve doğrulama listesi: [STEP-000-HA-IKI-ESP-BAGLANTI-PLANI-2026-10-16.md](./STEP-000-HA-IKI-ESP-BAGLANTI-PLANI-2026-10-16.md)
- PZEM ESP: `192.168.0.52` — YAML içinde `api:` mevcut; ESPHome logunda API bağlantısı ve PZEM ölçümleri görülüyor.
- SSR ESP: `192.168.0.111` — YAML içinde `api:` mevcut; ESPHome logunda API bağlantısı görülüyor.
- **İlk kayıt durumu:** HA arayüzünde ayrı cihazlar ve entity güncellemeleri o sırada henüz doğrulanmamıştı.


## 2026-10-16 — Home Assistant veri akışı doğrulandı

Kullanıcının Home Assistant ekran görüntüleri ve dışa aktardığı geçmiş CSV dosyaları incelendi.

### ESP32-WR1-PZEM
- Home Assistant cihaz sayfasında PZEM Gerilim, Akım, Güç, Enerji, Frekans ve Güç Faktörü sensörleri değerleriyle göründü.
- Örnek cihaz ekranı değerleri: Gerilim 227,2 V; Akım 0,000 A; Güç 0,00 W; Enerji 10.638 Wh; Frekans 49,9 Hz; Güç Faktörü 0,00.
- Home Assistant geçmiş CSV'sinde gerilim ölçümlerinin zaman damgalı kayıtları görüldü.
- Lamba açıldıktan sonraki CSV'de sıfır olmayan akım ve güç örnekleri de bulundu; yaklaşık 0,051 A ve 7,7 W örnekleri görüldü.
- Bu kanıtlar PZEM ölçümlerinin HA'ya ulaştığını ve en azından bazı sensörlerin geçmişe kaydedildiğini doğrular.
- Sensörlerin kayıt sayıları farklıydı. Bunun nedeni kesinleştirilmedi; sıfır değerlerin kaydedilmediği varsayımı kanıtlanmış değildir.

### ESP32-C3-SSR
- Home Assistant cihaz sayfasında `BERO SSR Kontrol` anahtarı, `BERO NTP Saat` ve `BERO DS3231 RTC Saat` varlıkları göründü.
- Ekran görüntüsünde SSR kontrol durumu `Kapalı` olarak, NTP ve RTC saatleri güncel zaman değerleriyle görünüyordu.
- Cihazın etkinlik alanında zaman damgalı saat güncellemeleri ve SSR kontrol durumuna ait kayıtlar görüldü.
- Bu, SSR cihazının HA'da temsil edildiğini ve ilgili varlıkların veri sunduğunu doğrular. UDP olay paketlerinin HA'da ayrı ve kalıcı olay kayıtları olarak tutulduğu henüz doğrulanmadı.

### Sonuç ve kapanış
**Doğrulanan:** İki ESP de HA'da ayrı cihaz olarak kayıtlıdır; PZEM ölçümleri HA'ya ulaşıyor ve geçmişte kayıtlar mevcut; SSR kontrolü ile saat varlıkları HA'da görünür ve güncellenmektedir.

**Açık kalan:** PZEM sensörlerinin neden farklı sayıda geçmiş kaydı ürettiğinin açıklanması; SSR UDP olaylarının HA'da ayrı kalıcı olay kaydına dönüştürülmesi ve PZEM ölçümleriyle zaman/deney kimliği üzerinden eşleştirilmesi.

**Kod değişikliği:** Yapılmadı. Mevcut çalışan firmware ve cihaz adları korunmuştur.

**Sonraki çalışma:** STEP-000'daki mevcut sistem doğrulaması tamamlandı. Üç okuma ESP'si için sonraki adıma geçilebilir; STEP-001'in klasör/başlık yapısı repo içinde ayrıca kontrol edilerek devam noktası netleştirilmelidir.
