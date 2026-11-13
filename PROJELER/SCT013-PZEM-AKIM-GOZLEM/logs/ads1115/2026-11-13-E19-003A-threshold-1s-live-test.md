# E19 — ADS1115 yüksüz taban eşiği ve 1 saniye yayın denemesi

Tarih: 2026-11-13

## HEDEF VE DEĞİŞİKLİK NEDENİ

Canlı cihaz gözleminde PZEM akım göstermeye devam ederken ADS1115/ct_clamp akım entity'sinin sıfır yayınlaması görüldü. Amaç, bu düşük akım bölgesini yazılım filtresi nedeniyle sıfırlamamak ve gerçek cihaz davranışını daha sık gözlemleyebilmektir.

## UYGULANAN KOD DEĞİŞİKLİĞİ

Kullanıcının paylaştığı 606 satırlık ESP32D2 yapılandırmasında yalnızca iki ayar değiştirildi:

| Ayar | Önceki | Yeni |
|---|---:|---:|
| ct_clamp yazılım alt eşiği | 0,05 A | 0,03 A |
| ct_clamp yayın aralığı | 2 s | 1 s |

Filtre, `calibrate_linear` sonrasında hesaplanan akıma uygulanır. Dolayısıyla 0,03 A altındaki sonuçlar 0,00 A yapılır; 0,03 A ve üzerindeki sonuçlar filtreyi geçer.

## KORUNAN AYARLAR

- ESPHome cihaz kimliği: `esp32d2`
- ESP32 framework: ESP-IDF
- ADS1115 I2C: GPIO21 SDA / GPIO22 SCL, adres 0x48
- Diferansiyel giriş: A0-A1
- PGA gain: 2.048
- Sample rate: 860 SPS
- Continuous mode: açık
- ct_clamp örnekleme penceresi: 200 ms
- Kalibrasyon katsayısı: 27.60
- UDP 4210 olay alıcısı ve mevcut HA olay entity'leri: bu deneme kodunda korundu

Yayın aralığının 1 saniyeye indirilmesi 200 ms RMS hesaplama penceresini değiştirmez. Yeni sonuçların yayınlanma sıklığını artırır.

## CANLI TEST GÖZLEMİ

**KULLANICI BİLDİRİMİ — 2026-11-13:**
- Yeni kod, sıçrama (spike) davranışı ayrı tutulduğunda genel olarak başarılı bulundu.
- Testin temel gerekçesi, PZEM sıfır olmayan akım gösterirken ADS1115 tarafının 0,00 A yayınlamasıydı.
- 0,05 A yazılım alt eşiği 0,03 A'ya indirildi.
- Aynı denemede 1 saniyelik yayın aralığı test edilmeye başlandı.

Bu kayıtta ham cihaz logu/CSV, sıçramaların sayısı veya büyüklüğü ve istatistiksel özet bulunmuyor. Bu nedenle spike davranışının nedeni veya sıklığı hakkında sonuç çıkarılmadı. Kullanıcı değerlendirmesi saha gözlemi olarak kaydedilmiştir; bağımsız ölçüm doğrulaması değildir.

## DOĞRULAMA DURUMU

- Kullanıcının 606 satırlık YAML'ında iki değişiklik: HAZIRLANDI.
- Kullanıcının canlı test değerlendirmesi: KULLANICI BİLDİRİMİ.
- Bu oturumda ESPHome derleme çıktısı: bulunmuyor.
- Bu oturumda OTA sonucu: bulunmuyor.
- Ham log/CSV ve spike analizi: bekleniyor.

Bu kayıt kod değişikliğinin amacını ve test değerlendirmesini belgelendirir; derleme/OTA doğrulaması iddiası taşımaz.

## KOD KAYNAĞI NOTU

Kullanıcının paylaştığı 606 satırlık tam yapılandırma konuşma eki olarak mevcuttur. Depodaki kısa referans YAML bu yapılandırmayla birebir aynı değildir: kısa referansta katsayı 30.0'dır ve UDP alıcısı yoktur. Bu nedenle kısa referans dosyası, 27.60 katsayılı ve UDP alıcılı canlı yapılandırmanın yerine geçmez.

İki satırlık değişiklik kaydı: [2026-11-13-e19-ads1115-003a-1s.patch](2026-11-13-e19-ads1115-003a-1s.patch).
