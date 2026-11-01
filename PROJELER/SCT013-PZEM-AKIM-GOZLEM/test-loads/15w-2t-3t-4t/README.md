# LOAD-15W-003 — 15 W ampul / 2T-3T-4T tek oturum karşılaştırması

**Durum:** PLANLANDI — kod ve test planı depoya eklendi; fiziksel test, UNIT başlangıç ölçümü ve yeni log henüz yok.

## HEDEF

Tek bir 15 W ampul yükü altında üç SCT kanalını aynı deney oturumunda çalıştırmak. Primer tur sayısı farklı üç ölçümü UNIT referansıyla karşılaştırmak:

- SCT1: faz, 2 primer tur → beklenen karşılaştırma değeri UNIT × 2
- SCT3: faz, 3 primer tur → beklenen karşılaştırma değeri UNIT × 3
- SCT2: nötr, 4 primer tur → beklenen karşılaştırma değeri UNIT × 4

Bu düzen, 2T / 3T / 4T ölçümlerini ayrı ayrı tekrar kurmak yerine tek test oturumunda toplar. Faz ve nötr tarafı da aynı yükte karşılaştırılır.

## DONANIM / BAĞLANTILAR

| Kanal | İletken | Primer tur | ESP32D1 girişi |
|---|---|---:|---|
| SCT1 / sarı | Faz | 2T | GPIO32 / ADC1_CH4 |
| SCT2 / yeşil | Nötr | 4T | GPIO33 / ADC1_CH5 |
| SCT3 / mavi | Faz | 3T | GPIO34 / ADC1_CH6 |
| Ortak bias / turuncu | Ortak bias | — | GPIO35 / ADC1_CH7 |

Her SCT kendi iletkenini ayrı izler. Faz ve nötr aynı SCT açıklığından birlikte geçirilmez. Tur sayısı, ilgili primer iletkenin CT çekirdeği açıklığından gerçek geçiş sayısıdır; SCT'nin sekonder kablosu sarılmaz.

## FIRMWARE

- ESPHome düğümü: `esp32d1`; ESP32D1 / Modül 2.
- YAML: [LOAD-15W-003 üç SCT YAML](../../firmware/archive/LOAD-15W-003-2026-11-01-esp32d1-15w-2t-3t-4t-unit.yaml).
- ESPHome: 2026.10.1 referans yapılandırması; ESP-IDF.
- K=24.22; ct_clamp 200 ms; slot 250 ms (200 ms pencere + 50 ms pay); çevrim 2 s.
- Okuma sırası: SCT1 faz 2T → SCT2 nötr 4T → SCT3 faz 3T → ortak bias.
- Kanallar aynı deney döngüsünde okunur, ancak **eşzamanlı örneklenmez**; ölçüm pencereleri sırayladır.
- Üç Ham Akim entity'si `on_raw_value` filtresiz akımını A birimiyle yayımlar. Önceki YAML'daki V etiketi bu yeni snapshot'ta düzeltilmiştir.
- YAML'ın derlenmesi/cihazda çalışması henüz doğrulanmadı.

## UNIT KARŞILAŞTIRMA YÖNTEMİ

UNIT, bu deneyde bağımsız referanstır; PZEM değildir. UNIT değeri logla örtüşen kararlı yük penceresinde kaydedilmelidir.

Her kanal için iki kıyas tutulur:

1. **Primer tur ölçekli karşılaştırma:** SCT1 / 2, SCT3 / 3, SCT2 / 4 değerleri UNIT ile karşılaştırılır.
2. **Doğrudan kanal çıktısı:** SCT1, SCT3 ve SCT2 ham ct_clamp akım çıktıları sırasıyla UNIT×2, UNIT×3 ve UNIT×4 ile karşılaştırılır.

UNIT lambanın ısınması veya şebeke gerilimi nedeniyle değişebileceğinden tek bir eski UNIT değeri tüm oturum için sabit kabul edilmez. Başlangıç, orta ve bitiş UNIT değerleri; saatleriyle birlikte kaydedilir. SCT log zamanlarıyla örtüşen kararlı bölüm ayrıca seçilir.

## BAŞLANGIÇ / REFERANS DURUMU

- 15 W tek ampul için bu testle eşleşen başlangıç UNIT ölçümü henüz depoda bulunmuyor.
- 57 W + 15 W karma yük Log 59, 15 W tekil yük referansı değildir; bu testte başlangıç baseline olarak kullanılmayacaktır.
- İlk fiziksel log ve UNIT değeri gelene kadar sayısal baseline: **YOK / BEKLENİYOR**.
- Testte 0,30 A altı ölçüm beklenebilir; bu bölgede BERO kuralı gereği ±%4 kabul/ret uygulanmaz. Sonuç gözlem, dağılım ve tur-normalize kıyas olarak raporlanır.

## BEKLENEN ÇIKTILAR

- Üç akım kanalı ve üç Ham Akim kanalı için örnek sayısı, ortalama, medyan, min–maks, SD ve CV.
- GPIO35 ortak bias istatistikleri.
- SCT1/2, SCT3/3 ve SCT2/4 normalize değerlerinin UNIT ile farkları.
- Faz 2T ve faz 3T arasındaki tur ölçekli tutarlılık; nötr 4T'nin faz kanallarıyla karşılaştırması.
- Başlangıç/orta/bitiş UNIT kayıtlarının kararlılık değerlendirmesi.
- Gerçek ESPHome logu, kaynak dosya boyutu/hash'i, örnek log satırı ve teknik yorum.

## GÜVENLİK

Tur bağlantılarını değiştirmeden önce yükün enerjisini kesin. Her CT yalnız tek bir yalıtılmış primer iletkeni kavrasın. Faz ve nötrü aynı CT'den birlikte geçirmeyin. Şebeke tarafı uygun muhafaza ve korumayla kurulmalıdır; yetkin kişi dışında müdahale edilmemelidir.

## DURUM / KABUL KAPILARI

- [ ] YAML derleme çıktısı alındı ve doğrulandı.
- [ ] Fiziksel bağlantı 2T faz / 4T nötr / 3T faz olarak kontrol edildi.
- [ ] UNIT başlangıç/orta/bitiş değerleri saatleriyle kaydedildi.
- [ ] Üç kanalın logları ve HA geçmişi alındı.
- [ ] Ham log hash'i ve analiz raporu depoya eklendi.
- [ ] Tur-normalize karşılaştırma ve sınırlamalar raporlandı.

**Şu anki işaret:** PLANLANDI / HAZIRLANDI. Fiziksel test yapılmadı; OK veya başarılı sonucu yok.
