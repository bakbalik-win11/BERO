# E00A — Protokol: bias trafosu DC noktalarının ADC gözlemi

## Ön koşullar
- Gerçek geliştirme kartı klasik ESP32-WROOM-32D mi ve GPIO34 kart üzerinde hangi pine çıkıyor: bağlantıdan önce işaret/pinout ile doğrula. GPIO34 yalnız uygun klasik ESP32 kartında ADC1_CH6 girişidir; ESP32-C3'te GPIO34 yoktur.
- Bias trafosu komple devre olarak ele alınır: RN130421 → KBU6M → 2200 µF / 35 V → L78L33 ve 2 × 10 kΩ Vmid bölücüsü.
- SCT bu deneyde kullanılmaz ve jack bağlı olmaz.
- GPIO34'e 3,3 V hattı doğrudan bağlanmaz. İlk koşul için harici 10 kΩ/10 kΩ ölçüm bölücüsü kullanılır; ADC düğümü iki direnç arasındadır, alt direnç GND'ye gider. Bu ölçüm bölücüsü bias devresinin Vmid bölücüsünden ayrıdır.
- Bias trafosu GND ve ESP32 GND ortaklanır. Bağlantı değişiklikleri enerji kesikken yapılır. Multimetre ile DC çıkışlar ölçülür; ADC girişine negatif veya izin verilen üst sınırı aşan gerilim uygulanmaz.
- ADR-007'deki 10 µF ekleme kararı Vmid/SCT ön ucu içindir; fiziksel uygulama durumu ayrıca kontrol edilir. Bu iki DC gözlem koşulunda kondansatörün varlığı/yokluğu LOG'a yazılır; fiziksel olarak yapıldığı varsayılmaz.

## Kayıt biçimi
- Yerel CSV: `data/raw/E00A/bias_trafo_3v3.csv`, `data/raw/E00A/bias_vmid.csv`.
- Sütunlar: `sample_index,adc_raw`. Ham CSV'ye dönüştürülmüş voltaj yazılmaz.
- Her koşul için hedef hız, geçen süre, örnek sayısı, firmware sürümü/commit'i, multimetre değeri ve bağlantı düzeni results.md LOG alanına yazılır.
- 3,3 V koşulunda kaynak voltaj tahmini: ADC pinindeki mV × 2 (iki eşit dirençli bölücü varsayımı). Vmid koşulunda ADC pinindeki mV doğrudan Vmid tahminidir. Dirençlerin fiilî değerleri ölçülürse LOG'a eklenir.

## Adımlar
1. Enerji kapalıyken kart/pinout'u doğrula; bias trafosu GND ve ESP32 GND bağlantısını kontrol et.
2. Multimetreyle L78L33 çıkışını ve bias Vmid'i ölç; değerleri kaydet.
3. 3,3 V çıkışını harici 10 kΩ/10 kΩ ölçüm bölücüsü üzerinden GPIO34'e bağla. Bağlantıyı kontrol ettikten sonra enerji ver.
4. Yaklaşık 1 saniye boyunca 2 kS/s hedefiyle aynı döngüde `analogRead()` ve `analogReadMilliVolts()` oku; CSV'ye ham ADC örneklerini kaydet.
5. Enerjiyi kes; ADC bağlantısını Vmid noktasına taşı. Yeniden bağlantıyı kontrol et, sonra enerji ver ve aynı kaydı al.
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
