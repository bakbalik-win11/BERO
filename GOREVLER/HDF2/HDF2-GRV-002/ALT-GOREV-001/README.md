# Hedef 2 / GRV-002 — Alt Görev 1
# Tek ESP ile sinyali en yüksek güvenilir hızda yakalama ve çizme

**Görev kimliği:** HDF2-GRV-002 / ALT-GOREV-001  
**Durum:** AÇIK — test edilmedi  
**Öncelik:** İlk teknik adım  
**Bağlı ana görev:** [HDF2-GRV-002 Veri Motoru Ön Test Planı](../RAPOR/HDF2-GRV-002-00-ON-TEST-PLANI.md)

## 1. Amaç

Önce tek bir ESP32-WROOM ile SCT ve BIAS sinyallerinin ham örneklerini mümkün olan en yüksek **güvenilir ve ölçülmüş** hızda yakalamak, Mac'e aktarmak ve dalga biçimlerini çizmek. Üç ESP'li 1T/2T/4T düzenine geçmeden önce tek ESP'deki veri yakalama zinciri doğrulanacaktır.

## 2. Donanım ve sınırlar

- ESP: ESP32-WROOM; ilk deneyde tek cihaz.
- ADC: ESP'nin dahili ADC'si ve uygun sürekli örnekleme/DMA yöntemi.
- Giriş adayları: GPIO34 / ADC1_CH6 (SCT), GPIO35 / ADC1_CH7 (BIAS); fiziksel kablo bağlantısı test öncesi doğrulanacak.
- MCP3208 kullanılmayacak.
- İlk hedef ham SCT ve BIAS verisi; bu görevde RMS, filtreleme, BIAS çıkarma, kalibrasyon veya akım hesabı yapılmayacak.
- Örnekleme sırasında seri/USB çıktısı örnekleme yolunu bloke etmemeli; aktarım ve tampon sahipliği kayıpları görünür olmalı.

## 3. İş planı

1. Mevcut ADC sürekli örnekleme API'sini ve ESP32-WROOM/ESPHome-Arduino hedef uyumunu incele.
2. Basit bir referans kayıtla cihazdan ham örnek alındığını doğrula.
3. Örnekleme hızını basamaklı artır. Her adımda gerçek hız, örnek aralığı, örnek sayısı, sıra, frame bütünlüğü ve taşma sayaçlarını kaydet.
4. Ham veriyi Mac'e aktar; kaynak kaydı değiştirmeden CSV olarak sakla.
5. Ham SCT ve BIAS dalgalarını zaman eksenine karşı çiz; grafik başlığına gerçek ölçülen örnekleme hızını yaz.
6. En yüksek hızın kayıpsız ve kararlı olduğu kanıtlanamazsa, dalgayı güvenilir gösteren daha düşük hızı seç.
7. Kod, derleme çıktısı, seri log, CSV ve grafik dosyalarını aynı test kaydı altında tut.

## 4. Başarı ölçütleri

- [ ] ESP32-WROOM için derleme başarılı ve kullanılan kod sürümü kaydedilmiş.
- [ ] Gerçek cihazdan ham kayıt alınmış.
- [ ] Gerçek örnekleme hızı bağımsız/uygun zamanlama kanıtıyla ölçülmüş; yalnızca ayar değerine dayanılmamış.
- [ ] İstenen örnek sayısı ve sıra korunmuş.
- [ ] DMA/kuyruk/frame overflow veya örnek kaybı yok; varsa ölçülmüş ve açıklanmış.
- [ ] Ham kayıt Mac'te yeniden okunmuş ve bütünlük kontrolünden geçmiş.
- [ ] SCT ve BIAS ham dalgaları çizilmiş.
- [ ] Sonuç raporu PASS/FAIL ve kanıt dosyalarıyla yazılmış.

## 5. Önemli teknik uyarı

DMA callback'lerinin başlangıç ve bitiş zamanları, ilk ve son ADC örneklerinin gerçek zaman damgalarıyla aynı değildir. Bu nedenle callback süresi tek başına örnekleme aralığını kanıtlamaz. “En yüksek hız” ancak gerçek örnekleme ve kayıp kontrolleriyle belirlenebilir.

## 6. Sonraki aşama

Bu alt görev tamamlanıp tek ESP zinciri doğrulandıktan sonra ayrı bir alt görev açılır: üç ESP ile 1T, 2T ve 4T ölçüm yapısının kurulması ve eşzamanlama testleri. Bu görev çoklu ESP kurulumunu kapsamına almaz.

**Şu anki devam noktası:** Tek ESP için ADC yakalama yolunu seçmek ve ilk ham kaydı almak. Derleme veya fiziksel test sonucu henüz yok.
