# LOAD-57W-001 — 57 W akkor ampul / SCT-1 Log 58 analizi

- **Tarih:** 2026-10-31
- **Test:** LOAD-57W-001
- **Yük:** 57 W akkor ampul (KULLANICI BİLDİRİMİ)
- **Düzenek:** ESP32D1 / Modül 2 / SCT-1 GPIO32 ADC1_CH4 / ortak bias GPIO35 ADC1_CH7
- **Firmware bilgisi logdan:** ESPHome 2026.10.1; ADC GPIO32 ve GPIO35, 12 dB, 1 s güncelleme; ct_clamp 200 ms pencere / 2 s güncelleme. K=24.22 depodaki mevcut firmware referansıdır; log tek başına çalışan binary'nin YAML ile birebir eşleştiğini kanıtlamaz.
- **UNIT:** 0,244 A (KULLANICI BİLDİRİMİ; ölçüm zamanı ve SCT penceresiyle örtüşmesi teyitsiz). PZEM verisi yok.

## 1. Kaynak bütünlüğü

- Özgün dosya: `esp32d1-logs (58).txt`
- Boyut: 66.456 bayt
- Satır: 906
- SHA-256: `f5a2d958dc2c85ec204516240c99ec2e87b519a422958a9ddd1cf122b4ee8d08`
- İlk/son SCT akım yayını: 21:14:44–21:18:34 (+03:00)
- Tam ham log: [Log 58 — tam kaynak dosya](../../logs/module2/2026-10-31-load-57w-001-module2-sct1-full.txt)

## 2. SCT-1 akım istatistikleri — LOG

| Metrik | Sonuç |
|---|---:|
| Yayın sayısı | 116 |
| Ortalama | 0,304207 A |
| Medyan | 0,303 A |
| Minimum | 0,284 A |
| Maksimum | 0,348 A |
| Örnek standart sapma | 0,009126 A |
| CV | %3,00 |
| 0,30 A altındaki yayın | 31 / 116 |
| 0,30 A ve üzerindeki yayın | 85 / 116 |

En yüksek üç değer 21:15:08'de 0,348 A, 21:17:20'de 0,344 A ve 21:18:04'te 0,333 A'dır. Ham değerler korunmuş, aykırı diye silinmemiştir.

## 3. Zaman içi kararlılık

116 yayın dört eşit, ardışık 29 örnekli bloğa ayrıldığında ortalamalar:

1. 0,3061 A (min–maks 0,284–0,348 A)
2. 0,3022 A (0,287–0,318 A)
3. 0,3046 A (0,291–0,344 A)
4. 0,3040 A (0,284–0,333 A)

Blok ortalamaları birbirine yakındır. Bu log aralığında belirgin bir sürekli yükselme veya düşme trendi görünmüyor. Dağılımın CV %3 olması, SCT çıktısının bu oturumda kendi içinde toplu olduğunu destekler; tek başına mutlak doğruluk anlamına gelmez.

## 4. Analog ve örnekleme verileri — LOG

| Sinyal | Örnek | Ortalama | Min–maks |
|---|---:|---:|---:|
| SCT-1 Raw AC | 116 | 0,012562 V | 0,01173–0,01436 V |
| Ortak bias GPIO35 | 232 | 1,663073 V | 1,651–1,672 V |
| SCT-1 ADC GPIO32 | 232 | 1,660694 V | 1,642–1,683 V |
| ct_clamp log SPS | 116 | 17.768 SPS | 17.280–18.260 SPS |

Wi-Fi bağlantısı başarılı; sinyal seviyesi −60 dB olarak raporlanmış. Logda üç ESPHome framework/optimizasyon uyarısı var. ERROR veya [E] seviyesinde uygulama hatası, brownout ya da reboot kaydı görülmedi.

## 5. UNIT karşılaştırmasının sınırı — HESAP

- UNIT bildirimi: 0,244 A.
- SCT ortalaması: 0,304207 A.
- Salt aritmetik fark: +0,060207 A; UNIT'e göre yaklaşık +%24,67.
- SCT medyanı ile aritmetik fark: +0,059 A; UNIT'e göre yaklaşık +%24,18.

Bu fark **eşzamanlı ölçüm sapması değildir**: UNIT 0,244 A değerinin logdaki 21:14:44–21:18:34 aralığıyla aynı kararlı pencereye ait olduğu teyit edilmemiştir. UNIT ve PZEM ayrı tutulur; bu logda PZEM yoktur.

## 6. Sonuç ve karar

- **ÖLÇÜLDÜ / LOG İLE DESTEKLENDİ:** Modül 2 / SCT-1 bu 57 W akkor oturumunda 116 akım yayını üretmiştir. Çıktı ortalaması 0,3042 A ve CV %3,00 ile kendi içinde görece kararlıdır.
- **GÖZLEM:** Yayınların %73,3'ü 0,30 A veya üzerindedir; bu nedenle SCT gösterimi 0,30 A eşiğinin iki tarafına da dağılmıştır. 0,30 A, BERO'nun değerlendirme sınırıdır; sensörün üretici alt ölçüm sınırı değildir.
- **REFERANS SINIRI:** Başlangıç UNIT değeri 0,244 A ile aritmetik fark +%24,67 görünür; zaman örtüşmesi doğrulanmadığından doğruluk/kalibrasyon sonucu çıkarılamaz. 0,30 A altı düşük akım bölgesinde ±%4 kabul/ret uygulanmaz.
- **KOD KARARI:** Firmware, K=24.22, pinler ve yazılımsal sıfır eşiği değiştirilmedi. Bu tek logdan yeni K hesaplanmadı.
- **TEST DURUMU:** LOAD-57W-001 AÇIK kalır. UNIT'in SCT ile aynı kararlı zaman aralığında okunması ve mümkünse aynı aralık için PZEM akım/PF kaydı sonraki adımdır.

## 7. Kaynak arşivi

Tam 906 satırlık özgün TXT, içeriği değiştirilmeden `logs/module2/2026-10-31-load-57w-001-module2-sct1-full.txt` yoluna kaydedilmiştir. Kaynak SHA-256 yukarıda verilmiştir.
