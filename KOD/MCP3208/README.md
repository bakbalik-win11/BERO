# MCP3208 — Kod, SPI denemeleri ve BERO test kaydı

## Amaç

Bu klasör MCP3208 için SPI okuma kodunu, protokol doğrulamasını ve BERO'ya özgü test geçmişini tutar. **Bu dosyalar doğrulanmış üretim kodu değildir.** Önce sabit giriş ve ham SPI baytlarıyla ADC haberleşmesi doğrulanmalıdır.

## Önemli adlandırma notu — BERO geçmişi

**Önceki BERO denemelerinde MCP3204 adıyla geçen ESPHome bileşeni/kod yapılandırması 8 kanal (CH0–CH7) okuma amacıyla kullanıldı.** Bu ayrıntı gelecekte hata ayıklarken kaybolmamalıdır.

- Yazılımda bileşen/entegrasyon adının `mcp3204` olması, fiziksel entegreyi tek başına kanıtlamaz.
- MCP3204 donanımı 4 tek uçlu kanallıdır; MCP3208 donanımı 8 tek uçlu kanallıdır.
- Önceki yapılandırmanın 8 kanal okuma hedefi ile gerçek entegre modeli ve kullanılan bileşenin sürüm/uygulama desteği ayrı ayrı doğrulanmalıdır.
- Bu nedenle eski kodu sadece adına bakıp MCP3204 donanımına ait diye sınıflandırma; aynı şekilde sekiz kanal konfigürasyonunun MCP3208 ile çalıştığını da donanım testi olmadan varsayma.
- Eski dosyalar ve loglar korunmalı; adlandırma ile gerçek parça arasında çelişki varsa bunu açıkça kaydet, sessizce düzeltme.

## BERO SPI test başlangıcı

Daha önce kullanılan yaygın ESP32-WROOM-32D / DevKitC pin eşlemesi:

| ESP32 GPIO | SPI sinyali | Yön |
|---|---|---|
| GPIO18 | SCLK | ESP32 → ADC saat |
| GPIO23 | MOSI / DIN | ESP32 → ADC komut |
| GPIO19 | MISO / DOUT | ADC → ESP32 veri |
| GPIO5 | CS | ESP32 → ADC seçim |

Geçmişte bir test taslağında SPI MODE0, 500 kHz, MSB-first, üç baytlık transfer ve aşağıdaki decode adayı kullanıldı:

```cpp
uint16_t value = ((rx[1] & 0x0F) << 8) | rx[2];
```

Bunlar geçmişte denenmiş/önerilmiş test parametreleridir; tek başına protokolün doğru olduğunu veya ölçümün doğrulandığını göstermez. MCP3208'in komut/yanıt hizalaması, CS'nin aktif kaldığı çerçeve ve saat kenarları üretici veri sayfasıyla karşılaştırılmalı; ilk testlerde TX ve RX baytları ham biçimde kaydedilmelidir.

## Bilinen test gözlemleri ve çözülmemişler

- ESPHome düğümü açılıp çalışırken MCP3208 CH0 gerilimi tekrarlayan biçimde **0.000 V** raporlandı.
- Bir test notunda VREF yaklaşık 3,35 V, CH0 test biası yaklaşık 1,60–1,72 V olarak kontrol edilmesi önerildi; bunlar doğrulanmış güncel ölçüm değil, geçmiş test hedefleridir. Yeniden ölç.
- Daha sonraki incelemede benzer RX örüntülerinin ADC fiziksel olarak çıkarılmışken de görüldüğü kaydedildi. Bu nedenle sorun yalnızca analog sensör veya ADC çipine bağlanamaz.
- `SPI_ERROR_COUNT=0` olması, SPI'den alınan baytların doğru olduğu veya kanalın doğru çözüldüğü anlamına gelmez.
- Kesin kök neden henüz doğrulanmış değildir. Kablo/pin eşlemesi, entegre yönü, besleme ve referans, CS/CLK/DIN/DOUT dalga biçimleri, transfer çerçevesi ve yazılım decode'u ayrı ayrı incelenmelidir.

## Test protokolü

Her denemede aşağıdakileri birlikte kaydet:

1. Entegrenin üzerindeki tam işaretleme ve paket/pin sayısı.
2. ESPHome/Arduino/ESP-IDF sürümü, kullanılan bileşen adı ve sürümü.
3. Fiziksel bağlantı: SCLK, MOSI/DIN, MISO/DOUT, CS, VDD, VREF, AGND, DGND.
4. Ölçülen VDD, VREF ve test giriş gerilimi.
5. SPI modu, frekansı, bit sırası ve transfer sırasında CS davranışı.
6. Kanal numarası, TX baytları, RX baytları, decode edilen raw değer (0–4095) ve hesaplanan gerilim.
7. Zaman damgaları ve gerçek örnek aralığı.
8. Beklenen değer, gözlenen değer ve bu denemeden çıkarılabilecek sonuç.

Önce sensör olmadan sabit bir DC girişle CH0, ardından tüm kanallar tek tek doğrulanmalı. Ancak bu aşamalar başarılı olduktan sonra SCT013, örnekleme penceresi ve RMS hesabına geç.

## İlgili dosyalar

- [MCP3208 donanım ve üretici referansı](../../DONANIM/MCP3208/README.md)
- [Eski SCT013 MCP3208 örnek kod notu](../SCT013/ORNEK-KOD-2/README.md)
- [SCT013 araştırma özeti ve BERO geçmişi](../SCT013/ÖZET.md)

## Üretici kaynakları

- [Microchip MCP3208](https://www.microchip.com/en-us/product/MCP3208)
- [Microchip MCP3204](https://www.microchip.com/en-us/product/MCP3204)
- [MCP3204/3208 DS21298 veri sayfası](https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf)

**Durum:** Araştırma ve test kaydı. Kodun donanım üzerinde doğru sonuç verdiği henüz kanıtlanmış değildir.
