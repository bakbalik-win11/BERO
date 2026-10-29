# T005 — ADC temel okumaları ve E01 gürültü tabanı

- **Durum:** PLANLANDI
- **Faz:** 1.2
- **Bağımlılık:** T004
- **Hedef:** Hatta akım yokken ADC ofsetini, gürültü tabanını ve zaman içindeki değişimi ölçüp grafiklemek.

## Mevcut durum
- Donanım henüz kurulmadı; fiziksel deney ve ölçüm yapılmadı.
- PZEM ve diğer ESP kartları ölçülen hattan beslenmiyor; bağımsız besleme düzeni deney kaydında korunacak.
- 30 saniye yalnızca asgari başlangıç süresidir, üst sınır değildir. Daha uzun, hatta saatler süren kayıt düşünülebilir; kesin süre henüz belirlenmedi.

## Sıralama — SCT bağlamadan başlayarak
1. **İlk test: E00 — bias-only ADC okuması.** SCT bağlı değilken bias noktasını ADC GPIO'suna bağla; aynı döngüde `analogRead()` ham sayısını ve `analogReadMilliVolts()` sonucunu yazdır. Voltmetre okumasıyla karşılaştır. Protokol: [E00](../experiments/E00-bias-adc-baseline/protocol.md).
2. **İkinci test: SCT bağlı, akım yok.** E00 çalıştıktan sonra SCT'yi bias/ADC düzenine bağla; ölçülen hatta akım yokken iki API'nin sonuçlarını tekrar kaydet. Bu, E01 gürültü tabanının başlangıç koşuludur.
3. **Sonraki aşama: uzun yüksüz kayıt ve analiz.** [E01 protokolü](../experiments/E01-noise-floor/protocol.md) içindeki 30 saniye veya daha uzun zaman serisi, grafik, ortalama, min/max ve ofset çıkarılmış gürültü RMS analizi bu iki temel karşılaştırmadan sonra yapılacak.
4. Her aşamada gerçek kart modeli, ADC GPIO, attenuation ayarı, besleme ve fiilî kondansatör düzenini kaydet.
5. Ölçülmeyen sonuç üretme; düşük akım sınırını hipotez olarak ayır ve tek deneyle genelleme yapma.

## Kabul ölçütü
Protokol, metadata, ham veri, grafik ve sonuç birbiriyle bağlanabilir; ölçülmeyen sonuç yoktur. Deney yapılmadığı sürece sonuç durumu açıkça YAPILMADI olarak kalır.

## Çıktı / dokunulacak dosyalar
- experiments/E01-noise-floor/
- İlgili veri ve doğrulama kayıtları

## 2026-10-29 kaynak raporu notu

SCT013-030 raporu nominal oranı 30 A/V olarak verir. Bu değer T005/E01 yüksüz gürültü ölçümünün sonucu veya yerine geçmez. [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md) uyarınca ölçümden önce orta noktadaki mevcut 100 nF'ye paralel 10 µF elektrolitik kondansatör eklenmesi önerilmiştir. Paralel 10 µF kondansatörü fiziksel olarak ekle ve metadata'ya fiilî düzeni yaz; değişiklik uygulanmadıysa sonucu bu karar uygulanmış gibi raporlama. ADC pinine ayrıca 100 nF ekleme bu ilk deneyin kapsamına dahil değildir.
