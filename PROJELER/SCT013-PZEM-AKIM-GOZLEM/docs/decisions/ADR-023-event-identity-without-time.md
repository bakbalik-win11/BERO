# ADR-023 — Olay kimliğinde TIME alanının kaldırılması

- **Tarih:** 2026-11-01
- **Durum:** KABUL EDİLDİ — kullanıcı onayı
- **Yerine geçtiği kayıt:** ADR-022 içindeki BOOT_ID/EVENT_ID/TIME açıklaması ve TIME içeren örnek paket

## Karar

Olay mesajı yalnızca şu alanları taşır:

`BERO_EVT,BOOT_ID=<32 HEX>,EVENT_ID=N,STATE=ON|OFF`

- **BOOT_ID:** Modül 3 her boot'ta ESP32 donanımsal RNG ile 128-bit (16 byte), 32 hexadecimal karakter kimlik üretir. O boot boyunca sabit kalır.
- **EVENT_ID:** Modül 3'te her SSR durum geçişinde artan uint32 sayaçtır. Yeni boot'ta yeniden başlar.
- **STATE:** SSR'nin olay anındaki ON/OFF durumudur.
- **Eşleştirme anahtarı:** BOOT_ID + EVENT_ID.
- **TIME:** Olay mesajından ve olay kimliği üretim/eşleştirme altyapısından tamamen çıkarılmıştır. NTP/DS3231 yalnız bu olay protokolü için gerekli değildir.
- **Modül 2:** UDP mesajındaki BOOT_ID, EVENT_ID ve STATE alanlarını aynen korur; kimlik üretmez ve TIME eklemez.
- **Home Assistant:** Recorder'ın kendi kayıt timestamp'leri bu karardan etkilenmez. HA timestamp'leri kendi kayıt sistemi içinde kalabilir; ancak Modül 2 ve Modül 3 ölçümlerini eşleştirme anahtarı değildir.

## Beklenen davranış

1. Modül 3 her SSR geçişinde tek BERO_EVT üretir.
2. Aynı metin Modül 3 HA olay entity'sine yayınlanır ve UDP 4210 broadcast ile Modül 2'ye gönderilir.
3. Modül 2 aldığı metni kendi SCT akışına ayrı olay kaydı olarak ekler.
4. Python akışları BOOT_ID + EVENT_ID ile paketler; TIME alanı aramaz veya üretmez.
5. UDP işareti eksik/uyuşmazsa ilgili paket aralığı eksik sayılır; tahminle doldurulmaz.

## Önceki ADR ile ilişki

ADR-022'nin bağımsız ölçüm akışları, tek olay kaynağı, aynı olay mesajını HA ve UDP'ye yayınlama ve BOOT_ID + EVENT_ID ile paket eşleştirme kararları korunur. Yalnızca TIME alanı ve ona bağlı açıklamalar bu ADR ile geçersizdir. ADR-022 tarihsel kayıt olarak korunur; çelişki halinde ADR-023 geçerlidir.

## Doğrulama sınırı

Kullanıcının 2026-11-01 logu TIME'sız mesajın HA ve UDP gönderim loglarını gösterir. Modül 2'nin UDP alımı ve Python paketleme uygulaması henüz doğrulanmış değildir.
