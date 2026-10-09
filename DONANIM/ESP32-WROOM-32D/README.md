# ESP32-WROOM-32D — Resmî Kaynaklar

## 1. Modül veri sayfası (Datasheet)

- **Üretici:** Espressif Systems
- **Belge:** ESP32-WROOM-32D & ESP32-WROOM-32U Datasheet
- **Resmî HTML veri sayfası:** https://documentation.espressif.com/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.html
- **Resmî PDF:** https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf
- **Durum:** Veri sayfası NRND (Not Recommended for New Designs) uyarısı içeriyor.

## 2. Geliştirme kartı kılavuzu ve pinout görseli

- **Belge:** ESP32-DevKitC V4 User Guide
- **Resmî kılavuz:** https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html
- **What You Need:** https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html#what-you-need
- **Pin layout (pinout) görselinin bulunduğu bölüm:** https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html#pin-layout
- **Resmî PDF kılavuzu:** https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp-dev-kits-en-master-esp32.pdf

Kullanıcının gönderdiği görsel, ESP32-DevKitC pin yerleşimini ve GPIO işlevlerini gösterir. Bu görseli karşılaştırmak için üreticinin yukarıdaki **Pin Layout** bölümünü kullan. Bu belge geliştirme kartının pinout'udur; modülün kendi pin dizilimi için modül veri sayfasındaki “ESP32-WROOM-32D Pin Layout (Top View)” şekline bak.

## 3. Temel modül bilgileri

- ESP32-WROOM-32D: PCB antenli modül; ESP32-WROOM-32U harici anten konnektörlü varyanttır.
- Flash: 4 MB.
- Besleme gerilimi: 3.0–3.6 V.
- Çalışma ortam sıcaklığı: −40 ila +85 °C.
- Wi-Fi: 802.11 b/g/n; Bluetooth 4.2 BR/EDR ve Bluetooth LE.

## 4. Geliştirme kartı güç uyarısı

DevKitC V4 kılavuzuna göre kart üç alternatiften yalnızca biriyle beslenmelidir: Micro-USB, 5V-GND pinleri veya 3V3-GND pinleri. Birden fazla besleme seçeneğini aynı anda kullanmak karta veya güç kaynağına zarar verebilir. Bu uyarı geliştirme kartı içindir; farklı kartlarda şemayı ayrıca kontrol et.

## Kaynakları kullanırken

Modül ile geliştirme kartını birbirine karıştırma. GPIO/pin bağlantılarını uygulamadan önce elindeki kartın tam modelini ve kart revizyonunu doğrula.
