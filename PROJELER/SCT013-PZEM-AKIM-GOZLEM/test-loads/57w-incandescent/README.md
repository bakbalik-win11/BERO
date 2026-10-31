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


## 2026-10-31 — Log 58 / SCT-1 ölçüm analizi

- **KAYNAK:** `esp32d1-logs (58).txt`; 66.456 bayt / 906 satır; SHA-256 `f5a2d958dc2c85ec204516240c99ec2e87b519a422958a9ddd1cf122b4ee8d08`.
- **ZAMAN:** İlk/son SCT akım yayını 21:14:44–21:18:34 (+03:00); 116 yayın.
- **SCT AKIM:** Ortalama 0,304207 A; medyan 0,303 A; min–maks 0,284–0,348 A; örnek SD 0,009126 A; CV %3,00. 31/116 yayın 0,30 A altında, 85/116 yayın 0,30 A ve üzerindedir.
- **BLOK DAVRANIŞI:** Ardışık 29 örnekli dört blok ortalaması 0,3061 / 0,3022 / 0,3046 / 0,3040 A. Belirgin uzun dönemli yükselme/düşme görünmüyor.
- **ANALOG:** Raw AC ortalaması 0,012562 V (0,01173–0,01436 V); GPIO35 bias ortalaması 1,663073 V (1,651–1,672 V); GPIO32 ADC ortalaması 1,660694 V (1,642–1,683 V). Log SPS ortalaması 17.768 (17.280–18.260).
- **UNIT SINIRI:** Başlangıç UNIT bildirimi 0,244 A. SCT ortalamasıyla salt aritmetik fark +0,060207 A / +%24,67; medyan farkı +%24,18. UNIT zamanının logdaki kararlı pencereyle örtüşmesi teyitsiz olduğundan bu eşzamanlı sapma veya doğruluk sonucu değildir. PZEM verisi yoktur.
- **YORUM:** SCT çıktısı bu oturumda kendi içinde görece kararlıdır (CV %3,00), ancak ölçüm dağılımı 0,30 A BERO gözlem sınırının iki tarafına yayılır. 0,30 A altı düşük akım değerlendirmesinde ±%4 kabul/ret uygulanmaz. Firmware/K=24.22 değiştirilmedi; tek logdan katsayı çıkarılmadı.
- **DURUM:** Test AÇIK kalır; UNIT'in aynı zamanlı kararlı pencerede tekrar kaydı ve mümkünse PZEM akım/PF verisi beklenir.
- **ANALİZ:** [Log 58 teknik analiz](../../logs/module2/2026-10-31-load-57w-001-module2-sct1-analysis.md).
- **HAM LOG:** [Log 58 tam ham TXT](../../logs/module2/2026-10-31-load-57w-001-module2-sct1-full.txt); dosya GitHub'a eksiksiz kaydedildi.
