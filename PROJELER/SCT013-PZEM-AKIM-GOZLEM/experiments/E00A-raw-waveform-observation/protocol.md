# E00A — Protokol: bias trafosu DC noktalarının ADC gözlemi

## Ön koşullar
- Gerçek geliştirme kartı klasik ESP32-WROOM-32D mi ve GPIO34 kart üzerinde hangi pine çıkıyor: bağlantıdan önce işaret/pinout ile doğrula. GPIO34 yalnız uygun klasik ESP32 kartında ADC1_CH6 girişidir; ESP32-C3'te GPIO34 yoktur.
- Bias trafosu komple devre olarak ele alınır: RN130421 → KBU6M → 2200 µF / 35 V → L78L33 ve 2 × 10 kΩ Vmid bölücüsü.
- SCT bu deneyde kullanılmaz ve jack bağlı olmaz.
- GPIO34'e 3,3 V hattı doğrudan bağlanmaz. İlk koşul için ayrı/geçici harici 10 kΩ/10 kΩ ölçüm bölücüsü planlanır; ADC düğümü iki direnç arasındadır, alt direnç GND'ye gider. Bu parça bias trafosunun veya bias devresinin parçası değildir; yalnız ölçüm aparatı olarak kullanılacaktır. Bağlantıdan önce ESP32 ADC ayarı ve pin elektriksel sınırları doğrulanmalıdır.
- Bias trafosu GND ve ESP32 GND ortaklanır. Bağlantı değişiklikleri enerji kesikken yapılır. Multimetre ile DC çıkışlar ölçülür; ADC girişine negatif veya izin verilen üst sınırı aşan gerilim uygulanmaz.
- ADR-007'deki 10 µF ekleme kararı Vmid/SCT ön ucu içindir; fiziksel uygulama durumu ayrıca kontrol edilir. Bu iki DC gözlem koşulunda kondansatörün varlığı/yokluğu LOG'a yazılır; fiziksel olarak yapıldığı varsayılmaz.

## Kayıt biçimi
- Yerel CSV: `data/raw/E00A/bias_trafo_3v3.csv`, `data/raw/E00A/bias_vmid.csv`.
- Sütunlar: `sample_index,adc_raw`. Ham CSV'ye dönüştürülmüş voltaj yazılmaz.
- Her koşul için hedef hız, geçen süre (30 saniye), örnek sayısı, firmware sürümü/commit'i, multimetre değeri ve bağlantı düzeni results.md LOG alanına yazılır.
- 3,3 V koşulunda kaynak voltaj tahmini: ADC pinindeki mV × 2 (iki eşit dirençli bölücü varsayımı). Vmid koşulunda ADC pinindeki mV doğrudan Vmid tahminidir. Dirençlerin fiilî değerleri ölçülürse LOG'a eklenir.

## Adımlar
1. Enerji kapalıyken kart/pinout'u doğrula; bias trafosu GND ve ESP32 GND bağlantısını kontrol et.
2. Multimetreyle L78L33 çıkışını ve bias Vmid'i ölç; değerleri kaydet.
3. ADC üst bölge sınırı ve attenuation ayarı doğrulandıktan sonra, 3,3 V çıkışını ayrı harici 10 kΩ/10 kΩ ölçüm bölücüsü üzerinden GPIO34'e bağla. Bu bağlantı bias trafosunun iç devresini değiştirmez. Bağlantıyı kontrol ettikten sonra enerji ver.
4. 30 saniye boyunca seçilen ve firmware LOG'unda bildirilen hedef hızla aynı döngüde `analogRead()` ve `analogReadMilliVolts()` oku; CSV'ye ham ADC örneklerini kaydet.
5. Enerjiyi kes; ADC bağlantısını Vmid noktasına taşı. Yeniden bağlantıyı kontrol et, sonra enerji ver ve yine 30 saniyelik kaydı al.
6. Her koşul için mean, min, max, peak-to-peak, standart sapma, gerçek süre, örnek sayısı ve yaklaşık gerçekleşen hızı hesapla.
7. Bilgisayarda ADC-değer/zaman grafiği üret; multimetre ve ADC mV sonuçlarını karşılaştır.

## HEDEF / LOG / SONUÇ
- HEDEF: Bias trafosunun 3,3 V regülatör çıkışı ve yaklaşık 1,65 V Vmid noktasını aynı ESP32 ADC zinciriyle güvenli biçimde gözlemek; ADC ham/mV çıktılarının ve kısa dönem değişiminin farkını görmek.
- LOG: Gerçek kart/GPIO, iki bağlantı şeması, direnç değerleri, multimetre ölçümleri, firmware sürümü, hedef/gerçek örnekleme hızı, geçen süre, örnek sayısı, istatistikler, CSV yolu ve gözlemler.
- SONUÇ: Yalnız ölçülen verinin desteklediği yorum. ADC mV API'si hassas voltmetre sayılmaz; ölçüm bölücüsü ve ADC doğrusal olmayan bölgeleri sınırlama olarak yazılır. Veri yoksa “henüz ölçülmedi” denir.

## Kabul ölçütü
İki koşulun ham CSV kaydı ve metadata'sı; her iki koşulda multimetre DC ölçümü; hedef hız, gerçek süre ve örnek sayısı; temel istatistikler; iki koşulun karşılaştırması ve zaman grafiği. Firmware derlemesi ve fiziksel çalıştırma ayrı ayrı doğrulanır.

## Durum
PLANLANDI. Firmware geliştirme/derleme ve fiziksel ölçüm yapılmadı.


## İlk referans ölçümü — 2026-10-30

- L78L33 DC çıkışı multimetre ile **3,31 V** ölçüldü (KULLANICI BİLDİRİMİ).
- Bu, A koşulunun multimetre referans değeridir; ADC verisi değildir.
- 30 saniyelik ADC kaydı henüz alınmadı. Önce gerçek kart/pinout ve ADC giriş aralığı/attenuation doğrulanmalıdır.


## Firmware uygulaması — 2026-10-30

İlk ESP32D2 firmware'i [firmware/esp32d2-e00a-adc.yaml](firmware/esp32d2-e00a-adc.yaml) altında saklanır.

- ESPHome cihaz adı: `esp32d2`; framework: ESP-IDF.
- GPIO34 / ADC1_CH6 yalnız ham ADC sayısı için (`raw: true`).
- GPIO35 / ADC1_CH7 yalnız kalibrasyonlu voltaj tahmini için (`raw: false`).
- Her kanal ayrı ADC sensörüdür; aynı pin iki sensörde tekrar kullanılmaz.
- İki sensörün `update_interval` değeri 1 saniyedir. Bu, 1 kS/s veya 2 kS/s örnekleme anlamına gelmez; gerçek örnekleme hızı ayrıca ölçülmemiştir.
- Kullanıcı kodun derlendiğini ve çalıştığını bildirdi (KULLANICI RAPORU). Derleme ve cihaz logları henüz bu protokole eklenmedi.
- Fiziksel kablo bağlantılarının iki kanalda nasıl yapıldığı ve gerçek ADC değerleri logla doğrulanacaktır.

### HEDEF / LOG / SONUÇ güncellemesi
- **HEDEF:** İki ayrı ADC kanalını kullanarak ham count ve voltaj tahmini çıktılarını aynı deneyde elde etmek.
- **LOG:** Firmware dosyası depoya eklendi; kullanıcı derlendiğini/çalıştığını bildirdi. Ölçüm logu bekleniyor.
- **SONUÇ:** Kod aşamasında ilerleme var. Fiziksel ölçüm, ADC kararlılığı ve 30 saniyelik ham kayıt kabul ölçütleri açık.
