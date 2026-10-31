# 150 W Akkor Ampul — Karşılaştırmalı Ölçüm Kaydı

**Yük ID:** LOAD-150W-INC  
**Yük:** 150 W akkor ampul  
**Amaç:** Modül 2 / ESP32D1 üzerinde 150 W akkor yükle SCT kanalı ölçümlerini, firmware sürümünü, logları ve referans karşılaştırmalarını ayrı bir yük kaydında izlemek.  
**Durum:** Yeni Modül 2 testi planlandı; bu dosya açıldığı sırada yeni fiziksel test sonucu henüz yoktur.

## Tarihsel Faz 1 kıyası — yeni test sonucu değildir

ROADMAP ve Faz 1 deney arşivinde daha önce şu sonuç kayıtlıdır:

- Referans: 0,616 A
- Kod sonucu: 0,615 A
- Sapma: yaklaşık −%0,2

Bu değer tarihsel Faz 1 karşılaştırmasıdır. Yeni Modül 2 testinde kullanılacak ampulün aynı fiziksel ampul olduğu, besleme koşullarının eşleştiği veya referansın aynı cihazdan alındığı henüz doğrulanmadı. Bu nedenle 0,616 A yeni test için kesin beklenen değer ya da PZEM referansı kabul edilmez. Yeni testte UNIT ve PZEM değerleri ayrıca kaydedilecektir.

## Yeni Modül 2 test koşulu

- Modül: BERO-SCT-OKUMA-TEST-002 / ESP32D1.
- İlk kanal: SCT-1 / sarı kablo / GPIO32 / ADC1_CH4.
- Ortak bias: turuncu kablo / GPIO35 / ADC1_CH7.
- Besleme: Kullanıcının bildirdiği masaüstü harici güç kaynağı.
- Yük: 150 W akkor ampul.
- Firmware: Test anındaki gerçek YAML/commit ve cihazın bildirdiği ESPHome derleme zamanı kaydedilecek.
- Test akışı: yük kapalı başlangıç → yük açık kararlı pencere → yük kapatma sonrası.
- Referans: UNIT ve PZEM mümkünse aynı zaman aralığında kaydedilecek.
- SCT-2 ve SCT-3 testleri, SCT-1 sonucu ayrı kaydedildikten sonra aynı yükle ayrı oturumlar olarak eklenebilir.

## Karşılaştırma tablosu

| Test ID | Tarih | Saat / log aralığı | ESP / düzenek | SCT kanalı | Kod / sürüm | Log | Referans | Kod sonucu | Sapma | ±%4 durumu |
|---|---|---|---|---|---|---|---|---|---|---|
| LOAD-150W-001 | Bekliyor | Bekliyor | ESP32D1 / Modül 2 / masaüstü besleme | SCT-1 / GPIO32 / sarı | Test anında kaydedilecek | Bekliyor | UNIT ve PZEM bekliyor | Ölçüm bekliyor | Hesaplanmadı | Değerlendirilmedi |

## Test oturumu kayıt standardı

Her yeni oturum ayrı Test ID alır; önceki satırlar değiştirilmez.

1. Tarih, başlangıç/bitiş saati ve gerçek log aralığı (Türkiye saati, UTC+03:00).
2. Ampulün fiziksel kimliği/etiketi ve test koşulu.
3. ESP, modül, SCT kanalı, kablo rengi ve GPIO.
4. Masaüstü besleme bilgisi; mümkünse ESP girişindeki gerilim ölçümü.
5. Firmware YAML snapshot'ı, commit SHA ve ESPHome derleme zamanı.
6. Ham log, satır sayısı, dosya boyutu ve SHA-256.
7. UNIT ve PZEM değerleri; ölçüm zamanı ve kararlı pencere.
8. Akım yayın sayısı, medyan, ortalama, standart sapma, min–maks ve kararlı pencere.
9. Referansla sapma; yalnız karşılaştırılabilir/eşzamanlı veri varsa.
10. ±%4 sonucu, teknik yorum, kanıt sınıfı ve açık eksikler.

## İlk test için not

Bu dosya yalnızca test kaydını ve planını açar. 150 W ampulün ölçümü yapılmış, firmware derlenmiş veya Modül 2 testi tamamlanmış sayılmaz. Yeni log geldiğinde hesaplanan sonuçlar ve yorum bu dosyaya, ham log ayrı log dosyasına eklenecektir.

## Güvenlik

SCT yalnız tek yalıtılmış iletkeni çevrelemelidir; faz ve nötr birlikte geçirilmez. SCT/kanal bağlantısı değiştirilirken yük enerjisiz olmalıdır. Şebeke tarafı kapalı ve korumalı lamba düzeneğinde tutulmalıdır.
