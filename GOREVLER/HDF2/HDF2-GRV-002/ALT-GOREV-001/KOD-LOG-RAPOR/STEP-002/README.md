# STEP-002 — Tek ESP'den ham sinyal yakalama

**Durum:** BEKLİYOR

- ESP32-WROOM'a doğrulanmış aday firmware'i yükle.
- TEST-001: SCT ve BIAS bağlı, yük kapalı, 100 frame yakala.
- Frame ID, marker'lar, örnek sayısı/sırası ve DMA/USB overflow göstergelerini kaydet.
- Ham kaydı değiştirmeden `LOG/` altında sakla.

Başarı, yalnızca gerçek cihaz kaydı ve loglarla değerlendirilecektir.


# STEP-002 — Tek ESP'den ham sinyal yakalama

**Durum:** BEKLİYOR

## Amaç
Tek ESP32-WROOM üzerinde ham SCT ve BIAS örneklerini yakalayıp gerçek frame kaydı elde etmek.

## Planlanan işler
1. Derlenmiş firmware'i ESP'ye yükle ve seri bağlantıyı doğrula.
2. TEST-001: SCT/BIAS bağlı, yük kapalı; 100 frame al.
3. Frame ID, marker, kanal örnek sayısı ve DMA/USB overflow göstergelerini kaydet.
4. Kaynak binary kaydı değiştirmeden LOG'a sakla.

## Tamamlanan işler
- Henüz tamamlanan iş kaydedilmedi.

## Kapanış ölçütü
Gerçek cihazdan ham kayıt ve ilgili seri logları saklanmış; frame bütünlüğü raporlanmış.

## Çalışma kaydı
Her tamamlanan işin tarihi, kullanılan kod sürümü, test sonucu ve kanıt bağlantısı aşağıya alt alta eklenecek. Step ancak kapanış ölçütü kanıtlandığında kapatılacak.

