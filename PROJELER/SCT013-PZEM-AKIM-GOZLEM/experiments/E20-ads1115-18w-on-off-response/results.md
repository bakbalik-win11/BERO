# E20 — Sonuç defteri

## Durum

**PLANLANDI — fiziksel aç/kapa çevrimleri ve CSV bekleniyor.**

## Deney kimliği

- Deney: E20 — ADS1115 + SCT 18 W fiziksel aç/kapa tepki deneyi.
- Önceki baz: E19 18 W sabit yük gözlemi; ADS1115 0.078715 A, PZEM 0.079500 A, fark yaklaşık −%0.99.
- Yük: 18 W nominal; gerçek PZEM gücü ayrıca kaydedilecek.
- Ölçüm yolu: aynı SCT-013 30A/1V + ADS1115/ESP32D2; PZEM-004T V3.0 karşılaştırma kaynağı.

## Test başlamadan doldurulacak bilgiler

- Başlangıç tarihi/saat (+03:00): BEKLİYOR.
- Bitiş tarihi/saat (+03:00): BEKLİYOR.
- Firmware/YAML ve çalışan katsayı: BEKLİYOR.
- ADS1115 gain / SPS / pencere / yayın aralığı / filtre: E19 ayarları korunacak; gerçek çalışma loguyla teyit edilecek.
- SCT tur sayısı ve iletken: BEKLİYOR.
- Fiziksel anahtarlama yöntemi: BEKLİYOR; güvenli ve operatörce doğrulanabilir olmalı.
- Çevrim dizisi: başlangıç OFF 180 s; 5 × (ON 60 s + OFF 60 s); son OFF 180 s. Gerçek süreler kayıt sırasında yazılacak.

## Ham kaynaklar

Henüz CSV/log yok. Ham kaynaklar geldikten sonra dosya adı, satır sayısı, kolon/entity adları, zaman aralığı, boyut ve SHA-256 eklenecek. Ham veri değiştirilmeden korunacak.

## Çevrim sonuç tablosu

| Çevrim | Operatör ON/OFF | PZEM fiziksel doğrulama | ADS ON seviyesi | ADS OFF seviyesi | Açılma gecikmesi | Kapanma/geri dönüş | Durum |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Bekliyor | Bekliyor | — | — | — | — | Bekliyor |
| 2 | Bekliyor | Bekliyor | — | — | — | — | Bekliyor |
| 3 | Bekliyor | Bekliyor | — | — | — | — | Bekliyor |
| 4 | Bekliyor | Bekliyor | — | — | — | — | Bekliyor |
| 5 | Bekliyor | Bekliyor | — | — | — | — | Bekliyor |

## Ön karar

Test henüz yapılmadı. E20 dinamik tepki deneyi olduğu için geçiş örnekleri ±%4 kararlılık/uyum değerlendirmesine katılmaz. PZEM'in gerçek yük durumunu doğrulamadığı çevrimler geçerli fiziksel ON/OFF örneği sayılmaz. SSR/UDP olayları yalnız ayrı olay akışıdır.
