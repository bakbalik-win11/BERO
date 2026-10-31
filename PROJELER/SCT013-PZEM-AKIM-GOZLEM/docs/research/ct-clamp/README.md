# ESPHome ct_clamp rapor arşivi

Bu klasör, BERO'nun ct_clamp ölçüm zinciri hakkındaki üç ayrı kaynağı saklar: kullanıcının sağladığı rapor, GitHub Copilot raporu ve bağımsız teknik inceleme.

## 1. Kullanıcının sağladığı rapor

- [Kullanıcı raporu — Markdown metin aktarımı](source/2026-10-31-user-supplied-ct-clamp-report.md)
- Kaynak: kullanıcı tarafından yüklenen dört sayfalık DOCX.
- Depoda metin aktarımı Markdown biçiminde tutulur; raporun varsayımları, simülasyon sonuçları ve kendi çıkarım notları kaynak metindeki gibi korunmuştur.
- Kaynak DOCX'in kendisi depoda ikili dosya olarak tutulmuyor; dört sayfalık içeriği Markdown metin aktarımı olarak korunuyor. Kaynak DOCX: 9.547 bayt; SHA-256 `cfb2d76f64a93efd8d80e0005c6e80b974d9086e77b72f61542898aa03f88a05`.

## 2. GitHub Copilot raporu

- [GitHub Copilot raporu — özgün metin](source/2026-10-31-github-copilot-ct-clamp-report.txt)
- Kullanıcının paylaştığı metin, içerik ve ifadeleri düzeltilmeden UTF-8 TXT olarak saklanmıştır.
- Bu dosya bağımsız teknik inceleme değildir; Copilot'un kendi değerlendirmesidir. İçindeki teknik iddialar doğrulanmış kabul edilmemelidir.

## 3. Bağımsız teknik inceleme

- [Bağımsız teknik inceleme](2026-10-31-independent-technical-review.md)
- Biçim: Markdown.
- Dayanak: ESPHome 2026.10.1 kaynak kodu, Espressif/CT dokümanları ve BERO Log 63.
- Kaynak koddan doğrulanan davranışlar, gerçek BERO log bulguları, üretici bilgileri, hesaplar ve teorik senaryolar ayrı sınıflandırılmıştır.
- Bu inceleme yeni firmware testi veya yeni fiziksel ölçüm değildir.

## 4. Tasarım tarihçesi ve geliştirici niyeti

- [ESPHome ct_clamp tasarım tarihçesi](2026-10-31-design-history.md)
- İlk PR/commit, Jesse Hills ve Otto Winter katkıları, EMonLib kökeni, CTL-10-CLS test düzeneği, 200 ms ve 60 s varsayılanlarının kanıt durumu, 2021 last_value filtresinin eklenme nedeni ve ilgili issue/PR tartışmaları incelendi.
- Geliştirici açıklaması ile kaynak koddan çıkarılan teknik yorumlar ayrı tutuldu; belgelenmeyen tasarım gerekçeleri varsayılmadı.

## Önemli karşılaştırma notu

Kullanıcı raporunun başlığında GPIO33 geçerken Log 63 ve güncel Modül 2 SCT-1 kaydı GPIO32'yi gösterir. Kullanıcı raporunun metni değiştirilmemiştir; pin farkı belgeler karşılaştırılırken dikkate alınmalıdır.

## Kapsam

Firmware/K değişikliği, yeni donanım testi veya proje görev sırası değişikliği yapılmamıştır.


## 5. Üç kaynaklı sentez

- [Claude + GitHub Copilot + bağımsız inceleme sentezi](2026-10-31-synthesis-copilot-claude-independent.md)
- İlk PR/commit (2019), 2021 AC-only RMS değişikliği (#1906), çoklu CT mutex (#1915), NaN düzeltmesi (#1916), yinelenen örnek filtresi (#2283) ve sıfır akım düzeltmeleri (#4229/#4236) birlikte değerlendirildi.
- Copilot'un doğru ek katkıları korundu; belgelenmeyen 200 ms / 60 s / performans gerekçeleri kesin bilgi olarak kabul edilmedi.
- BERO ayarları değiştirilmedi; E10 planı ve last_value için kontrollü inceleme kararı korundu.


## 6. Hipotez sicili ve sonraki deneyler

- [H1–H19 hipotez sicili ve deney önceliği](2026-10-31-hypothesis-register-and-next-experiments.md).
- Kaynak kodla kanıtlı bilgiler, BERO saha desteği, deney bekleyen hipotezler, açık araştırma soruları ve şu an kanıtsız iddialar ayrı sınıflandırıldı.
- T010 kanal davranışı → E10 pencere süresi → ayrı last_value A/B → T007 → T008 → T006 sırası önerildi; ana Faz 2 sırası değişmedi.
- Bu sicil yeni fiziksel test/kalibrasyon değildir; firmware ve K=24.22 değiştirilmedi.
