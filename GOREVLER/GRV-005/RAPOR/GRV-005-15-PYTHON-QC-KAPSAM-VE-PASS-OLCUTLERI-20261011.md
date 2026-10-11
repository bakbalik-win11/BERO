# GRV-005-15 v01 — Python CSV Kalite Kontrolü — Kapsam ve PASS Ölçütleri

- Tarih: 2026-10-11
- Durum: Kapsam tanımlandı; Python kodu henüz yazılmadı ve çalıştırılmadı.
- Ön koşul: GRV-005-14 v01 cihaz logu ve CSV v03 şeması.
- İlgili cihaz raporu: [GRV-005-14 derleme/cihaz sonucu](GRV-005-14-DERLEME-CIHAZ-SONUCU-20261011.md)

## Hedef

ESPHome logundan alınan GRV-005-14 CSV başlığı ve dört kanal satırını Python ile ayrıştırmak; kilitli CSV v03 şemasını değiştirmeden yapısal ve temel veri kalite kontrollerini uygulamak. QC aracı sorunları raporlamalı, veriyi sessizce düzeltmemeli.

## Girdi

- Kullanıcının sağladığı GRV-005-14 ESPHome log kopyası veya aynı logdan kullanıcı tarafından çıkarılmış bir metin dosyası.
- Beklenen CSV v03 başlığı, 42 alanın sırası ve boş/NOT_TRACKED değerlerine ilişkin mevcut sözleşme.
- Başlığın ESPHome log satırı uzunluğu nedeniyle kesilmesi olasılığı: başlık tek log satırında eksikse QC başlığı iki parçalı biçimde birleştirebilmeli veya ayrı tam şema sabitini kullanmalı; ham logda eksik görünen başlık, sessizce tammış gibi raporlanmamalı.

## Kapsam içi kontroller

1. **Başlık ve sütun sayısı:** beklenen 42 sütun, adlar ve sıra; yinelenen/eksik/fazla alanlar.
2. **Satır ayrıştırma:** CSV sözdizimi, her satırın sütun sayısı, baş/son boşluklar ve hatalı alan hizası. CSV standardına göre ayrıştırmak; virgülle basit split kullanmamak.
3. **Veri tipleri:** sayısal alanlar sayı olarak ayrışmalı; `invalid_count=NOT_TRACKED` gibi izinli metinsel değerler korunmalı; bilinmeyen değerler boş kalmalı, sıfıra çevrilmemeli.
4. **measurement_id:** dört kanal satırının aynı ölçüm kimliğini taşıması; beklenen kanal kümesinin CH0-1T, CH1-2T, CH2-3T ve BIAS olması; yinelenen/eksik kanal kontrolü.
5. **Zaman alanları:** pencere başlangıç/bitiş/merkez/süre ilişkisi, signed `time_delta_ms` aritmetiği (`pzem_update_millis - window_center_millis`) ve eksik duvar saati alanlarının kontrolü. Önceki kararlara uygun olarak keyfî GOOD/BAD eşiği icat edilmemeli.
6. **İstatistikler:** kanal bazında adc_mean, adc_std, min/max/range, adc_rms_raw ve adc_rms_ac dağılımlarını özetlemek; BIAS alanlarını ayrı kontrol etmek. Değerlerin makul görünmesi tek başına fiziksel doğruluk kanıtı sayılmamalı.
7. **PZEM referansı:** PZEM değerlerinin eksik/varlık durumunu ve aynı ölçüm kimliğindeki kanallara kopyalanıp kopyalanmadığını kontrol etmek. `pzem_update_millis` gerçek Modbus yanıt zamanı olarak adlandırılmamalı.
8. **Raporlama:** PASS/FAIL/WARN sonuçları ve satır/sütun konumu ile açıklama. Kaynak veriyi değiştirmeden rapor üretmek.

## GRV-005-14 logundan önceden bilinen QC vakaları

- CSV başlığı, paylaşılan log metninde `...pzem_pf,pz` şeklinde kesilmiş görünüyor; bu durum log görüntüleme sınırı olabilir. Kaynak logun tam satırı mevcut değilse kesin neden ilan edilmemeli.
- CH0/CH1/CH2 satırlarında `window_start_millis` alanı başında boşlukla ` 264` biçiminde çıktı.
- BIAS satırı sütun hizası bakımından şüpheli; özellikle `adc_rms_raw`, `adc_rms_ac`, `bias_mean`, `bias_std` ve devamındaki PZEM alanlarının başlıkla eşleşmesi otomatik test edilmeli.
- ADC işlemi için 80 ms süre uyarısı var (ESPHome uyarı sınırı 50 ms). QC bunu ham log gözlemi olarak raporlayabilir; tek başına veri geçersizliği ilan etmemeli.

## PASS ölçütleri

- [ ] Beklenen CSV v03 şeması 42 alanla tanımlanmış ve test edilmiş.
- [ ] Başlık kesilmesi/iki parçalı başlık durumu açıkça tanınıyor; eksik kaynak verisi sessizce onarılmıyor.
- [ ] Dört kanal satırının her biri tam 42 alanla ayrıştırılıyor veya kusurlu satır FAIL olarak doğru konumla yakalanıyor.
- [ ] BIAS satırındaki bilinen hizalama sorunu otomatik testte yakalanıyor.
- [ ] Başında boşluk olan sayısal alanlar tespit ediliyor; özgün değer değiştirilmeden uyarı veriliyor.
- [ ] `measurement_id`, kanal kümesi, veri tipleri, boş alanlar ve zaman aritmetiği kontrolleri test edilmiş.
- [ ] Sabit test örnekleri: geçerli satır, kesik başlık, fazla/eksik sütun, BIAS hizalama hatası, `NOT_TRACKED`, boş alan ve hatalı time_delta.
- [ ] QC çıktısı özet ve makinece okunabilir rapor üretir; kaynak CSV/log dosyasını değiştirmez.
- [ ] Python sürümü ve çalıştırma komutu raporda belirtilir.

## Kapsam dışı

- Ham ADC örneklerinden yeniden özellik hesaplama.
- Kalibrasyon katsayısı üretme veya SCT doğruluğunu ilan etme.
- PZEM callback zamanını gerçek Modbus yanıt zamanına dönüştürme.
- `time_delta_ms` için keyfî kabul eşiği koyma.
- Kaynak log/CSV'yi otomatik düzeltip üzerine yazma.

## Sıradaki adım

Önce Python QC betiği ve küçük test fixture'ları hazırlanacak; kullanıcı tarafından çalıştırılıp sonuçları doğrulanmadan kodun PASS olduğu söylenmeyecek. GRV-005-14 YAML ve raporları değiştirilmeden korunacak.
