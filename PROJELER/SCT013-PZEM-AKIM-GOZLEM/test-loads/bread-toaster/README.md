# BREAD-TOASTER-001 — Ekmek kızartma makinesi

## HEDEF
Ekmek kızartma makinesinin yaklaşık 3,30 A UNIT bildirimi çevresinde Modül 2 / ESP32D1 / SCT-1 davranışını gözlemek. 3 A çevresindeki yük örneklerini genişletmek; mevcut K=24.22 ve firmware'i değiştirmeden kısa dönem kararlılığı kaydetmek.

## TEST DÜZENEĞİ
- Yük: Ekmek kızartma makinesi (KULLANICI BİLDİRİMİ); etiket gücü, marka ve model henüz kaydedilmedi.
- Modül: 2 / ESP32D1 / SCT-1 GPIO32 ADC1_CH4 / ortak bias GPIO35 ADC1_CH7.
- ESPHome: 2026.10.1.
- ADC: 12 dB / 1 s; ct_clamp: 200 ms pencere / 2 s yayın.
- K: 24.22; firmware ve katsayı test sırasında değiştirilmedi.
- Referans: UNIT 3,30 A (KULLANICI BİLDİRİMİ); PZEM değildir. Tam zaman eşleşmesi ayrıca belgelenmedi.
- PZEM: Bu logda veri yok.

## LOG 63 — ilk SCT gözlemi (2026-10-31)
- Kaynak: `esp32d1-logs (63).txt`; 32.064 bayt / 449 satır / 32.056 UTF-8 karakter.
- SHA-256: `cf9254185e591650a06a990e5bc0f567ee499ba4ec541c4bb8748b132513f896`.
- İlk/son SCT yayını: 22:31:30.257–22:33:10.230.
- 51 SCT yayını bulundu. İlk yayın 3,027 A; yalnız 186 örnek / 930 SPS olduğundan açılış örneği olarak ayrıldı.
- Kalan 50 yayında SCT ortalaması 3,09636 A; medyan 3,094 A; aralık 3,071–3,144 A; SD 0,01340 A; CV %0,433.
- Kararlı bölüm Raw AC ortalaması 0,127843 V; SPS ortalaması 18.117 (17.635–18.335).
- UNIT 3,30 A ile SCT ortalaması arasındaki aritmetik fark −0,20364 A / −%6,17. Zaman eşleşmesi doğrulanmadığından doğruluk sapması değildir.
- Bias GPIO35: 101 örnek, medyan 1,664 V, ortalama 1,66203 V; tekil 1,565 V örneği ayrıca not edildi.
- PZEM verisi yok. K=24.22 ve firmware değişmedi; katsayı türetilmedi.
- [Teknik analiz raporu](../../logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-analysis.md).
- [Seçilmiş log kanıtı](../../logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-evidence.txt).
- Tam ham log bu commit'te GitHub'a aktarılmadı; kaynak dosya konuşma ekinde korunur ve yukarıdaki SHA-256 ile tanımlanır.

## DEĞERLENDİRME
- İlk kısa kayıt SCT-1'in 3,1 A civarında kendi içinde dar dağılım gösterdiğini destekler.
- UNIT ile aynı zaman penceresinde ölçüm yapıldığı belgelenmediği için −%6,17 yalnız betimleyici aritmetik farktır; kalibrasyon/doğruluk sonucu değildir.
- Sonraki tekrarlar aynı cihaz ve benzer çalışma koşulunda alınmalı; UNIT ve mümkün olduğunda PZEM değeri SCT loguyla aynı kararlı zaman aralığında kaydedilmelidir.
- Tek logdan K değişikliği veya model kararı çıkarılmaz.

## DURUM
AÇIK — ilk log analiz edildi. Tekrarlı log ve eşzamanlı UNIT/PZEM kararlı pencere karşılaştırması bekleniyor.

## GÜVENLİK
Şebeke tarafındaki bağlantı, CT yerleşimi ve ölçüm düzeneği yalnız uygun muhafaza/koruma ve yetkin elektrik güvenliği koşullarında yapılır. CT yalnız tek yalıtılmış faz iletkenini çevrelemelidir; faz ve nötr birlikte çekirdekten geçirilmez. CT bağlantısı veya kablo düzeni değiştirilecekse enerji kesilir.
