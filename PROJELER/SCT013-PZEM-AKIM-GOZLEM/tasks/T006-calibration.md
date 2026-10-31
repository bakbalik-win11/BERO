# T006 — SCT katsayısı/model değerlendirmesi

- **Durum:** BEKLEMEDE
- **Faz:** Faz 2 — Bulunan kodu PZEM ile eğitmek
- **Bağımlılık:** T008 kapsamında üretilmiş geçerli PZEM/SCT ortak kararlı alan eşleşmeleri ve etiketli veri.
- **Hedef:** Önce mevcut K=24.22 katsayısını yeni etiketli kararlı alanlarda değerlendirmek; yalnız veri gerekçelendirirse katsayı/modeli iyileştirmek.

## Yapılacaklar

1. T008'in eşleştirilmiş ve geçerli PZEM/SCT kararlı alanlarını kullan.
2. İlk karşılaştırmada K=24.22 değerini değiştirmeden sapmayı hesapla.
3. Sapmayı yük/akım seviyesi, Raw AC, pencere değişkenliği ve kayıt koşuluna göre incele.
4. Sistematik ve tekrarlanabilir hata görülürse en basit yeterli katsayı/model değişikliğini değerlendir.
5. Her yeni sürüme yeni calibration_id, veri hash'i, firmware/config sürümü, yöntem ve tarih ekle; eski sürümleri koru.
6. Eğitim verisi uyumunu, ayrı olay/yük doğrulamasından ayrı raporla.
7. Geçiş dinamiklerini kararlı etiketli eğitim alanlarıyla karıştırma.

## Kabul ölçütü

En az bir gerçek ortak kararlı alan veri setinde K=24.22 sonucu hesaplanmış; değişiklik gerekiyorsa gerekçelendirilmiş ve yeni calibration_id ile kaydedilmiş olmalı. Veri kökeni, yöntem, hata ölçütleri ve sınırlamalar raporlanmalı. Ayrı doğrulama yapılmadıysa açıkça belirtilmeli.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Etiketli PZEM/SCT verisi geldikçe mevcut katsayıyı ve gerekirse modeli izlenebilir biçimde iyileştirmek.
- **LOG:** T008 etiketli veri henüz yok; yeni katsayı/model hesaplanmadı.
- **SONUÇ:** T006 BEKLEMEDE. K=24.22 başlangıç baseline'ı olarak korunuyor.
