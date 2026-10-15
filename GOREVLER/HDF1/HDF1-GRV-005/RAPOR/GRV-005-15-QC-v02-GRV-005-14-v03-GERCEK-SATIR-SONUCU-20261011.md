# PROJE BERO — GRV-005-15 QC v02 Kurallarıyla GRV-005-14 v03 Gerçek Satır Testi

**Tarih:** 2026-10-11  
**Kaynak:** Kullanıcının paylaştığı ESPHome 2026.9.1 gerçek cihaz logu  
**Ölçüm kimliği:** `esp32d1_245_001`  
**İncelenen kanallar:** CH0-1T, CH1-2T, CH2-3T, BIAS

## Yöntem ve önemli sınırlama

Logdan alınan dört gerçek veri satırı, GRV-005-15 Python QC v02'de tanımlı 14 kontrol kuralının eşdeğer mantığıyla bir Python kontrolünde değerlendirildi. Bu rapor, depodaki QC v02 betiğinin dosyaya karşı doğrudan CLI çalıştırıldığı iddiasında bulunmaz.

**Başlık uyarısı:** Kullanıcının paylaştığı logdaki başlık satırı `pz` bölümünde kesiliyor. Kontrol CSV'sinde beklenen kanonik 41 alanlı başlık kullanıldı. Bu nedenle başlık eşleşmesi kontrol CSV'si için PASS olsa da, gerçek cihaz başlığının eksiksiz loglandığını kanıtlamaz. Dört veri satırı kullanıcı logundan alındı ve ayrı ayrı 41 alan olarak sayıldı.

## Sonuç

- QC v02'nin 14 kontrol kuralının eşdeğer mantığıyla kontrol CSV'si: **14/14 PASS**.
- Gerçek cihazdan alınan dört satırın alan sayısı: **4/4 satırda 41 alan**.
- Kanalların her biri bir kez mevcut: **PASS**.
- Tüm satırlarda ortak ve boş olmayan measurement_id: `esp32d1_245_001` — **PASS**.
- Her kanalda sample_count=1000: **PASS**.
- Pencere süresi, merkezi ve time_delta aritmetiği: **PASS**.
- Sayısal türler ve boş bırakılabilen alanlar: **PASS**.
- CH0/CH1/CH2 adc_rms_raw dolu: **PASS**.
- Başında/sonunda boşluk: **yok**.
- ADC min/max/range bağıntısı: **PASS**.
- PZEM current/power/PF alanları dolu: **PASS**.
- BIAS satırının kendi ADC özeti ile bias_* alanları: **PASS**.
- Fazladan/taşan CSV sütunu: **yok**.

## Fiziksel ölçüm veya zamanlama hakkında hüküm değildir

Bu sonuç CSV yapısı ve alan tutarlılığı testidir; akım ölçümünün fiziksel doğruluğunu kanıtlamaz.

Logda `adc.sensor took a long time for an operation (92 ms), max is 50 ms` uyarısı bulunuyor. Örnek sayısı 1000'e ulaşmış olsa da, 10 ms aralıklarla düzenli örnekleme veya kanallar arasında eşzamanlılık bu QC tarafından kanıtlanmaz.

PZEM için kaydedilen `pzem_update_millis` değeri, sensörün `on_value` anında alınmış yazılım zamanıdır; gerçek Modbus paketinin tam zaman damgası olarak kabul edilmemelidir.

## Durum

**GRV-005-14 v03 CSV satır alan kontrolü: PASS.**  
**QC v02 kurallarıyla eşdeğer kontrol: 14/14 PASS.**  
**Depodaki QC v02 betiğinin doğrudan çalıştırılması: bu adımda yapılmadı.**  
**Gerçek cihaz başlığının eksiksizliği: bu log dökümünden doğrulanamadı.**  
**ADC zamanlama uyarısının incelenmesi: açık iş.**

## Sonraki adım

Başlık satırını ayrı bir log mesajında daha kısa parçalara bölerek veya cihazın tam CSV dosyasını dışarı alarak doğrula. Ardından ADC'nin 92 ms uyarısını ayrı bir zamanlama deneyi olarak incele. Önceki kod ve deney kayıtları değiştirilmemiştir.
