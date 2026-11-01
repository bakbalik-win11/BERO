# 2026-11-01 — HA activity.csv ON/OFF olay aktarım kontrolü

## Kaynak
- Kullanıcı tarafından sağlanan `activity.csv`.
- 1.549 satır, 15 sütun.
- Kayıt zaman aralığı: 2026-11-01 15:00:01.041Z – 16:35:47.771Z (Türkiye saati 18:00:01 – 19:35:47).
- İnceleme yalnız Modül 3 olay kaydı, Modül 3 SSR switch entity'si, Modül 2 ham olay kaydı, Modül 2 EVENT_ID ve STATE entity'lerine dayalıdır.
- Ortak BOOT_ID: `53A14E04372DEB0E67FA07270AC69561`.

## Modül 3 — kaynak olay dizisi
- Modül 3 ham olay entity'sinde EVENT_ID 1–94 eksiksiz ve artan sırada görülüyor.
- Bu aralıkta EVENT_ID atlaması yok.
- ON/OFF dizisi beklenen biçimde dönüşümlü: ON yaklaşık 40 saniye, OFF yaklaşık 20 saniye.
- Son olay EVENT_ID 94 / OFF, 16:35:47.771Z.
- Bu, Modül 3'ün HA olay kaydında olay üretim dizisinin tam olduğunu gösterir; fiziksel SSR kontak/yük anahtarlamasını kanıtlamaz.

## Modül 2 — alıcı geçmişi
Karşılaştırma penceresi Modül 3 EVENT_ID 59–94'tür. Bu aralıkta Modül 3'te 36 olay vardır. Modül 2 ham olay entity'sinde 29 olay bulunmuştur.

### Modül 2'de görünmeyen EVENT_ID'ler
| EVENT_ID | Modül 3 durumu |
|---:|---|
| 60 | OFF |
| 63 | ON |
| 68 | OFF |
| 78 | OFF |
| 88 | OFF |
| 91 | ON |
| 94 | OFF |

- Eksik toplam: 7 / 36.
- Eksik durum dağılımı: 5 OFF, 2 ON.
- Modül 2'de görülen 29 olayın BOOT_ID, EVENT_ID ve STATE değerleri Modül 3'teki karşılıklarıyla aynı.
- Alınan olayların Modül 3 olay kaydından Modül 2 ham olay kaydına gecikmesi 50–273 ms; ortanca 155 ms (29 eşleşme).
- Modül 2'nin ilk görünen olay kaydı EVENT_ID 59 / ON, 16:18:07.851Z'dir. EVENT_ID 1–58 bu Modül 2 history entity aralığında görünmüyor; bu daha erken aralık için alıcı hakkında hüküm kurulmadı.
- EVENT_ID 94 / OFF Modül 3'te var, Modül 2'de yok.

## STATE entity'si hakkında
Modül 2 STATE entity'si yalnız STATE değiştiğinde history kaydı oluşturur. Bu nedenle aynı STATE ile gelen ardışık olaylar (ör. EVENT_ID 59 ON ve 61 ON; arada 60 OFF görünmüyorsa) STATE entity'sinden tek başına izlenemez. Olay kaydı ve EVENT_ID entity'si kontrol edilmelidir. Bu CSV'de Modül 2 EVENT_ID entity'si de 29 olayla sınırlıdır; yukarıdaki yedi atlama ham olay kaydıyla birlikte EVENT_ID history'sinde de vardır.

## Sonuç ve sınırlar
- Modül 3'ün HA olay geçmişinde 1–94 arasında atlama yok.
- Modül 2'nin HA olay geçmişinde, karşılaştırılabilir 59–94 aralığında 7 olay görünmüyor.
- Bu dosya, bu yedi olayın Modül 2 HA history'sinde bulunmadığını kanıtlar; tek başına olayların Modül 3'ten UDP ile hiç gönderilmediğini, ağda kaybolduğunu, Modül 2'de alınıp Recorder'a yazılmadığını veya export sırasında dışarıda kaldığını ayırt etmez.
- Kaynak Modül 3'te her olayın gönderildiğini doğrulayan UDP send logları ve Modül 2'de her olayın alındığını doğrulayan UDP receive logları ile aynı EVENT_ID'ler çapraz kontrol edilmelidir.
- Fiziksel SSR anahtarlaması bu CSV ile doğrulanmaz.

