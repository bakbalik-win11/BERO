# GRV-004 — Sürekli dört kanal ADC sonuçları (STD öncesi sürüm)

- Tarih: 2026-10-10
- Cihaz: `esp32d1`, ESPHome 2026.9.1, ESP-IDF
- Kanallar: GPIO32 BIAS, GPIO33 1T, GPIO34 2T, GPIO35 3T
- Yapılandırma: PZEM yok; `update_interval: 10ms`; tur başına 1000 örnek/kanal hedefi
- Kayıt türü: kullanıcı tarafından yüklenen gerçek cihaz logu ve STD eklenmeden önceki sürekli MIN/MAX/ORT YAML snapshot'ı

## Dosyalar

- Kod snapshot'ı: [esp32d1-4ch-1000-min-max-avg-continuous-20261010.yaml](KOD/esp32d1-4ch-1000-min-max-avg-continuous-20261010.yaml)
- Ham log: [esp32d1-4ch-adc-tur-20261010-logs-11.txt](LOG/esp32d1-4ch-adc-tur-20261010-logs-11.txt)
- Sonraki alt görev: [ALT-GÖREV-04 — ORT hesabının bağımsız doğrulanması](ALT-GOREV-04-ORT-HESABI-20261010.md)

## Logun desteklediği sonuçlar

- API bağlantısı ve handshake başarılı.
- TUR=1 ile TUR=16 arasında 16 adet `ADC_TEST` sonuç satırı var.
- Her sonuç satırında BIAS, K1, K2, K3 için MIN, MAX ve avg alanları bulunuyor.
- Turlar yaklaşık 10,6 saniye arayla görünüyor.
- Bir kez `safe_mode took a long time for an operation (68 ms), max is 50 ms` uyarısı görülüyor.
- ESPHome, çip revizyonu ve SRAM1 için iki optimizasyon uyarısı veriyor.

## Sınırlar

- Logda örnek başına ham ADC değerleri veya sayaçların açıkça yazdırılması yok. Bu yüzden bu log tek başına her turun dört kanalda da tam 1000 örnek içerdiğini bağımsız olarak kanıtlamaz.
- Log, yukarıdaki YAML'ın birebir derlenmiş ve cihaza yüklenmiş dosya olduğunu tek başına kanıtlamaz. Dosya, önceki sürekli MIN/MAX/ORT kodunun koruma amaçlı snapshot'ıdır.
- Logda avg değerleri zaten var; ancak ham örnek dizisi olmadığı için ortalamayı bilgisayarda bağımsız olarak yeniden hesaplamak mümkün değil.
- Sonraki alt görev, ORT hesabını ESP32'ye eklemek değil; ham örnekleri dışarı alıp ORT sonucunu bilgisayarda bağımsız hesaplamak ve ESPHome raporuyla karşılaştırmak olarak tanımlandı.

## Örnek bulgu

TUR=1 ortalamaları: BIAS 1.66339 V, K1 1.66171 V, K2 1.66008 V, K3 1.65575 V. Bunlar cihaz logunda bildirilen değerlerdir; ham veriden yeniden hesaplanmış değildir.

## Durum

- [x] 16 sürekli sonuç satırı arşivlendi.
- [x] STD öncesi sürekli MIN/MAX/ORT kod snapshot'ı ayrı dosyaya kaydedildi.
- [ ] 1000 örnek/kanal sayaçlarının her tur için açık kanıtı yok.
- [ ] Ham örneklerden bilgisayarda bağımsız ORT hesabı yapılmadı.
- [ ] Sonraki alt görev açık.
