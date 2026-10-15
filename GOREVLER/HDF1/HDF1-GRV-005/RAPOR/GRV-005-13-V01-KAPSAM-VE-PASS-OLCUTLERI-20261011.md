# GRV-005-13 v01 — PZEM Hizalama Kapsamı ve PASS Ölçütleri
**Tarih:** 2026-10-11  
**Durum:** Tasarım kararı kaydedildi; firmware uygulaması ve cihaz doğrulaması bekleniyor.

## 1. Hedef
Her ADC ölçüm penceresi sonunda pencere zamanlarını, PZEM güncelleme işaretini ve aralarındaki işaretli zaman farkını kaydetmek; PZEM current, power ve power factor (pf) değerlerini aynı sonuç satırında raporlamak.

## 2. Zorunlu alanlar
- `window_start_millis`
- `window_end_millis`
- `window_center_millis`
- `window_duration_ms`
- `pzem_update_millis`
- `time_delta_ms`
- PZEM current
- PZEM power
- PZEM pf

Zaman farkının sözleşmesi kilitlidir:
```text
time_delta_ms = pzem_update_millis - window_center_millis
```
İşaret korunur; mutlak değere çevrilmez.

## 3. İlk sürümde yapılmayacak sınıflandırmalar
GRV-005-13 v01:
- GOOD/BAD sınıfı üretmez.
- ±500 ms veya başka bir eşik tanımlamaz.
- “eşleşti/eşleşmedi” kararı vermez.
- `pzem_update_millis` değerini gerçek Modbus yanıt zamanı olarak iddia etmez; bu alan ESPHome PZEM sensör güncellemesinin `on_value` işaretidir.

İlk sürüm yalnızca gözlemlenen değerleri kaydeder.

## 4. PASS ölçütü
Aşağıdakilerin tümü cihaz logunda aynı pencere sonucu için üretildiğinde GRV-005-13 v01 PASS sayılır:
1. `window_start_millis`
2. `window_end_millis`
3. `window_center_millis`
4. `window_duration_ms`
5. `pzem_update_millis`
6. `time_delta_ms`, işaretli olarak `pzem_update_millis - window_center_millis` hesabıyla
7. PZEM current
8. PZEM power
9. PZEM pf

Derleme başarısı tek başına PASS değildir; cihaz logu ile kanıt gerekir.

## 5. Sonraki veri hattı
GRV-005-13 PASS sonrasında:
- GRV-005-14 — CSV üretimi
- GRV-005-15 — Python kalite kontrolü
- Daha sonra, yeterli etiketli ve kalite kontrolünden geçmiş veri oluştuğunda lineer regresyon, Random Forest ve XGBoost deneyleri değerlendirilebilir.

PZEM değerleri ilk aşamada referans/hedef veridir. Model hedefi `pzem_current` olarak seçilirse aynı `pzem_current` değerini veya hedefi doğrudan açığa çıkaran türetilmiş alanları giriş özelliklerine koymak veri sızıntısı yaratır.

## 6. Geçmişi koruma
Bu dosya yeni kapsam/karar kaydıdır. GRV-005-01…12 raporları ve kodları değiştirilmemiştir.
