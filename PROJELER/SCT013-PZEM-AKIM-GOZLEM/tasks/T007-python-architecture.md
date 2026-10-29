# T007 — Python program mimarisini kullanıcı hedeflerine göre tanımla

- **Durum:** BEKLEMEDE — taslak korunuyor; E00A/E00/E01 edinim sonuçları ve gerçek HA→PC veri akışı netleşene kadar aktif çalışma değil.
- **Faz:** 3–7 (PZEM edinimi, kayıt şeması, hizalama ve analiz hazırlığı)
- **Bağımlılık:** E00A/E00/E01 temel edinim sonuçları, kullanıcı tarafından açıklanan Home Assistant → PC veri akışı hedefi
- **Hedef:** Python tarafında yapılacak işlerin sınırlarını ve bağımlılıklarını, gerçek ölçüm verisi ve kullanıcı hedefleriyle uyumlu olacak şekilde aşamalı olarak tanımlamak; erken ve kanıtsız mimari varsayımlar üretmemek.

## Mevcut durum

- [Python Program Mimarisi](../docs/architecture/python-program-architecture.md) yalnızca hedefleri ve açık kararları kaydeden taslaktır.
- Proje klasöründe Python uygulama dosyası henüz bulunmuyor.
- Home Assistant kayıtlarının PC'ye aktarılması, PZEM ve üç SCT kanalının analiz/etiketlenmesi Python tarafında hedefleniyor.
- Program sayısı, çalıştırılabilir süreçler, modül sınırları, aktarım yöntemi ve veri sözleşmeleri henüz belirlenmedi.
- İlk ADC edinim deneyleri ve veri biçimi gereksinimleri anlaşılmadan uygulama mimarisini kesinleştirmek hedeflenmiyor.

## Yapılacak

1. Kullanıcının mevcut veri akışı hedefini mimari belgede koru; bilinmeyen ayrıntıları açık soru olarak tut.
2. E00A/E00/E01 çıktılarından gerçek ham kayıt ve metadata gereksinimlerini çıkar.
3. [FIELDS.md](../schema/FIELDS.md) ve JSON Schema dosyalarının hangi kayıt türleri için hedef olduğunu belirle; henüz üretilmeyen alanları uygulandı sayma.
4. HA → PC aktarım biçimi ve sıklığı netleşince en küçük gerekli program/modül sınırlarını öner.
5. Mimari kararları ancak somut gereksinim ve örnek kayıtlarla gerekçelendir; karar verilirse ilgili ADR veya mimari belgeye yaz.

## Kabul ölçütü

- Bilinen hedefler, bilinmeyen kararlar ve bağımlılıklar ayrı ayrı belgelenmiş olmalı.
- Gerçek kodun varlığı veya çalışması hakkında kanıtsız iddia bulunmamalı.
- Her önerilen program/modülün girdisi, çıktısı ve sorumluluğu açıklanmalı; kullanıcı tarafından onaylanmamış kararlar kesinleşmiş gibi sunulmamalı.
- Görev durumu, gerçek kod/deney ilerlemesini değil bu mimari tanımlama işinin durumunu yansıtmalı.

## Çıktı / dokunulacak dosyalar

- [docs/architecture/python-program-architecture.md](../docs/architecture/python-program-architecture.md)
- [schema/FIELDS.md](../schema/FIELDS.md) ve mevcut JSON Schema dosyaları
- Gerekirse STATUS.md, ROADMAP.md ve HISTORY/SESSION_LOG.md

## Kanıt

- Mimari taslak: [python-program-architecture.md](../docs/architecture/python-program-architecture.md)
- Gerçek Python uygulaması henüz yok; firmware, fiziksel ölçüm ve Python testleri bu görev kapsamında henüz çalıştırılmadı.

## Açık kalanlar

- Kaç süreç/program gerekeceği.
- Home Assistant'tan PC'ye veri aktarım yöntemi ve kayıt biçimi.
- Ham ADC kayıtlarının boyutu/sıklığı ve özet/olay kesiti saklama sınırları.
- JSON Schema doğrulamasının hangi aşamada ve hangi araçla çalıştırılacağı.
