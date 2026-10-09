# ESP32-WROOM-32D — Resmî Kaynaklar

## 1. Modül veri sayfası (Datasheet)

- **Üretici:** Espressif Systems
- **Belge:** ESP32-WROOM-32D & ESP32-WROOM-32U Datasheet, Version 2.6
- **Resmî PDF:** https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf
- **Durum notu:** Veri sayfası modülü **NRND (Not Recommended for New Designs)** olarak işaretliyor. Mevcut kartı belgelemek için kullanılabilir; yeni tasarım kararı verilecekse ürünün güncel durumu ayrıca değerlendirilmelidir.

### Veri sayfasından temel bilgiler

- ESP32-WROOM-32D modülünde PCB anteni bulunur; 32U modelinde harici anten konnektörü vardır.
- Flash: 4 MB.
- Besleme/çalışma gerilimi: 3.0–3.6 V.
- Çalışma ortam sıcaklığı: −40 ila +85 °C.
- Wi-Fi: 802.11 b/g/n.
- Bluetooth: Bluetooth 4.2 BR/EDR ve Bluetooth LE.
- Modül pin açıklamaları, açılış/boot yapılandırması, elektriksel ve RF özellikleri, şemalar ve mekanik ölçüler PDF içinde yer alır.

## 2. Geliştirme kartı kılavuzu

- **Belge:** ESP32-DevKitC V4 User Guide
- **Resmî kılavuz:** https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html
- Kullanıcının işaret ettiği bölüm: [What You Need](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html#what-you-need)

**Önemli ayrım:** Bu sayfa, ESP32-DevKitC V4 geliştirme kartının kılavuzudur; tek başına ESP32-WROOM-32D modül veri sayfası değildir. Kılavuz, DevKitC V4'ün farklı modül varyantlarını listeler ve WROOM-32D için üreticinin ayrı modül veri sayfasına bağlantı verir. Kartın pin başlıkları/güç seçenekleri için kılavuzu, modülün teknik sınırları için modül veri sayfasını kullan.

### Güç uyarısı — geliştirme kartı

DevKitC V4 kılavuzuna göre kart üç alternatiften yalnızca biriyle beslenmelidir: Micro-USB, 5V-GND pinleri veya 3V3-GND pinleri. Aynı anda birden fazla besleme seçeneğini kullanmak karta veya güç kaynağına zarar verebilir. Bu uyarı geliştirme kartı içindir; kendi kartının şemasını ayrıca kontrol et.

## Kaynak kullanımı

Önce modülün üzerindeki işaretlemenin gerçekten **ESP32-WROOM-32D** olduğunu ve geliştirme kartının modelini doğrula. Modül ve geliştirme kartı farklı bileşenlerdir; pin/güç bilgilerini birbirine karıştırma.
