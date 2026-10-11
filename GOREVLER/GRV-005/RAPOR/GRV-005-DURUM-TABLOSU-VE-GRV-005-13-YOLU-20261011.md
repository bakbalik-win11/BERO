# GRV-005 — Durum Tablosu ve Sonraki Mühendislik Kapısı
**Tarih:** 2026-10-11  
**Kaynak:** GRV-005 görev raporları ve kullanıcının paylaştığı cihaz logları  
**İlke:** Durumlar yalnızca raporlanmış test kanıtlarına göre gösterilir.

| Görev | Durum | Kanıt / sınır |
|---|---|---|
| GRV-005-05 Matematik | PASS | Matematik self-test cihaz sonucu kaydedildi. |
| GRV-005-09 Raw ADC | PASS | GPIO33 ham ADC cihaz sonucu kaydedildi. |
| GRV-005-10 Tek Kanal 1000 Örnek | PASS | v03 cihaz logunda 1000 örnek ve pencere süresi görüldü. |
| GRV-005-11 CH0 + BIAS | PASS | 1000 CH0 + 1000 BIAS; `adc_rms_ac=8.459832`. Eşzamanlı örnekleme doğrulanmadı. |
| GRV-005-12 Çok Kanallı Pencere | PASS (ilk doğrulama) | CH0/CH1/CH2/BIAS sayaçları 1000; üç CH kanalında `adc_rms_ac` üretildi. |
| GRV-005-13 PZEM Hizalama | Bekliyor | Tasarım, uygulama ve cihaz kanıtı gerekiyor. |
| GRV-005-14 CSV Üretimi | Bekliyor | Kilitli CSV veri sözleşmesine göre uygulama ve test gerekiyor. |
| GRV-005-15 Python QC | Bekliyor | Kaydedilmiş CSV üzerinde kalite kontrolü gerekiyor. |

## Mevcut teknik değerlendirme
Şu hat için cihaz kanıtı var: ham ADC callback'leri → kanal başına 1000 geçerli örnek → temel istatistikler → BIAS merkezli RMS. Bu, ADC örnekleme/istatistik aşamasının çalıştığına dair kanıttır; akım kalibrasyon doğruluğunu, kanal örneklerinin eşzamanlılığını veya PZEM ile hizalamayı kanıtlamaz.

## Sıradaki kapı: GRV-005-13 — PZEM hizalama
GRV-005-13 için önce zamanlama sözleşmesi ve PZEM sensör güncelleme davranışı doğrulanacak; ardından ayrı bir aday YAML hazırlanacak. CSV henüz bu görevde üretilmeyecek.

Asgari hedef:
- ADC penceresi için `window_start_millis`, `window_end_millis`, `window_center_millis`, `window_duration_ms`.
- PZEM için `pzem_update_millis` işareti.
- `time_delta_ms = pzem_update_millis - window_center_millis` işaretli farkı.
- PZEM `on_value` işaretinin gerçek Modbus yanıt zamanı olmadığı açıkça belgelenmeli.
- Millis taşması ve cihaz yeniden başlatmasıyla ilgili sınırlar belirtilmeli.
- İlk testte PZEM ölçümleriyle ADC penceresi arasında zaman ilişkisi loglanmalı; hizalama eşiği/kalite sınıfı henüz icat edilmemeli.

## Geçmişi koruma
Bu durum tablosu yeni bir özet kaydıdır. GRV-005-01…12 dosyaları ve tarihsel kod sürümleri değiştirilmemiştir.
