# PROJE BERO — GRV-005-15 doğrudan çalıştırma sonucu — v06 CSV

**Durum:** PASS — gerçek yerel çalıştırmada 14/14 kontrol başarılı  
**Çalıştırma ortamı:** Kullanıcının Mac mini bilgisayarı, macOS Terminal, `python3`  
**Girdi CSV:** `GOREVLER/GRV-005/RAPOR/GRV-005-14-v06-QC-GIRDİSİ-20261011.csv` (masaüstündeki kopya)  
**Script:** `GOREVLER/GRV-005/KOD/GRV-005-15-PYTHON-QC-v02.py` (depodaki scriptin masaüstündeki kopyası)

## Gerçek çalıştırma kanıtı

Kullanıcı aşağıdaki komutu Terminal'de çalıştırdı:

```bash
python3 "$(find . -maxdepth 1 -name 'GRV-005-15-PYTHON-QC-v02.py' -print -quit)" "$(find . -maxdepth 1 -name 'GRV-005-14-v06-QC-GIR*20261011.csv' -print -quit)"
```

Terminal'in bildirdiği dosya: `GRV-005-14-v06-QC-GIRDİSİ-20261011.csv`.

Gerçek terminal çıktısının son satırları:

```text
PASS | BIAS row's own ADC summary aligns with bias_* fields — BIAS row found
PASS | No unnamed overflow columns — CSV parser detected no extra fields
RESULT: PASS (14/14 checks)
NOTE: PASS is structural QC only; it is not proof of physical measurement accuracy.
```

Kullanıcı çıktıyı sohbet içinde paylaştı. Görünen çıktıda 14 kontrolün tamamı PASS. **Shell exit code ayrıca kaydedilmedi**; bu nedenle rapor yalnızca görünür program çıktısına dayanır, exit code=0 iddiasında bulunmaz.

## Kontrol kapsamı ve sonuç

- Başlık tam 41 alan; beklenen alan sayısıyla eşleşiyor.
- Tam dört veri satırı var ve her satır 41 alan içeriyor.
- CH0-1T, CH1-2T, CH2-3T ve BIAS birer kez bulunuyor.
- Tüm satırlar ortak `measurement_id=esp32d1_235_001` değerini taşıyor.
- Her satırda 1000 geçerli örnek bildiriliyor.
- Pencere süresi, pencere merkezi ve zaman farkı aritmetiği geçiyor.
- 33 sayısal alan beklenen türlere ayrıştırılıyor.
- Üç akım kanalında ham RMS alanı dolu.
- Alanlarda baştaki/sondaki boşluk ve fazladan sütun yok.
- ADC min/max/range ilişkisi geçiyor.
- PZEM akım/güç/PF alanlarının varlığı kontrolü geçiyor; fiziksel doğruluk iddiası değildir.
- BIAS satırındaki ADC özeti ile bias_* alanları uyumlu.

## Yorum ve sınırlar

Bu sonuç, depodaki QC v02 betiğinin kullanıcı Mac'inde gerçek CSV kopyasına karşı doğrudan çalıştırıldığını ve görünür çıktıda **14/14 PASS** verdiğini kanıtlar. Önceki bağımsız 14/14 değerlendirmesinden ayrı bir kanıt olarak kaydedilmiştir.

Bu, CSV'nin yapısal QC ölçütlerini karşıladığını gösterir; fiziksel akım ölçüm doğruluğunu, kalibrasyonu veya donanım zincirinin mutlak doğruluğunu kanıtlamaz. `invalid_count` alanı bu girdide `NOT_TRACKED` olarak göründüğünden, örneklerin geçerlilik takibi ayrıca ele alınmış sayılmaz.

## Kaynak dosya kimlikleri

Çalıştırmadan önce depodan geri okunan dosyalar:
- Script blob SHA: `1c455032af877e8898c6043a9bab97c8a38e7746`
- CSV blob SHA: `a71c03adb10cb8ba5264f7f8f1abb486900d0183`

## Sonraki adım

GRV-005-15'in bu doğrudan çalıştırma adımı tamamlandı. Yeni firmware/donanım deneyi açmadan önce mevcut kayıtlar korunmalı ve görevdeki sonraki somut hedef belirlenmeli. v06 YAML, ham cihaz logu ve CSV girdisi değiştirilmedi.
