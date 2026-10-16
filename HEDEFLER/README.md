# HEDEFLER — Proje BERO

Bu klasör, Proje BERO'daki **ana hedefleri** tanımlar. Ana hedef, birbiriyle ilişkili görevlerin hangi sonuca ulaşmak için yürütüldüğünü belirler.

## Hedef ve görev ilişkisi

- **Hedef (HDF-NNN)**: Ulaşılmak istenen üst düzey sonucu ve tamamlanma ölçütlerini tanımlar.
- **Görev (GRV-NNN)**: Ana hedefe katkı sağlayan, kapsamı ve doğrulama adımları belirli çalışma birimidir.
- Her görev kendi klasöründe, RAPOR/ ve KOD/ alt klasörleriyle yürütülür.
- Ana hedef dosyası, hedefe bağlı görev silsilesini ve her görevin durumunu izler.
- Ana hedef tamamlandığında sonuç raporu, doğrulanmış sonuçları ve açık noktaları toplar. Yeni ana hedefe geçiş, sonuç değerlendirildikten sonra kararlaştırılır.

## Ana hedefler

- [HDF-001 — Ölçüm Karakterini Öğrenmek, Gerçek Dalgayı Yakalamak ve Akımı ESP'de Hesaplamak](HDF-002-PZEM-AMPIRIK-KALIBRASYON/HEDEF.md) — açık. Güncel ilk kazanım, aynı fiziksel akım alanını temsil eden SCT bölgelerini PZEM'in sabit (I, V, PF) referans alanları ve deney bağlamıyla etiketlenmiş veri kümesine dönüştürmektir. Ardından Python ile etiketli veriden optimum paket adayı seçilecek, paket testleri yapılacak, F(x) hesaplanıp hata analiz edilecek. Hedefin ilerleyen aşamaları güvenli arşiv, bağımsız doğrulama ve onaylı modelin tek saha ESP'sinde çalıştırılmasını kapsar. Bunlar planlanan iş akışıdır; gerçekleşmiş test veya doğruluk sonucu iddiası değildir.

Ana hedef klasörleri HDF-NNN-KISA-AD biçiminde adlandırılır.

