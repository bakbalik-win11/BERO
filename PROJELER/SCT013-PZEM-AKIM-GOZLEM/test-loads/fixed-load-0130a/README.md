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
