# E00A — Protokol: ham dalga gözlemi

## Ön koşullar
- Kullanılacak ESP32 kartı ve ADC GPIO'su gerçek kart envanterinden doğrulanmalı; pin numarası varsayılmamalı.
- Ölçüm girişine şebeke gerilimi bağlanmaz. Bias-only ve SCT yüksüz adımlarında fiziksel bağlantı güvenli biçimde kontrol edilir.
- Bias orta noktası mevcut proje bağlantısına göre kullanılır; henüz uygulanmamış donanım önerileri tamamlanmış sayılmaz.

## Adımlar
1. **Bias-only:** SCT jack'i bağlı değilken bias noktasını oku. Ham ADC örneklerini hesaplama veya filtreleme yapmadan kaydet.
2. **SCT yüksüz:** SCT'yi bağla, ölçülen hatta akım olmadığını doğrula ve aynı tür kaydı al.
3. **100 W akkor:** Aynı sensör/bağlantı düzeninde ampul açıkken kaydı al. Yük değişikliğini not et.
4. Her durumda 1, 2 ve 2,5 kS/s hedeflerini dene; uygulama bu hızları gerçekten sağlayamıyorsa gerçekleşen hız ayrıca kaydedilir. Bu hızlar başlangıç karşılaştırma noktalarıdır.
5. Kayıtları PC'ye al. Ham örnek dizisini değiştirmeden sakla; çizim ve oynatma katmanı yalnız görüntüleme hızını değiştirir.
6. Her kayıt için dalga-zaman grafiği, yavaş oynatma ve ortalama/min/max/peak-to-peak/standart sapma üret.
7. Beklenen örnek sayısını hedef hız × gerçek kayıt süresi ile yaklaşık hesapla ve okunan örnek sayısıyla karşılaştır.

## Yorumlama
- Kaydı yavaş oynatmak, ADC örnekleme hızını düşürmek değildir.
- Aynı fiziksel sinyal farklı örnekleme hızlarında farklı ayrıntıda temsil edilebilir. Bu nedenle hem grafikleri hem tanımlayıcı istatistikleri karşılaştır.
- Toplam örnek sayısının beklenenle eşleşmesi, zamanlama aralıklarının kusursuz olduğunu veya hiç örnek kaybolmadığını kanıtlamaz; ilk gözlem için basit bir yeterlilik kontrolüdür.
- %90 örnek sayısı hedefi konuşmada geçici bir pratik durma fikri olarak tartışıldı; kesin kabul eşiği yapılmadı. Önce sonuçları görelim.
- Bu aşamada çift buffer, DMA, her örneğe zaman damgası, laboratuvar düzeyinde kayıp analizi veya gerçek akım hesabı şart değildir.

## Kabul ölçütü
Üç donanım durumundan en azından kayıt alınması, ham dosyaların saklanması, her kayıtta kullanılan hedef hız/süre/örnek sayısının belirtilmesi ve PC'de dalga ile temel istatistiklerin görüntülenmesi. Farklı hızların etkisi gözlemlenip paketleme öncesi basit aktarımın yeterliliğine dair bir karar notu yazılır.

## Durum
PLANLANDI. Fiziksel ölçüm ve yazılım uygulaması yapılmadı.
