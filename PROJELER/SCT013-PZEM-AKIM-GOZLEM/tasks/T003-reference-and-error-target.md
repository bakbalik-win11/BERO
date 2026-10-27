# T003 — Referans cihazı, yükler ve hata hedefi

- **Durum:** DEVAM EDİYOR — PZEM-004T V3.0 temel eğitim/etiket kaynağı olarak belirlendi; hata değerlendirme ölçütleri açık.
- **Faz:** 0.3
- **Bağımlılık:** T001; fiziksel deney öncesinde T002
- **Hedef:** PZEM ölçümlerini SCT verisini etiketlemek/eğitmek için temel almak; karşılaştırma ve model değerlendirme ölçütlerini tanımlamak.

## Yapılacak
1. **Eğitim/etiket kaynağı:** Projenin temel referansı mevcut PZEM-004T V3.0 düzenidir. PZEM'in akım okumaları, SCT verisinin paket bağlamı ve kararlılık ölçütleriyle eşleştirilerek eğitim/etiketleme amacıyla kullanılacaktır.
2. Test sırasında kullanılacak yük ve çalışma koşulları kullanıcı tarafından ilgili test kaydında beyan edilecek; T003 kapsamında önceden yük seviyesi belirleme şartı yoktur.
3. SCT modelinin PZEM okumalarını ne ölçüde yakaladığını değerlendirmek için MAE/RMSE gibi hata ölçütleri ve kararlı alan eşleştirme koşulları öner.
4. True RMS pens ampermetre kullanımı proje şartı değildir. PZEM, bu projenin eğitim/etiket referansıdır; bağımsız, kusursuz ölçüm standardı olduğu varsayılmayacaktır.
5. Hedefler ölçüm sonuçları görüldükten sonra geriye dönük değiştirilmemeli. Değişiklik gerekirse gerekçesi yeni bir karar kaydında açıklanmalı.

## Kabul ölçütü
PZEM'in eğitim/etiket referansı rolü ve SCT modelini değerlendirme ölçütleri dokümante edilmiştir. Test yükleri ilgili test kaydında belirtilir; True RMS pens ampermetre şartı yoktur.

## Çıktı / dokunulacak dosyalar
- hardware/inventory.md
- docs/00-scope.md
- Gerekirse docs/decisions/ altında yeni ADR

## Not
Teknik kabul hedefini kullanıcıya gerekçesiz seçtirme. Hedefin neyi garanti edip neyi etmediğini anlaşılır biçimde açıkla.
