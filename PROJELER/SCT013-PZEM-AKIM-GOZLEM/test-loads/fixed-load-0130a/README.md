# FIXED-LOAD-0130A-001 — 0,130 A sabit yük gözlem testi

## HEDEF
0,130 A civarında sabit bir yük koşulunda Modül 2 / SCT-1 çıktısının davranışını gözlemek. Bu kayıt düşük akım bölgesindeki gözlem ve karşılaştırma çalışmalarına aittir.

## BAŞLANGIÇ BİLGİSİ
- **Durum:** PLANLANDI — fiziksel test ve ESP32D1 logu bekleniyor.
- **Referans/hedef akım:** 0,130 A.
- **Kaynak sınıfı:** KULLANICI BİLDİRİMİ. Kullanıcı bu değeri sabit yük testi için bildirdi.
- **Ölçüm cihazı:** Henüz belirtilmedi; UNIT veya PZEM olarak varsayılmayacak.
- **Yükün kimliği/gücü:** Henüz belirtilmedi.
- **Ölçüm durumu:** Kullanıcı şu anda ölçüm alınamadığını belirtti. 0,130 A doğrulanmış ölçüm veya SCT sonucu değildir.

## DÜZENEK / KOD KİLİDİ
- ESP32D1 / Modül 2 / SCT-1: sarı sinyal GPIO32 (ADC1_CH4).
- Ortak bias: turuncu GPIO35 (ADC1_CH7).
- Mevcut ESPHome yapılandırması korunacak.
- K=24.22 korunacak; yazılımsal sıfır eşiği eklenmeyecek.
- Test sırasında firmware/katsayı değişikliği yapılmayacak.

## DEĞERLENDİRME
- 0,130 A, BERO'nun 0,30 A altı düşük akım gözlem bölgesindedir.
- Bu bölgede ±%4 kabul/ret uygulanmaz.
- SCT akım çıktısı, Raw AC, bias ve zaman içindeki kararlılık/dağılım birlikte incelenecek.
- Referans cihaz ve eşzamanlı kararlı pencere bilgisi sağlanmadan sapma hesabı yapılmayacak.

## BAĞLANTILAR VE GÜVENLİK
SCT-1 sinyali GPIO32'ye, ortak bias GPIO35'e bağlıdır. CT yalnız tek yalıtılmış faz iletkenini çevrelemelidir; faz ve nötr birlikte CT'den geçirilmez. Fiziksel bağlantı değişikliği enerji kesilerek yapılır. Şebeke tarafı açıkta bırakılmaz.

## BEKLENEN ÇIKTI
En az 30 geçerli yayınlık bir gözlem penceresi; logda akım, Raw AC ve bias değerleri. Test başladığında yük kimliği, referans cihaz/değer, başlangıç-bitiş zamanı ve kararlı bölüm ayrıca kaydedilecek.

## AÇIK NOKTALAR
1. Fiziksel yükün adı/gücü.
2. 0,130 A değerini gösterecek referans cihaz.
3. Gerçek test başlangıcı ve SCT logu.

**Sonuç:** Henüz ölçüm yok; bu dosya yalnızca test planıdır.

## 2026-10-31 — İlk SCT-1 log gözlemi

- **KAYNAK:** `esp32d1-logs (56).txt`; 298.344 bayt / 3.986 satır; SHA-256 `15c94083291b374e60f80d932494d6a6a58cbef9b5a3d82227cc2f58703dc20a`.
- **ZAMAN:** İlk/son SCT akım yayını 20:47:30–21:06:00 (+03:00); 556 yayın.
- **DÜZENEK:** ESP32D1 / Modül 2 / SCT-1 GPIO32 / ortak bias GPIO35; ESPHome 2026.10.1; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s; log SPS ortalaması 17.171.
- **SCT:** Ortalama 0,203637 A; medyan 0,203 A; min–maks 0,157–0,291 A; SD 0,017971 A; CV %8,82.
- **ANALOG:** Raw AC ortalaması 0,0084077 V; bias GPIO35 ortalaması 1,663729 V (1,647–1,675 V).
- **ZAMAN DAVRANIŞI:** Yaklaşık iki dakikalık blok ortalamaları 0,1993–0,2081 A aralığında; uzun dönemli ortalamada belirgin sürüklenme yok. Dağılım ve kısa süreli yüksek örnekler mevcut.
- **REFERANS SINIRI:** 0,130 A test hedefidir; logda UNIT/PZEM referansı veya fiziksel yük kimliği doğrulanmadı. Bu nedenle 0,203637 A SCT ortalaması ile 0,130 A hedef arasında sapma/doğruluk hesabı yapılmaz.
- **YORUM:** SCT-1 yaklaşık 18,5 dakika düzenli yayın üretmiş ve ortalama yaklaşık 0,20 A çevresinde kalmıştır. Bu, 0,130 A'nın doğrulandığı anlamına gelmez. 0,30 A altı gözlem bölgesinde ±%4 kabul/ret yoktur.
- **DURUM:** Log analiz edildi; test referans ve fiziksel yük koşulu netleşene kadar nihai doğrulama olarak kapatılmadı. K=24.22 korunur; yazılımsal sıfır eşiği eklenmez.
- **ANALİZ:** [FIXED-LOAD-0130A-001 teknik analiz](../../logs/module2/2026-10-31-fixed-load-0130a-001-sct1-analysis.md).
- **HAM KAYNAK:** Tam TXT kullanıcı yüklemesinde korunuyor; bu committe Git'e tam metin aktarılmadı. Dosya adı, boyutu ve SHA-256 yukarıda kayıtlı.
