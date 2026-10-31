# 100 W Akkor Ampul — Karşılaştırmalı Ölçüm Kaydı

**Yük ID:** LOAD-100W-INC  
**Yük:** 100 W akkor ampul  
**Amaç:** Aynı test yüküyle farklı ESP/modül/SCT düzeneklerinde alınan akım sonuçlarını, kodları ve log kanıtlarını tek tabloda karşılaştırmak.  
**Kabul hedefi:** Referans cihaza göre mutlak yüzde sapma en fazla %4.  
**Önemli:** Farklı tarihlerdeki ölçümler ancak aynı ampul ve karşılaştırılabilir elektriksel koşullar sağlandığında doğrudan karşılaştırılabilir. Test saati veya eşzamanlılık kanıtı yoksa bu sınırlama ayrıca belirtilir.

## Karşılaştırma tablosu

| Test ID | Tarih | Saat / log aralığı | ESP / düzenek | SCT kanalı | Kod / sürüm | Log | Referans | Kod sonucu | Sapma | ±%4 durumu |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| LOAD-100W-001 | Tarihsel kayıt; kesin tarih bu özet tabloda belirtilmemiş | Ham logdaki zaman aralığı mevcut özet kayıtta verilmemiş | ESP32D2, harici/Modül 2 kutusu olmadan | ESP32D2 baseline bağlantısı; GPIO33 ct_clamp | [firmware/esp32d2.yaml](../../firmware/esp32d2.yaml) — tarihsel baseline kodu; testte kullanılan tam commit ayrıca arşivlenmemiş | Ayrı ham log dosyası bulunamadı. Sonuç STATUS/ROADMAP tarihsel özetinden aktarılmıştır. | Pens: 0,446–0,447 A | 0,4471 A | yaklaşık %0 | **Hedef içinde** (tarihsel kayıt; ham log/zaman aralığı eksik) |
| LOAD-100W-002 | 2026-10-31 | Logdan çıkarılan son beş kararlı yayın; kesin başlangıç/bitiş timestamp'i özet dosyada korunmamış | ESP32D1 / Modül 2 | SCT-1 / GPIO32 / sarı | [firmware/esp32d1.yaml](../../firmware/esp32d1.yaml) — ilgili log başlığında 200 ms ct_clamp ve nominal 30 A/V belirtiliyor; **logda kullanılan tam YAML commit'i doğrulanmadı** | [SCT-1 100 W ct_clamp + PENS karşılaştırması](../../logs/module2/2026-10-31-sct1-100w-ct-clamp-comparison.txt) — 563 satırlık özgün logun tamamı değil, analiz özeti | PENS: 0,427 A (kullanıcı bildirimi) | Son beş kararlı değer: 0,578 / 0,591 / 0,597 / 0,590 / 0,589 A; ortalama 0,589 A | +%37,9 | **Hedef dışında** |

## Test 001 — ESP32D2 baseline

### Kurulum ve koşul
- İlk karşılaştırma, ESP32D2 ile Modül 2 SCT kutusu kullanılmadan yapılan tarihsel baseline ölçümüdür.
- Depodaki ESP32D2 firmware dosyası tarihsel referans kodudur.
- Faz 1 sonuç özetinde pens referansı 0,446–0,447 A, kod sonucu 0,4471 A olarak kayıtlıdır.

### Kanıt ve eksikler
- Kod dosyası depoda mevcuttur: [esp32d2.yaml](../../firmware/esp32d2.yaml).
- Bu sonuç için ayrı ham log dosyası ve kesin log zaman aralığı mevcut depo kayıtlarında bulunamadı.
- Bu nedenle sonuç, tarihsel STATUS/ROADMAP özetine dayalıdır; ham logdan yeniden hesaplanmış değildir.
- Sonuç ±%4 hedefi içinde görünmektedir; ancak ham kayıt ve kesin zaman aralığı eksikliği korunmalıdır.

## Test 002 — Modül 2 / ESP32D1 / SCT-1

### Kurulum ve koşul
- Tarih: 2026-10-31.
- Yük: 100 W akkor ampul.
- SCT-1: ön panel 1 numaralı giriş, sarı sinyal, GPIO32.
- Bias izleme: GPIO35.
- Log analizinde 200 ms ct_clamp penceresi ve yaklaşık 5 saniyelik akım yayınları belirtilmiştir.
- Son beş kararlı akım yayını 0,578–0,597 A aralığındadır; ortalama 0,589 A.
- PENS referansı 0,427 A kullanıcı bildirimidir.

### Hesap

\[
\\text{Sapma} = \\frac{0.589-0.427}{0.427}\\times100 \\approx 37.9\\%
\]

Bu kayıt ±%4 hedefinin dışında kalmıştır. Tek bir test sonucu katsayıyı değiştirmek için yeterli değildir.

### Kod sürümü uyarısı
Log özetinin başlığı, test sırasında kullanılan yapılandırmayı nominal 30 A/V olarak tanımlar. Depodaki güncel firmware dosyası daha sonra farklı düzenlemeler görmüş olabilir. Testte derlenen YAML'ın tam commit'i doğrulanmadığı için yukarıdaki kod bağlantısı ilgili firmware dosyasına referanstır; tarihsel binary/kod eşleşmesinin kesin kanıtı değildir.

## Sonraki kayıtlar için zorunlu alanlar

- Test başlangıç ve bitiş saati (Türkiye saati, UTC+03:00).
- Yükün kapalı → açık kararlı → kapalı aşamaları.
- Referans cihazın modeli ve aynı zaman aralığındaki okuması.
- ESPHome firmware commit'i veya YAML dosyasının o test anındaki kopyası.
- Ham log dosyası; büyükse özgün dosyanın SHA-256 özeti ve seçilmiş satırların ayrı kanıt dökümü.
- Kararlı bölümün başlangıç/bitiş timestamp'i, örnek/yayın sayısı, min/ortalama/max ve sapma hesabı.
- Fiziksel modül, SCT modeli ve kanal bağlantısı.

## İlgili dosyalar
- [ESP32D2 baseline firmware](../../firmware/esp32d2.yaml)
- [Modül 2 ESP32D1 firmware](../../firmware/esp32d1.yaml)
- [Modül 2 SCT-1 karşılaştırma özeti](../../logs/module2/2026-10-31-sct1-100w-ct-clamp-comparison.txt)
- [Modül 2 ilk SCT-1 test bildirimi](../../logs/module2/2026-10-31-sct1-100w-test.txt)
