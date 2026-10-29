# E00A — Ham sinyal kaydı ve temel istatistikler

## Amaç
Paketleme veya sürekli veri aktarım mimarisine karar vermeden önce SCT girişindeki ham ADC örneklerinden işe yarar, anlaşılır bir ilk sonuç çıkarmak. Öncelik canlı osiloskop görüntüsü değil; farklı donanım koşullarının temel istatistiklerle karşılaştırılmasıdır. Grafik, istatistiklerin açıklayamadığı durumları incelemek için yardımcı çıktıdır.

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
- İsteğe bağlı tanı grafiği: ADC değeri-zaman. Yalnızca beklenmeyen istatistikleri, kırpılma belirtilerini, sıçramaları veya bozuk/kopuk örnekleri araştırmak için kullanılır; sürekli canlı grafik zorunlu değildir.

Bu istatistikler ham ADC değerlerini tanımlar; tek başlarına amper ölçümü veya gürültünün kesin ölçümü değildir. Standart sapma hem gürültüden hem gerçek AC sinyalinden etkilenebilir.

## Basit örnek sayısı kontrolü
Beklenen örnek sayısı yaklaşık olarak hedef hız × gerçek kayıt süresidir. Okunan sayı ile karşılaştırılır. Bu ilk kontrol, zamanlama aralıklarının kusursuz olduğunu veya hiç örnek kaybolmadığını kanıtlamaz. Belirgin fark görülürse önce nedenini araştırırız.

## Karar
İlk soru, bias-only, SCT yüksüz ve yük altındaki koşulların istatistiklerinde anlamlı fark olup olmadığıdır. Grafik yalnızca yorumlamaya yardımcı olur. Örnekleme hızlarını geniş kapsamlı karşılaştırma, yavaş oynatma, üç ESP32 eşzamanlama, DMA veya çift buffer bu ilk adımın kabul koşulu değildir.

İlk kayıtlardan sonra basit edinim ve aktarım yeterliyse karmaşık mimari kurmayız. Yetersizliği gösteren kanıt varsa sonraki deneyi o soruya göre seçeriz.

## Durum
PLANLANDI. Firmware, kayıt, grafik ve fiziksel ölçüm henüz yapılmadı.


## Deney YAML dosyalarının rolleri
- [metadata.yaml](metadata.yaml): deney kimliği, durum, koşul listesi ve kısa özet metadata'sı.
- [experiment.yaml](experiment.yaml): planlanan koşulların açıklamalı, ayrıntılı çalışma planı.

İki dosya aynı bilgiyi farklı amaçlarla taşır; `metadata.yaml` kısa indeksleme içindir, `experiment.yaml` ise deney koşullarını açıklar. `experiment.yaml` şu anda firmware tarafından otomatik okunmaz. Gerçekte kullanılan kart, GPIO ve ayarlar ölçüm öncesi doğrulanıp LOG'a yazılmalıdır.
