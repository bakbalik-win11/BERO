# GRV-005-07 — ADC API ön incelemesi

- Tarih: 2026-10-11
- Durum: Kaynak YAML üzerinden statik inceleme tamamlandı; yeni firmware yazılmadı ve cihaz testi yapılmadı.
- İncelenen kaynak: `GOREVLER/GRV-004/RAPOR/KOD/esp32d1-4ch-1000-raw-csv-user-snapshot-20261010.yaml`
- İlgili çalışma koşulu: ALT10'da ESP32D1, ESPHome 2026.9.1/API; 8,5 W LED koşulu korunacak. ALT09 ve mevcut çalışan ALT10 üzerine yazılmayacak.

## 1. Kaynak YAML'da görülen davranış

- GPIO32 = BIAS, GPIO33 = 1T, GPIO34 = 2T, GPIO35 = 3T olarak tanımlanmış.
- Dört ayrı `platform: adc` sensörü `update_interval: 1ms` kullanıyor.
- Her ADC sensörünün `on_value` lambda'sı, gelen `x` değerini ve `millis()` zamanını vektöre ekliyor; sayaçları 1000'e kadar artırıyor.
- Bu yapı `x` değerini ESPHome ADC sensörünün yayınladığı **voltaj** olarak topluyor; ham ADC kodu olarak değil.
- Sayaç, `on_value` çağrılarının sayısını sayıyor. Tek başına donanım ADC dönüşüm denemelerinin sayısını veya başarısız dönüşümleri kanıtlamıyor.
- Dört ayrı sensörün 1 ms güncelleme aralığı tanımlı olması, dört fiziksel okumanın aynı anda veya kesin 1 ms aralıklarla yapıldığını garanti etmez.
- Bu snapshot'ta PZEM bilerek geçici olarak çıkarılmıştır; GRV-005'in PZEM eşleştirmesi için doğrudan çalışan firmware tabanı olarak kabul edilmemelidir.

## 2. GRV-005 veri sözleşmesine göre açık farklar

1. **Ham ADC kodu:** Sözleşmedeki ADC istatistikleri ADC count biriminde. Voltaj değerlerini doğrudan `adc_mean`, `adc_std` vb. diye kaydetmek birim hatası olur.
2. **Deneme/geçerli örnek ayrımı:** Standart ADC sensörünün `on_value` callback'i yayınlanan değeri verir; bu YAML tek başına her başarısız ADC dönüşümünü gözleyebildiğini göstermiyor. `invalid_count` uydurulmamalı.
3. **Örnekleme sırası ve zaman:** Her kanalın kendi callback zamanı var; kanal örnekleri aynı çevrimin eşzamanlı örnekleri olarak varsayılmamalı.
4. **1000 örnek hedefi:** Mevcut sayaçlar 1000 yayınlanan değeri topluyor; bu, 1000 açıkça sayılmış ADC denemesi ile aynı şey değil.
5. **CSV kapsamı:** Kaynak snapshot yalnız ham satırları loga döküyor. GRV-005-04'te kilitlenen istatistik, PZEM, pencere zamanlaması ve kanal kimlikleri şemasını henüz uygulamıyor.

## 3. Teknik karar kapısı

İstatistik ve CSV kodlamasına başlamadan önce, ESPHome 2026.9.1 + ESP-IDF + klasik ESP32 için kullanılabilecek ADC arayüzü belirlenmeli. Seçilecek arayüzün şu iki ayrı özelliği kanıtlanmalı:

- ham ADC sayım değerini verebiliyor mu;
- okuma başarısızlığını/sonuçsuzluğu gerçekten ayırt edebiliyor mu.

İkinci özellik yoksa veri sözleşmesindeki `invalid_count` donanım hatası sayacı olarak uygulanamaz. Bu sınırlama raporlanmalı; sahte hata üretimi yapılmamalı. `sample_count` anlamı da ancak seçilen okuma arayüzü kesinleştikten sonra kodda sabitlenmeli.

## 4. Güvenli devam sırası

1. ADC API ve ESPHome/ESP-IDF sürümü uyumluluğunu doğrula.
2. Mevcut ESP32D1 yapılandırmasına dokunmadan, ayrı ve sürümlenmiş bir tanılama YAML'ı tasarla.
3. Önce tek kanal okuma + ham count + monotonik zaman için derleme testi yap.
4. Derleme sonucu kullanıcı tarafından doğrulanmadan KOD klasörüne taşımama kuralını uygula.
5. Tek kanal testi geçerse dört kanala ve pencere/istatistik/CSV katmanına geç.

## 5. Kapsam dışı / henüz iddia edilemez

- ADC API seçimi kesinleşmedi.
- Yeni YAML hazırlanmadı, derlenmedi veya cihaza yüklenmedi.
- Gerçek ADC toplama, invalid_count, 1000 deneme garantisi, PZEM hizalaması ve CSV üretimi doğrulanmış değildir.
- Bu kayıt tarihsel ALT09/ALT10 veya GRV-004 YAML'larını değiştirmez.
