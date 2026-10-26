# T005 — E01 gürültü tabanı

- **Durum:** PLANLANDI
- **Faz:** 1.2
- **Bağımlılık:** T004
- **Hedef:** Önceden yazılmış bir protokolle yüksüz ADC ofsetini ve gürültü tabanını ölçmek.

## Yapılacak
1. experiments/E01-noise-floor/protocol.md içindeki düzenek, örnekleme, süre ve kabul ölçütlerini gerçek donanıma göre doldur.
2. Deneyden önce güç/bağlantı güvenliğini ve kalibrasyon gereksinimini kontrol et.
3. Deneyi protokole göre yap; mümkün değilse sonuç üretme ve engeli kaydet.
4. metadata.yaml içinde firmware/donanım kimliklerini ve yapılandırmayı yaz.
5. results.md içinde ölçülen ofset, gürültü metriği, veri yolu ve gözlemleri yaz; ham veriye bağ ver.
6. Gürültü tabanından çıkarılabilecek düşük akım sınırını hipotez olarak ayır; tek deneyle genelleme yapma.

## Kabul ölçütü
Protokol, metadata, ham/veri çıktısı ve sonuç birbiriyle bağlanabilir; ölçülmeyen sonuç yoktur. Sonuçların yokluğu açıkça YAPILMADI olarak kalır.

## Çıktı / dokunulacak dosyalar
- experiments/E01-noise-floor/
- İlgili veri ve doğrulama kayıtları
