# Hesaplama-2 — Enerji ve birim dönüşümü

Enerji, gücün zaman boyunca birikimidir. PZEM aktif enerji sayacını modül içinde tutar ve genellikle kWh olarak okutur.

## Birimler

- 1 kW = 1000 W
- 1 kWh = 1000 Wh
- Sabit 100 W yük 10 saat çalışırsa ideal enerji = 100 W × 10 h = 1000 Wh = 1 kWh.

## Harici entegrasyonla çapraz kontrol

Örnekler arasındaki zaman aralığı Δt saat ve ortalama aktif güç P watt ise:
E_kWh ≈ P × Δt / 1000

Bu, bağımsız kontrol hesabıdır. Yük hızlı değişiyorsa her örneğin gücünü ve zaman damgasını kullan; tek güç değerini uzun süre sabit varsayma. PZEM'in kendi enerji sayacı ile harici hesap farklı başlangıç zamanı, örnekleme aralığı ve yuvarlama nedeniyle ayrışabilir.

Enerji sayacını sıfırlama gibi yazma komutları kalıcı sonucu değiştirebilir; önce gerçek donanımda doğrulanmış kütüphane/API ile, açıkça istenen bakım işlemi olarak kullan.