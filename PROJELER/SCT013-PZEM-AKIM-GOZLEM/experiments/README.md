# Deneyler

Her deneyde protocol.md, metadata.yaml ve results.md bulunur. Ham veri varsayılan olarak Git'e eklenmez; yerel raw klasöründe tutulur, küçük sentetik örnekler samples altında saklanır.

- [E00A — Bias trafosu DC noktalarının ADC gözlemi](E00A-raw-waveform-observation/README.md) — SCT bağlı değilken bias-only Vmid alt koşulu analiz edilip kapatıldı; E00A'nın 3,3 V bölücü koşulu ve ham CSV/grafik işleri açık.
- [E00B — SCT bağlı, akımsız hat ADC gözlemi](E00B-sct-connected-no-current/README.md) — Açıklamalı ESPHome firmware'i eklendi ve kullanıcı bildirimiyle derlendi; GPIO34/35 bias, GPIO32/33 SCT. Fiziksel pinout/bağlantı ve cihaz logu bekleniyor.
- [E00 — Bias noktasını ADC ile okuma](E00-bias-adc-baseline/protocol.md) — E00A'dan sonraki temel ADC API karşılaştırma adımı.
- E01 — Yüksüz ofset ve gürültü tabanı
- E02 — Kararlı rezistif yük ve pencere değişkenliği
- E03 — PZEM adım yanıtı / yerleşme süresi
- E04 — PZEM alanlarının değişim zamanları
- E05 — Örnekleme hızı karşılaştırması
- E06 — Yük senaryoları / clipping
- [E07 — SCT kararlılık gözlemi: basamaklı yükler ve örnekleme hızı](E07-sct-stability-step-tests/protocol.md) — önceki basamaklı gözlem planı.
- [E08 — SCT sinyalini tanıma](E08-sct-characterization/README.md) — yüksüz uzun okuma; 100 W ile hız × tur matrisi; 150 W ve 8,5 W LED karşılaştırması; ardından aç-kapa davranışı.

E00A ve E00–E08 deneyleri plan/protokol düzeyindedir; fiziksel ölçüm sonuçları henüz yok. E00A, E00/E01 ve sonraki hız/paketleme çalışmalarından önce yapılacak. İlk geçişte 1 ve 2,5 kS/s karşılaştırması veya çoklu ESP32 eşzamanlaması zorunlu değildir; ilk istatistikler sonraki deneyi yönlendirecek.

- [E09 — ESP-2 düşük akım sensör karşılaştırması](E09-low-current-sensor-comparison/README.md) — PZEM, ACS712-5A ve ZMCT103C-5A için tekil → ikili → üçlü aşamalı test planı. Henüz uygulanmadı.
- [E00F-N02 — Dört ADC kanalı ilk cihaz logu](E00F-unthresholded-overnight-log/E00F-N02-first-device-log.md) — GPIO32/33 SCT ve GPIO34/35 bias kanalları cihazda başlatıldı; ilk kısa log istatistikleri kaydedildi. Sabah HA geçmiş analizi bekleniyor.
