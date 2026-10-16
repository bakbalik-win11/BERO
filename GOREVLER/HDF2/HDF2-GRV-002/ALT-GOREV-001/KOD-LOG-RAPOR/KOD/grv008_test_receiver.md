# GRV-008.2 — Mac Mini Python alıcısı ve ilk dalga grafiği

**Kaynak:** Kullanıcının önceki çalışma kaydındaki mevcut alıcı betiği. Yeni yazılmış kod değildir.

- Bağımlılıklar: `pyserial`, `numpy`, `matplotlib`
- Seri port: `SERIAL_PORT` gerçek Mac Mini portuna göre ayarlanmalı.
- Beklenen kayıt: 100 frame; CSV ham örnek kaydı; ilk beş frame grafiği.
- Durum: **ADAY — gerçek ESP akışıyla doğrulanmadı**.

## Önemli sınır

Kodun hesapladığı frame süresi, DMA callback zamanları arasındaki süreye dayanır. Her ADC örneğinin tam 100 µs aralıkla alındığını kanıtlamaz. Grafik x-ekseni de doğrulanmış zaman değil, örnek indeksidir.
