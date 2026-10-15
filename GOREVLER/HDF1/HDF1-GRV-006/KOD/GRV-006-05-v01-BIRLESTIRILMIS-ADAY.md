# GRV-006-05 v01 — Birleştirilmiş aday kod

## Hedef
GRV-005-14 v06'nın ADC örnekleme ve CSV loglama zincirini korurken GRV-006 Python → ESP32 → geri okuma API eylemini aynı firmware'e eklemek.

## Kaynak ve koruma
- Kaynak: `GOREVLER/GRV-005/KOD/GRV-005-14-v06-CALISAN-KOD.yaml`
- Yeni dosya; kaynak dosya değiştirilmedi.
- ESPHome adı aynen `esp32d1` bırakıldı.
- ADC girişleri: CH0 GPIO33, CH1 GPIO34, CH2 GPIO35, BIAS GPIO32.
- PZEM UART: TX GPIO16 / RX GPIO17, 9600 baud.
- Her ADC kanalında 1000 örnek ve mevcut CSV log satırları korunmuştur.
- Eklenen API action: `grv006_set_value(value: int)`.
- Eklenen echo sensörü: `GRV006 Echo Value`.

## Durum
**ADAY — henüz derleme doğrulaması yapılmadı.** Cihazda yüklemeden önce ESPHome derlemesi yapılmalı. Derleme başarılı olsa bile gerçek ADC satırlarının logda görünmesi ayrıca cihaz testiyle doğrulanmalıdır.

## Beklenen kontrol
1. Derle ve yükle.
2. ESPHome logunda `CSV_HEADER_PART_1`, `CSV_HEADER_PART_2` ve dört satırı (`CH0-1T`, `CH1-2T`, `CH2-3T`, `BIAS`) kontrol et.
3. Python testinde `grv006_set_value` action ile integer gönder; `GRV006 Echo Value` aynı değeri döndürmeli.
4. Log/derleme sonucunu göreve ekle. Fiziksel ölçüm doğruluğu bu testin kapsamı değildir.
