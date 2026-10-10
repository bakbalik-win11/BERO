# BIAS / 1T / 2T / 3T — Ham Log Kaydı

- **Görev:** GRV-004
- **Tarih:** 2026-10-10
- **Cihaz:** `esp32d1`
- **Kaynak log:** Kullanıcının sağladığı 5.000 satırlık ESPHome log dosyası.
- **Kod kaydı:** [esp32d1-bias-1t-2t-3t-user-config-20261010.yaml](KOD/esp32d1-bias-1t-2t-3t-user-config-20261010.yaml)
- **Ham log:** [esp32d1-bias-1t-2t-3t-20261010-raw.txt](LOG/esp32d1-bias-1t-2t-3t-20261010-raw.txt)

## Bu kayıtta görülenler

Log zaman aralığı yaklaşık **16:48:36.216–16:50:53.970**. Logda dört ADC kanalının voltaj yayınları ve PZEM ölçümleri bulunuyor.

Logda görülen, iki ondalık basamağa yuvarlanmış ADC değerlerinin özeti:

| Kanal | Log satırı sayısı | Gözlenen min. | Gözlenen maks. |
|---|---:|---:|---:|
| BIAS | 1209 | 1.58 V | 1.80 V |
| 1T | 1209 | 1.54 V | 1.83 V |
| 2T | 1208 | 1.54 V | 1.74 V |
| 3T | 1209 | 1.60 V | 1.69 V |

**Not:** Bu min./maks. değerler ham ADC sayımları değil, loga yazdırılmış iki ondalıklı voltaj değerlerinden çıkarılmıştır. Ortalama ve standart sapma için hesaplanan değerler de aynı yuvarlanmış loga dayanır; bu yüzden bunlar yüksek hassasiyetli ADC istatistikleri olarak değerlendirilmemelidir.

PZEM için logda 27 yayın bulunuyor. Gözlenen aralıklar:
- Gerilim: 227.9–229.8 V
- Akım: 0.028–0.029 A
- Güç: 1.7–1.9 W
- Frekans: 49.9–50.0 Hz
- Enerji: 10388 Wh

## Deney sınırları ve doğrulama notu

- Bu logda ALT-GÖREV-03 için `N=0`, `1000 okuma tamamlandı`, ortalama/min./maks. raporu veya ölçülmüş örnekleme hızı satırları bulunmuyor.
- Paylaşılan YAML anlık görüntüsünde ADC `update_interval: 1s` olarak tanımlı. Buna karşılık ham logdaki yayın zamanları daha sık görünüyor. PZEM adları da YAML anlık görüntüsünde Türkçe, logda İngilizce. Bu nedenle kaydedilen YAML **kullanıcı tarafından paylaşılan yapılandırma anlık görüntüsüdür; ham logu üreten birebir derlenmiş dosya olduğu doğrulanmış değildir.**
- Kayıtlar birbirinden ayrılmadan saklanmıştır; geçmiş dosyaların üzerine yazılmamıştır.
- Bu kayıt, dört kanal için 1000 ham ADC örneğiyle tamamlanmış bir hız testi olarak işaretlenmemelidir.

## Sonraki adım

ALT-GÖREV-03 için ayrı kodla dört kanalın her birinden 1000 yeni ADC dönüşümü toplama ve ölçüm sonuçlarını test sonunda loglama yaklaşımı ayrıca doğrulanacaktır.
