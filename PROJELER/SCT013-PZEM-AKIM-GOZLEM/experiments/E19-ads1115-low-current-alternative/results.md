# E19 — Sonuç defteri

## Durum

**AÇIK — Aşama 1 loglandı; Aşama 2 (100 W ortak alan/katsayı) PLANLANDI.**

İlk donanım gözlemleri 2026-11-13 tarihli kayıt altında eklendi. Önceki sipariş bilgisi tarihsel nottur.

## Deney öncesi kayıt

- Sipariş: 1 adet ADS1115 kartı (kullanıcı bildirimi).
- Hedef kullanım: BERO'da düşük akım, özellikle 0,5 A altı için alternatif ölçüm yolu araştırması.
- Mevcut mimari korunacak: SCT-013 + bias + ESP32 ADC.
- Alternatif: SCT-013 30A/1V + ADS1115.
- Referans: PZEM-004T V3.0.
- Bias'sız bağlantı: araştırılacak; henüz doğrulanmadı.
- Kart fotoğrafı, pin/komponent incelemesi, kod, derleme ve ölçüm logu henüz yok.

## Ölçüm kayıtları

Henüz ölçüm yapılmadı. Her deney oturumu için tarih/saat, gerçek bağlantı, firmware/kod sürümü, ADS1115 gain/data rate, örnek sayısı, pencere süresi, PZEM değeri, ham ADC ve istatistikler eklenecek.

## Sonuç / yorum

Henüz sonuç yok. Sipariş verilmesi veya deney planının hazırlanması, donanımın çalıştığı ya da bias'sız ölçümün mümkün olduğu anlamına gelmez.

## 2026-11-09 — Yeni hedef notu: yaklaşık 2 A civarı

Kullanıcı, ADS1115 alternatifi işe yararsa uygun kalibrasyon katsayısıyla yaklaşık 2 A civarında da kullanılabileceğini değerlendirmeyi istedi. Bu hedef E19'a ikincil doğrulama bölgesi olarak eklendi.

Henüz ölçüm veya katsayı yoktur. Kartın giriş aralığı/gain ayarı, SCT çıkış tepe değeri, clipping, kararlılık ve PZEM referansına göre sapma ölçülecek. Düşük akım ve yaklaşık 2 A aralıklarında tek katsayının geçerli olduğu varsayılmayacak.

## 2026-11-09 — Çift yol / aralık seçimi fikri (henüz uygulanmadı)

Kullanıcının mimari tarifi: Aynı ESP üzerinde mevcut ESP32 ADC ölçüm yolu ve I²C ADS1115 ikinci ölçüm yolu birlikte bulunabilir. Yaklaşık 1 A altına inildiğinde kullanılacak ölçüm ADS1115 yolundan, eşik üstünde mevcut dahili ADC yolundan seçilecek. Hedef, iki yolun güçlü olduğu akım bölgelerini birleştirmek.

Bu henüz deney sonucu veya kesin mimari kararı değildir. İlk olarak aynı SCT sinyalinin iki ön uca güvenli biçimde verilip verilemeyeceği incelenecek. Bias/common-mode ve giriş yüklemesi doğrulanmadan paralel bağlantı yapılmayacak. Eşik 1 A başlangıç fikridir; histerezis ve geçiş davranışı ölçümle belirlenecek. Her iki yolun ham kayıtları ayrı tutulacak.

## 2026-11-13 — Aşama 1: ADS1115 ilk donanım okuma gözlemleri

Gerçek log özeti ve sınırları [ilk log kaydında](../../logs/ads1115/2026-11-13-E19-ads1115-first-bringup.md) tutulur.

- I2C taraması ADS1115'i 0x48 adresinde buldu.
- GPIO21 SDA, GPIO22 SCL, 3.3 V besleme, ADDR-GND; SCT uçları A0/A1 olarak bildirildi.
- Yüksüz diferansiyel ölçümde 8–39 µV aralığında değerler görüldü.
- Yaklaşık 60 W yükte PZEM 0.264 A / yaklaşık 60 W gösterirken önceki düşük hızlı ADS logu yaklaşık -12.8 mV ile +13.1 mV arasında değişti. 7 SPS ve yaklaşık 1 s yayın aralığı nedeniyle bu RMS akım/katsayı ölçümü değildir; aliasing olasılığı vardır.
- ESP32D1 logunda ham ct_clamp 0.13757–0.13954 A, K uygulanmış çıktı 3.332–3.380 A ve 6.700–6.920 SPS görüldü. Aynı zamanlı PZEM bu log kesitinde bulunmadığından 3.35 A gerçek akım kabul edilmedi.
- Yeni YAML: [esp32d2-ads1115-ct-clamp.yaml](../../firmware/experiments/esp32d2-ads1115-ct-clamp.yaml). Depoya eklenmesi derlendiği veya 100 W testinin yapıldığı anlamına gelmez.

**Aşama 1 yorumu:** I2C haberleşmesi ve diferansiyel sayısal okuma gözlendi. Yük değişiminde giriş çıktısının değiştiği logla destekleniyor. RMS ölçüm, 860 SPS gerçek örnek akışı, giriş common-mode güvenliği ve kalibrasyon doğrulanmadı.

## 2026-11-13 — Aşama 2: 100 W ortak ölçüm alanı testi açıldı

- **Durum:** PLANLANDI.
- **Hedef:** ADS1115/ct_clamp ölçüm yolunu mevcut ESP32D1 yolu ve PZEM ile ortak ölçüm alanında karşılaştırmak; ADS1115 katsayısını belirlemek.
- **Yük:** 100 W akkor ampul, sürekli açık.
- **Referans:** PZEM-004T V3.0; mutlak ground truth değil, BERO karşılaştırma referansı.
- **Karşılaştırma:** ESP32D1 mevcut SCT/ADC/ct_clamp; ESP32D2 ADS1115/ct_clamp; PZEM akım/gerilim/güç.
- **Sabitler:** İlk testte bağlantı/tur sayısı ve firmware ayarları sabit tutulacak. ESP32D1 K=24.22 değişmez. ADS1115 YAML'daki 30A/1V doğrusu yalnız başlangıç ayarıdır.
- **Toplanacak veri:** Zaman damgalı kararlı değerler, her iki SCT yolunun ham ct_clamp çıktısı, kalibre edilmiş akım, PZEM akımı/gücü/gerilimi, örnek sayısı/SPS, minimum/ortalama/maksimum ve standart sapma.
- **Katsayı:** Birimler ve dönüşüm doğrulandıktan sonra ADS1115 ham ct_clamp kararlı ortalaması PZEM kararlı ortalamasıyla karşılaştırılarak hesaplanacak.
- **Kabul:** Tekrarlı ölçümlerde kararlılık, girişte clipping olmaması ve PZEM'e göre sapmanın raporlanması. ±%4 hedefi henüz sonuç değildir.
- **Sonuç:** Ölçüm ve katsayı henüz yok.
