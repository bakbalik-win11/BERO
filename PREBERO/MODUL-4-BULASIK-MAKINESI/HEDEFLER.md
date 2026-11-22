# Modül 4 – Bulaşık Makinesi

## Hedef

Bulaşık makinesinin elektriksel davranışını gözlemleyerek programını ve program aşamalarını mümkün olduğunca doğru tahmin etmek; tespit edilen aşamalara göre bildirim üretmek.

## Görevler

Donanım hazırlığı ve kullanım/analiz çalışmaları bu modülün GOREVLER klasörü altında, basamaklar halinde yürütülür. Yeni görevler ihtiyaç ve önceki görevin sonuçlarına göre açılır.


## Ölçüm altyapısı ve ek gözlem kanalları

- **Akım ölçümü:** Modül 2 masaüstü prototipinde geliştirilen SCT013 + ADS1115 + ESP32D2 ölçüm yolu ve V1.6 tek fonksiyon kalibrasyon modeli başlangıç referansıdır. Modül 4'te gerçek bulaşık makinesi üzerinde uygulanacak; saha davranışı bu modülün kendi kayıtlarında gözlemlenecektir.
- **Mevcut yazılım:** Modül 4 için kaba yazılım taslağı bulunmaktadır; görevler açıldıkça gözden geçirilip sürümlenecektir.
- **Planlanan ek kanallar:** Akım gözlemine ses ve titreşim verileri eklenecektir. Donanım bağlantısı, sensör seçimi, yazılım entegrasyonu ve aşama sınıflandırma başarısı henüz doğrulanmış değildir.
- **Hedef:** Bulaşık makinesinin programını ve program aşamalarını akım, ses ve titreşim davranışlarını birlikte değerlendirerek tahmin etmek; uygun aşamalarda bildirim üretmek.


## Ortak veri toplama mimarisi – imalat öncesi tasarım kapısı

Modül 4, Modül 3 ile ortak zaman pencereli çoklu sensör veri toplama mimarisini kullanacak şekilde tasarlanacaktır. SCT013 akım, MAX4466 ses ve MPU6050 titreşim verileri sensörlerin kendi uygun örnekleme hızlarında toplanacak; ortak 1 saniyelik slotta zaman damgalı özellik kayıtları birleştirilecektir. Örnek veri alanları: current_rms_a, sound_rms/peak/zcr, vib_x/y/z_rms. Bu yapı henüz taslak mimaridir; örnekleme hızları, ADC/pin paylaşımı, zaman damgası, veri aktarımı ve kaynak yükü kesinleşmemiştir. **Mimari kararlar ve bağlantı/veri planı netleşmeden Modül 4 imalatına geçilmeyecektir.** Ayrıntı: `PREBERO/ORTAK-MIMARI/MODUL-3-4-ORTAK-ZAMAN-PENCERELI-VERI-TOPLAMA-MIMARISI.md`.


## PF ve dalga biçimi araştırmasına katkı – koşullu tasarım bileşeni

Modül 3/4 saha deneyleri, cihazların farklı çalışma evrelerinde akım davranışı ve mevcutsa PF verisi sağlayarak Modül 2'nin dalga biçimi/PF etkisi araştırmasına katkıda bulunacaktır. Bu ilişki araştırma hedefidir; PF'nin ölçüm sapmasına neden olduğu henüz kanıtlanmış değildir.

- ZMPT101B başlangıçta zorunlu sensör değildir. Modül 2 araştırmasında yararlı ve tekrarlanabilir sonuç verirse, Modül 3/4 deneylerinde doğrulanırsa ve işlemci/kaynak yükü uygun bulunursa nihai modüle eklenebilir.
- PF için gerilim ve akım dalga biçimlerinin uygun zaman eşlemeli örneklenmesi gerekir; ZMPT101B tek başına PF üretmez.
- Mevcut ESP32'nin CPU/RAM/örnekleme/yayın yükü deneyle ölçülür. Yetersiz kalırsa ESP32-P4 değerlendirilir; işlemci seçimi şimdilik açık karardır.
- Nihai imalat, ses, titreşim, akımla senkronizasyon ve seçilirse PF katmanı deneylerle olgunlaştıktan sonra yapılacaktır.


## Dağıtık ESP ve PZEM paket yayınlama tecrübesi

Nihai Modül 4 donanımı oluşana kadar sensör kanalları ayrı/geçici ESP'lerde çalıştırılabilir. Her ESP kendi ölçüm özetini paket halinde yayınlayacak; PZEM ile kurulan paket yayınlama tecrübesi temel alınacaktır. Paketlerde cihaz/kanal kimliği, zaman damgası ve ortak zaman dilimi numarası bulunması hedeflenir. Paket alanları ve yayın davranışı, mevcut PZEM kaynak kodu/logları incelenerek kesinleştirilecektir; henüz görülmemiş protokol ayrıntıları varsayılmayacaktır. Merkezi alıcı paketleri zaman ve dilim bilgisiyle eşleştirecek; kayıp, tekrar, gecikme ve saat hizası test edilecektir. Deneyler tamamlandığında doğrulanan kanallar tek modülde birleştirilecektir.
