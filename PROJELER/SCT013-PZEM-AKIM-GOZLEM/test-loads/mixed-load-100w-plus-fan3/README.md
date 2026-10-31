# MIXED-LOAD-001 — 100 W Akkor + FAN-3

**Test ID:** MIXED-LOAD-001  
**Test sınıfı:** Karma yük / dirençli yük + motor yükü  
**Durum:** AÇILDI — fiziksel deney ve ölçüm bekliyor  
**Modül:** Modül 2 / ESP32D1 / SCT-1

## Amaç

100 W akkor ampul ile FAN-3 birlikte çalışırken SCT-1'in toplam hat akımını nasıl gözlemlediğini incelemek. FAN-3 tek başına çalışırken gözlenen düşük akım bölgesini, kararlı ve daha yüksek akımlı dirençli yükle birlikte çalışma koşulunda karşılaştırmak.

İkinci amaç, PZEM'in toplam akım ve PF bildirimleriyle SCT ölçüm pencerelerini karşılaştırarak karma yükte PF değişiminin toplam akım davranışıyla ilişkisini incelemektir.

Bu deney FAN-3'ün akımını tek başına ayrıştırmayı veya SCT üzerinden PF hesaplamayı hedeflemez. SCT, aynı hattan geçen toplam akımı gözlemler.

## Yük bileşenleri

| Bileşen | Ön bilgi | Bu testteki rol |
|---|---|---|
| 100 W akkor ampul | Ayrı testlerde kullanılmış dirençli yük; UNIT geçici bildirimi 0,427 A | Kararlı, daha yüksek akım bileşeni |
| FAN-3 | Önceki FAN-3 UNIT bildirimi 0,141 A; düşük akım gözlem sınıfında | Motor yükü / PF etkisi araştırılacak bileşen |

Önceki ayrı testlerdeki UNIT değerleri bu karma yükün referansı değildir. Birlikte çalışma için yeni, eşzamanlı referans ölçümleri alınacaktır.

## Deney düzeni

1. Yalnızca 100 W akkor açık: kararlı SCT ve referans penceresi.
2. Yalnızca FAN-3 açık: önceki FAN-3 gözlemiyle bağlam karşılaştırması; mümkünse yeni oturumda tekrar.
3. 100 W akkor + FAN-3 birlikte açık: toplam akımın kararlı penceresi.
4. 100 W akkor açık kalırken FAN-3 açılır: geçiş kaydı.
5. 100 W akkor açık kalırken FAN-3 kapanır: geçiş kaydı.

Yükler paralel bağlanır; aynı akım yolundan geçen toplam hat akımı SCT tarafından gözlenir. Paralel yük akımları faz açıları nedeniyle basit aritmetik toplam kabul edilmeyecektir.

## Ölçüm ve kayıt gereksinimleri

- Her durum için UNIT ölçümü; mümkünse aynı kararlı pencerede PZEM akım, aktif güç ve PF.
- SCT akım yayını, Raw AC, bias ve ADC değerleri.
- Açma/kapama olaylarının kesin zaman notu veya olay işareti.
- Kararlı pencere başlangıç/bitiş zamanları ve yayın sayısı.
- ESPHome sürümü, kullanılan YAML snapshot/commit, Modül 2 bağlantısı ve besleme koşulu.
- Ham log, kaynak SHA-256, analiz ve yorum.

## Mevcut donanım bağlantısı

- SCT-1 sarı sinyal: GPIO32 / ADC1_CH4.
- Ortak bias turuncu: GPIO35 / ADC1_CH7.
- Modül 2'de aynı ESP düğümü tek aktif SCT kanalını okur.
- Mevcut firmware çalışma ayarları önceki FAN-3 kapanış snapshot'ında kayıtlıdır; bu test için yeni firmware değişikliği varsayılmamıştır.

## Değerlendirme kuralları

- 0,30 A ve üzerindeki kararlı pencerelerde, eşleşmiş referans mevcutsa ±%4 kıyası yapılabilir.
- 0,30 A altındaki bölgede ±%4 kabul/ret uygulanmaz; düşük akım araştırma sınıfı olarak tutulur.
- UNIT ve PZEM ayrı kaynaklardır; birbirlerinin yerine yazılmaz.
- PZEM referansı bulunmadan PF etkisi doğrulanmış sayılmaz.
- SCT tek başına PF veya yük bileşenlerinin ayrı akımlarını vermez.
- K=24.22 korunur; kullanıcı kararı olmadan yazılımsal sıfır eşiği eklenmez.
- Test kapanışında kullanılan son YAML ayrı snapshot olarak arşivlenir; ham log ve analiz o snapshot'a bağlanır. Önceki kodlar üzerine yazılmaz.

## İlk durum

Henüz karma yük bağlantısı yapıldığı, UNIT/PZEM değeri alındığı veya SCT logu toplandığı bildirilmedi. Bu dosya test planının açılış kaydıdır; ölçüm sonucu değildir.

## Sonuç tablosu

| Aşama | UNIT | PZEM akım | PZEM PF | SCT kararlı sonuç | Log / analiz | Durum |
|---|---:|---:|---:|---:|---|---|
| 100 W yalnız | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | PLAN |
| FAN-3 yalnız | Önceki bildirim 0,141 A; yeni ölçüm bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | PLAN |
| 100 W + FAN-3 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | PLAN |
| FAN-3 açılma geçişi (100 W açık) | — | Bekliyor | Bekliyor | Bekliyor | Olay işaretli log bekliyor | PLAN |
| FAN-3 kapanma geçişi (100 W açık) | — | Bekliyor | Bekliyor | Bekliyor | Olay işaretli log bekliyor | PLAN |
