# PROJE BERO — GRV-005-14 v04 ADC Callback Ayrımı Adayı

**Durum:** Depoda ADAYLAR altında saklandı; derlenmedi ve cihaza yüklenmedi.  
**Temel kaynak:** GRV-005-14 v03 çalışan kodu ve 2026-10-11 gerçek cihaz logu.

## Neden v04 adayı açıldı?

v03 logunda:
- 41 alanlı CSV başlığı 507 karakter uzunluğunda; log çıktısı `...pzem_pf,pz` noktasında kesilmiş görünüyor.
- Dört CSV veri satırı ayrı ayrı 41 alan içeriyor.
- CSV başlığı ve dört veri satırı `grv514_report` lambda bloğunda ardışık olarak yazdırılıyor.
- Dört satırın yazılmasından hemen sonra `adc.sensor took a long time for an operation (92 ms)` uyarısı görülüyor.

## v04 adayındaki değişiklikler

1. Dört ADC sensörünün `on_value` akışından doğrudan `script.execute: grv514_report` çağrıları çıkarıldı.
2. Yeni bir `interval: 50ms` kontrolü, dört kanalın da 1000 örneğe ulaşmasını bekliyor ve ardından raporlama script'ini çalıştırıyor.
3. Uzun başlık iki kısa log mesajına ayrıldı:
   - `CSV_HEADER_PART_1|` — ilk 16 alan
   - `CSV_HEADER_PART_2|` — kalan 25 alan
4. Alan adları değiştirilmedi; iki başlık parçası önekleri çıkarılarak birleştirildiğinde özgün 41 alanlı başlığı oluşturmalı.
5. ESP adı `esp32d1` olarak korundu.

## Yorum ve sınırlar

ADC callback'i dışına taşıma, 92 ms uyarısının ADC callback'inde uzun log yazdırılmasından kaynaklanıyor olabileceği varsayımını sınamak içindir. Bu nedensellik log zamanlamasından çıkarılan güçlü bir olasılıktır, kesin kanıt değildir.

Raporlama hâlâ ana ESPHome döngüsünde log çıktısı üretir; bu değişiklik CPU/ana döngü gecikmesini tamamen ortadan kaldırdığını garanti etmez. Yalnızca uzun raporlamayı ADC `on_value` otomasyonundan ayırır. Yeni logda uyarının kaybolup kaybolmadığı ayrıca kontrol edilmelidir.

## Kontrol listesi

- [ ] ESPHome 2026.9.1 ile derleme
- [ ] Derleme başarılıysa derleme kaydını güncelle
- [ ] Henüz derlenmeden cihaza yükleme yapma
- [ ] Gerçek logda `CSV_HEADER_PART_1` ve `CSV_HEADER_PART_2` tam mı kontrol et
- [ ] İki başlık parçasını birleştirip 41 alan olduğunu doğrula
- [ ] Dört veri satırının her biri 41 alan mı kontrol et
- [ ] ADC 92 ms uyarısının devam edip etmediğini kaydet
- [ ] Gerçek satırları GRV-005-15 QC v02 ile kontrol et

## Dosya

`GOREVLER/GRV-005/ADAYLAR/GRV-005-14-v04-ADC-CALLBACK-AYRIMI-ADAYI.yaml`

Bu aday v03'ün üzerine yazmaz. v03 çalışan kod kaydı ve eski raporlar korunur.
