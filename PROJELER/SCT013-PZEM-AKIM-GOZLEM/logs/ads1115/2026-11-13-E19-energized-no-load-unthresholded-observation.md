# 2026-11-13 — ADS1115 filtresiz enerjili-yüksüz hat gözlemi

## HEDEF
ADS1115 + SCT ölçüm zincirinin, hatta şebeke enerjisi varken fakat ölçülen iletkende yük/akım yokken taban davranışını alt eşik filtresi olmadan gözlemek. Seyrek sıçramaların sıklığını görmek; bunları firmware'de bastırmanın gerekli olup olmadığına karar vermek.

## TEST KOŞULU
- Modül: ESP32D2 + ADS1115 + SCT
- ADS1115: I²C 0x48, diferansiyel A0-A1
- Gain: 2.048
- Sample rate: 860 SPS
- Continuous mode: açık
- ct_clamp penceresi: 200 ms
- Yayın aralığı: 1 saniye
- Kalibrasyon katsayısı: 27.60
- Yazılımsal alt eşik: YOK (kullanıcının bu testte çalıştırdığı sürüm)
- Spike filtresi: YOK
- Hat: enerjili; kullanıcı beyanına göre ölçülen hatta yük/akım yok
- PZEM akım göstergesi: grafiklerde 0.000 A

**Kaynak ayrımı:** Ayarlar önceki ADS1115 canlı YAML'ı ve kullanıcı bildirimlerinden alınmıştır. Depodaki esp32d2-ads1115-ct-clamp-live-27.60-003A-1s.yaml snapshot'ı hâlâ 0.03 A filtresini içerir; bu gece kullanılan filtresiz sürümün tam YAML snapshot'ı bu kayda eklenmemiştir. Bu nedenle depodaki snapshot filtresiz test kodu olarak gösterilmemelidir.

## GÖZLEM — KULLANICININ PAYLAŞTIĞI HA GRAFİKLERİ
- Normal taban çizgisi yaklaşık 0.001 A (1 mA) civarında, görsel olarak kararlı.
- Yaklaşık 0.048 A seviyesinde dar ve belirgin sıçramalar görülüyor.
- İlk paylaşılan yaklaşık 10 dakikalık grafikte 1 sıçrama gözlendi.
- Sonraki yaklaşık 13 dakikalık grafikte 2 sıçrama görüldü; aralarında yaklaşık 10 dakika vardı.
- İkinci grafikte sıçramalar dışında taban çizgisi belirgin biçimde değişmedi.
- PZEM akım serisi aynı ekranlarda 0.000 A gösterdi.
- Görselden örnek sayısı, kesin süre, spike genişliği ve istatistiksel dağılım hesaplanamaz; ham CSV henüz bu rapora eklenmedi.

## SONUÇ VE KARAR
1. Bu koşulda alt eşik filtresi olmadan yaklaşık 1 mA seviyesinde kararlı bir ölçüm tabanı gözlendi.
2. Gözlenen yaklaşık 48 mA sıçramalar seyrek ve normal tabandan belirgin ayrışıyor.
3. Kullanıcı kararı: şimdilik alt eşik, ortalama filtresi veya spike filtresi eklenmeyecek; ham yayınlar korunacak. Sıçramalar mevcut sıklıkta ölçümü bozacak düzeyde görülmedi.
4. Bu karar yalnızca mevcut gözlem dönemi içindir. Spike kaynağı teşhis edilmiş değildir.
5. Bu test enerjili hat/yüksüz iletken koşuludur; enerjisiz hat testi henüz yapılmadı. İki koşul birbirine karıştırılmayacaktır.

## SONRAKİ DENEY — ENERJİSİZ HAT
Aynı SCT, ADS1115, kablolama ve firmware ayarları korunarak, ölçülen iletkenin enerjisiz olduğu ayrı bir test yapılacak. ESP32/ADS1115 kendi güvenli beslemesinden çalışmaya devam edecek. Enerjisiz koşulda taban dağılımı ve spike davranışı ayrı kaydedilecek. Şebeke tarafında ayırma/bağlama işlemleri yalnız güvenli izolasyon ve yetkin uygulamayla yapılacak.

## YARIN İÇİN MİMARİ PLANI — TEK ESP DÜĞÜMÜ
Kullanıcı kararı/planı:
- Bir ESP32 üzerinde iki SCT kanalı.
- Bir ADS1115.
- PZEM-004T V3 aynı ESP32'ye UART üzerinden bağlanacak.
- Harici bias devresi kullanılmaması hedefleniyor.
- Alt eşik ve spike filtresi eklenmeyecek; ham ölçüm korunacak.
- 1 saniyelik yayın hedefleniyor.

Bu yalnız tasarım planıdır. Pinler, kart kimliği, UART eşlemesi, ADS1115 diferansiyel kanal eşlemesi, dönüşüm zamanlaması, giriş ortak-mod/rail güvenliği ve PZEM güncelleme aralığı henüz doğrulanmadı. Kod, derleme, OTA ve fiziksel entegrasyon yapılmadı.

## DOĞRULAMA SINIRI
- Kanıt: kullanıcı tarafından paylaşılan Home Assistant grafik ekran görüntüleri ve kullanıcı test koşulu bildirimi.
- Ham CSV/log: bu rapora eklenmedi.
- Spike nedeni: bilinmiyor; hipotez üretilmedi.
- Derleme/OTA: bu test için yeni bir derleme/OTA kanıtı sunulmadı.
- Enerjisiz hat testi: bekliyor.
- Tek ESP + iki SCT + ADS1115 + PZEM entegrasyonu: PLANLANDI.
