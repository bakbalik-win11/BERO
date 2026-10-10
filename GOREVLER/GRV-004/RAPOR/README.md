# GRV-004 — PZEM + SCT013 Üç Kanal Okuma

## Seviye: İlk birikimli ESPHome yapılandırması — derleme ve çalışma logu başarılı

- **Kart / cihaz adı:** ESP32D1 / `esp32d1`
- **Ağ adresi:** `192.168.0.8`
- **ESPHome sürümü:** 2026.9.1
- **Framework:** ESP-IDF
- **PZEM UART:** TX GPIO16, RX GPIO17, 9600 baud, 8N1
- **PZEM Modbus adresi:** 0x01
- **SCT013 analog girişleri:** GPIO32, GPIO33, GPIO34
- **ADC ayarı:** 12 dB attenuation, Samples: 1, update interval 1 s
- **Hesaplama:** Ortalama/RMS veya örnek biriktirme yapılmıyor; bu seviyede üç kanalın voltaj okumaları izleniyor.

## Derleme ve bağlantı sonucu

Logda ESPHome 2026.9.1 derlemesi 2026-10-10 15:56:15 +0300 olarak kayıtlı. Cihaz `192.168.0.8` adresinde bulunmuş, API bağlantısı ve handshake başarılı. Üç ADC kanalının da `Handle Init`, `Config`, `Calibration` ve `Overall Init` durumları OK.

## Logdan gözlenen örnekler

- GPIO32 / CH1: yaklaşık 1.658–1.669 V aralığında örnekler.
- GPIO33 / CH2: yaklaşık 1.638–1.669 V aralığında örnekler.
- GPIO34 / CH3: yaklaşık 1.643–1.669 V aralığında örnekler.
- PZEM gerilimi: yaklaşık 232.0–233.7 V.
- PZEM akımı: 0.028–0.029 A.
- PZEM gücü: yaklaşık 1.60–1.80 W.
- PZEM frekansı: 50.0 Hz.
- Enerji: 10387 Wh (logdaki değer).

## Bu seviyenin sonucu

**Başarılı:** yapılandırma doğrulanmış cache ile açılmış, ESP32D1'e bağlanılmış, PZEM telemetrisi ve üç ADC voltaj sensörü logda görünmüş.

**Henüz yapılmadı:** üç kanalın her birinde art arda 1000 ham örnek alan hızlı kararlılık testi. Bu log, saniyelik ESPHome ADC güncellemeleridir; hızlı 1000×3 testi olarak değerlendirilmemelidir.

## Kayıt dosyaları

- `KOD/esp32d1-pzem-sct-3kanal.yaml`: bu seviyede kullanılan tam YAML.
- `LOG/esp32d1-logs.md`: kullanıcı tarafından yüklenen loglardan doğrulanan bağlantı, yapılandırma ve örnek sonuçlar.
- `ALT-GOREV-02-FIZIKSEL-OKUMA.md`: daha önce kaydedilmiş fiziksel bias ölçümü.

## Notlar

Logda ESP32 rev3.1 için `minimum_chip_revision: "3.1"` ve `sram1_as_iram: true` önerileri uyarı olarak görünüyor; bunlar derlemeyi/çalışmayı engellememiştir. Bu aşamada mevcut yapılandırmaya dokunulmamıştır.


## Sonraki seviye — BIAS + 1T/2T/3T adlandırması

- **Durum:** Kullanıcı tarafından başarılı olarak bildirildi; bağlantılar OK.
- **Fiziksel referans:** GPIO32 / BIAS = 1,65 V (multimetre).
- **Kod:** [esp32d1-bias-1t-2t-3t.yaml](KOD/esp32d1-bias-1t-2t-3t.yaml)
- **Seviye raporu:** [BIAS + 1T/2T/3T raporu](BIAS-1T-2T-3T.md)
- **Not:** Bu ayrı bir kayıt dosyasıdır; önceki üç kanal YAML dosyası değiştirilmedi. ESPHome canlı ADC değeri ve 1000×3 hızlı örnekleme sonucu henüz bu rapora eklenmedi.
