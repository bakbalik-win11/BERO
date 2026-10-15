# PROJE BERO — GRV-005-14 v03 Başlık Kesilmesi ve ADC Uyarısı İncelemesi

**Tarih:** 2026-10-11  
**Kod:** `GOREVLER/GRV-005/KOD/GRV-005-14-v03-CALISAN-KOD.yaml`  
**Kaynak:** Depodaki v03 YAML ve kullanıcının paylaştığı ESPHome logu.

## 1. Yeni bulgu: başlık uzunluğu

41 alanlı CSV başlığının metin uzunluğu **507 karakter**. ESPHome log satırına zaman/öncelik/tag bilgisi eklendiğinde toplam satır daha da uzuyor. Kullanıcının logunda başlık `...pzem_pf,pz` noktasında kesilmiş görünüyor.

Bu, büyük olasılıkla log satırı uzunluk sınırından kaynaklanan kesilmedir; başlık metninin YAML kaynak kodunda eksik olduğuna dair kanıt yok. Tam sebebi runtime log çıktısında başlığı daha kısa parçalar halinde yazdırarak doğrulanmalı.

### Önerilen çözüm

41 alanın adlarını değiştirme; QC'nin beklediği şemayı koru. Başlığı iki ayrı, açıkça numaralanmış log mesajına böl (ör. `CSV_HEADER_PART_1:` ve `CSV_HEADER_PART_2:`). Dışarı alırken iki parçayı sırayla birleştirip tek başlık satırı oluştur. Parçalar, veri satırlarından ayırt edilebilir olmalı. Gerçek cihazdan tam başlık tekrar alınmadan header PASS verme.

## 2. ADC 92 ms uyarısının yeniden yorumlanması

Log sırası:
- 14:34:42.723 — başlık logu
- 14:34:42.741 — CH0-1T satırı
- 14:34:42.754 — CH1-2T satırı
- 14:34:42.771 — CH2-3T satırı
- 14:34:42.799 — BIAS satırı
- 14:34:42.809 — `adc.sensor took a long time for an operation (92 ms), max is 50 ms`

Depodaki YAML'da dört satırı ve başlığı yazdıran `ESP_LOGI` çağrıları, `grv514_report` script'inin lambda bloğu içindedir. Bu script, son ADC kanalı 1000 örneğe ulaştığında ADC sensörünün `on_value` otomasyonundan tetiklenir.

Bu nedenle 92 ms uyarısının **ADC dönüşümünün kendisinden ziyade, ADC callback'i içinde başlık ve dört uzun CSV satırının senkron loglanmasından kaynaklanması güçlü bir olasılıktır**. Yalnız log zamanları bunu kesin kanıtlamaz; uyarı, çağrı zincirindeki toplam işlem süresini işaret ediyor olabilir.

## 3. Önerilen düzeltme yönü

- ADC callback'i içinde uzun CSV metni yazdırma.
- Ölçüm tamamlandığında sadece tamamlandı bayrağını/sonucu kaydet.
- CSV raporlamasını ADC callback'i dışında, ayrı bir script/interval veya gecikmeli iş akışıyla tetikle.
- Başlığı iki parçaya böl ve QC öncesinde yeniden birleştir.
- Bu düzenlemeyi v03 üzerine yazma; **v04 aday** olarak aç ve önce derle.
- Derlemeden sonra yeni log al; başlık bütünlüğü, satır alan sayısı ve ADC uyarısı yeniden test edilsin.

## 4. Sonuç

- Veri satırları: dört satırın her biri 41 alan.
- Başlık: kaynakta 507 karakter; cihaz log görünümünde kesilmiş.
- ADC 92 ms uyarısı: senkron CSV loglama ile ilişkili olması olası; ADC örnekleme hızının doğrudan ölçümü değildir.
- Mevcut v03 dosyası ve geçmiş kayıtlar korunur. Bu rapor henüz kod değişikliği yapmaz.
