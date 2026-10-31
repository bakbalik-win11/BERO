# ADR-017 — Modül 2 tek SCT kanalına indirgeme

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ — kontrollü test yapılandırması; derleme ve fiziksel doğrulama bekliyor
- **İlgili görev:** T010
- **İlgili firmware:** [esp32d1.yaml](../../firmware/esp32d1.yaml)

## Bağlam

Modül 2'nin önceki firmware'inde GPIO32, GPIO33 ve GPIO34 için üç ayrı ADC kaynağı ve üç ayrı ct_clamp akım sensörü aynı ESP32 üzerinde tanımlıydı. Kanal testleri sırasında fiziksel SCT bağlı olmayan GPIO girişlerinde de akım değerleri üretildi. Bu değerler açıkta kalan ADC girişleri nedeniyle geçerli ölçüm kabul edilemez.

SCT-3 fiziksel olarak GPIO34'e bağlandığında 0.509–1.123 A aralığında 23 yayın görüldü; medyan 0.553 A. Bu kayıt tek başına yükün açık/kapalı tepkisini veya doğruluğu kanıtlamaz. Üçlü yapılandırmanın ölçüm kalitesini düşürdüğü henüz kanıtlanmış değildir; kanal zamanlaması/işlem yükü etkisi test edilecek hipotezdir.

## Karar

Kontrollü karşılaştırma için firmware tek aktif SCT kanalına indirgenir:

- SCT-3 / GPIO34 / ADC1_CH6: tek ADC kaynak sensörü ve tek ct_clamp.
- Ortak bias / GPIO35 / ADC1_CH7: voltaj izleme korunur.
- GPIO32 ve GPIO33 fiziksel modülde kalır ancak bu YAML'da tanımlanmaz ve okunmaz.
- sample_duration: 200ms, update_interval: 5s ve nominal 30 A/V dönüşümü korunur.
- Cihaz adı, Wi-Fi, API, OTA ve ESP-IDF ayarları değiştirilmez.

## Beklenen test

1. Tek ct_clamp akım entity'si yayımlanmalı.
2. GPIO35 bias değeri logda izlenmeli.
3. Aynı SCT-3 ve aynı yük koşulunda yük kapalı → açık kararlı → kapalı gözlemi alınmalı.
4. Önceki üç kanallı logla karşılaştırma yapılırken aynı CT, aynı giriş, aynı yük ve aynı fiziksel koşullar korunmalı.
5. Tek kanal sürümünde de sıçrama görülürse ADC/ct_clamp okuma zinciri ayrıca incelenmeli.

## Sınırlar

Bu değişiklik tek başına kalite artışı veya ölçüm doğruluğu kanıtı değildir. Derleme, OTA ve yeni fiziksel test henüz yapılmadı. 30 A/V katsayısı kalibre edilmiş değildir. GPIO32 ve GPIO33 donanım bağlantıları kaldırılmamıştır; yalnızca yazılımda devre dışıdır.
