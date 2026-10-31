# T008 — PZEM ve E00F SCT kararlı alan kaydı / etiketleme

- **Durum:** PLANLANDI
- **Öncelik:** AKTİF SONRAKİ GÖREV
- **Bağımlılık:** Kullanıcının çalışan E00F YAML baseline'ı ve mevcut PZEM-004T V3.0 akışı.
- **Hedef:** Aynı yük koşullarında PZEM referans ölçümleri ile E00F SCT Raw AC/akım çıktılarını birlikte kaydetmek; geçerli ve örtüşen kararlı alanları bulmak; PZEM akımıyla SCT kayıtlarını etiketlemek.
- **Kapsam dışı:** Ham 50 Hz dalga aktarımı, her ADC örneğine timestamp, DMA/ADC Continuous, FFT/THD, güç kalitesi analizi ve ct_clamp bileşenini şimdiden değiştirmek.

## Aşamalar
1. **Entity envanteri:** PZEM gerilim/akım/güç/enerji/PF/frekans alanları; E00F SCT GPIO32 RAW, GPIO33 ADC Voltage, SCT Raw AC ve SCT Akım entity'leri. Bias GPIO34/35 yalnız bağlam/izleme içindir. Entity ID ve birimler gerçek HA kurulumundan alınır, tahmin edilmez.
2. **Ortak olay kaydı:** Aynı fiziksel yük/olay altında PZEM ve SCT geçmişi dışa aktarılır. Zaman damgaları, saat dilimi, örnek aralıkları, eksik kayıtlar ve tekrarlar korunur. Yük, açma-kapama saatleri, CT tur sayısı/iletken konumu, firmware ve calibration_id metadata'ya eklenir. Sürekli ADC ham örnekleri istenmez.
3. **Geçersiz veri:** PZEM -1, NaN, timeout, parse hatası ve geçersiz alanlar etiketlemeden çıkarılır. Dışlanan satırlar silinmez; adet ve nedenleri raporlanır.
4. **Kararlılık:** PZEM ve SCT için ayrı pencere ölçütleri geliştirilir. Adaylar pencere içi yayılım, min-max aralığı, eğim ve ardışık pencere tutarlılığıdır. Sabit 3 saniye gecikme/maske kabul edilmez; eşikler gerçek kayıtta test edilir.
5. **Eşleştirme/etiket:** Aynı olay içindeki zaman bakımından örtüşen kararlı alanlar belirlenir. Geçerli PZEM akımı referans etikettir; PZEM mutlak ground truth sayılmaz. Geçiş/yerleşme dinamik raporu ayrı tutulur.
6. **Katsayı:** İlk karşılaştırmada 24.22 değiştirilmeden sapma hesaplanır. Sistematik hata varsa katsayı/model güncellemesi önerilir; her sürüm yeni calibration_id ile eklenir, eskiler korunur.

## Kabul ölçütü
- En az bir yük koşulunda PZEM ve SCT aynı olay altında kaydedilmiş.
- Entity, birim, timestamp, yük/kurulum ve firmware metadata'sı mevcut.
- Geçersiz PZEM okumaları sayılmış ve etiketlemeden çıkarılmış.
- PZEM/SCT kararlılık ölçütleri ayrı açıklanmış ve gerçek kayıtta sınanmış.
- En az bir ortak kararlı alan eşleştirilmiş; PZEM etiketi, SCT değeri ve farkı raporlanmış.
- 24.22 katsayısının sonucu hesaplanmış; değiştirilmişse yeni calibration_id ile gerekçelendirilmiş.
- Kaynak dosya/hash, analiz kodu sürümü, log örneği ve yorum depoda kayıtlı.

## HEDEF / LOG / SONUÇ
- **HEDEF:** PZEM referanslı, kararlı alan temelli, tekrarlanabilir SCT etiketleme döngüsünü kurmak.
- **LOG:** Yalnız gerçek HA export/log ve doğrulanmış entity bilgileri kullanılır; kaynak/ölçüm/yorum ayrımı korunur.
- **SONUÇ:** Henüz yeni ölçüm veya etiketleme yapılmadı. Bu kart plan ve kabul ölçütlerini tanımlar; kod/deney tamamlandı anlamına gelmez.
