# GRV-005-02 — ADC özelliklerinin kesin tanımları

- Tarih: 2026-10-11
- Durum: Tanım/karar aşaması; kodlama başlamadı.
- Ön koşul: GRV-005-01, mevcut prototipte PZEM güncelleme işareti davranışını gözlemleme hedefiyle kapatıldı.
- Amaç: 1000 örneklik her kanal penceresinden üretilecek istatistikleri matematiksel olarak tanımlamak; ham ADC RMS ile bias/offset çıkarılmış AC RMS'i birbirine karıştırmamak.
- Kapsam: CH0, CH1, CH2 ve BIAS; kanal başına 1000 örnek kararı korunur.
- Kapsam dışı: YAML uygulaması, nihai CSV kolon sırası ve PZEM zaman farkı kabul eşiği. Bunlar tanımlar sabitlendikten sonra ayrı adımlarda ele alınır.

## Karara bağlanacak tanımlar

1. **ADC ortalaması (mean):** 1000 geçerli ham ADC kodunun aritmetik ortalaması; geçersiz örneklerin dahil edilip edilmeyeceği kalite kuralıyla birlikte belirlenecek.
2. **ADC standart sapması (adc_std):** Örnek standart sapması mı ( N−1 ) yoksa popülasyon standart sapması mı ( N ) kullanılacak? Tek bir tanım seçilip veri sözlüğüne yazılacak.
3. **Median ve yüzdelikler:** Hangi yüzdeliklerin tutulacağı ve bunların gürültü/aykırı değer analizi için neyi ifade ettiği belirlenecek.
4. **adc_rms:** İki farklı nicelik açıkça ayrılacak:
   - Ham kod RMS: ADC kodlarının sıfıra göre RMS'i; bias çevresinde salınan AC sinyalinin akım karşılığı değildir.
   - Bias/offset çıkarılmış RMS: uygun merkez değeri çıkarıldıktan sonra kalan AC bileşenin RMS'i; ADC kodu veya volt cinsinden tanımlanmalı, akıma dönüşüm katsayısı ayrı kalibrasyon gerektirir.
5. **Bias kullanımı:** BIAS kanalının her ölçüm penceresindeki merkez/offset tahminine nasıl katkı vereceği; kanalın kendisinin de 1000 örneklik istatistiklerinin saklanacağı.
6. **zero_count:** Tam olarak hangi değerin “sıfır” sayıldığı. ADC kodu 0 mı, bias çıkarıldıktan sonra sıfır mı, yoksa tolerans bandı mı? Tanımlanmadan sayaç uygulanmayacak.
7. **invalid_count:** Örnekleme hatası, aralık dışı kod veya eksik örnek için hangi durumların geçersiz sayılacağı; sayaç kapsamı ve paydası.
8. **Örnek sayısı/kalite:** İstenen 1000 örneğin tamamı geçerli değilse pencerenin reddedilip reddedilmeyeceği veya geçerli örnek sayısıyla işaretlenip tutulacağı.

## Çıktı

Bu alt görev tamamlandığında her özelliğin adı, formülü, birimi, örnek sayısı, bias işlemi ve geçersiz örnek politikası bir veri sözlüğünde kilitlenecek. Ardından GRV-005-03 zaman hizalaması ve GRV-005-04 CSV şeması hazırlanabilir.

## Koruma kuralı

GRV-002, GRV-004, ALT09, ALT10 ve GRV-005-01 sürümleri değiştirilmez. GRV-005-02 için yeni karar kaydı oluşturulur; kod, kararlar netleşmeden ve derleme doğrulaması olmadan KOD klasörüne taşınmaz.
