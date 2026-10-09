# ACS712 — Hall akım sensörü donanım arşivi

- [5 A varyantı](5A/README.md)
- [20 A varyantı](20A/README.md)

**ACS712**, Allegro'nun 5 V beslemeli, AC ve DC ölçebilen, analog ratiometrik çıkışlı Hall akım sensörüdür. **SCT013/ZMCT103C gibi CT değildir**; burden direnci gerekmez. Primer akım yolu ile sinyal elektroniği entegre içinde galvanik ayrılmıştır; modül kartının şebeke güvenliği ayrıca incelenmelidir.

| Model | Aralık | Tipik hassasiyet | 5 V'ta ideal 0 A çıkışı |
|---|---|---|---|
| ACS712ELCTR-05B | ±5 A | 185 mV/A | 2,5 V |
| ACS712ELCTR-20A | ±20 A | 100 mV/A | 2,5 V |

**İki varyantın hassasiyetini karıştırma.** Gerçek modül üzerindeki entegre işaretini doğrula.

## Ortak pinler — SOIC-8 entegre

1–2 IP+; 3–4 IP−; 5 GND; 6 FILTER; 7 VIOUT; 8 VCC. Modül kartındaki üçlü VCC/GND/OUT soketinin fiziksel sırasını bu entegre pin sırasından çıkarma.

## Ortak güvenlik

5 V beslenen sensörün VIOUT çıkışı 3,3 V ADC aralığını aşabilir. ESP32/MCP3208'e doğrudan bağlamadan önce **tam akım aralığını** kapsayan gerilim bölücü/buffer ve ADC sınırlarını doğrula. MCP3208 için VREF ≤ VDD. Giriş ve GND ölçümünü enerjisiz bağlantı sonrası doğrula. Primer yolun klemensleri, bakır izleri, ısınması ve izolasyonu modüle göre değişir. Şebekede yalnızca uygun güvenlik tasarımıyla kullan; 2,1/2,4 kV izolasyon test değeri tek başına modülün güvenli olduğunu göstermez.

## Üretici kaynakları

- [Allegro ACS712 ürün sayfası](https://www.allegromicro.com/en/products/sense/current-sensor-ics/integrated-current-sensors/acs712)
- [Allegro ACS712 datasheet (PDF)](https://www.allegromicro.com/-/media/Files/Datasheets/ACS712-Datasheet.ashx)
- [ESPHome ADC](https://esphome.io/components/sensor/adc/)
- [Microchip MCP3208](https://www.microchip.com/en-us/product/mcp3208)

**Not:** Datasheet revizyonlarında izolasyon ve bant genişliği rakamları değişebilir (ör. 2,1/2,4 kVRMS ve 50/80 kHz). Kullanılan parçanın datasheet revizyonunu ve modül filtresini esas al. Bu klasörlerin kodları test edilmiş BERO firmware'i değildir.
