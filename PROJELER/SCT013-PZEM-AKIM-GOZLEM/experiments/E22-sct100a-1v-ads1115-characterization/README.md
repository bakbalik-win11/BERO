# E22 — Masaüstü ölçüm modülünde 30 A / 1 V ve 100 A / 1 V SCT karşılaştırma deneyi

## Durum

**FİKİR / PLAN TASLAĞI — DENEY YAPILMADI.** 100 A / 1 V SCT ile bu kapsamda ölçüm alınmadı. Ayrı bir 100 A ölçüm modülü imal edilmedi. E22 bir cihaz modülü veya modül numarası değildir; gelecekteki deney kimliğidir.

## Amaç

Mevcut günlük masaüstü ölçüm düzeneği olan **Modül 4 (ESP32D2 + ADS1115 + SCT ölçüm zinciri)** başarılı ve kararlı biçimde çalışmaya devam ettikten sonra, 100 A / 1 V SCT'nin aynı ölçüm yaklaşımında nasıl davrandığını incelemek.

Kullanıcıyla konuşulan olası karşılaştırma düzeni:
- Bir ölçüm kanalında SCT 30 A / 1 V.
- Diğer ölçüm kanalında SCT 100 A / 1 V.
- İki sensörün aynı koşullarda PZEM ölçümüyle karşılaştırılması.

Bu, henüz kesinleşmiş bağlantı planı değildir. İki kanalın mevcut ESP32D2/ADS1115 donanımında nasıl kurulacağı, kanal/ADC bağlantıları ve aynı anda mı yoksa ayrı oturumlarda mı ölçüm alınacağı fiziksel donanım görüldükten sonra kararlaştırılacaktır.

## Ön koşul

1. Modül 4'ün mevcut ESP32D2 + ADS1115 + SCT ölçüm zinciri günlük kullanımda kararlı biçimde çalışmalı.
2. Mevcut 30 A / 1 V ölçüm yolu ve çalışan firmware korunmalı.
3. 100 A / 1 V sensörün tam etiketi, çıkış oranı, kablo/konnektör yapısı ve uygun bağlantı ön ucu fiziksel olarak incelenmeli.
4. ADS1115 giriş ortak-mod seviyesi, mutlak giriş sınırları, burden/bias ve koruma koşulları doğrulanmalı.
5. İki SCT'nin PZEM ile karşılaştırılabileceği güvenli ve tekrarlanabilir yük koşulları seçilmeli.

## Deney ilkeleri

- 30 A / 1 V ve 100 A / 1 V sensörlerin katsayıları birbirine kopyalanmayacak.
- Mevcut günlük Modül 4 firmware'i deney öncesinde yedeklenip korunacak; değişiklikler ayrı deney snapshot'ında tutulacak.
- 100 A / 1 V sensörün daha yüksek nominal akım aralığı, düşük akımda daha iyi hassasiyet sağlayacağı anlamına gelmez.
- PZEM karşılaştırma/etiketleme referansıdır; kusursuz ground truth kabul edilmez.
- Ölçüm alınmadan katsayı, doğruluk, kararlılık veya çalışma aralığı sonucu yazılmayacak.
- Deney logu, kullanılan firmware snapshot'ı, sensör kimliği, bağlantı düzeni, PZEM verisi ve yorum aynı E22 kaydına bağlanacak.

## Güvenlik kapıları

- SCT sekonderi, primer iletkenden akım geçerken açık devre bırakılmaz.
- ADS1115 PGA aralığı, AIN pinlerinin mutlak gerilim sınırlarını yükseltmez.
- SCT çıkışının ADS1115'e doğrudan bağlanması uygun kabul edilmez; gerçek sinyal seviyesi, bias/common-mode ve giriş koruması doğrulanır.
- Şebeke bağlantısı uygun muhafaza ve koruma ile, yetkin kişi tarafından yapılır.

## Açık konular

- İki sensörün aynı anda mı, ayrı oturumlarda mı ölçüleceği.
- Mevcut ADS1115 modülünde iki SCT kanalı için uygun giriş düzeni.
- Sensörlerin primer tur sayısı ve karşılaştırma yükleri.
- 100 A / 1 V sensörün tam model/etiket teyidi.
- Gerekli ayrı firmware snapshot'ı ve kalibrasyon yöntemi.

## Sonuç kaydı

Bu belge yalnızca kullanıcıyla konuşulan gelecek deney fikrini korur. Şu ana kadar E22 kapsamında firmware hazırlanmadı, derleme/OTA yapılmadı, sensör bağlantısı kurulmadı ve ölçüm/analiz alınmadı.
