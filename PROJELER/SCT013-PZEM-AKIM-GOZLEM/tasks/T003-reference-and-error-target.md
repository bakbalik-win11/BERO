# T003 — PZEM tabanlı model hata hedefi

- **Durum:** DEVAM EDİYOR — PZEM'in eğitim/etiket referansı olduğu kararlaştırıldı; modelin kabul hata hedefi henüz belirlenmedi.
- **Faz:** 0.3
- **Bağımlılık:** T001; fiziksel deney öncesinde T002
- **Hedef:** SCT verisinden üretilen modelin PZEM okumalarını tahmin etmesi için kullanılacak hata hedefini ve değerlendirme ölçütlerini tanımlamak.

## Yapılacak
1. PZEM-004T V3.0, bu projede SCT verisini etiketlemek/eğitmek için temel referanstır.
2. PZEM'in kararlı anlarının gözlemlenmesi, SCT kararlı an istatistiklerinin çıkarılması ve bu alanların eşleştirilmesi T003 kapsamı dışındadır; bunlar kendi ilgili görev/deneylerinde ele alınacaktır.
3. Modelin PZEM okumalarına uyumunu değerlendirmek için uygun ölçütleri (ör. MAE/RMSE) ve hedef hata sınırını gerekçesiyle belirle.
4. Bu hedef, PZEM'e göre model uyumunu ifade eder; mutlak ölçüm doğruluğu veya PZEM'in kusursuz referans olduğu iddiası değildir.
5. Hedef ölçüm sonuçları görüldükten sonra geriye dönük değiştirilmemeli; değişiklik gerekirse gerekçesi karar kaydına yazılmalı.

## Kabul ölçütü
Model değerlendirme ölçütleri ve PZEM'e göre kabul hata hedefi gerekçesiyle dokümante edilmiştir. Test yükleri ilgili test kaydında kullanıcı tarafından beyan edilir.

## Çıktı / dokunulacak dosyalar
- docs/00-scope.md
- Gerekirse docs/decisions/ altında yeni ADR
- tasks/README.md ve STATUS.md

## Not
Kararlı alan bulma, SCT istatistiklerini çıkarma veya PZEM/SCT zaman eşleştirmesi bu kartın işi değildir.
