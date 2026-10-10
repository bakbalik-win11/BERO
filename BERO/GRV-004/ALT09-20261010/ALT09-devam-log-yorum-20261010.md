# ALT09 — Devam Logu ve İlk Yorum
Tarih: 2026-10-10

## Deney zaman çizelgesi
- 22:04 — 8,5 W LED açıldı.
- 22:06 — 8,5 W LED kapatıldı.
- 22:07 — 100 W akkor ampul açıldı.
- 22:08 — 100 W akkor ampul kapatıldı.
- 22:09 — 150 W yük açıldı.
- 22:10 — 150 W yük kapatıldı.

## Kod durumu
- ALT09 YAML değiştirilmedi.
- ESP yeniden başlatılmadı; amaç kesintisiz ham veri akışını korumaktı.
- Akım hesabı, RMS hesabı veya kalibrasyon katsayısı eklenmedi.

## Log dosyası
Kullanıcının bu oturumda yüklediği ham kayıt: `esp32d1-logs (22).txt`.
Bu rapor, ham logun kendisi değildir; deney işaretlerini ve ilk yorumu kaydeder. Ham dosyanın bu GitHub dalına ayrıca yüklenmesi henüz doğrulanmadı.

## İlk gözlemler
- Görünen log bölümünde örnek zaman damgaları çoğunlukla yaklaşık 1 ms aralıklıdır; batch 149 özeti `count=256`, `duration_us=256702`, `min_gap_us=1001`, `max_gap_us=1207`, `mean_gap_us=1005.8` bildiriyor.
- Bazı örneklerde tek kanal belirgin sıçrıyor; örneğin batch 149 index 89'da BIAS=2038, K1=1879, K2=1823, K3=1778. Batch 149 index 129'da BIAS=1889 ve K1=1934; index 169'da BIAS=1959, K1=1775, K2=1903.
- Bu sıçramalar tek başına gerçek akım dalga şekli, analog gürültü, örnekleme etkisi veya bağlantı sorunu olarak sınıflandırılamaz. Daha geniş batch karşılaştırması ve grafik gerekir.
- Önceki kısa incelemede K1/K2 değişkenliğinin bazı bölümlerde arttığı not edilmişti; yük geçişleriyle nedensel bağ henüz doğrulanmadı. Yük işaretleri kullanıcı tarafından yaklaşık saat olarak verildi; cihaz log saatleriyle bire bir eşleşme doğrulanmadı.

## Sonraki adım
Ham dosyayı değiştirmeden Mac/Python ile BIAS, K1, K2, K3 çizgilerini çiz; her kanal için medyan, MAD/robust dağılım, ardışık örnek farkları ve batch zamanlamasını karşılaştır. ALT09 YAML'a, bu analiz tamamlanmadan dokunma.
