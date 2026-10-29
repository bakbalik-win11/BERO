# ADR-007: Bias orta noktası kondansatörü

- **Durum:** E01 öncesi öneri kabul edildi; fiziksel değişiklik ve ölçüm henüz yapılmadı.
- **Tarih:** 2026-10-29
- **Kapsam:** 2 × 10 kΩ bölücüyle yaklaşık 1,65 V bias üreten ve SCT013-030 sinyalinin bu bias çevresinde ESP32 dahili ADC'sine uygulanacağı tarif edilen devre.

## Karar

- Bias orta noktası ile GND arasına **10 µF elektrolitik kondansatör, mevcut 104 (100 nF) seramikle paralel** bağlanmasını öneriyoruz. Elektrolitik kullanılırsa pozitif uç Vmid'e, negatif uç GND'ye bağlanır. Gerilim değeri bu düşük bias seviyesini güvenli biçimde karşılamalı; 6,3 V veya üzeri sınıf uygundur.
- Mevcut 104 kodlu 100 nF kondansatör yerinde kalır. E01 ölçüm düzeneği kurulurken 10 µF kondansatör aynı Vmid ve GND noktalarına eklenerek paralel bağlanır. Böylece orta noktada her iki kondansatör bulunur.
- 104 (100 nF), bias orta noktası ile GND arasında 10 µF ile paralel kalacaktır. ADC pinine ayrıca bir 100 nF bağlamak ayrı ve **opsiyonel** bir yüksek frekans/ADC gürültü azaltma seçeneğidir. GPIO henüz seçilmediği ve bu kondansatör ölçüm bant genişliğini etkileyebileceği için otomatik olarak eklenmeyecek; ilk ölçümlerden ve gerçek bağlantı planından sonra değerlendirilecektir.
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

## İki kondansatörün paralel kullanım gerekçesi

- **10 µF elektrolitik:** 50 Hz'de yaklaşık 318 Ω kapasitif reaktansla bias orta noktasına düşük empedanslı bir AC dönüş yolu sağlar. Bu, sanal referansın AC açısından daha kararlı olmasına yardımcı olur; ideal sıfır empedans veya hiç dalgalanmama garantisi değildir.
- **104 / 100 nF seramik:** 50 Hz'de yaklaşık 31,8 kΩ reaktans gösterir; bu nedenle 50 Hz için 10 µF'nin yerini tutmaz. Daha yüksek frekanslarda empedansı düşerek, fiziksel yerleşim ve parazit dönüş yolu uygunsa, elektrolitik kondansatöre tamamlayıcı bypass sağlayabilir.
- Wi-Fi/Bluetooth veya röle kaynaklı parazitin tümünü ortadan kaldırdığı iddia edilmez. Etki; parazitin kuplaj yoluna, kondansatörlerin ve GND yolunun fiziksel yerleşimine ve ADC örnekleme düzenine bağlıdır.

## Bağlantı topolojisi

```text
3V3
 |
 R1 10 kΩ
 |
 +------ Vmid ≈ 1.65 V ------ SCT013 çıkış ucu A
 |          |        |
 R2 10 kΩ  +|       104 / 100 nF
 |         10 µF     |
 |          |        |
 +----------+--------+------ GND

SCT013 çıkış ucu B ---------------- ESP32 ADC pini
```

Bu şema, 10 µF ve 104'ün **aynı Vmid–GND düğümlerine paralel** bağlanmasını gösterir. SCT'nin ikinci çıkış ucu ADC girişine gider; bu bağlantı gerçek kartın pin planı doğrulandıktan sonra yapılmalıdır. GPIO34 yalnızca klasik ESP32 ailesindeki uygun kartlarda kullanılabilir; ESP32-C3'te GPIO34 bulunmaz. BERO için ADC GPIO seçimi bu ADR ile kesinleştirilmiş değildir.

## 100 nF ADC giriş kondansatörü hakkında

Espressif ESP-IDF ADC kılavuzu, kullanım senaryosuna bağlı olarak ADC giriş pad'ine 100 nF bypass kondansatörü eklenebileceğini ve çoklu örneklemenin de gürültüyü azaltmaya yardımcı olabileceğini belirtir. Bu, bütün devrelerde zorunlu olduğu veya gürültüyü sıfırladığı anlamına gelmez. Kondansatörün ADC düğümündeki kaynak empedansıyla oluşturduğu RC filtresi, BERO'nun 2 kS/s edinim hedefiyle birlikte düşünülmelidir.

## E01 öncesi uygulanacaklar

1. Enerji bağlantıları yapılmadan önce mevcut breadboard düzeninde 104 kondansatörün gerçekten bias orta noktasından GND'ye bağlı olduğunu doğrula.
2. Mevcut 104 kondansatörü çıkarmadan, aynı Vmid ve GND noktalarına 10 µF elektrolitik kondansatör ekle. Elektrolitiğin pozitif ucunu Vmid'e, negatif ucunu GND'ye bağla.
3. ADC pinine ilave 100 nF eklemeyi bu ilk değişiklikle aynı anda yapma; önce düzenek ve ölçüm yapılandırmasını sabit tut.
4. Fiziksel kurulumda kullanılan kondansatör değerini E01 metadata'sına kaydet.
5. E01 yüksüz ADC verisini zaman grafiğinde incele. Kondansatör değişikliğiyle gürültünün mutlaka azalacağı varsayılmayacak; sonuç veriden değerlendirilecek.

## Kaynaklar

- OpenEnergyMonitor, “CT Sensors — Interfacing with an Arduino”: https://docs.openenergymonitor.org/electricity-monitoring/ct-sensors/interface-with-arduino.html
- Espressif, “ESP-IDF Programming Guide — ADC / Minimizing Noise”: https://docs.espressif.com/projects/esp-idf/en/v4.4.8/esp32/api-reference/peripherals/adc.html
- BERO'nun mevcut bağlantı kaydı: [hardware/frontend.md](../../hardware/frontend.md)
