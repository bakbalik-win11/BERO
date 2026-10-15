# PROJE BERO — GRV-005-14 v04 Gerçek Cihaz Logu Değerlendirmesi

**Tarih:** 2026-10-11  
**Firmware:** ESPHome 2026.9.1; compile time 14:40:42 +0300  
**Cihaz:** `esp32d1`, ESP32 rev3.1, 2 core  
**Kaynak log:** `GOREVLER/GRV-005/LOG/GRV-005-14-v04-GERCEK-CIHAZ-LOGU-20261011.txt`

## 1. Sonuç özeti

- **Derleme/çalışan firmware kanıtı:** PASS — cihaz logu firmware derleme zamanını bildiriyor ve API handshake başarılı.
- **CSV başlık bütünlüğü:** PASS — iki parça 16 + 25 = 41 alan.
- **Veri satırları:** PASS — 4 satırın her biri 41 alan.
- **Örnek sayısı:** PASS — CH0-1T, CH1-2T, CH2-3T ve BIAS için 1000'er örnek.
- **Temel zaman aritmetiği:** PASS.
- **ADC uzun işlem uyarısı:** FAIL / çözülmedi — uyarı devam ediyor; bileşen adı artık `interval`.
- **Ölçüm senkronizasyonu:** SINIRLI — PZEM zamanı pencere merkezinden 4145 ms sonra; bu değer gerçek Modbus paket zaman damgası değildir.

## 2. Başlık ve CSV alan kontrolü

Logdaki parçalar:
- `CSV_HEADER_PART_1`: 16 alan; son alan `sample_count`
- `CSV_HEADER_PART_2`: 25 alan; ilk alan `invalid_count`
- Birleştirilmiş başlık: 41 alan

Dört veri satırının her biri 41 alan içeriyor ve taşan fazladan alan yok. Kanallar tam olarak birer kez görünüyor: CH0-1T, CH1-2T, CH2-3T, BIAS. Dört satırda aynı `measurement_id=esp32d1_251_001` bulunuyor.

## 3. Pencere zamanlaması

| Alan | Değer | Kontrol |
|---|---:|---|
| `window_start_millis` | 251 ms | — |
| `window_end_millis` | 10309 ms | — |
| `window_duration_ms` | 10058 ms | 10309 − 251 = 10058 |
| `window_center_millis` | 5280 ms | 251 + floor(10058/2) = 5280 |
| `pzem_update_millis` | 9425 ms | `on_value` anında alınmış zaman |
| `time_delta_ms` | 4145 ms | 9425 − 5280 = 4145 |

Zaman aritmetiği tutarlı. Ancak PZEM güncellemesi pencere merkezinden 4.145 saniye sonra kaydedilmiş. Bu, PZEM değeri ile ADC penceresinin zaman bakımından yakın eşleşmediğini gösterir. Ayrıca `pzem_update_millis`, Modbus paketinin kesin alınma zamanı değildir.

## 4. ADC sonuçları

| Kanal | Ortalama ham ADC | Std. sapma | Min | Max | Aralık | Ham RMS | BIAS merkezli RMS |
|---|---:|---:|---:|---:|---:|---:|---:|
| CH0-1T | 1862.144 | 8.286 | 1660 | 1884 | 224 | 1862.162 | 8.605 |
| CH1-2T | 1860.891 | 5.375 | 1839 | 1917 | 78 | 1860.899 | 6.462 |
| CH2-3T | 1855.272 | 7.428 | 1783 | 1914 | 131 | 1855.287 | 11.830 |
| BIAS | 1864.482 | 5.271 | 1797 | 1905 | 108 | — | — |

### Yorum

- Dört kanalın da örnek sayısı 1000; `zero_count=0`.
- CH0 minimumu 1660 iken ortalaması 1862.144 ve maksimumu 1884. Bu tek başına kesin hata kanıtı değildir; fakat CH0 aralığı 224 ile diğer akım kanallarından belirgin büyük. Ham örnek dizisi olmadan bunun tekil bir uç değer mi, gerçek sinyal mi olduğu söylenemez.
- CH2 ortalaması BIAS ortalamasından yaklaşık 9.210 ADC sayımı düşük. BIAS merkezli RMS'nin 11.830, kanal standart sapmasının 7.428'den yüksek olması bu ortalama farkıyla uyumludur. Bu RMS, eşzamanlı CH2/BIAS örnek çiftlerinden hesaplanmış değildir.
- `adc_median`, yüzdelikler ve `adc_p95_minus_p05` boş bırakılmış; bu alanlar bu firmware sürümünde hesaplanmıyor.
- `invalid_count=NOT_TRACKED` alanı sayısal sayaç değildir; kaynak kodun mevcut davranışıyla tutarlıdır.

## 5. PZEM ve alan hizası

Dört satırda:
- Akım: 0.028 A
- Güç: 1.800 W
- Güç faktörü: 0.2800

Bu değerler logdaki PZEM sensör güncellemeleriyle uyumlu. Gerilim, frekans ve enerji alanları boş; mevcut YAML bu sensörleri CSV'ye doldurmuyor. Boş alanlar alan hizasını bozmuyor.

## 6. 92 ms uyarısı — kritik sonuç

Log sırası:
- 14:45:00.214 ve .229 — başlık parçaları
- 14:45:00.240–.277 — dört veri satırı
- 14:45:00.303 — `interval took a long time for an operation (92 ms), max is 50 ms`

v03'te benzer uyarı `adc.sensor` bileşeni için görünüyordu. v04'te raporlama ADC `on_value` callback'inden ayrılmış olmasına rağmen uyarı bu kez `interval` bileşeni adına sürüyor. Bu, raporlama/uzun loglama işleminin ana döngüde 50 ms sınırını aşmaya devam ettiğini güçlü biçimde düşündürüyor.

**Sonuç:** Callback ayrımı, uyarıyı ortadan kaldırmadı; yalnızca uyarının ilişkilendirildiği bileşen değişti. Başlık parçalama başarılı. Bir sonraki kod revizyonunda raporlamayı tek bir uzun lambda içinde yazdırmak yerine aşamalı/kısa işlere bölmek veya CSV çıktısını farklı bir taşıma/yazma yoluna almak değerlendirilmeli. Henüz yeni kod bu raporda değiştirilmedi.

## 7. Uyarı olmayan derleme notları

Cihaz şu önerileri verdi:
- `minimum_chip_revision: "3.1"`
- `sram1_as_iram: true`

Bunlar bu logda derleme/bağlantı başarısızlığı değil, isteğe bağlı binary boyutu/RAM yerleşimi optimizasyon önerileridir.

## 8. QC kaydı

CSV için 14 eşdeğer statik kontrol mantığı uygulandı:
1. 41 alanlı başlık
2. Dört veri satırı
3. Her satırda 41 alan
4. Dört beklenen kanalın bulunması
5. Kanal tekrarının olmaması
6. Ortak, boş olmayan measurement_id
7. Her kanalda 1000 örnek
8. Pencere süre aritmetiği
9. Merkez zamanı aritmetiği
10. PZEM delta aritmetiği
11. Sayısal alanların geçerli biçimi
12. Min/max/range tutarlılığı
13. PZEM alanlarının mevcut ve beklenen sütunlarda olması
14. BIAS özeti ve taşan sütun kontrolü

**Sonuç: 14/14 eşdeğer kontrol PASS.** Bu, depo içindeki QC Python dosyasının doğrudan çalıştırıldığı anlamına gelmez; kontrol mantığı paylaşılan log satırlarına uygulandı.

## Nihai karar

**GRV-005-14 v04: CSV yapı kontrolü PASS; ADC raporlama gecikmesi uyarısı hâlâ açık.** Başlık ve satır hizası düzelmiş görünür. Ancak 92 ms işlem uyarısı nedeniyle zamanlama/örnekleme davranışı henüz tam PASS olarak işaretlenmemelidir.
