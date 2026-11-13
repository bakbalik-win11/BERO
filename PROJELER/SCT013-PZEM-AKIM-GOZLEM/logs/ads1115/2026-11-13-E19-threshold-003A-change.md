# E19 — ADS1115 düşük akım sıfırlama eşiği 0,03 A

Tarih: 2026-11-13

## HEDEF
Çamaşır makinesi program kaydında düşük akımlı bekleme ve geçiş davranışlarının 0,05 A eşiği nedeniyle kaybolmasını azaltmak.

## DEĞİŞİKLİK
- Önceki yazılım filtresi: `if (x < 0.05) return 0.0;`
- Yeni yazılım filtresi: `if (x < 0.03) return 0.0;`
- Eşik, `calibrate_linear` filtresinden sonra uygulanan akım değeridir.
- 0,03 A altındaki değerler 0,00 A olarak yayınlanmaya devam eder; 0,03 A ve üzeri değerler geçirilir.
- ADS1115 PGA, 860 SPS, 200 ms ct_clamp penceresi, 2 s yayın aralığı ve katsayı değiştirilmedi.

## KAPSAM / KAYNAK
- Depo referans YAML: `firmware/experiments/esp32d2-ads1115-ct-clamp.yaml`
- Kullanıcının 2026-11-13 tarihinde paylaştığı çalışan yapılandırma: 606 satır; bu dosyanın 0,05 A eşiği 0,03 A olarak değiştirilmiş kopyası ayrıca hazırlandı.
- Depo referans YAML'ı, kullanıcının paylaştığı 606 satırlık çalışan YAML ile birebir aynı değildir: referans dosyada katsayı 30.0 ve UDP olay kodu bulunmaz; paylaşılan yapılandırmada katsayı 27.60 ve UDP olay alıcısı vardır. Bu nedenle cihazda hangi dosyanın çalıştığı ayrıca teyit edilmelidir.

## BEKLENEN DAVRANIŞ
0,03–0,05 A aralığındaki ct_clamp sonuçları artık sıfırlanmayacak ve Home Assistant akım entity'sinde görünebilecek. Bu aralıktaki değerlerin gerçek yük akımı mı yoksa ölçüm tabanı/gürültü mü olduğu sonraki kayıtlarla değerlendirilecek.

## DOĞRULAMA DURUMU
- GitHub YAML değişikliği: UYGULANDI.
- YAML yeniden okuma: ayrıca kontrol edilecek.
- ESPHome derleme: YAPILMADI.
- OTA / cihaza yükleme: YAPILMADI.
- Fiziksel ölçüm doğrulaması: YAPILMADI.

Bu nedenle değişiklik depoda hazırdır; cihazın yeni eşikle çalıştığı henüz söylenemez.
