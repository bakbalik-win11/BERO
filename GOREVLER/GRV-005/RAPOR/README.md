# GRV-005 — SCT/ADC istatistiksel veri seti ve Python model öğrenme altyapısı

- Tarih: 2026-10-11
- Durum: Açık; GRV-005-01 v01 derlendi ve cihaza yüklendi. İlk PZEM zaman damgası logu incelendi; sabit 0.028 A koşulunda yaklaşık 5 saniyelik güncelleme ve millis yenilenmesi gözlendi. Gerçek 0 A ve Modbus yanıtı/on_value bire bir eşleşmesi test bekliyor.
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

- GRV-005-01 — Ölçüm sözleşmesi ve PZEM zaman eşleştirmesi: v01 YAML derlendi/yüklendi. İlk log sabit 0.028 A değerinde on_value zaman işaretinin yaklaşık 5 saniyede bir yenilendiğini gösteriyor. [İlk log incelemesi](GRV-005-01-LOG-ILK-GOZLEM-20261011.md). Gerçek 0 A ve başarılı Modbus yanıtı ile bire bir eşleşme açık.
- GRV-005-02 — Özelliklerin kesin tanımları: adc_rms, adc_std, median/yüzdelikler, bias düzeltmesi ve kalite sayımları.
- GRV-005-03 — PZEM güncelleme davranışı ve zaman farkı kabul aralığı.
- GRV-005-04 — Nihai CSV şeması ve veri sözlüğü.
- Sonraki adımlar: gerçek 0 A koşulunda güncellemeyi doğrulamak; başarılı Modbus yanıtı ile on_value sayısını bağımsız gözlemle karşılaştırmak; sonra ADC örnekleme/CSV aşamasına geçmek ve Python kalite kontrolü/model karşılaştırmasını yapmak.

## İlk kod taslağının sınırları

İlk taslak ayrı bir dosyadır ve GRV-002'deki PZEM YAML'ını, GRV-004 kodlarını veya ALT09/ALT10'u değiştirmez. ESP32 cihaz adı esp32d1 korunur. PZEM UART için kayıtlı pinler TX=GPIO16/RX=GPIO17, 9600 baud; önceki GRV-002 raporunda pin yönüyle ilgili tutarsızlık ve Modbus iletişim hataları olduğu için fiziksel pin eşleşmesi ve ortak referans/toprak bağlantısı güvenli biçimde doğrulanmalıdır. Bu taslak donanımda çalıştırılmadan önce kullanıcı tarafından gözden geçirilecek.

## Doğrulama seviyesi

- Kod: v01
- Derleme: kullanıcı tarafından başarılı bildirildi
- Cihaza yükleme: logda çalışan cihaz doğrulandı
- PZEM zaman işareti: sabit 0.028 A altında yaklaşık 5 saniyelik yenilenme gözlendi
- Gerçek 0 A: test bekliyor
- Başarılı Modbus yanıtı ile on_value bire bir eşleşmesi: bağımsız olarak doğrulanmadı
- ADC istatistikleri ve RMS akım tahmini: bu logda doğrulanmadı
- Ölçüm doğruluğu / RMS akım tahmini: doğrulanmadı
