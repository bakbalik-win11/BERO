# ADR-003: PZEM yavaş referans akışı olarak kullanılacak

- **Durum:** Kabul edildi.
- **Karar:** Yaklaşık 1 s başlangıç sorgu aralığı; istek/yanıt zamanı, status ve tekrarlanan değer sayısı saklanır.
- **Bağlam:** PZEM hazır ölçüm register'ları verir; ham dalga biçimi vermez. İç ölçüm penceresi bu modülde doğrulanmadı.
- **Gerekçe:** Yanıt zamanını SCT penceresiyle aynı fiziksel anda alınmış değer gibi varsaymamak.
- **Risk:** Sorgu aralığını artırmak yeni bilgi sağlamayabilir; varyantlar değişebilir.
- **Gözden geçirme:** E03 ve E04.
