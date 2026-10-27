# T003 — Referans cihazı, yükler ve hata hedefi

- **Durum:** PLANLANDI
- **Faz:** 0.3
- **Bağımlılık:** T001; fiziksel deney öncesinde T002
- **Hedef:** Kalibrasyon için referans ekipmanını ve yük senaryolarını belirlemek, kabul hedeflerini ilk ölçümden önce yazılı olarak kararlaştırmak.

## Yapılacak
1. Kullanılabilir True-RMS referans ampermetrenin marka/modelini ve kalibrasyon/izlenebilirlik durumunu kaydet.
2. Planlanan yüklerin tipini, etiket gücünü ve güvenli kullanım koşullarını kaydet; lamba dâhil en az üç kontrollü akım seviyesi için aday senaryo belirle. Yüklerin değerlerini ölçüm/etiket kanıtı olmadan doldurma.
3. Hedef kullanım amacına göre SCT–referans hata sınırını ve diğer gerekli kabul ölçütlerini tanımlamak için gerekçeli seçenekler hazırla.
4. Asistan, hedefleri sessizce tahmin etmemeli: önerilen sayısal hedefi dayanağı ve ödünleşimleriyle açıklamalı; kullanıcı onayından sonra docs/00-scope.md ve gerekiyorsa yeni ADR'ye yazmalı.
5. Hedefler ölçüm sonuçları görüldükten sonra geriye dönük değiştirilmemeli. Değişiklik gerekirse gerekçesi yeni bir karar kaydında açıklanmalı.

## Kabul ölçütü
Referans cihazı ve en az üç yük seviyesi tanımlıdır. Sayısal kabul hedefleri ilk ölçümden önce gerekçesiyle kaydedilmiştir; hedef belirlenemiyorsa kart ENGELLENDİ kalır ve neden açıklanır.

## Çıktı / dokunulacak dosyalar
- hardware/inventory.md
- docs/00-scope.md
- Gerekirse docs/decisions/ altında yeni ADR

## Not
Teknik kabul hedefini kullanıcıya gerekçesiz seçtirme. Hedefin neyi garanti edip neyi etmediğini anlaşılır biçimde açıkla.
