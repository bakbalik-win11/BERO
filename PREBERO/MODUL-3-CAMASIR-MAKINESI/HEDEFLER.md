# Modül 3 – Çamaşır Makinesi

## Hedef

Çamaşır makinesinin elektriksel davranışını gözlemleyerek programını ve program aşamalarını mümkün olduğunca doğru tahmin etmek; tespit edilen aşamalara göre bildirim üretmek.

## Görevler

Donanım hazırlığı ve kullanım/analiz çalışmaları bu modülün GOREVLER klasörü altında, basamaklar halinde yürütülür. Yeni görevler ihtiyaç ve önceki görevin sonuçlarına göre açılır.


## Ölçüm altyapısı ve ek gözlem kanalları

- **Akım ölçümü:** Modül 2 masaüstü prototipinde geliştirilen SCT013 + ADS1115 + ESP32D2 ölçüm yolu ve V1.6 tek fonksiyon kalibrasyon modeli başlangıç referansıdır. Modül 3'te gerçek çamaşır makinesi üzerinde uygulanacak; saha davranışı bu modülün kendi kayıtlarında gözlemlenecektir.
- **Mevcut yazılım:** Modül 3 için kaba yazılım taslağı bulunmaktadır; görevler açıldıkça gözden geçirilip sürümlenecektir.
- **Planlanan ek kanallar:** Akım gözlemine ses ve titreşim verileri eklenecektir. Donanım bağlantısı, sensör seçimi, yazılım entegrasyonu ve aşama sınıflandırma başarısı henüz doğrulanmış değildir.
- **Hedef:** Çamaşır makinesinin programını ve program aşamalarını akım, ses ve titreşim davranışlarını birlikte değerlendirerek tahmin etmek; uygun aşamalarda bildirim üretmek.


## Ortak veri toplama mimarisi – imalat öncesi tasarım kapısı

Modül 3, Modül 4 ile ortak zaman pencereli çoklu sensör veri toplama mimarisini kullanacak şekilde tasarlanacaktır. SCT013 akım, MAX4466 ses ve MPU6050 titreşim verileri sensörlerin kendi uygun örnekleme hızlarında toplanacak; ortak 1 saniyelik slotta zaman damgalı özellik kayıtları birleştirilecektir. Örnek veri alanları: current_rms_a, sound_rms/peak/zcr, vib_x/y/z_rms. Bu yapı henüz taslak mimaridir; örnekleme hızları, ADC/pin paylaşımı, zaman damgası, veri aktarımı ve kaynak yükü kesinleşmemiştir. **Mimari kararlar ve bağlantı/veri planı netleşmeden Modül 3 imalatına geçilmeyecektir.** Ayrıntı: `PREBERO/ORTAK-MIMARI/MODUL-3-4-ORTAK-ZAMAN-PENCERELI-VERI-TOPLAMA-MIMARISI.md`.


## Step 2 – Ses/titreşim bağımsız veri toplama ve yayın

2026-11-22 kullanıcı kararı:

- Step 1 tamamlandı: Çamaşır makinesi uzatma kablosuyla masaüstü akım ölçüm düzeneğinden beslendi ve akım okundu.
- Step 2'de ses ve titreşim, çamaşır makinesinin yanına yerleştirilecek ayrı/geçici bir ESP ile alınacaktır.
- Geçici ESP, verileri PZEM'de kullanılan yayın yaklaşımına benzer şekilde zaman bilgisi ve zaman dilimi/slice numarasıyla yayınlayacaktır.
- Akım verisi ile ses/titreşim yayınları zaman damgası ve dilim numarası üzerinden eşleştirilerek deneylerle doğrulanacaktır.
- Bu aşamada nihai Modül 3 imalatı yapılmayacaktır. Deneyler sonucunda ses/titreşim ve akım tarafı birlikte çalışacak olgunluğa geldiğinde doğrulanmış yapı tek modülde toplanacaktır.

**Step 2'nin hedefi:** Ses/titreşim verisinin bağımsız ESP üzerinden alınması, zaman/dilim bilgisiyle yayınlanması ve akım kayıtlarıyla eşleştirilebilirliğinin deneysel olarak gösterilmesidir. Nihai modül imalatı bu adımın kapsamında değildir.
