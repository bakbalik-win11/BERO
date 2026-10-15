# GRV-005-03 — PZEM/ADC zaman hizalaması

- Tarih: 2026-10-11
- Durum: Açıldı; ölçüm sözleşmesi aşaması.
- Ön koşullar: GRV-005-01 zaman işareti gözlemi kapatıldı; GRV-005-02 ADC özellikleri tanımlandı.
- Amaç: ADC ölçüm penceresi ile PZEM referansının zaman ilişkisini tekrarlanabilir biçimde kaydetmek.
- Kod durumu: Kodlama başlamadı.

## Mevcut kilitli gereksinimler

- Her ADC kanalı için 1000 örnek hedefi korunur.
- Her ADC penceresinde `window_start`, `window_end`, `window_center) bulunur.
- PZEM referansı ayrı `pzem_timestamp) alanına sahiptir.
- `time_delta_ms), PZEM güncelleme anı ile ADC pencere merkezi arasındaki farkı temsil eder.
- ESP32'nin monoton `millis()` tabanı ile SNTP/epoch duvar saati birbirine karıştırılmaz.
- GRV-005-01 logunda PZEM `on_value) işaretinin yaklaşık 5 saniyede bir yenilendiği gözlendi; her başarılı Modbus yanıtıyla bire bir eşleşme bağımsız olarak kanıtlanmış değildir.
- Prototip kendi tüketimini ölçtüğü için gerçek 0 A testi uygulanabilir değil; 0.028 A gözlenen pratik taban değeridir.

## Bu alt görevde karara bağlanacaklar

1. `window_start`, `window_end) ve `window_center) hangi saat tabanında tutulacak? Öneri: aynı ESP32 monoton sayaç tabanında milisaniye işaretleri; ayrıca veri satırına insan tarafından okunabilir duvar saati/epoch zamanı bağlanacaksa eşleme kuralı ayrıca tanımlanır.
2. `pzem_timestamp) duvar saati zamanı mı, monoton zaman mı, yoksa ikisi ayrı alanlar olarak mı temsil edilecek? Öneri: `pzem_timestamp) duvar saati/epoch için; fark hesabı için `pzem_update_millis) gibi ayrı monoton işaret.
3. `time_delta_ms) işaret yönü: öneri `pzem_update_millis - window_center_millis). Pozitif değer PZEM güncelleme işaretinin ADC pencere merkezinden sonra geldiğini ifade eder; negatif değer önce geldiğini ifade eder.
4. PZEM verisinin ADC penceresiyle zaman yakınlığını değerlendirecek kabul aralığı. Bu eşik, PZEM'in gözlenen güncelleme ritmi ve ölçüm hedefi düşünülerek seçilecek; henüz sayı atanmadı.
5. Saat senkronizasyonu yokken duvar saati alanının boş/işaretsiz tutulması; monoton zaman ölçümünün yine de kullanılabilmesi.

## Beklenen çıktı

Alanların tanımı, birimleri, işaret yönü ve saat eşleme yöntemi kilitlenmiş bir zaman sözleşmesi. Ardından GRV-005-04 CSV satır yapısı tanımlanır. Kod, zaman sözleşmesi ve CSV şeması karara bağlanmadan hazırlanmaz.

## Koruma

GRV-002, GRV-004, ALT09, ALT10 ve önceki GRV-005 dosyaları değiştirilmez. Yeni kararlar yeni kayıt olarak tutulur.
