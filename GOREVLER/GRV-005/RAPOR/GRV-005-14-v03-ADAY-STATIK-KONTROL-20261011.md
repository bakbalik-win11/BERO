# PROJE BERO — GRV-005-14 v03 CSV Hizalama Adayı

**Durum:** Statik kontrol geçti; ESPHome derlemesi yapılmadı; cihaza yüklenmedi.

## Hedef

GRV-005-14 v02'nin gerçek cihaz logunda görülen CSV alan kaymasını düzeltmek ve başlık ile CH0, CH1, CH2, BIAS satırlarını aynı 41 alanlık şemada hizalamak.

## Korunanlar

- ESP adı: `esp32d1` (değiştirilmedi).
- Önceki v02 çalışan YAML ve ona ait Git kayıtları değiştirilmedi.
- Aday YAML görev deposunun `KOD` klasörüne taşınmadı.
- Örnekleme hedefi: CH0, CH1, CH2 ve BIAS için 1000 örnek.
- Henüz hesaplanmayan CSV alanları boş bırakılıyor.

## Bu adayda yapılan düzeltme

- CH0/CH1/CH2 satırlarının virgül/boş alan dizilimi 41 alanlı başlıkla eşleştirildi.
- BIAS satırında `adc_range` değeri (`max - min`) argüman listesine eklendi.
- BIAS satırındaki `bias_mean`, `bias_std`, `bias_min`, `bias_max` alanları ayrı sütunlara yerleştirildi.
- PZEM değerleri `pzem_current`, `pzem_power`, `pzem_pf` sütunlarına hizalandı; henüz sağlanmayan gerilim/frekans/enerji alanları boş kalıyor.

## Statik kontrol sonucu

- YAML ayrıştırma: **PASS** (özel `!secret` etiketi test sırasında çözümlendi).
- Başlık alan sayısı: **41**.
- CH0 satır şablonu: **41** alan, **22** printf dönüşümü.
- CH1 satır şablonu: **41** alan, **22** printf dönüşümü.
- CH2 satır şablonu: **41** alan, **22** printf dönüşümü.
- BIAS satır şablonu: **41** alan, **20** printf dönüşümü.
- Ek sütun konumu kontrolleri: **PASS**.
- Bu kontroller şablon ve alan sayısını doğrular; ESPHome/C++ derlemesinin yerine geçmez.

## Derleme ve cihaz doğrulaması

Bu ortamda `esphome` komutu ve Python `esphome` modülü bulunmadığından gerçek ESPHome derlemesi çalıştırılamadı. Bu nedenle:

1. **ESPHome derlemesi: BEKLEMEDE**
2. **Cihaza yükleme: YAPILMADI**
3. **Gerçek cihazdan v03 CSV üretimi: YOK**
4. **Gerçek v03 CSV için GRV-005-15 QC: BEKLEMEDE**

## Sonraki adım

Bu dosyayı ESPHome 2026.9.1 ortamında ayrı aday olarak derle. Derleme başarılı olursa sonucu kaydet. Gerçek v03 logu alındıktan sonra 41 sütun ve Python QC doğrulanmalı. Derleme doğrulanmadan kod görev deposundaki `KOD` klasörüne alınmayacak.
