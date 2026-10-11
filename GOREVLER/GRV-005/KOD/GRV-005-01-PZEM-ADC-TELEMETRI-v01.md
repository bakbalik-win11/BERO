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
