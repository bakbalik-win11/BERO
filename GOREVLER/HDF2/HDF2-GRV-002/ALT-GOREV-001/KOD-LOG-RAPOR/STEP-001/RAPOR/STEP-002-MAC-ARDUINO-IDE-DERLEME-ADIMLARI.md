# STEP-002 — Mac / Arduino IDE derleme adımları
**Tarih:** 2026-10-16  
**Durum:** Hazırlık notu — kullanıcı Mac'te derleyecek; derleme sonucu henüz yok.

## Kullanılacak kod
`KOD/GRV-008.3_candidate_safety_patch.ino`

Orijinal `GRV-008.2_candidate.ino` dosyasını değiştirme. Aday kodu ayrı tut.

## 1. Arduino IDE
- Arduino IDE 2.x aç.
- Boards Manager'dan **esp32 by Espressif Systems** kart paketini kontrol et.
- ESP32 klasik WROOM için `ESP32 Dev Module` kartını seç.
- Kart paketinin sürümünü not et. Kod ESP-IDF ADC Continuous API kullandığı için eski Arduino-ESP32 2.x kurulumuyla uyumlu olacağı varsayılmamalı; derleme sonucu belirleyici olacak.

## 2. Sketch'i hazırlama
- Yeni sketch aç: `GRV_008_3_candidate_safety_patch`.
- Depodaki `GRV-008.3_candidate_safety_patch.ino` dosyasının tamamını sketch dosyasına kopyala.
- Kaydet. Arduino IDE sketch klasörü ve ana `.ino` dosyası aynı adı taşımalı.

## 3. Derleme
- ESP32D1 USB ile bağlı değilse bu aşamada bağlamak şart değil; önce **Verify / ✓** ile derle.
- Hata olursa hatanın tamamını, özellikle ilk `error:` satırından başlayarak kopyala. Sadece son satırı gönderme.
- Derleme başarılıysa IDE sürümü, esp32 kart paketinin sürümü ve `Sketch uses...` / `Global variables use...` özetini kaydet.

## 4. Henüz yapma
- Derleme başarılı olmadan karta yükleme yapma.
- Python alıcısını başlatma.
- GPIO34/35'e veya analog devreye bağlantı değişikliği yapma.

## Önemli teknik not
Bu sketch adaydır. Derleme başarılı olması, 10 kHz/kanal örnekleme, callback güvenliği, binary frame bütünlüğü veya fiziksel ölçüm doğruluğunu kanıtlamaz. Bunlar ayrı test edilecek.
