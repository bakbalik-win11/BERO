# Görev kartları

Görev kartları yol haritasındaki işi küçük, kabul ölçütü belli adımlara böler. **ROADMAP.md** genel fazları, **STATUS.md** ise güncel durumu gösterir.

## Çalışma kuralı
- Bir oturumda STATUS.md içindeki tek aktif göreve odaklan.
- Yeni bir fikir çıkarsa mevcut görevi bölme; açık soruya veya uygun sonraki göreve not et.
- Bir kartın durumu, kanıtın gösterdiği seviyeyi aşamaz.
- Kullanıcıdan teknik ayrıntıları kendi başına değerlendirmesini bekleme. Gerekli kanıtı asistan bulmalı veya hangi fiziksel kanıtın gerektiğini açıkça söylemeli.
- Fiziksel olarak görülmeyen bileşen doğrulandı sayılmaz. Bilinmeyen alanları tahminle doldurma.
- 220–240 V AC tarafında çalışma ve güvenlik onayı yetkin kişi sorumluluğundadır. Güvenlik kontrolü bitmeden şebeke bağlantısı/deneyi başlatılmaz.

## Durum sözlüğü
- **PLANLANDI:** hedef ve kabul koşulu belirlendi.
- **HAZIRLANDI:** taslak veya plan hazır.
- **UYGULANDI:** çıktı hedef dosyaya/ortama işlendi.
- **DOĞRULANDI:** ilgili kontroller ve kanıt gözden geçirildi.
- **TAMAMLANDI:** kabul ölçütlerinin tamamı kanıtla karşılandı.
- **ENGELLENDİ:** gereken erişim, donanım, karar veya test eksik.
- **DEVAM EDİYOR:** iş başladı ancak kabul ölçütlerinin tamamı karşılanmadı.

Bir kart, yalnızca doküman dolduruldu diye otomatik olarak TAMAMLANDI olmaz.

## Sıra ve bağımlılıklar

| ID | Görev | Faz | Durum | Bağımlılık |
|---|---|---:|---|---|
| T001 | Fiziksel donanım envanteri | 0.1 | DEVAM EDİYOR — stok ve 8 kanallı bias kartı kaydedildi; ADC/VREF ve SCT kuplaj ayrıntıları açık | — |
| T002 | Güvenlik kontrolü | 0.2 | PLANLANDI | T001 |
| T003 | Referans cihazı, yükler ve hata hedefi | 0.3 | PLANLANDI | T001 |
| T004 | Analog ön uç | 1.1 | PLANLANDI | T002, T003 |
| T005 | E01 gürültü tabanı | 1.2 | PLANLANDI | T004 |
| T006 | SCT kalibrasyonu | 1.3 | PLANLANDI | T005 |

## Kart açma
Yeni görev için _template.md dosyasını kopyala; bir sonraki T numarasını kullan, bağımlılıkları ve ölçülebilir kabul koşulunu yaz. Yeni kart eklendiğinde bu tabloyu, ROADMAP.md ve gerekiyorsa STATUS.md'yi güncelle.
