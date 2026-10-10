# PROJE BERO — GRV-004 Ara Rapor

- **Tarih:** 2026-10-10
- **Görev:** GRV-004 — BIAS / 1T / 2T / 3T ADC sinyal tanıma
- **Cihaz:** `esp32d1` / ESP32D1
- **Durum:** Açık — deney yöntemi ve sonuç biçimi netleştiriliyor
- **Bu raporun amacı:** Mevcut adımı kayda geçirmek; sonraki kod kararını kullanıcıyla bu rapor üzerinden tartışmak.

## 1. Deney hedefi — son mutabakat

1. PZEM bu deneyde bulunmayacak.
2. Dört kanal kullanılacak:
   - GPIO32 — BIAS
   - GPIO33 — 1T
   - GPIO34 — 2T
   - GPIO35 — 3T
3. Her kanalda 1000 okuma alınacak.
4. Her kanal için MIN, MAX ve ORTALAMA hesaplanacak.
5. Dört kanalın sonuçları tek satırda yazdırılacak.
6. Bu aşamada beklenen bir ölçüm değeri kod içine konmayacak. Ölçüm yaklaşık 1,600 V çevresinde görünmezse sonuçtan hareketle ölçüm zinciri tartışılacak.
7. Okuma, daha önce denenmiş en hızlı yöntem esas alınarak yapılacak. Ancak bu yöntemin gerçek örnekleme hızı ayrıca kanıtlanmış değil.

## 2. Donanım ve yapılandırma

- ESPHome: 2026.9.1
- ESP32: rev3.1, ESP-IDF
- ADC pinleri: GPIO32 / GPIO33 / GPIO34 / GPIO35
- ADC attenuation: 12 dB
- Önceki YAML denemelerinde `update_interval: 1ms` kullanıldı.

**Önemli ayrım:** `update_interval: 1ms` bir ayardır; tek başına her 1 ms'de gerçekten yeni ADC dönüşümü alındığını kanıtlamaz.

## 3. Son yüklenen logdan gözlenenler

Kaynak: Kullanıcının 2026-10-10 tarihinde yüklediği `esp32d1-logs (8).txt`.

- ESPHome API bağlantısı başarılı.
- Dört ADC kanalının tamamı logda değer yayımlıyor.
- Bu log parçasında PZEM satırı görünmüyor.
- Logda `ADC_CSV` başlığı veya `VERI_AKTARIMI_TAMAMLANDI` satırı görünmüyor.
- Dört kanalın değerleri çoğunlukla yaklaşık 1,65–1,67 V civarında.
- Bazı tekil daha yüksek okumalar da var; örneğin 3T'de 1,721 V, BIAS'ta 1,749 V ve 1T'de 1,767 V. Bunların nedeni bu logdan belirlenemez.
- Yayınlar arasındaki zaman aralığı çoğunlukla yaklaşık 100–120 ms mertebesinde. Bu, log yayın aralığıdır; gerçek ADC donanım dönüşüm hızının kesin ölçümü olarak yorumlanmamalıdır.

## 4. Önceki denemeden korunan sorun kaydı

Önceki logda `Reason: Task wdt` ve `OTA rollback detected` mesajları görülmüştü. Bu, o açılışta bir görev zaman aşımı yaşandığını ve firmware'in önceki bölüme geri alındığını gösteriyordu. Yeni yüklenen log aynı crash/rollback mesajlarını göstermiyor. İki log aynı çalışma olarak birleştirilmemeli.

## 5. Kod durumları birbirinden ayrılmalı

- **Ham CSV biriktirme YAML'ı:** Dört kanal için vektörlerde veri ve `millis()` zaman damgası toplama, 1000'er örnekten sonra CSV satırları yazdırma amacı taşıyor. Başarıyla 1000'er örnek tamamladığı bu logla doğrulanmadı.
- **MIN/MAX/ORT tek satır testi:** Kullanıcının son onayladığı hedef budur. Bu rapor itibarıyla gerçek cihazda derlenip çalıştığı doğrulanmış nihai kod olarak işaretlenmiyor.
- Önceki çalışan YAML dosyaları ve kayıtlar değiştirilmemeli; yeni test kodu ayrı sürüm olarak tutulmalı.

## 6. Şu ana kadar doğrulananlar

- [x] `esp32d1` cihazına ESPHome API üzerinden bağlanılabildi.
- [x] BIAS, 1T, 2T ve 3T kanallarından canlı voltaj yayınları logda görüldü.
- [x] Son yüklenen log parçasında PZEM yayınları görünmüyor.
- [ ] Dört kanalın her birinde 1000 okuma tamamlandığı doğrulanmadı.
- [ ] MIN/MAX/ORT değerlerinin tek satırda üretildiği doğrulanmadı.
- [ ] Gerçek örnekleme hızı ölçülmedi.
- [ ] Nihai MIN/MAX/ORT YAML'ının derleme sonucu doğrulanmadı.

## 7. Tartışılacak açık noktalar

1. Daha önce denenmiş en hızlı okuma yönteminin tam olarak hangi kod sürümü olduğu ve gerçek ölçüm aralığı.
2. ESPHome ADC sensör callback'leriyle devam mı edileceği, yoksa daha önceki hızlı okuma yönteminin aynen geri getirilmesi mi gerektiği.
3. 1000 örnek/kanal sayımının ve tek satır çıktının logda açık bir tamamlanma işaretiyle nasıl doğrulanacağı.

## 8. Sonraki tek adım

Bu rapor üzerinden yöntemi ve kod taslağını netleştirmek. Kod ancak derleme ve cihaz logu ile doğrulandıktan sonra başarılı olarak işaretlenecek.

---

**Kayıt disiplini:** Bu rapor ara durumdur; teknik deneyin tamamlandığını veya kodun doğrulandığını iddia etmez. Önceki kod, log ve deney kayıtlarının üzerine yazmaz.
