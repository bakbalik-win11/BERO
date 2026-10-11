# GRV-005-15 Python QC v01 — Kod Notu

- Tarih: 2026-10-11
- Hedef: CSV v03 verisini kaynak dosyayı değiştirmeden yapısal ve temel tutarlılık kontrollerinden geçirmek.
- Girdi: `GRV-005-15-QC-SENTETIK-TEST-VERISI-v01.csv` (sentetik; gerçek cihaz kaydı değildir).
- Kod: `GRV-005-15-PYTHON-QC-v01.py`
- Bağımlılık: Python 3 standard library; üçüncü taraf paket yok.

## Çalıştırma

```bash
python3 GRV-005-15-PYTHON-QC-v01.py --self-test
python3 GRV-005-15-PYTHON-QC-v01.py GRV-005-15-QC-SENTETIK-TEST-VERISI-v01.csv
```

## Kontroller

- Tam başlık ve alan sayısı
- Dört beklenen kanal ve ortak measurement_id
- Kanal başına 1000 örnek
- Pencere süre/merkez/time_delta aritmetiği
- Sayısal alan tipleri, boşluklar ve ADC min/max/range
- PZEM alanlarının varlığı
- BIAS satırının kendi ADC özetinin bias_* alanlarıyla tutarlılığı
- Fazla sütunlar

## Kanıt sınırı

Sentetik testte PASS, kodun test örneklerinde beklenen hataları yakaladığını gösterir. Gerçek cihaz verisi, fiziksel ölçüm doğruluğu, gerçek Modbus yanıt zamanı veya ESP→Python→ESP dönüş döngüsü için kanıt değildir. Kod kaynak CSV'yi değiştirmez.
