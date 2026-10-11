# PROJE BERO — GRV-005-14 v03 Çalışan Kod Kaydı

**Durum:** Kullanıcı derlemenin başarılı olduğunu bildirdi (2026-10-11). Derleme logu bu kayıtla birlikte sunulmadı.

## Hedef

GRV-005-14 v02'nin gerçek cihaz logunda görülen CSV alan kaymasını düzeltmek ve başlık ile CH0, CH1, CH2, BIAS satırlarını aynı 41 alanlık şemada hizalamak.

## Korunanlar

- ESP adı: `esp32d1` (değiştirilmedi).
- GRV-005-14 v02 çalışan kodu ve geçmişi korunur; üzerine yazılmaz.
- v03 ayrı sürüm olarak kaydedilmiştir.
- Örnekleme hedefi: CH0, CH1, CH2 ve BIAS için 1000 örnek.
- Hesaplanmayan CSV alanları boş bırakılır.

## Düzeltmeler

- CH0/CH1/CH2 CSV satırlarında boş alan dizilimi 41 alanlı başlıkla hizalandı.
- BIAS satırında `adc_range` (`max - min`) alanı ve argümanı eklendi.
- BIAS özet değerleri kendi sütunlarına yerleştirildi.
- PZEM akım, güç ve güç faktörü alanları CSV satırlarına eklendi.

## Doğrulama durumu

- YAML statik ayrıştırma: **PASS** (önceki statik kontrolde).
- CSV şablon alan sayısı: **41** (önceki statik kontrolde).
- ESPHome derlemesi: **KULLANICI TARAFINDAN BAŞARILI OLARAK BİLDİRİLDİ**.
- Derleme sürümü ve tam derleme logu: bu kayda eklenmedi.
- Cihaza yükleme: bu mesajla doğrulanmış değil.
- Gerçek cihazdan v03 CSV üretimi ve GRV-005-15 QC: ayrıca doğrulanmalı.

## Sonraki doğrulama

Derleme logu mevcutsa ileride bu kayda eklenebilir. Cihaza yükleme ve gerçek CSV QC sonuçları ayrı bir rapor olarak tutulmalı; v02 geçmişi değiştirilmemeli.
