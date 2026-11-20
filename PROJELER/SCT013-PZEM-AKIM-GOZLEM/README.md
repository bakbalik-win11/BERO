# SCT013 + PZEM — Kapatılmış akım okuma çalışması

**DURUM: KAPATILDI — HEDEFE ULAŞILDI.**

Bu klasör önceki SCT013/PZEM akım okuma hedefinin tarihsel arşividir. Yeni aktif çalışma [PREBERO](../PREBERO/README.md) altındadır.

## Kapanış kararı
Pratik hedef, SCT + ADS1115 ölçüm zinciriyle hedeflenen ev içi yük koşullarında akım okuyabilmekti. E19 kayıtlarında 18 W, 42 W, 57 W ve 150 W sabit yük koşullarındaki ADS1115/PZEM karşılaştırma ortalamaları ±%4 hedefinin içinde raporlandı. 100 W kaydı bağımsız doğrulama sayılmadı.

Bu, test edilen koşullarda pratik akım okuma hedefinin başarıldığı anlamına gelir. PZEM karşılaştırma kaynağıdır; mutlak ground truth değildir. Sonuç tüm akım aralığına, tüm sensör/ADC kartlarına veya elektriksel güvenliğe genellenmez.

## Arşiv
Eski deneyler E00–E24, görevler T001–T011, ADR-001–ADR-035, YAML'lar, loglar, kalibrasyon notları ve veri şemaları silinmedi. Eski Modül 2/3 fiziksel donanım kayıtları ve eski Modül 5/6/7 hedefleri tarihsel kayıttır; yeni aşamanın aktif hedefi değildir.

- [Eski kararlar](docs/decisions/README.md)
- [Eski deney indeksi](experiments/README.md)
- [Eski görev indeksi](tasks/README.md)
- [Eski firmware envanteri](firmware/README.md)
- [Tarihsel oturum günlüğü](HISTORY/SESSION_LOG.md)

Yeni aşama: [PREBERO](../PREBERO/README.md).
