# 42 W Ampul — Düşük Akım Gözlem Kaydı

**Test ID:** LOAD-42W-001  
**Yük:** 42 W ampul (ampul teknolojisi/etiket bilgisi henüz ayrıca doğrulanmadı)  
**Amaç:** 42 W ampulün düşük akım koşulunda Modül 2 / SCT-1 ölçüm davranışını gözlemek ve UNIT referansıyla aynı kararlı pencerede karşılaştırma için veri toplamak.  
**Durum:** AÇIK — test kaydı oluşturuldu; SCT logu ve fiziksel koşul ayrıntıları bekleniyor.

## Başlangıç referansı

- **UNIT:** 0,174 A.
- **Kanıt sınıfı:** KULLANICI BİLDİRİMİ.
- **Yorum:** Kullanıcı tarafından bildirilen UNIT değeri başlangıç referansı olarak kaydedilmiştir. Değerin kararlı pencere ortalaması olup olmadığı henüz ayrıca teyit edilmedi.
- **PZEM:** Bu açılış bilgisinde PZEM değeri verilmedi; UNIT ile karıştırılmayacaktır.
- **Ölçüm zamanı:** Test açılış mesajında saat belirtilmedi.

## Düzenek — mevcut Modül 2 başlangıç yapılandırması

- ESPHome düğümü: `esp32d1` / ESP32D1.
- Modül: Modül 2.
- Aktif SCT kanalı: SCT-1; sarı sinyal GPIO32 / ADC1_CH4.
- Ortak bias: turuncu GPIO35 / ADC1_CH7.
- Firmware referansı: [firmware/esp32d1.yaml](../../firmware/esp32d1.yaml).
- Mevcut kayıtlı ayarlar: ESPHome 2026.10.1; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s; K=24.22; yazılımsal sıfır eşiği yok.
- **Kod kilidi:** Bu deneyde firmware ve K değiştirilmeden gözlem yapılacaktır. Değişiklik gerekirse önce ayrı karar alınır.

## Değerlendirme planı

- SCT-1 akım örnek sayısı, ortalama, medyan, min–maks, standart sapma ve değişim katsayısı çıkarılacak.
- Raw AC ve GPIO35 bias istatistikleri birlikte incelenecek.
- Zaman içindeki kararlılık ve aykırı örnekler ayrı değerlendirilecek.
- UNIT 0,174 A ile SCT kıyası, yalnız aynı fiziksel yük ve örtüşen kararlı pencere doğrulanırsa yapılacak.
- Bu test 0,30 A altı düşük akım gözlem bölgesindedir; BERO kuralı gereği ±%4 kabul/ret uygulanmayacak.
- PZEM verisi varsa ayrı referans olarak kaydedilecek; UNIT ve PZEM birleştirilmeyecek.

## Beklenen kayıtlar

1. Ampul etiketinin fotoğrafı veya marka/modeli; 42 W gücün ampul üzerindeki nominal değer olduğunun teyidi.
2. SCT-1 Modül 2 logu ve kaynak dosya kimliği/hash'i.
3. UNIT 0,174 A değerinin test boyunca kararlı olup olmadığı ve ölçüm zamanı.
4. Varsa aynı kararlı penceredeki PZEM akım/PF verisi.
5. Teknik analiz, sonuç ve açık sınırlamalar.

## Güvenlik

SCT yalnız tek yalıtılmış iletkeni çevrelemelidir; faz ve nötr birlikte geçirilmez. CT/kablo bağlantısı değiştirilirken enerji kesilir. Şebeke bağlantıları kapalı ve uygun korumalı lamba düzeneğinde tutulur.

## İlk durum

**PLANLANDI / AÇIK.** Şu an yalnız UNIT 0,174 A kullanıcı bildirimi ve 42 W ampul yük tanımı mevcut. SCT ölçümü, PZEM karşılaştırması ve test sonucu henüz yoktur.
