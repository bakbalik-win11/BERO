# GRV-005-05 — Matematik self-test v01 derleme kaydı

- Tarih: 2026-10-11
- Durum: **Derleme başarılı (kullanıcı bildirimi). Cihaza yüklenmedi.**
- Kapsam: ADC istatistik kodlamasına geçmeden önce temel matematik işlemlerinin küçük ve bağımsız bir self-test ile kontrol edilmesi.
- Önceki görevler ve deneyler değiştirilmemiştir.

## Doğrulama sınırı

Kullanıcı, GRV-005-05 matematik self-test v01 derlemesinin başarılı olduğunu bildirdi. Bu, derleyicinin ilgili yapılandırmayı derleyebildiğini doğrular; testin ESP32 üzerinde çalıştığını veya logda PASS çıktısı verdiğini doğrulamaz. Firmware cihaza yüklenmemiştir.

## Beklenen matematik sonuçları

Test girdisi: x = {1, 2, 3, 4}; bias_mean = 2.5.

| Ölçüt | Beklenen değer |
|---|---:|
| mean | 2.5 |
| Örnek standart sapması (N−1) | 1.29099445 |
| Ham RMS | 2.73861279 |
| Bias çıkarılmış RMS | 1.11803399 |
| Geçerli ham değeri sıfır olan örnek sayısı | 0 |

Bu değerler, testte kullanılan tanımlar için beklenen referans değerlerdir; henüz cihaz çıktısıyla karşılaştırılmamıştır.

## Sonraki adım

1. Bu kaydı derleme sonucu olarak sakla.
2. CSV şemasındaki açık kararları (özellikle kanal kimliği ve enerji birimi) uygulama öncesinde gözden geçirip kilitle.
3. Sonrasında ayrı bir uygulama sürümünde istatistik hesaplamalarını ve zaman alanlarını birleştir; cihaza yükleme için ayrıca açık onay ve ayrı doğrulama adımı uygula.

## Değişmezler

- `esp32d1` cihaz adı değiştirilmez.
- ALT09, ALT10, GRV-002, GRV-004 ve önceki görev kayıtları üzerine yazılmaz.
- Derleme başarısı, cihazda çalışma başarısı olarak sunulmaz.
