# EINHELL-CHARGER-001 — Einhell pil şarj cihazı düşük akım deneyi

## Durum
**AÇIK — test planı oluşturuldu; fiziksel ölçüm ve log henüz alınmadı.**

## Amaç
Einhell pil şarj cihazının normal şarj sürecinde BERO Modül 2 / ESP32D1 / SCT-1 hattında 0,5 A altındaki akım davranışını gözlemlemek. Projenin kullanıcı tarafından belirlenen alt inceleme sınırı 0,01 A'dır. Bu testin bildirilen başlangıç akımı 0,413 A olduğundan hedef aralığa uygundur.

## Başlangıç bilgisi
- Yük: Einhell pil şarj cihazı.
- Başlangıç akımı: **0,413 A**.
- Kaynak: **KULLANICI BİLDİRİMİ**.
- Referans cihazın (PZEM, UNIT veya başka ölçü aleti) hangisi olduğu henüz belirtilmedi; 0,413 A şimdilik doğrulanmış PZEM referansı olarak sınıflandırılmaz.
- Şarj aşaması, pilin durumu ve ölçüm zamanı henüz kaydedilmedi.

## Donanım ve kod
- ESP: ESP32D1 / BERO Modül 2.
- Aktif kanal: SCT-1, sarı sinyal GPIO32 / ADC1_CH4.
- Ortak bias: turuncu hat GPIO35 / ADC1_CH7.
- Firmware: firmware/esp32d1.yaml.
- Mevcut ayarlar: ESPHome 2026.10.1; ADC 12 dB; ct_clamp örnek penceresi 200 ms; akım yayın aralığı 2 s; K=24.22.
- **Kod kilidi:** Bu test için firmware veya K katsayısı değiştirilmez; yazılımsal sıfır eşiği eklenmez.

## Uygulama sırası
1. Şarj cihazını ve bağlı pili normal, üreticinin öngördüğü şekilde çalıştır.
2. Test başlangıcında referans cihazı ve gösterdiği akımı açıkça kaydet; mümkünse PZEM akımı ile SCT logunu aynı kararlı zaman aralığında al.
3. ESP32D1 logunu şarjın başlangıcında, kararlı şarj sırasında ve şarj ilerledikçe sürdür.
4. Akım belirgin biçimde değiştiğinde her kararlı bölümün başlangıç/bitiş zamanını ve şarj aşamasını not et.
5. Ham logu değiştirmeden sakla; ortalama, medyan, min–maks, standart sapma ve kararlı pencere sonuçlarını ayrı analiz et.
6. 0,01 A altındaki değerler proje inceleme kapsamı dışındadır; 0,01 A ve üzerindeki gözlemler kapsam içindedir.

## Değerlendirme
- 0,413 A başlangıç bildirimi 0,30 A üzerindedir. Aynı zaman aralığında doğrulanmış referans ve kararlı pencere elde edilirse mevcut ±%4 karşılaştırma kuralı uygulanabilir.
- Referans cihaz belirtilmeden veya eşzamanlı pencere bulunmadan sapma/başarı kararı verilmez.
- Şarj cihazı anahtarlamalı ve zamana bağlı bir yüktür; başlangıç, kararlı şarj ve sona yaklaşma bölümleri tek ortalamada birleştirilmez.
- Bu deney bir enerji analizörü veya güç kalitesi testi değildir; SCT akım gözlemi ve referansla karşılaştırma içindir.

## Güvenlik
- Şarj cihazı ve pil üretici talimatlarına uygun kullanılmalıdır.
- Şebeke tarafı kapalı ve yalıtılmış olmalıdır; açıkta 230 V bağlantı veya breadboard kullanılmaz.
- SCT yalnız tek yalıtılmış faz iletkenini çevreler; faz ve nötr birlikte CT içinden geçirilmez.
- CT/kablo bağlantısı değiştirilmeden önce enerji kesilir. Şarj cihazının muhafazası açılmaz.

## Sonuç
Henüz ölçüm logu yoktur. Bu kayıt yalnız deneyin açılış planıdır; test çalıştırılmış veya tamamlanmış değildir.


## 2026-10-31 — İlk kararlı akım gözlemi (kullanıcı bildirimi)

- İlk bildirilen akım: 0,413 A.
- Son bildirilen akım: **0,419 A — sabitlendi**.
- Değişim: +0,006 A; ilk değere göre yaklaşık +%1,45.
- Kaynak sınıfı: KULLANICI BİLDİRİMİ. Ölçüm cihazı henüz doğrulanmadı; bu değer PZEM veya SCT log ölçümü olarak etiketlenmez.
- Bu, şarj cihazının o andaki kararlı akımına ilişkin ön gözlemdir. Süre, pilin şarj aşaması ve ESP32D1 logu henüz yoktur.
- Test AÇIK kalır; uzun log ve referans cihaz bilgisi beklenir.


## 2026-10-31 — Ek akım gözlemi (kullanıcı bildirimi)

- Kullanıcı 0,422 A değerini de gördüğünü bildirdi; bu değer sabitlendi olarak değil, ek gözlem olarak kaydedildi.
- Bildirilen değerler: 0,413 A → 0,419 A (sabitlendi) → 0,422 A (görüldü).
- Bildirilen gözlem aralığı: 0,413–0,422 A. 0,419 A ile 0,422 A arasındaki fark +0,003 A (yaklaşık +%0,72); ilk 0,413 A değerine göre toplam fark +0,009 A (yaklaşık +%2,18).
- Kaynak sınıfı: KULLANICI BİLDİRİMİ. Ölçüm cihazı henüz doğrulanmadı; PZEM veya SCT ölçümü olduğu varsayılmaz.
- ESP32D1 uzun logu ve eşzamanlı referans verisi henüz yoktur. Deney AÇIK kalır.
