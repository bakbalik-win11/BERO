# Açık sorular

Aşağıdaki sorular yalnız bu projede hâlâ cevaplanmamış proje-özel konulardır. Genel donanım bilgileri [referans klasöründe](../hardware/references/README.md) ve ana BERO `DONANIM/` belgelerinde mevcuttur.

1. İlk uygulama adayı envanterdeki klasik ESP32-WROOM-32D ve GPIO34 (ADC1_CH6) olarak belirlendi. Ölçüm öncesinde gerçek geliştirme kartının modeli/işaretleri ve pinout'u doğrulanmalı; kart farklıysa GPIO yeniden seçilmeli. Bu karar fiziksel bağlantının yapıldığı veya GPIO'nun doğrulandığı anlamına gelmez.
2. SAMM Market 5 V 2 kanallı SSR kartının hangi iki AC yükü anahtarlayacağı ve hangi ESP32 GPIO'larının kullanılacağı nedir? Ürün sayfasındaki LOW/HIGH eşikleri ile “low-level trigger” notu tutarsız olabildiğinden kontrol mantığı düşük gerilimde doğrulanmalı; giriş akımı ve kanal başına termal/sürekli yük sınırları ayrıca teyit edilmeli.
3. PZEM'in iç ölçüm/ortalama penceresi nedir; V, I, P ve PF aynı anda mı yenileniyor? Bunlar deneyle ölçülecek.
4. Hangi düşük akım aralığında PZEM referans okumaları kararsızlaşıyor veya SCT modelinin PZEM'e göre bağıl sapması ±%4 hedefini karşılamıyor? Bu proje için bağımsız referans cihazı şartı yoktur.
5. 1 kS/s, 2 kS/s ve 2,5 kS/s seçenekleri arasında hedef yüklerde anlamlı performans farkı var mı?
6. 200 ms pencere kararlı yükte tekrarlanabilir mi; çevrime senkron pencere gerekli mi?
7. E00A'nın ilk geçişinde bias-only, SCT yüksüz ve 100 W yük koşullarının temel istatistikleri nasıl farklılaşıyor; ilk kayıtlardan sonra farklı örnekleme hızlarını veya daha karmaşık aktarımı denemek için somut bir neden oluşuyor mu?
8. E08 sonuçlarında RMS, mutlak Peak ve Peak-to-Peak yöntemlerinin kendi pencere değişkenliği ve tekrar edilebilirliği, örnekleme hızı ve 1/2/4 kablo turuna göre nasıl karşılaştırılacak? Eşik veya gerekli pencere sayısı önceden seçilmeyecek; veri görüldükten sonra karar verilecek.

**Karara bağlandı; yeniden sorulmayacak:**
- Eğitim/etiket referansı PZEM-004T V3.0'dır. Modelin geçerli PZEM akım okumasına göre ±%4 bağıl sapma içinde olması Python'da `OK` sayılır. Kararlı alan gözlemi ve SCT istatistikleri ayrı görev/deney konusudur.
- DS3231: kullanıcı beyanı — RTC kodu çalıştı, güç kesilip yeniden verildikten sonra saat korundu; iki modülde de 2032 tipi pil var. Bu test ve pil bilgisi tekrar istenmeyecek.
- Deney yükleri önceden sabitlenmeyecek; kullanıcı her testte kullandığı yükü ve koşulları beyan edecek.
- Öncelikli sensör: SCT013-030 (30 A / 1 V).
- Kullanıcı stok bildirimi: 7 adet SCT013 30 A / 1 V ve 10 adet SCT013 100 A / 1 V; ikisi de jack çıkışlı. Jack yuvaları mevcut.
- Kullanıcı SCT'nin dişi jack üzerinden breadboard bias devresine bağlandığını tarif etti: 2 × 10 kΩ dirençle orta nokta ve orta noktadan GND'ye 104 (100 nF) kondansatör. Bu bağlantı bilgisi tekrar sorulmayacak. ESP32'nin dahili ADC'si kullanılacak; MCP3208 sonraki aşamaya ayrılmıştır. T004 hobi kapsamındaki belgeleme olarak tamamlandı; laboratuvar düzeyinde ADC aralığı/clipping ölçümü kapanış şartı değildir.
- PZEM kaydı: mevcut [DONANIM/PZEM-004T/README.md](../../../DONANIM/PZEM-004T/README.md) esas alınır.
- Bağlı CT: PZCT-02, 0–100 A; kullanıcı tarafından model olarak belirtildi ve PZEM'e bağlı olduğu fotoğrafta gösterildi. Bu, 100 A harici CT'li yapılandırmadır.
- İlk aşamada kullanılacak ESP32 kartları: 2× WROOM-32D, 1× WROOM-32E ve 1× genel ESP-WROOM-32 NodeMCU ESP32 Bluetooth.
- Masaüstü güç kaynağı: 5 V / 1,8 A; test yükü: lamba. Kullanıcı bağlantı ve ölçüm parçalarının tamamının mevcut olduğunu bildirdi.
- 5 V, 2 kanallı SAMM Market SSR kartı proje donanımına dahil edildi (tedarikçi kodu İzmo9659, SKU MP02637). Ürün sayfası OMRON, fototriyak izolasyon, zero-cross; kanal başına 75–264 VAC ve 0,1–2 A; kart beslemesi tüm kanallar açıkken 160 mA bildiriyor. Tam SSR parça kodu, gerçek giriş tetik mantığı ve yük ataması ayrıca doğrulanacak.
- DS3231 RTC, ölçüm/olay kayıtlarına takvim zamanı sağlamak için projede kullanılacak. Önceki BERO bağlantı pinleri ve NTP örneği referanstır; bu proje için pin/başlatma kararı değildir.
- Temiz yaklaşık 1,65 V bias üretim alt devresi kullanıcı onayıyla tamamlandı: RN130421 6 V / 2 VA → KBU6M köprü → 2200 µF / 35 V → L78L33; ayrı breadboardda 2×10 kΩ ve orta noktadan GND'ye 104 kodlu 100 nF seramik. Bağımsız ölçüm raporu yoksa 1,650 V'nin cihazla ölçüldüğü iddia edilmeyecek.

Açık kalan pin/SSR/ölçüm soruları, fiziksel parçaların eksik olduğu anlamına gelmez; sonraki pin planlama ve deney aşamalarında ele alınacak proje-özel kararlardır.

## E00A öncesi açık teknik kapı

- [ ] Kullanılacak fiziksel geliştirme kartının WROOM-32D tabanlı olduğu ve GPIO34'ün ilgili kartta doğru pine çıktığı pinout üzerinden doğrulandı.
- [ ] Bias orta noktasındaki mevcut 100 nF'ye paralel 10 µF, ADR-007'ye göre fiziksel olarak eklendi; Vmid/GND bağlantısı ve elektrolitik polaritesi gözle kontrol edildi.
- [ ] E00A ham kayıt CSV biçimi (`sample_index,adc_raw`) ve `data/raw/E00A/` yerel kayıt yolu hazır; hedef hız ile gerçekleşen hızın ayrı kaydedileceği biliniyor.
- [ ] Fiziksel bağlantı, gerçek kart/GPIO, fiilî kondansatör düzeni ve firmware sürümü E00A LOG'una kaydedilecek.

Bu kapılar belge düzenlemesiyle tamamlanmış sayılmaz. PZEM zaman damgası/logging entegrasyonu E00A'nın ham ADC gözlemi için ön koşul değildir; PZEM/SCT etiketleme aşamasında ayrıca ele alınır.

## 2026-10-29 belge incelemesinden sonra

- [ADR-007](decisions/ADR-007-bias-midpoint-capacitor.md) sonucunda, 2 × 10 kΩ bias bölücüsünün orta noktasına mevcut 100 nF kondansatöre paralel 10 µF eklenmesi ilk SCT bağlantılı ölçümden (E00A) önce planlandı. Fiziksel değişiklik henüz yapılmış sayılmaz; mevcut devrenin belgelenen değeri 104 (100 nF) olarak korunur. ADC pinine ayrıca 100 nF eklenmesi kararlaştırılmadı.
- Satürasyon belgesi genel CT risklerini anlatır; BERO'da satürasyon oluştuğuna dair ölçüm yoktur.


## E08 — güncel deney kapsamı

E08'de PZEM veya başka ESP'nin ortalama akımı varsa yalnız genel deney koşulu notudur; SCT pencereleriyle zaman eşleştirmesi yapılmaz. Bu, proje genelindeki daha sonraki PZEM/SCT etiketleme hedefini kaldırmaz; yalnız E08'in kapsamını sınırlar. Güncel sıra ve her aşamanın gerekçesi [E08 genel açıklamasında](../experiments/E08-sct-characterization/README.md) kayıtlıdır. Fiziksel ölçüm yapılmadı.


## 2026-10-30 — E00F düşük akım teşhis soruları

1. 0.006 V Raw AC Value hangi fiziksel koşulda ve hangi 200 ms pencerede üretildi? Aynı log kesitinde yük durumu, farklı örnek sayısı (N) ve raporlanan SPS var mı?
2. D1 SCT bağlı/primer akımsız koşulu ile D2 8.35 W LED koşulunda Raw AC Value, N ve raporlanan SPS dağılımları nasıl değişiyor?
3. Düşük akımda ardışık aynı sayısal ADC değerlerini atlama davranışının ve 1 mV kalibre gerilim adımının sonuç üzerindeki etkisi BERO ham verisiyle ne ölçüde gösterilebilir?
4. D3 akkor kontrolünde aynı kurulum ve eşleşmiş pens/ESP32 kayıtları önceki ±%4 gözlemlerini tekrarlıyor mu?
5. D4 ayrı RAW count teşhisi veya D5 E08 ham edinimi, D0–D3 sonuçlarından sonra gerekli mi?

Bu sorular için deney sırası ve kabul ölçütleri [toplu teknik değerlendirmede](technical-reviews/2026-10-30-e00f-low-current-cumulative-review.md) tanımlıdır. Bu soruların eklenmesi fiziksel ölçüm yapıldığı anlamına gelmez.


## 2026-10-30 — E00F test kabul ölçütleri netleştirildi

6. D0'da her pencerenin Raw AC / N / SPS üçlüsü çıkarılabiliyor mu; N ve SPS min/max/ortalama/medyan/SD/p5/p95 dağılımları nasıl?
7. D1 yüksüz tabanı en az 30 geçerli 200 ms pencereyle hangi medyan ve standart sapmayı veriyor? 0.006 V seviyesi tekrarlanıyor mu, yoksa taban sıfıra veya başka bir seviyeye mi yakın?
8. D2 LED koşulunda en az 30 geçerli pencere D1 tabanından ayrışıyor mu? D1 medyanı + 3×SD ve gerektiğinde robust medyan + 3×MAD karşılaştırması ne gösteriyor?
9. D3'te 0.447 A ve/veya 0.616 A akkor koşulu aynı yüksüz tabanla karşılaştırıldığında Raw AC ve akım sapması nasıl değişiyor?
10. D0–D3 verisi N değişkenliği, Raw AC sıçramaları ve mV kuantizasyonu arasındaki belirsizliği çözüyor mu; çözmüyorsa D4 RAW teşhisi gerekli mi?

**Ölçüm protokolü:** D1/D2/D3 için her kararlı koşulda en az 30 geçerli 200 ms pencere tutulur; koşul değişiminden sonraki ilk pencere dışlanır. 0.0017 V, 0.041 A'nın 24.22 katsayısıyla gerilim karşılığıdır; yüksüz taban hedefi değildir. Standart sapma için keyfî mutlak Volt eşiği kullanılmaz; D1 dağılımı ampirik taban olarak alınır. Ayrıntı: [toplu teknik değerlendirme](technical-reviews/2026-10-30-e00f-low-current-cumulative-review.md).


## 2026-10-30 — Python kalibrasyon modeli için karar soruları

1. İlk tek doğrusal modelin artıkları akım aralığına göre sistematik eğilim gösteriyor mu; parçalı doğrusal model bunu ayrı kararlı pencerelerde anlamlı biçimde iyileştiriyor mu?
2. Düşük SCT RMS pencereleri yüksüz taban dağılımından güvenilir biçimde ayrışıyor mu? Ayrışmayan pencereyi gerçek 0 A yerine geçersiz/düşük güvenilirlik olarak nasıl etiketleyeceğiz?
3. T006 eğitim özelliği E08 ham örneklerinden Python'da hesaplanan RMS mi olacak, yoksa E00F ct_clamp çıktısı mı? İki hesaplama yolunun örnek kabul/dedup davranışı farklı olduğundan aynı özellik kabul edilmemeli.
4. Parçalı model gerekirse bölge sınırları, geçiş sürekliliği ve monotonluk hangi gerçek kararlı pencere verisiyle belirlenecek?

**Geçici karar:** Önce tek doğrusal model; yalnız artık analizi ve ayrı tutulan pencereler daha karmaşık yapıyı gerekçelendirirse parçalı doğrusal model. Sinyal ayrışma kontrolü model tahmininden ayrı tutulur. 0.1 V / 0.5 V gibi örnek eşikler şimdilik kabul edilmez. Ayrıntı: [E00F teknik değerlendirme, bölüm 10](technical-reviews/2026-10-30-e00f-low-current-cumulative-review.md).



## 2026-10-30 — Gemini son değerlendirmesi sonrası karar soruları

1. ESPHome ct_clamp dedup davranışının zaman ağırlıklı RMS'e etkisi, aynı sinyalin ham ADC örnekleriyle yeniden hesaplandığında ne kadar fark oluşturuyor?
2. ESPHome varyans hesabında float hassasiyeti veya pencere içi bias hareketi BERO sinyal seviyesinde anlamlı fark oluşturuyor mu? Sabit DC kaymasının ideal varyansta iptal olduğu ayrımı korunmalı.
3. E00F ct_clamp ve E08 Python ham örneklerinden hesaplanan özelliklerin aynı model girdisi sayılmaması için hangi edinim/özellik kimlikleri tutulmalı?
4. Aynı edinim yolunda yüksüz taban ve yük pencerelerinin dağılımı hangi tekrarlı/bağımsız oturum koşulunda güvenilir biçimde ayrışıyor? Gemini'nin 1.0–1.2 varyans oranı eşik olarak kabul edilmedi.
5. Model artıklarında bölgesel sistematik eğilim, bağımsız yük olayı/oturum tekrarlarında da görülüyor mu? Veri yeterli olmadan parçalı model veya cross-validation sonucu ilan edilmeyecek.

Karar özeti: Önce tek doğrusal model; parçalı model ancak veri gerekçelendirirse. Sinyal ayrışma kapısı regresyondan ayrı. E00F ve E08 özellikleri gelişigüzel birleştirilmeyecek. Ayrıntı: [E00F teknik değerlendirme, bölüm 11](technical-reviews/2026-10-30-e00f-low-current-cumulative-review.md).

