# PROJE BERO — GRV-005-14 v03 Gerçek CSV Satır Alan Kontrolü

**Tarih:** 2026-10-11  
**Kaynak log raporu:** [GRV-005-14-v03-GERCEK-CIHAZ-LOGU-20261011.md](./GRV-005-14-v03-GERCEK-CIHAZ-LOGU-20261011.md)

## Kontrol

Kullanıcının verdiği dört gerçek cihaz veri satırı virgülle ayrılarak alan sayısı ve kritik sütun eşleşmeleri bakımından kontrol edildi.

| Satır | Alan sayısı | Kanal | Sonuç |
|---|---:|---|---|
| 1 | 41 | CH0-1T | Alan sayısı PASS |
| 2 | 41 | CH1-2T | Alan sayısı PASS |
| 3 | 41 | CH2-3T | Alan sayısı PASS |
| 4 | 41 | BIAS | Alan sayısı PASS |

## Sütun eşleşmesi

CH0/CH1/CH2 satırlarında:
- `adc_rms_raw`: sırasıyla 1863.193899, 1861.616696, 1855.489362
- `adc_rms_ac`: sırasıyla 33.779911, 26.491071, 14.814929
- `bias_mean`: 1864.018000
- `bias_std`: 13.489538
- `bias_min`: 1739
- `bias_max`: 1988
- `pzem_current`: 0.028
- `pzem_power`: 1.700
- `pzem_pf`: 0.2600

BIAS satırında `adc_rms_raw` ve `adc_rms_ac` boş; `bias_mean`, `bias_std`, `bias_min`, `bias_max` doğru sütunlarda görünüyor.

## Sonuç

- Dört gerçek veri satırının her biri **41 alan** içeriyor.
- Görünen veri satırlarında önceki v02'deki 40 alan sorunu tekrarlanmıyor.
- Başlık logda `pz` bölümünde kesildiği için başlığın tamamının cihaz çıktısında bulunup bulunmadığı yalnızca bu metin dökümünden doğrulanamıyor.
- Bu kontrol yalnızca CSV satır alan sayısı ve belirli sütunların eşleşmesi üzerinedir; GRV-005-15 QC v02'nin tüm kontrollerinin geçtiği iddia edilmez.
- Logda ayrıca ADC sensör işleminin 92 ms sürdüğüne dair uyarı vardır; örnekleme zamanlaması ayrı inceleme gerektirir.
