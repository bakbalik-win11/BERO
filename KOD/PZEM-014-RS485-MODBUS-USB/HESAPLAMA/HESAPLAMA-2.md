# Hesaplama-2 — Enerji ve birim dönüşümü

Enerji zaman boyunca aktif gücün birikimidir.
- 1 kW = 1000 W
- 1 kWh = 1000 Wh
- Sabit 100 W yük 10 saat çalışırsa enerji 1 kWh olur.

Örnekler arasında geçen süre Δt saat ve ortalama aktif güç P watt ise:
E_kWh ≈ P × Δt / 1000

Yük değişkense her örneğin gücünü ve zaman damgasını kullan. PZEM sayacıyla harici entegrasyon örnekleme, başlangıç sayacı ve yuvarlama nedeniyle farklılaşabilir. Enerji sıfırlama komutu test kodunda otomatik kullanılmamalıdır.