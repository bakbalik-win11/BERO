## 2026-11-01 — ADR-025

- Kararlı SCT/PZEM alanları katsayı öğrenmek için kullanılır; ham kayıt korunur.
- Öğrenilmiş SCT modeli tam ham kayıtta da incelenir.
- Bu incelemede Python bilinen yük koşulunu kullanır; PZEM geçiş okumaları örnek başına referans değildir.
- Mimari karar kaydedildi; uygulama ve gerçek veri testi beklemede. Ayrıntı: [ADR-025](docs/decisions/ADR-025-raw-data-sct-model-behavior-validation.md).

## 2026-11-01 — E11 yüksüz iki modül uzun süreli gözlem planı

- İlk ortak deney olarak E11 planlandı: Modül 2 ve Modül 3 birlikte çalışacak; ölçülen hatta yük bulunmayacak.
- Modül 3 PZEM akım/gerilim/PF akışını, Modül 2 üç SCT kanalını sürekli yayınlayacak.
- Modül 3'ün 40 s ON / 20 s OFF mantıksal SSR döngüsü sürerken Modül 3 gönderim olayları ile Modül 2 alım olayları BOOT_ID + EVENT_ID + STATE üzerinden karşılaştırılacak.
- Önce kısa ortak açılış ve log kontrolü; başarılıysa ertesi gün akşama kadar hedeflenen yüksüz uzun gözlem.
- Deney sırası ihtiyaç ve donanım hazır oluşuna göre değişebilir; bu esneklik Faz 2 görev bağımlılıklarını değiştirmez.
- Modül 2 üç SCT kanalı açık kalır; kanal seçici jumper/düğme eklenmesi planlanmıyor.
- **Durum:** Yalnız planlama kaydı. Montaj, deney, log ve sonuç henüz yok. [E11 protokolü](experiments/E11-idle-dual-module-observation/README.md).

## 2026-11-01 — Python ON/OFF paket bütünlüğü kararı (ADR-024)

- Mevcut UDP/HA olay aktarımı korunur; yeni HA helper veya merkezi HA mimarisi kurulmaz.
- Modül 3 PZEM ve Modül 2 SCT akışları kendi ON/OFF olaylarıyla bağımsız paketlenir.
- ON başlangıcı veya OFF bitişi eksik/uyuşmazsa ilgili akış aralığı tamamlanmış paket değildir; Python bunu tanı koduyla raporlar.
- İki akışta aynı BOOT_ID + EVENT_ID paket aralığı doğrulanmadan eğitim örneği oluşturulmaz.
- Yeni ON açık pakete gelirse önceki paket eksik/bozuk olarak kapatılır ve yeni ON yeni paket adayı başlatır; BOOT_ID değişiminde açık paket tamamlanmamış sayılır.
- ADR-024 mimari kabul kuralıdır; Python kodu ve gerçek export testi henüz yapılmadı.

## 2026-11-01 — Modül 2/3 uzun ON/OFF olay aktarımı

- Modül 2 uzun logunda EVENT_ID 59 ON, 61 ON, 62 OFF ve 64 OFF alındı; her biri için HA_EVENT_PUBLISHED var.
- EVENT_ID 60 ve 63 bu alıcı logunda yok; kayıpsız aktarım sonucu çıkarılamaz.
- Ayrı HA History ekran görüntüsünde EVENT_ID 70 OFF ve 71 ON, Modül 2 ve Modül 3 olay kayıtlarında görünüyor; SSR HA entity mantıksal Kapalı/Açık durumlarını gösteriyor.
- 70 OFF → 71 ON arası 20 saniye. Fiziksel SSR kontak anahtarlaması ve Recorder DB kalıcılığı bağımsız doğrulanmadı.
- Kanıt ve analiz: [uzun ON/OFF analizi](logs/module2/2026-11-01-module2-on-off-extended-analysis.md), [seçilmiş kanıt](logs/module2/2026-11-01-module2-on-off-extended-evidence.log).
- Modül 2/3 kod başlıkları ve README protokol açıklamaları güncel mimariye göre düzenlendi; kod mantığı değiştirilmedi.
- T010 kapalı; T007/T008 Python veri aktarımı ve paketleme uygulaması henüz yapılmadı.


## 2026-11-01 — Modül 2 UDP olay alıcısı ilk gerçek paket kanıtı

- Yeni kaynak: [firmware/bero-modul2-esp32d1.yaml](firmware/bero-modul2-esp32d1.yaml). LOAD-15W-003 üç-SCT sıralı ölçüm temeli korunarak UDP 4210 dinleyicisi ve HA olay entity'leri eklendi.
- Gerçek Modül 2 logunda Modül 3 kaynak IP 192.168.0.70'ten EVENT_ID=59 / STATE=ON paketi alındı; ham mesaj ile BOOT_ID/EVENT_ID/STATE HA entity'lerine yayınlandı.
- [Seçilmiş log kanıtı](logs/module2/2026-11-01-module2-udp-event-receiver-evidence.log); [log analizi](logs/module2/2026-11-01-module2-udp-event-receiver-log-analysis.md).
- **Doğrulama sınırı:** Tek ON paketi doğrulandı. OFF alımı, çoklu olay/kayıpsızlık, Recorder kalıcılığı ve yeni kaydedilen YAML'ın bağımsız derleme/OTA testi açık.
- T010 kapalı kalır; olay alıcısı bu göreve eklenen yeni bir entegrasyon kaydıdır. T007/T008 veri aktarımı ve Python paketleme işleri ayrı aşamalardır.

## 2026-11-01 — Paket işaretli akış bölümleme kararı (ADR-022)

- Modül 3, SSR olay değişiminde tek `BERO_EVT` mesajı üretir; aynı mesajı kendi PZEM akışına ayrı kayıt olarak ekler ve UDP 4210 ile Modül 2'ye gönderir.
- Modül 2, aldığı aynı mesajı kendi SCT akışına ayrı kayıt olarak ekler; olay kimliğini yeniden üretmez.
- Ölçüm kayıtlarına örnek başına zaman/paket alanı eklenmez. ESP'ler kararlılık, kırpma, eşleştirme veya katsayı hesabı yapmaz.
- Python her akışı olay işaretleriyle paket aralıklarına böler; aralıkları BOOT_ID + EVENT_ID ile eşleştirir.
- PZEM ve SCT kararlılığı kendi akışlarında bağımsız tespit edilir; geçiş/yerleşme bölümleri kırpılır. Eğitim etiketi Python tarafından paket kimliğiyle eklenir.
- Timestamp iki sensörün ölçümlerini eşleştirme anahtarı değildir; HA dışa aktarımında yalnızca aynı modül içindeki kayıt sırasını yeniden kurmak için gerekebilir.
- ADR-019'un timestamp kesişimi şartı bu kararla geçersiz kılındı. [ADR-022](docs/decisions/ADR-022-packet-marker-segmented-training-streams.md).
- **Uygulama durumu:** Yalnızca mimari dokümantasyon. Firmware, derleme, OTA, UDP ve HA kayıt sıralaması henüz değiştirilmedi/doğrulanmadı.

## 2026-11-01 — T008 kararlı alan eşleştirme prensibi netleştirildi

- SCT ve PZEM kararlılığı kendi ölçüm akışlarından bağımsız tespit edilir; zaman veya UDP olayları kararlılık ölçütü değildir.
- Paket/zaman/SSR ON-OFF yalnızca deneyin olay çerçevesini sağlar.
- Eğitim verisi, iki bağımsız kararlı aralığın zaman kesişimidir. Örnek: SCT 10–16 s, PZEM 12–14 s ise ortak bölüm 12–14 s.
- Eşit başlangıç/bitiş veya eşit süre gerekmez. Zaman damgası yalnız kesişim hesabında kullanılır; zaman bazlı kararlılık penceresi yoktur.
- ON–OFF aralığı kendiliğinden kararlı değildir. Eşik/tolerans/minimum süre gerçek HA verisinden sonra belirlenecek.
- [ADR-019](docs/decisions/ADR-019-module2-module3-independent-event-streams.md); [Python veri hattı mimarisi](docs/architecture/python-program-architecture.md).


## 2026-11-01 — LOAD-15W-003 çok turlu UNIT kıyası hazırlandı

- Tek 15 W yük için tek oturum planlandı: SCT1 faz 2T, SCT3 faz 3T, SCT2 nötr 4T; UNIT bağımsız referans.
- Karşılaştırma: SCT1↔UNIT×2, SCT3↔UNIT×3, SCT2↔UNIT×4; ayrıca tur sayısına bölünmüş normalize değerler UNIT ile kıyaslanacak.
- [Test planı](test-loads/15w-2t-3t-4t/README.md) ve [YAML snapshot](firmware/archive/LOAD-15W-003-2026-11-01-esp32d1-15w-2t-3t-4t-unit.yaml) eklendi.
- Kanallar aynı çevrimde sıralı okunur; eşzamanlı örnekleme değildir. K=24.22, 200 ms, 250 ms slot ve 2 s çevrim korunur.
- 15 W tekil yük UNIT baseline'ı ve fiziksel log yok. Derleme/OTA/deney yapılmadı; durum PLANLANDI/HAZIRLANDI.

## 2026-11-01 — LOAD-42W-002 kısa log denetimi

- 68 saniyelik kısa logda 34 çevrim tamamlandı; Wi-Fi ve ADC başlatmaları normal, hata satırı yok.
- Ortalama: SCT1 0.25106 A; SCT2 0.24150 A; SCT3 0.34732 A; bias 1.66147 V.
- SCT3/SCT1 oranı 1.383; 2T/1T davranışı için takip gerekiyor.
- Raw AC entity'lerinde birim/semantik hatası tespit edildi: filtre öncesi ham akım A iken entity V olarak etiketlenmiş. Firmware henüz düzeltilmedi.
- HA Recorder/History kök nedeni doğrulanmadı; API server dinliyor fakat HA client bağlantısı ve Recorder yazımı logla kanıtlanmıyor.
- [Kısa log ve teşhis notu](logs/module2/2026-11-01-load-42w-002-short-log-ha-diagnostic.md). Test açık.

## 2026-11-01 — LOAD-42W-002 üç SCT / HA uzun kayıt

- 42 W ampul altında üç kanallı uzun süreli HA geçmiş gözlemi açıldı: [test kaydı](test-loads/42w-bulb/README.md).
- SCT1 faz 1T/GPIO32; SCT2 nötr 1T/GPIO33; SCT3 faz 2T/GPIO34; ortak bias GPIO35.
- Kullanıcı YAML'ın derlendiğini bildirdi; [kod snapshot](firmware/archive/LOAD-42W-002-2026-11-01-esp32d1-three-sct-ha-history.yaml).
- HA Recorder/History, OTA/cihaz çalışması ve uzun kayıt henüz doğrulanmadı. Test AÇIK.
- Bu yeni test T010'u yeniden açmaz; T010 kapalıdır.

## 2026-11-01 — Faz 2 veri hattı ve düşük akım yürütme planı

- [Ayrıntılı yürütme planı](docs/plans/2026-11-01-phase2-data-and-low-current-execution-plan.md) eklendi; STATUS ve ROADMAP'ten bağlandı.
- Görev sırası korundu: T009 → T010 → T007 → T008 → T006. T010 aktif kalır.
- 0.4 A fiziksel alt sınır ve güncel Modül 2'de 0.35 A eşik bulunduğu iddiaları kabul edilmedi; mevcut kanıt bunları desteklemiyor.
- Düşük akım nedeni henüz ayrıştırılmadı; K, firmware, eşik, pin ve deney ayarları değiştirilmedi.
- Bu değişiklik bir planlama kaydıdır; yeni derleme, OTA veya fiziksel ölçüm değildir.

## 2026-11-01 — Gün sonu kapanışı

- Bu sohbet kapsamında BERO'ya ait kod, YAML, donanım veya deney değişikliği yapılmadı; Claude hizmeti ve genel kod denetim promptu BERO dışı konulardı.
- Faz 2 / T010 aktif kaldı. E10 hâlâ PLANLANDI; yeni log, derleme, OTA veya fiziksel ölçüm eklenmedi.
- Sonraki çalışma: T010 kanal testlerinden kontrollü biçimde devam etmek; E10 protokolünü ayrı ve sabit değişkenli deney olarak yürütmek.

## 2026-10-31 — ct_clamp hipotez sicili ve sonraki deney sırası

- Bu sohbetin H1–H19 sınıflandırması tek bir [hipotez sicilinde](docs/research/ct-clamp/2026-10-31-hypothesis-register-and-next-experiments.md) toplandı.
- Kaynak kod/tarihçe bulguları, BERO saha desteği, hipotezler, açık araştırma soruları ve kanıtsız iddialar ayrıldı.
- Sonraki ölçüm sırası: T010 kanal davranışı; E10 200→500→1000→200 ms; ayrı last_value A/B; ardından T007→T008→T006.
- E10 hâlâ planlandı; bu kayıt sırasında YAML/firmware/K değiştirilmedi, derleme/OTA ve fiziksel deney yapılmadı.

## 2026-10-31 — BERO sensörden bağımsız mimari kaydı

- Depo kökünde [MIMARI](../../MIMARI/README.md) alanı oluşturuldu.
- [Pencereli Sensör Analizi ve Davranış Çıkarımı](../../MIMARI/PENCERELI-SENSOR-ANALIZI/README.md) üç katmanı tanımlar: veri toplama, özellik çıkarma, davranış çıkarımı.
- SCT013-PZEM bu mimarinin ilk uygulama/kanıt alanıdır; sensöre özgü pin, katsayı ve algoritmalar genel ilke sayılmaz.
- Özellik penceresi ile kararlılık penceresi ayrıldı; sürekli ham ADC saklama kararı değiştirilmedi.
- Yeni mimari belge tasarım kaydıdır; genel davranış sınıflandırması veya yeni sensör entegrasyonu tamamlanmış değildir.

## 2026-10-31 — Sensör okuma kalıpları

- ct_clamp araştırmasından hareketle genel sensör veri yolu ile CT'ye özgü AC RMS algoritması ayrıştırıldı.
- Açıklamalı referans YAML'lar eklendi: [CT / AC RMS](firmware/patterns/ct-clamp-ac-rms-reference.yaml), [analog DC ADC](firmware/patterns/adc-dc-voltage-observer.yaml).
- Ayrıntı ve sensör türüne göre seçim rehberi: [firmware/patterns/README.md](firmware/patterns/README.md).
- Patterns rehberinde gerçek Log 63 örnek çıktısı (0,12763 V Raw AC / 3,091 A / 3.656 kabul edilmiş örnek) gösterildi; tarihsel kanıt, yeni şablon testi değildir.
- Şablonlar henüz derlenmedi veya donanımda test edilmedi; mevcut ESP32D1/ESP32D2 firmware'leri değiştirilmedi.
- firmware/esp32d1.yaml ile daha sonraki üç kanallı T010 kaydı arasında içerik tutarsızlığı tespit edildi; mevcut dosya korunarak ayrı not edildi.

## 2026-10-31 — ESPHome ct_clamp üç kaynaklı sentez

- Claude, GitHub Copilot ve bağımsız inceleme; PR #559, #1906, #1915, #1916, #2283, #4229 ve #4236 kayıtlarıyla sentezlendi.
- 2019 ilk geliştirme ile 2021 algoritma/iyileştirme adımları ayrıştırıldı. Copilot'un 200 ms, 60 s ve performans gerekçeleri kanıt düzeyine göre düzeltildi.
- [Sentez raporu](docs/research/ct-clamp/2026-10-31-synthesis-copilot-claude-independent.md).
- Firmware, K=24.22, sample_duration ve update_interval değişmedi; fiziksel test yapılmadı.

## 2026-10-31 — ESPHome ct_clamp tasarım tarihçesi araştırıldı

- **DURUM:** Kaynak araştırması tamamlandı ve ayrı rapor olarak arşivlendi; firmware/YAML, K katsayısı ve fiziksel deney değişmedi.
- **İLK GELİŞTİRME:** PR #559 (26.05.2019); ilk bileşen commit'i 3089ffa (29.05.2019), author Jesse Hills; Otto Winter co-author/committer ve mimari inceleme katkısı.
- **KÖKEN/AMAÇ:** Jesse, kodun büyük bölümünü OpenEnergyMonitor EMonLib'den aldığını ve CTL-10-CLS ile D1 Mini üzerinde akıllı sayaç karşılaştırması yaptığını açıkladı. SCT013'e özel değil; CT clamp akım ölçümü için.
- **200 ms:** Resmî dokümanda 50 Hz'de 10 tam çevrim. İlk geliştiricinin 10 çevrimi neden seçtiğine ilişkin daha özel gerekçe bulunamadı.
- **60 s:** İlk kodda genel polling_component_schema varsayılanı; ct_clamp'e özel geliştirici gerekçesi bulunamadı. PR test örneklerinde 5 s ve 500 ms de var.
- **last_value filtresi:** PR #2283 / commit c33077bc (12.10.2021); PR gerekçesi yinelenen örnekleri atarak doğruluğu artırmak. ADC sample çağrısını engellemez; aynı değerin istatistik toplamına tekrar eklenmesini önler. Bellek/ADC dönüşüm tasarrufu hedefi belgelenmemiştir.
- **ANA KAYIT:** [Tasarım tarihçesi raporu](docs/research/ct-clamp/2026-10-31-design-history.md); [arşiv indeksi](docs/research/ct-clamp/README.md).
- **BERO ETKİSİ:** 200 ms/2 s/K=24.22 ayarları değiştirilmedi. E10 deneyi planlandığı gibi ayrı gözlem deneyi olarak kalır.

## 2026-10-31 — GitHub Copilot raporu arşivi

- GitHub Copilot tarafından hazırlanmış ct_clamp raporu, özgün metni korunarak TXT biçiminde arşivlendi.
- Üç kaynak ayrı tutuluyor: kullanıcı raporu, Copilot raporu ve bağımsız teknik inceleme. [Arşiv indeksi](docs/research/ct-clamp/README.md).
- Copilot raporundaki ifadeler doğrulanmış bulgu/karar olarak kabul edilmedi.
## 2026-10-31 — ESPHome ct_clamp teknik rapor arşivi

- Kullanıcının sağladığı dört sayfalık raporun metin aktarımı Markdown olarak arşivlendi; bağımsız kaynak kod/BERO Log 63 incelemesi ayrı Markdown raporu olarak oluşturuldu.
- Raporlar ve kapsam farkları: [ct_clamp rapor arşivi](docs/research/ct-clamp/README.md).
- Araştırma kaydıdır; firmware/K değişikliği veya yeni fiziksel test değildir.
## 2026-10-31 — ESPHome ct_clamp teknik rapor arşivi

- Kullanıcının sağladığı DOCX özgün haliyle arşivlendi; bağımsız kaynak kod/BERO Log 63 incelemesi ayrı Markdown raporu olarak oluşturuldu.
- Raporlar ve kapsam farkları: [ct_clamp rapor arşivi](docs/research/ct-clamp/README.md).
- Araştırma kaydıdır; firmware/K değişikliği veya yeni fiziksel test değildir.
## 2026-10-31 — BREAD-TOASTER-001 / Log 63

- Ekmek kızartma makinesi için, önceki TOASTER-001 tost makinesi kaydından ayrı BREAD-TOASTER-001 testi açıldı.
- UNIT 3,30 A kullanıcı bildirimi; PZEM değil ve SCT loguyla tam zaman eşleşmesi belgelenmedi.
- Log 63'te ilk açılış yayını dışlandıktan sonra 50 SCT yayını: ortalama 3,09636 A; medyan 3,094 A; min–maks 3,071–3,144 A; CV %0,433.
- Kararlı Raw AC ortalaması 0,127843 V; SPS ortalaması 18.117.
- UNIT'e göre aritmetik fark −%6,17; eşzamanlılık teyitsiz olduğundan doğruluk sonucu değil.
- K=24.22 ve firmware değişmedi; Python/modelleme yapılmadı; PZEM yok.
- [Test kaydı](test-loads/bread-toaster/README.md); [analiz](logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-analysis.md); [seçilmiş kanıt](logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-evidence.txt).
- Tam ham TXT GitHub'a aktarılmadı; kaynak dosya 32.064 bayt / 449 satır, SHA-256 `cf9254185e591650a06a990e5bc0f567ee499ba4ec541c4bb8748b132513f896`.
- Test açık; tekrarlı log ve eşzamanlı UNIT/PZEM kararlı pencere bekleniyor.

## 2026-10-31 — Toplu yük karşılaştırması

- [Tüm yükler ve karma yükler raporu](test-loads/COMPARATIVE-RESULTS-2026-10-31.md) oluşturuldu.
- Referans farkı ile kendi iç kararlılığı (SD/CV) ayrı gösterildi; eşzamanlılığı doğrulanmayan referans farkları hata sayılmadı.
- 0,30 A altı deneylerde ±%4 kabul/ret uygulanmadı. K=24.22 değişmedi.

## 2026-10-31 — TOASTER-001 / Log 62 ham arşiv ve analiz

- **HEDEF:** Mevcut K=24.22 ile tost makinesinin yüksek akım davranışını karakterize etmek; katsayıyı değiştirmemek.
- **LOG:** 934 satır / 68.572 bayt; kaynak SHA-256 `4790b00e69aaba791339f6d43aa13041efe373c5a87b9ed7fd4c1f481ce551f2`; tam ham log GitHub'a arşivlendi.
- **KARARLI BÖLGE:** İlk 119 yayın, 21:52:30.185–21:56:26.262; ortalama 7,1900 A, medyan 7,188 A, min–maks 7,135–7,264 A, SD 0,0247 A, CV %0,344.
- **REFERANS SINIRI:** UNIT 7,89 A kullanıcı bildirimi; zaman eşleşmesi doğrulanmadığından −%8,87 yalnız aritmetik farktır. PZEM yok.
- **GEÇİŞ:** Son yayın 6,096 A; tek örnek, termostat OFF kanıtı değil.
- **SONUÇ:** K=24.22 sabit; test açık. [Test kaydı](test-loads/toaster/README.md), [analiz](logs/module2/2026-10-31-toaster-001-module2-sct1-log62-analysis.md), [ham log](logs/module2/2026-10-31-toaster-001-module2-sct1-log62-full.txt).

## 2026-10-31 — MIXED-LOAD-57W-15W-001 / Log 59

- **YÜK:** 57 W akkor + 15 W ampul; UNIT 0,303 A'nın test boyunca sabit kaldığı kullanıcı bildirimi.
- **LOG:** 179 SCT-1 yayını; 21:20:18.203–21:26:14.218 (+03:00); kaynak 99.807 bayt / 1.349 satır; SHA-256 `6e7dea5c6c8991a6d4f915ebd6182f3de82b151d5726066700840f21a7d7124a`.
- **SONUÇ:** SCT ortalama 0,329553 A; medyan 0,328 A; CV %4,48. Teste özgü ±%5,6 bandı 0,286032–0,319968 A; 31/179 (%17,32) yayın band içinde, 148/179 (%82,68) üstünde. Ortalama sapma +%8,76.
- **ALT EŞİK:** 0,250 A ve altında yayın yok (%0); tüm yayınlar 0,250 A üzerinde.
- **KARAR:** Bu testte ±%5,6 tolerans hedefi karşılanmadı. 0,250 A alt eşiğinin korunması ayrı ve olumlu gözlemdir. Firmware/K değişmedi; test AÇIK.
- **DOSYALAR:** [Test kaydı](test-loads/mixed-57w-15w/README.md); [analiz](logs/module2/2026-10-31-mixed-load-57w-15w-001-module2-sct1-analysis.md); [tam ham log](logs/module2/2026-10-31-mixed-load-57w-15w-001-module2-sct1-full.txt).

## 2026-10-31 — Modül 2 SCT-1 / 100 W ct_clamp karşılaştırması

- Paylaşılan logda SCT-1 için 200 ms ct_clamp pencereleri ve akım çıktıları gözlendi.
- Son beş kararlı ESP32D1 değeri ortalama 0,589 A (aralık 0,578–0,597 A).
- Kullanıcı aynı test koşulunda PENS değerini 0,427 A bildirdi.
- Fark 0,162 A; ESP32D1, PENS değerinden yaklaşık %37,9 yüksek.
- Tek noktadan katsayı değiştirilmedi; nominal 30 A/V geçici olarak korundu.
- [SCT-1 karşılaştırma kaydı](logs/module2/2026-10-31-sct1-100w-ct-clamp-comparison.txt).
- **T010:** SCT-1 akım çıktısı logla desteklendi; ölçek/kalibrasyon doğrulanmadı. SCT-2 ve SCT-3 bekliyor.

## 2026-10-31 — SCT-1 / 100 W ilk kanal denemesi

- SCT-1 ön panel 1 numaralı girişe bağlandı ve 100 W ampul açıldı (KULLANICI BİLDİRİMİ).
- Ortak bias değeri ESPHome logunda görüldü; sayısal değer bu bildirimde paylaşılmadı.
- U200B+ göstergesinde 0,433 A görüldü (KULLANICI BİLDİRİMİ).
- GPIO32 ADC sayısal log örneği henüz bu kayıtla ilişkilendirilmedi; 0,433 A ESP32 ADC sonucu değildir.
- Ayrıntı: [SCT-1 100 W test kaydı](logs/module2/2026-10-31-sct1-100w-test.txt).
- Sonuç: SCT-1 denemesi kullanıcı bildirimiyle yapıldı; ADC log analizi ve SCT-2/SCT-3 testleri bekliyor. T010 AKTİF.

# BERO — İlerleme Ağacı

## Güncel konum

**FAZ 2 AKTİF — pratik yeniden kurulum ve sistem geliştirme.** Faz 1'de çalışan akım okuma kod yolu bulundu ve kullanıcının dört karşılaştırmasında ±%4 hedefi sağlandı. Faz 2'de sistem modül modül yeniden devreye alınacak; PZEM referanslı veri işleme daha sonraki alt aşamadır.

## İki fazlı proje ağacı

- **FAZ 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak: TAMAMLANDI**
  - Dış kaynaklı ESPHome ct_clamp kodu kullanıldı.
  - 100 W akkor: yaklaşık %0 sapma.
  - 150 W akkor: −%0,2.
  - Kettle düşük/kararlı: +%3,0.
  - Kettle kaynama: −%3,8.
  - Yapılmamış Faz 1 işleri hedefe ulaşıldığı için kapatıldı; kayıtlar arşivde.

- **FAZ 2 — Pratik yeniden kurulum ve sistem geliştirme: AKTİF**
  1. **T009 — Modül/ESP devreye alma üst görevi:** DEVAM EDİYOR.
  2. **T010 — Modül 2 ESP32D1 üçlü SCT + tek ortak bias modülü:** AKTİF.
  3. **T007 — HA → PC veri aktarımı:** PZEM/SCT entity'leri çalışınca.
  4. **T008 — PZEM/SCT kararlı alan eşleştirme/etiketleme:** T007 sonrasında.
  5. **T006 — K=24.22 katsayı/model değerlendirmesi:** T008 sonrasında.

## Faz 2 geliştirme ilkesi

Önce çalışan kod/örnek bulunur, donanım doğrulanır ve tek modül tek işlev şeklinde devreye alınır. Teori ve iç mimari araştırması yalnız somut arıza, uygulama engeli veya karar ihtiyacı varsa derinleştirilir. Başarılı kod ile gerçek log/çıktı ve yorum depoda saklanır. Eski YAML ve araştırmalar tarihsel referans olarak korunur; yeni donanımda test edilmiş sayılmaz.

## Korunan referans

- E00F ESP32D2 YAML ve eski ESP yapılandırmaları kayıtlıdır; yeni kurulumun değiştirilemez şablonu değildir.
- 200 ms pencere, 2 s yayın ve K=24.22 önceki çalışan ölçüm yolunun tarihsel değerleridir.
- Yeni üç SCT + bias Modül 2 bağlantısı ve yeni ESP pin eşlemesi henüz doğrulanmadı.

### 2026-10-31 ilk firmware açılışı

- Dört ADC sensörü (GPIO32/33/34/35) logda başlatıldı; tüm ADC setup durumları OK.
- ESPHome 2026.10.1 firmware'i açıldı; Wi-Fi/API bağlantısı başarılı.
- GPIO35 ortak bias örnekleri 1.643–1.668 V.
- SCT/ampul bağlantısı yoktu; üç SCT kanalı için 100 W test sonucu değildir.
- [İlk açılış log kanıt dökümü](logs/module2/2026-10-31-first-boot-no-load.txt).
- **T010:** Firmware açılışı ve ADC başlatma LOG İLE DESTEKLENDİ; 100 W kanal testleri bekliyor.

## Modül 2 — Üçlü SCT Okuma Modülü

- **ESPHome kimliği:** `esp32d1` / `ESP32D1`; temel başlangıç YAML'ı eklendi.
- **Kutu içeriği:** 3 SCT jack girişi, gömülü ESP32 kartı + GPIO shield, ortak bias mini breadboard.
- **Besleme:** ESP32 harici 5 V DC ile beslenecek; USB portundan PC bağlantısına erişim bulunacak.
- **Bias:** Tek kayıtlı bias devresi; tek ortak bias beslemesi üç SCT girişine dağıtılacak. Ortak bias düğümü tek ADC noktasından izlenecek.
- **ADC hedefi:** 3 bağımsız SCT sinyali + 1 ortak bias izleme = 4 ADC giriş noktası.
- **Bildirilen eşleştirmeler:** 1. dişi yuva sarı → GPIO32; 2. dişi yuva yeşil → GPIO33; 3. dişi yuva mavi → GPIO34; ortak bias turuncu → GPIO35.
- **Açık noktalar:** ESP32 kart/shield modeli, jack tip/ring/sleeve pinout'unun fiziksel teyidi, USB ile harici 5 V'un birlikte kullanım koşulları, bias ADC RAW/voltaj gösterimi.
- **Durum:** Tasarım tanımlandı; fiziksel bağlantı, YAML sensörleri, derleme ve donanım testi yapılmadı.
- **Görev:** [T010](tasks/T010-module2-triple-sct-bringup.md).
- **Karar:** [ADR-015](docs/decisions/ADR-015-module2-esp32d1-triple-sct.md).

## Dosya navigasyonu

| Bilgi | Dosya |
|---|---|
| Güncel durum | [STATUS.md](STATUS.md) |
| Yol haritası | [ROADMAP.md](ROADMAP.md) |
| Görev sırası | [tasks/README.md](tasks/README.md) |
| İlk aktif görev | [T009](tasks/T009-practical-system-bringup.md) |
| HA → PC aktarımı | [T007](tasks/T007-python-architecture.md) |
| Kararlı alan eşleştirme | [T008](tasks/T008-pzem-sct-stable-window-labeling.md) |
| Katsayı/model değerlendirmesi | [T006](tasks/T006-calibration.md) |
| Faz 1 deney geçmişi | [Deney arşivi](experiments/README.md) |
| Yeni Faz 2 kararı | [ADR-014](docs/decisions/ADR-014-phase2-practical-restart.md) |

## HEDEF / LOG / SONUÇ

- **HEDEF:** Faz 2'nin pratik başlangıç yaklaşımını, görev sırasını ve Modül 2'nin mevcut tasarım durumunu tek görünümde göstermek.
- **LOG:** ADR-014, T009 ve ana proje yönergeleri oluşturuldu/güncellendi.
- **SONUÇ:** Faz 1 tamamlandı; Faz 2 pratik yeniden kurulum ve geliştirme olarak aktif. T009 ilk görev. Bu belge donanımın çalıştığına veya firmware'in test edildiğine kanıt değildir.

## 2026-10-31 — FIXED-LOAD-0130A-001 planlandı

- 0,130 A sabit yük gözlem testi açıldı; durum PLANLANDI, ölçüm/log henüz yok.
- 0,130 A kullanıcı bildirimi; ölçüm cihazı ve fiziksel yük kimliği/gücü belirtilmedi.
- Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35; K=24.22 korunacak, yazılımsal sıfır eşiği eklenmeyecek.
- 0,30 A altı düşük akım gözlem alanında ±%4 kabul/ret uygulanmayacak.
- [Test planı](test-loads/fixed-load-0130a/README.md).

## 2026-10-31 — FIXED-LOAD-0130A-001 ilk log analizi

- SCT-1 logu incelendi: n=556; ortalama 0,203637 A; medyan 0,203 A; min–maks 0,157–0,291 A; SD 0,017971 A.
- 0,130 A hedefi UNIT/PZEM referansı olarak doğrulanmadı; fiziksel yük kimliği de bilinmiyor. Sapma hesabı yapılmadı.
- Durum: log analizi yapıldı; test referans ve kurulum teyidi beklediği için açık.
- [Test kaydı](test-loads/fixed-load-0130a/README.md); [analiz](logs/module2/2026-10-31-fixed-load-0130a-001-sct1-analysis.md).

## 2026-10-31 — LOAD-42W-001 açıldı

- 42 W ampul düşük akım gözlem testi açıldı.
- UNIT 0,174 A kullanıcı bildirimi; kararlılık ve ölçüm zamanı henüz teyit edilmedi.
- Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35; K=24.22 ve mevcut firmware korunacak.
- 0,30 A altı gözlem bölgesi; ±%4 kabul/ret uygulanmaz.
- SCT logu ve fiziksel ampul ayrıntıları bekleniyor.
- [Test kaydı](test-loads/42w-bulb/README.md).

## 2026-10-31 — LOAD-42W-001 / Log 57 gözlemi

- 42 W test yükü altında 96 SCT-1 yayını analiz edildi (21:09:28–21:12:38).
- SCT ortalaması 0,252438 A; medyan 0,251 A; aralık 0,221–0,295 A; CV %4,37.
- Raw AC ortalaması 0,0104248 V; ortak bias 1,663469 V.
- UNIT 0,174 A ile aynı zamanlı kararlı pencere doğrulanmadığından +%45,08 fark yalnız betimleyici; doğruluk sonucu değil.
- Test düşük akım gözlemi olarak açık. [Test kaydı](test-loads/42w-bulb/README.md); [analiz](logs/module2/2026-10-31-load-42w-001-log57-analysis.md).


## 2026-10-31 — LOAD-57W-001 / 57 W akkor testi açıldı

- 57 W akkor ampul test yükü ve UNIT 0,244 A başlangıç bildirimi kaydedildi.
- UNIT değerinin SCT ile aynı kararlı zaman penceresine ait olduğu henüz doğrulanmadı; PZEM verisi verilmedi.
- 0,30 A altı gözlem alanı; ±%4 kabul/ret yok.
- Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35; K=24.22 ve firmware korunacak.
- [Test kaydı](test-loads/57w-incandescent/README.md).


## 2026-10-31 — LOAD-57W-001 / Log 58

- 57 W akkor ampul testinde ESP32D1 Modül 2 / SCT-1 için 116 yayın analiz edildi.
- SCT ortalaması 0,304207 A; medyan 0,303 A; aralık 0,284–0,348 A; CV %3,00.
- Raw AC ortalaması 0,012562 V; ortak bias GPIO35 ortalaması 1,663073 V; GPIO32 ADC ortalaması 1,660694 V.
- UNIT 0,244 A başlangıç bildirimiyle aritmetik fark +%24,67; aynı zaman penceresi doğrulanmadığından doğruluk sonucu değildir. PZEM verisi yok.
- Test açık; firmware/K=24.22 değişmedi. [Test kaydı](test-loads/57w-incandescent/README.md); [analiz](logs/module2/2026-10-31-load-57w-001-module2-sct1-analysis.md); [tam log](logs/module2/2026-10-31-load-57w-001-module2-sct1-full.txt).

## 2026-10-31 — MIXED-LOAD-57W-15W-001 açıldı

- 57 W akkor + 15 W ampul karma yük testi açıldı; 15 W ampul tipi henüz belirtilmedi.
- Nominal etiket güçlerinin toplamı 72 W (hesap); gerçek güç ölçümü değildir.
- UNIT 0,303 A kullanıcı bildirimi; SCT ile zaman örtüşmesi/kararlılık doğrulanmadı.
- Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35; K=24.22 ve firmware kilitli.
- Eşleşmiş kararlı pencere elde edilirse ±%4 kıyası yapılabilir; test açık ve log bekliyor.
- Önceki LOAD-57W-001 bağımsız olarak açık kalır.
- [Test kaydı](test-loads/mixed-57w-15w/README.md).


## 2026-10-31 — IRON-001 kapatıldı; TOASTER-001 açıldı

- IRON-001 iki mevcut logla sınırlı gözlem raporu olarak kapatıldı; tüm termostat çevrimlerinin doğrulandığı iddia edilmez.
- Açık çevrimler: 9,2852 A (n=5) ve 9,3605 A (n=4). UNIT 10,16 A bildirimine göre aritmetik fark −%8,61 / −%7,87; eşzamanlılık teyitsiz.
- Kapalı/düşük akım: 40 yayın; 27 sıfır, 13 adet 0,011–0,092 A. Yaklaşık 104 s kayıt boşluğu süre hesabına katılmadı.
- TOASTER-001 tost makinesi testi AÇIK; fiziksel ölçüm bekleniyor. Güç ve referans cihazı bilinmiyor; Modül 2/K=24.22 korunacak.
- [IRON-001 raporu](test-loads/iron/README.md); [TOASTER-001 planı](test-loads/toaster/README.md).


## 2026-10-31 — TOASTER-001 / Log 62 ön değerlendirmesi

- İlk 119 SCT yayını yaklaşık 236 s boyunca 7,1900 A ortalama ve %0,344 CV ile kararlı.
- UNIT 7,89 A'ya göre aritmetik fark −%8,87; zaman eşleşmesi teyitsiz, doğruluk sonucu değil.
- Son tek yayın 6,096 A olarak ayrı geçiş verisi tutuldu.
- K=24.22 değişmedi; test açık.
- [TOASTER-001 raporu](test-loads/toaster/README.md).

## 2026-10-31 — E10 ct_clamp pencere süresi deneyi planlandı

- Faz 2 / T010 altında E10 gözlem protokolü açıldı.
- Tek değişken sample_duration: 200 → 500 → 1000 → 200 ms geri dönüş.
- update_interval: 2s, K=24.22, ESPHome 2026.10.1, SCT-1 GPIO32 ve ortak bias GPIO35 sabit.
- Deney yükü BREAD-TOASTER-001; Log 63 tarihsel 200 ms tabanı.
- Kullanıcı raporu, Copilot raporu ve bağımsız teknik inceleme protokolde ayrı ayrı referanslandı; simülasyonlar ölçüm sayılmadı.
- **Durum:** Yalnız planlandı. YAML/OTA/fiziksel ölçüm/log yok.
- [E10 protokolü](experiments/E10-ct-clamp-window-duration/README.md); [sonuç defteri](experiments/E10-ct-clamp-window-duration/results.md).


## 2026-11-01 — Modül 2 üretim kontrolleri için durum düzeltmesi

- Kullanıcı teyidi: modül ilk üretildiğinde üç SCT kanalının her birinde okuma kontrolü yapıldı.
- Kullanıcı teyidi: üç kanala ayrı bias değil, tek ortak bias noktası kullanıldı; üretim sırasında ölçüldü ve görseli daha önce paylaşıldı.
- Modül 2 ile test yükleri çalıştırıldı; gerçek cihaz logları/analizleri ve derleme-fiziksel çalışma kayıtları depoda mevcut.
- Bu kontroller yeniden yapılacak iş değildir. Önceki “kanal/bias/cihaz çıktısı bekliyor” anlatımı güncel kabul edilmeyecek.
- E10 200→500→1000→200 ms deneyi ayrı olarak PLANLANDI; henüz uygulanmadı.
- firmware/esp32d1.yaml mevcut hâli tek ct_clamp kanalı GPIO32 + ortak bias GPIO35 gösterir; fiziksel ilk kanal kontrolüyle firmware'in üç kanalı aynı anda ölçtüğü iddiası birbirinden ayrıdır.


## 2026-11-01 — Modül 2: taşınabilir tek kablolu ortak bias tasarımı

- Modül 2'nin sahibi ve imalatçısı kullanıcıdır; imalat ve test anlatımları birinci el proje kaynağı olarak ele alınır.
- Taşınabilirlik için tek bias devresi ve tek ortak bias kablosu kullanılmıştır; bu hat üç SCT kanalına ortak bias dağıtır.
- Üç SCT sinyal bağlantısı bağımsızdır; bias üç ayrı devre değildir. Breadboard bias görüntüsü daha önce paylaşılmış, ortak bias üretim sırasında ölçülmüştür.
- İlk üretimde üç SCT kanalının ayrı ayrı okuma kontrolü yapılmış; Modül 2 ile yük testleri çalıştırılmıştır. Mevcut cihaz logları, derleme ve fiziksel çalışma kayıtları depoda bulunur.
- Bunlar yeniden yapılacak işler değildir. E10 (200 → 500 → 1000 → 200 ms) hâlâ ayrı PLANLANDI deneyidir.
- Mevcut firmware YAML'ın tek SCT-1 kanalını göstermesi, fiziksel imalat ve ilk kanal kontrollerinin yapılmadığı anlamına gelmez; kod/konfigürasyon kapsamı ayrı bir tutarlılık konusudur.


## 2026-11-01 — LOAD-15W-004 / 15 W çok turlu uzun gözlem açıldı

- LOAD-15W-003'ten ayrı yeni oturum açıldı; önceki kayıt ve YAML üzerine yazılmadı.
- Faz UNIT 0,057 A ve nötr UNIT 0,059 A kullanıcı bildirimi olarak kaydedildi; zaman eşleşmesi teyitsiz.
- İlk yaklaşık 96 s log ön gözlemi: SCT1 0,18552 A, SCT2 0,24171 A, SCT3 0,07585 A; SCT3'te 11/48 sıfır; bias ortalama 1,66196 V.
- [LOAD-15W-004 deney kaydı](test-loads/15w-2t-3t-4t/LOAD-15W-004.md); [YAML snapshot](firmware/archive/LOAD-15W-004-2026-11-01-esp32d1-15w-2t-3t-4t-unit.yaml).
- AÇIK; uzun test, derleme/OTA ve HA Recorder doğrulaması yok. 0,30 A altında ±%4 kabul/ret uygulanmaz.


## 2026-11-01 — Kararlı alan eğitimi ana çerçevesi (ADR-019)

- Modül 2: SCT ölçümleri ile UDP'den alınan paket/zaman/SSR ON-OFF olayları HA'ya **ayrı kayıt akışları** olarak aktarılır.
- Modül 3: paket/zaman/SSR ON-OFF bilgisini UDP ile yayınlar; PZEM ölçümleri ve aradaki olay/yayın bilgileri HA'ya **ayrı kayıt akışları** olarak aktarılır.
- Python, SCT + PZEM + olay akışlarını sonradan kaynak zaman ve varsa BOOT_ID/EVENT_ID ile ilişkilendirir; olay çizgisinden yük durumunu çıkarır.
- SCT ve PZEM kararlılığı ayrı hesaplanır; zaman bakımından örtüşen kararlı pencereler eşleştirilir. PZEM eşleşen SCT penceresinin proje referans etiketidir.
- ESP/HA tarafında ölçüm ve olayın birebir eşleştirilmesi yoktur. Zaman toleransı/eşik/pencere süresi gerçek veri görülünce belirlenir.
- [ADR-019](docs/decisions/ADR-019-module2-module3-independent-event-streams.md); [Python veri hattı mimarisi](docs/architecture/python-program-architecture.md).
- Bu kayıt mimari karardır; firmware, UDP paketi veya fiziksel test değişikliği değildir.


## 2026-11-05 — E12 SCT kararlılık ve tepki süresi araştırması

- E12 planlandı: SCT1 kararlı alan tespiti; PZEM ve SCT kararlı alanlarının bağımsız belirlenip zaman kesişimiyle eşleştirilmesi; SCT tepki/yerleşme süresi ve daha kısa ölçüm penceresi araştırması.
- İlk gözlem adayı 20:07–20:37 100 W akkor oturumudur; 20:12 kablo değişikliği öncesi/sonrası ayrı incelenecek.
- İlk analizde 200 ms sample_duration, 2 s update_interval ve K=24.22 referans alınır.
- Deney sırası sabit değildir; kullanıcı ve asistan deneyleri ihtiyaca göre öne alabilir. Faz 2 görev bağımlılıkları korunur.
- **Durum:** Protokol kaydedildi; tam log analizi ve Python uygulaması beklemede. [E12](experiments/E12-sct-stability-window-and-response/README.md).


## 2026-11-05 — E11 sonucu ve E12 ilk veri gözlemi

- E11 yüksüz uzun gözlem analiz edildi: PZEM 0.0 A; SCT1/2/3 medyanları yaklaşık 0.163/0.170/0.157 A; olay görünürlüğü 85/92 (%92.4), kesin UDP kaybı hükmü verilmedi.
- E12 ilk 100 W CSV ön karşılaştırmasında 35 ON penceresi incelendi; SCT1/PZEM merkez farkı yaklaşık %3.34, 24/35 pencere ±%4 içinde. Bu ilk ön elemedir; bağımsız kararlılık algoritması ve Python eğitimi henüz yoktur.
- Kalibrasyon referansı yalnızca ON içindeki bağımsız SCT/PZEM kararlı alanlarının örtüşmesidir. Geçiş/interpolasyon değerleri katsayı öğrenimine katılmaz; ham kayıt korunur.
- K=24.22 değiştirilmedi. Hafta sonu farklı sabit yükler ve ilk Python veri hattı önceliklidir; canlı makine doğrulaması sonraki aşamadır.
- Ayrıntı: [E11](experiments/E11-idle-dual-module-observation/README.md), [E12](experiments/E12-sct-stability-window-and-response/README.md).


## 2026-11-06 — Eğitim yaklaşımı ve sonraki çalışma

- Kullanıcı, genel akım okuma aşamasına ulaşıldığını ve eğitim için kullanılabilecek kararlılıkta alanları hedeflediğimizi teyit etti; sayısal kararlılık algoritması henüz tamamlanmış değildir.
- Kullanıcı, eğitim felsefesinin ve istenen veri yaklaşımının bugün ekran görüntüsüyle de sabitlendiğini bildirdi.
- Yarın ilk iş, eğitim için kullanılacak SCT ve PZEM verisini gerçek kayıtlar üzerinden seçmek ve sabitlemek; kararlı alanların uygunluğunu değerlendirmektir.
- PY-01 arşiv/oturum tasarımı çalışan örnek üzerinden denenecek; henüz kesinleştirilmedi.
- Python eğitim/etiketleme uygulaması veya yeni model çıktısı bu oturumda üretilmedi. T007 → T008 → T006 sırası korunur.


## 2026-11-06 — E16: yüksüz/düşük akım ON/OFF davranışı planlandı

- HA ekran görüntüsünde PZEM 230,2 V / 0,000 A iken CH1 SCT akımı 0,204 A ve Raw AC göstergesi 0,00842 görünüyordu; grafikte SCT yaklaşık 0,18–0,30 A çevresinde basamaklıydı. Tek ekran görüntüsü sonuç değildir.
- Kullanıcının 18 W'ta SCT'nin genlik yerine aç/kapa değişimini algıladığı gözlemi doğrulanmamış hipotez olarak ayrı tutuldu.
- E16 gece boyu PZEM V/A, SCT CH1 akım/Raw AC ve iki modülün ON/OFF olay kayıtlarını toplama planıdır. Sabah HA History CSV'si incelenecek.
- Fiziksel yük koşulu ayrıca kaydedilecek; eğitim/kalibrasyon etiketi bu deneyden otomatik üretilmeyecek.
- Ayrıntı: [E16](experiments/E16-sct-on-off-response-idle-low-current/README.md). Durum PLANLANDI; veri ve analiz bekleniyor.
