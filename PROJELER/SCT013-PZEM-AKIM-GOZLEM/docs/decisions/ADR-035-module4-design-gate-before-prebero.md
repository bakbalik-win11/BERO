# ADR-035 — Modül 4 tasarım kapısı ve PREBERO ön koşulu

- **Tarih:** 2026-11-20
- **Durum:** KABUL EDİLDİ — çalışma mimarisi
- **Karar sahibi:** Kullanıcı

## Karar

PREBERO Modül 5, Modül 6 ve Modül 7 imalatına geçmeden önce Modül 4'ün teknik yapısı kararlaştırılacak ve Modül 4 imal edilecektir. Mevcut masaüstü ESP32D2 + ADS1115 + SCT düzeneği deney/öğrenme düzeneğidir; henüz imal edilmiş nihai Modül 4 sayılmaz.

Modül 4, PREBERO'da kullanılacak akım ölçüm yaklaşımının referans tasarımını oluşturacaktır. Bu nedenle Modül 4'ün tasarımı, teknik inceleme ve gerçek sinyal gözlemi tamamlanmadan dondurulmayacaktır.

## Kabul edilen çalışma sırası

1. **ADS1115 hobi düzeyinde donanım raporu:** Entegrenin ne olduğu ve nasıl ölçüm yaptığı; 16 bit çözünürlük, diferansiyel/single-ended giriş, PGA, örnekleme hızları, besleme ve giriş gerilimi sınırları. Yalnız BERO'daki SCT kullanımını anlamak için gereken ayrıntı; gereksiz laboratuvar karakterizasyonu yok.
2. **Mevcut masaüstü düzeneğini anlama:** Gerçek bağlantılar, SCT çıkışı/ön uç, ADS1115 beslemesi, AIN pinleri ve mevcut yazılım ayarları. Bilinmeyen bağlantılar varsayılmayacak.
3. **Biaslı/bias'sız karşılaştırma:** Aynı ölçüm zinciri ve mümkün olduğunca aynı yük/koşullarla iki yapının gözlemlenmesi. Ölçüm logları ve koşullar kaydedilecek.
4. **Osiloskopla gözlem:** Düşük gerilimli ve uygun şekilde izole edilmiş ölçüm tarafında AIN0-GND, AIN1-GND ve AIN0-AIN1 davranışının incelenmesi. Bias'sız ve bias'lı gözlemler, osiloskop ayarları ve ekran görüntüleri saklanacak.
5. **Modül 4 mimari kararı:** SCT/ADS1115 giriş yapısı, bias gerekliliği, besleme yaklaşımı, ESP32 bağlantısı, kablolama, konektörler ve fiziksel yerleşim için yeterli kararların verilmesi. Kanıtlanmamış hususlar açık bırakılacak.
6. **Modül 4 imalatı:** Kararlaştırılmış yapının masaüstü geçici düzeneğinden bağımsız, sabit ve tekrarlanabilir bir modül olarak kurulması. Bağlantı ve imalat kayıtları tutulacak; gerçek donanım testi yapılmadan çalışır kabul edilmeyecek.
7. **PREBERO'ya geçiş:** Modül 4'ün kabul kontrolleri tamamlandıktan sonra Modül 5 (çamaşır), Modül 6 (bulaşık) ve Modül 7 (ana hat + PZEM) imalat/kurulum çalışmalarına başlanacak.

## Bias kararı ve PREBERO besleme seçimi

Bias gerekliliği henüz karara bağlanmamıştır. Bias gerekiyorsa PREBERO Modül 5/6/7'de bias üretme yöntemi ayrıca değerlendirilecektir:
- ESP'nin uygun beslemesinden bias üretmek.
- Modül 1'in bias trafosu/güç kutusu yapısının ikizlerini üretmek.

Bu seçenekler Modül 4 deneyleri ve tasarım kararı öncesinde seçilmiş sayılmaz. Modül 1 mevcut fiziksel referans düzeneğidir; korunur.

## Hobi düzeyinde kapsam

- Amaç ADS1115 uzmanlığı veya laboratuvar seviyesinde karakterizasyon değildir.
- Veri sayfasından BERO kullanımını etkileyen temel özellikler ve sınırlar öğrenilir.
- Osiloskop, sinyalin gerçek davranışını görüp tasarım kararı verecek kadar kullanılır.
- İleri hata bütçesi, üretim kalite güvence prosedürü veya gereksiz ayrıntılı ADC karakterizasyonu bu aşamanın hedefi değildir.
- Güvenlik ve üretici tarafından belirtilen elektriksel sınırlar ise hobi projesi gerekçesiyle atlanmaz.

## Kanıt ve tamamlanma

Her aşama HEDEF / UYGULAMA / LOG / YORUM / SONUÇ biçiminde kaydedilir. Başarılı kod, gerçek cihaz çıktısı ve teknik yorum birlikte saklanır. Osiloskop görüntüsü varsa ayarlarıyla birlikte eklenir. Tasarım kararı ölçüm ve gözlemlere dayandırılır.

Bu ADR bir çalışma sırası kararıdır; ADS1115 raporunun, bias deneyinin, osiloskop incelemesinin, Modül 4 imalatının veya PREBERO modüllerinin tamamlandığını göstermez.

## İlgili kayıtlar

- [ADR-034 — Bias karşılaştırması ve PREBERO bias besleme sırası](ADR-034-module4-bias-comparison-and-prebero-bias-supply.md)
- [Modül 4 teknik inceleme görevi — T011](../../tasks/T011-module4-characterization-and-build.md)
