# T006 — SCT katsayısı/model değerlendirmesi

- **Durum:** PLANLANDI
- **Faz:** 1.3 ve sonraki analiz aşamalarıyla bağlantılı
- **Bağımlılık:** T005 ve T003; ilgili kararlı alan/etiketleme yöntemi geliştirilmiş olmalı
- **Hedef:** PZEM referans akışına göre SCT verisinden model/katsayı çıkarmak ve kullanılan veriyi izlenebilir biçimde kaydetmek.

## Yapılacak
1. [Kalibrasyon/model prosedürünü](../calibration/PROCEDURE.md) ve T003'teki ±%4 bağıl sapma kararını uygula.
2. Kullanılan SCT kayıtları ile geçerli PZEM akım okumalarının hangi kararlı alanlar üzerinden ilişkilendirildiğini belgele. Kararlılık ölçütleri deney verisiyle geliştirilecek; burada önceden sabit bir zaman maskesi varsayılmaz.
3. Kullanılan donanımı, tarihi, yük/olay koşullarını, ham veri konumunu, yazılım/hesaplama sürümünü ve dışlanan geçersiz kayıtları kaydet.
4. Sensör başına katsayı/model ve kullanılan veriyi yeni bir `calibration_id` ile `calibration/calibrations.csv` içine ekle; eski girdilerin üzerine yazma.
5. İlk uyum raporunda modeli eğitildiği aynı etiketli kararlı alan verisine yeniden uygula. Geçerli, sıfırdan farklı PZEM referansına göre bağıl sapma %4 veya altındaysa `OK`; aksi durumda `OUT_OF_RANGE`. Sıfır/geçersiz referans bu yüzde kuralıyla sınıflandırılmaz. Sonuç eğitim verisi içi uyumdur; bağımsız genelleme başarımı değildir.
6. Aynı SSR deneyinin geçişler dahil tam ham SCT akışına eğitilmiş modeli uygula; SCT tahmini ile PZEM zaman serisini aynı zaman ekseninde çiz. Tepki, yerleşme, güncelleme aralığı ve gecikme gözlemlerini ayrı raporla. Bu dinamik grafik, kararlı alanlardaki ±%4 metriğinin yerine geçmez.
6. Sonuçları ve sınırlamaları raporla. PZEM'e uyum, bağımsız mutlak ölçüm doğruluğu anlamına gelmez.

## Kabul ölçütü
Kullanılan veri ve yöntem kaydedilmiş; modelin aynı etiketli eğitim verisindeki uyumu ±%4 PZEM-referans hedefiyle raporlanmış; aynı olayın ham aç-kapa akışında dinamik gözlem grafiği ve zamanlama incelemesi ayrıca üretilmiş; başarısız örnekler ve sınırlamalar açıkça raporlanmış olmalıdır. Bu ilk kabul bağımsız genelleme kanıtı değildir. Uygun veri/kararlı alanlar henüz mevcut değilse görev PLANLANDI kalır. Harici True-RMS cihazı veya üç yük seviyesinde bağımsız referans ölçümü bu proje için varsayılan zorunluluk değildir.

## HEDEF / LOG / SONUÇ
- **HEDEF:** PZEM'e uyumu değerlendiren, verisi ve sürümü izlenebilir model oluşturmak.
- **LOG:** Gerçek kullanılan veriler, ayarlar, yöntem, hesaplama sürümü ve doğrulama ayrımı yazılır; yapılmayan işlemler açıkça belirtilir.
- **SONUÇ:** Kanıt olmadan başarı/kalibrasyon sonucu ilan edilmez.

## Çıktı / dokunulacak dosyalar
- calibration/calibrations.csv
- calibration/PROCEDURE.md
- STATUS.md ve ROADMAP.md (yalnız kabul ölçütleri kanıtla karşılanırsa)
