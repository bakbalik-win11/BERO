# BERO — Yükler ve karma yükler karşılaştırmalı sonuç tablosu

**Tarih:** 2026-10-31  
**Düzenek ağırlığı:** Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35; ESPHome 2026.10.1; K=24.22. Eski Faz 1 ESP32D2 kaydı ayrı belirtilmiştir.

## Okuma yöntemi ve önemli ayrım

- **Referans farkı (%)** = (SCT ortalaması − referans) / referans × 100. Referans UNIT ise kullanıcı tarafından bildirilen UNIT değeridir; PZEM değildir.
- Referansla aynı kararlı zaman penceresi doğrulanmadıysa yüzde fark yalnız **aritmetik/betimleyici farktır**, doğruluk hatası değildir.
- **Kendi iç kararlılığı** için örnek SD ve CV = SD / SCT ortalaması × 100 kullanılır. CV düşükse o oturumun okumaları kendi ortalaması çevresinde daha sıkıdır. CV, referansa doğruluğu göstermez.
- BERO deney kuralı: 0,30 A altındaki bölgede ±%4 kabul/ret uygulanmaz. 0,30 A ve üzeri için de ±%4 yalnız eşleşmiş kararlı referans varsa anlamlı kabul değerlendirmesidir.
- PZEM karşılaştırması yapılmış bir satır bu tabloda yoktur; kayıtlı referans karşılaştırmaları UNIT veya tarihsel referanstır.

## A. Tekil yükler

| Yük / test | Referans (kaynak) | SCT ort. / medyan | Referans farkı | Kendi iç kararlılığı | Yorum |
|---|---:|---:|---:|---:|---|
| 100 W akkor — Faz 1 ESP32D2 | Pens 0,446–0,447 A | 0,4471 A | yaklaşık +%0,02…+%0,25 | SD/CV yok | Tarihsel baseline; ham log yok |
| 100 W — LOAD-100W-002 | UNIT 0,427 A | 0,589 A (son 5 kararlı yayın) | +%37,9 | SD/CV yok | Belirgin yüksek; özet log |
| 100 W — LOAD-100W-003 | UNIT geçici 0,427 A | 0,4841 / 0,460 A | ort. +%13,35; medyan +%7,7 | SD/CV raporlanmamış | 10/160 yayın 0,55 A üstünde; sıçramalı |
| 100 W — LOAD-100W-004 | UNIT geçici 0,427 A | 0,425 / 0,423 A | ort. −%0,47; medyan −%0,94 | SD 0,01149 A; CV %2,70; aralık 0,401–0,480 A | 192/215 (%89,3) ±%4 bandında; bu en iyi kayıtlı 100 W Modül 2 oturumu |
| 150 W akkor — Faz 1 | Tarihsel referans 0,616 A | 0,615 A | −%0,2 | SD/CV yok | Tarihsel karşılaştırma |
| 150 W — LOAD-150W-001 | UNIT 0,5985 A | 0,60821 / 0,608 A | +%1,62 | SD 0,006595 A; CV %1,08; aralık 0,591–0,655 A | 388/391 (%99,23) UNIT ±%4 bandında |
| FAN-1 | UNIT 0,093 A | 0,146757 / 0,147 A | +%57,8* | SD 0,026064 A; CV %17,76; aralık 0,064–0,259 A | Düşük akım; ±%4 uygulanmaz. Kendi iç dağılımı geniş |
| FAN-2 | UNIT 0,106 A | 0,168969 / 0,1685 A | +%59,4* | SD 0,024640 A; CV %14,58; aralık 0,108–0,257 A | Düşük akım; ±%4 uygulanmaz |
| FAN-3 tek tur | UNIT 0,141 A | 0,224612 / 0,223 A | +%59,3* | SD 0,018657 A; CV %8,31; aralık 0,189–0,311 A | Düşük akım; 253/255 yayın 0,30 A altında |
| FAN-3 üç tur, gösterge/3 | UNIT 0,142 A | 0,137965 / 0,137667 A | −%2,84* | SD/CV normalize edilmiş seri için raporlanmamış; sıçrama hariç gösterge 0,392–0,454 A | Deneysel /3 normalizasyonu; kalibrasyon veya 3x doğrusallık kanıtı değil |
| 42 W ampul — Log 57 | UNIT 0,174 A | 0,252438 / 0,251 A | +%45,08* | SD 0,011038 A; CV %4,37; aralık 0,221–0,295 A | 0,30 A altı düşük akım; ±%4 yok |
| 57 W akkor — Log 58 | UNIT 0,244 A | 0,304207 / 0,303 A | +%24,67* | SD 0,009126 A; CV %3,00; aralık 0,284–0,348 A | Kısa oturumda blok ortalamaları 0,3022–0,3061 A |
| 0,130 A hedefli yük — Log 56 | 0,130 A hedef; cihaz/yük kimliği teyitsiz | 0,203637 / 0,203 A | Hesaplanmadı | SD 0,017971 A; CV %8,82; aralık 0,157–0,291 A | UNIT/PZEM referansı değil; hedef ile ölçümü hata diye kıyaslamak doğru değil |
| Tost makinesi — TOASTER-001 Log 62 | UNIT 7,89 A | 7,1900 / 7,188 A | −%8,87* | SD 0,0247 A; CV %0,344; aralık 7,135–7,264 A | Çok dar kısa dönem dağılım; UNIT zaman eşleşmesi yok, PZEM yok |
| Yüksüz — LOAD-IDLE-001 uzun log | Referans aranmadı | 0,017130 / 0,000 A | Uygulanmaz | SD/CV raporlanmamış; 146/200 (%73) sıfır; aralık 0–0,144 A | Boşta taban davranışı; yük akımı doğruluğu değil |

* Yıldızlı farklar zaman eşleşmesi doğrulanmadığından **hata oranı değil, UNIT bildirimiyle aritmetik farktır**. Düşük akım satırlarında ±%4 kabul/ret yapılmaz.

## B. Birleşik yükler

| Birleşik yük / test | Referans (UNIT) | SCT ort. / medyan | Referans farkı | Kendi iç kararlılığı | Yorum |
|---|---:|---:|---:|---:|---|
| 100 W akkor + FAN-3 — MIXED-LOAD-001 | 0,573 A | 0,582456 / 0,582 A | +%1,65 | SD 0,007335 A; CV %1,26; aralık 0,564–0,609 A | 130/136 (%95,59) UNIT ±%4 bandında; PZEM/PF yok |
| 57 W akkor + 15 W ampul — MIXED-LOAD-57W-15W-001 | 0,303 A | 0,329553 / 0,328 A | +%8,76 | SD 0,014762 A; CV %4,48; aralık 0,303–0,436 A | Teste özel ±%5,6 bandında 31/179 (%17,32); bandı karşılamadı |
| FAN-3 + 15 W ampul — Log 54 | 0,209 A | 0,28658 / 0,284 A | +%37,1* | SD 0,019443 A; CV %6,78; aralık 0,260–0,387 A | Düşük akım bölgesi; UNIT zaman eşleşmesi yok, ±%4 yok |

## C. Termostatlı yük — ütü

| Çevrim | UNIT bildirimi | SCT ort. / medyan | Aritmetik fark | SD / CV | Min–maks |
|---|---:|---:|---:|---:|---:|
| IRON-001 açık çevrim 1 (n=5) | 10,16 A | 9,2852 / 9,291 A | −%8,61* | 0,0285 A / %0,307 | 9,237–9,311 A |
| IRON-001 açık çevrim 2 (n=4) | 10,16 A | 9,3605 / 9,351 A | −%7,87* | 0,0542 A / %0,579 | 9,314–9,426 A |

Ütünün kapalı/düşük akım sınıfında 40 yayın kaydedildi: 27 adet 0,000 A, 13 adet 0,011–0,092 A. Bunlar geçerli OFF verisidir; kararlı ON istatistiklerine karıştırılmamıştır. Çevrim örnek sayıları çok azdır. UNIT ile zaman eşleşmesi yoktur.

## D. Henüz SCT logu olmayan yük

| Yük | Mevcut bildirim | SCT sonucu | Durum |
|---|---|---|---|
| Einhell pil şarj cihazı | 0,413 → 0,419 (sabitlendi) → 0,422 A görüldü; ölçüm cihazı belirtilmedi | Henüz yok | Kullanıcı bildirimi; SCT logu ve eşzamanlı referans bekleniyor |

## E. Kendi iç kararlılığına göre hızlı sıralama

CV yalnız aynı oturumun SCT okumalarının ortalamaya göre dağılımını gösterir. Farklı yüklerdeki CV değerleri, sensörün tüm akım aralığı boyunca doğruluğunu veya mutlak gürültüsünü tek başına kanıtlamaz.

| Oturum | CV | Kısa yorum |
|---|---:|---|
| TOASTER-001 / 7,19 A | %0,344 | En düşük CV; dar kararlı ON bölgesi |
| IRON-001 çevrim 1 | %0,307 | Çok az örnek (n=5), genelleme yapılmaz |
| IRON-001 çevrim 2 | %0,579 | Çok az örnek (n=4), genelleme yapılmaz |
| 150 W akkor | %1,08 | Dar dağılım |
| 100 W + FAN-3 | %1,26 | Dar dağılım |
| 100 W LOAD-100W-004 | %2,70 | İyi kısa dönem kararlılık |
| 57 W akkor | %3,00 | Görece kararlı |
| 42 W ampul | %4,37 | Daha geniş dağılım |
| 57 W + 15 W | %4,48 | Değişkenlik ve yüksek uç örnekleri mevcut |
| FAN-3 + 15 W | %6,78 | Daha geniş dağılım |
| 0,130 A hedefli yük | %8,82 | Daha geniş dağılım |
| FAN-3 tek tur | %8,31 | Düşük akımda dağılım daha geniş |
| FAN-2 | %14,58 | Geniş dağılım |
| FAN-1 | %17,76 | Geniş dağılım |

Not: FAN-3 üç tur için /3 normalize serinin SD/CV değeri raporlanmadığından sıralamaya alınmadı. Yüksüz kayıt için SD/CV raporlanmadığından sıralamaya alınmadı.

## F. Genel teknik sonuç

1. **Kararlılık ile doğruluk farklıdır.** Tost makinesi 7,19 A'da CV %0,344 ile çok kararlı görünürken UNIT 7,89 A bildirimiyle aritmetik fark −%8,87'dir. Zaman eşleşmesi yoksa bu durum “kararlı ama referansla henüz uyuşması doğrulanmamış” şeklinde okunmalıdır.
2. **En güçlü mevcut UNIT karşılaştırmaları:** 150 W (ortalama +%1,62; 388/391 bant içinde), 100 W LOAD-100W-004 (ortalama −%0,47; 192/215 bant içinde) ve 100 W + FAN-3 (ortalama +%1,65; 130/136 bant içinde). Bunlar PZEM doğrulaması değildir.
3. **57 W + 15 W birleşik yük**, kendi içinde CV %4,48 gösterdi; fakat yayınların yalnız %17,32'si bu teste özel ±%5,6 bandında kaldı. Kararlılık ve referans uyumu aynı şey değildir.
4. **Fanlar ve 0,30 A altındaki ampuller**, ayrı düşük akım veri sınıfı olarak değerlendirilmelidir. Bu bölgede yüzde farklar teşhis amaçlıdır; ±%4 kabul/ret değildir.
5. **Ütü ve tost makinesi gibi termostatlı yüklerde**, ON kararlı alan, OFF alanı ve geçişler ayrı istatistiklenmelidir.
6. Bu kayıtlarda eşzamanlı PZEM akım/PF penceresi bulunmadığından henüz hiçbir satır PZEM doğrulaması sayılmaz.
7. K=24.22 bu karşılaştırma boyunca değiştirilmemiştir; bu tablo katsayı değişikliği önerisi değildir.

## Kaynak kayıtlar

- [100 W test kaydı](100w-incandescent/README.md)
- [150 W test kaydı](150w-incandescent/README.md)
- [Fan testleri](fan/README.md)
- [42 W ampul](42w-bulb/README.md)
- [57 W ampul](57w-incandescent/README.md)
- [57 W + 15 W karma yük](mixed-57w-15w/README.md)
- [100 W + FAN-3 karma yük](mixed-load-100w-plus-fan3/README.md)
- [Ütü / IRON-001](iron/README.md)
- [Tost makinesi / TOASTER-001](toaster/README.md)
- [0,130 A hedefli yük](fixed-load-0130a/README.md)
- [Yüksüz kayıt](idle-no-load/README.md)
- [Einhell şarj cihazı](einhell-charger/README.md)
