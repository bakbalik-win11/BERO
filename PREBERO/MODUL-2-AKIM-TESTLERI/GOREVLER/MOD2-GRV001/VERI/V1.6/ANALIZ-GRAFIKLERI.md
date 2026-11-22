# V1.6 — Kalibrasyon Fonksiyonu ve Doğrusallık Grafikleri

**Tarih:** 2026-11-22  
**Görev:** MOD2-GRV001  
**Veri kaynağı:** [kalibre-yeni-formul-karma-2026-11-22.csv](./kalibre-yeni-formul-karma-2026-11-22.csv)  
**Grafik:** [v1.6-kalibrasyon-ve-dogrusallik.jpg](./v1.6-kalibrasyon-ve-dogrusallik.jpg)

## Grafiklerin kapsamı

Bu görsel iki paneli birlikte içerir:

1. **K(x) kalibrasyon fonksiyonu:** Ham taban akımına bağlı etkin K katsayısı. X ekseni logaritmiktir.
2. **PZEM referansı – BERO doğrusal karşılaştırması:** 22 ölçüm kademesinde PZEM referans akımı ile BERO akım sensörü çıktısı. Grafikte ideal 1:1 doğrusu ve ±%4 hedef bandı gösterilir.

## Grafikte kullanılan fonksiyon ve seviyeler

Grafikte verilen fonksiyon:

```text
K(x) = 26.89 + 5.39 * exp(-x / 0.882)
```

- İlk baz katsayı: **K = 27.59**
- Yüksek akım asimptotu: **K = 26.89**
- Düşük PF örnek noktası: **PF = 0.76**, grafikte **20.4 W** olarak işaretlenmiş.
- İdeal PF ölçüm noktaları: **PF ≥ 0.90** olarak işaretlenmiş.

## Okuma ve yorum sınırları

- Sağ panel, ölçüm noktalarının PZEM referansına göre dağılımını ve ±%4 hedef bandını görsel olarak karşılaştırır.
- Grafikteki 22 kademe bilgisi görsel açıklamasından alınmıştır; bu rapor yeni bir istatistik hesabı veya bağımsız doğrulama iddiası taşımaz.
- PZEM bu çalışmada referans cihazdır; mutlak/izlenebilir gerçek değer (ground truth) olarak kabul edilmez.
- Düşük PF örneği ayrı işaretlenmiştir. Bu nokta, ideal PF grubuyla aynı koşullarda değerlendirilmemelidir.
- Bu grafik, ham CSV'nin yerine geçmez. Yeniden analiz için CSV esas alınmalıdır.
