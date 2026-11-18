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

1. ADS01 ile sabit ve kararlı bir yükte PZEM ve ADS akım serilerini birlikte kaydet.
2. Başlangıç/ısınma-geçiş bölümünü kararlı karşılaştırma penceresinden ayır.
3. Aynı ortak kararlı pencerede ADS ortalaması ve PZEM ortalamasını hesapla.
4. Kullanılan mevcut katsayı ve katsayı uygulanmadan önceki ham ct_clamp değeri kaydedilebiliyorsa ikisi de saklanır.
5. Aynı hesap ve koşulları ADS02–ADS10 için tekrarla.
6. Her modül için ayrı katsayı sonucu üret; katsayı hesabında kullanılan formül, ham değerler, PZEM değeri ve birimler açıkça yazılır.
7. Modül sırası mümkünse tekrar ölçümle kontrol edilir. İlk modül tekrar ölçülerek yük/kurulum zamanla değişmiş mi görülür.
8. ADS-OLD aynı düzenekte ayrı oturum olarak ölçülür ve yeni partiden ayrı raporlanır.

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
