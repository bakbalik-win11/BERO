# ADR-007: Bias orta noktası kondansatörü

- **Durum:** E01 öncesi öneri kabul edildi; fiziksel değişiklik ve ölçüm henüz yapılmadı.
- **Tarih:** 2026-10-29
- **Kapsam:** 2 × 10 kΩ bölücüyle yaklaşık 1,65 V bias üreten ve SCT013-030 sinyalinin bu bias çevresinde ESP32 dahili ADC'sine uygulanacağı tarif edilen devre.

## Karar

- Bias orta noktası ile GND arasındaki ana bypass kondansatörü için **10 µF** kullanılmasını öneriyoruz. Polarize elektrolitik kullanılırsa pozitif uç Vmid'e, negatif uç GND'ye bağlanır. Gerilim değeri bu düşük bias seviyesini güvenli biçimde karşılamalı; pratikte en az 6,3 V sınıfı uygundur.
- Mevcut 104 kodlu 100 nF kondansatör tek başına 50 Hz bias kararlılığı için 10 µF ile eşdeğer değildir. Bu nedenle E01 ölçüm düzeneği kurulurken orta noktadaki 100 nF'nin yerine 10 µF takılması planlanır.
- 100 nF'nin ADC pinine GND'ye bağlanması ayrı ve **opsiyonel** bir yüksek frekans/ADC gürültü azaltma seçeneğidir. GPIO henüz seçilmediği ve bu kondansatör ölçüm bant genişliğini etkileyebileceği için otomatik olarak eklenmeyecek; ilk ölçümlerden ve gerçek bağlantı planından sonra değerlendirilecektir.
- Bu, ölçülmüş performans sonucu değildir. E01 öncesi fiziksel uygulama ve ardından kayıt alınması beklenmektedir.

## Hesap ve gerekçe

50 Hz sinyal için ideal kapasitif reaktans:

\[
X_C = \frac{1}{2\pi f C}
\]

| Kondansatör | 50 Hz'de yaklaşık reaktans |
|---|---:|
| 10 nF | 318 kΩ |
| 100 nF (104) | 31,8 kΩ |
| 10 µF | 318 Ω |

Eşit 10 kΩ dirençli bölücünün bias noktasından görülen Thevenin direnci yaklaşık 5 kΩ'dur. 100 nF kondansatörün 50 Hz'deki reaktansı bu değerden çok daha büyük olduğu için orta noktayı AC açısından güçlü biçimde sabitlemez. 10 µF'nin yaklaşık 318 Ω reaktansı ise 5 kΩ'dan belirgin biçimde küçüktür ve 50 Hz bileşenine daha düşük empedanslı dönüş yolu sağlar.

Bu hesaplar ideal bileşenler içindir; gerçek devrede kablo, SCT çıkışı, besleme, bağlantı topolojisi ve ADC girişi de sonucu etkiler. “Sıfır empedans”, “sanal toprak hiç oynamaz” veya “gürültü tamamen sıfırlanır” denmemelidir.

## 100 nF ADC giriş kondansatörü hakkında

Espressif ESP-IDF ADC kılavuzu, kullanım senaryosuna bağlı olarak ADC giriş pad'ine 100 nF bypass kondansatörü eklenebileceğini ve çoklu örneklemenin de gürültüyü azaltmaya yardımcı olabileceğini belirtir. Bu, bütün devrelerde zorunlu olduğu veya gürültüyü sıfırladığı anlamına gelmez. Kondansatörün ADC düğümündeki kaynak empedansıyla oluşturduğu RC filtresi, BERO'nun 2 kS/s edinim hedefiyle birlikte düşünülmelidir.

## E01 öncesi uygulanacaklar

1. Enerji bağlantıları yapılmadan önce mevcut breadboard düzeninde 104 kondansatörün gerçekten bias orta noktasından GND'ye bağlı olduğunu doğrula.
2. Bu kondansatörü 10 µF ile değiştir; polariteyi kontrol et.
3. ADC pinine ilave 100 nF eklemeyi bu ilk değişiklikle aynı anda yapma; önce düzenek ve ölçüm yapılandırmasını sabit tut.
4. Fiziksel kurulumda kullanılan kondansatör değerini E01 metadata'sına kaydet.
5. E01 yüksüz ADC verisini zaman grafiğinde incele. Kondansatör değişikliğiyle gürültünün mutlaka azalacağı varsayılmayacak; sonuç veriden değerlendirilecek.

## Kaynaklar

- OpenEnergyMonitor, “CT Sensors — Interfacing with an Arduino”: https://docs.openenergymonitor.org/electricity-monitoring/ct-sensors/interface-with-arduino.html
- Espressif, “ESP-IDF Programming Guide — ADC / Minimizing Noise”: https://docs.espressif.com/projects/esp-idf/en/v4.4.8/esp32/api-reference/peripherals/adc.html
- BERO'nun mevcut bağlantı kaydı: [hardware/frontend.md](../../hardware/frontend.md)
