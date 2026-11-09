# E19 — Sonuç defteri

## Durum

**PLANLANDI — henüz fiziksel deney yapılmadı.**

Kullanıcı 2026-11-09 tarihinde yaklaşık 250 TL tutarında bir ADS1115 kartı sipariş ettiğini ve hafta sonu denemeyi hedeflediğini bildirdi.

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
