# 42 W Ampul — Düşük Akım Gözlem Kaydı

**Test ID:** LOAD-42W-001  
**Yük:** 42 W ampul (ampul teknolojisi/etiket bilgisi henüz ayrıca doğrulanmadı)  
**Amaç:** 42 W ampulün düşük akım koşulunda Modül 2 / SCT-1 ölçüm davranışını gözlemek ve UNIT referansıyla aynı kararlı pencerede karşılaştırma için veri toplamak.  
**Durum:** AÇIK — ilk SCT-1 logu analiz edildi; eşzamanlı UNIT/PZEM referansı ve ampul ayrıntıları bekleniyor.

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


## 2026-10-31 — LOAD-42W-001 / Log 57 SCT-1 gözlemi

- **KAYNAK:** `esp32d1-logs (57).txt`; 55.924 bayt / 766 satır; SHA-256 `f519f752ea4466e82cc365dac832e3338195303e920520414e7be6538d0203ae`.
- **ZAMAN:** İlk/son SCT akım yayını 21:09:28–21:12:38 (+03:00); 96 yayın, yaklaşık 3 dk 10 sn.
- **DÜZENEK:** ESP32D1 / Modül 2 / SCT-1 GPIO32 ADC1_CH4 / ortak bias GPIO35 ADC1_CH7; ESPHome 2026.10.1; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s. K=24.22 mevcut firmware referansıdır; log binary eşleşmesini tek başına kanıtlamaz.
- **SCT AKIM:** Ortalama 0,252438 A; medyan 0,251 A; min–maks 0,221–0,295 A; örnek SD 0,011038 A; CV %4,37. 96/96 yayın 0,30 A altındadır.
- **ANALOG:** Raw AC ortalaması 0,0104248 V (0,00914–0,01218 V); ortak bias GPIO35 ortalaması 1,663469 V (1,656–1,673 V); SCT-1 ADC GPIO32 ortalaması 1,660745 V (1,632–1,678 V). Loglanan SPS ortalaması 17.354,8 (16.840–17.675).
- **ZAMAN İÇİ DAVRANIŞ:** Ardışık 24 örnekli dört blok ortalaması 0,25421 / 0,25392 / 0,24988 / 0,25175 A. Bu kısa kesitte belirgin uzun dönemli trend yok. ERROR/[E] satırı görülmedi.
- **UNIT SINIRI:** LOAD-42W-001 açılışında bildirilen UNIT 0,174 A ile log ortalaması arasındaki betimleyici fark +0,078438 A (+%45,08); medyan farkı +%44,25. UNIT değerinin logla aynı kararlı zaman penceresinde alındığı doğrulanmadığından bu eşzamanlı sapma/doğruluk sonucu değildir. PZEM verisi yoktur.
- **SONUÇ:** 42 W test yükünde SCT-1 yaklaşık 0,25 A çevresinde düzenli yayın üretmiştir. Bu 0,30 A altı düşük akım gözlemidir; ±%4 kabul/ret, kalibrasyon veya doğruluk onayı değildir. Test açık kalır; K ve firmware değiştirilmez.
- **ANALİZ:** [Log 57 teknik analiz](../../logs/module2/2026-10-31-load-42w-001-log57-analysis.md).
- **HAM KAYNAK:** Kullanıcı yüklemesi bu konuşmada korunmaktadır; ham TXT'nin GitHub'a tam kopyası bu güncellemede yapılmadı. Kaynak adı, boyutu ve SHA-256 kaydedildi.
