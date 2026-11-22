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
