# MIXED-LOAD-57W-15W-001 — Log 59 analizi

- **Tarih:** 2026-10-31
- **Test ID:** MIXED-LOAD-57W-15W-001
- **Yük:** 57 W akkor ampul + 15 W ampul; 15 W ampulün teknoloji/tipi henüz belirtilmedi.
- **Düzenek:** ESP32D1 / Modül 2 / SCT-1 GPIO32 ADC1_CH4 / ortak bias GPIO35 ADC1_CH7.
- **Firmware bilgisi logdan:** ESPHome 2026.10.1; derleme zamanı 2026-10-31 15:55:25 +03:00; GPIO32 ve GPIO35 ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s. Depodaki YAML referansı K=24.22'dir; log tek başına çalışan binary'nin YAML ile birebir eşleştiğini kanıtlamaz.
- **UNIT:** 0,303 A. Kullanıcı, değerin test boyunca sabit kaldığını ve değişirse bildireceğini belirtti. Bu, kullanıcı bildirimidir; logda UNIT verisi yoktur. PZEM değildir.

## 1. Kaynak bütünlüğü

- Özgün dosya: `esp32d1-logs (59).txt`
- Boyut: 99.807 bayt
- Satır: 1.349
- SHA-256: `6e7dea5c6c8991a6d4f915ebd6182f3de82b151d5726066700840f21a7d7124a`
- İlk/son SCT akım yayını: 21:20:18.203–21:26:14.218 (+03:00)
- Süre: yaklaşık 5 dk 56 sn
- Tam ham log: [Log 59 — tam kaynak dosya](2026-10-31-mixed-load-57w-15w-001-module2-sct1-full.txt)

## 2. SCT-1 akım istatistikleri — LOG

| Metrik | Sonuç |
|---|---:|
| Yayın sayısı | 179 |
| Ortalama | 0,329553 A |
| Medyan | 0,328 A |
| Minimum | 0,303 A |
| Maksimum | 0,436 A |
| Örnek standart sapma | 0,014762 A |
| Değişim katsayısı (CV) | %4,48 |
| 0,250 A ve altı | 0 / 179 (%0) |

Ham yayınlar aykırı değer diye silinmedi. En yüksek değer 0,436 A'dır.

## 3. Kullanıcı tarafından belirlenen deney kabul bandı — HESAP

Bu test için kullanıcı, 0,303 A UNIT referansına göre ±%5,6 toleransı kabul edilebilir olarak belirledi. Ayrıca 0,250 A seviyesini başarısız kabul etti.

- UNIT referansı: 0,303 A.
- ±%5,6 bandı: **0,286032–0,319968 A** (yuvarlatılmış: 0,286–0,320 A).
- Bandın altı: 0 yayın (%0).
- Bandın içinde: **31/179 yayın (%17,32)**.
- Bandın üstü: **148/179 yayın (%82,68)**.
- 0,250 A ve altı: 0/179 (%0); tüm yayınlar bu mutlak alt eşiğin üzerindedir.

| Karşılaştırma | Sonuç |
|---|---:|
| SCT ortalamasının UNIT'e göre farkı | +%8,76 |
| SCT medyanının UNIT'e göre farkı | +%8,25 |
| ±%5,6 bandında kalan yayın yüzdesi | %17,32 |
| 0,250 A üstünde kalan yayın yüzdesi | %100 |

**Yorum:** 0,250 A mutlak başarısızlık eşiğinin altında veri yoktur; ancak bu tek başına testin kabul edildiği anlamına gelmez. ±%5,6 bandına yayınların yalnız %17,32'si girmiştir. Ortalama ve medyan da bandın üst tarafındadır. Bu nedenle mevcut kayıt, 0,303 A referansına göre tolerans hedefini karşılamamıştır.

## 4. Zaman içi dağılım

179 yayın, sırayla 30 örnekli bloklara ayrıldığında ortalamalar:

| Yayın aralığı | n | Ortalama | Medyan | Min–maks | Band içi |
|---|---:|---:|---:|---:|---:|
| 1–30 | 30 | 0,3271 A | 0,327 A | 0,313–0,340 A | 7 |
| 31–60 | 30 | 0,3293 A | 0,328 A | 0,313–0,410 A | 5 |
| 61–90 | 30 | 0,3254 A | 0,328 A | 0,309–0,342 A | 7 |
| 91–120 | 30 | 0,3304 A | 0,331 A | 0,308–0,387 A | 7 |
| 121–150 | 30 | 0,3316 A | 0,330 A | 0,312–0,357 A | 2 |
| 151–179 | 29 | 0,3336 A | 0,327 A | 0,303–0,436 A | 3 |

Blok ortalamaları 0,3254–0,3336 A aralığında. Kayıt boyunca genel seviye 0,303 A UNIT referansının üzerinde seyrediyor. Son bloktaki 0,436 A maksimum değer ham veride korunmuştur.

## 5. Analog ve örnekleme verileri — LOG

| Sinyal | Örnek | Ortalama | Min–maks |
|---|---:|---:|---:|
| SCT-1 Raw AC | 179 | 0,013604 V | 0,01251–0,01801 V |
| Ortak bias GPIO35 | 359 | 1,663504 V | 1,651–1,678 V |
| SCT-1 ADC GPIO32 | 359 | 1,663869 V | 1,635–1,688 V |
| ct_clamp log SPS | 179 | 17.586 SPS | 17.230–17.940 SPS |

Logda uygulama seviyesinde `[E]` hata satırı veya timeout/failed kaydı görülmedi.

## 6. Sonuç ve karar

- **LOG İLE DESTEKLENDİ:** 179 SCT-1 akım yayını elde edildi; ortalama 0,329553 A, medyan 0,328 A ve CV %4,48.
- **KULLANICI BİLDİRİMİ:** UNIT 0,303 A test boyunca sabit kaldı; değişiklik olursa kullanıcı bildirecek.
- **HESAP:** Kullanıcının bu test için belirlediği ±%5,6 bandında yayınların %17,32'si kaldı. Ortalama fark +%8,76.
- **ALT EŞİK:** 0,250 A ve altında yayın yok (%0); tüm örnekler 0,250 A üzerindedir.
- **KARAR:** Bu log ±%5,6 bandı bakımından başarılı değildir. Bununla birlikte SCT çıktısının hiçbir yayında 0,250 A seviyesine düşmemesi, kullanıcının önem verdiği alt eşik açısından olumlu bir gözlemdir. Bu iki sonuç birbirine karıştırılmamalıdır.
- **SINIR:** UNIT sürekliliği kullanıcı bildirimi; logda UNIT/PZEM kanalı yoktur. PZEM karşılaştırması yapılmadı. 15 W ampul tipi belirtilmedi.
- **KOD:** Firmware ve K=24.22 değiştirilmedi; bu logdan katsayı türetilmedi. Test AÇIK kalır.

## 7. Kaynak arşivi

Tam kaynak log `logs/module2/2026-10-31-mixed-load-57w-15w-001-module2-sct1-full.txt` yoluna kaydedildi. Özgün dosya SHA-256 değeri yukarıda verilmiştir.
