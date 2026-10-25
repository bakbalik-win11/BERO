# ADR-001: SCT örnekleme hızı

- **Durum:** İlk test ayarı olarak kabul edildi; deney onayı bekliyor.
- **Karar:** 2 kS/s ile başla; 1 ve 2,5 kS/s aynı yüklerde karşılaştır.
- **Bağlam:** 50 Hz'de 2 kS/s nominal 40 örnek/çevrim sağlar. Açık kaynak uygulamalar daha yüksek hızlar kullanır; evrensel minimum yoktur.
- **Gerekçe:** Amaç RMS, yük değişimi ve PZEM korelasyonudur; harmonik analiz değil.
- **Risk:** Kısa darbelerin tepesi yine kaçırılabilir.
- **Gözden geçirme:** E05 ve E06 tamamlandığında.
