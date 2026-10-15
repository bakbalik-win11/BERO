# GRV-005-14 v02 — CSV Alan Hizalaması Statik Düzeltme Adayı

- Tarih: 2026-10-11
- Kaynak: Kullanıcının paylaştığı GRV-005-14 v01 YAML metni.
- Çıktı: `GRV-005-14-CSV-LOG-ADAYI-v02-STATIK-DUZELTME.yaml` (yerel çalışma dosyası; henüz depoya taşınmadı).
- ESPHome derlemesi: **Yapılmadı** — bu çalışma ortamında `esphome` komutu kurulu değil.
- Cihaza yükleme: **Yapılmadı**.
- Depodaki KOD klasörüne taşıma: **Yapılmadı**; derleme doğrulaması bekleniyor.

## Yapılan düzeltmeler

Yalnızca dört CSV `ESP_LOGI` format satırında değişiklik yapıldı:
1. `window_start_millis` önündeki `" %u"` biçimi `"%u"` oldu; baştaki boşluk kaldırıldı.
2. CH0-1T, CH1-2T ve CH2-3T satırlarında `adc_range` ile `adc_rms_raw` arasında eksik olan bir boş alan eklendi.
3. CH satırlarının sonunda bir fazla boş alan kaldırıldı; toplam alan sayısı 41 olarak korundu.
4. BIAS satırının sonunda bir fazla boş alan kaldırıldı; toplam alan sayısı 41 oldu.

## Statik doğrulama

Format belirteçleri test amaçlı yer tutucularla değiştirildi; sonuçlar CSV standardı ile ayrıştırıldı. Gerçek ADC/PZEM değerleri kullanılmadı.

- Başlık 41 alan: PASS
- CH0-1T: 41 alan, boşluk yok, RMS/BIAS/PZEM alanları yerinde: PASS
- CH1-2T: aynı kontroller PASS
- CH2-3T: aynı kontroller PASS
- BIAS: 41 alan; `adc_range`, BIAS özetleri ve PZEM alanları yerinde: PASS
- Toplam statik kontroller: **25/25 PASS**

## Sınırlar

Bu sonuç, metin biçimlendirme ve sütun hizası kontrolüdür. ESPHome derlemesi veya cihazda çalışması kanıtlanmış değildir. Kod, derleme onayı gelmeden görev deposunun KOD klasörüne taşınmamalıdır. Orijinal v01 metni değiştirilmemiştir.
