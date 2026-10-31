# BERO — Sensör okuma kalıpları

**Durum: REFERANS / ŞABLON.** Bu klasördeki YAML örnekleri yeni cihazda doğrudan çalıştığı doğrulanmış firmware değildir. Her dosya kendi amacı, bağlantı varsayımı, veri yolu ve sınırlarıyla açıklanır. Mevcut ESP32D1/ESP32D2 firmware dosyaları bu örnekler nedeniyle değiştirilmemiştir.

## Neden ayrı bir klasör?

ESPHome `ct_clamp` incelemesinden çıkan temel ders, sensör okumanın tek bir işlem olmadığıdır. Kaynak örneği alma, geçerli örneği seçme, pencere içinde istatistik üretme, fiziksel birime çevirme ve Home Assistant'a yayınlama farklı görevlerdir.

Bu görevlerin bazıları sensörler arasında ortaklaştırılabilir. Ancak her sensör için aynı matematiksel işlem kullanılamaz.

## Önerilen ortak veri yolu

```text
FİZİKSEL SENSÖR
      |
      v
1. KAYNAK OKUMA
   ADC / I2C / SPI / UART / pulse
      |
      v
2. GEÇERLİLİK KONTROLÜ
   NaN, timeout, aralık, bağlantı hatası
      |
      v
3. ÖRNEK YÖNETİMİ
   örnek zamanı, tekrar/stale kontrolü (gerekiyorsa)
      |
      v
4. SİNYALE UYGUN İŞLEME
   CT-AC: RMS
   DC analog: ölçekleme / ortalama / medyan
   pulse: frekans / sayaç
   dijital sensör: protokolden gelen ölçüm
      |
      v
5. FİZİKSEL BİRİME DÖNÜŞÜM
   V, A, °C, bar, rpm vb.
      |
      v
6. YAYIN VE KAYIT
   Home Assistant entity + timestamp + birim + kaynak
```

Bu bir mimari rehberdir; ESPHome'da bütün adımları otomatik yapan tek bir genel bileşen olduğu iddiası değildir. Bazı adımlar ilgili ESPHome platformunun içinde, bazıları filtrelerde, bazıları özel kodda uygulanır.

## Bu klasördeki örnekler

| Dosya | Amaç | Kullanım alanı |
|---|---|---|
| [ct-clamp-ac-rms-reference.yaml](ct-clamp-ac-rms-reference.yaml) | CT sinyalinden pencere bazlı AC RMS gerilim ve katsayılı akım üretmek | SCT013 gibi CT sensörleri |
| [adc-dc-voltage-observer.yaml](adc-dc-voltage-observer.yaml) | ADC girişindeki analog DC gerilimi izlemek | Analog çıkışlı yavaş/değişken sensörler; yalnız gerilim aralığı uygunsa |

## Örnek 1 — CT / AC RMS

Kaynak YAML: [mevcut ESP32D1 firmware](../esp32d1.yaml). Referans örneği, bu ölçüm yolunun açıklamalı ve bağımsız bir kopyasıdır.

### Bağlantı varsayımı

- SCT sinyal çıkışı: klasik ESP32 ADC1 GPIO32 (örnekte).
- Bias: yaklaşık orta besleme gerilimi; örnekte GPIO35 yalnız bias gözlemidir.
- SCT sekonderi, sensör üreticisinin bağlantı biçimine uygun kapalı düşük-gerilim devresine bağlanır.
- SCT013-030 30 A / 1 V türünde dahili burden bulunduğu için sensörün veri sayfası doğrulanmadan harici burden eklenmez.
- GPIO pinleri kart/shield üzerinde fiziksel olarak doğrulanmadan örnek yüklenmez.

### Kodun veri akışı

1. `platform: adc` GPIO32'yi `ct_clamp` için analog kaynak olarak tanımlar.
2. ADC entity'sinin `update_interval: 1s` değeri Home Assistant'ta tekil voltaj görünürlüğü içindir. Bu 1 saniye, ct_clamp örnekleme penceresi değildir.
3. `platform: ct_clamp` kaynak ADC'yi kendi örnekleme döngüsünde pencere boyunca çağırır.
4. `sample_duration: 200ms` 50 Hz'de 10 nominal şebeke çevrimine karşılık gelir.
5. `update_interval: 2s` yeni ölçüm penceresinin başlama aralığıdır; 200 ms pencereyle aynı şey değildir.
6. `on_raw_value` katsayı uygulanmadan önceki ct_clamp çıktısını ayrı Raw AC voltaj entity'sine aktarır.
7. `multiply: 24.22` Raw AC RMS voltajını akım göstergesine ölçekler. 24.22 BERO'nun mevcut tarihsel başlangıç katsayısıdır; başka SCT, analog ön uç veya kart için evrensel değildir.
8. GPIO35 bias gözlemi, bias seviyesini ayrı entity olarak gösterir. Bu değer ct_clamp'in pencere içindeki her ADC örneğiyle eşzamanlı bir kayıt değildir.

### last_value filtresi hakkında

ESPHome kaynak kodundaki `last_value == value` kontrolü `ct_clamp` bileşeninin içindedir; bu YAML'da açılıp kapatılan bir ayar değildir. ADC kaynağından `sample()` çağrısı yapıldıktan sonra eşit değer kontrol edilir. Aynı değer tekrar geldiyse RMS istatistiğine yeniden eklenmez; ADC okuma çağrısı engellenmez.

Bu davranış her sensöre kopyalanmamalıdır. Yavaş değişen bir sıcaklık veya basınç sensöründe aynı sayısal değerin tekrar gelmesi gerçek ve anlamlı bir sabit durumu gösterebilir. Tekrar eleme ancak kaynağın eski dönüşümü tekrar sunduğu biliniyorsa ve etkisi ölçülmüşse düşünülmelidir.

## Örnek 2 — Genel analog DC gerilim

[adc-dc-voltage-observer.yaml](adc-dc-voltage-observer.yaml) ESP32 ADC pininden analog gerilim okuyan temel örnektir.

### Bağlantı varsayımı

- Örnekte GPIO34 kullanılmıştır; yalnızca klasik ESP32 ADC1 pininin ilgili kartta gerçekten erişilebilir ve boş olduğu durumda kullanılmalıdır.
- BERO Modül 2'de GPIO34, SCT-3 için ayrılmıştır. Bu nedenle bu YAML mevcut Modül 2'ye olduğu gibi yüklenmemelidir.
- Sensör çıkış gerilimi ESP32 ADC giriş sınırları içinde kalmalıdır. Daha yüksek gerilimli sensörlerde uygun analog ölçekleme/koruma devresi tasarlanmalıdır.
- ADC GND ve sensör GND bağlantısı, sensör arayüzü buna izin veriyorsa ortaklanır.

### Kodun veri akışı

1. `platform: adc` doğrudan pin gerilimini okur.
2. `raw: false` ADC çıktısını kalibre edilmiş gerilim olarak verir; ham sayım değeri değildir.
3. `samples: 1` tek ADC okuma ayarını kullanır; otomatik çoklu örnek ortalaması değildir.
4. `update_interval: 1s` yavaş gözlem/yayın aralığıdır; dalga şekli örneklemesi değildir.
5. `force_update: true` aynı sayısal değer tekrarlansa da güncellemenin raporlanmasına yardımcı olur.
6. Bu örnek yalnız voltajı verir. Sıcaklık, basınç, seviye veya başka mühendislik birimine dönüşüm için sensörün transfer fonksiyonu, beslemesi, devre bağlantısı ve kalibrasyonu ayrıca eklenmelidir.

## Hangi sensörde hangi işlem?

| Sensör / sinyal | Uygun okuma yolu | Uygun işleme | `ct_clamp` kullanılır mı? |
|---|---|---|---|
| SCT / AC akım trafosu | ADC + CT platformu | DC ortalamasını ayırıp AC RMS, sonra akım katsayısı | Evet |
| Analog DC gerilim çıkışlı basınç/seviye sensörü | ADC | Sensör eğrisine göre ölçekleme; gerekirse ortalama/medyan | Hayır |
| NTC / direnç tipi sıcaklık | Uygun direnç bölücü + ADC/NTC platformu | Beta veya Steinhart-Hart dönüşümü | Hayır |
| I2C sıcaklık/nem/basınç | I2C sensör platformu | Sensörün dijital ölçümü; gerekirse yavaş filtre | Hayır |
| UART/Modbus ölçer | UART/Modbus platformu | Parse, timeout ve geçerlilik kontrolü | Hayır |
| Pulse çıkışlı debi/devir sensörü | pulse_counter / pulse_meter | Darbe sayımı, frekans, zaman penceresi | Hayır |

## Tasarım kuralları

### 1. Kaynak örnek hızı ile yayın aralığını ayır

Bir entity'nin 1 saniyede bir yayın yapması, ADC'nin yalnızca saniyede bir örnek aldığı anlamına gelmeyebilir. Tersine, bir pencere içinde çok sayıda örnek toplamak da her örneğin Home Assistant'a gönderildiği anlamına gelmez. Kodda hangi katmanın örnek aldığı ve hangi katmanın yayın yaptığı açıkça belirtilmelidir.

### 2. Tekrar örnek eleme evrensel değildir

`last_value` yaklaşımı belirli ADC kaynaklarının dönüşüm yenileme hızına ilişkin sorundan doğmuştur. Her sensörde eşit değerleri atmak veri kaybına yol açabilir. Tekrar sayısı, kabul edilen örnek sayısı ve zaman bilgisi ayrıştırılmalıdır. Logdaki kabul edilmiş SPS, fiziksel ADC dönüşüm hızı olarak adlandırılmamalıdır.

### 3. Pencere istatistiği sinyal türüne göre seçilir

- AC CT: RMS / AC bileşeni.
- DC analog: ortalama veya medyan; sensörün tepki süresine göre.
- Darbe: pencere başına darbe sayısı veya periyot.
- Dijital sensör: üreticinin ölçüm/filtreleme davranışı dikkate alınır.

Standart sapma formülünü her sensöre uygulamak doğru değildir. CT'de DC biası ayırmak için kullanılması, başka sensörde aynı fiziksel anlamı taşımaz.

### 4. Geçersiz ölçümü sessizce gerçek sıfıra çevirme

NaN, timeout, bağlantı hatası, aralık dışı değer ve gerçek sıfır ayrı durumlardır. Sensör protokolü veya uygulama sıfırın geçerli ölçüm olduğunu doğrulamadan hata değerleri 0 olarak sunulmamalıdır. Kaynak hata bilgisi logda korunmalıdır.

### 5. Kalibrasyon katsayısını sensör kimliğiyle bağla

Bir çarpan; sensör modeli, analog ön uç, besleme, ADC kartı, pin ve kalibrasyon koşuluna bağlı olabilir. `24.22` yalnız BERO'nun mevcut SCT zincirinde tarihsel başlangıç katsayısıdır. Başka bir sensöre taşınmaz.

## Uygulama ve doğrulama sırası

Yeni sensör eklerken:
1. Sensör modeli, çıkış türü, besleme ve üretici transfer fonksiyonu kaydedilir.
2. Pin ve elektriksel aralık fiziksel kart üzerinde doğrulanır.
3. Önce yalnız ham kaynak/voltaj okuması denenir.
4. Gerçek sensör çıktısı ve yüksüz/başlangıç davranışı loglanır.
5. Sinyale uygun işleme yöntemi eklenir.
6. Ölçekleme/kalibrasyon ayrı ve izlenebilir yapılır.
7. Derleme, cihaz bağlantısı ve gerçek ölçüm doğrulaması ayrı kaydedilir.
8. Başarılı kod, gerçek örnek log ve yorum birlikte arşivlenir.

## Bu kayıtla ilgili doğrulama durumu

- Kaynak dayanağı: BERO'daki ESPHome ct_clamp araştırma sentezi ve mevcut YAML örnekleri.
- Kodun niteliği: açıklamalı referans/şablon.
- Bu klasördeki YAML'lar için derleme: **yapılmadı**.
- Yeni donanımda OTA/fiziksel test: **yapılmadı**.
- Mevcut çalışan ESP32D1 YAML'ı: **değiştirilmedi**.
- Faz 2 aktif görev sırası: **değiştirilmedi**.

## İlgili araştırma

- [ct_clamp üç kaynaklı sentez](../../docs/research/ct-clamp/2026-10-31-synthesis-copilot-claude-independent.md)
- [ct_clamp bağımsız teknik inceleme](../../docs/research/ct-clamp/2026-10-31-independent-technical-review.md)
- [ESP32D1 mevcut firmware](../esp32d1.yaml)
- [ESP32D2 tarihsel firmware](../esp32d2.yaml)
