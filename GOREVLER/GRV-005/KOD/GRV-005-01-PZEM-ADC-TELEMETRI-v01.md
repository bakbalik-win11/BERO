# GRV-005-01 — PZEM + ADC telemetri taslağı v01

- Tarih: 2026-10-11
- Dosya: GRV-005-01-PZEM-ADC-TELEMETRI-v01.yaml
- ESP adı korunur: esp32d1 / ESP32D1
- Amaç: PZEM-004T V3.0 telemetrisini ve ADC özellik üretimi için yeni, ayrı bir deneme hattını başlatmak.
- Durum: YAML derlemesi kullanıcı tarafından başarılı bildirildi (2026-10-11); cihaza yükleme ve donanım testi bekliyor.

## Bu sürümün kapsamı

- PZEM UART: TX GPIO16, RX GPIO17, 9600 baud (mevcut GRV-002 kayıtlı yapılandırmasından kopyalanan başlangıç varsayımı).
- ADC kanalları: GPIO33=CH0, GPIO34=CH1, GPIO35=CH2, GPIO32=BIAS. Bu eşleme, kullanıcının mevcut donanım etiketleriyle son kez doğrulanmalıdır.
- Kanal başına 1000 örnek hedefi.
- Ham örnekleri seri/HA üzerinden yayımlamak yerine RAM'de geçici işleyip istatistik üretme hedefi.
- PZEM güncelleme anı için monoton millis() işareti tutulacak; ADC pencere merkeziyle fark aynı monoton saat tabanında hesaplanacak.
- Duvar saati alanları için zaman senkronizasyonu gereklidir; monoton saat ve epoch timestamp aynı kavram değildir.

## Derleme sonrası zorunlu PZEM davranış testleri

1. Akım 0 A iken güncelleme ve `on_value` tetiklemesi geliyor mu?
2. Akım sabitken, değer değişmediği halde `on_value` tetikleniyor mu?
3. `on_value` her Modbus çevriminde mi çalışıyor, yoksa yalnızca yayımlanan değer değiştiğinde mi?
4. Modbus sorgusu gönderilmesi, geçerli yanıt alınması ve `on_value` tetiklenmesi ayrı olaylar olarak izlenecek. `on_value` her başarılı yanıtı temsil ettiği kanıtlanmadan kesin Modbus yanıt zamanı kabul edilmeyecek.

## Kritik teknik sınırlar

1. GRV-002'de PZEM yanıt zaman aşımı/kısmi yanıt/parse hataları ve TX/RX pin yönü tutarsızlığı kaydedilmiştir. Önce fiziksel UART yönü, lojik seviye/arayüz ve topraklama düzeni güvenli biçimde doğrulanmalıdır.
2. ESP32 GPIO'larına 5 V uygulanmamalıdır. PZEM arayüz kartının çıkış seviyesi/izolasyonu doğrulanmadan bağlantı yapılmamalıdır.
3. PZEM bileşeninin 5 saniyelik güncellemesi ADC penceresiyle otomatik eşzamanlı değildir. time_delta_ms yalnızca zaman yakınlığını ölçer; ölçüm pencerelerinin aynı fiziksel dönemi kapsadığını tek başına garanti etmez.
4. Bu rapor kodun başarılı derlendiğini veya akım ölçtüğünü iddia etmez.


## Ek durum kaydı — 2026-10-11 (önceki metni silmeden)

- Kullanıcı başarılı derlemeyi bildirdi; sağlanan logda `esp32d1` cihazına API üzerinden bağlanıldığı ve PZEM sensörlerinin çalıştığı görülüyor.
- İlk log incelemesi: akım 0.028 A sabit görünürken `pzem_update_millis` yaklaşık 5 saniyede bir yenilendi.
- Prototip kendi tüketimini de ölçtüğünden gerçek 0 A koşulu bu düzenekte oluşturulamıyor. 0.028 A, bu prototip için pratik taban değeridir; gerçek sıfır akım olarak yorumlanmamalıdır.
- GRV-005-01, PZEM sensör yayınına eşlik eden zaman işaretinin yenilenmesini gözlemleme hedefi bakımından kapatıldı. Her başarılı Modbus yanıtı ile `on_value` arasında bire bir ilişki bu logla kanıtlanmadı.
- YAML bu aşamada yalnızca PZEM zaman işareti tanılama iskeletidir; 1000 örnekli ADC penceresi, RMS/istatistikler ve CSV kaydı uygulanmış değildir.
- Ayrıntı: [GRV-005-01 kapanış raporu](../RAPOR/GRV-005-01-KAPANIS-20261011.md).
