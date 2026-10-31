# Görev kartları

Faz 1 kapanmıştır. Faz 2'nin ilk aktif görevi T009'dur: modül ve ESP düğümlerinin pratik yeniden devreye alınması. PZEM referanslı veri aktarımı ve öğrenme görevleri bundan sonra gelir.

## Çalışma kuralı
- Her oturumda önce STATUS.md okunur; yalnız aktif görev üzerinde çalışılır.
- Yeni fikirler aktif görevin kapsamını dağıtmaz; gerekirse sonraki karar sorusu olarak kaydedilir.
- Bir kartın durumu, gerçek uygulama ve kanıtın gösterdiği seviyeyi aşamaz.
- Fiziksel olarak görülmeyen bileşen doğrulanmış sayılmaz; bilinmeyen alanlar tahmin edilmez.
- Önce çalışan örnek/kod/kütüphane araştırılır; gereksiz mimari yeniden tasarımı yapılmaz.
- 220–240 V AC tarafındaki güvenlik sorumluluğu yetkin kişidedir.

## Durum sözlüğü
- **KAPATILDI — HEDEFE ULAŞILDI:** Faz hedefi başka bir yolla sağlandığı için kalan iş yapılmadan kapatıldı.
- **TAMAMLANDI:** Kartın kendi kabul ölçütleri kanıtla karşılandı.
- **DEVAM EDİYOR:** İş başladı, kabul ölçütleri tamamlanmadı.
- **PLANLANDI:** Hedef ve kabul koşulu tanımlandı.
- **BEKLEMEDE:** Aktif değil; bağımlılığı veya sırası bekleniyor.

## Görev sırası

| ID | Görev | Faz | Durum | Sıra |
|---|---|---|---|---|
| T001 | Donanım envanteri | Faz 1 | KAPATILDI / tarihsel kayıt | Faz 1 |
| T002 | Güvenlik kontrol kaydı | Faz 1 | KAPATILDI / tarihsel kayıt | Faz 1 |
| T003 | PZEM referansı ve ±%4 hedefi | Faz 1 | HEDEF SAĞLANDI | Faz 1 kapanış ölçütü |
| T004 | Analog ön uç belgelemesi | Faz 1 | KAPATILDI / tarihsel kayıt | Faz 1 |
| T005 | Eski ADC/gürültü tabanı işleri | Faz 1 | KAPATILDI — HEDEFE ULAŞILDI | Eski iş; yeniden açılmayacak |
| E00A–E08, E00F alt adımları | Eski deney kayıtları | Faz 1 | KAPATILDI — HEDEFE ULAŞILDI | Deney kanıtları arşivde |
| **T009** | **Pratik modül ve ESP düğümü yeniden devreye alma** | **Faz 2** | **AKTİF** | **1** |
| T007 | Home Assistant → PC veri aktarımı | Faz 2 | BEKLEMEDE | PZEM/SCT düğümleri çalıştıktan sonra |
| T008 | PZEM/SCT kararlı alan eşleştirme ve etiketleme | Faz 2 | BEKLEMEDE | T007 aktarımından sonra |
| T006 | K=24.22 katsayısı/model değerlendirmesi | Faz 2 | BEKLEMEDE | T008 etiketli veri ürettikten sonra |

## Faz 2 görev bağımlılığı

1. **T009:** Modül kapsamını ve gerçek bağlantıları belirle; çalışan kod/örnek seç; en az uyarlamayla derle ve tekil modül işlevini gerçek donanımda doğrula. Modül sırası kullanıcıyla belirlenir.
2. **T007:** PZEM/SCT HA entity akışları çalıştığında geçmişi PC'ye al; kaynak alanları koru; aktarımı tekrar çalıştırılabilir yap.
3. **T008:** PC'deki kayıtta PZEM ve SCT kararlılığını ayrı hesapla; örtüşen alanları eşleştir ve PZEM referansıyla etiketle.
4. **T006:** Etiketli alanlarda K=24.22'yi değerlendir; veri gerekçelendirirse yeni calibration_id ile iyileştir.

## Fikir havuzu

Göreve dönüşmemiş fikirler [IDEA_BACKLOG.md](../IDEA_BACKLOG.md) içinde tutulur. Fikirler aktif görev değildir.

## İlgili karar

Faz 2 çalışma biçimi ve kapsamı [ADR-014](../docs/decisions/ADR-014-phase2-practical-restart.md) ile tanımlanmıştır.
