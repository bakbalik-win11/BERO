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


## 2026-11-07 — LOAD-57W-002 / 57 W sürekli açık, PZEM + CH1 HA History

### HEDEF VE KOŞUL

- **Yük:** 57 W akkor ampul; kullanıcı bildirimi.
- **İşletim:** Ampul sürekli açık; test yükü için aç/kapa çevrimi uygulanmadı.
- **Düzenek:** ESP32D1 / Modül 2 / CH1-1T Faz (GPIO32) ve Modül 3 WROOM / PZEM-004T V3.0.
- **Zaman:** 2026-11-07 13:00:00–14:09:59.705 (Europe/Istanbul), yaklaşık 70 dakika.
- **Kaynak:** Home Assistant History CSV, `57w 1 saat.csv`; 10.947 satır / 945.098 bayt; SHA-256 `53afb448f95a722c37680511f1e2ad7cce8c32ee190b7828be6d7f17a2cea50c`.
- **Ham CSV:** Kullanıcı kaynağı olarak korunur; bu kayıt istatistik/yorum özetidir. CSV Git'e eklenmedi.

### PZEM — LOG İLE DESTEKLENDİ

| Parametre | Örnek | Ortalama | Min–Maks |
|---|---:|---:|---:|
| Akım | 192 | 0,26307 A | 0,261–0,265 A |
| Güç | 642 | 59,8405 W | 58,6–60,9 W |
| Gerilim | 752 | 227,7117 V | 224,8–230,4 V |
| Frekans | 179 | 49,9503 Hz | 49,9–50,0 Hz |
| Güç faktörü | 1 | 1,00 | Tek kayıt; istatistiksel temsil gücü yok |

### CH1 — LOG İLE DESTEKLENDİ

Entity: `sensor.esp32d1_bero_mod2_ch1_1t_faz_akim`; ham SCT entity'si ayrıca kaydedildi.

| İstatistik | CH1 hesaplanan akım |
|---|---:|
| Örnek sayısı | 4.201 |
| Ortalama | 0,35550 A |
| Medyan | 0,35403 A |
| Standart sapma (örnek) | 0,01786 A |
| Değişim katsayısı | %5,02 |
| P95 | 0,38632 A |
| P99 | 0,40664 A |
| Min–Maks | 0,31097–0,49263 A |
| 0,41 A üzeri | 32 / 4.201 (%0,76) |
| 0,45 A üzeri | 2 / 4.201 (%0,048) |
| 0,50 A üzeri | 0 |

Ham SCT entity ortalaması: 0,014678 A (4.201 örnek). Ham SCT entity değeri, CH1 hesaplanan akım entity'si ve PZEM akımı farklı ölçüm/işleme katmanlarıdır; doğrudan birbirinin yerine kullanılmaz.

### ZAMAN İÇİNDE DAVRANIŞ

10 dakikalık CH1 ortalamaları: 0,3542 / 0,3540 / 0,3540 / 0,3574 / 0,3577 / 0,3557 / 0,3554 A. Ortalama seviye yaklaşık sabit kalmıştır. 18 W oturumuna göre sıçrama dağılımı ve standart sapma daha düşüktür.

### YORUM VE SINIR

- PZEM, 70 dakika boyunca yaklaşık 0,263 A / 59,84 W düzeyinde kararlı yük kaydı üretmiştir.
- CH1 yaklaşık 0,3555 A ortalama ve %5,02 CV ile bu oturumda daha dar bir dağılım göstermiştir.
- CH1'in 0,24–0,41 A aralığı mevcut proje kararı gereği **hesaplanmadı alanıdır**. Ortalama 0,3555 A bir doğru akım ölçümü/kalibrasyon sonucu değildir.
- P99 değeri 0,41 A sınırının hemen altındadır; 32 örnek bu sınırı aşmış, maksimum 0,4926 A olmuştur. Sıçramalar tamamen kaybolmamıştır.
- PZEM PF için tek kayıt vardır; PF kararlılığı veya PF etkisi hakkında sonuç çıkarılmaz.
- 18 W ve 57 W oturumları farklı zamanlarda yapılmıştır. Dağılım farkı gözlenmiştir; yük gücünün tek başına bu farka neden olduğu kanıtlanmamıştır.
- Firmware/K=24.22 değiştirilmedi; filtre veya sıfır eşiği eklenmedi.

### SONUÇ

LOAD-57W-002, 57 W sürekli yükte CH1 davranışının 70 dakikalık gözlem kaydı olarak **analiz edildi**. Düşük akım hesaplanmadı alanı sınıflandırması değişmez. Bu kayıt kalibrasyon veya ±%4 doğrulaması değildir.


## 2026-11-13 — E19 ADS1115 ile yeni 57 W oturumu (ayrı deney)

Bu kayıt, eski LOAD-57W-001/002 ESP32D1 dahili ADC deneylerini değiştirmez veya onlarla birleştirmez.

- **Yük:** 57 W nominal akkor ampul; kullanıcı düzeltmesi.
- **Başlangıç:** 18:32 (+03:00), kullanıcı bildirimi.
- **Ölçüm mimarisi:** ESP32D2 ADS1115 + ct_clamp; Modül 3 PZEM proje referansı; Modül 2 CH1-1T varsa ikincil kanal.
- **İşletim:** sürekli bağlı sabit yük; aç/kapa geçiş deneyi değil.
- 150 W E19 deneyiminden hareketle ilk 3 dakika geçici/ısınma bölgesi kabul edilir; kararlı pencere PZEM ve ADS/SCT serileri oturduktan sonra seçilir.
- İlk karşılaştırmada E19 ayarları korunur; gain 2.048, 860 SPS, 200 ms, 2 s, accuracy_decimals 2 ve 0.05 A filtre değiştirilmez.
- PZEM ile karşılaştırma yalnız ortak kararlı zaman penceresinde yapılır. Nominal 57 W teorik akım hesabı referans değildir.
- **Durum:** Başlangıç bildirimi kaydedildi; yeni E19 logu/CSV henüz yok. Eski 2026-11-07 LOAD-57W-002 sonuçları tarihsel Modül 2 kaydıdır.
- Ayrıntı: [E19 57 W oturum planı](../../logs/ads1115/2026-11-13-E19-57w-test.md).
