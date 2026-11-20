# E20 — Sonuç defteri

## Durum

**KAPATILDI — YAPILMADAN (2026-11-20).** E19'da hedeflenen akım ölçüm kriterleri karşılandığından E20 fiziksel aç/kapa çevrimleri proje hedefi açısından gerekli görülmedi.

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

## Kapanış kararı — 2026-11-20

## Kapanış kararı — 2026-11-20

**E20: KAPATILDI — YAPILMADAN.**

E19 kapsamında ADS1115 + SCT-013 30A/1V ölçüm zinciriyle 18 W, 42 W ve 57 W dahil düşük akım bölgesinde ölçümler alındı. Bu karşılaştırmalarda ADS1115 akım ortalaması PZEM karşılaştırma ortalamasına göre sırasıyla −%0,99, +%0,125 ve +%0,647 fark gösterdi; kayıtlı 18–150 W test koşullarının tamamı proje için belirlenen ±%4 ölçüm kriterinin içinde kaldı.

Böylece BERO'nun o aşamadaki temel ihtiyacı olan hedeflenen düşük akım bölgesinde kullanılabilir ve kriteri karşılayan akım ölçümü elde edildi. E20'nin planlanan fiziksel ON/OFF çevrimleri, bu ölçüm yeterliliğine ulaşmak için artık gerekli görülmedi. Proje odağı da E21 ile çamaşır makinesi program davranışının uzun süreli gözlemine kaydırıldı. Bu nedenle E20 için ayrıca fiziksel çevrim kaydı alınmadı ve deney **yapılmadan kapatıldı**.

### Kapanışın sınırları

- E20'nin beş fiziksel ON/OFF çevrimi gerçekleştirilmedi; açılma/kapanma gecikmesi, OFF sonrası tabana dönüş ve çevrim tekrarlanabilirliği ölçülmedi.
- E20'ye ait fiziksel test sonucu, CSV veya çevrim istatistiği yoktur.
- E19'un ±%4 sonucu yalnız kaydedilmiş sabit yük ve ölçüm koşulları için geçerlidir; E20 dinamik geçiş performansının kanıtı değildir.
- Bu karar ADS1115 A0/A1 ortak-mod ve GND–VDD giriş güvenliği doğrulamasını tamamlamaz.
- İleride dinamik geçiş davranışı yeni proje hedefi için gerekli olursa, E20 tarihçesi korunarak yeni ve güncel koşulları tanımlanmış bir deney açılabilir.

**Karar gerekçesi:** İstenen kriterlerde akım ölçümü elde edildiği için E20'nin ilave fiziksel aç/kapa deneyi proje hedefi açısından gereksiz kaldı. Deney, yapılmış veya başarılı dinamik test olarak değil, hedefe ulaşıldığı için yapılmadan kapatılmış plan olarak arşivlenir.


## Sonuç defteri notu

Fiziksel çevrim tablosundaki tüm satırlar **gerçekleştirilmedi** olarak kalır. Bekliyor alanları ölçüm sonucu değildir; E20 için CSV, geçiş gecikmesi veya çevrim istatistiği üretilmemiştir. SSR/UDP olayları yalnız ayrı olay akışıdır.
