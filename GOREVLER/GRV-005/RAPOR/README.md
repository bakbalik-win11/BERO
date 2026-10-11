# GRV-005 — SCT/ADC istatistiksel veri seti ve Python model öğrenme altyapısı

- Tarih: 2026-10-11
- Durum: GRV-005 açık; GRV-005-01 gözlem hedefi bakımından kapatıldı. Prototip kendi tüketimini ölçtüğü için gerçek 0 A testi uygulanabilir değil; 0.028 A mevcut pratik taban değeridir. Her başarılı Modbus yanıtı ile on_value arasında bire bir eşleşme doğrulanmış değildir. GRV-005-02 özellik tanımları aşamasında.
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

- GRV-005-01 — **Kapatıldı (gözlem hedefi tamamlandı).** [Kapanış raporu](GRV-005-01-KAPANIS-20261011.md); [ilk log incelemesi](GRV-005-01-LOG-ILK-GOZLEM-20261011.md). Gerçek 0 A testi prototipin kendi tüketimi nedeniyle uygulanabilir değil. Her başarılı Modbus yanıtı ile on_value bire bir eşleşmesi doğrulanmış sayılmıyor.
- GRV-005-02 — **Aktif alt görev:** ADC özelliklerinin kesin tanımları. [Alt görev kapsamı](GRV-005-02-OZELLIK-TANIMLARI-20261011.md) ve [teknik öneri v01](GRV-005-02-OZELLIK-TANIMLARI-ONERI-v01-20261011.md). Öneri kullanıcı onayı bekliyor; henüz kodlama yok.
- GRV-005-03 — PZEM güncelleme davranışı ve zaman farkı kabul aralığı.
- GRV-005-04 — Nihai CSV şeması ve veri sözlüğü.
- Sonraki adımlar: GRV-005-02'de özelliklerin matematiksel tanımlarını kilitlemek; ardından GRV-005-03 zaman hizalaması ve GRV-005-04 CSV şemasına geçmek. Modbus yanıtı/on_value bire bir eşleşmesi ancak ayrıca gerek duyulursa ayrı bir tanılama deneyi olarak açılacak.

## İlk kod taslağının sınırları

İlk taslak ayrı bir dosyadır ve GRV-002'deki PZEM YAML'ını, GRV-004 kodlarını veya ALT09/ALT10'u değiştirmez. ESP32 cihaz adı esp32d1 korunur. PZEM UART için kayıtlı pinler TX=GPIO16/RX=GPIO17, 9600 baud; önceki GRV-002 raporunda pin yönüyle ilgili tutarsızlık ve Modbus iletişim hataları olduğu için fiziksel pin eşleşmesi ve ortak referans/toprak bağlantısı güvenli biçimde doğrulanmalıdır. Bu taslak donanımda çalıştırılmadan önce kullanıcı tarafından gözden geçirilecek.

## Doğrulama seviyesi

- Kod: v01
- Derleme: kullanıcı tarafından başarılı bildirildi
- Cihaza yükleme: logda çalışan cihaz doğrulandı
- PZEM zaman işareti: sabit 0.028 A altında yaklaşık 5 saniyelik yenilenme gözlendi
- Gerçek 0 A: prototipin kendi tüketimi nedeniyle uygulanabilir değil; 0.028 A bu düzenekte pratik taban değeridir
- Başarılı Modbus yanıtı ile on_value bire bir eşleşmesi: bağımsız olarak doğrulanmadı
- ADC istatistikleri ve RMS akım tahmini: bu logda doğrulanmadı
- Ölçüm doğruluğu / RMS akım tahmini: doğrulanmadı
