# Hesaplama-3 — Haberleşme, doğrulama ve kalibrasyon

## Doğrulama listesi

1. Modülün sürümünü ve kütüphane uyumunu doğrula.
2. UART 9600 8N1 ve TX/RX yönlerini kontrol et.
3. PZEM ölçümlerini sabit ve bilinen bir yükte kaydet.
4. Gerilim, akım ve aktif gücü uygun sınıfta bir referans ölçerle karşılaştır.
5. Farklı yük türlerinde PF ve aktif güç tutarlılığını incele.
6. Enerji sayacını uzun bir aralıkta referans enerji ölçümüyle karşılaştır.
7. Test tarihini, yükü, referans cihazı, firmware/kütüphane sürümünü ve hata payını kaydet.

## Hata yorumlama

- NaN/okuma hatası: çoğunlukla UART pinleri, besleme, cihaz sürümü, adres veya haberleşme sorunu olabilir; tek bir nedeni varsayma.
- Akım sıfır görünmesi: yük akımı ölçüm başlangıç seviyesinin altında olabilir, CT bağlantısı/uyumu veya modül revizyonu kontrol edilmelidir.
- V×I ile W uyuşmaması: güç faktörü ve yükün dalga şekli dikkate alınmalıdır.
- Enerji farkı: başlangıç değeri, zaman aralığı, ölçüm güncelleme sıklığı ve sayaç çözünürlüğünü kontrol et.

**Güvenlik:** Şebeke gerilimiyle testler tehlikelidir; enerjili devrede bağlantı değiştirme.