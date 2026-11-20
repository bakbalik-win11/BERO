# Görev kartları

## Güncel mimari

Modül 4, PREBERO Modül 5/6/7'nin ön koşuludur. Masaüstündeki ESP32D2 + ADS1115 + SCT prototipi önce teknik olarak anlaşılacak; ardından bias kararı ve fiziksel tasarımı netleştirilecek, Modül 4 imal edilip doğrulanacaktır. Ancak bundan sonra PREBERO modüllerine geçilecektir.

## Çalışma kuralı

- Her oturumda önce STATUS.md, AGENTS.md ve ilgili deney/karar dosyaları okunur.
- Bir sonraki aşamaya geçiş, önceki aşamanın çıktısı ve kanıtı görüldükten sonra yapılır.
- Bir kartın durumu gerçek uygulama ve kanıtın gösterdiği seviyeyi aşamaz.
- Fiziksel olarak görülmeyen bileşen doğrulanmış sayılmaz; bilinmeyenler tahmin edilmez.
- 220–240 V AC tarafındaki güvenlik sorumluluğu yetkin kişidedir.
- Başarılı kod, gerçek çıktı/log ve teknik yorum birlikte saklanır.
- Çalışma hobi düzeyinde tutulur; gereksiz laboratuvar karakterizasyonu yapılmaz. Üretici elektriksel sınırları ve güvenlik şartları atlanmaz.

## Durum sözlüğü

- **KAPATILDI — HEDEFE ULAŞILDI:** Faz hedefi başka bir yolla sağlandığı için kalan iş yapılmadan kapatıldı.
- **TAMAMLANDI:** Kartın kendi kabul ölçütleri kanıtla karşılandı.
- **DEVAM EDİYOR:** İş başladı, kabul ölçütleri tamamlanmadı.
- **PLANLANDI:** Hedef ve kabul koşulu tanımlandı.
- **BEKLEMEDE:** Aktif değil; bağımlılığı veya sırası bekleniyor.

## Güncel çalışma sırası

| Sıra | İş | Çıktı / geçiş koşulu | Durum |
|---|---|---|---|
| 1 | ADS1115 teknik tanıma | Hobi düzeyinde donanım raporu; veri sayfası sınırları ve BERO kullanım notları | **AKTİF SIRADAKİ İŞ** |
| 2 | Modül 4 masaüstü bağlantı incelemesi | Gerçek bağlantı ve mevcut yazılım ayarlarının kaydı | BEKLEMEDE |
| 3 | Biaslı/bias'sız karşılaştırma | Koşulları belirtilmiş ölçüm logları | BEKLEMEDE |
| 4 | Osiloskop gözlemi | Biaslı/bias'sız sinyal görüntüleri, ayarlar ve yorum | BEKLEMEDE |
| 5 | Modül 4 tasarım kararı | Giriş/bias/besleme/bağlantı/fiziksel yerleşim kararı | BEKLEMEDE |
| 6 | Modül 4 imalatı ve testi | Sabit donanım, bağlantı kaydı ve gerçek çalışma logu | BEKLEMEDE |
| 7 | PREBERO Modül 5/6/7 | Modül 4 kabulünden sonra saha modüllerinin imalatı | BEKLEMEDE |

## Görev ve modül tarihçesi

| ID | Görev / modül | Durum | Not |
|---|---|---|---|
| T011 | Modül 4 teknik inceleme, tasarım ve imalat kapısı | **PLANLANDI — ilk adım aktif sırada** | Ayrıntı: [T011](T011-module4-characterization-and-build.md) |
| T009 | Pratik modül ve ESP düğümlerini devreye alma üst görevi | ÜST GÖREV / kapsamı güncel sıraya bağlı | T011 ve sonraki modül görevleri üzerinden yürütülür |
| T010 | Eski Modül 2 — ESP32D1 üçlü SCT okuma | KAPATILDI — mevcut kapsam | Eski fiziksel modül imha edildi; kod ve loglar tarihsel arşiv |
| T007 | HA → PC veri aktarımı | Tarihsel görev kaydı | Önceki veri hattı planının parçası |
| T008 | Kararlı alan eşleştirme/etiketleme | Tarihsel görev kaydı | Önceki PZEM referanslı akış; güncel bias kararının ön koşulu değil |
| T006 | Katsayı/model değerlendirmesi | Tarihsel görev kaydı | Önceki veri hattı planının parçası |

## Bias kararı için kabul koşulları

- Biaslı ve bias'sız koşulların gerçek bağlantı şeması ve besleme koşulları kaydedilmiş olmalı.
- Karşılaştırma aynı SCT/ADS1115 zinciri ve mümkün olduğunca aynı test yükü/koşullarıyla yapılmalı.
- Ölçüm logları, osiloskop ekran görüntüleri ve osiloskop ayarları saklanmalı.
- Sinyal seviyesi, DC çalışma noktası, dalga biçimi, kararlılık ve ADS1115 giriş sınırları birlikte değerlendirilmeli.
- Bias gerekli/gereksiz kararı yalnız kanıtlar incelendikten sonra verilmelidir.

## PREBERO bias mimarisi — açık karar

Bias gerekliliği belirlendikten sonra Modül 5 (çamaşır), Modül 6 (bulaşık) ve Modül 7 (ana hat + PZEM) için:
1. Bias'ı ESP'nin uygun beslemesinden üretme.
2. Modül 1'in ikiz bias devrelerini/kutularını imal etme.

Seçenekler elektriksel güvenlik, izolasyon, gürültü, besleme kapasitesi, fiziksel yerleşim ve modül bağımsızlığı açısından karşılaştırılacaktır. Henüz tercih yapılmamıştır.

## İlgili kararlar

- [ADR-033 — BERO modül kimlikleri ve PREBERO](../docs/decisions/ADR-033-module-identities-desktop-and-prebero.md)
- [ADR-034 — Bias karşılaştırması ve PREBERO bias sırası](../docs/decisions/ADR-034-module4-bias-comparison-and-prebero-bias-supply.md)
- [ADR-035 — Modül 4 tasarım kapısı ve PREBERO ön koşulu](../docs/decisions/ADR-035-module4-design-gate-before-prebero.md)
