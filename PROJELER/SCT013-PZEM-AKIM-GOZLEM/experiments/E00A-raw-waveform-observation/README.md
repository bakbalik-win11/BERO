# E00A — Ham sinyal kaydı ve temel istatistikler

## Amaç
İlk olarak ESP32 dahili ADC'sinden gerçekte ne okunduğunu görmek: ham örnekleri kaydetmek ve bilgisayarda zaman grafiğiyle görselleştirmek. Grafik bu adımın temel inceleme aracıdır; istatistikler grafiği tamamlar ve koşullar arasındaki farkı özetler. Paketleme veya sürekli veri aktarım mimarisi hakkında karar vermek için önce kaydın sinyali nasıl temsil ettiğini gözlemleyeceğiz.

Bu bir laboratuvar doğrulama deneyi değildir. Amaç, “SCT devreye girince ham ADC verisinde ne değişiyor?” sorusuna basit bir yanıt bulmaktır.

## Kapsam ve sıra
Üç koşul, aynı kayıt yaklaşımıyla karşılaştırılır:
1. **Bias-only:** SCT bağlı değil.
2. **SCT yüksüz:** SCT bağlı, ölçülen iletkenden akım geçmiyor.
3. **100 W akkor:** SCT bağlı, ampul açık.

İlk denemede yalnızca **2 kS/s hedef örnekleme hızı** kullanılır. Bu, BERO için daha önce seçilen başlangıç değeridir; bu deneyde hızın en iyisi olduğu varsayılmaz. Her koşul için yaklaşık 1 saniyelik ham kayıt hedeflenir. Gerçek süre ve örnek sayısı kaydedilir; süre/hedef hızdan beklenen örnek sayısı ile basitçe karşılaştırılır.

İlk sonuçlar alındıktan sonra örnekleme hızını karşılaştırmanın belirli bir soruya yanıt vereceği görülürse 1 ve 2,5 kS/s kayıtları eklenebilir. İlk denemede üç hızı her koşulda tekrarlamak veya üç ESP32'yi eşzamanlamak zorunlu değildir.

## Her kayıttan üretilecek çıktılar
- Ham ADC örneklerinin yerel dosyaya kaydı; veri varsayılan olarak Git'e eklenmez.
- Ortalama, minimum, maksimum, tepe-tepe aralığı ve standart sapma.
- Hedef örnekleme hızı, gerçek kayıt süresi, örnek sayısı ve mümkünse yaklaşık gerçekleşen örnekleme hızı.
- Koşulları kıyaslayan kısa bir istatistik tablosu.
- ADC ham değeri-zaman grafiği: her koşulun kaydını bilgisayarda görselleştir. Bu, sinyalin şeklini ve kayıt içindeki değişimleri incelemek için temel çıktıdır; canlı osiloskop arayüzü zorunlu değildir.

Bu istatistikler ham ADC değerlerini tanımlar; tek başlarına amper ölçümü veya gürültünün kesin ölçümü değildir. Standart sapma hem gürültüden hem gerçek AC sinyalinden etkilenebilir.

## Basit örnek sayısı kontrolü
Beklenen örnek sayısı yaklaşık olarak hedef hız × gerçek kayıt süresidir. Okunan sayı ile karşılaştırılır. Bu ilk kontrol, zamanlama aralıklarının kusursuz olduğunu veya hiç örnek kaybolmadığını kanıtlamaz. Belirgin fark görülürse önce nedenini araştırırız.

## Karar
İlk soru, ham kaydın bilgisayarda nasıl göründüğü ve bias-only, SCT yüksüz ve yük altındaki koşulların grafikleri ile istatistiklerinin nasıl farklılaştığıdır. Grafik temel inceleme çıktısıdır. Örnekleme hızlarını geniş kapsamlı karşılaştırma, yavaş oynatma, üç ESP32 eşzamanlama, DMA veya çift buffer bu ilk adımın kabul koşulu değildir.

İlk kayıtlardan sonra basit edinim ve aktarım yeterliyse karmaşık mimari kurmayız. Yetersizliği gösteren kanıt varsa sonraki deneyi o soruya göre seçeriz.

## Durum
PLANLANDI. Firmware, kayıt, grafik ve fiziksel ölçüm henüz yapılmadı.


## Deney YAML dosyalarının rolleri
- [metadata.yaml](metadata.yaml): deney kimliği, durum, koşul listesi ve kısa özet metadata'sı.
- [experiment.yaml](experiment.yaml): planlanan koşulların açıklamalı, ayrıntılı çalışma planı.

İki dosya aynı bilgiyi farklı amaçlarla taşır; `metadata.yaml` kısa indeksleme içindir, `experiment.yaml` ise deney koşullarını açıklar. `experiment.yaml` şu anda firmware tarafından otomatik okunmaz. Gerçekte kullanılan kart, GPIO ve ayarlar ölçüm öncesi doğrulanıp LOG'a yazılmalıdır.
