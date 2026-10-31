# ct_clamp / BERO — Hipotez sicili ve deney önceliği

**Tarih:** 2026-10-31  
**Kapsam:** Bu sohbet boyunca bir araya getirilen kaynak kod incelemesi, ESPHome tarihçesi, BERO saha logları ve henüz sınanmamış açıklamalar.  
**Durum:** Araştırma sentezi ve deney planlama kaydıdır; yeni fiziksel deney değildir.

## 1. Amaç

Bu kayıt, 19 teknik iddiayı kanıt seviyelerine ayırır. Amaç tüm iddiaları aynı kesinlikte sunmak değil; kaynak koduyla bilinenleri, BERO loglarının desteklediği saha gözlemlerini ve henüz deney gerektiren açıklamaları birbirinden ayırarak araştırma aşamasından veri üreten deneylere geçmektir.

Kanıt sınıfları:
- **KANITLI:** Kaynak kodu, resmî doküman veya birincil tarihsel kayıt doğrudan destekler. İddianın kapsamı yine dar tutulur.
- **GÜÇLÜ SAHA DESTEĞİ:** BERO logları/tecrübeleri destekler; evrensel sonuç veya tüm aralıkta doğrulama değildir.
- **GÜÇLÜ HİPOTEZ:** Teknik olarak makul ve bazı gözlemlerle uyumlu; kontrollü deneyle ayrıştırılmamıştır.
- **ARAŞTIRILACAK:** Sonuç bilinmiyor; deney veya eşleşmiş veri gerekir.
- **KANIT YOK:** Şu an iddiayı doğrulayacak yeterli veri yok.

## 2. On dokuz iddianın sınıflandırılması

### A. Kaynak kodu / tarihçe ile kanıtlı (H1–H5)

| ID | İddia | Değerlendirme ve sınır |
|---|---|---|
| H1 | ct_clamp RMS-türevi akım değeri üretir; AC bileşen hesabının temeli E[x²] − E[x]² ve karekök yaklaşımıdır. | **KANITLI.** Kaynak kod ve PR #1906 açıklaması destekler. Sensör katsayısı/kurulum ölçeği ayrıca önemlidir. |
| H2 | Sabit DC bias, varyans hesabında matematiksel olarak ayrılır. | **KANITLI, koşullu.** Sabit offset E[x²] − E[x]² ile iptal olur. Zamanla değişen bias, gürültü ve pencere içi kayma AC varyansına katkı verebilir; gerçek devrede her bias etkisi yok olmaz. |
| H3 | ct_clamp enerji analizörü değil, CT tabanlı AC akım sensörüdür. | **KANITLI.** Wh/kWh, aktif güç, PF, harmonik veya güç kalitesi hesabı yapmaz. |
| H4 | 200 ms, 50 Hz şebekede nominal 10 çevrimdir. | **KANITLI.** Bu aritmetik/dokümantasyon bilgisidir; 200 ms'nin BERO için en iyi pencere olduğunu kanıtlamaz. |
| H5 | last_value karşılaştırmasından önce source_->sample() çağrılır. | **KANITLI.** Bu nedenle filtre ADC örnekleme çağrısını engellemez. Tek başına filtrelemenin istatistiksel/ölçümsel yan etkisinin sıfır olduğunu kanıtlamaz. |

### B. BERO saha verisiyle güçlü desteklenenler (H6–H8)

| ID | İddia | Değerlendirme ve sınır |
|---|---|---|
| H6 | SCT013 + ct_clamp + ESP32 zinciri pratikte akım çıktısı üretebiliyor. | **GÜÇLÜ SAHA DESTEĞİ.** 100 W, 150 W, kettle, fan, tost/ekmek kızartma makinesi ve ütü benzeri yük kayıtları işlevsel çıktı gösterir. Her kanal, yük ve akım aralığı doğrulanmış değildir. |
| H7 | 0,3 A üzerindeki bazı test koşulları daha kullanılabilir/kararlı sonuç vermiştir. | **GÜÇLÜ SAHA DESTEĞİ.** Bu, “0,3 A üzerindeki her yük güvenilirdir” veya fiziksel alt sınırın 0,3 A olduğu anlamına gelmez. |
| H8 | 3–10 A bölgesinde bazı yüklerde tekrarlanabilir/kararlı SCT davranışı görülmüştür. | **GÜÇLÜ SAHA DESTEĞİ.** Tost, ekmek kızartma makinesi ve ütü kayıtları gözlem sağlar; sistematik, eşzamanlı PZEM kalibrasyonu değildir. |

### C. Kontrollü deney gerektiren güçlü hipotezler (H9–H11)

| ID | İddia | Değerlendirme ve sınır |
|---|---|---|
| H9 | Çoklu ct_clamp kanalı ölçüm kalitesini düşürebilir. | **GÜÇLÜ HİPOTEZ.** ESPHome PR #1915 çoklu CT örneklemesinde eşgüdüm/mutex ihtiyacını belgelemiştir; BERO'daki etkinin büyüklüğü ve nedeni tek/üç kanal kontrollü kıyasıyla ölçülmelidir. |
| H10 | last_value tekrar filtresi ESP32 dahili ADC'sinde beklenmeyen yanlılık oluşturabilir. | **GÜÇLÜ HİPOTEZ.** Filtrenin kökeni ADS1115'in istenen hızdan yavaş örnek üretmesi bağlamındadır; BERO ESP32'de etkisi ölçülmedi. Filtreyi doğrudan kaldırmak için kanıt yoktur. |
| H11 | Düşük akım sorunlarının önemli bir bölümü sinyal-gürültü oranı (SNR) ile ilişkili olabilir. | **GÜÇLÜ HİPOTEZ.** CT çıkış genliği, ADC davranışı ve bias etkisiyle uyumludur; ancak SNR'nin tek/ana neden olduğu gösterilmedi. |

### D. Veriyle cevaplanacak araştırma soruları (H12–H15)

| ID | Soru | Durum |
|---|---|---|
| H12 | 500 ms pencere 200 ms'den daha iyi sonuç verir mi? | **ARAŞTIRILACAK.** E10-B aşaması. |
| H13 | 1000 ms pencere 200/500 ms'den daha iyi sonuç verir mi? | **ARAŞTIRILACAK.** E10-C aşaması. Daha düşük dağılım tek başına daha doğru değer demek değildir. |
| H14 | K tek bir katsayı olarak tüm koşullarda kullanılabilir mi? | **ARAŞTIRILACAK.** Eşleşmiş SCT/PZEM kararlı pencereleri ve farklı yük aralıkları gerekir. |
| H15 | K akım aralığına, kanala veya yük koşuluna göre değişiyor mu? | **ARAŞTIRILACAK.** H14 ile bağlantılı; kanal ve koşul etkileri ayrıştırılmalı. |

### E. Şu an kanıtlanmamış iddialar (H16–H19)

| ID | İddia | Değerlendirme |
|---|---|---|
| H16 | 200 ms, BERO için en iyi RMS penceresidir. | **KANIT YOK.** Tarihsel varsayılan olması optimum olduğunu göstermez. |
| H17 | SCT/ölçüm zincirinin fiziksel alt akım sınırı 0,4 A'dır. | **KANIT YOK.** 0,4 A civarındaki saha güvenilirliği gözlemi fiziksel sensör sınırı değildir. |
| H18 | last_value filtresi birbirinden bağımsız fiziksel örnekleri korur. | **KANIT YOK.** Aynı sayısal ADC kodunun tekrarı, yeni dönüşüm mü yoksa aynı dönüşüm mü olduğunu tek başına açıklamaz. |
| H19 | Üç kanal sorunlarının kesin nedeni SPS düşüşüdür. | **KANIT YOK.** Çoklu kanal, kaynak örnekleme, mutex ve yayın zamanlaması etkileri kontrollü karşılaştırılmadan neden atanamaz. |

## 3. Kritik teknik ayrımlar

1. **ADC çağrısı ≠ kabul edilmiş örnek:** last_value filtresi source_->sample() çağrısından sonra çalışır. Logdaki örnek sayısı fiziksel ADC dönüşüm sayısı olarak adlandırılmayacaktır.
2. **Sabit bias ≠ değişken bias:** Varyans hesabı sabit DC merkezini ayırır; bias hareketi ve gürültü pencere varyansına girebilir.
3. **Kararlılık ≠ doğruluk:** Düşük CV, PZEM'e yakınlık veya kalibrasyon kanıtı değildir.
4. **UNIT ≠ PZEM:** Kullanıcı tarafından bildirilen UNIT değerleri PZEM referansı gibi etiketlenmez. Aynı zaman penceresi eşleşmesi yoksa fark yalnız aritmetik/betimleyici farktır.
5. **Saha aralığı ≠ garanti:** Bazı yüklerde 0,3 A üstü veya 3–10 A civarında çalışan örnekler, tüm yüklerde aynı performansı garanti etmez.
6. **200 ms ≠ 2 s:** sample_duration ölçüm penceresidir; update_interval yayın/yeniden ölçüm periyodudur.

## 4. Deney ve uygulama önceliği

Faz 2 görev sırası korunur: T009 → T010 → T007 → T008 → T006. Aşağıdaki sıra T010 altında ölçüm sorularını yürütme önerisidir; ana görev sırasını değiştirmez.

1. **T010 kanal davranışı:** Önce SCT-1, SCT-2, SCT-3 kanallarını aynı tekil yük ve aynı kurulum koşulunda ayrı ayrı gözle. Ardından gerekiyorsa tek kanal ve üç kanalın aynı anda çalıştığı koşulları karşılaştır. Her kanal için GPIO/bias, kabul edilmiş örnek sayısı/SPS, Raw AC, akım dağılımı ve log sürekliliği kaydedilsin. H9 ve H19'u ayrıştır.
2. **E10 pencere deneyi:** Mevcut protokol aynen korunsun: 200 → 500 → 1000 → 200 ms geri dönüş. Tek değişken sample_duration; update_interval=2s, K=24.22, SCT-1 GPIO32, bias GPIO35 ve aynı BREAD-TOASTER-001 yükü sabit. Bu deney H12/H13/H16'ya veri sağlar; kalibrasyon değildir.
3. **last_value etkisi:** E10'dan ayrı deney tasarla. Önce mevcut ESPHome sürümünde ilgili kaynak davranışını ve konfigürasyonu doğrula; değişiklik yapılacaksa tek değişkenli, geri dönüşlü A/B testi ve aynı giriş koşulu gerekir. H10/H18 için kanıt olmadan filtreyi kaldırma.
4. **T007:** Modüller ve PZEM düğümü çalışır veri ürettiğinde HA geçmişini PC'ye aktar. Kaynak timestamp, entity_id, birim, timezone ve ham durum korunmalı.
5. **T008:** PZEM ve SCT kararlılığını ayrı belirle; yalnız zaman bakımından örtüşen kararlı pencereleri eşleştir ve PZEM ile etiketle.
6. **T006:** Eşleşmiş veri yeterli olmadan K=24.22'yi değiştirme. H14/H15 ancak farklı yük/akım aralıklarında ve mümkünse tekrarlarla eşleşmiş pencerelerden incelensin.

## 5. Şu anki somut veri ve açık işler

- BREAD-TOASTER-001 Log 63: 200 ms koşulunda ilk açılış yayını hariç 50 yayın; SCT akım ortalaması 3,09636 A, medyan 3,094 A, CV %0,433; Raw AC ortalaması 0,127843 V; kabul edilmiş SPS ortalaması yaklaşık 18.117. UNIT 3,30 A kullanıcı bildirimidir; PZEM değildir ve zaman eşleşmesi yoktur.
- Log 63, 200 ms için tarihsel tabandır; E10-A aşamasının yerine geçmez.
- E10 henüz **PLANLANDI** durumundadır. YAML değişikliği, derleme, OTA, fiziksel aşamalar ve yeni log yoktur.
- K=24.22 ve firmware bu sohbetin araştırması nedeniyle değiştirilmemiştir.
- H9/H19 için T010 kanal karşılaştırması; H12/H13/H16 için E10; H10/H18 için ayrı last_value deneyi; H14/H15 için eşleşmiş PZEM/SCT verisi gerekir.

## 6. Bu kaydın sınırı

Bu belge, sohbet içindeki hipotezlerin düzenlenmiş sicilidir. H1–H5 dışındaki tüm iddiaları kaynak kod kesinliğiyle sunmaz. H6–H8 saha gözlemidir; H9–H11 deney bekleyen hipotezdir; H12–H15 açık araştırma sorusudur; H16–H19 şu an kanıtsızdır. Yeni fiziksel test, firmware değişikliği, OTA veya kalibrasyon bu kayıtla yapılmış sayılmaz.
