# SCT — ESP32 bağlantı pinleri

## 1. Envanterdeki ESP32

**ESP32-WROOM-32D** — BERO envanterindeki modül adı. Aşağıdaki GPIO numaraları, elimizdeki referans pin rehberinde esas alınan **ESP32-DevKitC V4 + ESP32-WROOM-32D geliştirme kartı** içindir. Çıplak WROOM modülünün fiziksel pin numaralarıyla karıştırma.

Referans: [DONANIM/ESP32-WROOM-32D/PIN.md](../../DONANIM/ESP32-WROOM-32D/PIN.md)

## 2. SCT013 analog sinyalini ESP32'nin dahili ADC'sine bağlama

SCT013-030 (30 A / 1 V) ve SCT013-100 (100 A / 1 V) gerilim çıkışlı modellerdir. Uygun analog ön uçtan gelen **biaslanmış ve güvenli aralığa ölçeklenmiş sinyal** ADC1 pinlerinden birine bağlanabilir.

| GPIO | ADC kanalı | Kullanım notu |
|---|---|---|
| GPIO36 (VP) | ADC1_CH0 | Analog giriş; yalnızca giriş |
| GPIO39 (VN) | ADC1_CH3 | Analog giriş; yalnızca giriş |
| GPIO34 | ADC1_CH6 | Analog giriş; yalnızca giriş |
| GPIO35 | ADC1_CH7 | Analog giriş; yalnızca giriş |
| GPIO32 | ADC1_CH4 | Analog giriş veya GPIO |
| GPIO33 | ADC1_CH5 | Analog giriş veya GPIO |

**Önerilen başlangıç:** GPIO34, GPIO35, GPIO36 veya GPIO39. Wi-Fi ile ADC okumada ADC1, ADC2'ye göre daha uygun seçimdir. GPIO34–39 pinlerinde dahili pull-up/pull-down yoktur.

## 3. MCP3208 kullanılıyorsa

SCT sinyali analog ön uç üzerinden MCP3208'in uygun analog girişine bağlanır. ESP32 pinleri bu durumda sensör analog girişini değil, MCP3208 ile SPI haberleşmesini taşır.

| ESP32-WROOM-32D GPIO | SPI sinyali | Yön |
|---|---|---|
| GPIO18 | SCLK | ESP32 → MCP3208 saat |
| GPIO23 | MOSI / DIN | ESP32 → MCP3208 komut |
| GPIO19 | MISO / DOUT | MCP3208 → ESP32 veri |
| GPIO5 | CS/SS | ESP32 → MCP3208 seçim |

Bu, klasik ESP32 DevKitC'de yaygın VSPI pin eşlemesidir; yazılımla değiştirilebilir. GPIO5 açılış yapılandırmasını etkileyen strapping pinidir. CS için başka uygun GPIO seçilecekse firmware ile fiziksel bağlantı birlikte değiştirilmelidir.

## 4. Bağlantıdan önce zorunlu kontroller

- **SCT013 çıkışını doğrudan GPIO'ya bağlama.** Negatif AC salınımı ESP32/ADC girişine uygulanmamalıdır; uygun bias ve koruma/ölçekleme devresi gerekir.
- GPIO'lara 5 V uygulama; ESP32 mantık seviyesi 3,3 V'tur.
- SCT013-030 ve SCT013-100, 1 V RMS çıkışlı modellerdir; SCT013-000 (100 A / 50 mA) ile aynı değildir. 1 V modellerinde dahili burden bulunur; rastgele ek burden direnci ekleme.
- 1 V RMS sinüsün tepesi yaklaşık 1,414 V'tur. Örneğin 1,67 V bias ile teorik üst tepe 3,084 V olur; 3,12 V VREF kullanan bir devrede pay çok azdır. Gerçek dalga biçimini ve ADC giriş sınırlarını ölçerek doğrula.
- MCP3208'in VDD/VREF/GND bağlantılarını kendi veri sayfasına göre kontrol et; VREF, VDD'yi aşmamalıdır.
- Önce sensör yerine bilinen güvenli bir DC/bias test sinyaliyle ADC'yi doğrula; sonra ham örnekleri ve zaman damgalarını kaydet. RMS/ampere geçişi bundan sonra yap.
- Bu pin listesi bir bağlantı planı başlangıcıdır; sensör ön ucu veya pin eşlemesi henüz fiziksel testle doğrulanmış sayılmaz.

## 5. İlgili BERO belgeleri

- [SCT013 kod ve hesaplama özeti](../SCT013/ÖZET.md)
- [Örnek Kod-1 — ESP32 dahili ADC](../SCT013/ORNEK-KOD-1/README.md)
- [Örnek Kod-2 — MCP3208 SPI](../SCT013/ORNEK-KOD-2/README.md)
- [SCT013-030 donanım rehberi](../../DONANIM/SCT013-30A-1V/README.md)
- [SCT013-100 donanım rehberi](../../DONANIM/SCT013-100A-1V/README.md)
- [Espressif ESP32-DevKitC V4 kılavuzu](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html)
