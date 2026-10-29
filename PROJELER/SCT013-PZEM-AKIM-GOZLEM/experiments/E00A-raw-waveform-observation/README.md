# E00A — Ham sinyal gözlemi ve örnekleme hızı

## Amaç
Paketleme veya sürekli veri aktarım mimarisine karar vermeden önce SCT girişindeki ham ADC sinyalini görmek, aynı kayıtları PC'de yavaş oynatmak ve farklı örnekleme hızlarında dalga biçimi ile temel istatistiklerin nasıl değiştiğini öğrenmek.

Bu bir laboratuvar doğrulama deneyi değildir. Amaç, “SCT'den neler geliyor?” sorusuna basit ve gözlemlenebilir bir cevap bulmaktır.

## Neden paketlemeden önce?
Önce sinyalin ne kadar örnekleme hızına ihtiyaç duyduğunu ve farklı hızlarda görünüm/istatistiklerin anlamlı biçimde değişip değişmediğini göreceğiz. Sonra basit aktarımın yeterli olup olmadığına karar veririz. Çift buffer, DMA veya daha karmaşık aktarım düzeni şimdiden şart koşulmaz.

## Aşamalar
1. **Bias-only:** SCT bağlı değilken ADC ham değerlerini kaydet.
2. **SCT yüksüz:** SCT bağlı, ölçülen hattan akım yokken kaydet.
3. **100 W akkor:** SCT bağlı ve ampul açıkken kaydet.
4. Her durumu mümkün olan birkaç örnekleme hızıyla karşılaştır; başlangıç adayları 1, 2 ve 2,5 kS/s'dir. Bunlar kesin gereksinim değil, karşılaştırma noktalarıdır.

## Her kayıttan üretilecek çıktılar
- PC'de ham ADC değeri-zaman grafiği.
- Kaydedilmiş veriyi yavaş oynatma, durdurma ve yakınlaştırma.
- Ortalama, minimum, maksimum, peak-to-peak ve standart sapma.
- Hedef örnekleme hızı, geçen kayıt süresi ve toplanan örnek sayısı.
- Mümkünse gerçekleşen örnekleme hızı; hedef değerle aynı olduğu varsayılmaz.

Akım (A), RMS akım, güç faktörü veya harmonik hesaplamak bu deneyin amacı değildir. İstatistikler ham ADC değerleri üzerinden tanımlayıcıdır; bunlar tek başına akım ölçümü değildir.

## Basit örnek sayısı kontrolü
Beklenen örnek sayısı yaklaşık olarak hedef hız × gerçek kayıt süresidir. Okunan sayıyla karşılaştırılır. İlk aşamada ayrıntılı kayıp analizi, her örneğe zaman damgası, DMA veya karmaşık buffer sistemi kurmak hedeflenmez. Sayı belirgin biçimde düşükse önce nedeni anlamaya çalışırız.

## Karar
Grafik ve temel istatistikler farklı hızlarda yeterince benzer ve veri toplama basitçe çalışıyorsa daha karmaşık aktarım mimarisi kurmayız. Hız farkı dalga/istatistikleri anlamlı değiştiriyorsa veya basit aktarım yetişmiyorsa sonraki adımı eldeki kayda göre seçeriz.

## Durum
PLANLANDI. Firmware, kayıt, grafik ve fiziksel ölçüm henüz yapılmadı.
