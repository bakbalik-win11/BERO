# SCT013 — Kod ve hesaplama araştırma özeti

## Amaç

Bu klasör SCT013-030 (30 A / 1 V) ve SCT013-100 (100 A / 1 V) sensörleri için farklı yazılım yaklaşımlarını karşılaştırır. Kodlar **öğrenme ve kontrollü test örnekleridir**; BERO'nun üretim firmware'i veya doğrulanmış kalibrasyonu değildir.

## Klasör haritası

- [Örnek Kod-1 — ESP32 dahili ADC ile ham örnekleme](ORNEK-KOD-1/README.md)
- [Örnek Kod-2 — MCP3208 SPI ile ham örnekleme](ORNEK-KOD-2/README.md)
- [Örnek Kod-3 — ESPHome ct_clamp yaklaşımı](ORNEK-KOD-3/README.md)
- [Akım Hesaplama yöntemleri](AKIM-HESAPLAMA/README.md)
- [Hesaplama-1 — Ham ADC örneklerinden RMS](AKIM-HESAPLAMA/HESAPLAMA-1.md)
- [Hesaplama-2 — Volt ve sensör oranından amper](AKIM-HESAPLAMA/HESAPLAMA-2.md)
- [Hesaplama-3 — EmonLib yaklaşımı](AKIM-HESAPLAMA/HESAPLAMA-3.md)

## İki sensörün nominal oranı

| Sensör | Nominal çıkış | Yaklaşık nominal ölçek |
|---|---:|---:|
| SCT013-030 | 30 A'da 1 V RMS | 33,33 mV/A |
| SCT013-100 | 100 A'da 1 V RMS | 10 mV/A |

Bu değerler sensörün nominal oranlarıdır. ADC kodundan ampere dönüşüm için ADC referansı/ölçeklemesi, analog devre, bias, örnekleme ve kalibrasyon da bilinmelidir. **SCT013-000 100 A / 50 mA farklı modeldir**; onun burden direnci örneklerini bu 1 V çıkışlı sensörlere doğrudan uygulamayın.

## Sensörden ne okuyoruz?

Akım trafosu, iletkenden geçen AC akımla orantılı küçük bir AC sinyal üretir. 1 V çıkışlı SCT013 modellerinde çıkış nominal akımda 1 V RMS'tir. Bu, ADC'nin doğrudan amper okuduğu anlamına gelmez.

ADC her örnekte dalga biçiminin o andaki gerilimine karşılık gelen sayısal bir ham değer (**raw count**) verir. Analog devrede sinyalin negatif kısmı çoğunlukla bir DC bias çevresine taşınır. Bu yüzden raw örnekler sıfırın etrafında değil, bir orta kod/gerilim çevresinde salınabilir. RMS hesabından önce bu merkez/bias kaldırılmalıdır.

## 1000 örnek ne demek?

- **N = 1000**, bir hesap penceresinde 1000 ADC ölçümü kullanıldığı anlamına gelir; saniyede 1000 örnek anlamına gelmez.
- Örnekleme hızı 1 kS/s ise 1000 örnek yaklaşık 1 saniye sürer. 10 kS/s ise yaklaşık 100 ms sürer.
- 50 Hz şebekede bir periyot 20 ms'dir. 1000 örnek, örnekleme hızına bağlı olarak farklı sayıda şebeke periyodu kapsar.
- Sabit örnek aralığı varsayımı, gerçek zamanlama düzensizse hatalı olabilir. Örnekler zaman damgalı kaydedilmeli; gerçek örnekleme aralığı ve pencere süresi ölçülmelidir.
- Örnek sayısı tek başına doğruluk garantisi değildir: analog kırpılma, bias, ADC referansı, gürültü, kanal geçişi ve örnekleme hızı önemlidir.

## RMS nedir?

RMS (Root Mean Square / karelerin ortalamasının karekökü), AC sinyalin eşdeğer ısıtma etkisini temsil eden etkin değeridir. Örneklenmiş, biası kaldırılmış gerilim için:

`V_{RMS}=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(V_i-\bar V)^2}`

Burada `V_i` örneğin volt cinsinden değeri, `\bar V` örnek penceresindeki ortalama/bias ve `N` örnek sayısıdır. İdeal sinüs için RMS = tepe / √2; bozuk dalga biçimlerinde RMS'i yalnızca tepe değerinden hesaplamak doğru değildir.

Akımı bulmak için sensörün gerçek kalibre edilmiş oranı kullanılır. Örneğin nominal oranla SCT013-030 için `I_RMS ≈ V_RMS × 30 A/V`; SCT013-100 için `I_RMS ≈ V_RMS × 100 A/V`. Gerilim, sensör çıkışındaki RMS gerilimidir; ADC pinindeki biaslı toplam gerilim değildir.

## İnternette bulunan yaklaşımların farkı

1. **Örneklerin RMS'i / doğrudan ADC:** Ham örneklerden DC merkezi çıkarılır, kareler ortalanır ve karekök alınır. ADC ve bias ölçeği doğru bilinmelidir.
2. **EmonLib:** Kayan offset filtresi ve kalibrasyon sabitiyle akım ölçer; örnek sayısı ile `calcIrms()` çağrılır. Örnek kodundaki kalibrasyon sabiti sensör/analog devreye özgüdür.
3. **ESPHome ct_clamp:** ADC kaynak sensörünün volt okumalarını örnekleyip akıma dönüştürür; `sample_duration` ve kalibrasyon filtresi kullanır.
4. **MCP3208 SPI:** Dahili ESP32 ADC'sinden farklı olarak harici ADC'nin SPI protokolü, CS zamanlaması, komut/yanıt bitleri ve kanal decode'u doğru olmalıdır. SPI hatası sayacının sıfır olması verinin doğru çözüldüğünü kanıtlamaz.

## BERO'ya özel geçmiş notları

- Önceki MCP3204/MCP3208 testlerinde sıfıra yakın veya tekrarlayan okumalar görüldü; sebep kesinleşmiş değildir.
- Benzer RX örüntülerinin ADC fiziksel olarak çıkarıldığında da görülmesi, sorunun yalnızca sensör kaynaklı varsayılmaması gerektiğini gösterir.
- Önce SPI ham TX/RX baytlarını, CS ve CLK davranışını, sabit ADC giriş testini doğrula; sonra sensör ve RMS hesabını ekle.
- 1,67 V bias ve 3,12 V VREF geçmiş testlerde konuşulmuş değerlerdir; her devrede yeniden ölçülmelidir. 1 V RMS sinüsün tepe değeri yaklaşık 1,414 V'tur; 1,67 V bias ile üst tepe yaklaşık 3,084 V olur ve 3,12 V VREF'e çok yaklaşır. Tolerans ve darbeler için pay azdır.
- Bir testte yalnızca bir değişkeni değiştir; sensör modeli, ADC modeli, VREF, bias, SPI ayarları, ham veri, örnekleme süresi ve referans akımını kaydet.

## Kaynaklardan

- ESPHome CT Clamp: https://esphome.io/components/sensor/ct_clamp/
- OpenEnergyMonitor — Arduino akım ölçümü: https://docs.openenergymonitor.org/electricity-monitoring/ct-sensors/how-to-build-an-arduino-energy-monitor-measuring-current-only.html
- OpenEnergyMonitor — EmonLib kalibrasyon teorisi: https://docs.openenergymonitor.org/electricity-monitoring/ctac/emonlib-calibration-theory.html
- EmonLib kaynak kodu: https://github.com/openenergymonitor/EmonLib
- Örnek ESP32/ADS1115 gerçek RMS projesi (başka donanım mimarisi; doğrudan BERO'ya kopyalanmamalı): https://github.com/abhradeepkayal/ESP32-True-RMS-Energy-Monitor

## Güvenlik ve durum

Bu örnekler şebeke ölçümü için sertifikalı cihaz değildir. Devreyi enerjisizken kur; uygun yalıtım ve korumayı kullan. Burada listelenen kodlar test edilip BERO donanımında doğrulanana kadar **örnek / doğrulanmadı** durumundadır.
