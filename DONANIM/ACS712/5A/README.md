# ACS712 5 A — donanım

## Model ve üretici verileri

| Özellik | Değer |
|---|---|
| Üretici | Allegro MicroSystems |
| Tam varyant | ACS712ELCTR-05B (paket/sonek ayrıca doğrulanmalı) |
| Ölçüm | AC ve DC; çift yönlü |
| Optimize aralık | ±5 A |
| Tipik duyarlılık (5 V, 25 °C) | 185 mV/A |
| Nominal besleme | 5,0 V (çalışma aralığı veri sayfasına göre) |
| Sıfır akım çıkışı | yaklaşık VCC/2 (5 V için 2,5 V) |
| Primer direnç | tipik 1,2 mΩ |
| Çıkış | VIOUT, analog ratiometrik |
| Filtre | FILTER pinine bağlı kondansatör; bant genişliği ve gürültüyü etkiler |
| Sıcaklık ve hata | ofset, hassasiyet, sıcaklık ve datasheet revizyonuna bağlı |

## Nominal çıkış hesabı

VIOUT ≈ V0 + I × 0.185 V/A.

5 V besleme ve ideal V0=2,5 V için:
- 0 A → 2,5 V.
- +5 A → 3.425 V.
- −5 A → 1.575 V.

Bu **ideal tipik** hesaptır, garanti edilen mutlak çıkış aralığı değildir. Gerçek sıfır akım ofseti ve eğim kalibre edilir.

## Entegre pinleri

| Pin | Görev |
|---|---|
| 1,2 | IP+ (primer akım girişi) |
| 3,4 | IP− (primer akım çıkışı) |
| 5 | GND |
| 6 | FILTER |
| 7 | VIOUT |
| 8 | VCC |

Kart üzerindeki klemens/OUT/VCC/GND pin dizilimi üretici entegre pinlerinden farklı olabilir. Multimetre ve kart işaretleriyle doğrula.

## BERO ESP32 + MCP3208 bağlantı notu

- ACS712 nominal 5 V ile çalışır; **3,3 V ile doğru çalışacağını varsayma**.
- VIOUT çıkışı ESP32 3,3 V giriş sınırını ve 3,12 V MCP3208 VREF'ini aşabilir. +5 A için yaklaşık 3,425 V bile 3,12 V'u aşar. Doğrudan bağlama.
- Örnek olarak 10 kΩ üst / 20 kΩ alt bölücü yaklaşık 2/3 oran verir. 3,425 V → yaklaşık 2,283 V. Bu **yalnızca hesap örneği**; tolerans, ani aşırı akım, kaynak empedansı, ADC örnekleme yükü, koruma ve filtre tasarımını doğrulamadan üretime alma.
- Ratiometrik sensörde VCC dalgalanması V0 ve duyarlılığı etkiler; VCC ve ADC VREF'i ayrıysa kalibrasyonda bunu göz önüne al.
- FILTER pinindeki kondansatör ve modülün ek RC filtresi gerçek bant genişliğini belirler. 50 Hz RMS için anti-alias ve yeterli örnekleme gerekir.

## İlk test

1. Modülün entegre üzerindeki 05B kodunu doğrula.
2. Primer akım yokken VCC, GND ve VIOUT'u ölç; gerçek V0'ı kaydet.
3. ADC'ye bağlamadan önce maksimum/minimum çıkışı ve bölücüyü hesapla.
4. Güvenli, bilinen düşük DC akımla çıkış yönünü ve hassasiyeti ölç.
5. AC testinde dalga biçimi, zaman damgası, RMS ve referans ampermetre karşılaştırmasını kaydet.
6. Birden çok akım noktasında kalibrasyon yap.

## Kaynaklar

- [Allegro ACS712 üretici ürün sayfası](https://www.allegromicro.com/en/products/sense/current-sensor-ics/integrated-current-sensors/acs712)
- [ACS712 datasheet PDF](https://www.allegromicro.com/-/media/Files/Datasheets/ACS712-Datasheet.ashx)
- [MCP3208 datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf)

**Durum:** Üretici verileriyle hazırlanmış tasarım/test notu. Fiziksel BERO modülü ve analog ön uç doğrulanmadı.
