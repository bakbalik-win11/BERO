# Analiz metrikleri

## Kararlı aralık
- SCT RMS ile PZEM akımı arasındaki ortalama fark (A).
- Bağıl fark; payda sıfıra/PZEM düşük akım bölgesine yakınsa sonucu yanıltıcı olarak işaretle.
- SCT pencere RMS değişkenliği.
- PZEM alanlarının tekrar süresi ve alan bazlı değişim zamanı.
- Yük olayı algılama gecikmesi, kaçırılan olay ve clipping sayısı.
- PZEM read_status hata oranı.

## Geçiş / kararlı ayrımı
Yaklaşık 3 s olay sonrası etiketi başlangıç maskesidir, cihaz garantisi değildir. E03/E04'e göre güncellenir.

## RMS pencerelerini birleştirme
RMS_toplam = √(Σ(Nᵢ × RMSᵢ²) / ΣNᵢ)

Aynı sinyal ve ofset giderme tanımı geçerli olmalı. Invalid/clipped kayıtlar ayrı ele alınır.

## Raporlama
Hız karşılaştırmasında aynı fiziksel yük dizisini kullan. Veri kapsamı, eksik kayıt, kalibrasyon kimliği ve filtreleri raporla. Genel "%95 bilgi korunur" iddiası kullanma; yalnız açıkça tanımlı veri ve metrik için deneysel sonuç bildir.
