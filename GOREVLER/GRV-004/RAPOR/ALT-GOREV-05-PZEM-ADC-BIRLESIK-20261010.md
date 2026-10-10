# GRV-004 — ALT-GÖREV-05: PZEM + ADC birleşik log

- Tarih: 2026-10-10
- Cihaz adı: `esp32d1` / `ESP32D1`
- Önceki aday: [PZEM + ADC temel sürümü](KOD/esp32d1-4ch-1000-min-max-avg-std-pzem-continuous-20261010.yaml)
- Güncel aday: [PZEM ID'leri ve ADC_TEST birleşik satırı](KOD/esp32d1-4ch-1000-min-max-avg-std-pzem-log-continuous-20261010.yaml)

## Hedef

PZEM akım, güç ve gerilim değerlerini ADC turunun aynı `ADC_TEST` log satırına eklemek; eski kod snapshot'larını korumak.

## Yapılan değişiklik

- PZEM sensörlerine ID verildi: `pzem_current`, `pzem_power`, `pzem_voltage`, `pzem_energy`, `pzem_frequency`, `pzem_power_factor`.
- ADC sonuç satırına `PZEM[A=%.3f P=%.1fW V=%.1f]` alanı eklendi.
- PZEM ilk ölçümünü henüz yayımlamadıysa `has_state()` kontrolüyle NaN kullanılır; logda sayısal olmayan değer görünebilir.
- Dört ADC kanalının MIN/MAX/ORT/STD hesabı ve GPIO pinleri korundu.

## Test planı

1. ESPHome derlemesi.
2. API bağlantısı.
3. PZEM sensörlerinin ilk ölçümleri.
4. Tek `ADC_TEST` satırında PZEM A/W/V ve dört ADC kanalının istatistikleri.
5. PZEM güncellemeleriyle ADC tur satırlarının sürekliliği.

## Durum

Kod adayı oluşturuldu; derleme, cihaz testi ve sabit yük kalibrasyonu henüz doğrulanmadı.
