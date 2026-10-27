# T003 — Referans cihazı, yükler ve hata hedefi

- **Durum:** DEVAM EDİYOR — referans cihazının modeli belirlendi; kalibrasyon/izlenebilirlik durumu, yük seviyeleri ve hata kabul hedefi açık.
- **Faz:** 0.3
- **Bağımlılık:** T001; fiziksel deney öncesinde T002
- **Hedef:** Kalibrasyon için referans ekipmanını ve yük senaryolarını belirlemek, kabul hedeflerini ilk ölçümden önce yazılı olarak kararlaştırmak.

## Yapılacak
1. **Referans cihazı belirlendi:** Kullanıcı fotoğrafında UNI-T UT200B+ True RMS pens ampermetre görülüyor. Akım karşılaştırma cihazı olarak kaydedildi. Kalibrasyon/izlenebilirlik durumu bilinmiyor; cihazın bağımsız referans standardı olduğu veya doğruluğunun kalibre edildiği varsayılmayacak.
2. Kullanıcının bildirdiği deney yüklerini kaydet: 100 W ve 150 W ampuller ana deney yükleri; ayrıca farklı güç faktörü (PF) karakteristiği için 5 W LED ampul kullanılacak. Bunlar etiket gücü/ kullanıcı bildirimi olarak kaydedilmiştir; gerçek güç, akım ve PF ölçümle doğrulanmalıdır. Bu yüklerle en az üç kontrollü akım seviyesi ve güvenli kullanım koşulları planlanmalı.
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
