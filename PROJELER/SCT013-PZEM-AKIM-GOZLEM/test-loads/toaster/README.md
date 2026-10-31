# TOASTER-001 — Tost makinesi yük gözlemi

## HEDEF
Tost makinesi çalışırken Modül 2 / ESP32D1 / SCT-1 kanalının yüksek akım bölgesindeki davranışını gözlemek. Açılış, ısınma boyunca kararlı bölgeler ve varsa termostat/ısı kontrolü nedeniyle oluşan akım değişimleri ayrı incelenecek.

## TEST DÜZENEĞİ
- Yük: tost makinesi.
- Modül: 2 / ESP32D1 / SCT-1 GPIO32 ADC1_CH4 / ortak bias GPIO35 ADC1_CH7.
- ESPHome baseline: 2026.10.1.
- ADC: 12 dB / 1 s; ct_clamp: 200 ms örnek penceresi / 2 s çıktı.
- K: 24.22; test sırasında firmware ve katsayı değiştirilmez.
- Primer: tek tur; aynı tek yalıtılmış faz iletkeni CT çekirdeğinden geçirilir.
- UNIT referansı: **7,89 A** (kullanıcı bildirimi, 2026-10-31). Bu değer PZEM değildir; SCT loguyla zaman eşleşmesi ayrıca teyit edilecek.
- PZEM referansı: henüz bildirilmedi.

## TEST AKIŞI
1. Yükün etiket gücü ve varsa referans cihaz bilgisi test öncesi kaydedilir.
2. Tost makinesi kapalıyken başlangıç taban logu alınır.
3. Açma anı ve ilk yükseliş ayrı işaretlenir.
4. Isınma boyunca SCT akımı ve analog Raw AC/bias davranışı kaydedilir.
5. Cihazın kendi termostatı devreye girerse her ON/OFF bölümü ve geçişi ayrı analiz edilir.
6. Referans ölçüm varsa SCT ile aynı zaman penceresinde kaydedilir; eşleşme yoksa fark yalnız betimleyici kalır.

## DEĞERLENDİRME
- Açılış/ilk yükseliş: min, maks ve geçiş süresi.
- Kararlı ON pencereleri: örnek sayısı, ortalama, medyan, min, maks, SD ve CV.
- OFF/azalan akım ve termostat geçişleri: ayrı sınıflandırma; veri silinmez.
- PZEM, UNIT ve SCT kaynakları birbirine karıştırılmaz.
- Eşleşmiş kararlı referans varsa 0,30 A ve üzerindeki pencerelerde proje ±%4 karşılaştırması uygulanabilir. 0,30 A altı için ±%4 kabul/ret yok.
- Tek testten K değişikliği veya genel kalibrasyon kararı çıkarılmaz.

## GÜVENLİK
Tost makinesi şebeke gerilimiyle çalışan yüksek güçlü bir yüktür. CT yalnız tek bir yalıtılmış faz iletkenini çevrelemelidir; faz ve nötr birlikte çekirdekten geçirilmez. Şebeke tarafında açık breadboard veya açıkta iletken bırakılmaz. Kablo/CT yerleşimi değiştirilecekse cihaz enerjisiz bırakılır; uygun muhafaza ve yetkin elektrik güvenliği şarttır.

## DURUM
AÇIK — test planı oluşturuldu; fiziksel ölçüm, etiket gücü, referans ve log bekleniyor.
