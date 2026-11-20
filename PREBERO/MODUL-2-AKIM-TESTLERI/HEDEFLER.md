# Modül 2 – Masaüstü 4 Kanal / Akım Testleri

## Hedef

Masaüstü 4 kanal düzeninde akımın ölçüm sisteminde nasıl temsil edildiğini anlamak; sinyal davranışını testlerle incelemek ve kullanılacak ölçüm katsayılarını deney sonuçlarına dayanarak belirlemek.

Akım okuma hedefi bu modülde elde edilmiştir. Çalışma, elde edilen okumayı anlamlandırma ve ölçüm yöntemini geliştirme aşamasında sürmektedir.

## Ana donanım yaklaşımı

- Ana kart: ESP32-D geliştirme kartı.
- Taşıyıcı kart: ESP32 shield.
- Akım sensörü: SCT013 30A/1V.
- Ara entegre / harici ADC: ADS1115.
- ESP32-D geliştirme kartı shield üzerine takılarak masaüstü deney düzeneği imal edilecektir.
- SCT013 30A/1V sensör sinyali ADS1115 üzerinden okunacak; ADS1115 ile ESP32 arasındaki haberleşme ve pin bağlantıları gerçek donanım üzerinde doğrulanacaktır.
- Paylaşılan ESP32 + shield görseli temsili yerleşim görselidir; kullanılacak kartın kesin modeli, pin eşleşmeleri veya bağlantı şeması olarak kabul edilmez.
- Fiziksel imalat ve gerçek bağlantılar doğrulandıkça `IMALAT/IMALAT.md` dosyasına kaydedilecektir.

## Çalışma başlıkları

- SCT013 30A/1V sensör sinyalinin ADS1115 üzerinden okunması.
- ADS1115 ile ESP32-D arasındaki haberleşmenin doğrulanması.
- Sinyalin osiloskopta gözlenmesi.
- Biaslı ve biassız durumların gerektiğinde karşılaştırılması.
- Test koşullarının ve ölçüm davranışının incelenmesi.
- Katsayıların test sonuçlarına göre belirlenmesi.
- Her testin kod, log, veri ve yorumunun kendi görevinde saklanması.

## Görevler

İlk aktif görev: `MOD2-GRV001` – Akım davranışı ve katsayı çalışmaları.
