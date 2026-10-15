# GRV-005-14 CSV Satır Şablonu — Alan Hizalama İncelemesi

- Tarih: 2026-10-11
- İnceleme girdisi: Kullanıcının paylaştığı GRV-005-14 v01 YAML metni.
- Yöntem: `ESP_LOGI` içindeki başlık ve dört satır format şablonu alındı; `%u`, `%ld`, `%.6f` vb. biçim belirteçleri test amaçlı `1` ile değiştirilip standart CSV ayrıştırıcısıyla alan sayısı/indeksleri kontrol edildi.
- Önemli: Bu bir format şablonu statik incelemesidir. `1` değerleri gerçek cihaz ölçümü değildir; cihaza kod yüklenmedi.

## Bulgular

### 1. Başlık alan sayısı

CSV v03 başlığı 41 alan içeriyor. `GRV-005-15-PYTHON-QC-KAPSAM-VE-PASS-OLCUTLERI-20261011.md` belgesindeki “42 alan” ifadesi başlık listesiyle uyuşmuyor. Kilitli başlık listesi sessizce değiştirilmedi.

### 2. CH0-1T / CH1-2T / CH2-3T satırları

Üç CH format şablonu 41 alan üretse de alan hizası hatalı. Statik şablon eşlemesinde:
- `raw0` değeri `adc_rms_raw` yerine `adc_p95_minus_p05` alanına düşüyor.
- `rms0` değeri `adc_rms_ac` yerine `adc_rms_raw` alanına düşüyor.
- `bias_mean` değeri `bias_mean` yerine `adc_rms_ac` alanına düşüyor.
- Devamındaki BIAS istatistikleri bir alan sola kayıyor ve `bias_max` boş kalıyor.
- PZEM current/power/PF değerleri de yanlış sütunlara kayıyor; `pzem_pf` boş kalıyor.
- `window_start_millis` alanı başında boşluk taşıyor (kaynak formatta `" %u"`).

Alan hizasının temel nedeni, `adc_range` sonrasındaki boş alan sayısının eksik olmasıdır. Ancak satır sonunda da gereğinden fazla boş alan var. Yalnızca araya virgül eklemek satırı 42 alana çıkarabilir; düzeltme iki ucu birlikte ele almalıdır: istatistikler öncesindeki eksik boş alanı eklemek ve sonda fazla olan boş alanı kaldırmak. Bu rapor YAML'ı değiştirmez.

### 3. BIAS satırı

BIAS format şablonu 42 alan üretiyor; beklenen başlık 41 alan. Son bölümde bir fazla boş alan bulunuyor. Şablondaki BIAS istatistikleri ve PZEM alanlarının konumu kontrol edilerek sondaki fazla alan kaldırılmalı.

### 4. Python QC bağlantısı

Yeni eklenen Python QC betiği, geçerli sentetik CSV'de 13/13 kontrol PASS verdi. Beş pozitif/negatif senaryonun tamamı beklenen şekilde sınıflandırıldı. Bu yalnızca QC betiğinin sentetik testlerde çalıştığını gösterir. Yukarıdaki gerçek GRV-005-14 satır şablonundaki hizalama sorunları nedeniyle mevcut YAML çıktısı için PASS iddiası yapılamaz.

## Sonraki teknik adım

Firmware'e yeni ADC testi yüklemek yerine, GRV-005-14 satır formatlarını 41 alanlı kilitli başlığa göre düzeltmek ve her `ESP_LOGI` satır şablonunu CSV ayrıştırıcısıyla statik olarak doğrulamak. Ardından aynı kontrolü Python QC betiğine regresyon testi olarak eklemek. Mevcut YAML, geçmiş loglar ve eski görev raporları korunur; düzeltme ayrı bir sürüm olarak tutulur.
