# 57 W Akkor Ampul — Düşük Akım Gözlem Kaydı

**Test ID:** LOAD-57W-001  
**Yük:** 57 W akkor ampul (kullanıcı tarafından bildirildi)  
**Amaç:** 57 W akkor yükte Modül 2 / SCT-1 ölçüm davranışını gözlemek ve UNIT referansıyla örtüşen kararlı pencerede karşılaştırma için veri toplamak.  
**Durum:** AÇIK — test yükü ve başlangıç UNIT değeri kaydedildi; SCT logu ve eşzamanlı referans penceresi bekleniyor.

## Başlangıç referansı

- **UNIT:** 0,244 A.
- **Kanıt sınıfı:** KULLANICI BİLDİRİMİ.
- **Yük:** 57 W akkor ampul; tür kullanıcı tarafından açıkça belirtildi.
- **Yorum:** UNIT değeri başlangıç referansı olarak kaydedilmiştir. Değerin kararlı pencere ortalaması olup olmadığı ve SCT loguyla zaman örtüşmesi henüz doğrulanmadı.
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
- UNIT 0,244 A ile SCT kıyası, yalnız aynı fiziksel yük ve örtüşen kararlı pencere doğrulanırsa yapılacak.
- 0,244 A, BERO'nun 0,30 A altı düşük akım gözlem bölgesindedir; ±%4 kabul/ret uygulanmayacak.
- PZEM verisi varsa ayrı referans olarak kaydedilecek; UNIT ve PZEM birleştirilmeyecek.

## Beklenen kayıtlar

1. 57 W nominal gücü ve akkor tipini gösteren ampul etiketi/fotoğrafı (varsa marka/model).
2. SCT-1 Modül 2 logu ve kaynak dosya kimliği/hash'i.
3. UNIT 0,244 A değerinin test boyunca kararlı olup olmadığı ve ölçüm zamanı.
4. Varsa aynı kararlı penceredeki PZEM akım/PF verisi.
5. Teknik analiz, sonuç ve açık sınırlamalar.

## Güvenlik

SCT yalnız tek yalıtılmış iletkeni çevrelemelidir; faz ve nötr birlikte geçirilmez. CT/kablo bağlantısı değiştirilirken enerji kesilir. Şebeke bağlantıları kapalı ve uygun korumalı lamba düzeneğinde tutulur.

## İlk durum

**PLANLANDI / AÇIK.** Şu an yalnız 57 W akkor ampul yük tanımı ve UNIT 0,244 A kullanıcı bildirimi mevcut. SCT ölçümü, eşzamanlı UNIT kararlılığı ve PZEM karşılaştırması henüz yok.
