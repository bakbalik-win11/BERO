# Mimari karar kayıtları (ADR)

- [ADR-001 — Örnekleme hızı](ADR-001-sample-rate.md)
- [ADR-002 — 200 ms pencere](ADR-002-window-200ms.md)
- [ADR-003 — PZEM yavaş referans akışı](ADR-003-pzem-as-slow-label.md)
- [ADR-004 — Sürekli ham veri yok](ADR-004-no-continuous-raw.md)
- [ADR-005 — Geçersiz okumalar](ADR-005-invalid-readings.md)
- [ADR-006 — SSR olay penceresi etiketleme](ADR-006-ssr-event-window-labeling.md)
- [ADR-007 — Bias orta noktası kondansatörü](ADR-007-bias-midpoint-capacitor.md)

ADR durumları kararın başlangıç niteliğini korur. Deneyle doğrulanmamış kararları ölçüm sonucu gibi göstermeyin.

- [ADR-008 — İki ölçüm düğümü ve aşamalı sensör testleri](ADR-008-two-node-staged-sensor-tests.md)

- [ADR-009 — ±%4 hedefi ve ham edinim ara işlerinin kapatılması](ADR-009-measurement-target-met-close-raw-capture.md)

- [ADR-010 — PZEM referanslı kararlı alan etiketleme ve sürekli öğrenme](ADR-010-pzem-stable-window-learning-focus.md)

- [ADR-022 — Paket işaretleriyle akış bölümleme ve eğitim verisi oluşturma](ADR-022-packet-marker-segmented-training-streams.md)

## ADR numaralandırma notu

Depoda tarihsel kayıtlar korunurken iki numara birden fazla dosya adına verilmiştir:
- ADR-017: ADR-017-module2-single-common-bias.md ve ADR-017-module2-single-sct-channel.md
- ADR-018: ADR-018-module2-four-adc-long-log.md ve ADR-018-module2-sequential-sct-window-test.md

Dosya slug'ları farklıdır ve bağlantılar bu dosya adları üzerinden çalışır. Geçmiş referansları bozmamak için bu oturumda dosyalar yeniden adlandırılmadı. Yeni kararlar ADR-024 ve sonrasından devam etmelidir; mevcut tarihsel numaralar tek başına benzersiz kimlik değildir.

- [ADR-023 — Olay kimliğinde TIME alanının kaldırılması](ADR-023-event-identity-without-time.md)
- [ADR-024 — Python tarafında ON/OFF paket bütünlüğü doğrulaması](ADR-024-python-packet-completeness-validation.md)

- [ADR-031 — CH1 yüksüz kapalı alan eşiği](ADR-031-ch1-idle-closed-area-threshold.md)
