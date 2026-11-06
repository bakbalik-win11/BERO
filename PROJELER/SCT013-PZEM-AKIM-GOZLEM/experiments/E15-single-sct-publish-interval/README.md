# E15 — Tek SCT kanalında yayın aralığı / sıçrama davranışı

**Durum:** PLANLANDI; deney firmware'i hazırlandı, Validate/Compile/OTA ve fiziksel test bekliyor  
**Tarih:** 2026-11-06  
**İlişkili kayıtlar:** E14 üç kanal gözlemleri; E13 tek kanal 2 Hz hedefi

## HEDEF ve araştırma sorusu

Üç kanallı Modül 2 düzeninde 0,5 / 1 / 2 saniyelik yayın aralıklarında gözlenen sıçrama davranışının, üç kanalın ortak ESP32 üzerinde çalışmasından veya kanalların sıralı/zamanlanmış okunmasından etkilenip etkilenmediğini araştırmak.

İlk aşamada yalnızca **tek SCT kanalı** çalıştırılacaktır. `sample_duration=100ms` sabit kalacak; yalnızca yeni ölçüm tetikleme/yayın aralığı üç turda değiştirilecektir.

Başlangıç hipotezi: Aynı tek kanal ve aynı 100 ms ölçüm penceresinde, ölçümler arasındaki bekleme süresi ölçüm penceresinin kendi sıçrama karakterini sistematik olarak iyileştirmemelidir. Bununla birlikte daha seyrek yayın, iki yayın arasında oluşan kısa süreli olayları gözlem dışı bırakabilir. Deney bu ayrımı gözeterek yorumlanacaktır.

## Deney düzeni

| Tur | Tek kanal | Ölçüm penceresi | Tetikleme aralığı | Nominal sonuç hızı | Süre |
|---|---|---:|---:|---:|---:|
| A | CH1-1T / GPIO32 | 100 ms | 500 ms | 2 Hz | 30 dk |
| B | CH1-1T / GPIO32 | 100 ms | 1 s | 1 Hz | 30 dk |
| C | CH1-1T / GPIO32 | 100 ms | 2 s | 0,5 Hz | 30 dk |

Her tur yaklaşık olarak sırasıyla 3.600, 1.800 ve 900 sonuç üretir. Bunlar nominal hesaptır; gerçek adet ve aralıklar HA timestamp'lerinden hesaplanacaktır.

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
- A/B/C arasında yalnızca `interval` satırı değiştirilir; her turda kullanılan YAML içeriği/commit ve HA kayıt zaman aralığı kaydedilir.

## Kod

Deney firmware'i: [bero-modul2-e15-single-sct-interval.yaml](../../firmware/experiments/bero-modul2-e15-single-sct-interval.yaml)

Bu dosya mevcut üç kanallı ana firmware'in üzerine yazmaz. ESPHome cihaz kimliği `esp32d1` korunmuştur; aynı fiziksel cihaza yalnız bir yapılandırma yüklenmelidir. Dosyanın başlangıç hali A turu için 500ms'dir.

## Sonuç durumu

Henüz ölçüm yapılmadı. YAML kaynak taslağının depoya eklenmesi, derleme veya cihaz doğrulaması anlamına gelmez. Tur sonuçları [results.md](results.md) dosyasına ham kayıt referansı, SHA-256, gerçek örnek sayısı, gerçek aralıklar ve yorumla eklenecektir.
