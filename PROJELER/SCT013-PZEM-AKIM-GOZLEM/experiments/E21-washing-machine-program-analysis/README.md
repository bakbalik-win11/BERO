## 8. Kayıt kimliği ve program sınıflandırma standardı

Kayıt kimliği ile program sınıfı birbirinden ayrılır:

- **RECORD_ID:** Her fiziksel çekime özgüdür. Biçim: `WM-YYYYMMDD-NN`. Örnek: `WM-20261114-01`.
- **PROGRAM_ID:** Aynı program adı ve aynı anlamlı seçenek kombinasyonuyla yapılan tekrar kayıtlarını gruplamak için kalıcı sınıf kimliğidir. Biçim: `WMP-NNN` (ör. `WMP-001`). Gerçek panel program adı ve ayarlar öğrenilmeden atanmaz.
- **PROGRAM_NAME:** Makine panelinde görünen tam program adı; kullanıcıdan aynen alınır.
- **PROGRAM_TAG:** “UZUN” gibi kısa, kolay okunur açıklama etiketi olabilir. Paneldeki gerçek program adı veya PROGRAM_ID yerine geçmez.

Sıcaklık, sıkma devri veya ek seçenekler değiştiğinde aynı PROGRAM_ID altında birleştirme otomatik yapılmaz. Önce aynı sınıfın varyantı mı, ayrı program sınıfı mı olduğu kararlaştırılır. Böylece ileride eğitimde kayıt çekimleri (RECORD_ID) ile öğrenilecek program sınıfları (PROGRAM_ID) karıştırılmaz.

Dosya standardı:
- `WM-YYYYMMDD-NN_raw-ha-history.csv`
- `WM-YYYYMMDD-NN_metadata.md`
- `WM-YYYYMMDD-NN_analysis.md`
- `WM-YYYYMMDD-NN_segments.csv`

Ham HA CSV değişmeden saklanır; analiz ve segmentasyon ayrı türetilmiş çıktılardır.

### 2026-11-14 ilk tam program kaydı
- **RECORD_ID:** `WM-20261114-01`
- **PROGRAM_TAG:** geçici olarak `UZUN` (kullanıcının tanımı)
- **PROGRAM_NAME / PROGRAM_ID:** makine paneli ve ayarlar öğrenilince doldurulacak.
- **Durum:** PLANLANDI; makinenin başlatılacağı haber bekleniyor.
- Kayıt şablonu: [WM-20261114-01](../../logs/washing-machine/WM-20261114-01/README.md).


# E21 — Çamaşır makinesi program davranışı analizi

- **Durum:** ÖN GÖZLEM KAYITLARI MEVCUT / VERİ TOPLAMA VE ANALİZ DEVAM EDECEK
- **Açılış tarihi:** 2026-11-13
- **Hedef:** Çamaşır makinesinin kısa ve uzun programlarını baştan sona akım zaman serisiyle kaydetmek; ilk görsel ve kayıt gözlemlerini korumak; daha fazla tam program kaydı biriktirerek Python ile zaman serisi korelasyonu ve uygun diğer analizleri daha sonra yapmak. İlk gözlemler nihai evre sınıflandırması değildir.
- **İlerideki yön:** İlk akım kaydından sonra farklı sensörler sisteme aşamalı olarak eklenip birlikte değerlendirilebilir. Sensör türleri ve bağlantıları henüz belirlenmedi; bu aşamada varsayılmayacak.
- **Önceki hedef:** PZEM kararlı-alan eşleştirmesiyle eğitim/kalibrasyon verisi üretme iş akışı ADR-026 ile kapatıldı. Bu işin eski kayıtları silinmez.

## 1. İlk testin amacı ve sınırı

İlk kayıtlar kısa ve uzun programların **tam program çekimleridir**. Amaç, programların baştan sona akım davranışını gözlemek ve ilerideki karşılaştırma/analizler için başlangıç verisi oluşturmaktır. Bu aşamada tüm evreleri kesin tanımlamak, makine durumlarını sınıflandırmak veya eğitim modeli oluşturmak hedeflenmez.

İlk kayıt sonrasında hangi ek sensörlerin anlamlı olacağı değerlendirilecektir. Farklı sensörlerle kombinasyon, ayrı bir sonraki aşamadır; ilk testin ön koşulu değildir.

Bu çalışma enerji tüketimi veya güç kalitesi analizi değildir. SCT zincirinin ürettiği akım gözlemi, cihazın çalışma karakterini incelemek için kullanılacaktır.

## 2. İlk kayıt kapsamı

İlk veri grubunda iki ayrı tam program kaydı bulunur: kısa program ve uzun program (dosya adında Pamuklu 60° olarak belirtilmiştir). Program adı ve makine panelindeki seçenekler kullanıcı tarafından bildirilecektir; makine modeli, program, sıcaklık, sıkma devri, ek seçenekler veya çamaşır yükü varsayılmaz.

Kayıt öncesi not edilecekler:
- Makine marka/modeli (biliniyorsa).
- Seçilen programın paneldeki tam adı.
- Sıcaklık, sıkma devri ve ek seçenekler.
- Yaklaşık çamaşır yükü ve yükün niteliği (kullanıcı bildirimi).
- Programın başlatıldığı saat ve programın bittiği saat.
- Kullanıcının gözlemlediği olaylar (su alma, tambur hareketi, bekleme, boşaltma, sıkma vb.); yalnız gerçekten gözlenenler.

## 3. Ölçüm ve veri ilkeleri

- Aynı SCT-013 + ADS1115 + ESP32D2 ölçüm zinciri kullanılacak; gerçek firmware/YAML sürümü ve çalışan ayarlar kayıt altına alınacak.
- Kullanıcı ayrıca onaylamadıkça mevcut gain, SPS, ct_clamp sample_duration, update_interval, filtre ve katsayı değiştirilmeyecek.
- Ham Home Assistant History CSV değişmeden korunacak; analiz çıktıları ayrı dosyalardır.
- Kaynak timestamp, timezone, entity_id, birim ve ham state korunur.
- PZEM verisi mevcutsa yardımcı karşılaştırma/bağlam olarak saklanabilir. Yeni hedefte PZEM kararlı alan eşleştirmesi veya PZEM etiketli eğitim verisi zorunlu değildir.
- 2 saniyelik yayın aralığı kullanılıyorsa rapor evre geçişlerinin bu zaman çözünürlüğüyle gözlendiğini açıkça belirtir; alt-saniye olay süresi iddia edilmez.
- Makinenin program evreleri yalnız akım değerinden kesin adlandırılmaz. Akım örüntüsü önce tarafsız biçimde bölümlenir; isimler panel bilgisi ve kullanıcı gözlemiyle ilişkilendirilir.
- OFF/yüksüz alanlar eğitim etiketi değildir; ancak tam program davranışını anlamak için ham zaman serisinde korunur.

## 4. İlk görsel ve kayıt gözlemleri

Kullanıcının daha önce paylaştığı görsel ve sohbet üzerinden yapılan ilk nitel gözlemde program davranışı içinde aşağıdaki örüntülerin ayırt edilebilir olduğu değerlendirilmiştir:
- Isıtma davranışı.
- Tamburun sağa-sola dönüşleri.
- Sıkma davranışı.

Bunlar görsel/ilk gözlem düzeyinde yorumlardır; kesin evre sınırları, süreler veya makinenin iç kontrol mantığı olarak kabul edilmez. İlk gözlemin kayda geçirilmesi, çalışmanın hiç yapılmamış gibi görünmesini önler; ancak Python analizi veya evre sınıflandırması tamamlandığı anlamına gelmez.

## 5. İlk kayıtların sonraki incelemesi

İki tam program kaydı için ileride:
1. CSV bütünlüğü, zaman aralığı ve akım entity'si doğrulanır.
2. Program boyunca akımın genel grafiği çıkarılır.
3. Belirgin yükselme, düşme, bekleme ve tekrar eden hareketler kabaca işaretlenir.
4. Programın toplam kayıt süresi ve dikkat çeken zaman aralıkları not edilir.
5. Makinenin iç işlemleri hakkında kesin olmayan yorumlar hipotez olarak bırakılır.

Bu aşamada ayrıntılı evre sınıflandırması, tekrar testi veya ek sensör entegrasyonu yapılması beklenmez.

## 6. Sonraki aşamalar

İlk kayıt değerlendirildikten sonra kullanıcıyla birlikte uygun farklı sensörler seçilecek ve aşamalı biçimde sisteme eklenerek kombinasyonları incelenecektir. Sensör seçimi, bağlantı ve kayıt yöntemi ayrı karar/protokolle belirlenecektir. Aynı programı tekrar etme veya başka programları kaydetme ihtiyacı ilk kaba testin sonucuna göre kararlaştırılır. Tek programdan bütün makine davranışı hakkında genelleme yapılmaz.

## 7. Güvenlik ve sınırlar

- ADS1115 A0/A1 ortak-mod ve GND–VDD giriş sınırlarının fiziksel doğrulaması açık ön koşuldur; iyi görünen ölçüm grafiği giriş güvenliğini kanıtlamaz.
- Şebeke ve CT kurulumu uygun muhafaza/koruma ve yetkin uygulamayla yapılmalıdır.
- Bu çalışma enerji tüketimi, gerçek güç, PF, harmonik veya arıza teşhisi iddiası taşımaz.
- Makine kapağı/interlock veya güvenlik mekanizmalarına müdahale edilmez.

## 8. Kabul ölçütü

E21 ilk oturumu ancak aşağıdakiler tamamlandığında “ilk kayıt analiz edildi” sayılır:
- Tam program CSV'si mevcut ve kaynak bütünlüğü kontrol edilmiş.
- Program/ayar/yük bilgileri kullanıcıdan kaydedilmiş.
- Akım zaman serisi ve gözlenen evre tablosu üretilmiş.
- Gözlem, kullanıcı bildirimi ve hipotezler birbirinden ayrılmış.
- Ham veri ve analiz özeti depoda birbirine bağlanmış.

**Mevcut durum:** Kısa ve uzun programlara ait tam kayıt dosyaları kullanıcı kitaplığında mevcut olarak gösterilmiştir; kısa kayıt adı `wm-kısa-prg-2026-11-14.csv`, uzun kayıt adı `wm-uzun pamuklu 60 - 2026-11-14.csv` olarak bildirilmiştir. Bu ham CSV dosyaları henüz bu repo yoluna alınmış ve içerikleri burada analiz edilmiş değildir. İlk nitel gözlemler (ısıtma, sağ-sol tambur dönüşü, sıkma) kaydedilmiştir. Daha fazla tam program kaydı toplanacak; Python korelasyonu ve diğer analizler sonraki aşamadır. E21 bu nedenle yapılmamış değil, ön gözlem/kayıt aşamasında ve analizi beklemektedir.
