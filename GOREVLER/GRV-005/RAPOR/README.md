# GRV-005 — SCT/ADC istatistiksel veri seti ve Python model öğrenme altyapısı

- Tarih: 2026-10-11
- Durum: Açık; GRV-005-01 v01 YAML derlemesi kullanıcı tarafından başarılı bildirildi (2026-10-11); donanım testi bekliyor.
- Önceki görevlerle ilişki: GRV-004/ALT09 ve ALT10 deneyleri referans olarak korunur; bu görevin dosyaları ve kodları ayrıdır.
- Amaç: Ham ADC örneklerini kalıcı olarak kaydetmeden, kanal başına 1000 örnekten hesaplanan özellikleri PZEM referans ölçümüyle zaman ilişkisini koruyarak kaydetmek; Python'da akım tahmini modelleri için kaliteli veri seti oluşturmak.

## Kilitlenen kararlar — GRV-005-01

1. CH0, CH1, CH2 ve BIAS kanallarının her biri ölçüm döngüsünde 1000 örnek alır (toplam 4000 okuma).
2. Her ölçüm penceresi için window_start, window_end ve window_center saklanır.
3. PZEM referansı ayrı pzem_timestamp alanına sahiptir.
4. time_delta_ms, PZEM güncellemesinin monoton saat kaydı ile pencere merkezi arasındaki fark olarak hesaplanır; kabul eşiği henüz belirlenmedi.
5. adc_rms veri setine eklenir. RMS tanımı GRV-005-02'de açıkça ayrıştırılacak: ham ADC RMS ile bias/offset çıkarılmış AC RMS aynı değildir.
6. zero_count ve invalid_count kalite alanları tutulur.
7. Ham örnekler seri/HA/CSV'ye dökülmez; RAM içinde geçici tutulmaları, median/yüzdelik gibi özellikleri hesaplamak için kullanılabilir.

## Alt görev sırası

- GRV-005-01 — Ölçüm sözleşmesi ve PZEM zaman eşleştirmesi: v01 YAML derlemesi kullanıcı tarafından başarılı bildirildi; 0 A ve sabit değer koşullarındaki on_value davranışı donanımda test edilecek.
- GRV-005-02 — Özelliklerin kesin tanımları: adc_rms, adc_std, median/yüzdelikler, bias düzeltmesi ve kalite sayımları.
- GRV-005-03 — PZEM güncelleme davranışı ve zaman farkı kabul aralığı.
- GRV-005-04 — Nihai CSV şeması ve veri sözlüğü.
- Sonraki adımlar: YAML'ın cihaza yüklenmesi; fiziksel PZEM haberleşmesi, 0 A davranışı ve on_value tetikleme sıklığının doğrulanması; ardından örnekleme/CSV kayıtlarının cihaz loguyla doğrulanması; ardından Python kalite kontrolü ve model karşılaştırması.

## İlk kod taslağının sınırları

İlk taslak ayrı bir dosyadır ve GRV-002'deki PZEM YAML'ını, GRV-004 kodlarını veya ALT09/ALT10'u değiştirmez. ESP32 cihaz adı esp32d1 korunur. PZEM UART için kayıtlı pinler TX=GPIO16/RX=GPIO17, 9600 baud; önceki GRV-002 raporunda pin yönüyle ilgili tutarsızlık ve Modbus iletişim hataları olduğu için fiziksel pin eşleşmesi ve ortak referans/toprak bağlantısı güvenli biçimde doğrulanmalıdır. Bu taslak donanımda çalıştırılmadan önce kullanıcı tarafından gözden geçirilecek.

## Doğrulama seviyesi

- Kod: v01
- Derleme: kullanıcı tarafından başarılı bildirildi
- Cihaza yükleme: yapılmadı
- PZEM zaman damgası ve ADC istatistikleri: doğrulanmadı
- 0 A / sabit değer / on_value çevrim sıklığı: donanım testi bekliyor
- Ölçüm doğruluğu / RMS akım tahmini: doğrulanmadı
