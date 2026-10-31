# Deney arşivi

Bu klasör Faz 1'deki tarihsel deney ve gözlem kayıtlarını korur. **Faz 1 kapalıdır.** Aşağıdaki kayıtlar yeni aktif deney planı değildir; yapılmış çalışmaların logları ve sonuçları ile hedefe ulaşıldığı için yapılmadan kapatılan planlar aynı tarihçe altında korunur.

## Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak (KAPATILDI)

Eski kayıtlar:
- [E00A — Bias/DC ve ADC gözlemleri](E00A-raw-waveform-observation/README.md)
- [E00B — SCT bağlı, akımsız hat gözlemi](E00B-sct-connected-no-current/README.md)
- [E00 — Bias ADC baseline](E00-bias-adc-baseline/protocol.md)
- E01 — Yüksüz ofset/gürültü tabanı
- E02 — Kararlı rezistif yük
- E03 — PZEM adım yanıtı/yerleşme
- E04 — PZEM alan değişim zamanları
- E05 — Örnekleme hızı karşılaştırması
- E06 — Yük senaryoları
- [E07 — SCT kararlılık basamak planı](E07-sct-stability-step-tests/protocol.md)
- [E08 — SCT sinyal karakterizasyonu](E08-sct-characterization/README.md)
- [E00F-N02/N03 — ESP32D2 gözlem logları](E00F-unthresholded-overnight-log/E00F-N02-first-device-log.md)

**Kapanış anlamı:** Faz 1 hedefi dış kaynaklı çalışan kodla ±%4 sapma olarak sağlandığı için Faz 1 kapsamında kalan yapılmamış deneyler ve işler KAPATILDI — HEDEFE ULAŞILDI. Bu deneylerin fiziksel olarak yapıldığı veya sonuç ürettiği anlamına gelmez. Gerçekten yapılmış alt deneylerin sonuçları kendi dosyalarında kalır. Eski planlar Faz 2'nin ön koşulu değildir ve yeniden açılmaz.

## Faz 1 başarı karşılaştırmaları

| Yük | Referans | Kod sonucu | Sapma |
|---|---:|---:|---:|
| 100 W akkor | 0,446–0,447 A | 0,4471 A | yaklaşık %0 |
| 150 W akkor | 0,616 A | 0,615 A | −%0,2 |
| Kettle düşük/kararlı | 0,637 A | 0,656 A | +%3,0 |
| Kettle kaynama | 6,39 A | 6,15 A | −%3,8 |

Dört koşulun tamamı ±%4 sınırındadır. Sonuç ve kapanış kararı [ADR-009](../docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md) içinde kayıtlıdır.

## Faz 2 — Yeni deneyler

Şu anda yeni Faz 2 deneyi planlanmış değildir. Önce [T007 veri aktarımı](../tasks/T007-python-architecture.md) yapılacaktır. Gerçek verinin ortaya çıkardığı somut bir soru deney gerektirirse yeni numara ve yeni protokolle açılır.

## Kayıt standardı

Her yeni deney için amaç/HEDEF, gerçek bağlantı ve ayarlar, LOG, SONUÇ, kaynak veri/hash, kod sürümü ve yorum birlikte saklanır. Yapılmayan adım yapılmış gibi gösterilmez. Ham veri varsayılan olarak Git'e eklenmez; gerekli küçük örnekler ve özetler saklanır.
