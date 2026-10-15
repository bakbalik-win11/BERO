# GRV-005-14 v06 — çalışan kod notu

**Hedef:** Dört ADC kanalından 1000'er örnek toplamak ve CSV satırlarında aynı PZEM snapshot değerlerini kullanmak.

**Derleme:** Kullanıcı tarafından ESPHome 2026.9.1 ile başarılı olduğu bildirildi. Firmware derleme zamanı: 2026-10-11 14:59:19 +0300.  
**Cihaz:** `esp32d1`, ESP32 rev3.1, 2 core.  
**Pinler:** CH0 GPIO33, CH1 GPIO34, CH2 GPIO35, BIAS GPIO32; PZEM TX GPIO16 / RX GPIO17.  
**Gerçek cihaz logu:** [GRV-005-14-v06-GERCEK-CIHAZ-LOGU-20261011.txt](../LOG/GRV-005-14-v06-GERCEK-CIHAZ-LOGU-20261011.txt)  
**Değerlendirme:** [GRV-005-14-v06-LOG-DEGERLENDIRME-20261011.md](../RAPOR/GRV-005-14-v06-LOG-DEGERLENDIRME-20261011.md)

## Yapılan değişiklik

Rapor başlangıcında PZEM güncelleme zamanı, akım, güç ve PF snapshot değişkenlerine kopyalanır. Dört kanal satırı bu snapshot değişkenlerini kullanır. `time_delta_ms` snapshot zamanından hesaplanır.

## Gerçek log sonucu

- Dört satır mevcut; her birinde 1000 örnek.
- Dört satırda aynı PZEM zaman damgası: 9532 ms.
- Dört satırda aynı delta: 4158 ms.
- PZEM akım/güç/PF alanları tüm satırlarda sırasıyla 0.028 A / 1.700 W / 0.2600.
- `9532 - 5374 = 4158` aritmetiği doğru.
- Log kesitinde önceki 92 ms uyarısı görünmüyor.

## Sınırlamalar

`pzem_update_millis` gerçek Modbus tel yanıt zaman damgası değildir. Median/yüzdelik alanlar hesaplanmıyor; bazı zaman/enerji alanları boş kalıyor. Bu alanlar bu görevde doğrulanmış sayılmaz.

## Sürüm disiplini

v06 ayrı dosya olarak tutulur. v05 ve önceki deney kayıtları değiştirilmez.
