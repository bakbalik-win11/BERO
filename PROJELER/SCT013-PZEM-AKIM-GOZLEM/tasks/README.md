# Görev kartları

Faz 1 kapanmıştır. Faz 2'nin güncel aktif işi, mevcut Modül 4 masaüstü düzeneğinde bias gerekliliğini deneysel olarak belirlemektir. Modül 2/3'ün eski fiziksel düzenekleri imha edilmiştir; T010 tarihsel görev olarak kapalıdır. Güncel modül kimlikleri için [ADR-033](../docs/decisions/ADR-033-module-identities-desktop-and-prebero.md) esas alınır.

## Çalışma kuralı
- Her oturumda önce STATUS.md, AGENTS.md ve ilgili deney/karar dosyaları okunur.
- Yalnız aktif aşama yürütülür; sonraki aşamanın mimari kararı erkenden verilmez.
- Bir kartın durumu gerçek uygulama ve kanıtın gösterdiği seviyeyi aşamaz.
- Fiziksel olarak görülmeyen bileşen doğrulanmış sayılmaz; bilinmeyen alanlar tahmin edilmez.
- 220–240 V AC tarafındaki güvenlik sorumluluğu yetkin kişidedir.
- Başarılı kod, gerçek çıktı/log ve teknik yorum birlikte saklanır.

## Durum sözlüğü
- **KAPATILDI — HEDEFE ULAŞILDI:** Faz hedefi başka bir yolla sağlandığı için kalan iş yapılmadan kapatıldı.
- **TAMAMLANDI:** Kartın kendi kabul ölçütleri kanıtla karşılandı.
- **DEVAM EDİYOR:** İş başladı, kabul ölçütleri tamamlanmadı.
- **PLANLANDI:** Hedef ve kabul koşulu tanımlandı.
- **BEKLEMEDE:** Aktif değil; bağımlılığı veya sırası bekleniyor.

## Güncel çalışma sırası

| Sıra | İş | Kapsam | Durum |
|---|---|---|---|
| 1 | Modül 4 biaslı/bias'sız karşılaştırması | ESP32D2 + ADS1115 + SCT masaüstü düzeneği; Modül 1 bias kutusu kullanılır | **AKTİF SIRADAKİ İŞ** |
| 2 | Osiloskopla sinyal incelemesi | Biaslı/bias'sız sinyal biçimi ve devre davranışını birlikte gözlemleme | BEKLEMEDE — 1. aşamadan sonra |
| 3 | Bias gerekliliği kararı | Deney + osiloskop kanıtıyla bias gerekli mi sorusunu cevaplama | BEKLEMEDE — 2. aşamadan sonra |
| 4 | PREBERO Modül 5/6/7 bias besleme mimarisi | ESP beslemesinden bias üretme veya Modül 1'in ikiz bias devrelerini imal etme seçeneklerini karşılaştırma | BEKLEMEDE — bias kararından sonra |

## Modül ve görev tarihçesi

| ID | Görev / modül | Durum | Not |
|---|---|---|---|
| T009 | Pratik modül ve ESP düğümlerini devreye alma üst görevi | DEVAM EDİYOR / üst görev | Güncel sıra ADR-034'e göre yürütülür |
| T010 | Eski Modül 2 — ESP32D1 üçlü SCT okuma | KAPATILDI — mevcut kapsam | Eski fiziksel modül imha edildi; kod ve loglar tarihsel arşiv |
| T007 | HA → PC veri aktarımı | Tarihsel görev kaydı | Önceki veri hattı planının parçası; şu an aktif sırayı belirlemiyor |
| T008 | Kararlı alan eşleştirme/etiketleme | Tarihsel görev kaydı | Önceki PZEM referanslı öğrenme akışı; güncel bias deneyinin ön koşulu değil |
| T006 | Katsayı/model değerlendirmesi | Tarihsel görev kaydı | Önceki veri hattı planının parçası |

## Bias kararı için kabul koşulları

- Biaslı ve bias'sız koşulların gerçek bağlantı şeması ve besleme koşulları kaydedilmiş olmalı.
- Karşılaştırma aynı SCT/ADS1115 ölçüm zinciri ve mümkün olduğunca aynı test yükü/koşullarıyla yapılmalı.
- Ölçüm logları, osiloskop ekran görüntüleri ve osiloskop ayarları saklanmalı.
- Sinyal seviyesi, DC çalışma noktası, dalga biçimi, kararlılık ve ADS1115 giriş sınırları birlikte değerlendirilmeli.
- Bias gerekli/gereksiz kararı ancak kanıtlar incelendikten sonra verilmelidir.

## PREBERO bias mimarisi — açık karar

Bias gerekliliği belirlendikten sonra Modül 5 (çamaşır), Modül 6 (bulaşık) ve Modül 7 (ana hat + PZEM) için:
1. Bias'ı ESP'nin uygun beslemesinden üretme.
2. Modül 1'in ikiz bias devrelerini/kutularını imal etme.

Seçenekler elektriksel güvenlik, izolasyon, gürültü, besleme kapasitesi, fiziksel yerleşim ve modül bağımsızlığı açısından karşılaştırılacaktır. Bu aşamada tercih yapılmış değildir.

## İlgili kararlar
- [ADR-033 — Modül kimlikleri ve PREBERO](../docs/decisions/ADR-033-module-identities-desktop-and-prebero.md)
- [ADR-034 — Modül 4 bias karşılaştırması ve PREBERO bias sırası](../docs/decisions/ADR-034-module4-bias-comparison-and-prebero-bias-supply.md)
- [T009 — Pratik sistem devreye alma](T009-practical-system-bringup.md)
