# T006 — SCT katsayısı/model değerlendirmesi

- **Durum:** PLANLANDI
- **Faz:** PZEM–SCT kararlı alan etiketleme ve sürekli iyileştirme
- **Bağımlılık:** T008 — en az bir geçerli PZEM/SCT ortak kararlı alan kaydı ve etiketleme
- **Hedef:** PZEM referans akışına göre mevcut SCT katsayısını değerlendirmek; veri desteklerse katsayı/modeli yeni calibration_id ile iyileştirmek.

## Yapılacak
1. T008 kapsamında eşleştirilmiş, geçerli PZEM/SCT kararlı alanlarını kullan.
2. Önce mevcut 24.22 katsayısını değiştirmeden farkı ve bağıl sapmayı hesapla.
3. Sapmayı yük/akım seviyesi, SCT Raw AC, pencere değişkenliği ve kayıt koşuluna göre incele.
4. Sistematik ve tekrarlanabilir hata varsa en basit yeterli katsayı/model güncellemesini değerlendir.
5. Her yeni katsayı/model için yeni calibration_id, veri hash'i, firmware/config sürümü, yöntem ve tarih kaydet. Önceki kayıtları silme.
6. Eğitim verisi içi uyum ile farklı olay/yükte ayrı doğrulama sonuçlarını ayrı raporla.
7. Geçiş dinamikleri ayrı tutulur; kararlı etiketli eğitim alanlarıyla karıştırılmaz.
8. PZEM'e uyum, bağımsız mutlak doğruluk veya kusursuz ground truth iddiası değildir.

## Kabul ölçütü
En az bir geçerli ortak kararlı alan veri setiyle 24.22 katsayısının sonucu hesaplanmış; gerekiyorsa yeni katsayı/model gerekçelendirilmiş; veri kökeni, calibration_id, hata ölçütleri ve sınırlamalar raporlanmış olmalıdır. Ayrı doğrulama yapılmadıysa açıkça belirtilir. Uygun veri yoksa görev PLANLANDI kalır.

## HEDEF / LOG / SONUÇ
- **HEDEF:** Yeni veriler geldikçe izlenebilir ve sürümlü katsayı/model iyileştirmesi yapmak.
- **LOG:** Gerçek PZEM/SCT eşleşmeleri, dışlanan kayıtlar, hesaplama sürümü ve örnek sonuçlar kaydedilir.
- **SONUÇ:** Bu kart modelin eğitildiği veya ±%4 başarımın BERO içinde yeniden üretildiği anlamına gelmez.
