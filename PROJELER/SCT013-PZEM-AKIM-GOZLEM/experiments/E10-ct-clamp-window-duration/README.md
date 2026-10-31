# E10 — ESPHome ct_clamp örnekleme penceresi süresi gözlemi

**Durum: PLANLANDI.** Fiziksel deney, YAML değişikliği, derleme/OTA ve yeni log henüz yapılmadı.
**Bağlı görev:** Faz 2 / T010 — Modül 2 ESP32D1 SCT-1.
**Yük:** [BREAD-TOASTER-001](../../test-loads/bread-toaster/README.md).

## 1. Hedef ve gerekçe

Mevcut Modül 2 ayarı ct_clamp sample_duration=200ms ve update_interval=2s. BREAD-TOASTER-001 Log 63'te, ilk açılış yayını ayrıldıktan sonraki 50 yayının akım ortalaması 3,09636 A, CV değeri %0,433 ve Raw AC ortalaması 0,127843 V'tur. 200 ms pencerelerde yaklaşık 3.500–3.667 kabul edilmiş örnek, ortalama yaklaşık 18.117 kabul edilmiş örnek/s raporlanmıştır.

Bu nedenle deneyin amacı ADC'yi daha hızlı okutmak veya örnek sayısının az olduğunu varsaymak değildir. Soru şudur: aynı ADC okuma yolu ve aynı yayın aralığı korunurken ölçüm penceresi uzatılırsa Raw AC RMS, akım dağılımı, kabul edilmiş örnek sayısı ve yük değişimlerinin görünürlüğü nasıl etkilenir?

Bu bir kalibrasyon deneyi değildir. K=24.22 değiştirilmeyecek; PZEM doğruluğu veya ±%4 başarısı iddia edilmeyecektir. Deney yalnızca pencere süresinin ölçüm davranışına etkisini gözlemleyecektir.

## 2. Raporlara açık atıflar

1. **Kullanıcının sağladığı ct_clamp raporu:** [kaynak metin](../../docs/research/ct-clamp/source/2026-10-31-user-supplied-ct-clamp-report.md), özellikle Bölüm 2 (kaynak kod akışı), Bölüm 4 (sample_duration analizi) ve Bölüm 5 (update_interval ilişkisi). 50 Hz'de 200/500/1000 ms pencerelerin yaklaşık 10/25/50 periyot olduğu; uzun pencerenin kesirli periyot etkisini azaltma ihtimali yanında olayları ortalayıp zaman çözünürlüğünü düşürebileceği anlatılır. Rapordaki LSB/gürültü, kesirli pencere hatası, float32 ve CPU yorumları raporun kendi hesap/varsayımlarıdır; BERO ölçümü değildir.
2. **GitHub Copilot raporu:** [özgün TXT](../../docs/research/ct-clamp/source/2026-10-31-github-copilot-ct-clamp-report.txt), “sample_duration analizi” ve “update_interval analizi” bölümleri. Daha uzun pencerenin RMS salınımını azaltabileceği, fakat hızlı değişimleri geciktirebileceği görüşünü sunar. Bu, ayrı bir analiz görüşüdür; doğrulanmış BERO bulgusu değildir.
3. **Bağımsız teknik inceleme:** [rapor](../../docs/research/ct-clamp/2026-10-31-independent-technical-review.md), özellikle Bölüm 3, 4, 8, 9 ve 10. ESPHome 2026.10.1 kaynak kodundaki pencere açma/kapama, source_->sample() çağrısı ve ardışık aynı değerlerin kabul edilmiş örnek sayısına katılmaması açıklanır. 200ms/2s ayarında yaklaşık 1,8 saniye pencere dışı süre bulunduğu belirtilir.
4. **Gerçek BERO tabanı:** [Log 63 analiz raporu](../../logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-analysis.md) ve [yük kaydı](../../test-loads/bread-toaster/README.md). UNIT 3,30 A kullanıcı bildirimidir; PZEM değildir ve zaman eşleşmesi doğrulanmadığından kalibrasyon referansı sayılmaz.

### Teknik çıkarımlar

- sample_duration pencerenin açık kaldığı süreyi belirler; tek başına ADC'nin saniyedeki okuma hızını artırmaz. Aynı çağrı hızı korunursa pencere başına daha fazla örnek toplanabilir.
- update_interval yeni pencerenin başlama sıklığıdır; deney boyunca 2s sabit kalacaktır.
- Uzun pencere kısa süreli dalgalanmaları ortalayabilir; bu yayın dağılımını daraltabilir, ancak geçişleri ve kısa olayları da yumuşatabilir.
- ct_clamp kaynak kodundaki tekrar örnek eleme nedeniyle logdaki örnek sayısı tüm fiziksel ADC dönüşümlerinin sayısı değildir. “Kabul edilmiş farklı örnek sayısı” olarak ele alınacaktır.

## 3. Deney sorusu ve hipotez

**Soru:** Aynı SCT-1 ve aynı kararlı yükte sample_duration 200ms, 500ms ve 1000ms olduğunda Raw AC RMS ve akım ortalaması/dağılımı, kabul edilmiş örnek sayısı ve yük değişimlerinin görünürlüğü nasıl değişir?

**Hipotez:** Uzun pencere kısa dönemli dalgalanmaların bir kısmını ortalayarak SD/CV'yi düşürebilir. Yük geçişleri ise daha yumuşak veya daha geç görünebilir. Ortalama değerin daha doğru olacağı peşinen kabul edilmez.

## 4. Sabit düzenek

| Parametre | Sabit değer |
|---|---|
| Cihaz | ESP32D1 / Modül 2 / T010 |
| SCT | SCT-1, 1 numaralı yuva |
| SCT sinyali | GPIO32 / ADC1_CH4 |
| Ortak bias izleme | GPIO35 / ADC1_CH7 |
| ESPHome | 2026.10.1 |
| ADC attenuation | 12 dB |
| ADC entity güncellemesi | 1 s |
| ct_clamp update_interval | 2 s |
| K | 24.22 |
| Yük | Aynı BREAD-TOASTER-001 ekmek kızartma makinesi ve aynı bağlantı |

**Tek değişken:** ct_clamp.sample_duration. GPIO, SCT, bias, besleme, ADC attenuation, ADC entity ayarı, update_interval, K, filtreler ve diğer YAML satırları sabit kalır. esphome.name: esp32d1 değiştirilmez.

## 5. Deney sırası

| Aşama | sample_duration | 50 Hz karşılığı |
|---|---:|---:|
| A — yeni başlangıç kontrolü | 200 ms | 10 periyot |
| B — deney 1 | 500 ms | 25 periyot |
| C — deney 2 | 1000 ms | 50 periyot |
| D — geri dönüş kontrolü | 200 ms | 10 periyot |

Her aşamada yük kararlı hale geldikten sonra en az 3 dakika log hedeflenir (2 saniyelik yayın aralığında yaklaşık 90 yayın). İlk OTA/açılış geçici yayını ayrıca işaretlenir. Aşamalar arasında yalnız sample_duration değiştirilir. D aşamasındaki 200 ms sonucu A'dan farklıysa zaman etkisi, termostat/ısınma, ortam ve besleme gibi etkenler ayrıca değerlendirilir.

## 6. Her aşamada kaydedilecek veriler

- Başlangıç/bitiş zamanı ve yerel saat dilimi.
- Yükün ON/OFF durumu; termostat kesintisi veya başka geçişlerin zamanı.
- Kullanılan YAML dosyası, sample_duration değeri, ESPHome sürümü ve YAML SHA-256.
- Akım yayını: n, ortalama, medyan, min, maks, SD ve CV.
- Raw AC RMS: n, ortalama, medyan, min, maks ve SD.
- Her pencerenin kabul edilmiş örnek sayısı ve raporlanan SPS.
- GPIO35 bias: n, ortalama, medyan, min, maks ve SD.
- Gerçek yayın aralığı, ERROR/timeout/yeniden başlama/bağlantı kopması kayıtları.
- Varsa aynı zaman aralığına ait PZEM değerleri; PZEM zorunlu kabul koşulu değildir.

## 7. Analiz ve yorumlama

Her aşamada akım ve Raw AC için ortalama/medyan/SD/CV karşılaştırılır. Kabul edilmiş örnek sayısının pencere süresiyle artıp artmadığı gözlenir; bu artış örnekleme hızının yükseldiği anlamına gelmez. Bias değişimleri ve yük geçişleri ayrı incelenir. Olay zamanı işaretlenmemişse kesin gecikme hesabı yapılmaz.

200ms/2s yaklaşık %10, 500ms/2s %25, 1000ms/2s %50 pencere görev oranına karşılık gelir. Bu oranlar CPU kullanım ölçümü değildir; işlemci yükü yüzdesi olarak raporlanmayacaktır.

## 8. Güvenlik ve durdurma

- Şebeke tarafı kapalı/korumalı ve uygun güvenlik koşullarında tutulur.
- SCT yalnız tek yalıtılmış faz iletkenini çevreler; faz ve nötr birlikte geçirilmez.
- SCT jakı veya düşük gerilim bağlantısı değiştirilecekse yük enerjisiz olmalıdır.
- Anormal ısınma, koku, bağlantı kararsızlığı, ESP yeniden başlatması veya beklenmeyen ADC/bias davranışında deney durdurulur.
- Termostat kesintisi olursa veri silinmez; ON, geçiş ve OFF bölümleri ayrı işaretlenir. Kararlı pencere kalmazsa aşama tekrarlanır.

## 9. Kabul ölçütü

Başarı, CV'nin mutlaka düşmesi değildir. Deneyin analiz edilebilir olması için dört gerçek ayar aşaması (200→500→1000→200ms), diğer sabit ayarların korunması, her aşamada hedef en az 60 (tercihen yaklaşık 90) kararlı yayın ve karşılaştırılabilir akım/Raw AC/örnek/SPS/bias verisi gerekir. Ham log veya kaynak hash'i, analiz tablosu ve yorum depoda saklanır.

Sonuç ne olursa olsun K=24.22 bu deney nedeniyle değiştirilmez. Kalibrasyon kararı için ayrıca eşleşmiş PZEM kararlı pencereleri gerekir.

## 10. Önceki kayıtlardan ayrım

- BREAD-TOASTER-001 Log 63 tarihsel 200ms tabanıdır; E10'da yeni A kontrolü de alınacaktır.
- TOASTER-001 Log 62 farklı tost makinesi testidir; bu deneyle birleştirilmez.
- Kullanıcı raporunun başlığında GPIO33 yazarken Log 63 ve mevcut Modül 2 YAML SCT-1 için GPIO32 gösterir. E10 güncel Modül 2 kaydını esas alır; tarihsel fark silinmez.
- E10 T010 altındaki bir ölçüm sorusudur; Faz 1 deneyleri yeniden açılmaz, T007/T008/T006 sırası değişmez.

## 11. Uygulama öncesi kontrol listesi

- [ ] Mevcut YAML yeniden okunacak; cihaz kimliği ve sabit ayarlar kaydedilecek.
- [ ] SCT-1 GPIO32 ve ortak bias GPIO35 bağlantıları değiştirilmeyecek.
- [ ] Aynı ekmek kızartma makinesi ve aynı bağlantı kullanılacak.
- [ ] A: 200ms YAML hazırlanıp derlenecek/cihaza yüklenecek; gerçek log alınacak.
- [ ] B: yalnız sample_duration=500ms yapılacak; derleme/cihaz logu doğrulanacak.
- [ ] C: yalnız sample_duration=1000ms yapılacak; derleme/cihaz logu doğrulanacak.
- [ ] D: sample_duration=200ms geri yüklenecek; derleme/cihaz logu doğrulanacak.
- [ ] Her aşamanın ham logu ve YAML hash'i korunacak.
- [ ] Sonuçlar results.md, T010, STATUS ve oturum günlüğüne işlenecek.

## 12. Mevcut durum

**Henüz deney yapılmadı.** Bu dosya yalnızca ayrıntılı protokoldür. YAML değiştirilmedi, ESP32'ye OTA yapılmadı, fiziksel yük çalıştırılmadı ve yeni log alınmadı.