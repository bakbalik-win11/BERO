# ADR-018 — Modül 2 dört ADC girişli uzun gerilim kaydı

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ — uzun gözlem için firmware geri yüklendi; derleme ve cihaz kaydı bekliyor
- **İlgili görev:** T010
- **Firmware:** [esp32d1.yaml](../../firmware/esp32d1.yaml)

## Karar

Önceki tek kanallı ct_clamp denemesi yerine, ESP32D1 için depo geçmişindeki dört ADC girişli log sürümü yeniden etkinleştirildi. Dört giriş 1 saniye aralıkla voltaj okur ve her örneği ESPHome loguna yazar.

- SCT-1 sarı / GPIO32 / ADC1_CH4
- SCT-2 yeşil / GPIO33 / ADC1_CH5
- SCT-3 mavi / GPIO34 / ADC1_CH6
- Ortak bias turuncu / GPIO35 / ADC1_CH7

ESPHome cihaz kimliği `esp32d1`, görünen ad `ESP32D1` olarak korunur.

## Test koşulu

Bu uzun kayıt turunda SCT-1'in GPIO32'ye bağlı olduğu kullanıcı bildirimi esas alınır. SCT-2 ve SCT-3 bağlı değilse GPIO33 ve GPIO34 okumaları boşta giriş ölçümüdür; bunlar SCT sensör çıktısı veya kanalın çalıştığına dair kanıt sayılmaz. GPIO35 ortak bias izleme noktasıdır.

## Ölçüm sınırları

Bu firmware yalnızca anlık ADC gerilimi yayınlar. `ct_clamp`, RMS/akım hesabı, katsayı veya kalibrasyon filtresi içermez. 1 saniyelik örnekleme 50 Hz dalga şeklini yakalamaz; uzun süreli yavaş gerilim/bias davranışını ve yük geçişlerinin genel etkisini izlemek içindir. Bu sürüm ölçüm doğruluğu veya akım ölçümü kanıtı değildir.

## Beklenen doğrulama

1. ESPHome derlemesi başarılı olmalı.
2. OTA yüklemesinden sonra cihaz `esp32d1` adıyla ağa bağlanmalı.
3. Logda dört sensörün GPIO/etiketleri ve yaklaşık 1 saniyelik yayınları görülmeli.
4. SCT-1 GPIO32, ortak bias GPIO35 ve ampulün kapalı/açık/kapalı zamanları aynı uzun logda işaretlenmeli.
5. Log analizinde yalnız fiziksel olarak bağlı SCT-1 kanalı ölçüm adayı kabul edilmeli; boşta GPIO33/34 değerleri dışlanmalı.

Derleme, OTA ve yeni fiziksel log henüz yapılmadı.
