# 57 W + 15 W Ampul — Karma Yük Test Kaydı

**Test ID:** MIXED-LOAD-57W-15W-001  
**Yük:** 57 W akkor ampul + 15 W ampul (15 W ampul tipi/teknolojisi henüz belirtilmedi)  
**Nominal güç toplamı:** 72 W (etiket değerlerinin aritmetik toplamı; gerçek çekilen güç ölçümü değildir)  
**Amaç:** İki ampul birlikte çalışırken Modül 2 / SCT-1 çıktısının dağılımını ve kararlılığını gözlemek; UNIT başlangıç referansıyla karşılaştırılabilir pencere oluşturmak.  
**Durum:** AÇIK — yük ve UNIT başlangıç değeri kaydedildi; SCT logu bekleniyor.

## Başlangıç referansı

- **UNIT:** 0,303 A.
- **Kanıt sınıfı:** KULLANICI BİLDİRİMİ.
- **Yük:** 57 W akkor + 15 W ampul.
- **Ölçüm zamanı:** Açılış mesajında saat belirtilmedi.
- **Kararlılık:** UNIT değerinin test boyunca kararlı olup olmadığı ve SCT loguyla zaman örtüşmesi henüz doğrulanmadı.
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
- UNIT 0,303 A ile SCT kıyası, aynı fiziksel yük ve örtüşen kararlı pencere doğrulanırsa yapılacak.
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
