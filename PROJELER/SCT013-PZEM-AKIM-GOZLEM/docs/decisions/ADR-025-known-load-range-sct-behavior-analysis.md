# ADR-025 — Bilinen yük aralığında SCT davranış analizi: geçişlerde PZEM'i yeniden referans almama

- **Tarih:** 2026-11-01
- **Durum:** KABUL EDİLDİ — kullanıcı kararı
- **İlişkili kararlar:** ADR-010, ADR-022, ADR-024
- **Kapsam:** Eğitim katsayısı elde edildikten sonra ham SCT kayıtlarının, bilinen yük koşulları altında değerlendirilmesi

## Bağlam

Önceki dokümantasyonda, katsayı belirlendikten sonra bütün ham kayıt boyunca SCT çıktısının PZEM ile tekrar tekrar karşılaştırılacağı izlenimi oluşabiliyordu. Kullanıcının açıkladığı yöntem bu değildir.

PZEM, eğitim aşamasında kararlı yük alanlarını etiketlemek ve SCT katsayısını/modelini elde etmek için proje referansıdır. Ancak katsayı belirlendikten sonra, yükün kapalı/açık durumları ve deneydeki nominal yük aralığı zaten biliniyorsa, geçiş anlarında PZEM'in gecikmeli veya basamaklı okumaları yeniden gerçek akım etiketi gibi kullanılmayacaktır.

Örnek: Deney kaydı, yükün OFF durumunda 0 A nominal koşulda ve ON durumunda yaklaşık 1 A nominal koşulda çalıştığı bilinen bir yük deneyidir. PZEM geçişte 0,8 → 0,6 → 0,8 → 1,0 A gibi değerler üretebilir. Bu ara değerler anlık gerçek akımın doğrulanmış referansı kabul edilmez.

## Karar

1. **Eğitim / katsayı çıkarımı:** PZEM referansı, geçerli ve kararlı yük alanlarında SCT verisini etiketlemek ve katsayı/model çıkarmak için kullanılır. PZEM mutlak ve kusursuz ground truth değildir.
2. **Katsayı sonrası ham veri analizi:** Öğrenilmiş katsayı/model, deneyin tüm SCT ham kayıtlarına uygulanabilir. Analiz yalnızca önceden seçilmiş kararlı pencerelerle sınırlı kalmaz; OFF, ON, geçiş ve yerleşme bölgeleri de incelenir.
3. **Bilinen yük koşulu:** Python'a deneyin bilinen koşulu açıkça verilir (ör. OFF ≈ 0 A, ON ≈ 1 A nominal yük koşulu; deney aralığı 0–1 A). Bu bilgi, SCT'nin beklenen davranışını ve durumlar arasındaki ayrımı incelemek için kullanılır.
4. **Geçişte PZEM'i tekrar etiket olarak kullanmama:** Katsayı sonrası tüm ham veri davranış analizinde PZEM'in geçiş okumaları, SCT'nin anlık doğruluğunu ölçen referans etiketler olarak kullanılmaz. PZEM'in geçişteki gecikmeli/basamaklı değerleri nedeniyle bu karşılaştırma yanıltıcı olabilir.
5. **İncelenecek SCT özellikleri:** OFF taban seviyesi, ON durumundaki SCT çıktısı, OFF/ON ayrımının tekrarlanabilirliği, geçiş yönü ve yanıtı, yerleşme davranışı, gürültü ve katsayının farklı bölümlerdeki tutarlılığı.
6. **Ham veri koruması:** Ham kayıt ve geçiş örnekleri silinmez. Bunlar katsayı sonrası davranış analizinin önemli girdileridir.
7. **Kanıtın doğru adlandırılması:** Bu analiz tek başına bağımsız mutlak doğruluk doğrulaması değildir. Bilinen nominal yük koşulları altında SCT davranışının/tutarlılığının incelenmesidir. Geçiş anındaki gerçek akımın tam değeri bağımsız olarak ölçülmüyorsa o değer bilinmiyor olarak kalır.
8. **Bağımsız genellenebilirlik:** Modül 4'te farklı bir SCT üzerinde aynı modelin denenmesi, sensörler arası genellenebilirlik için ayrı bir doğrulama adımıdır; bu ADR o testi yapılmış saymaz.

## Python veri hattına etkisi

Python akışında birbirinden ayrı iki analiz yolu bulunmalıdır:

- **PZEM referanslı eğitim:** Geçerli paketlerde kararlı PZEM/SCT alanlarını kullanarak etiketleme ve katsayı/model öğrenme.
- **Bilinen yük koşullu SCT davranış analizi:** Öğrenilmiş katsayıyı ham SCT akışına uygulama; deney metadata'sındaki OFF/ON ve nominal yük koşuluna göre tüm kaydı inceleme. Geçiş anlarında PZEM değerlerini otomatik ground-truth etiketi olarak kullanmama.

Bu iki yolun çıktıları raporda ayrı adlandırılmalıdır. İkinci yolun sonucu “PZEM ile geçiş doğrulaması” veya “bağımsız doğruluk testi” olarak sunulamaz.

## Değişmeyen kararlar ve sınırlar

- ADR-022/023/024 kapsamındaki bağımsız akış, BOOT_ID + EVENT_ID paketleme ve paket bütünlüğü kuralları geçerlidir.
- PZEM ve SCT eğitim akışlarının kararlılığı kendi ölçümlerinden bağımsız tespit edilir.
- ON/OFF olay işareti tek başına fiziksel yükün gerçekten anahtarlanmış olduğunu kanıtlamaz. SSR bypass gibi deney modlarında yazılım olayı ile fiziksel yük durumu ayrıştırılmalı; deney metadata'sı gerçek fiziksel koşulu belirtmelidir.
- Nominal OFF/ON yük koşulu, geçiş boyunca her milisaniyedeki gerçek akımın bilindiği anlamına gelmez.
- Python uygulaması, gerçek veri üzerinde analiz ve sonuç logu henüz bu ADR ile yapılmış sayılmaz.

## Kabul özeti

Katsayıyı PZEM referanslı kararlı alanlardan öğren; ardından bilinen yük koşulunu Python'a vererek tüm SCT ham kaydını incele. Geçişlerde PZEM'in gecikmeli ara okumalarını yeniden referans kabul etme.