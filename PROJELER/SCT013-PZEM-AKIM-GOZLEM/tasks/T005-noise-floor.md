# T005 — E01 gürültü tabanı

- **Durum:** PLANLANDI
- **Faz:** 1.2
- **Bağımlılık:** T004
- **Hedef:** Hatta akım yokken ADC ofsetini, gürültü tabanını ve zaman içindeki değişimi ölçüp grafiklemek.

## Mevcut durum
- Donanım henüz kurulmadı; fiziksel deney ve ölçüm yapılmadı.
- PZEM ve diğer ESP kartları ölçülen hattan beslenmiyor; bağımsız besleme düzeni deney kaydında korunacak.
- 30 saniye yalnızca asgari başlangıç süresidir, üst sınır değildir. Daha uzun, hatta saatler süren kayıt düşünülebilir; kesin süre henüz belirlenmedi.

## Yapılacak
1. experiments/E01-noise-floor/protocol.md içindeki düzenek ve örnekleme ayarlarını kurulan gerçek donanıma göre kesinleştir.
2. Donanım kurulduktan sonra bağlantı/güvenlik kontrolünü yap ve hatta akım olmadığını deney kaydına geçir.
3. Sabit ayarlarda ADC verisi al; ham veriyi sakla ve zaman ekseninde grafikle.
4. sample_count, ortalama, min/max ve ofset giderilmiş gürültü RMS değerini hesapla.
5. metadata.yaml içinde gerçek firmware/donanım kimliklerini, besleme düzenini, örnekleme ayarlarını ve gerçek süreyi yaz.
6. results.md içinde grafiklere ve ham veriye bağlantı ver. Ölçüm yapılana kadar sonuç üretme.
7. Gürültü tabanından çıkarılabilecek düşük akım sınırını hipotez olarak ayır; tek deneyle genelleme yapma.

## Kabul ölçütü
Protokol, metadata, ham veri, grafik ve sonuç birbiriyle bağlanabilir; ölçülmeyen sonuç yoktur. Deney yapılmadığı sürece sonuç durumu açıkça YAPILMADI olarak kalır.

## Çıktı / dokunulacak dosyalar
- experiments/E01-noise-floor/
- İlgili veri ve doğrulama kayıtları

## 2026-10-29 kaynak raporu notu

SCT013-030 raporu nominal oranı 30 A/V olarak verir. Bu değer T005/E01 yüksüz gürültü ölçümünün sonucu veya yerine geçmez. [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md) uyarınca ölçümden önce orta noktadaki mevcut 100 nF'nin 10 µF ile değiştirilmesi önerilmiştir. Fiziksel değişikliği uygula ve metadata'ya fiilî değeri yaz; değişiklik uygulanmadıysa sonucu bu karar uygulanmış gibi raporlama. ADC pinine ayrıca 100 nF ekleme bu ilk deneyin kapsamına dahil değildir.
