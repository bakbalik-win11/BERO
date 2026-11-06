# E15 — Sonuç defteri

**Durum:** TEST BEKLİYOR  
**Deney firmware'i:** [bero-modul2-e15-single-sct-interval.yaml](../../firmware/experiments/bero-modul2-e15-single-sct-interval.yaml)

## Ortak koşullar

- SCT: CH1-1T / GPIO32 / sarı
- Fiziksel SCT kimliği/seri tanımı: 
- Fiziksel yük ve bağlantı noktası: 
- `sample_duration`: 100 ms
- K: 24.22
- ESPHome sürümü: 
- YAML commit / içerik SHA: 
- Ortak koşul sapması veya test arası müdahale: 

## İlk cihaz çalışma kontrolü — 2026-11-06

**Durum:** Kısa cihaz ön kontrolü LOG İLE DESTEKLENDİ; 10 dakikalık A turu henüz tamamlanmadı.

- ESPHome 2026.10.2; API bağlantısı/handshake başarılı.
- GPIO32 / ADC1_CH4 başlatma, konfigürasyon ve kalibrasyon OK.
- ct_clamp sample_duration=100ms; update_interval=never.
- 28.492 saniyede 58 CH1 akım yayını; medyan yayın aralığı 0.500s (min 0.427s, max 0.577s).
- UDP EVENT_ID=314 / STATE=OFF paketi alındı ve HA text_sensor alanlarına yayınlandı.
- UDP OFF işareti fiziksel yükün kapandığını kanıtlamaz.
- Bu kısa log sıçrama karşılaştırması veya 10 dakikalık A turu sonucu değildir.

Kaynaklar: [ham cihaz logu](../../logs/module2/2026-11-06-e15-a-500ms-initial-device-log.txt), [log analizi](../../logs/module2/2026-11-06-e15-a-500ms-initial-device-log-analysis.md).

## Tur A — 500 ms / 2 Hz

- Başlangıç / bitiş (yerel saat +03:00):
- HA CSV / kaynak dosya:
- Kaynak SHA-256:
- Kayıt süresi:
- Toplam CH1 kayıt:
- Medyan / P05 / P95 yayın aralığı:
- Eksik veya uzun aralıklar:
- Akım ortalama / medyan / SD:
- Ardışık mutlak fark medyan / P95 / P99 / maksimum:
- Ortak sıçrama eşiği:
- Sıçrama adedi:
- Sıçrama / dakika:
- Sıçrama / 1.000 yayın:
- Geçiş veya veri dışlama kuralı:
- Yorum / kanıt sınırı:

## Tur B — 1 s / 1 Hz

- Başlangıç / bitiş (yerel saat +03:00):
- HA CSV / kaynak dosya:
- Kaynak SHA-256:
- Kayıt süresi:
- Toplam CH1 kayıt:
- Medyan / P05 / P95 yayın aralığı:
- Eksik veya uzun aralıklar:
- Akım ortalama / medyan / SD:
- Ardışık mutlak fark medyan / P95 / P99 / maksimum:
- Ortak sıçrama eşiği:
- Sıçrama adedi:
- Sıçrama / dakika:
- Sıçrama / 1.000 yayın:
- Geçiş veya veri dışlama kuralı:
- Yorum / kanıt sınırı:

## Tur C — 2 s / 0,5 Hz

- Başlangıç / bitiş (yerel saat +03:00):
- HA CSV / kaynak dosya:
- Kaynak SHA-256:
- Kayıt süresi:
- Toplam CH1 kayıt:
- Medyan / P05 / P95 yayın aralığı:
- Eksik veya uzun aralıklar:
- Akım ortalama / medyan / SD:
- Ardışık mutlak fark medyan / P95 / P99 / maksimum:
- Ortak sıçrama eşiği:
- Sıçrama adedi:
- Sıçrama / dakika:
- Sıçrama / 1.000 yayın:
- Geçiş veya veri dışlama kuralı:
- Yorum / kanıt sınırı:

## Üç tur karşılaştırması

| Ölçüt | A: 500 ms | B: 1 s | C: 2 s |
|---|---:|---:|---:|
| Gerçek medyan yayın aralığı | — | — | — |
| Kayıt adedi | — | — | — |
| Ardışık mutlak fark P95 | — | — | — |
| Ardışık mutlak fark P99 | — | — | — |
| Sıçrama / dakika | — | — | — |
| Sıçrama / 1.000 yayın | — | — | — |
| Akım SD | — | — | — |

## Sonuç

Henüz sonuç yok. Herhangi bir yayın aralığının daha kararlı olduğu veya fiziksel sıçramaları azalttığı iddia edilmemiştir. Daha seyrek örneklemenin kısa olayları kaçırabileceği karşılaştırma yorumunda korunacaktır.


## E15 ana hedef ve üç yayın aralığı için beklenen sonuç — 2026-11-06

**Kullanıcı tarafından netleştirilen ana hedef:** Katsayısız CH1-1T akım çıktısında, kararlı fiziksel koşul içindeki tekil ölçümlerin kendi ortalamasına yakınlığını iyileştirmek. Değerlendirme standart sapmayı tek başına hedef almayacaktır. Esas konu, ortalamadan sapmaların **ne sıklıkta** oluştuğu ve oluştuğunda **ne kadar büyük** olduğudur.

**E15'in bu üç turlu deneyine ait beklenti:** 500 ms, 1 s ve 2 s yayın aralıklarında bu sapma davranışının belirgin biçimde değişmemesi beklenmektedir. Deneyin sorusu, yayın aralığını değiştirmekle tekil ölçümlerin ortalamaya yakınlığının değişip değişmediğidir. Üç turda benzer sonuç çıkması, yayın aralığının bu kararlı durum sapma davranışında belirgin etkisi olmadığı yönünde kanıt sağlayacaktır; farklılık çıkması ise ayrıca incelenecektir. Bu beklenti sonuç değildir ve ölçümle sınanacaktır.

**Ana değerlendirme ölçütleri:**
- Her turun aynı kuralla seçilmiş kararlı bölümlerinde ortalama akım referans alınır; her tekil ölçüm için mutlak ortalamadan sapma hesaplanır: |I[n] − ortalama|.
- Önceden belirlenmiş ortak tolerans bandının dışında kalan tekil ölçümlerin adedi ve toplam geçerli ölçümlere oranı: sapma sıklığı.
- Tolerans dışı ölçümlerin ortalama, P95 ve maksimum mutlak sapması: sapma miktarı.
- Tüm ölçümlerde mutlak sapmanın medyanı ve P95'i de raporlanır; böylece yalnız eşik dışındaki değerler değil genel yakınlık da görünür.
- Tur süreleri ve yayın adetleri farklı olduğundan sıklık hem ölçüm başına oran (%) hem 1.000 yayın başına adet olarak verilir. Dakika başına adet yardımcı göstergedir.
- Tolerans bandı sonuçlar görülmeden, üç tur için ortak biçimde belirlenmelidir. Sayısal tolerans henüz kararlaştırılmamıştır; belirlenmeden eşik dışı sayım üzerinden üstünlük ilan edilmeyecektir.

**Zaman notu / kullanıcı bildirimi:** Görseldeki mevcut K=24.22 uygulanmış kararlı durum gözlemi 2026-11-06 saat 13:49'da başladı. Kullanıcı 14:00'te yeni koda geçmeyi planladığını bildirdi. Bu zaman bilgisi kullanıcı beyanıdır; görsel tek başına tam kayıt aralığı veya 10 dakikalık tur tamamlandığını kanıtlamaz.

**Yorum sınırı:** Daha seyrek yayın aralığı iki yayın arasında oluşup kaybolan sapmaları örneklemeyebilir. Bu nedenle üç turdaki benzerlik/farklılık yalnız yayımlanmış tekil değerlerin gözlenen davranışı için yorumlanacaktır; örneklenmeyen fiziksel olayların yokluğu anlamına gelmez.


## 2026-11-06 — Katsayı terminolojisi düzeltmesi

Önceki kayıtlarda geçen **“katsayısız”** ifadesi yanlıştı ve düzeltildi. E15/T008 kapsamında değerlendirilen SCT akım çıktısı, firmware'de `ct_clamp` filtresindeki `multiply: 24.22` ile katsayı uygulanmış değerdir. Amaç katsayıyı yok saymak değil; PZEM referanslı kararlı alanlardan mevcut K=24.22 katsayısını değerlendirmek ve gerekirse iyileştirmektir. Ham ADC/ct_clamp öncesi değer ile katsayı uygulanmış akım çıktısı birbirine karıştırılmayacaktır. Bu düzeltme ölçüm akışının ne olduğuna ilişkindir; yeni katsayı henüz hesaplanmış veya kabul edilmiş değildir.


## E15 B — 1 saniye kısa cihaz kontrolü (2026-11-06)

- Kullanıcı B turu kodunu cihaza yükledi ve kısa kontrol logunu paylaştı.
- ESPHome 2026.10.2; ESP32 rev3.1; derleme zamanı 14:12:57 +03:00. API çözümleme/bağlantı/handshake başarılı.
- GPIO32 / ADC1_CH4, 12 dB ADC init/config/calibration OK. ct_clamp sample_duration=100ms ve update_interval=never.
- CH1 katsayı uygulanmış akım entity'si 44 kez yayımlandı; 14:13:38.343–14:14:21.374 aralığında yaklaşık 43.0 saniye.
- Gerçek yayın aralığı medyanı 1.000 s; min 0.966 s; max 1.038 s; ortalama yaklaşık 1.001 s. Kısa kontrol B'nin 1 Hz ritmini doğruluyor.
- UDP EVENT_ID=370 / STATE=OFF alındı ve HA olay entity'lerine aktarıldı.
- OFF öncesi 33 ölçümün ortalaması yaklaşık 0.47085 A; OFF sonrası ilk değer 0.196 A. Bu yalnız betimleyici olay öncesi/sonrası gözlemidir; UDP STATE tek başına fiziksel yük durumunu kanıtlamaz.
- Log yaklaşık 43 saniyedir; 10 dakikalık B turu veya A/B/C sapma karşılaştırması değildir.
- ESPHome logu validated config cache'in esp32d1.yaml için kullanıldığını bildiriyor. Çalışan binary'nin depodaki B YAML snapshot'ıyla birebir hash eşleşmesi bu logla kanıtlanmıyor.
- [Ham log](../../logs/module2/2026-11-06-e15-b-1s-short-device-check.txt) ve [teknik analiz](../../logs/module2/2026-11-06-e15-b-1s-short-device-check-analysis.md) arşivlendi. B turunun resmi 10 dakikalık kaydı henüz tamamlanmadı.


## A/B/C kararlı ON sonuçları — HA History 2026-11-06

A=500ms, B=1s, C=2s pencereleri HA timestamp cadence geçişlerinden eşleştirildi. Her SSR ON çevriminde ilk/son 5 saniye çıkarıldı; test penceresinden önce başlamış ON çevrimleri dışarıda bırakıldı. Katsayısız ct_clamp ON serisi:

| Tur | n | ON çevrimi | Ortalama (A) | Medyan (A) | SD (A) | MAD (A) | P05–P95 (A) |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 581 | 10 | 0.019405 | 0.019185 | 0.001237 | 0.000491 | 0.018150–0.021124 |
| B | 271 | 10 | 0.019044 | 0.018939 | 0.000712 | 0.000451 | 0.018048–0.020301 |
| C | 135 | 9 | 0.018972 | 0.018892 | 0.000811 | 0.000518 | 0.017789–0.020225 |

Bu sonuçlar yalnız ON kararlı alt aralıkları içindir; tam A/B/C karşılaştırması, PZEM kontrolü, IQR uç değer işaretleri ve kanıt sınırları [A–F ortak raporunda](../../logs/module2/2026-11-06-e15-e16-a-f-on-only-comparison.md) bulunur. A/B/C build/hash doğrulaması CSV ile yapılamamıştır.
