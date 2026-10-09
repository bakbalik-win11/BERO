# PZEM-004T — ölçüm değerlerini yorumlama

## PZEM'in sunduğu değerler

PZEM-004T V3.0 gerilim (V), akım (A), aktif güç (W), enerji (kWh), frekans (Hz) ve güç faktörü (PF) değerlerini sayısal olarak sunar. Normal kullanımda ESP32 analog ADC'sinden RMS akım hesaplamak yerine modülün ölçüm sonuçları okunur.

## Tek fazlı AC ilişkileri

- Görünür güç: S = V_RMS × I_RMS (VA)
- Aktif güç: P = V_RMS × I_RMS × PF (W), uygun PF tanımı varsayımıyla
- Güç faktörü: PF = P / S
- Enerji, zaman boyunca aktif gücün integralidir; PZEM sayaç olarak Wh/kWh raporlar.

PF 1'den küçükse P = V × I eşitliği genel olarak aktif gücü vermez. PZEM'in aktif güç değeri ile V×I arasındaki fark bu nedenle normal olabilir.

## Ölçüm doğrulama

1. Gerilimi True-RMS multimetreyle karşılaştır.
2. Akımı uygun AC pens ampermetreyle karşılaştır.
3. Aktif gücü güç analizörüyle karşılaştır; yalnızca V×I ile doğrulama yapma.
4. Enerji sayacını bilinen yükte belirli süre gözle.
5. PF ve frekansın yük değişince makul biçimde değiştiğini kontrol et.
6. Haberleşme kopması ve geçersiz veri durumunu ayrıca izle.

Üretici doğruluk değerleri BERO'da doğrulanmış kalibrasyon anlamına gelmez. Register ölçeği ve birimler seçilen sürüme göre teyit edilmelidir.