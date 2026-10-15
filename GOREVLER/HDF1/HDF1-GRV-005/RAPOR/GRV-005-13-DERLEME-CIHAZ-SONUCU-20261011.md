# GRV-005-13 v01 — Derleme ve Cihaz Sonuç Raporu
Tarih: 2026-10-11
Durum: **Cihaz logunda temel PASS ölçütleri gözlendi; performans uyarısı ve zaman yorumu not edildi.**

## Hedef
Dört ADC girişinin 1000 örnekli penceresini zaman alanlarıyla raporlamak ve PZEM current, power, PF referanslarını aynı kanal sonuç satırında göstermek.

## Test ortamı
- ESP32D1OTA / `esp32d1`
- ESPHome 2026.9.1
- Derleme: 2026-10-11 11:18:50 +0300
- ESP32 rev3.1, iki çekirdek
- Kullanıcının bildirdiği sonuç: kod derlendi ve cihaz logu alındı.

## Sonuçlar

| Kanal | Örnek | Süre (ms) | Ortalama | Standart sapma | AC RMS | PZEM akım (A) | Güç (W) | PF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CH0-1T | 1000 | 10028 | 1863.882000 | 19.502831 | 19.502557 | 0.028 | 1.700 | 0.2700 |
| CH1-2T | 1000 | 10028 | 1861.355000 | 13.565286 | 13.916221 | 0.028 | 1.700 | 0.2700 |
| CH2-3T | 1000 | 10028 | 1855.409000 | 11.211129 | 14.423186 | 0.028 | 1.700 | 0.2700 |
| BIAS | 1000 | 10028 | 1864.490000 | 15.453502 | — | 0.028 | 1.700 | 0.2700 |

Ortak zaman alanları:
- `window_start_millis=235`
- `window_end_millis=10263`
- `window_center_millis=5249`
- `window_duration_ms=10028`
- `pzem_update_millis=9482`
- `time_delta_ms=4233`

## Değerlendirme
1. Dört sonuç satırında da `sample_count=1000` gözlendi.
2. Her sonuç satırında pencere başlangıcı, bitişi, merkezi, süresi ve PZEM zaman işareti yer aldı.
3. `time_delta_ms=4233` işaretli farkı koruyor. Bu değer, mevcut PZEM güncelleme işaretinin pencere merkezinden 4233 ms sonra olduğunu gösterir; tek başına gerçek Modbus yanıt zamanını kanıtlamaz.
4. Dört satırda da PZEM current, power ve PF aynı satırda raporlandı.
5. `invalid_count=NOT_TRACKED` doğru biçimde korunmuş; `zero_count=0` raporlanmıştır.
6. ESPHome `adc.sensor took a long time for an operation (116 ms), max is 50 ms` uyarısı oluştu. Örnekleme callback'lerinin çalışma süresi/periyodu bir sonraki aşamada incelenmelidir.
7. ESP32 rev3.1 için `minimum_chip_revision: "3.1"` ve `sram1_as_iram: true` ayarları derleyici tarafından önerildi. Bunlar bu testte zorunlu hata değil, optimizasyon önerileridir.

## PASS kapsamı
**Sınırlı PASS:** Dört kanal için 1000 örnek, ortak pencere zaman alanları ve PZEM current/power/PF'nin aynı sonuç satırında raporlanması cihaz logunda doğrulandı.

## PASS olmayan / henüz kanıtlanmayanlar
- `pzem_update_millis` gerçek Modbus yanıt zamanı değildir; current sensörünün `on_value` işaretidir.
- Current, power ve PF'nin aynı fiziksel Modbus yanıtına ait olduğu kanıtlanmadı.
- ADC kanalları eşzamanlı örneklenmiş değildir.
- ADC sürücü hata sayacı yoktur; `invalid_count` izlenmiyor.
- `time_delta_ms` için GOOD/BAD veya eşik kararı verilmedi.
- Sürekli/tekrarlanan pencere davranışı doğrulanmadı; bu çalışma tek pencere çıktısıdır.
- CSV dışa aktarımı ve Python kalite kontrolü yapılmadı.

## Sonraki adım
GRV-005-14: GRV-005-13 zaman alanları ve PZEM referanslarını CSV şemasına eklemek; her satırın bir kanal/pencere ölçümünü temsil etmesi ve mevcut kilitli CSV v03 sözleşmesini koruması.
