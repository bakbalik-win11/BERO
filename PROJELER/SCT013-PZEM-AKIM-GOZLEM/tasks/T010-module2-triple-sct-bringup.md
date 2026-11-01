## 2026-11-01 — T010 kapatıldı / SCT2-SCT3 soket değişimi gözlem planı

- T010 mevcut kapsamıyla **KAPATILDI**. E11 kodu 100 W akkor ampul yükünde üç SCT kanalından aynı deney oturumunda sıralı veri üretti.
- Yeni yük testleri T010 kapsamında yapılmayacak. İleride farklı yüklerde doğrulama, PZEM ile birlikte ayrı eşleştirme aşamasında yapılacak.
- T010 kapanışı PZEM entegrasyonunun tamamlandığı anlamına gelmez.
- Sonraki kısa gözlem: kullanıcı fiziksel SCT fişlerini 2 ve 3 numaralı soketler arasında değiştirecek. Aynı 100 W ampulle yalnız kanal/sensör davranışı gözlenecek; bu UNIT/PZEM doğruluk veya ±%4 kabul testi değildir. Firmware, K=24.22, GPIO eşlemesi ve okuma sırası değiştirilmeyecek. Değişim yük enerjisizken yapılacak.
- Gözlem amacı: önceki logda SCT2'de görülen yaklaşık %5 düşük kabul edilmiş örnek sayısının fiziksel sensörle mi yoksa GPIO/kanal yoluyla mı birlikte hareket ettiğini ayırt etmeye yardımcı olmak.
- Deney henüz yapılmadı; sonuç bekleniyor.

## 2026-11-01 — E11 Log 66 / 100 W UNIT karşılaştırması (kullanıcı yük teyidi)

- E11 deneyi 100 W akkor ampul yüküyle başlatıldı; Log 66 aynı oturumun uzun kaydıdır. Üç SCT sensörü aynı oturumda kullanıldı; kanallar eşzamanlı değil, sıralı okundu.
- 396 kararlı çevrim ortalaması: SCT1 0,423884 A, SCT2 0,424328 A, SCT3 0,425828 A. Tarihsel UNIT 0,427 A referansına sapmalar sırasıyla −%0,730 / −%0,626 / −%0,274; üç kanal ortalaması da ±%4 bandında.
- **SONUÇ:** Yeni E11 sıralı kodu, 100 W oturumunda tarihsel UNIT referansına göre üç kanal ortalaması bakımından başarılı. Eşzamanlı UNIT ölçümü olmadığı için eşzamanlı doğrulama değildir. Ayrıntı: [100 W yük kaydı](../test-loads/100w-incandescent/README.md), [Log 66 analizi](../logs/module2/2026-11-01-e11-three-sct-sequential-extended-analysis.md).
- **AÇIK:** SCT2 örnek sayısı yaklaşık %5 düşük; 42/396 çevrimde geçiş zamanlama işareti sapması var; gerçek ADC pencere bitiş callback'iyle doğrulanmadı. 50 ms pay korunacak. K=24.22 değişmedi. T010 AKTİF.

## 2026-11-01 — E11 üç SCT logu

E11 sıralı üç kanal logu analiz edildi. Ayrıntılı kanal istatistikleri, eski kayıt kıyası, zamanlama anomalisi ve kanıt sınırları [analiz raporunda](../logs/module2/2026-11-01-e11-three-sct-sequential-analysis.md); ham log kimliği ve arşiv [E11 README'de](../experiments/E11-sequential-three-sct/README.md) kayıtlıdır. 50 ms geçiş payı azaltılmayacak. 12:01:07 çevrimindeki 16/454/392 ms işaret aralıkları nedeniyle gerçek pencere çakışmasızlığı kesin kabul edilmedi. PZEM verisi yok; K=24.22 değişmedi. T010 AKTİF.

## 2026-10-31 — BREAD-TOASTER-001 / SCT-1 3,3 A bölgesi gözlemi

- **TEST:** Ekmek kızartma makinesi için ayrı BREAD-TOASTER-001 yük kaydı açıldı; mevcut TOASTER-001 tost makinesi kaydıyla birleştirilmedi.
- **LOG:** `esp32d1-logs (63).txt`; 32.064 bayt / 449 satır; SHA-256 `cf9254185e591650a06a990e5bc0f567ee499ba4ec541c4bb8748b132513f896`.
- **DÜZENEK:** ESP32D1 / Modül 2 / SCT-1 GPIO32 / ortak bias GPIO35; ESPHome 2026.10.1; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s.
- **UNIT:** 3,30 A kullanıcı bildirimi; PZEM değildir, aynı zaman penceresi olduğu belgelenmedi.
- **SCT SONUCU:** İlk 3,027 A açılış yayını (186 örnek / 930 SPS) dışlandı. Kalan 50 yayın ortalama 3,09636 A; medyan 3,094 A; aralık 3,071–3,144 A; SD 0,01340 A; CV %0,433.
- **ANALOG:** Raw AC ortalama 0,127843 V; SPS ortalama 18.117; GPIO35 bias medyan 1,664 V.
- **YORUM:** UNIT'e göre aritmetik fark −%6,17; eşzamanlılık teyitsiz olduğu için doğruluk/kalibrasyon sonucu değil. PZEM yok.
- **KOD:** K=24.22 ve firmware değişmedi. Python/modelleme yapılmadı.
- **KAYIT:** [BREAD-TOASTER-001 test](../test-loads/bread-toaster/README.md); [Log 63 analiz](../logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-analysis.md); [seçilmiş kanıt](../logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-evidence.txt); [tam ham Log 63](../logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-full.txt).
- **ARŞİV DOĞRULAMA:** Tam 32.064 baytlık ham TXT GitHub'a yüklendi ve geri okunarak doğrulandı; Git blob SHA `06a342ef00d156a9ca78d4dc5d55ea5debe1790c`. SCT-2/SCT-3 ve PZEM doğrulaması bekliyor. T010 AKTİF.



## 2026-10-31 — Modül 2 test yükü: 150 W akkor ampule geçiş

- **PLAN:** Kullanıcı, masaüstü harici besleme ile daha uzun bir SCT-1 logu daha paylaşacağını ve Modül 2 testinde 150 W akkor ampule geçileceğini bildirdi.
- **YÜK KAYDI:** [150 W akkor karşılaştırmalı test dosyası](../test-loads/150w-incandescent/README.md) açıldı. Ana envantere [test-loads/README.md](../test-loads/README.md) üzerinden bağlandı.
- **TARİHSEL KIYAS:** Faz 1 ROADMAP'inde 150 W için referans 0,616 A ve kod sonucu 0,615 A (yaklaşık −%0,2) kayıtlıdır. Bu, yeni Modül 2 testinin sonucu veya kesin hedef değeri değildir; yeni yük/koşul için UNIT ve PZEM ölçümleri ayrıca alınacaktır.
- **YENİ TEST PLANI:** İlk oturum SCT-1 / sarı / GPIO32; ortak bias GPIO35 izlenecek. Masaüstü harici besleme kullanıcı bildirimi olarak kaydedilecek. Firmware sürümü, log zaman aralığı ve eşzamanlı UNIT/PZEM değerleri test sırasında eklenecek.
- **DURUM:** 150 W fiziksel test henüz yapılmadı; bu kayıt plan/altyapı kaydıdır. 100 W uzun tekrar logu da bekleniyor. T010 AKTİF.
## 2026-10-31 — SCT-1 ct_clamp / 100 W PENS karşılaştırması

- **LOG:** Paylaşılan 563 satırlık ESPHome logunda SCT-1 ct_clamp 200 ms pencerelerle çalıştı. Log örnek sayısı yaklaşık 3.323–3.435/pencere; raporlanan örnekleme hızı yaklaşık 16.615–17.175 örnek/s.
- **KARARLI ALAN:** Son beş SCT-1 akım yayını 0,578 / 0,591 / 0,597 / 0,590 / 0,589 A; ortalama 0,589 A.
- **REFERANS:** Kullanıcı aynı 100 W ampul testinde PENS değerini 0,427 A olarak bildirdi.
- **SAPMA:** ESP32D1 ortalaması PENS'ten 0,162 A, yaklaşık %37,9 yüksek.
- **YORUM:** Hızlı örnekleme ve akım çıktısı logla desteklendi; ancak nominal 30 A/V katsayısı bu testte PENS ile uyuşmadı. Tek testten katsayı türetilip uygulanmayacak. CT modelinin SCT-1 için doğrulanması ve eşzamanlı tekrarlı karşılaştırma gerekli.
- **KAYIT:** [SCT-1 100 W ct_clamp + PENS karşılaştırması](../logs/module2/2026-10-31-sct1-100w-ct-clamp-comparison.txt).
- **DURUM:** SCT-1 ilk akım okuma testi yapıldı; ölçüm ölçeği doğrulanmadı. SCT-2/SCT-3 ve tekrarlı karşılaştırma bekliyor. T010 AKTİF.

## 2026-10-31 — Üç kanal ct_clamp akım sensörü eklendi

- **KOD:** [firmware/esp32d1.yaml](../firmware/esp32d1.yaml) GPIO32/33/34 ADC kaynaklarına üç ayrı `ct_clamp` sensörü eklendi. GPIO35 ortak bias ölçümü ve üç ADC voltaj entity'si korundu.
- **YÖNTEM:** Her kanal 200 ms örnekleme penceresi kullanır. Yayın aralıkları 5 s, 5.5 s ve 6 s olarak ayrıldı.
- **İLK KATSAYI:** SCT-013-030 nominal 30 A / 1 V verisinden 30 A/V dönüşümü uygulandı. Bu nominal başlangıç değeridir; saha kalibrasyonu değildir.
- **BEKLENEN:** HA'da üç ayrı akım entity'si A biriminde görünür; ESPHome logunda `sct_current` etiketiyle kanal akımları yazılır.
- **DOĞRULAMA DURUMU:** YAML GitHub'a kaydedildi. Derleme, OTA ve fiziksel akım ölçümü henüz yapılmadı. T010 AKTİF.
- **KABUL:** Derleme başarılı; üç kanalın 100 W yükte ve yüksüz okumaları alınmış; U200B+ veya PZEM karşılaştırması yapılmış olmalı. Gerçek kalibrasyon yapılmadan doğruluk iddiası verilmez.
- **KARAR:** [ADR-016](../docs/decisions/ADR-016-module2-three-channel-ct-clamp.md).

# T010 — Modül 2: ESP32D1 üçlü SCT okuma modülünü oluşturma

- **Durum:** KAPATILDI — mevcut kapsam. Üç SCT kanalının aynı deney oturumunda temel okuma işlevi doğrulandı; sonraki yük/PZEM veri hattı çalışmaları T007/T008 kapsamındadır.
- **Faz:** Faz 2 — Pratik yeniden kurulum ve sistem geliştirme
- **Modül:** BERO-SCT-OKUMA-TEST-002
- **Karar:** [ADR-015](../docs/decisions/ADR-015-module2-esp32d1-triple-sct.md)

## 2026-10-31 — Modül 2 ilk firmware açılışı / bağlantısız ADC kontrol logu

- **KANIT:** Kullanıcının paylaştığı ESPHome logu depoya ham kayıt olarak eklendi: [ilk açılış log kanıt dökümü](logs/module2/2026-10-31-first-boot-no-load.txt).
- **KOD:** [firmware/esp32d1.yaml](firmware/esp32d1.yaml) mevcut depodaki dört ADC sensörlü sürüm; GPIO32/33/34 SCT kanalları ve GPIO35 ortak bias. Log, ESPHome 2026.10.1 ile 2026-10-31 15:19:21 +0300 derlenmiş firmware'in cihazda açıldığını gösteriyor.
- **BAŞLATMA KANITI:** Dört ADC için Handle Init, Config, Calibration ve Overall Init durumları OK. GPIO32/33/34/35, ADC1_CH4/5/6/7 olarak listelenmiş; 12 dB attenuation ve 1.000 s güncelleme aralığı görülüyor.
- **BAĞLANTI DURUMU:** Kullanıcı beyanına göre bu açılış sırasında SCT ve 220 V ampul bağlantısı henüz yapılmamıştı. Bu nedenle üç SCT ADC değerleri sensör/yük ölçüm sonucu değildir; açıkta/bağlantısız analog girişlerin o andaki okumalarıdır.
- **LOG ÖZETİ:** 15:26:05–15:26:14 bölümünde 10'ar örnek: GPIO32 0.333–0.858 V (ortalama 0.634 V); GPIO33 0.142–0.468 V (ortalama 0.259 V); GPIO34 0.442–0.806 V (ortalama 0.588 V); ortak bias GPIO35 1.643–1.668 V (ortalama 1.657 V). Örnek sayısı kısa olduğundan bu aralıklar istatistiksel kararlılık iddiası değildir.
- **AĞ:** Wi-Fi Connected YES, IP 192.168.0.31; ESPHome API handshake başarılı.
- **BROWNOUT AYRIMI:** Önceki ayrı logda OTA rollback/brownout uyarısı vardı. Bu ilk bağlantısız ADC logunda brownout mesajı görünmüyor; bu kayıt önceki olayın nedenini açıklamaz.
- **SONUÇ:** Firmware'in cihazda çalıştığı ve dört ADC kanalının başlatıldığı LOG İLE DESTEKLENDİ. SCT okuma performansı, 100 W ampul tepkisi ve gerçek bağlantı doğrulanmadı. T010 AKTİF kalır; üç ayrı 100 W kanal testi bekliyor.
- **KAYNAK DOSYA ÖZETİ:** Kullanıcı ekindeki özgün log: 203 satır, 11,363 bayt; SHA-256 `88f897b2603815233b0c44e497261169be2e6bff73368b435ae04e38ebb312b3`. Depodaki kayıt dosyası önemli kurulum ve örnek satırlarını korur; özgün tam metin kullanıcı ekinde kalır ve SHA-256 özetiyle tanımlanır.

## 2026-10-31 — SCT-1 / 100 W ilk kanal denemesi

- **TEST:** SCT-1 ön panel 1 numaralı girişe bağlandı; 100 W ampul açıldı (KULLANICI BİLDİRİMİ).
- **BIAS:** Ortak bias logda görüldü; sayısal değer bu bildirimde yok (KULLANICI BİLDİRİMİ).
- **U200B+:** 0,433 A gösterdi (KULLANICI BİLDİRİMİ).
- **ADC:** GPIO32 ADC sayısal log örneği bu kayıtla paylaşılmadı; 0,433 A ESP32 ADC sonucu değildir.
- **KAYIT:** [SCT-1 100 W test kaydı](../logs/module2/2026-10-31-sct1-100w-test.txt).
- **SONRAKİ:** SCT-1 için GPIO32 ve eşzamanlı GPIO35 logu incelenecek; sonra SCT-2 ve SCT-3 aynı ampulle sırayla test edilecek.

## Hedef

Modül içine gömülü ESP32D1 ile üç bağımsız SCT sinyalini ve tek ortak bias noktasını okuyacak modülü oluşturmak. ESP harici 5 V ile beslenecek ve USB üzerinden PC'ye bağlanma imkânı korunacak.

## Kabul edilen işlevsel yapı

- 3 adet 3,5 mm dişi SCT girişi.
- Tek ortak bias devresi; kayıtlı bias yapısı mini breadboard üzerinde.
- Üç SCT için ayrı sinyal bağlantısı.
- Üç SCT'ye ortak dağıtılan bias noktasının tek ADC girişiyle izlenmesi.
- Toplam dört ADC giriş noktası: üç SCT sinyali + tek bias ölçümü.
- Modül içine gömülü ESP32 assembly: ESP32 kartı + GPIO shield.
- Harici 5 V DC besleme.
- ESP USB portundan PC bağlantısına erişim.
- Modül kutusunda şebeke, PZEM veya SSR bulunmaması.

## Bildirilen fiziksel eşleştirmeler

| SCT yuvası | Sinyal kablosu | Shield GPIO | Durum |
|---|---|---|---|
| 1. dişi yuva | Sarı | GPIO32 | Kullanıcı bildirdi |
| 2. dişi yuva | Yeşil | GPIO33 | Kullanıcı bildirdi |
| 3. dişi yuva | Mavi | GPIO34 | Kullanıcı bildirdi |
| Ortak bias ADC | Turuncu | GPIO35 | Kullanıcı bildirdi |

Dört eşleştirme de kullanıcı bildirimidir. Jakların tip/ring/sleeve pin diziliminin ve kabloların gerçek terminal güzergâhının tamamı fiziksel olarak doğrulanmış değildir.

## Kutu montajı ve 100 W kanal testi

**Kullanıcı bildirimi:** ESP32D1, üç SCT kanal bağlantısı ve Bias Trafosu modülü kapalı kutu içine gömüldü. Kutu harici 5 V DC ile beslenecek. Bu bilgi montaj beyanıdır; güç yolu/gerilim ölçümü veya çalışma testi anlamına gelmez.

| Test sırası | SCT kanalı | Kablo | GPIO | Test yükü | Sonuç |
|---:|---|---|---:|---|---|
| 1 | SCT-1 | Sarı | GPIO32 | 100 W akkor ampul | Bekliyor |
| 2 | SCT-2 | Yeşil | GPIO33 | 100 W akkor ampul | Bekliyor |
| 3 | SCT-3 | Mavi | GPIO34 | 100 W akkor ampul | Bekliyor |

Her testte aynı 100 W akkor ampul kullanılacak ve SCT kanalları sırayla, ayrı ayrı denenecek. GPIO35 ortak bias ADC kanalıdır; yük kanalı değildir ve her adımda izlenecektir. Yük kapalı başlangıç, açık kararlı bölüm ve kapatma sonrası değerleri ile GPIO35 bias değeri kaydedilecek. Test sonuçları henüz mevcut değildir.

**Güvenli test koşulu:** SCT, yalnız tek yalıtılmış iletkeni çevrelemelidir; faz ve nötr birlikte geçirilmez. CT bağlantısı/kanal değişimi yük enerjisizken yapılır. Şebeke tarafı kapalı ve korumalı lamba düzeneğinde tutulur; açıkta 230 V bağlantı veya breadboard kullanılmaz.

## Kod durumu

Başlangıç ESPHome iskeleti [esp32d1.yaml](../firmware/esp32d1.yaml) dosyasına kaydedildi. Cihaz kimliği esp32d1 / ESP32D1 olarak kullanıcı tarafından sağlandı.

İlk ADC giriş kontrolü YAML'ı eklendi: GPIO32/33/34 üzerinde üç SCT ADC gerilim sensörü ve GPIO35 üzerinde ortak bias ADC gerilim sensörü bulunur. Kod anlık gerilim yayınlar; RMS/akım hesabı içermez. Derleme ve cihaz testi yapılmadı.

## İş sırası

1. ESP32 kartı ve takılı GPIO shield'ın tam modelini/revizyonunu belirle.
2. ESP kartındaki USB konektörünü ve 5 V güç giriş yolunu doğrula. PC USB ve harici 5 V birlikte kullanılacaksa kartın güç yolu/geri besleme korumasını kontrol et.
3. Üç jack ve ortak bias mini breadboard bağlantılarını fiziksel olarak izle; tip/ring/sleeve pinout'unu doğrula.
4. Bildirilen dört eşleştirmeyi (GPIO32 sarı, GPIO33 yeşil, GPIO34 mavi, GPIO35 turuncu bias) fiziksel olarak teyit et.
5. Tek ortak bias bağlantısını üç SCT sinyal girişine nasıl dağıtacağını mevcut bias devresi üzerinde doğrula.
6. İlk sürümde dört ADC kanalı voltaj olarak tanımlandı; fiziksel bias gerilimi ölçülerek Home Assistant değeriyle karşılaştırılacak.
7. İlk ADC giriş kontrolü YAML'ını derle; derleme sonucunu kaydet.
8. Analog düğümlerin gerilimini multimetreyle doğrula; sonra düşük gerilim bağlantısı ve dört kanalın HA yayını testini yap.
9. Başarılı derleme/cihaz logu, gerçek sensör çıktısı ve yorumunu depoya ekle. SCT akım/RMS okuma yaklaşımı ancak bu temel aşama doğrulandıktan sonra seçilecek.

## Açık noktalar

- ESP32 kart model/revizyonu ve GPIO shield modeli.
- USB konektör tipi; harici 5 V ve PC USB'nin aynı anda kullanımı.
- Dört GPIO'nun gerçek ESP32 kartı ve shield terminaliyle birebir eşleştiğinin fiziksel teyidi.
- Üç jack'in tip/ring/sleeve pinout'u ve dört rengin gerçek terminal güzergâhının fiziksel teyidi.
- Bias devresinin elektrolitik kondansatör değeri/polaritesi ve Bias Trafosu modülünden besleme bağlantısı.
- Bias ADC'nin yazılım gösterimi (RAW count veya voltaj).
- SCT sinyalinden akım/RMS üretmek için sonraki aşamada seçilecek çalışan okuma yaklaşımı.

## Bağlantı ve güvenlik koşulları

- Harici 5 V yalnız kartın belgelenmiş girişine bağlanır; ADC/GPIO girişlerine verilmez.
- PC USB ile harici 5 V'un eşzamanlı bağlanması, kart güç devresi doğrulanmadan yapılmaz.
- ESP32 GND ve bias devresi GND ortaklanır; bağlantı noktaları devre görülerek doğrulanır.
- Analog giriş gerilimi ESP32 ADC giriş sınırları içinde olmalıdır.
- Jack pinout'u doğrulanmadan SCT kabloları bağlanmaz.
- Modül 2 yalnız düşük gerilim tarafıdır; 220–240 V bağlantı kutu kapsamı dışındadır.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Modül 2'nin elektriksel ve yazılımsal yapısını uygulanabilir hâle getirmek.
- **LOG:** Kullanıcının ESPHome temel ayarları, dört bağlantı bildirimi, kapalı kutu montajı, kutu içindeki Bias Trafosu modülü ve harici 5 V besleme planı kaydedildi.
- **SONUÇ:** GPIO eşleştirme tablosu ve 100 W akkor ampulle üç ayrı kanal test planı depoda. Üç test sonucu, derleme ve fiziksel çalışma doğrulaması beklemede. Modül tamamlanmış değildir.

## 2026-10-31 — E10 ct_clamp pencere süresi gözlem deneyi

T010 altında, mevcut SCT-1 okuma zincirinin pencere süresine duyarlılığını incelemek için [E10 protokolü](../experiments/E10-ct-clamp-window-duration/README.md) açıldı. Deney 200 → 500 → 1000 → 200 ms geri dönüş sırasını kullanır. SCT-1 GPIO32, ortak bias GPIO35, ESPHome 2026.10.1, ADC 12 dB/1 s, ct_clamp update_interval: 2s ve K=24.22 sabit kalır. Yalnızca sample_duration değişir. BREAD-TOASTER-001 aynı fiziksel yük olarak seçildi; Log 63 tarihsel 200 ms tabanıdır, yeni A kontrol aşaması yine alınacaktır.

**Amaç kalibrasyon değildir.** Pencere süresinin Raw AC RMS, akım dağılımı, kabul edilmiş örnek sayısı/SPS ve geçişleri yumuşatma davranışı üzerindeki etkisi gözlenecek. Raporlardaki simülasyonlar gerçek BERO ölçümü sayılmayacak. E10 henüz PLANLANDI; YAML değişikliği, derleme/OTA ve fiziksel log bekliyor. Sonuçlar [E10 sonuç defterine](../experiments/E10-ct-clamp-window-duration/results.md) yazılacak.


## 2026-10-31 — ct_clamp araştırma sentezi sonrası deney sırası

- **ARAŞTIRMA KAYDI:** [H1–H19 hipotez sicili](../docs/research/ct-clamp/2026-10-31-hypothesis-register-and-next-experiments.md).
- **ÖNCELİK:** Üç SCT kanalının tekil/çoklu davranışını kontrollü karşılaştır; ardından T010 altında E10 penceresini 200 → 500 → 1000 → 200 ms geri dönüş sırasıyla uygula.
- **AYRI SORU:** last_value tekrar filtresinin ESP32 dahili ADC üzerindeki etkisi E10'dan ayrı, tek değişkenli A/B deneyiyle incelenebilir. Mevcut filtreyi kaldırma kararı alınmadı.
- **SONRAKİ FAZ 2 SIRASI:** T010 tamamlanmadan T007/T008/T006'ya geçiş yapılmaz; ana görev sırası değişmedi.
- **DURUM:** Bu not araştırma/planlama kaydıdır. Yeni derleme, OTA, fiziksel test veya firmware değişikliği yapılmadı. T010 AKTİF kalır.


## 2026-11-01 — Kullanıcı düzeltmesi: Modül 2 üretim ve saha kontrolleri

Bu kayıt, BERO projesinin sahibi ve Modül 2'nin imalatçısı olan kullanıcının 2026-11-01 tarihli birinci el üretim/çalışma beyanına dayanır. Proje sahibinin kendi yaptığı işlemleri bildirmesi olağan birincil proje kaynağıdır; bu beyanı şüpheyle ele almak veya kullanıcıdan aynı işi yeniden kanıtlamasını istemek doğru değildir.

- **ÜÇ SCT KANALI:** Modül ilk üretildiğinde üç kanalın her birinde okuma kontrolü yapıldı. Bu ilk kanal okuma kontrolü tamamlanmış kabul edilir; aynı kontrol yeniden yapılacak iş olarak listelenmeyecek.
- **ORTAK BIAS:** Bias devresi üç kanala ayrı ayrı ait değildir; tek ortak bias noktası kullanılır. Modül üretiminde bias ölçümü yapıldı ve kullanıcı görsel de paylaştı. Bu ortak yapı ve ilk ölçüm kullanıcı tarafından doğrulandı.
- **GERÇEK CİHAZ ÇIKTILARI:** Modül 2 ile test yükleri çalıştırıldı; test yüklerine ait cihaz logları ve analiz kayıtları depoda bulunuyor. Bu kayıtlar yeniden üretilecek testler değil, mevcut kanıtlardır.
- **DERLEME / FİZİKSEL ÇALIŞMA:** İlgili derleme ve fiziksel çalışma loglarının depoda saklandığı kullanıcı tarafından teyit edildi. Her bir kaydın teknik kapsamı kendi log/analiz dosyasına göre okunmalıdır.
- **DÜZELTİLEN ÖNCEKİ SONUÇ:** Bu dosyanın önceki “üç kanal 100 W testleri, derleme ve fiziksel doğrulama beklemede” ifadesi, sonraki kullanıcı bildirimleri ve depo test kayıtları ışığında güncel durum özeti olarak kullanılmamalıdır. İlk üretim kanal kontrolleri ve bias kontrolü tamamlanmıştır.
- **AYRI KALAN İŞ:** E10 pencere deneyi (200 → 500 → 1000 → 200 ms ve 200 ms geri dönüş kontrolü) hâlâ PLANLANDI durumundadır; bu deneyin yapılmış olduğu iddia edilmez.
- **DOSYA TUTARSIZLIĞI:** firmware/esp32d1.yaml dosyası hâlen tek SCT kanalı GPIO32 ve ortak bias GPIO35 konfigürasyonunu gösteriyor; GPIO33/GPIO34 ilk kanal kontrollerinin yapıldığı kullanıcı beyanını firmware'de üç aktif ct_clamp kanalı bulunduğu şeklinde yorumlamamak gerekir. Üç kanalın mevcut firmware ile temsil edilip edilmediği ayrı bir dokümantasyon/kod tutarlılığı konusudur.
- **DURUM:** Kullanıcı tarafından bildirilen ilk üretim kontrolleri tamamlandı. E10 ve dosya/konfigürasyon tutarlılığı ayrı takip edilir. Bu kayıt yeni fiziksel ölçüm veya yeni derleme yapıldığı anlamına gelmez.


## 2026-11-01 — Tasarım kararı: taşınabilir modülde tek kablolu ortak bias

- **KARAR / FİZİKSEL TASARIM:** Modül 2'yi taşınabilir ve sade tutmak amacıyla bias dağıtımı tek ortak bias hattı üzerinden yapılmıştır. Üç SCT kanalı için üç ayrı bias devresi veya üç ayrı bias kablosu kullanılmamıştır.
- **İMALAT:** Bias devresi breadboard üzerinde kurulmuş; kullanıcı daha önce bu breadboard bias düzeninin görüntüsünü paylaşmıştır. İmalat sırasında ortak bias ölçümü de yapılmıştır.
- **MİMARİ:** Üç SCT'nin sinyal yolları birbirinden bağımsızdır; bias referansı tek ortak noktadan/tek kabloyla dağıtılır. GPIO35 bu ortak bias noktasını izleyen giriş olarak tanımlanmıştır.
- **AMAÇ:** Ayrı ayrı bias modülleri ve kabloları taşımak yerine tek ortak bias dağıtımıyla modülün taşınabilirliğini ve fiziksel sadeliğini korumak.
- **KAYNAK SINIFI:** Kullanıcının kendi imalatı ve yaptığı ölçüm hakkındaki birinci el beyanı (USER REPORT). Bu, proje sahibinin üretim kaydıdır; yeniden yapılacak doğrulama görevi değildir.
- **SONUÇ:** Tek kablolu ortak bias, Modül 2'nin bilinçli ve uygulanmış donanım tasarımıdır. Üç ayrı bias devresi/bağlantısı talep edilmeyecek ve bu tasarım eksik bağlantı olarak raporlanmayacaktır.


## 2026-11-01 — Üç SCT kanalının sıralı ölçümle sağlıklı okuma doğrulaması

### Amaç

Bu çalışmanın amacı üç SCT kanalının aynı yükü gözlerken **her birinin bağımsız ve sağlıklı ölçüm üretebildiğini** doğrulamaktır. Önceki üç kanalın yazılımda aynı anda örneklenmesi yaklaşımında sağlıklı sonuç alınmadığı kullanıcı tarafından bildirildi. Yeni yaklaşımda sensörler aynı fiziksel yükü aynı anda gözler; ESP32'nin ADC/ct_clamp ölçüm pencereleri ise sırayla açılır. Bir kanalın ölçüm penceresi açıkken diğer iki kanalın penceresi başlatılmaz.

Bu bir eşzamanlı örnekleme deneyi değildir. Amaç, kanalların aynı kararlı yük koşulunda, mümkün olan en küçük ve ölçülebilir zaman kaymasıyla karşılaştırılmasıdır.

### Sabit fiziksel düzen

- Yük: aynı 100 W akkor ampul.
- SCT-1: sarı sinyal / GPIO32 / ADC1_CH4.
- SCT-2: yeşil sinyal / GPIO33 / ADC1_CH5.
- SCT-3: mavi sinyal / GPIO34 / ADC1_CH6.
- Ortak bias: tek ortak hat; turuncu izleme / GPIO35 / ADC1_CH7.
- Her kanal ayrı sinyal yoluna, üç kanal tek ortak bias referansına sahiptir. Donanım tekrar imal edilmeyecek ve bias için üç ayrı hat oluşturulmayacaktır.
- Firmware ortamı: ESPHome 2026.10.1, ESP32D1, ESP-IDF.

### Sıralı okuma yöntemi

1. SCT-1 için `component.update` ile yalnızca SCT-1 `ct_clamp` penceresini başlat.
2. SCT-1'in 200 ms örnekleme penceresinin tamamlanmasını bekle.
3. SCT-2 penceresini başlat; SCT-1 artık örnekleme yapmıyor olmalı.
4. SCT-2 tamamlandıktan sonra SCT-3 penceresini başlat.
5. Üç kanal tamamlandıktan sonra GPIO35 ortak bias ölçümünü tetikle.
6. Her çevrimde START/COMPLETE loglarıyla kanal sırası ve zaman damgalarını görünür kıl.

İlk aday zamanlamada her kanal için 200 ms `sample_duration` ve 250 ms tetikleme aralığı kullanılmıştır. Bu, 200 ms ölçüm + 50 ms geçiş payı demektir. İlk ve son kanal ölçüm merkezleri arasında yaklaşık 500 ms bulunur. **Bu değer nihai hedef veya optimum kabul edilmemiştir.** Kullanıcının hedefi küçük senkron kayması olduğundan, ilk derleme/cihaz denemesinden sonra logdaki gerçek başlangıç-bitiş zamanlarına göre güvenli geçiş payı mümkün olan en düşük değere indirilecek; örnekleme pencerelerinin çakışmadığı doğrulanacaktır.

### Başarı ölçütleri

- Üç ayrı kanalın her biri geçerli ve tekrarlanabilir Raw AC / akım çıktısı üretmeli.
- Kanal etiketleri ve GPIO eşleştirmeleri karışmamalı.
- Bir kanalın örnekleme penceresi bitmeden sonraki kanal başlamamalı.
- Log zaman damgaları kanal sırasını ve gerçek kanal merkezleri arasındaki kaymayı hesaplamaya elverişli olmalı.
- Aynı 100 W ampul ve aynı fiziksel koşul korunmalı; böylece kanallar arası fark sensör/kanal davranışı olarak incelenebilmeli.
- Bias, üç kanalın ölçümü sırasında ayrı bir ADC örneklemesiyle araya girmemeli; ortak bias çevrim sonunda okunmalı.
- İlk turda hedef üç kanalın sağlıklı çalışması ve zamanlama ayrışmasıdır; bu test tek başına kalibrasyon veya doğruluk onayı değildir.

### Deney sırası

1. Sıralı üç-kanal YAML adayını ESPHome 2026.10.1 ile derle.
2. Derleme başarılıysa cihazı yükle ve açılış/kanal START-COMPLETE loglarını al.
3. Aynı 100 W ampul üç SCT tarafından fiziksel olarak gözlenirken sıralı çevrimi çalıştır.
4. Her kanalda yeterli sayıda çevrim topla; geçersiz/eksik yayın, kanal karışması, pencere çakışması ve dağılımı incele.
5. Log zaman damgalarından gerçek merkez-zaman farklarını hesapla.
6. 50 ms geçiş payı gereğinden büyükse, pencere çakışması olmadan azaltılabilecek en küçük güvenli aralığı belirle.
7. YAML, derleme sonucu, gerçek cihaz logu ve log yorumu birlikte arşivlenmeden kod başarılı sayılmayacak.

### Durum ve kayıt sınırı

- **DURUM:** Sıralı okuma hedefi ve deney yöntemi kaydedildi; YAML henüz derlenmedi veya cihaza yüklenmedi.
- **BAŞARI İDDİASI:** Yok. Üç kanalın sıralı firmware ile sağlıklı okuduğu henüz doğrulanmadı.
- **SONRAKİ ADIM:** Aday YAML'ı derlemek; derleme sonucu uygunsa cihazda kontrollü 100 W testini yapmak.
- **İLGİLİ KARAR:** [ADR-018](../docs/decisions/ADR-018-module2-sequential-sct-window-test.md).


## 2026-11-01 — E11 sıralı üç kanal firmware derleme ve çalışma bildirimi

- **KULLANICI BİLDİRİMİ:** Kullanıcı, SCT-1 GPIO32 → SCT-2 GPIO33 → SCT-3 GPIO34 sıralı okuma YAML'ının derlendiğini ve cihazda çalıştığını bildirdi.
- **KOD SNAPSHOT:** [E11 firmware YAML](../experiments/E11-sequential-three-sct/esp32d1-sequential-sct.yaml).
- **TEST KAYDI:** [E11 — Üç SCT sıralı okuma](../experiments/E11-sequential-three-sct/README.md).
- **SONUÇ SINIRI:** Derleme ve çalışma kullanıcı beyanı olarak kaydedildi. Bu aşamada ham log ve kanal başına sayısal sonuç sunulmadığından kanal doğruluğu, tekrarlanabilirliği, gerçek zaman kayması ve pencere çakışmasızlığı nicel olarak doğrulanmış sayılmaz.
- **SONRAKİ:** Cihaz logunu al; üç kanalın Raw AC/akım yayınlarını ve zaman damgalarını incele. Ardından 50 ms geçiş payının azaltılabilirliğini değerlendir.
- **T010 DURUMU:** Sıralı firmware denemesi çalıştırıldı. T010 genel kabulü, log analizi ve kalan doğrulama maddeleri tamamlanmadan kapatılmaz.


## 2026-11-01 — E11 uzatılmış Log 66 değerlendirmesi

- **KAYNAK:** [Log 66 arşivi](../logs/module2/2026-11-01-e11-three-sct-sequential-log66-full-overlap.txt); [uzatılmış analiz](../logs/module2/2026-11-01-e11-three-sct-sequential-extended-analysis.md); [seçilmiş kanıt](../logs/module2/2026-11-01-e11-three-sct-sequential-extended-evidence.txt).
- **BİRLEŞTİRME:** Log 66'nın ilk 1.678 satırı Log 64 ile birebir örtüştüğü için tekilleştirildi. Birleşik kayıtta 397 tamamlanmış çevrim vardır; ilk açılış ve son yarım çevrim dışarıda bırakılarak 396 kararlı çevrim incelendi.
- **KANAL ORTALAMALARI:** SCT1 0.423884 A; SCT2 0.424328 A; SCT3 0.425828 A. SCT3 dağılımı en düşük (CV %2.215), SCT2 en yüksek (CV %2.810).
- **ÖRNEK SAYISI:** SCT2 3235 farklı örnek/200 ms ortalamasıyla SCT1 ve SCT3'ten yaklaşık %5 düşük kalıyor; daha uzun kayıtta da tekrarlandı.
- **ZAMANLAMA:** 42/396 çevrimde en az bir geçiş işareti 200–300 ms tanısal aralığının dışındadır. START/COMPLETE işaretleri gerçek pencere callback'leri değildir; pencere çakışmasızlığı kesin kabul edilmedi.
- **ROAMING:** 12:01:04.985 ve 12:06:04.908 Wi-Fi roaming scan kayıtları zamanlama sapmalarına yakındır. Olası etki; neden kanıtlanmadı.
- **REFERANS SINIRI:** PZEM/UNIT yok; yük ve besleme koşulu açıkça tanımlanmamıştır. Kalibrasyon veya ±4% kabulü çıkarılmadı.
- **KARAR:** YAML, K=24.22 ve 50 ms geçiş payı değiştirilmedi. T010 AKTİF; sonraki adım gerçek pencere başlangıç/bitişini cycle_id ile callback tabanlı loglamaktır.
