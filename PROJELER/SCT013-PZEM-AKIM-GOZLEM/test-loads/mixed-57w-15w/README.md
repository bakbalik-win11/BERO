# 57 W + 15 W Ampul — Karma Yük Test Kaydı

**Test ID:** MIXED-LOAD-57W-15W-001  
**Yük:** 57 W akkor ampul + 15 W ampul (15 W ampul tipi/teknolojisi henüz belirtilmedi)  
**Nominal güç toplamı:** 72 W (etiket değerlerinin aritmetik toplamı; gerçek çekilen güç ölçümü değildir)  
**Amaç:** İki ampul birlikte çalışırken Modül 2 / SCT-1 çıktısının dağılımını ve kararlılığını gözlemek; UNIT başlangıç referansıyla karşılaştırılabilir pencere oluşturmak.  
**Durum:** AÇIK — Log 59 arşivlendi ve analiz edildi; test için belirlenen ±%5,6 bandı karşılanmadı. Alt 0,250 A eşiği altında yayın görülmedi.

## Başlangıç referansı

- **UNIT:** 0,303 A.
- **Kanıt sınıfı:** KULLANICI BİLDİRİMİ.
- **Yük:** 57 W akkor + 15 W ampul.
- **Ölçüm zamanı:** Açılış mesajında saat belirtilmedi.
- **Kararlılık:** Kullanıcı, UNIT 0,303 A değerinin test boyunca sabit kaldığını; değişirse bildireceğini belirtti (KULLANICI BİLDİRİMİ).
- **PZEM:** Bu açılışta PZEM değeri verilmedi. UNIT ile karıştırılmayacaktır.

## Düzenek — mevcut Modül 2 başlangıç yapılandırması

- ESPHome düğümü: `esp32d1` / ESP32D1.
- Modül: Modül 2.
- Aktif SCT kanalı: SCT-1; sarı sinyal GPIO32 / ADC1_CH4.
- Ortak bias: turuncu GPIO35 / ADC1_CH7.
- Firmware referansı: [firmware/esp32d1.yaml](../../firmware/esp32d1.yaml).
- Mevcut kayıtlı ayarlar: ESPHome 2026.10.1; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s; K=24.22; yazılımsal sıfır eşiği yok.
- **Kod kilidi:** Bu deneyde firmware ve K değiştirilmeden gözlem yapılacaktır. Değişiklik gerekirse önce ayrı karar alınır.

## Değerlendirme planı

- SCT-1 yayın sayısı, ortalama, medyan, min–maks, standart sapma ve değişim katsayısı çıkarılacak.
- Raw AC ve GPIO35 bias istatistikleri birlikte incelenecek.
- Zaman içindeki kararlılık ve aykırı örnekler ayrı değerlendirilecek.
- Kullanıcı bu test için UNIT 0,303 A referansına göre ±%5,6 toleransı kabul edilebilir belirledi; hesap bandı 0,286032–0,319968 A'dır. 0,250 A ve altı başarısız eşik olarak işaretlenir.
- UNIT değerinin test boyunca sabit kaldığı kullanıcı bildirimi esas alınarak Log 59 yayınlarıyla bu test için yüzde dağılımı hesaplandı; UNIT değeri log içinde ayrı kanal olarak kayıtlı değildir.
- 0,303 A, BERO'nun 0,30 A gözlem sınırının hemen üzerindedir. Eşleşmiş kararlı pencere varsa ±%4 kıyası yapılabilir; sınırın altında kalan yayınlar ayrıca düşük akım gözlemi olarak raporlanır.
- PZEM verisi varsa ayrı referans olarak kaydedilecek; UNIT ve PZEM birleştirilmeyecek.

## Beklenen kayıtlar

1. İki ampulün birlikte açık olduğu koşul ve mümkünse etiket/fotoğraf bilgisi.
2. SCT-1 Modül 2 logu ve kaynak dosya kimliği/hash'i.
3. UNIT 0,303 A değerinin test boyunca kararlılığı ve ölçüm zamanı.
4. Varsa aynı kararlı penceredeki PZEM akım/PF verisi.
5. Teknik analiz, sonuç ve açık sınırlamalar.

## Güvenlik

SCT yalnız tek yalıtılmış iletkeni çevrelemelidir; faz ve nötr birlikte geçirilmez. CT/kablo bağlantısı değiştirilirken enerji kesilir. Şebeke bağlantıları kapalı ve uygun korumalı lamba düzeneğinde tutulur.

## İlk durum

**PLANLANDI / AÇIK.** Şu an yalnız 57 W akkor + 15 W ampul yük koşulu ve UNIT 0,303 A kullanıcı bildirimi mevcut. SCT ölçümü, UNIT kararlılığı ve PZEM karşılaştırması henüz yok.


## 2026-10-31 — Log 59 analizi

- **KAYNAK:** `esp32d1-logs (59).txt`; 99.807 bayt / 1.349 satır; SHA-256 `6e7dea5c6c8991a6d4f915ebd6182f3de82b151d5726066700840f21a7d7124a`.
- **ZAMAN:** 21:20:18.203–21:26:14.218 (+03:00); 179 SCT-1 yayını.
- **UNIT:** 0,303 A'nın test boyunca sabit kaldığı kullanıcı tarafından bildirildi.
- **SCT:** Ortalama 0,329553 A; medyan 0,328 A; min–maks 0,303–0,436 A; SD 0,014762 A; CV %4,48.
- **±%5,6 bandı:** 0,286032–0,319968 A. 31/179 (%17,32) yayın bant içinde; 148/179 (%82,68) üstünde; bant altında yayın yok.
- **Sapma:** Ortalama +%8,76; medyan +%8,25.
- **0,250 A alt eşiği:** 0/179 yayın bu eşik altında veya eşit; tüm yayınlar 0,250 A üzerinde.
- **ANALOG:** Raw AC ortalama 0,013604 V; ortak bias GPIO35 ortalama 1,663504 V; SCT-1 ADC GPIO32 ortalama 1,663869 V; SPS ortalama 17.586.
- **SONUÇ:** ±%5,6 tolerans hedefi yayınların yalnız %17,32'siyle karşılandı; ortalama/medyan hedef bandının üstünde olduğundan test bu kritere göre başarılı değildir. 0,250 A altına düşülmemesi alt eşik açısından olumlu gözlemdir; ayrı bir kabul sonucudur. PZEM verisi yoktur.
- **KOD:** Firmware ve K=24.22 değiştirilmedi.
- **ARŞİV:** [analiz](../../logs/module2/2026-10-31-mixed-load-57w-15w-001-module2-sct1-analysis.md); [tam ham log](../../logs/module2/2026-10-31-mixed-load-57w-15w-001-module2-sct1-full.txt).
- **DURUM:** Test AÇIK kalır; 15 W ampulün tipi henüz belirtilmedi.
