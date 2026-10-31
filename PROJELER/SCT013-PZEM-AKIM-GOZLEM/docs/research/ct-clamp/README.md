# ESPHome ct_clamp rapor arşivi

Bu klasör, BERO'nun ct_clamp ölçüm zinciri hakkındaki iki ayrı raporu saklar.

## 1. Kullanıcının sağladığı rapor

- [Kullanıcı raporu — Markdown metin aktarımı](source/2026-10-31-user-supplied-ct-clamp-report.md)
- Kaynak: kullanıcı tarafından yüklenen dört sayfalık DOCX.
- Depoda metin aktarımı Markdown biçiminde tutulur; raporun varsayımları, simülasyon sonuçları ve kendi çıkarım notları kaynak metindeki gibi korunmuştur.
- Kaynak DOCX: 9.547 bayt; SHA-256 `cfb2d76f64a93efd8d80e0005c6e80b974d9086e77b72f61542898aa03f88a05`.

## 2. Bağımsız teknik inceleme

- [Bağımsız teknik inceleme](../ct-clamp/2026-10-31-independent-technical-review.md)
- Biçim: Markdown.
- Dayanak: ESPHome 2026.10.1 kaynak kodu, Espressif/CT dokümanları ve BERO Log 63.
- Kaynak koddan doğrulanan davranışlar, gerçek BERO log bulguları, üretici bilgileri, hesaplar ve teorik senaryolar ayrı sınıflandırılmıştır.
- Bu inceleme yeni firmware testi veya yeni fiziksel ölçüm değildir.

## Önemli karşılaştırma notu

Kullanıcı raporunun başlığında GPIO33 geçerken Log 63 ve güncel Modül 2 SCT-1 kaydı GPIO32'yi gösterir. Kullanıcı raporunun metni değiştirilmemiştir; pin farkı belgeler karşılaştırılırken dikkate alınmalıdır.

## Kapsam

Firmware/K değişikliği, yeni donanım testi veya proje görev sırası değişikliği yapılmamıştır.
