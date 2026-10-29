# Deneyler

Her deneyde protocol.md, metadata.yaml ve results.md bulunur. Ham veri varsayılan olarak Git'e eklenmez; yerel raw klasöründe tutulur, küçük sentetik örnekler samples altında saklanır.

- [E00A — Ham sinyal gözlemi ve örnekleme hızı](E00A-raw-waveform-observation/README.md) — paketleme öncesi bias-only, SCT yüksüz ve 100 W ampul ham kayıtları; PC'de yavaş oynatma, dalga grafiği ve temel istatistikler.
- E01 — Yüksüz ofset ve gürültü tabanı
- E02 — Kararlı rezistif yük ve pencere değişkenliği
- E03 — PZEM adım yanıtı / yerleşme süresi
- E04 — PZEM alanlarının değişim zamanları
- E05 — Örnekleme hızı karşılaştırması
- E06 — Yük senaryoları / clipping
- [E07 — SCT kararlılık gözlemi: basamaklı yükler ve örnekleme hızı](E07-sct-stability-step-tests/protocol.md) — önceki basamaklı gözlem planı.
- [E08 — SCT sinyalini tanıma](E08-sct-characterization/README.md) — yüksüz uzun okuma; 100 W ile hız × tur matrisi; 150 W ve 8,5 W LED karşılaştırması; ardından aç-kapa davranışı.

E00A ve E00–E08 deneyleri plan/protokol düzeyindedir; fiziksel ölçüm sonuçları henüz yok. E00A, E00/E01 ve sonraki hız/paketleme çalışmalarından önce yapılacak.
