# E24 — ADS1115 modül parti bazlı katsayı kontrolü

- **Durum:** AÇILDI / PLANLANDI — modül bazında karşılaştırmalı katsayı ölçümleri bekleniyor.
- **Açılış tarihi:** 2026-11-18.
- **İlişki:** E19 ADS1115 düşük akım ölçüm alternatifi; E24, farklı ADS1115 kartlarının ölçüm/katsayı eşdeğerliğini inceler.
- **Kapsam:** Yeni aynı marka/parti 10 modül (ADS01–ADS10) ve daha önce kullanılan farklı markalı eski ADS1115 modül.
- **Referans:** PZEM-004T V3.0 karşılaştırma referansıdır; mutlak ground truth kabul edilmez.

## Amaç

Yeni partideki her ADS1115 modülünün aynı ölçüm koşullarında verdiği akım sonucunu ayrı ayrı ölçmek, her modül için katsayı ihtiyacını belirlemek ve aynı parti içindeki modüllerin ortak katsayı kullanıp kullanamayacağını veriye dayanarak değerlendirmek.

Eski, farklı markalı ADS1115 modül ayrı bir karşılaştırma grubu olarak tutulur. Eski modülün katsayısı yeni 10'lu partiye aktarılmaz; yeni partinin katsayısı da eski modüle otomatik uygulanmaz.

## Modül kimlikleri

- Yeni parti: ADS01, ADS02, ADS03, ADS04, ADS05, ADS06, ADS07, ADS08, ADS09, ADS10.
- Eski farklı marka modül: ayrı kimlik **ADS-OLD**.
- Fiziksel etiket ile kayıt kimliği birebir eşleştirilir. Kartlar ölçüm sırasında karıştırılmaz.
- Marka/parti bilgisi, mümkünse kart üzerindeki baskı ve satın alma kaydıyla desteklenir.

## Sabit tutulacak koşullar

Her modül karşılaştırmasında mümkün olduğunca aynı koşullar korunur:

- Aynı ESP32D2, I²C bağlantısı ve besleme.
- Aynı ADS1115 adresleme ve diferansiyel giriş bağlantısı (A0-A1).
- Aynı SCT-013 30A/1V sensör, aynı iletken ve aynı tur sayısı.
- Aynı ADS1115 gain, sample rate ve continuous mode ayarları.
- Aynı ct_clamp sample_duration, update_interval, filtre ve yazılım sürümü.
- Aynı fiziksel yük ve PZEM ile eşzamanlı/ortak kararlı zaman aralığı.
- Modül değişimleri enerjisiz ve güvenli koşulda yapılır.

Test başlamadan önce gerçek cihazda çalışan YAML/firmware ayarları log ile doğrulanır. Depodaki YAML ile cihaz logu arasında uyuşmazlık varsa ölçüm başlamadan bu fark kayda alınır ve giderilir; hangi yapılandırmanın çalıştığı belirsiz sonuç katsayı hesabına alınmaz.

## Ölçüm yöntemi

**Temel kural:** Her ADS modülü, her test yükünde PZEM ile eşleştirilmiş en az 5, tercihen 10 ayrı kararlı kayıt üzerinden değerlendirilecektir. Tek bir anlık ekran değeriyle katsayı belirlenmeyecektir.

1. Birkaç farklı ve kararlı yük seviyesi seçilir. Yüklerin gerçek akım aralığı PZEM ölçümüyle belirlenir; testte kullanılan ampul/cihaz adı ve nominal gücü de yazılır. Mümkünse düşük, orta ve daha yüksek akım seviyeleri kapsanır.
2. Her yük seviyesinde yükün kararlı hale gelmesi beklenir. Geçiş/ilk kalkış örnekleri katsayı hesabına alınmaz.
3. Aynı zaman penceresinde ADS ve PZEM kayıtları eşleştirilir. Her eşleşme için zaman damgası, PZEM akımı, ADS akımı ve varsa ham ct_clamp değeri tek satırda saklanır.
4. Her modül + her yük kombinasyonu için 5–10 geçerli eşleşmiş kayıt toplanır. Veri akışı elveriyorsa 10 kayıt hedeflenir. Eksik/NaN/bozuk eşleşmeler geçerli kayıt sayısına dahil edilmez; nedenleri ayrıca not edilir.
5. ADS01 için tüm yük seviyeleri tamamlanır; aynı protokol ADS02–ADS10 için tekrarlanır. Modül değişimlerinde ölçüm zincirinin diğer bileşenleri ve ayarları sabit tutulur.
6. Her modül ve yük seviyesi için eşleşmiş kayıtların sayısı, ortalaması, medyanı, standart sapması, min–maks değeri ve PZEM'e göre sapması raporlanır. Tek tek kayıtlar da korunur; yalnız ortalama tabloya yazılıp ham eşleşmeler atılmaz.
7. Katsayı hesabında kullanılan formül açıkça belirtilir. Her modül için katsayı önce ayrı hesaplanır; birden fazla yük seviyesindeki sonuçlar karşılaştırılmadan tek bir genel katsayı kabul edilmez.
8. İlk modül (ADS01) ölçüm dizisinin sonunda en az bir yük seviyesinde tekrar ölçülür. Böylece zaman içinde yük/kurulum kayması olup olmadığı kontrol edilir.
9. ADS-OLD aynı yük seviyeleri ve aynı 5–10 eşleşmiş kayıt kuralıyla ayrı oturumda ölçülür; yeni parti sonuçlarıyla aynı gruba katılmaz.
10. Ölçüm sırası, kullanılan yük, modül kimliği, gerçek PZEM değerleri, YAML/firmware sürümü ve tüm ayarlar oturum günlüğüne yazılır.

### Eşleşmiş kayıt tablosu

Her satır tek bir zaman eşleşmesini temsil eder. Her modül ve yük seviyesi için bu tabloya 5–10 satır girilir.

| Modül | Yük kimliği | Kayıt no | Zaman damgası | PZEM A | ADS A | Ham ct_clamp A | Geçerli mi / not |
|---|---|---:|---|---:|---:|---:|---|
| ADS01 | L1 | 1 | Bekliyor | | | | |
| ADS01 | L1 | 2 | Bekliyor | | | | |
| ADS01 | L1 | … | Bekliyor | | | | |
| ADS01 | L2 | 1 | Bekliyor | | | | |
| ADS-OLD | L1 | 1 | Bekliyor | | | | |

Yük kimlikleri (L1, L2, L3…) gerçek test yükleri belirlendiğinde adlandırılır. Bu tablo örnek şablondur; henüz ölçüm sonucu içermez.

## Katsayı değerlendirmesi

- Her modülün bireysel katsayısı ayrı kaydedilir; tek bir katsayı baştan tüm modüllere atanmaz.
- ADS01–ADS10 sonuçlarının birbirine yakınlığı sayısal olarak karşılaştırılır.
- Ortak katsayı ancak modüller arası fark, tekrar ölçüm saçılımı ve yük koşulları birlikte değerlendirildikten sonra önerilebilir.
- Tek bir yük noktasından bulunan katsayı genel doğruluk veya tüm akım aralığında doğrusallık kanıtı değildir. Mümkünse farklı kararlı yük seviyelerinde kontrol tekrarlanır.
- Katsayı değişikliği deney boyunca sessizce yapılmaz. Önce mevcut ayarla ham/ölçülen sonuç saklanır; hesaplanan yeni katsayı ayrı bir sonuç olarak raporlanır.
- PZEM karşılaştırma referansıdır; PZEM'in kendi ölçüm belirsizliği bulunduğu için sonuçlar mutlak doğruluk iddiası olarak yazılmaz.

## Yüksüz davranış — ayrı gözlem

2026-11-18 ESP32D2 logunda ampul kapalıyken akım sensörü sürekli `NaN A` yayınladı. Ampul takıldığında ct_clamp debug satırları görünür oldu: yaklaşık 133–139 farklı örnek (665–695 SPS), Raw AC Value 0.003–0.004 A ve yayınlanan akım yaklaşık 0.094–0.100 A. Ampul çıkarılınca tekrar `NaN A` görüldü. Aynı ekran görüntüsünde PZEM yüksüzken 0.000 A gösteriyordu.

Bu gözlem E24'e yüksüz davranış kontrolü olarak eklenmiştir; katsayı hesabına dahil edilmez. `NaN` sıfır akım veya sıfır gürültü anlamına gelmez. Nedeni henüz belirlenmemiştir. Eski farklı marka modülün yüksüzken sürekli sayısal okuma verdiği kullanıcı gözlemidir; bunun marka/parti kaynaklı olduğu henüz kanıtlanmamıştır.

## Kayıt tablosu

| Modül | Marka/parti | Yük / PZEM A | Ham ct_clamp A | Mevcut katsayı | Hesaplanan katsayı | Tekrar / not |
|---|---|---:|---:|---:|---:|---|
| ADS01 | Yeni parti | Bekliyor | Bekliyor | Bekliyor | Bekliyor | |
| ADS02 | Yeni parti | Bekliyor | Bekliyor | Bekliyor | Bekliyor | |
| ADS03 | Yeni parti | Bekliyor | Bekliyor | Bekliyor | Bekliyor | |
| ADS04 | Yeni parti | Bekliyor | Bekliyor | Bekliyor | Bekliyor | |
| ADS05 | Yeni parti | Bekliyor | Bekliyor | Bekliyor | Bekliyor | |
| ADS06 | Yeni parti | Bekliyor | Bekliyor | Bekliyor | Bekliyor | |
| ADS07 | Yeni parti | Bekliyor | Bekliyor | Bekliyor | Bekliyor | |
| ADS08 | Yeni parti | Bekliyor | Bekliyor | Bekliyor | Bekliyor | |
| ADS09 | Yeni parti | Bekliyor | Bekliyor | Bekliyor | Bekliyor | |
| ADS10 | Yeni parti | Bekliyor | Bekliyor | Bekliyor | Bekliyor | |
| ADS-OLD | Eski, farklı marka | Bekliyor | Bekliyor | Ayrı tutulacak | Ayrı hesaplanacak | |

## Kaynak ve kanıt durumu

- **Kullanıcı bildirimi:** Yeni 10 modül aynı marka/partiden; ilk akım okumalarında birbirlerine benzer davranıyorlar. Eski modül farklı markadan ve farklı okuma/katsayı davranışı gösteriyor.
- **Log kanıtı:** 2026-11-18 ESP32D2 logu; ampul kapalı/açık davranışı ve ct_clamp örnek sayısı/SPS yukarıda özetlenmiştir.
- **Henüz yapılmadı:** ADS01–ADS10'un aynı yükte tek tek karşılaştırmalı ölçümü, modül bazında katsayı hesabı, tekrar testi ve ortak katsayı kararı.
- **Sonuç:** Bu dosya deney protokolüdür; modüllerin eşdeğer olduğu veya herhangi bir katsayının doğrulandığı anlamına gelmez.
