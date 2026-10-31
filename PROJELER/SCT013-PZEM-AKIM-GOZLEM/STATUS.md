## 2026-10-31 — Arşiv doğrulama notu: FAN-3-3T-001

- Tam ham log GitHub'a kaydedildi: [FAN-3-3T-001 full log](logs/module2/2026-10-31-fan3-3t-001-module2-sct1-full.txt); Git blob SHA `1f947025d9716ac5a3a4e8e586e8d1b65e5cdd22`; kaynak SHA-256 `fb48997412ced2a9f769b3084bec9f63dab8ef7174efea23062ce4e63dbc735c`.
- [Analiz](logs/module2/2026-10-31-fan3-3t-001-module2-sct1-analysis.md), [kapanış YAML](firmware/archive/FAN-3-3T-001-2026-10-31-esp32d1-sct1.yaml) ve test kaydı GitHub'dan yeniden okunarak doğrulandı.
- FAN-3-3T-001 kapalı; FAN-1-RETEST-001 açık.



## 2026-10-31 — FAN-3-3T-001 üç primer tur deneyi açıldı

- **DURUM:** AÇIK; fiziksel sarım ve ölçüm henüz yapılmadı.
- **AMAÇ:** FAN-3 yükünde mevcut SCT013-030 sensörün düşük akım sinyalini aynı tek yalıtılmış iletkeni CT'den üç kez geçirerek gözlemlemek.
- **KOD KİLİDİ:** `firmware/esp32d1.yaml` değiştirilmez; K=24.22 korunur; yazılımsal sıfır eşiği eklenmez. Açılış anındaki YAML blob SHA: `e1b110aca2ffa05fa792fd8e4b6248ed986e738c`.
- **HESAP:** Firmware akım göstergesi ham olarak korunur; gerçek akım için gösterge/3 yalnız analizde deneysel normalizasyon olarak hesaplanır. Bu işlem kalibrasyon değildir.
- **UNIT:** En güncel kullanıcı bildirimi 0,142 A; eski FAN-3 kaydındaki 0,141 A tarihsel olarak korunur.
- **ÖNCEKİ TEK TUR:** Raw AC ortalama 0,009273 V; SCT ortalama 0,224612 A.
- **KURAL:** 0,30 A altındaki düşük akım alanında ±%4 kabul/ret yok.
- **DOSYA:** [FAN-3-3T-001 test planı](test-loads/fan3-3turn/README.md).
- **GÜVENLİK:** Enerji kesikken yalnız aynı tek yalıtılmış iletken CT'den üç tur geçirilir; faz ve nötr birlikte geçirilmez.


## 2026-10-31 — 0,30 A altı düşük akım deney sınıflandırması ve FAN-1/FAN-2 düzeltmesi

- **KALICI TEST KURALI:** 0,30 A altındaki akım bölgesinde ±%4 kabul/ret ölçütü uygulanmaz. 0,30 A ve üzerindeki koşullarda, eşleşmiş kararlı referans verisi varsa ±%4 karşılaştırması yapılabilir.
- Bu sınır BERO'nun deney değerlendirme kararıdır; SCT-013 üretici spesifikasyonu, sensörün minimum ölçüm akımı veya doğruluk garantisi değildir.
- **FAN-1 DÜZELTME:** UNIT 0,093 A; düşük akım deney bölgesi. Önceki 0,08928–0,09672 A aritmetik bandı ve 4/247 sayımı tarihsel veri olarak korunur, kabul/ret ölçütü değildir. SCT istatistikleri değişmez: yaklaşık 247 yayın, ortalama 0,146757 A, medyan 0,147 A, min–maks 0,064–0,259 A. FAN-1 yalnız Modül 2 ısınma/deneme gözlemi olarak kapalıdır; düşük akım araştırması ayrıca açıktır.
- **FAN-2 DÜZELTME:** UNIT 0,106 A; aynı düşük akım bölgesinde. 2026-10-31 logundaki 54 yayın ve ortalama 0,164259 A yalnız gözlem istatistiğidir; ±%4 kıyası yapılmaz. PZEM akım + PF henüz logda yoktur.
- **DENEY PLANI:** Tek tur, 2 tur ve 4 tur koşullarıyla düşük akım sinyalinin gözlenmesi; PZEM akım/PF, UNIT bildirimi, SCT Raw AC ve ct_clamp istatistiklerinin aynı kararlı pencerelerde kaydı. Çok turlu koşullarda CT'nin gördüğü amper-sarım sayısı ayrıca dikkate alınır; firmware K değeri deney sırasında değiştirilmez. Plan henüz fiziksel olarak uygulanmadı.
- **DOSYA:** [0,30 A altı deney planı](test-loads/low-current-below-0p30/README.md).
- **DONANIM GÜVENLİĞİ:** Sarım düzenini değiştirirken enerji kesilir; yalnız aynı tek yalıtılmış iletken CT çekirdeğinden belirtilen sayıda geçirilir. Farklı faz/nötr iletkenleri birlikte çekirdekten geçirilmez.
## 2026-10-31 — FAN-1 Modül 2 ısınma/deneme kaydı kapatıldı

- **SINIF:** FAN-1, Modül 2 ısınma/deneme gözlemi olarak kapatıldı; ±%4 akım doğrulama testi olarak kabul edilmedi. PZEM ile ileri değerlendirme açık.
- **KAYNAK:** `esp32d1-logs (40).txt`; 140.312 bayt / 1.887 satır; SHA-256 `8687da052b254f16b88f6eb6d27d41c94ae8166b027f089f0b6186069c58bedf`; 17:13:51.283–17:22:23.079 (+03:00).
- **DÜZENEK:** ESP32D1 / Modül 2 / SCT-1 GPIO32 ADC1_CH4 / ortak bias GPIO35 ADC1_CH7; ESPHome 2026.10.1; ADC 12 dB, 1 s; ct_clamp 200 ms, yayın 2 s.
- **İSTATİSTİK:** 17:14:11.079 sonrası yaklaşık 247 yayın; ortalama 0,146757 A; medyan 0,147 A; min–maks 0,064–0,259 A; SD 0,026064 A.
- **UNIT:** Son kullanıcı bildirimi 0,093 A; önceki 0,097 A ve 0,096 A bildirimleri tarihsel not olarak korundu. ±%4 aritmetik bandı 0,08928–0,09672 A; 4/247 (%1,6) yayın bant içinde. Bu sonuç tek başına kabul/ret değildir.
- **PF:** UNIT PF göstermedi. PF etkisi olası açıklama olarak hipotez düzeyinde kaldı; aynı kararlı pencerede PZEM akım ve PF olmadan doğrulanamaz.
- **KOD:** Kapanış YAML snapshot [firmware/archive/FAN-1-2026-10-31-esp32d1-sct1.yaml](firmware/archive/FAN-1-2026-10-31-esp32d1-sct1.yaml); snapshot kaynak dosya [firmware/esp32d1.yaml](firmware/esp32d1.yaml). Kodun logla eşleşmesi yapılandırma düzeyindedir; binary eşleşmesi iddia edilmez.
- **ARŞİV:** [fan kaydı](test-loads/fan/README.md); [uzun analiz](logs/module2/2026-10-31-fan1-module2-sct1-long-analysis.md); [tam ham log](logs/module2/2026-10-31-fan1-module2-sct1-long-full.txt); [ana kayıt](test-loads/README.md).
- **SONRAKİ:** FAN-2'ye geçilebilir. FAN-2 ve sonraki kademelerde PZEM akım + PF verisi test girdisi olacaktır. K=24.22 korunur; yazılımsal sıfır eşiği eklenmez.

## 2026-10-31 — LOAD-IDLE-001 uzun yüksüz log arşivlendi

- **TEST:** LOAD-IDLE-001 aynı yüksüz oturumun uzatılmış kaydıdır; yeni test ID değildir.
- **KAYNAK:** `esp32d1-logs (37).txt`; 110.590 bayt / 1.492 satır; SHA-256 `e4b229b45abce1f85e74f60260c0a7ed279e48c6b8f59d70ccbabaf23c8ee22f`. Tam ham log GitHub'a aktarıldı.
- **ZAMAN:** İlk/son akım yayını 16:47:55.066–16:54:33.029 (+03:00), yaklaşık 6 dk 38 sn.
- **MÜKERRERLİK:** Önceki kısa logun 60 akım yayını, uzun logun ilk 60 yayınıyla zaman/değer bazında birebir aynı; 140 yeni yayın eklendi.
- **AKIM:** Toplam 200 yayın; ortalama 0,017130 A; medyan 0,000 A; min–maks 0,000–0,144 A; örnek SD 0,032705 A. 146/200 (%73) sıfır; 54/200 (%27) sıfır dışı.
- **DEVAM:** Yeni 140 yayın; ortalama 0,019643 A; medyan 0,000 A; 98/140 (%70) sıfır; 42/140 (%30) sıfır dışı.
- **ANALOG:** Raw AC ortalama 0,00070765 V; bias GPIO35 ortalama 1,664461 V; SCT-1 GPIO32 ADC ortalama 1,662461 V.
- **ÖRNEKLEME:** ct_clamp log SPS 17.465–18.465; ortalama 17.990. Üç derleyici/optimizasyon uyarısı; [E] hata, brownout veya reboot işareti yok.
- **REFERANS:** Yüksüz senaryoda UNIT aranmadı; logda PZEM yok.
- **KARAR:** K=24.22 korunur; yazılımsal sıfır eşiği eklenmez. İlk kısa logda %80 olan sıfır oranı uzun kayıtta %73'e düştü. Yüksüz dağılımı için daha fazla tekrarlı kayıt gerekir.
- **ARŞİV:** [Yüksüz test README](test-loads/idle-no-load/README.md); [analiz](logs/module2/2026-10-31-load-idle-001-analysis.md); [tam ham log](logs/module2/2026-10-31-load-idle-001-module2-sct1-no-load-full.txt).
- **SONRAKİ:** Aynı fiziksel koşul ve firmware ile ayrı bir yüksüz oturum; mevcut kod ve katsayı değişmeden.

## 2026-10-31 — LOAD-IDLE-001 ilk yüksüz SCT-1 logu arşivlendi

- **TEST:** Modül 2 / ESP32D1 / SCT-1 GPIO32 ADC1_CH4 / ortak bias GPIO35 ADC1_CH7; ESPHome 2026.10.1; ct_clamp 200 ms, yayın 2 s; ADC 1 s, 12 dB.
- **LOG:** Kullanıcı kaynağı Yapıştırılan metin(20261031-135010).txt; 36.687 bayt / 514 satır; SHA-256 `9ac3ece0770a85219e7ad6664f15f1ccc9db9b561d04f6195ef034d4e718e455`. İlk/son akım yayını 16:47:55.066–16:49:53.052 (+03:00).
- **AKIM:** 60 yayın; ortalama 0,011267 A; medyan 0,000 A; min–maks 0,000–0,104 A; örnek SD 0,025876 A. 48/60 (%80) sıfır, 12/60 (%20) sıfır dışı.
- **ANALOG:** Raw AC ortalama 0,0004657 V; bias GPIO35 ortalama 1,663881 V; SCT-1 GPIO32 ADC ortalama 1,662508 V.
- **ÖRNEKLEME:** ct_clamp log SPS 17.465–18.280; ortalama yaklaşık 17.971 SPS. Üç derleyici/optimizasyon uyarısı; [E] hata, brownout veya reboot işareti yok.
- **REFERANS:** Yüksüz senaryo için UNIT referansı aranmadı; logda PZEM yok.
- **YORUM:** Yüksüz durumda çoğunlukla sıfır okuma var; 12 aralıklı düşük sıfır dışı değer görüldü. Kaynağı bu logla ayrıştırılamaz. K değiştirilmedi; yazılımsal sıfır eşiği eklenmedi.
- **ARŞİV:** [Yüksüz test kaydı](test-loads/idle-no-load/README.md); [teknik analiz](logs/module2/2026-10-31-load-idle-001-analysis.md); [seçilmiş gerçek log satırları](logs/module2/2026-10-31-load-idle-001-evidence.txt). Kanıt dökümü tam ham log değildir; tam kaynak dosyanın adı, boyutu ve SHA-256 değeri kaydedilmiştir.
- **SONRAKİ:** Daha uzun/tekrarlı yüksüz log; mevcut kod ve katsayı değiştirilmeden.

## 2026-10-31 — LOAD-150W-001 uzun SCT-1 testi arşivlendi

- **TEST:** 150 W akkor; ESP32D1 / Modül 2 / SCT-1 sarı GPIO32 / ortak bias GPIO35; masaüstü harici besleme.
- **LOG:** Kullanıcı kaynağı `esp32d1-logs (36).txt`, 211.455 bayt; SHA-256 `a407bc3363a804a4a72c06e0163119d3fac2243e8c802a7ff781038f699bdb4e`; 16:31:30.179–16:44:32.407 (+03:00). 391 akım yayını. Dosya 35'teki 133 ölçüm aynı testin başındaki ölçümlerdir; mükerrer test sayılmadı.
- **UNIT:** Kullanıcı bildirimi 0,598 A ve 0,599 A; ortalama 0,5985 A. ±%4 bandı 0,57456–0,62244 A.
- **SCT SONUCU:** Ortalama 0,6082148 A; medyan 0,608 A; min–maks 0,591–0,655 A; örnek SD 0,006595 A; ortalama sapma +%1,6232; 388/391 (%99,23) yayın UNIT bandında.
- **ANALOG:** Raw AC ortalama 0,0251121 V; bias 1,6636003 V; SCT-1 ADC 1,661110 V. ct_clamp SPS ortalaması yaklaşık 17.411.
- **DURUM:** 3 derleyici/optimizasyon uyarısı; hata, brownout veya reboot işareti yok. PZEM değeri logda yok; bu UNIT kıyasıdır, PZEM doğrulaması değildir. K=24.22 değiştirilmedi.
- **ARŞİV:** [150 W test kaydı](test-loads/150w-incandescent/README.md); [uzun log analizi](logs/module2/2026-10-31-load-150w-001-sct1-long-analysis.md); [ana test kayıtları](test-loads/README.md). Ham log dosyasının tam metni GitHub'a henüz aktarılmadı; kaynak adı, boyutu ve SHA-256 korundu.
- **PROTOKOL KARARI:** Her yükte önce o yüke ait UNIT ölçümü; SCT kıyası UNIT ile. PZEM daha sonra eklenir; UNIT ve PZEM ayrı referanslardır.
- **SONRAKİ:** 150 W testi kapatıldı. SCT bağlı ve primer akımı olmayan koşulda boşta okuma tabanını kaydet. Mevcut kodda yazılımsal sıfır eşiği yok; boşta testte eşik ekleme.

## 2026-10-31 — Modül 2 tek aktif SCT kanalı / üç jack kararı

- **KARAR:** Aynı ESP düğümü aynı anda tek SCT akım kanalını okuyacak. Üç fiziksel jack korunacak ve seçilen jack farklı oturumlarda kullanılacak.
- **PINLER:** SCT-1 sarı GPIO32 / ADC1_CH4; SCT-2 yeşil GPIO33 / ADC1_CH5; SCT-3 mavi GPIO34 / ADC1_CH6; ortak bias turuncu GPIO35 / ADC1_CH7.
- **KULLANIM:** Tek, iki veya dört primer tur gibi sarım koşulları aynı test kutusunda, jack/tesisat sökülmeden ayrı zamanlarda denenebilecek. Eşzamanlı üç kanal okuma hedeflenmiyor.
- **KOD GÖZLEMİ:** Kullanıcı LOAD-100W-004 tek kanal kodunu 0,427 A geçici UNIT beklentisiyle uyumlu buluyor. Bu PZEM doğrulaması değildir; K değiştirilmedi.
- **GÜÇ:** Harici masaüstü beslemeli uzun log kararlı (215 yayın; medyan 0,423 A; ortalama 0,425 A; 0,55 A üzeri sıçrama yok). 5 V ve 3,3 V rayları logda ölçülmedi. Güç kaynağı etkisi hipotez; aynı koşulda tekrar ve mümkünse multimetre ölçümü bekliyor.
- **AYRINTI:** [ADR-021](docs/decisions/ADR-021-module2-one-active-sct-channel-three-jacks.md), [oturum tecrübe kaydı](HISTORY/SESSION_LOG.md).
- **SONRAKİ:** SCT-1 / 100 W / harici besleme koşusunu tekrarla ve güç raylarını gözlemle; sonra SCT-2 ve SCT-3 jack'lerini ayrı oturumlarda test et.

## 2026-10-31 — LOAD-100W-004 uzun masaüstü besleme tekrarı ve tek kanal mimarisi

- **LOG:** [Tam 1.602 satır / 118.860 bayt](logs/module2/2026-10-31-load-100w-004-sct1-desktop-power-full.txt); SHA-256 `de3f2289700f657cfcf1fd8bff816bbd8a8bc05bb2296f349462709cbb42d859`.
- **ANALİZ:** [Uzun tekrar teknik analizi](logs/module2/2026-10-31-load-100w-004-sct1-desktop-power-extended-analysis.md).
- **SÜRE:** İlk/son akım yayını 16:06:45.189–16:13:53.226 (+03:00), yaklaşık 7 dakika 8 saniye; 215 akım yayını.
- **AKIM:** Medyan 0,423 A; ortalama 0,425 A; örnek SD 0,01149 A; min–maks 0,401–0,480 A; 0,55 A üzeri sıçrama yok.
- **GEÇİCİ UNIT KIYASI:** 0,427 A ±%4 bandında 192/215 (%89,3) yayın. Bu değer PZEM teyidi değildir; logda eşzamanlı UNIT/PZEM ölçümü yoktur.
- **ANALOG:** Raw AC ortalama 0,01755 V; bias GPIO35 ortalama 1,66367 V (1,653–1,681 V); SCT-1 ADC ortalama 1,66144 V (1,631–1,692 V). ct_clamp raporlanan SPS ortalaması 17.659.
- **GÜÇ YORUMU:** Harici masaüstü besleme koşusunda uzun süreli kararlılık gözlendi. Log 5 V girişini veya 3,3 V rayını ölçmediği için güç kalitesi doğrudan doğrulanmadı; USB/harici besleme nedenselliği için kontrollü A/B testi gerekir.
- **MİMARİ ÇALIŞMA KARARI:** Şimdilik bir ESP düğümünde bir aktif SCT kanalı tercih edilecek. Bu, üç kanalın aynı ESP'de kesinlikle çalışamayacağının kanıtı değil; görev izolasyonu ve kararlılık için geçici test mimarisidir.
- **KATSAYI:** K değiştirilmedi. 150 W Modül 2 testi ayrı yük dosyasında bekliyor.

## 2026-10-31 — Modül 2 için 150 W akkor test yükü kaydı açıldı

- **KULLANICI PLANI:** Masaüstü harici besleme ile daha uzun 100 W SCT-1 logu paylaşılacak; ardından Modül 2 testinde 150 W akkor ampule geçilecek.
- **YENİ YÜK KAYDI:** [150 W akkor karşılaştırmalı test dosyası](test-loads/150w-incandescent/README.md) oluşturuldu.
- **ENVANTER:** [Test yükleri ana listesine](test-loads/README.md) 150 W akkor satırı eklendi. 100 W ve 150 W yükleri ayrı klasörlerde ve ayrı tablolarla izlenir.
- **TARİHSEL REFERANS:** ROADMAP/Faz 1 arşivinde 150 W için 0,616 A referans ve 0,615 A kod sonucu (yaklaşık −%0,2) bulunuyor. Bu sonuç tarihsel Faz 1 kaydıdır; yeni Modül 2 testinin sonucu veya doğrulanmış hedefi değildir.
- **YENİ TEST PLANI:** İlk oturum SCT-1 / sarı / GPIO32; ortak bias GPIO35. Masaüstü besleme, firmware sürümü, zaman aralığı, ham log ve mümkünse eşzamanlı UNIT/PZEM değerleri ayrı kaydedilecek.
- **DURUM:** 150 W fiziksel test henüz yapılmadı. Daha uzun 100 W tekrar logu alındı ve arşivlendi; T010 aktif.
- **GÖREV:** [T010 Modül 2](tasks/T010-module2-triple-sct-bringup.md) içine 150 W test planı eklendi.

## 2026-10-31 — LOAD-100W-004 masaüstü güç kaynağı sonrası SCT-1 kısa log kesiti (uzun logla genişletildi)

- **KULLANICI BİLDİRİMİ:** ESP32D1 beslemesi PC USB'den masaüstü harici güç kaynağına alındı; 100 W akkor test tekrarlanmıştır.
- **LOG:** [Tam 397 satır](logs/module2/2026-10-31-load-100w-004-sct1-desktop-power.txt); özgün dosya 28.161 bayt; SHA-256 `0cba41fa5f66894f17ba2cda45773cae6a77c82eab1aa4e4c8bda81e019d4ac3`.
- **SÜRE:** 16:06:43.782–16:08:09.198 (+03:00); 43 akım yayını.
- **DÜZENEK:** ESP32D1 / Modül 2 / SCT-1 sarı GPIO32 ADC1_CH4; ortak bias turuncu GPIO35 ADC1_CH7. ESPHome 2026.10.1; cihaz derleme zamanı 15:55:25; ct_clamp 200 ms, yayın 2 s; ADC update 1 s; 12 dB.
- **AKIM:** Medyan 0,423 A; ortalama 0,42274 A; örnek standart sapma 0,00852 A; min–maks 0,407–0,440 A.
- **0,427 A KIYASI:** Geçici UNIT beklentisi 0,427 A'nın ±%4 bandında 39/43 (%90,7) yayın; ortalama farkı −%1,0. Eşzamanlı PZEM/UNIT ölçümü logda yok.
- **ÖNCEKİ TESTE GÖRE:** LOAD-100W-003 uzun log medyanı 0,460 A, ortalama 0,4841 A, aralık 0,422–1,164 A ve 10 yüksek yayın içeriyordu. Yeni log medyanı 0,423 A, aralığı 0,407–0,440 A; 0,55 A üzeri yayın yok. Belirgin iyileşme işareti var; ancak yeni kayıt yaklaşık 84 saniye ve 43 yayından oluşuyor, nedensellik ispatı değil.
- **ANALOG:** Raw AC ortalama 0,01745 V; bias ortalama 1,66342 V; SCT-1 ADC ortalama 1,65952 V.
- **KARAR:** K katsayısı değiştirilmedi. 0,427 A UNIT kullanıcı bildirimi kaynaklı geçici beklenti; PZEM doğrulaması değildir. Aynı harici beslemeyle daha uzun tekrar ve aynı zaman aralığında PZEM/UNIT ölçümü bekleniyor.
- **ANALİZ:** [LOAD-100W-004 teknik analizi](logs/module2/2026-10-31-load-100w-004-sct1-desktop-power-analysis.md).
- **TEST TABLOSU:** [100 W akkor karşılaştırma arşivi](test-loads/100w-incandescent/README.md).

## 2026-10-31 — LOAD-100W-003 uzun SCT-1 tek kanal logu

- **YENİ KANIT:** [Tam 1.219 satırlık log](logs/module2/2026-10-31-load-100w-003-sct1-single-channel-full.txt); özgün dosya 90.076 bayt; SHA-256 `30fc5d5ccccf629423924ea17fe1706bdb4f8dfab1185f64f523596661663ed4`.
- **SÜRE:** 15:59:53.051–16:05:11.858 (+03:00), yaklaşık 5 dakika 19 saniye.
- **DÜZENEK:** ESP32D1 / Modül 2 / SCT-1 sarı GPIO32 ADC1_CH4; ortak bias turuncu GPIO35 ADC1_CH7. ESPHome 2026.10.1; ct_clamp 200 ms, yayın 2 s; ADC voltaj güncellemesi 1 s; 12 dB.
- **AKIM:** 160 yayın; medyan 0,460 A; ortalama 0,4841 A; min–max 0,422–1,164 A. 150/160 yayın 0,422–0,541 A; 10 yayın 0,55 A üzerindedir.
- **ANALOG:** Raw AC 160 yayında ortalama 0,01999 V; bias 321 yayında ortalama 1,65540 V; SCT-1 ADC 320 yayında ortalama 1,65253 V.
- **0,427 A KARŞILAŞTIRMASI:** UNIT kullanıcı bildirimi kaynaklı geçici beklenti, PZEM teyidi değildir. Medyan farkı +%7,7; 0,55 A üzerindeki yayınlar hariç 150 yayının ortalaması 0,46288 A (+%8,4). ±%4 bandında 17/160 yayın vardır. Eşzamanlı PZEM kararlı ölçümü logda yoktur.
- **YORUM:** 10 yüksek yayın nedeniyle ortalama tek başına kararlı değer kabul edilmedi. K katsayısı değiştirilmedi; 0,427 A PZEM ile teyit edilene kadar geçicidir.
- **ANALİZ:** [Uzun log teknik analizi](logs/module2/2026-10-31-load-100w-003-sct1-single-channel-extended-analysis.md).
- **TEST KAYDI:** [100 W akkor karşılaştırma dosyası](test-loads/100w-incandescent/README.md).
- **KOD:** [003 tek kanallı firmware snapshot](firmware/archive/LOAD-100W-003-esp32d1-sct1-single-channel.yaml). Log konfigürasyonu snapshot ile uyumludur; binary/YAML kriptografik eşleşme iddiası yoktur.

## 2026-10-31 — 100 W akkor için geçici beklenen akım değeri

- **BEKLENEN DEĞER:** 0,427 A.
- **KAYNAK:** UNIT cihazında görülen değer; kullanıcı bildirimi.
- **ANLAMI:** 100 W akkor ampul testlerinde şimdilik ne okunması beklendiğini gösteren geçici çalışma referansıdır.
- **PZEM:** Aynı yükte PZEM kararlı okuması henüz sabitlenmedi. PZEM ölçümü geldiğinde zaman aralığı ve kararlı pencereyle ayrı kaydedilecek; geçici 0,427 A değeri doğrulanacak veya güncellenecek.
- **003 ÖN KARŞILAŞTIRMA:** Tek kanallı SCT-1 medyanı 0,469 A; 0,427 A beklentiye göre yaklaşık +%9,8. Bu sonuç PZEM teyidi olmadan kesin sapma/±%4 kabul kararı değildir. Katsayı değiştirilmedi.
- **KAYIT:** [100 W akkor karşılaştırma dosyası](test-loads/100w-incandescent/README.md).

## 2026-10-31 — LOAD-100W-003: ESP32D1 SCT-1 tek kanal testi

- **TEST:** 100 W akkor ampul; Modül 2 / ESP32D1; SCT-1 sarı/GPIO32; ortak bias turuncu/GPIO35.
- **KOD:** Tek kanallı ct_clamp firmware snapshot'ı [LOAD-100W-003 kod arşivinde](firmware/archive/LOAD-100W-003-esp32d1-sct1-single-channel.yaml) sabitlendi. Arşiv commit'i: 720e52de7fac8c409fe2c7de8569849ca171f166.
- **LOG:** 2026-10-31 15:59:53.051–16:01:39.884 (+03:00); ESPHome 2026.10.1, derleme 15:55:25 +0300. GPIO32 ADC1_CH4, GPIO35 ADC1_CH7; ct_clamp 200 ms, yayın 2 s.
- **SONUÇ:** 54 akım yayını; medyan 0.469 A; 52/54 yayın 0.426–0.541 A. İki yüksek değer: 0.797 A ve 1.164 A. Bias ortalaması 1.65672 V (107 yayın; aralık 1.623–1.678 V).
- **REFERANS:** Bu logda PENS/U200B+ veya PZEM değeri yok. Sapma ve ±%4 kabulü hesaplanmadı; katsayı değiştirilmedi.
- **ANALİZ/LOG KANITI:** [003 log analizi ve seçilmiş gerçek satırlar](logs/module2/2026-10-31-load-100w-003-sct1-single-channel-analysis.md). Özgün log SHA-256: c92d51915de6b7ab69fdbc1f00ad4b7554455748958d18525ba2b3320a9d9723.
- **T010:** Tek kanal akım okuma işlevi bu logda çalışıyor; üç kanalın tamamı ve referansla doğrulama henüz tamamlanmış değildir.

## 2026-10-31 — E00F tek SCT ct_clamp kodu Modül 2'ye uyarlandı

- **KOD:** [firmware/esp32d1.yaml](firmware/esp32d1.yaml) artık Modül 2 SCT-1 soketine göre GPIO32 sinyal + GPIO35 ortak bias kullanır. Cihaz kimliği `esp32d1` / `ESP32D1` korunmuştur.
- **KORUNAN E00F AYARLARI:** 12 dB, 200 ms `ct_clamp`, 2 s yayın, `on_raw_value` ile ayrı Raw AC entity'si, 24.22 katsayısı, yazılımsal sıfırlama eşiği yok.
- **PIN FARKI:** E00F'de GPIO32/33 aynı SCT düğümünün iki ADC görüntüsü, GPIO34/35 bias düğümünün iki görüntüsüydü. Modül 2'de GPIO32/33/34 üç ayrı SCT soketi olduğundan bu dört girişli düzen bire bir kopyalanmadı. RAW count entity'si eklenmedi; GPIO33 ve GPIO34 bu tek kanal firmware'inde kullanılmıyor.
- **KARAR:** [ADR-020](docs/decisions/ADR-020-e00f-ct-clamp-module2-adaptation.md).
- **DOĞRULAMA:** GitHub'a kaydedildi; ESPHome derlemesi, OTA ve gece testi henüz yapılmadı. 24.22 katsayısı E00F'den taşınmış başlangıç değeridir, Modül 2 kalibrasyonu değildir.

## 2026-10-31 — Modül 2 dört ADC girişli uzun kayıt firmware'i geri yüklendi

- **KARAR:** Tek kanallı ct_clamp sürümü yerine depo geçmişindeki dört ADC girişli log sürümü geri yüklendi.
- **KOD:** [firmware/esp32d1.yaml](firmware/esp32d1.yaml) GPIO32/33/34/35 girişlerini 1 saniye aralıkla okur; dört örnek de ESPHome loguna `sct_test` etiketiyle yazılır.
- **ESP KİMLİĞİ:** `esp32d1` / `ESP32D1` korunmuştur.
- **TEST KOŞULU:** Kullanıcı SCT-1'i GPIO32'de test edeceğini bildirdi. GPIO33 ve GPIO34 fiziksel SCT bağlı değilse boşta giriş olarak değerlendirilir; akım/sensör kanıtı sayılmaz. GPIO35 ortak bias ölçümüdür.
- **SINIR:** Bu sürüm RMS/akım hesaplamaz; yalnız 1 saniyelik ADC voltaj gözlemi yapar. 50 Hz dalga şekli örneklemesi değildir.
- **KARAR KAYDI:** [ADR-018](docs/decisions/ADR-018-module2-four-adc-long-log.md).
- **DOĞRULAMA:** YAML GitHub'a kaydedildi; ESPHome derlemesi, OTA ve yeni uzun fiziksel log henüz yapılmadı. T010 AKTİF.

## 2026-10-31 — Modül 2 tek kanallı SCT test firmware'i

- **KARAR:** Üçlü ct_clamp yapılandırması kontrollü test için tek aktif kanala indirildi. Üçlü yapının kaliteyi düşürdüğü henüz kanıtlanmadı; bu değişiklik hipotezi sınamak içindir.
- **AKTİF GİRİŞ:** SCT-3 / GPIO34 / ADC1_CH6. Son fiziksel testte SCT bu girişteydi.
- **KORUNAN:** GPIO35 ortak bias ADC izlemesi, 200 ms ct_clamp penceresi, 5 s yayın aralığı ve nominal 30 A/V başlangıç katsayısı.
- **PASİF:** GPIO32 ve GPIO33 donanımda yerinde; bu firmware sürümünde tanımlı/okunur değiller.
- **KOD:** [Tek kanallı esp32d1.yaml](firmware/esp32d1.yaml). Karar: [ADR-017](docs/decisions/ADR-017-module2-single-sct-channel.md).
- **DOĞRULAMA:** YAML GitHub'a yazıldı; yeni sürüm henüz ESPHome'da derlenmedi, cihaza yüklenmedi ve fiziksel test edilmedi. T010 AKTİF.
- **SONRAKİ:** Derleme/OTA sonrası aynı SCT-3 ve aynı yükle kapalı → açık kararlı → kapalı logu al; önceki üç kanallı kayıtla karşılaştır.

## 2026-10-31 — Modül 2 SCT-1 / 100 W PENS karşılaştırması

- **LOG:** Yeni ct_clamp logunda SCT-1 için 200 ms pencerede hızlı örnekleme ve akım yayını görüldü. Son beş kararlı değer 0,578–0,597 A; ortalama 0,589 A.
- **REFERANS:** Kullanıcı aynı 100 W test koşulunda PENS değerini 0,427 A olarak bildirdi.
- **KARŞILAŞTIRMA:** ESP32D1 ortalaması PENS değerinden 0,162 A / yaklaşık %37,9 yüksek. Bu fark tek ölçümle katsayı düzeltmek için yeterli değildir.
- **KATSAYI:** Nominal 30 A/V başlangıç katsayısı şimdilik korunuyor. SCT-1 üzerindeki CT modelinin 30 A/1 V SCT-013-030 olduğu kanal bazında doğrulanmalı; yeni katsayı uygulanmadı.
- **KAYIT:** [SCT-1 100 W ct_clamp + PENS karşılaştırması](logs/module2/2026-10-31-sct1-100w-ct-clamp-comparison.txt). Ham 563 satırlık logun tamamı bu dosyada değildir; özet analiz ve kullanıcı PENS bildirimi kaydedilmiştir.
- **SONRAKİ:** Aynı koşulda PENS ve ESP32D1 değerlerini aynı kararlı zaman aralığında yeniden karşılaştır; ardından SCT-2 ve SCT-3 testlerine geç. T010 AKTİF.

## 2026-10-31 — Modül 2 üç kanal akım hesabı eklendi (derleme bekliyor)

- **KOD:** [firmware/esp32d1.yaml](firmware/esp32d1.yaml) üç GPIO32/33/34 ADC kaynağına ESPHome `ct_clamp` akım sensörleri ekleyecek şekilde güncellendi; GPIO35 ortak bias ve mevcut ADC voltaj entity'leri korundu.
- **HESAP:** SCT-013-030 nominal 30 A / 1 V oranından ilk dönüşüm 30 A/V olarak tanımlandı. Bu üretici nominal oranından türetilmiş başlangıç katsayısıdır; saha kalibrasyonu veya doğrulanmış doğruluk değildir.
- **ÖRNEKLEME:** Üç kanal 200 ms örnekleme penceresiyle; 5 s / 5.5 s / 6 s yayın aralıklarıyla yapılandırıldı.
- **BEKLENEN ENTITY'LER:** ESP32D1 SCT 1 Current, ESP32D1 SCT 2 Current, ESP32D1 SCT 3 Current (A); üç ADC voltajı ve ortak bias voltajı (V).
- **KARAR:** [ADR-016](docs/decisions/ADR-016-module2-three-channel-ct-clamp.md).
- **DOĞRULAMA:** YAML GitHub'a yazıldı; bu oturumda ESPHome derlemesi, OTA yüklemesi veya yeni akım logu alınmadı. Kod çalışır/doğrulandı olarak işaretlenmedi.
- **SONRAKİ:** ESPHome derlemesi; ardından her kanalda aynı 100 W ampulle yük kapalı/açık/kapalı ölçümü ve U200B+ karşılaştırması. SCT-1 için daha önce bildirilen U200B+ 0.433 A referans bilgisi korunur; yeni kodun sonucu değildir.

## 2026-10-31 — SCT-1 / 100 W ampul ilk kanal denemesi

- **TEST:** SCT-1, ön panel 1 numaralı girişe bağlandı. Kullanıcı 100 W ampulü açtığını bildirdi.
- **BIAS:** Ortak bias değeri ESPHome logunda görüldü (KULLANICI BİLDİRİMİ); bu mesajda sayısal bias değeri verilmedi.
- **REFERANS GÖSTERGE:** Kullanıcı U200B+ cihazında 0,433 A gördüğünü bildirdi (KULLANICI BİLDİRİMİ).
- **ADC KANITI:** Bu kayıtla birlikte SCT-1 GPIO32 ADC sayısal log örneği paylaşılmadı. Dolayısıyla 0,433 A, ESP32 ADC akım hesabı veya ADC doğruluk sonucu değildir.
- **KAYIT:** [SCT-1 100 W test kaydı](logs/module2/2026-10-31-sct1-100w-test.txt).
- **SONUÇ:** SCT-1 test adımı kullanıcı bildirimiyle gerçekleştirildi. GPIO32 ADC davranışını değerlendirmek için ampul açıkken GPIO32 ve aynı zaman aralığındaki GPIO35 log satırları gerekir. SCT-2 ve SCT-3 testleri bekliyor; T010 AKTİF.

## 2026-10-31 — Modül 2 ilk firmware açılışı / bağlantısız ADC kontrol logu

- **KANIT:** Kullanıcının paylaştığı ESPHome logundan seçilmiş ADC kurulum ve örnek satırları kanıt dökümü olarak depoya eklendi: [ilk açılış log kanıt dökümü](logs/module2/2026-10-31-first-boot-no-load.txt).
- **KOD:** [firmware/esp32d1.yaml](firmware/esp32d1.yaml) mevcut depodaki dört ADC sensörlü sürüm; GPIO32/33/34 SCT kanalları ve GPIO35 ortak bias. Log, ESPHome 2026.10.1 ile 2026-10-31 15:19:21 +0300 derlenmiş firmware'in cihazda açıldığını gösteriyor.
- **BAŞLATMA KANITI:** Dört ADC için Handle Init, Config, Calibration ve Overall Init durumları OK. GPIO32/33/34/35, ADC1_CH4/5/6/7 olarak listelenmiş; 12 dB attenuation ve 1.000 s güncelleme aralığı görülüyor.
- **BAĞLANTI DURUMU:** Kullanıcı beyanına göre bu açılış sırasında SCT ve 220 V ampul bağlantısı henüz yapılmamıştı. Bu nedenle üç SCT ADC değerleri sensör/yük ölçüm sonucu değildir; açıkta/bağlantısız analog girişlerin o andaki okumalarıdır.
- **LOG ÖZETİ:** 15:26:05–15:26:14 bölümünde 10'ar örnek: GPIO32 0.333–0.858 V (ortalama 0.634 V); GPIO33 0.142–0.468 V (ortalama 0.259 V); GPIO34 0.442–0.806 V (ortalama 0.588 V); ortak bias GPIO35 1.643–1.668 V (ortalama 1.657 V). Örnek sayısı kısa olduğundan bu aralıklar istatistiksel kararlılık iddiası değildir.
- **AĞ:** Wi-Fi Connected YES, IP 192.168.0.31; ESPHome API handshake başarılı.
- **BROWNOUT AYRIMI:** Önceki ayrı logda OTA rollback/brownout uyarısı vardı. Bu ilk bağlantısız ADC logunda brownout mesajı görünmüyor; bu kayıt önceki olayın nedenini açıklamaz.
- **SONUÇ:** Firmware'in cihazda çalıştığı ve dört ADC kanalının başlatıldığı LOG İLE DESTEKLENDİ. SCT okuma performansı, 100 W ampul tepkisi ve gerçek bağlantı doğrulanmadı. T010 AKTİF kalır; üç ayrı 100 W kanal testi bekliyor.
- **KAYNAK DOSYA ÖZETİ:** Kullanıcı ekindeki özgün log: 203 satır, 11,363 bayt; SHA-256 `88f897b2603815233b0c44e497261169be2e6bff73368b435ae04e38ebb312b3`. Depodaki kayıt dosyası önemli kurulum ve örnek satırlarını korur; özgün tam metin kullanıcı ekinde kalır ve SHA-256 özetiyle tanımlanır.

## 2026-10-31 — Modül 2 kapalı kutu montajı ve 100 W kanal test planı

- **KULLANICI BİLDİRİMİ:** ESP32D1, üç SCT kanalı ve Bias Trafosu modülü kapalı kutu içine gömüldü. Modül harici 5 V DC ile beslenecek.
- **KANAL TABLOSU:** SCT-1 sarı/GPIO32; SCT-2 yeşil/GPIO33; SCT-3 mavi/GPIO34; ortak bias izleme turuncu/GPIO35.
- **TEST PLANI:** Aynı 100 W akkor ampul SCT-1, SCT-2 ve SCT-3 kanallarında sırayla, ayrı ayrı kullanılacak. GPIO35 bias değeri her test boyunca izlenecek. Üç kanalın sonucu henüz girilmedi.
- **GÜVENLİK:** SCT yalnız tek yalıtılmış iletkeni çevrelemeli; faz+nötr birlikte geçirilmemeli. Kanal/CT bağlantısı değiştirilirken yük enerjisiz olmalı. Şebeke tarafı kapalı ve korumalı lamba düzeneğinde tutulmalı.
- **DURUM:** Montaj kullanıcı beyanıyla kaydedildi; YAML derleme ve üç kanalın fiziksel testi yapılmadı. T010 AKTİF.
- **KAYIT:** [Modül bağlantı tablosu ve test planı](docs/modules/SCT-OKUMA-TEST-MODULU.md#32-100-w-akkor-ampul-ile-kanal-bazli-test-plani).

# Güncel Durum — 2026-10-31

## Projenin iki fazı

1. **Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak: TAMAMLANDI.** Dış kaynaklı ESPHome ct_clamp koduyla hedef sağlandı. Dört yük karşılaştırmasının tamamı ±%4 içindedir. Faz 1'in yapılmamış işleri hedefe ulaşıldığı için kapatıldı; deney kayıtları tarihsel arşivde korunur.
2. **Faz 2 — Pratik yeniden kurulum ve sistem geliştirme: AKTİF.** Bu faz yalnız bulunan kodu PZEM ile eğitmek değildir. Kayıtlı kod ve çalışan örneklerden yararlanarak modüller ve ESP düğümleri yeniden devreye alınacak, temel işlevleri gerçek donanımda doğrulanacak ve sistem geliştirilecektir. PZEM referanslı veri aktarımı/etiketleme sonraki alt aşamadır. Kapsam kararı: [ADR-014](docs/decisions/ADR-014-phase2-practical-restart.md).

## Faz 1 sonuç kaydı

| Yük koşulu | Referans | Kod sonucu | Sapma |
|---|---:|---:|---:|
| 100 W akkor | 0,446–0,447 A | 0,4471 A | yaklaşık %0 |
| 150 W akkor | 0,616 A | 0,615 A | −%0,2 |
| Kettle düşük/kararlı | 0,637 A | 0,656 A | +%3,0 |
| Kettle kaynama | 6,39 A | 6,15 A | −%3,8 |

Bu karşılaştırmalar önceki kullanıcı kayıtları/loglarıyla desteklenmektedir. Harici kodun kaynak dosyasının depoda bulunmadığı ve Faz 2'nin henüz bağımsız öğrenme modeli üretmediği ayrımı korunur.

## Faz 2 yaklaşımı ve aktif görev

**Üst görev:** T009 — Modülleri ve ESP düğümlerini pratik olarak yeniden devreye alma.  
**Aktif somut modül görevi:** T010 — Modül 2 ESP32D1 üçlü SCT okuma modülü.

- Önce çalışan kod/örnek/kütüphane bulunur; depodaki YAML ve loglar başlangıç referansı olarak kullanılır.
- Her seferinde tek modül ve tek temel işlev ele alınır.
- Gerçek kart, pinout ve bağlantılar doğrulanır; minimum kod uyarlaması yapılır.
- Derleme, fiziksel bağlantı ve gerçek çalışma testi ayrı ayrı doğrulanır.
- Başarılı kod, gerçek log/çıktı ve yorum depoya eklenir.
- Manyetik teori ve ESP32 ADC iç mimarisi yalnız somut bir sorun veya karar bunları gerektirirse derinleştirilir. Önceki araştırmalar silinmez; gerektiğinde başvurulacak tarihsel bilgi olarak korunur.
- Modül/ESP sırası kullanıcıyla belirlenir; şimdiden sabit bir sıra dayatılmaz.

### Sonraki alt aşamalar

1. **T007 — HA → PC veri aktarımı:** PZEM ve SCT düğümleri çalışır, gerçek HA entity'leri oluşur hâle geldikten sonra.
2. **T008 — Kararlı alan eşleştirme/etiketleme:** gerçek PZEM/SCT geçmişi PC'ye aktarıldıktan sonra.
3. **T006 — K=24.22 değerlendirmesi:** eşleşmiş kararlı pencere verisi oluşunca.

## Korunan tarihsel kod ve donanım kayıtları

- Mevcut ESP32D2 ve diğer ESP YAML kayıtları silinmez; bunlar Faz 2 için başlangıç referanslarıdır, yeni donanımda test edilmiş oldukları varsayılmaz.
- E00F ayarları, eski pin eşlemesi ve bias RAW/voltaj geçmişi tarihsel baseline olarak korunur.
- Yeni Modül 2'nin üç SCT + bir bias ADC bağlantısı, GPIO seçimi ve firmware'i henüz uygulanmış/doğrulanmış değildir.
- ESP kartı, shield, USB bağlantısı, pin eşlemesi veya firmware değişiklikleri gerçek kart ve bağlantı bilgisi doğrulanmadan yapılmaz.

## Ana dosyalar

- [Yol haritası](ROADMAP.md)
- [İlerleme ağacı](PROGRESS_TREE.md)
- [Görev sırası](tasks/README.md)
- [T009 — Pratik modül/ESP devreye alma üst görevi](tasks/T009-practical-system-bringup.md)
- [T010 — Modül 2 ESP32D1 üçlü SCT modülü](tasks/T010-module2-triple-sct-bringup.md)
- [T007 — HA → PC aktarımı](tasks/T007-python-architecture.md)
- [T008 — Kararlı alan eşleştirme](tasks/T008-pzem-sct-stable-window-labeling.md)
- [T006 — Katsayı/model](tasks/T006-calibration.md)
- [Karar — Faz 2 yeni başlangıç](docs/decisions/ADR-014-phase2-practical-restart.md)

## 2026-10-31 — Modül 2 ilk dört kanallı ADC YAML kodu

- **KOD:** Kullanıcının verdiği ESPHome temel yapılandırması korundu; GPIO32/33/34 SCT girişleri ve GPIO35 ortak bias girişi için dört ayrı `platform: adc` sensörü eklendi.
- **YAYIN:** Dört sensör 1 saniyede bir voltaj örneği yayınlayacak şekilde tanımlandı.
- **SINIR:** Bu sürüm anlık ADC gerilim izleme kodudur; RMS/akım hesabı, ct_clamp, katsayı ve filtre içermez. Tekil ADC gerilimi akım ölçümü olarak yorumlanmaz.
- **DURUM:** YAML GitHub'a kaydedildi. Derleme, OTA yüklemesi, pinlerin fiziksel teyidi ve gerçek cihaz testi henüz yapılmadı. T010 AKTİF kalır.
- **SONRAKİ ADIM:** Önce analog düğüm gerilimlerini ölç; ardından ESPHome derleme kontrolü ve düşük gerilimde dört sensörün HA yayını testi.

## Modül 2 — T010 aktif çalışma

**Hedef:** Üç SCT sinyali + tek ortak bias ADC girişi olan, ESP32D1 gömülü, harici 5 V beslemeli ve USB üzerinden PC'ye erişilebilir modülü oluşturmak.

- ESPHome kimliği: `esp32d1` / `ESP32D1`.
- İlk ADC firmware: [firmware/esp32d1.yaml](firmware/esp32d1.yaml); GPIO32/33/34 için üç SCT gerilim sensörü ve GPIO35 için ortak bias gerilim sensörü tanımlı. Derleme ve fiziksel test bekliyor.
- 1. dişi SCT yuvası sarı sinyal kablosu: GPIO32 (KULLANICI BİLDİRİMİ).
- 2. dişi SCT yuvası yeşil sinyal kablosu: GPIO33 (KULLANICI BİLDİRİMİ).
- 3. dişi SCT yuvası mavi sinyal kablosu: GPIO34 (KULLANICI BİLDİRİMİ).
- Ortak bias ölçüm hattı turuncu kablo: GPIO35 (KULLANICI BİLDİRİMİ).
- Bias Trafosu modülü ve tek ortak bias devresi kapalı kutu içine gömülü (KULLANICI BİLDİRİMİ).
- Kapalı kutu modül harici 5 V DC ile beslenecek; PC USB erişimi mevcut olacak. İki kaynağın aynı anda kullanım koşulu kart güç yolu doğrulanmadan kabul edilmeyecek.
- ESP32 kart/shield tam modeli, jack tip/ring/sleeve eşleşmeleri ve bias ADC RAW/voltaj gösterimi açık.
- **LOG:** Kullanıcı ESPHome temel iskeletini, dört kablo/GPIO eşleştirmesini ve kapalı kutu montajını bildirdi; dört ADC sensörlü YAML ve 100 W kanal test planı depoya işlendi. Derleme, yükleme veya fiziksel kanal testi yapılmadı.
- **DURUM:** T010 AKTİF — kutu montajı kullanıcı beyanıyla yapıldı; ilk firmware derlemesi ve üç ayrı 100 W kanal testi bekliyor. Modül çalışır/tamamlandı değildir.
- Kayıtlar: [Modül 2](docs/modules/SCT-OKUMA-TEST-MODULU.md), [ADR-015](docs/decisions/ADR-015-module2-esp32d1-triple-sct.md), [T010](tasks/T010-module2-triple-sct-bringup.md).

## Önceki durum kayıtları — tarihsel arşiv

Aşağıdaki eski STATUS girdileri yazıldıkları tarihteki durumu korur. Güncel fazı ve aktif işi belirlemede bu dosyanın başındaki güncel bölüm esas alınır.

## 2026-10-31 — Güncel aktif yön: PZEM–SCT kararlı alan eşleştirme ve sürekli öğrenme

- **ANA HEDEF:** Kullanıcının paylaştığı çalışan E00F YAML'ını baseline olarak koru. PZEM-004T V3.0 ile SCT Raw AC/akım çıktısını aynı yük koşullarında karşılaştır; iki tarafta kararlı alanları ayrı belirle; örtüşen alanları eşleştirip PZEM ile etiketle; yeni verilerle 24.22 katsayısını/modelini iyileştir.
- **AKTİF SONRAKİ GÖREV:** T008 — PZEM ve E00F eşzamanlı gözlem kaydı ve kararlı alan eşleştirme hazırlığı. Henüz yeni kayıt/etiketleme yapılmadı; PLANLANDI.
- **ÇALIŞAN BASELINE:** Kullanıcının bu oturumda paylaştığı E00F ESP32D2 YAML. Bu kayıt derleme/OTA kanıtı değildir.
- **ÖĞRENME DÖNGÜSÜ:** kayıt → ayrı PZEM/SCT kararlılık analizi → örtüşen alanları eşleştirme → PZEM etiketleme → mevcut katsayıyı değerlendirme → yeni calibration_id ile iyileştirme → yeni koşullarda tekrarlama.
- **ct_clamp:** Şimdilik değiştirilmez. Önce PZEM eşleştirilmiş veride sorun aranır; tekrarlanabilir somut sorun çıkarsa hedefli kaynak kod incelemesi açılır.
- **KAPATILAN:** Ham 50 Hz dalga aktarımı, örnek başına timestamp, DMA/ADC Continuous ve bunlara bağlı örnekleme hızı geliştirmeleri (ADR-009).
- **PARK EDİLEN:** Eski T005/E00A/E01 yüksüz ADC/ham dalga planı ana PZEM etiketleme yolunun zorunlu ön koşulu değildir.
- **SINIR:** ±%4 sonucu harici kod için kullanıcı raporudur. Harici kodun kaynak dosyası depoda değildir; BERO Python öğrenme hattı bu sonucu yeniden üretmiş değildir.
- **SONRAKİ ÇIKTI:** T008 veri kayıt protokolü, gerçek PZEM/SCT HA entity listesi, zaman alanları ve ilk karşılaştırma senaryosu.
- **Ayrıntı:** [ROADMAP](ROADMAP.md), [ADR-010](docs/decisions/ADR-010-pzem-stable-window-learning-focus.md), [T008](tasks/T008-pzem-sct-stable-window-labeling.md).

## 2026-10-31 — Ölçüm hedefi sağlandı; yüksek hızlı ham edinim ara işleri kapatıldı

- **Karar:** Kullanıcının bildirdiği üzere yeni/harici kodla ±%4 sapma hedefi sağlandı. Bu nedenle 50 Hz ham dalga şeklini PC'ye aktarma, her ADC örneğini ayrı zaman damgasıyla saklama ve bu amaçla DMA/ADC Continuous firmware'i geliştirme işleri artık hedef değildir; **GEREKSİZ / KAPATILDI** olarak arşivlenir.
- **Kapsam:** Kapanış yalnızca bu ara edinim işlerine ilişkindir. E00F'nin çalışan ESPHome ct_clamp yolu ve ölçüm ayarları korunur. Ham dalga/örnek-zaman damgası gereksinimi yeni iş veya kabul kriteri olarak açılmaz.
- **Ölçüm kanıtı (KULLANICI RAPORU):** 100 W akkor: referans 0,446–0,447 A, kod 0,4471 A (yaklaşık %0); 150 W akkor: 0,616 A / 0,615 A (−%0,2); kettle düşük/kararlı: 0,637 A / 0,656 A (+%3,0); kettle kaynama: 6,39 A / 6,15 A (−%3,8). Dört karşılaştırmanın tamamı ±%4 sınırındadır. Değerler kullanıcının önceki gün sunduğu ölçümlerin mevcut konuşmada özetlenen tablosundan aktarılmıştır; ham ölçüm dosyaları ve referans cihazın bağımsız yeniden incelemesi bu depo güncellemesinde yapılmadı.
- **Önemli ayrım:** Bu sonuç, kullanıcı tarafından bildirilen harici kodla hedefe ulaşıldığını gösterir; harici kodun kaynak dosyası/commit'i bu kayda eklenmiş değildir. BERO deposundaki Python eğitim/model hattının tamamlandığı veya bağımsız genelleme testinin yapıldığı anlamına gelmez.
- **Korunan sınırlar:** ESPHome E00F YAML'ı, ct_clamp 200 ms penceresi, 2 s yayın aralığı, 24.22 katsayısı ve cihaz kimliği bu kararla değiştirilmez. E00F-N03 aç-kapa gözlemi kendi kapsamı içinde tamamlanmış kalır.
- **Sonraki odak:** Yeni örnek edinim altyapısı yerine çalışan ölçüm kodunun korunması, ölçüm koşullarının tekrarlanabilirliği ve mevcut referans karşılaştırmalarının kayıt altına alınması.
- **Durum etiketi:** ±%4 sonucu KULLANICI RAPORU; harici kodun repo içine alınması/bağımsız derlenmesi YAPILMADI.
- **Ayrıntı:** [ADR-009](docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md).

## 2026-10-31 — E00F-N03 100 W akkor yük aç-kapa gözlemi (TAMAMLANDI)

- **Durum:** Kullanıcı ampulü 10:32'de açtığını ve 10:39'da kapattığını bildirdi. Logdaki Raw AC düşüşü 10:39:27.837–10:39:29.819 aralığında gerçekleşiyor ve kullanıcı beyanıyla uyumlu. Kullanıcı CT bağlantısını da doğruladı: yalnız faz iletkeni, SCT içinden tek geçiş (1 tur). Bu donanım teyidi kullanıcı beyanıdır; bağımsız fiziksel inceleme değildir. N03'ün kendi kabul koşulu olan kapalı → açık kararlı → kapalı dönüş gözlemi karşılandı; test TAMAMLANDI. PZEM karşılaştırması/kalibrasyon ayrı görevdir, N03'ü açık tutmaz.
- **İlk log:** `esp32d2-logs (14).txt`, 222.950 bayt / 3.006 satır; SHA-256 `c4131d1d4a6f40f2024c05fa51eeed542cee4cf6b2d4a8f806d6a594ea72280e`. 262 CT penceresi; yük öncesi Raw AC medyanı 0.004 V, yük açık daha sakin bölüm medyanı 0.019 V.
- **İkinci log:** `esp32d2-logs (15).txt`, 375.017 bayt / 5.000 satır; SHA-256 `1ada9e16f102b8a290d2bdc3b8d7572c3ab442561f552acb081ee367f5a23952`. 455 CT penceresi; zaman aralığı 10:30:51.840–10:45:59.928.
- **Kapanış dönüşü:** 10:39:25.820'de 0.018 V, 10:39:27.837'de 0.006 V, 10:39:29.819'da 0.000 V. 10:40–10:46 bölümünde medyan 0.000 V (180 pencere), ortalama 0.00238 V. Başlangıç kesitinin 10:30:00–10:32:00 medyanı 0.004 V (35 pencere). Kullanıcının 10:39 kapatma beyanı bu geçişle uyumludur.
- **Yavaş ADC kanalları:** SCT GPIO32 RAW medyanı başlangıç/yük açık/yük sonrası 1842 / 1852 / 1842 count; SCT GPIO33 voltajı 1.642 / 1.657 / 1.642 V. Bias GPIO35 voltaj medyanı 1.653 / 1.653 / 1.653 V. Yavaş ADC yayınları 200 ms CT pencereleriyle eşzamanlı değildir.
- **Cihaz/log:** İkinci dosyada 455 CT DEBUG penceresi ve 0 ERROR/[E] satırı var. Bu dosya cihaz açılışını içermeyen devam kaydıdır; ilk dosyadaki açılış uyarılarıyla ilgili önceki not geçerlidir.
- **Sınırlar:** CT yerleşimi kullanıcı beyanıyla doğrulandı (yalnız faz, 1 tur); bağımsız fiziksel inceleme yapılmadı. PZEM karşılaştırması ve ham ADC örnek dizisi bu deneyin kapsamında/çıktısında yoktur. İki ham TXT dosyası Git'e aktarılmadı; SHA-256 ve analiz raporu kaydedildi.
- **Kapanış:** E00F-N03 aç-kapa gözlemi TAMAMLANDI. Sonraki çalışma proje STATUS/ROADMAP sırasındaki aktif göreve göre yürütülecek. Firmware, katsayı 24.22, eşik, pinler ve cihaz kimliği değiştirilmedi.
- **Ayrıntı:** [E00F-N03 raporu](experiments/E00F-unthresholded-overnight-log/E00F-N03-incandescent-step-observation.md), [deney YAML kaydı](experiments/E00F-unthresholded-overnight-log/E00F-N03-experiment.yaml).
## 2026-10-31 — E00F-N02 aykırı gözlem değerlendirmesi ve sonraki test

- **Aykırı olay:** 05:24:02 civarındaki 2.665238 A tepe, kullanıcının evde kedi bulunduğu ve tekil sıçramanın öneminin büyütülmemesi gerektiği yönündeki değerlendirmesiyle birlikte ele alındı. Olay ham veriden silinmedi; nedeni doğrulanmadığı için tekil/atıfsız aykırı gözlem olarak tutuldu. Kedi teması kanıtlanmış neden değildir.
- **Öncelik:** Tekil sıçrama yerine yüksüz davranışın geneli ve bilinen akkor yükte tekrarlanabilir tepki incelenecek.
- **Sıradaki test:** Önerilen E00F-N03 — 100 W akkor ampulle mevcut ESP32D2/E00F yapılandırmasını değiştirmeden kapalı → açık kararlı → kapalı kayıt. CT tek faz iletkenini tek turda çevrelemeli; fiziksel konum/tur sayısı ve olay saatleri kaydedilmeli. Dört ADC kanalı, Raw AC/akım ve cihaz DEBUG kaydı birlikte saklanmalı. Test henüz yapılmadı.
- **Değişiklik sınırı:** Katsayı 24.22, eşik, pinler, cihaz kimliği ve firmware bu test için değiştirilmeyecek. E00F-N03 sonrasında E08 Aşama 3 ADC Continuous/DMA tasarımına geçilecek; bu firmware henüz yazılmadı.
- **Ayrıntı:** [E00F-N02 raporu](experiments/E00F-unthresholded-overnight-log/E00F-N02-first-device-log.md#kullanici-degerlendirmesi-ve-sonraki-test-karari--2026-10-31).

## 2026-10-31 — E00F-N02 ESPHome DEBUG takip logu

- **Durum:** Kullanıcının sağladığı ESP32D2 DEBUG logu incelendi ve ham hali depoya arşivlendi.
- **Kapsam:** 10:18:09–10:23:46 cihaz log saati; 169 CT Clamp penceresi; N=2.820–3.309 (medyan 3.165), SPS=14.100–16.545 (medyan 15.825).
- **Teknik bulgu:** SPS her satırda N×5; bu 0.20 s pencerenin matematiksel karşılığıdır, bağımsız gerçek ADC örnekleme hızı değildir. Raw AC ile N/SPS korelasyonu yaklaşık 0.116; bu kısa logda örnek sayısı dalgalanması Raw AC değişimini açıklamıyor.
- **Tepe:** Takip logunda Raw AC maksimumu 0.02511 V / akım 0.608 A. Bu kayıt önceki 05:24:02 / 2.665238 A gece tepesini içermiyor. Yavaş GPIO okumaları CT penceresiyle eşzamanlı olmadığından tepeyi doğrulamaz/çürütmez.
- **Uyarılar:** ERROR veya [E] satırı yok; açılışta üç ESP32 framework optimizasyon uyarısı var.
- **Arşiv:** [E00F-N02 raporu](experiments/E00F-unthresholded-overnight-log/E00F-N02-first-device-log.md#esphome-debug-takip-logu--2026-10-31), [ham DEBUG logu](docs/technical-reviews/logs/2026-10-31-e00f-n02-debug-followup.log).
- **Karar:** YAML, katsayı, eşik, pin veya donanım değiştirilmedi. E00F-N02 AÇIK; gece tepe olayının fiziksel nedeni belirsiz.

## 2026-10-31 — E00F-N02 fiziksel koşul beyanı eklendi

- **KULLANICI BEYANI:** Gece gözlemi sırasında sistem boşta; kola temas 00:30 Türkiye saati sonrasında yok; akkor ampul henüz deney yükü olarak kullanılmadı.
- **YORUM:** 05:24:02'deki 2.665238 A tepe bildirilen kol temasına bağlanamaz. Sistem boşta beyanı altında 0.192920 A medyan, gerçek yük akımı olarak değil yüksüz CT/ADC/ct_clamp zinciri çıktısı olarak değerlendirilir.
- **SINIR:** Bu fiziksel koşul kullanıcı beyanıdır; bağımsız primer akım ölçümü değildir. E00F-N02'nin fiziksel nedeni belirsiz tepe olayı açık kalır.
- **Ayrıntı:** [E00F-N02 tam gece raporu](experiments/E00F-unthresholded-overnight-log/E00F-N02-first-device-log.md).
## 2026-10-31 — E00F-N02 tam gece HA geçmişi analizi

- **Durum:** Kullanıcının sağladığı tam gece CSV'si incelendi. Kayıt aralığı 2026-10-30 20:15:00Z–2026-10-31 07:07:48.897Z (Türkiye saati 23:15:00–10:07:48.897), toplam 10:52:48.897; 177.370 satır ve 6 entity.
- **Özet:** SCT akım 19.113 sayısal kayıt; medyan 0.192920 A, ortalama 0.194878 A, maksimum 2.665238 A. Raw AC medyan 0.007965 V, maksimum 0.110043 V. GPIO32 SCT RAW medyan 1841 count; GPIO34 Bias RAW medyan 1840 count. GPIO33 ve GPIO35 voltaj medyanları 1.653 V.
- **Karşılaştırma:** Yakın zamanlı (≤1.2 s) SCT/Bias RAW eşleştirmesinde 34.600 çift; fark medyanı 0 count, ortalaması −0.377 count, SD 12.673 count. Akım ve Raw AC aynı CT Clamp yolunun katsayı öncesi/sonrası çıktılarıdır; 24.22 çarpanı ile bağıntı doğrulandı, bağımsız teyit sayılmaz.
- **Dikkat çeken olay:** 31 Ekim 05:24:02.363 Türkiye saati civarında 2.665238 A / 0.110043 V tepe kaydı. Yavaş ve eşzamanlı olmayan ADC geçmişiyle olayın fiziksel nedeni sınıflandırılamaz; değer silinmedi.
- **Yorum sınırı:** Entity kayıt aralıkları farklıdır; CT/Raw AC medyanı fiziksel yük durumu teyit edilmeden gerçek akım veya yüksüz taban kabul edilmez. HA CSV 200 ms ham örnekleri ve N/SPS debug satırlarını içermez.
- **Açık:** Fiziksel primer yük durumu, CT'nin hangi iletkeni/kaç turu gördüğü ve kol teması zaman aralığı kullanıcı teyidi bekliyor. Varsa ESPHome DEBUG logu ayrıca incelenecek.
- **Ayrıntı:** [E00F-N02 tam gece analizi](experiments/E00F-unthresholded-overnight-log/E00F-N02-first-device-log.md#tam-gece-home-assistant-gecmis-analizi--2026-10-31).
- **Durum kararı:** Analiz yapıldı; fiziksel koşul doğrulaması açık olduğundan E00F-N02 TAMAMLANDI işaretlenmedi.

## 2026-10-30 — E00F-N02 gece gözlemi ara CSV ve oturum kapanışı

- **Durum:** Dört ADC kanalının cihazda başlatılması ve HA'ya yayın yapması kullanıcı loguyla doğrulandı. Gece gözlemi DEVAM EDİYOR; bu oturum kapatıldı, deney kapatılmadı.
- **Ara HA CSV:** Kullanıcının sağladığı 651 satırlık CSV, 20:15:00–20:17:32.469 UTC (Türkiye saati 23:15:00–23:17:32.469) aralığını kapsıyor; yalnızca 2 dk 32 sn. Altı entity mevcut. Akım 47 kayıt, 17 sıfır/30 sıfırdan farklı, maksimum 0.285943 A; Raw AC maksimum 0.011806 V. GPIO32/33/34/35 istatistikleri ve sınırlamalar [E00F-N02 raporuna](experiments/E00F-unthresholded-overnight-log/E00F-N02-first-device-log.md) işlendi.
- **Yorum sınırı:** Bu CSV sabaha kadar süren kayıt değildir. Entity kayıt sayıları farklı, okumalar eşzamanlı değil; fiziksel yük durumu teyit edilmedi. Korelasyon, nedensellik, yüksüz taban veya uzun dönem drift sonucu çıkarılmadı.
- **Sabah işi:** Tam HA geçmiş CSV'sinin kapsama aralığı ve entity kayıt sürekliliği incelenecek; varsa ESPHome DEBUG dosyası ayrıca değerlendirilecek. Yük durumu ve kablo/sensör konumu kullanıcı teyidiyle kaydedilecek.
- **Oturum kaydı:** [SESSION_LOG](HISTORY/SESSION_LOG.md) güncellendi. Ham CSV Git'e eklenmedi.

## 2026-10-30 — E00F-N02 dört ADC kanalı ilk cihaz logu

- **Durum:** İlk cihaz çalışma doğrulaması başarılı (KULLANICI LOGU). ESPHome 2026.10.1 / ESP32 rev3.1; OTA/API bağlantısı ve Home Assistant API bağlantısı başarılı.
- **HEDEF:** GPIO32/33 SCT çifti ile GPIO34/35 bias çiftinin aynı firmware'de çalışmasını doğrulamak.
- **LOG:** Dört ADC kanalı da ADC1 üzerinde başlatıldı; her kanal için Handle Init, Config, Calibration ve Overall Init OK. Dört sensör 1 s güncelleme aralığında. CT Clamp 200 ms pencere / 2 s yayın. Cihaz 23:13:34'te loga bağlandı; 23:14:28.959'da "Boot seems successful".
- **İLK KESİT:** 204 kayıt/kanal; GPIO32 RAW 1819–1865 count (ortalama 1849.75), GPIO33 1.644–1.671 V (ortalama 1.66029 V), GPIO34 RAW 1824–1872 count (ortalama 1849.67), GPIO35 1.600–1.677 V (ortalama 1.65978 V). GPIO35'te 1.600 V yalnızca bir kez görüldü; dışlanmadı, tekil aykırı gözlem olarak not edildi.
- **CT CLAMP:** 102 pencere; 47 sıfır ve 55 sıfırdan farklı akım yayını. Akım aralığı 0–0.343 A, ortalama 0.08504 A. Raw AC aralığı 0–0.01416 V. Hatta yük durumu logdan çıkarılamaz; yüksüzlük kullanıcı tarafından ayrıca teyit edilmelidir.
- **SPS:** Debug satırlarında 13,360–16,550 SPS, ortalama yaklaşık 15,783 SPS. Bu, CT Clamp'in kabul ettiği farklı örneklerden türetilen göstergedir; bağımsız doğrulanmış donanım ADC örnekleme hızı değildir.
- **YORUM:** Dört ADC girişinin başlatılması ve sensör yayınları cihaz üzerinde doğrulandı. Fiziksel analog doğruluk, pin kablolaması, yüksüz taban karakterizasyonu ve akım kalibrasyonu doğrulanmadı. Uzun süreli gözlem ve sabah HA geçmiş dökümü bekleniyor.
- **KAYIT:** [E00F-N02 ilk cihaz logu](experiments/E00F-unthresholded-overnight-log/E00F-N02-first-device-log.md).
- **Açık:** Sabah HA geçmiş CSV'si, fiziksel yük durumu teyidi ve uzun dönem analiz.

## 2026-10-30 — E00F-N01 bias referansı izleme eklentisi

- Mevcut SCT013/ct_clamp yolu GPIO33, 200 ms pencere, 2 s yayın ve 24.22 katsayısıyla korunmuştur.
- GPIO34 bias RAW count ve GPIO35 bias ADC voltajı, mevcut bağlantı noktaları kullanılarak 1 s aralıkla izlenecek şekilde YAML'a eklendi.
- SCT Raw AC gerilimi de `on_raw_value` üzerinden ayrı V entity'sine aktarılır; bu değer ct_clamp çarpanından öncedir.
- GPIO34/35 ayrı ADC okumalarıdır; eşzamanlı örnek değildir. 1 s kayıt yüksek frekanslı gürültü spektrumu veya 50 Hz dalga şekli sağlamaz.
- Depo YAML'ı güncellendi. Bu kayıt tek başına derleme, OTA veya gece ölçümünün gerçekleştiğini kanıtlamaz; bunlar kullanıcı cihaz loguyla doğrulanacaktır.
- Deney planı: [E00F-N01](../experiments/E00F-unthresholded-overnight-log/experiment.yaml).

**ESP ölçüm mimarisi / E09 kararı (2026-10-30):** Kullanıcı kararıyla ESP-1 yalnız SCT013 ana sensörüne ve hızlı örneklemeye ayrıldı; PZEM veya yardımcı sensör görevi almayacak. ESP-2'de PZEM-004T V3.0, 1 adet ACS712-5A ve 1 adet ZMCT103C-5A aşamalı test edilecek: PZEM tek başına → ACS712 tek başına → ZMCT103C tek başına → PZEM+ACS712 → PZEM+ZMCT103C → üçü birlikte. Karar ADR-008'e, test planı E09'a, sensör adetleri envantere işlendi. Bu mimari/test planı kaydıdır; ESP-2 pinleri, analog ön uç, fiziksel kart eşleşmesi ve sensör testleri henüz doğrulanmadı. E09 henüz uygulanmadı.

**E00F-N01 gece gözlemi (2026-10-30):** Kullanıcı talebiyle çalışan E00F YAML'ındaki 0.35 A altını sıfırlayan lambda filtresinin kaldırıldığı depo sürümü hazırlandı. GPIO33, ADC1/12 dB, raw:false, 200 ms, 2 s, 24.22 ve esp32d2 kimliği korundu. Derleme, cihaza yükleme ve gece logu henüz bekleniyor. Home Assistant geçmişi yayınlanan akım entity durumlarını tutar; Raw AC/N/SPS debug satırları ayrıca sürekli kaydedilmelidir. Deney: [E00F-N01](experiments/E00F-unthresholded-overnight-log/experiment.yaml).

# Proje durumu

**E00F yan inceleme notu (2026-10-30):** Claude/Copilot son değerlendirmesi ve üç sarımlı düşük akım cihaz logu teknik inceleme raporuna işlendi. Üç tur denemesinde yük açıkken pens yaklaşık 0.04 A; 12 Raw AC penceresi 0.004–0.014 V ve yayınlar 0.000 A. Değerler önceki yüksüz/LED aralıklarıyla örtüşüyor; bu kısa kayıt ayrışma başarısı göstermiyor. Ana fiziksel düzen için tek sarım korunuyor. Python'da PZEM referanslı bölgesel kalibrasyon önerisi kaydedildi; henüz model/eğitim/kalibrasyon uygulanmadı. E00F bu notu E00B aktif görev sırasının yerine geçirmez.


**Uzun vadeli yön:** Tek bir akım ölçerle sınırlı olmayan, göreve göre sensör ve donanımı değişebilen ESP tabanlı sistemler; model/katsayı öğrenimi ve ileride başka görevler için örüntü algılama. Bu vizyon [proje felsefesinde](docs/project-philosophy.md) açıklanır; E00A'nın SCT'siz bias-only alt koşulu kapatıldı; E00A'nın diğer işleri açık, yeni aktif hazırlık E00B SCT bağlı/akımsız ADC gözlemidir.

**Genel görünüm:** [İlerleme ağacı — PROGRESS_TREE.md](PROGRESS_TREE.md). Deneylerin nedenini, kod/kanıt durumunu ve sonraki karar kapısını izlemek için [Deney ve karar izleme defteri](EXPERIMENT_LEDGER.md) kullanılır. Projenin kişisel veri kümesi, model öğrenimi ve kabul edilebilir sınırlarına ilişkin yaklaşım [proje felsefesinde](docs/project-philosophy.md) kayıtlıdır. Depoyu baştan sona okumadan genel resmi görmek için önce ilerleme ağacına, ardından bu dosyadaki güncel duruma bak.

**Park edilmiş tasarım fikri:** İleride tur sayısı hat profiline göre seçilebilir; E08'in mevcut 1/2/4 tur matrisi korunur. 5 tur henüz yalnız öneridir; aktif görev veya firmware değişikliği değildir. [SCT tur sayısı tasarım notu](docs/technical-reviews/2026-10-30-ct-primary-turn-count-design-note.md) ve [I005 fikir kaydı](IDEA_BACKLOG.md).

**Son güncelleme:** 2026-10-30 — E08 grafik standardı kullanıcı tarafından onaylandı: zaman ekseninde mavi Bias GPIO34 RAW, kırmızı SCT GPIO32 RAW ve yeşil olay işareti. Kullanıcı daha hızlı örnekleme ile salınımları ayrıntılı görmek istedi. Sıradaki hazırlık, ESP32D2 kimliği ve mevcut GPIO eşlemeleri korunarak ADC continuous/DMA tabanlı iki kanallı ham edinim tasarımıdır; ilk hedef 1 kS/s/kanal (toplam 2 kconversion/s), 200 ms ham pencere. Bu henüz tasarım/plan aşamasıdır; firmware yazılmadı, derlenmedi veya cihaza yüklenmedi. Grafik standardı ve hızlandırma planı: [E08 yüksek hızlı edinim hazırlığı](experiments/E08-sct-characterization/stage-03-high-speed-capture.md).\n\n**Önceki güncelleme:** 2026-10-30 — E00B uzun logu kaydedildi; 351 geçerli yayın/kanal üzerinden SCT ve bias karşılaştırması olumlu (RAW fark +0.82 count, ADC voltaj farkı −1.4 mV). Ham log ve analiz E00B klasöründe. Fiziksel primer akım/CT montaj koşulu logdan bağımsız doğrulanmış değil. Sonraki yük koşulunda mevcut dört kanallı E00B firmware’i aynı noktaları izlediği için kod değişikliği gerektirmiyor; koşul ayrı log ve sonuç olarak kaydedilecek. E00A’nın diğer işleri açık kalır.\n\n**Önceki güncelleme:** 2026-10-30 — E00A'nın SCT bağlı olmayan bias-only alt adımı, son ESP32D2 logu ve taban dalgalanması yorumu ile KAPATILDI. GPIO35 gözlenen standart sapma 6.474 mV; GPIO34 RAW 6.97 count. Bu, tüm ölçüm zincirinin dalgalanmasıdır; ADC'nin tek başına gürültüsü değildir. RAW=0 başlangıçları eşleştirme dışı bırakıldı. E00A bütünü açık: 3.3 V bölücü koşulu ve ham CSV/grafik eksik. Önceki E00A-S01 GND referans testi kaydedildi; GPIO34 0 count, GPIO35 kararlı bölümde 0.142 V; floating giriş teşhisi destekleniyor. Elektriksel çözüm adayı Vmid'e yüksek değerli pasif bias direnci; kesin değer ve jack topolojisi doğrulanacak. Ayrıntı E00A-S01 raporunda. E00A henüz açık. Önceki durum: E00A açıldı; ilk iki multimetre referansı kaydedildi: L78L33 çıkışı 3,31 V, breadboard bias orta noktası/Vmid 1,65 V (KULLANICI BİLDİRİMİ). Bu ESP32 ADC ölçümü değildir. Her ADC koşulu için 30 saniyelik gözlem planlandı. Ayrı/geçici 10k/10k ölçüm bölücüsü bias devresinin parçası değildir ve fiziksel olarak kurulmuş sayılmaz. ESP32D2 için E00A firmware'i depoya eklendi; kullanıcı derlendiğini ve çalıştığını bildirdi (KULLANICI RAPORU). ADC sayısal logu ve ham kayıt henüz bekleniyor. 2026-10-29 — Gün sonu çapraz kontrolü: E00A'da ham ADC kaydı ve bilgisayarda zaman grafiği temel hedef; istatistikler yardımcı. T007 mimari taslağı, edinim kanıtı oluşana kadar beklemede. PZEM/akım formülü/MCP3208 ilk aşamanın kapsamı değil.  
**Belge denetimi:** TAMAMLANDI — temel durum/karar dosyaları, deney sırası, hedef alan sözlüğü ve 87 Markdown dosyasındaki göreli bağlantı hedefleri kontrol edildi; bulunan tek kırık göreli bağlantı düzeltildi. Bu yalnızca depo belgelerinin denetimidir; fiziksel veya yazılım doğrulaması değildir. **Fiziksel deney hazırlığı:** BEKLEMEDE — seçilecek kart/GPIO gerçek kart üzerindeki pinout ile eşleştirilmeli, ADR-007'deki 10 µF değişikliği fiilen uygulanıp kayda geçirilmeli, ham kayıt formatı ve yerel dosya yolu kullanılmalıdır. JSON Schema validator, YAML parser, firmware derlemesi, CI ve fiziksel test bu turda çalıştırılmadı. İlk teknik deney E00A olarak korunuyor.  
**Aktif faz:** Faz 1 — SCT analog ön uç ve yüksüz ölçüm hazırlığı  
**Sıradaki iş:** E00B firmware'i kullanıcı bildirimiyle derlendi; sırada gerçek kart pinout/GPIO32-33 doğrulaması, fiziksel bağlantı, cihaza yükleme ve SCT bağlı/primer akımsız logudur. Bias GPIO34/35, SCT GPIO32/33 planı korunur. E00A'nın 3,3 V bölücü koşulu ve ham CSV/grafik işi ayrıca açık kalır. E00A — bias trafosu DC noktalarının ADC gözlemi (AÇILDI; ilk multimetre referansı kaydedildi). L78L33 çıkışı 3,31 V (kullanıcı multimetre bildirimi); breadboard bias orta noktası/Vmid 1,65 V (kullanıcı multimetre bildirimi). Her koşul için 30 saniye planlandı. 3,3 V ölçüm aparatı olarak ayrı/geçici 10k/10k bölücü düşünüldü; ADC sınırları doğrulanmadan bağlantı yapılmayacak. SCT bağlı değil. GPIO34 yalnız gerçek ESP32-WROOM-32D kart/pinout doğrulanırsa kullanılacak. Sonrasında E00 ve T005/E01 hazırlığı gelir. [E00A — Ham sinyal kaydı ve temel istatistikler](experiments/E00A-raw-waveform-observation/README.md) AÇILDI; ilk iki multimetre referansı kaydedildi: L78L33 çıkışı 3,31 V, breadboard Vmid 1,65 V; ESP32D2 firmware'i kullanıcı bildirimiyle derlendi/çalıştı; GPIO34 raw ve GPIO35 voltaj sensörlerinin logu bekleniyor. 30 saniyelik ham CSV/grafik henüz yok; ardından [E00 — Bias ADC karşılaştırması](experiments/E00-bias-adc-baseline/protocol.md) ve [T005 — ADC temel okumaları ve E01 gürültü tabanı](tasks/T005-noise-floor.md). E00A'nın ilk hedefi ADC'den ne okunduğunu görmek, ham örnekleri kaydetmek ve bilgisayarda görselleştirmektir. Grafik bu aşamada temel inceleme aracıdır; istatistikler yardımcıdır. PZEM karşılaştırması, akım formülü/kalibrasyon ve MCP3208 ilk adımın kapsamı değildir. T005 — PLANLANDI. İlk önce SCT bağlamadan bias noktasında `analogRead()` ham sayısı ile `analogReadMilliVolts()` karşılaştırılacak; sonra SCT bağlıyken akım yok durumunda aynı iki okuma yapılacak; uzun E01 gürültü kaydı daha sonraya bırakıldı. T003, PZEM'e göre ±%4 bağıl sapma ve Python `OK` karar kuralı belirlenerek kapatıldı. T001 envanter ve T002 güvenlik kontrolü, kullanıcının tamamladığını bildirdiği bilgiler esas alınarak kaydedilip kapatıldı.  
**Öncelikli SCT:** SCT013-030 (30 A / 1 V)  
**PZEM:** Esas kaynak [DONANIM/PZEM-004T/README.md](../../DONANIM/PZEM-004T/README.md); CT modeli kullanıcı tarafından PZCT-02 (0–100 A) olarak belirtildi.  
**Bias üretim alt devresi:** TAMAMLANDI — kullanıcı onayı. RN130421 + KBU6M + 2200 µF / 35 V + L78L33; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) kondansatör. Bağımsız ölçüm raporu bu kayda eklenmedi.  
**SCT/bias devresi:** Kullanıcı tarafından tarif edilen bağlantıda SCT dişi jack üzerinden breadboard bias alt devresine bağlanır; alt devrede 2 × 10 kΩ dirençle orta nokta ve orta noktadan GND'ye mevcut 104 (100 nF) kondansatör vardır. ADR-007 planına göre bu kondansatör sökülmeden aynı Vmid–GND noktalarına paralel 10 µF elektrolitik kondansatör eklenecek (pozitif uç Vmid, negatif uç GND); fiziksel uygulama henüz doğrulanmadı. Bias yaklaşık 1,65 V kabul edilir; bu aşamada ayrıca ölçülmesi şart değildir. Harici ADC kullanılmayacak; ESP32 dahili ADC kullanılacak, MCP3208 sonraya bırakıldı. Bias'ın ayrı kayıt alanı olması yazılım/veri kaydı aşamasında ele alınacak. ADC GPIO/pin planı firmware aşamasına aittir. T004 hobi düzeyi belgeleme kapsamıyla tamamlandı; laboratuvar düzeyinde ADC aralığı/clipping hesabı T004 kapanış şartı değildir.  
**PF ve akım ölçümüne ilişkin teknik not:** [PF değişimi ve akım ölçümüne etkisi](docs/architecture/pf-and-current-measurement.md). PZEM'in gerilim ölçümü doğrudan hattan, akım ölçümü harici CT'den gelir; yayınlanan PF bu ölçüm zincirinin birleşik sonucudur. PZEM PF ve akım değerleri SCT karşılaştırmasında birlikte kaydedilecek. Farklı PF koşullarındaki SCT-PZEM hata davranışı [E09](experiments/E09-pf-current-relationship/README.md) kapsamında incelenecek; aktif ilk deney sırası değişmez.

**SCT/PZEM eğitim ve gözlem mimarisi:** [Hedef mimari notu](docs/architecture/sct-pzem-labeling-and-calibration.md) ve [eğitim + ham akış gözlem belgesi](docs/architecture/training-and-dynamic-observation.md). Aynı SSR aç-kapa deneyinden (1) PZEM/SCT ortak kararlı alanlarını etiketleyip model eğitme ve aynı etiketli veride eğitim içi uyum raporu, (2) aynı olayın geçişler dahil tam ham SCT akışında model tahminini PZEM zaman serisiyle ortak zaman ekseninde gözleyip tepki/gecikme incelemesi yapılması hedeflenir. Bu iki rapor ayrıdır. Firmware, algoritma, model ve deneyler henüz yapılmadı.  
**SSR:** SAMM Market 5 V, 2 kanallı kart; tedarikçi kodu İzmo9659, SKU MP02637. Giriş mantığı ve kart üzerindeki SSR'nin tam kodu doğrulanmalı.  
**RTC:** İki DS3231 modülünde de 2032 tipi pil bulunuyor. RTC kodunun çalıştığı ve güç kesilip yeniden verildikten sonra saatin korunduğu daha önce test edildi; bu bilgi esas alınır ve test tekrar istenmeyecek. Yüksek hızlı örnekleme zamanlaması ESP32 monoton zamanlayıcısına aittir.  
**Deney durumu:** Donanım henüz kurulmadı; E00A bias trafosu 3,3 V ve Vmid ADC karşılaştırması, E01 yüksüz gürültü kaydı, E07 eski planı, E08 karakterizasyon planı ve kalibrasyon YAPILMADI. Donanım henüz kurulmadı; E00 bias-only ADC karşılaştırması, E01 yüksüz gürültü kaydı, E07 eski planı, E08 yeni karakterizasyon planı ve kalibrasyon YAPILMADI. Güncel SCT karakterizasyon sırası [E08](experiments/E08-sct-characterization/README.md): (1) yüksüz uzun okuma, (2) 100 W akkorla 1/2/4 kablo turu × 1/2/2,5 kS/s matrisi, (3) aynı matrisin 150 W akkor ve 8,5 W LED'de tekrarı, (4) sonuçlardan sonra aç-kapa davranışı. Aynı pencere örneklerinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanacak; yardımcı istatistikler ve gerçekleşen örnekleme hızı kaydedilecek. PZEM veya başka ESP'nin ortalama akımı yalnız genel deney notudur; SCT pencereleriyle zaman eşleştirmesi yapılmaz. Kararlılık eşiği, pencere sayısı ve kesin kayıt süresi önceden sabitlenmez. Önceki [E07 protokolü](experiments/E07-sct-stability-step-tests/protocol.md) fiziksel olarak uygulanmadı; güncel plan için E08 esas alınır. E00A öncelikli ilk deneydir; ardından T005/E00-E01 hazırlığı gelir. 30 saniye asgari başlangıç referansıdır, üst sınır değildir; kesin süre belirlenmedi. PZEM ve diğer ESP kartları ölçülen hattan beslenmez; beslemeleri ayrıdır.

## Oturum sürekliliği
- Yeni oturumda başlangıç protokolü uygulanır: güncel main/son commit kontrol edilir; AGENTS, STATUS, ROADMAP, open-questions, ilgili görev/deney ve son günlük kaydı okunup karşılaştırılır.
- Başlangıç raporunda okunan kaynaklar, mevcut durum, hedef ve kabul koşulları kısaca belirtilir. Önceden kaydedilmiş bilgiler depoda aranıp kontrol edilmeden kullanıcıdan tekrar istenmez.
- Kullanıcı beyanı, üretici belgesi, hipotez, hesap ve ölçüm sonucu ayrı tutulur; commit sonrası dosyalar yeniden okunur, test/CI çalışmadıysa açıkça yazılır.

## Bildirilen stok

| Bileşen | Adet / özellik | Kaynak |
|---|---:|---|
| SCT013-030 (30 A / 1 V) | 7 | Kullanıcının verdiği envanter bilgisi; jack çıkışlı |
| SCT013-100A-1V | 10 | Kullanıcı bildirimi; jack çıkışlı |
| SCT013 toplamı | 17 | Kullanıcının verdiği envanter bilgisi |
| ESP32-C3 SuperMini | 1 | Envanter kaydı / önceki SSR düğümü |
| ESP32 ölçüm düğümü | 1 | Envanter kaydı / önceki PZEM düğümü |
| PZEM-004T | V3.0 | Kullanıcı bildirimi |
| Masaüstü güç kaynağı | 5 V / 1,8 A | Kullanıcı bildirimi |
| Test yükleri | 100 W ve 150 W ampuller ana deney yükleri; 5 W LED ampul farklı PF için | Planlanan test yükleri; gerçek güç, akım ve PF ilgili testte ölçülecek |
| Breadboard bias alt devresi | Mevcut kayıt: 2 × 10 kΩ ve Vmid–GND arasında 104 (100 nF); ilk SCT bağlantılı ölçümden önce aynı noktalara paralel 10 µF elektrolitik eklenmesi planlandı (pozitif Vmid, negatif GND) | Mevcut durum kullanıcı bildirimi; değişiklik bekliyor |
| Jack yuvaları ve bağlantı/ölçüm parçaları | Tam takım mevcut | Kullanıcı bildirimi |

## Mevcut bilgi
- Önceki BERO'daki SCT, PZEM, ESP32, MCP3208, SSR ve DS3231 teknik kaynakları proje referanslarına bağlandı.
- Bias üretim alt devresi, kullanıcının onayıyla tamamlandı sayılıyor; bağımsız voltaj ölçüm raporu eklenmedi.
- SCT013 sinyalinin breadboard bias devresi üzerinden ESP32'nin dahili ADC'sine alınması planlanıyor. 8 kanallı analog arayüz kartı mevcut değildir. MCP3208 sonraki aşamaya ayrılmıştır.
- PZEM için mevcut BERO kaydı kullanılıyor; bağlı CT modeli PZCT-02 (0–100 A) olarak belirtildi.
- SSR kartının tam giriş tetik mantığı ve fiziksel SSR parça kodu doğrulanmalı.
- Deneyler ve kalibrasyon sonuçları henüz eklenmedi.

## Karar kapıları
- [ ] G1 — SCT modeli PZEM referans akışına göre önceden belirlenen ±%4 hedefinde değerlendirildi; veri, sınırlamalar ve clipping durumu kaydedildi. Bu, bağımsız mutlak doğruluk kanıtı değildir.
- [ ] G2 — PZEM okuma durumu izleniyor; geçersiz okumalar özetlerden dışlanıyor.
- [ ] G3 — örnekleme hızı hedef yüklerde ölçülmüş metriklerle gerekçelendirilmiş.

## Sıradaki işler
1. [x] [T003 — PZEM tabanlı model hata hedefi](tasks/T003-reference-and-error-target.md): ±%4 bağıl sapma; Python geçerli örneklerde `OK` kararı verir.
2. [x] [T004 — Analog ön uç](tasks/T004-analog-frontend.md): mevcut jack/bias bağlantısı, SCT modelleri ve ESP32 dahili ADC yaklaşımı belgelendi.
3. [ ] [T005 — E01 gürültü tabanı](tasks/T005-noise-floor.md): donanım kurulduktan sonra yüksüz ADC verisini toplama ve grafikleme.
4. E00/E01 temel okumaları sonrasında [E08 SCT karakterizasyon planı](experiments/E08-sct-characterization/README.md) uygulanacak; E07 önceki, uygulanmamış plan olarak korunur.

## Açık engeller
- Donanım henüz kurulmadı. Gerçek bağlantı kurulurken SCT jack–breadboard bias bağlantısı ve ESP32 ADC pini uygulanacak donanımla eşleştirilecek; firmware/pin planlama aşamasında GPIO seçimi yapılacak. T004 kapsamında laboratuvar düzeyinde ADC aralığı/clipping hesabı istenmiyor.
- T005 için gerçek donanım kurulumundan sonra yüksüz veri toplama, süreyi belirleme ve grafik üretme bekleniyor.
- SSR'nin hangi iki AC yükü anahtarlayacağı, GPIO eşlemesi ve giriş mantığının düşük gerilimde doğrulanması.
- T003 TAMAMLANDI: model tahmini geçerli PZEM akımından ±%4 bağıl sapma içindeyse Python sonucu `OK` işaretler. Kararlı alan gözlemi ve SCT istatistikleri ayrı görev/deneylerde ele alınır. Test yükleri ilgili test kaydında beyan edilecek.

Firmware, deney ve kalibrasyon sonuçları henüz eklenmedi. E07 protokolü eklendi; kararlılık eşiği/pencere sayısı henüz belirlenmedi ve fiziksel test yapılmadı.

## Öncelikli ilk deney — E00A (2026-10-29)

E00A, E00/E01 hazırlığından önce gelir. E00A için ilk iki koşul bias trafosu L78L33 çıkışı ve Vmid'dir; her koşulda 30 saniyelik ADC gözlemi planlanır. Örnekleme hızı firmware aşamasında belirlenecek. Ortalama, min/max, tepe-tepe aralığı, standart sapma, gerçek süre ve örnek sayısı ana çıktılardır. Grafik yalnızca istatistikleri yorumlamak veya şüpheli örnekleri incelemek için üretilir. Farklı hızlar, üç ESP32 eşzamanlaması, yavaş oynatma, DMA veya çift buffer ilk kabul koşulu değildir. Fiziksel ölçüm yapılmadı.

## İlk test sıralaması — 2026-10-29

1. E00: SCT bağlı değil; bias orta noktası → ADC GPIO. `analogRead()` ham sayısı ve `analogReadMilliVolts()` aynı döngüde okunup voltmetreyle karşılaştırılacak.
2. SCT bağlı, ölçülen hatta akım yok: aynı iki okuma tekrar edilecek.
3. Ardından E01'in uzun yüksüz kayıt/grafik ve gürültü özeti yapılacak.

E00 protokolü: [Bias-only ADC baseline](experiments/E00-bias-adc-baseline/protocol.md). Henüz fiziksel ölçüm yapılmadı.

## 2026-10-29 belge incelemesi

- Kullanıcının sağladığı SCT013_30A_1V_ESP32_Raporu.docx ve ct-akım-trafosu-satürasyonu.txt okundu.
- SCT013-030 nominal oranı, gerilim çıkışlı modelde dahili burden bilgisi ve genel satürasyon riskleri donanım referanslarına eklendi.
- [ADR-007](docs/decisions/ADR-007-bias-midpoint-capacitor.md) kapsamında mevcut 100 nF kondansatöre paralel 10 µF eklenmesi, E00A'nın ilk SCT bağlantılı koşulundan önce planlandı. Fiziksel değişiklik ve sonuç ölçümü henüz yapılmadı; ADC GPIO'suna ek 100 nF kararı verilmedi.
- Rapordaki genel ESP32/ADS1115/RMS örnek kodları BERO firmware'i olarak alınmadı.
- Fiziksel ölçüm, ADC okuması, firmware testi ve kalibrasyon yapılmadı.


## Bias kondansatörü — aktif donanım notu

- Mevcut kayıtlı devrede bias orta noktasından GND'ye 104 (100 nF) bulunur.
- [ADR-007](docs/decisions/ADR-007-bias-midpoint-capacitor.md) 10 kΩ + 10 kΩ bölücü ve 50 Hz SCT sinyali için orta noktadaki mevcut 100 nF'ye paralel 10 µF eklenmesini önerir. Değişiklik E00A'nın ilk SCT bağlantılı koşulundan önce planlanmıştır; fiziksel olarak yapılana kadar tamamlandı sayılmaz.
- ADC pinine ayrıca 100 nF eklenmesi opsiyoneldir; ilk E01 ölçümünde aynı anda ikinci değişken eklememek için şimdilik planlanmadı.


## 2026-10-29 — E08 SCT karakterizasyon planı

Kullanıcıyla mutabık kalınan sıra E08 olarak kaydedildi: (1) SCT yüksüz uzun okuma ile temel gürültü/bias davranışı, (2) 100 W akkor ile 1/2/4 kablo turu × 1/2/2,5 kS/s matrisi, (3) aynı matrisin 150 W akkor ve 8,5 W LED'de tekrarı, (4) sonuçlar görüldükten sonra aç-kapa ve kararlı görünen bölgelerin incelenmesi. Her pencerenin aynı örneklerinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanır; yardımcı istatistikler ve gerçekleşen örnekleme hızı kaydedilir. PZEM/başka ESP ortalama akımı varsa genel koşul notudur; SCT ile zaman eşleştirmesi yapılmaz. Kararlılık eşiği, pencere sayısı ve kesin kayıt süresi önceden belirlenmez.

[E08 açıklaması](experiments/E08-sct-characterization/README.md) · [Protokol](experiments/E08-sct-characterization/protocol.md). E08 planlandı; fiziksel ölçüm yapılmadı. Aktif sıradaki iş hâlâ T005/E00-E01 yüksüz temel ölçüm hazırlığıdır; E08 bunun ardından uygulanacak.


## Model yaklaşımı — kapsam notu (2026-10-29)

BERO piyasaya sürülecek evrensel bir akım ölçer değildir. Evdeki sınırlı aygıt ve yüklerden zamanla büyüyen birleşik veri kümesi üzerinde öğrenen kişisel model hedeflenir. Eğitim kümesinde çok iyi sonuç veya aşırı öğrenme otomatik başarısızlık sayılmaz; hedef mevcut ev içi veri kümesine uyumu geliştirmektir. Eğitim sonucu, birleşik etiketli veri kümesi sonucu ve varsa eğitimde kullanılmamış kayıt sonucu ayrı raporlanır; bu ayrım ticari genelleme sertifikası için değil, gelişimi izlemek içindir.

Daha önce görülmemiş veya çok yüksek akımlı bir yükün ADC aralığını aşması, doygunluk oluşturması ya da modelin anlamlı tahmin üretememesi kabul edilebilir. Her yükü ölçmek şart değildir; bu durumlar kaydedilir ve ölçülmeyen akım için değer uydurulmaz. Ayrıntı: [proje felsefesi](docs/project-philosophy.md). Bu değişiklik yalnızca dokümantasyondur; model kodu ve fiziksel ölçüm yoktur.

## 2026-10-30 — PF fiziksel yorum ilkesinin yaygınlaştırılması

Düşük PF'nin aynı gerilim ve aktif güç koşulunda RMS akımı artırabileceği, BERO için yalnız E09 notu değil genel fiziksel yorumlama ilkesi olarak kaydedildi. Yüksek akım veya SCT genliği tek başına ölçüm hatası sayılmayacak; PZEM'in V/W/I/PF alanları ve yük türü birlikte değerlendirilecek. Sonuçlar yük/PF bağlamında raporlanacak; ±%4 kararlı alan uyum eşiği değiştirilmeyecek. PF-hata ilişkisi sebep-sonuç olarak varsayılmayacak.

İlke; [proje felsefesine](docs/project-philosophy.md), [PF teknik notuna](docs/architecture/pf-and-current-measurement.md), [SCT-PZEM etiketleme mimarisine](docs/architecture/sct-pzem-labeling-and-calibration.md), [E09](experiments/E09-pf-current-relationship/README.md), [E08 yük karşılaştırma aşamasına](experiments/E08-sct-characterization/stage-03-load-comparison.md) ve [analiz metriklerine](analysis/metrics.md) işlendi. Yalnızca dokümantasyon güncellendi; firmware, fiziksel test, ölçüm veya model değerlendirmesi yapılmadı. Aktif E00A → E00/T005/E01 → E08 sırası değişmedi.


## 2026-10-30 — E00A açılışı ve ilk referans verisi

- **HEDEF:** Bias trafosunun L78L33 çıkışı ve Vmid noktası için ESP32 ADC davranışını kısa, 30 saniyelik gözlemlerle incelemek.
- **LOG:** Kullanıcı L78L33 DC çıkışını multimetreyle 3,31 V ölçtüğünü bildirdi. Kayıt E00A results.md ve experiment.yaml içine KULLANICI BİLDİRİMİ olarak işlendi. Her ADC koşulunun süresi 30 saniye olarak güncellendi. Ayrı/geçici 10k/10k ölçüm bölücüsünün bias devresinin parçası olmadığı açıklandı.
- **SONUÇ:** İlk kaynak referansı var; ADC ölçümü yok. Gerçek ESP32-WROOM-32D kart/pinout, ADC attenuation ve giriş sınırları doğrulanmadan 3,31 V bağlantısı yapılmayacak. Firmware/derleme/ADC ham kayıt henüz yok.
- **Sonraki adım:** Gerçek kartı ve GPIO34 pinout'unu doğrula; ADC aralığına göre ölçüm bağlantısını kesinleştir; ardından iki koşul için 30 saniyelik kayıt al.


2026-10-30 ek kayıt: Kullanıcı bias breadboard orta noktasını multimetreyle 1,65 V okuduğunu bildirdi. Bu değer L78L33 çıkışından ayrı bir DC referans noktasıdır; ADC ölçümü değildir.


## 2026-10-30 — E00A ESP32D2 firmware kaydı

- **Durum:** KOD UYGULANDI; derleme/çalışma kullanıcı bildirimiyle raporlandı. Ölçüm sonucu bekleniyor.
- **Firmware:** [esp32d2-e00a-adc.yaml](experiments/E00A-raw-waveform-observation/firmware/esp32d2-e00a-adc.yaml).
- **Yapılandırma:** ESP-IDF; GPIO34 ADC raw; GPIO35 ADC voltaj; 12 dB attenuation; her sensör için 1 s güncelleme.
- **Kanıt:** Kullanıcı kodun derlendiğini ve çalıştığını bildirdi. Derleme/cihaz logu henüz paylaşılmadı.
- **Açık:** Fiziksel bağlantı düzeni, ADC sayısal değerleri, 30 saniyelik ham CSV, istatistik ve zaman grafiği.
- **Sonraki adım:** Kullanıcının göndereceği log ve sensör değerlerini incele; sonucu results.md'ye ekle.


**2026-10-30 — E00A-S01 GND referans testi:** Kullanıcının paylaştığı logda GPIO34 GND'de 0 count; GPIO35 yaklaşık 175 saniyelik kararlı bölümde 0.142 V gösterdi. Önceki açık giriş dalgalanması floating giriş teşhisini destekliyor. Bu sonuç ADC'nin tüm aralık doğruluğunu kanıtlamaz. Elektriksel çözüm adayı, jack/CT bağlantısı doğrulandıktan sonra ADC düğümünü Vmid'e yüksek değerli (ilk prototip değerlendirmesi 47–100 kΩ) dirençle biaslamak; kesin değer ve bağlantı henüz onaylanmadı. Ayrıntı: [E00A-S01 raporu](experiments/E00A-raw-waveform-observation/reports/E00A-S01-gnd-reference-stability.md). E00A açık; Vmid ve SCT testleri yapılmadı.


**2026-10-30 — E00A düzeltmesi:** GPIO34 count kanalı bağlı değildir; 0 count değeri GND testi kanıtı değildir ve yorum dışıdır. Yeni GPIO35 logu 1.678 V'tan başlayıp yaklaşık 25 saniyede 0.699 V'a düşüyor; kullanıcı Vmid'i multimetrede sabit yaklaşık 1.65 V DC olarak bildiriyor. ADC ile multimetre uyuşmazlığı var; kök neden henüz belirlenmedi. Önce GPIO35 pinindeki gerilim ESP32 GND referansıyla doğrudan ölçülürken eşzamanlı log alınacak. Kablo/ortak GND doğrulanmadan bias direnci veya yazılım filtresi eklenmeyecek. Ayrıntı: E00A results.md ve S01 raporu.


## E00A güncel adım — 2026-10-30

- **Adım 2:** GPIO35 voltaj sensörüne önceki GND logundaki 0.142 V tabanını çıkaran `max(0, x - 0.142)` filtresi eklendi; GPIO34 raw kanalı korundu.
- **Kod durumu:** Kullanıcı güncel firmware'in derlendiğini bildirdi (KULLANICI RAPORU). Kod commit'i `9eae26000a1dc460191bec68581cec0ac9ab9397`.
- **Hedef:** GND girişinde düzeltilmiş voltajı 0.000 V göstermek.
- **Henüz doğrulanmadı:** Güncel firmware ile alınmış GND logu yok. 0.142 V geçici ofset; genel ADC kalibrasyonu değil.
- **Sıradaki tek adım:** GPIO35 GND bağlantısındayken güncel logdan düzeltilmiş değerin 0.000 V olduğunu doğrula; sonra Vmid/multimetre karşılaştırmasına geç.



## E00A — Adım 2 güncel sonuç ve sıradaki kontrol (2026-10-30)

- **Sıfır kontrolü:** Kullanıcı logunda GPIO35 düzeltilmiş voltajı 49/49 kayıtta, yaklaşık 48 saniye boyunca 0.000 V. Kullanıcı Adım 2 hedefinin sağlandığını bildirdi.
- **GPIO34:** 0 count kayıtları fiziksel bağlantı olmadığı için yorum dışı.
- **Kod:** Değiştirilmeyecek.
- **Sıradaki işlem:** Aynı log oturumunda bias trafosuna enerji verilecek; GPIO35'in bias/Vmid altındaki düzeltilmiş voltajı izlenecek. Bias açık logu ve eşzamanlı multimetre değeri henüz bekleniyor.


## 2026-10-30 — E00A Adım 2 karar düzeltmesi
- **HEDEF:** GND sıfır gösterimi ile bias Vmid gerçek DC okuması arasındaki çelişkiyi çözmek.
- **LOG:** Ofsetli logda GND koşulunda 49/49 GPIO35 örneği 0.000 V. Bias açık logunda kararlı bölümün 85 filtreli örnek ortalaması yaklaşık 1.525 V; kullanıcı multimetre Vmid bildirimi 1.654 V. Çıkarılan 0.142 V geri eklendiğinde hesaplanan filtresiz tahmin yaklaşık 1.667 V; fark yaklaşık +0.013 V.
- **SONUÇ:** Sabit 0.142 V sıfırlama gerçek DC seviyeyi bozduğu için kaldırıldı. GND'deki 0.142 V gözlemi gizlenmeyecek. Ofsetsiz firmware depoya yazıldı; yeni derleme/cihaz testi henüz yapılmadı.
- **Sonraki tek adım:** Kullanıcı ofsetsiz YAML'ı derleyip cihaza yükleyecek; aynı Vmid koşulunda yeni log alınacak. E00A tamamlanmadı.


## 2026-10-30 — E00A RAW/voltaj karşılaştırma firmware'i

- **HEDEF:** GPIO34 RAW count değerinden nominal voltaj tahmini üretmek; GPIO35 ESPHome ADC voltajıyla karşılaştırmak ve aradaki işaretli farkı yayınlamak.
- **LOG:** Firmware'e GPIO34 RAW sensörü, `RAW × 3.1 / 4095` nominal voltaj tahmini, GPIO35 ofsetsiz ADC voltajı ve `GPIO35 - GPIO34 tahmini` fark sensörü eklendi. Kullanıcı yeni YAML'ın derlemeye alındığını bildirdi; derleme sonucu henüz bildirilmedi.
- **SONUÇ:** Değişiklik GitHub'a kaydedildi ve dosya yeniden okunarak doğrulandı. Derleme başarılı veya cihazda çalışıyor olarak henüz işaretlenemez. RAW dönüşüm katsayısı nominal tahmindir; kalibrasyon değildir.
- **Bağlantı koşulu:** Karşılaştırma için GPIO34 ve GPIO35 aynı 1.654 V Vmid noktasına bağlanmalı. GPIO34 bağlantısız kalırsa RAW voltajı ve fark sensörü geçerli karşılaştırma değildir.
- **Sonraki adım:** Derleme sonucunu al; başarılıysa cihaz yüklemesi ve aynı Vmid noktasında multimetre eşzamanlı logu.


## 2026-10-30 — E00A bias-only / SCT bağlı değil: RAW ve voltaj ilk karşılaştırma logu

### HEDEF
SCT bağlamadan bias Vmid noktasını ESP32D2'nin GPIO34 RAW ve GPIO35 ADC voltaj kanallarında gözlemek; multimetre bildirimi olan 1.654 V ile karşılaştırmak. Sonraki uzun logda RAW ve voltaj serilerinin korelasyonunu incelemek için başlangıç gözlemi oluşturmak.

### LOG
- Kaynak: Kullanıcının paylaştığı `Yapıştırılan metin(20261030-123911).txt`; ESPHome 2026.9.1; ESP32 rev3.1; cihaz `esp32d2`; log bağlantısı 192.168.0.66.
- ADC GPIO34 (ADC1_CH6) ve GPIO35 (ADC1_CH7) başlatma, konfigürasyon ve kalibrasyon durumları OK; iki sensörün güncelleme aralığı 1 s.
- Kullanıcının multimetre bildirimi: Vmid = **1.654 V**. Bu değer kullanıcı raporudur; bu logda multimetre ölçümünün zaman damgası yoktur.
- İlk bölümde GPIO34 RAW = 0 count ve GPIO35 = 0.142 V görülüyor. Ardından GPIO34 yaklaşık 1837–1871 count bölgesine geçiyor; GPIO35 de yaklaşık 1.65–1.68 V bandına oturuyor.
- Kararlı görünen bölümde (yaklaşık 15:37:46–15:39:03): GPIO34 RAW gözlemi yaklaşık 1829–1871 count; RAW nominal voltaj tahmini yaklaşık 1.385–1.416 V; GPIO35 ADC voltajı yaklaşık 1.650–1.679 V; fark sensörü yaklaşık +0.250…+0.294 V.
- RAW nominal tahmini firmware formülüdür: `count × 3.1 / 4095`; kalibre edilmiş voltaj değildir.
- Logda iki kanalın yayınları aynı saniyede ve aynı anda gerçekleşmiyor; GPIO34 ve GPIO35 ayrı ADC kanallarıdır. Bu nedenle bu kısa kayıt tek başına örnek-örnek korelasyon katsayısı veya tam eşzamanlılık kanıtı değildir.
- Logda trafo enerjilendirme anı ayrıca işaretlenmediğinden, ilk geçişi belirli bir trafo ON/OFF zamanına atamıyoruz. Kullanıcının gözlemi: kondansatörlerle birlikte değerler belirgin biçimde oturuyor.

### SONUÇ
- Bias-only gözleminde GPIO35 voltaj okuması kararlı bölümde kullanıcının bildirdiği 1.654 V multimetre değerine yakındır (yaklaşık 1.650–1.679 V).
- Aynı kararlı bölümde GPIO34 RAW'dan nominal hesaplanan voltaj yaklaşık 1.4 V'tur ve GPIO35'ten yaklaşık 0.27 V düşüktür. Bu fark henüz nedenlendirilmemiştir; RAW dönüşüm katsayısı nominaldir ve iki kanal ayrı ADC okumalarıdır.
- Bu test SCT davranışını, akım ölçümünü veya bias devresinin SCT yükü altındaki davranışını göstermez. Yalnızca SCT'siz bias/ADC zincirinin ilk karşılaştırmasıdır.
- Kullanıcının sonraki adımı: daha uzun RAW + voltaj logu paylaşmak. O kayıtta zaman serilerini eşleştirip korelasyon (Pearson ve/veya Spearman), eğim/kesişim, fark ve kararlı/geçiş bölümlerini inceleyeceğiz. Ham logdaki örnekleme zamanları korunmalı; farklı zaman damgaları körlemesine satır satır eşleştirilmeyecek.
- E00A tamamlanmadı; bu kayıt ön gözlemdir.


## 2026-10-30 — Güncel SCT'siz deney kapanışı

SCT bağlı değilken bias Vmid koşulunda son log analiz edildi ve bu alt deney kapatıldı. 603 geçerli zaman eşleşmesi; GPIO35 1.665138 V ortalama / 6.474 mV std; GPIO34 RAW 1846.80 count ortalama / 6.97 count std. Pearson r=-0.0201. RAW sıfır başlangıç kayıtları eşleştirmeye alınmadı. Bu sonuç ADC'ye özgü gürültü değil, SCT'siz bias+bağlantı+ADC ölçüm zincirinin gözlenen dalgalanmasıdır. E00A'nın 3.3 V ayrı bölücü koşulu ve ham CSV/zaman grafiği tamamlanmadığı için E00A bütünü açık kalır. Sıradaki teknik koşul: SCT bağlı, ölçülen hatta akım yok; önceki tabanla karşılaştırma.


## 2026-10-30 — E00B açıldı: SCT bağlı, akımsız hat ADC gözlemi

- Bias referans kanalları korunuyor: GPIO34 RAW (ADC1_CH6), GPIO35 voltaj (ADC1_CH7).
- SCT kanalları önerisi: GPIO32 RAW (ADC1_CH4), GPIO33 voltaj (ADC1_CH5).
- Kart adayı ESP32-WROOM-32D; gerçek geliştirme kartı pinout'u doğrulanmadan bağlantı yapılmayacak.
- Öncelikli sensör SCT013-030 (30 A / 1 V). Harici ADC kullanılmıyor.
- Deney PLANLANDI; firmware, fiziksel bağlantı, derleme ve ölçüm henüz yapılmadı.
- Ayrıntı: [E00B README](experiments/E00B-sct-connected-no-current/README.md), [experiment.yaml](experiments/E00B-sct-connected-no-current/experiment.yaml), [results.md](experiments/E00B-sct-connected-no-current/results.md).


## 2026-10-30 — E00B firmware derlemesi bildirildi
- **Durum:** HAZIRLANDI / DERLENDİ (KULLANICI RAPORU). E00B firmware'i depoya eklendi: [esp32d2-e00b-sct-no-current.yaml](experiments/E00B-sct-connected-no-current/firmware/esp32d2-e00b-sct-no-current.yaml).
- **HEDEF:** SCT bağlı/primer akımsız gözlem için dört ADC kanalını (GPIO34/35 bias, GPIO32/33 SCT) tek firmware'de toplamak.
- **LOG:** Kullanıcı 2026-10-30 tarihinde kodun derlendiğini bildirdi. Firmware commit: `20fbe9b4a99d057ef579d882bfd83d23f4ef199e`. ESPHome yayın aralığı 1 s; yüksek hızlı ham örnekleme değildir.
- **SONUÇ:** Derleme başarılı kullanıcı raporudur. Cihaza yükleme, gerçek pinout/fiziksel bağlantı ve deney ölçümü henüz doğrulanmadı. E00B TAMAMLANDI değildir.
- **Sonraki adım:** Gerçek kart pinout'unu doğrula; ardından güvenli fiziksel bağlantı ve cihaz logu.


## 2026-10-30 — E00B ilk cihaz logu kaydedildi
- **Durum:** CİHAZ LOGU ALINDI; fiziksel koşulların tam doğrulaması bekliyor.
- **HEDEF:** Dört ADC kanalının cihaz üzerinde çalıştığını ve SCT bağlı/akımsız koşulun ilk gözlemlerini kaydetmek.
- **LOG:** ESPHome 2026.9.1 / ESP32 rev3.1; GPIO34/35/32/33 ADC1 başlatma ve kalibrasyon OK. Kararlı bölüm 16:20:41 sonrası, 110 örnek/kanal. Bias RAW ortalaması 1854.14 count; SCT RAW 1853.45 count. Bias voltaj 1.6651 V; SCT voltaj 1.6639 V. İlk açılış geçişindeki 0 count ve 0.142 V değerleri analiz dışı bırakıldı.
- **YORUM:** Bias ve SCT kanalları bu log kesitinde birbirine yakın. Nominal RAW voltaj tahmini ile kalibre ADC voltajı arasındaki yaklaşık 0.25 V fark fiziksel devre düşümü olarak yorumlanamaz.
- **SONUÇ:** Cihaz bağlantısı ve dört ADC kanalının başlatılması doğrulandı. Primer akımın sıfır olduğu ve fiziksel SCT bağlantısı yalnız logdan bağımsız doğrulanamıyor.
- **Sonraki adım:** Fiziksel kurulum/akımsız koşulu not et ve daha uzun kararlı kayıt al.
- **Kayıt:** [E00B results](experiments/E00B-sct-connected-no-current/results.md), [ham log](experiments/E00B-sct-connected-no-current/logs/2026-10-30-e00b-esp32d2-startup-and-observation.log).


## 2026-10-30 — ESP32D2 / SCT013-030 hazır ct_clamp yapılandırması kaydedildi

- **Durum:** UYGULANDI (GitHub depo kaydı). Kullanıcının paylaştığı ve cihaz loglarında çalıştığı görülen ESPHome yapılandırması `firmware/esp32d2.yaml` dosyasına kaydedildi. Bu oturumda yeniden derleme veya cihaza yükleme yapılmadı.
- **HEDEF:** Hazır ESPHome `ct_clamp` paketiyle çalışan temel ölçüm yapılandırmasını, tek seferlik 24.22 katsayısını ve mevcut bağlantı/örnekleme ayarlarını kaybetmeden korumak.
- **LOG:** ESP32D2 kimliği korunmuştur. SCT013-030 → mevcut yaklaşık 1.65 V bias → GPIO33; ADC1 / 12 dB; `sample_duration: 200ms`; `update_interval: 2s`; katsayı 24.22; yayın eşiği 0.35 A. 150 W akkor testinde pens 0.616 A / ESP32 yaklaşık 0.615 A; kettle düşük akım kesitinde yaklaşık 0.637 A / 0.656 A; kettle kaynama kesitinde pens 6.39 A / ESP32 yaklaşık 6.15 A. 8.35 W LED'de pens 0.041 A iken 0.35 A eşiği nedeniyle yayınların çoğu 0.000 A; ara sıra 0.508 A ve 0.372 A sıçramaları görüldü. Bu ölçüm ve pens değerleri kullanıcı raporu/loglarıdır.
- **SONUÇ:** 150 W ve kettle koşullarında gözlenen farklar yaklaşık ±%4 hedefinin içinde. 41 mA LED akımı mevcut eşik tarafından bastırıldığı için düşük akım kabiliyeti henüz gösterilmedi. Katsayı değiştirilmedi. Kod açıklamasındaki ilk 0.30 A ifadesi, lambda'nın fiilen uyguladığı 0.35 A ile tutarlı olacak şekilde depo kopyasında düzeltildi; çalışan lambda mantığı değiştirilmedi.
- **Kayıt:** [firmware/esp32d2.yaml](firmware/esp32d2.yaml), [firmware/README.md](firmware/README.md).
- **Açık kalan:** Ham test loglarının kalıcı dosya olarak eklenmesi ve 0.35 A eşik davranışının düşük akım için değerlendirilmesi. Bu kayıt E00A/E00B/E08 planlarının kabul ölçütlerini tamamlamaz veya fiziksel doğrulama iddiası oluşturmaz.


## 2026-10-30 — Kettle ölçüm karşılaştırmaları rapora eklendi

- **Durum:** UYGULANDI — rapor ve durum kaydı GitHub'a yazıldı.
- **HEDEF:** Bu sohbet içinde paylaşılan kettle pens/ESP32 karşılaştırmalarını koşullarına göre ayrı kaydetmek; belirsiz 0.437 A bildirimini doğrulanmış kettle sonucu gibi göstermemek.
- **LOG:** Kettle düşük/kararlı kesiti: pens 0.637 A, ilk 20 ESP32 yayınının ortalaması yaklaşık 0.656 A (+%3.0). Kettle kaynama kesiti: pens 6.39 A, 22 ESP32 yayınının ortalaması yaklaşık 6.15 A (−%3.8). Daha sonraki ayrı logda pens 0.437 A bildirilmiş; 74 ESP32 yayınının ortalaması 0.664 A, son 0.910 A sıçraması çıkarıldığında 0.660 A. Bu son kaydın yük/koşul eşleşmesi teyit edilmediğinden kettle olarak sınıflandırılmadı.
- **SONUÇ:** İlk iki kettle kesiti kullanıcı tarafından belirlenen ±%4 sınırının içinde; kaynama kesiti sınıra yakındır. 0.437 A bildirimi ile log arasında yaklaşık +%52 fark vardır, ancak eşzamanlı ve aynı yük koşulu doğrulanmadan teknik sonuç çıkarılamaz. Katsayı 24.22 ve lambda eşiği 0.35 A değiştirilmedi.
- **Açık kalan:** 0.437 A pens okumasının hangi yük/koşula ait olduğu ve logla eşzamanlı olup olmadığı.
- **Kanıt:** [Firmware ve ölçüm raporu](firmware/README.md); [YAML](firmware/esp32d2.yaml).


## 2026-10-30 — E00F düşük akım / ct_clamp toplu teknik değerlendirmesi

- **Durum:** Kaynak kod incelemesi ve kademeli teşhis planı depoya kaydedildi; fiziksel test yapılmadı.
- **Kayıt:** [Toplu teknik değerlendirme](docs/technical-reviews/2026-10-30-e00f-low-current-cumulative-review.md) Gemini, Google, Claude ve GitHub Copilot raporlarını kaynak kod, kullanıcı logu ve hipotez sınıflarına ayırır.
- **Kesin kararlar:** E00F çalışan YAML, esp32d2 kimliği, GPIO33, raw: false, 200 ms, 24.22 ve 0.35 A korunur. Google'ın raw: true önerisi mevcut akım yapılandırmasına uygulanmaz; birim/ölçek değişir.
- **Teknik olarak doğrulanan:** ct_clamp ardışık eşit sayısal değerleri atlar; N ve raporlanan SPS bu nedenle gerçek ADC dönüşüm sayısı/hızı değildir. Raw AC Value, kaynak ADC sensörü Volt olduğunda RMS gerilimidir.
- **Açık kalan:** 0.006 V değerinin 0.041 A LED ölçümüyle aynı pencereye ait olduğu kanıtlanmadı. Deduplication, 1 mV kalibre çıkış basamağı, ADC gürültüsü ve float birikim etkilerinin BERO'daki büyüklüğü ölçülmedi.
- **Sıradaki teşhis dizisi:** D0 mevcut log eşleştirmesi → D1 SCT bağlı yüksüz pencere kayıtları → D2 aynı kurulumda 8.35 W LED → D3 akkor kontrol. D4 ayrı RAW teşhisi yalnız gerekirse; E08 ham edinim ayrı plan olarak kalır.
- **Durum ayrımı:** Bu belge ve plan kaydı firmware kodlandığı, derlendiği, cihaza yüklendiği veya deneylerin yapıldığı anlamına gelmez. Mevcut STATUS içindeki E00B aktif iş sırası bu kayıtla değiştirilmedi.


## 2026-10-30 — Claude incelemesi sonrası E00F test kabul ölçütleri sıkılaştırıldı

- **Durum:** Yalnız test protokolü ve kabul ölçütleri güncellendi; firmware ve fiziksel kurulum değişmedi.
- **D0:** Her pencere için Raw AC, N (farklı kabul edilen değer sayısı) ve raporlanan SPS birlikte çıkarılacak. N/SPS için min, max, ortalama, medyan, SD, p5/p95 ve dağılım; pencere bazında üçlü kayıt istenecek. N tek başına float32 etkisini kanıtlamaz; gerçek ADC örnek dizisi yoksa simülasyon varsayımlı duyarlılık analizi olarak etiketlenecek.
- **D1/D2:** Her koşulda en az 30 geçerli 200 ms pencere; anahtarlama/koşul değişiminden sonraki ilk pencere dışlanacak, bu nedenle en az 31 pencere yakalanacak. Raw AC, N ve SPS pencere bazında saklanacak.
- **Taban ve SD:** 0 V ve 0.006 V olasılıkları yüksüz taban yorumları olarak sınanacak. 0.0017 V, 24.22 katsayısıyla 0.041 A'ya karşılık gelen LED ölçek referansıdır; yüksüz taban eşiği değildir. D1'in ölçülen SD'si ampirik referans olacak; D2/D3 ayrışması D1 medyanı + 3×SD ve gerektiğinde medyan + 3×MAD ile değerlendirilecek. Bu, ±%4 akım kabul hedefinden farklıdır.
- **D3:** Mümkünse yaklaşık 0.447 A ve 0.616 A akkor koşulları D1 tabanıyla karşılaştırılacak. Gerçek yük/akım beyan edilecek; ham Raw AC ve yalnız tanısal olarak kareler farkı tahmini ayrı gösterilecek. Pens/ESP32 sapması yalnız eşleşmiş kararlı kayıtla hesaplanacak.
- **D4:** Koşul netleştirildi: D0–D3 sonrasında N değişkenliği Raw AC sıçramalarıyla ilişkiliyse, taban modeli sonucu açıklamıyorsa veya kalibre mV basamağı şüphesi hâlâ ham count gerektiriyorsa açılabilir. RAW:true deduplication'ı tek başına kaldırmaz.
- **D5:** E00F One-shot ve E08 Continuous aynı ADC1 biriminde eşzamanlı çalıştırılmayacak. Modlar arası karşılaştırma aynı yük ve aynı kararlı kurulumda sıralı kayıtla yapılacak.
- **Aktif görev:** Bu protokol güncellemesi E00B aktif iş sırasını değiştirmez; E00F teşhis planı ayrı tutulur.


**E00F sıfır-yük logu ve düşük akım araştırması (2026-10-30):** Kullanıcının paylaştığı 180 pencerelik E00F logunda 173 yayın 0.000 A, 7 yayın (%3.89) 0.353–0.770 A yanlış pozitif akım olarak görüldü (koşul kullanıcı tarafından yüksüz bildirildi). Kaynak Raw AC medyanı 5 mV, ortalaması 5.62 mV, pencere SD'si yaklaşık 5 mV. E00F 0.35 A yazılım eşiği 40 mA'yı tasarım gereği sıfırlar; bu eşik CT'nin minimum akımı değildir. SCT013-030 nominal 40 mA çıkışı yaklaşık 1.33 mV RMS; mevcut 24.22 A/V katsayısı 1.65 mV karşılığı verir. Mevcut yüksüz dağılımda güvenilir ayrışma gösterilmedi. GitHub araştırması düşük akımda en küçük uygun CT, yüksüz taban kalibrasyonu ve gerektiğinde ayrı düşük/yüksek aralık CT yaklaşımını gösterdi; BERO donanımı/YAML/deney sırası değiştirilmedi. Ayrıntı ve ham log: [E00F teknik değerlendirme, bölümler 13–14](docs/technical-reviews/2026-10-30-e00f-low-current-cumulative-review.md).


## 2026-10-31 — Test yükleri için karşılaştırmalı kayıt bölümü açıldı

- **YENİ BÖLÜM:** [Test yükleri ve karşılaştırmalı ölçüm kayıtları](test-loads/README.md). Her fiziksel yük için ayrı ana kayıt dosyası; her test oturumu için kod, log, tarih/saat aralığı, referans, sonuç, sapma ve kanıt durumu tutulacak.
- **İLK YÜK KAYDI:** [100 W akkor ampul karşılaştırma tablosu](test-loads/100w-incandescent/README.md).
- **TEST 001:** ESP32D2, Modül 2 kutusu olmadan yapılan tarihsel baseline. Referans 0,446–0,447 A; kod sonucu 0,4471 A; yaklaşık %0 sapma. Kod dosyası mevcut. Ayrı ham log ve kesin log zaman aralığı mevcut depo özetinde bulunmadığı için açıkça eksik kanıt olarak işaretlendi.
- **TEST 002:** Modül 2 / ESP32D1 / SCT-1 GPIO32, 2026-10-31. PENS 0,427 A kullanıcı bildirimi; son beş kararlı kod yayını ortalama 0,589 A; yaklaşık +%37,9. Karşılaştırma ±%4 dışında. Log dosyası analiz özeti içerir; özgün 563 satırın tamamı değildir. Logdaki nominal 30 A/V firmware ile depodaki güncel YAML'ın tam commit eşleşmesi doğrulanmadı.
- **KURAL:** Eski test satırları silinmez veya geriye dönük doldurulmuş gibi gösterilmez. Her yeni Modül 2 ölçümü aynı 100 W dosyasına yeni satır olarak eklenecek; kod ve log bağlantıları test anındaki sürümü gösterecek.


## 2026-10-31 — FAN-1 uzun logu arşivlendi

- Tam ham log `logs/module2/2026-10-31-fan1-module2-sct1-extended-full.txt` dosyasına kaydedildi. Özgün dosya SHA-256: `ccc520db070555741d45f3fa67b5866011bec0dadc092c839eb52ff5502eba8e`.
- 97 akım yayını; 17:13:53.070–17:17:05.067 (+03:00); ortalama 0,14114 A; medyan 0,147 A; aralık 0,000–0,259 A.
- FAN-1 UNIT son kullanıcı bildirimi 0,096 A; ilk bildirim 0,097 A. ±%4 bandı 0,09216–0,09984 A. Fanın gerçek açılma/kararlı zaman işareti bulunmadığından geçiş ile kararlı bölüm kesin ayrıştırılamadı.
- Kullanıcı ilk açılışta çok kısa yüksüz bölüm olduğunu belirtti. Başlangıç verileri kararlı FAN-1 verisiyle birleştirilmedi.
- UNIT PF göstermiyor; PZEM daha sonra eklenecek. UNIT değeri mutlak doğru kabul edilmedi.
- [Fan test kaydı](test-loads/fan/README.md); [analiz](logs/module2/2026-10-31-fan1-module2-sct1-analysis.md); [tam ham log](logs/module2/2026-10-31-fan1-module2-sct1-extended-full.txt).
- K=24.22 korundu; yazılımsal sıfır eşiği eklenmedi.


## 2026-10-31 — FAN-2 uzun logu arşivlendi ve gözlem oturumu kapatıldı

- **KAPANIŞ SINIFI:** FAN-2, Modül 2 düşük akım gözlem oturumu olarak kapatıldı; ±%4 akım doğrulama testi olarak kapatılmadı.
- **UNIT:** Kullanıcı bildirimi 0,106 A; 0,30 A altı BERO düşük akım bölgesidir, ±%4 kabul/ret uygulanmaz.
- **UZUN HAM LOG:** `logs/module2/2026-10-31-fan2-module2-sct1-long-full.txt`; kaynak `esp32d1-logs (42).txt`; 90.706 bayt; kaynak SHA-256 `e550d447b75b50e2b99581a70de23b8916caba576a8665240f44574e586a3dca`.
- **ZAMAN/ÖRNEK:** 17:26:19.113–17:31:41.120 (+03:00); 162 SCT akım yayını. Önceki kısa dosya (41) ilk 54 yayını içerir ve uzun dosyanın tam başlangıç önekidir; uzun dosya 108 yeni yayın ekler.
- **AKIM:** Ortalama 0,168969 A; medyan 0,1685 A; min–maks 0,108–0,257 A; örnek SD 0,024640 A. Tüm 162 yayın 0,30 A altındadır.
- **ANALOG:** Raw AC ortalama 0,00697685 V; bias GPIO35 ortalama 1,663426 V; SCT-1 ADC GPIO32 ortalama 1,660537 V.
- **KOD:** [FAN-2 kapanış YAML snapshot](firmware/archive/FAN-2-2026-10-31-esp32d1-sct1.yaml). ESPHome 2026.10.1; GPIO32/35; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s; K=24.22; yazılımsal sıfır eşiği yok. Binary eşleşmesi iddia edilmez.
- **PF:** Logda PZEM akım/PF yok; UNIT PF göstermiyor. PF etkisi hipotez olarak kalır.
- **RAPOR:** [FAN-2 teknik analiz](logs/module2/2026-10-31-fan2-module2-sct1-long-analysis.md); [tam ham log](logs/module2/2026-10-31-fan2-module2-sct1-long-full.txt); [fan test kaydı](test-loads/fan/README.md).
- **AÇIK İŞ:** PZEM akım + PF ile eşleşmiş kararlı pencere; 0,30 A altı ayrı 1T/2T/4T deney matrisi henüz uygulanmadı.


## 2026-10-31 — FAN-3 uzun SCT-1 logu arşivlendi ve gözlem oturumu kapatıldı

- **KAPANIŞ SINIFI:** FAN-3, Modül 2 düşük akım gözlem oturumu olarak kapatıldı; ±%4 akım doğrulama veya PF doğrulaması değildir.
- **UNIT:** Kullanıcı bildirimi 0,141 A; 0,30 A altı BERO düşük akım bölgesinde ±%4 kabul/ret uygulanmaz.
- **HAM LOG:** `logs/module2/2026-10-31-fan3-module2-sct1-long-full.txt`; kaynak `esp32d1-logs (43).txt`; 139.575 bayt / 1.877 satır; SHA-256 `a4345c7af2b5dcc608b264e1dceed50dbe8ee5e40c5137d1eeff2583f9a53a9f`.
- **ZAMAN/ÖRNEK:** 17:35:27.127–17:43:55.115 (+03:00); 255 akım yayını.
- **AKIM:** Ortalama 0,224612 A; medyan 0,223 A; min–maks 0,189–0,311 A; örnek SD 0,018657 A. 253/255 yayın 0,30 A altındadır; iki tekil yayın 0,305 A ve 0,311 A'dır.
- **ANALOG:** Raw AC ortalama 0,009273 V; bias GPIO35 ortalama 1,663387 V; SCT-1 ADC GPIO32 ortalama 1,661008 V.
- **KOD:** `firmware/archive/FAN-3-2026-10-31-esp32d1-sct1.yaml` kapanış snapshot'ı olarak kaydedildi. ESPHome 2026.10.1; GPIO32/35; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s; K=24.22; yazılımsal sıfır eşiği yok. Binary eşleşmesi iddia edilmez.
- **PF:** Logda PZEM akım/PF yok; UNIT PF göstermiyor. PF etkisi doğrulanamadı.
- **GEÇİŞ:** Açılma/kapanma olay işareti bulunmadığından gerçek anahtarlama anı ve tepki farkı hesaplanamadı.
- **ANALİZ:** `logs/module2/2026-10-31-fan3-module2-sct1-long-analysis.md`.
- **SONRAKİ:** PZEM akım + PF ile eşleşmiş kararlı pencere ve olay işaretli açılma/kapanma geçiş deneyi.


## 2026-10-31 — MIXED-LOAD-001 açıldı: 100 W akkor + FAN-3

- **DURUM:** Karma yük testi planı açıldı; fiziksel bağlantı ve ölçüm henüz yapılmadı.
- **AMAÇ:** 100 W akkor dirençli yük ile FAN-3 motor yükü birlikte çalışırken SCT-1'in toplam hat akımını gözlemlemesi; PZEM toplam akım ve PF verileriyle eşleşmiş kararlı pencereleri incelemek.
- **AŞAMALAR:** 100 W tek başına; FAN-3 tek başına; birlikte çalışma; 100 W açıkken FAN-3 açılma ve kapanma geçişleri.
- **ÖNCEKİ REFERANSLAR:** 100 W UNIT geçici bildirimi 0,427 A; FAN-3 UNIT bildirimi 0,141 A. Bunlar ayrı testlerden gelir, karma yük referansı değildir. Birlikte çalışma için yeni UNIT ve mümkünse eşzamanlı PZEM akım/PF ölçümü alınacak.
- **DEĞERLENDİRME:** 0,30 A ve üzeri kararlı pencerelerde eşleşmiş referans varsa ±%4; 0,30 A altında ±%4 kabul/ret yok. SCT toplam akımı gözlemler; PF veya motorun bileşen akımını tek başına ayırmaz.
- **DOSYA:** [MIXED-LOAD-001 — 100 W akkor + FAN-3](test-loads/mixed-load-100w-plus-fan3/README.md); [test yükleri ana listesi](test-loads/README.md).
- **SONRAKİ:** Fiziksel düzenek kurulunca UNIT ölçümünü al; ardından SCT ve PZEM loglarını aynı kararlı pencerelerde kaydet. Geçişlerde FAN-3 açma/kapatma anını ayrıca işaretle.


## 2026-10-31 — MIXED-LOAD-001 UNIT açılış referansı kaydedildi

- **YÜK:** 100 W akkor + FAN-3 birlikte.
- **UNIT BİLDİRİMLERİ:** FAN-3 tek başına 0,142 A; 100 W akkor tek başına yaklaşık 0,430 A; iki yük birlikte **0,573 A**.
- **KAYIT NİTELİĞİ:** 0,573 A, kullanıcının birlikte çalışma için bildirdiği UNIT-reported açılış referansıdır. Ayrı akımların aritmetik toplamı olarak türetilmemiştir. PZEM teyidi ve eşzamanlı SCT logu henüz yoktur.
- **DURUM:** UNIT başlangıç referansı kaydedildi; PZEM/PF ve SCT ölçümleri bekleniyor. ±%4 sonucu veya PF doğrulaması verilmedi.
- **DOSYA:** [MIXED-LOAD-001 test kaydı](test-loads/mixed-load-100w-plus-fan3/README.md).


## 2026-10-31 — MIXED-LOAD-001 karma yük kararlı oturumu kapatıldı

- **KAPSAM:** 100 W akkor + FAN-3 birlikte açık kararlı ölçüm oturumu kapatıldı. Test planındaki ayrı yük tekrarları ve FAN-3 açma/kapama geçişleri bu logda yer almadığından tamamlanmış sayılmaz; PZEM eşleştirmesi ve olay işaretli geçiş gözlemi sonraki çalışma olarak açık kalır.
- **REFERANS:** UNIT-reported 0,573 A (kullanıcı bildirimi; PZEM değildir). ±%4 bandı 0,55008–0,59592 A.
- **LOG:** `esp32d1-logs (44).txt`; 77.072 bayt; kaynak SHA-256 `f6f3434e540402e7d9a7d63fb38aed0f7dc660b96cb3ef14e00ad6affc07e910`; ilk/son SCT akım yayını 17:55:57.139–18:00:27.106 (+03:00); 136 yayın.
- **SCT:** Ortalama 0,582456 A; medyan 0,582 A; min–maks 0,564–0,609 A; örnek SD 0,007335 A. Ortalama sapma +%1,650; medyan sapması +%1,571. 130/136 (%95,59) yayın UNIT ±%4 bandında; 6 yayın üst sınırın üzerinde, alt sınır altında yayın yok.
- **ANALOG:** Raw AC ortalama 0,024048 V; bias GPIO35 ortalama 1,663754 V; SCT-1 ADC GPIO32 ortalama 1,663051 V.
- **KOD/DÜZENEK:** ESP32D1 / Modül 2 / SCT-1 sarı GPIO32 ADC1_CH4 / ortak bias turuncu GPIO35 ADC1_CH7; ESPHome 2026.10.1; ADC 12 dB/1 s; ct_clamp 200 ms/2 s; K=24.22. K değiştirilmedi, yazılımsal sıfır eşiği eklenmedi.
- **KARAR:** Bu kararlı karma-yük oturumu UNIT referansına göre ±%4 kriterini sağladı. Bu, PZEM doğrulaması veya genel kalibrasyon garantisi değildir. Logda PZEM akım/PF/aktif güç ve fan olay işaretleri bulunmaz; geçiş süresi/tepki farkı çıkarılamaz.
- **KOD SNAPSHOT:** [MIXED-LOAD-001 kapanış YAML](../../firmware/archive/MIXED-LOAD-001-2026-10-31-esp32d1-sct1.yaml). Snapshot aktif firmware ile aynı YAML içeriğidir; binary eşleşmesi iddia edilmez.
- **ARŞİV:** [Tam ham log](../../logs/module2/2026-10-31-mixed-load-001-module2-sct1-full.txt); [analiz raporu](../../logs/module2/2026-10-31-mixed-load-001-module2-sct1-analysis.md).


## 2026-10-31 — FAN-3-3T-001 kapatıldı; FAN-1-RETEST-001 açıldı

- **FAN-3-3T-001:** 3T düşük akım gözlem oturumu, `esp32d1-logs (47).txt` ile kapatıldı. Kaynak SHA-256: `fb48997412ced2a9f769b3084bec9f63dab8ef7174efea23062ce4e63dbc735c`; 236 akım yayını; 18:30:59.057–18:38:49.014.
- Sıçrama hariç akım ortalaması 0,413894 A; medyan 0,413 A; gösterge/3 ortalaması 0,137965 A; Raw AC ortalaması 0,017089 V. Tekil 0,932 A sıçrama ham veri içinde korundu.
- Önceki 1T FAN-3 ile artış yaklaşık 1,843x; 3x doğrusal ilişki kanıtlanmadı. UNIT 0,142 A kullanıcı bildirimi; /3 kıyası betimleyici ve ±%4 kabul/ret değildir.
- K=24.22 değişmedi; yazılımsal sıfır eşiği eklenmedi. Kapanış YAML snapshot ve analiz raporu eklendi.
- **FAN-1-RETEST-001:** Yeni FAN-1 gözlem oturumu AÇIK. Eski FAN-1 kayıtları değiştirilmedi. UNIT 0,093 A; 0,30 A altında ±%4 yok. Fan kapalı taban/açılış/kararlı/kapanış işaretli protokol açıldı.
- Ayrıntılar: [FAN-3-3T-001](test-loads/fan3-3turn/README.md), [FAN-1-RETEST-001](test-loads/fan1-retest/README.md).
