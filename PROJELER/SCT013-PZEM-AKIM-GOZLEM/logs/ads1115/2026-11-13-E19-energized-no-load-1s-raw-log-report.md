# 2026-11-13 — E19 ADS1115 enerjili-yüksüz hat / 1 saniye yayın logu

## HEDEF
Ölçülen iletkende yük yokken, hat enerjili durumda ADS1115 + SCT zincirinin 1 saniyelik yayın davranışını görmek. 5 mA yazılım eşiğinin gerekli olup olmadığını değerlendirmek ve kullanıcı kararı doğrultusunda alt eşiksiz kod snapshot'ını saklamak.

## TEST KOŞULU
- Cihaz: ESP32D2, IP 192.168.0.80
- ESPHome: 2026.10.2
- ADS1115: I²C 0x48, GPIO21 SDA / GPIO22 SCL, A0-A1 diferansiyel
- Gain: 2.048
- Sample rate ayarı: 860 SPS (logda enum değeri 7 görünür)
- Continuous mode: açık
- ct_clamp penceresi: 200 ms
- Yayın aralığı: 1 saniye
- Kalibrasyon katsayısı: 27.60
- Hat: enerjili; kullanıcı beyanına göre ölçülen iletkende yük/akım yok
- PZEM: paylaşılan grafikte 0.000 A

## OTA / CİHAZ LOGU
- OTA bağlantısı ve ESPHome API handshake başarılı.
- Derleme bilgisi: 2026-11-13 22:25:39 +0300.
- I²C taramasında ADS1115 0x48 bulundu.
- ct_clamp: Sample Duration 0.20 s; Update Interval 1.000 s.
- Log kesitinde tekrarlanan ct_clamp ham AC çıktısı 0.000 A; HA sensör yayını 0.000 A.
- Ham örnek sayısı log satırlarında yaklaşık 69–105 farklı örnek/200 ms pencere; raporlanan efektif hız yaklaşık 345–525 SPS aralığında değişiyor.
- ESP32D2 Wi-Fi bağlantısı sürüyor; sinyal yaklaşık -60 ile -65 dBm.
- UDP 4210 olay alıcısı aktif; örnek EVENT_ID 210–213 paketleri alınıp HA text entity'lerine aktarılmış.
- Kaynak log: [tam OTA logu](2026-11-13-E19-energized-no-load-1s-ota-log.txt).
- Log dosyası SHA-256: `18a0b7c47b92b5447d2c778917e4f4e738a9279d47c7827bf85f766701efda54`.

## KOD SNAPSHOT'I
- [ESP32D2 ADS1115 1 s / alt eşiksiz YAML](../../firmware/experiments/esp32d2-ads1115-ct-clamp-live-27.60-1s-unthresholded.yaml)
- Kaynak kullanıcı YAML SHA-256: `3dd5c108cdf963705e3e3d74740b2029959eb992c9fe45bcfca1cf5f2d793c0f`.
- Kaydedilen snapshot'ta 0.005 A lambda filtresi kaldırıldı; calibrate_linear katsayısı 27.60, 200 ms pencere, 1 s yayın ve UDP 4210 alıcısı korundu.
- Cihaz logu, yüklenen 0.005 A filtreli taslaktan alınmıştır. Depoya kaydedilen alt eşiksiz YAML, bu logla aynı binary olarak doğrulanmış değildir.

## SONUÇ / YORUM
1. **LOG İLE DESTEKLENDİ:** Cihaz 1 saniye güncelleme aralığıyla çalışıyor ve log kesitinde ct_clamp ile HA sensör çıktısı 0.000 A gösteriyor.
2. **KULLANICI GÖZLEMİ:** Paylaşılan grafikte ADS1115 serisi sıfır çizgisinde; PZEM de 0.000 A gösteriyor.
3. **KOD KARARI:** 0.005 A alt eşiği kaldırıldı. Bundan sonra ct_clamp 0.000 A üretiyorsa 0.000 A yayınlanacak; alt eşik veya spike filtresi uygulanmayacak. Bu, küçük sıfır çevresi değerlerin de görünmesine izin verir.
4. Yaklaşık 0.048 A tekil sıçramalar önceki grafiklerde görülmüştü; bu log kesitinde sıçrama kanıtı yok. Spike nedeni teşhis edilmiş değildir.
5. Ham logdaki 0.000 A sonucu, filtreli test anına aittir; filtresiz YAML'ın cihazda çalıştığını kanıtlamaz.

## DOĞRULAMA SINIRI / AÇIKLAR
- Tam OTA logu saklandı; cihazın API bağlantısı, I²C ADS1115 keşfi ve 1 s ct_clamp yapılandırması logla doğrulandı.
- Depoya kaydedilen alt eşiksiz YAML için ayrıca ESPHome derlemesi ve OTA yapılmadı.
- Enerjisiz hat taban testi henüz yapılmadı.
- ADS1115 A0/A1 ortak-mod ve giriş ray sınırlarının fiziksel doğrulaması hâlâ açık güvenlik koşuludur.
- Yarın planlanan tek ESP + 2 SCT + ADS1115 + PZEM entegrasyonu ayrı tasarım/derleme/cihaz doğrulaması gerektirir.
