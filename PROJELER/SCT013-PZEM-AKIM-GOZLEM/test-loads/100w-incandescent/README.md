# 100 W Akkor Ampul — Karşılaştırmalı Ölçüm Kaydı

**Yük ID:** LOAD-100W-INC  
**Yük:** 100 W akkor ampul  
**Amaç:** Aynı test yüküyle farklı ESP/modül/SCT düzeneklerinde alınan akım sonuçlarını, kodları ve log kanıtlarını tek tabloda karşılaştırmak.  
**Kabul hedefi:** Referans cihaza göre mutlak yüzde sapma en fazla %4.  
**Önemli:** Farklı tarihlerdeki ölçümler ancak aynı ampul ve karşılaştırılabilir elektriksel koşullar sağlandığında doğrudan karşılaştırılabilir. Test saati veya eşzamanlılık kanıtı yoksa bu sınırlama ayrıca belirtilir.

## 100 W akkor için geçici beklenen akım değeri

**Geçici çalışma referansı: 0,427 A (UNIT cihazı; kullanıcı bildirimi).**

Bu değer, 100 W akkor ampul için şimdilik “ne okumayı bekliyoruz?” sorusunun pratik karşılığı olarak kaydedilmiştir. Henüz PZEM tarafından aynı yük ve kararlı koşulda doğrulanmış/sabitlenmiş değer değildir. PZEM okuması alındığında aynı ampul ve karşılaştırılabilir besleme koşulunda kararlı pencere belirlenecek; PZEM değeri ayrıca kaydedilecek ve bu geçici 0,427 A beklentisiyle ilişkisi netleştirilecektir. O zamana kadar 0,427 A kesin PZEM referansı veya kalibrasyon gerçeği olarak kullanılmayacaktır.

## Karşılaştırma tablosu

| Test ID | Tarih | Saat / log aralığı | ESP / düzenek | SCT kanalı | Kod / sürüm | Log | Referans | Kod sonucu | Sapma | ±%4 durumu |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| LOAD-100W-003 | 2026-10-31 | 15:59:53–16:05:11 (+03:00) | ESP32D1 / Modül 2 | SCT-1 / GPIO32 / sarı | [Tek kanallı firmware snapshot](https://github.com/bakbalik-win11/BERO/blob/720e52de7fac8c409fe2c7de8569849ca171f166/PROJELER/SCT013-PZEM-AKIM-GOZLEM/firmware/archive/LOAD-100W-003-esp32d1-sct1-single-channel.yaml) | [Tam uzun log](../../logs/module2/2026-10-31-load-100w-003-sct1-single-channel-full.txt) / [uzun log analizi](../../logs/module2/2026-10-31-load-100w-003-sct1-single-channel-extended-analysis.md) | Geçici beklenti: 0,427 A (UNIT; PZEM teyidi bekleniyor) | 160 yayın; medyan 0,460 A; ortalama 0,4841 A; 150/160 yayın 0,422–0,541 A | Medyana göre +%7,7 (UNIT geçici değere göre) | **±%4 dışında; PZEM teyidi bekleniyor** |
| LOAD-100W-001 | Tarihsel kayıt; kesin tarih bu özet tabloda belirtilmemiş | Ham logdaki zaman aralığı mevcut özet kayıtta verilmemiş | ESP32D2, harici/Modül 2 kutusu olmadan | ESP32D2 baseline bağlantısı; GPIO33 ct_clamp | [firmware/esp32d2.yaml](../../firmware/esp32d2.yaml) — tarihsel baseline kodu; testte kullanılan tam commit ayrıca arşivlenmemiş | Ayrı ham log dosyası bulunamadı. Sonuç STATUS/ROADMAP tarihsel özetinden aktarılmıştır. | Pens: 0,446–0,447 A | 0,4471 A | yaklaşık %0 | **Hedef içinde** (tarihsel kayıt; ham log/zaman aralığı eksik) |
| LOAD-100W-002 | 2026-10-31 | Logdan çıkarılan son beş kararlı yayın; kesin başlangıç/bitiş timestamp'i özet dosyada korunmamış | ESP32D1 / Modül 2 | SCT-1 / GPIO32 / sarı | [Üç kanallı ESP32D1 firmware — test öncesi commit](https://github.com/bakbalik-win11/BERO/blob/33b2b8fcb17f51a97edbb5cbd416ee6f9a532278/PROJELER/SCT013-PZEM-AKIM-GOZLEM/firmware/esp32d1.yaml) — 31.10.2026 tarihli üç kanal ct_clamp sürümü | [SCT-1 100 W ct_clamp + PENS karşılaştırması](../../logs/module2/2026-10-31-sct1-100w-ct-clamp-comparison.txt) — 563 satırlık özgün logun tamamı değil, analiz özeti | PENS: 0,427 A (kullanıcı bildirimi) | Son beş kararlı değer: 0,578 / 0,591 / 0,597 / 0,590 / 0,589 A; ortalama 0,589 A | +%37,9 | **Hedef dışında** |

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

**Firmware düzeltmesi:** GitHub dosya geçmişinde test öncesi üç kanallı ct_clamp sürümü bulundu. Kod bağlantısı bu test öncesi commit'e sabitlendi; güncel tek kanallı dosyaya işaret etmiyor.

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


## Test 003 — Modül 2 / ESP32D1 / SCT-1 tek kanal

- Tarih: 2026-10-31; log aralığı 15:59:53.051–16:01:39.884 (+03:00).
- Yük: 100 W akkor ampul; SCT-1 / GPIO32 / sarı; ortak bias GPIO35 / turuncu.
- Firmware: tek kanallı akım okuma; arşiv snapshot'ı yukarıdaki bağlantıda sabitlendi.
- ESPHome 2026.10.1; derleme zamanı 15:55:25 +0300; ct_clamp 200 ms, yayın aralığı 2 s.
- 54 akım yayını; medyan 0,469 A; min–max 0,426–1,164 A. 52/54 yayın 0,426–0,541 A aralığında. İki yüksek değer: 0,797 A (16:00:13.890) ve 1,164 A (16:01:33.849).
- Bias 107 yayında 1,623–1,678 V; ortalama 1,65672 V.
- Logda referans cihaz değeri bulunmuyor; sapma ve ±%4 durumu hesaplanamaz. Katsayı değişikliği yapılmadı.
- Özgün log SHA-256: c92d51915de6b7ab69fdbc1f00ad4b7554455748958d18525ba2b3320a9d9723.


## 0,427 A geçici referansının kullanımı

- **Beklenen okuma:** 0,427 A.
- **Kaynak:** UNIT cihazında görülen değer; kullanıcı bildirimi. Bu değer 100 W akkor yük için geçici çalışma beklentisidir.
- **PZEM durumu:** Aynı yükte PZEM ölçümü henüz alınmadı veya kararlı pencere olarak doğrulanmadı. PZEM değeri geldiğinde tarih/saat ve kararlı aralıkla ayrı kaydedilecek; gerekirse 0,427 A beklentisi güncellenecek.
- **003 ile kaba karşılaştırma:** 003 medyanı 0,469 A olduğundan 0,427 A geçici beklentiye göre yaklaşık +%9,8 fark vardır. Bu yalnızca ön karşılaştırmadır; referans PZEM ile sabitlenmeden ±%4 kabul kararı değildir. İki yüksek yayın (0,797 A ve 1,164 A) ayrıca değerlendirilmelidir.
- **Karar:** Şimdilik katsayı değiştirilmez. 0,427 A, PZEM teyidi gelene kadar “geçici beklenen değer” olarak tutulur.


## Test 003 — uzun log güncellemesi (esas analiz)

Daha uzun log, önceki kısa 003 kaydını silmeden esas analiz olarak eklendi.
- Tam ham kayıt: [1.219 satırlık log](../../logs/module2/2026-10-31-load-100w-003-sct1-single-channel-full.txt).
- Teknik analiz: [uzun log analizi](../../logs/module2/2026-10-31-load-100w-003-sct1-single-channel-extended-analysis.md).
- Süre: 15:59:53.051–16:05:11.858 (+03:00), yaklaşık 5 dakika 19 saniye.
- 160 akım yayını; medyan 0,460 A; ortalama 0,4841 A; min–max 0,422–1,164 A.
- 150/160 yayın 0,422–0,541 A aralığında; 10 yayın 0,55 A üzerindedir.
- 0,427 A geçici UNIT beklentisine göre medyan farkı +%7,7. 0,55 A üzerindeki yayınlar hariç 150 örneğin ortalaması 0,46288 A (+%8,4).
- 0,427 A ±%4 bandında 17/160 yayın vardır. Bu PZEM doğrulaması değildir.
- Bias 321 yayında ortalama 1,65540 V; SCT-1 ADC 320 yayında ortalama 1,65253 V.
- K katsayısı değiştirilmedi; PZEM kararlı ölçümü bekleniyor.
- Özgün dosya SHA-256: `30fc5d5ccccf629423924ea17fe1706bdb4f8dfab1185f64f523596661663ed4`.
