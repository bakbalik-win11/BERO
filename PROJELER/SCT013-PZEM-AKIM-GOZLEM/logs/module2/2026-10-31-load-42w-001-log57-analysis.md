# LOAD-42W-001 — Log 57 / SCT-1 değerlendirmesi

- Tarih: 2026-10-31
- Kaynak: esp32d1-logs (57).txt; 55.924 bayt / 766 satır.
- SHA-256: f519f752ea4466e82cc365dac832e3338195303e920520414e7be6538d0203ae
- Yük: 42 W ampul; teknoloji/marka/model ayrıca doğrulanmadı.
- Düzenek: ESP32D1 / Modül 2 / SCT-1 GPIO32 ADC1_CH4 / ortak bias GPIO35 ADC1_CH7.
- Log yapılandırması: ESPHome 2026.10.1; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s. K=24.22 mevcut YAML referansıdır; binary eşleşmesi iddia edilmez.

## Hedef

42 W test yükü altında SCT-1'in düşük akım davranışını, Raw AC ve ortak bias ile incelemek. 0,30 A altındaki BERO gözlem kuralı uygulanır; ±%4 kabul/ret yapılmaz.

## Ölçüm özeti

İlk/son SCT akım yayını 21:09:28–21:12:38 (+03:00); 96 yayın, yaklaşık 3 dakika 10 saniye.

| Alan | Sonuç |
|---|---:|
| SCT akım ortalaması | 0,252438 A |
| SCT akım medyanı | 0,251 A |
| Minimum – maksimum | 0,221–0,295 A |
| Örnek standart sapma | 0,011038 A |
| CV | %4,37 |
| Raw AC ortalaması | 0,0104248 V |
| Raw AC medyanı | 0,010355 V |
| Raw AC aralığı | 0,00914–0,01218 V |
| Ortak bias ortalaması (GPIO35) | 1,663469 V |
| Ortak bias aralığı | 1,656–1,673 V |
| SCT-1 ADC ortalaması (GPIO32) | 1,660745 V |
| SCT-1 ADC aralığı | 1,632–1,678 V |
| Loglanan SPS ortalaması | 17.354,8 |
| Loglanan SPS aralığı | 16.840–17.675 |

Ardışık 24 örnekli dört blok ortalaması 0,25421 A, 0,25392 A, 0,24988 A ve 0,25175 A'dır. Bu kısa kesitte belirgin uzun dönemli yükselme veya düşme eğilimi görünmüyor. Örneklerin tamamı 0,30 A altındadır. Logda hata satırı bulunmadı.

## UNIT referansıyla ilişki

Test açılışında kullanıcı tarafından bildirilen UNIT başlangıç değeri 0,174 A'dır. Bu logdaki SCT ortalaması 0,252438 A; aritmetik fark +0,078438 A, başlangıç UNIT değerine göre +%45,08'dir. Medyanın 0,174 A'ya göre farkı +%44,25'tir.

**Bu oranlar eşzamanlı doğruluk/sapma sonucu değildir.** UNIT 0,174 A değerinin bu logla aynı zaman aralığında ve aynı kararlı yük koşulunda ölçüldüğü doğrulanmadı. Yalnız iki kayıt arasındaki betimleyici fark olarak tutulur; kalibrasyon veya ±%4 değerlendirmesi yapılmaz. Logda PZEM verisi yoktur.

## Sonuç

- Log, bu 42 W test yükü oturumunda 96 SCT-1 akım yayını üretildiğini gösteriyor. Akım çıktısı yaklaşık 0,25 A çevresinde kalmış; dört blok ortalaması birbirine yakındır.
- Raw AC ortalaması yaklaşık 10,42 mV; ortak bias ortalaması 1,66347 V'tur.
- UNIT 0,174 A ile aynı kararlı zaman penceresi doğrulanmadı. PZEM akım/PF kaydı yoktur. Ampul teknolojisi ve etiket bilgisi doğrulanmadı.
- LOAD-42W-001 açık kalır. Bu kayıt düşük akım test yükü gözlemidir; kalibrasyon veya doğruluk onayı değildir. K=24.22 ve firmware değiştirilmez.

## Sonraki doğrulama

Aynı fiziksel 42 W yük çalışırken UNIT değerini SCT loguyla zaman bakımından örtüşen kararlı pencerede yeniden kaydet; varsa PZEM akım/PF'yi ayrı alanlarda ekle. Ampulün etiket/teknoloji bilgisini de test kaydına ekle.
