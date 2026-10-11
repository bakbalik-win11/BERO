# HEDEFLER — Proje BERO

Bu klasör, Proje BERO'daki **ana hedefleri** tanımlar. Ana hedef, birbiriyle ilişkili görevlerin hangi sonuca ulaşmak için yürütüldüğünü belirler.

## Hedef ve görev ilişkisi

- **Hedef (HDF-NNN)**: Ulaşılmak istenen üst düzey sonucu ve tamamlanma ölçütlerini tanımlar.
- **Görev (GRV-NNN)**: Ana hedefe katkı sağlayan, kapsamı ve doğrulama adımları belirli çalışma birimidir.
- Her görev kendi klasöründe, RAPOR/ ve KOD/ alt klasörleriyle yürütülür.
- Ana hedef dosyası, hedefe bağlı görev silsilesini ve her görevin durumunu izler.
- Ana hedef tamamlandığında sonuç raporu, doğrulanmış sonuçları ve açık noktaları toplar. Yeni ana hedefe geçiş, sonuç değerlendirildikten sonra kararlaştırılır.

## Ana hedefler

- [HDF-001 — Akımı Okuma](HDF-001-AKIMI-OKUMA/HEDEF.md) — tarihsel temel olarak korunur; eski kod ve deney kayıtları silinmez.
- [HDF-002 — Ölçüm Karakterini Öğrenmek ve Gerçek Hayatı Yakalamak](HDF-002-PZEM-AMPIRIK-KALIBRASYON/HEDEF.md) — açık; önce ham veride aynı fiziksel olayı temsil eden bölgeleri PZEM referansıyla eşleştirip Python ile ilişkiyi öğrenmek, daha sonra ölçüm hızı ve paketlemeyi seçmek.

Ana hedef klasörleri HDF-NNN-KISA-AD biçiminde adlandırılır.

Kayıtların korunması için [Kayıt, Sürümleme ve Süreklilik Politikası](../KAYIT_VE_SUREKLILIK.md) uygulanır.
