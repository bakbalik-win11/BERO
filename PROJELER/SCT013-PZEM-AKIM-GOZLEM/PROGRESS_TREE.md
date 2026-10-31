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
