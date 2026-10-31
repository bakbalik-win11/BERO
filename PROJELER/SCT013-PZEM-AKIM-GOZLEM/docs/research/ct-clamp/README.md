# ESPHome ct_clamp rapor arşivi

Bu klasör, BERO'nun ESPHome `ct_clamp` ölçüm zinciri hakkındaki iki ayrı raporunu saklar. Belgeler birbirinin yerine geçmez.

## 1. Kullanıcı tarafından sağlanan rapor

- Özgün dosya: [2026-10-31-user-supplied-ct-clamp-report.docx](source/2026-10-31-user-supplied-ct-clamp-report.docx)
- Biçim: DOCX, özgün yükleme; içerik ve pin adı dahil değiştirilmemiştir.
- Boyut: 9.547 bayt.
- Kaynak SHA-256: `cfb2d76f64a93efd8d80e0005c6e80b974d9086e77b72f61542898aa03f88a05`.
- Kaynak raporun kendi açıklamasına göre bazı sayısal örnekler sandbox simülasyonudur; varsayımlar ve kendi çıkarımıyla tamamlanan bölüm rapor içinde belirtilmiştir.

## 2. Bağımsız teknik inceleme

- [2026-10-31-independent-technical-review.md](2026-10-31-independent-technical-review.md)
- Biçim: Markdown.
- Dayanak: ESPHome 2026.10.1 kaynak kodu, Espressif/CT dokümanları ve BERO Log 63.
- Kaynak koddan doğrulanan davranışlar, gerçek BERO log bulguları, üretici bilgileri, hesaplar ve teorik senaryolar ayrı sınıflandırılmıştır.
- Bu inceleme yeni firmware testi veya yeni fiziksel ölçüm değildir.

## Önemli karşılaştırma notu

Kullanıcı raporunun başlığında GPIO33 geçerken Log 63 ve güncel Modül 2 SCT-1 kaydı GPIO32'yi gösterir. Özgün DOCX üzerinde düzeltme yapılmamıştır. Pin farkı, iki belgenin bağlamı değerlendirilirken göz önünde tutulmalıdır.

## Kapsam

Bu rapor arşivi ölçüm zinciri ve ct_clamp davranışını anlamak içindir. Firmware/K değişikliği, yeni donanım testi veya proje görev sırası değişikliği yapılmamıştır.
