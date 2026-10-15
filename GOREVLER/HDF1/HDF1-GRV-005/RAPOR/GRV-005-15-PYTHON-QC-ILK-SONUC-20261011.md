# GRV-005-15 — Python QC İlk Sonucu ve Şema Sayımı

- Tarih: 2026-10-11
- Durum: Sentetik testler yerel Python ortamında çalıştırıldı; gerçek cihaz CSV'si üzerinde PASS iddiası yoktur.
- Kod: [GRV-005-15 Python QC v01](../KOD/GRV-005-15-PYTHON-QC-v01.py)
- Sentetik fixture: [GRV-005-15 QC sentetik veri v01](../KOD/GRV-005-15-QC-SENTETIK-TEST-VERISI-v01.csv)

## Sonuç

- Geçerli sentetik CSV: **13/13 kontrol PASS**
- Negatif test senaryoları: **5/5 senaryo doğru sınıflandırıldı**
  1. Geçerli sentetik fixture kabul edildi.
  2. BIAS satırından alan eksiltme tespit edildi.
  3. Sayısal alandaki baştaki boşluk tespit edildi.
  4. Yanlış `time_delta_ms` aritmetiği tespit edildi.
  5. Beklenmeyen 42. sütun tespit edildi.

Bu, QC betiğinin sentetik örneklerde çalıştığını gösterir; gerçek ESP32 verisinin PASS olduğu anlamına gelmez.

## Şema sayımı bulgusu

GRV-005-04 v03 alan listesi ve GRV-005-14 aday YAML başlığı, mevcut listede **41 alan** içeriyor. GRV-005-15 kapsam belgesinde ise 42 alan yazıyor. Sayım, listedeki alan adları üzerinden yapıldı; bu rapor kilitli şemayı sessizce değiştirmez. 42 alan beklentisi dokümantasyon tutarsızlığı olarak kayda alındı ve eski belge korunuyor.

## Sınırlar ve sıradaki iş

- `invalid_count=NOT_TRACKED` izinli metin olarak korunur; sahte sayısal değere çevrilmez.
- Boş alanlar kaynak veriye yazılmaz veya otomatik doldurulmaz.
- PZEM değerlerinin bulunması fiziksel doğruluğu ya da zaman eşleşmesinin doğruluğunu kanıtlamaz.
- Bir sonraki aşama, mevcut GRV-005-14 CSV satır şablonunun 41 alanlı sözleşmeye alan alan eşleştirilmesidir. Bunun ardından QC, gerçek cihazdan zaten alınmış ham log metnine uygulanabilir; yeni ADC testi ön koşul değildir.
- Mevcut YAML, geçmiş raporlar ve eski deneyler değiştirilmemiştir.
