# Analiz metrikleri

## Kararlı aralık
- SCT RMS ile PZEM akımı arasındaki ortalama fark (A).
- Bağıl fark; payda sıfıra/PZEM düşük akım bölgesine yakınsa sonucu yanıltıcı olarak işaretle.
- SCT pencere RMS değişkenliği.
- PZEM alanlarının tekrar süresi ve alan bazlı değişim zamanı.
- Yük olayı algılama gecikmesi, kaçırılan olay ve clipping sayısı.
- PZEM read_status hata oranı.

## Aç-kapa dinamik gözlem ve zamanlama
- SCT model tahmini ile PZEM akım akışı aynı deneyin ortak zaman ekseninde çizilir; geçişler grafikte korunur.
- SSR olay zamanı, SCT örnek/pencere zamanı, PZEM istek zamanı ve PZEM yanıt zamanı ayrı saklanır.
- PZEM istek-yanıt süresi, haberleşme/okuma süresidir; cihazın iç ölçüm güncelleme gecikmesini tek başına vermez.
- Açma ve kapama tepkisi, yerleşme ve gözlenen zaman farkı ayrı incelenir. Sabit bir zaman kaydırması kararlı alan etiketlemesinin yerine geçmez.
- Bu grafik dinamik davranış incelemesidir; geçiş anındaki fark, PZEM'in iç ölçüm zamanı bilinmediğinden tek başına model doğruluk hatası sayılmaz.

## Eğitim verisi içi uyum
İlk aşamada model, eğitildiği aynı etiketli kararlı alan verisine yeniden uygulanır. ±%4 raporu eğitim verisi içi uyumu gösterir; bağımsız genelleme başarımı değildir. Geçerli, sıfırdan farklı PZEM akımı için bağıl hata `abs(prediction - pzem_current) / abs(pzem_current)` olarak hesaplanır.

## RMS pencerelerini birleştirme
RMS_toplam = √(Σ(Nᵢ × RMSᵢ²) / ΣNᵢ)

Aynı sinyal ve ofset giderme tanımı geçerli olmalı. Invalid/clipped kayıtlar ayrı ele alınır.

## Raporlama
Hız karşılaştırmasında aynı fiziksel yük dizisini kullan. Veri kapsamı, eksik kayıt, kalibrasyon kimliği ve filtreleri raporla. Genel "%95 bilgi korunur" iddiası kullanma; yalnız açıkça tanımlı veri ve metrik için deneysel sonuç bildir.

## PF ve yük koşulu bağlamında sonuç değerlendirme

- Aynı gerilim ve aktif güç civarında düşük PF daha yüksek RMS akım gerektirebilir. Düşük PF'li yükte yüksek SCT RMS/Peak veya yüksek PZEM akımı tek başına hata değildir.
- Yükler arası sonuçlar yalnız ham akım/genlik büyüklüğüne göre sıralanmaz. Yük türü, ölçülen PZEM V/W/I/PF, SCT sensör kimliği, tur sayısı ve örnekleme koşulu birlikte raporlanır.
- ±%4 `OK` / `OUT_OF_RANGE` kararı, ilgili ortak kararlı alanın model tahmini ile geçerli PZEM akımı arasındaki bağıl farka uygulanır. PF'nin düşük olması bu matematiksel eşiği değiştirmez; fakat sonucun fiziksel yorumunda bağlam sağlar.
- `OUT_OF_RANGE` sonucu görüldüğünde önce PZEM akımı, PF, gerilim, aktif güç, yük türü, SCT dalga biçimi/ADC sınırları ve PZEM güncelleme davranışı incelenir. Fiziksel akım artışı, sensör ölçüm hatası ve model uyumsuzluğu ayrı olgulardır.
- PF ile hata arasında korelasyon, tek başına PF'nin SCT'yi veya CT ölçümünü bozduğunu kanıtlamaz. İlişki deneysel gözlem olarak raporlanır.
