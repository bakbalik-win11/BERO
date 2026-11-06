# E15 — Tek SCT kanalında yayın aralığı / sıçrama davranışı

**Durum:** PLANLANDI; deney firmware'i hazırlandı, Validate/Compile/OTA ve fiziksel test bekliyor  
**Tarih:** 2026-11-06  
**İlişkili kayıtlar:** E14 üç kanal gözlemleri; E13 tek kanal 2 Hz hedefi

## HEDEF ve araştırma sorusu

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

**Zaman notu / kullanıcı bildirimi:** Görseldeki mevcut katsayısız kararlı durum gözlemi 2026-11-06 saat 13:49'da başladı. Kullanıcı 14:00'te yeni koda geçmeyi planladığını bildirdi. Bu zaman bilgisi kullanıcı beyanıdır; görsel tek başına tam kayıt aralığı veya 10 dakikalık tur tamamlandığını kanıtlamaz.

**Yorum sınırı:** Daha seyrek yayın aralığı iki yayın arasında oluşup kaybolan sapmaları örneklemeyebilir. Bu nedenle üç turdaki benzerlik/farklılık yalnız yayımlanmış tekil değerlerin gözlenen davranışı için yorumlanacaktır; örneklenmeyen fiziksel olayların yokluğu anlamına gelmez.


Üç kanallı Modül 2 düzeninde 0,5 / 1 / 2 saniyelik yayın aralıklarında gözlenen sıçrama davranışının, üç kanalın ortak ESP32 üzerinde çalışmasından veya kanalların sıralı/zamanlanmış okunmasından etkilenip etkilenmediğini araştırmak.

İlk aşamada yalnızca **tek SCT kanalı** çalıştırılacaktır. `sample_duration=100ms` sabit kalacak; yalnızca yeni ölçüm tetikleme/yayın aralığı üç turda değiştirilecektir.

Başlangıç hipotezi: Aynı tek kanal ve aynı 100 ms ölçüm penceresinde, ölçümler arasındaki bekleme süresi ölçüm penceresinin kendi sıçrama karakterini sistematik olarak iyileştirmemelidir. Bununla birlikte daha seyrek yayın, iki yayın arasında oluşan kısa süreli olayları gözlem dışı bırakabilir. Deney bu ayrımı gözeterek yorumlanacaktır.

## Deney düzeni

| Tur | Tek kanal | Ölçüm penceresi | Tetikleme aralığı | Nominal sonuç hızı | Süre |
|---|---|---:|---:|---:|---:|
| A | CH1-1T / GPIO32 | 100 ms | 500 ms | 2 Hz | 10 dk |
| B | CH1-1T / GPIO32 | 100 ms | 1 s | 1 Hz | 10 dk |
| C | CH1-1T / GPIO32 | 100 ms | 2 s | 0,5 Hz | 10 dk |

Her tur yaklaşık olarak sırasıyla 1.200, 600 ve 300 sonuç üretir. Bunlar nominal hesaptır; gerçek adet ve aralıklar HA timestamp'lerinden hesaplanacaktır.

**Sıra sabittir:** A → B → C. Her turun başında yapılandırma/OTA sonrası başlangıç ve yerleşme bölümü ayrıca işaretlenir; analizde bu bölümün dışlanıp dışlanmayacağı aynı kuralla uygulanır.

## Sabit tutulacaklar

- Aynı ESP32D1 cihazı ve ESPHome yapılandırma sürümü.
- Aynı fiziksel SCT sensörü, aynı CH1 sarı kablo, GPIO32 / ADC1_CH4 ve aynı 1T geçiş.
- Aynı SCT kablosu, burden/bias devresi, fiziksel yerleşim ve ölçülen iletken.
- Aynı fiziksel yük ve mümkün olduğunca aynı kararlı çalışma koşulu; üç tur arasında yük/tesisat değiştirilmez.
- `sample_duration: 100ms`, K=24.22, ADC attenuation=12dB, `raw: false`, ADC kaynak `samples: 1`.
- CH1 akım ve ham akım entity kimlikleri korunur.
- Modül 3 UDP 4210 olay alıcısı üç turda da aynı biçimde korunur.
- CH2 ve CH3 SCT ölçümleri ile GPIO35 bias ADC ölçümü deney YAML'ında devre dışıdır. Ortak bias devresi fiziksel olarak bağlı kalır; yalnızca ayrı bias ADC okuması yapılmaz.

## Kodun çalışma mantığı

- `ct_clamp.update_interval: never`: ct_clamp kendi başına periyodik ölçüm başlatmaz.
- YAML'daki tek SCT `interval` tetikleyicisi `component.update: sct_1_current` çağırır.
- Her tetiklemede ct_clamp 100 ms ölçüm penceresini yürütür; pencere sonunda akım sonucu yayımlanır.
- A/B/C turları arasında yalnız `interval` değeri 500ms → 1s → 2s olarak değiştirilir.
- UDP alıcısının 100 ms kontrol döngüsü ölçüm interval'inden ayrıdır; tüm turlarda sabit tutulur.

Bu düzen, yayın aralığının ADC ölçüm penceresi dışında kalan bekleme süresini değiştirir. Gerçek yayın aralıkları varsayılmayacak; HA timestamp'lerinden ölçülecektir.

## Değerlendirme yöntemi

Her tur için önce veri bütünlüğü ve gerçek yayın ritmi incelenir. Sonra aynı fiziksel kararlı yük bölümlerinde:

1. Ardışık yayımlanmış akım sonuçlarının mutlak farkı `|I[n]-I[n-1]|`.
2. Sıçrama genliği dağılımı: medyan, P95, P99 ve maksimum mutlak fark.
3. Önceden belirlenecek ortak eşik üzerindeki sıçrama adedi.
4. Gözlenen sıçrama sayısı / dakika.
5. Gözlenen sıçrama sayısı / 1.000 yayın.
6. Akım değerlerinin standart sapması ve sağlam dağılım ölçüleri.
7. Gerçek yayın aralığı dağılımı, eksik/uzamış aralıklar.

Sıçrama eşiği sonuçlar görüldükten sonra seçilmeyecek. Analiz başlamadan önce üç tur için ortak ve gerekçeli eşik belirlenecek; eşik henüz bu protokolde sayısal olarak sabitlenmemiştir. Eşik seçilene kadar mutlak ardışık farkların tam dağılımı da raporlanır.

### Önemli örnekleme sınırı

500 ms, 1 s ve 2 s akışları aynı zaman çözünürlüğüne sahip değildir. 2 saniyelik tur, iki yayın arasında oluşup kaybolan kısa bir sıçramayı hiç örneklemeyebilir. Bu nedenle:

- “dakika başına gözlenen sıçrama” gerçek fiziksel sıçrama olaylarının tam sayısı değildir.
- “1.000 yayın başına sıçrama” örnek sayısı farkını kısmen normalize eder; zaman çözünürlüğü farkını ortadan kaldırmaz.
- Sıçrama genliği, yalnız gözlenmiş ardışık yayın değerleri arasındaki farktır; arada gerçekleşen tepeyi göstermez.
- Sonuçlar örnekleme aralığının gözlenen veri serisine etkisi olarak raporlanır; görünmeyen olaylar hakkında kesin hüküm verilmez.

## Başlatma ön koşulları

- Kullanıcı aynı fiziksel yük/kararlı koşulu üç tur boyunca koruyacağını teyit eder.
- SCT yalnız CH1 girişinde ve 1T olarak bağlıdır. CT sekonderi açık bırakılmaz; bağlantı değişikliği yük enerjisizken yapılır.
- Deney YAML'ı ESPHome Validate ve Compile kontrolünden geçirilir.
- OTA sonrası cihaz kimliği, Wi-Fi/API, CH1 ADC ve HA entity yayınları kontrol edilir.
- A/B/C arasında yalnızca `interval` satırı değiştirilir; her tur 10 dakika sürer. Kullanılan YAML içeriği/commit ve HA kayıt zaman aralığı kaydedilir.

## Kod

Deney firmware'i: [bero-modul2-e15-single-sct-interval.yaml](../../firmware/experiments/bero-modul2-e15-single-sct-interval.yaml)

B turu için `interval: 1s` içeren ayrı ve tam YAML snapshot'ı: [bero-modul2-e15-single-sct-interval-b-1s.yaml](../../firmware/experiments/bero-modul2-e15-single-sct-interval-b-1s.yaml). A turu YAML'ı değiştirilmeden korunur.

Bu dosya mevcut üç kanallı ana firmware'in üzerine yazmaz. ESPHome cihaz kimliği `esp32d1` korunmuştur; aynı fiziksel cihaza yalnız bir yapılandırma yüklenmelidir. Dosyanın başlangıç hali A turu için 500ms'dir.

## Sonuç durumu

2026-11-06 tarihinde ilk kısa cihaz çalışma kontrolü yapıldı. ESPHome 2026.10.2 ile cihaz API bağlantısı, GPIO32 ADC başlatması, CH1 yayınları ve UDP EVENT_ID=314 / STATE=OFF alımı logda görüldü. Bu kayıt yaklaşık 28.5 saniyedir; 10 dakikalık A turu değildir ve sıçrama karşılaştırması sonucu üretmez. Yapılandırma adı logda esp32d1.yaml olarak geçtiğinden depodaki E15 YAML kaynak snapshot'ı ile çalışan binary'nin birebir hash eşleşmesi kanıtlanmış değildir.

- [İlk cihaz logu](../../logs/module2/2026-11-06-e15-a-500ms-initial-device-log.txt)
- [İlk log analizi](../../logs/module2/2026-11-06-e15-a-500ms-initial-device-log-analysis.md)
- Tur A/B/C ölçümleri ve karşılaştırma için [sonuç defteri](results.md) kullanılacaktır.

E15'in üç adet 10 dakikalık kayıt turu henüz tamamlanmadı.
