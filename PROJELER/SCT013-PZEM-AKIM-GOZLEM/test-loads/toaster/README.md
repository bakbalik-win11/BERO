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


## LOG 62 — ilk SCT gözlemi (2026-10-31)

### Kaynak ve düzenek
- Kaynak dosya: `esp32d1-logs (62).txt`; 934 satır, 68.564 karakter.
- Kaynak SHA-256: `4790b00e69aaba791339f6d43aa13041efe373c5a87b9ed7fd4c1f481ce551f2`.
- ESPHome 2026.10.1; ESP32 rev3.1; SCT-1 GPIO32 / ADC1, ortak bias GPIO35 / ADC1.
- ADC 12 dB / 1 s; ct_clamp 0,20 s örnek penceresi / 2 s çıktı; K=24.22.
- Cihaz bağlantısı ve ADC/ct_clamp başlatma durumları OK. Logda çalışma hatası veya timeout görülmedi. Derleme çıktısındaki üç ESP32 framework satırı optimizasyon önerisi uyarısıdır; ölçüm hatası olarak değerlendirilmedi.

### Kararlı ON bölgesi — son düşüş örneği hariç
İlk 119 akım yayını 21:52:30.185–21:56:26.262 aralığında, yaklaşık 236,1 saniyelik kararlı bölgedir.

| Ölçüt | SCT |
|---|---:|
| n | 119 |
| Ortalama | 7,1900 A |
| Medyan | 7,188 A |
| Min–maks | 7,135–7,264 A |
| Örnek SD | 0,0247 A |
| CV | %0,344 |
| Raw AC ortalaması | 0,29686 V |
| Raw AC min–maks | 0,29461–0,29991 V |
| GPIO35 bias ortalaması | 1,66391 V |
| SPS ortalaması | 18.561 |

- Kararlı bölgedeki SCT dağılımı dardır; yaklaşık 7,19 A seviyesinde yüksek kısa dönem kararlılık gözlenmiştir.
- UNIT 7,89 A kullanıcı bildirimiyle aritmetik ortalama farkı −%8,87; medyan farkı −%8,90'dır. UNIT ölçümünün aynı zaman aralığına ait olduğu doğrulanmadığından bu değerler **eşzamanlı doğruluk sapması değildir**.
- 21:56:28.190'da son yayın 6,096 A'ya düşmüştür (önceki 7,208 A). Bu tek örnek kararlı istatistiklere katılmadı; yük geçişi/kapanma olasılığı olarak ayrıca izlenecek, tek başına termostat çevrimi kanıtı sayılmayacaktır.
- K=24.22 sabit tutuldu. Bu logda katsayı değişikliği yapılmadı ve yapılması önerilmiyor; amaç yüksek akım bölgesindeki mevcut davranışı gözlemlemektir.
- PZEM verisi ve UNIT ile eşzamanlı zaman damgası bu logda yoktur.

### Ön değerlendirme
**Gözlem:** Mevcut K=24.22 ile 7,19 A civarında SCT çıkışı kararlı görünmektedir. UNIT 7,89 A ile görülen yaklaşık %8,9 aritmetik fark, zaman eşleşmesi doğrulanmadan kalibrasyon/katsayı sonucu olarak yorumlanamaz. Son 6,096 A örneği ayrı geçiş verisi olarak korunur.

### Arşiv notu
Bu rapor, sohbet eki olan Log 62'nin tam içeriğinden hesaplanmıştır. Ham dosyanın GitHub'a birebir arşivlenmesi bu adımda yapılmadı; kaynak adı, satır/karakter sayısı ve SHA-256 kaydedildi.

## DURUM
AÇIK — Log 62 ön değerlendirmesi yapıldı. Yeni loglar/UNIT zaman eşleşmesi ve varsa termostat geçişleri bekleniyor.

## 2026-10-31 — Log 62 ham arşiv tamamlandı
- İlk ön değerlendirme sırasında ham logun GitHub arşivi henüz yoktu; bu not o anki durumu anlatıyordu.
- Sonraki işlemde aynı kaynak dosya birebir GitHub'a aktarıldı: [tam ham log](../../logs/module2/2026-10-31-toaster-001-module2-sct1-log62-full.txt).
- Ham dosya: 68.572 bayt, 934 satır; SHA-256 `4790b00e69aaba791339f6d43aa13041efe373c5a87b9ed7fd4c1f481ce551f2`.
- Teknik analiz ayrı dosyaya alındı: [Log 62 analiz raporu](../../logs/module2/2026-10-31-toaster-001-module2-sct1-log62-analysis.md).
- Ham log ve analiz dosyaları GitHub'a yazıldı; yeniden okuma/doğrulama bir sonraki adımda yapılacaktır.
