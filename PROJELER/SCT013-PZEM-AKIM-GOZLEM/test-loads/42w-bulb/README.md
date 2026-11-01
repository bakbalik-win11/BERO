
 
## 2026-11-01 — LOAD-42W-002 kısa log ve HA geçmiş teşhisi

- **KAYNAK:** `Yapıştırılan metin(20261101-101343).txt`, 50.257 bayt / 668 satır, SHA-256 `0c316527df2df9105d8745dd1fd009d41c9f7f7150d4e0ea95e0377f8165a3fd`.
- **SÜRE:** 13:12:20.893–13:13:28.860 (+03:00), yaklaşık 68 saniye / 34 çevrim.
- **ÇALIŞMA:** Wi-Fi YES (-62 dB); GPIO32/33/34/35 ADC init/config/calibration OK; üç SCT çevrimi ve bias okuması tamamlandı; ERROR/[E]/Disconnected bulunmadı.
- **ORTALAMALAR:** SCT1 0.25106 A; SCT2 0.24150 A; SCT3 0.34732 A; bias 1.66147 V.
- **ÖNEMLİ GÖZLEM:** SCT3/SCT1 oranı 1.383; bu kısa kesitte 2T/1T için yaklaşık 2x gözlenmedi. Neden henüz belirlenmedi.
- **KOD DENETİMİ:** `ct_clamp.on_raw_value` ile gelen filtre öncesi ham değer logda A olarak yazılıyor; YAML bu değeri `V` birimli Raw AC entity'ye yayımlıyor. Raw AC entity birimi/semantiği yanlış etiketli. Bu HA Recorder'ı durdurmaz, ancak veriyi yanlış tanımlar. Firmware düzeltmesi henüz yapılmadı.
- **HA SINIRI:** `api:` sunucusu dinliyor; log ESPHome CLI bağlantısını gösteriyor, HA API istemcisinin bağlantısını kanıtlamıyor. `force_update: true` Recorder ayarını etkinleştirmez. Canlı state ve History ayrımı HA Developer Tools → States ile kontrol edilmeli.
- **ANALİZ:** [Kısa log / kod denetimi / HA teşhisi](../../logs/module2/2026-11-01-load-42w-002-short-log-ha-diagnostic.md).
- **DURUM:** Firmware kısa çevrimi LOG İLE DESTEKLENDİ. HA geçmiş sorunu çözülmedi; uzun kayıt doğrulanmadı.
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

 
## 2026-11-01 — LOAD-42W-002 açıldı: üç SCT / HA uzun kayıt

**Test ID:** LOAD-42W-002  
**Durum:** AÇIK — YAML kullanıcı bildirimiyle derlendi; HA geçmiş aktarımı ve uzun süreli cihaz kaydı henüz doğrulanmadı.

### Amaç
42 W ampul yükünde Modül 2'nin üç SCT kanalını uzun süreli çalıştırarak akım, Raw AC ve ortak bias değerlerinin Home Assistant'a aktarılmasını ve HA History/Recorder geçmişinde tutulmasını gözlemek. Özellikle SCT3'ün iki primer turdaki davranışının zaman içindeki kararlılığı incelenecek.

### Fiziksel kanal düzeni
| Kanal | İletken | Primer tur | ESP32D1 pini |
|---|---|---:|---|
| SCT1 | Faz | 1T | GPIO32 / ADC1_CH4 |
| SCT2 | Nötr | 1T | GPIO33 / ADC1_CH5 |
| SCT3 | Faz | 2T | GPIO34 / ADC1_CH6 |
| Ortak bias | Ortak bias hattı | — | GPIO35 / ADC1_CH7 |

SCT2 nötrü ayrı izler. Faz ve nötr aynı SCT açıklığından birlikte geçirilmez. SCT3'te iki tur, faz iletkeninin CT açıklığından iki geçişidir; sensörün sekonder kablosu sarılmaz.

### Firmware ve sabitler
- ESPHome düğümü: `esp32d1` / ESP32D1; Modül 2.
- ESPHome: 2026.10.1; ESP-IDF.
- YAML snapshot: [LOAD-42W-002 üç SCT / HA geçmiş YAML](../../firmware/archive/LOAD-42W-002-2026-11-01-esp32d1-three-sct-ha-history.yaml).
- Derleme durumu: **KULLANICI BİLDİRİMİYLE DERLENDİ.** Derleme çıktısı bu kayıtla birlikte paylaşılmadı; bağımsız derleme doğrulaması yapılmadı.
- ADC attenuation: 12 dB.
- ct_clamp penceresi: 200 ms.
- Kanal slotu: 250 ms (200 ms pencere + 50 ms bekleme payı).
- Kanal sırası: SCT1 → SCT2 → SCT3 → ortak bias.
- Çevrim aralığı: 2 saniye.
- Akım katsayısı: K=24.22; değiştirilmedi.
- Akım, Raw AC ve bias sensörlerinde `force_update: true`.

### HA sensör adları
- BERO Mod2 SCT1 Faz 1T Akim
- BERO Mod2 SCT1 Faz 1T Raw AC
- BERO Mod2 SCT2 Notr 1T Akim
- BERO Mod2 SCT2 Notr 1T Raw AC
- BERO Mod2 SCT3 Faz 2T Akim
- BERO Mod2 SCT3 Faz 2T Raw AC
- BERO Mod2 Ortak Bias

### Kayıt protokolü
- Uzun kayıt için başlangıç hedefi 60 dakikadır; kullanıcı tarafından kesin süre ayrıca teyit edilene kadar öneri/hedef olarak kalır.
- HA Recorder etkinliği, entity'lerin dışlama listesinde olmaması ve gerçek History güncellemeleri kontrol edilecek.
- Başlangıç ve bitiş zamanı, saat dilimi, yükün kesintisiz çalışma durumu ve varsa kesintiler kaydedilecek.
- Üç akım kanalı, üç Raw AC kanalı ve ortak bias için yayın sayısı, ortalama, medyan, min–maks, standart sapma ve CV hesaplanacak.
- SCT3/SCT1 oranı zaman blokları bazında incelenecek; 2T verisi 1T gibi etiketlenmeyecek.
- SCT1 faz ve SCT2 nötr değerlerinin eşit olması zorunlu varsayılmayacak; sensör, yön, bağlantı ve sıralı ölçüm etkileri ayrı yorumlanacak.
- Önceki LOAD-42W-001 / Log 57 verisi tarihsel bağlamdır; yeni oturumla aynı pencereye ait referans değildir.
- 0,30 A altı BERO düşük akım sınıflandırmasında ±%4 kabul/ret uygulanmaz. Bu deney doğruluk/kalibrasyon testi değildir.

### Beklenen doğrulama
1. ESPHome cihazı üç akım, üç Raw AC ve bir bias sensörünü yayımlıyor.
2. Home Assistant'ta yedi sensörün varlığı ve güncellenmesi doğrulanıyor.
3. Recorder/History geçmişi boyunca zaman damgalı kayıtlar oluşuyor.
4. Uzun log ve HA geçmiş dışa aktarımı alınarak zaman blokları karşılaştırılıyor.

### Açık kalanlar
- HA Recorder ayarı ve geçmiş saklama süresi henüz incelenmedi.
- Cihazda OTA/çalışma ve HA History aktarımı bu kayıtta henüz doğrulanmadı.
- 60 dakikalık fiziksel kayıt henüz yapılmadı; sonuç/log yok.
