# E11 Log 69 — SCT3 iki primer tur gözlemi

- **Tarih:** 2026-11-01
- **Kaynak:** Kullanıcının yüklediği `esp32d1-logs (69).txt`; 108.063 bayt / 1.466 satır.
- **Orijinal kaynak SHA-256:** `2c031c08b333b9f5900e530f053f1c3894bb9fecd6e049394f946f368321a90c`.
- **Arşiv:** [Ağ kimlikleri maskelenmiş gzip+Base64 log](2026-11-01-e11-log69-sanitized.txt.gz.b64). Açılmış maskeli metin SHA-256: `2dc20bf5e1407c56b71f222683c6c901981ec5a0495555dbd126ec57e8e5b015`.
- **Zaman aralığı:** 12:40:34–12:43:28 (log saatleri).
- **Kanıt sınıfı:** Ham log = kullanıcı tarafından sağlanan cihaz çıktısı; fiziksel iki tur düzeni = kullanıcının deney açıklaması.

## Deney düzeni

Kullanıcının açıklamasına göre:
- SCT1 / GPIO32: mevcut düzen, değişiklik yok.
- SCT2 / GPIO33: iletken tek tur; kablo düz.
- SCT3 / GPIO34: şebeke yük iletkeni SCT'nin açıklığından iki kez geçirilmiş (iki primer tur).
- YAML, K=24.22, GPIO atamaları, örnekleme penceresi ve çevrim ayarları değiştirilmedi.

**Terim netliği:** Buradaki “iki tur”, SCT'nin sekonder/sensör kablosunun sarılması değildir. Yükün primer iletkeninin CT açıklığından iki kez geçirilmesidir. CT çıktısının yaklaşık iki katına çıkması beklenen amper-sarım etkisidir.

## Log kapsamı ve örnek sayısı

- Toplam 262 ct_clamp debug kaydı ve 262 akım yayını bulundu.
- Kanal kayıtları: SCT1 87, SCT2 87, SCT3 88. SCT3'ün ilk açılış/geçiş kaydı 444 örnek / 2.220 SPS olduğu için normal çevrim istatistiğinden çıkarıldı.
- Karşılaştırma: 87 normal çevrim/kanal.

| Kanal | Ortalama farklı örnek / 200 ms | Ortalama SPS | SCT1'e göre |
|---|---:|---:|---:|
| SCT1 / GPIO32 | 3393,34 | 16.966,72 | referans |
| SCT2 / GPIO33 | 3264,95 | 16.324,77 | −%3,78 |
| SCT3 / GPIO34 | 3352,06 | 16.760,29 | −%1,22 |

SCT3'ün iki primer tur kullanması, örnek sayısının da iki katına çıkması anlamına gelmez. Örnek sayısı/SPS ayrı bir yazılım-örnekleme gözlemidir.

## Akım sonuçları

| Kanal | Yayın sayısı | Ortalama akım | Medyan | Standart sapma |
|---|---:|---:|---:|---:|
| SCT1 / GPIO32 | 87 | 0,424793 A | 0,425 A | 0,010238 A |
| SCT2 / GPIO33 | 87 | 0,412862 A | 0,413 A | 0,008719 A |
| SCT3 / GPIO34 — iki primer tur | 87 | 0,857874 A | 0,857 A | 0,007093 A |

- SCT3 / SCT1 = **2,0195**.
- SCT1'in iki katı = 0,849586 A.
- SCT3 ölçümü bu değerden +0,008288 A, yani yaklaşık **+%0,98** farklıdır.
- İki tur verisi tek tur eşdeğerine indirildiğinde SCT3 = 0,428937 A; SCT1'in 0,424793 A değerinden yaklaşık **+%0,98** yüksektir.

## Yorum ve karar

1. **İki primer tur sonucu beklenen yönde ve büyüklüktedir.** SCT3'ün ortalaması SCT1'in yaklaşık 2,02 katıdır. Tam iki kat beklentisine göre fark yaklaşık %0,98'dir. Bu oturum için iki tur davranışı olumlu gözlem olarak kaydedilir.
2. Bu, CT'nin iki primer geçişte yaklaşık iki kat amper-sarım görmesiyle uyumludur. İki tur, aynı fiziksel akımın CT tarafından yaklaşık iki kat ölçeklenmiş okunmasını sağlar; tek tur akımının kendisi değişmiş değildir.
3. İki tur testi **kalibrasyon, PZEM doğrulaması veya ±%4 kabul testi değildir**. Logda PZEM/UNIT eşzamanlı referansı bulunmuyor.
4. Örnek sayısı ayrı değerlendirilmelidir: SCT2, SCT1'den %3,78 düşük; SCT3 %1,22 düşük örnek sayısına sahip. Bu farklar akımın iki kat görünmesinin nedeni değildir.
5. SCT2 akım ortalaması SCT1'den yaklaşık %2,81 düşüktür; bu log tek başına nedenini ayırt etmez.
6. Başlangıçtaki SCT3 kısmi kaydı normal istatistiklerden çıkarılmıştır. Log, kanal başına 87 normal çevrim içerir; daha uzun tekrarlar tekrarlanabilirlik için yararlı olacaktır.

## Firmware / donanım kararı

- YAML, K=24.22, GPIO32/33/34 eşlemesi, 200 ms pencere, 250 ms slot, 50 ms geçiş payı ve 2 s çevrim değiştirilmedi.
- Bu gözlem nedeniyle kod değişikliği veya yeni kalibrasyon katsayısı önerilmez.
- İki tur ölçümünün raporlanacağı veri kayıtlarında `primary_turns=2` gibi açık bir deney metadata alanı tutulmalıdır. Tek tur ve iki tur verileri etiketlenmeden aynı eğitim grubuna karıştırılmamalıdır.

## Yeniden üretim

Arşivlenmiş logu açmak için:

```bash
base64 -d 2026-11-01-e11-log69-sanitized.txt.gz.b64 | gunzip > 2026-11-01-e11-log69-sanitized.txt
```
