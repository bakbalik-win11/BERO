# MOD2-GRV001 V1.0 – ADS1115 No.10 kalibrasyon denemesi
Tarih: 2026-11-21
Durum: Katsayı hesaplandı; yeni YAML henüz kullanıcı cihazında doğrulanmadı.

## Amaç
ADS1115 fiziksel modül No.10 ve SCT013 30A/1V için, 100 W ve 150 W yüklerde kararlı PZEM/SCT akım okumalarından geçici kalibrasyon katsayısı çıkarmak.

## Kaynak veri ve kararlı pencereler
Kaynak: kullanıcı tarafından aynı oturumda sağlanan `history.csv`.
Saatler Türkiye yerel saatidir (UTC+03:00). Yük geçişleri, sıfır durumları ve ilk geçiş sıçramaları pencerelere alınmadı.

| Yük / pencere | PZEM akım ort. | SCT akım ort. | K = 27.60 × PZEM/SCT |
|---|---:|---:|---:|
| 150 W, 15:57:00–15:57:38 | 0.65050 A | 0.58537 A | 30.67 |
| 150 W, 15:58:33–15:59:58 | 0.65043 A | 0.58507 A | 30.68 |
| 100 W, 16:00:53–16:02:35 | 0.47450 A | 0.42759 A | 30.63 |

Üç pencerenin katsayılarının aritmetik ortalaması yaklaşık 30.6607'dir. Deneme YAML'inde kullanılacak katsayı 30.66 olarak yuvarlanmıştır.

## Değerlendirme
- 150 W iki ayrı kararlı pencerede katsayılar 30.67 ve 30.68 çıktı.
- 100 W penceresinde katsayı 30.63 çıktı.
- Üç pencere birbirini yakından doğruluyor; mevcut 27.60 katsayısı bu veri setinde SCT akımını düşük hesaplıyor.
- PZEM karşılaştırma referansıdır; kusursuz ground truth değildir.
- Katsayı yalnızca ADS1115 No.10 için kaydedilir. Başka ADS1115 modüllerine aktarılmaz.

## Yazılım değişikliği
Kod 0 değiştirilmedi. Ayrı V1.0 YAML dosyasında yalnızca kalibrasyon doğrusal dönüşüm katsayısı 27.60'tan 30.66'ya alındı. Diğer ESPHome ayarları Kod 0 ile aynı bırakıldı.

## Doğrulama durumu
- CSV kararlı pencereleri analiz edildi.
- Katsayı hesaplandı.
- V1.0 YAML hazırlandı.
- ESPHome derlemesi ve cihaz OTA testi henüz yapılmadı.
- Yeni katsayıyla 100 W / 150 W tekrar ölçümü henüz alınmadı.

## Sonraki test
V1.0 yüklendikten sonra aynı 100 W ve 150 W yükleri tekrar ölç. Kararlı PZEM ve SCT ortalamalarını karşılaştır. Bu tekrar testi geçmeden 30.66 kesin kalibrasyon olarak ilan edilmeyecek.
